# Sound Factory — Technical Specification

## Agent Behavior

When operating as a Sound Factory agent, follow these rules:

- Do not index or search the local file system for other game projects or audio files.
- Assume this is a brand-new effort unless the user explicitly provides a path or the agent is activated from within a Game Builder session.
- Only modify files within the project directory (or the `sound-factory/` subdirectory in embedded mode).
- Audio generation scripts must never use networking libraries.
- Explain every shell command before executing it.
- Execute bootstrap steps one at a time so the user can verify each.
- Maintain `JOURNAL.md` in the project root. Append a short, dated entry after every significant action. When reconnecting to an existing project, read `JOURNAL.md` first to restore context.
- Every 2-3 successful audio iterations, remind the user to commit and suggest a commit message.
- After every 5-10 sounds or at a major milestone, ask: "Would you like to package the current sounds into a production audio manifest?"

### Standalone Mode

When the Sound Factory is launched directly (not from a Game Builder session), the agent's first response must be:

> I have initialized the Sound Factory framework. Are we:
> - Starting a **brand-new sound library**
> - Connecting to an **existing project path**
> - **Importing existing audio files** to organize into the asset structure

Do not take any other action until the user answers.

### Embedded Mode

When the Sound Factory is activated from within a Game Builder session, the handoff is seamless:

- The "new or existing?" question is skipped — the project already exists.
- The agent works within the `sound-factory/` subdirectory of the existing game project.
- The agent uses the parent project's git repo and root `JOURNAL.md` (not its own).
- Audio direction decisions from the Game Builder's L4 (style, tone, format, sample rate) are inherited — the agent does not re-ask these.
- The first response in embedded mode is:

> Sound Factory activated. Working in `sound-factory/`. I see from your design decisions that the audio style is [style]. Do you have any existing audio files to import, or are we building from scratch?

If the user has existing audio files, run the Import Workflow (below) first to populate the asset structure before creating new sounds. This ensures every sound in the project is represented in `public/sounds/` and visible in the player.

When the user is done building sounds, the agent offers to package the manifest, logs a summary in `JOURNAL.md`, and returns control to the Game Builder to resume the design cascade.

## Template Repository

The unified 4SAGE project template is available at:

```
https://github.com/4Sage-Dev/template.git
```

The `sound-factory/` directory within this template contains the full Sound Factory structure, pre-scaffolded and ready to use.

## Project Structure

### Standalone

When used standalone, the Sound Factory operates within the cloned template:

```
my-project/                     # Cloned from 4Sage-Dev/template
  sound-factory/                # Sound Factory working directory
    player.html                 # Audio preview and playback page
    gen_master_manifest.py      # Packages all sounds into a production manifest
    import_audio.py             # Imports external audio files into sound folders
    integrity_check.py          # Detects mismatches between sounds, registry, and manifest
    public/
      sounds/
        [name]/                 # One folder per sound
          gen.py                # Generation script for this sound
          sound.wav             # Output audio file
    src/
      preview.ts                # Audio registry and playback integration
    dist/                       # Output folder for packaged artifacts
      manifest.json             # Production manifest with metadata
  JOURNAL.md                    # Project state log (append-only)
```

### Embedded (within a Game Builder project)

When activated from a Game Builder session, the Sound Factory works within the same project structure. The `sound-factory/` directory is already in place:

```
my-game/                        # Game Builder project root
  kdd/                          # Design decisions (L0-L6)
  decisions/
  knowledge-base/
  sprite-factory/               # Sprite Builder
  sound-factory/                # Sound Factory works here
    player.html
    gen_master_manifest.py
    public/sounds/
    src/preview.ts
    dist/
  JOURNAL.md                    # Shared with Game Builder
```

## Bootstrap Sequence

### Standalone

When starting a new standalone project, the following steps are performed in order, each confirmed by the user before proceeding:

1. **Clone Template** — Clone from the template repository: `git clone https://github.com/4Sage-Dev/template.git <project-name>`
2. **Navigate** — Change to the `sound-factory/` directory within the cloned project.
3. **Install Dependencies** — Run `pip install numpy scipy` if not already installed (required for audio synthesis).
4. **Generate Example** — Run the `gen.py` script located in `public/sounds/example/` to produce the example sound.
5. **Start Server** — Launch the local development server in the background.
6. **Provide URL** — Display the local access URL (e.g., `http://localhost:5174/player.html`).

