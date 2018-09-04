# pylint: disable=missing-docstring,no-self-use

import importlib
import pytest

from context import esperanto_analyzer

from esperanto_analyzer.speech import Word, NotContentError
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

from esperanto_analyzer.analyzers.morphological import AdjectiveMorphologicalAnalyzer
from esperanto_analyzer.analyzers.morphological import AdverbMorphologicalAnalyzer
from esperanto_analyzer.analyzers.morphological import ArticleMorphologicalAnalyzer
from esperanto_analyzer.analyzers.morphological import ConjunctionMorphologicalAnalyzer
from esperanto_analyzer.analyzers.morphological import InterjectionMorphologicalAnalyzer
from esperanto_analyzer.analyzers.morphological import NounMorphologicalAnalyzer
from esperanto_analyzer.analyzers.morphological import NumeralMorphologicalAnalyzer
from esperanto_analyzer.analyzers.morphological import PrepositionMorphologicalAnalyzer
from esperanto_analyzer.analyzers.morphological import PronounMorphologicalAnalyzer
from esperanto_analyzer.analyzers.morphological import VerbMorphologicalAnalyzer
from esperanto_analyzer.analyzers.morphological import AnalyzeResult

from esperanto_analyzer.analyzers import MorphologicalAnalyzer

class TestMorphologicalAnalyzerBasic():
    TEST_WORD = 'komputilo'
    DEFAULT_ANALYZERS = [
        AdverbMorphologicalAnalyzer,
        ArticleMorphologicalAnalyzer,
        ConjunctionMorphologicalAnalyzer,
        InterjectionMorphologicalAnalyzer,
        NumeralMorphologicalAnalyzer,
        PrepositionMorphologicalAnalyzer,
        PronounMorphologicalAnalyzer,
        AdjectiveMorphologicalAnalyzer,
        NounMorphologicalAnalyzer,
        VerbMorphologicalAnalyzer,
    ]

    def test_import(self):
        assert MorphologicalAnalyzer

    def test_initialize(self):
        assert MorphologicalAnalyzer(self.TEST_WORD)

    def test_default_analyzers(self):
        assert self.DEFAULT_ANALYZERS == MorphologicalAnalyzer.DEFAULT_ANALYZERS

    def test_default_analyzers_size(self):
        assert len(MorphologicalAnalyzer.DEFAULT_ANALYZERS) == 10

    def test_initialize_raw_word(self):
        analyzer = MorphologicalAnalyzer(self.TEST_WORD)

        assert analyzer.raw_word == self.TEST_WORD

    def test_initialize_results(self):
        analyzer = MorphologicalAnalyzer(self.TEST_WORD)

        assert analyzer.results is None

    def test_initialize_processed(self):
        analyzer = MorphologicalAnalyzer(self.TEST_WORD)

        assert analyzer.processed is False

    def test_process(self):
        analyzer = MorphologicalAnalyzer(self.TEST_WORD)

        assert analyzer.analyze()

    def test_process_cache(self):
        analyzer = MorphologicalAnalyzer(self.TEST_WORD)

        assert analyzer.analyze() == True
        assert analyzer.analyze() == None

    def test_process_processed_change(self):
        analyzer = MorphologicalAnalyzer(self.TEST_WORD)

        assert not analyzer.processed

        analyzer.analyze()

        assert analyzer.processed

    def test_process_results_change(self):
        analyzer = MorphologicalAnalyzer(self.TEST_WORD)

        assert analyzer.results is None

        analyzer.analyze()

        assert analyzer.results is not None

    def test_empty_analyzers(self):
        class MorphologicalEmptyAnalyzer(MorphologicalAnalyzer):
            DEFAULT_ANALYZERS = []

        analyzer = MorphologicalEmptyAnalyzer(self.TEST_WORD)

        assert analyzer.analyze()
        assert analyzer.results.result is None
        assert analyzer.processed is True

    def test_none_analyzers(self):
        class MorphologicalNoneAnalyzer(MorphologicalAnalyzer):
            DEFAULT_ANALYZERS = None

        analyzer = MorphologicalNoneAnalyzer(self.TEST_WORD)

        assert analyzer.analyze()
        assert analyzer.results.result is None
        assert analyzer.processed is True



