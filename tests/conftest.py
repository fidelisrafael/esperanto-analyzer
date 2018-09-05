import os
import tempfile

import pytest

from context import esperanto_analyzer

from esperanto_analyzer.web.api.server import create_app

@pytest.fixture
def app():
    # create the app with common test config
    app = create_app().app
    app.config['TESTING'] = True

    yield app

    return app

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

@pytest.fixture
def runner(app):
    """A test runner for the app's Click commands."""
    return app.test_cli_runner()
