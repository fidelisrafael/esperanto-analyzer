"""
This class represent one word beloging to grammar class classified as 'Article'

What's an Article?
===
An article is a word used to modify a noun, which is a person, place, object, or idea.
Technically, an article is an **adjective**, which is any word that modifies a noun.

TODO: Should Article inherits from `Adjective`?
"""

from .word import Word

# pylint: disable=too-few-public-methods,missing-docstring
class Article(Word):
    # All the articles existents in Esperanto, just the definite article: 'la'
    # This article is invariable.
    # eg:
    #  "La suno brilas" -> "The sun shines"   [Singular]
    #  "La homoj kuiras" -> "The people cook" [Plural]
    VALID_ARTICLES = ['la']

    def has_plural(self):
        """
        Articles are ALWAYS written as: "la" but they can be in plural
        """
        return True


    def _match_plural(self, context=None):
        """
        Depending of the `context` the meaning of the article "la" can change, eg:

        "la suno" =>  # Singular
        "la homoj" => # Plurar

        So if this method receives `context`(which is basically a string), it can
        foreseen if the article is in singular or plural, eg:

        > Article('la')._match_plural(None)     # => False
        > Article('la')._match_plural('domo')   # => False
        > Article('la')._match_plural('domoj')  # => True
        """
        if context:
            return Word(context).plural

        return False

    def _validate_content(self, content):
        Word._validate_content(self, content)


        # Since Esperanto ONLY HAS 1 article("la"), we make sure to validate if the current
        # instance is really representing one valid Esperanto article.
        if not content.lower() in self.VALID_ARTICLES:
            raise InvalidArticleError


class InvalidArticleError(Exception):
    """
    This Exception is raised when Article is created with invalid content.
    Eg: Article('lo') # raise InvalidArticleError
    """
    pass
