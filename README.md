# Sentimental
*Sentiment analysis made easy; built on top off solid libraries.*

[![PyPI](https://img.shields.io/pypi/v/sentimental.svg)](https://pypi.python.org/pypi/sentimental)

Sentimental uses *Scikit-learn* to perform easy sentiment analysis. The idea is to create a simple out-of-box solution that yields acceptable results without complex configuration. Sentimental also uses a simple format for its training corpora that makes it easy to add more training data.

Sentimental labels a sentence either: positive, neutral or negative together with the probability.

Take a look at [sentimental/data](./sentimental/data) for the included training corpora.

## Usage
Sentimental is released as a python package, just run:
```bash
pip install sentimental
```

### Examples
Below are some simple examples that covers most functions and use cases.

#### Extracting example sentences from a corpus
Using lists of negative and positive words Sentimental can extract files containing positive, neutral and negative sentences.
```python
from sentimental import ExampleExtractor, get_data_path

e = ExampleExtractor()
e.load_labeled_words(get_data_path() + '/sv/lexicon/positive_examples.txt', 'positive')
e.load_labeled_words(get_data_path() + '/sv/lexicon/negative_examples.txt', 'negative')
e.extract_examples(get_data_path() + '/sv/_newcorpus/corpus.txt', 'data/sv/_newcorpus')
```

#### Training a model from example sentences
Once you have a lists of positive, negative and neutral sentences you can train the Sentimental model on them to make prediction on other sentences.
```python
from sentimental import Sentimental

sentimental = Sentimental()
sentimental.train(['path/to/a/data_folder'])
sentimental.sentiment('Erik is very happy about the nice weather')
>>> {'negative': 0.012843021692660004, 'positive': 0.97922132069306, 'neutral': 0.0079356576142799052}
```

#### Saving and loading a pre-trained model:
Training a model and performing cross-validation can take some time on large datasets. To save time, one a model has been trained it can be saved and later loaded.

```python
sentimental.save('model.pickle')
sentimental2 = Sentimental.load('model.pickle')
```

#### Evaluating the predictor
There are two ways to evaluate Sentimental. The first is by looking at the cross-validation scores:

```python
sentimental.accuracy()
```

The second is to perform validation on an external test set:
```python
sentimental.validate('path/to/validation_files/positive.txt', 'positive')
sentimental.validate('path/to/validation_files/negative.txt', 'negative')
sentimental.validate('path/to/validation_files/neutral.txt', 'neutral')
```

## Data
A sentimental analyzer is only as good as its data. Sentimental comes with some data and pre-trained models. As a bonus the format is very simple and it is easy to train the model on your own data.

For details see the [readme](./sentimental/data/README.md) in the data folder.

If you have good data, either lexicons of polarity words or example sentences, feel free to make a pull request.

## Technical
Sentimental uses Logistic Regression on a ff-idf matrix of n-grams.

## Contributions
Please feel free to make pull requests, especially to add more training data.

## License
Copyright 2016 Erik Gärtner

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
