# Level 6: Implementation

> **Priority:** Mostly NH — implementation details are the most replaceable layer
> **Driven by:** All levels above — every implementation choice traces back to a design decision
> **Drives:** The actual playable game

This is the bottom of the cascade — where design becomes reality. This level
defines code architecture, testing strategy, build/deploy pipeline, and
post-launch operations. It is the most flexible layer because implementation
details can be changed without affecting the design above (as long as the
design contracts are maintained).

However, "most replaceable" does not mean "least important." Poor
implementation destroys good design. This level ensures the engineering
approach is disciplined and sustainable.

---

## KDD-6.1: Code Architecture & Patterns

**Question:** How is the codebase organized? What patterns and conventions
does the team follow?

**Why this matters:**
Code architecture determines maintainability, testability, and the team's
ability to work in parallel. A well-structured codebase can be extended and
modified for years. A poorly structured one becomes unmaintainable within
months. Architecture patterns should match the team's experience (L0) and
the engine's conventions (L5).

**Priority:** SH — Good architecture is a force multiplier; the specific
patterns depend on the engine and team.

```answer
# Example:
code_architecture:
  language: C#
  patterns:
    - name: Component-based (ECS-lite)
      scope: "Game objects — use Unity's component model"
    - name: Service Locator
      scope: "Global systems (audio, save, input) — registered at startup"
    - name: State Machine
      scope: "Player states, NPC behavior, UI screens"
    - name: Observer / Event Bus
      scope: "Decoupled communication between systems"
  conventions:
    naming: "PascalCase for types and methods, camelCase for locals"
    file_organization: "One class per file, folder per system"
    documentation: "XML docs on public APIs; no docs on obvious code"
    max_file_length: "500 lines — split if larger"
  anti_patterns:
    - "No singletons — use service locator instead"
    - "No god objects — split responsibilities"
    - "No string-based communication — use typed events"
```

**LLM follow-on areas:**
- Does the architecture match engine best practices?
- How does the architecture support the systems identified at L3?
- What are the coupling points between major systems?
- How is the architecture documented for new team members?
- What refactoring triggers are defined? (When is complexity too high?)

---

## KDD-6.2: Testing Strategy

**Question:** How is the game tested? What kinds of tests exist, and when
do they run?

**Why this matters:**
Games are notoriously hard to test — the state space is enormous, "correct"
behavior is subjective, and many bugs are feel issues rather than crashes.
A testing strategy that works for games combines automated testing (unit,
integration, smoke) with structured playtesting and manual QA. The strategy
must be realistic for the team size (L0).

**Priority:** SH — Testing is essential, but the approach depends on team
and project scale.

```answer
# Example:
testing:
  automated:
    unit_tests:
      scope: "Core systems — economy, crafting logic, save/load"
      framework: "NUnit (Unity Test Framework)"
      coverage_target: "80% on core systems, no target on MonoBehaviours"
      when: "Run on every PR; block merge on failure"
    integration_tests:
      scope: "System interactions — crafting + inventory, save + load"
      when: "Run nightly"
    smoke_tests:
      scope: "Game launches, main menu loads, new game starts, save/load"
      when: "Run on every build"
  manual:
    playtesting:
      frequency: "Weekly internal playtests from prototype onward"
      external: "Monthly external playtests from alpha"
      tracking: "Structured feedback forms + recorded sessions"
    qa:
      approach: "Exploratory testing by team members on rotation"
      bug_tracking: "GitHub Issues with severity labels"
  performance_testing:
    frequency: "Weekly profiling from vertical slice"
    regression: "Frame time benchmarks checked in CI"
```

**LLM follow-on areas:**
- What is testable by automation vs. what requires human judgment?
- How is playtest feedback structured and prioritized?
- What is the bug severity classification?
- How are platform-specific bugs tracked?
- What is the QA process for certification builds?

---

## KDD-6.3: Build & Deployment Pipeline

**Question:** How are builds created, distributed, and released?

**Why this matters:**
The build pipeline determines how quickly the team can iterate, how builds
reach testers and players, and how releases are managed. A slow or
unreliable build pipeline is a constant drag on productivity.

**Priority:** SH — A working pipeline is essential; specific tooling choices
are flexible.

