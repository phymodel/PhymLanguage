# PATH_OPEN

Creates an open polyline profile from a sequence of points, then revolves it around an axis to form a solid of revolution. Unlike `PATH` which produces a closed polygon and extrudes linearly, `PATH_OPEN` expects an open chain of `x,y` pairs and uses `REV` with a rotation axis and angle (in degrees).

> `DEF name = PATH_OPEN x,y,z NORMAL x1,y1 x2,y2 ... REV axis angle [SEG n]`

```phymodel

CAD()
.name("cone")
.mesh(commands: [
    "DEF cone = PATH_OPEN 0,0,0 Z 0,0.2 0.1,0 0,0 REV Y 360"
])
.material(red: 0.7, green: 0.3, blue: 0.3, opacity: 1, roughness: 0.5, metallic: 0.8)
.physic(mass: 0.5, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .dynamic)
.position(x: 0.0, y: 1.5, z: 0.0)

```
