# Wait

> `Wait(duration: Float = 0)`

## Purpose

Pauses the `Behavior` action chain for the specified duration before continuing to the next action.

## Parameters

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| duration | Float | ❌ | 0 | Wait duration (seconds) |

## Constraints

- `Wait` does not affect any entity — it only introduces a delay in the action sequence.
- `duration: 0` effectively skips the action (no-op).
- Using `Wait` between `Speak` actions is unnecessary (TTS auto-waits); use `Wait` only for extra silence padding.
- `Wait` runs concurrently with any ongoing animation from the previous action; it does not interrupt or pause animations.

## Example

### Entities

```phymodel

CAD()
.name("cube1")
.mesh(commands: [
    "DEF box1 = PATH -0.05,-0.1,-0.1 Y -0.05,-0.1 0.05,-0.1 0.05,0.1 -0.05,0.1 EXT 0.2 FILLET 0.005",
])
.physic(mass: 0.3, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .kinematic)
.material(red: 0.27, green: 0.39, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 0.0, y: 1.0, z: 0.0)

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
    Transform(1){
        objects: ["cube1"],
        scale: [1.0, 1.0, 1.0],
        rotation(angle: -45, axis: [1,0,0]),
        translation: [1.0, 1.5, -1.5],
        duration: 2.0
    }
    Wait(2){
        duration: 3.0
    }
    Transform(3){
        objects: ["cube1"],
        scale: [1.0, 1.0, 1.0],
        rotation(angle: 0, axis: [1,0,0]),
        translation: [0.0, 1.2, -1.5],
        duration: 2.0
    }
}

```
