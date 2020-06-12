# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 15:35:06 2020

@author: Maja
"""

from collections import Counter
import math
import huffman

alf = "Existe una cosa muy misteriosa, pero muy cotidiana. Todo el mundo participa de ella,  todo el mundo la conoce, pero muy pocos se paran a pensar en ella.  Casi todos se limitan a tomarla como viene, sin hacer preguntas.  Esta cosa es el tiempo."

res = Counter(alf)

probs = dict(Counter(res))

#print(probs)

for key in probs:
   probs[key]/=len(alf)
print(probs)
   
entropy = 0;
for key in probs:
    entropy+= probs[key]* math.log2(probs[key])*(-1)
    
print(entropy)   


freqs = list(probs.items())
huff = huffman.HuffmanCode(freqs, 2)

hufmann = huff.huffman
print(hufmann)
suma = 0
for char in alf:
    for key in hufmann:
        if char == hufmann[key]:
            suma+=len(key)
        
print(suma)
        
longitudmedia = 0
for k, v in probs.items():
    for kH, vH in hufmann.items():
        if k == vH:
            longitudmedia += v * len(kH)
            
print(longitudmedia)
print(len(probs))
eficacia = entropy / (math.log2(2) * longitudmedia)
print(eficacia)