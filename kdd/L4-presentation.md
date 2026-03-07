# Level 4: Presentation

> **Priority:** Mix of SH and NH — presentation serves the experience; style is a creative choice
> **Driven by:** L0 (platform, budget), L1 (emotional goals), L2 (camera, mechanics), L3 (world, content)
> **Drives:** Art/audio production pipeline, technical requirements (L5), asset creation (L6)

This level defines how the game looks, sounds, and feels at the surface level.
Presentation is the player's interface to the game — everything they see,
hear, and physically interact with. Good presentation amplifies good design;
poor presentation obscures it.

This is the level where art direction, audio design, UI/UX, and "game feel"
(juice, polish, tactile feedback) are decided.

---

## KDD-4.1: Art Direction & Visual Style

**Question:** What does the game look like? Define the visual identity.

**Why this matters:**
Art direction determines the entire visual production pipeline — 3D or 2D,
realistic or stylized, the number of unique assets needed, the team skills
required, and the performance budget. A stylized low-poly game can be
beautiful and cheap to produce. A photorealistic game requires enormous
resources. This must be realistic for the team and budget from L0.

**Priority:** SH — Art style is a creative choice, but must be achievable
within L0 constraints.

```answer
# Example:
art_direction:
  style: "Stylized low-poly with painterly textures"
  references: ["Firewatch", "Sable", "The Witness"]
  palette: "Warm earth tones, with vibrant accents for interactables"
  rendering:
    approach: Cel-shaded / toon shader
    fidelity: Medium — stylization over realism
    target_polycount: "Low — characters ~3K tris, environment ~500-2K tris"
  production_pipeline:
    modeling: "Low-poly in Blender"
    texturing: "Hand-painted in Substance Painter"
    animation: "Minimal — procedural + simple keyframe"
  asset_scope:
    unique_models_estimated: 200-300
    tilesets: 5-8 biome sets
    characters: 10-15 (player + NPCs + creatures)
```

**LLM follow-on areas:**
- Is this art style achievable by the team (L0)?
- Does the style serve the emotional goals (L1)?
- What is the asset reuse strategy?
- How does the style affect readability and accessibility?
- What are the performance implications per platform (L0)?

---

## KDD-4.2: Audio Design

**Question:** What does the game sound like? Define the audio identity.

**Why this matters:**
Audio is often underestimated but has outsized impact on emotional experience.
Music sets mood. Sound effects create tactile feedback. Ambient audio builds
atmosphere. Voice acting adds production cost and localization complexity.
Audio decisions directly affect the emotional experience (L1) and budget (L0).

**Priority:** SH — Audio is expected in all games; quality and scope
are budget-dependent.

```answer
# Example:
audio:
  music:
    style: "Ambient, atmospheric — sparse piano and strings"
    references: ["Journey OST", "Outer Wilds OST"]
    implementation: "Context-sensitive layers that respond to location and time"
    scope: "15-20 tracks, ~45 minutes of unique music"
    source: "Commissioned from composer"
  sound_effects:
    style: "Naturalistic with slight stylization"
    scope: "200-300 unique effects"
    priority_systems: [crafting, environment, UI, creatures]
    source: "Mix of library sounds and custom recordings"
  ambient:
    approach: "Dynamic ambient layers — wind, water, wildlife"
    variation: "Per-biome ambient profiles"
  voice:
    enabled: false
    rationale: "Budget constraint; text-based dialogue is sufficient"
  spatial_audio: "3D positional audio for environmental immersion"
```

**LLM follow-on areas:**
- Is the audio scope realistic for the budget?
- How does audio support the core emotions (L1)?
- What audio middleware is needed? (L5 implication)
- Accessibility: are there visual alternatives for all audio cues?
- Music licensing vs. original composition trade-offs

---

## KDD-4.3: User Interface Design

**Question:** How does the player interact with game systems through menus,
HUD elements, and information displays?

**Why this matters:**
UI is the player's primary tool for understanding and controlling the game.
Bad UI makes good mechanics frustrating. Good UI makes complex systems
approachable. UI design must balance information density with clarity,
and must work across all target platforms and input methods (L0).

**Priority:** SH — Genre conventions set strong expectations for UI patterns.

