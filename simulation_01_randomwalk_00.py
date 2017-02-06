#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Randomwalk

Created on Tue Jan 17 23:21:43 2017

@author: Wool(wool@wool.pe.kr)
"""

import random
import matplotlib
import matplotlib.pyplot as plt

x = 500
y = 500

plt.axis([0, 1000, 0, 1000])
plt.grid(True)
      
for i in range(0,10000):
    dir = random.randint(0,3)
    if dir == 0:
        x = x + 1
    elif dir == 1:
        x = x - 1
    elif dir == 2:
        y = y + 1
    else:
        y = y - 1
    plt.plot(x, y, 'ro')
    
plt.show()