"""
Make 'Parts of Speech' available through the namespace: `esperanto_analyzer.speech`
Eg: `from esperanto_analyzer.speech import Word, Adjective`
"""

from .word import Word, NotContentError
from .adverb import Adverb
from .adjective import Adjective
from .article import Article, InvalidArticleError
from .conjunction import Conjunction
from .interjection import Interjection
from .noun import Noun
from .numeral import Numeral
from .preposition import Preposition
from .pronoun import Pronoun
from .verb import Verb
