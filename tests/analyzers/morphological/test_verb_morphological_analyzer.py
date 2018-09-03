# pylint: disable=missing-docstring,no-self-use

import re
import pytest

from context import esperanto_analyzer

from esperanto_analyzer.speech import Verb
from esperanto_analyzer.analyzers.morphological import VerbMorphologicalAnalyzer

class TestVerbMorphologicalAnalyzerBasic():
    TEST_WORD = 'ŝatas'

    def test_import(self):
        assert VerbMorphologicalAnalyzer

    def test_initialize_default_options(self):
        analyzer = VerbMorphologicalAnalyzer(self.TEST_WORD)

        assert analyzer.options == dict()

    def test_initialize_overwrite_options(self):
        analyzer = VerbMorphologicalAnalyzer(self.TEST_WORD, dict(option='ok'))

        assert analyzer.options == dict(option='ok')

    def test_initialize_raw_word(self):
        analyzer = VerbMorphologicalAnalyzer(self.TEST_WORD)

        assert analyzer.raw_word == self.TEST_WORD

    def test_initialize_word(self):
        analyzer = VerbMorphologicalAnalyzer(self.TEST_WORD)

        # analyzer.word is only populated after calling `analyze()` method
        assert analyzer.word is None

    def test_initialize_matches(self):
        analyzer = VerbMorphologicalAnalyzer(self.TEST_WORD)

        # analyzer.matches is only populated after calling `analyze()` method
        assert analyzer.matches is None

    def test_initialize_processed(self):
        analyzer = VerbMorphologicalAnalyzer(self.TEST_WORD)

        # analyzer.matches is only populated after calling `analyze()` method
        assert analyzer.processed is False

    def test_match_regexp(self):
        assert VerbMorphologicalAnalyzer.MATCH_REGEXP is not None

    def test_word_class(self):
        assert isinstance(VerbMorphologicalAnalyzer.word_class()(self.TEST_WORD), Verb)

class TestVerbMorphologicalAnalyzerMatchMethod():
    VALID_WORDS = ['ŝatis', 'ŝatas', 'ŝatu', 'ŝatus', 'ŝati']
    INVALID_WORDS = ['multe', 'domo', 'hundoj', 'vi', 'bela', 'belajn', 'tio']

    def test_match(self):
        for word in self.VALID_WORDS:
            analyzer = VerbMorphologicalAnalyzer(word)
            matches = analyzer.match()

            assert matches is not None

    def test_match_empty(self):
        for word in self.INVALID_WORDS:
            analyzer = VerbMorphologicalAnalyzer(word)
            matches = analyzer.match()

            assert matches is None


class TestVerbMorphologicalAnalyzerAnalyzeMethod():
    INVALID_WORDS = ['multe', 'domo', 'hundoj', 'vi', 'bela', 'belajn', 'tio'] #, 'kiu']
    VALID_WORDS = ['ŝatis', 'ŝatas', 'ŝatu', 'ŝatus', 'ŝati', 'amas']

    def test_invalid_analyze(self):
        for word in self.INVALID_WORDS:
            analyzer = VerbMorphologicalAnalyzer(word)
            result = analyzer.analyze()

            assert not result

    def test_invalid_analyze_word(self):
        for word in self.INVALID_WORDS:
            analyzer = VerbMorphologicalAnalyzer(word)
            analyzer.analyze()

            # if(analyzer.word): breakpoint()

            assert analyzer.word is None

    def test_invalid_analyze_match(self):
        for word in self.INVALID_WORDS:
            analyzer = VerbMorphologicalAnalyzer(word)
            analyzer.analyze()

            assert analyzer.matches is None

    def test_analyze(self):
        for word in self.VALID_WORDS:
            analyzer = VerbMorphologicalAnalyzer(word)

            assert analyzer.analyze()

    def test_analyze_word(self):
        for word in self.VALID_WORDS:
            analyzer = VerbMorphologicalAnalyzer(word)
            analyzer.analyze()

            assert isinstance(analyzer.word, Verb)
            assert analyzer.word.content == word

    def test_analyze_match(self):
        for word in self.VALID_WORDS:
            analyzer = VerbMorphologicalAnalyzer(word)
            analyzer.analyze()

            assert analyzer.matches is not None

    def test_analyze_return_false(self):
        for word in self.INVALID_WORDS:
            analyzer = VerbMorphologicalAnalyzer(word)

            assert analyzer.analyze() is False

    def test_analyze_return_true(self):
        for word in self.VALID_WORDS:
            analyzer = VerbMorphologicalAnalyzer(word)

            assert analyzer.analyze()


    def test_analyze_processed(self):
        for word in self.VALID_WORDS:
            analyzer = VerbMorphologicalAnalyzer(word)

            assert analyzer.processed is False

            analyzer.analyze()

            assert analyzer.processed is True

    def test_analyze_processed_response(self):
        for word in self.VALID_WORDS:
            analyzer = VerbMorphologicalAnalyzer(word)
            analyzer.analyze()

            assert analyzer.analyze() is None
            assert analyzer.analyze() is None
