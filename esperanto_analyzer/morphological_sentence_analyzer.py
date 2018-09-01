"""

"""

# pylint: disable=too-few-public-methods,missing-docstring

from esperanto_analyzer.analyzers import MorphologicalAnalyzer

class MorphologicalSentenceAnalyzer:
    def __init__(self, sentence):
        self.sentence = sentence
        self.sentence_words = sentence.split()
        self.processed = False
        self.results = []

    def analyzes(self):
        # Avoid running the same thing many times returning the previous cached results
        if self.processed is True:
            return self.results

        # Cache the results
        self.results = self._process_words(self.sentence_words)
        self.processed = True

        return self.results

    def _process_words(self, words):
        results = []

        for word in words:
            processor = MorphologicalAnalyzer(word)
            results.append(processor.process())

        return results
