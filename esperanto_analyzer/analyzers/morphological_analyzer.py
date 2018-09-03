"""
This class receives one word as input and process it through all Morphological Analyzers
"""

# pylint: disable=too-few-public-methods,missing-docstring

from esperanto_analyzer.analyzers.morphological import AdjectiveMorphologicalAnalyzer
from esperanto_analyzer.analyzers.morphological import AdverbMorphologicalAnalyzer
from esperanto_analyzer.analyzers.morphological import ArticleMorphologicalAnalyzer
from esperanto_analyzer.analyzers.morphological import ConjunctionMorphologicalAnalyzer
from esperanto_analyzer.analyzers.morphological import InterjectionMorphologicalAnalyzer
from esperanto_analyzer.analyzers.morphological import NounMorphologicalAnalyzer
from esperanto_analyzer.analyzers.morphological import NumeralMorphologicalAnalyzer
from esperanto_analyzer.analyzers.morphological import PrepositionMorphologicalAnalyzer
from esperanto_analyzer.analyzers.morphological import PronounMorphologicalAnalyzer
from esperanto_analyzer.analyzers.morphological import VerbMorphologicalAnalyzer

from esperanto_analyzer.analyzers.morphological import AnalyzeResult


class MorphologicalAnalyzer:
    # TODO: Reorganize this order for better perfomance
    DEFAULT_ANALYZERS = [
        AdverbMorphologicalAnalyzer,
        ArticleMorphologicalAnalyzer,
        ConjunctionMorphologicalAnalyzer,
        InterjectionMorphologicalAnalyzer,
        NumeralMorphologicalAnalyzer,
        PrepositionMorphologicalAnalyzer,
        PronounMorphologicalAnalyzer,
        AdjectiveMorphologicalAnalyzer,
        NounMorphologicalAnalyzer,
        VerbMorphologicalAnalyzer,
    ]

    def __init__(self, raw_word):
        self.raw_word = raw_word
        self.processed = False
        self.results = None

    def analyze(self):
        if self.processed:
            return None

        analyzer = self.__apply_analyzers(self.raw_word, self.DEFAULT_ANALYZERS)

        self.results = self.__finish_result(result=analyzer, raw_word=self.raw_word)
        self.processed = True

        return True

    def __finish_result(self, result, raw_word):
        return AnalyzeResult(result=result, raw_word=raw_word)

    def __apply_analyzers(self, word, analyzers=None):
        if analyzers is None or len(analyzers) is 0:
            return None

        for analyzer in analyzers:
            analyzer_instance = analyzer(word)

            if analyzer_instance.analyze() is True:
                return analyzer_instance
