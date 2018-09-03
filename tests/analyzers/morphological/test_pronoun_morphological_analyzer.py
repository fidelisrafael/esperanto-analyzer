# pylint: disable=missing-docstring,no-self-use

import re
import pytest

from context import esperanto_analyzer

from esperanto_analyzer.speech import Pronoun
from esperanto_analyzer.analyzers.morphological import PronounMorphologicalAnalyzer

class TestPronounMorphologicalAnalyzerBasic():
    TEST_WORD = 'mi'

    def test_import(self):
        assert PronounMorphologicalAnalyzer

    def test_initialize_default_options(self):
        analyzer = PronounMorphologicalAnalyzer(self.TEST_WORD)

        assert analyzer.options == dict()

    def test_initialize_overwrite_options(self):
        analyzer = PronounMorphologicalAnalyzer(self.TEST_WORD, dict(option='ok'))

        assert analyzer.options == dict(option='ok')

    def test_initialize_raw_word(self):
        analyzer = PronounMorphologicalAnalyzer(self.TEST_WORD)

        assert analyzer.raw_word == self.TEST_WORD

    def test_initialize_word(self):
        analyzer = PronounMorphologicalAnalyzer(self.TEST_WORD)

        # analyzer.word is only populated after calling `analyze()` method
        assert analyzer.word is None

    def test_initialize_matches(self):
        analyzer = PronounMorphologicalAnalyzer(self.TEST_WORD)

        # analyzer.matches is only populated after calling `analyze()` method
        assert analyzer.matches is None

    def test_initialize_processed(self):
        analyzer = PronounMorphologicalAnalyzer(self.TEST_WORD)

        # analyzer.matches is only populated after calling `analyze()` method
        assert analyzer.processed is False

    def test_match_regexp(self):
        assert PronounMorphologicalAnalyzer.MATCH_REGEXP is not None

    def test_word_class(self):
        isinstance(PronounMorphologicalAnalyzer.word_class()(self.TEST_WORD), Pronoun)

class TestPronounMorphologicalAnalyzerMatchMethod():
    VALID_WORDS = [
        'mi', 'vi', 'li', 'ŝi', 'ĝi', 'oni', 'ili', 'ni',
        'min', 'vin', 'lin', 'ŝin', 'ĝin', 'onin', 'ilin', 'nin',
        'mia', 'via', 'lia', 'ŝia', 'ĝia', 'onia', 'ilia', 'nia',
        'miaj', 'viaj', 'liaj', 'ŝiaj', 'ĝiaj', 'oniaj', 'iliaj', 'niaj',
        'mian', 'vian', 'lian', 'ŝian', 'ĝian', 'onian', 'ilian', 'nian',
        'miajn', 'viajn', 'liajn', 'ŝiajn', 'ĝiajn', 'oniajn', 'iliajn', 'niajn',
        'kiu', 'kio', 'kies', 'tiu', 'ĉi tiu', 'tia',
        'nenio', 'neniu', 'ĉio', 'ĉiu', 'io', 'iu', 'io ajn', 'iu ajn',
        'nenion', 'neniun', 'ĉion', 'ĉiun', 'ion', 'iun', 'io ajn', 'iu ajn',
        'io ajn', 'ĉio ajn', 'iu ajn', 'ĉiu ajn'
    ]

    INVALID_WORDS = ['lo', 'bela', 'la', 'kun', 'multe', 'ankoraŭ',
                     'a10', '2a0', '-1x', '01#', '102041@', '!9992232213', 'ilianj',
                     'ilimia', 'miaan', 'miani', 'vianj'
                    ]

    def test_match(self):
        for word in self.VALID_WORDS:
            analyzer = PronounMorphologicalAnalyzer(word)
            matches = analyzer.match()

            assert matches is not None
            assert len(matches.span()) == 2

    def test_match_empty(self):
        for word in self.INVALID_WORDS:
            analyzer = PronounMorphologicalAnalyzer(word)
            matches = analyzer.match()
            assert matches is None

