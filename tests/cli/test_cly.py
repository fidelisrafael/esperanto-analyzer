# pylint: disable=missing-docstring,no-self-use

import pytest
from io import StringIO

from context import esperanto_analyzer

from esperanto_analyzer import MorphologicalSentenceAnalyzer
from esperanto_analyzer.cli.cli import CLI, AnalyzerNotProcessedError

class TestCLIBasic():
    TEST_SENTENCE = 'Mi loĝas en Brazilo'
    EXPECT_OUTPUT_TEST_SENTENCE = '╭─────────────────┬─────────────────╮\n│      Word       │ Part of Speech  │\n├─────────────────┼─────────────────┤\n│             \x1b[96mMi \x1b[0m │        \x1b[96mPronoun \x1b[0m │\n│          \x1b[31mloĝas \x1b[0m │           \x1b[31mVerb \x1b[0m │\n│             \x1b[36men \x1b[0m │    \x1b[36mPreposition \x1b[0m │\n│        \x1b[34mBrazilo \x1b[0m │           \x1b[34mNoun \x1b[0m │\n╰─────────────────┴─────────────────╯\n'

    COLORS = {
        'Adjective': 92,    # Light Green
        'Adverb': 32,       # Green
        'Article': 33,      # Yellow
        'Conjunction': 35,  # Magenta
        'Interjection': 95, # Light Magenta
        'Noun': 34,         # Blue
        'Numeral': 93,      # Light Yellow
        'Preposition': 36,  # Cian
        'Pronoun': 96,      # Light Cian
        'Verb': 31,         # Red
        'Undefined': 30     # Black
    }

    def test_import(self):
        assert CLI

    def test_colors(self):
        assert CLI.COLORS == self.COLORS

    def test_output_table_headers(self):
        assert CLI.OUTPUT_TABLE_HEADERS == ['Word', 'Part of Speech']

    def test_display_output_for_analyzer_without_executing(self):
        analyzer = MorphologicalSentenceAnalyzer(self.TEST_SENTENCE)

        with pytest.raises(AnalyzerNotProcessedError):
            CLI.display_output_for_analyzer(analyzer)

    def test_print_results(self):
        analyzer = MorphologicalSentenceAnalyzer(self.TEST_SENTENCE)
        analyzer.analyze()

        output = StringIO()

        # Execute the method that will write to `output`
        CLI.print_results(analyzer.simple_results(), output=output)

        assert output.getvalue() == self.EXPECT_OUTPUT_TEST_SENTENCE

    def test_run(self):
        output = StringIO()
        CLI.run(self.TEST_SENTENCE, output)

        assert output.getvalue() == self.EXPECT_OUTPUT_TEST_SENTENCE

    def test_format_table_data_with_formating(self):
        analyzer = MorphologicalSentenceAnalyzer(self.TEST_SENTENCE)
        analyzer.analyze()

        expected = [
            ['\x1b[96mMi \x1b[0m', '\x1b[96mPronoun \x1b[0m'],
            ['\x1b[31mloĝas \x1b[0m', '\x1b[31mVerb \x1b[0m'],
            ['\x1b[36men \x1b[0m', '\x1b[36mPreposition \x1b[0m'],
            ['\x1b[34mBrazilo \x1b[0m', '\x1b[34mNoun \x1b[0m']
        ]

        assert CLI.format_table_data(analyzer.simple_results()) == expected

    def test_format_table_data_without_formating(self):
        analyzer = MorphologicalSentenceAnalyzer(self.TEST_SENTENCE)
        analyzer.analyze()

        expected = [
            ['Mi', 'Pronoun'],
            ['loĝas', 'Verb'],
            ['en', 'Preposition'],
            ['Brazilo', 'Noun']
        ]

        assert CLI.format_table_data(analyzer.simple_results(), colorize=False) == expected

