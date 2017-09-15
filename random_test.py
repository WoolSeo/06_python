#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 21:12:40 2017

@author: woolseo
"""

import numpy as np
import matplotlib.pyplot as plt
import multiprocessing as proc
import time
import datetime

N = 1000
t_max =10
a = 0
b = 0

def randwalk(b,q):    
    thistime = int(time.time()*10000000)
    random.seed(thistime)
    if(random.random()<0.5):
        a = a + 1
    else:
        b = b + 1
        
    print(a)
    print(b)




startTime = time.time()

Q = proc.Queue() # queue

p = [] #proceesing array

for i in range(N):
    p.append( proc.Process(target = randwalk, args=(i,Q)) )
    p[i].start()