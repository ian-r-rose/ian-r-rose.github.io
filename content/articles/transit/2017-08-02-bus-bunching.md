Title: Buses are bosons, or How I learned to stop worrying and love AC Transit (Part one)
Slug: bus-bunching-1
Summary: ![bunch](/articles/transit/images/18-bunch.jpg)

If you have spent any amount of time using mass transit,
you know the frustration of waiting for the better part of an hour for a bus to arrive,
only to see two or three of them roll up in quick succession.
This phenomenon is a common enough problem that it has a name: "bus bunching":

![18-bunch2](articles/transit/images/18-bunch2.jpg "Bunching on the 18 bus line in Berkeley")

In this two-part series, we'll investigate bunching by making a mathematical model of a bus route.
In the first part, we'll construct the model and find it's equilibrium headway.
In the second part, we'll demonstrate the inevitability for that model to bunch.

A typical mass transit route operates with a given [headway](https://en.wikipedia.org/wiki/Headway),
the distance (or time) between successive vehicles on the route.
If everything is operating according to the plan,
the headway from one bus to the next should be approximately constant,
with possible scheduled variations depending on the time of day
(such as increased frequency during rush hour, or decreased frequency at night).

Let's start by constructing a model for the speed of a single bus.
We will assume that the bus has a fixed route, on which it travels all day.
That route may be on any number of different streets, go wending through different
neighborhoods, and generally make very little sense 
(like my beloved [12 line](http://www.actransit.org/pdf/maps/version_38/12.pdf)).
However, if it travels back and forth on this same route, we can model it as a loop,
and its position on that loop can be mapped to an angle on a circle $\theta$.
We can then identify the speed of the bus with the time derivative of $\theta$.

The simplest model for $d\theta/ dt$ is for the bus to travel at a constant speed $v_0$:

\begin{equation}
\frac{d \theta}{d t} = v_0
\end{equation}
Or, expressed in a simulation:
<iframe src=/visualization/bus/bus-bunching.html?interactive=false&boost=false&equilibrium=true&gamma=0&n=1 width=700 height=700></iframe>

Now, this model isn't very interesting.
There is only a single bus, and it is traveling at a fixed speed,
so it has no hope of exhibiting the kind of bunching behavior that we want to explain.
We can increase the complexity by adding some more buses:

\begin{equation}
\frac{d \theta_n}{d t} = v_0
\label{constant}
\end{equation}
In this equation the subscript indicates the $n$th bus out of $N$ on the route,
so a simulation with five buses looks like this:
<iframe src=/visualization/bus/bus-bunching.html?interactive=false&equilibrium=true&boost=false&gamma=0&n=5 width=700 height=700></iframe>
Okay, so this is starting to more closely resemble a bus route.
However, the buses are still moving at a constant speed, and have no effect on each other.
In order for our model to exhibit the richer characteristics of a system that can bunch,
there must be some way for their speed to be a function of conditions on the road.

There are many factors that can control the speed of a bus traveling through town,
including traffic, construction, scheduled layovers, and number of passengers.
In order to keep the model simple, we will focus on the last reason:
the number of passengers who board and exit the bus.
A traveling bus constantly picks up and drops off passengers as it makes its way around its route.
This process takes time (as anyone who has watched a passenger fumble with change upon boarding knows).
A bus that boards and deposits more passengers will, in general, make slower progress along its route.

Manu things affect the number of passengers boarding a given bus, 
including time-of-day, scheduling, and population density.
We will assume that the amount of time since the previous bus is also a big factor:
the more time that has passed, the more passengers will have arrived at the bus stops for pickup.
If a bus falls behind schedule, more time will have passed since the last bus,
meaning that it will be further slowed down by excess passengers.
In the following analysis, we will use the distance between buses as a proxy
for the number of passengers that need to be picked up.

We need to augment our model to account for this slowing-down behavior.
The expression for speed in equation \eqref{constant} is a constant,
so the next-simplest expression is to make it linear in the distance between buses
(our proxy for the number of passengers):
\begin{equation}
\frac{d\theta_n}{d t} = 
 v_0 \left[ 1 - \gamma (\theta_{n+1} - \theta_n) \right]
\label{evolution}
\end{equation}

In this equation, a bus picking up *no* passengers travels at $v_0$
(which happens if there has been no time for them to accumulate since the previous bus).
As the distance between a bus and the one ahead of it increases,
the speed of the bus slows down, reflecting the additional time spent boarding and disembarking.
The dimensionless parameter $\gamma$ sets how sensitive the bus speeds are to differences in headway.

Equation \eqref{evolution} is a set of ordinary differential equations
(one equation for each of the $N$ buses).
It will be the primary  evolution equation for our system of buses,
which we will analyze by answering the following two questions.

1. Is there an equilibrium solution to these equations?
That is to say, is there a solution that does not evolve in time?

2. If there is an equilibrium solution, is it stable? A stable solution,
when perturbed, will return to the equilibrium.
An unstable one will get further and further from equilibrium until the buses are completely bunched.

Strictly speaking, an equilibrium solution does not exist for the system of equations as described:
as long as the buses have a nonzero velocity, their positions will evolve in time.
However, with a slight reframing of the question it makes sense to talk about an equilibrium:
is there a configuration for which the bus velocities are constant,
and that the distance between them (headways) are not changing?
That is to say, can we find a solution where the buses are traveling steadily,
getting no closer to or further from the others?

In a coordinate system traveling with the buses at equilibrium speed
the solution to the system would then look like:

<iframe src=/visualization/bus/bus-bunching.html?interactive=false&equilibrium=true&boost=true&gamma=0&n=5 width=700 height=700></iframe>

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
\frac{d\theta_n}{d t} =
\frac{d \psi_n}{d t} + v_0
\end{equation}
\begin{equation}
\theta_n =
\psi_n + v_0 t
\end{equation}

Substituting these into equation \eqref{evolution},
we get the governing equations in terms of $\psi_n$:
\begin{equation}
\frac{d \psi_n}{d t} + v_0 = 
v_0 \left[ 1 - \gamma (\psi_{n+1} - \psi_n) \right]
\end{equation}
\begin{equation}
\frac{d \psi_n}{d t} = 
v_0 \gamma (\psi_{n} - \psi_{n+1})
\end{equation}

When the buses are equally spaced around the loop, then the distance
between them is the whole loop length divided between the number of buses, or
$\psi_{n+1} - \psi_n = 2 \pi/N$,
which makes the governing equations in the $\psi$ coordinates

\begin{equation}
\frac{d \psi_n}{d t} = 
\frac{ 2 \pi v_0 \gamma }{N}
\end{equation}

Unless the interaction term $\gamma$ is zero, the time evolution of $\psi_n$ is nonzero,
making this configuration a non-equilibrium solution to the system.

This should make sense, as we defined $v_0$ to be the speed of the bus
in the absence of any delays due to loading and unloading of passengers.
As soon as we include that delay, the buses will be slower than that.
Instead, let's construct a speed for buses that takes into account the
delay due to passengers.

Again, presume that the buses are equally spaced,
such that the distance between them is $2 \pi/N$.
Then, given the evolution equation \eqref{evolution}, we can calculate the speed $v_e$:
\begin{equation}
v_e = \frac{d \theta_n}{d_t} = v_0 \left[ 1 - \frac{2 \pi \gamma}{N} \right]
\end{equation}
Let's boost into a *new* coordinate system $\phi_n$, defined by
\begin{equation}
\phi_n \equiv \theta_n - v_e t
\end{equation}

Substituting this into equation \eqref{evolution}, we find

\begin{equation}
\frac{d \phi_n}{d t} + v_e =
v_0 \left[ 1 - \gamma \left(\phi_{n+1} - \phi_n \right) \right]
\end{equation}
Again, when the buses are equally spaced, $\phi_{n+1} - \phi_n = 2 \pi/N$:
\begin{equation}
\frac{d \phi_n}{d t} + v_e =
v_0 \left[ 1 - \frac{2 \pi \gamma}{N}  \right]
\end{equation}

The right-hand-side is exactly $v_e$, so we can subtract it from both sides to get

\begin{equation}
\frac{d \phi_n}{d t} = 0
\end{equation}
which is exactly what we wanted! In the $v_e$ coordinate system,
equally-spaced buses are all in equilibrium.

In order to get a feel for the equilibrium solution,
experiment with this interactive simulation, which shows the buses
traveling at their equilibrium speed and spacing
(in the $\phi$ coordinate system that moves with them).

<iframe src=/visualization/bus/bus-bunching.html?interactive=true&equilibrium=true&boost=true&gamma=0.15&n=5 width=700 height=700></iframe>

You can see that as the number of buses increases and the headway between the buses gets smaller,
the equilibrium speed increases, reflecting the decreased number of passengers each has to pick up.

At this point we have answered the first of the two above questions: there is an equilibrium solution.
In the next installment of this series, we are going to answer the second question:
is this equilibrium solution stable? (Spoiler: it's not.)

![streetcar](/articles/transit/images/streetcar-bunch.jpg "New Orleans streetcars can be bunched too")
