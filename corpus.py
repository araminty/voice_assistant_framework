from preprocessor import Preprocessor
from collections.abc import Iterable

class Corpus:
    """Corpus is the storage of a set of utterances.  \
        The vocabularies are gathered at this level.  \
        An intent selects a subset of data from the corpus.
        
        A corpus could be a child of a corpus, containing 
        some but not all of the utterances."""
    
    
    default_removed =  "[^a-zA-Z0-9 -]"

    def __init__(self, utterances):
        self.utterances=utterances
        try:
            if type(utterances) != str and isinstance(utterance, Iterable):
                    self.utterances=' '.join(utterances)
        except:
            pass
        if type(self.utterances)!=str:
            raise TypeError("Corpus needs to receive string or iterable of strings input")

    def _all_utterances(self):
        """merge all the utterances from all the intents"""

    def punctuation_remover(self, words, removed=default_removed):
        return re.sub(removed, '', words)

    def tokenizer(self, words):
        return self.vectorizer.transform(words)
    
    def number_remover(self, words):
        words = re.sub("[0-9]", " # ", words)
        
    def __call__(self, words):
        words = self.punctuation_remover(words)
        words = self.number_remover(words)
        words = self.tokenizer(words)
        return words