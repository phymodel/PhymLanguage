# Newton's Second Law

## Formula

$$
\boxed{
\vec{F}=m\vec{a}
}
$$

## The Three Laws
- Newton's first law: every body keeps its state of uniform rectilinear motion, or its state of rest, unless a force acting on it compels it to change that state. This is Newton's first law.
- Newton's second law: the magnitude of a body's acceleration is directly proportional to the force acting on it and inversely proportional to its mass, and the direction of the acceleration is the same as the direction of the force. Its expression is $\vec{F}=m\vec{a}$.
- Newton's third law: the action and reaction forces between two bodies are always equal in magnitude, opposite in direction, and act along the same straight line.

## Newton's Second Law

- SI unit: the newton, symbol $\rm N$.
- In $F=kma$ the value of $k$ depends on the units chosen for $F$, $m$ and $a$; if all three are taken in SI units then exactly $k=1$.
- When $k=1$, a body of mass $m=1\,\rm kg$ under a force $F=1\rm N$ acquires an acceleration $a=1\,\rm m/s^2$, that is, $\begin{cases}1\,{\rm N}=1\,{\rm kg\cdot m/s^2},\\F=ma.\end{cases}$
- With all three quantities in SI units, Newton's second law reads: $F=ma$.
- **Expression for the acceleration**: $\vec{a} = \dfrac{\vec{F}_{\text{net}}}{m}$.

## Force and Motion

- From the forces to the motion: given the forces acting on a body, Newton's second law gives its acceleration, and the kinematic laws then give its state of motion.
- From the motion to the forces: given the state of motion of a body, the kinematic laws give its acceleration, and Newton's second law then gives the force acting on it.

$$
\begin{matrix}
\text{Force}\\
\text{analysis}
\end{matrix}
{
\color{red}
\Longleftrightarrow
}
F=ma
{
\color{red}
\Longleftrightarrow
}
a
{
\color{red}
\Longleftrightarrow
}
\begin{cases}
v=v_0+at\\
x=v_0t+\frac{1}{2}at^2\\
v^2-v_0^2=2ax
\end{cases}
{
\color{red}
\Longleftrightarrow
}
\begin{matrix}
\text{Motion}\\
\text{state}
\end{matrix}
$$

## Example 1

(**2024 National Paper A, Q 2-15**) (6 points) As shown in the figure, a light string passes over a smooth fixed pulley. One end of the string is tied to a block $P$ placed on a horizontal table, and there is friction between $P$ and the table; the other end hangs a light pan (of negligible mass) with weights placed in it. The total mass $m$ of the weights in the pan is varied, and the magnitude $a$ of the acceleration of $P$ is measured, giving the $a$–$m$ graph. The magnitude of the gravitational acceleration is $g$. Among the following $a$–$m$ graphs, the one that may be correct is ($\qquad$).

![example1.html](./01 example1.html)

**Analysis:**
Let the mass of the block be $\rm M$ and the tension in the string be $F_f$. By Newton's second law,

$$
\begin{cases}mg-F_T=ma,\\F_T-\mu Mg=Ma,\end{cases}
$$

which gives

$$
a=\dfrac{mg}{M+m}-\dfrac{\mu Mg}{M+m}.
$$

Hence $a$ is not a linear function of $m$, so $\rm A$ and $\rm C$ are wrong; when $a=0$, $m=\mu M$, so $\rm D$ is correct and $\rm B$ is wrong.
**Answer:** $\rm D$.
**Formula:** Newton's second law $F=ma$.

## Example 2

(**2023 National Paper A, Q 2-19**) (Multiple choice) (6 points) A horizontal pulling force makes two objects of mass $m_\text{P}$ and $m_\text{Q}$ respectively start from rest on a horizontal table and move along a straight line, and the coefficients of kinetic friction between the two objects and the table are $\mu_\text{P}$ and $\mu_\text{Q}$ respectively. After the two objects $P$ and $Q$ start moving, the relation between the pulling force $F$ they experience and their acceleration $a$ is shown in the figure. From the figure we know ($\qquad$).

![example2.html](./01 example2.html)

