"""
Stores the latest news briefing.
"""

latest_briefing = []


def save_briefing(articles):
    """
    Save latest briefing articles.
    """

    global latest_briefing

    latest_briefing = articles


def get_briefing():
    """
    Return latest briefing articles.
    """

    return latest_briefing