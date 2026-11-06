# EXT_BSpline

Extrudes a 2D profile along a B-spline curve defined by a sequence of control points. Use with path-based primitives (`PATH_FORMULA`, `PATH_FORMULA_XY`, `PATH`) to create swept solids. Control points are given as `(x,y,z)` triplets. `DEG` sets the B-spline degree (default 3). `SEG` sets the segment count along the curve; `FILLET` optionally rounds the resulting edges.

> `... EXT_BSpline (x1,y1,z1),(x2,y2,z2),... SEG N [DEG D] [FILLET r]`

```phymodel

CAD()
.name("BSplineConcave")
.mesh(commands: [
    "DEF concave = PATH_FORMULA_XY 0,0,0 X (6-2*sin(t))*cos(t) -(2+(0.2-3*sin(t))*sin(t)) 0.2 64 EXT_BSpline (2.5,1,0),(2,1,0),(1.5,0.4,0),(1,0.2,0),(0.5,0,0),(0,0,0) SEG 48"
])
.material(red: 0.2, green: 0.8, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.physic(mass: 0.2, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .kinematic)
.position(x: -1.0, y: 0.2, z: 0.0)

CAD()
.name("BSplineTube")
.mesh(commands: [
    "DEF Tube = PATH_FORMULA 0,0,0 X (x-0.0)^2+(y-0.0)^2=0.1^2 EXT_BSpline (2.5,1,0),(2,1,0),(1.5,0.4,0),(1,0.2,0),(0.5,0,0),(0,0,0) SEG 48 FILLET 0.02"
])
.material(red: 0.2, green: 0.6, blue: 0.8, opacity: 1, roughness: 0.3, metallic: 0.5)
.physic(mass: 0.5, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .kinematic)
.position(x: -1.0, y: 0.2, z: -0.5)

CAD()
.name("BSplineRoundedSquare")
.mesh(commands: [
    "DEF RoundedSquare = PATH_FORMULA 0,0,0 X ((x-0.0)^4+(y-0.0)^4-0.5*(x-0.0)^2*(y-0.0)^2-0.0002)=0 0.35 48 EXT_BSpline (1.5,0.6,0),(1,0.6,0),(0.5,0.2,0),(0,0,0) SEG 48 FILLET 0.02"
])
.material(red: 0.9, green: 0.7, blue: 0.2, opacity: 1, roughness: 0.4, metallic: 0.6)
.physic(mass: 0.4, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .kinematic)
.position(x: -1.0, y: 0.2, z: -1.0)

CAD()
.name("BSplineSquare")
.mesh(commands: [
    "DEF Square = PATH 0,0,0 Y 0.1,0.1 -0.1,0.1 -0.1,-0.1 0.1,-0.1 EXT_BSpline (1.5,0.6,0),(1,0.6,0),(0.5,0.2,0),(0,0,0) DEG 3 SEG 32 FILLET 0.02"
])
.material(red: 0.9, green: 0.5, blue: 0.2, opacity: 1, roughness: 0.4, metallic: 0.6)
.physic(mass: 0.4, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .kinematic)
.position(x: -1.0, y: 0.2, z: -1.5)

```
