# pylint: disable=missing-docstring
import re

from esperanto_analyzer.speech import Conjunction
from esperanto_analyzer.analyzers.morphological import BaseMorphologicalAnalyzer

class ConjunctionMorphologicalAnalyzer(BaseMorphologicalAnalyzer):
    #  MATCHES: ["patro", "patroj", "patron", "patrojn"]
    MATCH_REGEXP = re.compile('^(.)$', re.IGNORECASE|re.UNICODE)

    @staticmethod
    def word_class():
        return Conjunction
