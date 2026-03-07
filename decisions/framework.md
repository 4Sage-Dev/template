# Framework Decisions Log

Full reasoning for decisions about the 4SAGE Framework itself — its name,
structure, methodology, and tooling.

---

### D-001: Name "4SAGE" for the project

**Date:** 2026-03-04
**Context:** Needed a name for the AI-guided game design methodology framework.
**Decided:** 4SAGE — "Structured AI-Guided Experience Design"
**Alternatives considered:**
- SAGE (plain) — rejected because: EA's SAGE (Strategy Action Game Engine) would cause search confusion, and the word is too generic for a unique project identity.
- SageForge — rejected because: the best domain TLDs (.com, .io, .ai) were already taken by other parties.
- Arcwright — rejected because: less immediately meaningful; requires explanation.
- Codex — rejected because: too generic; commonly used across many projects.
- Crucible — rejected because: common word, harder to claim as a unique identity.
- GameSage — rejected because: less distinctive than 4SAGE; no parallel to existing 4GRP project.
**Rationale:** "4SAGE" parallels the companion project 4GRP (4th Generation Resource Planning), suggesting a family of AI-guided design frameworks. "SAGE" means wise counselor, which describes the AI's role perfectly. The "4" prefix provides uniqueness and a generational narrative. Domain availability is excellent (4sage.dev registered, 4sage.ai/io/org all available).
**References:** Project-wide naming, `README.md`

---

### D-002: Seven-level design cascade (L0–L6)

