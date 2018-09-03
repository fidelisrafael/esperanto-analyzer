# pylint: disable=missing-docstring,no-self-use

import re
import pytest

from context import esperanto_analyzer

from esperanto_analyzer.speech import Word
from esperanto_analyzer.speech import Adverb
from esperanto_analyzer.speech import Adjective
from esperanto_analyzer.speech import Article, InvalidArticleError
from esperanto_analyzer.speech import Conjunction
from esperanto_analyzer.speech import Interjection
from esperanto_analyzer.speech import Noun
from esperanto_analyzer.speech import Numeral
from esperanto_analyzer.speech import Preposition
from esperanto_analyzer.speech import Pronoun
from esperanto_analyzer.speech import Verb

from esperanto_analyzer import MorphologicalSentenceAnalyzer


class TestMorphologicalSentenceAnalyzerBasic():
    TEST_SENTENCE = 'Mi loĝas en Brazilo'

    def test_import(self):
        assert MorphologicalSentenceAnalyzer

    def test_initialize(self):
        assert MorphologicalSentenceAnalyzer(self.TEST_SENTENCE)

    def test_initialize_sentence(self):
        analyzer = MorphologicalSentenceAnalyzer(self.TEST_SENTENCE)

        assert analyzer.sentence is self.TEST_SENTENCE

    def test_initialize_sentence_words(self):
        analyzer = MorphologicalSentenceAnalyzer(self.TEST_SENTENCE)

        assert analyzer.sentence_words == ['Mi', 'loĝas', 'en', 'Brazilo']

    def test_initialize_results(self):
        analyzer = MorphologicalSentenceAnalyzer(self.TEST_SENTENCE)

        assert analyzer.results() is None

    def test_initialize_processed(self):
        analyzer = MorphologicalSentenceAnalyzer(self.TEST_SENTENCE)

        assert analyzer.processed is False

    def test_analyze(self):
        analyzer = MorphologicalSentenceAnalyzer(self.TEST_SENTENCE)

        assert analyzer.analyze()

    def test_analyze_results(self):
        analyzer = MorphologicalSentenceAnalyzer(self.TEST_SENTENCE)

        assert analyzer.analyze()
        assert analyzer.results() is not None

    def test_analyze_results_size(self):
        analyzer = MorphologicalSentenceAnalyzer(self.TEST_SENTENCE)

        assert analyzer.analyze()
        assert len(analyzer.results()) == 4
        assert len(analyzer.results()[1]) == 2

    def test_analyze_processed(self):
        analyzer = MorphologicalSentenceAnalyzer(self.TEST_SENTENCE)

        assert analyzer.processed is False
        assert analyzer.analyze()
        assert analyzer.processed is True

    def test_analyze_processed_multiples_times(self):
        analyzer = MorphologicalSentenceAnalyzer(self.TEST_SENTENCE)

        assert analyzer.processed is False
        assert analyzer.analyze() # First analyze
        assert analyzer.processed is True
        assert analyzer.analyze() is None
        assert analyzer.analyze() is None

    def test_analyze_internal_results_class(self):
        analyzer = MorphologicalSentenceAnalyzer(self.TEST_SENTENCE)
        analyzer.analyze()

        classes_names = [an.__class__.__name__ for an in analyzer.internal_results]

        assert classes_names == ['MorphologicalAnalyzer', 'MorphologicalAnalyzer', 'MorphologicalAnalyzer', 'MorphologicalAnalyzer']

    def test_analyzes_results_not_processed(self):
        analyzer = MorphologicalSentenceAnalyzer(self.TEST_SENTENCE)

        assert analyzer.analyzes_results() is None

    def test_analyzes_internals_results_processed(self):
        analyzer = MorphologicalSentenceAnalyzer(self.TEST_SENTENCE)
        analyzer.analyze()

        assert analyzer.analyzes_results() == [result.results for result in analyzer.internal_results]

    def test_analyzes_results_class(self):
        analyzer = MorphologicalSentenceAnalyzer(self.TEST_SENTENCE)
        analyzer.analyze()

        classes_names = [analyze.__class__.__name__ for analyze in analyzer.analyzes_results()]

        assert classes_names == ['AnalyzeResult', 'AnalyzeResult', 'AnalyzeResult', 'AnalyzeResult']

    def test_analyzes_results_class_result(self):
        analyzer = MorphologicalSentenceAnalyzer(self.TEST_SENTENCE)
        analyzer.analyze()

        result_classes = [analyze.result.__class__.__name__ for analyze in analyzer.analyzes_results()]

        assert result_classes == ['PronounMorphologicalAnalyzer', 'VerbMorphologicalAnalyzer', 'PrepositionMorphologicalAnalyzer', 'NounMorphologicalAnalyzer']

    def test_analyzes_results_word_classnames(self):
        analyzer = MorphologicalSentenceAnalyzer(self.TEST_SENTENCE)
        analyzer.analyze()

        result_classes = [analyze.result.word.__class__.__name__ for analyze in analyzer.analyzes_results()]

        assert result_classes == ['Pronoun', 'Verb', 'Preposition', 'Noun']

    def test_analyzes_results_raw_word(self):
        analyzer = MorphologicalSentenceAnalyzer(self.TEST_SENTENCE)
        analyzer.analyze()

        words = [analyze.result.raw_word for analyze in analyzer.analyzes_results()]

        assert words == ['Mi', 'loĝas', 'en', 'Brazilo']

    def test_analyzes_results_processed(self):
        analyzer = MorphologicalSentenceAnalyzer(self.TEST_SENTENCE)
        analyzer.analyze()

        processed_status = [an.result.processed for an in analyzer.analyzes_results()]

        assert processed_status == [True, True, True, True]

    def test_analyzes_results_word_class(self):
        analyzer = MorphologicalSentenceAnalyzer(self.TEST_SENTENCE)
        analyzer.analyze()

        words_classes = [an.result.word_class() for an in analyzer.analyzes_results()]

        assert words_classes == [Pronoun, Verb, Preposition, Noun]


    def test_sentence_clean_regexp(self):
        sentence = '(Mia) [nomo] estas, Esperanto. Hodiau estas la jaro 2018. jes'
        new_sentence = re.sub(MorphologicalSentenceAnalyzer.SENTENCE_CLEAN_REGEXP, '', sentence)

        assert new_sentence == 'Mia nomo estas Esperanto Hodiau estas la jaro 2018 jes'

    def test_undefined_token(self):
        analyzer = MorphologicalSentenceAnalyzer('Mia asdiosdsds')
        analyzer.analyze()

        assert analyzer.simple_results() == [['Mia', 'Pronoun'], ['asdiosdsds', 'Undefined']]
        assert analyzer.simple_results()[1][1] == 'Undefined'
