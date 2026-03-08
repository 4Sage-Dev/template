"""
Sound Factory — Import Audio Tool

Imports external audio files (WAV, OGG, MP3) into the public/sounds/
hierarchy, converting to a consistent format.

Usage:
    python import_audio.py laser.wav --name laser-shot --category effect
    python import_audio.py bgm.mp3 --name theme --category music
    python import_audio.py *.wav --names "laser,explosion,pickup" --category effect
    python import_audio.py alert.ogg --name alert --category ui --mode replace

Arguments:
    sources             One or more audio files to import
    --name NAME         Sound name (for single file import)
    --names NAMES       Comma-separated names (for multi-file import)
    --category CAT      Category: effect, ambient, music, ui (default: effect)
    --mode MODE         Conflict resolution: "ask" (default), "replace", "rename"
    --sample-rate N     Target sample rate (default: 44100)

Requires: numpy, scipy (for format conversion)
Optional: pydub (for MP3/OGG support — falls back to scipy for WAV)
"""

import argparse
import os
import sys
import shutil
import wave
import struct

try:
    import numpy as np
    from scipy.io import wavfile
    HAS_SCIPY = True
except ImportError:
    HAS_SCIPY = False

try:
    from pydub import AudioSegment
    HAS_PYDUB = True
except ImportError:
    HAS_PYDUB = False


def convert_to_wav(source_path, target_path, target_rate=44100):
    """Convert an audio file to WAV format at the target sample rate."""
    ext = os.path.splitext(source_path)[1].lower()

    if ext == ".wav":
        if HAS_SCIPY:
            rate, data = wavfile.read(source_path)
            # Convert to mono if stereo
            if len(data.shape) > 1:
                data = data.mean(axis=1).astype(data.dtype)
            # Resample if needed
            if rate != target_rate:
                duration = len(data) / rate
                num_samples = int(duration * target_rate)
                indices = np.linspace(0, len(data) - 1, num_samples).astype(int)
                data = data[indices]
            # Ensure 16-bit
            if data.dtype != np.int16:
                if np.issubdtype(data.dtype, np.floating):
                    data = np.int16(data / np.max(np.abs(data)) * 32767)
                elif data.dtype == np.int32:
                    data = np.int16(data >> 16)
            wavfile.write(target_path, target_rate, data)
        else:
            # Fallback: just copy WAV files
            shutil.copy2(source_path, target_path)
        return True

    elif ext in (".mp3", ".ogg", ".flac", ".m4a"):
        if HAS_PYDUB:
            audio = AudioSegment.from_file(source_path)
            audio = audio.set_frame_rate(target_rate)
            audio = audio.set_channels(1)
            audio = audio.set_sample_width(2)  # 16-bit
            audio.export(target_path, format="wav")
            return True
        else:
            print(f"  Warning: Cannot convert {ext} files without pydub.")
            print(f"  Install with: pip install pydub")
            print(f"  (Also requires ffmpeg on the system)")
            return False
    else:
        print(f"  Warning: Unsupported format: {ext}")
        return False


def write_gen_py(sound_dir, source_file, category, sound_name):
    """Write a gen.py stub documenting the import source."""
    gen_path = os.path.join(sound_dir, "gen.py")
    code = f'''"""
Imported from: {source_file}
Category: {category}
"""

def generate():
    # This sound was imported from an external file.
    # The sound.wav was converted from the source file.
    # To regenerate, re-run: python import_audio.py
    print("Sound '{sound_name}' was imported — sound.wav is the source of truth.")

if __name__ == "__main__":
    generate()
'''
    with open(gen_path, "w") as f:
        f.write(code)


def get_sound_info(wav_path):
    """Get basic info about a WAV file."""
    try:
        with wave.open(wav_path, 'r') as wf:
            frames = wf.getnframes()
            rate = wf.getframerate()
            channels = wf.getnchannels()
            duration = round(frames / rate, 2)
            return {"duration": duration, "sampleRate": rate, "channels": channels}
    except Exception:
        return None


