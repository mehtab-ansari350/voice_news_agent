"""
Process the latest news articles.

Responsibilities:
- Fetch latest news headlines
- Extract article content
- Generate AI summaries
- Save articles to the database
"""

from news.fetch_news import get_latest_news
from news.extract_article import extract_article
from models.llm import summarize_article

from memory.database import (
    initialize_database,
    save_article,
)


def process_news(limit: int = 5) -> list[dict]:
    """
    Fetch, extract, summarize, and store news articles.

    Args:
        limit: Number of articles to process.

    Returns:
        List of processed article dictionaries.
    """

    processed_articles: list[dict] = []

    news_items = get_latest_news(limit=limit)

    if not news_items:
        print("No news articles found.")
        return processed_articles

    for index, news_item in enumerate(news_items, start=1):

        print(f"\n[{index}/{len(news_items)}] Processing article...")
        print(f"Title: {news_item['title']}")

        article_data = extract_article(news_item["link"])

        if not article_data:
            print("Failed to extract article.")
            continue

        article_text = article_data["text"]

        if not article_text.strip():
            print("Article text is empty.")
            continue

        # Limit article size to reduce LLM inference time
        article_text = article_text[:10000]

        try:
            summary = summarize_article(article_text)

        except Exception as error:
            print(f"Summary generation failed: {error}")
            continue

        save_article(
            title=news_item["title"],
            link=news_item["link"],
            article=article_text,
            summary=summary,
        )

        print("Article saved successfully.")

        processed_articles.append(
            {
                "title": news_item["title"],
                "link": news_item["link"],
                "article": article_text,
                "summary": summary,
            }
        )

    return processed_articles


def main() -> None:
    """
    Execute the news processing workflow.
    """

    initialize_database()

    processed_news = process_news(limit=5)

    print("\n" + "=" * 100)
    print("PROCESSED NEWS")
    print("=" * 100)

    for index, article in enumerate(processed_news, start=1):

        print(f"\nNEWS {index}")
        print("-" * 100)

        print(f"TITLE:\n{article['title']}\n")

        print("SUMMARY:")
        print(article["summary"])

        print("\nLINK:")
        print(article["link"])

        print()


if __name__ == "__main__":
    main()