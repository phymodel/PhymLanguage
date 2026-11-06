# Tap

> `Tap(objects: [String])`

## Purpose

Fires the associated `.actions` when the user taps on any entity listed in `objects`. This is the primary interaction trigger for touch-based 3D content.

## Parameters

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| objects | [String] | ✅ | — | Target entity name array; tapping any one of them fires the trigger |

## Constraints

- Only **ModelEntity** instances are hittable (both CAD- and Text-generated entities are supported).
- Tapping is declared **by triggers**: the entity must be named in `Tap(){ objects: […] }` — that is the only place interaction is declared, since the entity-level `.gesture(...)` modifier has been **removed** (writing it is an error). An entity no `Tap` behavior names is pure decoration: it receives no taps, so a stray tap can never fire the wrong behavior.
- Hidden entities (via `Hide`) are removed from hit-testing and cannot receive taps until `Show` is called.
- A **tap is not a grab** on any platform: on iOS, a light tap (shorter than 0.25 s and moving the entity less than 1 cm) only fires `Tap` triggers and never counts as releasing a `Slider` / `Drag` / `Throw` grab — so an entity named by both `Tap` and `Throw` will not report a "throw" when you merely tap it. Press and hold that same entity and the `Throw` path takes over instead.
- A single `Behavior` can contain only one `Tap` trigger block — multiple taps on the same entity require separate `Behavior` definitions.
- Each tap fires the full `.actions` chain from the start, even if a previous invocation is still running.

## Example

### Entities

```phymodel

CAD()
.name("TapPlane")
.mesh(commands: [
    "DEF plate = PATH 0,0,0 Y 0.15,0.15 -0.15,0.15 -0.15,-0.15 0.15,-0.15 EXT 0.005 FILLET_V 0.01",
])
.physic(mass: 0.2, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .dynamic)
.material(red: 0.46, green: 0.2, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 0.0, y: 1.5, z: 0.0)

CAD()
.name("cylinder1")
.mesh(commands: [
    "DEF cyl1 = PATH_FORMULA 0.0,0.0,0.0 Y (x-0.0)^2+(y-0.0)^2=0.4^2 EXT 0.2 FILLET 0.1"
])
.physic(mass: 0.4, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .dynamic)
.material(red: 0.47, green: 0.83, blue: 0.3, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 0.0, y: 1.0, z: 0.0)

CAD()
.name("TapBezierCurve")
.mesh(commands: [
    "DEF concave = PATH_FORMULA_XY 0,0,0 X (6-2*sin(t))*cos(t) 2+(0.2-3*sin(t))*sin(t) 0.2 64 EXT_Bezier (2.5,1,0),(2,1,0),(1.5,0.4,0),(1,0.2,0),(0,0,0),(-1,0.2,0) SEG 48"
])
.physic(mass: 0.2, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .kinematic)
.material(red: 0.2, green: 0.8, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: -1.0, y: 0.5, z: 0.0)

```

### Multiple Tap Triggers

```phymodel

Behavior()
.name("tapPlane")
.trigger{
    Tap(){
        objects: ["TapPlane"]
    }
}
.actions{
    Speak(1){
        object: "TapPlane",
        volume: 0.5,
        text: "你好，这是平面。"
    }
}

Behavior()
.name("tapBezierCurve")
.trigger{
    Tap(){
        objects: ["TapBezierCurve"]
    }
}
.actions{
    Speak(1){
        object: "TapBezierCurve",
        volume: 0.5,
        text: "你好，这是贝塞尔曲线。"
    }
}

```
