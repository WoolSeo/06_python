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
plt.plot(t,x,color='green', linewidth=2.)
plt.plot([2,4],[-2,12],color='red',linestyle='dashed')
plt.grid(True)
plt.xticks([0,2,4])
plt.yticks([-2,0,12])
plt.show()