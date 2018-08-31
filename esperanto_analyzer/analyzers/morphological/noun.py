# pylint: disable=missing-docstring
import re

from esperanto_analyzer.speech import Noun
from esperanto_analyzer.analyzers.morphological import BaseMorphologicalAnalyzer

class NounMorphologicalAnalyzer(BaseMorphologicalAnalyzer):
    #  MATCHES: ["patro", "patroj", "patron", "patrojn"]
    MATCH_REGEXP = re.compile('(.{1,}(o((j?n?))?)$)', re.IGNORECASE|re.UNICODE)

    @staticmethod
    def word_class():
        return Noun