class TestMorphologicalAnalyzerTypesBase():
    VALID_WORDS = {
        Adverb: dict(words=['almenaŭ', 'ambaŭ', 'multe', 'rapide'], analyzer=AdverbMorphologicalAnalyzer),
        Adjective: dict(words=['bela', 'belaj', 'belan', 'belajn'], analyzer=AdjectiveMorphologicalAnalyzer),
        Article: dict(words=['la'], analyzer=ArticleMorphologicalAnalyzer),
        Conjunction: dict(words=['kaj', 'tial', 'kiel', 'ĉar'], analyzer=ConjunctionMorphologicalAnalyzer),
        Interjection: dict(words=['Aĥ!', 'Ek!', 'Ĝis!', 'Volapukaĵo!'], analyzer=InterjectionMorphologicalAnalyzer),
        Noun: dict(words=['komputilo', 'komputilon', 'komputiloj', 'komputilojn'], analyzer=NounMorphologicalAnalyzer),
        Numeral: dict(words=['10', '-1', 'unu', 'ducent', 'tridek', 'okcent', 'mil', 'miliardo', 'milionoj'], analyzer=NumeralMorphologicalAnalyzer),
        Preposition: dict(words=['anstataŭ', 'apud', 'dum', 'pri', 'pro', 'sur', 'tiu', 'tiuj', 'tra', 'ĉe'], analyzer=PrepositionMorphologicalAnalyzer),
        Pronoun: dict(words=['mi', 'min', 'mia', 'mian', 'miajn', 'vi', 'viaj', 'kio', 'kiu', 'kies', 'ĉiu', 'io', 'iu', 'nenio'], analyzer=PronounMorphologicalAnalyzer),
        Verb: dict(words=['ami', 'amis', 'amas', 'amos', 'amu', 'amus'], analyzer=VerbMorphologicalAnalyzer)
    }

    def test_process(self):

        for klass in self.VALID_WORDS:
            for word in self.VALID_WORDS[klass]['words']:
                analyzer = MorphologicalAnalyzer(word)

                assert analyzer.analyze()

    def test_results(self):
        for klass in self.VALID_WORDS:
            for word in self.VALID_WORDS[klass]['words']:
                analyzer = MorphologicalAnalyzer(word)

                assert analyzer.analyze()
                assert isinstance(analyzer.results, AnalyzeResult)

    def test_result_word(self):
        for klass in self.VALID_WORDS:
            for word in self.VALID_WORDS[klass]['words']:
                analyzer = MorphologicalAnalyzer(word)

                assert analyzer.analyze()
                assert isinstance(analyzer.results.result.word, klass)

    def test_result_raw_word(self):
        for klass in self.VALID_WORDS:
            for word in self.VALID_WORDS[klass]['words']:
                analyzer = MorphologicalAnalyzer(word)

                assert analyzer.analyze()
                assert analyzer.results.result.raw_word == word


    def test_results_result_analyzer(self):
        for klass in self.VALID_WORDS:
            for word in self.VALID_WORDS[klass]['words']:
                analyzer = MorphologicalAnalyzer(word)

                assert analyzer.analyze()
                assert isinstance(analyzer.results.result, self.VALID_WORDS[klass]['analyzer'])


class TestMorphologicalAnalyzerAdverb():
    VALID_WORDS = ['almenaŭ', 'ambaŭ', 'multe', 'rapide']

    def test_adverbs_process(self):
        for word in self.VALID_WORDS:
            analyzer = MorphologicalAnalyzer(word)

            assert analyzer.analyze()

    def test_adverbs_results(self):
        for word in self.VALID_WORDS:
            analyzer = MorphologicalAnalyzer(word)

            assert analyzer.analyze()
            assert isinstance(analyzer.results, AnalyzeResult)

    def test_adverbs_results_result_is_analyzer(self):
        for word in self.VALID_WORDS:
            analyzer = MorphologicalAnalyzer(word)

            assert analyzer.analyze()
            assert isinstance(analyzer.results.result, AdverbMorphologicalAnalyzer)

    def test_adverbs_result_word(self):
        for word in self.VALID_WORDS:
            analyzer = MorphologicalAnalyzer(word)

            assert analyzer.analyze()
            assert isinstance(analyzer.results.result.word, Adverb)

    def test_adverbs_result_raw_word(self):
        for word in self.VALID_WORDS:
            analyzer = MorphologicalAnalyzer(word)

            assert analyzer.analyze()
            assert analyzer.results.result.raw_word == word

