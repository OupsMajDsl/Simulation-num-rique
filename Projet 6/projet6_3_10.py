#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 20:01:04 2018

@author: mathieu
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

rate, data = wavfile.read('Projet 6/PROJET6.3/moteurdiesel.wav')
t1 = np.linspace(0, len(data)/rate, len(data))

gauche = data[:, 0]
droite = data[:, 1]
if gauche.tolist() == droite.tolist():
    print('gauche == droite')

wavfile.write('Projet 6/PROJET6.3/dieseldroite.wav', 44100, droite)
wavfile.write('Projet 6/PROJET6.3/dieselgauche.wav', 44100, gauche)


fig, ax = plt.subplots()
ax.plot(t1, gauche, alpha = 0.5)
ax.plot(t1, droite, alpha = 0.5)
ax.grid(True)
plt.show()
print(data)