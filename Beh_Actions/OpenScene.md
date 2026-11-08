# OpenScene

> `OpenScene(scene: String, duration: Float = 0)`

## Purpose

从当前场景跳到文档库里另一个 `.md` 场景文件。路径相对当前场景的 `.md` 解析。

## Parameters

| 参数 | 类型 | 必填 | 默认 | 说明 |
|---|---|---|---|---|
| scene | String | ✅ | — | 目标 `.md` 场景的相对路径（支持 `../`、`./` 与同目录文件名） |
| duration | Float | ❌ | 0 | 跳转前的延时（秒）；0 = 执行到这一步就立刻跳 |

## Constraints

- 解析出的路径必须在文档库内、且扩展名是 `.md`；否则这个动作被跳过并给出警告。
- 与 `MoveAlong` 的 `path` 参数（那个引用的是 `Graph` 实体名）无关。
- 不需要 `objects`。
- 与 `Speak` 写在同一条 `Behavior` 链里时，`OpenScene` 会等 `Speak` 说完（或被新的 `Speak` 打断）；需要额外留白就加一个 `Wait`。

## Example

### 实体

```phymodel

CAD()
.name("nextButton")
.mesh(commands: [
    "DEF plate = PATH 0,0,0 Y 0.15,0.15 -0.15,0.15 -0.15,-0.15 0.15,-0.15 EXT 0.005 FILLET_V 0.01",
])
.physic(mass: 0.2, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .kinematic)
.material(red: 0.46, green: 0.2, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 0.0, y: 1.5, z: 0.0)

```

### 触发系统

```phymodel

Behavior()
.name("goNextChapter")
.trigger{
    Tap(){
        objects: ["nextButton"]
    }
}
.actions{
    Speak(1){
        object: "nextButton",
        text: "进入下一章"
    }
    OpenScene(2){
        scene: "../Beh_Actions/Orbit.md",
        duration: 0
    }
}

```
