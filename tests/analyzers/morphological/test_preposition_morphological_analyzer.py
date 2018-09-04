# pylint: disable=missing-docstring,no-self-use

import re
import pytest

from context import esperanto_analyzer

from esperanto_analyzer.speech import Preposition
from esperanto_analyzer.analyzers.morphological import PrepositionMorphologicalAnalyzer

class TestPrepositionMorphologicalAnalyzerBasic():
    TEST_WORD = 'anstataŭ'

    def test_import(self):
        assert PrepositionMorphologicalAnalyzer

    def test_initialize_default_options(self):
        analyzer = PrepositionMorphologicalAnalyzer(self.TEST_WORD)

        assert analyzer.options == dict()

    def test_initialize_overwrite_options(self):
        analyzer = PrepositionMorphologicalAnalyzer(self.TEST_WORD, dict(option='ok'))

        assert analyzer.options == dict(option='ok')

    def test_initialize_raw_word(self):
        analyzer = PrepositionMorphologicalAnalyzer(self.TEST_WORD)

        assert analyzer.raw_word == self.TEST_WORD

    def test_initialize_word(self):
        analyzer = PrepositionMorphologicalAnalyzer(self.TEST_WORD)

        # analyzer.word is only populated after calling `analyze()` method
        assert analyzer.word is None

    def test_initialize_matches(self):
        analyzer = PrepositionMorphologicalAnalyzer(self.TEST_WORD)

        # analyzer.matches is only populated after calling `analyze()` method
        assert analyzer.matches is None

    def test_initialize_processed(self):
        analyzer = PrepositionMorphologicalAnalyzer(self.TEST_WORD)

        # analyzer.matches is only populated after calling `analyze()` method
        assert analyzer.processed is False

    def test_match_regexp(self):
        assert PrepositionMorphologicalAnalyzer.MATCH_REGEXP is not None

    def test_word_class(self):
        assert isinstance(PrepositionMorphologicalAnalyzer.word_class()(self.TEST_WORD), Preposition)

class TestPrepositionMorphologicalAnalyzerMatchMethod():
    VALID_WORDS = ['K', 'al', 'anstataŭ', 'antaŭ', 'antaŭ ol', 'apud', 'da', 'de', 'disde',
                   'du vortoj', 'dum', 'ekde', 'ekster', 'eksteren', 'el', 'en', 'ene',
                   'estiel', 'far', 'fare de', 'flanke de', 'for de', 'graŭ', 'inter', 'je',
                   'kaj ankaŭ', 'kiel', 'kontraŭ', 'kontraŭe de', 'krom', 'kun', 'laŭ',
                   'mala', 'malantaŭ', 'malgraŭ', 'malkiel', 'malsupre de', 'malsupren',
                   'meze de', 'na', 'nome de', 'ol', 'per', 'pere de', 'plus', 'po', 'por',
                   'post', 'preter', 'pri', 'pro', 'proksime de', 'samkiel', 'sed', 'sekva',
                   'sen', 'sub', 'suben', 'super', 'supren', 'sur', 'tiu', 'tiuj', 'tra',
                   'trans', 'tri vortoj', 'tuj post', 'tutĉirkaŭ',
                   'ĉe', 'ĉi tiu', 'ĉi tiuj', 'ĉirkaŭ', 'ĝis'
                   ]

    INVALID_WORDS = ['io', 'bela', 'domo', 'hundoj', 'kiu', 'vi', 'multe', 'ankoraŭ', 'dek',
                     'du', 'ĉar', 'aŭ', '?', '!']

    def test_match(self):
        for word in self.VALID_WORDS:
            analyzer = PrepositionMorphologicalAnalyzer(word)
            matches = analyzer.match()

            assert matches is not None
            assert len(matches.span()) == 2

    def test_match_empty(self):
        for word in self.INVALID_WORDS:
            analyzer = PrepositionMorphologicalAnalyzer(word)
            matches = analyzer.match()

            assert matches is None

