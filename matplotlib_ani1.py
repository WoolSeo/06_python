#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 22:53:14 2017

@author: woolseo
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
 
 
fig, ax = plt.subplots()
 
ax.set(xlim=[0, 10], ylim=[0, 5])
ax.set_aspect('equal', adjustable='box')
ax.grid(True)
 
g = 9.81
v0 = 10
theta = np.pi/3
 
projectile, = ax.plot([], [], 'ro')
 
 
def animate(i):
    t = 0.02 * i
    x = v0 * np.cos(theta) * t
    y = v0 * np.sin(theta) * t - 0.5 * g * t**2
 
    projectile.set_data(x, y)
    return projectile,
 
 
anim = animation.FuncAnimation(fig, animate,
                               frames=100, interval=20)