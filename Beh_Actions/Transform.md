# Transform

> `Transform(objects: [String], scale: [Float×3]? = nil, rotation(angle: angle:axis:)? = nil, translation: [Float×3]? = nil, easeType: EaseType = .none, duration: Float = 0)`

## Purpose

Applies a combination of scale, rotation, and/or translation to target entities, with optional easing and animation over a duration.

## Parameters

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| objects | [String] | ✅ | — | Target entity names. Accepts a range spec `"Prefix[0..4]"` (expands to one action per instance) and the legacy single-target spelling `object: "Name"` |
| scale | [Float×3] | ❌ | nil | Target scale `[sx, sy, sz]`; when omitted the target scale is **1** (see Semantics) |
| rotation(angle:axis:) | (Float, [Float×3]) | ❌ | nil | Rotation by `angle` (degrees) around `axis` `[x, y, z]`; when omitted the target rotation is **identity** |
| translation | [Float×3] | ❌ | nil | Target position `[x, y, z]` in world units — **absolute target, not an offset**; when omitted it is **(0, 0, 0)** |
| easeType | enum | ❌ | .easeOut | `.none` `.easeOut` `.easeIn` `.easeInOut`. Currently parsed but **not consumed** by the runtime (the timing function is fixed to `.easeInOut`) |
| duration | Float | ❌ | 1.0 | Animation duration (seconds); 0 = apply immediately, no animation |

## Target ranges and per-instance `index` (new)

`objects` accepts a range spec, so a whole family of instances can be driven by one block:

```phymodel
Transform(1){
    objects: ["PulseSphere[0..4]"],
    translation: [-0.5 + index * 0.1/pi, 1.5, 0.0],
    duration: 0
}
```

- `"PulseSphere[0..4]"` expands to `PulseSphere0 … PulseSphere4`; every expanded action keeps the block `id`, so the instances run **in parallel**, exactly as if the blocks had been written out one by one.
- `index` (alias `i`) is the instance index inside that range, usable in `scale:`, `translation:` and `rotation(angle:axis:)`.
- Components are full math expressions (`pi`, `2*pi`, `+ - * /`, ternary, `%`), evaluated by the same engine as `Graph().mesh(...)` and `MoveAlong`'s `tStart` / `tEnd`.
- A plain name (no `[a..b]`) may also use expressions; its `index` is 0.
- A malformed range (`"Node[0-2]"`) or an expression that cannot be evaluated is reported as a parse error and the action is dropped — it never silently falls back to `(0, 0, 0)`.
- `objects` / `object` may be written with several names (`objects: ["a", "b"]`); each becomes its own action.

## Semantics of `translation` / `duration`

- `duration == 0`: the entity's transform is **overwritten** — `translation` is the absolute pose and every field you did not supply is reset (scale → 1, rotation → identity, translation → `(0, 0, 0)`).
- `duration > 0`: animates from the pose at action start to that absolute target; unspecified fields still resolve to the defaults above.
- Consequence: `translation` is a **target position**, not a delta. A “reset to the initial pose” block therefore has to repeat the declared `.position(...)` values (or mirror their expression, e.g. `-0.5 + index * 0.1/pi`).

## Constraints

- Only affects **ModelEntity** instances (all entity types supported: CAD, Text, Graph, Tree, HeightMap, etc.).
- At least one of `scale`, `rotation`, or `translation` should be provided; an action with all nil is a no-op.
- Rotation uses the angle–axis representation: `rotation(angle: -90, axis: [1, 0, 0])` rotates -90° around the X axis.
- `Transform` does not switch the entity to `.kinematic` — physics continue to apply during the animation.

## Example

### Entities

```phymodel

HeightMap()
.name("heightMap1")
.mesh(size: (2, 2), thickness: 0.2, resolution: (64, 64))
.physic(mass: 0.8, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .dynamic)
.material(red: 0.6, green: 0.3, blue: 0.2, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 0.0, y: 0.8, z: 0.0)

```

### Trigger System

```phymodel

Behavior()
.name("tapHeightMap1")
.trigger{
    Tap(){
        objects: ["heightMap1"]
    }
}
.actions{
    Transform(1){
        objects: ["heightMap1"],
        scale: [1.0, 1.0, 1.0],
        rotation(angle: -90, axis: [1,0,0]),
        translation: [0.0, 0.1, -1.5],
        easeType: .easeOut,
        duration: 3.0
    }
}

```