```answer
# Example:
ui:
  philosophy: "Minimal HUD — information in the world, not on the screen"
  hud_elements:
    persistent: ["Mini-compass", "Quick-slot bar (3 items)"]
    on_demand: ["Full map (toggle)", "Inventory (toggle)", "Journal (toggle)"]
    contextual: ["Interaction prompt", "Resource pickup notification"]
  menu_systems:
    - "Inventory — grid-based, drag and drop"
    - "Crafting — recipe list with material requirements"
    - "Map — hand-drawn style that fills in as explored"
    - "Journal — collected lore, quest tracking"
    - "Settings — audio, video, controls, accessibility"
  input_adaptation:
    keyboard_mouse: "Click-to-interact, WASD movement, scroll wheel zoom"
    controller: "Context-sensitive face buttons, radial menus"
    touch: "Not applicable (no mobile target)"
  accessibility:
    - "Scalable UI text"
    - "Color-blind safe palette with icon differentiation"
    - "Remappable controls"
    - "Subtitle options with speaker identification"
```

**LLM follow-on areas:**
- Does the UI support the "minimal" emotional goals (L1)?
- What UI frameworks or tools are available in the chosen engine?
- How does the UI scale across screen sizes and resolutions?
- What localization challenges does the UI create?
- Are there platform-specific UI requirements? (Steam Deck, console)

---

## KDD-4.4: Game Feel & Juice

**Question:** How does the game feel moment-to-moment? What feedback systems
create tactile satisfaction?

**Why this matters:**
"Game feel" — the micro-level feedback from every action — is what makes
the difference between a game that feels good and one that feels lifeless.
Screen shake, particle effects, animation curves, haptic feedback, sound
timing — these small details compound into the overall feeling of the game.
This is where L1's emotional goals become physical sensations.

**Priority:** NH — Game feel is polish, but it has disproportionate impact
on player satisfaction.

```answer
# Example:
game_feel:
  movement:
    responsiveness: "Immediate — no acceleration curve, instant stop"
    weight: "Light and agile — the player should feel free"
    camera_behavior: "Smooth follow with slight lag for momentum feel"
  interaction:
    gathering: "Satisfying 'pop' on resource collection, particle burst"
    crafting: "Building animation with progress, completion chime"
    discovery: "Musical sting + screen bloom on major discoveries"
  feedback_channels:
    visual: "Particle effects, screen effects (bloom, vignette)"
    audio: "Impact sounds, UI confirmation sounds"
    haptic: "Controller rumble on interactions (subtle)"
    camera: "Subtle zoom/shake on impactful moments"
```

**LLM follow-on areas:**
- Does the game feel align with the core emotions (L1)?
- Which feedback elements are highest priority for the prototype?
- What is the risk of over-polishing early?
- How is game feel tested and iterated?

---

## KDD-4.5: Accessibility

**Question:** What accessibility features will the game include?

**Why this matters:**
Accessibility is both ethical and practical — it expands the audience and
often improves the experience for all players. Platform certification may
require specific accessibility features (MH). Industry best practices set a
baseline (SH). Additional features expand reach (NH). Accessibility should
be designed in from the start, not bolted on at the end.

**Priority:** Mix — platform requirements are MH; best practices are SH;
expanded features are NH.

```answer
# Example:
accessibility:
  must_have:
    - "Remappable controls"
    - "Subtitle options"
    - "Scalable UI text"
    - "Color-blind considerations in UI (don't rely on color alone)"
  should_have:
    - "High-contrast mode"
    - "Screen reader support for menus"
    - "One-handed control option"
    - "Adjustable game speed"
  nice_to_have:
    - "Full audio descriptions"
    - "Cognitive accessibility options (simplified UI mode)"
  standards: "Target CVAA compliance and Xbox Accessibility Guidelines"
```

**LLM follow-on areas:**
- What platform-specific accessibility requirements exist?
- What accessibility features does the engine provide natively?
- How does accessibility testing work?
- What is the cost of each accessibility feature?
- Are there accessibility consultants or testing services to engage?

---

## How This Level Drives the Next

Once Level 4 is answered, the LLM can:

1. **Define technical requirements** — art style determines rendering
   pipeline, audio design determines middleware needs, UI determines
   framework choices (L5).

2. **Scope asset production** — the number and complexity of art assets,
   audio tracks, and UI screens define the production pipeline for L6.

3. **Identify tool needs** — the art pipeline may require specific tools
   (level editor, particle editor, audio middleware) that must be built
   or acquired at L5.

4. **Set performance targets** — visual fidelity and audio complexity
   constrain frame rate and memory budgets at L5.
