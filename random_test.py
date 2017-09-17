#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 21:12:40 2017

@author: woolseo
"""

import numpy as np
import multiprocessing as proc
import time

N = 10


def test(b,q):
    x = [0]
    np.random.seed()
    for i in range(1,10):
        if( np.random.random() < 0.5):
            s = +1
        else:
            s = -1
        x.append(x[i-1]+s)
        
    print(x)
    


######### 

Q = proc.Queue() # queue
p = [] #proceesing array
for i in range(N):
    p.append( proc.Process(target = test, args=(i,Q)) )
    p[i].start()