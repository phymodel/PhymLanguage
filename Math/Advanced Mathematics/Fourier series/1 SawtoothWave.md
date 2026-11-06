# Sawtooth Wave

（傅立叶级数-锯齿波）设 $f(x)$ 是周期为 $2\pi$ 的周期函数，它在 $[-\pi,\pi]$ 上的表达式为 

$$
f(x)=\frac{1}{\pi}x,\,\,-\pi\le x<\pi.
$$

将 $f(x)$ 展开成傅立叶级数。

解：由于 $f(x)=-f(-x)$，函数是奇数(odd)，所以 

$$
a_0=a_n=0,
$$

只需算

$$
b_n=\frac{1}{\pi}\int_{-\pi}^{\pi}\frac{x}{\pi}\sin nx\,dx
$$

因为 $x$ 是奇函数，$\sin nx$ 是奇函数，奇函数乘奇函数为偶函数，被积函数 $\dfrac{x}{\pi}\sin nx$ 是偶函数，所以

$$
b_n=\frac{2}{\pi}\int_0^\pi \frac{x}{\pi}\sin nx\,dx
=\frac{2}{\pi^2}\int_0^\pi x\sin nx\,dx
$$

根据分部积分，有

$$
\int_0^\pi x\sin nx\,dx
=\left[-\frac{x\cos nx}{n}\right]_0^\pi+\frac{1}{n}\int_0^\pi \cos nx\,dx
=-\frac{\pi\cos n\pi}{n}+0
=-\frac{\pi(-1)^n}{n}
$$

所以

$$
b_n=\frac{2}{\pi^2}\left(-\frac{\pi(-1)^n}{n}\right)
=-\frac{2(-1)^n}{\pi n}
=\frac{2(-1)^{n+1}}{\pi n}
$$

也就是

$$
b_n=
\begin{cases}
\dfrac{2}{\pi n}, & n\text{ 为奇数}\\[6pt]
-\dfrac{2}{\pi n}, & n\text{ 为偶数}
\end{cases}
$$

由于 

$$
f(x)=\frac{a_0}{2}+\sum_{n=1}^{\infty}(a_n\cos\,nx+b_n\sin\,nx),\,x\in C
$$

即

$$
f(x)=\frac{2}{\pi}\sin x
-\frac{2}{2\pi}\sin 2x
+\frac{2}{3\pi}\sin 3x
-\frac{2}{4\pi}\sin 4x
+\frac{2}{5\pi}\sin 5x-\cdots
$$


## 设计交互场景

### Entity

![SawtoothWaveEntity](./1 SawtoothWaveEntity.phym)

### 触发系统

![SawtoothWaveBehavior](./1 SawtoothWaveBehavior.phym)
