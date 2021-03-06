#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 21:34:55 2017

@author: woolseo
"""

import numpy as np
import matplotlib.pyplot as plt
#import numpy as np

N = 100
t_max = 10000
p = 0.3
cnt = 0
multi = 1
a = 1
k=1


store_xx = np.array([])

vari = np.array([])



def randwalk(t):
    
    store_x = np.zeros(t_max)
    store_t = np.arange(t_max)
    #N번 시행
    for j in range(1, N):
        x = np.array([])
        s = np.array([])
        
        #t=1
        if( np.random.random() < 0.5 ):
            s_next = +1
        else:
            s_next = -1
        
        x = np.insert(x,0,s_next)
        s = np.insert(s,0,s_next)
        
      
        #t>1
        for i in range(1, t_max):
            if( np.random.random() < (1/(t**a)) ):
                r = np.random.random()
                if( r < 0.5 ):
                    s_next = +1
                else:
                    s_next = -1
                
            else:
                s_next = s[i-1]
            
            x = np.insert(x,i,x[i-1]+s_next)
            s = np.insert(s,i,s_next)
        
        
        
        store_x = np.vstack((store_x,x))

    var = np.var(store_x,1)
    
    for t in range(0,t_max-10,5):
        plt.plot(store_t[t], var[t], 'ro')

    plt.axis([10, t_max, 10, t_max*t_max])
    plt.xscale('log')  
    plt.yscale('log')  
    plt.xlabel('$t$', fontsize=15)
    plt.ylabel('$< {x_t}^2> - {< x_t >}^2$', fontsize=15)
    #plt.title(title)

    plt.show()
                
    
randwalk(k)

print("done")