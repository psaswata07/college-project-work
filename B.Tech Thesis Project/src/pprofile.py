#Script To Classify Papers from the Dataset into Different Categories.
from __future__ import division
import matplotlib.pyplot as plt
import pprint
import re
import json
import math
import os
import numpy as np
import peakutils
paper_year={ }              #paperindex->paperyear
paper_author={ }            #paperindex->authors
paper_citations= { }        #paperindex->citations
paper_title={ }             #paperindex->papername
for line in open('AMiner-Paper.txt'):
    if re.match('#index.*',line):
        line=line.rstrip()
        index=int(line[6:])
    if re.match('(#)(\*).*',line):
        line=line.rstrip()
        title=line[2:]
        paper_title.setdefault(index,[])
        paper_title[index].append(title)
    if re.match('#@.*',line):
        line=line.rstrip()
        authors=line[2:]
        templist=authors.split(';')
        for x in templist:
            x=x.rstrip()
            paper_author.setdefault(index,[])
            paper_author[index].append(x)
    if re.match('#t.*',line):
        line=line.rstrip()
        line=re.sub(r'\s+', '',line)
        try:
            year=int(line[2:])
            #paper_year.setdefault(index,[])
            paper_year[index]=year
        except Exception:
            pass
    if re.match('#%.*',line):
        line=line.rstrip()
        cit=int(line[2:])
        paper_citations.setdefault(cit,[])
        paper_citations[cit].append(index)


print('-------------------------------------------------------------------------')

paper_cityear={}


for paper in paper_citations:
    templist=paper_citations[paper]
    for x in templist:
        if x in paper_year:
            paper_cityear.setdefault(paper,[])
            paper_cityear[paper].append(paper_year[x])

print('-------------------------------------------------------------------------')


paper_10year={}
peakmul={}
peaklate={}
peakint={}
monicr={}
mondcr={}

for paper in paper_cityear:
    years=paper_cityear[paper]
    years.sort(reverse=False)
    #first_year=years[0]
    #last_year=years[-1]
    #first=first_year[0]
    #last=last_year[0]
    year_citations=[]
    first=min(years)
    last=max(years)
    window=first+20
    #years=sum(years,[])
    count=[]

    if (last-first)>=20:
        x=first
        total=0
        while x<=last and x<=window:
            total=0
            for y in range(len(years)):
                if x==years[y]:
                    total=total+1
            count.append(total)
            x=x+1
        if sum(count)>20:
            for z in count:
                paper_10year.setdefault(paper,[])
                paper_10year[paper].append(z)



        normalised=[]
        x=0
        while x<21:
            normalised.append(count[x])
            x=x+1


        s=max(normalised)

        for y in range(len(normalised)):
            normalised[y]=normalised[y]/s

        normalised1=[]

        x=0
        while x+2<21:
            normalised1.append((normalised[x]+normalised[x+1]+normalised[x+2])/3)
            x=x+1



        cb=np.array(normalised1)
        indexes=peakutils.indexes(cb, thres=0.75, min_dist=2)

        if len(indexes)==0:
            last1=normalised1[-1]
            first1=normalised1[0]
            if first1>last1:
                mondcr[paper]=paper_title[paper]
            else:
                monicr[paper]=paper_title[paper]

        elif len(indexes)==1:
            ele=indexes[0]
            if ele>=4:
                peaklate[paper]=paper_title[paper]
            else:
                peakint[paper]=paper_title[paper]

        elif len(indexes)>1:
            peakmul[paper]=paper_title[paper]


print('\n')
print('NUMBER OF PAPERS IN PEAKINT:%d'%len(peakint))
print('NUMBER OF PAPERS IN PEAKLATE:%d'%len(peaklate))
print('NUMBER OF PAPERS IN PEAKMUL:%d'%len(peakmul))
print('NUMBER OF PAPERS IN MONICR:%d'%len(monicr))
print('NUMBER OF PAPERS IN MONDCR:%d'%len(mondcr))


with open('paper_20year.txt','w') as fp:
    json.dump(paper_10year,fp,indent=4)

with open('peaklatepapers20.txt','w') as fp:
    json.dump(peaklate,fp,indent=4)

with open('peakintpapers20.txt','w') as fp:
    json.dump(peakint,fp,indent=4)

with open('peakmulpapers20.txt','w') as fp:
    json.dump(peakmul,fp,indent=4)

with open('monicrpapers20.txt','w') as fp:
    json.dump(monicr,fp,indent=4)

with open('mondcrpapers20.txt','w') as fp:
    json.dump(mondcr,fp,indent=4)
