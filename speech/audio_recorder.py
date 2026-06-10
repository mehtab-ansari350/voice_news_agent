"""
Audio Recorder with Silence Detection.

Responsibilities:
- Record microphone input
- Detect silence
- Stop recording automatically
"""

from pathlib import Path

import numpy as np
import sounddevice as sd
import soundfile as sf


OUTPUT_FILE = Path("temp_audio.wav")


def record_until_silence(
    sample_rate: int = 16000,
    silence_threshold: float = 0.003,
    silence_duration: float = 3.0,
    minimum_recording_time: float = 3.0,
):
    """
    Record audio until silence is detected.

    Args:
        sample_rate: Audio sample rate.
        silence_threshold: Volume threshold.
        silence_duration: Seconds of silence before stopping.
    """

    print("\nListening... Speak now.")

    chunk_duration = 0.5
    chunk_size = int(sample_rate * chunk_duration)

    recorded_chunks = []

    silence_chunks_needed = int(
        silence_duration / chunk_duration
    )

    silent_chunks = 0
    total_chunks = 0
    

    while True:

        audio_chunk = sd.rec(
            chunk_size,
            samplerate=sample_rate,
            channels=1,
            dtype="float32",
        )

        sd.wait()

        recorded_chunks.append(audio_chunk)
        total_chunks += 1

        volume = np.abs(audio_chunk).mean()

        if volume < silence_threshold:

            silent_chunks += 1

        else:

            silent_chunks = 0

        recorded_time = total_chunks * chunk_duration

        if (
            recorded_time >= minimum_recording_time
            and silent_chunks >= silence_chunks_needed
        ):
            break

    full_audio = np.concatenate(
        recorded_chunks,
        axis=0,
    )

    sf.write(
        OUTPUT_FILE,
        full_audio,
        sample_rate,
    )

    print("Recording finished.")

    return str(OUTPUT_FILE)


def main():

    file_path = record_until_silence()

    print("\nSaved Audio:")
    print(file_path)


if __name__ == "__main__":
    main()