# pylint: disable=missing-docstring
import sys
import tableprint

from esperanto_analyzer import MorphologicalSentenceAnalyzer

class AnalyzerNotProcessedError(BaseException):
    pass

class CLI():
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

    OUTPUT_TABLE_HEADERS = ['Word', 'Part of Speech']

    @staticmethod
    def run(input_sentence=None, output=sys.stdout):
        analyzer = MorphologicalSentenceAnalyzer(input_sentence)
        analyzer.analyze()

        CLI.display_output_for_analyzer(analyzer, output=output)

    @staticmethod
    def display_output_for_analyzer(analyzer, output=sys.stdout):
        if analyzer.processed is False:
            raise AnalyzerNotProcessedError('Analyzer must be processed before output display. You must call `analyze()` in your instance')

        CLI.print_results(analyzer.simple_results(), output=output)

    @staticmethod
    def format_table_data(results, colorize=True):
        out_data = []

        format_color = lambda string, cname: ('\x1b[%sm%s \x1b[0m') % (CLI.COLORS[cname], string)

        for result in results:
            out_data.append([
                format_color(result[0], result[1]) if colorize else result[0],
                format_color(result[1], result[1]) if colorize else result[1]
            ])

        return out_data

    @staticmethod
    def print_results(results, width=15, output=sys.stdout):
        table_data = CLI.format_table_data(results)

        return tableprint.table(table_data, CLI.OUTPUT_TABLE_HEADERS, width=width, out=output)
