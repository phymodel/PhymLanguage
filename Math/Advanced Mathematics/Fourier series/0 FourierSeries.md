# Fourier series

## 公式

$$
\boxed{
\begin{aligned}
a_0 &= \frac{1}{\pi}\int_{-\pi}^{\pi} f(x)\,dx \\[4pt]
a_n &= \frac{1}{\pi}\int_{-\pi}^{\pi} f(x)\cos nx\,dx \quad (n\ge 1)\\[4pt]
b_n &= \frac{1}{\pi}\int_{-\pi}^{\pi} f(x)\sin nx\,dx \quad (n\ge 1)\\[4pt]
f(x) &=\frac{a_0}{2}+\sum_{n=1}^{\infty}(a_n\cos\,nx+b_n\sin\,nx),\,x\in C
\end{aligned}
}
$$

其中 $C$ 表示连续点集 $C = \left\{ x \;\middle|\; f(x) = \dfrac{1}{2}\left[ f(x^{-}) + f(x^{+}) \right] \right\}$.

## 推导

傅立叶级数的推导，核心思想是：**用一组正交函数族 $\{1,\cos nx,\sin nx\}$ 去“逼近”周期函数 $f(x)$**，然后利用正交性把系数“投影”出来。下面给出完整推导。

---

### 1. 基本假设

设 $f(x)$ 是周期为 $2\pi$ 的函数，并且可以展开成三角级数：

$$
f(x)=\frac{a_0}{2}+\sum_{n=1}^{\infty}\left(a_n\cos nx+b_n\sin nx\right)
$$

这里写成 $\dfrac{a_0}{2}$ 而不是 $a_0$，是为了让 $a_0$ 的公式与 $a_n$ 统一，后面会看到。

---

### 2. 三角函数系的正交性

考虑函数系

$$
1,\ \cos x,\ \sin x,\ \cos 2x,\ \sin 2x,\ \dots
$$

在区间 $[-\pi,\pi]$ 上，它们满足以下正交关系：

**(1) 常数与三角函数正交**

$$
\int_{-\pi}^{\pi} 1\cdot \cos nx\,dx=0
$$

$$
\int_{-\pi}^{\pi} 1\cdot \sin nx\,dx=0
$$

**(2) 不同余弦之间正交**

$$
\int_{-\pi}^{\pi}\cos mx\cos nx\,dx=
\begin{cases}
0,& m\ne n\\[4pt]
\pi,& m=n\ne 0
\end{cases}
$$

**(3) 不同正弦之间正交**

$$
\int_{-\pi}^{\pi}\sin mx\sin nx\,dx=
\begin{cases}
0,& m\ne n\\[4pt]
\pi,& m=n\ne 0
\end{cases}
$$

**(4) 正弦与余弦正交**

$$
\int_{-\pi}^{\pi}\sin mx\cos nx\,dx=0
$$

这些都可以用积化和差公式直接验证。关键结论是：

> **不同函数相乘在 $[-\pi,\pi]$ 上积分为 0；相同函数相乘积分为 $\pi$（常数 1 与自身相乘积分为 $2\pi$）。**

这就是“正交性”。

---

### 3. 求 $a_0$

对展开式两边在 $[-\pi,\pi]$ 上积分：

$$
\int_{-\pi}^{\pi} f(x)\,dx
=
\int_{-\pi}^{\pi}\frac{a_0}{2}\,dx
+
\sum_{n=1}^{\infty}\left(
a_n\int_{-\pi}^{\pi}\cos nx\,dx
+
b_n\int_{-\pi}^{\pi}\sin nx\,dx
\right)
$$

由于

$$
\int_{-\pi}^{\pi}\cos nx\,dx=0,\qquad
\int_{-\pi}^{\pi}\sin nx\,dx=0
$$

所以右边只剩下第一项：

$$
\int_{-\pi}^{\pi} f(x)\,dx
=
\frac{a_0}{2}\cdot 2\pi
=
a_0\pi
$$

因此

$$
\boxed{a_0=\frac{1}{\pi}\int_{-\pi}^{\pi}f(x)\,dx}
$$

