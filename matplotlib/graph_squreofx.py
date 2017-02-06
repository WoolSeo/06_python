# -*- coding: utf-8 -*-
"""
Spyder Editor
한글도 되나요?? ㅎㅎㅎ 잘되넹...
This is a temporary script file.
"""
import random
import matplotlib
import matplotlib.pyplot as plt

x = 500
y = 500

plt.axis([0, 1000, 0, 1000])
plt.grid(True)
      
for i in range(0,100000):
    dir = random.randint(0,3)
    if dir == 0:
        x = x + 1
    elif dir == 1:
        x = x - 1
    elif dir == 2:
        y = y + 1
    elif dir == 3:
        y = y - 1
    plt.plot(x, y, 'ro')
    
plt.show()
