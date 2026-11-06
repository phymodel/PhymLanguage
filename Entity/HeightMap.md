# HeightMap

Generates a height-mapped terrain mesh from one or more procedural waveform commands. Each `commands:` entry is a waveform layer that modulates the mesh surface:

| Command | Effect |
|---------|--------|
| `"WATER"` | Water-like rippling wave pattern |
| `"SINE"` | Single sine-wave elevation |
| `"TERRAIN"` | Fractal terrain-like pattern |

Stacking `"SINE"` entries produces multi-octave sine waves. `size:` controls the horizontal extent (width, depth), `thickness:` sets the base slab depth below the lowest point, and `resolution:` defines the sampling grid density (higher values produce finer detail).

> Note: The HeightMap() type does not support dynamic.

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
