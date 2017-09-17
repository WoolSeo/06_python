#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 21:34:55 2017
hihi
@author: woolseo
"""

import numpy as np
import matplotlib.pyplot as plt
import multiprocessing as proc #insert this line
import time
import random

N = 10
t_max =100

def randwalk(pp, q): #insert q
    
    #print(pp)
    var_mean = np.array([0,0])

    var = np.array([])

    np.random.seed(); 
    
    for k in range(1, t_max, 20):
        #N번 시행
        store_x = np.arange(0,k,1,dtype=np.int)
        
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
            for i in range(1, k):
                if( np.random.random() < pp):
                    s_next = s[np.random.randint(0,i)]
                else:
                    r = random.random()
                    if( r < 0.5 ):
                        s_next = +1
                    else:
                        s_next = -1
                
                x = np.insert(x,i,x[i-1]+s_next)
                s = np.insert(s,i,s_next)
            
            
            store_x = np.vstack((store_x,x))
            #print()
            #print("done1")
    
    
        var_mean = np.vstack((var_mean,[k,np.mean(np.var(store_x,1))]))
    
    
    #print(var_mean.shape)
    #print(var_mean)
    
    q.put(var_mean)
    #print(var_mean[:,0])
    #print(var_mean[:,1])
    
    
    #for i in range(1,N):
    #    plt.plot(store_x[0,:],store_x[i,:],'o')
    
    
    #
    


startTime = time.time()                
Q = proc.Queue() # queue

p = []

for i in range(3):
    p.append( proc.Process(target = randwalk, args=((i+1)*0.3, Q)) )
    p[i].start()


results = np.array([None,2])

for i in range(3):
    results=Q.get(True)
    print(results.shape)
    plt.plot(results[:,0],results[:,1],'o')





#

plt.axis([10, t_max, 10, t_max*t_max])
plt.xscale('log')  
plt.yscale('log')  
plt.xlabel('$t$', fontsize=15)
plt.ylabel('$<X^2>-<X>^2$', fontsize=15)
plt.legend(loc=4)
plt.show()

print(time.time()-startTime)
