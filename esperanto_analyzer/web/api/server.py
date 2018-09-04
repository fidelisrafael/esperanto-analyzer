from flask import Flask, request
from flask_restful import Resource, Api, marshal_with, fields, abort

from flask_restful_swagger import swagger
from esperanto_analyzer.web.api import MorphologicalAnalyzeEndpoint

API_VERSION_NUMBER = '1.0'
API_VERSION_LABEL = 'v1'

class MorphologicalAnalyzesAPI(object):

    def __init__(self):
        self.app = Flask(__name__)

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

    def run(self, *args, **kwargs):
        self.app.config['PROPAGATE_EXCEPTIONS'] = False
        self.app.run(*args, **kwargs)


def run_app(*args, **kwargs):
    app = MorphologicalAnalyzesAPI()
    app.run(*args, **kwargs)