### Embedded

When activated from a Game Builder session:

1. **Navigate** — Change to the `sound-factory/` directory (already exists in the project).
2. **Install Dependencies** — Run `npm install` if `node_modules/` does not exist, and verify Python dependencies (`numpy`, `scipy`).
3. **Generate Example** — Run the example `gen.py` to verify the pipeline works.
4. **Start Server** — Launch the local development server in the background.
5. **Provide URL** — Display the local access URL.

## Audio Generation Approach

The Sound Factory uses Python scripts to synthesize audio programmatically. Each sound is generated by a `gen.py` script that produces a `.wav` file using standard libraries.

### Recommended Libraries

- **numpy** — waveform generation (sine, square, sawtooth, noise)
- **scipy.io.wavfile** — writing WAV files
- **scipy.signal** — filters, envelopes, frequency sweeps

These are sufficient for a wide range of game audio:

### What Works Well

- **Retro/chiptune effects** — laser shots, pickups, power-ups, jumps, 8-bit explosions
- **UI sounds** — button clicks, menu hovers, confirmations, error tones
- **Ambient tones** — engine hums, electrical buzzing, wind, room tone
- **Alert sounds** — alarms, notifications, warning beeps
- **Procedural variations** — randomized pitch, timing, and decay for organic feel
- **Simple music** — chiptune melodies, ambient loops, drum patterns using synthesized percussion

### Generation Pattern

Every `gen.py` script follows this pattern:

```python
import numpy as np
from scipy.io import wavfile

SAMPLE_RATE = 44100

def generate():
    # Build waveform using numpy
    # Apply envelope (attack, decay, sustain, release)
    # Apply effects (reverb, filter, distortion)
    # Normalize to 16-bit range
    # Write to sound.wav
    pass

if __name__ == "__main__":
    generate()
```

The agent always explains what the script will produce before generating: waveform type, duration, frequency range, envelope shape, and intended game use.

## Sound Registration (The "Sound Map" Pattern)

Every new sound must be registered in `src/preview.ts` with two updates:

1. **soundMap** — Add an entry pointing to `/sounds/[name]/sound.wav`.
2. **player.html** — Add a new row to the sound list with a play button.

## Iterative Workflow

1. Create an isolated `public/sounds/[name]/` folder for each new sound.
2. Write and refine `gen.py` to produce `sound.wav`.
3. Register in the player page immediately after generation.
4. Package into the production manifest only as a final step.

## Importing Existing Audio Files

When the user provides existing audio files — whether in standalone mode, embedded mode, or at any point during the session — the agent organizes them into the standard structure. Any audio file entering the project must be placed into the `public/sounds/` hierarchy so the player always reflects the full set of available sounds.

The user may import audio files at any point during the session — not only at startup. Whenever the user provides audio files, run the import workflow immediately.

The `import_audio.py` script in the `sound-factory/` directory handles conversion and conflict resolution. The agent should use this script rather than writing import code from scratch.

```
python import_audio.py <source-file> --name <sound-name> --category effect
python import_audio.py <source-file1> <source-file2> --names "laser,explosion" --category effect
```

Conflict modes: `--mode replace`, `--mode rename`, or `--mode ask` (default, interactive).

### Import Workflow

1. **Receive the audio files.** The user provides one or more audio files (WAV, OGG, MP3).
2. **Identify and name.** Ask the user to name each sound and categorize it (effect, ambient, music, UI).
3. **Check for existing sounds.** Before creating folders, check if any named sound already exists in `public/sounds/`:
   - If the sound folder exists, ask the user: "This sound already exists. Should I **replace** it with the imported version or **keep both** (rename the import)?"
   - Apply the user's choice before proceeding.
4. **Organize.** For each sound:
   - Create a `public/sounds/[name]/` folder (or update existing)
   - Copy or convert the audio file to `sound.wav` (WAV format, target sample rate)
   - Generate a `gen.py` stub that documents the source file and conversion parameters
5. **Register.** Add each imported sound to `src/preview.ts` and `player.html`. If the sound was already registered, update the existing entry.
6. **Verify.** Start the dev server and confirm all imported sounds play correctly.
7. **Log.** Append an import summary to `JOURNAL.md` noting source files and sounds imported or updated.

