# Spin

> `Spin(objects: [String], iterations: Float = 1.0, clockwise: Bool = false, axis: AxisType = .yaw, duration: Float = 0)`

## Purpose

Rotates target entities around a specified local axis for a given number of iterations over the duration.

## Parameters

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| objects | [String] | ✅ | — | Target entity name array |
| iterations | Float | ❌ | 1.0 | Number of full 360° rotations within `duration`; supports fractional values |
| clockwise | Bool | ❌ | false | If true, spins clockwise instead of counter-clockwise |
| axis | enum | ❌ | .yaw | Rotation axis: `.pitch` (X) `.yaw` (Y) `.roll` (Z) |
| duration | Float | ❌ | 0 | Total animation duration (seconds); 0 = instantaneous |

## Constraints

- Only affects **ModelEntity** instances.
- During animation the target entity temporarily switches to `.kinematic`; it reverts to `.dynamic` afterward (same behavior as `MoveAlong` / `Orbit`).
- The rotation axis is in the entity's **local** coordinate frame.

## Example

### Entities

```phymodel

CAD()
.name("plane1")
.mesh(commands: [
    "DEF plate = PATH 0,0,0 Y 0.15,0.15 -0.15,0.15 -0.15,-0.15 0.15,-0.15 EXT 0.005 FILLET_V 0.01",
])
.physic(mass: 0.2, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .dynamic)
.material(red: 0.46, green: 0.2, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 0.0, y: 1.5, z: 0.0)

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
    Spin(1){
        objects: ["plane1"],
        iterations: 2.0,
        clockwise: true,
        axis: .yaw,
        duration: 3
    }
}

```
