"""
4SAGE — Spec/Tool Sync Verifier

Checks that specs in specs/ correctly reference the tools that exist
in sprite-factory/ and sound-factory/. Run this before committing
changes to either specs or tools.

Usage:
    python verify_sync.py

Exit code 0 = in sync, 1 = mismatches found.
"""

import os
import re
import sys


def get_python_scripts(factory_dir):
    """List all .py scripts in a factory directory (top-level only)."""
    if not os.path.exists(factory_dir):
        return set()
    return {f for f in os.listdir(factory_dir)
            if f.endswith(".py") and os.path.isfile(os.path.join(factory_dir, f))}


def get_spec_script_refs(spec_path):
    """Find all .py filenames referenced in a spec."""
    if not os.path.exists(spec_path):
        return set()
    with open(spec_path, "r") as f:
        content = f.read()
    # Match things like import_sheet.py, gen_master_atlas.py, integrity_check.py
    return set(re.findall(r'\b(\w+\.py)\b', content))


def check_factory(factory_name, factory_dir, spec_path):
    """Check one factory's tools against its spec. Returns list of issues."""
    issues = []

    scripts = get_python_scripts(factory_dir)
    spec_refs = get_spec_script_refs(spec_path)

    if not os.path.exists(spec_path):
        issues.append(f"Spec not found: {spec_path}")
        return issues

    # Scripts that exist but aren't mentioned in the spec
    for script in sorted(scripts):
        if script == "__init__.py":
            continue
        if script not in spec_refs:
            issues.append(
                f"Tool '{script}' exists in {factory_dir}/ but is not "
                f"referenced in {spec_path}")

    # Scripts referenced in spec but don't exist
    # Only check names that look like factory scripts (not stdlib like os.py)
    factory_script_pattern = re.compile(
        r'(gen_|import_|integrity_|export_|validate_|build_|pack_)\w+\.py')
    for ref in sorted(spec_refs):
        if factory_script_pattern.match(ref) and ref not in scripts:
            issues.append(
                f"Spec references '{ref}' but it does not exist in "
                f"{factory_dir}/")

    return issues


def check_project_structure(spec_path, factory_dir):
    """Check that the project structure listing in the spec matches reality."""
    issues = []

    if not os.path.exists(spec_path):
        return issues

    with open(spec_path, "r") as f:
        content = f.read()

    # Check that top-level scripts listed in the structure block exist
    # Look for lines like "    import_sheet.py             # description"
    # but not indented deeper (those are inside subdirectories like public/assets/)
    structure_refs = re.findall(
        r'^    (\w[\w_]*\.py)\s+#', content, re.MULTILINE)

    scripts = get_python_scripts(factory_dir)
    for ref in structure_refs:
        if ref not in scripts:
            issues.append(
                f"Spec structure listing includes '{ref}' but it does not "
                f"exist in {factory_dir}/")

    return issues


def main():
    print("4SAGE — Spec/Tool Sync Verifier")
    print("=" * 40)

    all_issues = []

    # Check sprite-factory
    issues = check_factory(
        "sprite-factory",
        "sprite-factory",
        "specs/sprite-builder/spec.md")
    issues += check_project_structure(
        "specs/sprite-builder/spec.md",
        "sprite-factory")
    if issues:
        print(f"\nSprite Builder:")
        for issue in issues:
            print(f"  - {issue}")
        all_issues.extend(issues)

    # Check sound-factory
    issues = check_factory(
        "sound-factory",
        "sound-factory",
        "specs/sound-factory/spec.md")
    issues += check_project_structure(
        "specs/sound-factory/spec.md",
        "sound-factory")
    if issues:
        print(f"\nSound Factory:")
        for issue in issues:
            print(f"  - {issue}")
        all_issues.extend(issues)

    # Check game-builder spec exists
    gb_spec = "specs/game-builder/spec.md"
    if not os.path.exists(gb_spec):
        all_issues.append(f"Game Builder spec not found: {gb_spec}")
        print(f"\nGame Builder:")
        print(f"  - Spec not found: {gb_spec}")

    if not all_issues:
        print("\nAll specs and tools are in sync.")
    else:
        print(f"\nFound {len(all_issues)} issue(s). Fix before committing.")

    sys.exit(1 if all_issues else 0)


if __name__ == "__main__":
    main()
