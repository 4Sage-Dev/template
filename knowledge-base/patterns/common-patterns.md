# Common Game Design Patterns

Reference catalog of recurring game design patterns. Use this to identify which patterns apply to a given design, flag missing patterns, or warn about pattern misuse.

---

## Core Loop

**What it solves:** Gives the game a repeatable heartbeat that keeps players engaged moment-to-moment.

**How it works:** A short cycle of actions the player repeats throughout the game. Typically 3-4 steps that feed into each other. The output of the loop becomes the input for the next iteration.

**Structure:** Action -> Reward -> Upgrade -> Harder Action (repeat)

**When to use:** Every game needs one. Define it first. If you cannot describe your core loop in one sentence, the design is not ready.

**When to avoid:** N/A -- but beware of core loops that are satisfying in theory but tedious in practice. Prototype the loop before building content.

**Examples:**
- Diablo: Kill monsters -> Get loot -> Equip better gear -> Fight harder monsters
- Stardew Valley: Plant crops -> Wait/tend -> Harvest -> Sell -> Buy better seeds/tools
- Slay the Spire: Enter room -> Fight with cards -> Choose new card/relic -> Enter harder room

---

## Progression Systems

**What it solves:** Gives players a sense of forward momentum and growing mastery/power over time.

**How it works:** The player's character, abilities, or resources improve as they play. Can be numerical (stats go up), qualitative (new abilities unlock), or narrative (story advances).

**Types:**
- **Vertical progression:** Power increases linearly (levels, gear score)
- **Horizontal progression:** Options increase without power creep (new classes, cosmetics, side-grades)
- **Hybrid:** Combines both (common in RPGs)

**When to use:** Most games benefit from some form of progression. Essential for games longer than 2-3 hours.

**When to avoid:** Pure skill-based competitive games where progression would create unfair advantages (e.g., Counter-Strike keeps weapons equal). Short-form puzzle games where mastery IS the progression.

**Examples:**
- Dark Souls: Souls spent on level-ups and weapon upgrades (vertical)
- Smash Bros.: Unlocking new fighters (horizontal)
- Hades: Mirror upgrades (vertical) + weapon aspects (horizontal)

---

## Difficulty Curves

**What it solves:** Keeps the game challenging enough to be engaging without being frustrating.

**How it works:** The game increases difficulty over time, ideally matching the player's growing skill. Can be achieved through enemy stats, level complexity, mechanical demands, time pressure, or resource scarcity.

