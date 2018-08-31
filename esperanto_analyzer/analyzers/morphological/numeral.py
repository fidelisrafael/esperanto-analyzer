# pylint: disable=missing-docstring
import re

from esperanto_analyzer.speech import Numeral
from esperanto_analyzer.analyzers.morphological import BaseMorphologicalAnalyzer

class NumeralMorphologicalAnalyzer(BaseMorphologicalAnalyzer):
    # These are the basics numbers names in Esperanto
    BASIC_NUMBERS_LIST = [
        'nul',    # 0
        'unu',    # 1
        'du',     # 2
        'tri',    # 3
        'kvar',   # 4
        'kvin',   # 5
        'ses',    # 6
        'sep',    # 7
        'ok',     # 8
        'naŭ',    # 9
        'dek'     # 10
    ]

    # Shared regexp flags
    RE_FLAGS = re.IGNORECASE|re.UNICODE

    # TODO: Should this be dynamic?
    # Basically: `re.compile('(nul|unu|du|tri|kvar|kvin|ses|sep|ok|naŭ|dek)')`
    BASIC_NUMBERS_REGEXP = re.compile('|'.join(BASIC_NUMBERS_LIST), RE_FLAGS)

    # TODO: This still matches "unudek", solve it!
    # MATCHES: ["tridek", "okdek", "kvin", "sepcent", "tri miliono"]
    OTHERS_NUMBERS_REGEXP = re.compile('(unu|du|tri|kvar|kvin|ses|sep|ok|naŭ|dek)?(dek|cent|milionoj|miliono|miliardoj|miliardo|bilionoj|biliono|mil)', RE_FLAGS)

    # MATCHES: ["1", "100", "-123", "9009809809", "-90123283232"]
    NUMBERS_DIGIT_REGEXP = re.compile('-?\d+', re.UNICODE)

    # Join regexps to create the final pattern utilized for this analyzer
    FINAL_REGEXP = '^(%s|%s|%s)$' % (NUMBERS_DIGIT_REGEXP.pattern, BASIC_NUMBERS_REGEXP.pattern, OTHERS_NUMBERS_REGEXP.pattern)

    # The final regexp utilized internally in `match()`
    MATCH_REGEXP = re.compile(FINAL_REGEXP, RE_FLAGS)

    @staticmethod
    def word_class():
        return Numeral
