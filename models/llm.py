from ollama import chat
import ollama

def answer_question(
    news_context: str,
    conversation_context: str,
    question: str,
) -> str:
    """
    Answer a question using:
    - News context
    - Conversation history
    """

    prompt = f"""
You are a professional news assistant.

Use the conversation history when relevant.

Use ONLY the provided news context.

If the answer is not available, say:

"I could not find that information in today's news."

CONVERSATION HISTORY:
{conversation_context}

NEWS CONTEXT:
{news_context}

CURRENT QUESTION:
{question}

ANSWER:
"""

    response = ollama.chat(
        model="llama3.2:3b",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    return response["message"]["content"]


def summarize_article(article_text):

    prompt = f"""
You are a professional news analyst.

Summarize the following news article in 5-7 concise bullet points.

ARTICLE:

{article_text}
"""

    response = chat(
        model="llama3.2:3b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]


if __name__ == "__main__":

    sample_text = """
    Iran and Israel say they have halted attacks on each other after exchanging fire.
    Israel conducted air strikes while Iran launched missiles.
    The United States encouraged both countries to stop further escalation.
    """

    summary = summarize_article(sample_text)

    print("\nSUMMARY:\n")
    print(summary)