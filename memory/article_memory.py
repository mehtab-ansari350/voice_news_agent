"""
Stores currently selected article.
"""

current_article = None


def set_current_article(article):
    """
    Save selected article.
    """
    global current_article

    current_article = article


def get_current_article():
    """
    Retrieve current article.
    """
    return current_article