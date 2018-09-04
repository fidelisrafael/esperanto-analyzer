"""
This class represent one word beloging to grammar class classified as 'Interjection'

What's an Interjection?
===
In linguistics, an interjection is a word or expression that occurs as an utterance on its
own and expresses a spontaneous feeling or reaction.
"""

from .word import Word

# pylint: disable=too-few-public-methods,missing-docstring,no-self-use
class Interjection(Word):

    def has_plural(self):
        return False
