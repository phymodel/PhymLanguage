# Throw

> `Throw(objects: [String], through: [String])`

## Purpose

Grab any entity listed in `objects`, move it, and **let go with velocity** — this is the only trigger that keeps the release speed (a real throw). Optionally declare `through` to detect the thrown entity passing through a ring/frame (a basketball hoop, a target ring), and fire the `.actions` on the hit.

Two-stage event:

- `through` empty → the `.actions` run **on release** ("thrown").
- `through` non-empty → the `.actions` run **on the pass-through**, not on release, so a miss stays silent.

## Parameters

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| objects | [String] | ✅ | — | Entity names that can be grabbed and thrown |
| through | [String] | ❌ | — | Pass-through targets; the actions fire when the thrown entity crosses the target's hole |
| dragAxes | [String] | ❌ | all three axes | Restricts dragging before the release (e.g. only let it be lifted upward) |
| dragRangeX / dragRangeY / dragRangeZ | [Float, Float] | ❌ | unlimited | Clamps the dragged position along each axis (DSL local coordinates) |
| dragRangeR | [Float, Float] | ❌ | unlimited | Clamps the radial distance from the drag start point |

## Constraints

- Throwing is declared **by this trigger** — the entity must be named in `Throw(){ objects: […] }` (no entity-level switch; `.gesture(...)` has been removed).
- **Only `Throw` keeps the release velocity.** `Slider` / `Drag` stop the entity where you let go (contract D2). The release velocity is sampled from the entity's position delta, clamped to ±5 m/s and scaled by 1.2; the angular velocity is currently random (configurable `speedScale` / `spin` are pending — see `Docs/TriggerContract.md` §3).
- The thrown entity must be `.physic(mode: .dynamic)` — the release velocity is applied as a physics motion, so a `.kinematic` entity simply stops when you let go.
- A `through` target **must use `.physic(mode: .static)` or `.physic(mode: .kinematic)`** so it keeps an exact triangle-mesh collider. A `.dynamic` target degenerates to a convex hull, which **seals the hole** and the entity can never pass through.
- The hole axis is derived from the target's **local bounding box**: the thinnest axis is the hole axis, and the hole's lateral extent is the largest half-extent of the other two axes. A ring generated in the XZ plane therefore has a vertical hole axis, and rotating the target rotates the hole with it.
- The hit test is geometric: the segment "previous frame position → current frame position" is intersected with the hole plane, and the intersection must fall inside the lateral extent. This is tunnel-proof at high speed and does not rely on collision events.
- A real "throw" needs a release speed of at least **0.5 m/s**; slower than that counts as placing the object and no pass-through is judged.
- One throw settles each target **at most once**: the session ends on hit, after a 5 s timeout, or once the entity has come to rest.
- The pass-through is judged in flight; a ball that is merely carried through the ring by hand does not count.
- Platform: on visionOS, pinch and fling your hand. On iOS, **press and hold to grab and release to throw**: the entity follows the device while your finger is down, and the release velocity is sampled frame by frame from its position delta, per-axis clamped to ±5 m/s and scaled by 1.2 with a random spin (the same constants as visionOS), so a `through` target **is** judged on iOS (contract D5). A quick tap is not a grab — it only feeds `Tap` triggers, so tapping a throwable never counts as a release. The web build **can** throw: the release velocity is sampled from the carried entity's position delta over the last ~0.15 s of pointer movement, per-axis clamped to ±5 m/s, scaled by 1.2 and given a random spin (the same constants as visionOS), so a `through` target is judged there — a slow, deliberate placement stays a put (< 0.5 m/s, no session), and one throw settles each target at most once (5 s timeout, or once the entity comes to rest). On any platform the thrown entity must be in the physics layer (`.physic(mode: .dynamic)`); otherwise there is no body to receive the velocity and it simply stops where you let go.

## Example

- sphere: $(x/0.1)^2+(y/0.1)^2+(z/0.1)^2-1=0$
- torus: $(x^2+z^2+y^2+0.15^2-0.05^2)^2-4*0.15^2*(x^2+z^2)=0$

### Entities

```phymodel

CAD()
.name("sphere")
.mesh(commands: [
    "DEF sphere = SOLID_FORMULA 0,0,0 (x/0.1)^2+(y/0.1)^2+(z/0.1)^2-1=0",
])
.physic(mass: 0.6, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .dynamic)
.material(red: 0.67, green: 0.32, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 0.5, y: 1.5, z: 0.0)

CAD()
.name("torus")
.mesh(commands: [
    "DEF torus = SOLID_FORMULA 0,0,0 (x^2+z^2+y^2+0.225^2-0.02^2)^2-4*0.225^2*(x^2+z^2)=0 0.25 48",
])
.physic(mass: 0.3, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .static)
.material(red: 0.8, green: 0.2, blue: 0.4, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 0.0, y: 1.0, z: 0.0)

```

### Trigger System 

```phymodel

Behavior()
.name("Throw_sphere")
.trigger{
    Throw(){
        objects: ["sphere"],
        through: "torus"
    }
}
.actions{
    Speak(1){
        object: "sphere",
        volume: 0.5,
        text: "球体穿过了圆形平面，即：篮球穿过了篮筐。"
    }
}

```
