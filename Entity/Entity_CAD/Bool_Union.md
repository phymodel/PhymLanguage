# UNION

并集布尔：把两个已存在的 CAD 实体合并，取两者体积之和。两个操作数都必须在同一个 `commands` 数组里更早定义过。

> `DEF name = UNION entity1 entity2`

```phymodel

CAD()
.name("Union")
.mesh(commands: [
    "DEF box1 = PATH 0,0.1,0 Y 0.2,0.2 -0.2,0.2 -0.2,-0.2 0.2,-0.2 EXT 0.3 FILLET 0.0",
    "DEF cyl1 = PATH_FORMULA 0,0,0 Y (x-0.0)^2+(y-0.0)^2=0.4^2 1.2 EXT 0.2 FILLET 0.02",
    "DEF union1 = UNION box1 cyl1"
])
.material(red: 0.6, green: 0.4, blue: 0.8, opacity: 1, roughness: 0.5, metallic: 0.8)
.physic(mass: 0.5, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .kinematic)
.position(x: 0.0, y: 1.1, z: 0.0)

```
