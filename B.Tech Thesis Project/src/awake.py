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


def entropy2(labels):
    n_labels = len(labels)
    if n_labels <= 1:
        return 0
    counts = np.bincount(labels)
    probs = counts / n_labels
    n_classes = np.count_nonzero(probs)
    if n_classes <= 1:
        return 0
    ent = 0.
    # Compute standard entropy.
    for i in probs:
        if i!=0:
            ent -= i * (math.log(i,n_classes))
    return ent

"""
authorid_paper={}
authorid_score={}
authorid_paperyear={}
authorid_10years={}
paper_citations={}
paper_year={}

with open('authorid_score20.txt','r') as fp:
    authorid_score=json.loads(fp.read(),encoding='utf-8')
authorid_score=convert(authorid_score)
authorid_score={int(k):[float(i) for i in v] for k,v in authorid_score.items()}

with open('authorid_paper.txt','r') as fp:
    authorid_paper=json.loads(fp.read(),encoding='utf-8')
authorid_paper=convert(authorid_paper)
authorid_paper={int(k):[int(i) for i in v] for k,v in authorid_paper.items()}

with open('authorid_paperyear.txt','r') as fp:
    authorid_paperyear=json.loads(fp.read(),encoding='utf-8')
authorid_paperyear=convert(authorid_paperyear)
authorid_paperyear={int(k):[int(i) for i in v] for k,v in authorid_paperyear.items()}

with open('authorid_20years.txt','r') as fp:
    authorid_10years=json.loads(fp.read(),encoding='utf-8')
authorid_10years=convert(authorid_10years)
authorid_10years={int(k):[int(i) for i in v] for k,v in authorid_10years.items()}

with open('paper_citations.txt','r') as fp:
    paper_citations=json.loads(fp.read(),encoding='utf-8')
paper_citations=convert(paper_citations)
paper_citations={int(k):[int(i) for i in v] for k,v in paper_citations.items()}

with open('paper_year.txt','r') as fp:
    paper_year=json.loads(fp.read(),encoding='utf-8')
paper_year=convert(paper_year)
paper_year={int(k):int(v) for k,v in paper_year.items()}

print('-------------------------------------------------------------------------')
"""

peakint={}

with open('peakmul_awake.txt','r') as fp:
    peakint=json.loads(fp.read(),encoding='utf-8')
peakint=convert(peakint)
peakint={int(k):[int(i) for i in v] for k,v in peakint.items()}

print('-------------------------------------------------------------------------')

years=[]
for key in peakint:
    oo=peakint[key]
    years.append(oo[1])

unique=[]
unique=np.unique(years)

ans=[]

for xx in unique:
    ans.append(years.count(xx)/len(years))

for i in range(len(ans)):
    print(unique[i])
    print(ans[i])
