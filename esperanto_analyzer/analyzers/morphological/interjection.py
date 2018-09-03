# pylint: disable=missing-docstring
import re

from esperanto_analyzer.speech import Interjection
from esperanto_analyzer.analyzers.morphological import BaseMorphologicalAnalyzer

class InterjectionMorphologicalAnalyzer(BaseMorphologicalAnalyzer):
    INTERJECTIONS_LIST = ['Aĥ!', 'Aj!', 'Ba!', 'Baf!', 'Baj!', 'Be!', 'Bis!', 'Diable!', 'Ek!',
                          'Fi!', 'Fu!', 'Ĝis!', 'Ha!', 'Ha lo!', 'He!', 'Hej!', 'Ho!', 'Ho ve!',
                          'Hoj!', 'Hola!', 'Hu!', 'Hup!', 'Hura!', 'Lo!', 'Lu lu!', 'Nu!', 'Uf!',
                          'Up!', 'Ŭa!', 'Ve!', 'Volapukaĵo!', 'Jen'
                         ]

    # Shared regexp flags
    RE_FLAGS = re.IGNORECASE|re.UNICODE

    # REGEXP: `/Aĥ!|'Aj!|'Ba!|'Baf!|'Baj!(...)/`
    INTERJECTIONS_MATCH_REGEXP = re.compile('|'.join(INTERJECTIONS_LIST), RE_FLAGS)

    #  MATCHES only elements in `INTERJECTIONS_LIST`
    MATCH_REGEXP = re.compile('^(%s)$' % (INTERJECTIONS_MATCH_REGEXP.pattern), RE_FLAGS)

    @staticmethod
    def word_class():
        return Interjection
