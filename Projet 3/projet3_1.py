#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 17:28:18 2018

@author: mathieu
"""

import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.family'] = 'serif'

x = np.linspace(-np.pi, 4*np.pi, 1000)
fx = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, fx, 'k-')
ax.set_xlabel (r"$x$")
ax.set_ylabel (r"$f(x)$")

ax.set_yticks([-1, 0, 1])
ax.set_yticklabels([r"$-A$", r"$0$", r"$A$"])
ax.set_xticks(np.arange(-np.pi, 4*np.pi+1, np.pi))
ax.set_xticklabels([r"$-\pi$", r"$0$", r"$\pi$", r"$2 \pi$", r"$3 \pi$", r"$4 \pi$"], rotation = 45)

plt.grid()
plt.show()