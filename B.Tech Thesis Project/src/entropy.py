#To calculate entropy of all authors over a period of time taken into consideration.
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


peakmul={}

peakmul_paper_details_at_peak={}


for key in authorid_score:
    normalised=authorid_score[key]
    max_value=max(normalised)
    if max_value==0:
        max_value=1
    for y in range(len(normalised)):
        normalised[y]=normalised[y]/max_value

    cb=np.array(normalised)
    indexes=peakutils.indexes(cb, thres=0.75, min_dist=2)

    if len(indexes)>1:
        for pos in indexes:
            cumu=[]
            consider_paper=[]
            contribute=[]
            window=pos+2
            if key in authorid_paper and key in authorid_paperyear:
                list_papers=authorid_paper[key]
                list_years=authorid_paperyear[key]
                first_year=list_years[0]
                consider=window+first_year
                length=len(list_papers)
                x=0
                while x<length:
                    counter=0
                    if list_years[x]<=consider:
                        consider_paper.append(list_papers[x])
                        if list_papers[x] in paper_citations:
                            templist=paper_citations[list_papers[x]]
                            for paper in templist:
                                if paper in paper_year:
                                    if paper_year[paper]<=consider:
                                        counter=counter+1
                        contribute.append(counter)
                    x=x+1
                total_citations=sum(contribute)
                total_papers=len(contribute)
                each=total_citations/total_papers
                xx=0
                """ent=0
                while xx<total_papers:
                    try:
                        ent-=(each/total_citations)*math.log(each/total_citations,2)
                    except Exception as e:
                        pass
                    xx=xx+1
                print(ent)
                peakmul.setdefault(key,[])
                peakmul[key].append(ent)"""
                ent=0
                for xx in contribute:
                    try:
                        ent-=(xx/total_citations)*math.log(xx/total_citations,2)
                    except Exception as e:
                        pass
                print(ent)
                peakmul.setdefault(key,[])
                peakmul[key].append(ent)



with open('peakmul_entropy.txt','w') as fp:
    json.dump(peakmul,fp,indent=4)
