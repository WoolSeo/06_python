#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 21:34:55 2017

@author: woolseo
"""

import numpy as np
import matplotlib.pyplot as plt
#import numpy as np

N = 10
t_max = 5
p = 0.3
q = 1-p
cnt = 0
multi = 1
a = 1
k=1


store_xx = np.array([],dtype=np.int)

var = np.array([])



def randwalk(t):
    
    store_x = np.zeros(t_max,dtype=np.int)
    store_t = np.arange(t_max,dtype=np.int)
    #N번 시행
    for j in range(1, N):
        x = np.array([],dtype=np.int)
        s = np.array([],dtype=np.int)
        
        #t=1
        if( np.random.random() < 0.5 ):
            s_next = +1
        else:
            s_next = -1
        
        x = np.insert(x,0,s_next)
        s = np.insert(s,0,s_next)
        
      
        #t>1
        for i in range(1, t_max):
            if( np.random.random() < q):
                r = np.random.random()
                if( r < 0.5 ):
                    s_next = +1
                else:
                    s_next = -1
                
            else:
                s_next = s[np.random.randint(0,i)]
            
            x = np.insert(x,i,x[i-1]+s_next)
            s = np.insert(s,i,s_next)
        
        
        store_x = np.vstack((store_x,x))
        print(store_x)
        print("s")
    
    print("done1")
    var = np.var(store_x,1)
    print(var)
    
    
    for t in range(0,t_max-10,5):
        #plt.plot(store_t[t], var[t], 'ro')
        plt.plot(t, var[t], 'ro')

    plt.axis([10, t_max, 10, t_max*t_max])
    plt.xscale('log')  
    plt.yscale('log')  
    plt.xlabel('$t$', fontsize=15)
    plt.ylabel('$< {x_t}^2> - {< x_t >}^2$', fontsize=15)
    #plt.title(title)

    plt.show()
                
    
randwalk(k)

print("done")