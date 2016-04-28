# Sentimental
*Sentiment analysis made easy; built on top off solid libraries.*

Sentimental uses *Scikit-learn* to perform easy sentiment analysis. The idea is to create a simple out-of-box solution that yields acceptable results without complex configuration. Sentimental also uses a simple format for its training corpora that makes it easy to add more training data.

Take a look at `sentimental/data` for the included training corpora.

## Usage
```python
from sentimental.sentimental import Sentimental

sentimental = Sentimental()
sentimental.train([Sentimental.get_datafolder() + '/sv/lexicon'])
sentimental.sentiment('Erik är jätteglad över det vackra vädret.')
```

## Installation
Sentimental is released as a python package. For now install using:
```
pip install git+https://github.com/ErikGartner/sentimental.git
```

## Contributions
Please feel free to make pull request, especially to add more training data.

## License
Copyright Erik Gärtner 2016
