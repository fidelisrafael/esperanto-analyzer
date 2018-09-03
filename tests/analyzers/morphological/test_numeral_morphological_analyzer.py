# pylint: disable=missing-docstring,no-self-use

import re
import pytest

from context import esperanto_analyzer

from esperanto_analyzer.speech import Numeral
from esperanto_analyzer.analyzers.morphological import NumeralMorphologicalAnalyzer

class TestNumeralMorphologicalAnalyzerBasic():
    TEST_WORD = 'dek'

    def test_import(self):
        assert NumeralMorphologicalAnalyzer

    def test_initialize_default_options(self):
        analyzer = NumeralMorphologicalAnalyzer(self.TEST_WORD)

        assert analyzer.options == dict()

    def test_initialize_overwrite_options(self):
        analyzer = NumeralMorphologicalAnalyzer(self.TEST_WORD, dict(option='ok'))

        assert analyzer.options == dict(option='ok')

    def test_initialize_raw_word(self):
        analyzer = NumeralMorphologicalAnalyzer(self.TEST_WORD)

        assert analyzer.raw_word == self.TEST_WORD

    def test_initialize_word(self):
        analyzer = NumeralMorphologicalAnalyzer(self.TEST_WORD)

        # analyzer.word is only populated after calling `analyze()` method
        assert analyzer.word is None

    def test_initialize_matches(self):
        analyzer = NumeralMorphologicalAnalyzer(self.TEST_WORD)

        # analyzer.matches is only populated after calling `analyze()` method
        assert analyzer.matches is None

    def test_initialize_processed(self):
        analyzer = NumeralMorphologicalAnalyzer(self.TEST_WORD)

        # analyzer.matches is only populated after calling `analyze()` method
        assert analyzer.processed is False

    def test_match_regexp(self):
        assert NumeralMorphologicalAnalyzer.MATCH_REGEXP is not None

    def test_regexp_value(self):
        assert NumeralMorphologicalAnalyzer.MATCH_REGEXP == re.compile('^(-?\\d+|nul|unu|du|tri|kvar|kvin|ses|sep|ok|naŭ|dek|(unu|du|tri|kvar|kvin|ses|sep|ok|naŭ|dek)?(dek|cent|milionoj|miliono|miliardoj|miliardo|bilionoj|biliono|mil))$', re.IGNORECASE)

    def test_word_class(self):
        isinstance(NumeralMorphologicalAnalyzer.word_class()(self.TEST_WORD), Numeral)

class TestNumeralMorphologicalAnalyzerMatchMethod():
    VALID_WORDS = [
        'unu', 'du', 'tri', 'kvar', 'kvin', 'ses', 'sep', 'ok', 'naŭ', 'dek',
        'dudek', 'tridek', 'kvardek', 'kvindek', 'sesdek', 'sepdek', 'okdek', 'naŭdek',
        'cent', 'ducent', 'tricent', 'kvarcent', 'kvincent', 'sescent', 'sepcent', 'okcent', 'naŭcent',
        'mil', 'dumil', 'miliardo', 'miliono', 'miliardoj', 'milionoj'
    ]

    VALID_DIGITS = ['10', '20', '-1', '0', '102041', '9992232213']

    INVALID_DIGITS = ['a10', '2a0', '-1x', '01#', '102041@', '!9992232213']

    INVALID_WORDS = ['io', 'lo', 'bela', 'la', 'kiu', 'vi', 'kun', 'multe', 'ankoraŭ', '?', '!']

    def test_match(self):
        for word in self.VALID_WORDS:
            analyzer = NumeralMorphologicalAnalyzer(word)
            matches = analyzer.match()

            assert matches is not None
            assert len(matches.span()) == 2

    def test_match_digits(self):
        for word in self.VALID_DIGITS:
            analyzer = NumeralMorphologicalAnalyzer(word)
            matches = analyzer.match()

            assert matches is not None
            assert len(matches.span()) == 2

    def test_match_invalid_digits(self):
        for word in self.INVALID_DIGITS:
            analyzer = NumeralMorphologicalAnalyzer(word)
            matches = analyzer.match()

            assert matches is None

    def test_match_empty(self):
        for word in self.INVALID_WORDS:
            analyzer = NumeralMorphologicalAnalyzer(word)
            matches = analyzer.match()

            assert matches is None