---

### 4. 求 $a_n$

两边乘以 $\cos nx$，再在 $[-\pi,\pi]$ 上积分：

$$
\int_{-\pi}^{\pi} f(x)\cos nx\,dx
=
\frac{a_0}{2}\int_{-\pi}^{\pi}\cos nx\,dx
+
\sum_{m=1}^{\infty}
a_m\int_{-\pi}^{\pi}\cos mx\cos nx\,dx
+
\sum_{m=1}^{\infty}
b_m\int_{-\pi}^{\pi}\sin mx\cos nx\,dx
$$

利用正交性：

- $\int_{-\pi}^{\pi}\cos nx\,dx=0$
- $\int_{-\pi}^{\pi}\sin mx\cos nx\,dx=0$
- $\int_{-\pi}^{\pi}\cos mx\cos nx\,dx=0$（当 $m\ne n$），只有 $m=n$ 时等于 $\pi$

所以右边只剩下 $a_n\pi$：

$$
\int_{-\pi}^{\pi} f(x)\cos nx\,dx=a_n\pi
$$

因此

$$
\boxed{a_n=\frac{1}{\pi}\int_{-\pi}^{\pi}f(x)\cos nx\,dx}
$$

---

### 5. 求 $b_n$

两边乘以 $\sin nx$，再积分：

$$
\int_{-\pi}^{\pi} f(x)\sin nx\,dx
=
\frac{a_0}{2}\int_{-\pi}^{\pi}\sin nx\,dx
+
\sum_{m=1}^{\infty}
a_m\int_{-\pi}^{\pi}\cos mx\sin nx\,dx
+
\sum_{m=1}^{\infty}
b_m\int_{-\pi}^{\pi}\sin mx\sin nx\,dx
$$

同理，只有 $m=n$ 的正弦项保留：

$$
\int_{-\pi}^{\pi} f(x)\sin nx\,dx=b_n\pi
$$

因此

$$
\boxed{b_n=\frac{1}{\pi}\int_{-\pi}^{\pi}f(x)\sin nx\,dx}
$$

---

### 6. 为什么连续点处等于 $f(x)$，间断点处等于左右极限平均？

上面推导的是“如果 $f$ 能展开成三角级数，系数应该怎么取”。但反过来，给定系数后得到的级数是否一定收敛到 $f(x)$？

这需要 **狄利克雷收敛定理**：

若 $f$ 在 $[-\pi,\pi]$ 上分段光滑（或满足狄利克雷条件），则它的傅立叶级数在每点收敛，并且

$$
\frac{a_0}{2}+\sum_{n=1}^{\infty}\left(a_n\cos nx+b_n\sin nx\right)
=
\frac{f(x^+)+f(x^-)}{2}
$$

- 在 $f$ 的连续点，$f(x^+)=f(x^-)=f(x)$，所以收敛到 $f(x)$；
- 在跳跃间断点，收敛到左右极限的平均值。

因此，连续点集

$$
C=\left\{x\ \middle|\ f(x)=\frac12\left[f(x^-)+f(x^+)\right]\right\}
$$

正好就是级数收敛到 $f(x)$ 的那些点。

---

### 7. 总结推导逻辑

1. **假设** $f(x)$ 可展开为三角级数；
2. **利用正交性**，分别用 $1,\cos nx,\sin nx$ 去乘并积分；
3. 所有交叉项消失，只剩下对应系数项；
4. 得到系数公式；
5. **收敛性**由狄利克雷定理保证，连续点收敛到 $f(x)$，间断点收敛到左右极限平均。

所以傅立叶级数的本质是：

> 把周期函数 $f(x)$ 投影到正交三角函数系上，投影系数就是 $a_0,a_n,b_n$。

## 设计交互场景

- 实体：3D场景所需的实体。
- 触发系统：3D场景交互所需的触发系统。

### 实体

![FourierSeriesEntity](./0 FourierSeriesEntity.phym)

### 触发系统

![FourierSeriesBehavior](./0 FourierSeriesBehavior.phym)
