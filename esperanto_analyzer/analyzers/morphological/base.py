# pylint: disable=missing-docstring
class BaseMorphologicalAnalyzer:
    # OVERWRITING THIS PROPERTY IS REQUIRED FOR ALL SUBCLASSES
    MATCH_REGEXP = None

    def __init__(self, raw_word, options=None):
        # Python dicts() as default argument is not a great idea since Python don't
        # creates a new version of the default argument in every method call
        if options is None:
            options = dict()

        self.options = options
        self.raw_word = raw_word
        self.word = None
        self.matches = dict()

    def analyze(self):
        matches = self.match()

        if matches:
            self.matches = matches
            self.word = self.word_class()(self.raw_word)

            return True

        return False

    def match(self):
        return self.MATCH_REGEXP.match(self.raw_word)

    def word_class(self):
        raise NotImplementedError
