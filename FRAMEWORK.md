# The 4SAGE Framework

> An open framework for designing games through hierarchical decision
> cascades, guided by AI-assisted dialogue.

## Purpose

The 4SAGE Framework separates *what a game should be* from *how it is built*
by organizing design decisions into a hierarchy where higher-level answers
progressively constrain lower-level choices. An LLM conducts interactive
dialogues at each level, generating context-aware follow-on questions from
a set of pre-planned Key Design Decisions.

The output is a set of structured, version-controlled documents that serve
as the single source of truth for the entire game design — readable by
humans, parseable by machines, and durable across technology changes.

## Core Principles

### 1. Decisions Cascade Downward

Every design decision exists at a level. Answers at higher levels constrain
the options available at lower levels. Vision determines experience goals.
Experience goals shape mechanics. Mechanics drive content design. Content
drives presentation. Presentation constrains technology. Technology guides
implementation.

This is not optional structure — it reflects reality. You cannot choose an
engine before you know your visual fidelity requirements. You cannot design
level layouts before you know your core mechanics. You cannot define your
core mechanics before you know what experience you're trying to create.

*Borrowed from: Lafley & Martin's Strategy Choice Cascade*

### 2. The Cascade Is Iterative

Sometimes a lower-level answer reveals that a higher-level choice is
infeasible or suboptimal. The framework supports upward feedback — surfacing
a constraint discovered at L5 (Architecture) that forces a reconsideration
at L2 (Core Design). This is not a failure; it is the system working.

*Borrowed from: Strategy Choice Cascade ("reverse engineering")*

### 3. Every Decision Has a Priority

Each decision is classified by how much flexibility exists:

| Priority | Label | Meaning |
|----------|-------|---------|
| **MH** | Must-Have | Non-negotiable. Platform requirements, physics, budget limits, existing commitments. Facts to be recorded, not choices to be made. |
| **SH** | Should-Have | Strongly recommended. Industry best practice, genre conventions, proven patterns. Deviation requires documented justification. |
| **NH** | Nice-to-Have | Opportunistic. Improves the game but trade off against scope, cost, and timeline. |
| **WH** | Won't-Have | Explicitly excluded. Documenting what you chose *not* to do prevents scope creep and revisiting settled decisions. |

When decisions conflict, higher priority wins. A Nice-to-Have never
overrides a Must-Have.

*Borrowed from: MoSCoW (DSDM)*

### 4. Six Questions at Every Level

At each level of the cascade, decisions are examined across six dimensions:

| Dimension | Question |
|-----------|----------|
| **What** | What elements, systems, or artifacts are involved? |
| **How** | How do they interact, transform, or flow? |
| **Where** | Where does this happen — in the game world, on screen, in the system? |
| **Who** | Who is the player? Who on the team is responsible? |
| **When** | When does it occur — sequence, frequency, triggers, pacing? |
| **Why** | Why does this decision matter? What is the rationale? |

Not every dimension applies to every decision, but the framework ensures
none are overlooked.

*Borrowed from: Zachman Framework (six interrogatives)*

### 5. Best Practice First, Then Diverge

At every level, the framework presents the established industry convention
as the default. The dialogue then asks: does this fit your game? Where it
does, adopt it. Where it doesn't, document the divergence and the
justification.

This is faster than starting from blank, more disciplined than unconstrained
design, and produces better documentation.

*Borrowed from: SAP Activate (fit-to-standard)*

### 6. The AI Is the Guide, Not the Authority

The AI conducts the dialogue, generates follow-on questions, identifies
gaps, and suggests best practices. But every decision is made by a human
and recorded as a human decision. The LLM's role is to ensure thoroughness
— to ask the questions that a team of experienced game designers would ask
— not to make choices (unless the human delegates — see Principle 9).

The AI is also frank. When a decision contradicts best practice or
introduces significant risk, the AI says so directly — explaining the
concern, citing the convention, and letting the designer decide with full
information. Honest feedback over polite agreement.

To prevent hallucination, the LLM must consult the `knowledge-base/`
directory (containing genre conventions, platform constraints, and design
patterns) before finalizing KDDs.

*Original to 4SAGE (LLM-guided dialogue for systematic
decision capture)*

### 7. Decisions Have Typed Relationships

Decisions relate to each other in specific ways:

| Relationship | Meaning |
|--------------|---------|
| **constrains** | Narrows the options available for the target decision |
| **enables** | Opens options that would otherwise not be available |
| **conflicts** | Mutually exclusive — choosing one eliminates the other |
| **refines** | Adds detail to a higher-level decision |
| **overrides** | Replaces a previous decision (with justification and audit trail) |
| **depends-on** | Cannot be resolved until the source decision is answered |

