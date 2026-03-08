"""
Sprite Factory — Import Sheet Tool

Slices an existing sprite sheet into individual asset folders
in the public/assets/ hierarchy.

Usage:
    python import_sheet.py <source.png> --frame-size 32x32 --assets "player:0-3,enemy:4-7"
    python import_sheet.py <source.png> --frame-size 32x32 --name walk-cycle
    python import_sheet.py <source.png> --frame-size 64x48 --cols 4 --rows 2 --name boss

Arguments:
    source              Path to the sprite sheet PNG file
    --frame-size WxH    Frame dimensions (e.g., 32x32, 64x48)
    --cols N            Number of columns (auto-detected from image width if omitted)
    --rows N            Number of rows (auto-detected from image height if omitted)
    --name NAME         Name for a single-asset sheet (all frames = one asset)
    --assets SPEC       Multi-asset spec: "name:start-end,name:start-end"
                        Frame indices are 0-based, left-to-right then top-to-bottom
    --mode MODE         Conflict resolution: "ask" (default), "replace", "add", "rename"
"""

from PIL import Image
import argparse
import os
import sys
import json


def detect_grid(img, frame_w, frame_h):
    """Calculate columns and rows from image size and frame dimensions."""
    cols = img.width // frame_w
    rows = img.height // frame_h
    return cols, rows


def extract_frames(img, frame_w, frame_h, cols, rows):
    """Extract all frames from a sprite sheet, left-to-right then top-to-bottom."""
    frames = []
    for r in range(rows):
        for c in range(cols):
            x = c * frame_w
            y = r * frame_h
            frame = img.crop((x, y, x + frame_w, y + frame_h))
            # Skip fully transparent frames
            if frame.getextrema()[3][1] > 0:  # alpha channel max > 0
                frames.append(frame)
            else:
                frames.append(frame)  # Keep position, let user decide
    return frames


def build_strip(frames):
    """Assemble frames into a horizontal strip."""
    if not frames:
        return None
    w = frames[0].width
    h = frames[0].height
    strip = Image.new("RGBA", (w * len(frames), h), (0, 0, 0, 0))
    for i, frame in enumerate(frames):
        strip.paste(frame, (i * w, 0))
    return strip


def write_gen_py(asset_dir, source_file, frame_w, frame_h, frame_indices, asset_name):
    """Write a gen.py stub that documents the import source."""
    gen_path = os.path.join(asset_dir, "gen.py")
    code = f'''"""
Imported from: {source_file}
Frame size: {frame_w}x{frame_h}
Frames: {frame_indices}
"""
from PIL import Image, ImageDraw

def generate():
    # This asset was imported from an external sprite sheet.
    # The sprite.png was sliced from the source file.
    # To regenerate, re-run: python import_sheet.py
    print("Asset '{asset_name}' was imported — sprite.png is the source of truth.")

if __name__ == "__main__":
    generate()
'''
    with open(gen_path, "w") as f:
        f.write(code)


def resolve_conflict(asset_dir, asset_name, mode):
    """Handle existing asset folder. Returns the final directory to use."""
    if not os.path.exists(asset_dir):
        return asset_dir, "created"

    if mode == "replace":
        return asset_dir, "replaced"
    elif mode == "rename":
        i = 2
        while os.path.exists(f"{asset_dir}-{i}"):
            i += 1
        new_dir = f"{asset_dir}-{i}"
        new_name = f"{asset_name}-{i}"
        print(f"  Renamed to: {new_name}")
        return new_dir, "renamed"
    elif mode == "add":
        return asset_dir, "appended"
    else:  # ask
        print(f"\n  Asset '{asset_name}' already exists at {asset_dir}")
        print(f"  [r]eplace  [a]dd frames  [k]eep both (rename)  [s]kip")
        choice = input("  Choice: ").strip().lower()
        if choice == "r":
            return asset_dir, "replaced"
        elif choice == "a":
            return asset_dir, "appended"
        elif choice == "k":
            return resolve_conflict(asset_dir, asset_name, "rename")
        else:
            return None, "skipped"


