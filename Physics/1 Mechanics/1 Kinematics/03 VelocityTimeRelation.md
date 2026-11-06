# Velocity–Time Relation

## Formula

$$
\boxed{
v=v_0+at
}
$$

## Relation between Velocity and Time

- Algebraic method: since $a=\dfrac{\Delta v}{\Delta t}=\dfrac{v_2-v_1}t$, we have $v=v_0+at$.
- Graphical method: since $y=kx+b$, we have $v=v_0+at$.
- Condition of applicability: uniformly accelerated rectilinear motion.

## Ratios

When $v_0 = 0$,
$$
v=at
$$
Taking successive equal time intervals $t$,
$$
v_1:v_2:v_3:\cdots:v_n=1:2:3:\cdots:n
$$

## Example 1

(**2022 National Paper A, Q 2-15**) (6 points) A high-speed train of length $l$ runs at a normal speed $v_0$ on a straight level track and is about to pass through a tunnel of length $L$ ahead. While any part of the train is inside the tunnel, the speed of the train may not exceed $v\ (v<v_0)$. The magnitudes of the acceleration and of the deceleration of the train are $a$ and $2a$ respectively. Then the time the train needs, at least, from the moment it starts to decelerate until it is back at its normal speed is ($\qquad$).

$\rm A$. $\dfrac{v_0-v}{2a}+\dfrac{L+l}{v}$
$\rm B$. $\dfrac{v_0-v}{a}+\dfrac{L+2l}{v}$
$\rm C$. $\dfrac{3(v_0-v)}{2a}+\dfrac{L+l}{v}$
$\rm D$. $\dfrac{3(v_0-v)}{a}+\dfrac{L+2l}{v}$

**Figure:**

![VelocityTime](./03 VelocityTime.html)

**Analysis:**
The deceleration time is $t_1=\dfrac{v-v_0}{-2a}$,
the time inside the tunnel is $t_2=\dfrac{L+l}{v}$,
the acceleration time is $t_3=\dfrac{v_0-v}{a}$,
so the least total time is $t=t_1+t_2+t_3=\dfrac{3(v_0-v)}{2a}+\dfrac{L+l}{v}$, and $\rm C$ is correct.

**Answer:** $\rm C$.

**Formulas:** velocity formula $v=\dfrac{\Delta x}{\Delta t}$; velocity–time relation $v=v_0+at$.

## Design Interactive Scene

### Entities

```phymodel


```

### Trigger System

```phymodel


```
