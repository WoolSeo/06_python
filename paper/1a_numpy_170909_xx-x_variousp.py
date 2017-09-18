#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 21:34:55 2017
hihi
@author: woolseo
"""

import numpy as np
import matplotlib.pyplot as plt
import time

N = 500
t_max =100000


def randwalk(pp):
    
    print(pp)
    var_mean = np.array([0,0])

    var = np.array([])

    

    for k in range(10, t_max, 100):
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
                    r = np.random.random()
                    if( r < 0.5 ):
                        s_next = +1
                    else:
                        s_next = -1
                
                x = np.insert(x,i,x[i-1]+s_next)
                s = np.insert(s,i,s_next)
            
            
            store_x = np.vstack((store_x,x))
            
            #print("done1")

    
    	#print(k)
        var_mean = np.vstack((var_mean,[k,np.mean(np.var(store_x,1))]))
        
    #print(var_mean)
    #print("doen")
    #print(var_mean[:,0])
    #print(var_mean[:,1])
    
    
    #for i in range(1,N):
    #    plt.plot(store_x[0,:],store_x[i,:],'o')
    label_temp = "p="+str(pp)
    plt.plot(var_mean[:,0],var_mean[:,1],'o',label=label_temp)
        
        

                
startTime = time.time()

for p in range(2, 11, 2):
    randwalk(p/10.0)

plt.axis([10, t_max, 10, t_max*t_max])

plt.xscale('log')  
plt.yscale('log')  
plt.xlabel('$t$', fontsize=15)
plt.ylabel('$<X^2>-<X>^2$', fontsize=15)
plt.legend(loc=4)
plt.show()

print("done")
print(time.time()-startTime)
