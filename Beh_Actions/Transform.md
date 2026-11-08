# Transform

> `Transform(objects: [String], scale: [Float×3]? = nil, rotation(angle: angle:axis:)? = nil, translation: [Float×3]? = nil, easeType: EaseType = .none, duration: Float = 0)`

## Purpose

对目标实体组合施加缩放、旋转与（或）平移，可选缓动，并在 `duration` 内做成动画。

## Parameters

| 参数 | 类型 | 必填 | 默认 | 说明 |
|---|---|---|---|---|
| objects | [String] | ✅ | — | 目标实体名。接受范围写法 `"Prefix[0..4]"`（展开成每个实例一个动作）与旧的单目标写法 `object: "Name"` |
| scale | [Float×3] | ❌ | nil | 目标缩放 `[sx, sy, sz]`；省略时目标缩放为 **1**（见「语义」） |
| rotation(angle:axis:) | (Float, [Float×3]) | ❌ | nil | 绕 `axis` `[x, y, z]` 转 `angle` 度；省略时目标旋转为**单位旋转** |
| translation | [Float×3] | ❌ | nil | 目标位置 `[x, y, z]`（世界单位）—— **绝对目标，不是偏移**；省略时为 **(0, 0, 0)** |
| easeType | enum | ❌ | .easeOut | `.none` `.easeOut` `.easeIn` `.easeInOut`。目前只解析、运行时**尚未消费**（计时函数固定为 `.easeInOut`） |
| duration | Float | ❌ | 1.0 | 动画时长（秒）；0 = 立即生效、不做动画 |

## 目标范围与逐实例 `index`（新）

`objects` 接受范围写法，一个块就能驱动一族实例：

```phymodel
Transform(1){
    objects: ["PulseSphere[0..4]"],
    translation: [-0.5 + index * 0.1/pi, 1.5, 0.0],
    duration: 0
}
```

- `"PulseSphere[0..4]"` 展开成 `PulseSphere0 … PulseSphere4`；展开出来的每个动作都保留块 id，所以这些实例**并行**执行，跟一块块手写出来完全一样。
- `index`（别名 `i`）是该范围内的实例下标，可用在 `scale:`、`translation:` 与 `rotation(angle:axis:)` 里。
- 每个分量都是完整的数学表达式（`pi`、`2*pi`、`+ - * /`、三目、`%`），由与 `Graph().mesh(...)`、`MoveAlong` 的 `tStart` / `tEnd` 同一个求值引擎计算。
- 普通名字（没有 `[a..b]`）也可以用表达式；它的 `index` 是 0。
- 范围写法不合法（`"Node[0-2]"`）或表达式求不出值，会报解析错误并丢掉这个动作 —— 绝不会静默退化成 `(0, 0, 0)`。
- `objects` / `object` 可以写多个名字（`objects: ["a", "b"]`）；每个各自成为一个动作。

## `translation` / `duration` 的语义

- `duration == 0`：实体的变换被**整体覆盖** —— `translation` 是绝对位姿，你没给的字段全部复位（缩放 → 1、旋转 → 单位旋转、平移 → `(0, 0, 0)`）。
- `duration > 0`：从动作开始那一刻的位姿动画到这个绝对目标；没给的字段同样解析成上面的默认值。
- 由此带来的后果：`translation` 是**目标位置**，不是增量。所以「复位到初始位姿」的块必须把声明的 `.position(...)` 数值再写一遍（或写成它们的对称表达式，例如 `-0.5 + index * 0.1/pi`）。

## Constraints

- 只影响 **ModelEntity** 实例（各种实体类型都支持：CAD、Text、Graph、Tree、HeightMap 等）。
- `scale`、`rotation`、`translation` 至少要给一个；三者都为 nil 的动作是空操作。
- 旋转用角–轴表示：`rotation(angle: -90, axis: [1, 0, 0])` 即绕 X 轴转 -90°。
- `Transform` 不会把实体切换成 `.kinematic` —— 动画期间物理照常生效。

## Example

### 实体

```phymodel

HeightMap()
.name("heightMap1")
.mesh(size: (2, 2), thickness: 0.2, resolution: (64, 64))
.physic(mass: 0.8, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .dynamic)
.material(red: 0.6, green: 0.3, blue: 0.2, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 0.0, y: 0.8, z: 0.0)

```

### 触发系统

```phymodel

Behavior()
.name("tapHeightMap1")
.trigger{
    Tap(){
        objects: ["heightMap1"]
    }
}
.actions{
    Transform(1){
        objects: ["heightMap1"],
        scale: [1.0, 1.0, 1.0],
        rotation(angle: -90, axis: [1,0,0]),
        translation: [0.0, 0.1, -1.5],
        easeType: .easeOut,
        duration: 3.0
    }
}

```
