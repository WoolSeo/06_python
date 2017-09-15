#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 21:34:55 2017

@author: woolseo
"""

import numpy as np
import matplotlib.pyplot as plt
#import numpy as np

N = 30
t_max =100000

a = 0.05

#var = np.array([])


def randwalk():
    
    store_x = np.arange(0,t_max,1,dtype=np.int)

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
            if( np.random.random() < ( 1.0 / ( i**a ) ) ):
                r = np.random.random()
                if( r < 0.5 ):
                    s_next = +1
                else:
                    s_next = -1
                
            else:
                #s_next = s[i-1] #pLMEM
                s_next = (-1) * s[i-1] #nLMEM
            
            x = np.insert(x,i,x[i-1]+s_next)
            s = np.insert(s,i,s_next)
        
        
        store_x = np.vstack((store_x,x))
        #print(store_x)
        #print("done1")
    
    
    #var = np.var(store_x,1)
    #print(var)
    
    
    for i in range(1,N):
        plt.plot(store_x[0,:],store_x[i,:],'o', ms=1)
        
        
    #plt.axis([0, t_max, -t_max, t_max])
    plt.axis([0, t_max, -500, 500])
    
    #plt.xscale('log')  
    #plt.yscale('log')  
    plt.xlabel('$t$', fontsize=15)
    plt.ylabel('$x(t)$', fontsize=15)

    plt.title("2a nLMEM $x(t)$, $a=$" + str(a)  )

    plt.show()
                
    
randwalk()

print("done")