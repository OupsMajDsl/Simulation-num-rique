#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 10:09:05 2018

@author: mathieu
"""
import numpy as np

def pair(mini, maxi):
    liste_pair = np.arange(mini, maxi+1, 2).tolist()
    return liste_pair

def pair2(mini, maxi):
    liste_pair = [i for i in range(mini, maxi+1) if i% 2 == 0]
    return liste_pair

if __name__=="__main__":
    pair  = pair(2, 14)
    pair2 = pair2(2, 14)
    print(pair)
    print(pair2)
    
    print(pair == pair2)
    print(type(pair), type(pair2))