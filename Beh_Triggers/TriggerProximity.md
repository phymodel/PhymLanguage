# Proximity

> `Proximity(objects: [String], distance: Float = 1.0)`

## Purpose

相机进入 `objects` 中任一实体 `distance` 米范围内时，触发这里挂载的 `.actions`。相机移动时持续重新求值 —— 每次「进入近距」只触发一次。

## Parameters

| 参数 | 类型 | 必填 | 默认 | 说明 |
|---|---|---|---|---|
| objects | [String] | ✅ | — | 目标实体名数组；靠近其中任意一个即触发 |
| distance | Float | ❌ | 1.0 | 近距阈值（米）；相机与实体的距离 ≤ 该值时触发 |

## Constraints

- 只有 **ModelEntity** 实例参与近距判定。
- 距离从当前相机量到实体的原点 / 枢轴点。
- 只在**进入**时触发 —— 相机从阈值外穿到阈值内。相机退回阈值外之后再进入会重新触发。
- 隐藏的实体依然参与近距判定（这一点与 `Tap` 不同，后者要求可见）。

## Example

### 实体

```phymodel

CAD()
.name("ProximityPlane")
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
.name("ProximityBezierCurve")
.mesh(commands: [
    "DEF concave = PATH_FORMULA_XY 0,0,0 X (6-2*sin(t))*cos(t) 2+(0.2-3*sin(t))*sin(t) 0.2 64 EXT_Bezier (2.5,1,0),(2,1,0),(1.5,0.4,0),(1,0.2,0),(0,0,0),(-1,0.2,0) SEG 48"
])
.physic(mass: 0.2, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .kinematic)
.material(red: 0.2, green: 0.8, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: -1.0, y: 0.5, z: 0.0)

```

### 多个 Proximity 触发器

```phymodel

Behavior()
.name("proximityPlane")
.trigger{
    Proximity(){
        objects: ["ProximityPlane"],
        distance: 1
    }
}
.actions{
    Speak(1){
        object: "ProximityPlane",
        volume: 0.5,
        text: "你好，这是平面。"
    }
}

Behavior()
.name("proximityBezierCurve")
.trigger{
    Proximity(){
        objects: ["ProximityBezierCurve"],
        distance: 1
    }
}
.actions{
    Speak(1){
        object: "ProximityBezierCurve",
        volume: 0.5,
        text: "你好，这是贝塞尔曲线。"
    }
}

```
