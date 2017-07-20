#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Wool(wool@wool.pe.kr)
"""

from numpy import *
import matplotlib.pyplot as plt

t = 10000

def randwalk(p):    
    x = []
    s = []
    av_x = []
    av_xx = []
    
    p_critic = p
    
    x.extend([0])
    s.extend([0])
    av_x.extend([0])
    av_xx.extend([0])
                
    
    
    for i in range(1, t):
        sum_x = 0
        sum_xx = 0
        if( random.rand() < p_critic ):
            r = random.randint(0,i);
            s_next = s[r]
        else:
            r = random.rand()
            if( r < 0.5 ):
                s_next = +1
            else:
                s_next = -1
                
        s.extend([s_next])
        x.extend([x[i-1]+s[i]])
        
        for j in range(0,i):
            sum_x = x[j] + sum_x
            sum_xx = sum_xx + x[j] * x[j]
            
        av_x.extend([ (sum_x / i)*(sum_x / i)])
        av_xx.extend([sum_xx / i])
        
    for i in range(0, t, 100):
        #plt.plot(i, x[i], 'ro')
        plt.plot(i, av_xx[i] - av_x[i], 'x')
    
     
plt.axis([10, t, 10, t*1000])

randwalk(0.4)
randwalk(0.6)
randwalk(0.8)
plt.xscale('log')  
plt.yscale('log')  
plt.show()