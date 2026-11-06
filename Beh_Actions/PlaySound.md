# PlaySound

> `PlaySound(objects: [String], volume: Float? = nil, url: String? = nil, duration: Float = 0)`

## Purpose

Plays a spatial audio clip from a remote URL, attached to the specified entities. The sound is positional — it emanates from the entity's location in the 3D scene.

## Parameters

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| objects | [String] | ✅ | — | Target entity name array (sound sources) |
| volume | Float | ❌ | system default | Playback volume (0.0–1.0) |
| url | String | ❌ | — | Remote audio URL (mp3, wav, etc.) |
| duration | Float | ❌ | 0 | Playback duration in seconds; 0 = play until end |

## Constraints

- Only affects **ModelEntity** instances.
- `url` must be a reachable remote HTTP(S) URL; local file paths are not supported.
- `PlaySound` and `PlayMusic` can play simultaneously (they use separate audio channels).

## Example

### Entities

```phymodel

CAD()
.name("bezierCurve1")
.mesh(commands: [
    "DEF concave = PATH_FORMULA_XY 0,0,0 X (6-2*sin(t))*cos(t) 2+(0.2-3*sin(t))*sin(t) 0.2 64 EXT_Bezier (2.5,1,0),(2,1,0),(1.5,0.4,0),(1,0.2,0),(0.5,0,0),(0,0,0) SEG 48"
])
.physic(mass: 0.2, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .kinematic)
.material(red: 0.2, green: 0.8, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: -1.0, y: 0.5, z: 0.0)

```

### Trigger System

```phymodel

Behavior()
.name("tapBezierCurve1")
.trigger{
    Tap(){
        objects: ["bezierCurve1"]
    }
}
.actions{
    PlaySound(1){
        objects: ["bezierCurve1"],
        volume: 0.3,
        url: "https://cdn.pixabay.com/download/audio/2025/09/30/audio_a59a02b883.mp3?filename=cascade-breathe-future-garage-412839.mp3",
        duration: 20
    }
}

```
