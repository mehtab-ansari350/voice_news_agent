"""
News Question Answering System.

Responsibilities:
- Receive user questions
- Retrieve relevant news articles
- Build context
- Generate answers using Llama
"""

from ai.retriever import retrieve_relevant_articles
from models.llm import answer_question


def build_news_context(question: str) -> str:
    """
    Build context using only relevant articles.

    Args:
        question: User question.

    Returns:
        Context string.
    """

    articles = retrieve_relevant_articles(
        question=question,
        top_k=3,
    )

    if not articles:
        return ""

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
    """
    Start the news QA system.
    """

    print("=" * 80)
    print("NEWS QA SYSTEM")
    print("=" * 80)

    while True:

        question = input(
            "\nAsk a question (type 'exit' to quit): "
        ).strip()

        if question.lower() == "exit":
            break

        context = build_news_context(question)

        if not context:
            print(
                "\nI could not find any relevant news article."
            )
            continue

        try:

            answer = answer_question(
                context=context,
                question=question,
            )

            print("\nANSWER:")
            print(answer)

        except Exception as error:

            print(
                f"\nFailed to generate answer: {error}"
            )


if __name__ == "__main__":
    main()