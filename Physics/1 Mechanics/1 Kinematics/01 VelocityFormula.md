# Velocity Formula

## Formula

$$
\boxed{
\begin{aligned}
\text{Time interval: } &\Delta t = t_2 - t_1 \\
\text{Displacement: } &\Delta x = x_2 - x_1 \\
\text{Average velocity: } &\bar{v}=\dfrac{\Delta x}{\Delta t}
\end{aligned}
}
$$

## Instants and Time Intervals

- Instant $t$: a single moment, drawn as a point on the time axis.
- Time interval $\Delta t$: a process, drawn as a segment on the time axis; the gap between two instants is a time interval.
- Time interval formula: the time interval $\Delta t$ equals the final instant $t_2$ minus the initial instant $t_1$, that is $\Delta t = t_2 - t_1$.

- Instants:
  - **Beginning of the $n$th second:** $(n-1)\, {\rm s}$
  - **End of the $n$th second = beginning of the $(n+1)$th second:** $n\, {\rm s}$
  - **End of the first $n$ seconds:** $n\, {\rm s}$
- Time intervals:
  - **Within the $n$th second:** $\Delta t = n\,{\rm s} - (n-1)\,{\rm s} = 1\,{\rm s}$
  - **Within the $n$th $n$-second span:** $\Delta t = n\cdot n\,{\rm s} - (n-1)n\,{\rm s} = n\,{\rm s}$
  - **Within the first $n$ seconds:** $\Delta t = n\,{\rm s} - 0\,{\rm s} = n\,{\rm s}$

## Position and Displacement

- Position $x$: one location, drawn as a point on the coordinate axis.
- Displacement $\Delta x$: the directed segment from the initial position to the final position.
- Displacement formula: the displacement $\Delta x$ equals the final position $x_2$ minus the initial position $x_1$, that is $\Delta x=x_2-x_1$.
- Displacement versus distance travelled:
  - displacement: a vector, determined only by the initial and the final position, with magnitude ≤ distance travelled;
  - distance travelled: a scalar, determined by the actual path — going round a full circle back to the starting point gives distance > 0 but displacement = 0;
  - in one-way rectilinear motion the magnitude of the displacement equals the distance travelled.

- Coordinate system
  - Coordinate system: origin, positive direction, unit length, physical quantity, and the unit of the physical quantity.
  - If the difference of the two coordinates is positive, the displacement points along the positive direction of the axis.
  - If the difference of the two coordinates is negative, the displacement points along the negative direction of the axis.

## Position–Time Graph

- Position: the ordinate of a point on the $x$-$t$ graph.
- Displacement: the difference of the ordinates of two points on the $x$-$t$ graph.
- The line of an $x$-$t$ graph must be a **single-valued function** of time, that is, a particle has only one position at any instant.
- Reading the graph (for rectilinear motion):
  - a slanted straight line: uniform rectilinear motion;
  - a curve: rectilinear motion with varying velocity;
  - a line parallel to the $t$ axis: at rest;
  - the intersection of two graphs: the two bodies meet;
  - the slope: represents the velocity, and its sign represents the direction of the velocity.

## Velocity

- Definition of average velocity: $\bar{v} = \dfrac{\Delta x}{\Delta t}$.
- Definition of instantaneous velocity: $v = \displaystyle\lim_{\Delta t \to 0} \dfrac{\Delta x}{\Delta t} = \dfrac{dx}{dt}$.
- Relation between average and instantaneous velocity: $\bar v = v_{t/2}$, $\bar v = \dfrac{v_0+v}{2}$.
- Physical meaning — magnitude: describes how fast the position of a body changes.
- Physical meaning — direction: the direction of the average velocity is the direction of the displacement; the direction of the instantaneous velocity is along the tangent to the path.
- Physical meaning — vector: a change of direction is a change of velocity (in uniform circular motion the direction of the velocity changes at every instant, so there is an acceleration).
- Relativity:
  - velocity depends on the reference frame; there is no absolute velocity.
  - the same body has different velocities in different reference frames.

## Velocity–Time Graph

- Instantaneous velocity: the instantaneous velocity of a body at each instant can be shown directly by a graph.
- Average velocity: on a $v$-$t$ graph the difference of the ordinates of two points is the change of velocity $\Delta v$, and the area enclosed by the graph and the time axis is the displacement $\Delta x$; the average velocity is the displacement divided by the time.
- The line of a $v$-$t$ graph must be a **single-valued function** of time, that is, a particle has only one velocity at any instant.
- Reading the graph (for rectilinear motion):
  - uniform rectilinear motion;
  - uniformly accelerated rectilinear motion;
  - uniformly decelerated rectilinear motion;
  - uniformly accelerated rectilinear motion in the opposite direction;
  - the slope: represents the acceleration, and its sign represents the direction of the acceleration.

## Example 1

**(AI-assisted, 2026.10.16)** In a one-dimensional coordinate system a body moves from $x_1=10\text{ m}$ to $x_2=2\text{ m}$.

Find the displacement $\Delta x$.

**Given:** initial position $x_1=10\text{ m}$, final position $x_2=2\text{ m}$.

**To find:** the displacement $\Delta x$

**Figure:**

![DisplacementImage](./01 DisplacementImage.html)

**Solution:**

By the displacement formula

$\Delta x = x_2 - x_1$

Substituting the data

$\Delta x=x_2-x_1=2\,{\rm m}-10\,{\rm m}=-8\text{ m}$

**Answer:** the displacement is $-8\text{ m}$.

## Example 2

(**2024 National New Curriculum Paper, Q 2-14**) (6 points) A particle moves in a straight line. Among the following graphs describing its displacement $x$ or its velocity $v$ against time $t$, the one that may be correct is ($\qquad$).
![VelocityImage](./01 VelocityImage.html)
**Analysis:** the lines of both the $x$-$t$ graph and the $v$-$t$ graph must be **single-valued functions** of time, so:
- $\rm A$ ($x$-$t$ graph): the line folds back on its rising part, so the same instant corresponds to two positions — impossible;
- $\rm B$ ($x$-$t$ graph): after reaching its highest point the line folds back to the left, so the falling part falls in the same range of instants as the rising part, and the same instant corresponds to two positions — impossible;
- $\rm C$ ($v$-$t$ graph): the line is continuous and always runs along the positive direction of the $t$ axis (it never folds back); $v$ stays positive, so the particle always moves in the positive direction, and its speed first increases, then decreases, then increases again; by $a=\dfrac{\Delta v}{\Delta t}$ this means the acceleration is first positive, then negative, then positive, that is, the net force changes continuously — a possible motion, so C is correct;
- $\rm D$ ($v$-$t$ graph): the line folds back near its highest point, so the same instant corresponds to two velocities — impossible.

**Answer:** $\rm C$.

## Design Interactive Scene

### Entities

```phymodel


```

### Trigger System

```phymodel


```
