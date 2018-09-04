# -*- coding: utf-8 -*-

import pytest

from context import esperanto_analyzer

from esperanto_analyzer.speech import Word, Numeral, NotContentError

class TestNumeralBasic():
  def test_import(self):
    assert(Numeral)

  def test_init(self):
    assert(Numeral('10') != None)

  def test_superclass(self):
    assert(issubclass(Numeral, Word))

  def test_valid_content(self):
    assert(Numeral('dek'))

  def test_invalid_content(self):
    with pytest.raises(NotContentError):
      assert(Numeral(''))

  def test_content(self):
    word = Numeral('du dek')

    assert(word.content == 'du dek')

  def test_metadata_exists(self):
    word = Numeral(' ')

    assert(word.metadata == dict())
