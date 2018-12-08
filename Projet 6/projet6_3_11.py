#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 20:01:04 2018

@author: mathieu
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

data = np.loadtxt('Projet 6/PROJET6.3/FRF.txt')[1:,]
fq   = data[:, 0]
real = data[:, 1]
imag = data[:, 2]
mod  = np.sqrt(real**2 + imag**2)
phas = np.arctan2(real, imag)

fig, ax = plt.subplots(2, 1)
ax[0].plot(fq, mod)
ax[0].set_title('Module')
ax[0].grid(True)

ax[1].plot(fq, phas)
ax[1].set_title('Phase')
ax[1].grid(True)
plt.show()