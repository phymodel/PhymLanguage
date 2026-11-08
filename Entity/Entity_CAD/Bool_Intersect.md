# INTERSECT

交集布尔：保留两个已存在 CAD 实体的公共体积，其余丢掉。两个操作数都必须在同一个 `commands` 数组里更早定义过。关键字 `INTERSECTION` 等价。

> `DEF name = INTERSECT entity1 entity2`

```phymodel

CAD()
.name("Intersect")
.mesh(commands: [
    "DEF box1 = PATH 0,0,0 Y 0.3,0.5 -0.3,0.5 -0.3,-0.5 0.3,-0.5 EXT 0.2",
    "DEF cyl1 = PATH_FORMULA 0,0,0 Y (x-0.0)^2+(y-0.0)^2=0.5^2 1.5 EXT 0.8",
    "DEF intersect1 = INTERSECT box1 cyl1"
])
.material(red: 0.2, green: 0.6, blue: 0.8, opacity: 1, roughness: 0.3, metallic: 0.5)
.physic(mass: 0.5, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .kinematic)
.position(x: 0.0, y: 1.1, z: 0.0)

```
