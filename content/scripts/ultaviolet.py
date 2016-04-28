import matplotlib.pyplot as plt
import numpy as np
plt.style.use('./blueschisting.mplstyle')

xend = 0.9
x = np.linspace(0, xend, 100)
y = x*x

violet= '#988ED5'
red='#E23A23'

fig = plt.figure( figsize=(4,4) )
ax = fig.add_subplot(111)

ax.axes.get_yaxis().set_major_formatter(plt.NullFormatter())
ax.axes.get_xaxis().set_major_formatter(plt.NullFormatter())
ax.tick_params( top='off', bottom='off', left='off', right='off')

ax.plot(x, y, linewidth=8, color=red)
ax.arrow( xend, xend*xend, 0.05,  2.*0.05, width=0.033, head_width=0.06, head_length=0.06, color=red)
ax.fill_between(x, -0.01*np.ones_like(x), y, color=violet, hatch='//')


ax.set_ylim(-0.02,1)
ax.set_xlim(0,1)
ax.set_xlabel(r'$\nu$')
ax.set_ylabel(r'$B$')
plt.savefig("../images/ultraviolet_catastrophe.png")

plt.clf()

xend = 12.0
x = np.linspace(0, xend, 100)
y = np.power(x, 3.)/(np.exp(x)-1)

fig = plt.figure( figsize=(4,4) )
ax = fig.add_subplot(111)

ax.axes.get_yaxis().set_major_formatter(plt.NullFormatter())
ax.axes.get_xaxis().set_major_formatter(plt.NullFormatter())
ax.tick_params( top='off', bottom='off', left='off', right='off')

ax.plot(x, y, linewidth=8, color=red)
ax.arrow( xend, xend*xend, 0.05,  2.*0.05, width=0.033, head_width=0.06, head_length=0.06, color=red)
ax.fill_between(x, -0.01*np.ones_like(x), y, color=violet, hatch='//')


ax.set_ylim(-0.02,1.5)
ax.set_xlim(0,xend)
ax.set_xlabel(r'$\nu$')
ax.set_ylabel(r'$B$')
plt.savefig("../images/planck_law.png")

plt.clf()

