"""
This class represent one word beloging to grammar class classified as 'Noun'

What's a Noun?
===
A noun is a word(other than a pronoun) that functions as the name of some specific thing
or set of things, such as living creatures, objects, places, actions, feelings...
"""
from .word import Word

# pylint: disable=too-few-public-methods,missing-docstring,no-self-use
class Noun(Word):

    def has_gender(self):
        return True
