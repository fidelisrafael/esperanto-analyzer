"""
This class represent one word beloging to grammar class classified as 'Preposition'

What's a Preposition?
===
A word governing, and usually preceding, a noun or pronoun and expressing a relation
to another word or element in the clause.
Prepositions are often used to express spatial or temporal relations (in, under, towards, before)
"""

from .word import Word

# pylint: disable=too-few-public-methods,missing-docstring,no-self-use
class Preposition(Word):

    def has_plural(self):
        return False
