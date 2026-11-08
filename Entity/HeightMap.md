# HeightMap

用一条或多条程序化波形命令生成高度图地形网格。每条 `commands:` 项都是一层调制网格表面的波形：

| 命令 | 效果 |
|---------|--------|
| `"WATER"` | 水面似的波纹图案 |
| `"SINE"` | 单层正弦起伏 |
| `"TERRAIN"` | 分形地形图案 |

叠加多条 `"SINE"` 就得到多倍频正弦。`size:` 控制水平范围（宽、深），`thickness:` 设定最低点以下的底板厚度，`resolution:` 定义采样网格密度（越大越细）。

> 说明：HeightMap() 类型不支持 dynamic。

```phymodel

CAD()
.name("ellipsoid1")
.mesh(commands: [
    "DEF ellipsoid1 = SOLID_FORMULA 0,0,0 (x/0.1)^2+(y/0.1)^2+(z/0.1)^2-1=0",
])
.physic(mass: 0.6, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .dynamic)
.material(red: 0.67, green: 0.32, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 0.0, y: 1.5, z: 0.0)

HeightMap()
.name("heightMap_WATER")
.mesh(
    size: (2, 2), 
    thickness: 0.2, 
    resolution: (32, 32),
    commands: [
        "WATER"
    ]
)
.material(red: 0.2, green: 0.6, blue: 0.8, opacity: 1, roughness: 0.3, metallic: 0.1)
.physic(mass: 0.1, staticFriction: 0.9, dynamicFriction: 0.75, restitution: 0.22, mode: .kinematic)
.position(x: 0.0, y: 0.5, z: 0.0)

HeightMap()
.name("heightMap_multiSine")
.mesh(
    size: (2, 2), 
    thickness: 0.2, 
    resolution: (64, 64),
    commands: [
        "SINE",
        "SINE"
    ]
)
.material(red: 0.6, green: 0.3, blue: 0.2, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 2.0, y: 0.5, z: 0.0)

HeightMap()
.name("heightMap_TERRAIN")
.mesh(
    size: (2, 2), 
    thickness: 0.2, 
    resolution: (64, 64),
    commands: [
        "TERRAIN"
    ]
)
.material(red: 0.2, green: 0.6, blue: 0.8, opacity: 1, roughness: 0.3, metallic: 0.1)
.position(x: -2.0, y: 0.5, z: 0.0)

```
