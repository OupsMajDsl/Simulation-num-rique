#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 19:42:01 2018

@author: mathieu
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
t       = np.linspace(0, 1, 2000)
x       = np.zeros_like(t)
line,   = ax.plot(t, x)

def animate(i):
    line.set_data(t, np.sin(2* np.pi* t* i))
    return line,

ax.axis([0, 1, -1, 1])
ax.set_yticks([-1, 0, 1])
ax.set_yticklabels([r"$-A$", r"$0$", r"$A$"])
ax.set_xticks([0, 0.5, 1])
ax.set_xticklabels([r"$0$", r"$t/2$", r"$t$"])
ax.grid()    
ani = animation.FuncAnimation(fig, animate, frames = np.arange(0, 25, 0.01), interval = 10, blit = True)

plt.show()
