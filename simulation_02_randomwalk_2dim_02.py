#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2D - Randomwalk

used array

@author: Wool(wool@wool.pe.kr)
"""

import random
import matplotlib
import matplotlib.pyplot as plt

x = []
y = []
count = 1000
width = 100

x.extend([0])
y.extend([0])

for i in range(1, count):
    temp = random.randint(-1,1)
    if temp < 0:
        x.extend([x[i-1] - 1 ])
    else:
        x.extend([x[i-1] + 1 ])
    y.extend([y[i-1] + random.randint(-1,1)])
    
    
    
plt.axis([-width, width, -width, width])
plt.grid(True)

plt.xlabel('x')
plt.ylabel('y')
plt.title('2-D RandomWalk')
      
for i in range(0,count):
    plt.scatter(x[i], y[i], color=(str(i*0.001)))
    
plt.show()