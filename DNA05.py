#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 00:21:35 2017

@author: woolseo
"""

DNA = ''
RNA = ''
protein = ''
codon = ['UUU','UUC','UUA','UUG','CUU','CUC','CUA','CUG']
amino = ['Phe','Phe','Leu','Leu','Leu','Leu','Leu','Leu']

DNA = input('input DNA : ')

for c in DNA:
    if( c == 'A'):
        RNA = RNA + 'U'
    elif( c == 'T'):
        RNA = RNA + 'A'
    elif( c == 'G'):
        RNA = RNA + 'C'
    elif( c == 'C'):
        RNA = RNA + 'G'

print('RNA : %s' %RNA)

for i in range(0,len(RNA),3):
    for code in codon:
        if( RNA[i:i+3] == code):
            j = codon.index(code)
    protein = protein + amino[j]
    
print('protein : %s' %protein)