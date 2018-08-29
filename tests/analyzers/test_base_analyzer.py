# -*- coding: utf-8 -*-

import pytest

from context import esperanto_analyzer
from esperanto_analyzer import BaseAnalyzer

class TestBaseAnalyzerBasic():
    def test_import(self):
        assert(esperanto_analyzer != None)

    def test_init(self):
        assert(BaseAnalyzer() != None)

    def test_custom_options(self):
      options = dict(custom_options = True)
      klass = BaseAnalyzer(options)

      assert(options == klass.options)

    def test_matches(self):
      klass = BaseAnalyzer()

      assert(klass.matches == dict())

## Context: Method
#  Method: "TestBaseAnalyzer().matched()"
class TestBaseAnalyzerMatchedMethod():
  def test_matched(self):
    klass = BaseAnalyzer()
    klass._set_match('test', True)

    assert(klass.matched('test'))

  def test_not_matched(self):
    klass = BaseAnalyzer()
    klass._set_match('test', False)

    assert(klass.matched('test') == False)

  def test_key_not_existent_matched(self):
    klass = BaseAnalyzer()

    assert(klass.matched('test') == False)

## Context: Method
#  Method: "TestBaseAnalyzer().match()"
class TestBaseAnalyzerMatchMethod():
  def test_not_implemented_error(self):
    klass = BaseAnalyzer()

    with pytest.raises(NotImplementedError):
      assert(klass.match('vorto'))

## Context: Method
#  Method: "TestBaseAnalyzer()._set_match()"
class TestBaseAnalyzerSetMatchMethod():
  def test_return_value(self):
    klass = BaseAnalyzer()

    assert(klass._set_match('test', True))
    assert(klass._set_match('test', 'SomeValue') == 'SomeValue')

  def test_set_matches(self):
    klass = BaseAnalyzer()
    klass._set_match('test', True)

    assert(klass.matches['test'] == True)
