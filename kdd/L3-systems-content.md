# Level 3: Systems & Content Design

> **Priority:** Mix of SH and NH — systems implement the core design; content fills the world
> **Driven by:** L0 (scope, resources), L1 (experience goals), L2 (mechanics, progression)
> **Drives:** Presentation needs, architecture requirements, implementation scope

This level takes the mechanics and progression from L2 and expands them into
detailed, interconnected systems. It also defines the content that fills those
systems — narrative, levels, encounters, items, and everything the player
experiences. This is where the game becomes tangible.

This is typically the largest level, because most of the game's design detail
lives here. Each KDD below spawns extensive follow-on questions depending
on the game's genre and complexity.

---

## KDD-3.1: Game Economy

**Question:** What are the game's resources, currencies, and exchange systems?
How do resources flow?

**Why this matters:**
Nearly every game has an economy — even if it's just "health" and "ammo."
The economy is the circulatory system of the game: how resources are earned,
spent, stored, and lost. A well-designed economy creates meaningful choices.
A poorly designed one creates grind, inflation, or exploitation.

**Priority:** SH — Economy design directly implements the progression system
from L2 and must support the emotional goals from L1.

```answer
# Example:
economy:
  resources:
    - name: Raw Materials
      types: [wood, stone, metal, fiber]
      acquisition: Gathering from the environment
      storage: Player inventory (limited) + storage containers (expandable)
      consumption: Crafting, building

    - name: Knowledge Fragments
      acquisition: Exploring ruins, solving puzzles
      storage: Permanent — recorded in the journal
      consumption: Unlocking new crafting recipes, story progression

  currencies: None — no abstract currency; all trade is barter or crafting
  sinks: [crafting, building, tool wear]
  faucets: [gathering, exploration rewards, puzzle solutions]
  inflation_control: "Resources are regional — you must explore new areas for new materials"
```

**LLM follow-on areas:**
- Is the economy balanced? Are there infinite resource loops?
- Is there resource scarcity? Is it fun scarcity or frustrating scarcity?
- Does the economy support the session length from L1?
- Are there economic exploits that undermine the intended experience?
- How is resource abundance or scarcity communicated to the player?

---

## KDD-3.2: Detailed Mechanics Specification

**Question:** For each primary mechanic from L2, define the detailed rules
and parameters.

**Why this matters:**
L2 defined *what* the mechanics are. L3 defines *exactly how* they work —
the formulas, the parameters, the edge cases. This is where the game gets
balanced and tuned. Each mechanic needs enough detail that it could be
prototyped and tested.

**Priority:** SH — This is the detailed design that enables implementation.

```answer
# Example (crafting mechanic):
mechanic: crafting
  recipe_structure:
    inputs: "1-4 materials with quantities"
    outputs: "1 item"
    discovery: "Some recipes known from start; others discovered by experimentation"
    failure: "No failure — if you have materials, crafting always succeeds"
  crafting_stations:
    - name: Workbench
      unlocked: Start of game
      recipes: Basic tools, simple structures
    - name: Forge
      unlocked: After finding metal ore
      recipes: Metal tools, advanced structures
  tool_durability:
    enabled: true
    wear_rate: "Tools last 50-100 uses"
    repair: "Same materials as creation, at 50% cost"
    break_consequence: "Tool disappears; must craft a new one"
```

**LLM follow-on areas:**
- Are the parameters fun? (playtesting required)
- How do different mechanics interact at the detail level?
- Are there degenerate strategies or exploits?
- What are the tuning knobs for difficulty and pacing?
- What data needs to be configurable vs. hard-coded?

---

## KDD-3.3: Narrative & World Design

**Question:** What is the story, the world, and how is narrative delivered?

**Why this matters:**
Not every game has narrative — but the decision to include or exclude it
affects content scope, writing budget, localization needs, and player
expectations. If narrative is present, the delivery mechanism must be
designed to work *with* the core mechanics, not against them.

**Priority:** Varies by genre — MH for narrative-driven games, NH for
purely mechanical games.

```answer
# Example:
narrative:
  type: Environmental / Embedded
  delivery:
    - "Environmental storytelling — ruins tell the story through layout and artifacts"
    - "Journal entries — found documents that piece together the mystery"
    - "NPC dialogue — sparse, meaningful conversations with rare NPCs"
  structure:
    main_arc: "Discover what happened to the ancient civilization"
    side_stories: "Individual island histories, character backstories"
    pacing: "Story beats tied to exploration milestones, not time"
  player_narrative_agency: "Interpretation — the player pieces together the truth"
  voice_acting: false
  text_volume: "Moderate — ~30,000 words across all content"
  localization_scope: "English at launch; EFIGS planned"
world:
  setting: "Archipelago of islands in a vast ocean"
  generation: "Procedural island shapes with handcrafted points of interest"
  lore: "Ancient civilization that mastered the islands' natural forces"
  tone: "Mysterious, melancholic, beautiful"
```

