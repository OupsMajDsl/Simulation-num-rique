#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 18:18:24 2018

@author: mathieu
"""

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.size'] = 11
plt.rcParams['font.family'] = 'serif'


A       = 1
x       = np.linspace(0, 1, 1000)
f       = 340
T       = 1/f
w       = 2*np.pi*f
c       = 340
k       = w/c
t_var   = np.linspace(0, T, 16)
fig, ax = plt.subplots(2, 1)


for t in t_var:
    ax[0].plot(x, A* np.cos(w* t - k* x), 'k-')
    ax[1].plot(x, A* np.cos(k* x)* np.cos(w* t), 'k-')

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


plt.show()
