# PATH_FORMULA

Creates a 2D profile from an implicit plane equation `f(x,y)=0`, then extrudes it along the profile normal to form a solid. The first three numbers `x,y,z` specify the base position; the next token (`X`, `Y`, or `Z`) sets the normal direction of the profile plane. The `equation` defines the 2D shape contour (e.g. `(x-0)^2+(y-0)^2=0.4^2` for a circle). The `domainHalfSize` controls the sampling bounds around the origin. The optional `SECTOR [start,end]` restricts the profile to an angular sector in degrees. `EXT h` drives the extrusion height, with optional `FILLET`, `FILLET_H`, and `FILLET_V` for edge rounding.

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
