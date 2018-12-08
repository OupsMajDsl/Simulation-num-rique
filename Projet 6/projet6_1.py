#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 20:01:04 2018

@author: mathieu
"""
import numpy as np
import matplotlib.pyplot as plt

nb_file = 19
lg_file = len(np.loadtxt("Projet 6/PROJET6.1/mes1.dat")[:, 0])
ampl    = np.zeros((nb_file, lg_file))
phas    = np.zeros((nb_file, lg_file))

for k_file in range(1, nb_file + 1):
    filename         = "Projet 6/PROJET6.1/mes{}.dat".format(k_file)
    file_load        = np.loadtxt(filename)
    real             = file_load[:, 2]
    imag             = file_load[:, 1]
    ampl[k_file - 1] = np.sqrt(real**2 + imag**2)
    phas[k_file - 1] = np.arctan2(real, imag)
    if k_file == 1:
        fq = file_load[:, 0]

fig, ax = plt.subplots(2, 1)            #tracé linéaire
for i in range(len(ampl[:, 0])):
    ax[0].plot(fq, ampl[i], alpha = 0.3)
    ax[1].plot(fq, phas[i], alpha = 0.3)
plt.show()
    
fig, ax = plt.subplots(2, 1)            #tracé db + phase déroulée
for i in range(len(ampl[:, 0])):
    ampl_db = 20* np.log10(ampl[i])
    ax[0].plot(fq, ampl_db)
    ax[1].plot(fq, np.unwrap(phas[i]))
plt.show()

fig, ax = plt.subplots(2, 1)            #tracé écart-type
std_ampl = []
std_phas = []
for i in range(lg_file):
    std_ampl.append( ((np.std(ampl[:, i])) /np.mean(ampl[:, i])* 100))
    std_phas.append( np.abs((np.std(phas[:, i]))/np.mean(phas[:, i])* 100))
ax[0].plot(fq, std_ampl)
ax[0].axis([0, 1000, 0, 30])
ax[0].set_title('Ecart-type relatif en %')
ax[1].plot(fq, std_phas)
ax[1].axis([0, 1000, 0, 100])

plt.show()
