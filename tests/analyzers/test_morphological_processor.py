# pylint: disable=missing-docstring,no-self-use

import pytest

from context import esperanto_analyzer

from esperanto_analyzer.analyzers.morphological_processor import MorphologicalProcessor

class TestMorphologicalProcessorBasic():
    def test_import(self):
        assert MorphologicalProcessor
