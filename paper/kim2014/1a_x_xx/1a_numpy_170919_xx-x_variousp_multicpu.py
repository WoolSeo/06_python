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

N = 10
t_max =100

filename = 'kim 2014 1a xx'


var_mean = np.array([0,0])
store_x = np.arange(0,l,1,dtype=np.int)

def randwalk(pp, l, q): #insert q
    
    global filename
    
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
    
    var_mean = np.vstack((var_mean,[l,np.mean(np.var(store_x,1))]))
    


startTime = time.time()
now = datetime.datetime.now()
nowDate = now.strftime('%Y%m%d')

filename = filename + nowDate
filename_csv = filename + '.csv'
filename_pdf = filename + '.pdf'


var_mean = np.array([0,0])
         
Q = proc.Queue() # queue

p = []

for i in range(4):
    
    pp = (i+1)*0.2 
    
    l = 1
    dl = 1
    
    while(l < t_max):
        
        for j in range(0,9):  
            #N번 시행
            
            
            for i in range(1, N):
                
                p.append( proc.Process(target = randwalk, args=(pp, l, Q)) )
                p[i].start()
                
            
            
        l = l + dl
            

    dl = dl * 10


results = np.array([None,2])

for i in range(4):
    results=Q.get(True)
    np.savetxt(filename_csv, results, delimiter=',')
    plt.plot(results[:,0],results[:,1],ms=2, label=i)


plt.axis([10, t_max, 10, t_max*t_max])
plt.xscale('log')  
plt.yscale('log')  
plt.xlabel('$t$', fontsize=15)
plt.ylabel('$<X^2>-<X>^2$', fontsize=15)
plt.legend(loc=4)
plt.savefig(filename_pdf)
plt.show()

print(time.time()-startTime)
