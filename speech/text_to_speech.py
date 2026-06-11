"""
Text-to-Speech Module.

Responsibilities:
- Convert text into speech
- Speak responses aloud
"""

import pyttsx3


def speak(text: str) -> None:
    """
    Convert text to speech.

    Args:
        text: Text to speak.
    """

    if not text.strip():
        return

    engine = pyttsx3.init()

    engine.setProperty("rate", 180)
    engine.setProperty("volume", 1.0)

    engine.say(text)
    engine.runAndWait()

    engine.stop()


def main() -> None:
    """
    Test TTS.
    """

    speak("First message")
    speak("Second message")
    speak("Third message")


if __name__ == "__main__":
    main()