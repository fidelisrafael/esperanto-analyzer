# pylint: disable=missing-docstring
import re

from esperanto_analyzer.speech import Pronoun
from esperanto_analyzer.analyzers.morphological import BaseMorphologicalAnalyzer

class PronounMorphologicalAnalyzer(BaseMorphologicalAnalyzer):

    # These are the personal pronouns and also the base for possessive pronouns
    # Ex:
    #   Personal = "mi" Possesive = "mia"
    #   Personal = "ili" Possesive = "ilia"
    PERSONAL_PRONOUNS_LIST = [
        'mi',
        'vi',
        'li',
        'ŝi',
        'ĝi',
        'ni',
        'oni',
        'ili'
    ]

    # Interrogative Pronouns
    # Relative Pronouns
    # https://esperanto.lingolia.com/en/grammar/pronouns/indefinite-pronouns
    OTHERS_PRONOUNS_LIST = [
        'kiu',
        'kio',
        'kies',
        'tiu',
        'ĉi tiu',
        'tia',
    ]

    # https://esperanto.lingolia.com/en/grammar/pronouns/indefinite-pronouns
    INDEFINITE_PRONOUNS_LIST = [
        'nenio',
        'neniu',
        'ĉio',
        'ĉiu',
        'io',
        'iu',
        'io ajn',
        'iu ajn',
        'io ajn',
        'ĉio ajn',
        'iu ajn',
        'ĉiu ajn'
    ]

    # Shared flags
    RE_FLAGS = re.IGNORECASE|re.UNICODE

    # /mi|vi|li|ŝi|gi|(...)/
    PERSONAL_PRONOUNS_LIST_REGEXP = re.compile('|'.join(PERSONAL_PRONOUNS_LIST), RE_FLAGS)

    # /kiu|kio|kies|tiu|ĉi tiu|tia/
    OTHERS_PRONOUNS_LIST_REGEXP = re.compile('|'.join(OTHERS_PRONOUNS_LIST), RE_FLAGS)

    # /nenio|neniu|ĉio|ĉiu|io|iu|io ajn|iu ajn|io ajn|ĉio ajn|iu ajn|ĉiu ajn/
    INDEFINITE_PRONOUNS_LIST_REGEXP = re.compile('|'.join(INDEFINITE_PRONOUNS_LIST), RE_FLAGS)

    # ["mia", "via", "lia", (...)]
    PERSONAL_POSSESSIVE_PRONOUNS_LIST = [pronoun + "a" for pronoun in PERSONAL_PRONOUNS_LIST]

    # /mia|via|lia|ŝia|gia|(...)/
    PERSONAL_POSSESSIVE_PRONOUNS_LIST_REGEXP = re.compile('|'.join(PERSONAL_POSSESSIVE_PRONOUNS_LIST), RE_FLAGS)

    # /mi|vi|li|ŝi|gi|(...)|mia|via|lia|ŝia|gia|(...)/
    ALL_PERSONAL_PRONOUNS_REGEXP = re.compile("(%s|%s|%s|%s)" % (PERSONAL_POSSESSIVE_PRONOUNS_LIST_REGEXP.pattern, PERSONAL_PRONOUNS_LIST_REGEXP.pattern, OTHERS_PRONOUNS_LIST_REGEXP.pattern, INDEFINITE_PRONOUNS_LIST_REGEXP.pattern))

    #  MATCHES: ["mi", "via", "viajn", "viaj", "liajn"]
    MATCH_REGEXP = re.compile('(^(%s((j?n?)?))$)' % ALL_PERSONAL_PRONOUNS_REGEXP.pattern, RE_FLAGS)

    # breakpoint()

    @staticmethod
    def word_class():
        return Pronoun
