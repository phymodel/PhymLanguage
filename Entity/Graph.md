# Graph

Generates a 3D parametric curve (Lissajous figure) from the coordinate expressions `x:`, `y:`, `z:` sampled over the parameter interval `t:`. The curve is meshed as a tube; the optional `radius` controls its thickness. A Lissajous figure results when the x/y components are sinusoidal with integer frequency ratios — here x = 20cos(3t), y = 20cos(4t + pi/2), z = 20sin(3t) trace a closed 3D knot-like curve over t ∈ [0, 2π].

> Note: The Graph() type does not support dynamic.
> `Graph().mesh(x: String, y: String, z: String, t: String, radius: Float?)`

```phymodel

Graph()
.name("Lissajous")
.mesh(x: "20cos(3t)", y: "20cos(4t + pi/2)", z: "20sin(3t)", t: "[0,6.2832]")
.physic(mass: 0.7, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .kinematic)
.material(red: 0.46, green: 0.2, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 0.0, y: 1.5, z: 0.0)

Graph()
.name("ProjectileCurve")
.mesh(x: "5.5t", y: "(-0.0)t+(-0.8)t^2", z: "0.0", t: "[0,8]")
.physic(mass: 0.7, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .kinematic)
.material(red: 0.46, green: 0.2, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: -1.0, y: 1.7, z: 0.0)

Graph()
.name("Sine")
.mesh(x: "10t", y: "10sin(10t)", z: "10cos(10t)", t: "[0,6.2832]", radius: 0.005)
.physic(mass: 0.7, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .kinematic)
.material(red: 0.46, green: 0.2, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 0.5, y: 1.5, z: 0.0)

```
