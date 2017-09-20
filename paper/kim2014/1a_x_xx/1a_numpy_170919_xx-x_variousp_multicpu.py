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
import datetime

N = 1000
t_max =10000
step = 10

filename = 'kim 2014 1a xx'

def randwalk(pp, l, q): #insert q
    
    global filename
    
    var_mean = np.array([2,0])
    
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
    
    np.savetxt(filename + '_x_.csv', x, delimiter=',') 
    
    var_mean = np.array([pp, l, np.var(x)])
    #print(var_mean)
    q.put(var_mean)
    
    


startTime = time.time()
now = datetime.datetime.now()
nowDate = now.strftime('%Y%m%d')

filename = filename + nowDate
filename_csv = filename + '.csv'
filename_pdf = filename + '.pdf'


var_mean = np.array([0,0])
         
Q = proc.Queue() # queue

p = []

x = 0

results = np.array([3,])

#dtype = [('pp',float),('t',float),('var',float)]
var_data = np.array([0,0,0], dtype = np.float64)

mean_data = np.array([0,0,0], dtype = np.float64)

for i in range(4):
    
    pp = (i+1)*0.2 
    
    temp_mean_data = np.array([0,0], dtype = np.float64) 
    
    for t in range(0,t_max,step):
        
        temp_var_data = 0
        
        for k in range(0, N):
                
            p.append( proc.Process(target = randwalk, args=(pp, t,  Q)) )
            p[x].start()
                
            x = x + 1
                
            results = Q.get(True)
            #print(results)
            var_data = np.vstack((var_data,results))
            temp_var_data = temp_var_data + results[2]
        
        #temp_mean_data = np.array()
        mean_data = np.vstack((mean_data,[pp,t,temp_var_data/N]))
        temp_mean_data = np.vstack((temp_mean_data,[t,temp_var_data/N]))
        print(x)
        
    plt.plot(temp_mean_data[:,0],temp_mean_data[:,1],'o',ms=2, label=i)    
                
              
#print(mean_data)  

#var_data = np.sort(var_data, order='pp')

#print(var_data) 


plt.axis([10, t_max, 10, t_max*t_max])
plt.xscale('log')  
plt.yscale('log')  
plt.xlabel('$t$', fontsize=15)
plt.ylabel('$<X^2>-<X>^2$', fontsize=15)
plt.legend(loc=4)
plt.savefig(filename_pdf)
plt.show()

print(time.time()-startTime)
