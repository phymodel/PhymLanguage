# PATH_FORMULA_XY

用参数方程 `x(t)` 与 `y(t)` 创建 2D 轮廓，再沿路径拉伸或扫掠。与使用隐式方程 `f(x,y)=0` 的 `PATH_FORMULA` 不同，这里用的是 `t` 的显式参数函数。`domainHalfSize` 控制采样范围，`segCount` 决定分段数。

> `DEF name = PATH_FORMULA_XY x,y,z NORMAL x_expr y_expr domainHalfSize segCount EXT h [FILLET r]`
> `DEF name = PATH_FORMULA_XY x,y,z NORMAL x_expr y_expr domainHalfSize segCount EXT_Bezier ... SEG N [FILLET r]`
> `DEF name = PATH_FORMULA_XY x,y,z NORMAL x_expr y_expr domainHalfSize segCount EXT_BSpline ... SEG N [DEG D] [FILLET r]`

```phymodel

CAD()
.name("folium")
.mesh(commands: [
    "DEF folium = PATH_FORMULA_XY 0,0,0 Y 0.9*tan(t/2)^2/(1+tan(t/2)^6) 0.9*tan(t/2)^4/(1+tan(t/2)^6) 65 EXT 0.02"
])
.material(red: 0.2, green: 0.6, blue: 0.8, opacity: 1, roughness: 0.3, metallic: 0.5)
.physic(mass: 0.5, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .kinematic)
.position(x: 0.0, y: 1.4, z: 0.0)

```
