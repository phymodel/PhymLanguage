# Drag

> `Drag(objects: [String], target: [String])`

## Purpose

用手抓起 `objects` 中的任一实体，带着它走，走到 `target` 中任一实体处时**触发一次**这里挂载的 `.actions`。这是「把它送到该去的地方」这一类触发器。

`Drag` 与 `Slider` 共用同一套抓取 / 夹紧声明（`Drag = Slider − output + target`）：两者都用 `objects` 点名实体，都接受 `dragAxes` / `dragRange*`。唯一的区别是「什么算完成」—— `Slider` 把拖动位置流给动作，`Drag` 报告的是「到位」。

## Parameters

| 参数 | 类型 | 必填 | 默认 | 说明 |
|---|---|---|---|---|
| objects | [String] | ✅ | — | 可被抓取并携带的实体名 |
| target | [String] | ❌ | — | 到达目标：被携带的实体进入其中任意一个的公差范围时触发一次 |
| dragAxes | [String] | ❌ | 三个轴全开 | 限制只能沿列出的轴拖动（`["y"]`、`["x","z"]` …） |
| dragRangeX / dragRangeY / dragRangeZ | [Float, Float] | ❌ | 不限制 | 逐轴夹紧拖动位置（DSL 局部坐标，与 `.position` 同一个空间） |
| dragRangeR | [Float, Float] | ❌ | 不限制 | 以拖动起点为圆心，夹紧径向距离 |

## Constraints

- 抓取**由这个触发器声明**：实体必须被写进 `Drag(){ objects: […] }`。没有实体级的交互开关 —— `.gesture(...)` 已删除（写了会报错），没有被任何「可抓取」触发器点名的实体根本拖不动。
- **松手即停。** `Drag` 不保留松手速度 —— 松手就让它在原地落下。只有 `Throw` 会保留（契约 D2，见 `Docs/TriggerContract.md`）。
- **到位是边沿触发**：实体进入公差范围时触发一次，离开之后重新武装，所以可以反复把同一个物体搬回来再报一次。
- 到位公差目前固定为到目标原点的 **0.15 m**（还不能配置；`tolerance:` 参数是待办项，见 `Docs/TriggerContract.md` §3）。
- 不写 `target` 是合法的，但这时 `Drag` 就退化成「不带位置输出的 `Slider`」：实体能拖，什么也不报。
- 同一个实体可以被多个「可抓取」触发器点名（`Slider` / `Drag` / `Throw`）；这时夹紧字段会逐字段合并，**值冲突是解析错误**，不会静默地「后者覆盖前者」。
- 平台差异：visionOS 上捏合并移动手即拖动；iOS 上**按住抓取、松手放开**（手指按下期间实体跟着设备走 —— 轻点不算抓取，轻点只喂给 `Tap`，所以轻触永远不会报「到位」）；Web 端按住（鼠标 / 手指）拖动，指针期间被捕获 —— 被带的实体在朝向相机的平面上跟着指针走，所以小物体也能一路拖到比它自身轮廓更远的目标上。

## Example

### 实体

```phymodel

CAD()
.name("Box")
.mesh(commands: [
    "DEF box = PATH 0,0,0 Y 0.25,0.25 -0.25,0.25 -0.25,-0.25 0.25,-0.25 EXT 0.2 FILLET 0.02",
])
.material(red: 0.2, green: 0.6, blue: 0.8, opacity: 1, roughness: 0.3, metallic: 0.5)
.physic(mass: 0.5, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .kinematic)
.position(x: 0.0, y: 1.1, z: 0.0)

CAD()
.name("targetBox")
.mesh(commands: [
    "DEF box = PATH 0,0,0 Y 0.25,0.25 -0.25,0.25 -0.25,-0.25 0.25,-0.25 EXT 0.2 FILLET 0.02",
])
.material(red: 0.2, green: 0.6, blue: 0.8, opacity: 0.5, roughness: 0.3, metallic: 0.5)
.physic(mass: 0.5, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .static)
.position(x: 0.8, y: 1.1, z: 0.0)

```

### 触发系统

```phymodel

Behavior()
.name("Drag_target_Box")
.trigger{
    Drag(){
        objects: ["Box"],
        target: "targetBox"
    }
}
.actions{
    Speak(1){
        object: "Box",
        volume: 0.5,
        text: "移动到了正确位置。"
    }
}

```
