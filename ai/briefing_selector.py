"""
Select article from briefing references.
"""

from memory.database import (
    get_all_articles,
)


NUMBER_WORDS = {
    "first": 1,
    "one": 1,

    "second": 2,
    "two": 2,

    "third": 3,
    "three": 3,

    "fourth": 4,
    "four": 4,

    "fifth": 5,
    "five": 5,

    "sixth": 6,
    "six": 6,

    "seventh": 7,
    "seven": 7,

    "eighth": 8,
    "eight": 8,

    "ninth": 9,
    "nine": 9,

    "tenth": 10,
    "ten": 10,
}


def get_article_from_reference(
    user_input: str,
):
    """
    Detect article references.

    Examples:
    - first article
    - article 2
    - second one
    - fifth one
    - last article
    """

    articles = get_all_articles()

    if not articles:
        return None

    text = user_input.lower()

    # Handle "last article"
    if "last" in text:
        return articles[len(articles)-1]

    # Handle words
    for word, index in NUMBER_WORDS.items():

        if word in text:

            if index <= len(articles):
                return articles[index - 1]

    # Handle digits
    for number in range(
        1,
        len(articles) + 1,
    ):

        if str(number) in text:
            return articles[number - 1]

    # Title matching
    for article in articles:

        title = article["title"].lower()

        title_words = title.split()

        for word in title_words:

            if len(word) > 4 and word in text:
                return article

    return None