### Notes

- Original files are preserved — the import process copies, never moves or modifies originals.
- Audio is converted to a consistent format (WAV, 44100 Hz, 16-bit) for uniformity.
- The `gen.py` stub for imported sounds documents the source but cannot regenerate the audio from scratch (unlike synthesized sounds).

## Version Control Discipline

- Every 2-3 successful sound iterations (or after a major milestone), the user should be reminded to commit.
- Suggested commit messages should be concise and descriptive (e.g., `feat: add airlock hiss with pressure release decay`).
- Audio files (WAV) can be large. The agent should note when the repository is growing and suggest `.gitattributes` with Git LFS for audio files if needed.

## Project Journal (`JOURNAL.md`)

- Located in the project root (not inside `sound-factory/`).
- Every significant action (new sound, parameter tweak, import) gets a short, dated entry appended.
- When reconnecting to an existing project, the journal is read first to restore context.
- In embedded mode, the journal is shared with the Game Builder — sound entries are interleaved with design and sprite entries.

## Final Assembly — Production Manifest

The game engine references sounds through a production manifest.

- **Trigger:** After every 5-10 sounds or at a major milestone, the user is asked whether to package.
- **Process:** Run `gen_master_manifest.py` from the `sound-factory/` directory, which scans all `public/sounds/` subdirectories and builds the manifest.
- **Output:** `sound-factory/dist/manifest.json` containing metadata for every sound.
- **Manifest format:**

```json
{
  "sounds": {
    "laser-shot": {
      "file": "sounds/laser-shot/sound.wav",
      "category": "effect",
      "duration": 0.3,
      "sampleRate": 44100,
      "channels": 1
    },
    "ambient-hum": {
      "file": "sounds/ambient-hum/sound.wav",
      "category": "ambient",
      "duration": 5.0,
      "loop": true,
      "sampleRate": 44100,
      "channels": 1
    }
  }
}
```

The manifest provides enough metadata for any consumer (game engine, other AI sessions, the Game Builder's L5/L6 architecture) to integrate the audio without prior knowledge.

## Integrity Check

Before packaging the production manifest and periodically during a session, the agent runs an integrity check comparing individual sounds against the packaged manifest and the player registrations.

The `integrity_check.py` script in the `sound-factory/` directory performs this check automatically:

```
python integrity_check.py          # Report only
python integrity_check.py --fix    # Interactive repair mode
```

The agent should run this script rather than writing check code from scratch.

### What to Check

1. **Sound coverage.** Every entry in `dist/manifest.json` (if it exists) should have a corresponding sound in `public/sounds/`. If the manifest references sounds that are not represented as individual assets, flag them.
2. **Sound freshness.** Compare timestamps of each `public/sounds/[name]/sound.wav` against the manifest. If a sound has been modified since the last package, flag it.
3. **Orphaned sounds.** Check for sound folders in `public/sounds/` that are not registered in `src/preview.ts` or `player.html`.
4. **Missing files.** Check for sound folders that are registered but missing `sound.wav` or `gen.py`.

### When Mismatches Are Found

Do not auto-fix. Present the findings and ask the user what to do:

> I found some mismatches between your individual sounds and the production manifest:
> - **[sound-name]**: sound file has been modified since last package
> - **[sound-name]**: exists in the manifest but has no individual sound folder
> - **[sound-name]**: registered in the player but missing sound.wav
>
> How would you like to handle each one?

For each mismatch, offer clear options:
- **Modified since package:** "Re-package the manifest to pick up the change" or "Revert the sound to match the packaged version"
- **In manifest but no folder:** "Remove from the next manifest build"
- **Missing files:** "Regenerate by running gen.py" or "Remove this sound from the registry"

### When to Run

- Automatically before every manifest package
- When reconnecting to an existing project (after reading `JOURNAL.md`)
- When the user asks to verify project health
- After any import operation

## Safety Constraints

- File modifications are limited to the project directory only (or `sound-factory/` in embedded mode).
- Audio generation scripts must never use networking libraries.
- Shell commands are explained before execution.
- Bootstrap steps are executed one at a time with user verification between each.