*Borrowed from: Zimmermann's Architectural Decision Models*

### 8. Every Level Has a Corresponding Validation

For every level of decisions going down, there is a corresponding
verification going back up:

```
L0  Vision & Constraints  ◄────────── Market validation / playtesting
L1  Player Experience      ◄────────── Experience testing / focus groups
L2  Core Design            ◄────────── Prototype playtesting
L3  Systems & Content      ◄────────── Systems testing / balance testing
L4  Presentation           ◄────────── Polish testing / accessibility audit
L5  Architecture           ◄────────── Integration / performance testing
L6  Implementation         ◄────────── Unit testing / TDD
```

*Borrowed from: V-Model (Systems Engineering)*

### 9. Don't Overwhelm — Delegate to the AI When the User Doesn't Care

Most users of 4SAGE are not game designers, not programmers, and not LLM
experts. They have a game idea and want to make it real. The framework must
respect this by **only asking questions the user actually needs to answer.**

The cascade has many decisions. Some are fundamental creative choices that
only the human can make ("What is your game about?"). Many others are
implementation details that have clear best-practice answers ("What save
file format should we use?").

The rule: **at every decision point, the AI should assess whether this is
something the user cares about.** If the user signals they don't — through
explicit delegation ("you decide"), apparent fatigue, or the question being
deeply technical for a non-technical user — the AI should:

1. **Make the best-practice choice itself.**
2. **Briefly state what it chose and why** (one sentence, not a lecture).
3. **Record the decision** with a note that it was AI-recommended and
   accepted by default.
4. **Move on** without requiring confirmation.

The user can always revisit any AI-made decision later. Nothing is locked.
The goal is a complete, working design with minimum friction — not a
comprehensive interrogation.

This is especially important for the MVP path: a user who says "I just
want to get something working" should be able to answer 10–15 core
questions and have the AI fill in everything else with sensible defaults.
The full cascade of 40+ KDD questions is available for users who want
depth, but it should never be mandatory.

*Principle: Respect the user's time and attention. Ask only what matters
to them. Fill in the rest with expertise.*

---

## The Design Cascade

```
Level 0: Vision & Constraints
  │  The immovable facts: what game, who for, what platform, what resources.
  │  Priority: Almost entirely Must-Have.
  │
  ▼
Level 1: Player Experience
  │  What it should feel like to play. Emotional and experiential goals.
  │  Driven by L0. Priority: Mix of MH and SH.
  │
  ▼
Level 2: Core Design
  │  What the player actually does. Game loop, mechanics, progression.
  │  Driven by L0 + L1. Priority: Mix of SH and NH.
  │
  ▼
Level 3: Systems & Content Design
  │  Detailed systems, balance, narrative, level design, content scope.
  │  Driven by L0 + L1 + L2. Priority: Mix of SH and NH.
  │
  ▼
Level 4: Presentation
  │  Art direction, audio, UI/UX, game feel, accessibility.
  │  Driven by L0 + L1 + L4 context. Priority: Mix of SH and NH.
  │
  ▼
Level 5: Architecture & Technology
  │  Engine, networking, data, tools, performance targets.
  │  Driven by all levels above. Priority: Mostly SH.
  │
  ▼
Level 6: Implementation
  │  Code, assets, testing, CI/CD, deployment, live ops.
  │  The most replaceable layer.
  │  Priority: Mostly NH.
  │
  ▼
[Playable Game]
```

Each level has its own KDD (Key Design Decision) document containing the
pre-planned questions for that level. Follow-on questions are generated
by the LLM based on answers given at the current and higher levels.

---

## The Dialogue Process

### Starting a New Game Design

1. The LLM begins at Level 0 and works through the pre-planned Key Design
   Decisions in order. For each KDD:
   - Present the question and explain why it matters.
   - Offer best-practice defaults where applicable (Principle 5).
   - Be frank about risks and trade-offs (Principle 6).
   - Record the answer in the KDD document.
   - Generate follow-on questions based on the answer.
   - Classify each follow-on by priority (MH/SH/NH/WH).
   - Note relationships to other decisions.

2. When Level 0 is complete, the LLM has enough context to generate
   Level 1 questions tailored to this specific game.

3. The process continues through each level. At Level 3, the dialogue
   shifts from high-level KDD questions to detailed systems and content
   design — the LLM walks the designer through each game system.

4. At Level 5, the LLM proposes architecture decisions driven by everything
   above, presenting trade-offs for the designer to confirm.

5. Level 6 is primarily about implementation strategy — TDD, CI/CD,
   deployment, and live operations planning.

### Modifying an Existing Design

1. The designer describes what they want to change in natural language.
2. The LLM identifies which level(s) and decision(s) are affected.
3. The LLM assesses the blast radius — what downstream decisions and
   documents would be impacted by this change.
4. The designer confirms the scope of the change.
5. The affected documents are updated, and downstream artifacts are
   flagged for revision.

### Querying the Design

Anyone can ask the LLM questions about the game design at any time:
- "Why did we choose turn-based combat over real-time?"
- "What happens to our scope if we add multiplayer?"
- "Which systems are affected by changing the camera perspective?"

The LLM answers from the decision documents, not from general knowledge.
It cites specific KDD answers and design decisions. If the answer isn't
in the documents, it says so — identifying a gap rather than guessing.

---

## Document Types

The framework produces and maintains these document types:

### Key Design Decisions (KDD)
**Location:** `kdd/L0-vision.md` through `kdd/L6-implementation.md`
**Purpose:** Capture the questions asked and answers given at each level.

### Knowledge Base
**Location:** `knowledge-base/`
**Purpose:** Genre conventions, platform constraints, design patterns, and
reference material to ground the AI consultant.

### Architecture Decisions
**Location:** `architecture/decisions.md`
**Purpose:** Cross-cutting technology and design constraints that apply to
all implementations.

### Decision Log
**Location:** `decisions/`
**Purpose:** Full reasoning for every significant decision — what was chosen,
what was rejected, and why.

### Common Design Elements
**Location:** `common/`
**Purpose:** Shared design elements referenced across multiple game systems.

### References
**Location:** `references/`
**Purpose:** Research from existing games, engines, and methodologies that
inform the design.

---

## Structured Block Types

Within KDD documents and design files, these fenced block types carry
structured information:

| Block Type | Purpose | Used In |
|------------|---------|---------|
| `mechanic:` | Game mechanic with properties and interactions | Design docs |
| `system:` | Game system with components | Design docs |
| `state:` | State machine with valid transitions and triggers | Design docs |
| `flow:` | Sequence of steps with a trigger | Design docs |
| `decision:` | Design choices with conditions | Design docs, KDD |
| `rule:` | Invariants that must always hold | Design docs |
| `directive:` | Architectural constraints with rationale | Architecture |
| `answer:` | Captured response to a KDD question | KDD documents |

---

## Project Structure

```
project-root/
├── FRAMEWORK.md                  ← this document
├── kdd/
│   ├── README.md                 ← cascade overview, priority definitions
│   ├── L0-vision.md              ← vision, genre, platform, audience, team
│   ├── L1-experience.md          ← player experience and emotional goals
│   ├── L2-core-design.md         ← game loop, mechanics, progression
│   ├── L3-systems-content.md     ← detailed systems, narrative, levels
│   ├── L4-presentation.md        ← art, audio, UI/UX, game feel
│   ├── L5-architecture.md        ← engine, networking, data, tools
│   └── L6-implementation.md      ← code, testing, deployment, live ops
├── architecture/
│   └── decisions.md
├── decisions/
│   ├── README.md
│   └── (topic-organized decision logs)
├── common/
│   └── (shared design elements)
├── knowledge-base/
│   └── (genre conventions, platform constraints, design patterns)
└── references/
    └── (research from existing games and methodologies)
```

---

## Intellectual Foundations

| Concept | Source | How It Is Used |
|---------|--------|---------------|
| Cascading choices | Lafley & Martin, *Playing to Win* (2013) | Core structure — each level constrains the next |
| Iterative feedback | Strategy Choice Cascade | Lower levels can surface issues that revise higher levels |
| Six interrogatives | Zachman Framework | What/How/Where/Who/When/Why at every level |
| MH/SH/NH/WH priorities | MoSCoW (DSDM) | Decision classification |
| Decision dependency graphs | Zimmermann et al. | Typed relationships between decisions |
| Best practice first | SAP Activate | Present conventions, diverge with justification |
| Verification pyramid | V-Model (Systems Engineering) | Each design level has corresponding validation |
| Mechanics/Dynamics/Aesthetics | MDA Framework (Hunicke et al., 2004) | Vocabulary for reasoning about player experience |
| Game design document topics | Traditional GDD practice | Ensures complete topic coverage at each level |
| LLM-guided dialogue | 4SAGE original | Dynamic question generation, ongoing queryability |

---

## Versioning and Change Management

All documents are stored in git. Every change is a commit with a message
explaining what changed and why.

The principle: **edit at the highest level that owns the change.** If the
core loop changes, edit L2 — don't patch the level design at L3. The
change cascades down through revision.
