# -*- coding: utf-8 -*-
"""
1D - Randomwalk

This is a temporary script file.

@author: Wool(wool@wool.pe.kr)

"""

import random
import matplotlib
import matplotlib.pyplot as plt

y = 0

plt.axis([0, 100, -30, 30])
plt.grid(True)
    
for i in range(0,100):
        dir = random.randint(0,1)
        if dir == 0:
            y = y + 1
        elif dir == 1:
            y = y - 1   
        plt.plot(i, y, 'ro')
y=0
    
for i in range(0,100):
        dir = random.randint(0,1)
        if dir == 0:
            y = y + 1
        elif dir == 1:
            y = y - 1   
        plt.plot(i, y, 'bs')
y=0

for i in range(0,100):
        dir = random.randint(0,1)
        if dir == 0:
            y = y + 1
        elif dir == 1:
            y = y - 1   
        plt.plot(i, y, 'g^')
y=0

for i in range(0,100):
        dir = random.randint(0,1)
        if dir == 0:
            y = y + 1
        elif dir == 1:
            y = y - 1   
        plt.plot(i, y, 'y^')
y=0
    
plt.xlabel('Time')
plt.ylabel('x')
plt.title('1-D RandomWalk')
    
plt.show()