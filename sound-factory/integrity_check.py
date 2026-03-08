"""
Sound Factory — Integrity Check Tool

Compares individual sounds in public/sounds/ against the packaged
manifest in dist/ and the player/preview registrations.
Reports mismatches and suggests fixes.

Usage:
    python integrity_check.py
    python integrity_check.py --fix   (interactive repair mode)
"""

import json
import os
import sys
import re


def get_registered_sounds():
    """Parse src/preview.ts and player.html to find registered sound names."""
    registered_preview = set()
    registered_player = set()

    # Check preview.ts
    preview_path = "src/preview.ts"
    if os.path.exists(preview_path):
        with open(preview_path, "r") as f:
            content = f.read()
        for match in re.finditer(r"(\w[\w-]*)\s*:\s*['\"]\/sounds\/", content):
            registered_preview.add(match.group(1))

    # Check player.html
    player_path = "player.html"
    if os.path.exists(player_path):
        with open(player_path, "r") as f:
            content = f.read()
        for match in re.finditer(r"/sounds/([\w-]+)/sound\.wav", content):
            registered_player.add(match.group(1))

    return registered_preview, registered_player


def get_sound_folders():
    """List all sound folders in public/sounds/."""
    sound_root = "public/sounds"
    if not os.path.exists(sound_root):
        return {}

    sounds = {}
    for name in sorted(os.listdir(sound_root)):
        folder = os.path.join(sound_root, name)
        if not os.path.isdir(folder):
            continue
        wav_path = os.path.join(folder, "sound.wav")
        sounds[name] = {
            "has_wav": os.path.exists(wav_path),
            "has_gen": os.path.exists(os.path.join(folder, "gen.py")),
            "wav_mtime": os.path.getmtime(wav_path)
                         if os.path.exists(wav_path) else 0,
        }
    return sounds


def get_manifest_sounds():
    """Read the packaged manifest.json to find manifest sound names."""
    manifest_path = "dist/manifest.json"
    if not os.path.exists(manifest_path):
        return None, set()

    with open(manifest_path, "r") as f:
        data = json.load(f)

    manifest_mtime = os.path.getmtime(manifest_path)
    manifest_names = set(data.get("sounds", {}).keys())

    return manifest_mtime, manifest_names


def run_check():
    """Run the full integrity check. Returns list of issues."""
    issues = []

    sound_folders = get_sound_folders()
    registered_preview, registered_player = get_registered_sounds()
    manifest_mtime, manifest_names = get_manifest_sounds()

    all_known = (set(sound_folders.keys()) | registered_preview |
                 registered_player | manifest_names)

    for name in sorted(all_known):
        in_folders = name in sound_folders
        in_preview = name in registered_preview
        in_player = name in registered_player
        in_manifest = name in manifest_names

        # Missing sound.wav
        if in_folders and not sound_folders[name]["has_wav"]:
            issues.append({
                "sound": name,
                "type": "missing_wav",
                "message": "Sound folder exists but sound.wav is missing",
                "fixes": ["Regenerate by running gen.py",
                          "Remove this sound folder"]
            })

        # Missing gen.py
        if in_folders and not sound_folders[name]["has_gen"]:
            issues.append({
                "sound": name,
                "type": "missing_gen",
                "message": "Sound folder exists but gen.py is missing",
                "fixes": ["Create a gen.py stub",
                          "Not critical if sound.wav exists"]
            })

        # Orphaned sound — in folder but not registered
        if in_folders and sound_folders[name]["has_wav"] and not in_preview:
            issues.append({
                "sound": name,
                "type": "not_registered_preview",
                "message": "Has sound.wav but not registered in src/preview.ts",
                "fixes": ["Register in preview.ts", "Remove sound folder"]
            })

        if in_folders and sound_folders[name]["has_wav"] and not in_player:
            issues.append({
                "sound": name,
                "type": "not_registered_player",
                "message": "Has sound.wav but not registered in player.html",
                "fixes": ["Add to player.html", "Remove sound folder"]
            })

        # Registered but no folder
        if not in_folders and (in_preview or in_player):
            where = []
            if in_preview:
                where.append("preview.ts")
            if in_player:
                where.append("player.html")
            issues.append({
                "sound": name,
                "type": "registered_no_folder",
                "message": f"Registered in {', '.join(where)} but no sound folder exists",
                "fixes": ["Create sound folder and generate audio",
                          "Remove from registry"]
            })

        # In manifest but no individual sound
        if in_manifest and not in_folders:
            issues.append({
                "sound": name,
                "type": "manifest_no_folder",
                "message": "Exists in manifest but has no individual sound folder",
                "fixes": ["Create the sound folder with the audio file",
                          "Will be removed on next manifest build"]
            })

        # Modified since last package
        if (in_manifest and in_folders and sound_folders[name]["has_wav"]
                and manifest_mtime):
            if sound_folders[name]["wav_mtime"] > manifest_mtime:
                issues.append({
                    "sound": name,
                    "type": "modified_since_package",
                    "message": "Sound file modified after last manifest package",
                    "fixes": ["Re-package manifest: python gen_master_manifest.py",
                              "Revert sound to match packaged version"]
                })

        # In folders but not in manifest (and manifest exists)
        if (in_folders and sound_folders[name]["has_wav"]
                and manifest_mtime and not in_manifest):
            issues.append({
                "sound": name,
                "type": "not_in_manifest",
                "message": "Sound exists but was not included in the last manifest",
                "fixes": ["Re-package manifest: python gen_master_manifest.py",
                          "Sound may have been added after last package"]
            })

    return issues


def print_report(issues):
    """Print a human-readable report."""
    if not issues:
        print("Integrity check passed — no issues found.")
        return

    print(f"\nIntegrity check found {len(issues)} issue(s):\n")

    for issue in issues:
        print(f"  [{issue['type']}] {issue['sound']}")
        print(f"    {issue['message']}")
        for fix in issue['fixes']:
            print(f"    -> {fix}")
        print()


def interactive_fix(issues):
    """Walk through issues and let the user choose fixes."""
    if not issues:
        print("No issues to fix.")
        return

    print(f"\n{len(issues)} issue(s) found. Walking through each:\n")

    for issue in issues:
        print(f"  [{issue['type']}] {issue['sound']}: {issue['message']}")
        for i, fix in enumerate(issue['fixes']):
            print(f"    {i + 1}. {fix}")
        print(f"    s. Skip")
        choice = input("    Choice: ").strip().lower()

        if choice == "s":
            print("    Skipped.\n")
            continue

        try:
            idx = int(choice) - 1
            if 0 <= idx < len(issue['fixes']):
                print(f"    Selected: {issue['fixes'][idx]}")
                print(f"    (Action must be performed manually or by the AI agent)\n")
        except ValueError:
            print("    Skipped.\n")


def main():
    fix_mode = "--fix" in sys.argv

    print("Sound Factory — Integrity Check")
    print("=" * 40)

    issues = run_check()
    print_report(issues)

    if fix_mode and issues:
        interactive_fix(issues)

    sys.exit(1 if issues else 0)


if __name__ == "__main__":
    main()
