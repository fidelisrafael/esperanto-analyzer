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
        self.matches = None
        self.processed = False

    def match(self):
        return self.MATCH_REGEXP.match(self.raw_word)

    def analyze(self):
        if self.processed is True:
            return None

        matches = self.match()

        # Set as the first time runned
        self.processed = True

        if matches:
            self.word = self.word_class()(self.raw_word)
            self.matches = matches

            return True

        return False

    @staticmethod
    def word_class():
        raise NotImplementedError
