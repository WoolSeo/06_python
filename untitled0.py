#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 00:34:47 2017

@author: woolseo
"""

import gizeh as gz
import numpy as np
from fractions import gcd

def rose(d, n):
    """ Returns a polyline representing a rose of radius 1 """
    n_cycles = 1.0 * d / gcd(n,d) # <- number of cycles to close the rose 
    aa = np.linspace(0,2*np.pi*n_cycles,1000)
    rr = np.cos( n*aa/d)
    points = gz.polar2cart(rr, aa)
    return gz.polyline(points, stroke=[0,0,0], stroke_width=.05)

max_d = 8
max_n = 7
rose_radius = 30

def position(d, n):
    """ Defines the (x,y) position of the rose(d,n)."""
    return [(1.1*(2*i-.6) * rose_radius) for i in [d, n]]

W, H = [int(c+2*rose_radius) for c in position(max_d,max_n)] 

surface = gz.Surface(W, H, bg_color=(1, 1, 1))

for d in range(1, max_d+1):
    for n in range(1, max_n+1):
        rose_nd = rose(n, d).scale(rose_radius).translate( position(d,n) )
        rose_nd.draw(surface)

surface.write_to_png("roses.png")