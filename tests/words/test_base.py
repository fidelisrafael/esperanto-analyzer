# -*- coding: utf-8 -*-

import pytest

from context import esperanto_analyzer

from esperanto_analyzer.speech import Word, NotContentError

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


class TestValidWordPlural():
  def test_esperanto_words(self):
    for word in ['kaj', 'ajn']:
      assert(Word(word).plural == False)

  def test_plural_without_acusative(self):
    word = Word('domoj')

    assert(word.plural == True)

  def test_plural_with_acusative(self):
    word = Word('domojn')

    assert(word.plural == True)

class TestInvalidWordPlural():
  def test_plural_without_acusative(self):
    word = Word('domo')

    assert(word.plural == False)

  def test_plural_with_acusative(self):
    word = Word('domon')

    assert(word.plural == False)

class TestPluralWord(Word):
  def has_plural(self):
    return False

class TestValidWordDontHasPlural:
  def test_valid_word_plural(self):
    word = TestPluralWord('multe')

    assert(word.plural == False)
