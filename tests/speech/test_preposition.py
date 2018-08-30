# -*- coding: utf-8 -*-

import pytest

from context import esperanto_analyzer

from esperanto_analyzer.speech import Word, Preposition, NotContentError

class TestPrepositionBasic():
  def test_import(self):
    assert(Preposition)

  def test_init(self):
    assert(Preposition('post') != None)

  def test_superclass(self):
    assert(issubclass(Preposition, Word))

  def test_valid_content(self):
    assert(Preposition('post'))

  def test_invalid_content(self):
    with pytest.raises(NotContentError):
      assert(Preposition(''))

  def test_content(self):
    word = Preposition('content')

    assert(word.content == 'content')

  def test_metadata_exists(self):
    word = Preposition(' ')

    assert(word.metadata == dict())