class TestNumeralMorphologicalAnalyzerAnalyzeMethod():
    VALID_WORDS = [
        'unu', 'du', 'tri', 'kvar', 'kvin', 'ses', 'sep', 'ok', 'naŭ', 'dek',
        'dudek', 'tridek', 'kvardek', 'kvindek', 'sesdek', 'sepdek', 'okdek', 'naŭdek',
        'cent', 'ducent', 'tricent', 'kvarcent', 'kvincent', 'sescent', 'sepcent', 'okcent', 'naŭcent',
        'mil', 'dumil', 'miliardo', 'miliono', 'miliardoj', 'milionoj',
        '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
        '11', '20', '-1', '0', '102041', '9992232213'
    ]

    INVALID_WORDS = ['io', 'lo', 'bela', 'la', 'kiu', 'vi', 'kun', 'multe', 'ankoraŭ',
                     'a10', '2a0', '-1x', '01#', '102041@', '!9992232213'
                    ]

    def test_invalid_analyze(self):
        for word in self.INVALID_WORDS:
            analyzer = NumeralMorphologicalAnalyzer(word)
            result = analyzer.analyze()

            assert not result

    def test_invalid_analyze_word(self):
        for word in self.INVALID_WORDS:
            analyzer = NumeralMorphologicalAnalyzer(word)
            analyzer.analyze()

            assert analyzer.word is None

    def test_invalid_analyze_match(self):
        for word in self.INVALID_WORDS:
            analyzer = NumeralMorphologicalAnalyzer(word)
            analyzer.analyze()

            assert analyzer.matches is None

    def test_analyze(self):
        for word in self.VALID_WORDS:
            analyzer = NumeralMorphologicalAnalyzer(word)

            assert analyzer.analyze()

    def test_analyze_word(self):
        for word in self.VALID_WORDS:
            analyzer = NumeralMorphologicalAnalyzer(word)
            analyzer.analyze()

            assert isinstance(analyzer.word, Numeral)
            assert analyzer.word.content == word

    def test_analyze_match(self):
        for word in self.VALID_WORDS:
            analyzer = NumeralMorphologicalAnalyzer(word)
            analyzer.analyze()

            assert analyzer.matches is not None

    def test_analyze_return_false(self):
        for word in self.INVALID_WORDS:
            analyzer = NumeralMorphologicalAnalyzer(word)

            assert analyzer.analyze() is False

    def test_analyze_return_true(self):
        for word in self.VALID_WORDS:
            analyzer = NumeralMorphologicalAnalyzer(word)

            assert analyzer.analyze()


    def test_analyze_processed(self):
        for word in self.VALID_WORDS:
            analyzer = NumeralMorphologicalAnalyzer(word)

            assert analyzer.processed is False

            analyzer.analyze()

            assert analyzer.processed is True

    def test_analyze_processed_response(self):
        for word in self.VALID_WORDS:
            analyzer = NumeralMorphologicalAnalyzer(word)
            analyzer.analyze()

            assert analyzer.analyze() is None
            assert analyzer.analyze() is None

class TestNumeralMorphologicalAnalyzerBasicNumbersList:
    def test_numbers_not_empty(self):
        assert NumeralMorphologicalAnalyzer.BASIC_NUMBERS_LIST is not None

    def test_basic_numbers_included(self):
        for number in ['nul', 'unu', 'du', 'tri', 'kvar', 'kvin', 'ses', 'sep', 'ok', 'naŭ', 'dek']:
            assert number in NumeralMorphologicalAnalyzer.BASIC_NUMBERS_LIST

    def test_numbers_not_size(self):
        assert len(NumeralMorphologicalAnalyzer.BASIC_NUMBERS_LIST) == 11

    def test_numbers_match_list(self):
        for word in NumeralMorphologicalAnalyzer.BASIC_NUMBERS_LIST:
            assert NumeralMorphologicalAnalyzer.BASIC_NUMBERS_REGEXP.match(word)

    def test_numbers_match_final_regexp_list(self):
        for word in NumeralMorphologicalAnalyzer.BASIC_NUMBERS_LIST:
            assert NumeralMorphologicalAnalyzer.MATCH_REGEXP.match(word)

    def test_others_numbers_regexp(self):
        for word in ['dudek', 'tridek', 'ducent', 'dumil', 'trimil', 'mil', 'miliono', 'milionoj', 'cent', 'dek', 'miliardo']:
            assert NumeralMorphologicalAnalyzer.OTHERS_NUMBERS_REGEXP.match(word)

    def test_numbers_digit_regexp(self):
        for word in ['1', '20', '300', '999999', '-10']:
            assert NumeralMorphologicalAnalyzer.NUMBERS_DIGIT_REGEXP.match(word)

    def test_invalid_others_numbers_regexp(self):
        for word in ['domo', 'la', 'multe', 'bela', 'belajn', 'a0x']:
            assert NumeralMorphologicalAnalyzer.OTHERS_NUMBERS_REGEXP.match(word) is None

    def test_invalid_numbers_digit_regexp(self):
        for word in ['@', '!10', '*10*']:
            assert NumeralMorphologicalAnalyzer.NUMBERS_DIGIT_REGEXP.match(word) is None
