# Drag

> `Drag(objects: [String], target: [String])`

## Purpose

Grab any entity listed in `objects` with your hand, carry it around, and fire the associated `.actions` **once** when it reaches any entity listed in `target`. This is the "carry it to the right place" trigger.

`Drag` and `Slider` share the same grab/clamp declaration (`Drag = Slider − output + target`): both name the entity in `objects` and both accept `dragAxes` / `dragRange*`. The only difference is what counts as "done" — `Slider` streams the dragged position into actions, `Drag` reports the arrival instead.

## Parameters

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| objects | [String] | ✅ | — | Entity names that can be grabbed and carried |
| target | [String] | ❌ | — | Arrival targets: fires once when the carried entity comes within tolerance of any one of them |
| dragAxes | [String] | ❌ | all three axes | Restricts dragging to the listed axes (`["y"]`, `["x","z"]`, …) |
| dragRangeX / dragRangeY / dragRangeZ | [Float, Float] | ❌ | unlimited | Clamps the dragged position along each axis (DSL local coordinates, same space as `.position`) |
| dragRangeR | [Float, Float] | ❌ | unlimited | Clamps the radial distance from the drag start point |

## Constraints

- Grabbing is declared **by this trigger**: the entity must be named in `Drag(){ objects: […] }`. There is no entity-level interaction switch — `.gesture(...)` has been removed (writing it is an error), and an entity no grab-capable trigger names cannot be dragged at all.
- **Release stops the entity.** `Drag` does not keep the release velocity — releasing lets it drop where it is. Only `Throw` keeps it (contract D2, see `Docs/TriggerContract.md`).
- **Arrival is edge-triggered**: it fires once when the entity enters the tolerance, and re-arms after it leaves, so you can carry the same object in again for another report.
- Arrival tolerance is currently a fixed **0.15 m** to the target's origin (not configurable yet; a `tolerance:` parameter is a pending item — see `Docs/TriggerContract.md` §3).
- Omitting `target` is legal but makes `Drag` behave like a `Slider` without position output: the entity can be dragged, and nothing is reported.
- The same entity may be named by several grab-capable triggers (`Slider` / `Drag` / `Throw`); the clamp fields are then merged field by field, and **conflicting values are a parse error** rather than a silent last-one-wins.
- Platform: on visionOS, pinch and move your hand to drag; on iOS, **press and hold to grab and release to let go** (the carried entity follows the device while your finger is down — a quick tap is not a grab, it only feeds `Tap` triggers, so a light touch never reports an arrival); on the web build, press (mouse / finger) and drag while the pointer is captured — the carried entity follows the pointer on a camera-facing plane, so a small object can be carried all the way to a target that is farther away than its own silhouette.

## Example

### Entities

```phymodel

CAD()
.name("Box")
.mesh(commands: [
    "DEF box = PATH 0,0,0 Y 0.25,0.25 -0.25,0.25 -0.25,-0.25 0.25,-0.25 EXT 0.2 FILLET 0.02",
])
.material(red: 0.2, green: 0.6, blue: 0.8, opacity: 1, roughness: 0.3, metallic: 0.5)
.physic(mass: 0.5, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .kinematic)
.position(x: 0.0, y: 1.1, z: 0.0)

CAD()
.name("targetBox")
.mesh(commands: [
    "DEF box = PATH 0,0,0 Y 0.25,0.25 -0.25,0.25 -0.25,-0.25 0.25,-0.25 EXT 0.2 FILLET 0.02",
])
.material(red: 0.2, green: 0.6, blue: 0.8, opacity: 0.5, roughness: 0.3, metallic: 0.5)
.physic(mass: 0.5, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .static)
.position(x: 0.8, y: 1.1, z: 0.0)

```

### Trigger System 

```phymodel

Behavior()
.name("Drag_target_Box")
.trigger{
    Drag(){
        objects: ["Box"],
        target: "targetBox"
    }
}
.actions{
    Speak(1){
        object: "Box",
        volume: 0.5,
        text: "移动到了正确位置。"
    }
}

```
