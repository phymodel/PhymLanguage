# SOLID_FORMULA

Generates a solid directly from an implicit 3D surface equation `f(x,y,z)=0`. The isosurface is meshed using marching cubes. The optional `domainHalfSize` (default 0.5) and `resolution` (default 30) control mesh bounds and grid density. The keyword `INSIDE` inverts the fill to mesh the interior of the surface.

> `DEF name = SOLID_FORMULA x,y,z equation [domainHalfSize] [resolution] [INSIDE]`

The last example (a `skybox` from inside a sphere) takes its texture from `./black-and-white.png` next to this document: `.material(imagePath: "…")` resolves **relative to the directory of the current `.md` scene**, so the image travels with the document — no image host, no CORS, works offline. This is the **only** texture channel: the remote `imageURL:` form has been removed (a remote texture needs CORS on the Web and is often unreachable anyway — ship the image with the document instead), and writing it now reports an error instead of being silently ignored.

`INSIDE` surfaces are only visible **from inside**, so the skybox must enclose the viewer: this one is 3 m in radius, which leaves both the headset scene (origin) and the Web editor's camera (eye height 1.7 m, 2 m out) inside it. A 1 m sphere would sit below that camera's view cone and look like nothing rendered at all.

![black-and-white](./black-and-white.png)

```phymodel

CAD()
.name("sphere")
.mesh(commands: [
    "DEF sphere = SOLID_FORMULA 0,0,0 (x/0.1)^2+(y/0.1)^2+(z/0.1)^2-1=0",
])
.physic(mass: 0.6, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .dynamic)
.material(red: 0.67, green: 0.32, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 0.5, y: 1.5, z: 0.0)

CAD()
.name("ellipsoid")
.mesh(commands: [
    "DEF ellipsoid = SOLID_FORMULA 0,0,0 (x/0.2)^2+(y/0.1)^2+(z/0.1)^2-1=0",
])
.physic(mass: 0.6, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .dynamic)
.material(red: 0.67, green: 0.32, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: -0.5, y: 1.5, z: 0.0)

CAD()
.name("superquadric")
.mesh(commands: [
    "DEF superquadric = SOLID_FORMULA 0,0,0 (x/0.15)^4+(y/0.15)^4+(z/0.15)^4-1=0 0.5 40",
])
.physic(mass: 0.6, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .dynamic)
.material(red: 0.67, green: 0.32, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 0.0, y: 1.5, z: 0.0)

CAD()
.name("torus")
.mesh(commands: [
    "DEF torus = SOLID_FORMULA 0,0,0 (x^2+z^2+y^2+0.15^2-0.05^2)^2-4*0.15^2*(x^2+z^2)=0 0.25 48",
])
.physic(mass: 0.3, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .dynamic)
.material(red: 0.8, green: 0.2, blue: 0.4, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 0.0, y: 1.0, z: 0.0)

CAD()
.name("skybox")
.mesh(commands: [
    "DEF skybox = SOLID_FORMULA 0,0,0 (x/10)^2+(y/10)^2+(z/10)^2-1=0 INSIDE",
])
.physic(mass: 0.6, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .kinematic)
.material(red: 1.00, green: 1.00, blue: 1.00, opacity: 1, roughness: 0.5, metallic: 0.8, imagePath: "./black-and-white.png")
.position(x: 0.0, y: 0.0, z: 0.0)

```
