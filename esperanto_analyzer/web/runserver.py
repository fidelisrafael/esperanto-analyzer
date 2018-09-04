import os
from context import esperanto_analyzer

from esperanto_analyzer.web.api.server import run_app

# from esperanto_analyzer import MorphologicalSentenceAnalyzer

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    host = str(os.environ.get('HOST', '0.0.0.0'))

    run_app(debug=True, host=host, port=port)
