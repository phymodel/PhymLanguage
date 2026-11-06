# Polyhedron

The five Platonic solids, all accessed through the single `Polyhedron()` entry point. Select the variant via `.mesh(polyhedron:)`:

| `polyhedron` | Solid |
|--------------|-------|
| `.tetrahedron` | Tetrahedron (4 faces) |
| `.hexahedron` | Hexahedron / Cube (6 faces) |
| `.octahedron` | Octahedron (8 faces) |
| `.dodecahedron` | Dodecahedron (12 faces) |
| `.icosahedron` | Icosahedron (20 faces) |

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
