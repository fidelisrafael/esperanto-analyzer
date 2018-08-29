# -*- coding: utf-8 -*-

class BaseAnalyzer:
  def __init__(self, options = None):
    # Python dicts() as default argument is not a great idea since Python don't
    # creates a new version of the default argument in every method call
    if options is None: options = dict()

    self.metadata = dict()
    self.options = options

  def match(self, word):
    raise NotImplementedError

  def _set_metadata(self, key, value):
    self.metadata[key] = value
