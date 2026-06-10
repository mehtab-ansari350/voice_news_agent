"""
Conversation memory management.
"""

from collections import deque


MAX_HISTORY = 5


conversation_history = deque(
    maxlen=MAX_HISTORY
)


def add_interaction(
    question: str,
    answer: str,
) -> None:
    """
    Store conversation turn.
    """

    conversation_history.append(
        {
            "question": question,
            "answer": answer,
        }
    )


def get_conversation_context() -> str:
    """
    Build conversation history context.
    """

    if not conversation_history:
        return ""

    parts = []

    for interaction in conversation_history:

        parts.append(
            f"""
USER:
{interaction['question']}

ASSISTANT:
{interaction['answer']}
"""
        )

    return "\n".join(parts)


def clear_memory() -> None:
    """
    Clear conversation history.
    """

    conversation_history.clear()