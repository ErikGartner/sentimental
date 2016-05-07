# Data
This folder contains data and models that can be used by sentimental. The format is simple and external sources can easily be used.

## Folder structure
Inside this folder are several folders containing corpora that are grouped by language. The corpus folder should contain:

- `negative_examples.txt`
- `positive_examples.txt`
- `README.md`
- `LICENSE.txt`

The folder *may* also contain:

- `scripts/` - scripts for downloading/updating the data
- `corpus.txt` - the source document if applicable
- `model.pickle` - a pre-trained model

## Generating example sentences from a corpus
If your corpus doesn't have labeled example sentences they can be generated pretty easily if you have lexicons of negative and positive words/phrases.

1. Use a lexicon of positive and negative words (can be found in `<lang>/lexicon` for some languages).
2. Use `example_extractor.py` to extract sentences that contain these words. See example below.
3. Train sentimental on the extracted sentences.
4. Using the trained model you can now classify the rest of the sentences.

### Example

```python
e = ExampleExtractor()
e.load_labeled_words('data/sv/lexicon/positive_examples.txt', 'positive')
e.load_labeled_words('data/sv/lexicon/negative_examples.txt', 'negative')
e.extract_examples('data/sv/_newcorpus/corpus.txt', 'data/sv/_newcorpus')
```
