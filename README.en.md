# PhymLanguage — Chinese edition

> The **language reference + content library** for PhyModel's scene DSL (`.phym`) — one document *is* one
> scene you can tap, drag and simulate.

This repository is the **Chinese edition**: every document, every table and every figure caption is written
in Chinese, and the physics library keeps its Chinese chapter folders (`Physics/1 力学/…`). The full
project description is in [`README.md`](./README.md) (Chinese).

**English edition**: [`PhymLanguage_en`](https://github.com/phymodel/PhymLanguage_en) — the same document
tree with all of its prose in English (`Physics/1 Mechanics/…`). The two editions are kept in step by hand;
the DSL contract itself is identical, so a `.phym` snippet moves between them unchanged.

| Directory | Contents |
|---|---|
| `Entity/` | Entity reference: geometry, material, physics, plus the `CAD()` command stack |
| `Beh_Actions/` | Action reference: animation, motion, forces, audio, scene navigation |
| `Beh_Triggers/` | Trigger reference: tap, collide, proximity, slider, drag, throw |
| `Physics/` | Physics scenes organised by textbook chapter (derivation + runnable scene) |
| `Math/` | Maths scenes (Fourier series et al.) |
| `EmbodiedIntelligence/` | Worked example: phym as the **source** for 3D-printed parts (MicroDuck) |

## Opening it

**Web (read-only viewer, quickest)**

```bash
cd ../PhyModel_Web
./start-dev.command          # runs npm install on first launch, then opens http://localhost:5173
```

In the directory panel click **📁 choose folder** and pick this repository. Everything is read into browser
memory — **no upload, no disk writes**.

**Native (visionOS / iOS)**: point PhyModel's document library at this repository — you get interaction,
physics, speech and file sync.

## Language contract

One unit only: **metres**, **Y up** — a 30 mm diameter is a `0.015` radius. Interaction is declared by
triggers only (`.gesture(...)` has been removed from the DSL). `ModelURL()` has been removed too: parts are
modelled here, never imported as binary assets.
