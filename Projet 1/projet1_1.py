#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 09:05:55 2018

@author: mathieu
"""

s1    = input("Entrez un texte:")
f     = float(input("Entrez un nombre réel:"))
vowel = ["a", "e", "i", "o", "u", "y"] 
for i in s1:
    if i in vowel:
        s2 = s1.replace(i, "?")
#s2 = s1.replace("a", "?").replace("e", "?").replace("i", "?").replace("o", "?").replace("u", "?").replace("y", "?")

print("La partie entière de {} est {}.".format(f, int(f)))
print("La chaîne de caractère '{}' sans voyelles répétée {} fois prend la forme: \n{}".format(s1, int(f), s2*int(f)))