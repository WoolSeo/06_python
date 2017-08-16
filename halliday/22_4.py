# -*- coding: utf-8 -*-
"""
Halliday physics

@author: Wool(wool@wool.pe.kr)
"""

import numpy as np
import matplotlib.pyplot as plt

e = 8.85*10**(-12)
R = 0.01
z = np.arange(0.,0.5,0.001)
q = 1
pi = 3.14

E = q*z/(4*pi*e*(z*z+R*R)**(3/2))


plt.plot(z,E, label='$v_1$' )

plt.title('The electric field due to a ring charge ', fontsize=14)
plt.xlabel('$z[\\rm{m}]$', fontsize=20)
plt.ylabel('$E[\\rm{N/C}]$', fontsize=20)
#plt.grid(True)

plt.legend()
plt.show()