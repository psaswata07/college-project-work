#Script To calculate Statistics of Authors on different Indexes.
from __future__ import division
import matplotlib.pyplot as plt
import pprint
import re
import json
import math
import os
import numpy as np
import peakutils
# ImPortant Function
def convert(input):
    if isinstance(input, dict):
        return {convert(key): convert(value) for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [convert(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input

dic={}
h={}


with open('m_quo.txt','r') as fp:
    dic=json.loads(fp.read(),encoding='utf-8')

with open('h_index(changed).txt','r') as fp:
    h=json.loads(fp.read(),encoding='utf8')

dic=convert(dic)
h=convert(h)

dic={int(k):float(v) for k,v in dic.items()}
h={int(k):float(v) for k,v in h.items()}

print('-------------------------------------------------------------------------')

new={}

data=[]
for key in dic:
    if key in h:
        data.append(dic[key])
        new[key]=dic[key]
print('------------------------------------------------------------------------')

print('Number of Authors')
print(len(data))
print('Maximum Value')
print(max(data))
print('Minimum Value')
print(min(data))
print('Mean Value')
print(np.mean(data))
print('Standard Deviation')
print(np.std(data))
print('Median')
print(np.median(data))
