# SUBTRACT

Boolean subtraction: subtracts the volume of the second entity from the first. Both operands must be defined earlier in the same `commands` array. The keyword `SUBTRACTION` is equivalent.

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
