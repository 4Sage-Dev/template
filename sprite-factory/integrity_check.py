"""
Sprite Factory — Integrity Check Tool

Compares individual assets in public/assets/ against the baked
sprite sheet in dist/ and the gallery/preview registrations.
Reports mismatches and suggests fixes.

Usage:
    python integrity_check.py
    python integrity_check.py --fix   (interactive repair mode)
"""

from PIL import Image
import json
import os
import sys
import re


def get_registered_assets():
    """Parse src/preview.ts and gallery.html to find registered asset names."""
    registered_preview = set()
    registered_gallery = set()

    # Check preview.ts
    preview_path = "src/preview.ts"
    if os.path.exists(preview_path):
        with open(preview_path, "r") as f:
            content = f.read()
        # Match entries in assetMap like: name: '/assets/name/sprite.png'
        for match in re.finditer(r"(\w[\w-]*)\s*:\s*['\"]\/assets\/", content):
            registered_preview.add(match.group(1))

    # Check gallery.html
    gallery_path = "gallery.html"
    if os.path.exists(gallery_path):
        with open(gallery_path, "r") as f:
            content = f.read()
        # Match asset references in gallery
        for match in re.finditer(r"/assets/([\w-]+)/sprite\.png", content):
            registered_gallery.add(match.group(1))

    return registered_preview, registered_gallery


def get_asset_folders():
    """List all asset folders in public/assets/."""
    asset_root = "public/assets"
    if not os.path.exists(asset_root):
        return {}

    assets = {}
    for name in sorted(os.listdir(asset_root)):
        folder = os.path.join(asset_root, name)
        if not os.path.isdir(folder):
            continue
        assets[name] = {
            "has_sprite": os.path.exists(os.path.join(folder, "sprite.png")),
            "has_gen": os.path.exists(os.path.join(folder, "gen.py")),
            "sprite_mtime": os.path.getmtime(os.path.join(folder, "sprite.png"))
                           if os.path.exists(os.path.join(folder, "sprite.png")) else 0,
        }
    return assets


def get_baked_assets():
    """Read the baked spritesheet.json manifest to find baked asset names."""
    manifest_path = "dist/spritesheet.json"
    if not os.path.exists(manifest_path):
        return None, set()

    with open(manifest_path, "r") as f:
        data = json.load(f)

    manifest_mtime = os.path.getmtime(manifest_path)

    # Extract unique asset names (strip frame suffixes like _0, _1)
    baked_names = set()
    for frame_name in data.get("frames", {}):
        # "player_0" -> "player", "tree" -> "tree"
        parts = frame_name.rsplit("_", 1)
        if len(parts) == 2 and parts[1].isdigit():
            baked_names.add(parts[0])
        else:
            baked_names.add(frame_name)

    return manifest_mtime, baked_names


def run_check():
    """Run the full integrity check. Returns list of issues."""
    issues = []

    asset_folders = get_asset_folders()
    registered_preview, registered_gallery = get_registered_assets()
    bake_mtime, baked_names = get_baked_assets()

    all_known = set(asset_folders.keys()) | registered_preview | registered_gallery | baked_names

    for name in sorted(all_known):
        in_folders = name in asset_folders
        in_preview = name in registered_preview
        in_gallery = name in registered_gallery
        in_bake = name in baked_names

        # Missing sprite.png
        if in_folders and not asset_folders[name]["has_sprite"]:
            issues.append({
                "asset": name,
                "type": "missing_sprite",
                "message": f"Asset folder exists but sprite.png is missing",
                "fixes": ["Regenerate by running gen.py", "Remove this asset folder"]
            })

        # Missing gen.py
        if in_folders and not asset_folders[name]["has_gen"]:
            issues.append({
                "asset": name,
                "type": "missing_gen",
                "message": f"Asset folder exists but gen.py is missing",
                "fixes": ["Create a gen.py stub", "Not critical if sprite.png exists"]
            })

        # Orphaned asset — in folder but not registered
        if in_folders and asset_folders[name]["has_sprite"] and not in_preview:
            issues.append({
                "asset": name,
                "type": "not_registered_preview",
                "message": f"Has sprite.png but not registered in src/preview.ts",
                "fixes": ["Register in preview.ts", "Remove asset folder"]
            })

        if in_folders and asset_folders[name]["has_sprite"] and not in_gallery:
            issues.append({
                "asset": name,
                "type": "not_registered_gallery",
                "message": f"Has sprite.png but not registered in gallery.html",
                "fixes": ["Add to gallery.html", "Remove asset folder"]
            })

        # Registered but no folder
        if not in_folders and (in_preview or in_gallery):
            where = []
            if in_preview:
                where.append("preview.ts")
            if in_gallery:
                where.append("gallery.html")
            issues.append({
                "asset": name,
                "type": "registered_no_folder",
                "message": f"Registered in {', '.join(where)} but no asset folder exists",
                "fixes": ["Create asset folder and generate sprite", "Remove from registry"]
            })

        # In baked sheet but no individual asset
        if in_bake and not in_folders:
            issues.append({
                "asset": name,
                "type": "baked_no_folder",
                "message": f"Exists in baked sprite sheet but has no individual asset folder",
                "fixes": ["Import from baked sheet: python import_sheet.py dist/spritesheet.png ...",
                          "Will be removed on next bake"]
            })

        # Modified since last bake
        if in_bake and in_folders and asset_folders[name]["has_sprite"] and bake_mtime:
            if asset_folders[name]["sprite_mtime"] > bake_mtime:
                issues.append({
                    "asset": name,
                    "type": "modified_since_bake",
                    "message": f"Individual sprite modified after last bake",
                    "fixes": ["Re-bake atlas: python gen_master_atlas.py",
                              "Revert sprite to match baked version"]
                })

        # In folders but not in bake (and bake exists)
        if in_folders and asset_folders[name]["has_sprite"] and bake_mtime and not in_bake:
            issues.append({
                "asset": name,
                "type": "not_in_bake",
                "message": f"Asset exists but was not included in the last bake",
                "fixes": ["Re-bake atlas: python gen_master_atlas.py",
                          "Asset may have been added after last bake"]
            })

    return issues


def print_report(issues):
    """Print a human-readable report."""
    if not issues:
        print("Integrity check passed — no issues found.")
        return

    print(f"\nIntegrity check found {len(issues)} issue(s):\n")

    for issue in issues:
        print(f"  [{issue['type']}] {issue['asset']}")
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
        print(f"  [{issue['type']}] {issue['asset']}: {issue['message']}")
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

    print("Sprite Factory — Integrity Check")
    print("=" * 40)

    issues = run_check()
    print_report(issues)

    if fix_mode and issues:
        interactive_fix(issues)

    # Exit with non-zero if issues found (useful for CI/scripting)
    sys.exit(1 if issues else 0)


if __name__ == "__main__":
    main()
