# PlayMusic

> `PlayMusic(volume: Float? = nil, url: String? = nil, duration: Float = 0)`

## Purpose

从远端音频 URL 播放背景音乐。与 `PlaySound` 不同，这是不挂在任何实体上的环境音。

## Parameters

| 参数 | 类型 | 必填 | 默认 | 说明 |
|---|---|---|---|---|
| volume | Float | ❌ | 系统默认 | 播放音量（0.0–1.0） |
| url | String | ❌ | — | 远端音频 URL（mp3、wav 等）；nil 表示停掉当前音乐 |
| duration | Float | ❌ | 0 | 播放时长（秒）；0 = 一直播到结束或被停止 |

## Constraints

- `url` 必须是可访问的远端 HTTP(S) 地址；不支持本地文件路径。
- 用新的 `url` 调用 `PlayMusic` 会替换掉当前正在播的音乐。
- `PlaySound` 与 `PlayMusic` 可以同时播放（两者用各自的音频通道）。

## Example

### 实体

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

### 触发系统

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
