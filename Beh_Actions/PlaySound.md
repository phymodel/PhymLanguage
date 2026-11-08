# PlaySound

> `PlaySound(objects: [String], volume: Float? = nil, url: String? = nil, duration: Float = 0)`

## Purpose

从远端 URL 播放一段空间音频，挂在指定实体上。声音是有方位的 —— 从实体在 3D 场景里的位置发出。

## Parameters

| 参数 | 类型 | 必填 | 默认 | 说明 |
|---|---|---|---|---|
| objects | [String] | ✅ | — | 目标实体名数组（声源） |
| volume | Float | ❌ | 系统默认 | 播放音量（0.0–1.0） |
| url | String | ❌ | — | 远端音频 URL（mp3、wav 等） |
| duration | Float | ❌ | 0 | 播放时长（秒）；0 = 一直播到结束 |

## Constraints

- 只影响 **ModelEntity** 实例。
- `url` 必须是可访问的远端 HTTP(S) 地址；不支持本地文件路径。
- `PlaySound` 与 `PlayMusic` 可以同时播放（两者用各自的音频通道）。

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
    PlaySound(1){
        objects: ["bezierCurve1"],
        volume: 0.3,
        url: "https://cdn.pixabay.com/download/audio/2025/09/30/audio_a59a02b883.mp3?filename=cascade-breathe-future-garage-412839.mp3",
        duration: 20
    }
}

```