**LLM follow-on areas:**
- Is the narrative scope achievable with the team (L0)?
- How is narrative pacing synchronized with mechanical progression?
- Does environmental storytelling require specific art/level design approaches?
- What is the localization strategy and cost?
- How is narrative completeness tracked by the player?

---

## KDD-3.4: Level / World Design

**Question:** How is the game world structured? What are the spaces the
player inhabits?

**Why this matters:**
Level design is where mechanics meet content. The game world must support
the core loop (L2), deliver the narrative (KDD-3.3), and create the
emotional experience (L1). World structure also directly impacts production
scope — a game with 50 handcrafted levels is a very different production
challenge than one with procedural generation.

**Priority:** SH — The structure is a design choice; the scope must be
realistic for L0 resources.

```answer
# Example:
world_structure:
  type: Open world — archipelago with discrete islands
  hub: "Player's home island — the base of operations"
  zones:
    - name: Starting Islands (3)
      difficulty: Beginner
      resources: Basic (wood, stone, fiber)
      content: Tutorial, basic crafting, first story fragments
    - name: Outer Islands (8-12, procedurally varied)
      difficulty: Intermediate
      resources: Intermediate (metal, rare plants)
      content: Main story, advanced crafting
    - name: Deep Islands (3-5)
      difficulty: Advanced
      resources: Rare materials
      content: Story climax, endgame crafting
  procedural_elements: "Island terrain, resource placement, minor ruins"
  handcrafted_elements: "Key story ruins, puzzle rooms, NPC locations"
```

**LLM follow-on areas:**
- Is the world size appropriate for the content scope and team?
- How does the player navigate between areas? (fast travel?)
- What is the ratio of procedural to handcrafted content?
- How is visual variety maintained across procedural content?
- How does the world teach the player without explicit tutorials?

---

## KDD-3.5: AI & NPC Design

**Question:** What non-player entities exist? How do they behave?

**Why this matters:**
NPCs, enemies, creatures, and autonomous systems require AI behavior design,
animation budgets, and testing effort. The complexity of AI directly impacts
architecture (L5) and implementation (L6). Even "simple" AI can become a
major production cost.

**Priority:** Varies — MH if combat or social interaction is core to the
game, NH if minimal.

```answer
# Example:
npcs:
  characters:
    - type: Rare hermit NPCs
      count: "5-8 across all islands"
      behavior: "Stationary, dialogue-based interaction"
      ai_complexity: "Minimal — dialogue tree with state tracking"
  creatures:
    - type: Wildlife
      behavior: "Ambient — wander, flee from player, ecosystem simulation"
      ai_complexity: "Simple — state machine (idle, wander, flee)"
      hostile: false
  enemies: None — this is a non-combat game
```

**LLM follow-on areas:**
- What AI architectures are needed? (state machines, behavior trees, GOAP)
- What is the testing burden for AI behavior?
- How do NPCs affect the narrative delivery?
- What animation requirements do NPCs create?
- How do creatures affect the game's atmosphere?

---

## KDD-3.6: Multiplayer Systems

**Question:** If multiplayer (from L1-KDD-1.4), how do the game systems
work in a multiplayer context?

**Why this matters:**
Multiplayer doesn't just add networking — it transforms every system.
Resource economies need anti-exploit design. Progression needs fairness
consideration. Content needs to work at multiple player counts. If the game
is single-player, this KDD is marked N/A and skipped.

**Priority:** MH if multiplayer is part of the game; N/A otherwise.

```answer
# Example:
multiplayer_systems: N/A — single-player game (see L1-KDD-1.4)
```

---

## How This Level Drives the Next

Once Level 3 is answered, the LLM can:

1. **Define art requirements** — world structure, NPC count, item variety,
   and environmental storytelling directly drive the art production pipeline
   at L4.

2. **Identify technical requirements** — procedural generation, AI complexity,
   economy simulation, and content volume define the architecture at L5.

3. **Scope the implementation** — detailed mechanics specifications become
   the engineering task list at L6.

4. **Estimate content production** — the world design and narrative scope
   define the content pipeline, which must be realistic for L0 resources.
