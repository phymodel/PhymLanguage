# PATH

从一串顶点创建一个闭合的 2D 多边形轮廓，再沿轮廓法线拉伸成实体。最前面三个数 `x,y,z` 给出基点；紧接的记号（`X`、`Y` 或 `Z`）定下轮廓平面的法线方向；之后每个 `x,y` 对给出该平面内的顶点偏移。顶点要按**环形顺序**给（沿轮廓走一圈）：自交的「蝴蝶结」顺序（例如把矩形的最后两个角互换）会让两端封盖的绕向相反，两者的有符号面积相互抵消，实体体积就成了 0。

> `DEF name = PATH x,y,z NORMAL x1,y1 x2,y2 ... EXT h [FILLET r] [FILLET_H r] [FILLET_V r]`

```phymodel

CAD()
.name("Box")
.mesh(commands: [
    "DEF box = PATH 0,0,0 Y 0.25,0.25 -0.25,0.25 -0.25,-0.25 0.25,-0.25 EXT 0.2 FILLET 0.02",
])
.material(red: 0.2, green: 0.6, blue: 0.8, opacity: 1, roughness: 0.3, metallic: 0.5)
.physic(mass: 0.5, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .dynamic)
.position(x: 0.0, y: 1.1, z: 0.0)

CAD()
.name("Polygon")
.mesh(commands: [
    "DEF box1 = PATH 0,0,0 Y 0.25,0.25 0.0,0.3 -0.25,0.25 -0.25,-0.25 0.2,-0.4 0.4,-0.4 EXT 0.2 FILLET 0.02",
])
.material(red: 0.2, green: 0.6, blue: 0.8, opacity: 1, roughness: 0.3, metallic: 0.5)
.physic(mass: 0.5, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .kinematic)
.position(x: 0.0, y: 1.1, z: 0.0)

```
