# -*- coding: utf-8 -*-
from .base import Word

class Article(Word):
  def __init__(self, content):
    Word.__init__(self, content)
