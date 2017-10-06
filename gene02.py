#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 23:23:04 2017

@author: woolseo
"""
import random

#목표 유전자
a = 5
b = 3
c = 4

#현재 유전자
x = 0
y = 0
z = 0

#세대
i = 1

while (a != x) or (b != y) or (c != z)  :    
    x = random.randint(1,6)
    y = random.randint(1,6)
    z = random.randint(1,6)
        
    print(i, x, y, z)
    i = i + 1