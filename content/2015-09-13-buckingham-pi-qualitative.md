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
Moreover, the most useful way of looking at this problem is to compare 
the relative size of these two different fluid velocity scales.
How the fluid behaves is determined by this comparison: if the driving velocity is
much larger than the natural fluid velocity scale, the Couette flow 
will look very different than if the driving velocity is much smaller than the fluid velocity scale.

We can express this comparison mathematically by calculating the ratio of the two velocity scales.
In fact, this ratio is so important for the Couette flow setup (and others like it)
that it goes by a special name, the Reynolds number:

\begin{equation}
\mathrm{Re} = \frac{\rho u_0 D}{\eta}
\end{equation}

The Reynolds number has a nice physical interpretation: it represents the 
relative importance of the inertia of the fluid (which is driven by
the wall motion, and tends to keep the fluid moving) and the viscous 
forces in the fluid (which is tends to damp out fluid motions).
If the Reynolds is large, inertia is more important, and the 
fluid will have whorls, vortices, and be very chaotic.
If the Reynolds number is small, the fluid will move slowly
and regularly, in a fashion that is known as "laminar."

## Nondimensional numbers

Something very important happened when we compared the two velocity scales
by computing the Reynolds number: we divided something with units of velocity
by something with units of velocity. By doing so we canceled out all the units 
in the number: we could compute the Reynolds number by measuring velocity 
in meters per second, we could compute it using feet per hour, we could compute 
it using light years per fortnight, and we would always come up with the same
Reynolds number. And that Reynolds number will still have the 
physical interpretation of inertial-to-viscous effects.

Circling back to our initial goal of characterizing the velocity solution 
in terms of our parameters, we found that we can represent the units 
correctly by doing either of the following:
\begin{equation}
\mathbf{u} \sim u_0
\end{equation}
\begin{equation}
\mathbf{u} \sim \frac{\eta}{\rho D}
\end{equation}
Unlike the pendulum example, there is an additional wrinkle.
Sure, those expressions correctly represent the units of velocity,
but I can multiply the right hand sides by the Reynolds number, 
which has no dimensions, and still have the correct units.
Even more, I can multiply by *any arbitrary function of 
the Reynolds number*, with no effect on the units.

Expressed in terms of an equation, I can write 
\begin{equation}
\mathbf{u} = u_0 \; f( \mathrm{Re} )
\end{equation}
\begin{equation}
\mathbf{u} = \frac{\eta}{\rho D} \; g( \mathrm{Re} )
\end{equation}
Which expression is more correct? For the most part, it does not matter.
It is not hard to show from the above equations that
\begin{equation}
g(\mathrm{Re}) = \mathrm{Re} \; f(\mathrm{Re})
\end{equation}
so these two expressions are really just different ways of writing the same thing.

## The Buckingham Pi theorem

Let's try to put the observations we've made so far into a coherent picture.
