from flask_restful import Resource, Api, marshal_with, fields, abort
from flask_restful_swagger import swagger

@swagger.model
class MorphologicalAnalyzeResult(object):
    """The result of a call to /hello"""
    resource_fields = {
        'word': fields.String,
        'value': fields.String,
    }

    def __init__(self, results):
        self.results = results
