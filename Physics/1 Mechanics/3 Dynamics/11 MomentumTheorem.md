# Momentum Theorem

## Formula

$$
\boxed{
\begin{aligned}
\text{Momentum: } &p=mv \\
\text{Impulse: } &I=F\Delta t \\
\text{Momentum theorem: } &I=p'-p
\end{aligned}
}
$$

## Example 1

(2019 National Paper II, Q 3-25) (20 points) A car of mass $m=2\,000\,\rm kg$ travels at a certain speed at constant velocity along a straight level road. During the journey the driver suddenly notices a warning sign $100\rm \, m$ ahead and brakes immediately. During the braking, the variation of the magnitude of the resistance on the car with time can be simplified to the curve in Figure $(\rm a)$. In Figure $(\rm a)$, the time interval $0\sim t_1$ is the reaction time from the driver noticing the warning sign to taking action (during this time the resistance on the car is neglected and the car still moves at constant velocity), $t_1=0.8\,\rm s$; the time interval $t_1\sim t_2$ is the starting time of the braking system, $t_2=1.3\,\rm s$; from the moment $t_2$ on, the braking system of the car works steadily until the car stops. It is known that from the moment $t_2$ on, the displacement of the car in the $1\,\rm s$ is $24\,\rm m$ and the displacement in the $4\,\rm s$ is $1\,\rm m$.
(1) Sketch qualitatively in Figure $(\rm b)$ the $v-t$ curve of the motion of the car from the moment the driver notices the warning sign until the braking system works steadily;
(2) find the magnitude of the velocity of the car at the moment $t_2$ and the magnitude of its acceleration at that moment;
(3) find the magnitude of the velocity of the car when it travels at constant velocity before braking and the work done by the car against the resistance during $t_1\sim t_2$; what is the approximate distance the car travels from the moment the driver notices the warning sign to the moment the car stops (replace the average velocity of the car during $t_1\sim t_2$ by the arithmetic mean of the velocities at the beginning and the end of this interval)?
![example1-1](./11 example1-1.html)
**Analysis:**
(1) The graph is as shown in the figure:
![example1-2](./11 example1-2.html)
(2) Take $\Delta t=1\rm\,s$ and suppose the car has not stopped during $t_2+3\Delta t\sim t_2+4\Delta t$; then by the kinematic formulas
$$
\begin{cases}
x_1-x_4=3a(\Delta t)^2\\
\color{NavyBlue}x_1=v_2\Delta t-\frac{1}{2}a(\Delta t)^2\\
\color{NavyBlue}v_4=v_2-4a\Delta t
\end{cases}
\,\,\,
\Rightarrow
\,\,\,
v_4=-\frac{17}{6}\rm\, m/s
$$
This shows that the car has already stopped before the moment $t_2+4\Delta t$. Since the car stops within $t_2+3\Delta t\sim t_2+4\Delta t$, the kinematic formulas give
$$
\begin{cases}
\color{NavyBlue}x_1=v_2\Delta t-\frac{1}{2}a(\Delta t)^2\\
\color{NavyBlue}v_3=v_2-3a\Delta t\\
2as_4=v_3^2
\end{cases}
\,\,\,
\Rightarrow
\,\,\,
\begin{cases}
a=8\,\rm m/s^2\\
v_2=28\,\rm m/s
\end{cases}
\text{ or }
\begin{cases}
a=\frac{288}{25}\,\rm m/s^2\\
v_2=29.76\,\rm m/s
\end{cases}
\text{ (discard }v_3>0\text{)}
$$
Therefore the magnitude of the velocity of the car at the moment $t_2$ is $28\,\rm m/s$, and the magnitude of the acceleration after that is $8\,\rm m/s^2$, in the direction opposite to the direction of motion.
(3)
$$
\begin{cases}
a=8\,\rm m/s^2,\,\,   v_2=28\,\rm m/s\\
f_1=ma\\
I=\dfrac{1}{2}f_1(t_2-t_1)\\
I=mv_1-mv_2\\
W=\dfrac{1}{2}mv_1^2-\dfrac{1}{2}mv_2^2
\end{cases}
\,
\Rightarrow
\,
\begin{cases}
v_1=30\,\rm m/s\\
W=1.16\times 10^5\rm\, J
\end{cases}
$$
$$
\begin{cases}
s_1=v_1t_1=30\times0.8\,\rm m=24\,\rm m\\
s_2=\dfrac{v_1+v_2}{2}(t_2-t_1)=\dfrac{30+28}{2}\times0.5\,\rm m=14.5\,\rm m\\
s_3=\dfrac{v_2^2}{2a}=\dfrac{28^2}{2\times8}\,\rm m=49\,\rm m
\end{cases}
\,\,\,
\Rightarrow
\,\,\,
s=s_1+s_2+s_3=87.5\,\rm m
$$
Therefore the distance the car travels from the moment the driver notices the warning sign to the moment it stops is about $87.5\,\rm m$, which is less than $100\,\rm m$: the car does not hit the warning sign.
**Formulas:** displacement–time relation $x=v_0t+\dfrac{1}{2}at^2$; Newton's second law $F=ma$; kinetic energy theorem $W=E_{\rm k2}-E_{\rm k1}$; momentum theorem $I=p'-p$.
