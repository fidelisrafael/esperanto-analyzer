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


class MorphologicalProcessor:
    DEFAULT_ANALYZERS = [
        AdjectiveMorphologicalAnalyzer,
        AdverbMorphologicalAnalyzer,
        ArticleMorphologicalAnalyzer,
        ConjunctionMorphologicalAnalyzer,
        InterjectionMorphologicalAnalyzer,
        NounMorphologicalAnalyzer,
        NumeralMorphologicalAnalyzer,
        PrepositionMorphologicalAnalyzer,
        PronounMorphologicalAnalyzer,
        VerbMorphologicalAnalyzer
    ]

    def __init__(self, word):
        self.word = word

    def process(self):
        analyzer = self.__apply_analyzers(self.word, self.DEFAULT_ANALYZERS)

        return self.__finish_result(analyzer)

    def __finish_result(self, result):
        return AnalyzeResult(result)

    def __apply_analyzers(self, word, analyzers=None):
        if analyzers is None or len(analyzers) is 0:
            return None

        for analyzer in analyzers:
            # TODO: Should we create one instance for each analysis or the analyzers
            ## could be changed to be Modules(class static methods) or Singleton
            analyzer_instance = analyzer()

            if analyzer_instance.analyze(word) is True:
                return analyzer_instance
