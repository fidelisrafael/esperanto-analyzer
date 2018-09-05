from flask import Flask, request
from flask_cors import CORS

from flask_restful import Resource, Api, marshal_with, fields, abort

from flask_restful_swagger import swagger
from esperanto_analyzer.web.api import MorphologicalAnalyzeEndpoint

API_VERSION_NUMBER = '1.0'
API_VERSION_LABEL = 'v1'

class MorphologicalAnalyzesAPI(object):

    def __init__(self):
        self.create_app()


    def create_app(self):
        self.app = Flask(__name__)
        CORS(self.app)

        custom_errors = {
            'SentenceInvalidError': {
                'status': 500,
                'message': 'Sentence format not valid'
            },
            'SentenceRequiredError': {
                'status': 400,
                'message': 'Sentence not provided'
            }
        }

        self.api = swagger.docs(Api(self.app, errors=custom_errors), apiVersion=API_VERSION_NUMBER)

        self.api.add_resource(MorphologicalAnalyzeEndpoint, '/analyze', endpoint='analyze')

        return self.app

    def run(self, *args, **kwargs): # pragma: no cover
        self.app.config['PROPAGATE_EXCEPTIONS'] = False
        self.app.run(*args, **kwargs)


def create_app():
    return MorphologicalAnalyzesAPI()

def run_app(*args, **kwargs): # pragma: no cover
    app = create_app()
    app.run(*args, **kwargs)

