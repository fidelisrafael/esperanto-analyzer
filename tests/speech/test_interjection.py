# -*- coding: utf-8 -*-

import pytest

from context import esperanto_analyzer

from esperanto_analyzer.speech import Word, Interjection, NotContentError

class TestInterjectionBasic():
  def test_import(self):
    assert(Interjection)

  def test_init(self):
    assert(Interjection('ek!') != None)

  def test_superclass(self):
    assert(issubclass(Interjection, Word))

  def test_valid_content(self):
    assert(Interjection('ek!'))

  def test_invalid_content(self):
    with pytest.raises(NotContentError):
      assert(Interjection(''))

  def test_content(self):
    word = Interjection('content')

    assert(word.content == 'content')

  def test_metadata_exists(self):
    word = Interjection(' ')

    assert(word.metadata == dict())
