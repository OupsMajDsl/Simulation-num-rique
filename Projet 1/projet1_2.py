#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 09:24:38 2018

@author: mathieu
"""

import numpy as np
import matplotlib.pyplot as plt 

x    = np.linspace(0,2*np.pi, 1000)
f_1  = np.sin(x)*np.exp(-x)
f_2  = np.sin(x)*np.exp(-2* x)
f_3  = np.cos(x)*np.exp(-x)
f_4  = np.cos(x)*np.exp(-2*x)

plt.figure(figsize = (15,10))
plt.subplot(211)
plt.plot(x, f_1, 'k--', label = "$f_1(x)$")
plt.plot(x, f_2, 'r-.', label = "$f_2(x)$")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.legend()

plt.subplot(212)
plt.plot(x, f_3, 'k--', label = "$f_3(x)$")
plt.plot(x, f_4, 'r-.', label = "$f_4(x)$")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.legend()

plt.savefig("projet1_2.pdf")
plt.show()