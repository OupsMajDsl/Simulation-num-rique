#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 20:01:04 2018

@author: mathieu
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

audio = wavfile.read('Projet 6/PROJET6.3/countdown1.wav')
rate  = audio[0]
data  = audio[1]
len_file   = len(data)
temps      = np.linspace(0, len_file/rate, len_file)
duree      = temps[-1]

# amplitude = []
# for i in range(len_file):
#     amplitude.append(data[i])

print("échantillonnage = ", rate, "Hz")
print("nb éléments = ", len_file)
print("Durée = ", duree, "s")
fig, ax = plt.subplots()
ax.plot(temps, data)
ax.grid(True)
plt.show()