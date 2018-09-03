"""
Make 'Parts of Speech' available through the namespace: `esperanto_analyzer.analyzers.morphological`
Eg: `from esperanto_analyzer.analyzers.morphological import AdverbMorphologicalAnalyzer`
"""

from .base import BaseMorphologicalAnalyzer

from .adverb import AdverbMorphologicalAnalyzer
from .adjective import AdjectiveMorphologicalAnalyzer
from .article import ArticleMorphologicalAnalyzer
from .conjunction import ConjunctionMorphologicalAnalyzer
from .interjection import InterjectionMorphologicalAnalyzer
from .noun import NounMorphologicalAnalyzer
from .numeral import NumeralMorphologicalAnalyzer
from .preposition import PrepositionMorphologicalAnalyzer
from .pronoun import PronounMorphologicalAnalyzer
from .verb import VerbMorphologicalAnalyzer

from .analyze_result import AnalyzeResult
