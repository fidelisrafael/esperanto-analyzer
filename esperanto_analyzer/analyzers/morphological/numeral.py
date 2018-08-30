# pylint: disable=missing-docstring
import re

from esperanto_analyzer.speech import Numeral
from .base import BaseMorphologicalAnalyzer # TODO: change to module name

class NumeralMorphologicalAnalyzer(BaseMorphologicalAnalyzer):
    #  MATCHES: ["patro", "patroj", "patron", "patrojn"]
    MATCH_REGEXP = re.compile('^(.)$', re.IGNORECASE|re.UNICODE)

    def word_class(self):
        return Numeral
