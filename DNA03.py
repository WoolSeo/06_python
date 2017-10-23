#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 18:43:03 2017

@author: woolseo
"""
list1 = ['안','녕','하','삼']
list2 = ['TAA', 'GAC','CAG', 'AGT']

input_data = input('input : ')

for c in input_data:
    for i in range(0,4):
        if(c == list1[i]):
            print(list2[i])