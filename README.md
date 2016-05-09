# Sentimental
*Sentiment analysis made easy; built on top off solid libraries.*

[![PyPI](https://img.shields.io/pypi/v/sentimental.svg)](https://pypi.python.org/pypi/sentimental)

Sentimental uses *Scikit-learn* to perform easy sentiment analysis. The idea is to create a simple out-of-box solution that yields acceptable results without complex configuration. Sentimental also uses a simple format for its training corpora that makes it easy to add more training data.

Take a look at `sentimental/data` for the included training corpora.

## Usage
Sentimental is released as a python package. For now install using:
```bash
pip install sentimental
```

### Examples
Training a model from example sentences:

```python
from sentimental import Sentimental

sentimental = Sentimental()
sentimental.train([Sentimental.get_datafolder() + '/sv/lexicon'])
sentimental.sentiment('Erik är jätteglad över det vackra vädret.')
```

Saving and loading a pre-trained model:

```python
sentimental.save('model.pickle')
sentimental2 = Sentimental.load('model.pickle')
```

## Data
A sentimental analyzer is only as good as its data. Sentimental comes with some data and pre-trained models. As a bonus the format is very simple and it is easy to train the model on your own data.

For details the readme in the [data](https://github.com/ErikGartner/sentimental/tree/master/sentimental/data) folder.

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
