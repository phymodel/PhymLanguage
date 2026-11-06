# Hide

> `Hide(objects: [String], motionType: HideMotionType = .scale, duration: Float = 1.0)`

## Purpose

Hides target entities with an optional exit animation. Hidden entities are invisible and non-interactive until shown again via `Show`.

## Parameters

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| objects | [String] | ✅ | — | Target entity name array |
| motionType | enum | ❌ | .scale | `.none` `.moveToLeft` `.moveToRight` `.moveToFront` `.moveToRear` `.moveToAbove` `.moveToBelow` `.pop` `.scale` `.scaleUp` |
| duration | Float | ❌ | 1.0 | Animation duration (seconds) |

## Constraints

- Only affects **ModelEntity** instances (both CAD- and Text-generated entities are supported).
- Hidden entities are removed from hit-testing; they cannot receive `Tap`/`Slider` triggers until `Show` is called.
- An entity that is already hidden will still play the exit animation if `motionType` is not `.none`.

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
    Hide(1){
        objects: ["cube1"],
        motionType: .scale,
        duration: 2.0
    }
    Wait(2){
        duration: 3.0
    }
    Show(3){
        objects: ["cube1"],
        motionType: .pop,
        duration: 2.5
    }
}

```
