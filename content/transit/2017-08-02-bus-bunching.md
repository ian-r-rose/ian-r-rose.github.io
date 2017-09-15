Title: Buses are bosons, or How I learned to stop worrying and love AC Transit

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

```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython.display import HTML

N = 23
theta = np.linspace(0, 2.*np.pi*(1.-1/N), N)
r = np.ones_like(theta)

fig = plt.figure()
ax = fig.add_subplot(111, projection='polar', frameon=False)
line, = ax.plot(theta, r, marker='o', ls='None')
ax.set_yticklabels([])
ax.set_axis_off()
# Setup time stepping
dt = .01
global time, theta
time = 0 

# Define callbacks for the animation
def init():
    line.set_data([], [])
    return line,
    
def animate(i):
  global theta,time
  theta = theta + dt
  time = time+dt
  line.set_data(theta,r)
  return line,
ani = animation.FuncAnimation(fig, animate, interval=50, blit=True, init_func=init)
ani.save('images/rotate2.mp4')
HTML(ani.to_html5_video())

```

<video src="images/rotate2.mp4" autoplay loop controls></video>

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

