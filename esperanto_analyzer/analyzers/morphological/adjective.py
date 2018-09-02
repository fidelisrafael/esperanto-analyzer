# pylint: disable=missing-docstring
import re

from esperanto_analyzer.speech import Adjective
from esperanto_analyzer.analyzers.morphological import BaseMorphologicalAnalyzer

class AdjectiveMorphologicalAnalyzer(BaseMorphologicalAnalyzer):
    # MATCHES: ["bela", "belaj", "belan", "belajn", "belajn!", "belajn?", 'bela??']
    # DONT MATCHES: ["la"] => Article
    MATCH_REGEXP = re.compile('(^[a-zA-Z]{2,}(a((j?n?)?)([?!]+)?)$)', re.IGNORECASE|re.UNICODE)

    @staticmethod
    def word_class():
        return Adjective
