#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 09:50:08 2018

@author: mathieu
"""

import numpy as np

mat = np.zeros((10, 10))
for i in range(len(mat[0,:])):
    for j in range(len(mat[:,0])):
        if i == j:
            mat[i, j] = 99
        if j > i:
            mat[i, j] = 8
        if j < i:
            mat[i, j] = 1

print(mat)