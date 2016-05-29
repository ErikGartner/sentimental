import os
import pickle
from collections import Counter

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn import cross_validation
from sklearn.metrics import accuracy_score


class Sentimental:
    def __init__(self,
                 min_ngrams=1,
                 max_ngrams=2,
                 min_df=0.0,
                 max_df=1.0,
                 max_features=None,
                 undersample=False):
        self.min_ngrams = min_ngrams
        self.max_ngrams = max_ngrams
        self.max_df = max_df
        self.min_df = min_df
        self.max_features = max_features
        self.undersample = undersample
        self.labels = ['negative', 'neutral', 'positive']

    def train(self, corpus_folders):
        self.vectorizer = TfidfVectorizer(
            analyzer='word',
            ngram_range=(self.min_ngrams, self.max_ngrams),
            max_df=self.max_df,
            min_df=self.min_df,
            max_features=self.max_features,
            decode_error='replace')

        x_input = []
        y_target = []
        for folder in corpus_folders:
            for i in range(len(self.labels)):
                label = self.labels[i]
                data_file = '%s/%s_examples.txt' % (folder, label)
                with open(data_file, 'r') as f:
                    read_data = f.readlines()
                    x_input.extend(read_data)
                    y_target.extend([i] * len(read_data))

        if self.undersample:
            (x_input, y_target) = Sentimental._undersample(x_input, y_target)

        x_train = self.vectorizer.fit_transform(x_input)

        self.predictor = LogisticRegression(solver='lbfgs',
                                            multi_class='multinomial',
                                            n_jobs=-1,
                                            class_weight='balanced')
        self.scores = cross_validation.cross_val_score(self.predictor,
                                                       x_train,
                                                       y_target,
                                                       cv=5)
        self.predictor.fit(x_train, y_target)

    def sentiment(self, text):
        x = self.vectorizer.transform([text])
        probabilities = self.predictor.predict_proba(x)[0]
        res = {}
        for i in range(len(self.labels)):
            res[self.labels[i]] = probabilities[i]
        return res

    def accuracy(self):
        return {'mean': self.scores.mean(), 'std': self.scores.std() * 2}

    def validate(self, validation_file, expected_label):
        with open(validation_file, 'r') as f:
            x_data = f.readlines()
        y_target = [self.labels.index(expected_label)] * len(x_data)
        x_validate = self.vectorizer.transform(x_data)
        y_result = self.predictor.predict(x_validate)
        return accuracy_score(y_target, y_result)

    def save(self, output_file):
        with open(output_file, 'wb') as f:
            pickle.dump(self, f)

    def load(pickel_file):
        with open(pickel_file, 'rb') as f:
            return pickle.load(f)

    def _undersample(x_data, y_data):
        sample_sizes = Counter(y_data)
        new_size = sample_sizes.most_common()[-1][1]
        found = {}
        for i in range(len(y_data)):
            found[y_data[i]] = found.get(y_data[i], 0) + 1
            if found[y_data[i]] > new_size:
                x_data[i] = None
                y_data[i] = None
        x_data = list(filter(lambda x: x is not None, x_data))
        y_data = list(filter(lambda x: x is not None, y_data))
        return (x_data, y_data)
