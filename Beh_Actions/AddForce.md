# AddForce

> `AddForce(objects: [String], force: [Float×3] = [0,0,0], atPosition: [Float×3] = [0,0,0], relativeTo: String = "nil")`

## Purpose

对目标实体施加一个力（单位 N，沿力矢量方向），在给定时长内产生持续加速度。

## Parameters

| 参数 | 类型 | 必填 | 默认 | 说明 |
|---|---|---|---|---|
| objects | [String] | ✅ | — | 目标实体名数组 |
| force | [Float×3] | ❌ | [0,0,0] | 力矢量 [x, y, z]，单位 N |
| atPosition | [Float×3] | ❌ | [0,0,0] | 作用点（世界坐标）；偏离质心会产生力矩 |
| relativeTo | String | ❌ | "nil" | 力矢量的参考系：`"nil"` = 世界系；实体名 = 该实体的局部系 |

## Constraints

- 只影响 **ModelEntity** 实例（CAD 与 Text 生成的实体都支持）。
- 目标实体应当用 `.physic(mode:)` 的 **`.dynamic`**，否则力不会产生运动。
- `relativeTo` 引用了不存在的实体时，回退到世界坐标（警告级别）。

## Example

### 实体

```phymodel

CAD()
.name("ellipsoid1")
.mesh(commands: [
    "DEF ellipsoid1 = SOLID_FORMULA 0,0,0 (x/0.1)^2+(y/0.1)^2+(z/0.1)^2-1=0",
])
.physic(mass: 1.6, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .dynamic)
.material(red: 0.67, green: 0.32, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 0.0, y: 1.5, z: 0.0)

```

### 触发系统

```phymodel

Behavior()
.name("tapEllipsoid1")
.trigger{
    Tap(){
        objects: ["ellipsoid1"]
    }
}
.actions{
    AddForce(1){
        objects: ["ellipsoid1"],
        force: [0.0, 500.0, 0.0],
        atPosition: [0.0, 0.0, 0.0],
        relativeTo: "nil"
    }
}

```
