#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 18:43:03 2017

@author: woolseo
"""
list1 = ['e','l','o','H']
list2 = ['TAA', 'GAC','CAG', 'AGT']


input_data = input('input : ')
for i in range(0,2):
    if(input_data == list1[i]):
        print(list2[i])