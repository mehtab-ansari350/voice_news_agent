"""
Improved retrieval layer.
"""

import re

from memory.database import (
    get_all_articles,
)

STOP_WORDS = {
    "what",
    "why",
    "when",
    "where",
    "who",
    "did",
    "does",
    "is",
    "are",
    "the",
    "a",
    "an",
    "tell",
    "about",
    "me",
    "please",
    "can",
    "you",
    "next",
    "happened",
}


def clean_words(text):

    words = re.findall(
        r"\b[a-zA-Z]+\b",
        text.lower(),
    )

    return {
        word
        for word in words
        if word not in STOP_WORDS
    }


def retrieve_relevant_articles(
    question: str,
    top_k: int = 3,
):

    articles = get_all_articles()

    question_words = clean_words(
        question
    )

    scored_articles = []

    for article in articles:

        searchable_text = (
            article["title"]
            + " "
            + article["summary"]
        ).lower()

        article_words = clean_words(
            searchable_text
        )

        score = len(
            question_words.intersection(
                article_words
            )
        )

        scored_articles.append(
            (
                score,
                article,
            )
        )

    scored_articles.sort(
        key=lambda x: x[0],
        reverse=True,
    )

    return [
        article
        for score, article in scored_articles[:top_k]
        if score > 0
    ]