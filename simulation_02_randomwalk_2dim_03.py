#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2D - Randomwalk

used array, color

Created on Tue Jan 31 2017

@author: Wool(wool@wool.pe.kr)
"""

from numpy import *
import matplotlib
import matplotlib.pyplot as plt

x = []
y = []
colors=[]

count = 750
width = 6000
walk = 100
flight = 2000

def colorarray(c):
    r = 0x00
    g = 0x00
    b = 0x00
    
    for i in range(0, c):
        if( b != 0xff ):
            temp = str("%x"%b)    
            if( len(temp) != 2):
                temp = "0" + temp
            temp = "#0000"+temp
            colors.extend([temp])
            b = b + 1
        elif( g != 0xff):
            temp = str("%x"%g)    
            if( len(temp) != 2):
                temp = "0" + temp
            temp = "#00"+ temp +"00"
            colors.extend([temp])
            g = g + 1
        else:
            temp = str("%x"%r)    
            if( len(temp) != 2):
                temp = "0" + temp
            temp = "#"+temp +"0000"
            colors.extend([temp])
            r = r + 1
        

colorarray(count)

x.extend([0])
y.extend([0])

c_flight = 0
for i in range(1, count):
    temp = random.random()
    if( temp > 0.01):
        x.extend([x[i-1] + random.randint(-walk,walk)])
        y.extend([y[i-1] + random.randint(-walk,walk)])
    else:
        x.extend([x[i-1] + random.randint(-flight,flight)])
        y.extend([y[i-1] + random.randint(-flight,flight)])
        c_flight = c_flight + 1

print(c_flight)
    
    
plt.axis([-width, width, -width, width])
plt.grid(True)

plt.xlabel('x')
plt.ylabel('y')
plt.title('2-D RandomWalk')
      
for i in range(0,count):
    #plt.scatter(x[i], y[i], color=colors[i])
    plt.plot(x[i], y[i],'o', color=colors[i])
    plt.plot(x[i], y[i],lw=1)
    
plt.show()