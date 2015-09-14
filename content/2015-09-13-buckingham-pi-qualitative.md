Title: Nondimensional numbers and the Buckingham Pi theorem

In my [previous post](introduction-to-dimensional-analysis.html) I 
tried to establish the context for nondimensional analysis, which 
allowed us to ask the central questions which the Buckingham Pi theorem
will allow us to answer. At the heart of the matter was the relationship
between the units of the physical paraemters which are important for a given problem,
and the units of the quantity which we are trying to determine.

For the example of the period of the pendulum in a grandfather clock,
we surmised that the important parameters were the length of the pendulum $L$,
the mass of the bob $M$, and the acceleration due to gravity $g$.
When we tried to come up with something that matched the units of the period (seconds),
we found that there was only one way to do that:
\begin{equation}
T \sim \sqrt{\frac{L}{g}}
\label{period}
\end{equation}
Since there was only one way to make something with the right units,
we were pretty sure that the solution to this problem would look a lot like
Equation \eqref{period}, and indeed that was correct, up to a factor of $2 \pi$.

## Couette flow

It is not always the case that there is only one way to make something of the correct units
In many more complicated problems there can be several ways to rearrange the parameters to get the units we want.
A good example of this is [Couette flow](https://en.wikipedia.org/wiki/Couette_flow),
which is among the simpler fluid dynamics setups, but still exhibits
a huge amount of richness and complexity, and research on this style of flow is still being done.

In Couette flow there are two parallel plates with a fluid between them.
The fluid has a viscosity $\eta \; (kg/m s)$ and a density $\rho \; (kg/m^3)$,
and the plates are separated by a distance $D \; (m)$. The top plate is 
being moved in the $x$-direction at velocity $u_0 \; (m/s)$. We presume
that the plates are large enough laterally that we can neglect their edges.

We are interested in determining the velocity and pressure in the 
fluid, which means that, in general, you have to solve 
the Navier-Stokes equations for an incompressible fluid:
\begin{equation}
\rho \frac{D \mathbf{u}}{Dt} = -\nabla P + \eta \nabla^2 \mathbf{u}
\end{equation}
\begin{equation}
\nabla \cdot \mathbf{u} = 0
\end{equation}

The Navier-Stokes equations are notoriously difficult to solve:
there is a rather [large prize](http://www.claymath.org/millennium-problems/navier%E2%80%93stokes-equation)
available to anybody able to make some foundational progress towards a general solution.
How much can we learn about this system from a dimensional standpoint?

Well, let's do the same accounting we did for the pendulum problem. We would like to
know the velocity of the fluid between the plates, and the relevant parameters 
for the problem are the fluid viscosity $\eta$, the fluid density $\rho$, the distance
between the two plates $D$, and the velocity of the upper plate $u_0$. which is driving 
the fluid flow. How can we make something with units of velocity ($m/s$)?

Well, (you might think at first), this is easier than the pendulum problem. The driving 
velocity $u_0$ has the right units, so we are already done!
A closer look, though, reveals another way to make something of the right units:
\begin{equation}
\frac{\eta}{\rho D}
\end{equation}

There are, in fact, two different ways to represent the units of the velocity $\mathbf{u}$.
We can look at this system as having two different velocity "scales," of a sort.
There is the scale which is determined by the driving velocity $u_0$, but there 
is also the scale which is determined by the properties of the fluid and the 
geometry of the setup $\eta/\rho D$. So which one is the correct scale? 
Which one is more appropriate for trying to learn about the velocity of the fluid?

The answer, you may not be surprised to learn, is that both are important.
Moreover, the most useful way of looking at this problem is by looking at the ratio of the two different "scales."
How the fluid behaves is determined by this ratio: if the driving velocity is
much larger than the natural fluid velocity scale, the Couette flow 
will look very different than if the driving velocity is much smaller than the fluid velocity scale.

In fact, this ratio is so important for the Couette flow setup (and others like it)
that it goes by a special name, the Reynolds number:

\begin{equation}
\mathrm{Re} = \frac{\rho u_0 D}{\eta}
\end{equation}

## Nondimensional numbers


## The Buckingham Pi theorem
