#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#import numpy as np
#from matplotlib import pyplot as plt
#from matplotlib import animation
#
#fig, ax = plt.subplots(figsize = (5, 3))
#
#t   = np.linspace(0, 1, 1000)
#f_var   = np.linspace(0, 25, 1)
#
#
#lines = []
#for f in f_var:
#    line = ax.plot(t, np.sin(2*np.pi*f*t), 'k-')
#    lines.append(line)
#
#def animate (i):
#    line.set_data(lines[i])
#
#
#anim = animation.FuncAnimation(
#    fig, animate, interval=100, frames=500)
# 
#plt.draw()
#plt.show()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
# plt.style.use('ggplot')
fig, ax = plt.subplots(figsize=(5, 3))
ax.set(xlim=(-3, 3), ylim=(-1, 1))
x = np.linspace(-3, 3, 91)
t = np.linspace(1, 25, 30)
X2, T2 = np.meshgrid(x, t)
 
F = np.sin(2*np.pi*T2/T2.max())

line = ax.plot(x, F[0, :])[0]
def animate(i):
    line.set_ydata(F[i, :])

anim = FuncAnimation(
        fig, animate, interval=100, frames=len(t)-1)
 
plt.draw()
plt.show()
