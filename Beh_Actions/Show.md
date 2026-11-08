# Show

> `Show(objects: [String], motionType: ShowMotionType = .pop, duration: Float = 1.0)`

## Purpose

把之前隐藏的实体显示出来，可选入场动画。恢复目标实体的可见性与交互（命中检测）。

## Parameters

| 参数 | 类型 | 必填 | 默认 | 说明 |
|---|---|---|---|---|
| objects | [String] | ✅ | — | 目标实体名数组 |
| motionType | enum | ❌ | .pop | `.none` `.moveToLeft` `.moveToRight` `.moveToFront` `.moveToRear` `.moveToAbove` `.moveToBelow` `.pop` `.scale` `.scaleBig` |
| duration | Float | ❌ | 1.0 | 动画时长（秒） |

## Constraints

- 只影响 **ModelEntity** 实例（CAD 与 Text 生成的实体都支持）。
- 实体本来就是可见的，入场动画照样播。
- 用 `.isEnabled(false)` 创建的实体一开始是隐藏的，必须用 `Show` 显示。

## Example

### 实体

```phymodel

CAD()
.name("cube1")
.mesh(commands: [
    "DEF box1 = PATH -0.05,-0.1,-0.1 Y 0.05,-0.1 -0.05,-0.1 -0.05,0.1 0.05,0.1 EXT 0.2 FILLET 0.005",
])
.physic(mass: 0.3, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .kinematic)
.material(red: 0.27, green: 0.39, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 0.0, y: 1.0, z: 0.0)

CAD()
.name("cube2")
.mesh(commands: [
    "DEF box1 = PATH -0.05,-0.1,-0.1 Y 0.05,-0.1 -0.05,-0.1 -0.05,0.1 0.05,0.1 EXT 0.2 FILLET 0.005",
])
.physic(mass: 0.3, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .kinematic)
.material(red: 0.27, green: 0.39, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 0.5, y: 1.0, z: 0.0)
.isEnabled(false)

```

### 触发系统

```phymodel

Behavior()
.name("tapCube1")
.trigger{
    Tap(){
        objects: ["cube1"]
    }
}
.actions{
    Hide(1){
        objects: ["cube1"],
        motionType: .scale,
        duration: 2.0
    }
    Wait(2){
        duration: 3.0
    }
    Show(3){
        objects: ["cube2"],
        motionType: .pop,
        duration: 2.5
    }
}

```
