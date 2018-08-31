# pylint: disable=missing-docstring
import re

from esperanto_analyzer.speech import Adjective
from esperanto_analyzer.analyzers.morphological import BaseMorphologicalAnalyzer

class AdjectiveMorphologicalAnalyzer(BaseMorphologicalAnalyzer):
    #  MATCHES: ["bela", "belaj", "belan", "belajn"]
    MATCH_REGEXP = re.compile('(.{1,}(a((j?n?))?)$)', re.IGNORECASE|re.UNICODE)

    @staticmethod
    def word_class():
        return Adjective
