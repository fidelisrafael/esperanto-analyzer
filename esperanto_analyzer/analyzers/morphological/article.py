# pylint: disable=missing-docstring
import re

from esperanto_analyzer.speech import Article
from .base import BaseMorphologicalAnalyzer # TODO: change to module name

class ArticleMorphologicalAnalyzer(BaseMorphologicalAnalyzer):
    #  MATCHES: ["patro", "patroj", "patron", "patrojn"]
    MATCH_REGEXP = re.compile('^(la)$', re.IGNORECASE|re.UNICODE)

    @staticmethod
    def word_class():
        return Article
