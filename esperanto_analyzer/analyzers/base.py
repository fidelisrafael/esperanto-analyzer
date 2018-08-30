# -*- coding: utf-8 -*-

class BaseAnalyzer:
    def __init__(self, options = None):
    # Python dicts() as default argument is not a great idea since Python don't
    # creates a new version of the default argument in every method call
        if options is None: options=dict()

        self.matches = dict()
        self.options = options

    def match(self, word):
        raise NotImplementedError

    def matched(self, type):
        if not type in self.matches: return False

        return self.matches[type] == True

    def _set_match(self, key, value):
        self.matches[key] = value

        return value
