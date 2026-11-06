# OpenScene

> `OpenScene(scene: String, duration: Float = 0)`

## Purpose

Navigates from the current scene to another `.md` scene file within the document library. The path is resolved relative to the current scene's `.md` file.

## Parameters

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| scene | String | ✅ | — | Relative path to the target `.md` scene (supports `../`, `./`, and same-directory filenames) |
| duration | Float | ❌ | 0 | Delay before navigation (seconds); 0 = immediately when the action is reached |

## Constraints

- The resolved path must be inside the document library and have a `.md` extension; otherwise the action is skipped with a warning.
- This is unrelated to `MoveAlong`'s `path` parameter (which references a `Graph` entity name).
- Does not require `objects`.
- When used in the same `Behavior` chain with `Speak`, `OpenScene` will wait for `Speak` to finish (or be interrupted by another `Speak`); add a `Wait` action for extra padding.

## Example

### Entities

```phymodel

CAD()
.name("nextButton")
.mesh(commands: [
    "DEF plate = PATH 0,0,0 Y 0.15,0.15 -0.15,0.15 -0.15,-0.15 0.15,-0.15 EXT 0.005 FILLET_V 0.01",
])
.physic(mass: 0.2, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .kinematic)
.material(red: 0.46, green: 0.2, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 0.0, y: 1.5, z: 0.0)

```

### Trigger System

```phymodel

Behavior()
.name("goNextChapter")
.trigger{
    Tap(){
        objects: ["nextButton"]
    }
}
.actions{
    Speak(1){
        object: "nextButton",
        text: "进入下一章"
    }
    OpenScene(2){
        scene: "../Beh_Actions/Orbit.md",
        duration: 0
    }
}

```
