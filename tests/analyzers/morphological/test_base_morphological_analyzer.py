# pylint: disable=missing-docstring,no-self-use

import re
import pytest

from context import esperanto_analyzer

from esperanto_analyzer.speech import Word
from esperanto_analyzer.analyzers.morphological import BaseMorphologicalAnalyzer

class TestBaseMorphologicalAnalyzerBasic():
    TEST_WORD = 'komputilo'

    def test_import(self):
        assert BaseMorphologicalAnalyzer

    def test_initialize_default_options(self):
        analyzer = BaseMorphologicalAnalyzer(self.TEST_WORD)

        assert analyzer.options == dict()

    def test_initialize_overwrite_options(self):
        analyzer = BaseMorphologicalAnalyzer(self.TEST_WORD, dict(option='ok'))

        assert analyzer.options == dict(option='ok')

    def test_initialize_raw_word(self):
        analyzer = BaseMorphologicalAnalyzer(self.TEST_WORD)

        assert analyzer.raw_word == self.TEST_WORD

    def test_initialize_word(self):
        analyzer = BaseMorphologicalAnalyzer(self.TEST_WORD)

        # analyzer.word is only populated after calling `analyze()` method
        assert analyzer.word is None

    def test_initialize_matches(self):
        analyzer = BaseMorphologicalAnalyzer(self.TEST_WORD)

        # analyzer.matches is only populated after calling `analyze()` method
        assert analyzer.matches is None

    def test_initialize_processed(self):
        analyzer = BaseMorphologicalAnalyzer(self.TEST_WORD)

        # analyzer.matches is only populated after calling `analyze()` method
        assert analyzer.processed is False

    def test_match_regexp(self):
        assert BaseMorphologicalAnalyzer.MATCH_REGEXP is None

    def test_word_class(self):
        with pytest.raises(NotImplementedError):
            BaseMorphologicalAnalyzer.word_class()

class TestBaseMorphologicalAnalyzerMatchMethod():
    TEST_WORD = 'komputilo'

    def test_match(self):
        analyzer = BaseMorphologicalAnalyzer(self.TEST_WORD)

        with pytest.raises(AttributeError, match="'NoneType' object has no attribute 'match'"):
            analyzer.match()

class TestAnalyzer(BaseMorphologicalAnalyzer):
    # Only words with MINIMUM 9 letters
    MATCH_REGEXP = re.compile('.{9,}')

    @staticmethod
    def word_class():
        return Word

class TestChildMorphologicalAnalyzerMatchMethod():
    TEST_WORD = 'komputilo'

    def test_match(self):
        analyzer = TestAnalyzer(self.TEST_WORD)
        matches = analyzer.match()

        assert matches is not None

    def test_match_empty(self):
        analyzer = TestAnalyzer('vorto')
        matches = analyzer.match()

        assert matches is None


class TestBaseMorphologicalAnalyzerAnalyzeMethod():
    TEST_WORD = 'komputilo'

    def test_analyze(self):
        analyzer = TestAnalyzer(self.TEST_WORD)
        result = analyzer.analyze()

        assert result
        assert isinstance(analyzer.word, Word)
        assert analyzer.matches is not None

    def test_analyze_word(self):
        analyzer = TestAnalyzer(self.TEST_WORD)
        result = analyzer.analyze()

        assert result
        assert isinstance(analyzer.word, Word)
        assert analyzer.raw_word == self.TEST_WORD
        assert analyzer.word.content == self.TEST_WORD
        assert analyzer.raw_word == analyzer.word.content

    def test_analyze_word_invalid(self):
        analyzer = TestAnalyzer('io')
        result = analyzer.analyze()

        assert result is False
        assert analyzer.word is None
        assert analyzer.raw_word == 'io'

    def test_analyze_matches(self):
        analyzer = TestAnalyzer(self.TEST_WORD)
        result = analyzer.analyze()

        assert result
        assert isinstance(analyzer.matches, re.Match)
        assert analyzer.matches

    def test_analyze_matches_span(self):
        analyzer = TestAnalyzer(self.TEST_WORD)
        result = analyzer.analyze()

        assert result
        assert len(analyzer.matches.span()) == 2
        assert analyzer.matches.span() == (0, 9)

    def test_analyze_matches_invalid(self):
        analyzer = TestAnalyzer('io')
        result = analyzer.analyze()

        assert result is False
        assert analyzer.matches is None

    def test_analyze_matches_span_invalid(self):
        analyzer = TestAnalyzer('io')
        result = analyzer.analyze()

        assert result is False
        assert analyzer.matches is None
        assert not analyzer.matches

    def test_analyze_return_true(self):
        analyzer = TestAnalyzer(self.TEST_WORD)

        assert analyzer.analyze()

    def test_analyze_return_false(self):
        analyzer = TestAnalyzer('io')

        assert analyzer.analyze() is False

    def test_analyze_processed(self):
        analyzer = TestAnalyzer(self.TEST_WORD)

        assert analyzer.processed is False

        analyzer.analyze()

        assert analyzer.processed is True

    def test_analyze_processed_response(self):
        analyzer = TestAnalyzer(self.TEST_WORD)
        analyzer.analyze()

        assert analyzer.analyze() is None
        assert analyzer.analyze() is None

