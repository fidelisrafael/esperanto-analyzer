# pylint: disable=missing-docstring
import re

from esperanto_analyzer.speech import Verb
from esperanto_analyzer.analyzers.morphological import AdverbMorphologicalAnalyzer
from esperanto_analyzer.analyzers.morphological import ConjunctionMorphologicalAnalyzer
from esperanto_analyzer.analyzers.morphological import NumeralMorphologicalAnalyzer
from esperanto_analyzer.analyzers.morphological import PrepositionMorphologicalAnalyzer
from esperanto_analyzer.analyzers.morphological import PronounMorphologicalAnalyzer

from esperanto_analyzer.analyzers.morphological import BaseMorphologicalAnalyzer

class VerbMorphologicalAnalyzer(BaseMorphologicalAnalyzer):

    # https://en.wiktionary.org/wiki/Appendix:Esperanto_verbs
    # Note: Not completed
    VERBS_ENDINGS = [
        'i',     # Infinitive
        'u',     # Volative/Jussive
        'as',    # Present indicative
        'os',    # Future indicative
        'is',    # Past indicative
        'us',    # Conditional
        'ite',   # Past passive adverbial
        'ate',   # Present passive adverbial
        'ote',   # Future passive adverbial
        'inte',  # Past active adverbial
        'ante',  # Present active adverbial
        'onte',  # Future active adverbial
    ]

    # Tenses that receives acusative (n) and plural (j) suffix
    VERBS_ENDINGS_ACUSATIVE_PLURAL = [
        'inta',  # Past active participle,
        'anta',  # Present active participle
        'onta',  # Future active participle
        'into',  # Past active nominal
        'anto',  # Present active nominal
        'onto',  # Future active nominal
        'ita',   # Past passive participle
        'ata',   # Present passive participle
        'ota',   # Future passive participle
        'ito',   # Past passive nominal
        'ato',   # Past passive nominal
        'oto',   # Future passive nominal
    ]

    RE_FLAGS = re.IGNORECASE|re.UNICODE

    VERBS_ENDINGS_REGEXP = re.compile('|'.join(VERBS_ENDINGS), RE_FLAGS)

    VERBS_ENDINGS_ACUSATIVE_PLURAL_REGEXP = re.compile('|'.join(VERBS_ENDINGS_ACUSATIVE_PLURAL), RE_FLAGS)

    #  MATCHES: ["ŝatis", "ŝatas", "ŝatu", "ŝatus", "ŝati"] and so on
    MATCH_REGEXP = re.compile('^([a-zA-Zĉĝĵĥŝŭ]{2,}(%s|(%s)(j?n?)?))$' % (VERBS_ENDINGS_REGEXP.pattern, VERBS_ENDINGS_ACUSATIVE_PLURAL_REGEXP.pattern), RE_FLAGS)

    @staticmethod
    def word_class():
        return Verb
