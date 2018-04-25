import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
plt.style.use('./blueschisting.mplstyle')

fig = plt.figure(figsize=(8,4))

ax = fig.add_subplot(121, aspect='equal')
x = np.linspace(-1, 1)
y = np.exp(-x*x*4.)
ax.plot(x, y, lw=8)
circ = Circle((0,1.1), 0.1, zorder=100)
ax.add_artist(circ)
ax.set_ylim(-0.2,1.2)
ax.set_axis_off()

ax = fig.add_subplot(122, aspect='equal')
x = np.linspace(-1, 1)
y = 1.-np.exp(-x*x*4.)
ax.plot(x, y, lw=8)
circ = Circle((0,0.1), 0.1, zorder=100)
ax.add_artist(circ)
ax.set_ylim(-0.2,1.2)
ax.set_axis_off()

plt.tight_layout()
plt.savefig("../articles/transit/images/stability.png", transparent=True)
