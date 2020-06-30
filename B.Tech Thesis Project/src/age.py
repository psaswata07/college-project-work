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


authorid_author={}
peakint={}
peaklate={}
peakmul={}
monicr={}
mondcr={}

authorid_fyear={}
authorid_lyear={}

with open('authorid_fyear.txt','r') as fp:
    authorid_fyear=json.loads(fp.read(),encoding='utf=8')

with open('authorid_lyear.txt','r') as fp:
    authorid_lyear=json.loads(fp.read(),encoding='utf=8')

authorid_lyear=convert(authorid_lyear)
authorid_fyear=convert(authorid_fyear)


with open('authorid_author.txt','r') as fp:
    authorid_author=json.loads(fp.read(),encoding='utf-8')
authorid_author=convert(authorid_author)

authorid_fyear={int(k):int(v) for k,v in authorid_fyear.items()}
authorid_lyear={int(k):int(v) for k,v in authorid_lyear.items()}

authorid_author={int(k):str(v) for k,v in authorid_author.items()}

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


intage=0
lateage=0
mulage=0
icrage=0
dcrage=0


print('--------------------------------------------------------------------------')

for key in authorid_author:
    if key in peakmul:
        if key in authorid_fyear and key in authorid_lyear:
            mulage=(authorid_lyear[key]-authorid_fyear[key]) + mulage
    elif key in peaklate:
        if key in authorid_fyear and key in authorid_lyear:
            lateage=(authorid_lyear[key]-authorid_fyear[key]) + lateage
    elif key in peakint:
        if key in authorid_fyear and key in authorid_lyear:
            intage=(authorid_lyear[key]-authorid_fyear[key]) + intage
    elif key in monicr:
        if key in authorid_fyear and key in authorid_lyear:
            icrage=(authorid_lyear[key]-authorid_fyear[key]) + icrage
    elif key in mondcr:
        if key in authorid_fyear and key in authorid_lyear:
            dcrage=(authorid_lyear[key]-authorid_fyear[key]) + dcrage

print('Avg Age in PEAKINT')
print((np.sum(intage))/len(peakint))
print('Avg Age in PEAKLATE')
print((np.sum(lateage))/len(peaklate))
print('Avg Age in PEAKMUL')
print((np.sum(mulage))/len(peakmul))
print('Avg Age in MONICR')
print((np.sum(icrage))/len(monicr))
print('Avg Age in MONDCR')
print((np.sum(dcrage))/len(mondcr))
