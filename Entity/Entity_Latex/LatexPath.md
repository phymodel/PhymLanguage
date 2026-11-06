# LatexPath

In `Latex()`'s `.mesh`, choose either `text` or `textPath`. `textPath` renders the body text of a heading section from the current or a specified `.md` file (Markdown + LaTeX, excluding phymodel code blocks) as a 3D plane.

Path format: file path + `#` + heading hierarchy (top-down, separated by `#`).

| Notation | Meaning |
|------|------|
| `时刻与时间间隔` | Heading within the current scene file |
| `时间间隔公式#时刻与时间间隔` | Multi-level heading in the current file (`# 时间间隔公式` → `## 时刻与时间间隔`) |
| `./01.1 时间间隔公式#时间间隔公式#时刻与时间间隔` | File relative to the current `.md` directory + heading |
| `../../Physics/1 力学/1 运动学/01.1 时间间隔公式#时间间隔公式#时刻与时间间隔` | Document library root-relative path + heading |

```phymodel

Latex()
.name("textConcept")
.mesh(width: 1.2, textPath: "../../Physics/1 力学/1 运动学/01 时间间隔公式")
.material(red: 1.0, green: 1.0, blue: 1.0, opacity: 0.999, roughness: 0.5, metallic: 0.8)
.physic(mass: 0.1, staticFriction: 0.9, dynamicFriction: 0.75, restitution: 0.22, mode: .kinematic)
.position(x: 0.0, y: 1.6, z: 0.0)

```
