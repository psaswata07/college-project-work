#Script To find out the Shifting of Authors from one Category to others during a considered period of time sya 5,10 or 20 years.
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


peakmul={}
peaklate={}
peakint={}
monicr={}
mondcr={}


with open('peakmul.txt','r') as fp:
    peakmul=json.loads(fp.read(),encoding='utf-8')

with open('peaklate.txt','r') as fp:
    peaklate=json.loads(fp.read(),encoding='utf-8')

with open('peakint.txt','r') as fp:
    peakint=json.loads(fp.read(),encoding='utf-8')

with open('monicr.txt','r') as fp:
    monicr=json.loads(fp.read(),encoding='utf-8')

with open('mondcr.txt','r') as fp:
    mondcr=json.loads(fp.read(),encoding='utf-8')

peakmul=convert(peakmul)
peaklate=convert(peaklate)
peakint=convert(peakint)
monicr=convert(monicr)
mondcr=convert(mondcr)


peakmul={int(k):str(v) for k,v in peakmul.items()}
peaklate={int(k):str(v) for k,v in peaklate.items()}
peakint={int(k):str(v) for k,v in peakint.items()}
monicr={int(k):str(v) for k,v in monicr.items()}
mondcr={int(k):str(v) for k,v in mondcr.items()}



peakmul15={}
peaklate15={}
peakint15={}
monicr15={}
mondcr15={}

with open('peakmulpapers.txt','r') as fp:
    peakmul15=json.loads(fp.read(),encoding='utf-8')

with open('peaklatepapers.txt','r') as fp:
    peaklate15=json.loads(fp.read(),encoding='utf-8')

with open('peakintpapers.txt','r') as fp:
    peakint15=json.loads(fp.read(),encoding='utf-8')

with open('monicrpapers.txt','r') as fp:
    monicr15=json.loads(fp.read(),encoding='utf-8')

with open('mondcrpapers.txt','r') as fp:
    mondcr15=json.loads(fp.read(),encoding='utf-8')


peakmul15=convert(peakmul15)
peaklate15=convert(peaklate15)
peakint15=convert(peakint15)
monicr15=convert(monicr15)
mondcr15=convert(mondcr15)


peakmul15={int(k):str(v) for k,v in peakmul15.items()}
peaklate15={int(k):str(v) for k,v in peaklate15.items()}
peakint15={int(k):str(v) for k,v in peakint15.items()}
monicr15={int(k):str(v) for k,v in monicr15.items()}
mondcr15={int(k):str(v) for k,v in mondcr15.items()}


paper_author={}
with open('paper_author.txt','r') as fp:
    paper_author=json.loads(fp.read(),encoding='utf-8')

paper_author=convert(paper_author)
paper_author={int(k):[str(i) for i in v] for k,v in paper_author.items()}

print('-------------------------------------------------------------------------')


int_int_keys=0
for author in peakint:
    name=peakint[author]
    for paper in peakint15:
        if paper in paper_author:
            if name in paper_author[paper]:
                print(name)
                int_int_keys=int_int_keys+1


int_late_keys=0
for author in peakint:
    name=peakint[author]
    for paper in peaklate15:
        if paper in paper_author:
            if name in paper_author[paper]:
                int_late_keys=int_late_keys+1


int_mul_keys=0
for author in peakint:
    name=peakint[author]
    for paper in peakmul15:
        if paper in paper_author:
            if name in paper_author[paper]:
                int_mul_keys=int_mul_keys+1


int_icr_keys=0
for author in peakint:
    name=peakint[author]
    for paper in monicr15:
        if paper in paper_author:
            if name in paper_author[paper]:
                int_icr_keys=int_icr_keys+1


int_dcr_keys=0
for author in peakint:
    name=peakint[author]
    for paper in mondcr15:
        if paper in paper_author:
            if name in paper_author[paper]:
                int_dcr_keys=int_dcr_keys+1

late_int_keys=0
for author in peaklate:
    name=peaklate[author]
    for paper in peakint15:
        if paper in paper_author:
            if name in paper_author[paper]:
                late_int_keys=late_int_keys+1

late_late_keys=0
for author in peaklate:
    name=peaklate[author]
    for paper in peaklate15:
        if paper in paper_author:
            if name in paper_author[paper]:
                late_late_keys=late_late_keys+1

late_mul_keys=0
for author in peaklate:
    name=peaklate[author]
    for paper in peakmul15:
        if paper in paper_author:
            if name in paper_author[paper]:
                late_mul_keys=late_mul_keys+1

late_icr_keys=0
for author in peaklate:
    name=peaklate[author]
    for paper in monicr15:
        if paper in paper_author:
            if name in paper_author[paper]:
                late_icr_keys=late_icr_keys+1

late_dcr_keys=0
for author in peaklate:
    name=peaklate[author]
    for paper in mondcr15:
        if paper in paper_author:
            if name in paper_author[paper]:
                late_dcr_keys=late_dcr_keys+1

