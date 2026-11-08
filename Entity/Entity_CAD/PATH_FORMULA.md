# PATH_FORMULA

用隐式平面方程 `f(x,y)=0` 创建 2D 轮廓，再沿轮廓法线拉伸成实体。最前面三个数 `x,y,z` 给出基点；紧接的记号（`X`、`Y` 或 `Z`）定下轮廓平面的法线方向。`equation` 定义 2D 形状的轮廓（例如圆是 `(x-0)^2+(y-0)^2=0.4^2`）。`domainHalfSize` 控制原点周围的采样范围。可选的 `SECTOR [start,end]` 把轮廓限制在一个角度扇区（度）内。`EXT h` 决定拉伸高度，还可选 `FILLET`、`FILLET_H`、`FILLET_V` 做边缘倒圆。

> `DEF name = PATH_FORMULA x,y,z NORMAL equation domainHalfSize [SECTOR [start,end]] EXT h [FILLET r] [FILLET_H r] [FILLET_V r]`

```phymodel

CAD()
.name("cylinder")
.mesh(commands: [
    "DEF cyl1 = PATH_FORMULA 0,0,0 Y (x-0.0)^2+(y-0.0)^2=0.4^2 1.5 EXT 0.3 FILLET 0.02"
])
.material(red: 0.2, green: 0.6, blue: 0.8, opacity: 1, roughness: 0.3, metallic: 0.5)
.physic(mass: 0.5, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .dynamic)
.position(x: 0.0, y: 0.8, z: 0.0)

CAD()
.name("sector")
.mesh(commands: [
    "DEF sector = PATH_FORMULA 0,0,0 Z (x-0.0)^2+(y-0.0)^2=0.4^2 SECTOR [30,90] EXT -0.3"
])
.material(red: 0.2, green: 0.6, blue: 0.8, opacity: 1, roughness: 0.3, metallic: 0.5)
.physic(mass: 0.5, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .kinematic)
.position(x: 0.0, y: 1.2, z: 0.0)

```
