# -*- coding: utf-8 -*-
from .base import Word


class Article(Word):
  VALID_ARTICLES = ['la']

  def __init__(self, content, context = None):
    Word.__init__(self, content, context)

  def has_plural(self):
    return True

  def _match_plural(self, context = None):
    if(context):
      return Word(context).plural

    return False

  def _validate_content(self, content):
    Word._validate_content(self, content)

    if not content.lower() in self.VALID_ARTICLES:
      raise InvalidArticleError

class InvalidArticleError(Exception):
  pass
