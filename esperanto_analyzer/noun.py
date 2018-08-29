# -*- coding: utf-8 -*-

import re

from esperanto_analyzer import BaseAnalyzer

class NounAnalyzer(BaseAnalyzer):

  #  MATCHES: ["patro", "patroj", "patron", "patrojn"]
  NOUN_MATCH_REGEXP = r'(/(o((j?n?))?)$/)'

  def match(self, word):
    return self.set_metadata('is_substantive', re.compile(NOUN_MATCH_REGEXP).match(word))
