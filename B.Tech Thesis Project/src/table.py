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


with open('mondcr.txt','r') as fp:
    peakmul=json.loads(fp.read(),encoding='utf-8')

peakmul=convert(peakmul)
peakmul={int(k):str(v) for k,v in peakmul.items()}


author_paper={}

with open('author_paper.txt','r') as fp:
    author_paper=json.loads(fp.read(),encoding='utf-8')

author_paper=convert(author_paper)

author_paper={str(k):[int(i) for i in v] for k,v in author_paper.items()}



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


print('========================================================================')

int_mul_keys=0
for author in peakmul:
    name=peakmul[author]
    if name in author_paper:
        temp=author_paper[name]
        for x in temp:
            if x in mondcr15:
                int_mul_keys=int_mul_keys+1
                mondcr15.pop(x)


print("DCR TO DCR")
print(int_mul_keys)
