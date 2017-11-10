#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 00:21:35 2017

@author: woolseo
"""

DNA = ''
RNA = ''
protein = ''
codon = ['UUU','UUC','UUA','UUG','UCU','UCC','UCA','UCG','UAU','UAC','UAA','UAG','UGU','UGC','UGA','UGG','CUU','CUC','CUA','CUG','CCU','CCC','CCA','CCG','CAU','CAC','CAA','CAG','CGU','CGC','CGA','CGG','AUU','AUC','AUA','AUG','ACU','ACC','ACA','ACG','AAU','AAC','AAA','AAG','AGU','AGC','AGA','AGG','GUU','GUC','GUA','GUG','GCU','GCC','GCA','GCG','GAU','GAC','GAA','GAG','GGU','GGC','GGA','GGG']
amino = ['~ ','~ ','! ','! ','% ','% ','% ','% ','( ','( ',') ',') ','< ','< ','> ','? ','! ','! ','! ','! ','^ ','^ ','^ ','^ ','- ','- ','_ ','_ ','/ ','/ ','/ ','/ ','@ ','@ ','@ ','# ','& ','& ','& ','& ','+ ','+ ','= ','= ','[ ','[ ','] ','] ','$ ','$ ','$ ','$ ','* ','* ','* ','* ','{ ','{ ','} ','} ','\\ ','\\ ','\\ ','\\ ']

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