class TestPronounMorphologicalAnalyzerAnalyzeMethod():
    VALID_WORDS = [
        'mi', 'vi', 'li', 'ŝi', 'ĝi', 'oni', 'ili', 'ni',
        'min', 'vin', 'lin', 'ŝin', 'ĝin', 'onin', 'ilin', 'nin',
        'mia', 'via', 'lia', 'ŝia', 'ĝia', 'onia', 'ilia', 'nia',
        'miaj', 'viaj', 'liaj', 'ŝiaj', 'ĝiaj', 'oniaj', 'iliaj', 'niaj',
        'mian', 'vian', 'lian', 'ŝian', 'ĝian', 'onian', 'ilian', 'nian',
        'miajn', 'viajn', 'liajn', 'ŝiajn', 'ĝiajn', 'oniajn', 'iliajn', 'niajn',
        'kiu', 'kio', 'kies', 'tiu', 'ĉi tiu', 'tia',
        'nenio', 'neniu', 'ĉio', 'ĉiu', 'io', 'iu', 'io ajn', 'iu ajn',
        'nenion', 'neniun', 'ĉion', 'ĉiun', 'ion', 'iun', 'io ajn', 'iu ajn',
        'io ajn', 'ĉio ajn', 'iu ajn', 'ĉiu ajn'
    ]

    INVALID_WORDS = ['lo', 'bela', 'la', 'kun', 'multe', 'ankoraŭ',
                     'a10', '2a0', '-1x', '01#', '102041@', '!9992232213', 'ilianj',
                     'ilimia', 'miaan', 'miani', 'vianj'
                    ]

    def test_invalid_analyze(self):
        for word in self.INVALID_WORDS:
            analyzer = PronounMorphologicalAnalyzer(word)
            result = analyzer.analyze()

            assert not result

    def test_invalid_analyze_word(self):
        for word in self.INVALID_WORDS:
            analyzer = PronounMorphologicalAnalyzer(word)
            analyzer.analyze()

            assert analyzer.word is None

    def test_invalid_analyze_match(self):
        for word in self.INVALID_WORDS:
            analyzer = PronounMorphologicalAnalyzer(word)
            analyzer.analyze()

            assert analyzer.matches is None

    def test_analyze(self):
        for word in self.VALID_WORDS:
            analyzer = PronounMorphologicalAnalyzer(word)

            assert analyzer.analyze()

    def test_analyze_word(self):
        for word in self.VALID_WORDS:
            analyzer = PronounMorphologicalAnalyzer(word)
            analyzer.analyze()

            assert isinstance(analyzer.word, Pronoun)
            assert analyzer.word.content == word

    def test_analyze_match(self):
        for word in self.VALID_WORDS:
            analyzer = PronounMorphologicalAnalyzer(word)
            analyzer.analyze()

            assert analyzer.matches is not None

    def test_analyze_return_false(self):
        for word in self.INVALID_WORDS:
            analyzer = PronounMorphologicalAnalyzer(word)

            assert analyzer.analyze() is False

    def test_analyze_return_true(self):
        for word in self.VALID_WORDS:
            analyzer = PronounMorphologicalAnalyzer(word)

            assert analyzer.analyze()


    def test_analyze_processed(self):
        for word in self.VALID_WORDS:
            analyzer = PronounMorphologicalAnalyzer(word)

            assert analyzer.processed is False

            analyzer.analyze()

            assert analyzer.processed is True

    def test_analyze_processed_response(self):
        for word in self.VALID_WORDS:
            analyzer = PronounMorphologicalAnalyzer(word)
            analyzer.analyze()

            assert analyzer.analyze() is None
            assert analyzer.analyze() is None

class TestPronounMorphologicalAnalyzerPersonalPronounsList:
    BASIC_PERSONAL_PRONOUNS = ['mi', 'vi','li', 'ŝi', 'ĝi', 'oni', 'ili']

    def test_pronouns_not_empty(self):
        assert PronounMorphologicalAnalyzer.PERSONAL_PRONOUNS_LIST is not None

    def test_basic_pronouns_included(self):
        for number in self.BASIC_PERSONAL_PRONOUNS:
            assert number in PronounMorphologicalAnalyzer.PERSONAL_PRONOUNS_LIST

    def test_pronouns_not_size(self):
        assert len(PronounMorphologicalAnalyzer.PERSONAL_PRONOUNS_LIST) == 8

    def test_pronouns_list_match_regexp(self):
        for word in PronounMorphologicalAnalyzer.PERSONAL_PRONOUNS_LIST:
            assert PronounMorphologicalAnalyzer.PERSONAL_PRONOUNS_LIST_REGEXP.match(word)

    def test_pronouns_match_hardcoded_list(self):
        for word in self.BASIC_PERSONAL_PRONOUNS:
            assert PronounMorphologicalAnalyzer.PERSONAL_PRONOUNS_LIST_REGEXP.match(word)

    def test_pronouns_match_final_regexp_list(self):
        for word in PronounMorphologicalAnalyzer.PERSONAL_PRONOUNS_LIST:
            assert PronounMorphologicalAnalyzer.MATCH_REGEXP.match(word)

    def test_pronouns_acusative_match_final_regexp(self):
        for word in self.BASIC_PERSONAL_PRONOUNS:
            assert PronounMorphologicalAnalyzer.MATCH_REGEXP.match(word)

    def test_pronouns_acusative_match_final_regexp_list(self):
        for word in self.BASIC_PERSONAL_PRONOUNS:
            assert PronounMorphologicalAnalyzer.MATCH_REGEXP.match(word + 'n')

