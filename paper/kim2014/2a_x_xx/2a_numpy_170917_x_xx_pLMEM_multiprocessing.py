#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 21:34:55 2017

To do!

store t array


@author: woolseo
"""

import numpy as np
import matplotlib.pyplot as plt
import multiprocessing as proc
import time
import datetime

N = 500
t_max =100000
filename = 'kim 2014 2a xx'

def randwalk(a,q):
    
    temp_var_mean = np.array([0,0])
    
    l = 1
    dl = 1
    
    while(l < t_max):
        
        for k in range(0,9):  
            
            store_x = np.arange(0,l,1,dtype=np.int)
            
            for j in range(1, N):
                
            
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
                for i in range(1, l):
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
                
                
                print(l,k)
                
                store_x = np.vstack((store_x,x))
                
            temp_var_mean = np.vstack((temp_var_mean,[l,np.mean(np.var(store_x,1))]))
            
            l = l + dl
            
        dl = dl * 10
    temp = str(a) + 'done'
    print(temp)
    q.put(temp_var_mean)
    
                
############## start program ###############


startTime = time.time()
now = datetime.datetime.now()
nowDate = now.strftime('%Y%m%d')

filename = filename + nowDate
filename_csv = filename + '.csv'
filename_pdf = filename + '.pdf'


Q = proc.Queue() # queue

p = [] #proceesing array

for i in range(4):
    p.append( proc.Process(target = randwalk, args=((i*2+2)*0.1,Q)) )
    p[i].start()
    

results = np.array([None,2])
var_mean = np.array([0,0])



for i in range(4):
    results = Q.get(True)
    var_mean = np.vstack((var_mean,results))
    np.savetxt(filename_csv, var_mean, delimiter=',')
    plt.plot(var_mean[:,0],var_mean[:,1],'o', ms=2, label=i)
    #print(i)
    #print(var_mean)

print(time.time()-startTime)
    
#plt.axis([10, t_max, 10, t_max*t_max])
plt.xscale('log')  
plt.yscale('log')  
plt.xlabel('$t$', fontsize=15)
plt.ylabel('$<X^2>-<X>^2$', fontsize=15)
plt.legend(loc=4)

#plt.title("2a pLMEM $<X^2>-<X>^2$" )

plt.savefig(filename_pdf)
plt.show()



print("done")
