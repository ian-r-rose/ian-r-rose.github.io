Title: Buses are bosons, or How I learned to stop worrying and love AC Transit (Part two)
Slug: bus-bunching-2
Summary: ![bunch](/articles/transit/images/6-bunch.jpg)
Date: 24 April 2018

![6-bunch](articles/transit/images/6-bunch.jpg "Bunching on the 6 bus line in Oakland")

\begin{equation}
\frac{d\theta_n}{d t} = 
 v_0 \left[ 1 - \gamma (\theta_{n+1} - \theta_n) \right]
\label{evolution}
\end{equation}

<iframe src=/visualization/bus/bus-bunching.html?interactive=false&equilibrium=true&boost=true&gamma=0.15&n=5 width=700 height=700></iframe>
\begin{equation}
v_e = v_0 \left[ 1 - \frac{2 \pi \gamma}{N} \right]
\label{equilibrium}
\end{equation}

## Stability analysis

Most stability analyses are centered on answering a central question:
"Is my equlibrium solution stable with respect to small perturbations?"
That is to say, if I have an eqilibrium solution and poke it slightly,
does it return to equlibrium, or does that poke keep growing until the solution
is no longer anything like the equilibrium one?
![stability](articles/transit/images/stability.png "Illustration of stability")
This behavior can be visualized by thinking of a ball balanced on a hill,
and another resting in a trough.
Both of the balls are not moving around, and are thus in equilibrium solutions.
However, if I nudge the ball on the hill, it will continue rolling until it is far from the peak.
If I nudge the ball in the trough, it will roll back to the center of the trough and
eventually come to a rest.
The first situation is an unstable equilibrium, and the second is a stable one.

Our approach for analyzing the system of equations in equation \eqref{evolution} will be similar:
we will investigate its behavior when we nudge it slightly away from the equilibrium solution
represented by equation \eqref{equilibrium}.

## Perturbation equations

The first step in deriving the perturbation equations is to split the
bus positions $\theta_n(t)$ into two parts, an equilibrium part and a perturbation:
\begin{equation}
\theta_n = \theta^e_n + \theta^\prime_n
\label{decompose}
\end{equation}

In equation \eqref{decompose}, $\theta^e_n$ is the equilibrium solution for the buses
(i.e. $v_e$ integrated with respect to time),
and $\theta^\prime_n$ is a *small* perturbation away from that equilibrium.
You may wonder what the perturbation actually *is*, since it can be a function of time,
and each of the buses can have a different perturbation.
Fortunately, we will be able to show that this analysis does not depend on the form
of the perturbation (other than that it is nonzero), so it can be completely arbitrary.

The governing equations are in terms of velocities rather than positions,
so we take the time derivative of equation \eqref{decompose},
noting that $d \theta^e_n / dt = v^e$:
\begin{equation}
\frac{d \theta_n}{dt} = \frac{d \theta^e_n}{dt} + \frac{d \theta^\prime_n}{dt} = v_e + \frac{d \theta^\prime_n}{dt}
\label{decompose2}
\end{equation}

We can substitute equations \eqref{decompose} and \eqref{decompose2}
into equation \eqref{evolution} to get
\begin{equation}
\frac{d \theta^\prime_n}{dt} + v_e = 
v_0 \left[ 1 - \gamma (\theta^e_{n+1} - \theta^e_n) - \gamma(\theta^\prime_{n+1} - \theta^\prime_n) \right]
\end{equation}
Note that in the equilibrium configuration the buses are equally spaced,
so $\theta^e_{n+1} - \theta^e_{n} = 2 \pi / N$:
\begin{equation}
\frac{d \theta^\prime_n}{dt} + v_e = 
v_0 \left[ 1 - \frac{2 \pi \gamma}{N}  - \gamma(\theta^\prime_{n+1} - \theta^\prime_n) \right]
\end{equation}

This allows $v_e$ to be subtracted from both sides, leaving us with:
\begin{equation}
\frac{d \theta^\prime_n}{dt} = 
v_0 \gamma(\theta^\prime_{n+1} - \theta^\prime_n)
\label{perturb}
\end{equation}

