# Displacement–Time Relation

## Formula

$$
\boxed{
x=v_0t+\dfrac{1}{2}at^2
}
$$

## Relation between Displacement and Time

- Formula $x=v_0t+\dfrac{1}{2}at^2$.
- Derivation:
  - graphical method $x=\dfrac{1}{2}(v_0+v)t$;
  - velocity–time relation $v=v_0+at$;
  - combining the two expressions above gives the displacement–time relation $x=v_0t+\dfrac{1}{2}at^2$.

## Ratio 1 (ratio of the total displacements)

When $v_0 = 0$,
$$
x=\dfrac{1}{2}at^2
$$
Taking successive equal time intervals $t$,
$$
x_1:x_2:x_3:\cdots:x_n=1:2^2:3^2:\cdots:n^2
$$

> Here $x_1:x_2:x_3:\cdots:x_n$ are the total displacements from the start of the motion within the first $t,2t,3t,…,nt$.

## Ratio 2 (ratio of the displacements within successive equal time intervals)

When $v_0 = 0$,
$$
x = \frac12 a t^2
$$

Taking successive equal time intervals, the ratio of the displacements within the 1st, 2nd, …, $n$th interval is
$$
\Delta x_1 : \Delta x_2 : \Delta x_3 : \cdots : \Delta x_n
= 1 : 3 : 5 : \cdots : (2n - 1)
$$

> Here  
> $\Delta x_1 = x_1 - 0$,  
> $\Delta x_2 = x_2 - x_1$,  
> ……,
> $\Delta x_n = x_n - x_{n-1}$,
> are the **displacements** within the 1st, 2nd, …, $n$th time interval.

## Ratio 3 (ratio of the times taken to cover successive equal displacements)

When $v_0 = 0$,

$$
x = \frac12 a t^2
$$

Divide the total displacement into $n$ equal parts, each of magnitude $x_0$.
Then the ratio of the times the body takes to cover the 1st, 2nd, …, $n$th part is

$$
t_1:t_2:t_3:\cdots:t_n
=
1:(\sqrt{2}-1):(\sqrt{3}-\sqrt{2}):\cdots:(\sqrt{n}-\sqrt{n-1})
$$

> Here  
> $t_1$ is the time taken to cover the 1st part $x_0$,  
> $t_2$ is the time taken to cover the 2nd part $x_0$,  
> $t_n$ is the time taken to cover the $n$th part $x_0$.

## Example 1

(**2024 National Paper A, Q 3-24**) (12 points) An ambulance sets off in a hurry to save a patient, sounding its siren, and moves along a straight level road from rest starting at $t=0$ with uniform acceleration of magnitude $a=2\,\rm m/s^2$. At $t_1=10\,\rm s$ it stops accelerating and moves at constant velocity. At some moment after that the siren is switched off, and at $t_2=41\,\rm s$ the person at the point where the ambulance started hears the last siren sound emitted by the ambulance. Given that the speed of sound is $v_0=340\,\rm m/s$, find:
(1) the speed of the ambulance while it moves at constant velocity;
(2) the distance from the starting point to the ambulance at the moment the siren is switched off.
**Analysis:**
(1) With acceleration $a=2\,\rm m/s^2$ and time $t_1=10\,\rm s$, the speed is $v=at_1=2\,\rm m/s^2\times 10\,\rm s=20\,\rm m/s$.
(2) Let the siren be switched off at the instant $t_0$. The distance from the starting point at that moment is $x=\dfrac{1}{2}at^2_1+v(t_0-t_1)$, and the sound takes $t_2-t_0$ to travel the distance $x$, so $x=v_0(t_2-t_0)$; solving the two equations together gives $x=680\,\rm m$.
**Answer:** (1) $20\,\rm m/s$; (2) $680\,\rm m$.
**Formulas:** displacement–time relation $x=v_0t+\dfrac{1}{2}at^2$.

## Example 2

