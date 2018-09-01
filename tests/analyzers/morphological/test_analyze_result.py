# pylint: disable=no-self-use,missing-docstring

import pytest

from context import esperanto_analyzer

from esperanto_analyzer.analyzers.morphological import AnalyzeResult

class TestAdjectiveBasic():
    TEST_WORD = 'kapo'

    def test_import(self):
        assert AnalyzeResult

    def test_init(self):
        assert AnalyzeResult(result=None, raw_word=None) is not None

    def test_result(self):
        analyze_result = AnalyzeResult(dict(some='object'), raw_word=self.TEST_WORD)

        assert analyze_result.result == dict(some='object')

    def test_raw_word(self):
        analyze_result = AnalyzeResult(dict(some='object'), raw_word=self.TEST_WORD)

        assert analyze_result.raw_word == self.TEST_WORD
