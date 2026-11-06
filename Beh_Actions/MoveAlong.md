# MoveAlong

> `MoveAlong(objects: [String], path: String, tStart: Float? = nil, tEnd: Float? = nil, alignPath: Bool = false, clockwise: Bool = false, iterations: Float = 1.0, duration: Float = 0)`

## Purpose

Moves target entities along a named `Graph()` parametric curve over the specified duration. The `path` parameter references a `Graph()` entity's name; its parametric expressions (`x:`/`y:`/`z:`, time variable `t`) are reused as the motion trajectory.

## Parameters

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| objects | [String] | ✅ | — | Target entity name array |
| path | String | ✅ | — | Name of a `Graph()` entity whose curve serves as the trajectory |
| tStart | Float | ❌ | Graph's t-start | Start of the parameter interval; supports expressions like `2*pi`, `pi/2` |
| tEnd | Float | ❌ | Graph's t-end (or 8) | End of the parameter interval |
| alignPath | Bool | ❌ | false | If true, entity faces the tangent direction of the path |
| clockwise | Bool | ❌ | false | If true, travels from `tEnd` to `tStart` (reversed) |
| iterations | Float | ❌ | 1.0 | Number of full traversals of `[tStart, tEnd]` within `duration`; supports fractional values |
| duration | Float | ❌ | 0 | Total animation duration (seconds); 0 = instantaneous |

## Constraints

- Only affects **ModelEntity** instances.
- `tStart` / `tEnd` follow the same expression rules as `Graph().mesh(..., t: "[a,b]")`. Omitted values fall back to the Graph's declared `t` range, then to the global default `[0, 8]`.
- During animation the target entity temporarily switches to `.kinematic`; it reverts to `.dynamic` afterward (same behavior as `Orbit` / `Spin`).
- The referenced `Graph()` entity is a trajectory template only — **do not** assign `.physic(...)` to it.
- Moving entities can use `.trail(...)` to leave a particle or line trail; the trail automatically activates during `MoveAlong` and stops extending when the action finishes (existing trail fades according to `lifeSpan`).
- `.trail(...)` parameters: `style` (`.particles` / `.line`), `lifeSpan` (seconds), `size` (particle size or line radius), `color` (RGB array), `opacity`.

## Example

### Entities

```phymodel

Graph()
.name("ProjectileCurve")
.mesh(x: "5.5t", y: "(-0.0)t+(-0.8)t^2", z: "0.0", t: "[0,8]")
.material(red: 0.46, green: 0.2, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 0.0, y: 1.5, z: 0.0)

CAD()
.name("sphere")
.mesh(commands: [
    "DEF sphere = SOLID_FORMULA 0,0,0 (x/0.02)^2+(y/0.02)^2+(z/0.02)^2-1=0",
])
.physic(mass: 0.6, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .kinematic)
.material(red: 0.67, green: 0.32, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 0.0, y: 1.5, z: 0.0)
.trail(style: .particles, lifeSpan: 3.5, size: 0.02, color: [1.0, 0.4, 0.2], opacity: 0.8)

```

### Trigger System

```phymodel

Behavior()
.name("tapSphere")
.trigger{
    Tap(){
        objects: ["sphere"] 
    }
}
.actions{
    MoveAlong(1){
        objects: ["sphere"],
        path: "ProjectileCurve",
        tStart: 0.0,
        tEnd: 8.0,
        alignPath: true,
        clockwise: false,
        iterations: 1,
        duration: 3.0
    }
}

```
