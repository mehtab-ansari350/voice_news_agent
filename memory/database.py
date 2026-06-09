"""
Database layer for the Voice News Agent.

Responsible for:
- Database initialization
- Saving articles
- Retrieving articles
"""

from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Any


DATABASE_PATH = Path("voice_news_agent.db")


def get_connection() -> sqlite3.Connection:
    """
    Create and return a database connection.

    Returns:
        sqlite3.Connection
    """
    return sqlite3.connect(DATABASE_PATH)


def initialize_database() -> None:
    """
    Create required tables if they do not already exist.
    """

    query = """
    CREATE TABLE IF NOT EXISTS news_articles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        link TEXT UNIQUE NOT NULL,
        article TEXT NOT NULL,
        summary TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """

    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()


def save_article(
    title: str,
    link: str,
    article: str,
    summary: str,
) -> None:
    """
    Save a processed article.

    Args:
        title: News title.
        link: Original article URL.
        article: Full article content.
        summary: AI generated summary.
    """

    query = """
    INSERT OR IGNORE INTO news_articles (
        title,
        link,
        article,
        summary
    )
    VALUES (?, ?, ?, ?)
    """

    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(
            query,
            (
                title,
                link,
                article,
                summary,
            ),
        )
        connection.commit()


def get_all_articles() -> list[dict[str, Any]]:
    """
    Retrieve all stored articles.

    Returns:
        List of article dictionaries.
    """

    query = """
    SELECT
        id,
        title,
        link,
        article,
        summary,
        created_at
    FROM news_articles
    ORDER BY created_at DESC
    """

    with get_connection() as connection:
        connection.row_factory = sqlite3.Row

        cursor = connection.cursor()
        cursor.execute(query)

        rows = cursor.fetchall()

        return [dict(row) for row in rows]


if __name__ == "__main__":

    initialize_database()

    print("Database initialized successfully.")