#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Wool(wool@wool.pe.kr)
"""

from numpy import *
import matplotlib.pyplot as plt
import numpy as np

N = 100
t_max = 1000
p = 0.3
cnt = 0
multi = 10;

store_t = []
store_xx = []
store_x = []
vari = []

def randwalk(t):
    
    n = []
    
    for i in range(0, 2*t+1):
        n.append(0)
    
    #N번 시행
    for j in range(1, N):
        x = 0
        s = []
        
        #t=1
        r = random.rand()
        if( r < 0.5 ):
            s_next = +1
        else:
            s_next = -1
        
        x = x + s_next
        s.append(s_next)
        
        """#t=2
        if( random.rand() < p ):
            s_next = s[0]
        else:
            r = random.rand()
            if( r < 0.5 ):
                s_next = +1
            else:
                s_next = -1
        x = x + s_next
        s.append(s_next)"""
        
        #t>1
        for i in range(1, t):
            if( random.rand() < p ):
                r = random.randint(0,i)
                s_next = s[r]
            else:
                r = random.rand()
                if( r < 0.5 ):
                    s_next = +1
                else:
                    s_next = -1
            
            x = x + s_next
            s.append(s_next)
        
        n[x+t] = n[x+t] + 1     
        #print(x)
    
    expect_x = 0.
    expect_xx = 0.
    
    for i in range(0, 2*t+1):
        #print(i,-1*t+i,n[i])
        expect_xx = expect_xx + (-1*t+i)*(-1*t+i)*n[i]*1.0/N
        expect_x = expect_x + (-1*t+i)*n[i]*1.0/N
        #print(i,expect_xx, expect_x*expect_x)
    
    print(expect_xx - expect_x*expect_x)
    store_t.append(t)
    store_xx.append(expect_xx)
    store_x.append(expect_x*expect_x)
    vari.append(np.var(expect_x))

for k in range(10, t_max, multi):
    randwalk(k)
    cnt = cnt + 1
    if( (k % multi) == 0 ):
        multi = multi * 10
    

for l in range(2, cnt):
    plt.plot(store_t[l], store_xx[l]-store_x[l], 'bo')
    plt.plot(store_t[l], vari[l], 'ro')

plt.axis([10, t_max, 10, t_max*t_max])
plt.xscale('log')  
plt.yscale('log')  
plt.xlabel('$t$', fontsize=15)
plt.ylabel('$< {x_t}^2> - {< x_t >}^2$', fontsize=15)
#plt.title(title)

plt.show()

print(cnt);