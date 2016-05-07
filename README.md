# Sentimental
*Sentiment analysis made easy; built on top off solid libraries.*

Sentimental uses *Scikit-learn* to perform easy sentiment analysis. The idea is to create a simple out-of-box solution that yields acceptable results without complex configuration. Sentimental also uses a simple format for its training corpora that makes it easy to add more training data.

Take a look at `sentimental/data` for the included training corpora.

## Usage
Sentimental is released as a python package. For now install using:
```bash
pip install git+https://github.com/ErikGartner/sentimental.git
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
A sentimental analyzer is only as good as its data. Sentimental comes with some pre-trained models and data but the format is very simple and it is easy to use your own data.

For details the readme in the ``data`` folder.

If you have good data, either lexicons of polarity words or example sentences, feel free to make a pull request.

## Technical
Sentimental uses Logistic Regression on a ff-idf matrix of n-grams.

## Contributions
Please feel free to make pull requests, especially to add more training data.

## License
Copyright Erik Gärtner 2016
