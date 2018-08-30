# -*- coding: utf-8 -*-

import pytest

from context import esperanto_analyzer

from esperanto_analyzer.speech import Word, Conjunction, NotContentError

class TestConjunctionBasic():
  def test_import(self):
    assert(Conjunction)

  def test_init(self):
    assert(Conjunction('kaj') != None)

  def test_superclass(self):
    assert(issubclass(Conjunction, Word))

  def test_valid_content(self):
    assert(Conjunction('kaj'))

  def test_invalid_content(self):
    with pytest.raises(NotContentError):
      assert(Conjunction(''))

  def test_content(self):
    word = Conjunction('content')

    assert(word.content == 'content')

  def test_metadata_exists(self):
    word = Conjunction(' ')

    assert(word.metadata == dict())
