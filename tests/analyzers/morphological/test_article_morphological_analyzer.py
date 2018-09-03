# pylint: disable=missing-docstring,no-self-use

import re
import pytest

from context import esperanto_analyzer

from esperanto_analyzer.speech import Article
from esperanto_analyzer.analyzers.morphological import ArticleMorphologicalAnalyzer

class TestArticleMorphologicalAnalyzerBasic():
    TEST_WORD = 'la'

    def test_import(self):
        assert ArticleMorphologicalAnalyzer

    def test_initialize_default_options(self):
        analyzer = ArticleMorphologicalAnalyzer(self.TEST_WORD)

        assert analyzer.options == dict()

    def test_initialize_overwrite_options(self):
        analyzer = ArticleMorphologicalAnalyzer(self.TEST_WORD, dict(option='ok'))

        assert analyzer.options == dict(option='ok')

    def test_initialize_raw_word(self):
        analyzer = ArticleMorphologicalAnalyzer(self.TEST_WORD)

        assert analyzer.raw_word == self.TEST_WORD

    def test_initialize_word(self):
        analyzer = ArticleMorphologicalAnalyzer(self.TEST_WORD)

        # analyzer.word is only populated after calling `analyze()` method
        assert analyzer.word is None

    def test_initialize_matches(self):
        analyzer = ArticleMorphologicalAnalyzer(self.TEST_WORD)

        # analyzer.matches is only populated after calling `analyze()` method
        assert analyzer.matches is None

    def test_initialize_processed(self):
        analyzer = ArticleMorphologicalAnalyzer(self.TEST_WORD)

        # analyzer.matches is only populated after calling `analyze()` method
        assert analyzer.processed is False

    def test_match_regexp(self):
        assert ArticleMorphologicalAnalyzer.MATCH_REGEXP is not None

    def test_word_class(self):
        assert isinstance(ArticleMorphologicalAnalyzer.word_class()(self.TEST_WORD), Article)

class TestArticleMorphologicalAnalyzerMatchMethod():
    VALID_WORDS = ['la']
    INVALID_WORDS = ['io', 'lo', 'bela', 'domo', 'hundoj', 'kiu', 'vi', 'kun', 'multe', 'ankoraŭ', '?', '!']

    def test_match(self):
        for word in self.VALID_WORDS:
            analyzer = ArticleMorphologicalAnalyzer(word)
            matches = analyzer.match()

            assert matches is not None
            assert len(matches.span()) == 2

    def test_match_empty(self):
        for word in self.INVALID_WORDS:
            analyzer = ArticleMorphologicalAnalyzer(word)
            matches = analyzer.match()

            assert matches is None

class TestArticleMorphologicalAnalyzerAnalyzeMethod():
    VALID_WORDS = ['la']
    INVALID_WORDS = ['io', 'lo', 'bela', 'domo', 'hundoj', 'kiu', 'vi', 'kun', 'multe', 'ankoraŭ', '?', '!']

    def test_invalid_analyze(self):
        for word in self.INVALID_WORDS:
            analyzer = ArticleMorphologicalAnalyzer(word)
            result = analyzer.analyze()

            assert not result

    def test_invalid_analyze_word(self):
        for word in self.INVALID_WORDS:
            analyzer = ArticleMorphologicalAnalyzer(word)
            analyzer.analyze()

            assert analyzer.word is None

    def test_invalid_analyze_match(self):
        for word in self.INVALID_WORDS:
            analyzer = ArticleMorphologicalAnalyzer(word)
            analyzer.analyze()

            assert analyzer.matches is None

    def test_analyze(self):
        for word in self.VALID_WORDS:
            analyzer = ArticleMorphologicalAnalyzer(word)

            assert analyzer.analyze()

    def test_conjunctions_list(self):
        for word in ArticleMorphologicalAnalyzer.ARTICLES_LIST:
            analyzer = ArticleMorphologicalAnalyzer(word)

            assert analyzer.analyze()

    def test_analyze_word(self):
        for word in self.VALID_WORDS:
            analyzer = ArticleMorphologicalAnalyzer(word)
            analyzer.analyze()

            assert isinstance(analyzer.word, Article)
            assert analyzer.word.content == word

    def test_analyze_match(self):
        for word in self.VALID_WORDS:
            analyzer = ArticleMorphologicalAnalyzer(word)
            analyzer.analyze()

            assert analyzer.matches is not None

    def test_analyze_return_false(self):
        for word in self.INVALID_WORDS:
            analyzer = ArticleMorphologicalAnalyzer(word)

            assert analyzer.analyze() is False

    def test_analyze_return_true(self):
        for word in self.VALID_WORDS:
            analyzer = ArticleMorphologicalAnalyzer(word)

            assert analyzer.analyze()


    def test_analyze_processed(self):
        for word in self.VALID_WORDS:
            analyzer = ArticleMorphologicalAnalyzer(word)

            assert analyzer.processed is False

            analyzer.analyze()

            assert analyzer.processed is True

    def test_analyze_processed_response(self):
        for word in self.VALID_WORDS:
            analyzer = ArticleMorphologicalAnalyzer(word)
            analyzer.analyze()

            assert analyzer.analyze() is None
            assert analyzer.analyze() is None

class TestArticleMorphologicalAnalyzerConjuctionList:
    def test_conjunctions_not_empty(self):
        assert ArticleMorphologicalAnalyzer.ARTICLES_LIST is not None

    def test_conjunctions_not_size(self):
        assert len(ArticleMorphologicalAnalyzer.ARTICLES_LIST) == 1

    def test_conjunctions_match_list(self):
        for word in ArticleMorphologicalAnalyzer.ARTICLES_LIST:
            assert ArticleMorphologicalAnalyzer.ARTICLES_MATCH_REGEXP.match(word)

    def test_conjunctions_match_final_regexp_list(self):
        for word in ArticleMorphologicalAnalyzer.ARTICLES_LIST:
            assert ArticleMorphologicalAnalyzer.MATCH_REGEXP.match(word)
