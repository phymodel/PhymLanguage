# AddForce

> `AddForce(objects: [String], force: [Float×3] = [0,0,0], atPosition: [Float×3] = [0,0,0], relativeTo: String = "nil")`

## Purpose

Applies a force (unit: N, along the force vector direction) to target entities, causing continuous acceleration for the specified duration.

## Parameters

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| objects | [String] | ✅ | — | Target entity name array |
| force | [Float×3] | ❌ | [0,0,0] | Force vector [x, y, z] in N |
| atPosition | [Float×3] | ❌ | [0,0,0] | Point of application in world coordinates; off-center produces torque |
| relativeTo | String | ❌ | "nil" | Reference frame for force vector: `"nil"` = world; entity name = local frame |

## Constraints

- Only affects **ModelEntity** instances (both CAD- and Text-generated entities are supported).
- Target entities should use `.physic(mode:)` **`.dynamic`**, otherwise the force will not produce motion.
- When `relativeTo` references a missing entity, falls back to world coordinates (warning level).

## Example

### Entities

```phymodel

CAD()
.name("ellipsoid1")
.mesh(commands: [
    "DEF ellipsoid1 = SOLID_FORMULA 0,0,0 (x/0.1)^2+(y/0.1)^2+(z/0.1)^2-1=0",
])
.physic(mass: 1.6, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .dynamic)
.material(red: 0.67, green: 0.32, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 0.0, y: 1.5, z: 0.0)

```

### Trigger System

```phymodel

Behavior()
.name("tapEllipsoid1")
.trigger{
    Tap(){
        objects: ["ellipsoid1"]
    }
}
.actions{
    AddForce(1){
        objects: ["ellipsoid1"],
        force: [0.0, 500.0, 0.0],
        atPosition: [0.0, 0.0, 0.0],
        relativeTo: "nil"
    }
}

```
