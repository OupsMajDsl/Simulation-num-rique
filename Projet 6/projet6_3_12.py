#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 20:01:04 2018

@author: mathieu
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

data1 = wavfile.read('Projet 6/PROJET6.3/countdown1.wav')[1]
rate, data2 = wavfile.read('Projet 6/PROJET6.3/countdown2.wav')
t1 = np.linspace(0, len(data1)/rate, len(data1))


data2 = data2.tolist()
while len(data1) != len(data2):
    data2.append(0)

stereo = np.zeros((len(data1), 2))
for j in range(len(data1)):
    stereo[j, 0] = data2[j]
    stereo[j, 1] = data1[j]

fig, ax = plt.subplots()
ax.plot(t1, stereo)
plt.show()

wavfile.write('Projet 6/PROJET6.3/countdown_stereo.wav', 44100, np.asarray(stereo))