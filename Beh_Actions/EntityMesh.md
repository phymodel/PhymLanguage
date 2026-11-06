# EntityMesh

> `EntityMesh(objects: String | [String], x?: String, y?: String, z?: String, t?: String, radius?: Float, growthProgress?: String, duration: Float = 0, ...bindings)`

## Purpose

Updates a target entity's mesh at runtime — either a `Graph()` parametric curve (`x`/`y`/`z`/`t`) or a `Tree()` growth progress (`growthProgress`). Supports animated interpolation when bindings or `growthProgress` use interval syntax with `duration > 0`.

## Parameters

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| objects | String or [String] | ✅ | — | Target entity name(s) |
| x | String | ❌ | inherit | Parametric x expression (Graph) |
| y | String | ❌ | inherit | Parametric y expression (Graph) |
| z | String | ❌ | inherit | Parametric z expression (Graph) |
| t | String | ❌ | inherit | t interval, e.g. `"[0, 2*pi]"` (Graph) |
| radius | Float | ❌ | inherit | Tube / line radius |
| growthProgress | String | ❌ | inherit | Tree growth value `"0…1"` or interval `"[0, 1]"` |
| duration | Float | ❌ | 0 | When >0 and bindings / growthProgress use interval syntax, animates interpolation over duration (seconds) |
| *bindings* | String | ❌ | — | Any extra key–value pairs become dynamic variables (e.g. `phase: "sphere.x * pi"`) |

## Constraints

- Only affects **ModelEntity** instances — `Graph()` and `Tree()` entities are supported.
- Omitted `x`/`y`/`z`/`t`/`radius`/`growthProgress` inherit from the target entity's current mesh. If a Graph entity has no `x`/`y`/`z` and none are provided, the action is a no-op.
- If the target entity has a `TreeComponent`, `growthProgress` is used; otherwise `x`/`y`/`z`/`t` apply.
- Binding values support interval syntax (e.g. `"[2*pi, 0]"`) — with `duration > 0` the value interpolates from start to end over the duration.
- Bindings can reference other entity positions via `EntityName.x` / `.y` / `.z` (commonly paired with `Slider` trigger).
- Unlike `MoveAlong`, `EntityMesh` alters the curve shape itself and does not move the entity.

## Example

### Entities

```phymodel

Graph()
.name("Sine")
.mesh(x: "10t", y: "10sin(10t)", z: "10cos(10t)", t: "[0,2*pi]")
.physic(mass: 0.7, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .kinematic)
.material(red: 0.46, green: 0.2, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 0.0, y: 1.5, z: 0.0)

Text()
.name("text_run")
.mesh(text: "Run", extrusionDepth: 0.02, fontSize: 0.1)
.physic(mass: 0.1, staticFriction: 0.9, dynamicFriction: 0.75, restitution: 0.22, mode: .kinematic)
.material(red: 0.2, green: 0.8, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: -0.2, y: 1.7, z: 0.0)

Text()
.name("text_stop")
.mesh(text: "Stop", extrusionDepth: 0.02, fontSize: 0.1)
.physic(mass: 0.1, staticFriction: 0.9, dynamicFriction: 0.75, restitution: 0.22, mode: .kinematic)
.material(red: 0.2, green: 0.8, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 0.2, y: 1.7, z: 0.0)

CAD()
.name("sphere")
.mesh(commands: [
    "DEF sphere = SOLID_FORMULA 0,0,0 (x/0.1)^2+(y/0.1)^2+(z/0.1)^2-1=0",
])
.physic(mass: 0.6, staticFriction: 0.6, dynamicFriction: 0.4, restitution: 0.2, mode: .kinematic)
.material(red: 0.67, green: 0.32, blue: 1.0, opacity: 1, roughness: 0.5, metallic: 0.8)
.position(x: 0.0, y: 1.3, z: 0.0)

```

### Trigger System — Tap (animate bindings with interval)

```phymodel

Behavior()
.name("tap_text_run")
.trigger{
    Tap(){
        objects: ["text_run"]
    }
}
.actions{
    EntityMesh(1){
        objects: "Sine",
        x: "10t",
        y: "10*(4/pi)*(sin(t+phase)+sin(3*(t+phase))/3+sin(5*(t+phase))/5)",
        z: "0",
        t: "[0,2*pi]",
        phase: "[2*pi, 0]",
        duration: 12.0
    }
    Wait(2){
        duration: 0.5
    }
    EntityMesh(3){
        objects: "Sine",
        x: "10t",
        y: "10*(4/pi)*(sin(t)+sin(3*t)/3+sin(5*t)/5)",
        z: "0",
        t: "[0,2*pi]"
    }
}

Behavior()
.name("tap_text_stop")
.trigger{
    Tap(){
        objects: ["text_stop"]
    }
}
.actions{
    EntityMesh(1){
        objects: "Sine",
        x: "10t",
        y: "10sin(10t)",
        z: "10cos(10t)",
        t: "[0,2*pi]"
    }
}

```

### Trigger System — Slider (bindings referencing another entity)

```phymodel

Behavior()
.name("slider_sphere")
.trigger{
    Slider(){
        objects: ["sphere"],
        output: ["x", "y", "z"]
    }
}
.actions{
    EntityMesh(1){
        objects: "Sine",
        x: "10t",
        y: "10*(4/pi)*(sin(t+phase)+sin(3*(t+phase))/3+sin(5*(t+phase))/5)",
        z: "0",
        t: "[0,2*pi]",
        phase: "sphere.x * pi"
    }
}

```
