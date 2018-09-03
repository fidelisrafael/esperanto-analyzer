import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from esperanto_analyzer_api.api import MorphologicalAnalyzeEndpoint

from pkg_resources import get_distribution

__version__ = '0.0.1'
