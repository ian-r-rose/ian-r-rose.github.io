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

\begin{equation}
\Theta^\prime = \sum_k a_k \Theta^\prime_k
\end{equation}

\begin{equation}
\sum_k a_k \frac{d \Theta^\prime_k}{d t} = 
\sum_k a_k \mathbf{A}\Theta^\prime_k = 
\sum_k a_k \lambda_k \Theta^\prime_k
\end{equation}

\begin{equation}
\frac{d \Theta^\prime_k}{d t} = 
\lambda_k \Theta^\prime_k
\end{equation}

## A hunt for eigenvalues

\begin{equation}
\Theta^\prime_k(t) = \Theta^\prime_k(0) e^{\lambda_k t}
\end{equation}

\begin{equation}
det(\mathbf{A}) = 
(v_0 \gamma)^n 
\begin{vmatrix}
1-\lambda & -1 & 0 & 0 & \ldots & 0 \\
0 & 1-\lambda & -1 & 0 & \ldots & 0 \\
0 & 0 & 1-\lambda & -1 & \ldots & 0 \\
\vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\
-1 & 0 & 0 & 0 & \ldots & 1-\lambda\\
\end{vmatrix}
\end{equation}

\begin{equation}
det(\mathbf{A}) = 
(v_0 \gamma)^N \left[ (1-\lambda)^N + (-1)(-1)^{N+1}(-1)^{N-1} \right] = 0
\end{equation}


\begin{equation}
(1-\lambda)^N = 1
\end{equation}

\begin{equation}
\lambda_k = e^{\frac{2 k \pi i}{n}} + 1 = \cos \frac{2 k \pi}{n} + i \sin \frac{2 k \pi}{n} + 1
\end{equation}

![roots_of_unity](articles/transit/images/roots_of_unity.png "Eigenvalues of the stability problem")

## Simulating bus bunching

<iframe src=/visualization/bus/bus-bunching.html?interactive=true&equilibrium=false&boost=true&gamma=0.15&n=5 width=700 height=700></iframe>
<iframe src=/visualization/bus/bus-bunching.html?interactive=true&equilibrium=false&boost=false&gamma=0.15&n=5 width=700 height=700></iframe>
