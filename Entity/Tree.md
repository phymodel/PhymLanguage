# Tree

生成一棵程序化的 3D 树。`growthProgress` 控制从树苗（0.0）到长成（1.0）的生长阶段。绑到 Slider 上时，`growthProgress` 通常取自一颗可拖动球体的局部 Y 坐标（例如 `sphere.y - 1.2 + 0.15`，把值归一到 0…1）。球体的局部 Y 与它的 `.position`、`dragRangeY` 在同一个坐标空间里。

> 说明：Tree() 类型不支持 dynamic。iOS 上：点一下抓取、再点一下放开；设备姿态位移会投影到局部坐标，并受 `dragAxes` / `dragRangeY` 约束。

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