(**2023 National Paper A, Q 2-16**) (6 points) A small car moves along a straight line: from $t=0$ it accelerates uniformly from rest until the instant $t=t_1$, then it decelerates uniformly until its speed drops to $0$ at the instant $t=t_2$. Among the following curves of the displacement $x$ of the car against the time $t$, the one that may be correct is ($\qquad$).

![example2](./04 example2.html)

**Analysis:**
$0\sim t_1$: the position coordinate of the car is $x=\frac{1}{2}a_1t^2$, so the $x$-$t$ graph is a parabola opening upwards;
$t=t_1$: here $x=x_1=v_1t_1$;
$t_1\sim t_2$: the position coordinate of the car is $x=x_1+v_1(t-t_1)+\frac{1}{2}(-a_2)(t-t_1)^2$, so the $x$-$t$ graph is a parabola opening downwards.
Hence $\rm D$ is correct.
**Answer:** $\rm D$.
**Formulas:** displacement–time relation $x=v_0t+\dfrac{1}{2}at^2$.

## Example 3

(**2014 Hainan Province**) The run of a sprinter over $100\,\rm m$ can be simplified into two stages: uniformly accelerated rectilinear motion and uniform rectilinear motion. In one race a sprinter covered the whole distance in $11.00\,\rm s$. It is known that the distance the sprinter covered within the 2nd second of the acceleration stage was $7.5\,\rm m$. Find the acceleration of the sprinter and the distance covered during the acceleration stage.

**Given:** total displacement $x=100\,\rm m$, total time $t=11.00\,\rm s$; initial velocity $v_0=0\,\rm m/s$; the motion has two stages — uniform acceleration (of duration $t_1$), then uniform velocity (of duration $t_2$); the displacement within the 2nd second of the acceleration stage is $x_{2\rm s}=7.5\,\rm m$.

**To find:** the acceleration $a$ and the distance $x_1$ covered during the acceleration stage.

**Solution:**
Since the distance covered within the 2nd second is $7.5\,\rm m$ and the time interval of that 2nd second is $t_{2\rm s}=1\,\rm s$, and since in uniformly accelerated rectilinear motion the average velocity equals the instantaneous velocity at the middle instant, the instantaneous velocity at $1.5\,\rm s$ is
$$
v_{1.5}=\bar v_{2\rm s}=\frac{x_{2\rm s}}{t_{2\rm s}}=\frac{7.5\,\rm m}{1\,\rm s}=7.5\,{\rm m/s}
$$
so the acceleration of the sprinter at $1.5\,\rm s$ is
$$
a=\frac{\Delta v}{\Delta t}=\frac{7.5\,{\rm m/s} - 0\,{\rm m/s}}{1.5\,{\rm s} - 0\,{\rm s}}=5\,{\rm m/s^2}
$$
The time of the uniform stage is
$$
t_2=t-t_1 \tag{1}
$$
The speed of the uniform stage equals the final speed of the acceleration stage:
$$
v_2=at_1 \tag{2}
$$
The total displacement is
$$
x=\frac{1}{2}a t_1^2+v_2t_2 \tag{3}
$$
The distance covered during the acceleration stage is
$$
x_1=\frac{1}{2}at_1^2 \tag{4}
$$
Combining (1)(2)(3)(4) gives
$$
x_1=10\,{\rm m}
$$

**Answer:** the acceleration of the sprinter is $5\,{\rm m/s^2}$, and the distance covered during the acceleration stage is $10\,{\rm m}$.

**Formulas:** definition of average velocity $\bar v=\dfrac{\Delta x}{\Delta t}$; definition of acceleration $a=\dfrac{\Delta v}{\Delta t}$; displacement–time relation $x=v_0t+\dfrac{1}{2}at^2$.

## Example 4

