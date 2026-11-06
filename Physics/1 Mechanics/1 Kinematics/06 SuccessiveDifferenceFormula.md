# Successive Difference Formula

## Formula

$$
\boxed{
\begin{aligned}
\text{Successive-difference displacement: } &\Delta x=aT^2 \\
\text{Successive-difference acceleration: } &a=\dfrac{( x_{4}+ x_{5}+ x_{6})-(x_{1}+ x_{2}+ x_{3})}{9T^2}
\end{aligned}
}
$$

## Successive-Difference Displacement Formula

- $x_1=v_0T+\dfrac{1}{2}aT^2$, $x_2=v_0(2T)+\dfrac{1}{2}a(2T)^2$;
- $x_{\rm I}=x_1-0$, $x_{\rm II}=x_2-x_1$;
- $\Delta x=x_{\rm II}-x_{\rm I}=aT^2$.

> The capital $T$ is used to denote an "artificially chosen equal time interval", so as to distinguish it from an arbitrary instant $t$.

## Successive-Difference Acceleration Formula

- $a=\dfrac{\Delta x}{T^2}=\dfrac{x_{n+1}-x_n}{T^2}=\dfrac{x_{n+2}-x_n}{2T^2}=\dfrac{x_{n+3}-x_n}{3T^2}=\cdots$;
- $a=\dfrac{x_m-x_n}{(m-n)T^2}$;
- $a_1=\dfrac{ x_{3}- x_{1}}{3T^2},\,\,\,\,a_2=\dfrac{ x_{4}- x_{2}}{3T^2},\,\,\,\,a_3=\dfrac{ x_{5}- x_{3}}{3T^2}$;
- $a=\dfrac{a_1+a_2+a_3}{3}=\dfrac{(x_{4}+ x_{5}+ x_{6})-(x_{1}+ x_{2}+ x_{3})}{9T^2}$.

## Example 1

(**2023 National Paper A, Q 3-23**) (10 points) A student uses the apparatus of Figure $(a)$ to investigate the relation between the average velocity and the time for a body in rectilinear motion. The left end of a small car is connected to a paper tape, and its right end is connected to some slotted weights by a thin string passing over a fixed pulley; the weights fall and drive the car, and a spark timer prints the tape. The tape and the related data obtained in one run are shown in Figure $(b)$.
(1) The time interval between two adjacent counting points in Figure $(b)$ is $0.1\,\rm s$. Taking the position of the car when $A$ was printed as the initial position, fill in the table with the displacement $\Delta x$ of the car when $B$, $C$, $D$, $E$ and $F$ were printed; the time taken by the car to cover the corresponding displacement and its average velocity are $\Delta t$ and $\bar v$ respectively. In the table, $\Delta x_{AD}=\,\underline{\qquad\qquad}\,\rm cm$, $\bar v_{AD}=\,\underline{\qquad\qquad}\,\rm cm/s$.
(2) From the data in the table, the relation between the average velocity $\bar v$ of the car and the time $\Delta t$ is obtained as shown in Figure $(c)$. Complete the experimental points in Figure $(c)$.
(3) The experiment shows that the $\bar v$–$\Delta t$ graph of the car may be regarded as a straight line, described by $\bar v=k\Delta t+b$, where $k=\,\underline{\qquad\qquad}\,\rm cm/s^2$ and $b=\,\underline{\qquad\qquad}\,\rm cm/s$. (Keep 3 significant figures for both results.)
(4) The straight line found in (3) shows that the car is in uniformly accelerated rectilinear motion; then the speed of the car when $A$ was printed is $v_A=\,\underline{\qquad\qquad}\,$, and its acceleration is $a=\,\underline{\qquad\qquad}\,$. (Express the results in terms of the letters $k$ and $b$.)
【Answer】(1) $24.00$, $80.0$; (2) see "Figure A"; (3) $71.5$, $58.7$; (4) $b$, $2k$.
【Analysis】
(1) The displacement of the segment $AD$ is $\Delta x_{AD}=(6.60+8.00+9.40)\,\rm cm=24.00\,cm$, and the average velocity of the segment $AD$ is $\bar v_{AD}=\dfrac{\Delta x_{AD}}{\Delta t_{AD}}=\dfrac{24.00}{0.3}\,\rm cm/s=80.0\,cm/s$.
(2) Complete the experimental point $(0.3\,\rm s,\,80.0\,cm/s)$, as shown in "Figure A".
(3) The straight-line fit is shown in "Figure B", with the slope $k=\dfrac{94.6-66.0}{0.5-0.1}\,\rm cm/s^2\approx71.5\,\rm cm/s^2$ and the intercept $b=58.7\,\rm cm/s$.
(4) By the displacement–time formula and the velocity formula, solving gives
【Formulas】successive difference formula $\Delta x=aT^2$.

## Example 2

(**2022 National Paper B, Q 3-22**) (5 points) A radar is used to locate a high-speed aircraft. During a period starting from a certain instant ($t=0$) the aircraft may be regarded as moving along a straight line; its position, of coordinate $x$, is measured every $1\rm s$, and the results are shown in the table below.

| $t/\text{s}$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $x/\text{m}$ | 0 | 507 | 1094 | 1759 | 2505 | 3329 | 4233 |

Answer the following questions:
(1) The data in the table show that the aircraft is approximately in uniformly accelerated motion during this period; the reason is: ${\underline{\qquad\qquad\qquad\qquad\qquad\qquad}}$;
(2) When $x=507\rm\, m$, the speed of the aircraft is $v=\underline{\qquad}\,\rm m/s$;
(3) The acceleration of the aircraft during this period is $a=\underline{\qquad}\,\rm m/s^2$ (keep 2 significant figures).
**Analysis:**
(1) From the data, $\Delta x_{01}=507\,\rm m$, $\Delta x_{12}=587\,\rm m$, $\Delta x_{23}=665\,\rm m$, $\Delta x_{34}=746\,\rm m$, $\Delta x_{45}=824\,\rm m$ and $\Delta x_{56}=904\,\rm m$. Hence the difference of the displacements within the equal time $1\,\rm s$ is a constant, about $80\,\rm m$.

(2) The instantaneous velocity is

$$
v_1=\bar v_{02}=\frac{\Delta x_{02}}{\Delta t}=547\,\rm m/s.
$$

(3) By the method of successive differences,

$$
a=\frac{(\Delta x_{56}+\Delta x_{45}+\Delta x_{34})-(\Delta x_{01}+\Delta x_{12}+\Delta x_{23}) }{9T^2}=79\,\rm m/s^2.
$$

**Answer:** (1) the difference of the displacements within equal time intervals is constant; (2) 547; (3) 79.
**Formulas:** average velocity formula $\bar v=\frac{\Delta x}{\Delta t}$; successive difference formula $\Delta x=aT^2$.

## Design Interactive Scene

- Entities: the entities required for the 3D scene.
- Trigger system: the trigger system required for the 3D scene interaction.

### Entities

```phymodel


```

### Trigger System

```phymodel


```
