"""
This class represent one word beloging to grammar class classified as 'Verb'

What's a Verb?
===
A verb, is a word (part of speech) that in syntax conveys an action (bring, read, walk),
an occurrence (happen, become), or a state of being (be, exist, stand)
"""

from .word import Word

# pylint: disable=too-few-public-methods,missing-docstring,no-self-use
class Verb(Word):
    def __init__(self, content, context=None):
        Word.__init__(self, content, context)

    def has_plural(self):
        return False
