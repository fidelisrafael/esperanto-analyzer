"""
This class represents one analyzed raw word transformed in one `Part of Speech` object
such as `Verb`, `Adverb`.

Eg: word = AnalyzedWord.
"""

# pylint: disable=too-few-public-methods,missing-docstring
class AnalyzeResult:
    def __init__(self, result):
        self.result = result
