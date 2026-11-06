# PATH

Creates a closed 2D polygon profile from a sequence of vertex points, then extrudes it along the profile normal to form a solid. The first three numbers `x,y,z` specify the base position; the next token (`X`, `Y`, or `Z`) sets the normal direction of the profile plane; each subsequent `x,y` pair defines a vertex offset in that plane. Give the vertices in **ring order** (walking around the outline once): a self-intersecting "bowtie" order (e.g. swapping the last two corners of a rectangle) makes the two cap halves wind in opposite directions, so their signed areas cancel and the solid ends up with zero volume.

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