class TestMorphologicalAnalyzerAdjective():
    VALID_WORDS = ['bela', 'belaj', 'belan', 'belajn']

    def test_adjectives_process(self):
        for word in self.VALID_WORDS:
            analyzer = MorphologicalAnalyzer(word)

            assert analyzer.analyze()

    def test_adjectives_results(self):
        for word in self.VALID_WORDS:
            analyzer = MorphologicalAnalyzer(word)

            assert analyzer.analyze()
            assert isinstance(analyzer.results, AnalyzeResult)

    def test_adjectives_results_result_is_analyzer(self):
        for word in self.VALID_WORDS:
            analyzer = MorphologicalAnalyzer(word)

            assert analyzer.analyze()
            assert isinstance(analyzer.results.result, AdjectiveMorphologicalAnalyzer)

    def test_adjectives_result_word(self):
        for word in self.VALID_WORDS:
            analyzer = MorphologicalAnalyzer(word)

            assert analyzer.analyze()
            assert isinstance(analyzer.results.result.word, Adjective)

    def test_adjectives_result_raw_word(self):
        for word in self.VALID_WORDS:
            analyzer = MorphologicalAnalyzer(word)

            assert analyzer.analyze()
            assert analyzer.results.result.raw_word == word

class TestMorphologicalAnalyzerArticles():
    VALID_WORDS = ['la']

    def test_articles_process(self):
        for word in self.VALID_WORDS:
            analyzer = MorphologicalAnalyzer(word)

            assert analyzer.analyze()

    def test_articles_results(self):
        for word in self.VALID_WORDS:
            analyzer = MorphologicalAnalyzer(word)

            assert analyzer.analyze()
            assert isinstance(analyzer.results, AnalyzeResult)

    def test_articles_results_result_is_analyzer(self):
        for word in self.VALID_WORDS:
            analyzer = MorphologicalAnalyzer(word)

            assert analyzer.analyze()
            assert isinstance(analyzer.results.result, ArticleMorphologicalAnalyzer)

    def test_articles_result_word(self):
        for word in self.VALID_WORDS:
            analyzer = MorphologicalAnalyzer(word)

            assert analyzer.analyze()
            assert isinstance(analyzer.results.result.word, Article)

    def test_articles_result_raw_word(self):
        for word in self.VALID_WORDS:
            analyzer = MorphologicalAnalyzer(word)

            assert analyzer.analyze()
            assert analyzer.results.result.raw_word == word

class TestMorphologicalAnalyzerConjunctions():
    # VALID_WORDS = ['kvazaŭ', 'tial', 'kiel', 'ĉar']
    # TODO: 'kvazau' is also an adverb. We need to test this better
    VALID_WORDS = ['kaj', 'tial', 'kiel', 'ĉar']

    def test_conjunctions_process(self):
        for word in self.VALID_WORDS:
            analyzer = MorphologicalAnalyzer(word)

            assert analyzer.analyze()

    def test_conjunctions_results(self):
        for word in self.VALID_WORDS:
            analyzer = MorphologicalAnalyzer(word)

            assert analyzer.analyze()
            assert isinstance(analyzer.results, AnalyzeResult)

    def test_conjunctions_results_result_is_analyzer(self):
        for word in self.VALID_WORDS:
            analyzer = MorphologicalAnalyzer(word)

            assert analyzer.analyze()
            assert isinstance(analyzer.results.result, ConjunctionMorphologicalAnalyzer)

    def test_conjunctions_result_word(self):
        for word in self.VALID_WORDS:
            analyzer = MorphologicalAnalyzer(word)

            assert analyzer.analyze()
            assert isinstance(analyzer.results.result.word, Conjunction)

    def test_conjunctions_result_raw_word(self):
        for word in self.VALID_WORDS:
            analyzer = MorphologicalAnalyzer(word)

            assert analyzer.analyze()
            assert analyzer.results.result.raw_word == word

