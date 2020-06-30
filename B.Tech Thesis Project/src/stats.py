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

authorid_author={}
h_index={}
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

with open('authorid_author.txt','r') as fp:
    authorid_author=json.loads(fp.read(),encoding='utf-8')

with open('authorid_10pubs.txt','r') as fp:
    authorid_10pubs=json.loads(fp.read(),encoding='utf-8')

with open('h_index.txt','r') as fp:
    h_index=json.loads(fp.read(),encoding='utf-8')

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

authorid_author=convert(authorid_author)
authorid_10pubs=convert(authorid_10pubs)
h_index=convert(h_index)
peakint=convert(peakint)
peakmul=convert(peakmul)
monicr=convert(monicr)
mondcr=convert(mondcr)
peaklate=convert(peaklate)


authorid_author={int(k):str(v) for k,v in authorid_author.items()}
peakint={int(k):str(v) for k,v in peakint.items()}
peakmul={int(k):str(v) for k,v in peakmul.items()}
peaklate={int(k):str(v) for k,v in peaklate.items()}
monicr={int(k):str(v) for k,v in monicr.items()}
mondcr={int(k):str(v) for k,v in mondcr.items()}
h_index={int(k):int(v) for k,v in h_index.items()}
authorid_10pubs={int(k):[int(i) for i in v] for k,v in authorid_10pubs.items()}


for key in authorid_10pubs:
    print(key)
    search=authorid_author[key]
    if key in peakint:
        if key in h_index:
            init.append(h_index[key])
    elif key in peaklate:
        if key in h_index:
            late.append(h_index[key])
    elif key in peakmul:
        if key in h_index:
            mul.append(h_index[key])
    elif key in monicr:
        if key in h_index:
            icr.append(h_index[key])
    elif key in mondcr:
        if key in h_index:
            dcr.append(h_index[key])



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

keys_late=len(peaklate)
keys_init=len(peakint)
keys_mul=len(peakmul)
keys_icr=len(monicr)
keys_dcr=len(mondcr)

total=len(authorid_10pubs)


print('\n')
print('TOTAL NUMBER OF AUTHORS:%d'%total)
print('NUMBER OF AUTHORS IN PEAKINT:%d'%len(peakint))
print('NUMBER OF AUTHORS IN PEAKLATE:%d'%len(peaklate))
print('NUMBER OF AUTHORS IN PEAKMUL:%d'%len(peakmul))
print('NUMBER OF AUTHORS IN MONICR:%d'%len(monicr))
print('NUMBER OF AUTHORS IN MONDCR:%d'%len(mondcr))

print('\n')
keys_late=(keys_late/total)*100
keys_dcr=(keys_dcr/total)*100
keys_icr=(keys_icr/total)*100
keys_mul=(keys_mul/total)*100
keys_init=(keys_init/total)*100

print('\n')
print('% in PEAKLATE:')
print(keys_late)
print('% in PEAKINT:')
print(keys_init)
print('% in PEAKMUL:')
print(keys_mul)
print('% in MONDCR:')
print(keys_dcr)
print('% in MONICR:')
print(keys_icr)


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
