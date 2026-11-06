# FILLET_H

Rounds the horizontal edges (edges parallel to the extrusion direction) of an extruded solid. Applied after `EXT`, `EXT_Bezier`, or `EXT_BSpline`. The radius must be a positive number.

> `... EXT h FILLET_H r`

```phymodel

CAD()
.name("FILLET_H_box")
.mesh(commands: [
    "DEF box = PATH 0,0,0 Y 0.25,0.25 -0.25,0.25 -0.25,-0.25 0.25,-0.25 EXT 0.2 FILLET_H 0.02",
])
.material(red: 0.2, green: 0.6, blue: 0.8, opacity: 1, roughness: 0.3, metallic: 0.5)
.physic(mass: 0.5, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .dynamic)
.position(x: 0.0, y: 1.1, z: 0.0)

```