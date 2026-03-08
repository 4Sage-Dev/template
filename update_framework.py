"""
4SAGE Framework Updater

Pulls the latest framework files from the template repository without
touching project-specific content (KDD decisions, assets, sounds, journal).

Usage:
    python update_framework.py              # Preview changes (dry run)
    python update_framework.py --apply      # Apply updates

What gets updated:
    - sprite-factory/ scripts and configs (not public/assets/ content)
    - sound-factory/ scripts and configs (not public/sounds/ content)
    - FRAMEWORK.md, CONTRIBUTING.md, conductor.md
    - Top-level tooling files

What is NEVER touched:
    - kdd/                  (your design decisions)
    - decisions/            (your recorded choices)
    - knowledge-base/       (your reference material)
    - JOURNAL.md            (your session log)
    - sprite-factory/public/assets/*   (your sprites)
    - sprite-factory/dist/*            (your baked output)
    - sound-factory/public/sounds/*    (your audio files)
    - sound-factory/dist/*             (your packaged output)
    - .git/                 (your repo history)
"""

import os
import sys
import subprocess
import shutil
import tempfile

TEMPLATE_REPO = "https://github.com/4Sage-Dev/template.git"

# Files/dirs that are ALWAYS updated from the template
FRAMEWORK_FILES = [
    "FRAMEWORK.md",
    "CONTRIBUTING.md",
    "conductor.md",
    "update_framework.py",
]

# Directories where we update scripts/configs but NOT user content
FACTORY_UPDATES = {
    "sprite-factory": {
        "update": [
            "gallery.html",
            "gen_master_atlas.py",
            "import_sheet.py",
            "integrity_check.py",
            "package.json",
            "vite.config.ts",
            "tsconfig.json",
            "src/preview.ts",
        ],
        "preserve": [
            "public/assets/",
            "dist/",
            "node_modules/",
        ],
    },
    "sound-factory": {
        "update": [
            "player.html",
            "gen_master_manifest.py",
            "package.json",
            "vite.config.ts",
            "tsconfig.json",
            "src/preview.ts",
        ],
        "preserve": [
            "public/sounds/",
            "dist/",
            "node_modules/",
        ],
    },
}

# These are NEVER touched
NEVER_TOUCH = [
    "kdd/",
    "decisions/",
    "knowledge-base/",
    "JOURNAL.md",
    ".git/",
    ".gitignore",
    "README.md",
    "LICENSE",
]


def clone_template(tmpdir):
    """Clone the latest template into a temp directory."""
    print(f"Fetching latest template from {TEMPLATE_REPO}...")
    result = subprocess.run(
        ["git", "clone", "--depth", "1", TEMPLATE_REPO, tmpdir],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"Error cloning template: {result.stderr}")
        sys.exit(1)
    print("Template fetched.\n")


def compare_file(source, target):
    """Compare two files. Returns True if they differ."""
    if not os.path.exists(target):
        return True
    if not os.path.exists(source):
        return False
    with open(source, "rb") as f1, open(target, "rb") as f2:
        return f1.read() != f2.read()


def find_updates(tmpdir, project_dir):
    """Find all files that would be updated. Returns list of (source, target, status)."""
    updates = []

    # Top-level framework files
    for filename in FRAMEWORK_FILES:
        source = os.path.join(tmpdir, filename)
        target = os.path.join(project_dir, filename)
        if os.path.exists(source) and compare_file(source, target):
            status = "new" if not os.path.exists(target) else "updated"
            updates.append((source, target, status))

    # Factory directories
    for factory_name, config in FACTORY_UPDATES.items():
        for filename in config["update"]:
            source = os.path.join(tmpdir, factory_name, filename)
            target = os.path.join(project_dir, factory_name, filename)
            if os.path.exists(source) and compare_file(source, target):
                status = "new" if not os.path.exists(target) else "updated"
                updates.append((source, target, status))

        # Check for new files in factory that we don't know about yet
        source_factory = os.path.join(tmpdir, factory_name)
        if os.path.exists(source_factory):
            for item in os.listdir(source_factory):
                source_path = os.path.join(source_factory, item)
                # Skip preserved directories
                skip = False
                for preserved in config["preserve"]:
                    if item == preserved.rstrip("/"):
                        skip = True
                        break
                if skip or not os.path.isfile(source_path):
                    continue
                if item not in config["update"]:
                    target_path = os.path.join(project_dir, factory_name, item)
                    if compare_file(source_path, target_path):
                        status = "new" if not os.path.exists(target_path) else "updated"
                        updates.append((source_path, target_path, status))

    return updates


def apply_updates(updates):
    """Copy updated files into place."""
    for source, target, status in updates:
        os.makedirs(os.path.dirname(target), exist_ok=True)
        shutil.copy2(source, target)
        print(f"  [{status}] {os.path.relpath(target)}")


def main():
    apply = "--apply" in sys.argv
    project_dir = os.getcwd()

    # Sanity check — are we in a 4SAGE project?
    if not os.path.exists(os.path.join(project_dir, "kdd")):
        print("Error: This doesn't look like a 4SAGE project (no kdd/ directory).")
        print("Run this script from your project root.")
        sys.exit(1)

    tmpdir = tempfile.mkdtemp(prefix="4sage-update-")

    try:
        clone_template(tmpdir)
        updates = find_updates(tmpdir, project_dir)

        if not updates:
            print("Your framework files are up to date. Nothing to change.")
            return

        print(f"Found {len(updates)} file(s) to update:\n")
        for source, target, status in updates:
            rel = os.path.relpath(target, project_dir)
            print(f"  [{status:>7}] {rel}")

        print()
        print("Your project content (kdd/, decisions/, assets/, sounds/, JOURNAL.md)")
        print("will NOT be modified.\n")

        if apply:
            apply_updates(updates)
            print(f"\nDone. {len(updates)} file(s) updated.")
            print("Review the changes with 'git diff', then commit when satisfied.")
        else:
            print("This was a dry run. To apply these updates, run:")
            print("  python update_framework.py --apply")

    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)


if __name__ == "__main__":
    main()
