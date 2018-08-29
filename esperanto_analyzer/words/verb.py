# -*- coding: utf-8 -*-
from .base import Word

class Verb(Word):
  def __init__(self, content, context = None):
    Word.__init__(self, content, context)
