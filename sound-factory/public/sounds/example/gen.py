import numpy as np
from scipy.io import wavfile

SAMPLE_RATE = 44100

def generate():
    duration = 0.5
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), endpoint=False)

    # Simple beep: 880Hz sine wave
    waveform = np.sin(2 * np.pi * 880 * t)

    # Envelope: fast attack, quick decay
    envelope = np.exp(-t * 8)
    waveform *= envelope

    # Normalize to 16-bit
    waveform = waveform / np.max(np.abs(waveform))
    audio = np.int16(waveform * 32767 * 0.8)

    wavfile.write("sound.wav", SAMPLE_RATE, audio)
    print("Generated: example beep (880Hz, 0.5s)")

if __name__ == "__main__":
    generate()