| ${\rm A.}\,m_\text{P}<m_\text{Q}$ | ${\rm B.}\,m_\text{P}>m_\text{Q}$ | ${\rm C.}\,\mu_\text{P}<\mu_\text{Q}$ | ${\rm D.}\,\mu_\text{P}>\mu_\text{Q}$ |
|:-----:|:-----:|:-----:|:-----:|

**Analysis:**
By Newton's second law,

$$
F-\mu mg=ma,
$$

that is,

$$
F=ma+\mu mg,
$$

where the slope is $m$, so

$$
m_\text{P}>m_\text{Q}.
$$

The intercept is $\mu mg$, so the kinetic friction $\mu mg$ of $P$ and of $Q$ are equal, and since $m_\text{P}>m_\text{Q}$ we have

$$
\mu_\text{P}<\mu_\text{Q}.
$$

Therefore B and C are correct.
**Answer:** $\rm BC$.
**Formula:** Newton's second law $F=ma$.

## Example 3

(**2022 National Paper A, Q 2-19**) (Multiple choice) (6 points) As shown in the figure, two blocks $P$ and $Q$ of equal mass are placed on a horizontal table and connected horizontally by a light spring; the coefficient of kinetic friction between each block and the table is $\mu$. The magnitude of the gravitational acceleration is $g$. A horizontal pulling force $F$ to the right pulls $P$, so that both blocks move at constant velocity; at a certain moment this pulling force is suddenly removed. Then from that moment until the spring first returns to its natural length ($\qquad$).

![example3.html](./01 example3.html)

${\rm A.}\,P$ the maximum magnitude of the acceleration of $P$ is $2\mu g$
${\rm B.}\,Q$ the maximum magnitude of the acceleration of $Q$ is $2\mu g$
${\rm C.}$ the magnitude of the displacement of $P$ is certainly greater than that of $Q$
${\rm D.}$ the speed of $P$ is never greater than the speed of $Q$ at the same moment
**Answer:**.
**Analysis:**
While the two blocks move at constant velocity, by Newton's third law the magnitude of the pulling force is $F=2\mu mg$;
analyzing the forces on $Q$, the spring force is $F_T=\mu mg$;
at the instant the pulling force is removed the spring force is unchanged, so for block $P$, by Newton's second law, $-F_T-\mu mg=ma_p$;
combining these gives $a_P=-2\mu g$.
After the pulling force is removed, the acceleration of block $P$ keeps decreasing, so $a_{P\,\,max}=2\mu g$, hence A is correct.
After the pulling force is removed, for block $Q$ the acceleration is greatest when the spring returns to its natural length, and by Newton's second law $-\mu mg=ma_Q$, which gives $a_Q=-\mu g$, hence B is wrong.
After the pulling force is removed the distance between the two objects decreases, so the displacement of $P$ is certainly smaller in magnitude than that of $Q$, hence C is wrong.
After the pulling force is removed (the initial speeds are equal), for P: $2\mu g\to \mu g$, the acceleration decreases; for Q: $0\to \mu g$, the acceleration increases, hence D is correct.
Therefore $\rm AD$ is chosen.
**Formulas:** kinetic friction $F_f=\mu F_N$; Newton's second law $F=ma$.

## Example 4

(**2021 National Paper A, Q 2-14**) As shown in the figure, the lower end of a smooth long board is placed against the stop $P$ on the horizontal base of an iron stand, and the upper part rests on a crossbar. The position of the crossbar can be adjusted on the vertical rod, so that the angle $\theta$ between the board and the base is variable. A small block is released from rest at the point $Q$ where the board meets the vertical rod, and the time $t$ the block takes to slide along the board from $Q$ to $P$ depends on the angle $\theta$. If $\theta$ is gradually increased from $30^\circ$ to $60^\circ$, the sliding time $t$ of the block will ($\qquad$).

![example4.html](./01 example4.html)

| A. gradually increase | B. gradually decrease | C. first increase then decrease | D. first decrease then increase |
|:-----:|:-----:|:-----:|:-----:|

