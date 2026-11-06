# Show

> `Show(objects: [String], motionType: ShowMotionType = .pop, duration: Float = 1.0)`

## Purpose

Shows previously hidden entities with an optional entrance animation. Restores visibility and interactivity (hit-testing) for the target entities.

## Parameters

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| objects | [String] | ✅ | — | Target entity name array |
| motionType | enum | ❌ | .pop | `.none` `.moveToLeft` `.moveToRight` `.moveToFront` `.moveToRear` `.moveToAbove` `.moveToBelow` `.pop` `.scale` `.scaleBig` |
| duration | Float | ❌ | 1.0 | Animation duration (seconds) |

## Constraints

- Only affects **ModelEntity** instances (both CAD- and Text-generated entities are supported).
- If the entity is already visible, the entrance animation still plays.
- Entities created with `.isEnabled(false)` start hidden and must be shown via `Show`.

## Example

### Entities

```phymodel

CAD()
.name("cube1")
.mesh(commands: [
    "DEF box1 = PATH -0.05,-0.1,-0.1 Y 0.05,-0.1 -0.05,-0.1 -0.05,0.1 0.05,0.1 EXT 0.2 FILLET 0.005",
])
.physic(mass: 0.3, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .kinematic)
.material(red: 0.27, green: 0.39, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 0.0, y: 1.0, z: 0.0)

CAD()
.name("cube2")
.mesh(commands: [
    "DEF box1 = PATH -0.05,-0.1,-0.1 Y 0.05,-0.1 -0.05,-0.1 -0.05,0.1 0.05,0.1 EXT 0.2 FILLET 0.005",
])
.physic(mass: 0.3, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .kinematic)
.material(red: 0.27, green: 0.39, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 0.5, y: 1.0, z: 0.0)
.isEnabled(false)

```

### Trigger System

```phymodel

Behavior()
.name("tapCube1")
.trigger{
    Tap(){
        objects: ["cube1"]
    }
}
.actions{
    Hide(1){
        objects: ["cube1"],
        motionType: .scale,
        duration: 2.0
    }
    Wait(2){
        duration: 3.0
    }
    Show(3){
        objects: ["cube2"],
        motionType: .pop,
        duration: 2.5
    }
}

```
