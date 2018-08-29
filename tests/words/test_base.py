# -*- coding: utf-8 -*-

import pytest

from context import esperanto_analyzer
from esperanto_analyzer.words.base import Word, NotContentError

class TestWordBasic():
  def test_import(self):
    assert(Word)

  def test_init(self):
    assert(Word(' ') != None)

  def test_valid_content(self):
    assert(Word('a'))

  def test_invalid_content(self):
    with pytest.raises(NotContentError):
      assert(Word(''))

  def test_content(self):
    word = Word('content')

    assert(word.content == 'content')

  def test_metadata_exists(self):
    word = Word(' ')

    assert(word.metadata == dict())
