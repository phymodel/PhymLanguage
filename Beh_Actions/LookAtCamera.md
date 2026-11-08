# LookAtCamera

> `LookAtCamera(objects: [String], facingDirection: FacingDirection = .front, rotationEuler: RotationFreedom = .free, duration: Float = 0)`

## Purpose

让目标实体转到指定的一面朝向当前相机。`duration > 0` 时旋转平滑过渡。

## Parameters

| 参数 | 类型 | 必填 | 默认 | 说明 |
|---|---|---|---|---|
| objects | [String] | ✅ | — | 目标实体名数组 |
| facingDirection | enum | ❌ | .front | 朝向相机的面：`.front` `.back` `.left` `.right` `.top` `.bottom` |
| rotationEuler | enum | ❌ | .free | 受限的旋转轴：`.free` `.pitch` `.yaw` `.roll` |
| duration | Float | ❌ | 0 | 旋转动画时长（秒）；0 = 瞬时 |

## Constraints

- 只影响 **ModelEntity** 实例（CAD 与 Text 生成的实体都支持）。
- 把 `rotationEuler` 设成 `.pitch`/`.yaw`/`.roll` 时，朝向旋转会投影到那一个轴上；那一个面可能并不会完全对准相机。
- 正在参与物理仿真的实体（`.dynamic`）在动画期间朝向被接管，动画结束后交回物理。

## Example

### 实体

```phymodel

CAD()
.name("cube2")
.mesh(commands: [
    "DEF box2 = PATH -0.4,-0.1,-0.25 Y -0.4,-0.25 0.4,-0.25 0.4,0.25 -0.4,0.25 EXT 0.2 FILLET 0.06",
])
.physic(mass: 0.3, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.3, mode: .dynamic)
.material(red: 0.5, green: 0.5, blue: 0.5, opacity: 0.6, roughness: 0.3, metallic: 0.9)
.position(x: 0.0, y: 1.5, z: 0.0)

```

### 触发系统

```phymodel

Behavior()
.name("tapCube2")
.trigger{
    Tap(){
        objects: ["cube2"]
    }
}
.actions{
    LookAtCamera(2){
        objects: ["cube2"],
        facingDirection: .front,
        rotationEuler: .free,
        duration: 5
    }
}

```
