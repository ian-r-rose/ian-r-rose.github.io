import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator
import numpy as np
plt.style.use('./blueschisting.mplstyle')

fig = plt.figure(figsize=(4,4))
ax = fig.add_subplot(111, aspect='equal')

# Add the data
N = 10
k = np.array(list(range(N)))
x = np.cos(2 * np.pi * k / N) + 1
y = np.sin(2 * np.pi * k / N)
ax.scatter(x,y, s=100, c='#E24A33', zorder=100)

# add axes
ax.set_xlim(-0.2, 2.2)
ax.set_ylim(-1.2, 1.2)
ax.xaxis.set_major_locator(FixedLocator([1, 2]))
ax.yaxis.set_major_locator(FixedLocator([-1, 1]))
ax.axhline(0, lw=4, color='#348ABD')
ax.axvline(0, lw=4, color='#348ABD')
ax.set_xlabel('Real')
ax.set_ylabel('Imaginary')

# Remove a lot of visual noise from the image
ax.grid(False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

# save the figure
plt.savefig('../articles/transit/images/roots_of_unity.png', transparent=True)

