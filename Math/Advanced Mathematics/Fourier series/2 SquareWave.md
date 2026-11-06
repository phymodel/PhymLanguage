# Square Wave

（傅立叶级数-方波）设 $f(x)$ 是周期为 $2\pi$ 的周期函数，它在 $[-\pi,\pi]$ 上的表达式为

$$
f(x)=
\begin{cases}
-1,&-\pi\le x < 0,\\
1,&0\le x < \pi.
\end{cases}
$$

将 $f(x)$ 展开成傅立叶级数。

解：由于 $f(-x)=-f(x)$（等价地 $f(2\pi-x)=-f(x)$），函数是奇函数(odd)，所以

$$
a_0=a_n=0,
$$

只需算

$$
b_n=\frac{1}{\pi}\int_{-\pi}^{\pi}f(x)\sin nx\,{\rm d}x
$$

因为 $f(x)$ 是奇函数，$\sin nx$ 是奇函数，奇函数乘奇函数为偶函数，被积函数 $f(x)\sin nx$ 是偶函数，所以

$$
b_n=\frac{2}{\pi}\int_0^\pi f(x)\sin nx\,{\rm d}x=\frac{2}{\pi}\int_0^\pi 1\cdot\sin nx\,{\rm d}x
=\frac{2}{\pi}\left[-\frac{\cos nx}{n}\right]_0^\pi
=\frac{2}{n\pi}\bigl(1-\cos n\pi\bigr)
=\frac{2}{n\pi}\bigl(1-(-1)^n\bigr)
$$

（这一步只是基本积分公式 $\int\sin nx\,{\rm d}x=-\dfrac{\cos nx}{n}$，**不需要分部积分** —— 方波的被积函数是"常数 × $\sin nx$"；只有当被积函数里出现 $x\sin nx$ 时才需要分部积分，例如锯齿波和三角波。）

也就是

$$
b_n=
\begin{cases}
\dfrac{4}{n\pi}, & n\text{ 为奇数}\\[6pt]
0, & n\text{ 为偶数}
\end{cases}
$$

令 $n=2k-1$，即 $b_{2k-1}=\dfrac{4}{(2k-1)\pi}$。由于

$$
f(x)=\frac{a_0}{2}+\sum_{n=1}^{\infty}(a_n\cos\,nx+b_n\sin\,nx),\,x\in C
$$

即

$$
f(x)=\frac{4}{\pi}\sin x+\frac{4}{3\pi}\sin 3x+\frac{4}{5\pi}\sin 5x+\cdots+\frac{4}{(2k-1)\pi}\sin(2k-1)x+\cdots
$$

几点观察：

- 偶次谐波**整体缺席**（$b_2=b_4=\cdots=0$）：只保留 $1,3,5,7,\cdots$ 次项，这正是 $1-(-1)^n$ 的直接结果。
- 系数按 $1/n$ 衰减，与锯齿波同阶，收敛较慢；跳变越"硬"，高频项就越多。
- 在间断点 $x=0,\pm\pi$ 处级数收敛到左右极限的平均值 $\dfrac{-1+1}{2}=0$，这些点不在 $C$ 中 —— 所以 $C$ 只是"连续点集"。
- 跳变附近出现 **Gibbs 现象**：任意有限项部分和在跳变处都会过冲约 9%，动画里看 4 项部分和的"方角"，这个毛刺很明显。

## 设计交互场景

- 实体：3D场景所需的实体。
- 触发系统：3D场景交互所需的触发系统。

### 实体

![SquareWaveEntity](./2 SquareWaveEntity.phym)

### 触发系统

![SquareWaveBehavior](./2 SquareWaveBehavior.phym)
