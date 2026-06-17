"""
Stores currently selected article.
"""

current_article = None


def set_current_article(article):

    global current_article

    current_article = article


def get_current_article():

    return current_article


def clear_current_article():

    global current_article

    current_article = None