# PlayMusic

> `PlayMusic(volume: Float? = nil, url: String? = nil, duration: Float = 0)`

## Purpose

Plays background music from a remote audio URL. Unlike `PlaySound`, this is ambient audio not tied to any specific entity.

## Parameters

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| volume | Float | ❌ | system default | Playback volume (0.0–1.0) |
| url | String | ❌ | — | Remote audio URL (mp3, wav, etc.); nil stops current music |
| duration | Float | ❌ | 0 | Playback duration in seconds; 0 = play until end or stopped |

## Constraints

- `url` must be a reachable remote HTTP(S) URL; local file paths are not supported.
- Calling `PlayMusic` with a new `url` replaces any currently playing music.
- `PlaySound` and `PlayMusic` can play simultaneously (they use separate audio channels).

## Example

### Entities

```phymodel

CAD()
.name("plane1")
.mesh(commands: [
    "DEF plate = PATH 0,0,0 Y 0.15,0.15 -0.15,0.15 -0.15,-0.15 0.15,-0.15 EXT 0.005 FILLET_V 0.01",
])
.physic(mass: 0.2, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .dynamic)
.material(red: 0.46, green: 0.2, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 0.0, y: 1.5, z: 0.0)

```

### Trigger System

```phymodel

Behavior()
.name("tapPlane1")
.trigger{
    Tap(){
        objects: ["plane1"]
    }
}
.actions{
    PlayMusic(1){
        volume: 0.5,
        url: "https://cdn.pixabay.com/download/audio/2025/07/18/audio_a9351c39ad.mp3?filename=mouse-click-sfx-free-376869.mp3",
        duration: 1.5
    }
}

```
