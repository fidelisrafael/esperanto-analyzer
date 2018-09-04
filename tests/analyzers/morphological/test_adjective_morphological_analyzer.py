# pylint: disable=missing-docstring,no-self-use

import re
import pytest

from context import esperanto_analyzer

from esperanto_analyzer.speech import Adjective
from esperanto_analyzer.analyzers.morphological import AdjectiveMorphologicalAnalyzer

class TestAdjectiveMorphologicalAnalyzerBasic():
    TEST_WORD = 'bela'

    def test_import(self):
        assert AdjectiveMorphologicalAnalyzer

    def test_initialize_default_options(self):
        analyzer = AdjectiveMorphologicalAnalyzer(self.TEST_WORD)

        assert analyzer.options == dict()

    def test_initialize_overwrite_options(self):
        analyzer = AdjectiveMorphologicalAnalyzer(self.TEST_WORD, dict(option='ok'))

        assert analyzer.options == dict(option='ok')

    def test_initialize_raw_word(self):
        analyzer = AdjectiveMorphologicalAnalyzer(self.TEST_WORD)

        assert analyzer.raw_word == self.TEST_WORD

    def test_initialize_word(self):
        analyzer = AdjectiveMorphologicalAnalyzer(self.TEST_WORD)

        # analyzer.word is only populated after calling `analyze()` method
        assert analyzer.word is None

    def test_initialize_matches(self):
        analyzer = AdjectiveMorphologicalAnalyzer(self.TEST_WORD)

        # analyzer.matches is only populated after calling `analyze()` method
        assert analyzer.matches is None

    def test_initialize_processed(self):
        analyzer = AdjectiveMorphologicalAnalyzer(self.TEST_WORD)

        # analyzer.matches is only populated after calling `analyze()` method
        assert analyzer.processed is False

    def test_match_regexp_value(self):
        assert AdjectiveMorphologicalAnalyzer.MATCH_REGEXP == re.compile('(^[a-zA-Zĉĝĵĥŝŭ]{2,}(a(j?n?)?)$)', re.IGNORECASE)

    def test_match_regexp(self):
        assert AdjectiveMorphologicalAnalyzer.MATCH_REGEXP is not None

    def test_word_class(self):
        assert isinstance(AdjectiveMorphologicalAnalyzer.word_class()(self.TEST_WORD), Adjective)

class TestAdjectiveMorphologicalAnalyzerMatchMethod():
    VALID_WORDS = ['bela', 'belan', 'belaj', 'belajn']
    INVALID_WORDS = ['domo', 'la', '?', '!']

    def test_match(self):
        for word in self.VALID_WORDS:
            analyzer = AdjectiveMorphologicalAnalyzer(word)
            matches = analyzer.match()

            assert matches is not None

    def test_match_empty(self):
        for word in self.INVALID_WORDS:
            analyzer = AdjectiveMorphologicalAnalyzer(word)
            matches = analyzer.match()

            assert matches is None

class TestAdjectiveMorphologicalAnalyzerAnalyzeMethod():
    INVALID_WORDS = [
        'io', 'multe', 'domo', 'hundoj', 'kiu', 'vi',
        '[', ']', '{', '}', '|', '\\', '(', ')', '=', '+', '*',
        '&', '^', '%', '$', '#', '@', '`', '~', ';', ':', ',', '.',
        '<', '>', '/',
        '.!', '!', 'n!', 'jn!', 'j!',
        '..!', '..!', '..n!', '..jn!',
        '..aj!', '..ajn!', '..aj', '..ajn', 'ajn',
        '.!', '?', 'n?', 'jn?', 'j?',
        '90a', '000an', '999ajn', '000aj', '__ajn', '__an', '__a',
        'bel0an', 'bel9ajn', '9belajn', '9bela',
    ]

    VALID_WORDS = [
        'ĝusta', 'bela', 'belan', 'belaj', 'belajn', 'bongusta'
    ]

    def test_invalid_analyze(self):
        for word in self.INVALID_WORDS:
            analyzer = AdjectiveMorphologicalAnalyzer(word)
            result = analyzer.analyze()

            assert not result

    def test_invalid_analyze_word(self):
        for word in self.INVALID_WORDS:
            analyzer = AdjectiveMorphologicalAnalyzer(word)
            analyzer.analyze()

            assert analyzer.word is None

    def test_invalid_analyze_match(self):
        for word in self.INVALID_WORDS:
            analyzer = AdjectiveMorphologicalAnalyzer(word)
            analyzer.analyze()

            assert analyzer.matches is None

    def test_analyze(self):
        for word in self.VALID_WORDS:
            analyzer = AdjectiveMorphologicalAnalyzer(word)

            assert analyzer.analyze()

    def test_analyze_word(self):
        for word in self.VALID_WORDS:
            analyzer = AdjectiveMorphologicalAnalyzer(word)
            analyzer.analyze()

            assert isinstance(analyzer.word, Adjective)
            assert analyzer.word.content == word

    def test_analyze_match(self):
        for word in self.VALID_WORDS:
            analyzer = AdjectiveMorphologicalAnalyzer(word)
            analyzer.analyze()

            assert analyzer.matches is not None

    def test_analyze_return_false(self):
        for word in self.INVALID_WORDS:
            analyzer = AdjectiveMorphologicalAnalyzer(word)

            assert analyzer.analyze() is False

    def test_analyze_return_true(self):
        for word in self.VALID_WORDS:
            analyzer = AdjectiveMorphologicalAnalyzer(word)

            assert analyzer.analyze()


    def test_analyze_processed(self):
        for word in self.VALID_WORDS:
            analyzer = AdjectiveMorphologicalAnalyzer(word)

            assert analyzer.processed is False

            analyzer.analyze()

            assert analyzer.processed is True

    def test_analyze_processed_response(self):
        for word in self.VALID_WORDS:
            analyzer = AdjectiveMorphologicalAnalyzer(word)
            analyzer.analyze()

            assert analyzer.analyze() is None
            assert analyzer.analyze() is None
