# -*- coding: utf-8 -*-

import pytest

from context import esperanto_analyzer

from esperanto_analyzer.words.base import Word, NotContentError
from esperanto_analyzer.words import Adverb

class TestAdverbBasic():
  def test_import(self):
    assert(Adverb)

  def test_init(self):
    assert(Adverb('multe') != None)

  def test_superclass(self):
    assert(issubclass(Adverb, Word))

  def test_valid_content(self):
    assert(Adverb('multe'))

  def test_invalid_content(self):
    with pytest.raises(NotContentError):
      assert(Adverb(''))

  def test_content(self):
    word = Adverb('content')

    assert(word.content == 'content')

  def test_metadata_exists(self):
    word = Adverb(' ')

    assert(word.metadata == dict())
