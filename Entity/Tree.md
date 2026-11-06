# Tree

Generates a procedural 3D tree mesh. `growthProgress` controls the growth stage from sapling (0.0) to fully grown (1.0). When bound to a Slider, `growthProgress` typically maps from a draggable sphere's local Y coordinate (e.g. `sphere.y - 1.2 + 0.15` to normalise into the 0…1 range). The sphere's local Y lives in the same coordinate space as its `.position` and `dragRangeY`.

> Note: The Tree() type does not support dynamic. On iOS: tap to grab, tap again to release; device-attitude displacement is projected locally and constrained by `dragAxes` / `dragRangeY`.

```phymodel

Tree()
.name("treeProgress")
.mesh(growthProgress: 0.15)
.material(red: 0.6, green: 0.4, blue: 0.2, opacity: 1, roughness: 0.5, metallic: 0.8)
.physic(mass: 0.5, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .kinematic)
.position(x: 0.0, y: 0.0, z: 0.0)

CAD()
.name("sphere")
.mesh(commands: [
    "DEF sphere = SOLID_FORMULA 0,0,0 (x/0.05)^2+(y/0.05)^2+(z/0.05)^2-1=0",
])
.physic(mass: 0.6, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .kinematic)
.material(red: 0.67, green: 0.32, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 0.5, y: 1.2, z: 0.0)

CAD()
.name("cylinder")
.mesh(commands: [
    "DEF cyl1 = PATH_FORMULA 0,0,0 Y (x-0.0)^2+(y-0.0)^2=0.05^2 1.5 EXT 1.0 FILLET 0.04"
])
.material(red: 0.2, green: 0.6, blue: 0.8, opacity: 0.4, roughness: 0.3, metallic: 0.5)
.position(x: 0.5, y: 1.0, z: 0.0)

Behavior()
.name("slider_sphere")
.trigger{
    Slider(){
        objects: ["sphere"],
        output: ["y"],
        dragAxes: ["y"],
        dragRangeY: [1.05, 1.95]
    }
}
.actions{
    EntityMesh(1){
        objects: "treeProgress",
        growthProgress: "sphere.y - 1.2 + 0.15"
    }
}

```
