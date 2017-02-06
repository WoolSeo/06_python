#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2D - Randomwalk

used array

Created on Tue Jan 17 23:21:43 2017

@author: Wool(wool@wool.pe.kr)
"""

import random
import matplotlib
import matplotlib.pyplot as plt

x = []
y = []
count = 1000
width = 50

x.extend([0])
y.extend([0])

for i in range(1, count):
    x.extend([x[i-1] + random.randint(-1,1)])
    y.extend([y[i-1] + random.randint(-1,1)])
    
    
plt.axis([-width, width, -width, width])
plt.grid(True)

plt.xlabel('x')
plt.ylabel('y')
plt.title('2-D RandomWalk')
      
for i in range(0,count):
    plt.plot(x[i], y[i], 'ro')
    
plt.show()