import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
plt.rcParams['font.size'] = 11
plt.rcParams['font.family'] = 'serif'

A       = 1
x       = np.linspace(0, 1, 50)
f       = 340
T       = 1/f
w       = 2*np.pi*f
c       = 340
k       = w/c
t_var   = np.linspace(0, T, 100)
lines   = []
fig, ax = plt.subplots(2, 1)


for t in t_var:
    line0, = ax[0].plot(x, A* np.cos(w* t - k* x), 'k')
    line1, = ax[1].plot(x, A* np.cos(k* x)* np.cos(w* t), 'k')
    lines.append([line0, line1])

for i in range(len(ax)):
    ax[i].grid()
    ax[i].axis([0, 1, -1, 1])
    ax[i].set_yticks([-1, -1/2, 0, 1/2, 1])
    ax[i].set_yticklabels([r"$-A$", r"$-A/2$", r"$0$", r"$A/2$", r"$A$"])
    ax[i].set_xticks(np.arange(0, 1+0.1, 0.25))
ax[1].set_xlabel (r"$x$")
ax[0].set_ylabel(r"$P_p(x)$")
ax[1].set_ylabel(r"$P_s(x)$")
ax[0].set_xticklabels([])
ax[1].set_xticklabels([r"$0$", r"$L/4$", r"$L/2$", r"$3L/4$", r"$L$"])

ani = animation.ArtistAnimation(fig, lines, interval = 40, blit = True)
plt.show()