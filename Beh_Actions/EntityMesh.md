# EntityMesh

> `EntityMesh(objects: String | [String], x?: String, y?: String, z?: String, t?: String, radius?: Float, growthProgress?: String, duration: Float = 0, ...bindings)`

## Purpose

运行时更新目标实体的网格 —— 要么是 `Graph()` 参数曲线（`x`/`y`/`z`/`t`），要么是 `Tree()` 的生长进度（`growthProgress`）。当绑定或 `growthProgress` 用区间写法且 `duration > 0` 时，带插值动画。

## Parameters

| 参数 | 类型 | 必填 | 默认 | 说明 |
|---|---|---|---|---|
| objects | String 或 [String] | ✅ | — | 目标实体名（可多个） |
| x | String | ❌ | 继承 | 参数 x 表达式（Graph） |
| y | String | ❌ | 继承 | 参数 y 表达式（Graph） |
| z | String | ❌ | 继承 | 参数 z 表达式（Graph） |
| t | String | ❌ | 继承 | t 区间，例如 `"[0, 2*pi]"`（Graph） |
| radius | Float | ❌ | 继承 | 管 / 线半径 |
| growthProgress | String | ❌ | 继承 | Tree 的生长值 `"0…1"` 或区间 `"[0, 1]"` |
| duration | Float | ❌ | 0 | 大于 0、且绑定 / growthProgress 用区间写法时，在 duration（秒）内插值做动画 |
| *bindings* | String | ❌ | — | 任意额外键值对都会变成动态变量（例如 `phase: "sphere.x * pi"`） |

## Constraints

- 只影响 **ModelEntity** 实例 —— 支持 `Graph()` 与 `Tree()` 实体。
- 省略的 `x`/`y`/`z`/`t`/`radius`/`growthProgress` 从目标实体当前的网格继承。若 Graph 实体自己没有 `x`/`y`/`z`、这里也没给，这个动作就是空操作。
- 目标实体带 `TreeComponent` 时用 `growthProgress`；否则用 `x`/`y`/`z`/`t`。
- 绑定的值支持区间写法（例如 `"[2*pi, 0]"`）—— `duration > 0` 时，值在时长内从起点插值到终点。
- 绑定可以用 `EntityName.x` / `.y` / `.z` 引用别的实体的位置（常见搭配是 `Slider` 触发器）。
- 与 `MoveAlong` 不同，`EntityMesh` 改的是曲线本身，不会移动实体。

## Example

### 实体

```phymodel

Graph()
.name("Sine")
.mesh(x: "10t", y: "10sin(10t)", z: "10cos(10t)", t: "[0,2*pi]")
.physic(mass: 0.7, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .kinematic)
.material(red: 0.46, green: 0.2, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 0.0, y: 1.5, z: 0.0)

Text()
.name("text_run")
.mesh(text: "Run", extrusionDepth: 0.02, fontSize: 0.1)
.physic(mass: 0.1, staticFriction: 0.9, dynamicFriction: 0.75, restitution: 0.22, mode: .kinematic)
.material(red: 0.2, green: 0.8, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: -0.2, y: 1.7, z: 0.0)

Text()
.name("text_stop")
.mesh(text: "Stop", extrusionDepth: 0.02, fontSize: 0.1)
.physic(mass: 0.1, staticFriction: 0.9, dynamicFriction: 0.75, restitution: 0.22, mode: .kinematic)
.material(red: 0.2, green: 0.8, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 0.2, y: 1.7, z: 0.0)

CAD()
.name("sphere")
.mesh(commands: [
    "DEF sphere = SOLID_FORMULA 0,0,0 (x/0.1)^2+(y/0.1)^2+(z/0.1)^2-1=0",
])
.physic(mass: 0.6, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .kinematic)
.material(red: 0.67, green: 0.32, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 0.0, y: 1.3, z: 0.0)

```

### 触发系统 —— Tap（用区间给绑定做动画）

```phymodel

Behavior()
.name("tap_text_run")
.trigger{
    Tap(){
        objects: ["text_run"]
    }
}
.actions{
    EntityMesh(1){
        objects: "Sine",
        x: "10t",
        y: "10*(4/pi)*(sin(t+phase)+sin(3*(t+phase))/3+sin(5*(t+phase))/5)",
        z: "0",
        t: "[0,2*pi]",
        phase: "[2*pi, 0]",
        duration: 12.0
    }
    Wait(2){
        duration: 0.5
    }
    EntityMesh(3){
        objects: "Sine",
        x: "10t",
        y: "10*(4/pi)*(sin(t)+sin(3*t)/3+sin(5*t)/5)",
        z: "0",
        t: "[0,2*pi]"
    }
}

Behavior()
.name("tap_text_stop")
.trigger{
    Tap(){
        objects: ["text_stop"]
    }
}
.actions{
    EntityMesh(1){
        objects: "Sine",
        x: "10t",
        y: "10sin(10t)",
        z: "10cos(10t)",
        t: "[0,2*pi]"
    }
}

```

### 触发系统 —— Slider（绑定引用另一个实体）

```phymodel

Behavior()
.name("slider_sphere")
.trigger{
    Slider(){
        objects: ["sphere"],
        output: ["x", "y", "z"]
    }
}
.actions{
    EntityMesh(1){
        objects: "Sine",
        x: "10t",
        y: "10*(4/pi)*(sin(t+phase)+sin(3*(t+phase))/3+sin(5*(t+phase))/5)",
        z: "0",
        t: "[0,2*pi]",
        phase: "sphere.x * pi"
    }
}

```
