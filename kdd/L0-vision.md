# Level 0: Vision & Constraints

> **Priority:** Must-Have — these are facts and foundational creative choices
> **Drives:** Everything below. Every other decision is constrained by these answers.

These are the first questions asked in any game design. Some answers are
immovable facts (budget, team, platform). Others are the foundational creative
vision. Together they define the design space for everything that follows.

---

## KDD-0.1: Game Concept

**Question:** What is the game? Describe the core idea in 1–3 sentences.

**Why this matters:**
The concept statement is the anchor for every subsequent decision. If you
cannot articulate the game in a few sentences, the vision is not yet clear
enough to design from. This is the "elevator pitch" — it sets genre, tone,
and scope expectations before any details are discussed.

**Priority:** MH — Without a concept, there is no game to design.

```answer
# Example:
concept:
  title: "Untitled Exploration Game"
  pitch: >
    A single-player open-world survival game where the player explores
    procedurally generated islands, gathers resources, crafts tools, and
    uncovers the mystery of an ancient civilization — all in 30-minute
    sessions designed for busy adults.
  genre: Survival / Exploration
  tone: Mysterious, contemplative, low-stress
```

**LLM follow-on areas** (generated, not pre-planned):
- What existing games does this most resemble? (establish reference points)
- What makes this game different from those references?
- Is there an IP or franchise constraint?
- Is the concept validated with any audience yet?

---

## KDD-0.2: Target Audience

**Question:** Who is this game for? Describe the primary player.

**Why this matters:**
Audience determines difficulty, complexity, session length, accessibility
requirements, content ratings, monetization models, and marketing strategy.
A game for hardcore strategy enthusiasts is designed completely differently
than one for casual mobile players. Knowing your audience constrains nearly
every decision that follows.

**Priority:** MH — The audience is a choice, but once chosen it acts as a constraint.

```answer
# Example:
audience:
  primary:
    description: "Adults 25-45 who game casually, 30-60 min sessions"
    gaming_experience: Moderate — played games before but not hardcore
    platform_preference: PC and Switch
    session_length: 30-60 minutes
  secondary:
    description: "Younger players 16-24 who enjoy exploration games"
  content_rating_target: ESRB E10+ / PEGI 7
```

**LLM follow-on areas:**
- Accessibility requirements for this audience
- Session length and save system implications
- Control complexity expectations
- Content and difficulty expectations
- Monetization tolerance and expectations

---

## KDD-0.3: Target Platforms

**Question:** What platforms will the game ship on?

**Why this matters:**
Platform is arguably the highest-leverage technical constraint. It determines
input methods (controller, touch, keyboard/mouse), performance budgets,
screen sizes, certification requirements, store policies, and monetization
options. A mobile game and a PC game with the same concept are fundamentally
different products.

**Priority:** MH — Platform commitments are often non-negotiable (publisher
contracts, team expertise, market strategy).

```answer
# Example:
platforms:
  primary: PC (Steam)
  secondary: [Nintendo Switch]
  future_consideration: [PlayStation 5, Xbox Series]
  minimum_spec:
    pc: "GTX 1060 / Ryzen 3 3100 / 8GB RAM"
  input_methods:
    - Keyboard and mouse
    - Controller (Xbox, PlayStation, Switch Pro)
```

**LLM follow-on areas:**
- Platform-specific certification requirements
- Cross-platform save and progression
- Input method design implications
- Performance budget per platform
- Store-specific requirements (Steam Deck verification, etc.)
- Release timing and platform exclusivity

---

## KDD-0.4: Team & Resources

**Question:** What resources are available to build this game?

**Why this matters:**
The gap between vision and resources is where most game projects fail.
A solo developer cannot build a AAA open world. A team of 5 can build a
remarkable focused experience. Honestly recording team size, budget, timeline,
and skill gaps prevents designing a game that cannot be built.

**Priority:** MH — Resources are facts, not choices.

```answer
# Example:
resources:
  team:
    size: 3
    roles:
      - name: "Alice"
        role: Designer / Producer
        skills: [game design, project management, writing]
      - name: "Bob"
        role: Programmer
        skills: [C#, Unity, networking]
      - name: "Carol"
        role: Artist
        skills: [3D modeling, texturing, UI design]
    skill_gaps: [audio design, marketing, QA]
  budget:
    total: $50,000
    source: Self-funded
    runway: 18 months
  timeline:
    target_release: 2027 Q3
    milestones:
      - name: Prototype
        target: 2026 Q4
      - name: Vertical slice
        target: 2027 Q1
      - name: Alpha
        target: 2027 Q2
```

**LLM follow-on areas:**
- Which skill gaps are critical vs. deferrable?
- Outsourcing strategy for missing skills
- Scope calibration — is this buildable by this team in this time?
- Tool and asset store strategy to multiply the team
- Risk assessment — what happens if a team member leaves?

---

## KDD-0.5: Existing Commitments & Constraints

**Question:** What external commitments, obligations, or constraints already exist?

**Why this matters:**
Games rarely start from zero. There may be
publisher contracts, IP licensing agreements, engine commitments, or prior
work that constrains the design. These are facts on the ground.

**Priority:** MH — Obligations are non-negotiable.

```answer
# Example:
constraints:
  publisher:
    name: None (self-published)
  ip_obligations: None — original IP
  engine_commitment:
    engine: Unity 6
    reason: "Team expertise; switching cost too high"
  existing_work:
    - description: "6 months of prototype work in Unity"
      status: Partially reusable
    - description: "200 concept art pieces"
      status: Keep — defines art direction
  legal:
    - "Music must be original or properly licensed"
    - "No trademarked references"
```

**LLM follow-on areas:**
- Publisher milestone and delivery requirements
- IP usage restrictions and approval processes
- Engine-imposed limitations on design
- Reusability assessment of existing work
- Legal review needs

---

## KDD-0.6: Success Criteria

**Question:** What does success look like for this project?

**Why this matters:**
Without explicit success criteria, scope creep is inevitable and "done" is
undefined. Success criteria should be concrete and measurable. They may be
commercial (units sold, revenue), creative (awards, critical reception),
personal (portfolio piece, learning), or community-driven (player retention,
community size).

**Priority:** SH — The team should agree on success criteria, but they can
evolve as the project develops.

```answer
# Example:
success_criteria:
  commercial:
    - "Recoup development costs within 12 months of launch"
    - "10,000+ units sold in first year"
  creative:
    - "Positive reviews (>80% on Steam)"
    - "Players describe the game as 'relaxing' and 'mysterious'"
  personal:
    - "Ship a complete game as a team"
    - "Build a portfolio piece for each team member"
```

**LLM follow-on areas:**
- Are commercial and creative goals aligned or in tension?
- What metrics will be tracked post-launch?
- What is the minimum viable product that still meets success criteria?
- Is there a "walk away" threshold?

---

## How This Level Drives the Next

Once Level 0 is answered, the LLM has enough context to:

1. **Generate Level 1 (Player Experience) questions** tailored to this genre,
   audience, and platform — the experience goals for a mobile puzzle game are
   very different from a PC survival game.

2. **Calibrate scope expectations** — the team size and budget constrain how
   ambitious the mechanics and content can be.

3. **Identify early conflicts** — if the concept implies AAA scope but the
   team is 3 people, surface this tension immediately.

4. **Load relevant knowledge** — the genre, platform, and audience answers
   tell the LLM which knowledge-base documents to consult for best practices.

The key principle: **Level 0 questions are universal.** Every game has a
concept, an audience, platforms, resources, constraints, and success criteria.
The LLM's job is to take these answers and generate the *specific* follow-on
questions that matter for *this particular* game.
