#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 21:12:40 2017

@author: woolseo
"""

import numpy as np
import multiprocessing as proc
import time

N = 100

def test(b,q):    
    print(np.random.random())
    


######### 

Q = proc.Queue() # queue
p = [] #proceesing array
for i in range(N):
    p.append( proc.Process(target = test, args=(i,Q)) )
    p[i].start()