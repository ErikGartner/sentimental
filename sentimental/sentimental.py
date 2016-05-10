import os
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn import cross_validation


class Sentimental:
    def __init__(self,
                 max_ngrams=1,
                 min_df=0.0,
                 max_df=1.0,
                 max_features=None):
        self.n_grams = max_ngrams
        self.max_df = max_df
        self.min_df = min_df
        self.max_features = max_features
        self.labels = ['negative', 'neutral', 'positive']

    def train(self, corpus_folders):
        self.vectorizer = TfidfVectorizer(analyzer='word',
                                          ngram_range=(1, self.n_grams),
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

        x_train = self.vectorizer.fit_transform(x_input)

        self.predictor = LogisticRegression(solver='lbfgs',
                                            multi_class='multinomial',
                                            n_jobs=-1)
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

    def save(self, output_file):
        with open(output_file, 'wb') as f:
            pickle.dump(self, f)

    def load(pickel_file):
        with open(pickel_file, 'rb') as f:
            return pickle.load(f)

    def get_datafolder():
        return os.path.dirname(__file__) + '/data'
