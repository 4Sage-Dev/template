# Level 2: Core Design

> **Priority:** Mix of SH and NH — mechanics are creative choices constrained by vision and experience
> **Driven by:** L0 (concept, platform, resources), L1 (emotional goals, session structure)
> **Drives:** Systems design, content, presentation, architecture

This level defines what the player *does* — the core game loop, the primary
mechanics, and the progression systems. These are the "Mechanics" and
"Dynamics" of MDA: the rules and the emergent behavior they create.

This is where the game's identity takes concrete shape. L0 said "survival
exploration game" and L1 said "curiosity and calm." L2 defines *how* the
player explores and *what makes it feel curious and calm.*

---

## KDD-2.1: Core Game Loop

**Question:** What is the core loop — the cycle of actions the player repeats
most frequently?

**Why this matters:**
The core loop is the heartbeat of the game. Players will experience it
hundreds or thousands of times. If the core loop is not inherently
satisfying, no amount of content or polish can save the game. The loop must
serve the emotional goals from L1 and be executable within the session
length constraints.

**Priority:** MH — The core loop is the game. Everything else supports it.

```answer
# Example (driven by L0: survival/exploration, L1: curiosity + satisfaction):
core_loop:
  steps:
    1: "Explore — move through the world, discover new areas"
    2: "Gather — collect resources and information"
    3: "Craft/Build — use resources to create tools, structures, knowledge"
    4: "Unlock — new areas, abilities, or story become accessible"
  cycle_time: "10-15 minutes per full loop iteration"
  satisfaction_source: "Tangible progress — visible base growth, map reveal"
  emotional_map:
    explore: curiosity
    gather: anticipation
    craft: satisfaction
    unlock: wonder
```

**LLM follow-on areas:**
- Does each step in the loop serve an L1 emotional goal?
- Is the cycle time compatible with the session length (L1)?
- What genre conventions exist for this type of loop?
- What is the player doing moment-to-moment in each step?
- Where is the decision-making? (Player agency within the loop)
- What prevents the loop from becoming tedious after 100 iterations?

---

## KDD-2.2: Primary Mechanics

**Question:** What are the 3–5 mechanics the player uses most? How do they work?

**Why this matters:**
Primary mechanics are what the player interacts with most. They must be
intuitive enough to learn quickly, deep enough to stay interesting, and
aligned with the emotional goals from L1. Each mechanic should have clear
verbs (move, shoot, build, trade, negotiate) and clear feedback.

**Priority:** SH — Genre conventions define expected mechanics; specific
implementation is a creative choice.

```answer
# Example:
mechanics:
  - name: Exploration/Movement
    verbs: [walk, swim, climb, sail]
    depth: "Simple movement with environmental puzzles"
    feedback: "Map reveals, visual landmarks, ambient audio changes"

  - name: Resource Gathering
    verbs: [harvest, mine, fish, forage]
    depth: "Context-sensitive — different tools for different materials"
    feedback: "Satisfying collection sounds, inventory fills visibly"

  - name: Crafting
    verbs: [combine, build, upgrade]
    depth: "Recipe-based with discovery — experiment to find new recipes"
    feedback: "Preview before build, satisfying construction animation"

  - name: Environmental Puzzle
    verbs: [observe, interact, rearrange]
    depth: "Logic puzzles using game world physics and mechanics"
    feedback: "Cascading reactions, environmental transformation"
```

**LLM follow-on areas:**
- How do these mechanics interact with each other?
- Are there secondary mechanics that emerge from combinations?
- What input complexity does each mechanic require? (fits platform from L0?)
- What is the skill ceiling for each mechanic?
- How do these mechanics compare to genre conventions?

---

## KDD-2.3: Progression Systems

**Question:** How does the player advance? What changes as the game
progresses?

**Why this matters:**
Progression is what gives the player a sense of growth and forward momentum.
It can be character-based (leveling, skill trees), world-based (unlocking
areas, building a base), knowledge-based (learning secrets, understanding
systems), or narrative-based (story advancement). The progression system
must match the emotional goals and the retention model from L1.

**Priority:** SH — Progression is expected in almost all genres, but the
form varies enormously.

