# PhymLanguage

> The **language reference + content library** for PhyModel's scene DSL (`.phym`) — one document *is* one
> scene you can tap, drag and simulate.

This repository contains **no engine code**. It is a document library read by [PhyModel](#related-repositories)
(visionOS / iOS, RealityKit) and PhyModel_Web (browser): an `.md` file is both the manual page and the scene
source — the prose is the board on the wall, the fenced DSL *is* the scene. The renderers, editors and
parsers live in the sibling repositories.

## What's in here

| Directory | Contents | Size |
|---|---|---|
| [`Entity/`](./Entity) | Entity reference: geometry, material, physics, plus the `CAD()` command stack | 10 entity types · 14 CAD commands |
| [`Beh_Actions/`](./Beh_Actions) | Action reference: animation, motion, forces, audio, scene navigation | 15 actions |
| [`Beh_Triggers/`](./Beh_Triggers) | Trigger reference: tap, collide, proximity, slider, drag, throw | 6 triggers |
| [`Physics/`](./Physics) | Physics scenes organised by textbook chapter (derivation + runnable scene) | 8 chapters · 61 `.md` · 29 `.html` figures |
| [`Math/`](./Math) | Maths scenes (Fourier series et al.) | 4 waveform scenes |
| [`EmbodiedIntelligence/`](./EmbodiedIntelligence) | Worked example: phym as the **source** for 3D-printed parts | MicroDuck parts |

## A document is a scene

One `.md` carries everything; there is no separate project file:

| What you write | What the reader does with it |
|---|---|
| Prose (Markdown + LaTeX) | The document panel; `Latex()` / `LatexPath()` can also lift that prose into the 3D scene as a board |
| A ```` ```phymodel ```` fence | **Scene content**: entities + behaviours, merged into the scene in document order |
| `![Entity](./01 Entity.phym)` | **Fragment include**: the DSL in that `.phym` is merged in place (resolved relative to the current `.md`, spaces allowed, ignored inside code fences, nesting followed, cycles refused) |
| `![ca](./HCP_ca.html)` | **HTML figure**: a `sandbox=""` iframe — a picture, not a broken image |
| `![](./tex.png)`, `.material(imagePath:)` | Bitmap texture / illustration, path likewise relative to the current `.md` |

The library is therefore a directory tree you can **run**: change a line, reload, the scene changes.

## Minimal runnable scene

```phymodel
CAD()
.name("plate1")
.mesh(commands: [
    "DEF plate = PATH 0,0,0 Y 0.15,0.15 -0.15,0.15 -0.15,-0.15 0.15,-0.15 EXT 0.005 FILLET_V 0.01",
])
.material(red: 0.46, green: 0.2, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.physic(mass: 0.2, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .dynamic)
.position(x: 0, y: 1.5, z: 0)

Behavior()
.name("tapPlate1")
.trigger{
    Tap(){
        objects: ["plate1"]
    }
}
.actions{
    Spin(1){
        objects: ["plate1"],
        iterations: 2.0,
        clockwise: true,
        axis: .yaw,
        duration: 3
    }
}
```

A plate that spins twice when tapped. Paste it into the ```` ```phymodel ```` fence of any `.md`.

## Opening / running it

**Web (read-only viewer, quickest)**

```bash
cd ../PhyModel_Web
./start-dev.command          # runs npm install on first launch, then opens http://localhost:5173
```

In the directory panel click **📁 choose folder** and pick this repository (or drag the folder in). Everything
is read into browser memory — **no upload, no disk writes**; a page reload means picking it again.

**Native (visionOS / iOS)**: point PhyModel's document library at this repository — you get interaction,
physics, speech and iCloud sync.

## DSL cheat sheet

### Common modifiers

Every entity starts with `.name(...)` and chains whatever else it needs:

| Modifier | Example | Meaning |
|---|---|---|
| `.name(...)` | `.name("plate1")` | Entity name — behaviours address the entity by this; required |
| `.mesh(...)` | `.mesh(text: "hello")` | Geometry definition; parameters depend on the entity type; required |
| `.physic(...)` | `.physic(mass: 0.2, …, mode: .dynamic)` | Mass / static friction / dynamic friction / restitution / mode (`.dynamic` `.kinematic` `.static`) |
| `.material(...)` | `.material(red: 0.46, …, metallic: 0.8, imagePath: "./tex.png")` | Colour, opacity, roughness, metallic, optional texture |
| `.position(...)` | `.position(x: 0, y: 1.5, z: 0)` | World position (**metres**) |
| `.rotation(...)` | `.rotation(angle: 90, axis: [0,0,1])` | Rotation about an axis (degrees) |
| `.isEnabled(...)` | `.isEnabled(false)` | Whether it takes part in rendering and physics |
| `.simulation(...)` | `.simulation(wind: (0.6, 0, 0.4), windEnabled: true)` | Simulation parameters for cloth-like types |

There is exactly one unit system: **metres**, **Y up**. Font size, radius and offsets are all metres — a
30 mm diameter is a radius of `0.015`.

### Entities (10)

| Entity | Purpose | Docs |
|---|---|---|
| `CAD()` | Command-stack modelling: profile extrusion, solids of revolution, isosurfaces, booleans, loft, shell | [`Entity/Entity_CAD/`](./Entity/Entity_CAD) |
| `Polyhedron()` | The five Platonic solids | [Polyhedron.md](./Entity/Polyhedron.md) |
| `Text()` | Real 3D text — the strokes have thickness, cast shadows and collide | [Text.md](./Entity/Text.md) |
| `Latex()` | Markdown + LaTeX rendered onto a 3D plane; `textPath` can pull a section straight out of an `.md` | [Latex.md](./Entity/Entity_Latex/Latex.md) |
| `Graph()` | Parametric curve (`x` / `y` / `z` / `t` expressions) meshed as a tube | [Graph.md](./Entity/Graph.md) |
| `Tree()` | Procedural tree; `growthProgress` runs it from sapling to grown | [Tree.md](./Entity/Tree.md) |
| `HeightMap()` | Terrain from stacked procedural waveform layers | [HeightMap.md](./Entity/HeightMap.md) |
| `Cloth()` | Cloth / skirt with a wind field (`.dynamic` unsupported) | [Cloth.md](./Entity/Entity_Cloth/Cloth.md) |
| `HEWF()` | Hydrogen electron wave function ψ<sub>nℓm</sub> — real quantum-orbital clouds | [HEWF.md](./Entity/HEWF.md) |
| `Group()` | Names its members; groups flat entities into one body | [Group.md](./Entity/Group.md) |

The `CAD()` command stack ([full reference](./Entity/Entity_CAD)):

| Category | Commands |
|---|---|
| Profile extrusion | `PATH` (vertex ring) · `PATH_FORMULA` (implicit `f(x,y)=0`) · `PATH_FORMULA_XY` (parametric `x(t)`/`y(t)`) |
| Solids of revolution | `PATH_OPEN` + `REV` (open chain revolved about an axis) |
| Solid modelling | `SOLID_FORMULA` (implicit `f(x,y,z)=0`, marching cubes) · `LOFT` (varying cross-section) · `SHELL` (hollow out) |
| Curve sweeps | `EXT_Bezier` · `EXT_BSpline` |
| Fillets | `FILLET` · `FILLET_H` (horizontal edges) · `FILLET_V` (vertical edges) |
| Booleans | `UNION` · `SUBTRACT` · `INTERSECT` |

### Triggers (6)

| Trigger | Fires when |
|---|---|
| [`Tap`](./Beh_Triggers/TriggerTap.md) | An entity is tapped (under 0.25 s and 1 cm, so it never counts as a throw) |
| [`Collide`](./Beh_Triggers/TriggerCollide.md) | The entity collides with the named entities |
| [`Proximity`](./Beh_Triggers/TriggerProximity.md) | The camera comes within `distance` metres |
| [`Slider`](./Beh_Triggers/TriggerSlider.md) | The entity is dragged; its displacement is exposed to actions via `output` |
| [`Drag`](./Beh_Triggers/TriggerDrag.md) | A carried entity reaches its `target` |
| [`Throw`](./Beh_Triggers/TriggerThrow.md) | The entity is thrown, or passes through a `through` target |

### Actions (15)

| Category | Actions |
|---|---|
| Transform | [`Transform`](./Beh_Actions/Transform.md) (translation / rotation / scale; targets are absolute) · [`Spin`](./Beh_Actions/Spin.md) · [`Orbit`](./Beh_Actions/Orbit.md) · [`MoveAlong`](./Beh_Actions/MoveAlong.md) · [`LookAtCamera`](./Beh_Actions/LookAtCamera.md) |
| Visibility | [`Show`](./Beh_Actions/Show.md) · [`Hide`](./Beh_Actions/Hide.md) · [`Emphasize`](./Beh_Actions/Emphasize.md) |
| Physics & runtime | [`AddForce`](./Beh_Actions/AddForce.md) · [`EntityMesh`](./Beh_Actions/EntityMesh.md) (runtime geometry: parametric curves, tree growth) |
| Audio & speech | [`PlaySound`](./Beh_Actions/PlaySound.md) · [`PlayMusic`](./Beh_Actions/PlayMusic.md) · [`Speak`](./Beh_Actions/Speak.md) |
| Flow | [`Wait`](./Beh_Actions/Wait.md) · [`OpenScene`](./Beh_Actions/OpenScene.md) (navigate to another `.md` in the library) |

### Behaviours and loops

```phymodel
Behavior()
.name("tapPlate1")
.trigger{
    Tap(){
        objects: ["plate1"]
    }
}
.actions{
    Transform(1){
        objects: ["plate1"],
        translation: [0.0, 1.7, 0.0],
        duration: 1.5
    }
    Wait(2){
        duration: 0.5
    }
    Transform(3){
        objects: ["plate1"],
        translation: [0.0, 1.5, 0.0],
        duration: 1.5
    }
}
```

- Actions inside `.actions { … }` run **in order, as a queue**: the number after the name is the block's
  sequence id (`Transform(1)`, `Wait(2)`, `Transform(3)`), and `Wait` is simply a gap in that queue.
- `Transform`'s `translation` is an **absolute target pose, not a delta** — so "lift, then put back" has to
  repeat the original `.position(...)` value; writing `[0, -0.2, 0]` would teleport the entity there.
- Interaction is declared **by triggers only**: the entity-level `.gesture(...)` modifier has been removed and
  writing it is an error, so an entity no trigger names is pure decoration — a stray tap can never fire the
  wrong behaviour.
- For many entities at once use `Repeat(11) { i in … }` with interpolation in the name: `.name("tick[i]")`.

## Physics and maths library

`Physics/` follows the textbook's chapter structure; each page pairs a derivation with a runnable scene:

| Ch. | Directory | Coverage |
|---|---|---|
| 1 | [`1 Mechanics/`](./Physics/1%20Mechanics) | Kinematics · statics · dynamics (Newton's laws, projectiles, circular motion, momentum and energy, SHM…) |
| 2 | [`2 Thermodynamics/`](./Physics/2%20Thermodynamics) | Boyle / Charles / Gay-Lussac, first law, fundamental equation |
| 3 | [`3 Optics/`](./Physics/3%20Optics) | Snell's law, spherical refraction, thin lenses |
| 4 | [`4 Electromagnetism/`](./Physics/4%20Electromagnetism) | Charge to field, circuits, magnetism, induction, AC and transformers (21 pages) |
| 5 | [`5 MathematicalMethodsOfPhysics/`](./Physics/5%20MathematicalMethodsOfPhysics) | Fourier transform |
| 6 | [`6 AtomicPhysics/`](./Physics/6%20AtomicPhysics) | Half-life, mass–energy equation |
| 7 | [`7 QuantumMechanics/`](./Physics/7%20QuantumMechanics) | Energy quanta, photoelectric effect, photon momentum, frequency condition |
| 8 | [`8 SolidStatePhysics/`](./Physics/8%20SolidStatePhysics) | Hexagonal close packing (with an interactive `.html` figure) |

`Math/` currently holds [Fourier series](./Math/Advanced%20Mathematics/Fourier%20series): the decomposition
and synthesis of sawtooth, square, triangle and pulse waves, with derivations and waveform entities side by
side.

## Worked example: phym as the source file for parts

[`EmbodiedIntelligence/MicroDuck/`](./EmbodiedIntelligence/MicroDuck) rewrites a set of 3D-printed parts in
phym: a part is no longer a binary STL but modelling commands that diff, parameterise and recompute —

```text
phym code (this repo) ──render──▶ ⚙︎ Settings → export entity ──▶ STL / 3MF ──▶ slice and print
```

The direction is **one-way**: this repository is always the source, an exported STL is a product. Change a
dimension in phym and export again.

## Conventions

Keep these when adding content — they are what makes the library machine-readable:

1. **One source of units**: metres, Y up; dimensions live in the DSL, never in an asset file.
2. **No external binary models**: `ModelURL()` has been removed from the DSL — external assets break diffing,
   replay and export, so the parser now answers it with a migration error.
3. **One `.md` per entity / trigger / action**, same shape: `# Name` → `> signature` → `## Purpose` →
   `## Parameters` → `## Constraints` → `## Example`.
4. **Examples must run as written**: the `Example` code stands on its own (entities + behaviours), and names
   the entities it depends on.
5. **Interaction is declared by triggers**, never by a `.gesture(...)` on an entity.
6. **Stay in sync with the engines**: this repository describes the DSL *contract*, so removing or renaming a
   keyword leaves a migration note in place (as `ModelURL()` and `.gesture(...)` both do).

## Related repositories

This repository is the single source of content and contract; both renderers are sibling checkouts:

| Repository | Role |
|---|---|
| `PhyModel` | Native renderer / editor (visionOS, iOS; RealityKit + iCloud, MiniAGI conversation) |
| `PhyModel_Web` | Browser side (Vite + React + react-three-fiber/Three.js, Rapier / Jolt physics, marked + KaTeX; read-only viewer + AI chat, `src/dsl/` is the web parser) |
| **PhymLanguage** (this repo) | DSL reference + scene library, read by both of the above |

## License

There is currently **no `LICENSE` file** at the repository root, i.e. all rights reserved by default. If you
want to reuse these documents or scenes elsewhere, please check with the author first.
