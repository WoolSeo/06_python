# -*- coding: utf-8 -*-
"""
Halliday physics

@author: Wool(wool@wool.pe.kr)
"""

import numpy as np
import matplotlib.pyplot as plt

E = 3.0
R = 1000.0
C = 0.001
t = np.arange(0.,5.0,0.001)

V = E*(1.0 - np.exp(-t/(R*C)))

plt.plot(t, V )

#plt.title('The electric field due to a ring charge ', fontsize=14)
plt.xlabel('$t[\\rm{s}]$', fontsize=20)
plt.ylabel('$V_C [\\rm{V}]$', fontsize=20)
plt.axis([0,5,0,3.2])
plt.grid(True)

plt.legend()
plt.show()