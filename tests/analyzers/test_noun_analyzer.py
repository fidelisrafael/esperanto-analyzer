# -*- coding: utf-8 -*-

import pytest

from context import esperanto_analyzer
from esperanto_analyzer import NounAnalyzer

class TestNounAnalyzerBasic():
  def test_import(self):
      assert(NounAnalyzer != None)

  def test_init(self):
    assert(NounAnalyzer() != None)

## Context: Method
#  Method: "TestNounAnalyzer().match()"
class TestNounAnalyzerMatchMethodSimple():
  def test_singular(self):
    assert(NounAnalyzer().match('vorto'))

  def test_plural(self):
    assert(NounAnalyzer().match('vortoj'))

  def test_singular_acusative(self):
    assert(NounAnalyzer().match('vorton'))

  def test_plural_acusative(self):
    assert(NounAnalyzer().match('vortojn'))

## Context: Method
#  Method: "TestNounAnalyzer().match()"
class TestNounAnalyzerMatchMethodBatch():

  EXAMPLE_VALID_WORDS = [
    'vorto', 'vorton', 'vortoj', 'vortojn',
    'patro', 'patron', 'patroj', 'patrojn',
    'patrino', 'patrinon', 'patrinoj', 'patrinoj'
  ]

  def test_valid_batch(self):
    for word in self.EXAMPLE_VALID_WORDS:
      assert(NounAnalyzer().match(word))

  def test_valid_batch_upper(self):
    for word in self.EXAMPLE_VALID_WORDS:
      assert(NounAnalyzer().match(word.upper()))

  def test_valid_batch_lower(self):
    for word in self.EXAMPLE_VALID_WORDS:
      assert(NounAnalyzer().match(word.lower()))


## Context: Method
#  Method: "TestNounAnalyzer().match()"
class TestNounAnalyzerMatchMethodError():

  EXAMPLE_NOT_VALID_WORDS = [
    # Adjectives
    'bela', 'belan', 'belaj', 'belajn',
    # Adverbs
    'multe', 'nun',
    # Verbs
    'estis', 'estas', 'estos',
    'estu', 'estus', 'esti'
  ]

  def test_invalid_batch(self):
    for word in self.EXAMPLE_NOT_VALID_WORDS:
      assert(NounAnalyzer().match(word) == False)

  def test_invalid_batch_upper(self):
    for word in self.EXAMPLE_NOT_VALID_WORDS:
      assert(NounAnalyzer().match(word.upper()) == False)

  def test_invalid_batch_lower(self):
    for word in self.EXAMPLE_NOT_VALID_WORDS:
      assert(NounAnalyzer().match(word.lower()) == False)
