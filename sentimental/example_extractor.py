import os
import re
from collections import Counter

import ahocorasick


class ExampleExtractor:
    def __init__(self):
        self.indicators = {'neutral': []}

    def load_labeled_words(self, word_file, label):
        word_set = self.indicators.get(label, set())
        with open(word_file, 'r') as f:
            word_set.update([x.lower().strip() for x in f.readlines()])
        self.indicators[label] = word_set

    def extract_examples(self, corpus_file, output_dir, cutoff=2):
        with open(corpus_file, 'r') as f:
            text = f.read()
        text = re.sub(r'\s+', ' ', text, flags=re.UNICODE)
        sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|!)\s',
                             text)

        labeled = {l: [] for l in self.indicators}

        automaton = ahocorasick.Automaton()
        for label in self.indicators:
            for indi in self.indicators[label]:
                automaton.add_word(indi, (label, indi))
        automaton.make_automaton()

        for sentence in sentences:
            sent = sentence.strip().lower()
            matches = [label
                       for (pos, (label, indi)) in automaton.iter(sent)
                       if self._validate_match(sent, pos, indi)]
            c = Counter(matches)

            common = c.most_common(2)
            if len(common) >= 2 and common[0][1] - common[1][1] >= cutoff:
                labeled[common[0][0]].append(sentence.strip())
            elif len(common) == 1 and common[0][1] >= cutoff:
                labeled[common[0][0]].append(sentence.strip())
            elif len(common) == 0 or common[0][1] < cutoff:
                labeled['neutral'].append(sentence.strip())

        for label in labeled:
            with open('%s/%s_examples.txt' % (output_dir, label), 'w') as f:
                f.write('\n'.join(labeled[label]))

    def _validate_match(self, sentence, pos, indi):
        end = pos + 2
        start = max(0, pos - len(indi))
        return re.search(r'\b%s\b' % indi,
                         sentence[start:end],
                         flags=re.UNICODE) is not None