class TestMorphologicalAnalyzerInterjections():
    VALID_WORDS = ['Aĥ!', 'Ek!', 'Ĝis!', 'Volapukaĵo!']

    def test_interjections_process(self):
        for word in self.VALID_WORDS:
            analyzer = MorphologicalAnalyzer(word)

            assert analyzer.analyze()

    def test_interjections_results(self):
        for word in self.VALID_WORDS:
            analyzer = MorphologicalAnalyzer(word)

            assert analyzer.analyze()
            assert isinstance(analyzer.results, AnalyzeResult)

    def test_interjections_results_result_is_analyzer(self):
        for word in self.VALID_WORDS:
            analyzer = MorphologicalAnalyzer(word)

            assert analyzer.analyze()
            assert isinstance(analyzer.results.result, InterjectionMorphologicalAnalyzer)

    def test_interjections_result_word(self):
        for word in self.VALID_WORDS:
            analyzer = MorphologicalAnalyzer(word)

            assert analyzer.analyze()
            assert isinstance(analyzer.results.result.word, Interjection)

    def test_interjections_result_raw_word(self):
        for word in self.VALID_WORDS:
            analyzer = MorphologicalAnalyzer(word)

            assert analyzer.analyze()
            assert analyzer.results.result.raw_word == word

class TestMorphologicalAnalyzerNouns():
    VALID_WORDS = ['komputilo', 'komputilon', 'komputiloj', 'komputilojn']

    def test_nouns_process(self):
        for word in self.VALID_WORDS:
            analyzer = MorphologicalAnalyzer(word)

            assert analyzer.analyze()

    def test_nouns_results(self):
        for word in self.VALID_WORDS:
            analyzer = MorphologicalAnalyzer(word)

            assert analyzer.analyze()
            assert isinstance(analyzer.results, AnalyzeResult)

    def test_nouns_results_result_is_analyzer(self):
        for word in self.VALID_WORDS:
            analyzer = MorphologicalAnalyzer(word)

            assert analyzer.analyze()
            assert isinstance(analyzer.results.result, NounMorphologicalAnalyzer)

    def test_nouns_result_word(self):
        for word in self.VALID_WORDS:
            analyzer = MorphologicalAnalyzer(word)

            assert analyzer.analyze()
            assert isinstance(analyzer.results.result.word, Noun)

    def test_nouns_result_raw_word(self):
        for word in self.VALID_WORDS:
            analyzer = MorphologicalAnalyzer(word)

            assert analyzer.analyze()
            assert analyzer.results.result.raw_word == word

class TestMorphologicalAnalyzerNumerals():
    VALID_WORDS = ['10', '-1', 'unu', 'ducent', 'tridek', 'okcent', 'mil', 'miliardo', 'milionoj']

    def test_numerals_process(self):
        for word in self.VALID_WORDS:
            analyzer = MorphologicalAnalyzer(word)

            assert analyzer.analyze()

    def test_numerals_results(self):
        for word in self.VALID_WORDS:
            analyzer = MorphologicalAnalyzer(word)

            assert analyzer.analyze()
            assert isinstance(analyzer.results, AnalyzeResult)

    def test_numerals_results_result_is_analyzer(self):
        for word in self.VALID_WORDS:
            analyzer = MorphologicalAnalyzer(word)

            assert analyzer.analyze()
            assert isinstance(analyzer.results.result, NumeralMorphologicalAnalyzer)

    def test_numerals_result_word(self):
        for word in self.VALID_WORDS:
            analyzer = MorphologicalAnalyzer(word)

            assert analyzer.analyze()
            assert isinstance(analyzer.results.result.word, Numeral)

    def test_numerals_result_raw_word(self):
        for word in self.VALID_WORDS:
            analyzer = MorphologicalAnalyzer(word)

            assert analyzer.analyze()
            assert analyzer.results.result.raw_word == word

