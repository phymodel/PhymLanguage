# MoveAlong

> `MoveAlong(objects: [String], path: String, tStart: Float? = nil, tEnd: Float? = nil, alignPath: Bool = false, clockwise: Bool = false, iterations: Float = 1.0, duration: Float = 0)`

## Purpose

让目标实体在指定的 `duration` 内沿一条命名的 `Graph()` 参数曲线移动。`path` 引用某个 `Graph()` 实体的名字；它的参数表达式（`x:`/`y:`/`z:`，时间变量 `t`）被复用为运动轨迹。

## Parameters

| 参数 | 类型 | 必填 | 默认 | 说明 |
|---|---|---|---|---|
| objects | [String] | ✅ | — | 目标实体名数组 |
| path | String | ✅ | — | 作为轨迹的 `Graph()` 实体名 |
| tStart | Float | ❌ | Graph 的 t 起点 | 参数区间起点；支持 `2*pi`、`pi/2` 这类表达式 |
| tEnd | Float | ❌ | Graph 的 t 终点（或 8） | 参数区间终点 |
| alignPath | Bool | ❌ | false | 为 true 时实体朝向路径的切线方向 |
| clockwise | Bool | ❌ | false | 为 true 时从 `tEnd` 走到 `tStart`（反向） |
| iterations | Float | ❌ | 1.0 | `duration` 内完整走完 `[tStart, tEnd]` 的遍数；支持小数 |
| duration | Float | ❌ | 0 | 动画总时长（秒）；0 = 瞬时 |

## Constraints

- 只影响 **ModelEntity** 实例。
- `tStart` / `tEnd` 遵循与 `Graph().mesh(..., t: "[a,b]")` 相同的表达式规则。省略时先回退到 Graph 声明的 `t` 区间，再回退到全局默认 `[0, 8]`。
- 动画期间目标实体临时切成 `.kinematic`，结束后恢复 `.dynamic`（与 `Orbit` / `Spin` 一致）。
- 被引用的 `Graph()` 实体只是轨迹模板 —— **不要**给它写 `.physic(...)`。
- 会动的实体可以用 `.trail(...)` 拖出粒子或线条轨迹；`MoveAlong` 期间轨迹自动启用，动作结束就不再延伸（已有轨迹按 `lifeSpan` 淡出）。
- `.trail(...)` 参数：`style`（`.particles` / `.line`）、`lifeSpan`（秒）、`size`（粒子大小或线半径）、`color`（RGB 数组）、`opacity`。

## Example

### 实体

```phymodel

Graph()
.name("ProjectileCurve")
.mesh(x: "5.5t", y: "(-0.0)t+(-0.8)t^2", z: "0.0", t: "[0,8]")
.material(red: 0.46, green: 0.2, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 0.0, y: 1.5, z: 0.0)

CAD()
.name("sphere")
.mesh(commands: [
    "DEF sphere = SOLID_FORMULA 0,0,0 (x/0.02)^2+(y/0.02)^2+(z/0.02)^2-1=0",
])
.physic(mass: 0.6, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .kinematic)
.material(red: 0.67, green: 0.32, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 0.0, y: 1.5, z: 0.0)
.trail(style: .particles, lifeSpan: 3.5, size: 0.02, color: [1.0, 0.4, 0.2], opacity: 0.8)

```

### 触发系统

```phymodel

Behavior()
.name("tapSphere")
.trigger{
    Tap(){
        objects: ["sphere"] 
    }
}
.actions{
    MoveAlong(1){
        objects: ["sphere"],
        path: "ProjectileCurve",
        tStart: 0.0,
        tEnd: 8.0,
        alignPath: true,
        clockwise: false,
        iterations: 1,
        duration: 3.0
    }
}

```
