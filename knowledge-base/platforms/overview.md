# Game Platforms Reference

Quick-reference for major game platforms. Use this to ground platform recommendations in real hardware constraints, store policies, and audience expectations.

---

## PC (Steam)

| Attribute | Details |
|---|---|
| **Input methods** | Keyboard + mouse (primary); gamepad; touch (Steam Deck); VR controllers |
| **Performance range** | Extremely wide. Low end: integrated graphics, 8GB RAM. High end: RTX 4090, 64GB RAM. Target minimum spec matters more than max. |
| **Typical resolutions** | 1920x1080 (most common), 2560x1440, 3840x2160; ultrawide 3440x1440; Steam Deck 1280x800 |
| **Store/distribution** | Steam (dominant), Epic Games Store, GOG, itch.io, direct/DRM-free |
| **Certification** | None required. Steam has a review process (~2-5 business days) but no formal cert. |
| **Monetization rules** | Steam takes 30% cut (drops to 25% at $10M, 20% at $50M). Supports premium, F2P, DLC, MTX, subscriptions. External payment links prohibited in-app. |
| **Audience** | Broadest range. Skews 18-35 male but all demographics present. Strong indie and niche communities. |

**Key notes:**
- Steam Deck compatibility is increasingly important. Test with gamepad and 800p.
- Steam wishlists are a critical marketing metric. 7-10 wishlists per day-1 sale is a common ratio.
- Refund policy: automatic refund if <2 hrs playtime and <14 days owned. Design first impressions accordingly.
- Steam Next Fest demos drive significant wishlist growth.

---

## Nintendo Switch

| Attribute | Details |
|---|---|
| **Input methods** | Joy-Con (detached or attached), Pro Controller, touchscreen (handheld mode), motion controls |
| **Performance** | Custom NVIDIA Tegra X1. Roughly equivalent to a mobile GPU from 2015. 4GB RAM. CPU is the primary bottleneck for most games. |
| **Typical resolutions** | Handheld: 1280x720. Docked: 1920x1080 (many games render lower and upscale). |
| **Store/distribution** | Nintendo eShop (only official channel) |
| **Certification** | Nintendo lotcheck process required. Strict quality and content guidelines. Can take weeks. |
| **Monetization rules** | Nintendo takes 30%. Supports premium, DLC, F2P with IAP. Loot boxes face scrutiny. Must comply with parental controls API. |
| **Audience** | All ages; strongest with families, kids, and Nintendo franchise fans. Large casual audience. Japan is a major market. |

**Key notes:**
- Performance is the primary constraint. Budget CPU/GPU carefully. Target 30fps as baseline.
- Successor console (Switch 2) expected 2025; plan for potential cross-gen.
- Local multiplayer is a strong selling point on this platform.
- eShop discoverability is poor. External marketing matters more here.

---

## PlayStation 5

| Attribute | Details |
|---|---|
| **Input methods** | DualSense controller (haptic feedback, adaptive triggers, touchpad, gyro, speaker, mic) |
| **Performance** | Custom AMD Zen 2 CPU (8-core, 3.5 GHz), RDNA 2 GPU (10.28 TFLOPS), 16GB GDDR6, custom SSD (5.5 GB/s raw). |
| **Typical resolutions** | 1920x1080, 2560x1440, 3840x2160; performance/quality mode toggle is standard. VRR support. |
| **Store/distribution** | PlayStation Store (digital), physical disc retail |
| **Certification** | Sony Technical Requirements Checklist (TRC). Formal QA certification required. Process takes 1-4 weeks. Strict rules on crashes, load times, trophy implementation, DualSense features. |
| **Monetization rules** | Sony takes 30%. Supports premium, F2P, DLC, MTX, subscriptions. PS Plus tiers affect discoverability. |
| **Audience** | Skews 18-35 male. Strong single-player narrative audience. Large in North America, Europe, Japan. |

