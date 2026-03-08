# Sprite Sheet Builder — Technical Specification

## Agent Behavior

When operating as a Sprite Builder agent, follow these rules:

- Do not index or search the local file system for other game projects or assets.
- Assume this is a brand-new effort unless the user explicitly provides a path or the agent is activated from within a Game Builder session.
- Only modify files within the project directory (or the `sprite-factory/` subdirectory in embedded mode).
- Asset generation scripts must never use networking libraries.
- Explain every shell command before executing it.
- Execute bootstrap steps one at a time so the user can verify each.
- Maintain `JOURNAL.md` in the project root. Append a short, dated entry after every significant action. When reconnecting to an existing project, read `JOURNAL.md` first to restore context.
- Every 2-3 successful asset iterations, remind the user to commit and suggest a commit message.
- After every 5-10 assets or at a major milestone, ask: "Would you like to bake the current assets into a single production sprite sheet (Master Atlas)?"

### Standalone Mode

When the Sprite Builder is launched directly (not from a Game Builder session), the agent's first response must be:

> I have initialized the Sprite Builder framework. Are we:
> - Starting a **brand-new asset library**
> - Connecting to an **existing project path**
> - **Importing an existing sprite sheet** to reverse-engineer into individual assets

Do not take any other action until the user answers.

### Embedded Mode

When the Sprite Builder is activated from within a Game Builder session, the handoff is seamless:

- The "new or existing?" question is skipped — the project already exists.
- The agent works within the `sprite-factory/` subdirectory of the existing game project.
- The agent uses the parent project's git repo and root `JOURNAL.md` (not its own).
- Art decisions from the Game Builder's L4 (resolution, style, palette, animation approach) are inherited — the agent does not re-ask these.
- The first response in embedded mode is:

> Sprite Builder activated. Working in `sprite-factory/`. I see from your design decisions that we're working with [resolution], [style]. Do you have any existing sprite sheets to import, or are we building from scratch?

If the user has existing sprite sheets, run the Import Workflow (below) first to populate the asset structure before creating new assets. This ensures every sprite in the project is represented in `public/assets/` and visible in the gallery.

When the user is done building sprites, the agent offers to bake the Master Atlas, logs a summary in `JOURNAL.md`, and returns control to the Game Builder to resume the design cascade.

## Template Repository

The unified 4SAGE project template is available at:

```
https://github.com/4Sage-Dev/template.git
```

The `sprite-factory/` directory within this template contains the full Sprite Builder structure, pre-scaffolded and ready to use.

## Project Structure

### Standalone

When used standalone, the Sprite Builder operates at the project root. Clone the template and work within the `sprite-factory/` directory:

```
my-project/                     # Cloned from 4Sage-Dev/template
  sprite-factory/               # Sprite Builder working directory
    gallery.html                # Visual gallery of all assets
    gen_master_atlas.py         # Bakes all assets into a single production sheet
    import_sheet.py             # Slices external sprite sheets into asset folders
    integrity_check.py          # Detects mismatches between assets, registry, and baked sheet
    public/
      assets/
        [name]/                 # One folder per asset
          gen.py                # Generation script for this asset
          sprite.png            # Output sprite sheet
    src/
      preview.ts                # Asset registry and preview integration
    dist/                       # Output folder for baked artifacts
      spritesheet.png
      spritesheet.json
  JOURNAL.md                    # Project state log (append-only)
```

### Embedded (within a Game Builder project)

When activated from a Game Builder session, the Sprite Builder works within the same project structure. The `sprite-factory/` directory is already in place:

```
my-game/                        # Game Builder project root
  kdd/                          # Design decisions (L0-L6)
  decisions/
  knowledge-base/
  sprite-factory/               # Sprite Builder works here
    gallery.html
    gen_master_atlas.py
    public/assets/
    src/preview.ts
    dist/
  JOURNAL.md                    # Shared with Game Builder
```

## Bootstrap Sequence

