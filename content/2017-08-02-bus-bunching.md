Title: Buses are bosons, or How I learned to stop worrying and love AC Transit

Consider the simplest model for bus speed:
\begin{equation}
\frac{\partial \theta_n}{\partial t} = v_0
\end{equation}
This is very boring.
Now suppose that the speed of a bus is slowed down by a longer headway between it and the bus before it:

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

