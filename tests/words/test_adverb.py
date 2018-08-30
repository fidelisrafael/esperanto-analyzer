# -*- coding: utf-8 -*-

import pytest

from context import esperanto_analyzer

from esperanto_analyzer.speech import Word, Adverb, NotContentError

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


class TestAdverbPlural():
  def test_has_plural(self):
    assert(Adverb('multe').has_plural() == False)

  def test_plural(self):
    word = Adverb('multe')

    assert(word.plural == False)

  def test_plural_ending_word(self):
    for word in ['multaj', 'multajn']:
      assert(Adverb(word).plural == False)
