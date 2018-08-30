# -*- coding: utf-8 -*-

import pytest

from context import esperanto_analyzer

from esperanto_analyzer.speech import Word, Adjective, NotContentError

class TestAdjectiveBasic():
  def test_import(self):
    assert(Adjective)

  def test_init(self):
    assert(Adjective('bela') != None)

  def test_superclass(self):
    assert(issubclass(Adjective, Word))

  def test_valid_content(self):
    assert(Adjective('bela'))

  def test_invalid_content(self):
    with pytest.raises(NotContentError):
      assert(Adjective(''))

  def test_content(self):
    word = Adjective('content')

    assert(word.content == 'content')

  def test_metadata_exists(self):
    word = Adjective(' ')

    assert(word.metadata == dict())
