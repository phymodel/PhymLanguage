# Collide

> `Collide(objects: [String], collisionWith: [String])`

## Purpose

Fires the associated `.actions` when any entity in `objects` physically collides with any entity in `collisionWith`. Both sides must be `.dynamic` to participate in the physics simulation collision detection.

## Parameters

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| objects | [String] | ✅ | — | Primary entity name array (the "subject" of the collision) |
| collisionWith | [String] | ✅ | — | Target entity name array (the "object" to collide with) |

## Constraints

- Only **ModelEntity** instances participate (CAD, Text, etc. with `.physic(mode:)`).
- Both `objects` entities and `collisionWith` entities must use `.physic(mode: .dynamic)` — kinematic or static entities do not generate collision events.
- Collision matching is **bidirectional**: entityA in `objects` colliding with entityB in `collisionWith` fires the same trigger as entityB in `objects` colliding with entityA in `collisionWith`.
- Each collision pair (`entityA` ↔ `entityB`) fires the trigger exactly once per contact-began event; the actions chain runs from the start on each new collision.

## Example

### Entities

```phymodel

CAD()
.name("cube1")
.mesh(commands: [
    "DEF box1 = PATH -0.05,-0.1,-0.1 Y -0.05,-0.1 0.05,-0.1 0.05,0.1 -0.05,0.1 EXT 0.2 FILLET 0.005",
])
.physic(mass: 0.3, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .dynamic)
.material(red: 0.27, green: 0.39, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: -1.8, y: 1.0, z: 0.0)

CAD()
.name("cube2")
.mesh(commands: [
    "DEF box2 = PATH -0.4,-0.1,-0.25 Y -0.4,-0.25 0.4,-0.25 0.4,0.25 -0.4,0.25 EXT 0.2 FILLET 0.06",
])
.physic(mass: 0.3, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.3, mode: .dynamic)
.material(red: 0.5, green: 0.5, blue: 0.5, opacity: 0.6, roughness: 0.3, metallic: 0.9)
.position(x: -1.2, y: 1.5, z: 0.0)

CAD()
.name("ellipsoid1")
.mesh(commands: [
    "DEF ellipsoid1 = SOLID_FORMULA 0,0,0 (x/0.1)^2+(y/0.1)^2+(z/0.1)^2-1=0",
])
.physic(mass: 0.6, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .dynamic)
.material(red: 0.67, green: 0.32, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 1.0, y: 1.5, z: 0.0)

```

### Trigger System

```phymodel

Behavior()
.name("collideEllipsoidCubes")
.trigger{
    Collide(){
        objects: ["ellipsoid1"],
        collisionWith: ["cube1", "cube2"]
    }
}
.actions{
    Hide(1){
        objects: ["cube1", "cube2", "ellipsoid1"],
        motionType: .scale,
        duration: 2.0
    }
    Wait(2){
        duration: 3.0
    }
    Show(3){
        objects: ["cube1", "cube2"],
        motionType: .pop,
        duration: 2.5
    }
}

```