```answer
# Example:
progression:
  primary:
    type: World-based
    description: "Unlock new islands, expand the base, reveal the map"
    pacing: "New island roughly every 2-3 hours"
  secondary:
    type: Knowledge-based
    description: "Discover crafting recipes, lore fragments, ancient language"
    pacing: "Continuous — something new in every session"
  character:
    type: Minimal
    description: "No experience levels; player improves through better tools"
  gates:
    - "New areas require specific crafted tools (boat, climbing gear)"
    - "Story progression unlocks understanding of ancient mechanisms"
  anti_patterns:
    - "No grinding — progression is gated by exploration, not repetition"
```

**LLM follow-on areas:**
- Is the progression pacing realistic for the content scope (L0 resources)?
- Does the progression system support or undermine the session structure (L1)?
- How is progression saved and communicated to the player?
- What happens if the player hits a progression wall?
- Is progression linear, branching, or open?

---

## KDD-2.4: Player Agency & Choice

**Question:** What meaningful choices does the player make? What are the
consequences?

**Why this matters:**
Agency is what separates games from movies. The player must feel that their
choices matter — but the scope and permanence of choices must match the
game's emotional goals. A game about "calm exploration" might offer spatial
choices (where to go) rather than moral dilemmas. A narrative RPG might
offer branching story choices with permanent consequences.

**Priority:** SH — The type and weight of player agency is a defining
design characteristic.

```answer
# Example:
agency:
  spatial: "Full freedom — explore islands in any order"
  strategic: "Choose which tools to craft, how to build the base"
  narrative: "Minor choices — NPC dialogue options, lore interpretation"
  consequence_weight: "Low — no permanent failures, reversible choices"
  branching: "Minimal — the main mystery has one resolution"
```

**LLM follow-on areas:**
- Does the level of agency match the audience expectations (L0)?
- Are there any illusions of choice that should be avoided?
- How is consequence communicated to the player?
- Does the game allow experimentation without punishment?

---

## KDD-2.5: Win/Lose Conditions & Game States

**Question:** How does the game end? Can the player fail? What states
can the game be in?

**Why this matters:**
Win and lose conditions define the stakes. Some games have clear victory
conditions (defeat the boss, solve the puzzle). Some are open-ended
(sandbox, simulation). Some have no failure state at all (walking simulators).
This must be consistent with the challenge philosophy from L1.

**Priority:** SH — Genre conventions set expectations; specific conditions
are creative choices.

```answer
# Example:
game_states:
  win_condition: "Solve the central mystery — discover the civilization's fate"
  lose_condition: "None — the player cannot permanently fail"
  failure_handling: "Temporary setbacks — lose some carried resources, respawn"
  end_state: "Credits roll after mystery resolution; open play continues"
  game_over: false
  states:
    - exploring: "Normal gameplay"
    - building: "Construction mode"
    - story_event: "Triggered narrative sequences (skippable)"
    - post_game: "Continue playing after main story completes"
```

**LLM follow-on areas:**
- Does the lack of a lose condition reduce tension too much?
- How does the game maintain engagement without failure stakes?
- Is there a satisfying final moment or climax?
- How does the post-game work?
- Does the genre typically have win/lose conditions?

---

## KDD-2.6: Camera & Perspective

**Question:** What is the player's viewpoint of the game world?

**Why this matters:**
Camera perspective is a mechanical decision with enormous downstream impact.
It determines what the player can see (information access), how they interact
with space (2D vs. 3D navigation), how art is created (L4), and what engine
features are needed (L5). Changing camera perspective late in development
is often as expensive as rebuilding the game.

**Priority:** MH — Once committed, changing perspective is extremely expensive.

```answer
# Example:
camera:
  type: Third-person
  distance: "Close follow, adjustable zoom"
  rotation: "Full 360° player-controlled"
  special_modes:
    - "First-person zoom for examining objects"
    - "Overhead view for base building"
```

**LLM follow-on areas:**
- Does this perspective serve the emotional goals (L1)?
- Does it match genre conventions?
- What are the art production implications?
- What are the input implications? (e.g., camera control on controller vs. mouse)
- Does the perspective support the game's information needs?

---

## How This Level Drives the Next

Once Level 2 is answered, the LLM can:

1. **Design Level 3 systems around the core loop** — each step in the core
   loop becomes one or more systems that need detailed design (resource
   economy, crafting system, world generation, narrative delivery).

2. **Scope content realistically** — progression pacing and game length
   define how much content is needed, which must be achievable with L0 resources.

3. **Identify mechanical conflicts** — if two mechanics compete for the
   same player attention or input, resolve it before building systems.

4. **Set art and audio direction** — camera perspective and mechanics
   determine what needs to be visible and how the player perceives space.
