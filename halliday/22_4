# -*- coding: utf-8 -*-
"""
Halliday physics

Chapter2, Problem46

@author: Wool(wool@wool.pe.kr)
"""

import numpy as np
import matplotlib.pyplot as plt

g = 9.81
t_1 = np.arange(0.,3.31,0.01)
t_2 = np.arange(1.,3.31,0.01)

h_1 = 0.5 * g * t_1**2
h_2 = 11.9 * (t_2 - 1) + 0.5 * g * (t_2-1)**2
v_1 = g*t_1
v_2 = 11.9 + g * (t_2 - 1)

plt.plot(t_1,v_1, label='$v_1$' )
plt.plot(t_2,v_2, linestyle='dashed',label='$v_2$')

plt.title('halliday physics, Ch2-54', fontsize=14)
plt.xlabel('$t[\\rm{s}]$', fontsize=20)
plt.ylabel('$v[\\rm{m/s}]$', fontsize=20)
plt.grid(True)

plt.legend()
plt.show()