**Date:** 2026-03-04
**Context:** Needed to determine the right number of levels and their ordering for a game design decision cascade.
**Decided:** Seven levels: L0 Vision & Constraints → L1 Player Experience → L2 Core Design → L3 Systems & Content Design → L4 Presentation → L5 Architecture & Technology → L6 Implementation
**Alternatives considered:**
- Six levels (matching 4GRP's L0–L5) — rejected because: game design has a distinct "Presentation" layer (art, audio, UI) that has no clear analog in ERP. Combining it with another level would obscure important decisions.
- Eight+ levels (separating narrative, level design, etc.) — rejected because: additional levels should earn their place. Narrative and level design are content that flows through mechanical systems and naturally belongs in L3.
- Fewer levels (3-4, matching MDA's Mechanics/Dynamics/Aesthetics) — rejected because: too coarse. MDA doesn't cover vision, constraints, technology, or implementation. A practical framework needs finer granularity.
**Rationale:** Each level genuinely constrains the next: vision constrains experience goals, experience constrains mechanics, mechanics constrain systems/content, content constrains presentation, presentation constrains technology, technology constrains implementation. The ordering was validated by asking "can you answer this level without the level above?" — the answer is no for each pair.
**References:** `FRAMEWORK.md` → The Design Cascade, `kdd/README.md`

---

### D-003: Mechanics before narrative in the cascade

**Date:** 2026-03-04
**Context:** Needed to determine whether narrative/world design should come before or after core mechanics in the level ordering.
**Decided:** Core mechanics (L2) before narrative (L3). Narrative is part of Systems & Content Design.
**Alternatives considered:**
- Narrative before mechanics — rejected because: even in heavily narrative games (Disco Elysium, visual novels), the mechanical framework ("dialogue-driven RPG with skill checks," "branching visual novel") must be established before narrative can be designed. The narrative delivery mechanism is a mechanical decision.
- Narrative as its own level — rejected because: many games have no narrative at all (Tetris, chess, most puzzle games). A dedicated level would be empty for a large class of games. As part of L3, it's addressed when applicable and skipped when not.
**Rationale:** The core game loop determines how narrative is delivered, paced, and experienced. A turn-based RPG delivers story completely differently than an action game. Mechanics are the container; narrative is content that fills the container.
**References:** `FRAMEWORK.md`, `kdd/README.md`

---

### D-004: Adapt 4GRP methodology for game design

**Date:** 2026-03-04
**Context:** Needed a methodology foundation for the game design framework. Evaluated existing game design frameworks and methodologies.
**Decided:** Adapt the 4GRP (4th Generation Resource Planning) framework methodology, supplemented by MDA Framework vocabulary and traditional GDD topic coverage.
**Alternatives considered:**
- MDA Framework alone — rejected because: only three layers (Mechanics/Dynamics/Aesthetics) with no structured dialogue process, no decision logging, no priority system, no technology/implementation guidance. An analytical lens, not a design methodology.
- Traditional GDD templates — rejected because: provide topic checklists but no decision hierarchy, no dependency tracking, no structured dialogue. Fill-in-the-blank, not guided conversation.
- Build from scratch — rejected because: 4GRP already solved the hard problems of cascading decisions, priority classification, decision logging, LLM dialogue patterns, and structured markdown. No reason to reinvent.
**Rationale:** 4GRP provides the methodology skeleton (cascade, priorities, decision log, structured blocks, LLM dialogue). MDA provides conceptual vocabulary for the game-specific middle layers. Traditional GDD practice ensures complete topic coverage. The combination is stronger than any individual source.
**References:** `FRAMEWORK.md` → Intellectual Foundations, `README.md`

---

### D-005: Domain registration at 4sage.dev

**Date:** 2026-03-04
**Context:** Needed a web domain for the project.
**Decided:** Register `4sage.dev` as the primary domain.
**Alternatives considered:**
- 4sage.ai — available, strong AI signal, but more expensive (~$20-80/year vs ~$10-15/year for .dev).
- 4sage.io — available, popular for tech projects, but .io TLD has ongoing controversy about its future governance.
- 4sage.com — taken (parked since 2015 on NameBright), would require premium purchase.
- sage4.dev / sage4.ai — available, but "4SAGE" reads better as a name (parallels 4GRP) than "SAGE4."
**Rationale:** .dev is controlled by Google Registry, is well-regarded in the developer/tech community, enforces HTTPS by default (security benefit), and is affordable. Combined with the 4sage prefix, it's clean and memorable.
**References:** Project-wide

---

### D-006: Website as the universal bootstrap point

**Date:** 2026-03-04
**Context:** Needed to determine how a user — especially a non-technical one — actually starts using 4SAGE. The framework lives in a git repo, but most users don't know what git is.
**Decided:** 4sage.dev serves as the single entry point for all users. The website is simultaneously a human-readable landing page and an LLM-readable instruction set. When a user tells any LLM "I want to use the 4SAGE framework," the LLM fetches 4sage.dev and gets everything it needs to bootstrap the experience.
**Alternatives considered:**
- GitHub repo only — rejected because: requires users to know git, find the repo, and understand the file structure. Too high a barrier for non-technical users.
- Downloadable app or installer — rejected because: high development cost, platform-specific builds, update distribution problem. Overkill when the LLM itself can handle setup.
- Published as an LLM plugin/extension only — rejected because: locks the framework to a specific LLM vendor. Against the LLM-agnostic principle.
**Rationale:** The website is the lowest-friction entry point that works for everyone. Technical users get the repo link. Non-technical users get step-by-step guidance. LLMs get machine-readable setup instructions. One URL serves all three audiences. The LLM does the heavy lifting of setup — the website just tells it what to do.
**References:** Website planning, `README.md`

---

### D-007: Three-tier onramp (text, project, voice)

**Date:** 2026-03-04
**Context:** Users will have vastly different technical capabilities and hardware. Needed to define what "getting started" looks like for different user profiles.
**Decided:** Three tiers of engagement, all starting from 4sage.dev:
1. **Text only** — user chats with any LLM in a browser. No local files, no git, no installation. The LLM follows the framework in conversation. Lowest barrier.
2. **Full project** — user has Claude Code or similar tool. The LLM clones the repo, sets up local files, initializes git, and runs the guided interview with version-controlled output. Full methodology.
3. **Voice interactive** — full project setup plus speech-to-text and text-to-speech. The user has a verbal conversation with their AI game design consultant. Highest experience quality.
**Alternatives considered:**
- Single path only (full project) — rejected because: excludes the majority of potential users who don't have CLI tools installed.
- Voice only as the primary experience — rejected because: requires specific hardware and complex setup. Should be an option, not a requirement.
- Web app that wraps an LLM API — rejected because: high development cost, ongoing hosting cost, API key management, locks to one LLM provider.
**Rationale:** Each tier adds capability without invalidating the others. A user can start at Tier 1 (just chatting) and graduate to Tier 2 or 3 as they get more invested. The framework itself is identical across all tiers — only the delivery channel changes.
**References:** Website planning, `FRAMEWORK.md`

---

### D-008: Conductor prompt as the core execution mechanism

**Date:** 2026-03-04
**Context:** The framework files (FRAMEWORK.md, KDD levels) describe the methodology, but they don't contain explicit instructions telling an LLM *how to run a session*. An LLM reading FRAMEWORK.md understands the theory but lacks the step-by-step operating procedure.
**Decided:** Create a "conductor prompt" — a dedicated document that instructs any LLM on exactly how to conduct a 4SAGE design session. This prompt is the bridge between the framework (what to ask) and the experience (how to ask it). It will be hosted on 4sage.dev and included in the repo.
**Alternatives considered:**
- Embed instructions in each KDD file — rejected because: scatters the execution logic across 7+ files. Hard to maintain, hard for an LLM to follow a single coherent flow.
- Rely on the LLM to figure it out from FRAMEWORK.md — rejected because: different LLMs would interpret the methodology differently, leading to inconsistent experiences. Explicit is better than implicit.
- Build a software orchestrator — rejected because: adds a software dependency, breaks LLM-agnosticism, and is unnecessary when the LLM itself can follow instructions.
**Rationale:** The conductor prompt is the "how" that complements the framework's "what." It tells the LLM: start here, ask this, record the answer this way, generate follow-ons this way, be frank when this happens, move to the next level when this condition is met. One document, universally applicable, works with any LLM.
**References:** `conductor.md` (to be created), website planning

---

### D-009: Voice-interactive tier with guided hardware/software setup

**Date:** 2026-03-04
**Context:** The ideal 4SAGE experience is a natural conversation — the user talks about their game idea and the AI consultant responds verbally. This requires speech-to-text (STT) and text-to-speech (TTS) infrastructure that most users won't have.
**Decided:** The voice tier includes an LLM-guided setup process: the website and conductor prompt contain a voice setup matrix (per platform, per LLM tool) so the LLM can walk the user through installing and configuring STT and TTS on their specific system. The LLM handles the setup, involving the user only when necessary (e.g., "plug in a microphone," "say hello to test").
**Alternatives considered:**
- Require users to set up voice themselves before starting — rejected because: contradicts the "start from scratch" principle. If the user could set up voice pipelines, they probably don't need hand-holding for game design either.
- Browser-based voice (Web Speech API) — considered as a simpler alternative for Tier 1 users. Not rejected — may be a good intermediate option. But doesn't provide the full local experience.
- Skip voice entirely — rejected because: voice interaction is a significantly better experience for creative brainstorming. Worth the setup complexity for users who want it.
**Rationale:** The LLM is already guiding the user through game design decisions — it can also guide them through technical setup. The voice setup matrix on the website gives the LLM the platform-specific knowledge it needs. This is consistent with the framework's philosophy: the AI handles complexity so the human can focus on creative decisions.
**References:** Website planning, voice setup matrix (to be created)

---

### D-010: Don't overwhelm — AI delegation and MVP mode

**Date:** 2026-03-04
**Context:** The framework has 40+ KDD questions across 7 levels. The primary expected user is non-technical, not a game designer, and not an LLM expert. They have a game idea and want to make it real without answering dozens of detailed questions they don't understand or care about.
**Decided:** Add Principle 9 ("Don't Overwhelm") to the framework and build three engagement modes into the conductor prompt:
1. **Deep mode** — user discusses every decision (for experts who want control).
2. **Guided mode** — user makes key creative choices; AI handles the rest with best-practice defaults, briefly stating each choice.
3. **MVP mode** — user answers ~15 essential questions; AI fills in everything else and produces a complete design document. User reviews and revises later.
The AI must detect the user's engagement level and offer delegation proactively. When a user says "you decide" or shows fatigue, the AI takes over without asking "are you sure?" All AI-made decisions are recorded as such and are always revisitable.
**Alternatives considered:**
- Always ask every question (original approach) — rejected because: overwhelms non-technical users. Most people don't want to answer 40 questions. They want a working game design with minimum friction.
- Skip levels entirely for non-technical users — rejected because: skipping levels creates gaps. Better to have the AI fill in best-practice answers than to leave sections empty.
- Separate "simple" and "advanced" question sets — rejected because: artificial separation. The same question can be simple or complex depending on the user's answer. Better to let the AI adapt dynamically.
**Rationale:** The framework should serve the user, not the other way around. A non-technical user should be able to go from "I have an idea for a game" to a complete, well-structured design document in one conversation. The AI's expertise is the product — the questions are just the mechanism. Respecting the user's time and attention is a core principle, not an optimization.
**References:** `FRAMEWORK.md` → Principle 9, `conductor.md` → Delegation section
