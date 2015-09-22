import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

fig = plt.figure( figsize=(16,8) , frameon=False)
ax = fig.add_subplot(111)

#Remove axes
ax.axis('off')

#Add walls
bottom = 0.1
top = 0.9
ax.add_patch(patches.Rectangle( (0.0, 0.0), 2.0, bottom, color='gray', fill=True) )
ax.add_patch(patches.Rectangle( (0.0, top), 2.0, 0.1, color='gray', fill=True) )

#Setup arrows
head_size = head_length = 0.05
u0 = 1.70
y_vals = np.linspace( top, bottom, 10, endpoint = False)
y_vals = y_vals[1:]
u_vals =  np.array( [u0 * (y-bottom)/(top-bottom) for y in y_vals])

#draw wall arrow
ax.arrow(0.1, 0.95, u0, 0.0, head_width=head_size, head_length=head_size, fc='k', ec='k')

#Draw arrows in the fluid
for y, u in zip(y_vals, u_vals):
    ax.arrow(0.1, y, u, 0.0, head_width=head_size, head_length=head_size, fc='k', ec='k')


ax.text(1.88, .94, r'$u_0$', fontsize=40)

ax.set_xlim(0,2.0)
ax.set_ylim(0,1.0)

#plt.show()
plt.savefig('../images/couette.svg', transparent = True)
