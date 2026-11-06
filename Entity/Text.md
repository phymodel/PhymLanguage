# Text

Extrudes 2D text into a 3D mesh. The glyphs themselves are **solid**: the strokes have real thickness (the side walls are visible), they cast shadows and take part in collisions — this is not a flat card with letters painted on it.

`.mesh(text:extrusionDepth:fontSize:font:alignment:)`

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `text` | String | — | 文字内容 |
| `extrusionDepth` | Float | `0.01` | 笔画厚度（字形沿 +Z 挤出的深度） |
| `fontSize` | Float | `0.05` | 字高（1 em，单位与场景一致） |
| `font` | String | `Times New Roman` | 字体名；`"Times New Roman Italic"` 这类「族名 + 字型后缀」写法同样有效 |
| `alignment` | TextAlignment | `.center` | 锚点：`.leading` / `.center` / `.trailing` |

`alignment` decides which point of the text's bounding box `.position` lands on: the box's **min** (`.leading`), its **center** (`.center`, default) or its **max** (`.trailing`). It applies to all three axes — with `.leading` the left edge, the bottom edge and the front face (z = 0) of the ink all sit on `.position`.

> Note: `font` 由运行平台解析。设备没装该字体（如 Linux 上的 `Times New Roman`），或字体里没有该字形（用西文字体写中文），都会由平台回退到同类字体 —— 字宽因此可能有细微差别。

> Note: Web 端正文里的 `\n` 转义会还原成换行（写回端就是按这个转义的）。

```phymodel

Text()
.name("text1")
.mesh(text: "Hello, World! 你好，世界！", extrusionDepth: 0.02, fontSize: 0.1)
.physic(mass: 0.1, staticFriction: 0.9, dynamicFriction: 0.75, restitution: 0.22, mode: .kinematic)
.material(red: 0.2, green: 0.8, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 0.0, y: 1.5, z: 0.0)

Text()
.name("textLeading")
.mesh(text: "左对齐", extrusionDepth: 0.02, fontSize: 0.05, alignment: .leading)
.physic(mass: 0.1, staticFriction: 0.9, dynamicFriction: 0.75, restitution: 0.22, mode: .kinematic)
.material(red: 0.2, green: 0.8, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 0.0, y: 1.4, z: 0.0)

Text()
.name("textCenter")
.mesh(text: "居中对齐", extrusionDepth: 0.02, fontSize: 0.05, alignment: .center)
.physic(mass: 0.1, staticFriction: 0.9, dynamicFriction: 0.75, restitution: 0.22, mode: .kinematic)
.material(red: 0.2, green: 0.8, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 0.0, y: 1.3, z: 0.0)

Text()
.name("textTrailing")
.mesh(text: "右对齐", extrusionDepth: 0.02, fontSize: 0.05, alignment: .trailing)
.physic(mass: 0.1, staticFriction: 0.9, dynamicFriction: 0.75, restitution: 0.22, mode: .kinematic)
.material(red: 0.2, green: 0.8, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 0.0, y: 1.2, z: 0.0)

```