# Polyhedron

五种正多面体，统一由 `Polyhedron()` 这一个入口进入。用 `.mesh(polyhedron:)` 选出具体是哪一种：

| `polyhedron` | 立体 |
|--------------|-------|
| `.tetrahedron` | 正四面体（4 面） |
| `.hexahedron` | 正六面体 / 立方体（6 面） |
| `.octahedron` | 正八面体（8 面） |
| `.dodecahedron` | 正十二面体（12 面） |
| `.icosahedron` | 正二十面体（20 面） |

```phymodel

Polyhedron()
.name("tetrahedron1")
.mesh(radius: 0.1, polyhedron: .tetrahedron)
.physic(mass: 0.1, staticFriction: 0.9, dynamicFriction: 0.75, restitution: 0.22, mode: .kinematic)
.material(red: 1.0, green: 0.4, blue: 0.2, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: -0.4, y: 1.5, z: 0.0)

Polyhedron()
.name("hexahedron1")
.mesh(radius: 0.1, polyhedron: .hexahedron)
.physic(mass: 0.1, staticFriction: 0.9, dynamicFriction: 0.75, restitution: 0.22, mode: .dynamic)
.material(red: 0.2, green: 0.8, blue: 0.3, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: -0.2, y: 1.5, z: 0.0)

Polyhedron()
.name("octahedron1")
.mesh(radius: 0.1, polyhedron: .octahedron)
.physic(mass: 0.1, staticFriction: 0.9, dynamicFriction: 0.75, restitution: 0.22, mode: .dynamic)
.material(red: 0.9, green: 0.7, blue: 0.1, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 0.0, y: 1.5, z: 0.0)

Polyhedron()
.name("dodecahedron1")
.mesh(radius: 0.1, polyhedron: .dodecahedron)
.physic(mass: 0.1, staticFriction: 0.9, dynamicFriction: 0.75, restitution: 0.22, mode: .dynamic)
.material(red: 0.6, green: 0.2, blue: 0.9, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 0.2, y: 1.5, z: 0.0)

Polyhedron()
.name("icosahedron1")
.mesh(radius: 0.1, polyhedron: .icosahedron)
.physic(mass: 0.1, staticFriction: 0.9, dynamicFriction: 0.75, restitution: 0.22, mode: .dynamic)
.material(red: 0.2, green: 0.8, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 0.4, y: 1.5, z: 0.0)

```
