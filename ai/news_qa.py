"""
News Question Answering System.

Responsibilities:
- Receive user questions
- Retrieve relevant news articles
- Build news context
- Build conversation context
- Generate answers using Llama
- Save conversation history
"""

from ai.retriever import retrieve_relevant_articles

from models.llm import answer_question

from memory.database import (
    get_recent_conversations,
    save_conversation,
)


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


def build_conversation_context() -> str:
    """
    Build conversation context from SQLite history.

    Returns:
        Formatted conversation history.
    """

    conversations = get_recent_conversations(
        limit=5
    )

    if not conversations:
        return ""

    parts = []

    # Oldest -> Newest
    for conversation in reversed(conversations):

        parts.append(
            f"""
USER:
{conversation['question']}

ASSISTANT:
{conversation['answer']}
"""
        )

    return "\n".join(parts)


def main() -> None:
    """
    Start the News QA System.
    """

    print("=" * 80)
    print("NEWS QA SYSTEM")
    print("=" * 80)

    while True:

        question = input(
            "\nAsk a question (type 'exit' to quit): "
        ).strip()

        if question.lower() == "exit":
            print("\nGoodbye!")
            break

        news_context = build_news_context(
            question=question
        )

        if not news_context:

            print(
                "\nI could not find any relevant news article."
            )

            continue

        try:

            conversation_context = (
                build_conversation_context()
            )

            answer = answer_question(
                news_context=news_context,
                conversation_context=conversation_context,
                question=question,
            )

            save_conversation(
                question=question,
                answer=answer,
            )

            print("\nANSWER:")
            print(answer)

        except Exception as error:

            print(
                f"\nFailed to generate answer: {error}"
            )


if __name__ == "__main__":
    main()