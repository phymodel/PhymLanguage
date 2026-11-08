# Spin

> `Spin(objects: [String], iterations: Float = 1.0, clockwise: Bool = false, axis: AxisType = .yaw, duration: Float = 0)`

## Purpose

让目标实体在 `duration` 内绕指定的局部轴转给定圈数。

## Parameters

| 参数 | 类型 | 必填 | 默认 | 说明 |
|---|---|---|---|---|
| objects | [String] | ✅ | — | 目标实体名数组 |
| iterations | Float | ❌ | 1.0 | `duration` 内转满 360° 的圈数；支持小数 |
| clockwise | Bool | ❌ | false | 为 true 时顺时针转，否则逆时针 |
| axis | enum | ❌ | .yaw | 旋转轴：`.pitch`（X）`.yaw`（Y）`.roll`（Z） |
| duration | Float | ❌ | 0 | 动画总时长（秒）；0 = 瞬时 |

## Constraints

- 只影响 **ModelEntity** 实例。
- 动画期间目标实体临时切成 `.kinematic`，结束后恢复 `.dynamic`（与 `MoveAlong` / `Orbit` 一致）。
- 旋转轴在实体的**局部**坐标系里。

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
    Spin(1){
        objects: ["plane1"],
        iterations: 2.0,
        clockwise: true,
        axis: .yaw,
        duration: 3
    }
}

```
