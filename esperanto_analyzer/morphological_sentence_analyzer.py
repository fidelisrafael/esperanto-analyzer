"""

"""

# pylint: disable=too-few-public-methods,missing-docstring

from esperanto_analyzer.analyzers import MorphologicalAnalyzer

class MorphologicalSentenceAnalyzer:
    def __init__(self, sentence):
        self.sentence = sentence
        self.sentence_words = sentence.split()
        self.processed = False
        self.results = None

    def analyze(self):
        # Avoid running the same thing many times returning the previous cached results
        if self.processed is True:
            return None

        # Cache the results
        self.results = self._process_words(self.sentence_words)
        self.processed = True

        return True

    def analyzes_results(self):
        if not self.processed:
            return None

        return [result.results for result in self.results]

    def _process_words(self, words):
        results = []

        for word in words:
            analyzer = MorphologicalAnalyzer(word)
            analyzer.analyze()

            results.append(analyzer)

        return results