class TestMorphologicalAnalyzerPrepositions():
    # VALID_WORDS = ['anstataŭ', 'apud', 'dum', 'kiel', 'pri', 'pro', 'sur', 'tiu', 'tiuj', 'tra', 'ĉe']
    # TODO: 'kiel' is a conjunction as well, we need to test this better.
    VALID_WORDS = ['anstataŭ', 'apud', 'dum', 'pri', 'pro', 'sur', 'tiu', 'tiuj', 'tra', 'ĉe']

    def test_prepositions_process(self):
        for word in self.VALID_WORDS:
            analyzer = MorphologicalAnalyzer(word)

            assert analyzer.analyze()

    def test_prepositions_results(self):
        for word in self.VALID_WORDS:
            analyzer = MorphologicalAnalyzer(word)

            assert analyzer.analyze()
            assert isinstance(analyzer.results, AnalyzeResult)

    def test_prepositions_results_result_is_analyzer(self):
        for word in self.VALID_WORDS:
            analyzer = MorphologicalAnalyzer(word)

            assert analyzer.analyze()
            assert isinstance(analyzer.results.result, PrepositionMorphologicalAnalyzer)

    def test_prepositions_result_word(self):
        for word in self.VALID_WORDS:
            analyzer = MorphologicalAnalyzer(word)

            assert analyzer.analyze()
            assert isinstance(analyzer.results.result.word, Preposition)

    def test_prepositions_result_raw_word(self):
        for word in self.VALID_WORDS:
            analyzer = MorphologicalAnalyzer(word)

            assert analyzer.analyze()
            assert analyzer.results.result.raw_word == word


class TestMorphologicalAnalyzerPronouns():
    VALID_WORDS = ['mi', 'min', 'mia', 'mian', 'miajn', 'vi', 'viaj', 'kio', 'kiu', 'kies', 'ĉiu', 'io', 'iu', 'nenio']

    def test_pronouns_process(self):
        for word in self.VALID_WORDS:
            analyzer = MorphologicalAnalyzer(word)

            assert analyzer.analyze()

    def test_pronouns_results(self):
        for word in self.VALID_WORDS:
            analyzer = MorphologicalAnalyzer(word)

            assert analyzer.analyze()
            assert isinstance(analyzer.results, AnalyzeResult)

    def test_pronouns_results_result_is_analyzer(self):
        for word in self.VALID_WORDS:
            analyzer = MorphologicalAnalyzer(word)

            assert analyzer.analyze()
            assert isinstance(analyzer.results.result, PronounMorphologicalAnalyzer)

    def test_pronouns_result_word(self):
        for word in self.VALID_WORDS:
            analyzer = MorphologicalAnalyzer(word)

            assert analyzer.analyze()
            assert isinstance(analyzer.results.result.word, Pronoun)

    def test_pronouns_result_raw_word(self):
        for word in self.VALID_WORDS:
            analyzer = MorphologicalAnalyzer(word)

            assert analyzer.analyze()
            assert analyzer.results.result.raw_word == word


class TestMorphologicalAnalyzerVerbs():
    VALID_WORDS = ['ami', 'amis', 'amas', 'amos', 'amu', 'amus']

    def test_verbs_process(self):
        for word in self.VALID_WORDS:
            analyzer = MorphologicalAnalyzer(word)

            assert analyzer.analyze()

    def test_verbs_results(self):
        for word in self.VALID_WORDS:
            analyzer = MorphologicalAnalyzer(word)

            assert analyzer.analyze()
            assert isinstance(analyzer.results, AnalyzeResult)

    def test_verbs_results_result_is_analyzer(self):
        for word in self.VALID_WORDS:
            analyzer = MorphologicalAnalyzer(word)

            assert analyzer.analyze()
            assert isinstance(analyzer.results.result, VerbMorphologicalAnalyzer)

    def test_verbs_result_word(self):
        for word in self.VALID_WORDS:
            analyzer = MorphologicalAnalyzer(word)

            assert analyzer.analyze()
            assert isinstance(analyzer.results.result.word, Verb)

    def test_verbs_result_raw_word(self):
        for word in self.VALID_WORDS:
            analyzer = MorphologicalAnalyzer(word)

            assert analyzer.analyze()
            assert analyzer.results.result.raw_word == word
