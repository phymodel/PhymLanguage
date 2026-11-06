# HEWF — 氢原子电子波函数

`HEWF()`（**H**ydrogen **E**lectron **W**ave **F**unction）渲染氢原子的真实量子力学轨道电子云
ψ_{nℓm}（径向为关联拉盖尔多项式 × 指数衰减，角向为实型球谐）。在「场景实体树」窗口选中实体即可
编辑量子数与显示参数。

## `.mesh(...)` 参数

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `n` | Int | `1` | 主量子数（电子层），1…7（K–Q） |
| `l` | Int | `0` | 角量子数（亚层），0…min(n-1, 6)（s–i） |
| `m` | Int | `0` | 磁量子数，0…ℓ |
| `mode` | enum | `.isosurface` | `.isosurface`（等值面轮廓）/ `.scatter`（概率散点） |
| `contour` | Float | `0.002` | 等值面相对最大概率密度的比例（仅 `isosurface` 生效） |
| `scale` | Float | `0.01` | 显示用玻尔半径（米），控制整体尺寸 |

> 说明：等值面通过 Marching Cubes 提取，GPU（Metal）加速、CPU 并行回退；散点通过拒绝采样按
> |ψ|² 分布生成。ℓ ≤ 4（s/p/d/f/g）为精确实球谐，ℓ = 5、6（h/i）为近似角向包络。

```phymodel

HEWF()
.name("hydrogen_1s")
.mesh(n: 1, l: 0, m: 0, mode: .isosurface, contour: 0.002, scale: 0.01)
.material(red: 0.2, green: 0.6, blue: 1.0, opacity: 0.7, roughness: 0.5, metallic: 0.0)
.position(x: 0.0, y: 1.5, z: 0.0)

HEWF()
.name("hydrogen_3d")
.mesh(n: 3, l: 2, m: 2, mode: .isosurface, contour: 0.004, scale: 0.012)
.material(red: 1.0, green: 0.85, blue: 0.2, opacity: 0.6, roughness: 0.5, metallic: 0.0)
.position(x: 0.6, y: 1.5, z: 0.0)

HEWF()
.name("hydrogen_2p_scatter")
.mesh(n: 2, l: 1, m: 1, mode: .scatter, contour: 0.002, scale: 0.01)
.material(red: 1.0, green: 0.5, blue: 0.2, opacity: 0.5, roughness: 0.5, metallic: 0.0)
.position(x: -0.6, y: 1.5, z: 0.0)

```