(**2013 National Syllabus Paper, Q 3-24**) (15 points) A passenger train runs at constant velocity, and its wheels produce a periodic impact at the joints between the rails. A passenger in this train measures a time interval of $10.0\,\rm s$ between the 1st and the 16th impact sound. On the parallel track next to it there is a freight train: when the passenger passes the rear of the freight train, the freight train happens to start from rest with constant acceleration in the same direction as the passenger train is moving. Within the next $20.0\,\rm s$ the passenger sees exactly $30$ freight wagons overtaken by him in succession. Each rail is $25.0\,\rm m$ long, each freight wagon is $16.0\,\rm m$ long, and the gaps between the wagons are neglected. Find:
(1) the speed of the passenger train;
(2) the acceleration of the freight train.
**Analysis:**
(1) The time interval is $\Delta t=\dfrac{10.0\,\rm s}{16-1}=\dfrac{2}{3}\,\rm s$ and the distance is $\Delta x=25.0\,\rm m$; find the speed $v$ of the passenger train; by the formula $\bar v=\dfrac{\Delta x}{\Delta t}$, substituting the data gives $\bar v=37.5\,\rm m/s$.
(2) Given the speed of the passenger train $v=37.5\,\rm m/s$ and the time $t=20.0\,\rm s$, find the displacement $x_1$ of the passenger train; by the formula $v=\dfrac{\Delta x}{\Delta t}$ we have $x_1=vt$, and substituting the data gives $x_1=750\,\rm m$.
Given the displacement of the freight train $x_2=x_1-30\times16\,\rm m=270\,\rm m$ and the time $t=20.0\,\rm s$, find the acceleration $a$ of the freight train; by the formula $x=v_0t+\dfrac{1}{2}at^2$ we have $x_2=\dfrac{1}{2}at^2$, and substituting the data gives $a=1.35\,\rm m/s^2$.
**Answer:** (1) $37.5\,\rm m/s$; (2) $1.35\,\rm m/s^2$.
**Formulas:** average velocity formula $v=\dfrac{\Delta x}{\Delta t}$; displacement–time relation $x=v_0t+\dfrac{1}{2}at^2$.

## Example 5

(**2015 Jiangsu Province, Q 1-5**) As shown in the figure, on the straight corridor of a "challenge game" there is a gate every $8\,\rm m$, and all the gates open and close in step; the opening and the closing each last $5\,\rm s$ and $2\,\rm s$ respectively. Just as the gates open, a student at gate $1$ immediately accelerates from rest to $2\,\rm m/s$ with acceleration $2\,\rm m/s^2$ and then moves forward at constant velocity. The gate that first blocks his way is ($\qquad$).

![example5](./04 example5.html)

| A. Gate 2 | B. Gate 3 | C. Gate 4 | D. Gate 5 |
|:--------:|:--------:|:--------:|:--------:|

**Analysis:**
Given the acceleration $a=2\,\rm m/s^2$, the final speed $2\,\rm m/s$ and the initial speed $0\ \rm m/s$, the formula $v=v_0+at$ gives $t=1\,\rm s$. The speed now reaches its maximum, and the displacement is $x=v_0t+\dfrac{1}{2}at^2=0+\frac{1}{2}\times 2\times(1)^2=1\,\rm m$. Hence:

(1) at $t=0$ he is at gate $1$; here $0\,{\rm s} < 5\,{\rm s}$, so the gate is open;

(2) at $t=1\,{\rm s}+\dfrac{x}{v}=1\,\rm s+\dfrac{8-1}{2}\,\rm s=4.5\,\rm s$ he is at gate $2$; here $4.5\rm \,s < 5\,\rm s$, so the gate is open;

(3) at $t=4.5\,{\rm s}+\dfrac{x}{v}=4.5\,{\rm s}+4\,{\rm s}=8.5\,\rm s$ he is at gate $3$; here $7\,\rm s < 8.5\,\rm s < 12\,\rm s$, so the gate is open;

(4) at $t=8.5\,{\rm s}+\dfrac{x}{v}=8.5\,{\rm s}+4\,{\rm s}=12.5\,\rm s$ he is at gate $4$; here $12\,\rm s < 12.5\,\rm s < 14\,\rm s$, so the gate is closed.

