# pylint: disable=missing-docstring
import re

from esperanto_analyzer.speech import Adverb
from esperanto_analyzer.analyzers.morphological import BaseMorphologicalAnalyzer

class AdverbMorphologicalAnalyzer(BaseMorphologicalAnalyzer):
    #  MATCHES: ["multe", "flanke", "rapide"]
    BASE_MATCH_REGEXP = re.compile('([a-zA-Zĉĝĵĥŝŭ]{2,}(e))', re.IGNORECASE|re.UNICODE)

    # Some specials Esperanto adverbs and time related adverbs(now, yesterday, etc) list
    # @see https://www.wikiwand.com/en/Special_Esperanto_adverbs
    # @see: http://mylanguages.org/esperanto_adverbs.php
    SPECIAL_ADVERBS = [
        'almenaŭ',
        'ambaŭ',
        'antaŭ',
        'ankaŭ',
        'ankoraŭ',
        'apenaŭ',
        'baldaŭ',
        'ĉirkaŭ',
        'hieraŭ',
        'hodiaŭ',
        'kvazaŭ',
        'morgaŭ',
        'preskaŭ',
        'nun',
        'tiam',
        'ĉiam',
        'neniam',
        'tuj',
        'jam',
        'tie',
        'tien',
        'ĉie',
        'nenie',
        'for',
        'eksteren',
        'tre',
    ]

    # Create one regexp joining all the special adverbs
    SPECIAL_ADVERBS_MATCH_REGEXP = re.compile('|'.join(SPECIAL_ADVERBS), re.IGNORECASE|re.UNICODE)

    # Creates one string representation of the final `MATCH_REGEXP` joining two regexps
    FINAL_REGEXP = '^(%s|%s)$' % (BASE_MATCH_REGEXP.pattern, SPECIAL_ADVERBS_MATCH_REGEXP.pattern)

    # Finally create the FINAL regexp joining all the regexp need to match Adverbs
    MATCH_REGEXP = re.compile(FINAL_REGEXP, re.IGNORECASE|re.UNICODE)

    @staticmethod
    def word_class():
        return Adverb
