# Slider

> `Slider(objects: [String], output: [String])`

## Purpose

用户拖动 `objects` 中任一实体时，**反复**触发这里挂载的 `.actions`。`output` 数组声明哪些位置轴（`"x"`、`"y"`、`"z"`）作为动态绑定暴露出去，让下游的 `EntityMesh` 动作能实时引用被拖动实体的位置。

## Parameters

| 参数 | 类型 | 必填 | 默认 | 说明 |
|---|---|---|---|---|
| objects | [String] | ✅ | — | 目标实体名数组；拖动其中任意一个即触发 |
| output | [String] | ✅ | — | 暴露给动作的轴绑定，例如 `["x", "y", "z"]` |

## Constraints

- 只有 **ModelEntity** 实例支持拖动。
- 拖动**由这个触发器声明**：实体必须被写进 `Slider(){ objects: […] }`。已经没有实体级的交互开关了 —— `.gesture(...)` 修饰符已**删除**（写了会报错），没有被任何 `Slider` 点名的实体根本拖不动（纯装饰，所以不会误拖）。
- 拖动夹紧也写在同一个 `Slider` 块里：`dragAxes: ["y"]` 限制只能沿列出的轴拖动（省略即自由 3D 拖动）；`dragRangeX` / `dragRangeY` / `dragRangeZ: [min, max]` 逐轴夹紧拖动位置（DSL 局部坐标，与 `.position` 同一个空间）；`dragRangeR: [min, max]` 以拖动起点为圆心夹紧径向距离。
- iOS 上：**按住抓取、松手放下** —— 手指按下期间实体跟着设备走（相机平移会先换算到实体的父级局部空间再夹紧），所以没有「第二次长按结束拖动」这回事。轻点**不是**抓取：它只喂给 `Tap`，永远不会成为拖动。Web 端：按住鼠标（或手指）拖动，指针被捕获 —— 指针在朝向相机的平面上移动实体，下面的夹紧在拖动的每一帧都生效。
- 最常见的搭配是 `Slider` → `EntityMesh`，其中 `phase: "sphere.x * pi"` 这类绑定通过 `entityName.x` / `.y` / `.z` 引用滑杆实体的位置。
- `output` 里的轴会以 `实体名.x` / `.y` / `.z` 的形式暴露；只有声明过的轴可用。

## Example

### 实体

```phymodel

CAD()
.name("sphere_s")
.mesh(commands: [
    "DEF sphere = SOLID_FORMULA 0,0,0 (x/0.1)^2+(y/0.1)^2+(z/0.1)^2-1=0",
])
.physic(mass: 0.6, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .kinematic)
.material(red: 0.67, green: 0.32, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 0.5, y: 1.5, z: 0.0)

Graph()
.name("Sine")
.mesh(x: "10t", y: "10*(4/pi)*(sin(t)+sin(3*t)/3+sin(5*t)/5)", z: "0", t: "[0,2*pi]")
.material(red: 0.46, green: 0.2, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 0.0, y: 1.5, z: 0.0)

```

### 触发系统 —— Slider 驱动 EntityMesh

```phymodel

Behavior()
.name("slider_sphere")
.trigger{
    Slider(){
        objects: ["sphere_s"],
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
        phase: "sphere_s.x * pi"
    }
}

```
