# EXT_Bezier

沿一条由四个控制点定义的三次贝塞尔曲线拉伸 2D 轮廓。与基于路径的图元（`PATH_FORMULA`、`PATH_FORMULA_XY`、`PATH`）配合，可以做出扫掠实体。控制点写成 `(x,y,z)` 三元组。`SEG` 决定沿曲线的分段数；`FILLET` 可选，把生成的边倒圆。

> `... EXT_Bezier (x1,y1,z1),(x2,y2,z2),(x3,y3,z3),(x4,y4,z4) SEG N [FILLET r]`

```phymodel

CAD()
.name("sphere")
.mesh(commands: [
    "DEF sphere = SOLID_FORMULA 0,0,0 (x/0.1)^2+(y/0.1)^2+(z/0.1)^2-1=0",
])
.physic(mass: 0.6, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .dynamic)
.material(red: 0.67, green: 0.32, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 1.2, y: 1.3, z: 0.0)

CAD()
.name("BezierConcave")
.mesh(commands: [
    "DEF concave = PATH_FORMULA_XY 0,0,0 X (6-2*sin(t))*cos(t) 2+(0.2-3*sin(t))*sin(t) 0.2 64 EXT_Bezier (2.5,1,0),(2,1,0),(1.5,0.4,0),(1,0.2,0),(0.5,0,0.5),(0,0,1) SEG 48"
])
.material(red: 0.2, green: 0.8, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.physic(mass: 0.2, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .kinematic)
.position(x: -1.0, y: 0.2, z: 0.0)

CAD()
.name("BezierTube")
.mesh(commands: [
    "DEF tube = PATH_FORMULA 0,0,0 X (x-0.0)^2+(y-0.0)^2=0.1^2 EXT_Bezier (2.5,1,0),(2,1,0),(1.5,0.4,0),(1,0.2,0),(0.5,0,0),(0,0,0) SEG 48 FILLET 0.02"
])
.material(red: 0.2, green: 0.6, blue: 0.8, opacity: 1, roughness: 0.3, metallic: 0.5)
.physic(mass: 0.5, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .kinematic)
.position(x: -1.0, y: 0.2, z: -0.5)

CAD()
.name("BezierRoundedSquare")
.mesh(commands: [
    "DEF RoundedSquare = PATH_FORMULA 0,0,0 X ((x-0.0)^4+(y-0.0)^4-0.5*(x-0.0)^2*(y-0.0)^2-0.0002)=0 0.35 48 EXT_Bezier (1.5,0.6,0),(1,0.6,0),(0.5,0.2,0),(0,0,0) SEG 48 FILLET 0.02"
])
.material(red: 0.9, green: 0.7, blue: 0.2, opacity: 1, roughness: 0.4, metallic: 0.6)
.physic(mass: 0.4, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .kinematic)
.position(x: -1.0, y: 0.2, z: -1.0)

CAD()
.name("BezierSquare")
.mesh(commands: [
    "DEF Square = PATH 0,0,0 Y 0.1,0.1 -0.1,0.1 -0.1,-0.1 0.1,-0.1 EXT_Bezier (1.5,0.6,0),(1,0.6,0),(0.5,0.2,0),(0,0,0) SEG 32 FILLET 0.02"
])
.material(red: 0.9, green: 0.5, blue: 0.2, opacity: 1, roughness: 0.4, metallic: 0.6)
.physic(mass: 0.4, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .kinematic)
.position(x: -1.0, y: 0.2, z: -1.5)
  
```
