# Emphasize

> `Emphasize(objects: [String], motionType: MotionType = .pop, duration: Float = 1.0)`

## Purpose

Plays a single emphasis animation (pulse, bounce, blink, etc.) on target entities to draw the user's attention.

## Parameters

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| objects | [String] | ✅ | — | Target entity name array |
| motionType | enum | ❌ | .pop | `.pop` `.blink` `.bounce` `.flip` `.float` `.jiggle` `.pulse` `.spin` |
| duration | Float | ❌ | 1.0 | Animation duration (seconds) |

## Constraints

- Only affects **ModelEntity** instances (both Text- and CAD-generated entities are supported).

## Example

### Entities

```phymodel

Text()
.name("textHello")
.mesh(text: "Hello, World!", extrusionDepth: 0.02, fontSize: 0.1)
.physic(mass: 0.1, staticFriction: 0.9, dynamicFriction: 0.75, restitution: 0.22, mode: .kinematic)
.material(red: 0.2, green: 0.8, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 0.0, y: 1.5, z: 0.0)

```

### Trigger System

```phymodel

Behavior()
.name("tapTextHello")
.trigger{
    Tap(){
        objects: ["textHello"]
    }
}
.actions{
    Emphasize(1){
        objects: ["textHello"],
        motionType: .pulse,
        duration: 1
    }
}

```
