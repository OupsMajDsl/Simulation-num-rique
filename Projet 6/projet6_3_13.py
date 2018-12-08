#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

rate = wavfile.read('Projet 6/PROJET6.3/countdown_stereo.wav')[0]
data = wavfile.read('Projet 6/PROJET6.3/countdown_stereo.wav')[1]
t1 = np.linspace(0, len(data)/rate, len(data))


fig, ax = plt.subplots()
ax.plot(t1, data)
plt.show()