**Answer:** $\rm D$.
**Analysis:**
Let the horizontal distance from the lower end $P$ of the board to the vertical rod be $l$ (the stop is fixed, so $l$ does not change with $\theta$). By Newton's second law, $mg\sin\theta = ma$; the magnitude of the displacement of the small block sliding down the board is $x=\dfrac{l}{\cos\theta }$; by the kinematic formula, $x=\dfrac{1}{2}at^2$;
combining these gives $t=\sqrt{\dfrac{4l}{g\sin 2\theta}}$. When $\theta$ increases from $30^\circ$ to $60^\circ$, $2\theta$ increases from $60^\circ$ to $120^\circ$, so $\sin 2\theta$ first increases then decreases (it is greatest at $2\theta=90^\circ$, i.e. $\theta=45^\circ$); hence $t$ first decreases then increases. $\rm D$ is correct.
**Formulas:** displacement–time relation $x=v_0t+\dfrac{1}{2}at^2$; Newton's second law $F=ma$.

## Example 5

(**2021 National Paper A, Q 3-22**) To measure the coefficient of kinetic friction between a small copper block and a tile surface, a student places one end of a tile with a ruler attached on a horizontal table, forming an incline of angle $\alpha$ (given $\sin\alpha=0.34$, $\cos\alpha=0.94$), and the small copper block can slide down the incline with acceleration, as shown in the figure.

![example5.html](./01 example5.html)

| $s_1$ | $s_2$ | $s_3$ | $s_4$ | $s_5$ |
|:-----:|:-----:|:-----:|:-----:|:-----:|
| $5.87\,\rm cm$ | $7.58\,\rm cm$ | $9.31\,\rm cm$ | $11.02\,\rm cm$ | $12.74\,\rm cm$ |

The student films the sliding process of the small copper block with a mobile phone, then analyzes the images recorded in the video, and obtains the distances $s_i(i=1,2,3,4,5)$ the block slides along the incline within $5$ consecutive equal time intervals (each interval $\Delta T=0.20\,\rm s$), as shown in the table below. From the data in the table, the magnitude of the acceleration of the small copper block sliding down the incline is ${\underline{\qquad}}\,\rm m/s^2$, and the coefficient of kinetic friction between the small copper block and the tile surface is ${\underline{\qquad}}$. (Keep $2$ significant figures in both results; take the magnitude of the gravitational acceleration as $9.80\,\rm m/s^2$)
**Analysis:**
From $\Delta x=a(\Delta T)^2$, the acceleration is $a=\dfrac{[(s_4+s_5)-(s_2+s_3)]\times 10^{-2}}{(2\Delta T)^2}\,\rm m/s^2\approx0.43\, m/s^2$.
From Newton's second law $mg\sin\alpha-\mu mg\cos\alpha=ma$, we get $\mu=0.32$.
**Answer:** $0.43$, $0.32$.
**Formulas:** successive-difference method $\Delta x=a(\Delta T)^2$; kinetic friction $F_f=\mu F_N$; Newton's second law $F=ma$.

## Example 6

(**2022 National Paper B, Q 2-15**) (6 points) As shown in the figure, the two ends of an inextensible light string are each tied to a small ball of mass $m$. Initially the whole system rests on a smooth horizontal table, and the distance between the two balls equals the length $L$ of the string. A constant horizontal force of magnitude $F$ acts on the midpoint of the string, in a direction perpendicular to the line joining the two balls. When the two balls have moved until they are a distance $\dfrac{3}{5}L$ apart, the magnitude of their acceleration is ($\qquad$).

![example6-1.html](./01 example6-1.html)

| A. $\dfrac{5F}{8m}$ | B. $\dfrac{2F}{5m}$ | C. $\dfrac{3F}{8m}$ | D. $\dfrac{3F}{10m}$ |
|:-----:|:-----:|:-----:|:-----:|

**Analysis:**
As shown in the figure

![example6-2.html](./01 example6-2.html)

we have
$$
F=2F_{\rm T}\cos\theta,
$$
$$
\sin\theta=\dfrac{\dfrac{3}{10}L}{\dfrac{1}{2}L}=\frac{3}{5},
$$
which gives
$$
F_{\rm T}=\frac{5}{8}F,
$$
by Newton's second law, $F'_{\rm T}=ma$, and by Newton's third law, $F_{\rm T}=F'_{\rm T}$, so
$$
a=\dfrac{5F}{8m}.
$$
Therefore $\rm A$ is correct.
**Answer:** $\rm A$.
**Formula:** Newton's second law $F=ma$.

