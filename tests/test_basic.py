import os
import tempfile

import pytest

from context import esperanto_analyzer

from esperanto_analyzer import MorphologicalSentenceAnalyzer

class TestBasic:
    def test_import(self):
        assert MorphologicalSentenceAnalyzer
