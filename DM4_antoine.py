#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import floor, log10

for p in range(2, 28):
    for q in range(3, 29):
        if p < q:
            if floor(log10(p**q)) + 1 == floor(log10(q**p)) + 1:
                print(p, q)
 
#                print(len(str(p**q)), len(str(q**p)))