## Example 7

(**2014 Shandong Province, Q 23**) (18 points) Studies show that the braking reaction time of an ordinary person (the time spent in the "reaction process" in Figure A) is $t_0=0.4\,\rm s$, but drinking alcohol lengthens the reaction time. In an experiment, a volunteer drives at a constant velocity $v_0=72\,\rm km/h$ on a horizontal test-track road after drinking a small amount of alcohol; from noticing the situation to the car stopping, the car travels a distance $L=39\,\rm m$. The curve of the displacement $x$ of the car against its velocity $v$ during the deceleration is shown in Figure B, and this process can be regarded as uniformly varying rectilinear motion. Take the magnitude of the gravitational acceleration as $g=10\,\rm m/s^2$. Find:

![example7.html](./01 example7.html)

(1) the magnitude of the acceleration of the car during the deceleration and the time it takes;
(2) how much longer the reaction time of the volunteer is than that of an ordinary person because of drinking;
(3) the ratio of the magnitude of the force the car exerts on the volunteer during the deceleration to the magnitude of the volunteer's weight.
**Answer:** (1) $8\,\rm m/s^2$, $2.5\,\rm s$; (2) $0.3\,\rm s$; (3) $\dfrac{\sqrt{41}}{5}$ ($\approx1.3$).
**Analysis:**
(1)
Given: initial velocity $v_0=72\,\rm km/h=20\,\rm m/s$, final velocity $v=0$, displacement $x=25\,\rm m$ (read from Figure B);
find: the acceleration $a$.
By the kinematic "velocity–displacement" formula $v^2-v_0^2=-2ax$, substituting the data gives $a=\dfrac{v_0^2}{2x}=\dfrac{20^2}{2\times25}\,\rm m/s^2=8\,\rm m/s^2$;
given: initial velocity $v_0=20\,\rm m/s$, acceleration $a=8\,\rm m/s^2$;
find: the time $t$.
By the kinematic "acceleration" formula $a=\dfrac{v_0-v}{t}$, substituting the data gives $t=\dfrac{v_0}{a}=\dfrac{20}{8}\,\rm s=2.5\,\rm s$.
(2)
Given: travelled distance $L=39\,\rm m$, initial velocity $v_0=20\,\rm m/s$, displacement $x=25\,\rm m$;
find: the reaction time after drinking $t_1$.
By the kinematic "velocity" formula $v=\dfrac{x}{t}$, the displacement during the reaction process is $x_{\text{re}}=L-x=39\,\rm m-25\,\rm m=14\,\rm m$, and substituting the data gives $t_1=\dfrac{x_{\text{re}}}{v_0}=\dfrac{14}{20}\,\rm s=0.7\,\rm s$;
also, the reaction time of an ordinary person is $t_0=0.4\,\rm s$, so drinking increases the reaction time of the volunteer by $\Delta t=t_1-t_0=0.7\,\rm s-0.4\,\rm s=0.3\,\rm s$.
(3)
Let the magnitude of the force the car exerts on the volunteer be $F$ and the mass of the volunteer be $m$;
by Newton's second law and the Pythagorean theorem, $F=m\sqrt{a^2+g^2}$, which gives $\dfrac{F}{mg}=\dfrac{\sqrt{a^2+g^2}}{g}=\dfrac{\sqrt{8^2+10^2}}{10}=\dfrac{\sqrt{41}}{5}\approx1.3$.
**Formulas:** velocity–displacement relation $v^2-v_0^2=2ax$; velocity formula $v=\dfrac{x}{t}$; definition of acceleration $a=\dfrac{v-v_0}{t}$; Newton's second law $F=ma$.

## Design Interactive Scene

- Entity: the entities needed by the 3D scene.
- Trigger system: the trigger system needed for interaction with the 3D scene.

### Entity

```phymodel


```

### Trigger System

```phymodel


```
