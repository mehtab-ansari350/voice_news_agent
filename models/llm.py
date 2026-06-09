from ollama import chat


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