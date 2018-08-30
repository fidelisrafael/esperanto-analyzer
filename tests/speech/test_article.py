# -*- coding: utf-8 -*-

import pytest

from context import esperanto_analyzer

from esperanto_analyzer.speech import Word, Article
from esperanto_analyzer.speech import NotContentError, InvalidArticleError

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
    word = Article('la')

    assert(word.content == 'la')

  def test_metadata_exists(self):
    word = Article('la')

    assert(word.metadata == dict())

class TestInvalidArticleContent():
  def test_empty_content(self):
    with pytest.raises(NotContentError):
      assert(Article(''))

  def test_whitespace_content(self):
    with pytest.raises(InvalidArticleError):
      assert(Article(' '))

  def test_invalid_content(self):
    for word in [' ', 'lo', 'en', 'laj']:
      with pytest.raises(InvalidArticleError):
        assert(Article(word))


class TestArticlePlural():
  def test_has_plural(self):
    assert(Article('la').has_plural())

  def test_plural(self):
    word = Article('la')

    assert(word.plural == False)

  def test_plural_with_plural_context(self):
    for word in ['ĉevaloj', 'ĉevalojn', 'belaj', 'belajn']:
      article = Article('la', context = word)
      assert(article.plural == True)

  def test_plural_with_singular_context(self):
    for word in ['ĉevalo', 'ĉevalon', 'bela', 'belan', 'multe', 'tre']:
      article = Article('la', context = word)
      assert(article.plural == False)
