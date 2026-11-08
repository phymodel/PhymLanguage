# 六方最密堆积（Hexagonal Close-Packing, 简称 HCP）

## HCP Unit Cell (Lattice)

- HCP Unit Cell: 
- HCP Unit Cell (Lattice): 

## Coordination Number

A single atom is directly connected to 
 (i). 6 corner atoms
 (ii). 3+3=6 middle layer atoms
 Coordination Number = 6 + 6 = 12

## Corner Atom Division in HCP

$\dfrac{1}{2}$ of an atom

$\dfrac{1}{2}\times\dfrac{1}{3}=\dfrac{1}{6}$ of an atom

## Number of atoms in a Unit Cell

12 Corner Atoms = $12\times\dfrac{1}{6}=2$
3 Midplane Atoms = $3\times1=3$
2 Face Center Atoms = $2\times\dfrac{1}{2}=1$
Total Atoms = 2 + 3 + 1 = 6

## 例1: 证理想六方密堆结构中 $\dfrac{c}{a} \approx 1.633$

解析：由于 $AO=\dfrac{c}2$, $BC=a$, 且图形 $ABCD$ 为正四面体，有

![ca](./HCP_ca.html)

$$
\begin{aligned}
|AO|^2+|BO|^2&=|AB|^2\\
|BF|^2+|CF|^2&=|BC|^2\\
|BO|&=\dfrac{2}{3}|BF|
\end{aligned}
$$

计算，得

$$
c=\dfrac{2\sqrt{6}}{3}a,
$$

所以

$$
\therefore \dfrac{c}{a}\approx1.633.
$$

---

## 例2: 计算理想六方密堆结构的原子空间利用率.

解析：由例1，知 

![utilization](./HCP_utilization.html)

$$
AO=\frac{c}{2}=\frac{\sqrt{6}}{3}a, BF=\frac{\sqrt{3}}{2}a.
$$

由“总原子数目：2+1+3=6”,
所以 

$$
V_a=\frac{4}{3}\pi\left(\dfrac{a}{2}\right)^3\times6=\pi a^3,
$$

六方体积：

$$
V=\frac{1}{2}\times\frac{\sqrt{3}}{2}a\times a\times6\times\frac{2\times\sqrt{6}}{3}a=3\sqrt2 a^3,
$$

故：

$$
\frac{V_a}{V}\times 100\%\approx74.05\%.
$$