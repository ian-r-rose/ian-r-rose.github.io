Title: Buses are bosons, or How I learned to stop worrying and love AC Transit (Part two)
Slug: bus-bunching-2
Summary: ![bunch](/articles/transit/images/6-bunch.jpg)
Date: 24 April 2018

![6-bunch](articles/transit/images/6-bunch.jpg "Bunching on the 6 bus line in Oakland")

<iframe src=/visualization/bus/bus-bunching.html?interactive=false&equilibrium=true&boost=false&gamma=0.15&n=5 width=700 height=700></iframe>
\begin{equation}
\frac{d\theta_n}{d t} = 
 v_0 \left[ 1 - \gamma (\theta_{n+1} - \theta_n) \right]
\label{evolution}
\end{equation}

<iframe src=/visualization/bus/bus-bunching.html?interactive=false&equilibrium=true&boost=true&gamma=0.15&n=5 width=700 height=700></iframe>
\begin{equation}
v_e = v_0 \left[ 1 - \frac{2 \pi \gamma}{N} \right]
\end{equation}

![stability](articles/transit/images/stability.png "Illustration of stability")

\begin{equation}
\theta_n = \theta^e_n + \theta^\prime_n
\end{equation}
\begin{equation}
\frac{d \theta_n}{dt} = \frac{d \theta^e_n}{dt} + \frac{d \theta^\prime_n}{dt} = v_e + \frac{d \theta^\prime_n}{dt}
\end{equation}
\begin{equation}
\frac{d \theta^\prime_n}{dt} = 
v_0 \left[ 1 - \gamma (\theta^e_{n+1} - \theta^e_n) - \gamma(\theta^\prime_{n+1} - \theta^\prime_n) \right]
- v_0 \left[ 1 - \frac{2 \pi \gamma}{N} \right]
\end{equation}
\begin{equation}
\frac{d \theta^\prime_n}{dt} = 
v_0 \gamma(\theta^\prime_{n+1} - \theta^\prime_n)
\end{equation}

\begin{equation}
\frac{d \Theta^\prime}{d t} = 
\mathbf{A}\Theta^\prime
\end{equation}

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

\begin{equation}
\Theta^\prime = \sum_k a_k \Theta^\prime_k
\end{equation}

\begin{equation}
\sum_k a_k \frac{d \Theta^\prime_k}{d t} = 
\sum_k a_k \mathbf{A}\Theta^\prime_k = 
\sum_k a_k \lambda_k \Theta^\prime_k
\end{equation}

\begin{equation}
\frac{d \Theta^\prime_k}{d t} = 
\lambda_k \Theta^\prime_k
\end{equation}

\begin{equation}
\Theta^\prime_k(t) = \Theta^\prime_k(0) e^{\lambda_k t}
\end{equation}

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

\begin{equation}
det(\mathbf{A}) = 
(v_0 \gamma)^N \left[ (1-\lambda)^N + (-1)(-1)^{N+1}(-1)^{N-1} \right] = 0
\end{equation}


\begin{equation}
(1-\lambda)^N = 1
\end{equation}

\begin{equation}
\lambda_k = e^{\frac{2 k \pi i}{n}} + 1 = \cos \frac{2 k \pi}{n} + i \sin \frac{2 k \pi}{n} + 1
\end{equation}

![roots_of_unity](articles/transit/images/roots_of_unity.png "Eigenvalues of the stability problem")

<iframe src=/visualization/bus/bus-bunching.html?interactive=true&equilibrium=false&boost=true&gamma=0.15&n=5 width=700 height=700></iframe>
<iframe src=/visualization/bus/bus-bunching.html?interactive=true&equilibrium=false&boost=false&gamma=0.15&n=5 width=700 height=700></iframe>
