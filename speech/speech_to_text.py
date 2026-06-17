"""
Speech-to-Text using Whisper.

Responsibilities:
- Load Whisper model
- Record audio
- Transcribe audio
"""

import os
import tempfile

import whisper
import sounddevice as sd
import soundfile as sf


def load_whisper_model(
    model_name: str = "base",
):
    """
    Load Whisper model.

    Args:
        model_name: Whisper model name.

    Returns:
        Loaded Whisper model.
    """

    print(
        f"Loading Whisper model: {model_name}"
    )

    return whisper.load_model(model_name)


def transcribe_audio(
    model,
    audio_file: str,
) -> str:


    # File exists?
    if not os.path.exists(audio_file):
        return ""

    try:
        audio_data, sample_rate = sf.read(audio_file)

        # Empty audio
        if len(audio_data) == 0:
            return ""

    except Exception:
        return ""

    try:

        result = model.transcribe(
            audio_file,
            fp16=False,
        )
        print("WHISPER RESULT:")
        print(result)

        return result["text"].strip()

    except Exception as e:

        print("Whisper Error:", e)

        return ""


def listen_and_transcribe(
    model,
    duration: int = 5,
) -> str:
    """
    Record speech and transcribe it.

    Args:
        model: Loaded Whisper model.
        duration: Recording duration.

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

        temp_audio_path = temp_file.name

    try:

        text = transcribe_audio(
            model=model,
            audio_file=temp_audio_path,
        )

    finally:

        if os.path.exists(
            temp_audio_path
        ):
            os.remove(
                temp_audio_path
            )

    if len(text) < 3:
        return ""

    return text


def main() -> None:
    """
    Test Speech-to-Text.
    """

    model = load_whisper_model()

    text = listen_and_transcribe(
        model=model,
    )

    print("\nTRANSCRIPT:")
    print(text)


if __name__ == "__main__":
    main()