mul_int_keys=0
for author in peakmul:
    name=peakmul[author]
    for paper in peakint15:
        if paper in paper_author:
            if name in paper_author[paper]:
                mul_int_keys=mul_int_keys+1

mul_late_keys=0
for author in peakmul:
    name=peakmul[author]
    for paper in peaklate15:
        if paper in paper_author:
            if name in paper_author[paper]:
                mul_late_keys=mul_late_keys+1

mul_mul_keys=0
for author in peakmul:
    name=peakmul[author]
    for paper in peakmul15:
        if paper in paper_author:
            if name in paper_author[paper]:
                mul_mul_keys=mul_mul_keys+1

mul_icr_keys=0
for author in peakmul:
    name=peakmul[author]
    for paper in monicr15:
        if paper in paper_author:
            if name in paper_author[paper]:
                mul_icr_keys=mul_icr_keys+1

mul_dcr_keys=0
for author in peakmul:
    name=peakmul[author]
    for paper in mondcr15:
        if paper in paper_author:
            if name in paper_author[paper]:
                mul_dcr_keys=mul_dcr_keys+1


icr_int_keys=0
for author in monicr:
    name=monicr[author]
    for paper in peakint15:
        if paper in paper_author:
            if name in paper_author[paper]:
                icr_int_keys=icr_int_keys+1


icr_mul_keys=0
for author in monicr:
    name=monicr[author]
    for paper in peakmul15:
        if paper in paper_author:
            if name in paper_author[paper]:
                icr_mul_keys=icr_mul_keys+1


icr_late_keys=0
for author in monicr:
    name=monicr[author]
    for paper in peaklate15:
        if paper in paper_author:
            if name in paper_author[paper]:
                icr_late_keys=icr_late_keys+1

icr_icr_keys=0
for author in monicr:
    name=monicr[author]
    for paper in monicr15:
        if paper in paper_author:
            if name in paper_author[paper]:
                icr_icr_keys=icr_icr_keys+1

icr_dcr_keys=0
for author in monicr:
    name=monicr[author]
    for paper in mondcr15:
        if paper in paper_author:
            if name in paper_author[paper]:
                icr_dcr_keys=icr_dcr_keys+1

dcr_int_keys=0
for author in mondcr:
    name=mondcr[author]
    for paper in peakint15:
        if paper in paper_author:
            if name in paper_author[paper]:
                dcr_int_keys=dcr_int_keys+1

dcr_mul_keys=0
for author in mondcr:
    name=mondcr[author]
    for paper in peakmul15:
        if paper in paper_author:
            if name in paper_author[paper]:
                dcr_mul_keys=dcr_mul_keys+1

dcr_late_keys=0
for author in mondcr:
    name=mondcr[author]
    for paper in peaklate15:
        if paper in paper_author:
            if name in paper_author[paper]:
                dcr_late_keys=dcr_late_keys+1

dcr_icr_keys=0
for author in mondcr:
    name=mondcr[author]
    for paper in monicr15:
        if paper in paper_author:
            if name in paper_author[paper]:
                dcr_icr_keys=dcr_icr_keys+1

dcr_dcr_keys=0
for author in mondcr:
    name=mondcr[author]
    for paper in mondcr15:
        if paper in paper_author:
            if name in paper_author[paper]:
                dcr_dcr_keys=dcr_dcr_keys+1



print('Author Dictionary')
print(len(peakint))
print(len(peakmul))
print(len(peaklate))
print(len(monicr))
print(len(mondcr))


print('Paper Dictionary')
print(len(peakint15))
print(len(peakmul15))
print(len(peaklate15))
print(len(monicr15))
print(len(mondcr15))



print('int-late')
print(int_late_keys)

print('int-mul')
print(int_mul_keys)

print('int-int')
print(int_int_keys)

print('int-icr')
print(int_icr_keys)

print('int-dcr')
print(int_dcr_keys)



print('late-late')
print(late_late_keys)

print('late-mul')
print(late_mul_keys)

print('late-int')
print(late_int_keys)

print('late-icr')
print(late_icr_keys)

print('late-dcr')
print(late_dcr_keys)




print('mul-late')
print(mul_late_keys)

print('mul-mul')
print(mul_mul_keys)

print('mul-int')
print(mul_int_keys)

print('mul-icr')
print(mul_icr_keys)

print('mul-dcr')
print(mul_dcr_keys)



print('icr-late')
print(icr_late_keys)

print('icr-mul')
print(icr_mul_keys)

print('icr-int')
print(icr_int_keys)

print('icr-icr')
print(icr_icr_keys)

print('icr-dcr')
print(icr_dcr_keys)


print('dcr-late')
print(dcr_late_keys)

print('dcr-mul')
print(dcr_mul_keys)

print('dcr-int')
print(dcr_int_keys)

print('dcr-icr')
print(dcr_icr_keys)

print('dcr-dcr')
print(dcr_dcr_keys)
