# -*- coding: utf-8 -*-

import pytest

from context import esperanto_analyzer

from esperanto_analyzer.speech import Word, Noun, NotContentError

class TestNounBasic():
  def test_import(self):
    assert(Noun)

  def test_init(self):
    assert(Noun('lingvo') != None)

  def test_superclass(self):
    assert(issubclass(Noun, Word))

  def test_valid_content(self):
    assert(Noun('lingvo'))

  def test_invalid_content(self):
    with pytest.raises(NotContentError):
      assert(Noun(''))

  def test_content(self):
    word = Noun('content')

    assert(word.content == 'content')

  def test_metadata_exists(self):
    word = Noun(' ')

    assert(word.metadata == dict())


class TestNounGender():
    def test_has_gender(self):
        assert(Noun('lingvo').has_gender())
