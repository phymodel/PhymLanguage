# Orbit

> `Orbit(objects: [String], center: String, angle: Float = 0, alignPath: Bool = false, clockwise: Bool = false, revolutions: Float = 1.0, duration: Float = 0)`

## Purpose

Makes target entities revolve around a specified `center` entity in a circular motion over the given duration.

## Parameters

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| objects | [String] | ✅ | — | Target entity name array |
| center | String | ✅ | — | Name of the entity to orbit around |
| angle | Float | ❌ | 0 | Initial tangent angle in degrees (0–360) controlling the starting direction |
| alignPath | Bool | ❌ | false | If true, entity faces the tangent direction of the orbit |
| clockwise | Bool | ❌ | false | If true, orbits clockwise instead of counter-clockwise |
| revolutions | Float | ❌ | 1.0 | Number of full revolutions within `duration`; supports fractional values |
| duration | Float | ❌ | 0 | Total animation duration (seconds); 0 = instantaneous |

## Constraints

- Only affects **ModelEntity** instances.
- During animation the target entity temporarily switches to `.kinematic`; it reverts to `.dynamic` afterward (same behavior as `MoveAlong` / `Spin`).
- The `center` entity must exist in the scene; otherwise the action is skipped with a warning.
- Moving entities can use `.trail(...)` to leave a particle or line trail; the trail automatically activates during `Orbit` and stops extending when the action finishes (existing trail fades according to `lifeSpan`).
- `.trail(...)` parameters: `style` (`.particles` / `.line`), `lifeSpan` (seconds), `size` (particle size or line radius), `color` (RGB array), `opacity`.

## Example

### Entities

```phymodel

CAD()
.name("cylinder1")
.mesh(commands: [
    "DEF cyl1 = PATH_FORMULA 0.0,0.0,0.0 Y (x-0.0)^2+(y-0.0)^2=0.4^2 EXT 0.2 FILLET 0.1"
])
.physic(mass: 0.4, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .kinematic)
.material(red: 0.47, green: 0.83, blue: 0.3, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 0.0, y: 0.3, z: 0.0)

CAD()
.name("plane1")
.mesh(commands: [
    "DEF plate = PATH 0,0,0 Y 0.25,0.15 -0.25,0.15 -0.25,-0.15 0.25,-0.15 EXT 0.005 FILLET_V 0.01",
])
.physic(mass: 0.2, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .dynamic)
.material(red: 0.46, green: 0.2, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 1.0, y: 0.2, z: 0.0)

```

### Trigger System

```phymodel

Behavior()
.name("tapPlane1")
.trigger{
    Tap(){
        objects: ["plane1"]
    }
}
.actions{
    Orbit(1){
        objects: ["plane1"],
        center: "cylinder1",
        angle: 0,
        alignPath: true,
        clockwise: true,
        revolutions: 3,
        duration: 15
    }
}

```