**Common shapes:**
- **Linear ramp:** Steady increase. Simple but can feel flat.
- **Staircase:** Plateaus with sharp jumps (often at boss fights). Creates rhythm.
- **Sawtooth:** Difficulty spikes then drops (new area is hard, then you gear up and it gets easier, then next area spikes again).
- **Adaptive/dynamic:** Game adjusts to player performance (RE4's hidden difficulty scaling).

**When to use:** Always. Even sandbox games benefit from escalating challenges or self-imposed difficulty.

**When to avoid:** The pattern itself always applies, but avoid rigid curves in games with high player skill variance. Offer difficulty options or adaptive systems instead.

**Examples:**
- Portal: Each test chamber teaches one concept, then combines concepts in later chambers (staircase)
- Resident Evil 4: Hidden adaptive difficulty adjusts enemy aggression and item drops based on player performance
- Celeste: Linear ramp in main story; B-sides and C-sides provide optional extreme difficulty

---

## Risk / Reward

**What it solves:** Creates meaningful decisions by making players weigh potential gains against potential losses.

**How it works:** The game offers choices where greater potential reward comes with greater potential loss. The player must assess their situation and decide how much to risk.

**When to use:** Whenever you want decisions to feel meaningful. Works in combat, exploration, resource management, gambling mechanics, and narrative choices.

**When to avoid:** When the "right" choice is always obvious (that is fake risk/reward). When the downside is so punishing it discourages experimentation in a game that should encourage it.

**Examples:**
- Darkest Dungeon: Push deeper into a dungeon for better loot, but risk party stress/death
- Poker (and poker-like mechanics): Bet more to win more, but lose more if wrong
- Spelunky: Ghost appears after time limit, punishing slow play but rewarding fast, risky exploration

---

## Resource Management

**What it solves:** Creates strategic depth through scarcity, forcing prioritization and planning.

**How it works:** Players have limited resources (currency, materials, ammo, health, time, energy, inventory space) and must decide how to allocate them. Resources are gained through gameplay and spent on upgrades, actions, or survival.

**Key design levers:**
- **Income rate:** How fast resources come in
- **Sink rate:** How fast they are consumed
- **Storage limits:** Caps that prevent hoarding
- **Conversion options:** Trade one resource for another

**When to use:** Strategy, survival, RPGs, management sims, city builders. Any game where planning ahead should matter.

**When to avoid:** Games focused on flow-state action where inventory management would break the pacing. Keep resource management complexity proportional to game depth.

**Examples:**
- Factorio: Entire game is resource management at industrial scale
- Resident Evil: Limited ammo and healing creates tension
- FTL: Scrap, fuel, missiles, drone parts -- all scarce, all critical

---

## Unlock Systems

**What it solves:** Provides long-term goals, rewards exploration/mastery, and drip-feeds content to avoid overwhelming new players.

**How it works:** Content (characters, levels, items, modes, cosmetics) starts locked and becomes available through play. Unlock conditions can be progression-based, achievement-based, discovery-based, or currency-based.

**When to use:** Games with large content pools. Helps with onboarding (don't show everything at once) and retention (always something new to work toward).

**When to avoid:** When locked content feels like artificial gatekeeping rather than earned reward. When competitive fairness requires all options be available from the start. When the unlock grind exists primarily to sell shortcuts (this is a monetization red flag, not a design pattern).

**Examples:**
- Mario Kart: Unlock vehicles and tracks through Grand Prix cups
- Smash Bros. Ultimate: Unlock fighters through play (roster of 80+ would overwhelm new players)
- Dead Cells: Unlock new weapons and abilities through cells found in runs

---

## Procedural Generation

**What it solves:** Creates variety and replayability without hand-crafting every piece of content.

**How it works:** Algorithms generate content (levels, maps, items, quests, terrain) at runtime using rules, seeds, and randomness. Quality depends on the strength of the ruleset.

**Approaches:**
- **Pure random:** High variety, low quality control (rarely used alone)
- **Template + variation:** Hand-authored chunks assembled randomly (most common)
- **Wave Function Collapse / constraint-based:** Generates content that satisfies rules (good for tilesets)
- **Seed-based:** Same input seed = same output (enables sharing and speedrunning)

**When to use:** Roguelikes, survival games, open-world games, any game where replayability is core.

**When to avoid:** Story-driven games where pacing and setpieces matter. Games where level design IS the content (Mario, Portal). Can produce mediocre results if rules are weak -- hand-crafted content is almost always higher quality per-piece.

**Examples:**
- Minecraft: Terrain, caves, structures generated from world seed
- Hades: Room layouts and encounter compositions randomized per run
- No Man's Sky: Entire planets generated procedurally

---

## Skill Trees

**What it solves:** Lets players customize their character build, creating personal investment and build diversity.

**How it works:** A branching structure of upgrades where players spend points to unlock abilities or passive bonuses. Branches typically represent different playstyles. Points are limited, forcing specialization.

**Variants:**
- **Tree:** Branching paths from a root (classic Diablo II)
- **Web/constellation:** Non-linear grid of nodes (Path of Exile)
- **Linear tracks:** Simple per-class upgrade lines (simpler games)

**When to use:** RPGs, action-RPGs, strategy games with hero units, games with class systems. When you want meaningful build decisions.

**When to avoid:** When all players should have the same capabilities (competitive shooters). When the tree has obvious "best" paths (illusion of choice). When the game is too short for the investment to pay off.

**Examples:**
- Path of Exile: Massive shared web with hundreds of nodes
- Borderlands: Three trees per character class, mix and match
- Horizon Zero Dawn: Skill categories for stealth, combat, and resource gathering

---

## Combo Systems

**What it solves:** Rewards skilled play with escalating power or score, creating a high skill ceiling.

**How it works:** Performing actions in sequence (attacks, moves, inputs) within timing windows yields enhanced effects. Longer/more complex combos yield greater rewards. Breaking a combo resets the counter.

**When to use:** Fighting games, action games (hack-and-slash), rhythm games, score-attack games. When you want deep mechanical mastery.

**When to avoid:** Slow-paced or strategic games. Games targeting very casual audiences (complex combos are intimidating). If combos are mandatory to progress, you exclude less skilled players.

**Examples:**
- Devil May Cry: Style meter rewards varied, uninterrupted combat combos
- Tony Hawk's Pro Skater: Chain tricks together for multiplied score
- Street Fighter: Input sequences for special moves and super combos

---

## Permadeath

**What it solves:** Makes every decision feel consequential. Creates emotional stakes and memorable stories.

**How it works:** When a character dies, they are gone permanently. May apply to the player character (roguelikes) or to squad members (XCOM). No reload, no undo.

**When to use:** Roguelikes/roguelites, tactical games with squad management, survival games. When you want tension and consequence.

**When to avoid:** Long narrative games where losing 40+ hours of progress would be devastating. Games targeting casual audiences who expect forgiveness. Always pair with systems that make starting over interesting (procedural gen, meta-progression).

**Examples:**
- XCOM: Soldiers die permanently; you feel every loss because you named and leveled them
- Hades: Player dies and restarts, but narrative continues between runs
- Fire Emblem (Classic mode): Lost units are gone for the rest of the campaign

---

## Save Systems

**What it solves:** Lets players stop and resume play. Also a design tool that affects tension and pacing.

**How it works:** Game state is serialized and stored for later retrieval.

**Types:**
| Type | Description | Effect on design |
|---|---|---|
| **Save anywhere** | Player saves at any time | Maximum convenience; reduces tension; enables save-scumming |
| **Checkpoint** | Game saves at specific points | Designer controls pacing; prevents save-scumming; can frustrate if checkpoints are sparse |
| **Save point** | Physical locations in-game (typewriters, bonfires) | Creates resource management around saving; adds exploration tension |
| **Auto-save** | Game saves automatically at intervals or triggers | Invisible to player; combine with manual save for safety |
| **No save (run-based)** | No persistent save within a run | Full commitment; used in roguelikes; sessions must be short enough |

**When to use:** Always have a save system unless the game is explicitly run-based. Match save type to desired tension level.

**When to avoid:** Don't use save-anywhere in games designed around tension and consequence. Don't use checkpoint-only in games with long, unskippable sections before difficulty spikes (the "boss behind a cutscene" problem).

**Examples:**
- Resident Evil: Typewriter save points with limited ink ribbons (resource management)
- Dark Souls: Constant auto-save, no manual save, no take-backs
- Celeste: Instant respawn at room start (effectively continuous checkpoint)

---

## Tutorial Design

**What it solves:** Teaches the player how to play without boring them or overwhelming them.

**How it works:** Introduces mechanics one at a time in a controlled environment, then lets the player apply them. The best tutorials are invisible -- the player learns by doing, not by reading.

**Principles:**
1. **Teach one thing at a time.** Don't stack new mechanics.
2. **Safe space to practice.** Low or no penalty while learning.
3. **Show, don't tell.** Level design that naturally teaches (see: World 1-1 of Super Mario Bros.).
4. **Let players skip.** Experienced players resent forced tutorials.
5. **Just-in-time.** Teach a mechanic right before the player needs it, not 30 minutes before.

**When to use:** Every game needs onboarding. The question is how invisible you can make it.

**When to avoid:** Avoid forced, unskippable, text-heavy tutorials. Avoid teaching mechanics the player won't use for hours. Avoid tutorials that prevent the player from playing (the "press A to walk forward" problem).

**Examples:**
- Super Mario Bros. World 1-1: Teaches running, jumping, power-ups, and enemies through level design alone
- Breath of the Wild: Great Plateau is a tutorial area that feels like open-world exploration
- Vampire Survivors: No tutorial; game is simple enough that playing IS learning

---

## Daily Rewards / Login Bonuses

**What it solves:** Drives habitual engagement and daily active user (DAU) metrics.

**How it works:** Players receive escalating rewards for logging in on consecutive days. Missing a day may reset the streak or simply skip that day's reward.

**When to use:** Free-to-play games, live-service games, mobile games where DAU drives ad revenue or engagement metrics.

**When to avoid:** Premium single-player games (feels manipulative and out of place). Games where you want players to play at their own pace. If the reward for logging in is better than the reward for playing, the system is broken. Increasingly viewed negatively by players as a transparent retention trick -- use with care.

**Examples:**
- Genshin Impact: Daily commission rewards plus monthly login calendar
- Wordle: Not a reward system, but the daily puzzle format drives habitual play (better design)
- Fall Guys: Daily shop rotation and challenges create daily check-in incentive

---

## Loot Tables

**What it solves:** Controls item distribution, creating desirable rarities and farming targets.

**How it works:** Each enemy, chest, or event has a table of possible drops with associated probabilities. Tables can be weighted by rarity tier, player level, game state, or other conditions.

**Key concepts:**
- **Rarity tiers:** Common > Uncommon > Rare > Epic > Legendary (or similar)
- **Pity/mercy system:** Guarantees a rare drop after N unsuccessful attempts
- **Weighted random:** Not uniform distribution; tuned for desired pace
- **Context-sensitive drops:** Different tables for different enemies/areas/difficulties
- **Pseudo-random distribution:** Avoids streaks by adjusting probability after each result

**When to use:** Looter games, RPGs, gacha, any game where randomized rewards drive replayability.

**When to avoid:** Games where fairness requires deterministic outcomes. If drop rates are so low they feel punishing rather than exciting. If loot tables interact with paid currency (legal and ethical considerations around gambling mechanics).

**Examples:**
- Diablo IV: Every monster has drop tables tuned by level, difficulty, and area
- Destiny 2: Raid bosses have specific loot pools that players farm
- Monster Hunter: Material drop rates drive the "just one more hunt" loop

---

## Matchmaking

**What it solves:** Creates fair, competitive, and enjoyable multiplayer matches by pairing players of similar skill.

**How it works:** Players are assigned a skill rating (visible or hidden). The matchmaking system finds opponents/teammates with similar ratings. Common algorithms: Elo, Glicko-2, TrueSkill.

**Key design decisions:**
- **Visible vs. hidden MMR:** Visible creates ranked anxiety but also aspiration. Hidden reduces toxicity but feels opaque.
- **Queue time vs. match quality:** Wider skill range = faster queues but worse matches.
- **New player placement:** Calibration matches (5-10 games) or start low and climb.
- **Smurf detection:** Rapid win-rate adjustment for accounts performing above their rating.
- **Party/group handling:** Mixed-skill groups require compromise (match to highest, average, or weighted).

**When to use:** Any competitive multiplayer game with enough concurrent players to form matches.

**When to avoid:** When the player base is too small for meaningful skill brackets (better to optimize for queue time). Co-op PvE games where exact skill matching matters less. Games with <1000 concurrent users will struggle with tight matchmaking.

**Examples:**
- League of Legends: Visible ranked tiers (Iron through Challenger) backed by hidden MMR
- Overwatch 2: Role-based matchmaking with separate ratings per role
- Rocket League: Visible rank with transparent MMR adjustments

---

## Pattern Interactions

Patterns rarely exist in isolation. Common pairings:

| Pattern A | Pattern B | Interaction |
|---|---|---|
| Core Loop | Progression Systems | Progression gives the core loop a direction and sense of growth |
| Loot Tables | Risk/Reward | Higher-risk content drops better loot, motivating engagement |
| Permadeath | Procedural Generation | New content each run makes restarting interesting rather than tedious |
| Skill Trees | Unlock Systems | Tree nodes are unlocked over time, gating complexity |
| Difficulty Curves | Tutorial Design | Tutorial IS the early difficulty curve |
| Daily Rewards | Resource Management | Login rewards feed into resource economy |
| Matchmaking | Progression Systems | Tension: skill-based matchmaking vs. gear-based progression can conflict |
| Combo Systems | Risk/Reward | Extending a combo risks losing the whole chain but yields higher score |

When consulting on a design, check which patterns are present and whether their interactions are intentional and well-tuned.
