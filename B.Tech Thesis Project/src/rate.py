# Script To find Citation Statistics of Authors in Different Categories.
from __future__ import division
import matplotlib.pyplot as plt
import pprint
import re
import json
import math
import os
import numpy
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


peakint={}
peaklate={}
peakmul={}
monicr={}
mondcr={}
authorid_10pubs={}


icr=[]
dcr=[]
mul=[]
late=[]
init=[]


with open('authorid_10pubs.txt','r') as fp:
    authorid_10pubs=json.loads(fp.read(),encoding='utf-8')

with open('peakint.txt','r') as fp:
    peakint=json.loads(fp.read(),encoding='utf-8')

with open('peaklate.txt','r') as fp:
    peaklate=json.loads(fp.read(),encoding='utf-8')

with open('peakmul.txt','r') as fp:
    peakmul=json.loads(fp.read(),encoding='utf-8')

with open('monicr.txt','r') as fp:
    monicr=json.loads(fp.read(),encoding='utf-8')

with open('mondcr.txt','r') as fp:
    mondcr=json.loads(fp.read(),encoding='utf-8')


peakint=convert(peakint)
peakmul=convert(peakmul)
monicr=convert(monicr)
mondcr=convert(mondcr)
peaklate=convert(peaklate)
authorid_10pubs=convert(authorid_10pubs)



peakint={int(k):str(v) for k,v in peakint.items()}
peakmul={int(k):str(v) for k,v in peakmul.items()}
peaklate={int(k):str(v) for k,v in peaklate.items()}
monicr={int(k):str(v) for k,v in monicr.items()}
mondcr={int(k):str(v) for k,v in mondcr.items()}
authorid_10pubs={int(k):[int(i) for i in v] for k,v in authorid_10pubs.items()}


for key in authorid_10pubs:
    print(key)
    s=0
    if key in peakint:
        l=len(authorid_10pubs[key])
        s=sum(list(authorid_10pubs[key]))
        init.append(s/10)
    elif key in peaklate:
        l=len(authorid_10pubs[key])
        s=sum(list(authorid_10pubs[key]))
        late.append(s/10)
    elif key in peakmul:
        l=len(authorid_10pubs[key])
        s=sum(list(authorid_10pubs[key]))
        mul.append(s/10)
    elif key in monicr:
        l=len(authorid_10pubs[key])
        s=sum(list(authorid_10pubs[key]))
        icr.append(s/10)
    elif key in mondcr:
        l=len(authorid_10pubs[key])
        s=sum(list(authorid_10pubs[key]))
        dcr.append(s/10)

mean_init=numpy.mean(init)
mean_late=numpy.mean(late)
mean_icr=numpy.mean(icr)
mean_dcr=numpy.mean(dcr)
mean_mul=numpy.mean(mul)


std_init=numpy.std(init)
std_late=numpy.std(late)
std_mul=numpy.std(mul)
std_icr=numpy.std(icr)
std_dcr=numpy.std(dcr)


print('\n')
print('\n')
print('MEAN IN PEAKLATE:')
print(mean_late)
print('MEAN IN PEAKINT:')
print(mean_init)
print('MEAN IN PEAKMUL:')
print(mean_mul)
print('MEAN IN MONDCR:')
print(mean_dcr)
print('MEAN IN MONICR:')
print(mean_icr)


print('\n')
print('\n')
print('STD IN PEAKLATE')
print(std_late)
print('STD IN PEAKINT')
print(std_init)
print('STD IN PEAKMUL')
print(std_mul)
print('STD IN MONDCR')
print(std_dcr)
print('STD IN MONICR')
print(std_icr)
