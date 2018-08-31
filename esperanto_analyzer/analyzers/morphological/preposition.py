# pylint: disable=missing-docstring
import re

from esperanto_analyzer.speech import Preposition
from esperanto_analyzer.analyzers.morphological import BaseMorphologicalAnalyzer

class PrepositionMorphologicalAnalyzer(BaseMorphologicalAnalyzer):
    PREPOSITIONS_LIST = ['K', 'al', 'anstataŭ', 'antaŭ', 'antaŭ ol', 'apud', 'da', 'de', 'disde',
                         'du vortoj', 'dum', 'ekde', 'ekster', 'eksteren', 'el', 'en', 'ene',
                         'estiel', 'far', 'fare de', 'flanke de', 'for de', 'graŭ', 'inter', 'je',
                         'kaj ankaŭ', 'kiel', 'kontraŭ', 'kontraŭe de', 'krom', 'kun', 'laŭ',
                         'mala', 'malantaŭ', 'malgraŭ', 'malkiel', 'malsupre de', 'malsupren',
                         'meze de', 'na', 'nome de', 'ol', 'per', 'pere de', 'plus', 'po', 'por',
                         'post', 'preter', 'pri', 'pro', 'proksime de', 'samkiel', 'sed', 'sekva',
                         'sen', 'sub', 'suben', 'super', 'supren', 'sur', 'tiu', 'tiuj', 'tra',
                         'trans', 'tri vortoj', 'tuj post', 'tutĉirkaŭ',
                         'ĉe', 'ĉi tiu', 'ĉi tiuj', 'ĉirkaŭ', 'ĝis']

    PROPOSITIONS_MATCH_REGEXP = re.compile('|'.join(PREPOSITIONS_LIST), re.IGNORECASE|re.UNICODE)

    #  MATCHES only elements in `PREPOSITIONS_LIST`
    MATCH_REGEXP = re.compile('^(%s)$' % (PROPOSITIONS_MATCH_REGEXP.pattern), re.IGNORECASE|re.UNICODE)

    @staticmethod
    def word_class():
        return Preposition
