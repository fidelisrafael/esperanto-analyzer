"""

"""

# pylint: disable=too-few-public-methods,missing-docstring

from esperanto_analyzer.analyzers import MorphologicalAnalyzer

class MorphologicalSentenceAnalyzer:
    def __init__(self, sentence):
        self.sentence = sentence
        self.sentence_words = self._split_sentence(sentence)
        self.processed = False
        self.internal_results = None

    def analyze(self):
        # Avoid running the same thing many times returning the previous cached results
        if self.processed is True:
            return None

        # Cache the results
        self.internal_results = self._process_words(self.sentence_words)
        self.processed = True

        return True

    def analyzes_results(self):
        if not self.processed:
            return None

        return [result.results for result in self.internal_results]

    def results(self):
        if not self.processed:
            return None

        results = []

        for analyze in self.analyzes_results():
            results.append([analyze.raw_word, analyze])

        return results

    def _split_sentence(self, sentence):
        return sentence.split()

    def _process_words(self, words):
        results = []

        for word in words:
            analyzer = MorphologicalAnalyzer(word)
            analyzer.analyze()

            results.append(analyzer)

        return results
