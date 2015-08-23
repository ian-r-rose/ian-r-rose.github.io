Title: Introduction to dimensional analysis

The Buckingham Pi theorem is probably the most important result in the field of dimensional analysis.
That being said, many descriptions of the theorem leave something to be desired, and when 
I used to read them I would come away as confused as when I started.  The Wikipedia article on the 
topic describes it thusly:

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
