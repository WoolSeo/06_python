#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 21:34:55 2017

@author: woolseo
"""

import numpy as np
import matplotlib.pyplot as plt
import multiprocessing as proc
import time
import datetime

N = 10
t_max =10000

a = 0.8

store_x = np.arange(0,t_max,1,dtype=np.int)


def randwalk(b,q):
    
    
    x = np.array([],dtype=np.int)
    s = np.array([],dtype=np.int)
    
    np.random.seed();  
    
    #t=1
    if( np.random.random() < 0.5 ):
        s_next = +1
    else:
        s_next = -1
        
    x = np.insert(x,0,s_next)
    s = np.insert(s,0,s_next)
        
      
    #t>1
    for i in range(1, t_max):
        if( np.random.random()   < ( 1.0 / ( i**a ) ) ):
            r = np.random.random()
            if( r < 0.5 ):
                s_next = +1
            else:
                s_next = -1
                
        else:
            s_next = s[i-1] #pLMEM
            #s_next = (-1) * s[i-1] #nLMEM
            
        x = np.insert(x,i,x[i-1]+s_next)
        s = np.insert(s,i,s_next)
    
    print(x)
    q.put(x)
    
                
############## start program ###############
startTime = time.time()

Q = proc.Queue() # queue

p = [] #proceesing array

results = np.array([None,2])

for i in range(2):
    
    p.append( proc.Process(target = randwalk, args=(i,Q)) )
    p[i].start()
    results=Q.get(True)
    store_x = np.vstack((store_x,results))
    np.savetxt('test.csv', store_x, delimiter=',')
    plt.plot(store_x[0,:],store_x[i,:],'o', ms=1)
    




#for i in range(1,N):
    
    
plt.axis([0, t_max, -t_max, t_max])
#plt.xscale('log')  
#plt.yscale('log')  
plt.xlabel('$t$', fontsize=15)
plt.ylabel('$x(t)$', fontsize=15)

plt.title("2a nLMEM $x(t)$, $a=$" + str(a)  )

plt.savefig('test.pdf')
plt.show()


print(time.time()-startTime)

now = datetime.datetime.now()
nowDate = now.strftime('%Y%m%d')
print(nowDate)
print("done")
