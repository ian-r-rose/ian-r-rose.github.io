Title: Linear algebra and the Buckingham Pi theorem
Summary: \begin{equation*} p = n-k \end{equation*} ![lightbulb](/images/lightbulb.png)

We previously spent [two](introduction-to-dimensional-analysis.html)
[longish](nondimensional-numbers-and-the-buckingham-pi-theorem.html)
posts on motivating, and then semi-quantitatively describing the Buckingham Pi theorem.
Here we will try to describe the theorem more precisely and more generally, and the tool
we use will be linear algebra. As is always the case with mathematics, a more
precise and general solution is going to be more abstract. But bear with me,
hopefully it will not be too bad.

As we've seen, the general statement of the problem is that we have 
some quantity in which we are interested, and some set of parameters
which we think describe the physics of that quantity. 
We know that the parameters must combine in some way to 
make something of the correct units (if not, they cannot possibly
be the correct set of parameters for the problem!).

We can describe this setup in terms of a set of "fundamental units,"
which we define to be units which cannot be made by combining other units.  
For instance, meters and seconds are both fundamental units,
but velocity is not, since it can be made by dividing meters by seconds.
The choice of fundamental units is not necessarily unique, but by 
convention we most commonly use the SI measures for length (m),
time (s), temperature (K), mass (kg), quantity (mol), current (A),
and luminosity (cd).

![lightbulb](images/lightbulb.png "not entirely sure how luminosity got in there")

So, let's say that the quantity of interest is called $\Omega$, and that
there are $n$ parameters $\omega_i$, where $i$ goes from one to $n$.
We denote the units of something by enclosing it in square brackets,
so the symbolic representation of the problem is
\begin{equation}
\begin{bmatrix}
\Omega
\end{bmatrix}
=
\begin{bmatrix}
\omega_1^{\alpha_1}\omega_2^{\alpha_2}...\omega_n^{\alpha_n}
\end{bmatrix}
\label{parameters}
\end{equation}

That is to say, we expect to be able to make the units of $\Omega$
by combining the parameters $\omega_i$ in some way, where each parameter
is raised to some power $\alpha_i$.
Furthermore, we have chosen some set of fundamental units which we 
call $f_j$, where the index is for the $j$th fundamental unit that appears
in the problem. We denote the number of fundemental units by $k$. 
Another way of representing the units of $\Omega$ is by using those fundamental units:
\begin{equation}
\begin{bmatrix}
\Omega
\end{bmatrix}
=
f_1^{\beta_1}f_2^{\beta_2} \cdots f_m^{\beta_k}
\label{fundamental_units}
\end{equation}
where the $\beta_j$ are the powers of the fundamental units that
make up the units of $\Omega$.
Since both \eqref{parameters} and \eqref{fundamental_units} are equal to 
the same thing, we can set them equal to each other:
\begin{equation}
\begin{bmatrix}
\omega_1^{\alpha_1}\omega_2^{\alpha_2} \cdots \omega_n^{\alpha_n}
\end{bmatrix}
=
f_1^{\beta_1}f_2^{\beta_2} \cdots f_m^{\beta_k}
\label{intermediate}
\end{equation}
where the $\beta_j$ are the powers of the fundamental units that
make up the units of $\Omega$.
This next step gets a little ugly: we also know that each 
of the parameters $\omega_i$ has some units, so we 
can also represent them using the $f_j$:
\begin{equation}
\begin{bmatrix}
\omega_i
\end{bmatrix}
=
f_1^{\gamma_{1i}}f_2^{\gamma_{2i}} \cdots f_k^{\gamma_{ki}}
\end{equation}
where the $\gamma_{ji}$ are the powers for the $j$th fundamental unit
in the $i$th parameter.
We can substitute this representation of the units of the $\omega_i$
into \eqref{intermediate}:

\begin{equation}
\begin{aligned}
& f_1^{\gamma_{11}\alpha_1}
f_2^{\gamma_{21}\alpha_1}\cdots
f_k^{\gamma_{k1}\alpha_1}  \times \\\\
& f_1^{\gamma_{12}\alpha_2}
f_2^{\gamma_{22}\alpha_2}\cdots
f_k^{\gamma_{k2}\alpha_2} \times \\\\
& \vdots \\\\
& f_1^{\gamma_{1n}\alpha_n}
f_2^{\gamma_{2n}\alpha_n}\cdots
f_k^{\gamma_{kn}\alpha_n} \\\\
=
& f_1^{\beta_1}f_2^{\beta_2}...f_k^{\beta_k}
\end{aligned}
\end{equation}

Almost there. We can now collect together each $f_j$ so that they
only appear once on the left hand side, so by the rules of exponents
their powers are added:

