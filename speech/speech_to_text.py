"""
Speech-to-Text using Whisper.

Responsibilities:
- Record audio
- Convert speech to text
"""

import whisper

from speech.audio_recorder import (
    record_until_silence,
)


# Load model once
model = whisper.load_model("base")


def listen_and_transcribe() -> str:
    """
    Record audio and convert to text.
    """

    audio_file = record_until_silence()

    print("Processing speech...")

    result = model.transcribe(
        audio_file,
        fp16=False,
    )

    text = result["text"].strip()

    if len(text) < 3:
        return ""

    return text


def main() -> None:

    text = listen_and_transcribe()

    print("\nTRANSCRIPT:")
    print(text)


if __name__ == "__main__":
    main()