# Fundamental Differential Equation of the Second Law of Thermodynamics

## Formula

$$
\boxed{
dU = T\,dS - p\,dV
}
$$

where:

- $U$: internal energy
- $T$: thermodynamic temperature
- $S$: entropy
- $p$: pressure
- $V$: volume

It states: for a **reversible infinitesimal process**, the change in internal energy consists of two parts:

- $T\,dS$: the part related to heat transfer
- $-p\,dV$: the part related to volume work

## Fundamental Differential Equation of the Second Law of Thermodynamics

The **fundamental differential equation** of the second law of thermodynamics usually means the set of equations obtained by combining the first law with the second law, which describes how entropy, internal energy and volume are related in a **reversible process**. It is one of the most basic and most important differential equations in thermodynamics and is often called the **fundamental thermodynamic equation**.

---

### First Law

$$
dU = \delta Q + \delta W
$$

For a reversible process, the work done on the system by the surroundings is:

$$
\delta W = -p\,dV
$$

(because the work done by the system on the surroundings is $p\,dV$, the work done on the system by the surroundings is therefore $-p\,dV$)

### Second Law

For a reversible process:

$$
\delta Q_{\text{reversible}} = T\,dS
$$

Substituting into the first law:

$$
dU = T\,dS - p\,dV
$$

So this equation is in fact **the first law and the second law combined for a reversible process**.

---

## Significance

Why is it called the "fundamental differential equation"? Because it connects the most important state quantities in thermodynamics:

$$
U,\quad S,\quad V
$$

and moreover:

- $T$ and $p$ can be regarded as the partial derivatives of $U$ with respect to $S$ and $V$:

$$
T = \left(\frac{\partial U}{\partial S}\right)_V
$$

$$
p = -\left(\frac{\partial U}{\partial V}\right)_S
$$

This shows that as long as $U(S,V)$ is known, the thermodynamic properties of the system are essentially determined.

---

## Other Equivalent Fundamental Differential Equations

Through Legendre transformations, the other fundamental equations can be obtained.

- Enthalpy $H = U + pV$

$$
\boxed{dH = T\,dS + V\,dp}
$$

- Helmholtz free energy $F = U - TS$

$$
\boxed{dF = -S\,dT - p\,dV}
$$

- Gibbs free energy $G = H - TS$

$$
\boxed{dG = -S\,dT + V\,dp}
$$

---

## Irreversible Processes

Strictly speaking, the fundamental equations above apply to **reversible processes** or **reversible infinitesimal changes**.

For an irreversible process, the second law gives an inequality:

$$
dS \ge \frac{\delta Q}{T}
$$

Combining this with the first law:

$$
dU = \delta Q + \delta W
$$

If the work done on the system by the surroundings is still \(-p\,dV\), then:

$$
dU \le T\,dS - p\,dV
$$

that is:

$$
\boxed{dU \le T\,dS - p\,dV}
$$

The equality sign corresponds to a reversible process, the inequality sign to an irreversible process.

Similarly, for an isolated system:

$$
dS \ge 0
$$
