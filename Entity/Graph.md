# Graph

用坐标表达式 `x:`、`y:`、`z:` 在参数区间 `t:` 上采样，生成一条 3D 参数曲线（利萨茹图形）。曲线按管状网格化；可选的 `radius` 控制粗细。当 x/y 分量是整数频率比的正弦时，结果就是利萨茹图形 —— 这里的 x = 20cos(3t)、y = 20cos(4t + pi/2)、z = 20sin(3t)，在 t ∈ [0, 2π] 上描出一条闭合的、绳结般的三维曲线。

> 说明：Graph() 类型不支持 dynamic。
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
