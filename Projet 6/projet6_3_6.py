#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 20:01:04 2018

@author: mathieu
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile


rate, data = wavfile.read('Projet 6/PROJET6.3/countdown1.wav')
fs_faster  = int(rate* 1.33)
fs_slower  = int(rate* 0.66)


wavfile.write('Projet 6/PROJET6.3/faster.wav', fs_faster, data)
wavfile.write('Projet 6/PROJET6.3/slower.wav', fs_slower, data)