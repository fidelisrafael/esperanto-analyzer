"""
This class represent one word beloging to grammar class classified as 'Conjuction'

What's a Conjuction?
===
In grammar, a conjunction is a part of speech(a word) that connects words, phrases, or clauses
that are called the conjuncts of the conjoining construction.
"""

from .word import Word

# pylint: disable=too-few-public-methods,missing-docstring,no-self-use
class Conjunction(Word):

    def has_plural(self):
        return False
