from memory.database import get_all_articles
from models.llm import answer_question


def build_news_context() -> str:
    """
    Build a context string from stored news articles.
    """

    articles = get_all_articles()

    context_parts = []

    for article in articles:

        context_parts.append(
            f"""
TITLE:
{article['title']}

SUMMARY:
{article['summary']}
"""
        )

    return "\n\n".join(context_parts)


def main() -> None:

    context = build_news_context()

    print("=" * 80)
    print("NEWS QA SYSTEM")
    print("=" * 80)

    while True:

        question = input("\nAsk a question (type 'exit' to quit): ")

        if question.lower() == "exit":
            break

        answer = answer_question(
            context=context,
            question=question,
        )

        print("\nANSWER:")
        print(answer)


if __name__ == "__main__":
    main()