"""
Speech-to-Text using Whisper.

Records audio from microphone,
saves it temporarily,
then transcribes it using Whisper.
"""

import tempfile

import whisper
import sounddevice as sd
import soundfile as sf


# Load model once during startup
model = whisper.load_model("base")


def listen_and_transcribe(
    duration: int = 5,
) -> str:
    """
    Record audio and convert to text.

    Args:
        duration: Recording length in seconds.

    Returns:
        Transcribed text.
    """

    sample_rate = 16000

    print("\nListening...")

    audio = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="float32",
    )

    sd.wait()

    print("Processing speech...")

    with tempfile.NamedTemporaryFile(
        suffix=".wav",
        delete=False,
    ) as temp_file:

        sf.write(
            temp_file.name,
            audio,
            sample_rate,
        )

        result = model.transcribe(
            temp_file.name
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