# Emphasize

> `Emphasize(objects: [String], motionType: MotionType = .pop, duration: Float = 1.0)`

## Purpose

在目标实体上播放一次强调动画（脉冲、弹跳、闪烁等），把用户的注意力引过去。

## Parameters

| 参数 | 类型 | 必填 | 默认 | 说明 |
|---|---|---|---|---|
| objects | [String] | ✅ | — | 目标实体名数组 |
| motionType | enum | ❌ | .pop | `.pop` `.blink` `.bounce` `.flip` `.float` `.jiggle` `.pulse` `.spin` |
| duration | Float | ❌ | 1.0 | 动画时长（秒） |

## Constraints

- 只影响 **ModelEntity** 实例（Text 与 CAD 生成的实体都支持）。

## Example

### 实体

```phymodel

Text()
.name("textHello")
.mesh(text: "Hello, World!", extrusionDepth: 0.02, fontSize: 0.1)
.physic(mass: 0.1, staticFriction: 0.9, dynamicFriction: 0.75, restitution: 0.22, mode: .kinematic)
.material(red: 0.2, green: 0.8, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 0.0, y: 1.5, z: 0.0)

```

### 触发系统

```phymodel

Behavior()
.name("tapTextHello")
.trigger{
    Tap(){
        objects: ["textHello"]
    }
}
.actions{
    Emphasize(1){
        objects: ["textHello"],
        motionType: .pulse,
        duration: 1
    }
}

```
