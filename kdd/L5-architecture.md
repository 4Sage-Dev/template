# Level 5: Architecture & Technology

> **Priority:** Mostly SH — technology serves the design, not the other way around
> **Driven by:** All levels above — vision, experience, mechanics, systems, presentation
> **Drives:** Implementation approach, performance, tooling, deployment

This level defines the technical foundation: what engine, what tools, what
infrastructure, what performance targets. Every decision here should be
*driven by* the design levels above — the engine is chosen because it can
deliver the game described at L0–L4, not because the team likes it (though
team expertise from L0 is a legitimate constraint).

Technology decisions are expensive to reverse. Changing an engine mid-project
is often a project restart. These decisions warrant careful analysis.

---

## KDD-5.1: Engine & Platform Technology

**Question:** What game engine or framework will be used? Why?

**Why this matters:**
The engine choice determines the development workflow for the entire project.
It constrains rendering capabilities, platform support, available tools,
asset pipeline, scripting language, and community/marketplace resources.
Engine choice should be driven by L0 (team skills, platform targets, budget)
and L4 (rendering requirements).

**Priority:** MH — Once committed, engine changes are catastrophic.

```answer
# Example:
engine:
  choice: Unity 6
  rationale:
    - "Team has 5+ years of Unity experience (L0)"
    - "Supports all target platforms (L0: PC, Switch)"
    - "URP meets rendering needs for stylized art (L4)"
    - "Large asset store for prototyping velocity"
  alternatives_considered:
    - name: Unreal Engine 5
      rejected: "Team has no Unreal experience; overkill for art style"
    - name: Godot 4
      rejected: "Console export maturity uncertain for Switch target"
  version: "Unity 6 LTS"
  render_pipeline: Universal Render Pipeline (URP)
  scripting: C#
```

**LLM follow-on areas:**
- Does the engine support all L0 platform targets natively?
- What engine-specific limitations affect the design?
- What is the engine's licensing model and cost implications?
- What version/branch policy will the project follow?
- Are there engine-specific best practices the team should adopt?

---

## KDD-5.2: Networking Architecture

**Question:** If multiplayer (L1), what networking model will be used?

**Why this matters:**
Networking architecture is one of the most impactful technical decisions.
Client-server vs. peer-to-peer, authoritative vs. non-authoritative, tick
rate, serialization format — each choice has major implications for gameplay
feel, cheating resistance, infrastructure cost, and development complexity.

**Priority:** MH if multiplayer; N/A for single-player games.

```answer
# Example:
networking: N/A — single-player game (see L1-KDD-1.4)
```

---

## KDD-5.3: Data Architecture

**Question:** How is game data stored, loaded, and managed?

**Why this matters:**
Data architecture affects load times, save file size, modding support,
content pipeline flexibility, and development iteration speed. Decisions
here include save system implementation, asset loading strategy, data
serialization formats, and database usage (if any).

**Priority:** SH — Good data architecture enables fast iteration and
reliable saves.

```answer
# Example:
data:
  save_system:
    format: JSON (human-readable for debugging)
    storage: Local filesystem + Steam Cloud
    frequency: "Auto-save every 2 minutes + manual save"
    slots: "3 save slots"
    migration: "Version-stamped saves with forward migration"
  game_data:
    format: "ScriptableObjects (Unity) for items, recipes, biomes"
    loading: "Addressable assets — load by biome on demand"
    localization: "Unity Localization package — string tables"
  procedural_data:
    seeds: "World seed generates deterministic island layouts"
    persistence: "Generated chunks saved to player save file"
```

**LLM follow-on areas:**
- How large will save files get?
- What is the load time budget?
- How is data validated to prevent corruption?
- Does the data format support modding?
- What tools are needed for content authoring?

---

## KDD-5.4: Performance Targets

**Question:** What are the frame rate, memory, and load time targets
per platform?

**Why this matters:**
Performance targets are non-negotiable contracts with the player. They
constrain art complexity (L4), world size (L3), and AI complexity (L3).
Platform certification often enforces minimum performance standards.
Setting these targets early prevents discovering performance problems late.

**Priority:** MH for platform certification requirements; SH for quality targets.

