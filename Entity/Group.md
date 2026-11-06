# Group

把多个实体归成一个**整体**：`Group` 只**引用**成员名字，实体本身**平铺**写在文档里。
（这是唯一写法；早期那种「把子实体写在 `Group(…) { … }` 块里、由组创建」的写法已废弃，**写了会明确报错**。）

> `Group()` + `.name("X")` + `.entity["成员名", …]`，可选 `.position(x:y:z:)` / `.isEnabled(bool)`

```phymodel

Group()
.name("CoordinateSystem")
.entity[
    "CoordinateSystemEllipsoid[i]",
    "CoordinateSystemText[i]",
    "CoordinateSystemBody",
    "CoordinateSystemBody2"
]
.position(x: 0.0, y: 1.5, z: 0.0)

Repeat(11) { i in
    CAD()
    .name("CoordinateSystemEllipsoid[i]")
    .mesh(commands: [
        "DEF tick = SOLID_FORMULA 0,0,0 (x/0.02)^2+(y/0.02)^2+(z/0.02)^2-1=0",
    ])
    .material(red: 0.67, green: 0.32, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
    .physic(mass: 0.6, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .kinematic)
    .position(x: -0.5 + i * 0.1, y: 0.0, z: 0.0)
}

Repeat(11) { i in
    Text()
    .name("CoordinateSystemText[i]")
    .mesh(text: "[i]", extrusionDepth: 0.001, fontSize: 0.05)
    .material(red: 0.9, green: 0.1, blue: 0.3, opacity: 1, roughness: 0.5, metallic: 0.8)
    .physic(mass: 0.3, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .kinematic)
    .position(x: -0.5 + i * 0.1, y: -0.05, z: 0.0)
}

CAD()
.name("CoordinateSystemBody")
.mesh(commands: [
    "DEF coordinateAxis = PATH_FORMULA 0.0,-0.7,0.0 Y (x-0.0)^2+(y-0.0)^2=0.005^2 0.06 80 EXT 1.4"
])
.material(red: 0.5, green: 0.5, blue: 0.5, opacity: 1, roughness: 0.3, metallic: 0.9)
.physic(mass: 0.3, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .kinematic)
.position(x: 0.0, y: 0.0, z: 0.0)
.rotation(angle: 90.0, axis: [0,0,1])

CAD()
.name("CoordinateSystemBody2")
.mesh(commands: [
    "DEF coordCone = PATH_OPEN 0,-0.025,0 Z 0,0.05 0.02,0 0,0 REV Y 360"
])
.physic(mass: 0.5, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .kinematic)
.material(red: 0.7, green: 0.3, blue: 0.3, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 0.7, y: 0.0, z: 0.0)
.rotation(angle: -90.0, axis: [0,0,1])

Group()
.name("ruler")
.entity[
    "rulerBody",
    "rulerBody2",
    "rulerCube[i]",
    "rulerText[i]"
]
.position(x: 0.0, y: 1.7, z: 0.0)

CAD()
.name("rulerBody")
.mesh(commands: [
    "DEF rulerBody = PATH 0,-0.01,0 Y -0.1025,-0.001 -0.1025,0.001 0.1025,0.001 0.1025,-0.001 EXT 0.02",
])
.material(red: 0.5, green: 0.5, blue: 0.5, opacity: 1, roughness: 0.3, metallic: 0.9)
.physic(mass: 0.3, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .kinematic)
.position(x: 0.0, y: 0.0, z: 0.0)

CAD()
.name("rulerBody2")
.mesh(commands: [
    "DEF rulerBody2 = PATH_FORMULA 0,-0.001,0 Y (x-0.0)^2+(y-0.0)^2=0.01^2 0.06 80 EXT 0.002"
])
.material(red: 0.5, green: 0.5, blue: 0.5, opacity: 1, roughness: 0.3, metallic: 0.9)
.physic(mass: 0.3, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .kinematic)
.position(x: 0.103, y: 0.0, z: 0.0)
.rotation(angle: 90, axis: [1,0,0])

Repeat(201) { i in
    CAD()
    .name("rulerCube[i]")
    .mesh(commands: [
        "DEF tick = PATH -0.00005,-((i % 10 == 0 ? 0.008 : (i % 5 == 0 ? 0.006 : 0.004))/2),-0.0005 Y 0.00005,-0.0005 -0.00005,-0.0005 -0.00005,0.0005 0.00005,0.0005 EXT (i % 10 == 0 ? 0.008 : (i % 5 == 0 ? 0.006 : 0.004))",
    ])
    .material(red: 0.0, green: 0.0, blue: 0.0, opacity: 1, roughness: 0.8, metallic: 0.5)
    .physic(mass: 0.3, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .kinematic)
    .position(x: -0.20/2 + i * 0.001, y: (i % 10 == 0 ? 0.006 : (i % 5 == 0 ? 0.007 : 0.008)), z: 0.001)
}

Repeat(21) { i in
    Text()
    .name("rulerText[i]")
    .mesh(text: "[i]", extrusionDepth: 0.001, fontSize: 0.005)
    .material(red: 0.9, green: 0.1, blue: 0.3, opacity: 1, roughness: 0.5, metallic: 0.8)
    .physic(mass: 0.3, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .kinematic)
    .position(x: -0.20/2 + i * 0.01, y: -0.003, z: 0.001)
}

```

