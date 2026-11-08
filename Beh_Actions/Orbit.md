# Orbit

> `Orbit(objects: [String], center: String, angle: Float = 0, alignPath: Bool = false, clockwise: Bool = false, revolutions: Float = 1.0, duration: Float = 0)`

## Purpose

让目标实体在给定 `duration` 内绕 `center` 实体做圆周运动。

## Parameters

| 参数 | 类型 | 必填 | 默认 | 说明 |
|---|---|---|---|---|
| objects | [String] | ✅ | — | 目标实体名数组 |
| center | String | ✅ | — | 绕哪个实体转 |
| angle | Float | ❌ | 0 | 初始切线角（度，0–360），决定起始方向 |
| alignPath | Bool | ❌ | false | 为 true 时实体朝向轨道的切线方向 |
| clockwise | Bool | ❌ | false | 为 true 时顺时针转，否则逆时针 |
| revolutions | Float | ❌ | 1.0 | `duration` 内转的整圈数；支持小数 |
| duration | Float | ❌ | 0 | 动画总时长（秒）；0 = 瞬时 |

## Constraints

- 只影响 **ModelEntity** 实例。
- 动画期间目标实体临时切成 `.kinematic`，结束后恢复 `.dynamic`（与 `MoveAlong` / `Spin` 一致）。
- `center` 实体必须存在于场景里，否则这个动作会被跳过并给出警告。
- 会动的实体可以用 `.trail(...)` 拖出一条粒子或线条轨迹；`Orbit` 期间轨迹自动启用，动作结束就不再延伸（已有轨迹按 `lifeSpan` 淡出）。
- `.trail(...)` 参数：`style`（`.particles` / `.line`）、`lifeSpan`（秒）、`size`（粒子大小或线半径）、`color`（RGB 数组）、`opacity`。

## Example

### 实体

```phymodel

CAD()
.name("cylinder1")
.mesh(commands: [
    "DEF cyl1 = PATH_FORMULA 0.0,0.0,0.0 Y (x-0.0)^2+(y-0.0)^2=0.4^2 EXT 0.2 FILLET 0.1"
])
.physic(mass: 0.4, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .kinematic)
.material(red: 0.47, green: 0.83, blue: 0.3, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 0.0, y: 0.3, z: 0.0)

CAD()
.name("plane1")
.mesh(commands: [
    "DEF plate = PATH 0,0,0 Y 0.25,0.15 -0.25,0.15 -0.25,-0.15 0.25,-0.15 EXT 0.005 FILLET_V 0.01",
])
.physic(mass: 0.2, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .dynamic)
.material(red: 0.46, green: 0.2, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 1.0, y: 0.2, z: 0.0)

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
    Orbit(1){
        objects: ["plane1"],
        center: "cylinder1",
        angle: 0,
        alignPath: true,
        clockwise: true,
        revolutions: 3,
        duration: 15
    }
}

```
