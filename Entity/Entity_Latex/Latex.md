# Latex

`Latex()` renders Markdown + LaTeX content as a 3D planar texture (supports HTML formatting, e.g., `<center>`, `<span style="font-size: …">`).

Choose one of two content sources for `.mesh`:
- `text: "…"` — inline Markdown + LaTeX directly, content wrapped in paired `¥¥` fences (see example);
- `textPath: "…"` — reference the body text of a heading section from the current or a specified `.md` file, see [LatexPath](LatexPath.md).

`width:` controls the plane width.

```phymodel

Latex()
.name("text12")
.mesh(width: 1.0, text: ¥¥
<center>
<span style="font-size: 90px;"> 时间间隔 $\Delta x = t_2 - t_1$</span>
</center>
¥¥
)
.material(red: 1.0, green: 1.0, blue: 1.0, opacity: 0.999, roughness: 0.5, metallic: 0.8)
.physic(mass: 0.1, staticFriction: 0.9, dynamicFriction: 0.75, restitution: 0.22, mode: .kinematic)
.position(x: 0.0, y: 1.3, z: 0.0)

```
