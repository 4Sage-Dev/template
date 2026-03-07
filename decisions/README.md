# Decision Log

This directory records the reasoning behind significant project decisions —
what was chosen, what was considered, and why alternatives were rejected.

## Why This Exists

The 4SAGE Framework principle: *"You know not just what you chose but what
you chose instead of and why."*

Keeping decision rationale separate from the main files prevents clutter
while preserving full traceability.

## How It Works

1. **Main files** contain a short reference like `→ D-001` next to any
   significant choice.
2. **This directory** contains the full reasoning in topic-organized files.
3. Each decision has an ID, the choice made, alternatives considered with
   rejection reasons, and the date.

## Decision ID Format

`D-{number}` — sequential, never reused. If a decision is superseded, the
old entry gets a "Superseded by D-xxx" note rather than being deleted.

## Files

| File | Covers |
|------|--------|
| `framework.md` | Naming, methodology, structure decisions about the framework itself |

Additional topic files will be created as the project grows (e.g.,
`design.md`, `architecture.md`, `presentation.md`).

## Decision Entry Format

```
### D-001: Short title

**Date:** YYYY-MM-DD
**Context:** What prompted this decision
**Decided:** What was chosen
**Alternatives considered:**
- Alternative A — rejected because: reason
- Alternative B — rejected because: reason
**Rationale:** Why the chosen option wins
**References:** Links to main files where this decision appears
```
