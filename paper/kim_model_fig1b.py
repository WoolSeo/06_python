#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Wool(wool@wool.pe.kr)
"""

from numpy import *
import matplotlib.pyplot as plt

N = 100
t_max = 100000
p = 0.5
cnt = 0

store_t = []
store_xx = []
store_x = []

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
        
        #t=2
        if( random.rand() < p ):
            s_next = s[0]
        else:
            r = random.rand()
            if( r < 0.5 ):
                s_next = +1
            else:
                s_next = -1
        x = x + s_next
        s.append(s_next)
        
        #t>=2
        for i in range(2, t):
            if( random.rand() < p ):
                r = random.randint(0,i);
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
        #expect_x = expect_x + (-1*t+i)*n[i]*1.0/N
        print(i,expect_xx)
    
    #print(expect_xx - expect_x*expect_x)
    store_t.append(t)
    store_xx.append(expect_xx/t)
    #store_x.append(expect_x*expect_x)


for k in range(10, t_max, 100):
    randwalk(k)
    cnt = cnt + 1

for l in range(1, cnt):
    plt.plot(store_t[l], store_xx[l], 'ro')

plt.axis([10, t_max, 10, 1000])
plt.xscale('log')  
plt.yscale('log')  
plt.xlabel('$t$', fontsize=15)
plt.ylabel('$< {x_t}^2> / t$', fontsize=15)
#plt.title(title)

plt.show()