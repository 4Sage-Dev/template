# Level 1: Player Experience

> **Priority:** Mix of MH and SH — emotional goals are creative commitments
> **Driven by:** L0 (concept, audience, platform)
> **Drives:** Core mechanics, content, presentation, and everything below

This level defines what the game should *feel like* to play — not what the
player does (that's L2), but the emotional and experiential outcome. These
are the goals that mechanics, content, and presentation must serve.

This maps roughly to the "Aesthetics" layer of the MDA Framework — the
emotional responses the game is designed to evoke.

---

## KDD-1.1: Core Emotional Experience

**Question:** What emotions should the player feel during a typical play
session? Rank the top 3–5.

**Why this matters:**
Every design decision should be tested against these emotional goals. If
the core experience is "tense and strategic," a mechanic that creates
randomness and chaos works against the goal. If the experience is "relaxing
exploration," a punishing death mechanic contradicts it. These emotions are
the north star for design.

**Priority:** MH — This is the creative commitment. Everything serves these goals.

```answer
# Example (driven by L0: survival/exploration, casual adults):
emotions:
  primary:
    - curiosity: "Wonder at discovering new islands and ruins"
    - satisfaction: "Tangible progress — building, crafting, upgrading"
    - calm: "Low-pressure exploration at the player's own pace"
  secondary:
    - mystery: "Unfolding lore that rewards attentive players"
  explicitly_not:
    - frustration: "No punishing failure states"
    - anxiety: "No time pressure or competitive stress"
```

**LLM follow-on areas:**
- Are any of these emotions in tension with each other?
- Which MDA aesthetic categories do these map to? (Sensation, Fantasy,
  Narrative, Challenge, Fellowship, Discovery, Expression, Submission)
- What reference games achieve these emotions well?
- How does session length affect the emotional arc?

---

## KDD-1.2: Player Fantasy

**Question:** Who does the player get to *be* in this game? What fantasy
does the game fulfill?

**Why this matters:**
The player fantasy is the identity the game offers. "You are a powerful
wizard" drives very different design than "You are a struggling survivor."
The fantasy determines the power level, agency, narrative voice, and the
player's relationship with the game world.

**Priority:** SH — Strong games have clear player fantasies, but the specific
fantasy is a creative choice with flexibility.

```answer
# Example:
fantasy:
  identity: "A curious explorer discovering a lost world"
  power_level: "Capable but not superhuman — cleverness over strength"
  agency: "High — the player chooses where to go and what to investigate"
  relationship_to_world: "The world existed before you; you are a visitor"
```

**LLM follow-on areas:**
- Does the fantasy align with the genre conventions from L0?
- Does the power level match the audience expectations?
- How does the fantasy evolve over the course of the game?
- Is the player a blank slate or a defined character?

---

## KDD-1.3: Challenge & Difficulty Philosophy

**Question:** How challenging should the game be, and how should difficulty
be managed?

**Why this matters:**
Challenge philosophy directly constrains mechanics (L2) and content (L3).
A game that values mastery needs fail states and skill ceilings. A game
that values accessibility needs difficulty options and gentle failure.
The audience (L0) heavily constrains this — casual players and hardcore
players have very different expectations.

**Priority:** SH — Genre conventions set a baseline; deviation is a
deliberate creative choice.

```answer
# Example:
challenge:
  philosophy: "Gentle — the game should be completable by anyone"
  failure_consequence: "Minimal — lose some resources, respawn nearby"
  difficulty_options: "No explicit difficulty settings; difficulty is organic"
  skill_expression: "Optional mastery — speedrunning, 100% completion"
  onboarding: "Gradual — teach through play, not tutorials"
```

**LLM follow-on areas:**
- How does the genre typically handle difficulty?
- Is there a tension between "completable by anyone" and "rewarding for skilled players"?
- What does failure look like concretely?
- How is progress gated — skill, time, resources, or knowledge?
- Accessibility considerations for difficulty

---

## KDD-1.4: Social Experience

**Question:** Is this a solo experience, social experience, or both?
How do players relate to each other?

**Why this matters:**
Multiplayer is not a feature — it is an architecture decision that
fundamentally changes the game. Even "optional co-op" has enormous
implications for level design, difficulty scaling, networking, save systems,
and testing. This must be decided at the experience level, not bolted on later.

**Priority:** MH — This constrains architecture (L5) and every design
decision that follows.

```answer
# Example:
social:
  mode: Single-player only
  shared_elements:
    - "Asynchronous messages left by other players (like Dark Souls signs)"
  competitive: false
  cooperative: false
  community:
    - "Steam community hub"
    - "Discord server"
```

**LLM follow-on areas:**
- If multiplayer: what networking model? (peer-to-peer, dedicated servers, etc.)
- If multiplayer: how does it affect save/progression?
- If single-player: are there any shared-world or asynchronous social elements?
- Does the social model match genre conventions?
- What community features are expected?

---

## KDD-1.5: Session Structure

**Question:** How does a typical play session work? How long is it,
and how does it start and end?

**Why this matters:**
Session structure is where audience (L0) meets experience design. Mobile
players need 5-minute sessions with instant save. PC gamers might tolerate
2-hour sessions. Session length drives save system design, quest/mission
pacing, mechanical complexity, and even UI design (larger text for TV,
smaller for desktop).

**Priority:** SH — Genre and platform set strong conventions, but the
specific design is a creative choice.

```answer
# Example:
session:
  typical_length: "30-60 minutes"
  minimum_meaningful_session: "15 minutes"
  save_model: "Auto-save every 2 minutes + manual save anywhere"
  session_start: "Resume exactly where you left off"
  session_end: "Natural stopping points every 15-20 minutes"
  pacing: "Exploration → Discovery → Build/Craft → Repeat"
```

**LLM follow-on areas:**
- Does the save system support the session length?
- Are there natural stopping points, or can the player stop anywhere?
- What happens if the player quits mid-task?
- How does pacing differ early vs. late game?
- Does the platform affect session expectations? (handheld vs. desktop)

---

## KDD-1.6: Player Retention & Engagement Model

**Question:** What keeps the player coming back? What is the long-term
engagement loop?

**Why this matters:**
A game that is meant to be played once for 10 hours has very different
design needs than one meant to be played daily for months. This drives
content scope (L3), progression systems (L2), monetization (if applicable),
and post-launch support planning (L6).

**Priority:** SH — The engagement model should be intentional, not accidental.

```answer
# Example:
retention:
  model: "Finite experience with optional extended play"
  main_content: "20-30 hours of exploration and story"
  extended_play: "Procedural islands, completionist goals, creative building"
  replayability: "Moderate — different island generation, alternate paths"
  post_launch: "Planned content updates, no live service"
```

**LLM follow-on areas:**
- Is the content scope realistic for the team (L0)?
- How does retention align with the monetization model?
- What is the "content treadmill" risk?
- How much procedural vs. handcrafted content?
- What metrics will measure retention success?

---

## How This Level Drives the Next

Once Level 1 is answered, the LLM can:

1. **Shape Level 2 (Core Design) questions** — if the core emotion is "calm,"
   combat mechanics need to be optional or non-threatening. If the session
   target is 30 minutes, the core loop must complete within that window.

2. **Identify experience contradictions early** — if the player fantasy is
   "powerful warrior" but the difficulty philosophy is "no challenge," there
   is a tension to resolve.

3. **Set the emotional benchmark** — every mechanic proposed at L2 can be
   tested: "Does this serve the emotional goals defined at L1?"

4. **Constrain social and session architecture** — multiplayer decisions
   here flow directly into L5 (Architecture) and cannot be easily changed later.
