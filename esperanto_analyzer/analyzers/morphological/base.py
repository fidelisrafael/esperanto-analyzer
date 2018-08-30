# pylint: disable=missing-docstring
class BaseMorphologicalAnalyzer:
    def __init__(self, options=None):
        # Python dicts() as default argument is not a great idea since Python don't
        # creates a new version of the default argument in every method call
        if options is None:
            options = dict()

        self.options = options
        self.raw_word = None
        self.word = None
        self.matches = dict()

    def analyze(self, word):
        matches = self.match(word)

        if matches:
            self.raw_word = word
            self.matches = matches
            self.word = self.word_class(word)

            return True

        return False

    def match(self, word):
        raise NotImplementedError

    def word_class(self, word):
        raise NotImplementedError
