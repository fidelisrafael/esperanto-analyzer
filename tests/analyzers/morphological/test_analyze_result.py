# pylint: disable=no-self-use,missing-docstring

import pytest

from context import esperanto_analyzer

from esperanto_analyzer.analyzers.morphological import AnalyzeResult

class TestAdjectiveBasic():
    def test_import(self):
        assert AnalyzeResult

    def test_init(self):
        assert AnalyzeResult(None) is not None

    def test_result(self):
        analyze_result = AnalyzeResult(dict(some='object'))

        assert analyze_result.result == dict(some='object')