\begin{equation}
\begin{aligned}
& f_1^{\gamma_{11}\alpha_1 + \gamma_{12}\alpha_2 \cdots \gamma_{1n} \alpha_n } \times \\\\
& f_2^{\gamma_{21}\alpha_1 + \gamma_{22}\alpha_2 \cdots \gamma_{2n} \alpha_n } \times \\\\
& \vdots \\\\
& f_k^{\gamma_{k1}\alpha_1 + \gamma_{k2}\alpha_2 \cdots \gamma_{kn} \alpha_n } \\\\
&= f_1^{\beta_1}f_2^{\beta_2}...f_k^{\beta_k}
\end{aligned}
\end{equation}
Here is the cool part: because we chose the $f_j$ to be a set of fundamental
units, there is no way to make them out of the other fundamental units.
Therefore, if the above equation is true, then the exponents for 
each of the $f_j$ on both sides of the equation have to be equal!
So this (terribly) ugly equation is really just a set of much simpler
equations where we set the exponents of each $f_j$ to be equal:

\begin{equation}
\begin{aligned}
\gamma_{11}\alpha_1 + \gamma_{12}\alpha_2 \cdots \gamma_{1n} \alpha_n &= \beta_1 \\\\
\gamma_{21}\alpha_1 + \gamma_{22}\alpha_2 \cdots \gamma_{2n} \alpha_n &= \beta_2 \\\\
\vdots \\\\
\gamma_{k1}\alpha_1 + \gamma_{k2}\alpha_2 \cdots \gamma_{kn} \alpha_n &= \beta_k\\\\
\end{aligned}
\end{equation}

If you have ever learned linear algebra, this should start to look very familiar:
it is actually a matrix equation:

\begin{equation}
\begin{bmatrix}
\gamma_{11} & \gamma_{12} & \cdots & \gamma_{1n} \\\\
\gamma_{21} & \gamma_{22} & \cdots & \gamma_{2n} \\\\
\vdots & \ddots & & \vdots \\\\
\gamma_{k1} & \gamma_{k2} & \cdots & \gamma_{kn} \\\\
\end{bmatrix}
\begin{bmatrix}
\alpha_1 \\\\
\alpha_2 \\\\
\vdots \\\\
\alpha_n \\\\
\end{bmatrix}
=
\begin{bmatrix}
\beta_1 \\\\
\beta_2 \\\\
\vdots \\\\
\beta_k \\\\
\end{bmatrix}
\label{dimension_matrix}
\end{equation}

Any time you can make your math problem look like a matrix equation,
you should be very happy. This is primarily for two reasons:

* Linear algebra and matrix equations are an extremely well-developed
and well-understood branch of mathematics, with a rich set of tools
and very elegant theory. If your problem is a linear algebra problem
you can use all that.

* Computers are quite good at doing linear algebra. The only thing
better than doing linear algebra is having a computer do it for you
[[citation needed]](linear-algebra-and-the-buckingham-pi-theorem.html).

