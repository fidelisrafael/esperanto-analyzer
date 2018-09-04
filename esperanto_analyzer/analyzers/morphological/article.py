# pylint: disable=missing-docstring
import re

from esperanto_analyzer.speech import Article
from esperanto_analyzer.analyzers.morphological import BaseMorphologicalAnalyzer

class ArticleMorphologicalAnalyzer(BaseMorphologicalAnalyzer):
    ARTICLES_LIST = ['la']

    ARTICLES_MATCH_REGEXP = re.compile('|'.join(ARTICLES_LIST), re.IGNORECASE|re.UNICODE)

    #  MATCHES: ["la"]
    MATCH_REGEXP = re.compile('^(%s)$' % (ARTICLES_MATCH_REGEXP.pattern), re.IGNORECASE|re.UNICODE)

    @staticmethod
    def word_class():
        return Article
