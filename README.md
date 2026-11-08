# PhymLanguage

> PhyModel 场景 DSL（`.phym`）的**语言参考 + 内容库** —— 一篇文档，就是一个能点、能拖、能算的场景。

本仓库**不含引擎代码**。它是一套写给 [PhyModel](#相关仓库)（visionOS / iOS，RealityKit）与
PhyModel_Web（浏览器）读取的文档库：`.md` 既是说明书，也是场景源文件 —— 正文是场景里的展板，
围栏里的 DSL 是场景本身。渲染器、编辑器、解析器都在隔壁仓库里。

## 仓库里有什么

| 目录 | 内容 | 规模 |
|---|---|---|
| [`Entity/`](./Entity) | 实体参考：几何、材质、物理，以及 `CAD()` 的命令栈 | 10 类实体 · 14 条 CAD 命令 |
| [`Beh_Actions/`](./Beh_Actions) | 动作参考：动画、位移、物理力、声音、场景跳转 | 15 个动作 |
| [`Beh_Triggers/`](./Beh_Triggers) | 触发器参考：点、碰、近、滑、拖、抛 | 6 个触发器 |
| [`Physics/`](./Physics) | 按教材章节组织的物理场景库（公式推导 + 可运行场景） | 8 章 · 63 篇 `.md` · 29 张 `.html` 图 |
| [`Math/`](./Math) | 数学场景库（傅里叶级数等） | 4 个波形场景 |
| [`EmbodiedIntelligence/`](./EmbodiedIntelligence) | 工程样例：用 phym 当 3D 打印件的**源文件** | MicroDuck 零件 |

## 文档即场景

一条 `.md` 文档承载全部内容，没有单独的工程文件：

| 你写的 | 阅读器怎么读 |
|---|---|
| 正文（Markdown + LaTeX） | 文档面板；`Latex()` / `LatexPath()` 还能把正文直接搬进 3D 场景当展板 |
| ```` ```phymodel ```` 围栏 | **场景内容**：实体 + 行为，按文档顺序并入场景 |
| `![Entity](./01 Entity.phym)` | **片段引用**：此处并入该 `.phym` 里的 DSL（相对当前 `.md`、允许空格、围栏内不算、嵌套跟随、环引用拒绝） |
| `![ca](./HCP_ca.html)` | **HTML 图**：`sandbox=""` 的 iframe，就是一幅画 |
| `![](./tex.png)`、`.material(imagePath:)` | 位图贴图 / 插图，路径同样相对当前 `.md` |

所以文档库是一棵**可直接运行**的目录树：改一行代码再刷新，场景就变了。

## 最小可运行场景

```phymodel
CAD()
.name("plate1")
.mesh(commands: [
    "DEF plate = PATH 0,0,0 Y 0.15,0.15 -0.15,0.15 -0.15,-0.15 0.15,-0.15 EXT 0.005 FILLET_V 0.01",
])
.material(red: 0.46, green: 0.2, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.physic(mass: 0.2, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .dynamic)
.position(x: 0, y: 1.5, z: 0)

Behavior()
.name("tapPlate1")
.trigger{
    Tap(){
        objects: ["plate1"]
    }
}
.actions{
    Spin(1){
        objects: ["plate1"],
        iterations: 2.0,
        clockwise: true,
        axis: .yaw,
        duration: 3
    }
}
```

一块板子，点一下转两圈。把这段贴进任意 `.md` 的 ```` ```phymodel ```` 围栏即可。

## 打开 / 运行

**网页版（只读查看器，最快）**

```bash
cd ../PhyModel_Web
./start-dev.command          # 首次会自动 npm install，然后打开 http://localhost:5173
```

在目录面板点 **📁 选文件夹**，选中本仓库目录（也可直接把文件夹拖进去）。内容全部读进浏览器内存，
**不上传、不写盘**；刷新页面要重新选一次。

**原生版（visionOS / iOS）**：用 PhyModel 的文档库指向本仓库目录 —— 支持交互、物理、语音与文件同步。

## DSL 速查

### 通用修饰符

每个实体都以 `.name(...)` 起头，后面按需串联：

| 修饰符 | 例子 | 说明 |
|---|---|---|
| `.name(...)` | `.name("plate1")` | 实体名，行为用这个名字点名；必填 |
| `.mesh(...)` | `.mesh(text: "你好")` | 几何定义，参数随实体类型不同；必填 |
| `.physic(...)` | `.physic(mass: 0.2, …, mode: .dynamic)` | 质量 / 静摩擦 / 动摩擦 / 弹性 / 模式（`.dynamic` `.kinematic` `.static`） |
| `.material(...)` | `.material(red: 0.46, …, metallic: 0.8, imagePath: "./tex.png")` | 颜色、不透明度、粗糙度、金属度，可选贴图 |
| `.position(...)` | `.position(x: 0, y: 1.5, z: 0)` | 世界坐标（**米**） |
| `.rotation(...)` | `.rotation(angle: 90, axis: [0,0,1])` | 绕轴旋转（度） |
| `.isEnabled(...)` | `.isEnabled(false)` | 是否参与渲染与物理 |
| `.simulation(...)` | `.simulation(wind: (0.6, 0, 0.4), windEnabled: true)` | 布料等类型的仿真参数 |

单位只有一套：**米**，**Y 朝上**。字号、半径、位移全都用米 —— 30 mm 的直径写成 `0.015` 的半径。

### 实体（10 类）

| 实体 | 用途 | 文档 |
|---|---|---|
| `CAD()` | 命令栈建模：路径 / 隐式方程挤出、旋转体、等值面、布尔、放样、抽壳 | [`Entity/Entity_CAD/`](./Entity/Entity_CAD) |
| `Polyhedron()` | 5 种正多面体 | [Polyhedron.md](./Entity/Polyhedron.md) |
| `Text()` | 实体化 3D 文字（笔画有真实厚度，投影、参与碰撞） | [Text.md](./Entity/Text.md) |
| `Latex()` | Markdown + LaTeX 渲染成 3D 平面；`textPath` 可直接取当前 `.md` 某段正文 | [Latex.md](./Entity/Entity_Latex/Latex.md) |
| `Graph()` | 参数曲线（`x` / `y` / `z` / `t` 表达式）→ 管状网格 | [Graph.md](./Entity/Graph.md) |
| `Tree()` | 过程化树，`growthProgress` 控制从树苗到长成 | [Tree.md](./Entity/Tree.md) |
| `HeightMap()` | 多层程序化波形叠加出的地形 | [HeightMap.md](./Entity/HeightMap.md) |
| `Cloth()` | 布料 / 裙摆，支持风场（不支持 `.dynamic`） | [Cloth.md](./Entity/Entity_Cloth/Cloth.md) |
| `HEWF()` | 氢原子电子波函数 ψ<sub>nℓm</sub> 电子云（真实量子力学轨道） | [HEWF.md](./Entity/HEWF.md) |
| `Group()` | 只引用成员名字，把平铺的实体归成一个整体 | [Group.md](./Entity/Group.md) |

`CAD()` 的命令栈（[完整参考](./Entity/Entity_CAD)）：

| 类别 | 命令 |
|---|---|
| 轮廓挤出 | `PATH`（顶点环）· `PATH_FORMULA`（隐式方程 `f(x,y)=0`）· `PATH_FORMULA_XY`（参数方程 `x(t)`/`y(t)`） |
| 旋转体 | `PATH_OPEN` + `REV`（开链绕轴旋转） |
| 立体成形 | `SOLID_FORMULA`（隐式曲面 `f(x,y,z)=0`，Marching Cubes）· `LOFT`（变截面放样）· `SHELL`（抽壳） |
| 沿曲线扫掠 | `EXT_Bezier` · `EXT_BSpline` |
| 倒角 | `FILLET` · `FILLET_H`（水平边）· `FILLET_V`（垂直边） |
| 布尔 | `UNION` · `SUBTRACT` · `INTERSECT` |

### 触发器（6）

| 触发器 | 何时触发 |
|---|---|
| [`Tap`](./Beh_Triggers/TriggerTap.md) | 点到实体（短于 0.25 s、位移小于 1 cm，不会被当作「抛出」） |
| [`Collide`](./Beh_Triggers/TriggerCollide.md) | 与指定实体发生碰撞 |
| [`Proximity`](./Beh_Triggers/TriggerProximity.md) | 相机进入实体的 `distance` 米范围内 |
| [`Slider`](./Beh_Triggers/TriggerSlider.md) | 拖动实体，位移经 `output` 暴露给动作（做滑杆用） |
| [`Drag`](./Beh_Triggers/TriggerDrag.md) | 被携带的实体到达 `target` |
| [`Throw`](./Beh_Triggers/TriggerThrow.md) | 抛出实体，或穿过 `through` 目标 |

### 动作（15）

| 类别 | 动作 |
|---|---|
| 变换 | [`Transform`](./Beh_Actions/Transform.md)（位移 / 旋转 / 缩放，目标位姿是绝对值）· [`Spin`](./Beh_Actions/Spin.md) · [`Orbit`](./Beh_Actions/Orbit.md) · [`MoveAlong`](./Beh_Actions/MoveAlong.md) · [`LookAtCamera`](./Beh_Actions/LookAtCamera.md) |
| 显隐与强调 | [`Show`](./Beh_Actions/Show.md) · [`Hide`](./Beh_Actions/Hide.md) · [`Emphasize`](./Beh_Actions/Emphasize.md) |
| 物理与运行时 | [`AddForce`](./Beh_Actions/AddForce.md) · [`EntityMesh`](./Beh_Actions/EntityMesh.md)（运行时改几何：参数曲线、树的生长） |
| 声音与语音 | [`PlaySound`](./Beh_Actions/PlaySound.md) · [`PlayMusic`](./Beh_Actions/PlayMusic.md) · [`Speak`](./Beh_Actions/Speak.md) |
| 流程 | [`Wait`](./Beh_Actions/Wait.md) · [`OpenScene`](./Beh_Actions/OpenScene.md)（跳到文档库里另一个 `.md`） |

### 行为与循环

```phymodel
Behavior()
.name("tapPlate1")
.trigger{
    Tap(){
        objects: ["plate1"]
    }
}
.actions{
    Transform(1){
        objects: ["plate1"],
        translation: [0.0, 1.7, 0.0],
        duration: 1.5
    }
    Wait(2){
        duration: 0.5
    }
    Transform(3){
        objects: ["plate1"],
        translation: [0.0, 1.5, 0.0],
        duration: 1.5
    }
}
```

- `.actions { … }` 里的动作**按顺序排队执行**：块名后的数字就是它的序号（`Transform(1)`、`Wait(2)`、`Transform(3)`），`Wait` 就是队列里的一个空档。
- `Transform` 的 `translation` 是**绝对目标位姿**，不是位移增量 —— 所以「抬起再落回」要把原来的
  `.position(...)` 再写一遍（写成 `[0, -0.2, 0]` 会把实体送到那个绝对坐标上去）。
- 交互**只在触发器里声明**：实体级的 `.gesture(...)` 已删除，写了会报错 ——
  一个实体不被任何触发器点名，就是纯装饰，永远不会误触发。
- 批量生成实体用 `Repeat(11) { i in … }`，名字里可以插值：`.name("tick[i]")`。

## 物理与数学场景库

`Physics/` 按教材章节目录排布，每篇都是「公式推导 + 可运行场景」的对照：

| 章 | 目录 | 覆盖 |
|---|---|---|
| 1 | [`1 力学/`](./Physics/1%20力学) | 运动学 · 静力学 · 动力学（牛顿定律、抛体、圆周运动、动量与能量、简谐振动…） |
| 2 | [`2 热学/`](./Physics/2%20热学) | 玻意耳 / 查理 / 盖-吕萨克定律、热力学第一定律、基本方程 |
| 3 | [`3 光学/`](./Physics/3%20光学) | 折射定律、球面折射、薄透镜 |
| 4 | [`4 电磁学/`](./Physics/4%20电磁学) | 电荷到场、电路、磁场、电磁感应、交流电与变压器（21 篇） |
| 5 | [`5 数学物理方法/`](./Physics/5%20数学物理方法) | 傅里叶变换 |
| 6 | [`6 原子物理/`](./Physics/6%20原子物理) | 半衰期、质能方程 |
| 7 | [`7 量子力学/`](./Physics/7%20量子力学) | 能量量子、光电效应、光子动量、频率条件 |
| 8 | [`8 固体物理/`](./Physics/8%20固体物理) | 六方最密堆积（配 `.html` 交互图） |

`Math/` 目前有[傅里叶级数](./Math/Advanced%20Mathematics/Fourier%20series)：锯齿波、方波、三角波、脉冲波的
分解与合成，公式推导与波形实体放在同一个目录里。

## 工程样例：phym 当零件的源文件

[`EmbodiedIntelligence/MicroDuck/`](./EmbodiedIntelligence/MicroDuck) 把一套 3D 打印件用 phym 重写：
零件不再是二进制 STL，而是一段可 diff、可参数化、可复算的建模命令 ——

```text
phym 代码（本仓库） ──渲染──▶ ⚙︎ 设置 → 导出实体 ──▶ STL / 3MF ──▶ 切片打印
```

方向是**单向**的：这里永远是源，导出的 STL 是产物。改尺寸就改 phym、再导一次。

## 约定

新增内容时请守住这几条，它们决定了这套文档能不能被机器读写：

1. **单位只有一个来源**：米、Y 朝上；尺寸写在 DSL 里，不写在资产文件里。
2. **不引入外部二进制模型**：`ModelURL()` 已从 DSL 整体删除 —— 外部资产破坏可 diff、可复算、可导出，
   解析器现在会对它报迁移错误。
3. **每个实体 / 触发器 / 动作一个 `.md`**，结构统一：`# 名称` → `> 签名` → `## Purpose` →
   `## Parameters` → `## Constraints` → `## Example`。
4. **示例必须能直接跑**：`Example` 里的代码要自成一体（实体 + 行为齐全），并注明依赖的实体名。
5. **交互只在触发器里声明**，不要在任何实体上写 `.gesture(...)`。
6. **与引擎保持同步**：本仓库描述的是 DSL 的**契约**，删除或改写某个关键字时，要在文档里留下
   迁移说明（例如 `ModelURL()`、`.gesture(...)` 都是在原处写明「已删除 / 写了会报错」）。

## 相关仓库

本仓库是内容与契约的**唯一来源**，两个渲染端都在同级的相邻仓库里：

| 仓库 | 角色 |
|---|---|
| `PhyModel` | 原生渲染器 / 编辑器（visionOS、iOS，RealityKit + iCloud，MiniAGI 对话驱动） |
| `PhyModel_Web` | 浏览器端（Vite + React + react-three-fiber/Three.js，Rapier / Jolt 物理，marked + KaTeX 渲染；只读查看器 + AI 对话，`src/dsl/` 是 Web 侧解析器） |
| **PhymLanguage**（本仓库） | DSL 参考 + 场景库，上面两端共同读取的文档库 |

## 许可证

仓库根目录目前**没有 `LICENSE` 文件**，即默认保留所有权利。若要在别处复用这里的文档或场景，
请先与作者确认。
