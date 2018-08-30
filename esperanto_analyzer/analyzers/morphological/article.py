# pylint: disable=missing-docstring
import re

from esperanto_analyzer.speech import Article
from .base import BaseMorphologicalAnalyzer # TODO: change to module name

class ArticleMorphologicalAnalyzer(BaseMorphologicalAnalyzer):
    #  MATCHES: ["patro", "patroj", "patron", "patrojn"]
    MATCH_REGEXP = re.compile('^(la)$', re.IGNORECASE|re.UNICODE)

    def match(self, word):
        return self.MATCH_REGEXP.match(word)

    def word_class(self, word):
        return Article(word)