**Key notes:**
- DualSense features (haptics, adaptive triggers) are expected by players and reviewers. Budget time for implementation.
- SSD speed means load screens should be minimal or absent. Long loads are noticed and criticized.
- Trophy system is mandatory. Plan achievements during design.
- PS Plus Essential/Extra/Premium tiers affect game economics (day-one catalog inclusion deals).

---

## Xbox Series X|S

| Attribute | Details |
|---|---|
| **Input methods** | Xbox Wireless Controller (no haptic feedback comparable to DualSense; standard rumble, impulse triggers) |
| **Performance** | **Series X:** Custom AMD Zen 2 CPU (8-core, 3.8 GHz), RDNA 2 GPU (12 TFLOPS), 16GB GDDR6, 1TB SSD. **Series S:** Same CPU at 3.6 GHz, 4 TFLOPS GPU, 10GB RAM, 512GB SSD. |
| **Typical resolutions** | Series X: targets 4K. Series S: targets 1440p or 1080p. Must support both SKUs. |
| **Store/distribution** | Microsoft Store (digital), physical disc retail (Series X only; Series S is digital-only) |
| **Certification** | Xbox Requirements (XRs). Formal certification required. Similar timeline to PlayStation. Must pass on both Series X and Series S. |
| **Monetization rules** | Microsoft takes 30% (reduced to 12% for PC Microsoft Store titles in some programs). Supports premium, F2P, DLC, MTX. |
| **Audience** | Skews 18-35 male. Strong in North America and UK. Game Pass shapes purchasing behavior heavily. |

**Key notes:**
- **Series S is a real constraint.** Lower GPU, less RAM. Cannot ignore it. Design scalable rendering.
- **Game Pass** is the dominant platform dynamic. Day-one Game Pass inclusion drives massive player counts but changes revenue model (lump-sum deal vs. per-unit sales).
- Smart Delivery: single purchase covers both Series X and Series S. Cross-gen (Xbox One) is fading but check market.
- Play Anywhere: some titles support cross-buy with PC (Windows Store).

---

## iOS (iPhone / iPad)

| Attribute | Details |
|---|---|
| **Input methods** | Touchscreen (primary), gamepad (MFi / Bluetooth controllers), keyboard (iPad) |
| **Performance** | Wide range. Low end: iPhone SE (A15, 4GB RAM). High end: iPhone 16 Pro (A18 Pro, 8GB RAM). iPad Pro M-series chips rival laptops. |
| **Typical resolutions** | iPhone: 1170x2532 to 1320x2868. iPad: 2048x2732. Many aspect ratios; must handle notch/Dynamic Island safe areas. |
| **Store/distribution** | App Store (primary). EU allows alternative marketplaces (Digital Markets Act) as of 2024. |
| **Certification** | App Review required. 24-48 hrs typical. Content guidelines enforced (no real-money gambling without license, age ratings, privacy rules). Can be rejected for bugs, UI issues, or policy violations. |
| **Monetization rules** | Apple takes 30% (15% for Small Business Program under $1M/year). IAP mandatory for digital goods. No linking to external payment for digital content (except some regions post-DMA). Physical goods/services can use external payment. Subscription auto-renewal rules apply. |
| **Audience** | Broadest demographic of any platform. Casual-dominant. Higher average revenue per user than Android. Strong in North America, Europe, Japan. |

**Key notes:**
- Design for thumb reach zones and one-handed play where possible.
- Battery and thermal throttling are real constraints for intensive games. 15-minute thermal test is prudent.
- App Store Optimization (ASO): icon, screenshots, and first 3 sentences of description drive downloads.
- Privacy: ATT (App Tracking Transparency) framework required. IDFA access requires user opt-in.
- Minimum iOS version support: typically target current minus 2 (e.g., iOS 16+ in 2025).

---

## Android