**Answer:** $\rm C$.
**Formulas:** velocity–time relation $v=v_0+at$; displacement–time relation $x=v_0t+\dfrac{1}{2}at^2$.

## Example 6

(**2009 Jiangsu Province, Q 2-7**) (Multiple choice) As shown in the figure, a car travelling at a constant $8\,\rm m/s$ is about to pass a junction; the green light will go out in $2\,\rm s$ and the car is $18\,\rm m$ from the stop line. The maximum acceleration of the car is $2\,\rm m/s^2$ and its maximum deceleration is $5\,\rm m/s^2$. The maximum speed allowed on this road section is $12.5\,\rm m/s$. Which of the following statements are correct? ($\qquad$)

![example6](./04 example6.html)

A. If the car accelerates uniformly immediately, it may pass the stop line before the green light goes out
B. If the car accelerates uniformly immediately, it must exceed the speed limit when it passes the stop line before the green light goes out
C. If the car decelerates uniformly immediately, it certainly cannot pass the stop line before the green light goes out
D. If the car starts to decelerate $5\,\rm m$ from the stop line, it can stop at the stop line

**Analysis:**
Let the constant speed be $v_0=8\,\rm m/s$, the acceleration $a_1=2\,\rm m/s^2$ and the deceleration $a_2=5\,\rm m/s^2$.
(1) The displacement within the remaining $t_1=2\,\rm s$ of the green light is $x=v_0t_1+\dfrac{1}{2}a_1t_1^2=20\,\rm m>18\,\rm m$, so the car can pass; A is correct.
(2) The speed of the car is $v_1=v_0+a_1t_1=12\,\rm m/s < 12.5\,\rm m/s$, so the car does not exceed the speed limit; B is wrong.
(3) The time for the speed to drop to zero is $t_2=\dfrac{v_0}{a_2}=1.6\,\rm s$, and the displacement in that process is $x_2=\dfrac{1}{2}a_2t_2^2=6.4\,\rm m < 18\,\rm m$, so C is correct.
(4) Since $x_2=6.4\,\rm m > 5\,\rm m$, D is wrong.
**Answer:** $\rm AC$.
**Formulas:** definition of acceleration $a=\dfrac{\Delta v}{\Delta t}$; displacement–time relation $x=v_0t+\dfrac{1}{2}at^2$.

## Example 7

(**2011 Anhui Province, Q 1-16**) (6 points) A body in uniformly accelerated rectilinear motion takes a time $t_1$ to cover a displacement $\Delta x$, and then a time $t_2$ to cover the next displacement $\Delta x$. Then the acceleration of the body is ($\qquad$).

| A. $\dfrac{2\Delta x(t_1-t_2)}{t_1t_2(t_1+t_2)}$ | B. $\dfrac{\Delta x(t_1-t_2)}{t_1t_2(t_1+t_2)}$ | C. $\dfrac{2\Delta x(t_1+t_2)}{t_1t_2(t_1-t_2)}$ | D. $\dfrac{\Delta x(t_1+t_2)}{t_1t_2(t_1-t_2)}$ |
|:--------:|:--------:|:--------:|:--------:|


**Analysis:**
By the laws of uniformly accelerated rectilinear motion,

$$
\begin{cases}
\Delta x=v_1t_1+\dfrac{1}{2}at_1^2,\\[1ex]
\Delta x=v_2t_2+\dfrac{1}{2}at_2^2,\\[1ex]
v_2=v_1+at_1.
\end{cases}
$$

Solving gives
$$
a=\frac{2\Delta x(t_1-t_2)}{t_1t_2(t_1+t_2)}.
$$
**Answer:** A.
**Formulas:** velocity–time relation $v=v_0+at$; displacement–time relation $x=v_0t+\dfrac{1}{2}at^2$.

## Design Interactive Scene

- Entities: the entities required for the 3D scene.
- Trigger system: the trigger system required for the 3D scene interaction.

### Entities

```phymodel


```

### Trigger System

```phymodel


```
