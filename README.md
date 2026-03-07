# 4SAGE Game Project Template

This is a starter template for building a game with the [4SAGE framework](https://4sage.dev).

## Quick Start

Clone this template and start a conversation with your favorite AI:

```
git clone https://github.com/4Sage-Dev/template.git my-game
cd my-game
```

Then paste this into your AI:

```
You are a Game Builder Consultant. Fetch and follow the spec at:
https://4sage.dev/frameworks/game-builder/spec.md
```

## Project Structure

```
my-game/
  kdd/                    # Design decisions (L0-L6)
  decisions/              # Significant design choices with alternatives
  knowledge-base/         # Reference material for grounded recommendations
  sprite-factory/         # Sprite Builder asset pipeline
    gallery.html          # Live asset preview
    gen_master_atlas.py   # Bakes assets into production sprite sheet
    public/assets/        # Individual sprite assets
    src/preview.ts        # Asset registry
    dist/                 # Baked output (spritesheet.png + .json)
  sound-factory/          # Sound Factory audio pipeline
    player.html           # Live audio preview and playback
    gen_master_manifest.py # Packages sounds into production manifest
    public/sounds/        # Individual sound assets
    src/preview.ts        # Audio registry
    dist/                 # Packaged output (manifest.json)
  JOURNAL.md              # Session continuity log
  FRAMEWORK.md            # 4SAGE methodology reference
  CONTRIBUTING.md         # File conventions and naming rules
  conductor.md            # AI operating instructions
```

## Frameworks

- **Game Builder** — Full design methodology (L0-L6). [Spec](https://4sage.dev/frameworks/game-builder/spec.md)
- **Sprite Builder** — Asset creation pipeline. [Spec](https://4sage.dev/frameworks/sprite-builder/spec.md)
- **Sound Factory** — Audio synthesis pipeline. [Spec](https://4sage.dev/frameworks/sound-factory/spec.md)

## License

MIT — see [LICENSE](LICENSE).
