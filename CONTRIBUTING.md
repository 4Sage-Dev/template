# Contributing to 4SAGE

This document explains how to work with the project files — whether you're a
human, Claude, Gemini, GPT, or any other LLM assistant.

## Project Conventions

### File Formats

All documentation is **Markdown** (`.md`). Tools (when added) will be
**Python** (`.py`). No proprietary formats. Everything is readable with a
text editor.

### Priority Labels

Used throughout KDD and design files:
- **MH** = must-have (non-negotiable — physics, platform requirements, budget)
- **SH** = should-have (strong default — industry best practice, proven patterns)
- **NH** = nice-to-have (opportunistic — improves the game but trade off against scope)
- **WH** = won't-have (explicitly excluded — prevents scope creep and revisiting)

### Naming Conventions

| Layer | Convention | Example |
|-------|-----------|---------|
| Design elements (in markdown) | PascalCase singular | `Player Character` |
| Properties (in markdown) | snake_case | `movement_speed` |
| File names | lowercase hyphenated | `core-design.md` |

## How to Read the Project

**Start with these files, in order:**

1. `README.md` — project overview and orientation
2. `FRAMEWORK.md` — the full methodology
3. `kdd/README.md` — how the decision cascade works
4. `kdd/L0-vision.md` — first KDD level (read L0 → L1 → ... → L6)
5. `decisions/README.md` — how design decisions are logged

## How to Write / Edit Files

### KDD Files (`kdd/L*.md`)

Follow the format established in `kdd/L0-vision.md`:

- Header with priority, driven-by, and drives metadata
- Intro paragraph explaining the level
- KDDs, each with:
  - `## KDD-{level}.{number}: Title`
  - `**Question:**` — the decision to be made
  - `**Why this matters:**` — rationale
  - `**Priority:**` — MH/SH/NH with explanation
  - `**Best practice default:**` — the industry convention
  - An `answer` fenced block with example YAML
  - `**LLM follow-on areas:**` — bullet list of generated questions
- Closing section: "How This Level Drives the Next"

### Decision Log (`decisions/`)

**Every significant decision must be logged.** This is a core 4SAGE principle:
*"You know not just what you chose but what you chose instead of and why."*

Each entry follows this format:

```
### D-{number}: Short title

**Date:** YYYY-MM-DD
**Context:** What prompted this decision
**Decided:** What was chosen
**Alternatives considered:**
- Alternative A — rejected because: reason
- Alternative B — rejected because: reason
**Rationale:** Why the chosen option wins
**References:** Links to main files where this decision appears
```

In main files, add `→ D-{number}` next to the decision point so readers can
find the full reasoning. Decision IDs are sequential and never reused.

### Structured Block Types

Within KDD documents and design files, these fenced block types carry
structured information:

| Block Type | Purpose | Used In |
|------------|---------|---------|
| `mechanic:` | Game mechanic definition with properties | Design documents |
| `system:` | Game system with components and interactions | Design documents |
| `state:` | State machine definitions with valid transitions | Design documents |
| `flow:` | Sequence of steps with a trigger | Design documents |
| `decision:` | Design choices with conditions | Design documents, KDD |
| `rule:` | Invariants that must always hold | Design documents |
| `directive:` | Architectural constraints with rationale | Architecture decisions |
| `answer:` | Captured response to a KDD question | KDD documents |

These blocks are embedded in natural language narrative. The document reads
as prose; the blocks provide machine-parseable precision where needed.

## Specs and Tools Must Stay in Sync

The `specs/` directory contains the framework specifications that LLMs fetch
and follow. These specs describe the tools in `sprite-factory/` and
`sound-factory/`. **When you modify a tool, you must update the corresponding
spec. When you add a new tool, you must add it to the spec.**

Before committing changes to tools or specs, run:

```
python verify_sync.py
```

This checks that every tool is referenced in its spec and every spec reference
points to a tool that exists. Do not commit if the verifier reports issues.

The specs are the source of truth for the website. After updating specs here,
run `sync_specs.py` in the website repo (`4Sage-Dev/4sage.dev`) to deploy them.

## Git Workflow

- `main` branch should always be consistent
- Use descriptive commit messages
- Commit related changes together
- Run `python verify_sync.py` before committing tool or spec changes

## LLM-Specific Notes

### For Claude Code
Claude Code will automatically read `CLAUDE.md` in the project root for context.
That file points to this README and CONTRIBUTING guide.

### For Gemini
Read `README.md` and `CONTRIBUTING.md` first. The project is structured so
that reading files in the order listed under "How to Read the Project" gives
you full context.

### For Any LLM
- All project knowledge is in the files — there's no external database or API.
- The structured blocks are machine-parseable.
- When adding new content, follow existing files as templates.
- When in doubt, `kdd/L0-vision.md` is the reference implementation for KDD files.
- Consult the `knowledge-base/` directory for genre conventions and platform
  constraints to avoid hallucinating game design realities.
