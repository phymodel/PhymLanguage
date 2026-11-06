# LookAtCamera

> `LookAtCamera(objects: [String], facingDirection: FacingDirection = .front, rotationEuler: RotationFreedom = .free, duration: Float = 0)`

## Purpose

Orients target entities so that a specified face points toward the active camera. When `duration > 0`, the rotation is animated smoothly.

## Parameters

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| objects | [String] | ✅ | — | Target entity name array |
| facingDirection | enum | ❌ | .front | Face to point at camera: `.front` `.back` `.left` `.right` `.top` `.bottom` |
| rotationEuler | enum | ❌ | .free | Constrained rotation axis: `.free` `.pitch` `.yaw` `.roll` |
| duration | Float | ❌ | 0 | Rotation animation duration (seconds); 0 = instantaneous |

## Constraints

- Only affects **ModelEntity** instances (both CAD- and Text-generated entities are supported).
- With `rotationEuler` set to `.pitch`/`.yaw`/`.roll`, the look-at rotation is projected onto that single axis; the face may not fully point at the camera.
- An entity engaged in a physics simulation (`.dynamic`) will have its orientation overridden during the animation and revert to physics afterward.

## Example

### Entities

```phymodel

CAD()
.name("cube2")
.mesh(commands: [
    "DEF box2 = PATH -0.4,-0.1,-0.25 Y -0.4,-0.25 0.4,-0.25 0.4,0.25 -0.4,0.25 EXT 0.2 FILLET 0.06",
])
.physic(mass: 0.3, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.3, mode: .dynamic)
.material(red: 0.5, green: 0.5, blue: 0.5, opacity: 0.6, roughness: 0.3, metallic: 0.9)
.position(x: 0.0, y: 1.5, z: 0.0)

```

### Trigger System

```phymodel

Behavior()
.name("tapCube2")
.trigger{
    Tap(){
        objects: ["cube2"]
    }
}
.actions{
    LookAtCamera(2){
        objects: ["cube2"],
        facingDirection: .front,
        rotationEuler: .free,
        duration: 5
    }
}

```
