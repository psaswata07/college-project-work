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




authorid_10years={}
authorid_10pubs={}

with open('authorid_20pubs.txt','r') as fp:
    authorid_10pubs=json.loads(fp.read(),encoding='utf-8')


with open('authorid_20years.txt','r') as fp:
    authorid_10years=json.loads(fp.read(),encoding='utf-8')

authorid_10pubs=convert(authorid_10pubs)
authorid_10years=convert(authorid_10years)

authorid_10pubs={int(k):[int(i) for i in v] for k,v in authorid_10pubs.items()}
authorid_10years={int(k):[int(i) for i in v] for k,v in authorid_10years.items()}

print('-------------------------------------------------------------------------')


peakmul={}
peaklate={}
peakint={}
monicr={}
mondcr={}
others={}


with open('peakmul20.txt','r') as fp:
    peakmul=json.loads(fp.read(),encoding='utf-8')

with open('peaklate20.txt','r') as fp:
    peaklate=json.loads(fp.read(),encoding='utf-8')

with open('peakint20.txt','r') as fp:
    peakint=json.loads(fp.read(),encoding='utf-8')

with open('monicr20.txt','r') as fp:
    monicr=json.loads(fp.read(),encoding='utf-8')

with open('mondcr20.txt','r') as fp:
    mondcr=json.loads(fp.read(),encoding='utf-8')

with open('others20.txt','r') as fp:
    others=json.loads(fp.read(),encoding='utf-8')


peakmul=convert(peakmul)
peaklate=convert(peaklate)
peakint=convert(peakint)
monicr=convert(monicr)
mondcr=convert(mondcr)
others=convert(others)

peakmul={int(k):str(v) for k,v in peakmul.items()}
peaklate={int(k):str(v) for k,v in peaklate.items()}
peakint={int(k):str(v) for k,v in peakint.items()}
monicr={int(k):str(v) for k,v in monicr.items()}
mondcr={int(k):str(v) for k,v in mondcr.items()}
others={int(k):str(v) for k,v in others.items()}

print('-------------------------------------------------------------------------')


init_cit=[]
mul_cit=[]
late_cit=[]
icr_cit=[]
dcr_cit=[]
oth_cit=[]



init_pubs=[]
mul_pubs=[]
late_pubs=[]
icr_pubs=[]
dcr_pubs=[]
oth_pubs=[]

for key in authorid_10years:
    cit=authorid_10years[key]
    if key in authorid_10pubs:
        pubs=authorid_10pubs[key]
        if key in peakint:
            init_cit.append(sum(cit))
            init_pubs.append(sum(pubs))
        elif key in peaklate:
            late_cit.append(sum(cit))
            late_pubs.append(sum(pubs))
        elif key in peakmul:
            mul_cit.append(sum(cit))
            mul_pubs.append(sum(pubs))
        elif key in monicr:
            icr_cit.append(sum(cit))
            icr_pubs.append(sum(pubs))
        elif key in mondcr:
            dcr_cit.append(sum(cit))
            dcr_pubs.append(sum(pubs))
        elif key in others:
            oth_cit.append(sum(cit))
            oth_pubs.append(sum(pubs))

print('Avg-Cit in int')
print(np.mean(init_cit))
print('Avg-Cit in late')
print(np.mean(late_cit))
print('Avg-Cit in mul')
print(np.mean(mul_cit))
print('Avg-Cit in icr')
print(np.mean(icr_cit))
print('Avg-Cit in dcr')
print(np.mean(dcr_cit))


print('Avg-pubs in int')
print(np.mean(init_pubs))
print('Avg-pubs in late')
print(np.mean(late_pubs))
print('Avg-pubs in mul')
print(np.mean(mul_pubs))
print('Avg-pubs in icr')
print(np.mean(icr_pubs))
print('Avg-pubs in dcr')
print(np.mean(dcr_pubs))
