"""
Entry point to load classes
"""
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from .morphological_sentence_analyzer import MorphologicalSentenceAnalyzer

name = 'esperanto_analyzer'