def resolve_conflict(sound_dir, sound_name, mode):
    """Handle existing sound folder. Returns the final directory to use."""
    if not os.path.exists(sound_dir):
        return sound_dir, "created"

    if mode == "replace":
        return sound_dir, "replaced"
    elif mode == "rename":
        i = 2
        while os.path.exists(f"{sound_dir}-{i}"):
            i += 1
        new_dir = f"{sound_dir}-{i}"
        new_name = f"{sound_name}-{i}"
        print(f"  Renamed to: {new_name}")
        return new_dir, "renamed"
    else:  # ask
        print(f"\n  Sound '{sound_name}' already exists at {sound_dir}")
        print(f"  [r]eplace  [k]eep both (rename)  [s]kip")
        choice = input("  Choice: ").strip().lower()
        if choice == "r":
            return sound_dir, "replaced"
        elif choice == "k":
            return resolve_conflict(sound_dir, sound_name, "rename")
        else:
            return None, "skipped"


def import_audio(source_paths, names, category="effect", mode="ask",
                 sample_rate=44100):
    """Main import function. Returns list of (sound_name, action) tuples."""
    sound_root = "public/sounds"
    os.makedirs(sound_root, exist_ok=True)

    if len(names) != len(source_paths):
        if len(names) == 1 and len(source_paths) == 1:
            pass  # OK
        else:
            print(f"Error: {len(source_paths)} files but {len(names)} names provided")
            return []

    results = []
    for source_path, sound_name in zip(source_paths, names):
        if not os.path.exists(source_path):
            print(f"Error: Source file not found: {source_path}")
            results.append((sound_name, "error"))
            continue

        print(f"\nImporting: {source_path} -> {sound_name} ({category})")

        sound_dir = os.path.join(sound_root, sound_name)
        final_dir, action = resolve_conflict(sound_dir, sound_name, mode)

        if action == "skipped":
            results.append((sound_name, "skipped"))
            continue

        os.makedirs(final_dir, exist_ok=True)
        target_wav = os.path.join(final_dir, "sound.wav")

        if convert_to_wav(source_path, target_wav, sample_rate):
            actual_name = os.path.basename(final_dir)
            write_gen_py(final_dir, os.path.basename(source_path),
                         category, actual_name)

            info = get_sound_info(target_wav)
            if info:
                print(f"  Saved: {final_dir}/sound.wav ({info['duration']}s, "
                      f"{info['sampleRate']}Hz, {info['channels']}ch)")
            else:
                print(f"  Saved: {final_dir}/sound.wav")

            results.append((actual_name, action))
        else:
            results.append((sound_name, "error"))

    print(f"\nImport complete: {len(results)} sound(s) processed")
    return results


def main():
    parser = argparse.ArgumentParser(
        description="Import audio files into the sound structure")
    parser.add_argument("sources", nargs="+", help="Source audio file(s)")
    parser.add_argument("--name", help="Sound name (single file)")
    parser.add_argument("--names",
                        help='Comma-separated names (multi-file): "laser,explosion"')
    parser.add_argument("--category", default="effect",
                        choices=["effect", "ambient", "music", "ui"],
                        help="Sound category (default: effect)")
    parser.add_argument("--mode", choices=["ask", "replace", "rename"],
                        default="ask", help="Conflict resolution (default: ask)")
    parser.add_argument("--sample-rate", type=int, default=44100,
                        help="Target sample rate (default: 44100)")

    args = parser.parse_args()

    if args.names:
        names = [n.strip() for n in args.names.split(",")]
    elif args.name:
        names = [args.name]
    else:
        # Auto-name from filenames
        names = [os.path.splitext(os.path.basename(s))[0] for s in args.sources]
        print(f"Auto-naming from filenames: {names}")

    import_audio(args.sources, names, category=args.category,
                 mode=args.mode, sample_rate=args.sample_rate)


if __name__ == "__main__":
    main()
