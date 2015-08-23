Title: Introduction to dimensional analysis

The Buckingham Pi theorem is probably the most important result in the field of dimensional analysis.
That being said, many descriptions of the theorem leave something to be desired, and when 
I used to read them I would come away as confused as when I started.  
The [Wikipedia article](https://en.wikipedia.org/wiki/Buckingham_%CF%80_theorem) on the topic describes it thusly:

> ...if there is a physically meaningful equation involving a certain number $n$ of physical variables, 
> then the original equation can be rewritten in terms of a set of $p = n − k$  dimensionless parameters 
> $\pi_1$, $\pi_2$, ..., $\pi_p$ constructed from the original variables. (Here $k$ is the number of 
> physical dimensions involved; it is obtained as the rank of a particular matrix.)

This is a true statement, but it is essentially the punchline of the theorem. Without the 
context for what $p$, $n$, and $k$ are, how they relate to the $\pi_p$, and why we care 
about any of it, it is very difficult to understand.

I would like to develop some of that context, and to begin we will ask what is meant by 
dimensional analysis in the first place. A lot of what follows will be similar to first-rate 
treatements of dimensional analysis by [Percy Bridgman](https://archive.org/details/dimensionalanaly00bridrich) 
and by [G.I. Barenblatt](http://www.cambridge.org/us/academic/subjects/mathematics/mathematical-modelling-and-methods/scaling?format=PB).
Both of these (short) books are excellent, and I have shamelessly borrowed from them.
As an aside, Bridgman was a physicist at Harvard who did foundational work on high pressure 
physics and materials science. Recently the most abundant mineral on Earth (in Earth?),
[bridgmanite](https://en.wikipedia.org/wiki/Silicate_perovskite), was named in his honor.

## Physical equations

Central to dimensional analysis is the concept of a physical equation. 
A physical equation is something which is has the following properties:

* It involves an equals sign ($=$).
* The terms on both sides of the equals sign have physical dimensions.
* The physical dimensions of these terms are the same.

This may sound trivial, but we will see that many of the statements in dimensional analysis
which sound trivial are, in fact, quite slippery. When a quantity has physical dimensions it 
means that there is some standard that we have agreed upon to measure that quantity. We then can 
determine any quantity of that type in multiples of the standard. This is quite abstract, 
but it means that we can, for instance, define a [standard kilogram](https://en.wikipedia.org/wiki/Kilogram),
and then measure the mass of any item by determining how many of that standard have 
an equal mass to the item.

As another example, the initial definition of the meter had it as one ten-millionth 
of the distance from the equator to the north pole. With that definition, anybody could
(at least in principle), construct a meter-stick and measure the lengths of things to 
their hearts content.
![kilogram](images/standard_kilogram.jpg "The standard kilogram")

Okay, so this standardization of units is all well and good, but at the end of the day, the natural world 
should not care at all what system of units we use for measuring things. There is nothing 
special about one ten-millionth of one-fourth of the circumference of Earth
(except, perhaps, when performing navigation or geography). 
Since the choice of unit is arbitrary, we should be able to convert from one 
system of units to another. For instance, if we are measuring length in inches, we can 
convert to centimeters by multiplying our values in inches by 2.54.

This gets us to the third point in the above list. 
In a physical equation, both sides of the equation must have the same units.

## Example: a simple pendulum

The constraint that both sides of the equation have the same units is actually stronger than it may seem at first. 
If we have a physical system that we are trying to understand, it likely has some parameters which characterize it.
Any physical equation that we cook up must satisfy the rules of dimensional analysis, and therefore 
the parameters have to be combined in such a way that they have the right units. 
Any other combination of these parameters has to be nonsense.

For instance, let us say that we are trying to understand how a the pendulum in a grandfather clock works.
It does a very good job of marking time, and it occurs to us that somebody has 
designed the pendulum so that its period is exactly one second.
We decide to figure out what sets the period ($T$) of the pendulum.
![clock](images/grandfather_clock.jpg "It felt like there was a lot of text, here is a clock!")
After studying the clock for a few minutes, we decide that the most important parameters 
must be the mass ($M$) of the penulum, which makes it swing back and forth, and the length ($L$) of the pendulum.
Therefore, we begin looking for an equation that relates the period to the mass and length, or 
\begin{equation}
T = f( M, L )
\label{incorrect-period}
\end{equation}
Seems simple enough.  But as soon as we look at the units, we run into a problem.
The unit of $T$ is seconds, the unit of $M$ is kilograms, and the unit of $L$ is meters.
There is simply no way to combine the parameters $m$ and $L$ to make something in seconds,
so you cannot actually find a relation like \eqref{incorrect-period}.

So what was our mistake? Well, it turns out that our accounting of the important parameters missed one.
A pendulum also needs gravity, otherwise there is no reason for it to swing back towards the ground.
Therefore we add the acceleration due to gravity $g$ to our list of parameters, which has units of  $m/s^2$.
\begin{equation}
T = f( M, L, g )
\label{correct-period}
\end{equation}
Now we have a parameter that has seconds as a component, so it may be possible to combine the units 
to match the units of the period $T$.
Indeed, after some playing around, we figure out that there is really only one way to combine 
the units to make seconds, which is to say
\begin{equation}
T \sim \sqrt{ \frac{L}{g} }
\label{period}
\end{equation}
Not only is this the only way to make something with units of seconds, but there is no place for the mass of the bob on the pendulum. 
This turns out to be correct: for simple pendula, the mass is irrelevant: only gravity and the length matter.
Now, the [full formula](https://en.wikipedia.org/wiki/Pendulum_%28mathematics%29#Simple_gravity_pendulum)
for the period of a simple pendulum has a factor of $2\pi$, so we were 
not 100% correct, but we got pretty close, and we captured the essential physics of the pendulum without 
actually solving any equations. Instead, all we considered were the dimensions of the thing we were looking for,
and the dimensions of the parameters.

## Asking the right questions

So all this is well and good, but the initial guess about the relevant parameters forgot about gravity, 
and it included a superfluous parameter. We had to play around with the parameters a bit in order to figure 
out how to combine them in the correct way. And even then, it is not necessarily obvious that there is only 
one correct way to combine them.
It would be nice to have a way to go about this more systematic and rigorous way.

We now have the context to ask more specific questions.
Given a system to study and some relevant paramters, we want to answer:

* Can these parameters represent the physics we are interested in?
* How many ways can we combine them to get the correct units?
* What are allowable functional forms of the solution according to the rules of dimensional analysis? 

These are the fundamental questions of dimensional analysis: 
questions which are more or less answered by the Buckingham Pi theorem.
Along the way we will encounter nondimensional numbers, which turn out to be, in a sense,
the most natural system of units to represent the physics of the system.
And hopefully at the end we will be able to go back to the above Wikipedia quote and understand what it means.

In my next post, I will be taking a qualitative look at the content of the Buckingham Pi theorem.
