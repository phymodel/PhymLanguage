# Triangle Wave

（傅立叶级数-三角波）设 $f(x)$ 是周期为 $2\pi$ 的周期函数，它在 $[-\pi,\pi]$ 上是一个峰值 $\pm1$、峰位在 $x=\pm\dfrac{\pi}{2}$ 的三角波：

$$
f(x)=
\begin{cases}
-2-\dfrac{2}{\pi}x, & -\pi\le x<-\dfrac{\pi}{2},\\[6pt]
\dfrac{2}{\pi}x, & -\dfrac{\pi}{2}\le x<\dfrac{\pi}{2},\\[6pt]
2-\dfrac{2}{\pi}x, & \dfrac{\pi}{2}\le x<\pi.
\end{cases}
$$

（$f(\pi/2)=1$，$f(0)=f(\pm\pi)=0$，且 $f(-x)=-f(x)$。）将 $f(x)$ 展开成傅立叶级数。

解：由于 $f(-x)=-f(x)$，函数是奇函数(odd)，所以

$$
a_0=a_n=0,
$$

只需算

$$
b_n=\frac{1}{\pi}\int_{-\pi}^{\pi}f(x)\sin nx\,{\rm d}x
$$

被积函数 $f(x)\sin nx$ 是偶函数（奇函数 × 奇函数），所以只算 $[0,\pi]$ 上的积分再乘 2。三角波在 $[0,\pi]$ 上分两段：$[0,\pi/2]$ 上升、$[\pi/2,\pi]$ 下降，所以

$$
b_n=\frac{2}{\pi}\int_0^\pi f(x)\sin nx\,{\rm d}x
=\frac{2}{\pi}\left[\int_0^{\pi/2}\frac{2x}{\pi}\sin nx\,{\rm d}x+\int_{\pi/2}^{\pi}\left(2-\frac{2x}{\pi}\right)\sin nx\,{\rm d}x\right]
$$

两段都要**分部积分**（被积函数是 $x\sin nx$ 型）。

**第一段：**

$$
\int_0^{\pi/2}\frac{2x}{\pi}\sin nx\,{\rm d}x
=\frac{2}{\pi}\left(\left[-\frac{x\cos nx}{n}\right]_0^{\pi/2}+\frac{1}{n}\int_0^{\pi/2}\cos nx\,{\rm d}x\right)
=-\frac{\cos\frac{n\pi}{2}}{n}+\frac{2}{\pi n^2}\sin\frac{n\pi}{2}
$$

**第二段：**

$$
\int_{\pi/2}^{\pi}\sin nx\,{\rm d}x=\left[-\frac{\cos nx}{n}\right]_{\pi/2}^{\pi}=\frac{-\cos n\pi+\cos\frac{n\pi}{2}}{n}
$$

$$
\int_{\pi/2}^{\pi}x\sin nx\,{\rm d}x
=\left[-\frac{x\cos nx}{n}\right]_{\pi/2}^{\pi}+\frac{1}{n}\int_{\pi/2}^{\pi}\cos nx\,{\rm d}x
=\frac{-\pi\cos n\pi+\frac{\pi}{2}\cos\frac{n\pi}{2}}{n}-\frac{\sin\frac{n\pi}{2}}{n^2}
$$

把这两个结果代回（注意第二段带系数 $2-\frac{2x}{\pi}$）：

$$
\int_{\pi/2}^{\pi}\left(2-\frac{2x}{\pi}\right)\sin nx\,{\rm d}x
=\frac{\cos\frac{n\pi}{2}}{n}+\frac{2}{\pi n^2}\sin\frac{n\pi}{2}
$$

两段相加，含 $\cos\frac{n\pi}{2}$ 的项正好抵消：

$$
b_n=\frac{2}{\pi}\left(\frac{4}{\pi n^2}\sin\frac{n\pi}{2}\right)
=\frac{8}{\pi^2 n^2}\sin\frac{n\pi}{2}
$$

也就是

$$
b_n=
\begin{cases}
\dfrac{8(-1)^{k-1}}{\pi^2(2k-1)^2}, & n=2k-1\text{（奇数）}\\[6pt]
0, & n\text{ 为偶数}
\end{cases}
$$

由于

$$
f(x)=\frac{a_0}{2}+\sum_{n=1}^{\infty}(a_n\cos\,nx+b_n\sin\,nx),\,x\in C
$$

即

$$
f(x)=\frac{8}{\pi^2}\sin x-\frac{8}{9\pi^2}\sin 3x+\frac{8}{25\pi^2}\sin 5x-\frac{8}{49\pi^2}\sin 7x+\cdots
=\frac{8}{\pi^2}\sum_{k=1}^{\infty}\frac{(-1)^{k-1}}{(2k-1)^2}\sin(2k-1)x
$$

（自检：在峰点 $x=\dfrac{\pi}{2}$ 处，$\sin\dfrac{(2k-1)\pi}{2}=(-1)^{k-1}$，级数给出 $\dfrac{8}{\pi^2}\sum_{k\ge1}\dfrac{1}{(2k-1)^2}=\dfrac{8}{\pi^2}\cdot\dfrac{\pi^2}{8}=1=f\!\left(\dfrac{\pi}{2}\right)$，对上。）

几点观察：

- 和方波一样**只含奇次谐波**，但系数按 $1/n^2$ 衰减，比方波、锯齿波的 $1/n$ 快得多 —— 因为 $f$ 本身连续，没有跳变。
- 收敛是**绝对且一致**的：$|b_n|\le\dfrac{8}{\pi^2n^2}$，而 $\sum 1/n^2$ 收敛，由 Weierstrass 判别法即得。所以三角波本身没有 Gibbs 现象；同样的 9% 过冲出现在"跳变"处，也就是它的导数（方波）上。
- 系数正负交替 $(-1)^{k-1}$：几何上就是动画里矢量球公转方向的顺逆交替（对比方波全同向）。
- 因为 $1/n^2$ 衰减极快，动画里只取 4 项就已经很接近三角波了；而方波、锯齿波取 4 项还只是"带毛刺的斜线"。

## 设计交互场景

- 实体：3D场景所需的实体。
- 触发系统：3D场景交互所需的触发系统。

### 实体

![TriangleWaveEntity](./3 TriangleWaveEntity.phym)

### 触发系统

![TriangleWaveBehavior](./3 TriangleWaveBehavior.phym)
