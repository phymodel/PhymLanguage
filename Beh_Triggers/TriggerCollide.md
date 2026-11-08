# Collide

> `Collide(objects: [String], collisionWith: [String])`

## Purpose

`objects` 中任一实体与 `collisionWith` 中任一实体发生物理碰撞时，触发这里挂载的 `.actions`。两侧都必须是 `.dynamic`，才会参与物理仿真的碰撞检测。

## Parameters

| 参数 | 类型 | 必填 | 默认 | 说明 |
|---|---|---|---|---|
| objects | [String] | ✅ | — | 主实体名数组（碰撞的「主语」） |
| collisionWith | [String] | ✅ | — | 目标实体名数组（被撞的「宾语」） |

## Constraints

- 只有 **ModelEntity** 实例参与（带 `.physic(mode:)` 的 CAD、Text 等）。
- `objects` 与 `collisionWith` 里的实体都必须用 `.physic(mode: .dynamic)` —— kinematic 或 static 实体不产生碰撞事件。
- 碰撞匹配是**双向**的：`objects` 里的 entityA 撞上 `collisionWith` 里的 entityB，与 entityB 在 `objects`、entityA 在 `collisionWith` 时触发的是同一个触发器。
- 每一对碰撞（`entityA` ↔ `entityB`）在每个「开始接触」事件上只触发一次；每出现一次新的碰撞，动作链都从头上重跑。

## Example

### 实体

```phymodel

CAD()
.name("cube1")
.mesh(commands: [
    "DEF box1 = PATH -0.05,-0.1,-0.1 Y -0.05,-0.1 0.05,-0.1 0.05,0.1 -0.05,0.1 EXT 0.2 FILLET 0.005",
])
.physic(mass: 0.3, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .dynamic)
.material(red: 0.27, green: 0.39, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: -1.8, y: 1.0, z: 0.0)

CAD()
.name("cube2")
.mesh(commands: [
    "DEF box2 = PATH -0.4,-0.1,-0.25 Y -0.4,-0.25 0.4,-0.25 0.4,0.25 -0.4,0.25 EXT 0.2 FILLET 0.06",
])
.physic(mass: 0.3, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.3, mode: .dynamic)
.material(red: 0.5, green: 0.5, blue: 0.5, opacity: 0.6, roughness: 0.3, metallic: 0.9)
.position(x: -1.2, y: 1.5, z: 0.0)

CAD()
.name("ellipsoid1")
.mesh(commands: [
    "DEF ellipsoid1 = SOLID_FORMULA 0,0,0 (x/0.1)^2+(y/0.1)^2+(z/0.1)^2-1=0",
])
.physic(mass: 0.6, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .dynamic)
.material(red: 0.67, green: 0.32, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 1.0, y: 1.5, z: 0.0)

```

### 触发系统

```phymodel

Behavior()
.name("collideEllipsoidCubes")
.trigger{
    Collide(){
        objects: ["ellipsoid1"],
        collisionWith: ["cube1", "cube2"]
    }
}
.actions{
    Hide(1){
        objects: ["cube1", "cube2", "ellipsoid1"],
        motionType: .scale,
        duration: 2.0
    }
    Wait(2){
        duration: 3.0
    }
    Show(3){
        objects: ["cube1", "cube2"],
        motionType: .pop,
        duration: 2.5
    }
}

```
