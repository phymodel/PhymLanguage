# Speak

> `Speak(object: String, volume: Float? = nil, text: String? = nil)`

## Purpose

用语音合成（TTS）从目标实体的位置朗读 `text`。在同一个 `Behavior` 链里，后续动作会等 TTS 说完；新的 `Speak` 会打断当前这一句。

## Parameters

| 参数 | 类型 | 必填 | 默认 | 说明 |
|---|---|---|---|---|
| object | String | ✅ | — | 目标实体名（单个实体；声音从它的位置发出） |
| volume | Float | ❌ | 系统默认 | 播放音量（0.0–1.0） |
| text | String | ❌ | — | 要朗读的文本 |

## Constraints

- 只影响 **ModelEntity** 实例。
- 在同一个 `Behavior` 链里，`Speak` 之后的动作会自动等它说完 —— 不需要用 `Wait` 去补。
- 同一条链里新的 `Speak` 会打断正在播的 TTS 并立刻开始新文本；`Wait` 只用来在两段话之间额外留白。
- 说话是有方位的：从目标实体的位置发出。

## Example

### 实体

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

### 触发系统

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
