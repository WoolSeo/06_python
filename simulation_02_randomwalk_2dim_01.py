#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2D - Randomwalk

used array, color

Created on Tue Jan 17 23:21:43 2017

@author: Wool(wool@wool.pe.kr)
"""

import random
import matplotlib
import matplotlib.pyplot as plt

x = []
y = []
colors=[]

count = 1000
width = 50

def colorarray(c):
    color = 0x000000
    for i in range(0, c):
        temp = str("%x"%color)
        if( len(temp) != 6):
            for j in range(0, 6-len(temp)):
                temp = "0" + temp
        temp = "#"+temp
        colors.extend([temp])
        color = color + 1

colorarray(count)

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
    plt.scatter(x[i], y[i], color=(str(i*0.001)))
    print i

    
plt.show()