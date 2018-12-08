#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 00:50:20 2018

@author: mathieu
"""
import numpy as np

freq    = 1001
nb_file = 50
delta_f = 5000/4096
lg_file = len(np.loadtxt("kundt1.txt")[:, 0])
fq      = np.arange(0, lg_file*delta_f, delta_f)


def find_nearest(array, value):         #https://stackoverflow.com/questions/2566412/find-nearest-value-in-numpy-array
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]


elt = find_nearest(fq, freq)
#[row, col]

for i in range(lg_file):
    if elt == fq[i]:
        indice = i
#    print(fq[i])
