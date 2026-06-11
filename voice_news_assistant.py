"""
Main Voice News Assistant.

Responsibilities:
- Listen to user speech
- Detect intent
- Generate response
- Speak response
"""

from speech.speech_to_text import (
    load_whisper_model,
    listen_and_transcribe,
)

from speech.text_to_speech import speak

from ai.intent_classifier import (
    detect_intent,
)

from ai.news_briefing import (
    generate_news_briefing,
)

from ai.briefing_selector import (
    get_article_from_reference,
)

from ai.news_qa import (
    build_news_context,
    build_conversation_context,
)

from memory.database import (
    save_conversation,
)

from models.llm import (
    answer_question,
)


def handle_question(
    question: str,
) -> str:
    """
    Handle news QA requests.
    """

    news_context = build_news_context(
        question
    )

    if not news_context:

        return (
            "I could not find any relevant news article."
        )

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

    return answer


def main() -> None:
    """
    Start the voice assistant.
    """

    print("=" * 80)
    print("VOICE NEWS ASSISTANT")
    print("=" * 80)

    whisper_model = (
        load_whisper_model()
    )

    print("\nAssistant Ready.")

    while True:

        print(
            "\nSpeak your command..."
        )

        user_input = (
            listen_and_transcribe(
                model=whisper_model,
            )
        )

        if not user_input:

            print(
                "\nCould not understand speech."
            )

            continue

        print(
            f"\nYOU SAID: {user_input}"
        )

        clean_input = (
            user_input.lower()
            .replace(".", "")
            .replace(",", "")
            .strip()
        )

        if clean_input in [
            "exit",
            "quit",
            "stop",
        ]:

            speak("Goodbye Boss.")

            break

        intent = detect_intent(
            user_input
        )

        # NEWS BRIEFING
        if intent == "briefing":

            response = (
                generate_news_briefing()
            )

        else:

            # Check if user refers to
            # first, second, third, fourth, fifth story
            article = (
                get_article_from_reference(
                    user_input
                )
            )

            if article:

                response = f"""
Title:
{article['title']}

Summary:

{article['summary']}
"""

            else:

                response = handle_question(
                    user_input
                )

        print("\nASSISTANT:")
        print(response)

        speak(response)

    print("\nAssistant stopped.")


if __name__ == "__main__":
    main()