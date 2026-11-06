# Velocity–Displacement Relation

## Formula

$$
\boxed{
v^2-v_0^2=2ax
}
$$

## Relation between Velocity and Displacement

- Formula $v^2-v_0^2=2ax$.
- Derivation: the displacement–time relation $x=v_0t+\dfrac{1}{2}at^2$ and the velocity–time relation $v=v_0+at$; combining the two gives the velocity–displacement relation $v^2-v_0^2=2ax$.

## Example 1

(**2008 National Paper I, Q 2-11**) (14 points) $O$, $A$, $B$ and $C$ are four points on the same straight line. The distance between $A$ and $B$ is $l_1$, and the distance between $B$ and $C$ is $l_1$. A body starts from rest at $O$ and moves along this line with uniform acceleration, passing the three points $A$, $B$ and $C$ in turn; the times the body takes to cover $AB$ and $BC$ are equal. Find the distance between $O$ and $A$.
**Analysis:**
Let the acceleration of the body be $a$, its speed on reaching $A$ be $v_0$, the time it takes to cover $AB$ be $t$, and the distance between $O$ and $A$ be $l$. From
$$
\begin{cases}
x=v_0t+\frac{1}{2}at^2,\\
v^2-v_0^2=2ax,
\end{cases}
$$
we have
$$
\begin{cases}
l_1=v_0t+\frac{1}{2}at^2,\\
l_1+l_2=v_0(2t)+\frac{1}{2}a(2t)^2,\\
l=\frac{v_0^2}{2a},
\end{cases}
$$
and solving gives
$$
l=\frac{(3l_1-l_2)^2}{8(l_2-l_1)}.
$$
**Answer:** $\dfrac{(3l_1-l_2)^2}{8(l_2-l_1)}.$
**Formulas:** displacement–time relation $x=v_0t+\dfrac{1}{2}at^2$, velocity–displacement relation $v^2-v_0^2=2ax$.


## Design Interactive Scene

- Entities: the entities required for the 3D scene.
- Trigger system: the trigger system required for the 3D scene interaction.

### Entities

```phymodel


```

### Trigger System

```phymodel


```
