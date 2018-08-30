# pylint: disable=missing-docstring,no-self-use

import pytest

from context import esperanto_analyzer

from esperanto_analyzer.analyzers.morphological import BaseMorphologicalAnalyzer

class TestMorphologicalProcessorBasic():
    def test_import(self):
        assert BaseMorphologicalAnalyzer
