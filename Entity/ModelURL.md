# ModelURL

Loads a 3D model from a `.usdz` file **shipped with the scene document**. `.mesh(urlPath:)` takes the path relative to the `.md` that contains this block — same convention as `.material(imagePath:)` and `Latex(textPath:)` (`./` optional, `..` normalized, escaping the document library root is rejected). `.playAnimation(play:loop:)` starts/stops the model's embedded animation with optional looping. `.gesture(...)` declares what the loaded model can do — **removed**, tapping / dragging is now declared by triggers (a `Tap` behavior naming it makes it tappable, a `Slider` behavior naming it makes it draggable). Physics from `.physic(...)` is unaffected. `.material(...)` does **not** apply to the loaded model — it keeps its own `UsdPreviewSurface` materials.

> Note: The ModelURL() type does not support dynamic.

```phymodel

ModelURL()
.name("Anime_fox_girl")
.mesh(urlPath: "./Anime_fox_girl.usdz")
.playAnimation(play: true, loop: false)
.physic(mass: 0.1, staticFriction: 0.9, dynamicFriction: 0.75, restitution: 0.22, mode: .kinematic)
.material(red: 1.0, green: 1.0, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8 )
.position(x: 0.5, y: 0.0, z: 0.0)

```
