# -*- coding: utf-8 -*-

class Word:

  def __init__(self, content):
    self.__validate_content(content)

    self.content = content
    self.metadata = dict()

  def __validate_content(self, content):
    if not content:
      raise NotContentError

class NotContentError(Exception):
  pass
