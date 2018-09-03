# pylint: disable=missing-docstring
import re

from esperanto_analyzer.speech import Conjunction
from esperanto_analyzer.analyzers.morphological import BaseMorphologicalAnalyzer

class ConjunctionMorphologicalAnalyzer(BaseMorphologicalAnalyzer):
    CONJUNCTIONS_LIST = [
        'antaŭ kiam',
        'antaŭ ol'
        'au',
        'aŭ',
        'ĉar',
        'ĉu',
        'K',
        'k',
        'kaj',
        'kaŭ',
        'ke',
        'kial',
        'kiam',
        'kie',
        'kiel',
        'kune kun',
        'kvankam',
        'kvazau',
        'kvazaŭ',
        'minus',
        'nek',
        'ol',
        'plus',
        'se',
        'sed',
        'tial'
    ]

    RE_FLAGS = re.IGNORECASE|re.UNICODE

    CONJUCTIONS_MATCH_REGEXP = re.compile('|'.join(CONJUNCTIONS_LIST), RE_FLAGS)

    #  MATCHES only elements in `CONJUNCTIONS_LIST`
    MATCH_REGEXP = re.compile('^(%s)$' % (CONJUCTIONS_MATCH_REGEXP.pattern), RE_FLAGS)

    @staticmethod
    def word_class():
        return Conjunction
