from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC

class SentimentModel:

    LABELS = ['negative', 'positive', 'neutral']

    def __init__(self):
        self.n_grams = 2
        self.max_df = 1
        self.max_features = None

    def train(self, corpus_folders):
        self.vectorizer = TfidfVectorizer(strip_accents='unicode',
        analyzer='word', ngram_range=(1, self.n_grams), max_df=self.max_df, min_df=0, max_features=self.max_features)

        x_input = []
        y_target = []
        for folder in corpus_folders:
            for i in range(len(SentimentModel.LABELS)):
                label = SentimentModel.LABELS[i]
                data_file = '%s/%s_examples.txt' % (folder, label)
                with open(data_file, 'r') as f:
                    read_data = f.readlines()
                    x_input.extend(read_data)
                    y_target.extend([i] * len(read_data))

        x_train = self.vectorizer.fit_transform(x_input)

        self.predictor = SVC()
        self.predictor.fit(x_train, y_target)

    def sentiment(self, text):
        x = self.vectorizer.transform([text])
        return SentimentModel.LABELS[self.predictor.predict(x)[0]]

    def save(self, output_file):
        pass

    def load(self, corpus_folder=None, pickel_file=None):
        pass
