import json
import os
import wave

def build_manifest():
    sound_root = "public/sounds"
    dist_dir = "dist"

    if not os.path.exists(dist_dir):
        os.makedirs(dist_dir)

    manifest = {"sounds": {}}

    sound_folders = [f for f in os.listdir(sound_root)
                     if os.path.isdir(os.path.join(sound_root, f))]
    sound_folders.sort()

    for folder in sound_folders:
        wav_path = os.path.join(sound_root, folder, "sound.wav")
        if not os.path.exists(wav_path):
            continue

        try:
            with wave.open(wav_path, 'r') as wf:
                frames = wf.getnframes()
                rate = wf.getframerate()
                channels = wf.getnchannels()
                duration = round(frames / rate, 2)
        except Exception as e:
            print(f"Warning: could not read {wav_path}: {e}")
            continue

        manifest["sounds"][folder] = {
            "file": f"sounds/{folder}/sound.wav",
            "category": "effect",
            "duration": duration,
            "sampleRate": rate,
            "channels": channels
        }
        print(f"Added {folder}: {duration}s, {rate}Hz, {channels}ch")

    out_path = os.path.join(dist_dir, "manifest.json")
    with open(out_path, "w") as f:
        json.dump(manifest, f, indent=2)

    print(f"\nManifest built: {out_path}")
    print(f"Total sounds: {len(manifest['sounds'])}")

if __name__ == "__main__":
    build_manifest()
