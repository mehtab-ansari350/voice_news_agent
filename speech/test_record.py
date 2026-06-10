import sounddevice as sd
import soundfile as sf

sample_rate = 16000
duration = 10

print("Recording for 10 seconds...")

audio = sd.rec(
    int(duration * sample_rate),
    samplerate=sample_rate,
    channels=1,
    dtype="float32",
)

sd.wait()

sf.write(
    "fixed_test.wav",
    audio,
    sample_rate,
)

print("Saved fixed_test.wav")