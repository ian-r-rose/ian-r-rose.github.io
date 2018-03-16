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
\label{evolution}
\end{equation}

This set of ordinary differential equations will be the primary 
evolution equation for our system of buses.
We will analyze it by answering the following two questions.

1. Is there an equilibrium solution to these equations?
That is to say, is there a solution that does not evolve in time?

2. If there is an equilibrium solution, is it stable? A stable solution,
when perturbed, will return to the equilibrium. An unstable one will get further and further.

Strictly speaking, an equilibrium solution cannot exist for the system of equations as described:
as long as the buses have a nonzero velocity, their positions will evolve in time.
However, with a slight reframing of the question it makes sense to talk about an equilibrium:
is there a configuration and velocity for which the velocity is constant,
and that the distance *between* the buses is not changing?
That is to say, can we find a solution where the buses are traveling steadily,
getting no closer to or further from the others?

It seems intuitive that an equilibrium solution, if it exists,
should have the buses equally spaced, so let's start looking for a solution of that form.
Let's further guess that the equilibrium velocity is the base bus speed $v_0$.

A change of coordinates makes this system a bit easier to reason about.
Let's boost ourselves into moving a coordinate system $\psi$, defined by:
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
Substituting these into equation \eqref{evolution},
we get the governing equations in terms of $\psi_n$:
\begin{equation}
\frac{\partial \psi_n}{\partial t} + v_0 = 
v_0 \left[ 1 - \gamma (\psi_{n+1} - \psi_n) \right]
\end{equation}
\begin{equation}
\frac{\partial \psi_n}{\partial t} = 
v_0 \gamma (\psi_{n} - \psi_{n+1})
\end{equation}

When the buses are equally spaced around the loop, then the distance
between them is the whole loop length divided between the number of buses, or
$\psi_{n+1} - \psi_n = \frac{2 \pi}{N}$,
which makes the governing equations in the $\psi$ coordinates
\begin{equation}
\frac{\partial \psi_n}{\partial t} = 
\frac{ 2 \pi v_0 \gamma }{N}
\end{equation}
-Unless the interaction term $\gamma$ is zero, the time evolution of $\psi_n$ is nonzero,
making this configuration a non-equilibrium solution to the system.

This should make sense, as we defined $v_0$ to be the speed of the bus
in the absense of any delays due to loading and unloading of passengers.
As soon as we include that delay, the buses will be slower than that.
Instead, let's construct a speed for buses that takes into account the
delay due to passengers.

Again, presume that the buses are equally spaced,
such that the distance between them is $2 \pi/N$.
Then, given the evolution equation \eqref{evolution}, we can calculate the speed $v_e$:
\begin{equation}
v_e = \frac{\partial \theta_n}{\partial_t} = v_0 \left[ 1 - \frac{2 \pi \gamma}{N} \right]
\end{equation}
Let's boost into a *new* coordinate system $\phi_n$, defined by
\begin{equation}
\phi_n \equiv \theta_n - v_e t
\end{equation}

Substituting this into equation \eqref{evolution}, we find
\begin{equation}
\frac{\partial \phi_n}{\partial t} + v_e =
v_0 \left[ 1 - \gamma \left(\phi_{n+1} - \phi_n \right) \right]
\end{equation}
Again, when the buses are equally spaced, $\phi_{n+1} - \phi_n = 2 \pi/N$:
\begin{equation}
\frac{\partial \phi_n}{\partial t} + v_e =
v_0 \left[ 1 - \frac{2 \pi \gamma}{N}  \right] = v_e
\end{equation}
Subtracting $v_e$ from both sides, we get
\begin{equation}
\frac{\partial \phi_n}{\partial t} = 0
\end{equation}
which is exactly what we wanted! In the $v_e$ coordinate system,
equally-spaced buses are all in equilibrium.

In the next installment of this two-part series,
we are going to answer the second queation asked above:
is this equilibrium solution stable? (Spoiler: it's not.)
