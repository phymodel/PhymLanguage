# LatexPath

在 `Latex()` 的 `.mesh` 里，`text` 与 `textPath` 二选一。`textPath` 把当前或指定 `.md` 文件里某一节标题下的正文（Markdown + LaTeX，不含 phymodel 代码块）渲染成一块 3D 平面。

路径格式：文件路径 + `#` + 标题层级（自上而下，用 `#` 分隔）。

| 记号 | 含义 |
|------|------|
| `时刻与时间间隔` | 当前场景文件里的某个标题 |
| `速度公式#时刻与时间间隔` | 当前文件里的多级标题（`# 速度公式` → `## 时刻与时间间隔`） |
| `./01 速度公式#速度公式#时刻与时间间隔` | 相对当前 `.md` 目录的文件 + 标题 |
| `../../Physics/1 力学/1 运动学/01 速度公式#速度公式#时刻与时间间隔` | 相对文档库根的路径 + 标题 |

```phymodel

Latex()
.name("textConcept")
.mesh(width: 1.2, textPath: "../../Physics/1 力学/1 运动学/01 速度公式")
.material(red: 1.0, green: 1.0, blue: 1.0, opacity: 0.999, roughness: 0.5, metallic: 0.8)
.physic(mass: 0.1, staticFriction: 0.9, dynamicFriction: 0.75, restitution: 0.22, mode: .kinematic)
.position(x: 0.0, y: 1.6, z: 0.0)

```
