"""
Simple intent classifier.
"""


def detect_intent(
    user_input: str,
) -> str:
    """
    Detect user intent.

    Returns:
        briefing
        question
    """

    text = user_input.lower()

    briefing_keywords = [
        "today news",
        "today's news",
        "latest news",
        "news briefing",
        "headlines",
        "top news",
        "world news",
        "what is happening",
        "what's happening",
    ]

    for keyword in briefing_keywords:

        if keyword in text:
            return "briefing"

    return "question"


def main():

    while True:

        user_input = input(
            "\nEnter text: "
        )

        print(
            detect_intent(user_input)
        )


if __name__ == "__main__":
    main()