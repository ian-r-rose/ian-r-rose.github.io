Title: Ultriviolet catastrophe and the beginning of quantum mechanics

We just finished a very long explication of the fundamentals of dimensional
analysis and the Buckingham Pi theorem. That could be the end of this series,
but it would be a shame to end it without showing at least one
example of some of the cool analysis that can be done in a more complicated
system than the ones we have considered so far.

The example that we will be considering is the problem of the ultraviolet
catastrophe, a famous problem which demonstrated in the late nineteenth
and early twentieth century that not all was right with classical physics.
It also has the distinction of having one of the coolest names for an 
unsolved problem in science. For a long time sedimentary geology had 
an unsolved problem about the origin of the mineral dolomite, known as
the "dolomite problem". Doesn't quite have the same ring to it.

At heart, the ultraviolet catastrophe has to do with the question of how
hot objects cool off (as somebody who studies convection and the thermal
evolution of planets, it is my bias that a great many problems in 
science boil down to a question of how things cools off!).
It was observed that objects at high temperature would radiate electromagnetic
waves to the space around them, a process known as radiative cooling.
The frequency of the radiation was not a single value, but was instead 
a spectrum. Furthermore, the shape of that spectrum and its dominant 
frequency seemed to be a function of what temperature the object was
at. At lower temperatures, the object would give off dominantly 
lower frequency radiation and at higher temperatures it would give off
dominantly higher frequency radiation.

Most objects that we interact with on a daily basis are at too low of 
temperatures to radiate in the visible spectrum, but you have probably
seen a hot poker glow red, which means it is certainly too hot to touch.
If it gets a lot hotter than that, it may start to glow white, reflecting
the temperature dependence of the radiative spectrum.

The question of the radiative spectrum that a body emits is not just of 
theoretical interest: it is intensely practical in many areas of science
and engineering. After all, if we understand what determines the 
spectrum of a radiating body, we can measure its temperature without
needing to touch it, nor do we even need to be particularly close to it.
We just need to be able to see it. This would allow us to know the temperature
of stars and planets, as well as measure the temperature of many otherwise
difficult to access laboratory experiments.

Okay, so with that prelude, let's get cracking on dimensional analysis.
The observation that we are trying to explain is the radiation of 
energy from the surface of an object. That is to say, the object
gives off a certain amount of energy per unit surface area per time, or
\begin{equation}
[I] = \frac{\text{energy}}{\text{frequency} \cdot \text{area} \cdot \text{time} }
\end{equation}
Expressed in terms of SI units this becomes
\begin{equation}
[I] = \frac{\mathrm{kg}}{\mathrm{s}^2}
\end{equation}
Pedants may note that the conventional dimensions of this quantity also
include the units of the solid angle over which this energy is measured.
This solid angle is dimensionless (steradians), so does not affect the 
analysis here. If you like, you can pretend I have integrated over some
solid angle and am carrying around an additional paramter indicating that
angle. It is otherwise unimportant here.

As for the parameters that are important in this problem, we already know
several based upon the observations. First, we know that the frequency
of the radiation $\nu$ plays a role. Second, we know that the temperature $T$
of the body in question must matter, since that is a large part of the
motivation for this problem. And if temperature is important, Boltzmann's
constant $k_B$ cannot be far behind, since that is statistical mechanics'
bridge between temperature and energy.
These parameters have units

\begin{equation}
\begin{aligned}
[ \nu ] &= \frac{1}{\mathrm{s}} \\
[T] &= \mathrm{K} \\
[k_B] &= \frac{\mathrm{kg} \; \mathrm{m}^2}{\mathrm{s}^2 \; \mathrm{K}}
\end{aligned}
\end{equation}

Is that enough? Well, let's try to get the right units with these parameters.
After some playing around, the closest I can get is 
\begin{equation}
\left[ k_B \mathrm{T} \nu \right] = \frac{ \mathrm{kg} \; \mathrm{m}^2 }{\mathrm{s}^3}
\end{equation}

There appears to be no way of getting rid of the meters in the numerator with
this set of parameters. The ambitious reader can try themselves, either 
by hand or by using the buckinghampy software developed previously.
A bit of rumination suggests an answer: electromagnetic radiation is, after all,
a light waves, and these light waves are traveling through space to arrive
at our instruments (or eyes). The speed of light $c$ is probably important 
in their generation, and that has units of $\mathrm{m}/\mathrm{s}$.

With the introduction of the speed of light, we can represent the units of $I$
in one (and only one) way:

\begin{equation}
I \sim \frac{k_B T \nu^3}{c^2}
\end{equation}

Up to __ this equation is known as the Rayleigh-Jeans equation. It was 
developed to explain the spectrum of radiating bodies, and at least for
lower temperatures, it did a pretty good job. So we could pat ourselves on
the back. Another dimensional analysis well done.

But wait, what if we inquire further about the total energy that this 
body is giving off? After all, we are not only interested in the spectrum, 
but also the rate of cooling of an object. Well, we have an expression
that gives the energy radiated as a function of frequency. As far as we know,
no frequencies of light are special: all are equally allowable. We can go
to higher and higher frequencies just by inserting more "wiggles."

So we should be able to get the total energy by integrating
