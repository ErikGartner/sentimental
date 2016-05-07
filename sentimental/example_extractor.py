import os
import re
from collections import Counter

import ahocorasick


class ExampleExtractor:
    def __init__(self):
        self.indicators = {}

    def load_labeled_words(self, word_file, label):
        word_set = self.indicators.get(label, set())
        with open(word_file, 'r') as f:
            word_set.update([x.lower().strip() for x in f.readlines()])
        self.indicators[label] = word_set

    def extract_examples(self, corpus_file, output_dir, cutoff=2):
        with open(corpus_file, 'r') as f:
            text = f.read()
        text = re.sub(r'\s', ' ', text)
        sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s',
                             text)

        labeled = {l: [] for l in self.indicators}

        automaton = ahocorasick.Automaton()
        for label in self.indicators:
            for indi in self.indicators[label]:
                automaton.add_word(indi, label)
        automaton.make_automaton()

        for sentence in sentences:
            sentence = sentence.strip()
            c = Counter([label for (pos, label) in automaton.iter(sentence)])

            common = c.most_common(2)
            if len(common) >= 2 and common[0][1] - common[1][1] >= cutoff:
                labeled[common[0][0]].append(sentence)
            elif len(common) == 1 and common[0][1] >= cutoff:
                labeled[common[0][0]].append(sentence)

        for label in labeled:
            with open('%s/%s_examples.txt' % (output_dir, label), 'w') as f:
                f.write('\n'.join(labeled[label]))