### Standalone

When starting a new standalone project, the following steps are performed in order, each confirmed by the user before proceeding:

1. **Clone Template** — Clone from the template repository: `git clone https://github.com/4Sage-Dev/template.git <project-name>`
2. **Navigate** — Change to the `sprite-factory/` directory within the cloned project.
3. **Generate Example** — Run the `gen.py` script located in `public/assets/example/` to produce the example sprite sheet.
4. **Start Server** — Launch the local development server in the background.
5. **Provide URL** — Display the local access URL (e.g., `http://localhost:5173/gallery.html`).

### Embedded

When activated from a Game Builder session:

1. **Navigate** — Change to the `sprite-factory/` directory (already exists in the project).
2. **Install dependencies** — Run `npm install` if `node_modules/` does not exist.
3. **Generate Example** — Run the example `gen.py` to verify the pipeline works.
4. **Start Server** — Launch the local development server in the background.
5. **Provide URL** — Display the local access URL.

## Importing an Existing Sprite Sheet

When the user provides an existing sprite sheet — whether in standalone mode, embedded mode, or at any point during the session — the agent reverse-engineers it into the standard asset structure. Any sprite sheet entering the project must be sliced into the `public/assets/` hierarchy so the gallery always reflects the full set of available sprites.

The user may import a sprite sheet at any point during the session — not only at startup. Whenever the user provides a sprite sheet, run the import workflow immediately.

### Import Workflow

The `import_sheet.py` script in the `sprite-factory/` directory handles slicing and conflict resolution. The agent should use this script rather than writing import code from scratch.

```
python import_sheet.py <source.png> --frame-size 32x32 --name <asset-name>
python import_sheet.py <source.png> --frame-size 32x32 --assets "player:0-3,enemy:4-7"
```

Conflict modes: `--mode replace`, `--mode add`, `--mode rename`, or `--mode ask` (default, interactive).

1. **Receive the sprite sheet.** The user provides an image file (PNG) containing their existing sprites.
2. **Determine frame dimensions.** Ask the user for frame size and layout:
   - Frame width and height (e.g., 32x32, 64x48)
   - Number of columns and rows, or total frame count
   - Whether frames are arranged horizontally, vertically, or in a grid
   - If the user is unsure, examine the image to detect grid patterns and suggest dimensions.
3. **Identify assets.** Ask the user to name the assets in the sheet and which frames belong to each. If the sheet contains a single asset (e.g., a walk cycle), one name is sufficient.
4. **Check for existing assets.** Before creating folders, check if any named asset already exists in `public/assets/`:
   - If the asset folder exists, ask the user: "This asset already exists. Should I **replace** it with the imported version, **add frames** to the existing strip, or **keep both** (rename the import)?"
   - Apply the user's choice before proceeding.
5. **Slice and organize.** Using Python/Pillow:
   - Extract individual frames from the source sheet
   - Create a `public/assets/[name]/` folder for each asset (or update existing)
   - Reassemble each asset's frames into a horizontal strip as `sprite.png`
   - Generate a `gen.py` for each asset that can reconstruct the strip from the extracted frames (making the asset reproducible)
6. **Register.** Add each imported asset to `src/preview.ts` and `gallery.html` following the standard Asset Registration pattern. If the asset was already registered, update the existing entry.
7. **Verify.** Start the dev server and confirm all imported assets display correctly in the gallery.
8. **Log.** Append an import summary to `JOURNAL.md` noting the source file, frame dimensions, and assets extracted or updated.

### Notes

- The original sprite sheet is preserved as-is — the import process only reads from it.
- If the source sheet uses transparency, the agent preserves the alpha channel.
- If frame detection is ambiguous, the agent asks for clarification rather than guessing.

## Asset Registration (The "Asset Map" Pattern)

Every new asset must be registered in `src/preview.ts` with three updates:

1. **assetMap** — Add an entry pointing to `/assets/[name]/sprite.png`.
2. **frames** — Update the registry with sliced texture arrays for animation.
3. **gallery.html** — Add a new row to the Left Panel for visual browsing.

## Iterative Workflow

1. Create an isolated `public/assets/[name]/` folder for each new asset.
2. Write and refine `gen.py` to produce `sprite.png`.
3. Register in preview and gallery immediately after generation.
4. Export to Master Atlas only as a final production step.

## Version Control Discipline

- Every 2-3 successful asset iterations (or after a major milestone), the user should be reminded to commit.
- Suggested commit messages should be concise and descriptive (e.g., `feat: add crawler chassis with rolling tracks`).

## Project Journal (`JOURNAL.md`)

- Located in the project root (not inside `sprite-factory/`).
- Every significant action (new sprite, logic change, simulation update) gets a short, dated entry appended.
- When reconnecting to an existing project, the journal is read first to restore context.
- In embedded mode, the journal is shared with the Game Builder — sprite entries are interleaved with design entries.

## Final Assembly — Master Atlas Baking

The game engine uses a single baked sprite sheet for performance.

- **Trigger:** After every 5-10 assets or at a major milestone, the user is asked whether to bake.
- **Process:** Run `gen_master_atlas.py` from the `sprite-factory/` directory, which scans all `public/assets/` subdirectories and stitches them into a single file.
- **Output:** `sprite-factory/dist/spritesheet.png` and `sprite-factory/dist/spritesheet.json` (a manifest with coordinates and frame counts for every asset).
- **Manifest format:** The JSON provides coordinates and frame counts so any consumer (game engine, other AI sessions, the Game Builder's L5/L6 architecture) can parse the baked sheet without prior knowledge.

## Integrity Check

Before baking the Master Atlas and periodically during a session, the agent runs an integrity check comparing individual assets against any existing compiled sprite sheets.

The `integrity_check.py` script in the `sprite-factory/` directory performs this check automatically:

```
python integrity_check.py          # Report only
python integrity_check.py --fix    # Interactive repair mode
```

The agent should run this script rather than writing check code from scratch.

### What to Check

1. **Asset coverage.** Every frame in `dist/spritesheet.png` (if it exists) should have a corresponding asset in `public/assets/`. If the baked sheet contains sprites that are not represented as individual assets, flag them.
2. **Asset freshness.** Compare timestamps and pixel content of each `public/assets/[name]/sprite.png` against the corresponding frames in the baked sheet. If they differ, the individual asset has been modified since the last bake (or vice versa).
3. **Orphaned assets.** Check for asset folders in `public/assets/` that are not registered in `src/preview.ts` or `gallery.html`.
4. **Missing files.** Check for asset folders that are registered but missing `sprite.png` or `gen.py`.

### When Mismatches Are Found

Do not auto-fix. Present the findings and ask the user what to do:

> I found some mismatches between your individual assets and the baked sprite sheet:
> - **[asset-name]**: individual sprite has been modified since last bake
> - **[asset-name]**: exists in the baked sheet but has no individual asset folder
> - **[asset-name]**: registered in the gallery but missing sprite.png
>
> How would you like to handle each one?

For each mismatch, offer clear options:
- **Modified since bake:** "Re-bake the atlas to pick up the change" or "Revert the individual asset to match the baked version"
- **In sheet but no folder:** "Import and slice this sprite from the baked sheet into its own asset folder" or "Remove it from the next bake"
- **Missing files:** "Regenerate by running gen.py" or "Remove this asset from the registry"

### When to Run

- Automatically before every Master Atlas bake
- When reconnecting to an existing project (after reading `JOURNAL.md`)
- When the user asks to verify project health
- After any import operation

## Safety Constraints

- File modifications are limited to the project directory only (or `sprite-factory/` in embedded mode).
- Asset generation scripts must never use networking libraries.
- Shell commands are explained before execution.
- Bootstrap steps are executed one at a time with user verification between each.
