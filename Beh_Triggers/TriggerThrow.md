# Throw

> `Throw(objects: [String], through: [String])`

## Purpose

抓起 `objects` 中任一实体、把它带出去，然后**带着速度松手** —— 这是唯一保留松手速度的触发器（真正的抛出）。可选地用 `through` 检测被抛出的实体穿过一个环 / 框（篮筐、靶环），穿过时触发 `.actions`。

两段式事件：

- `through` 为空 → `.actions` 在**松手时**执行（「抛出去了」）。
- `through` 非空 → `.actions` 在**穿过时**执行，不在松手时执行，所以没穿过去就什么也不报。

## Parameters

| 参数 | 类型 | 必填 | 默认 | 说明 |
|---|---|---|---|---|
| objects | [String] | ✅ | — | 可被抓取并抛出的实体名 |
| through | [String] | ❌ | — | 穿过的目标；被抛出的实体穿过目标的孔时触发动作 |
| dragAxes | [String] | ❌ | 三个轴全开 | 限制松手前的拖动（例如只允许往上抬） |
| dragRangeX / dragRangeY / dragRangeZ | [Float, Float] | ❌ | 不限制 | 逐轴夹紧拖动位置（DSL 局部坐标） |
| dragRangeR | [Float, Float] | ❌ | 不限制 | 以拖动起点为圆心，夹紧径向距离 |

## Constraints

- 抛出**由这个触发器声明** —— 实体必须被写进 `Throw(){ objects: […] }`（没有实体级开关；`.gesture(...)` 已删除）。
- **只有 `Throw` 保留松手速度。** `Slider` / `Drag` 都在你松手的位置把实体停住（契约 D2）。松手速度由实体的位置差分采样，逐轴夹到 ±5 m/s 并乘 1.2；角速度目前是随机值（可配置的 `speedScale` / `spin` 是待办项 —— 见 `Docs/TriggerContract.md` §3）。
- 被抛出的实体必须是 `.physic(mode: .dynamic)` —— 松手速度是以物理运动方式施加的，`.kinematic` 实体松手就停。
- `through` 目标**必须用 `.physic(mode: .static)` 或 `.physic(mode: .kinematic)`**，这样它才保有精确的三角网格碰撞体。`.dynamic` 目标会退化成凸包，**把孔封死**，实体永远穿不过去。
- 孔轴由目标的**局部包围盒**推出：最薄的那个轴就是孔轴，孔的横向范围是另外两个轴里较大的半长。所以在 XZ 平面上生成的环，孔轴是竖直的；旋转目标，孔跟着一起转。
- 命中检测是几何的：把「上一帧位置 → 当前帧位置」这条线段与孔平面求交，交点必须落在横向范围内。这在高速下也不会穿模，且不依赖碰撞事件。
- 真正的「抛出」需要至少 **0.5 m/s** 的松手速度；更慢就算「放下去」，不判穿过。
- 一次抛出对每个目标**最多结算一次**：命中即结束，或 5 s 超时结束，或实体静止后结束。
- 穿过是在飞行中判定的；用手把球「拿着穿过」环不算。
- 平台差异：visionOS 上捏合后甩手。iOS 上**按住抓取、松手抛出**：手指按下期间实体跟着设备走，松手速度按帧从它的位置差分采样，逐轴夹到 ±5 m/s 后乘 1.2 并给一个随机自旋（与 visionOS 同一组常数），所以在 iOS 上 `through` 目标**是**会被判定的（契约 D5）。轻点不是抓取 —— 它只喂给 `Tap`，所以点一下可抛物体永远不会被当成松手。Web 端**可以**抛：松手速度取自被带实体在指针移动最后约 0.15 s 的位置差分，逐轴夹到 ±5 m/s，乘 1.2 并给随机自旋（与 visionOS 同一组常数），所以那里也判 `through` —— 慢慢地、刻意地放下去仍然是「放」（< 0.5 m/s，不开局），而一次抛出对每个目标最多结算一次（5 s 超时，或实体静止）。任何平台上被抛出的实体都必须在物理层（`.physic(mode: .dynamic)`）；否则没有刚体接收速度，它只会在你松手的地方停下。

## Example

- 球：$(x/0.1)^2+(y/0.1)^2+(z/0.1)^2-1=0$
- 环面：$(x^2+z^2+y^2+0.15^2-0.05^2)^2-4*0.15^2*(x^2+z^2)=0$

### 实体

```phymodel

CAD()
.name("sphere")
.mesh(commands: [
    "DEF sphere = SOLID_FORMULA 0,0,0 (x/0.1)^2+(y/0.1)^2+(z/0.1)^2-1=0",
])
.physic(mass: 0.6, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .dynamic)
.material(red: 0.67, green: 0.32, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 0.5, y: 1.5, z: 0.0)

CAD()
.name("torus")
.mesh(commands: [
    "DEF torus = SOLID_FORMULA 0,0,0 (x^2+z^2+y^2+0.225^2-0.02^2)^2-4*0.225^2*(x^2+z^2)=0 0.25 48",
])
.physic(mass: 0.3, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .static)
.material(red: 0.8, green: 0.2, blue: 0.4, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 0.0, y: 1.0, z: 0.0)

```

### 触发系统

```phymodel

Behavior()
.name("Throw_sphere")
.trigger{
    Throw(){
        objects: ["sphere"],
        through: "torus"
    }
}
.actions{
    Speak(1){
        object: "sphere",
        volume: 0.5,
        text: "球体穿过了圆形平面，即：篮球穿过了篮筐。"
    }
}

```
