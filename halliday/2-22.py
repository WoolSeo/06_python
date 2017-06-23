# -*- coding: utf-8 -*-
"""
Halliday physics

Chapter2, Problem18

@author: Wool(wool@wool.pe.kr)
"""

import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0.,1.5,0.01)
x = 3* t**2 - 2* t**3
v = 6*t - 6* t**2
a = 6 - 12*t

plt.subplot(311)
plt.plot(t,x)
plt.ylabel('$x[\\rm{m}]$')
plt.grid(True)

plt.subplot(312)
plt.plot(t,v)
plt.xlabel('t[s]')
plt.ylabel('$v[\\rm{m/s}]$')
plt.grid(True)

plt.subplot(313)
plt.plot(t,a)
plt.xlabel('$t[\\rm{s}]$')
plt.ylabel('$a[\\rm{m/s^2}]$')
plt.grid(True)

plt.show()