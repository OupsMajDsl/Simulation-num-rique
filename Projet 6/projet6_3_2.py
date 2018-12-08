#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 20:01:04 2018

@author: mathieu
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

audio1 = wavfile.read('Projet 6/PROJET6.3/countdown1.wav')
audio2 = wavfile.read('Projet 6/PROJET6.3/countdown2.wav')
rate  = audio1[0]

data1 = audio1[1]
data2 = audio2[1] 
len_file1   = len(data1)
len_file2   = len(data2)
t1 = np.linspace(0, len_file1/rate, len_file1)
t2 = np.linspace(0, len_file2/rate, len_file2)
duree1 = t1[-1]
duree2 = t2[-1]


# amplitude = []
# for i in range(len_file):
#     amplitude.append(data[i])
print("échantillonnage = ", rate, "Hz")
print("nb éléments = ", len_file1, len_file2)
print("Durée = ", duree1, "s", duree2, 's')
fig, ax = plt.subplots()
ax.plot(t1, data1, t2, data2)
ax.grid(True)
plt.show()