Equation \eqref{dimension_matrix} is fairly abstract, but it represents
the same basic idea that we dealt with in the previous post: we 
need to combine the parameters (in a recipe defined by the $\alpha$'s)
in such a way to get the right dimensions (defined by the $\beta$'s).
The matrix $\gamma_{ji}$ tells us how to convert between the parameters
and the dimensions.

We can rewrite Equation \eqref{dimension_matrix} in a more compact notation:

\begin{equation}
\bar{\bar{\gamma}} \bar{\alpha} = \bar{\beta}
\label{dimension_equation}
\end{equation}
where one overbar indicates a vector, and two overbars indicate a matrix.

A particular solution to \eqref{dimension_equation} tells us one way to 
combine the parameters to get the right units.
However, we saw previously that in some cases there was more than one
way to combine the parameters to get the right units, and this 
led to parameter combinations without any dimensions: so-called nondimensional numbers.
We could multiply by any function of these nondimensional numbers
and still get the units we wanted. We can represent this phenomenon using
our dimensional equation: suppose that we have a particular
combination of the $\alpha$'s that satisfies Equation \eqref{dimension_equation},
which we denote by $\bar{\alpha}_0$. Suppose furthermore that we have some
nondimensional number, denoted by $\bar{\pi}$. Since

\begin{equation}
\bar{\bar{\gamma}} \bar{\alpha}_0 = \bar{\beta}
\end{equation}

we must also have

\begin{equation}
\bar{\bar{\gamma}} \left( \bar{\alpha}_0 + \bar{\pi} \right) = \bar{\beta}
\end{equation}

This is just a statement that the nondimensional number
$\bar{\pi}$ does not change the units of the answer.
We can subtract the above two equations to get

\begin{equation}
\bar{\bar{\gamma}} \bar{\pi} = 0
\label{nullspace}
\end{equation}

This is a very special equation in linear algebra, the solution to which is the 
*[nullspace](https://en.wikipedia.org/wiki/Kernel_(linear_algebra))* of the matrix $\bar{\bar{\gamma}}$.
The nullspace is the set of vectors which, when acted upon by a matrix, give the zero vector.
From a dimensional standpoint, equation \eqref{nullspace} is just saying that the 
nondimensional number vectors $\bar{\pi}$ indeed have no dimensions.
However, now we know that the nullspace of the matrix $\bar{\bar{\gamma}}$ is *exactly*
the same thing as the set of nondimensional numbers for that problem.

So why is the matrix representation of dimensional analysis useful?
The answer is that it allows us to apply one of the most important results of linear algebra: the 
[rank-nullity theorem](https://en.wikipedia.org/wiki/Rank%E2%80%93nullity_theorem).
The matrix $\bar{\bar{\gamma}}$ is, in general, not square: it has shape $k$ rows 
(the number of fundamental units) by $n$ columns (the number of parameters).
The rank-nullity theorem is a statement about the relationship between 
the dimensionality of the [image](https://en.wikipedia.org/wiki/Row_and_column_spaces)
of a matrix (i.e. its rank), the dimensionality of the nullspace of 
that matrix, and the number of columns of that matrix.
The theorem states:

\begin{equation}
\mathrm{dim}(\mathrm{image}( \bar{\bar{\gamma}} ) ) + 
\mathrm{dim}(\mathrm{nullspace}(\bar{\bar{\gamma}}) ) = \mathrm{number \; of \; columns}
\label{rank-nullity}
\end{equation}

If the rows of the matrix are linearly independent (which is not always the case!)
then the rank is just the number of rows $k$.
The dimensionality of the nullspace of $\bar{\bar{\gamma}}$ is the number of 
nondimensional numbers in our problem $p$.

For our central problem of dimensional analysis, the number of rows is
the number of fundamental units $k$, and the number of columns
is the number of parameters $n$.
Then, by the rank-nullity theorem, the number of nondimensional numbers is just
\begin{equation}
p = n - k
\end{equation}

which is exactly the statement of the Buckingham pi theorem! 
So we see, when reformulated in terms of linear algebra,
the Buckingham pi theorem is just an application of the rank-nullity theorem.
Not only is this an interesting mathematical result by itself,
it allows for a more careful treatment of dimensional analysis problems
in more complicated cases where the actual list of parameters is
unclear, or when they may be linearly dependent on each other.

To be more concrete, we can return to the example of 
[Couette flow](https://en.wikipedia.org/wiki/Couette_flow).
The parameters are the viscosity $\eta \; (\mathrm{kg}/\mathrm{m s})$, 
the density $\rho \; (\mathrm{kg}/\mathrm{m}^3)$,
the separation distance $D \; (\mathrm{m})$, 
and the upper plate velocity $u_0 \; (\mathrm{m/s})$.
The fundamental units are mass ($kg$), length ($m$), and time ($s$).

![couette](images/couette.svg "Couette flow")

We therefore have three fundamental units and four parameters, meaning that
our dimensional matrix (defined in Equation \eqref{dimension_matrix})
must have three rows (one for each fundamental unit), and four columns (one for each parameter).
The entries of the matrix correspond to the exponent of that row's unit in that column's parameter.
We order the units $kg$, $m$, and $s$, and order the parameters $\eta$, $\rho$, $D$, and $u_0$,
allowing us to construct the matrix:

\begin{equation}
\bar{\bar{\gamma}} = 
\begin{bmatrix}
1 & 1 & 0 & 0 \\\\
-1 & -3 & 1 & 1 \\\\
-1 & 0 & 0 & -1 \\\\
\end{bmatrix}
\end{equation}

I won't solve it here, but this 3x4 matrix has exactly one vector in its nullspace, which is given by

\begin{equation}
\bar{\pi} =
\begin{bmatrix}
-1 \\\\
1 \\\\
1 \\\\
1 \\\\
\end{bmatrix}
\end{equation}

You can verify that this does indeed make the zero vector when you apply $\bar{\bar{\gamma}}$ to it.
This vector $\bar{\pi}$ can be converted back into its symbolic unit description:
\begin{equation}
\frac{\rho u_0 D}{\eta}
\end{equation}

This, you may not be surprised to see, is the nondimensional number associated with
Couette flow, the Reynolds number!

To summarize, we have seen that the problem of dimensional analysis, which we 
described in some detail in the previous two articles, can be written
equivalently in terms of matrix-vector operations. This allows us 
to bring the whole edifice of linear algebra to bear on the problem.
It also suggests an interesting possibility: since computers are *extremely*
good at linear algebra, it should be possible to write some 
code that does dimensional analysis for us, with a minimum of 
effort on our part. That is what I will be attempting in my [next article](automated-dimensional-analysis.html).
