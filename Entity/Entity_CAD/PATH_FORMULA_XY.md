# PATH_FORMULA_XY

Creates a 2D profile from parametric equations `x(t)` and `y(t)`, then extrudes or sweeps it along a path. Unlike `PATH_FORMULA` which uses an implicit equation `f(x,y)=0`, this uses explicit parametric functions of `t`. The `domainHalfSize` controls the sampling range and `segCount` sets the number of segments.

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