```answer
# Example:
build_pipeline:
  build_system: Unity Cloud Build + GitHub Actions
  platforms:
    pc:
      build_frequency: "Every push to main"
      distribution: "Steam (Steamworks)"
      build_time: "~10 minutes"
    switch:
      build_frequency: "Weekly + on-demand"
      distribution: "Nintendo Developer Portal"
      build_time: "~20 minutes"
  versioning:
    scheme: "Semantic versioning (major.minor.patch)"
    tagging: "Git tags for every release build"
  release_process:
    1: "Feature complete → code freeze"
    2: "Release candidate → QA pass"
    3: "Platform certification submission"
    4: "Store page preparation"
    5: "Launch day build + day-one patch if needed"
  hotfix_process: "Branch from release tag, fix, test, submit"
```

**LLM follow-on areas:**
- What is the certification timeline for each platform?
- How are beta/early access builds managed?
- What is the rollback strategy if a release has critical bugs?
- How are builds archived for post-launch debugging?

---

## KDD-6.4: Content Pipeline

**Question:** How is game content (art, audio, levels, text) authored,
reviewed, and integrated into the game?

**Why this matters:**
Content production is often the bottleneck in game development. A smooth
content pipeline means artists and designers can work independently of
programmers. A broken pipeline means every content change requires
engineering support. The pipeline must match the team structure (L0) and
tools (L5).

**Priority:** SH — Content pipeline efficiency directly affects the
team's output.

```answer
# Example:
content_pipeline:
  art:
    authoring: "Blender → FBX export → Unity import"
    review: "Art review in Unity scene before merge"
    naming: "kebab-case, prefixed by type (env-tree-palm, chr-hermit-01)"
    atlas: "Texture atlases per biome, generated by build tool"
  audio:
    authoring: "DAW → WAV export → FMOD integration"
    naming: "sfx-action-detail (sfx-craft-hammer-hit)"
  levels:
    authoring: "Unity Scene editor for handcrafted areas"
    procedural: "Island generator tool → review → tweak → approve"
  text:
    authoring: "Google Sheets → export to Unity Localization"
    review: "In-game review with placeholder text flagging"
  integration:
    process: "Content PR → team review → merge to main"
    validation: "Automated checks for missing references, naming violations"
```

**LLM follow-on areas:**
- What is the content review bottleneck?
- How are content errors caught before they reach players?
- What is the localization integration workflow?
- How is content versioned alongside code?

---

## KDD-6.5: Post-Launch & Live Operations

**Question:** What happens after the game launches? How is it supported?

**Why this matters:**
Launch is not the end — it's the beginning of the game's life with players.
Bug reports, patches, content updates, community management, and analytics
monitoring all require planning and resources. The post-launch plan must be
realistic for the team size (L0) and aligned with the retention model (L1)
and success criteria (L0).

**Priority:** SH — Post-launch planning should begin before launch, not after.

```answer
# Example:
post_launch:
  support:
    duration: "12 months of active support"
    team: "Full team for 3 months post-launch, then 1 person maintenance"
    response_time: "Critical bugs: patch within 1 week; other: monthly updates"
  content_updates:
    planned:
      - "Month 2: New island biome"
      - "Month 4: Photo mode + quality-of-life"
      - "Month 6: Extended ending + new story content"
    pricing: "Free updates — no DLC planned for Year 1"
  community:
    platforms: ["Steam Community", "Discord", "Twitter/X"]
    moderation: "Team member rotation, 1 hour/day"
  analytics:
    tracked: ["Session length", "Progression milestones", "Drop-off points"]
    privacy: "GDPR compliant, opt-in analytics, no PII collected"
    tools: "Unity Analytics or custom dashboard"
  end_of_life:
    plan: "Game remains purchasable and playable indefinitely"
    server_dependencies: "None — fully offline capable"
```

**LLM follow-on areas:**
- Is the post-launch plan sustainable for the team?
- How are post-launch priorities determined? (data-driven vs. planned roadmap)
- What is the communication strategy with players?
- How does post-launch support affect the next project?
- What legal obligations exist for post-launch support? (consumer protection)

---

## How This Level Completes the Design

Level 6 produces the information needed to actually *build* the game:

1. **Engineering task breakdown** — code architecture + testing strategy
   define the development workflow.

2. **Production schedule** — content pipeline + build pipeline define how
   fast content can be created and integrated.

3. **Release checklist** — deployment pipeline + certification requirements
   define what must be done before launch.

4. **Sustainability plan** — post-launch planning ensures the game and
   team survive beyond launch day.

The complete cascade from L0 through L6 provides a comprehensive, traceable
game design where every implementation detail traces back through systems,
mechanics, experience goals, and vision to the original concept.
