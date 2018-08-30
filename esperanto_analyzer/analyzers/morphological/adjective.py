# pylint: disable=missing-docstring
import re

from esperanto_analyzer.speech import Adjective
from .base import BaseMorphologicalAnalyzer # TODO: change to module name

class AdjectiveMorphologicalAnalyzer(BaseMorphologicalAnalyzer):
    #  MATCHES: ["patro", "patroj", "patron", "patrojn"]
    MATCH_REGEXP = re.compile('(.{1,}(a((j?n?))?)$)', re.IGNORECASE|re.UNICODE)

    @staticmethod
    def word_class():
        return Adjective
