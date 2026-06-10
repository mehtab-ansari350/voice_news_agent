"""
Voice-enabled News QA System.

Flow:
Microphone
    ↓
Whisper STT
    ↓
Question
    ↓
News Retriever (RAG)
    ↓
Conversation Memory
    ↓
LLM 
    ↓
Answer
    ↓
Database Memory
    ↓
User
"""

from speech.speech_to_text import listen_and_transcribe
from speech.text_to_speech import speak

from ai.news_qa import (
    build_news_context,
    build_conversation_context,
)

from memory.database import save_conversation

from models.llm import answer_question


def main() -> None:

    print("=" * 80)
    print("VOICE NEWS QA SYSTEM")
    print("=" * 80)

    while True:

        print("\nSpeak your question...")

        question = listen_and_transcribe()

        print(f"\nYOU SAID: {question}")

        if not question:

            print(
                "\nSpeech not detected. Please try again."
            )

            speak(
                "I could not understand. Please try again."
            )
            continue


        if question.lower() in (
            "exit",
            "quit",
            "stop",
        ):
            break

        news_context = build_news_context(
            question=question,
        )

        if not news_context:

            print(
                "\nNo relevant news found."
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

            # Speak answer aloud
            speak(answer)

        except Exception as error:

            print(
                f"\nError: {error}"
            )


if __name__ == "__main__":
    main()