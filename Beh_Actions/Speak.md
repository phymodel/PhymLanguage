# Speak

> `Speak(object: String, volume: Float? = nil, text: String? = nil)`

## Purpose

Uses text-to-speech (TTS) to read `text` aloud from the position of the target entity. Within the same `Behavior` chain, subsequent actions wait until TTS finishes; a new `Speak` interrupts the current speech.

## Parameters

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| object | String | ✅ | — | Target entity name (single entity; audio emanates from its position) |
| volume | Float | ❌ | system default | Playback volume (0.0–1.0) |
| text | String | ❌ | — | Text to be spoken via TTS |

## Constraints

- Only affects **ModelEntity** instances.
- Within the same `Behavior` chain, actions after `Speak` automatically wait for the speech to finish — no need to pad with `Wait`.
- A new `Speak` in the same chain interrupts any currently playing TTS and starts the new text immediately; use `Wait` only for extra silence between speeches.
- Speech is positional: it emanates from the target entity's location.

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
    Speak(1){
        object: "bezierCurve1",
        volume: 0.5,
        text: "你好，这是贝塞尔曲线。可用于平抛运动、曲线运动的演示。"
    }
}

```
