# -*- coding: utf-8 -*-

import pytest

from context import esperanto_analyzer

from esperanto_analyzer.words.base import Word, NotContentError
from esperanto_analyzer.words import Article

class TestArticleBasic():
  def test_import(self):
    assert(Article)

  def test_init(self):
    assert(Article('la') != None)

  def test_superclass(self):
    assert(issubclass(Article, Word))

  def test_valid_content(self):
    assert(Article('la'))

  def test_invalid_content(self):
    with pytest.raises(NotContentError):
      assert(Article(''))

  def test_content(self):
    word = Article('content')

    assert(word.content == 'content')

  def test_metadata_exists(self):
    word = Article(' ')

    assert(word.metadata == dict())
