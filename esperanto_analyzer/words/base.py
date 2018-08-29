# -*- coding: utf-8 -*-

import re

class Word:

  # Only words with at least 4 characteres can be in plural, so this exclude
  # words such "ajn" and "kaj".
  PLURAL_DETECT_REGEXP = re.compile('.{2,}([^n]j|jn)$', re.IGNORECASE|re.UNICODE)

  def __init__(self, content, context = None):
    self._validate_content(content)

    self.content = content
    self.context = context
    self.metadata = dict()
    self.plural = (self._match_plural(context) not in [False, None])

  def has_plural(self):
    return True

  def _match_plural(self, context = None):
    if not self.has_plural(): return None

    return self.PLURAL_DETECT_REGEXP.match(self.content)

  def _validate_content(self, content):
    if not content:
      raise NotContentError

class NotContentError(Exception):
  pass
