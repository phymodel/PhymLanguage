# Proximity

> `Proximity(objects: [String], distance: Float = 1.0)`

## Purpose

Fires the associated `.actions` when the camera moves within `distance` meters of any entity listed in `objects`. Continuously re-evaluates as the camera moves — the trigger fires once per proximity entry event.

## Parameters

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| objects | [String] | ✅ | — | Target entity name array; approaching any one of them fires the trigger |
| distance | Float | ❌ | 1.0 | Proximity threshold in meters; trigger fires when camera–entity distance ≤ this value |

## Constraints

- Only **ModelEntity** instances are evaluated for proximity.
- Proximity is measured from the active camera to the entity's origin/pivot point.
- The trigger fires on **entry** — the camera crossing from outside to inside the threshold. Re-fires on re-entry after the camera moves back outside the threshold.
- Hidden entities are still evaluated for proximity (unlike `Tap`, which requires visibility).

## Example

### Entities

```phymodel

CAD()
.name("ProximityPlane")
.mesh(commands: [
    "DEF plate = PATH 0,0,0 Y 0.15,0.15 -0.15,0.15 -0.15,-0.15 0.15,-0.15 EXT 0.005 FILLET_V 0.01",
])
.physic(mass: 0.2, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .dynamic)
.material(red: 0.46, green: 0.2, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 0.0, y: 1.5, z: 0.0)

CAD()
.name("cylinder1")
.mesh(commands: [
    "DEF cyl1 = PATH_FORMULA 0.0,0.0,0.0 Y (x-0.0)^2+(y-0.0)^2=0.4^2 EXT 0.2 FILLET 0.1"
])
.physic(mass: 0.4, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .dynamic)
.material(red: 0.47, green: 0.83, blue: 0.3, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 0.0, y: 1.0, z: 0.0)

CAD()
.name("ProximityBezierCurve")
.mesh(commands: [
    "DEF concave = PATH_FORMULA_XY 0,0,0 X (6-2*sin(t))*cos(t) 2+(0.2-3*sin(t))*sin(t) 0.2 64 EXT_Bezier (2.5,1,0),(2,1,0),(1.5,0.4,0),(1,0.2,0),(0,0,0),(-1,0.2,0) SEG 48"
])
.physic(mass: 0.2, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .kinematic)
.material(red: 0.2, green: 0.8, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: -1.0, y: 0.5, z: 0.0)

```

### Multiple Proximity Triggers

```phymodel

Behavior()
.name("proximityPlane")
.trigger{
    Proximity(){
        objects: ["ProximityPlane"],
        distance: 1
    }
}
.actions{
    Speak(1){
        object: "ProximityPlane",
        volume: 0.5,
        text: "你好，这是平面。"
    }
}

Behavior()
.name("proximityBezierCurve")
.trigger{
    Proximity(){
        objects: ["ProximityBezierCurve"],
        distance: 1
    }
}
.actions{
    Speak(1){
        object: "ProximityBezierCurve",
        volume: 0.5,
        text: "你好，这是贝塞尔曲线。"
    }
}

```
