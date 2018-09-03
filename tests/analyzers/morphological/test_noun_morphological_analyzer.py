# pylint: disable=missing-docstring,no-self-use

import re
import pytest

from context import esperanto_analyzer

from esperanto_analyzer.speech import Noun
from esperanto_analyzer.analyzers.morphological import NounMorphologicalAnalyzer

class TestNounMorphologicalAnalyzerBasic():
    TEST_WORD = 'kaj'

    def test_import(self):
        assert NounMorphologicalAnalyzer

    def test_initialize_default_options(self):
        analyzer = NounMorphologicalAnalyzer(self.TEST_WORD)

        assert analyzer.options == dict()

    def test_initialize_overwrite_options(self):
        analyzer = NounMorphologicalAnalyzer(self.TEST_WORD, dict(option='ok'))

        assert analyzer.options == dict(option='ok')

    def test_initialize_raw_word(self):
        analyzer = NounMorphologicalAnalyzer(self.TEST_WORD)

        assert analyzer.raw_word == self.TEST_WORD

    def test_initialize_word(self):
        analyzer = NounMorphologicalAnalyzer(self.TEST_WORD)

        # analyzer.word is only populated after calling `analyze()` method
        assert analyzer.word is None

    def test_initialize_matches(self):
        analyzer = NounMorphologicalAnalyzer(self.TEST_WORD)

        # analyzer.matches is only populated after calling `analyze()` method
        assert analyzer.matches is None

    def test_initialize_processed(self):
        analyzer = NounMorphologicalAnalyzer(self.TEST_WORD)

        # analyzer.matches is only populated after calling `analyze()` method
        assert analyzer.processed is False

    def test_match_regexp(self):
        assert NounMorphologicalAnalyzer.MATCH_REGEXP is not None

    def test_word_class(self):
        assert isinstance(NounMorphologicalAnalyzer.word_class()(self.TEST_WORD), Noun)

    def test_regexp_value(self):
        assert NounMorphologicalAnalyzer.MATCH_REGEXP == re.compile('(^[a-zA-Z]{2,}(o(j?n?)?)$)', re.IGNORECASE|re.UNICODE)

class TestNounMorphologicalAnalyzerMatchMethod():
    VALID_WORDS = [
        'domo', 'domoj', 'homon', 'homojn'
    ]

    INVALID_WORDS = ['io', 'lo', 'bela', 'la', 'kiu', 'vi', 'kun', 'multe', 'ankoraŭ']

    def test_match(self):
        for word in self.VALID_WORDS:
            analyzer = NounMorphologicalAnalyzer(word)
            matches = analyzer.match()

            assert matches is not None
            assert len(matches.span()) == 2

    def test_match_empty(self):
        for word in self.INVALID_WORDS:
            analyzer = NounMorphologicalAnalyzer(word)
            matches = analyzer.match()

            assert matches is None

class TestNounMorphologicalAnalyzerAnalyzeMethod():
    VALID_WORDS = [
        'domo', 'domoj', 'homon', 'homojn',
    ]

    INVALID_WORDS = ['io', 'lo', 'bela', 'la', 'kiu', 'vi', 'kun', 'multe', 'ankoraŭ']

    def test_invalid_analyze(self):
        for word in self.INVALID_WORDS:
            analyzer = NounMorphologicalAnalyzer(word)
            result = analyzer.analyze()

            assert not result

    def test_invalid_analyze_word(self):
        for word in self.INVALID_WORDS:
            analyzer = NounMorphologicalAnalyzer(word)
            analyzer.analyze()

            assert analyzer.word is None

    def test_invalid_analyze_match(self):
        for word in self.INVALID_WORDS:
            analyzer = NounMorphologicalAnalyzer(word)
            analyzer.analyze()

            assert analyzer.matches is None

    def test_analyze(self):
        for word in self.VALID_WORDS:
            analyzer = NounMorphologicalAnalyzer(word)

            assert analyzer.analyze()

    def test_analyze_word(self):
        for word in self.VALID_WORDS:
            analyzer = NounMorphologicalAnalyzer(word)
            analyzer.analyze()

            assert isinstance(analyzer.word, Noun)
            assert analyzer.word.content == word

    def test_analyze_match(self):
        for word in self.VALID_WORDS:
            analyzer = NounMorphologicalAnalyzer(word)
            analyzer.analyze()

            assert analyzer.matches is not None

    def test_analyze_return_false(self):
        for word in self.INVALID_WORDS:
            analyzer = NounMorphologicalAnalyzer(word)

            assert analyzer.analyze() is False

    def test_analyze_return_true(self):
        for word in self.VALID_WORDS:
            analyzer = NounMorphologicalAnalyzer(word)

            assert analyzer.analyze()


    def test_analyze_processed(self):
        for word in self.VALID_WORDS:
            analyzer = NounMorphologicalAnalyzer(word)

            assert analyzer.processed is False

            analyzer.analyze()

            assert analyzer.processed is True

    def test_analyze_processed_response(self):
        for word in self.VALID_WORDS:
            analyzer = NounMorphologicalAnalyzer(word)
            analyzer.analyze()

            assert analyzer.analyze() is None
            assert analyzer.analyze() is None