class TestPrepositionMorphologicalAnalyzerAnalyzeMethod():
    VALID_WORDS = ['K', 'al', 'anstataŭ', 'antaŭ', 'antaŭ ol', 'apud', 'da', 'de', 'disde',
                   'du vortoj', 'dum', 'ekde', 'ekster', 'eksteren', 'el', 'en', 'ene',
                   'estiel', 'far', 'fare de', 'flanke de', 'for de', 'graŭ', 'inter', 'je',
                   'kaj ankaŭ', 'kiel', 'kontraŭ', 'kontraŭe de', 'krom', 'kun', 'laŭ',
                   'mala', 'malantaŭ', 'malgraŭ', 'malkiel', 'malsupre de', 'malsupren',
                   'meze de', 'na', 'nome de', 'ol', 'per', 'pere de', 'plus', 'po', 'por',
                   'post', 'preter', 'pri', 'pro', 'proksime de', 'samkiel', 'sed', 'sekva',
                   'sen', 'sub', 'suben', 'super', 'supren', 'sur', 'tiu', 'tiuj', 'tra',
                   'trans', 'tri vortoj', 'tuj post', 'tutĉirkaŭ',
                   'ĉe', 'ĉi tiu', 'ĉi tiuj', 'ĉirkaŭ', 'ĝis',
                   ]

    INVALID_WORDS = ['io', 'bela', 'domo', 'hundoj', 'kiu', 'vi', 'multe', 'ankoraŭ', 'dek',
                     'du', 'ĉar', 'aŭ', '?', '!']

    def test_invalid_analyze(self):
        for word in self.INVALID_WORDS:
            analyzer = PrepositionMorphologicalAnalyzer(word)
            result = analyzer.analyze()

            assert not result

    def test_invalid_analyze_word(self):
        for word in self.INVALID_WORDS:
            analyzer = PrepositionMorphologicalAnalyzer(word)
            analyzer.analyze()

            assert analyzer.word is None

    def test_invalid_analyze_match(self):
        for word in self.INVALID_WORDS:
            analyzer = PrepositionMorphologicalAnalyzer(word)
            analyzer.analyze()

            assert analyzer.matches is None

    def test_analyze(self):
        for word in self.VALID_WORDS:
            analyzer = PrepositionMorphologicalAnalyzer(word)

            assert analyzer.analyze()

    def test_prepositions_list(self):
        for word in PrepositionMorphologicalAnalyzer.PREPOSITIONS_LIST:
            analyzer = PrepositionMorphologicalAnalyzer(word)

            assert analyzer.analyze()

    def test_analyze_word(self):
        for word in self.VALID_WORDS:
            analyzer = PrepositionMorphologicalAnalyzer(word)
            analyzer.analyze()

            assert isinstance(analyzer.word, Preposition)
            assert analyzer.word.content == word

    def test_analyze_match(self):
        for word in self.VALID_WORDS:
            analyzer = PrepositionMorphologicalAnalyzer(word)
            analyzer.analyze()

            assert analyzer.matches is not None

    def test_analyze_return_false(self):
        for word in self.INVALID_WORDS:
            analyzer = PrepositionMorphologicalAnalyzer(word)

            assert analyzer.analyze() is False

    def test_analyze_return_true(self):
        for word in self.VALID_WORDS:
            analyzer = PrepositionMorphologicalAnalyzer(word)

            assert analyzer.analyze()


    def test_analyze_processed(self):
        for word in self.VALID_WORDS:
            analyzer = PrepositionMorphologicalAnalyzer(word)

            assert analyzer.processed is False

            analyzer.analyze()

            assert analyzer.processed is True

    def test_analyze_processed_response(self):
        for word in self.VALID_WORDS:
            analyzer = PrepositionMorphologicalAnalyzer(word)
            analyzer.analyze()

            assert analyzer.analyze() is None
            assert analyzer.analyze() is None

class TestPrepositionMorphologicalAnalyzerPrepositionsList:
    PREPOSITIONS_LIST = ['K', 'al', 'anstataŭ', 'antaŭ', 'antaŭ ol', 'apud', 'da', 'de', 'disde',
                         'du vortoj', 'dum', 'ekde', 'ekster', 'eksteren', 'el', 'en', 'ene',
                         'estiel', 'far', 'fare de', 'flanke de', 'for de', 'graŭ', 'inter', 'je',
                         'kaj ankaŭ', 'kiel', 'kontraŭ', 'kontraŭe de', 'krom', 'kun', 'laŭ',
                         'mala', 'malantaŭ', 'malgraŭ', 'malkiel', 'malsupre de', 'malsupren',
                         'meze de', 'na', 'nome de', 'ol', 'per', 'pere de', 'plus', 'po', 'por',
                         'post', 'preter', 'pri', 'pro', 'proksime de', 'samkiel', 'sed', 'sekva',
                         'sen', 'sub', 'suben', 'super', 'supren', 'sur', 'tiu', 'tiuj', 'tra',
                         'trans', 'tri vortoj', 'tuj post', 'tutĉirkaŭ',
                         'ĉe', 'ĉi tiu', 'ĉi tiuj', 'ĉirkaŭ', 'ĝis']

    def test_preposition_list_not_changed(self):
        assert PrepositionMorphologicalAnalyzer.PREPOSITIONS_LIST == self.PREPOSITIONS_LIST

    def test_prepositions_not_empty(self):
        assert PrepositionMorphologicalAnalyzer.PREPOSITIONS_LIST is not None

    def test_prepositions_not_size(self):
        assert len(PrepositionMorphologicalAnalyzer.PREPOSITIONS_LIST) == 73

    def test_prepositions_match_list(self):
        for word in PrepositionMorphologicalAnalyzer.PREPOSITIONS_LIST:
            assert PrepositionMorphologicalAnalyzer.PROPOSITIONS_MATCH_REGEXP.match(word)

    def test_prepositions_match_final_regexp_list(self):
        for word in PrepositionMorphologicalAnalyzer.PREPOSITIONS_LIST:
            assert PrepositionMorphologicalAnalyzer.MATCH_REGEXP.match(word)