## 修饰行

| 修饰 | 说明 |
|---|---|
| `.name("X")` | **必填**。组名是成员挂载、场景树分组、行为寻址的键 |
| `.entity["成员名", …]` | 成员列表：实体名、`Repeat` 模板名（`名字[i]`）、或另一个组名 |
| `.position(x:…, y:…, z:…)` | 组的**叠加偏移**（见「语义」） |
| 交互（点 / 拖） | **不在组上写**：实体级与组级的 `.gesture(...)` 都已删除。想让整组可点 / 可拖，就用触发器点名**组名** —— `Tap(){ objects: ["组名"] }` / `Slider(){ objects: ["组名"], output: ["x"] }`（组是容器实体，拖它就是整组一起动） |
| `.isEnabled(bool)` | `false` = 整组隐藏 |

## 语义

1. **成员坐标就是场景坐标**。组的 `.position` 是叠加在成员之上的偏移：
   世界坐标 = 成员自己的坐标 + 组偏移。所以「把整组挪高 1.5 m」只要改组的一行，
   成员一个数都不用动。
2. **前向引用**：成员可以写在组声明**之后**（上例就是）。解析是「先收全部实体，再按名字链接」。
3. **`名字[i]` 是模板**：`rulerCube[i]` 匹配 `Repeat(201)` 展开出的 `rulerCube0 … rulerCube200`
   （`[…]` 里写什么都行，按下标通配 —— 模型侧不知道展开后的具体下标）。
4. **组引用组**：成员名写另一个组名，就是把那个组的成员整批并进来，偏移按祖先链**逐层叠加**。
5. **一个实体只能属于一个组**（多归属报错）；**一个组也只能被一个更大的组引用**。
   要「共享」一批实体，请抽一个更大的组去引用它们。
6. **环检测**：`A → B → A` 直接报错。
7. 名字先按**实体名**（精确 / 模板）匹配，再按**组名**匹配；都没找到就报错，不会静默成空组。

## 顶层 Repeat

`Repeat(n) { i in <模板实体> }` 可以**平铺**写在文档里（不套 Group），展开成 n 个顶层实体：

```phymodel

Repeat(5) { i in
    CAD()
    .name("domino[i]")
    .mesh(commands: [
        "DEF domino = PATH 0,0,0 Y 0.05,0.05 -0.05,0.05 -0.05,-0.05 0.05,-0.05 EXT 0.01"
    ])
    .physic(mass: 0.5, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .dynamic)
    .material(red: 0.2, green: 0.6, blue: 0.9, opacity: 1, roughness: 0.5, metallic: 0.8)
    .position(x: i * 0.05, y: 0.5, z: 0.0)
}

```

三条索引通道与组内 Repeat 完全一致：`.name("…")` / `text: "…"`、`.mesh(commands: [ … ])` 里的
命令字符串、`.position(x: …)` 里的数值表达式。

## 报错路径（都不会静默）

- **包含式写法**（`Group(name: "X") { … }` / `Group { … }`）：整块拒绝并指出新写法，不半解析；
- 忘了 `.name("…")`；
- `.entity[…]` 是空的；
- 成员名没找到（既不是实体名 / 模板名，也不是组名）；
- 实体重名（名字是 Behavior / Group / 场景树唯一的寻址键，**同一场景内实体名必须唯一**）；
- 实体同时属于多个组（**同一个组**里重复列出是幂等的，不算多归属）；
- 一个组被两个更大的组引用；
- 组引用成环；
- 组里写了实体行 / `Repeat`（成员要平铺写在文档里，组只收成员名字与组级修饰行）。