```answer
# Example:
performance:
  targets:
    pc:
      frame_rate: "60 fps at minimum spec (GTX 1060)"
      resolution: "1080p at minimum, 4K supported"
      memory: "4 GB RAM budget"
      load_time: "< 10 seconds from menu to gameplay"
    switch:
      frame_rate: "30 fps docked, 30 fps handheld"
      resolution: "720p handheld, 1080p docked"
      memory: "3 GB RAM budget"
      load_time: "< 15 seconds"
  profiling:
    approach: "Weekly profiling sessions from vertical slice onward"
    tools: "Unity Profiler, RenderDoc, platform-specific tools"
  optimization_priorities:
    1: Frame rate stability (no drops below target)
    2: Load times
    3: Memory footprint
```

**LLM follow-on areas:**
- What are the platform certification performance requirements?
- What is the LOD (Level of Detail) strategy?
- How does procedural generation affect performance?
- What is the draw call budget?
- How is performance tested across minimum-spec hardware?

---

## KDD-5.5: Development Tools & Pipeline

**Question:** What tools and workflows will the team use for development?

**Why this matters:**
The development pipeline affects iteration speed, collaboration efficiency,
and the ability to create content quickly. This includes version control,
CI/CD, art pipeline tools, level design tools, and debugging tools. A
smooth pipeline multiplies the team; a broken one divides it.

**Priority:** SH — Good tooling is a force multiplier but requires
investment to set up.

```answer
# Example:
tools:
  version_control:
    system: Git
    hosting: GitHub (private repo)
    lfs: "Git LFS for textures, audio, and 3D models"
    branching: "Trunk-based development with short-lived feature branches"
  ci_cd:
    system: GitHub Actions
    builds: "Automated PC build on every push to main"
    tests: "Unit tests + smoke tests on PR"
    console_builds: "Manual trigger for Switch builds"
  art_pipeline:
    modeling: Blender 4.x
    texturing: Substance Painter
    format: FBX → Unity import
  level_design:
    tool: "Unity Scene editor + custom island generation tool"
  debugging:
    logging: "Structured logging with severity levels"
    console: "In-game debug console (dev builds only)"
    replay: "Not planned — manual repro for bugs"
```

**LLM follow-on areas:**
- What custom tools need to be built?
- How does the CI/CD pipeline handle large binary assets?
- What is the backup and disaster recovery strategy?
- How are builds distributed to team members and testers?
- What code quality tools will be used? (linting, static analysis)

---

## KDD-5.6: Third-Party Dependencies

**Question:** What external libraries, services, and middleware will the
project depend on?

**Why this matters:**
Every dependency is a risk — it can be abandoned, change its license, have
security vulnerabilities, or break with engine updates. But dependencies
also save enormous development time. The decision is which risks are worth
the benefit, and how to mitigate them.

**Priority:** SH — Dependencies should be chosen deliberately, not accumulated
accidentally.

```answer
# Example:
dependencies:
  middleware:
    - name: FMOD / Wwise
      purpose: Audio middleware for adaptive music
      license: Free for indie budgets; paid above threshold
      risk: Medium — proprietary but industry standard
    - name: TextMeshPro
      purpose: Text rendering
      license: Free (Unity package)
      risk: Low — maintained by Unity
  services:
    - name: Steam SDK (Steamworks)
      purpose: Achievements, cloud saves, store integration
      risk: Low — required for Steam release
    - name: Analytics (Unity Analytics or custom)
      purpose: Player behavior tracking
      risk: Low — optional, privacy considerations
  policy:
    - "Prefer engine-native solutions over third-party when quality is comparable"
    - "No dependencies with restrictive licenses (GPL in proprietary game)"
    - "Document license type and cost for every dependency"
```

**LLM follow-on areas:**
- What is the license compatibility matrix?
- Are there open-source alternatives to proprietary middleware?
- What is the update and maintenance strategy for each dependency?
- What happens if a dependency is deprecated?
- Privacy and compliance implications of analytics services

---

## How This Level Drives the Next

Once Level 5 is answered, the LLM can:

1. **Plan the implementation** — engine, tools, and pipeline define *how*
   the team works day-to-day at L6.

2. **Identify infrastructure needs** — CI/CD, build servers, test devices,
   and hosting requirements become actionable tasks.

3. **Estimate technical risk** — engine limitations, dependency risks, and
   performance constraints surface risks before code is written.

4. **Set coding standards** — language, engine, and tools determine the
   coding conventions and patterns for L6.
