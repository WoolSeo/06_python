# -*- coding: utf-8 -*-
"""
Halliday physics

Chapter2, Problem2 - c - b

@author: Wool(wool@wool.pe.kr)
"""

import matplotlib.pyplot as plt

plt.axis([0,130,0,300])
plt.plot([0,60,120],[0,1.22*60,3.05*60+1.22*60])
plt.plot([0,120],[0,3.05*60+1.22*60])
plt.xlabel('t[s]')
plt.ylabel('x[m]')
plt.show()