Okay, so what did those manipulations buy us?
There are two attractive features that equation \eqref{perturb} has:

1. It is now a system of differential equations involving only the perturbations,
the time evolution of which we are interested in for the stability problem.
The equilibrium solution has completely disappeared.
1. More importantly, *it is now a system of linear equations!*
There are no nonlinearities or constant offsets getting in our way.
And if there is one thing we are good at analyzing, it is linear equations.

In fact, since it is a set of linear equations,
we can write it using matrix notation:
\begin{equation}
\frac{d \Theta^\prime}{d t} = 
\mathbf{A}\Theta^\prime
\label{matrix}
\end{equation}
where $\Theta^\prime$ is a vector containing all the perturbations to the $N$ buses,
and $\mathbf{A}$ is a matrix describing the linear coupling between the buses, given by:

\begin{equation}
\mathbf{A} = 
v_0 \gamma 
\begin{bmatrix}
1 & -1 & 0 & 0 & \ldots & 0 \\
0 & 1 & -1 & 0 & \ldots & 0 \\
0 & 0 & 1 & -1 & \ldots & 0 \\
\vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\
-1 & 0 & 0 & 0 & \ldots & 1\\
\end{bmatrix}
\label{A}
\end{equation}
Note that the last row couples the speed of the $N$th bus to the first bus,
reflecting the circular nature of the model.

## The eigendecomposition

When analyzing a system of linear equations,
it is often helpful consider it in terms of its eigenvalues and eigenvectors
(exactly how it is helpful should be clearer in a moment).
A general perturbation vector $\Theta^\prime$ can be decomposed
into a linear combination of the $N$ eigenvectors[^1] of $\mathbf{A}$
(known as an eigendecomposition):
\begin{equation}
\Theta^\prime = \sum_k a_k \Theta^\prime_k
\label{eigs}
\end{equation}
where $a_k$ is the amount of each eigenvector contributing to $\Theta^\prime$
and $\Theta^\prime_k$ is the the $k$th eigenvector. 

Substituting equation \eqref{eigs} into \eqref{matrix}, we get
\begin{equation}
\sum_k \frac{d a_k}{dt} \Theta^\prime_k = 
\sum_k a_k \mathbf{A}\Theta^\prime_k = 
\sum_k a_k \lambda_k \Theta^\prime_k
\end{equation}
where we have used the definition of the eigenvalues $\lambda_k$:
$\mathbf{A}\Theta^\prime_k = \lambda_k \Theta^\prime_k$.

The eigenvectors of $\mathbf{A}$ are linearly independent,
so the components of the summation decouple,
giving us a set of independent ordinary differential equations:
\begin{equation}
\frac{d a_k}{d t} = 
\lambda_k a_k
\label{diff_eigen}
\end{equation}

Equation \eqref{diff_eigen} looks very much like equation \eqref{matrix},
but with one important difference:
the matrix $\mathbf{A}$ has been replaced with the scalar eigenvalues.
This change turns the system of coupled differential equations into
a set of uncoupled differential equations.


## A hunt for eigenvalues


\begin{equation}
a_k(t) = a_k(0) e^{\lambda_k t}
\label{integrated}
\end{equation}

Equation \eqref{integrated} gives us the solution for the
time evolution of the perturbations of $\mathbf{A}$.
Remember, our pertubation to the equilibrium solution can be written
in terms of the eigenvectors, and we are interested in whether
the perturbation grows in time or shrinks in time.
The answer to that question all comes down to the values for the eigenvalues $\lambda_k$.
Broadly speaking, there are three possibilities:

1. $\lambda_k$ is negative. In this case, a perturbation of the shape of $\Theta^\prime_k$
will shrink in time, since \eqref{integrated} is a negative exponential.
1. $\lambda_k$ is positive. In this case, a perturbation of the shape of $\Theta^\prime_k$
will grow in time, since \eqref{integrated} is a positive exponential.
1. $\lambda_k$ is complex. In this case, a perturbation of the shape of $\Theta^\prime_k$
will have combined behaviors: it will oscillate according to the imaginary part
of $\lambda_k$ (due to [Euler's formula](https://en.wikipedia.org/wiki/Euler%27s_formula)),
and either shrink or grow according to the sign of the real part.
For our purposes, we want to know it shrinks or grows,
so we are most interested in the real part of any complex eigenvalues.

In physical systems, there is always a certain amount of noise,
and in general that noise will put some amount of power
into each of the eigenvectors of the system.
Some eigenvectors get a bit more power, some might get a bit less,
but for random, uncorrelated noise, we expect all the eigenvectors to get some.
This means that if *just one* eigenvalue has a positive real part,
then the power in that eigenvalue will grow in time.
So our stability metric is this: *all* of the eigenvalues must have
negative real parts for the system to be considered stable to perturbations.

So let's find the eigenvalues of $\mathbf{A}$.
Usually calculating the eigenvalues of a matrix of a larger order than 2 or 3
is a pretty involved process, but in this case the matrix is
ordered enough and has enough zeroes in it that we can come up
with a closed-form solution.

The eigenvalues of $\mathbf{A}$ can be found by solving its
[characteristic polynomial](https://en.wikipedia.org/wiki/Characteristic_polynomial),
found by taking the the determinant of $\mathbf{A} - \lambda \mathbf{I}$:
\begin{equation}
det(\mathbf{A - \lambda \mathbf{I}}) = 
(v_0 \gamma)^N 
\begin{vmatrix}
1-\lambda & -1 & 0 & 0 & \ldots & 0 \\
0 & 1-\lambda & -1 & 0 & \ldots & 0 \\
0 & 0 & 1-\lambda & -1 & \ldots & 0 \\
\vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\
-1 & 0 & 0 & 0 & \ldots & 1-\lambda\\
\end{vmatrix}
\end{equation}

We apply the [Laplace expansion](https://en.wikipedia.org/wiki/Laplace_expansion)
(where I have ellided some operations):
\begin{equation}
det(\mathbf{A} - \lambda \mathbf{I}) = 
(v_0 \gamma)^N \left[ (1-\lambda)^N + (-1)(-1)^{N+1}(-1)^{N-1} \right] = 0
\end{equation}

which may be simplified to

\begin{equation}
(1-\lambda)^N = 1
\end{equation}

Now, this polynomial equation of order $N$ has a fairly straightforward set
of solutions for $\lambda$: they are the
[roots of unity](https://en.wikipedia.org/wiki/Root_of_unity),
shifted along the positive $x$-axis by one.

We can write the solution for $\lambda_k$ explicitly
\begin{equation}
\lambda_k = e^{\frac{2 k \pi i}{N}} + 1 = \cos \frac{2 k \pi}{N} + i \sin \frac{2 k \pi}{N} + 1
\end{equation}
which, when plotted (for $N=10$), gives the following:

![roots_of_unity](articles/transit/images/roots_of_unity.png "Eigenvalues of the stability problem")

Hey, look at that! The real part of each eigenvalues is greater than or equal to zero![^2]
That is to say, not only is the system unstable, it is *wildly* unstable.
Remember, if *just one* of the eigenvalues had a positive real part
the system would be unstable, and yet they almost all do.

## Simulating bus bunching

So that was a long way to go,
but by determining that the eigenvalues of the system of equations \eqref{perturb}
all have nonnegative real parts, we determined that any perturbation
to our equilibrium solution is unstable.
Therefore, if any of the buses on our bus route get slightly off schedule,
they will get further and further off schedule.




<iframe src=/visualization/bus/bus-bunching.html?interactive=true&equilibrium=false&boost=true&gamma=0.15&n=5 width=700 height=700></iframe>
<iframe src=/visualization/bus/bus-bunching.html?interactive=true&equilibrium=false&boost=false&gamma=0.15&n=5 width=700 height=700></iframe>

[^1]: This is a footnote
[^2]: This is a footnote