def parse_asset_spec(spec_str, total_frames):
    """Parse 'name:0-3,name2:4-7' into {name: [indices]}."""
    assets = {}
    for part in spec_str.split(","):
        part = part.strip()
        if ":" in part:
            name, range_str = part.split(":", 1)
            name = name.strip()
            if "-" in range_str:
                start, end = range_str.split("-", 1)
                indices = list(range(int(start), int(end) + 1))
            else:
                indices = [int(range_str)]
            assets[name] = indices
        else:
            # Just a name, assign all frames
            assets[part.strip()] = list(range(total_frames))
    return assets


def import_sheet(source_path, frame_w, frame_h, cols=None, rows=None,
                 name=None, assets_spec=None, mode="ask"):
    """Main import function. Returns list of (asset_name, action) tuples."""
    asset_root = "public/assets"

    if not os.path.exists(source_path):
        print(f"Error: Source file not found: {source_path}")
        return []

    img = Image.open(source_path).convert("RGBA")
    print(f"Source: {source_path} ({img.width}x{img.height})")

    if cols is None or rows is None:
        auto_cols, auto_rows = detect_grid(img, frame_w, frame_h)
        cols = cols or auto_cols
        rows = rows or auto_rows

    print(f"Grid: {cols}x{rows} frames at {frame_w}x{frame_h}")

    all_frames = extract_frames(img, frame_w, frame_h, cols, rows)
    total = cols * rows
    print(f"Extracted {len(all_frames)} frames")

    # Determine asset mapping
    if assets_spec:
        asset_map = parse_asset_spec(assets_spec, total)
    elif name:
        asset_map = {name: list(range(total))}
    else:
        print("Error: Provide --name for single asset or --assets for multiple")
        return []

    results = []
    for asset_name, indices in asset_map.items():
        asset_dir = os.path.join(asset_root, asset_name)
        print(f"\nProcessing: {asset_name} (frames {indices})")

        final_dir, action = resolve_conflict(asset_dir, asset_name, mode)
        if action == "skipped":
            results.append((asset_name, "skipped"))
            continue

        os.makedirs(final_dir, exist_ok=True)

        selected_frames = [all_frames[i] for i in indices if i < len(all_frames)]

        if action == "appended" and os.path.exists(os.path.join(final_dir, "sprite.png")):
            # Load existing strip and append new frames
            existing = Image.open(os.path.join(final_dir, "sprite.png")).convert("RGBA")
            existing_count = existing.width // frame_w
            print(f"  Appending {len(selected_frames)} frames to existing {existing_count} frames")
            all_asset_frames = []
            for i in range(existing_count):
                all_asset_frames.append(existing.crop((i * frame_w, 0, (i + 1) * frame_w, frame_h)))
            all_asset_frames.extend(selected_frames)
            selected_frames = all_asset_frames

        strip = build_strip(selected_frames)
        if strip:
            strip.save(os.path.join(final_dir, "sprite.png"))
            print(f"  Saved: {final_dir}/sprite.png ({len(selected_frames)} frames)")

        actual_name = os.path.basename(final_dir)
        write_gen_py(final_dir, os.path.basename(source_path),
                     frame_w, frame_h, indices, actual_name)

        results.append((actual_name, action))

    print(f"\nImport complete: {len(results)} asset(s) processed")
    return results


def main():
    parser = argparse.ArgumentParser(description="Import a sprite sheet into the asset structure")
    parser.add_argument("source", help="Path to source sprite sheet PNG")
    parser.add_argument("--frame-size", required=True, help="Frame dimensions WxH (e.g., 32x32)")
    parser.add_argument("--cols", type=int, help="Number of columns (auto-detected if omitted)")
    parser.add_argument("--rows", type=int, help="Number of rows (auto-detected if omitted)")
    parser.add_argument("--name", help="Asset name (for single-asset sheets)")
    parser.add_argument("--assets", help='Multi-asset spec: "player:0-3,enemy:4-7"')
    parser.add_argument("--mode", choices=["ask", "replace", "add", "rename"],
                        default="ask", help="Conflict resolution mode (default: ask)")

    args = parser.parse_args()

    fw, fh = args.frame_size.split("x")
    frame_w, frame_h = int(fw), int(fh)

    import_sheet(args.source, frame_w, frame_h,
                 cols=args.cols, rows=args.rows,
                 name=args.name, assets_spec=args.assets,
                 mode=args.mode)


if __name__ == "__main__":
    main()