class TestPronounMorphologicalAnalyzerPossessivePronounsList:
    BASIC_POSSESSIVE_PRONOUNS = [
        'mia', 'via', 'lia', 'ŝia', 'ĝia', 'onia', 'nia', 'ilia'
    ]

    def test_pronouns_not_empty(self):
        assert PronounMorphologicalAnalyzer.PERSONAL_POSSESSIVE_PRONOUNS_LIST is not None

    def test_basic_pronouns_included(self):
        for number in self.BASIC_POSSESSIVE_PRONOUNS:
            assert number in PronounMorphologicalAnalyzer.PERSONAL_POSSESSIVE_PRONOUNS_LIST

    def test_pronouns_not_size(self):
        assert len(PronounMorphologicalAnalyzer.PERSONAL_POSSESSIVE_PRONOUNS_LIST) == 8

    def test_pronouns_list_match_regexp(self):
        for word in PronounMorphologicalAnalyzer.PERSONAL_POSSESSIVE_PRONOUNS_LIST:
            assert PronounMorphologicalAnalyzer.PERSONAL_POSSESSIVE_PRONOUNS_LIST_REGEXP.match(word)

    def test_pronouns_match_hardcoded_list(self):
        for word in self.BASIC_POSSESSIVE_PRONOUNS:
            assert PronounMorphologicalAnalyzer.PERSONAL_POSSESSIVE_PRONOUNS_LIST_REGEXP.match(word)

    def test_pronouns_match_final_regexp_list(self):
        for word in PronounMorphologicalAnalyzer.PERSONAL_POSSESSIVE_PRONOUNS_LIST:
            assert PronounMorphologicalAnalyzer.MATCH_REGEXP.match(word)

    def test_pronouns_plural_match_final_regexp_list(self):
        for word in self.BASIC_POSSESSIVE_PRONOUNS:
            assert PronounMorphologicalAnalyzer.MATCH_REGEXP.match(word + 'j')

    def test_pronouns_plural_acusative_match_final_regexp_list(self):
        for word in self.BASIC_POSSESSIVE_PRONOUNS:
            assert PronounMorphologicalAnalyzer.MATCH_REGEXP.match(word + 'jn')

    def test_pronouns_acusative_match_final_regexp_list(self):
        for word in self.BASIC_POSSESSIVE_PRONOUNS:
            assert PronounMorphologicalAnalyzer.MATCH_REGEXP.match(word + 'n')


class TestPronounMorphologicalAnalyzerAllBasicPersonalPronounsList:
    ALL_BASIC_PRONOUNS = [
        'mi', 'vi', 'li', 'ŝi', 'ĝi', 'oni', 'ni', 'ili',
        'mia', 'via', 'lia', 'ŝia', 'ĝia', 'onia', 'nia', 'ilia',
        'miaj', 'viaj', 'liaj', 'ŝiaj', 'ĝiaj', 'oniaj', 'niaj', 'iliaj'
    ]

    def test_pronouns_not_empty(self):
        assert PronounMorphologicalAnalyzer.ALL_PERSONAL_PRONOUNS_REGEXP is not None

    def test_pronouns_list_match_regexp(self):
        for word in PronounMorphologicalAnalyzer.PERSONAL_POSSESSIVE_PRONOUNS_LIST:
            assert PronounMorphologicalAnalyzer.ALL_PERSONAL_PRONOUNS_REGEXP.match(word)

    def test_pronouns_match_hardcoded_list(self):
        for word in self.ALL_BASIC_PRONOUNS:
            assert PronounMorphologicalAnalyzer.ALL_PERSONAL_PRONOUNS_REGEXP.match(word)

    def test_pronouns_match_final_regexp_list(self):
        for word in self.ALL_BASIC_PRONOUNS:
            assert PronounMorphologicalAnalyzer.MATCH_REGEXP.match(word)

    def test_pronouns_acusative_match_final_regexp_list(self):
        for word in self.ALL_BASIC_PRONOUNS:
            assert PronounMorphologicalAnalyzer.MATCH_REGEXP.match(word + 'n')

