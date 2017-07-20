# -*- coding: utf-8 -*-
"""
1D - Randomwalk with Memory Effect : Kim Model

This is a temporary script file.

@author: Wool(wool@wool.pe.kr)

"""

import random
import matplotlib
import matplotlib.pyplot as plt


p = 0.4
q = 1-p
target_t = 100
t = 0
X_0 = target_t/2
dis=[]
memory=[]
total_realization = 10000


for i in range(0, target_t):
    dis.extend([0])
    memory.extend([0])

for j in range(0, total_realization):
    for i in range(0, target_t):
        memory.extend([0])   

    x = X_0
    dis[x] = 1
    if ( random.random() < 0.5 ):
        memory[t] = 1
    else:
        memory[t] = -1
    x = x + memory[t]
    dis[x] = dis[x] + 1
    
    t = t+1
    
    if( random.random() < p ):
        memory[t] = memory[t-1]
    else:
        if ( random.random() < 0.5 ):
            memory[t] = 1
        else:
            memory[t] = -1
        
    x = x + memory[t]
    dis[x] = dis[x] + 1
    
    t = t+1
    
    
    for i in range(2, target_t):
        if( random.random() < p ):
            memory[i] = memory[random.randint(0,i-1)]
        else:
            if ( random.random() < 0.5 ):
                memory[i] = 1
            else:
                memory[i] = -1
        x = x + memory[i]
        dis[x] = dis[x] + 1


plt.axis([-target_t/2, target_t/2, 0, target_t*13])
plt.grid(True)


expect_x = 0
expect_x2 = 0
for i in range(0,len(dis)):
    #if(dis[i] != 0):
        plt.plot(i-X_0, dis[i], 'ro')
        expect_x = expect_x + dis[i] / total_realization * (i-X_0)
        expect_x2 = expect_x2 + dis[i] / total_realization * (i-X_0) * (i-X_0)
        
expect_x = expect_x * expect_x
print(expect_x)
print("   ")
print(expect_x2)
print("   ")
print(expect_x2 - expect_x)

    
title = 'RandomWalk with Memory Effect : Kim Model'
plt.xlabel('$t$', fontsize=20)
plt.ylabel('$< {x_t}^2>$', fontsize=20)
plt.title(title)
    
plt.show()