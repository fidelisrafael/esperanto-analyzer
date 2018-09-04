# -*- coding: utf-8 -*-

import pytest

from context import esperanto_analyzer

from esperanto_analyzer.speech import Word, Verb, NotContentError

class TestVerbBasic():
  def test_import(self):
    assert(Verb)

  def test_init(self):
    assert(Verb('esti') != None)

  def test_superclass(self):
    assert(issubclass(Verb, Word))

  def test_valid_content(self):
    assert(Verb('esti'))

  def test_invalid_content(self):
    with pytest.raises(NotContentError):
      assert(Verb(''))

  def test_content(self):
    word = Verb('content')

    assert(word.content == 'content')

  def test_metadata_exists(self):
    word = Verb(' ')

    assert(word.metadata == dict())
