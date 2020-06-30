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


peaklate={}

uu=[]
tt=[]
maximum=0

for key in authorid_score:
    normalised=authorid_score[key]
    max_value=max(normalised)
    if max_value==0:
        max_value=1
    for y in range(len(normalised)):
        normalised[y]=normalised[y]/max_value

    cb=np.array(normalised)
    indexes=peakutils.indexes(cb, thres=0.75, min_dist=2)

    if len(indexes)==1 and indexes[0]>=4:
            cumu=[]
            consider_paper=[]
            contribute=[]
            window=indexes[0]+2
            if key in authorid_paper and key in authorid_paperyear:
                consider_paper=authorid_paper[key]
                contribute=authorid_paperyear[key]
                first_year=contribute[0]
                consider=first_year+window
                length=len(consider_paper)
                x=0
                while x<length:
                    counter=0
                    if contribute[x]<=consider:
                        if consider_paper[x] in paper_citations:
                            templist=paper_citations[consider_paper[x]]
                            for paper in templist:
                                if paper in paper_year and paper_year[paper]==consider:
                                    counter=counter+1
                        if counter>=maximum:
                            maximum=counter
                            uu.append(consider_paper[x])
                            tt.append(key)
                    x=x+1

print(maximum)
print(uu[-1])
print(tt[-1])
