"""
Simple retrieval layer for selecting relevant news articles.
"""

from memory.database import get_all_articles


def retrieve_relevant_articles(
    question: str,
    top_k: int = 3,
) -> list[dict]:
    """
    Retrieve the most relevant articles based on keyword overlap.
    """

    articles = get_all_articles()

    question_words = {
        word.lower()
        for word in question.split()
    }

    scored_articles = []

    for article in articles:

        searchable_text = (
            article["title"]
            + " "
            + article["summary"]
        ).lower()

        score = sum(
            1
            for word in question_words
            if word in searchable_text
        )

        scored_articles.append(
            (
                score,
                article,
            )
        )

    scored_articles.sort(
        key=lambda item: item[0],
        reverse=True,
    )

    return [
        article
        for score, article in scored_articles[:top_k]
        if score > 0
    ]