# -*- coding: utf-8 -*-
"""
1D - Randomwalk with Memory Effect : Gunter Model

This is a temporary script file.

@author: Wool(wool@wool.pe.kr)

"""

import random
import matplotlib
import matplotlib.pyplot as plt

def randwalk(p_, q_, a_):
    p = p_
    q = q_
    a = a_
    target_t = 1000
    t = 0
    X_0 = target_t/2
    dis=[]
    memory=[]
    
    
    for i in range(0, target_t):
        dis.extend([0])
        memory.extend([0])
    
    for j in range(0, 500):
        for i in range(0, target_t):
            memory.extend([0])   
    
        x = X_0
        dis[x] = 1
        if ( random.random() < q ):
            memory[t] = 1
        else:
            memory[t] = -1
        x = x + memory[t]
        dis[x] = dis[x] + 1
        
        t = t+1
        
        if( random.random() < p ):
            memory[t] = memory[t-1]
        else:
            memory[t] = memory[t-1] * -1
            
        x = x + memory[t]
        dis[x] = dis[x] + 1
        
        t = t+1
        
        
        for i in range(2, target_t):
            if( random.random() < p ):
                memory[i] = memory[random.randint(0,i-1)]
            else:
                memory[i] = memory[random.randint(0,i-1)] * -1
            x = x + memory[i]
            dis[x] = dis[x] + 1
    
    
    plt.axis([-target_t/2, target_t/2, 0, target_t*20])
    plt.grid(True)
        
    for i in range(0,len(dis)):
        #if(dis[i] != 0):
        name, = plt.plot(i-X_0, dis[i], a, label='hi')
    return(name)
#(p, q, spot)
name1 = randwalk(0.2, 0.2, 'yo')
name2 = randwalk(0.5, 0.2, 'ro')
name3 = randwalk(0.9, 0.2, 'bo')
#title = 'RandomWalk with Memory Effect : Gunter Model ( p=' + str(p) +' q=' + str(q) + ' )'
plt.xlabel('x')
plt.ylabel('frequency')
#plt.title(title)
plt.title('RandomWalk with Memor    y Effect : Gunter Model')
plt.legend([name1, name2, name3], ["q=0.2", "q=0.5", "q=0.8"]) 
   
    
plt.show()