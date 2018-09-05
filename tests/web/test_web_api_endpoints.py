import os
import tempfile

import pytest

from context import esperanto_analyzer

from esperanto_analyzer.web.api.server import create_app, run_app
from esperanto_analyzer.web.api.errors import SentenceRequiredError, SentenceInvalidError
from esperanto_analyzer.web.api.morphological_endpoint import MorphologicalAnalyzeEndpoint
from esperanto_analyzer.web.api.results import MorphologicalAnalyzeResult

class TestWebRoot:
    def test_get_404(self, client):
        response = client.get('/')

        assert(response.status_code == 404)

class TestSentenceAnalyze:
    def test_bad_request_without_sentence(self, client):
        response = client.get('/analyze')

        assert(response.status_code == 400)

    def test_ok_with_sentence(self, client):
        response = client.get('/analyze?sentence=Mia%nomo')

        assert(response.status_code == 200)

    def test_response_with_sentence(self, client):
        response = client.get('/analyze?sentence=Mia%nomo')

        assert response.get_json() == [{'word': 'Mianomo', 'value': 'Noun'}]

    def test_response_with_sentence_but_invalid(self, client):
        response = client.get('/analyze?sentence=```')

        assert response.get_json() == []

    def test_response_status_code_with_sentence_but_invalid(self, client):
        response = client.get('/analyze?sentence=```')

        assert response.status_code == 200

    def test_bad_request_without_sentence(self, client):
        response = client.get('/analyze')

        assert(response.status_code == 400)

    def test_exception_with_empty_sentence(self, client):
        with pytest.raises(SentenceRequiredError):
            assert client.get('/analyze?sentence=')

    def test_options_request(self, client):
        response = client.options('/analyze')

        assert response.status_code == 200

    def test_options_response_CORS_origin_header(self, client):
        response = client.options('/analyze')

        assert response.headers['Access-Control-Allow-Origin'] == '*'

    def test_options_response_CORS_headers_header(self, client):
        response = client.options('/analyze')
        assert response.headers['Access-Control-Allow-Headers'] == '*'

    def test_options_response_CORS_origin_header(self, client):
        response = client.options('/analyze')

        assert response.headers['Access-Control-Allow-Method'] == 'POST, GET, OPTIONS'

    def test_unicode_encoded_response(self, client):
        response = client.get('analyze?sentence=👍👍👍')

        assert response.get_json() == [{'word': '👍', 'value': 'Undefined'}, {'word': '👍', 'value': 'Undefined'}, {'word': '👍', 'value': 'Undefined'}]

    def test_unicode_encoded_response(self, client):
        response = client.get('analyze?sentence=%F0%9F%91%8D%20%F0%9F%91%8E%20%F0%9F%91%8E')

        assert response.get_json() == [{'word': '👍', 'value': 'Undefined'}, {'word': '👎', 'value': 'Undefined'}, {'word': '👎', 'value': 'Undefined'}]

class TestMorphologicalAnalyzeEndpoint():
    def test__format_results_none(self):
        instance = MorphologicalAnalyzeEndpoint()

        assert instance._format_results(None) == []

    def test__format_results_error(self):
        instance = MorphologicalAnalyzeEndpoint()
        results = [[dict(), None]]

        assert instance._format_results(results) == [{'word': {}, 'value': 'Undefined', 'extra': {}}]


class TestMorphologicalAnalyzeResult():
    def test_results(self):
        result = MorphologicalAnalyzeResult(dict(test=1, works=2))

        assert result.results == dict(test=1, works=2)