| Attribute | Details |
|---|---|
| **Input methods** | Touchscreen (primary), gamepad (Bluetooth), keyboard |
| **Performance** | Extreme fragmentation. Low end: 2GB RAM, Mali-G52 GPU. High end: Snapdragon 8 Gen 3, 16GB RAM. Must test across tiers. |
| **Typical resolutions** | 1080x2400 most common; ranges from 720p budget phones to 1440p+ flagships. Many aspect ratios (16:9, 19.5:9, 20:9, foldables). |
| **Store/distribution** | Google Play Store (dominant), Samsung Galaxy Store, Amazon Appstore, third-party APK distribution, Epic Games Store |
| **Certification** | Google Play review: typically hours to a few days. Less strict than Apple but enforces content policies, target API level requirements, and data safety declarations. |
| **Monetization rules** | Google takes 30% (15% for first $1M/year). IAP required for digital goods in Play Store. Third-party stores have their own terms. Supports premium, F2P, ads, IAP, subscriptions. |
| **Audience** | Largest global install base. Dominant in Asia, South America, Africa. More price-sensitive than iOS. Ad-supported and F2P models perform well. |

**Key notes:**
- **Device fragmentation is the #1 challenge.** Test on at least 3-4 tiers of devices.
- Google Play requires targeting recent API levels (updated annually). Keep up or get delisted.
- Android Go (low-RAM devices) is a significant market in developing regions.
- Foldable phones are a growing segment; consider multi-window and flex-mode.
- Piracy rates are higher than iOS. Server-authoritative design helps protect revenue.

---

## Web / Browser

| Attribute | Details |
|---|---|
| **Input methods** | Keyboard + mouse (primary), touchscreen (mobile browsers), gamepad (Gamepad API) |
| **Performance** | Depends entirely on user's device and browser. JavaScript/WASM execution is slower than native. GPU access via WebGL 2 or WebGPU (emerging). 2-4GB effective memory budget is safe. |
| **Typical resolutions** | Anything from 360px wide (mobile) to 3840px (4K desktop). Must be responsive or declare minimum. |
| **Store/distribution** | Direct URL (no gatekeeper). Portals: itch.io, Newgrounds, Kongregate, CrazyGames, Poki. Facebook Instant Games. Discord Activities. |
| **Certification** | None for direct distribution. Portal-specific review if using a platform. |
| **Monetization rules** | No platform cut for direct distribution. Portal cuts vary (itch.io: creator sets %, CrazyGames: ad revenue share). Ad-supported is dominant. IAP possible via web payment APIs. |
| **Audience** | Very broad. Strong casual audience. Lower tolerance for long load times. High bounce rate if game doesn't start in <5 seconds. |

**Key notes:**
- **Instant access is the superpower.** No install, no app store. Share a link and play.
- Initial load size target: under 20MB for casual, under 50MB for mid-core. Lazy-load assets.
- WebGPU is the future but WebGL 2 is the safe baseline today.
- Common engines: Godot (web export), Unity (WebGL), Phaser, PlayCanvas, Three.js, Babylon.js.
- Mobile browser performance is significantly worse than native mobile apps. Test accordingly.
- No access to push notifications (limited), background processing, or local file system (without user action).

---

## Cross-Platform Considerations

| Factor | Guidance |
|---|---|
| **Cross-play** | Increasingly expected in multiplayer games. Each platform cert process tests cross-play flows separately. |
| **Cross-save** | Requires cloud save infrastructure. Platform holders have their own cloud save systems; cross-platform sync is custom work. |
| **Parity requirements** | Sony and Nintendo historically resist cross-play. Verify current policies per title. Content parity rules vary. |
| **Simultaneous launch** | Ideal but certification timelines differ. Budget 2-4 extra weeks for console cert vs. PC/mobile. |
| **Input abstraction** | Design for the least capable input method you support, then add richness for more capable inputs. |
| **Performance scaling** | If targeting both Switch and PS5, design for Switch first and scale up. Easier than scaling down. |
| **Revenue split** | All major stores take 30% baseline. Factor this into pricing. Direct sales (web, own store) avoid platform cuts. |
