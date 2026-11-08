# Latex

`Latex()` 把 Markdown + LaTeX 内容渲染成 3D 平面贴图（支持 HTML 排版，例如 `<center>`、`<span style="font-size: …">`）。

`.mesh` 的内容来源二选一：
- `text: "…"` —— 直接写 Markdown + LaTeX，内容用成对的 `¥¥` 围起来（见示例）；
- `textPath: "…"` —— 引用当前或指定 `.md` 文件里某一节标题下的正文，见 [LatexPath](LatexPath.md)。

`width:` 控制平面宽度。

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
