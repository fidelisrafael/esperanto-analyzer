# -*- coding: utf-8 -*-

import re

from esperanto_analyzer import BaseAnalyzer

class NounAnalyzer(BaseAnalyzer):

  #  MATCHES: ["patro", "patroj", "patron", "patrojn"]
  NOUN_MATCH_REGEXP = re.compile('(.{1,}(o((j?n?))?)$)', re.IGNORECASE|re.UNICODE)
  NOUN_TYPE = 'noun'

  def match(self, word):
    return self._set_match(self.NOUN_TYPE, (self.NOUN_MATCH_REGEXP.match(word) != None))
