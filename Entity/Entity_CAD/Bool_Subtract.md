# SUBTRACT

减法布尔：从第一个实体的体积里减掉第二个实体的体积。两个操作数都必须在同一个 `commands` 数组里更早定义过。关键字 `SUBTRACTION` 等价。

> `DEF name = SUBTRACT entity1 entity2`

```phymodel

CAD()
.name("Subtract")
.mesh(commands: [
    "DEF box1 = PATH 0,-0.1,0 Y 0.5,0.5 -0.5,0.5 -0.5,-0.5 0.5,-0.5 EXT 0.2",
    "DEF heartShaped = PATH_FORMULA 0,0,0 Y (((x-0.0)/0.3)^2+((y-0.0)/0.3)^2-1)^3-((x-0.0)/0.3)^2*((y-0.0)/0.3)^3=0 0.9 EXT 1.5",
    "DEF subtract1 = SUBTRACT box1 heartShaped"
])
.material(red: 0.8, green: 0.9, blue: 0.3, opacity: 1, roughness: 0.4, metallic: 0.6)
.physic(mass: 0.5, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .kinematic)
.position(x: 0.0, y: 1.1, z: 0.0)

```
