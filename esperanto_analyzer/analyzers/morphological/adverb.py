# pylint: disable=missing-docstring
import re

from esperanto_analyzer.speech import Adverb
from .base import BaseMorphologicalAnalyzer # TODO: change to module name

class AdverbMorphologicalAnalyzer(BaseMorphologicalAnalyzer):
    #  MATCHES: ["patro", "patroj", "patron", "patrojn"]
    MATCH_REGEXP = re.compile('(.{1,}(e((j?n?))?)$)', re.IGNORECASE|re.UNICODE)

    @staticmethod
    def word_class():
        return Adverb
