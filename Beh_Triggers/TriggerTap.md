# Tap

> `Tap(objects: [String])`

## Purpose

当用户点按 `objects` 中任一实体时，触发这里挂载的 `.actions`。这是触屏 3D 内容最主要的交互触发器。

## Parameters

| 参数 | 类型 | 必填 | 默认 | 说明 |
|---|---|---|---|---|
| objects | [String] | ✅ | — | 目标实体名数组；点到其中任意一个即触发 |

## Constraints

- 只有 **ModelEntity** 实例可被命中（CAD 与 Text 生成的实体都支持）。
- 点按是**由触发器声明**的：实体必须被写进 `Tap(){ objects: […] }` —— 这是声明交互的唯一位置，实体级的 `.gesture(...)` 修饰符已**删除**（写了会报错）。没有被任何 `Tap` 点名的实体就是纯装饰：它收不到点按，所以误点也永远不会触发错误的行为。
- 被 `Hide` 隐藏的实体会从命中检测里移除，在 `Show` 之前收不到点按。
- 任何平台上**点按都不等于抓取**：在 iOS 上轻点一下（短于 0.25 s、且实体位移小于 1 cm）只触发 `Tap`，绝不算松开 `Slider` / `Drag` / `Throw` 的抓取 —— 所以同时被 `Tap` 与 `Throw` 点名的实体，轻轻一点不会报「抛出」。按住同一个实体待够时间，接管的就是 `Throw` 那条路。
- 一个 `Behavior` 只能包含一个 `Tap` 触发块 —— 同一个实体上的多次点按要用多个 `Behavior` 定义。
- 每次点按都把整条 `.actions` 从头上重跑一遍，即使上一次调用还在执行。

## Example

### 实体

```phymodel

CAD()
.name("TapPlane")
.mesh(commands: [
    "DEF plate = PATH 0,0,0 Y 0.15,0.15 -0.15,0.15 -0.15,-0.15 0.15,-0.15 EXT 0.005 FILLET_V 0.01",
])
.physic(mass: 0.2, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .dynamic)
.material(red: 0.46, green: 0.2, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 0.0, y: 1.5, z: 0.0)

CAD()
.name("cylinder1")
.mesh(commands: [
    "DEF cyl1 = PATH_FORMULA 0.0,0.0,0.0 Y (x-0.0)^2+(y-0.0)^2=0.4^2 EXT 0.2 FILLET 0.1"
])
.physic(mass: 0.4, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .dynamic)
.material(red: 0.47, green: 0.83, blue: 0.3, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 0.0, y: 1.0, z: 0.0)

CAD()
.name("TapBezierCurve")
.mesh(commands: [
    "DEF concave = PATH_FORMULA_XY 0,0,0 X (6-2*sin(t))*cos(t) 2+(0.2-3*sin(t))*sin(t) 0.2 64 EXT_Bezier (2.5,1,0),(2,1,0),(1.5,0.4,0),(1,0.2,0),(0,0,0),(-1,0.2,0) SEG 48"
])
.physic(mass: 0.2, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .kinematic)
.material(red: 0.2, green: 0.8, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: -1.0, y: 0.5, z: 0.0)

```

### 多个 Tap 触发器

```phymodel

Behavior()
.name("tapPlane")
.trigger{
    Tap(){
        objects: ["TapPlane"]
    }
}
.actions{
    Speak(1){
        object: "TapPlane",
        volume: 0.5,
        text: "你好，这是平面。"
    }
}

Behavior()
.name("tapBezierCurve")
.trigger{
    Tap(){
        objects: ["TapBezierCurve"]
    }
}
.actions{
    Speak(1){
        object: "TapBezierCurve",
        volume: 0.5,
        text: "你好，这是贝塞尔曲线。"
    }
}

```
