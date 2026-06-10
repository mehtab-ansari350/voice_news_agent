"""
Text-to-Speech Module.

Responsibilities:
- Convert text into speech
- Speak responses aloud
"""

import pyttsx3


# Initialize engine once
engine = pyttsx3.init()

# Speech settings
engine.setProperty("rate", 180)
engine.setProperty("volume", 1.0)


def speak(text: str) -> None:
    """
    Convert text to speech.

    Args:
        text: Text to speak.
    """

    if not text.strip():
        return

    engine.say(text)
    engine.runAndWait()


def main() -> None:
    """
    Test TTS.
    """

    speak(
        "Hello Mehtab. Your voice assistant is working."
    )


if __name__ == "__main__":
    main()