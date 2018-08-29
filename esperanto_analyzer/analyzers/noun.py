# -*- coding: utf-8 -*-

import re

from esperanto_analyzer import BaseAnalyzer

class NounAnalyzer(BaseAnalyzer):

  #  MATCHES: ["patro", "patroj", "patron", "patrojn"]
  NOUN_MATCH_REGEXP = re.compile('(/(o((j?n?))?)$/)')

  def match(self, word):
    return self._set_metadata('is_substantive', self.NOUN_MATCH_REGEXP.match(word))
