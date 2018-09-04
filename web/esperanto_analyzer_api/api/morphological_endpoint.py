from flask import request
from flask_restful import Resource, Api, marshal_with, fields, abort
from flask_restful_swagger import swagger
from .results import MorphologicalAnalyzeResult
from .errors import SentenceRequiredError
from .errors import SentenceInvalidError

from esperanto_analyzer import MorphologicalSentenceAnalyzer
from esperanto_analyzer.cli import CLI

class MorphologicalAnalyzeEndpoint(Resource):
    @swagger.operation(
        responseClass=MorphologicalAnalyzeResult.__name__,
        nickname='analyzes',
        responseMessages=[
            {"code": 400, "message": "Input required"},
            {"code": 500, "message": "JSON format not valid"},
        ],
        parameters=[
            {
                "name": "sentence",
                "description": "The esperanto sentence to be analyzed morphologically",
                "required": True,
                "allowMultiple": False,
                "dataType": "string",
                "paramType": "query"
            },
        ])
    @marshal_with(MorphologicalAnalyzeResult.resource_fields)
    def get(self):
        """Return a MorphologicalAnalyzeResult object"""
        sentence = request.args['sentence']

        if not sentence:
            raise SentenceRequiredError()
        try:
            analyzer = MorphologicalSentenceAnalyzer(sentence=sentence)
            analyzer.analyze()

            return self._format_results(analyzer.results())
        except (KeyError, AttributeError) as error:
            raise SentenceInvalidError()

    def _format_results(self, results=None):
        if results is None:
            results = []

        data = []

        for result in results:
            try:
                # Get the current 'Part of Speech' name, such as: 'Adverb', 'Noun'
                pos_name = result[1].result.word.__class__.__name__
            except:
                pos_name = 'Undefined'

            data.append(dict(word=result[0], value=pos_name, extra=dict()))

        return data
