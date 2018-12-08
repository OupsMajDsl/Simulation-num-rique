#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 20:01:04 2018

@author: mathieu
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile


rate, data = wavfile.read('Projet 6/PROJET6.3/chirp.wav')
t1 = np.linspace(0, len(data)/rate, len(data))
#2e chirp: 1.75 --> 4

def find_nearest(array, value):         #https://stackoverflow.com/questions/2566412/find-nearest-value-in-numpy-array
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]

debut = find_nearest(t1, 1.75)
fin   = find_nearest(t1, 4)
for i in range(len(t1)):
    if debut == t1[i]:
        i_dbt = i
    if fin == t1[i]:
        i_fin = i

chirp = data[i_dbt:i_fin]
reverse_chirp = chirp[::-1]
wavfile.write('Projet 6/PROJET6.3/prihc.wav', 44100, reverse_chirp)

fig, ax = plt.subplots()
ax.plot(t1[i_dbt:i_fin], reverse_chirp)
ax.grid(True)
plt.show()