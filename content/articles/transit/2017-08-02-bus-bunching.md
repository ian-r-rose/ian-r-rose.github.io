Title: Buses are bosons, or How I learned to stop worrying and love AC Transit (Part one)
Slug: bus-bunching-1

If you have spent any amount of time using mass transit,
you know the frustration of waiting for the better part of an hour for a bus to arrive,
only to see two or three of them roll up in quick succession.
This phenomenon is a common enough problem that it has a name: "bus bunching".

Some reflection on the mechanics of running a bus line suggests a reason for bus bunching.
A traveling bus constantly picks up and drops off passengers as it makes its way around its route.
This process takes time (as anyone who has watched a passenger fumble with change upon boarding knows).
A bus that boards and deposits more passengers will, in general, travel more slowly.

Now, there are many factors that contribute to the number of passengers boarding a given bus, 
including time-of-day, scheduling, and population density.
I will hypothesize that a big contributor is the amount of time since the last bus is also a big factor:
the more time that has passed, the more passengers will have arrived for pickup.

Let's construct a model for the speed of a bus.
We will assume that the bus is on a fixed route, on which it travels all day.
That route may be on any number of different streets, wend through different
neighborhoods, and generally make very little sense 
(like my beloved [12 line](http://www.actransit.org/pdf/maps/version_38/12.pdf)).
However, if it travels back and forth on this same route, we can model it as a loop,
and its position on that loop can be mapped to an angle on a circle $\theta$.
We can then identify the speed of the bus with the time derivative of $\theta$.

The simplest model for $d\theta/ dt$ is for the bus to travel at a constant speed $v_0$:
\begin{equation}
\frac{\partial \theta}{\partial t} = v_0
\end{equation}
Or, expressed in a simulation:
<object data=/visualization/bus/bus-bunching.html?interactive=false&boost=false&gamma=0&n=1 width=700 height=700></object>
This model isn't very interesting. There is only a single bus, and it is travelling at a fixed speed,
so it has no hope of exhibiting the kind of bunching behavior that we want to explain.
So let's start by adding some more buses:
\begin{equation}
\frac{\partial \theta_n}{\partial t} = v_0
\end{equation}
In this equation the subscript indicates the $n$th bus on the route,
so a simulation with five buses would look like:
<object data=/visualization/bus/bus-bunching.html?interactive=false&boost=false&gamma=0&n=5 width=700 height=700></object>
Okay, so this is starting to more closely resemble a bus route,
but the buses still are moving at a constant speed, and have no effect on each other.
What we need is some way of modeling the fact that buses are slowed down
by loading and unloading of passengers.
\begin{equation}
\frac{\partial \theta_n}{\partial t} = 
 v_0 \left[ 1 - \gamma (\theta_{n+1} - \theta_n) \right]
\end{equation}

A change of coordinates makes this system a bit easier to reason about.
Let's boost ourselves into a coordinate system moving at the normal bus speed $v_0$:
\begin{equation}
\psi_n \equiv \theta_n - v_0 t
\end{equation}
From this we can also get the relations
\begin{equation}
\frac{\partial\theta_n}{\partial t} =
\frac{\partial \psi_n}{\partial t} + v_0
\end{equation}
\begin{equation}
\theta_n =
\psi_n + v_0 t
\end{equation}
Substituting this into __ , we find
\begin{equation}
\frac{\partial \psi_n}{\partial t} + v_0 = 
v_0 \left[ 1 - \gamma (\psi_{n+1} - \psi_n) \right]
\end{equation}
\begin{equation}
\frac{\partial \psi_n}{\partial t} = 
v_0 \gamma (\psi_{n} - \psi_{n+1})
\end{equation}
This component-wise equation can be grouped into a single vector equation:
\begin{equation}
\frac{\partial \Theta}{\partial t} = 
\mathbf{A}\Theta
\end{equation}
where
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
\end{equation}
We are interested in the eigenvalues of this matrix.
We can calculate the eigenvalues by forming the characteristic equation:

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

By applying the recursive determinant algorithm, we find
\begin{equation}
det(\mathbf{A}) = 
(v_0 \gamma)^n \left[ (1-\lambda)^n + (-1)(-1)^{n+1}(-1)^{n-1} \right] = 0
\end{equation}

\begin{equation}
(1-\lambda)^n = 1
\end{equation}

