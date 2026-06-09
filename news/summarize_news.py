from news.fetch_news import get_latest_news
from news.extract_article import extract_article
from models.llm import summarize_article


def main() -> None:
    """
    Execute the end-to-end news summarization workflow.
    """

    news_items = get_latest_news(limit=1)

    if not news_items:
        print("No news articles found.")
        return

    selected_news = news_items[0]

    print("\n" + "=" * 80)
    print("LATEST NEWS")
    print("=" * 80)
    print(f"Title: {selected_news['title']}")
    print(f"Link : {selected_news['link']}")

    article_data = extract_article(selected_news["link"])

    if not article_data:
        print("Failed to extract article content.")
        return

    article_text = article_data["text"]

    if not article_text.strip():
        print("Article content is empty.")
        return

    # Prevent extremely large prompts from slowing inference
    article_text = article_text[:10000]

    print("\nGenerating summary...\n")

    summary = summarize_article(article_text)

    print("=" * 80)
    print("AI SUMMARY")
    print("=" * 80)
    print(summary)


if __name__ == "__main__":
    main()