# Cloth

> 说明：Cloth() 类型不支持 dynamic。

```phymodel

CAD()
.name("ellipsoid1")
.mesh(commands: [
    "DEF ellipsoid1 = SOLID_FORMULA 0,0,0 (x/0.1)^2+(y/0.1)^2+(z/0.1)^2-1=0",
])
.physic(mass: 0.6, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .kinematic)
.material(red: 0.67, green: 0.32, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 0.5, y: 1.3, z: 0.0)

Cloth()
.name("skirt1")
.mesh(topRadius: 0.12, bottomRadius: 0.35, height: 0.7)
.material(red: 1.0, green: 1.0, blue: 1.0, opacity: 1, roughness: 0.3, metallic: 0.1, imagePath: "../Entity_CAD/black-and-white.png")
.physic(mass: 0.1, staticFriction: 0.9, dynamicFriction: 0.75, restitution: 0.22, mode: .kinematic)
.position(x: 0.0, y: 1.4, z: 0.0)
.simulation(wind: (0.6, 0.0, 0.4), windEnabled: false)

```
