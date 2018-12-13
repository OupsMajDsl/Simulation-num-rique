import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
plt.rcParams['font.family'] = 'serif'

fig, ax = plt.subplots()
lines   = []
t       = np.linspace(0, 1, 1000)
f_var   = np.arange(0, 25, 0.1)

for f in f_var:
    line = ax.plot(t, np.sin(2*np.pi*f*t), 'k-', animated = True)
    lines.append(line)

ax.axis([0, 1, -1, 1])
ax.set_yticks([-1, 0, 1])
ax.set_yticklabels([r"$-A$", r"$0$", r"$A$"])
ax.set_xticks([0, 0.5, 1])
ax.set_xticklabels([r"$0$", r"$t/2$", r"$t$"])
ax.grid()    

ani = animation.ArtistAnimation(fig, lines, interval = 200, blit = True)

plt.show()