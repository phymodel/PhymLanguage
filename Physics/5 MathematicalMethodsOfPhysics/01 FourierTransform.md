# Fourier Transform

## Formula

$$
\boxed{G(\omega)=F[f(x)]=\int_{-\infty}^{\infty}f(x)e^{-i\omega x}\,dx}
$$

$$
\boxed{f(x)=F^{-1}[G(\omega)]=\frac{1}{2\pi}\int_{-\infty}^{\infty}G(\omega)e^{i\omega x}\,d\omega}
$$

## 1 Fourier integral and the Fourier integral theorem

- Fourier integral

It satisfies the Fourier integral theorem: let $f(x)$ be defined on $(-\infty,\infty)$ and
(1) satisfy Dirichlet's conditions on any finite interval;
(2) be absolutely integrable on the infinite interval $(-\infty,\infty)$: $\int_{-\infty}^{\infty}\left|f(x)\right|dx<+\infty$.
Then the Fourier integral formula holds:

$$
f(x)=\frac{1}{2\pi}\int_{-\infty}^{\infty}\left[\int_{-\infty}^{\infty}f(\xi)e^{-i\omega \xi}d\xi\right]e^{i\omega x}
$$

- Three-dimensional form of the Fourier integral

$$
f(x,y,z)=\left(\frac{1}{2\pi}\right)^2\iiint_{-\infty}^{\infty}\left[\iiint_{-\infty}^{\infty}f(\xi,\eta,\zeta)e^{-i(\omega_1\xi+\omega_2\eta+\omega_3\zeta)}d\xi d\eta d\zeta\right]\cdot e^{i(\omega_1 x+\omega_2y+\omega_3z)}d\omega_1d\omega_2d\omega_3
$$

## 2 Fourier transform

- Fourier transform (image function)

$$
F[f(x)]=G(\omega)=\int_{-\infty}^{\infty}f(x)e^{-i\omega x}dx
$$

- Inverse Fourier transform (original function)

$$
F^{-1}[G(\omega)]=f(x)=\frac{1}{2\pi}\int_{-\infty}^{\infty}G(\omega)e^{i\omega x}d\omega
$$

- Relation

$$
f(x)=F^{-1}\{F[f(x)]\}
$$

## 3 Even and odd functions

- Integral of an even function over one period

$$
\int_{-\pi}^{\pi}f(x)dx=2\int_0^\pi f(x)dx
$$

- Integral of an odd function over one period

$$
\int_{-\pi}^{\pi}g(x)dx=0
$$
