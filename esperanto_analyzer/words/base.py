"""
This class represent the smallest unit with pratical meaning of one language. The function
of one word is to describe parts of humans thoughts, so its one unit of human language.

What's an Word?
===

A unit of language, consisting of one or more spoken sounds or their written representation,
that functions as a principal carrier of meaning.

Words are composed of one or more morphemes and are either the smallest units susceptible of
independent use or consist of two or three such units combined under certain linking conditions,
as with the loss of primary accent that distinguishes black·bird· from black· bird·.

Words are usually separated by spaces in writing, and are distinguished phonologically,
as by accent, in many languages.

Technically one word is one set of "Letters"
"""

import re

# pylint: disable=too-few-public-methods,missing-docstring
class Word:
    # Only words with at least 4 characteres(This exclude words such as "ajn" and "kaj") that
    # finish with "j", or "jn" are in plural.
    PLURAL_DETECT_REGEXP = re.compile('.{2,}([^n]j|jn)$', re.IGNORECASE|re.UNICODE)

    def __init__(self, content, context=None):
        self._validate_content(content)

        self.content = content
        self.context = context
        self.metadata = dict()
        self.plural = (self._match_plural(context) not in [False, None])

    def _match_plural(self, _context=None):
        """
        This method determine if one word is in it's plural form.
        Some context can be send to help to determine if some word is in plural or not.
        """

        # Some words dont have plural (such as 'Adverb')
        if not self.has_plural():
            return None

        return self.PLURAL_DETECT_REGEXP.match(self.content)


    def has_plural(self): # pylint: disable=no-self-use
        """
        This method determines if one words has the capibility of being in the plural.
        This method should be override for subclasses(eg: Adverb)
        """
        return True

    def _validate_content(self, content): # pylint: disable=no-self-use
        if not content:
            raise NotContentError

class NotContentError(Exception):
    """
    This Exception is raised when one Word is created with empty content.
    Eg: Word('') # raise InvalidArticleError
    """
    pass
