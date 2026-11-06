# Slider

> `Slider(objects: [String], output: [String])`

## Purpose

Fires the associated `.actions` repeatedly as the user drags any entity listed in `objects`. The `output` array declares which position axes (`"x"`, `"y"`, `"z"`) are exposed as dynamic bindings, allowing downstream `EntityMesh` actions to reference the dragged entity's position in real time.

## Parameters

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| objects | [String] | ✅ | — | Target entity name array; dragging any one of them fires the trigger |
| output | [String] | ✅ | — | Axis bindings exposed to actions, e.g. `["x", "y", "z"]` |

## Constraints

- Only **ModelEntity** instances support dragging.
- Dragging is declared **by this trigger**: the entity must be named in `Slider(){ objects: […] }`. There is no entity-level interaction switch any more — the `.gesture(...)` modifier has been **removed** (writing it is an error), and an entity no `Slider` names cannot be dragged at all (pure decoration, so nothing gets dragged by accident).
- The drag clamps live in the same `Slider` block: `dragAxes: ["y"]` restricts dragging to the listed axes (omit it for free 3D drag); `dragRangeX` / `dragRangeY` / `dragRangeZ: [min, max]` clamp the dragged position along each axis (DSL local coordinates, same space as `.position`); `dragRangeR: [min, max]` clamps the radial distance from the drag start point.
- On iOS: **press and hold to grab, release to drop** — while your finger is down the entity follows the device (camera translation is converted to the entity's parent local space before clamping), so there is no second long-press to end the drag. A quick tap is **not** a grab: it only feeds `Tap` triggers, never a drag. On the web build: press and drag with the mouse (or finger) while the pointer is captured — the pointer moves the entity on a camera-facing plane and the clamps below are applied on every frame of the drag.
- The most common pairing is `Slider` → `EntityMesh`, where bindings like `phase: "sphere.x * pi"` reference the slider entity's position via `entityName.x` / `.y` / `.z`.
- `output` axes will be exposed via `实体名.x` / `.y` / `.z` syntax; only declared axes are available.

## Example

### Entities

```phymodel

CAD()
.name("sphere_s")
.mesh(commands: [
    "DEF sphere = SOLID_FORMULA 0,0,0 (x/0.1)^2+(y/0.1)^2+(z/0.1)^2-1=0",
])
.physic(mass: 0.6, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .kinematic)
.material(red: 0.67, green: 0.32, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 0.5, y: 1.5, z: 0.0)

Graph()
.name("Sine")
.mesh(x: "10t", y: "10*(4/pi)*(sin(t)+sin(3*t)/3+sin(5*t)/5)", z: "0", t: "[0,2*pi]")
.material(red: 0.46, green: 0.2, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 0.0, y: 1.5, z: 0.0)

```

### Trigger System — Slider driving EntityMesh

```phymodel

Behavior()
.name("slider_sphere")
.trigger{
    Slider(){
        objects: ["sphere_s"],
        output: ["x", "y", "z"]
    }
}
.actions{
    EntityMesh(1){
        objects: "Sine",
        x: "10t",
        y: "10*(4/pi)*(sin(t+phase)+sin(3*(t+phase))/3+sin(5*(t+phase))/5)",
        z: "0",
        t: "[0,2*pi]",
        phase: "sphere_s.x * pi"
    }
}

```
