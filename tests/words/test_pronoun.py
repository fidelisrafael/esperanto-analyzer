# -*- coding: utf-8 -*-

import pytest

from context import esperanto_analyzer

from esperanto_analyzer.words.base import Word, NotContentError
from esperanto_analyzer.words import Pronoun

class TestPronounBasic():
  def test_import(self):
    assert(Pronoun)

  def test_init(self):
    assert(Pronoun('mi') != None)

  def test_superclass(self):
    assert(issubclass(Pronoun, Word))

  def test_valid_content(self):
    assert(Pronoun('mi'))

  def test_invalid_content(self):
    with pytest.raises(NotContentError):
      assert(Pronoun(''))

  def test_content(self):
    word = Pronoun('content')

    assert(word.content == 'content')

  def test_metadata_exists(self):
    word = Pronoun(' ')

    assert(word.metadata == dict())
