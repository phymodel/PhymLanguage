# Wait

> `Wait(duration: Float = 0)`

## Purpose

让 `Behavior` 的动作链暂停指定时长，再继续下一个动作。

## Parameters

| 参数 | 类型 | 必填 | 默认 | 说明 |
|---|---|---|---|---|
| duration | Float | ❌ | 0 | 等待时长（秒） |

## Constraints

- `Wait` 不影响任何实体 —— 它只是在动作序列里插入一段延时。
- `duration: 0` 等于跳过这个动作（空操作）。
- 在两个 `Speak` 之间不需要 `Wait`（TTS 会自动等）；`Wait` 只用来额外留白。
- `Wait` 与上一个动作正在进行的动画并发运行；它不会打断或暂停动画。

## Example

### 实体

```phymodel

CAD()
.name("cube1")
.mesh(commands: [
    "DEF box1 = PATH -0.05,-0.1,-0.1 Y -0.05,-0.1 0.05,-0.1 0.05,0.1 -0.05,0.1 EXT 0.2 FILLET 0.005",
])
.physic(mass: 0.3, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .kinematic)
.material(red: 0.27, green: 0.39, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 0.0, y: 1.0, z: 0.0)

```

### 触发系统

```phymodel

Behavior()
.name("tapCube1")
.trigger{
    Tap(){
        objects: ["cube1"]
    }
}
.actions{
    Transform(1){
        objects: ["cube1"],
        scale: [1.0, 1.0, 1.0],
        rotation(angle: -45, axis: [1,0,0]),
        translation: [1.0, 1.5, -1.5],
        duration: 2.0
    }
    Wait(2){
        duration: 3.0
    }
    Transform(3){
        objects: ["cube1"],
        scale: [1.0, 1.0, 1.0],
        rotation(angle: 0, axis: [1,0,0]),
        translation: [0.0, 1.2, -1.5],
        duration: 2.0
    }
}

```
