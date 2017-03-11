# -*- coding: utf-8 -*-
"""
Halliday physics

Chapter2, Problem5 - g

@author: Wool(wool@wool.pe.kr)
"""

import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0.,4.,0.01)
x = 3*t - 4 * t**2 + t**3

plt.axis([0,5,-5,15])
plt.plot(t,x,linewidth=2.)
plt.plot([2,4],[-2,12],color='black',linestyle='dashed')
plt.scatter([2,4],[-2,12],color='black')
plt.xlabel('t[s]')
plt.ylabel('x[m]')
plt.show()