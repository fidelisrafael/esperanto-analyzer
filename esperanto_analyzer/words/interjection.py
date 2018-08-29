# -*- coding: utf-8 -*-
from .base import Word

class Interjection(Word):
  def __init__(self, content, context = None):
    Word.__init__(self, content, context)
