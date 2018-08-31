# pylint: disable=missing-docstring,no-self-use

import re
import pytest

from context import esperanto_analyzer

from esperanto_analyzer.speech import Adverb
from esperanto_analyzer.analyzers.morphological import AdverbMorphologicalAnalyzer

class TestAdverbMorphologicalAnalyzerBasic():
    TEST_WORD = 'bonege'

    def test_import(self):
        assert AdverbMorphologicalAnalyzer

    def test_initialize_default_options(self):
        analyzer = AdverbMorphologicalAnalyzer(self.TEST_WORD)

        assert analyzer.options == dict()

    def test_initialize_overwrite_options(self):
        analyzer = AdverbMorphologicalAnalyzer(self.TEST_WORD, dict(option='ok'))

        assert analyzer.options == dict(option='ok')

    def test_initialize_raw_word(self):
        analyzer = AdverbMorphologicalAnalyzer(self.TEST_WORD)

        assert analyzer.raw_word == self.TEST_WORD

    def test_initialize_word(self):
        analyzer = AdverbMorphologicalAnalyzer(self.TEST_WORD)

        # analyzer.word is only populated after calling `analyze()` method
        assert analyzer.word is None

    def test_initialize_matches(self):
        analyzer = AdverbMorphologicalAnalyzer(self.TEST_WORD)

        # analyzer.matches is only populated after calling `analyze()` method
        assert analyzer.matches is None

    def test_initialize_processed(self):
        analyzer = AdverbMorphologicalAnalyzer(self.TEST_WORD)

        # analyzer.matches is only populated after calling `analyze()` method
        assert analyzer.processed is False

    def test_match_regexp(self):
        assert AdverbMorphologicalAnalyzer.MATCH_REGEXP is not None

    def test_word_class(self):
        isinstance(AdverbMorphologicalAnalyzer.word_class(), Adverb)

class TestAdverbMorphologicalAnalyzerMatchMethod():
    VALID_WORDS = ['multe', 'bone', 'rapide', 'almenaŭ', 'ankoraŭ']

    def test_match(self):
        for word in self.VALID_WORDS:
            analyzer = AdverbMorphologicalAnalyzer(word)
            matches = analyzer.match()

            assert matches is not None
            assert len(matches.span()) == 2

    def test_match_empty(self):
        analyzer = AdverbMorphologicalAnalyzer('io')
        matches = analyzer.match()

        assert matches is None

class TestAdverbMorphologicalAnalyzerAnalyzeMethod():
    TEST_WORD = 'multe'
    INVALID_WORD = 'io'
    VALID_WORDS = ['multe', 'bone', 'rapide', 'almenaŭ', 'ankoraŭ']

    def test_invalid_analyze(self):
        analyzer = AdverbMorphologicalAnalyzer(self.INVALID_WORD)
        result = analyzer.analyze()

        assert not result

    def test_invalid_analyze_word(self):
        analyzer = AdverbMorphologicalAnalyzer(self.INVALID_WORD)
        analyzer.analyze()

        assert analyzer.word is None

    def test_invalid_analyze_match(self):
        analyzer = AdverbMorphologicalAnalyzer(self.INVALID_WORD)
        analyzer.analyze()

        assert analyzer.matches is None

    def test_analyze(self):
        for word in self.VALID_WORDS:
            analyzer = AdverbMorphologicalAnalyzer(word)

            assert analyzer.analyze()

    def test_analyze_word(self):
        for word in self.VALID_WORDS:
            analyzer = AdverbMorphologicalAnalyzer(word)
            analyzer.analyze()

            assert isinstance(analyzer.word, Adverb)
            assert analyzer.word.content == word

    def test_analyze_match(self):
        for word in self.VALID_WORDS:
            analyzer = AdverbMorphologicalAnalyzer(word)
            analyzer.analyze()

            assert analyzer.matches is not None

    def test_analyze_return_false(self):
        analyzer = AdverbMorphologicalAnalyzer(self.INVALID_WORD)

        assert analyzer.analyze() is False

    def test_analyze_return_true(self):
        for word in self.VALID_WORDS:
            analyzer = AdverbMorphologicalAnalyzer(word)

            assert analyzer.analyze()


    def test_analyze_processed(self):
        for word in self.VALID_WORDS:
            analyzer = AdverbMorphologicalAnalyzer(word)

            assert analyzer.processed is False

            analyzer.analyze()

            assert analyzer.processed is True

    def test_analyze_processed_response(self):
        for word in self.VALID_WORDS:
            analyzer = AdverbMorphologicalAnalyzer(word)
            analyzer.analyze()

            assert analyzer.analyze() is None
            assert analyzer.analyze() is None
