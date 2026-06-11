"""
Generate a spoken news briefing.
"""

from memory.database import get_all_articles
from memory.briefing_memory import save_briefing

def generate_news_briefing(
    limit: int = 5,
) -> str:
    """
    Create a short spoken briefing.
    """

    articles = get_all_articles()

    if not articles:
        return "I could not find any news articles."

    save_briefing(
        articles[:limit]
    )
    
    if not articles:

        return (
            "I could not find any news articles."
        )

    briefing = [
        "Here are today's top news stories."
    ]

    for index, article in enumerate(
        articles[:limit],
        start=1,
    ):

        briefing.append(
            f"{index}. {article['title']}"
        )

    briefing.append(
        "Which story would you like to hear more about?"
    )

    return "\n".join(briefing)


def main():

    briefing = generate_news_briefing()

    print(briefing)


if __name__ == "__main__":
    main()