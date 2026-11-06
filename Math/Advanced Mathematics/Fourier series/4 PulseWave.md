# Pulse Wave

（傅立叶级数-脉冲波）设 $f(x)$ 是周期为 $2\pi$ 的周期函数，它在 $[-\pi,\pi]$ 上是一个宽度 $\varepsilon$、高度 $1/\varepsilon$ 的窄矩形脉冲：

$$
f(x)=
\begin{cases}
\dfrac{1}{\varepsilon},&|x|<\dfrac{\varepsilon}{2},\\[6pt]
0,&\text{其他}.
\end{cases}
$$

（高度取 $1/\varepsilon$ 是为了让脉冲**面积恒等于 1**：$\int_{-\pi}^{\pi}f\,{\rm d}x=1$。$\varepsilon\to0$ 时它趋于 $\delta$ 函数。）

将 $f(x)$ 展开成傅立叶级数。

解：矩形脉冲是**偶函数**，所以 $b_n=0$，只需算 $a_0$ 和 $a_n$。

$$
a_0=\frac{1}{\pi}\int_{-\pi}^{\pi}f(x)\,{\rm d}x=\frac{1}{\pi}\cdot 1=\frac{1}{\pi}
$$

$$
a_n=\frac{1}{\pi}\int_{-\pi}^{\pi}f(x)\cos nx\,{\rm d}x
=\frac{2}{\pi}\int_0^{\varepsilon/2}\frac{1}{\varepsilon}\cos nx\,{\rm d}x
=\frac{2}{n\pi\varepsilon}\sin\frac{n\varepsilon}{2},\qquad n\ge1
$$

把它写成"包络 × 抽样函数"的形式更清楚：

$$
a_n=\frac{1}{\pi}\cdot\frac{\sin\frac{n\varepsilon}{2}}{\frac{n\varepsilon}{2}}
$$

由于

$$
f(x)=\frac{a_0}{2}+\sum_{n=1}^{\infty}(a_n\cos\,nx+b_n\sin\,nx),\,x\in C
$$

即

$$
f(x)=\frac{1}{2\pi}+\frac{1}{\pi}\sum_{n=1}^{\infty}\frac{\sin\frac{n\varepsilon}{2}}{\frac{n\varepsilon}{2}}\cos nx
$$

**关键一步：让 $\varepsilon\to0$。** 对任意固定的 $n$，由 $\lim\limits_{t\to0}\dfrac{\sin t}{t}=1$ 得

$$
a_n\longrightarrow\frac{1}{\pi}\qquad(n=1,2,3,\cdots)
$$

也就是**所有谐波的权重都趋于同一个值 $1/\pi$** —— 这就是**等幅谱**。

- 对比：方波、锯齿波的系数按 $1/n$ 衰减，三角波按 $1/n^2$ 衰减；脉冲**不衰减**，高低频一视同仁。
- 物理含义：**时域越窄，频域越宽**。脉冲宽 $\varepsilon$ 时，$n\lesssim 1/\varepsilon$ 的谐波权重几乎都是 $1/\pi$，一直到 $n=\dfrac{2\pi}{\varepsilon}$ 才出现第一个零点。
- 代价：$\varepsilon\to0$ 的极限对象已经**不是普通函数**（而是周期冲激串），所以级数

$$
\frac{1}{2\pi}+\frac{1}{\pi}\sum_{n=1}^{\infty}\cos nx
$$

在通常意义下处处不收敛，只能按分布意义（或只看部分和）理解。它的部分和就是狄利克雷核的一半，在 $x=0$ 附近堆出一个高度 $\approx N/\pi$ 的尖峰。

**场景画的是它的正弦（奇对称）版本。** 动画里的 8 个矢量球初始都沿 $+x$ 方向排开，矢链末端描出的是正弦级数

$$
\frac{1}{\pi}\sum_{n=1}^{\infty}\sin nx=\frac{1}{2\pi}\cot\frac{x}{2}\qquad(\text{Abel 求和 / 主值意义})
$$

它的频率成分与上面的余弦版本**完全一样**（每一项都是等幅 $1/\pi$），只是奇对称：$t\to0^{+}$ 时向上冲、$t\to2\pi^{-}$ 时向下冲，动画里 8 项部分和画出的正是这一对尖峰。（把矢量球的初始方向从 $+x$ 改成 $+y$，同一套装置画出的就是 $\sum a_n\cos nx$ 的余弦版本。）

几点观察：

- 方波只含奇次谐波；脉冲**所有次数都在**，偶次项不消失。
- 场景当前取到 $N=8$ 项（原先 4 项）：等幅谱让尖峰大致随项数成比例变高 —— 部分和峰值从 $N=4$ 的 $\approx3.23$ 涨到 $N=8$ 的 $\approx6.14$，乘显示尺度 $10/\pi$ 后即 $\approx10.3\to19.6$；项数越多峰越尖，但永远消不掉。
- 部分和永远"不平"：等幅谱意味着每一项都不衰减，所以不管取多少项，$t=0$ 附近的尖峰都留着。
- 这也是为什么短促的信号（脉冲、敲击、闪电）听起来/看起来"什么都含"：它的频谱是平的。

## 设计交互场景

- 实体：3D场景所需的实体。
- 触发系统：3D场景交互所需的触发系统。

### 实体

![PulseWaveEntity](./4 PulseWaveEntity.phym)

### 触发系统

![PulseWaveBehavior](./4 PulseWaveBehavior.phym)
