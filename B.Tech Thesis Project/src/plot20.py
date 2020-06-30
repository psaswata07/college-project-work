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


authorid_20years={}
authorid_20pubs={}
authorid_author={}

with open('authorid_20pubs.txt','r') as fp:
    authorid_20pubs=json.loads(fp.read(),encoding='utf-8')

with open('authorid_20years.txt','r') as fp:
    authorid_20years=json.loads(fp.read(),encoding='utf-8')


with open('authorid_author.txt','r') as fp:
    authorid_author=json.loads(fp.read(),encoding='utf-8')


authorid_20pubs=convert(authorid_20pubs)
authorid_20years=convert(authorid_20years)
authorid_author=convert(authorid_author)



authorid_20pubs={int(k):[int(i) for i in v] for k,v in authorid_20pubs.items()}
authorid_20years={int(k):[int(i) for i in v] for k,v in authorid_20years.items()}
authorid_author={int(k):str(v) for k,v in authorid_author.items()}


total=len(authorid_20pubs)

authorid_normalised={}

peakmul={}
peaklate={}
peakint={}
monicr={}
mondcr={}

authorid_score20={}

for key in authorid_20pubs:
    #print(key)
    citations=authorid_20years[key]
    pubs=authorid_20pubs[key]
    cumu=[]
    if pubs[11]==0:
        pubs[11]=1
    uu=0
    while uu<11:
        cumu.append(0)
        uu=uu+1
    cumu.append(citations[11])
    x=12
    while x<21:
        cumu.append(cumu[x-1]+citations[x])
        x=x+1

    x=11
    while x<=19:
        pubs[x+1]=pubs[x]+pubs[x+1]
        x=x+1

    normalised=[]
    x=13
    while x<21:
        normalised.append(cumu[x]/pubs[x])
        x=x+1
    for r in normalised:
        authorid_normalised.setdefault(key,[])
        authorid_normalised[key].append(r)

with open('authorid_score20.txt','w') as fp:
    json.dump(authorid_normalised,fp,indent=4)
"""
    s=normalised[0]
    for y in range(len(normalised)):
        if s<normalised[y]:
            s=normalised[y]


    if s==0:
        s=1
        print('bal')
    for y in range(len(normalised)):
        normalised[y]=normalised[y]/s

    for r in normalised:
        authorid_normalised.setdefault(key,[])
        authorid_normalised[key].append(r)

    cb=np.array(normalised)
    indexes=peakutils.indexes(cb, thres=0.75, min_dist=2)


    if len(indexes)==0:
        last=normalised[-1]
        first=normalised[0]
        if first>last:
            mondcr[key]=authorid_author[key]
        else:
            monicr[key]=authorid_author[key]

    elif len(indexes)==1:
        ele=indexes[0]
        if ele>=4:
            peaklate[key]=authorid_author[key]
        else:
            print(indexes[0])
            print(key)
            peakint[key]=authorid_author[key]

    elif len(indexes)>1:
        peakmul[key]=authorid_author[key]



print('\n')
print('TOTAL NUMBER OF AUTHORS:%d'%total)
print('NUMBER OF AUTHORS IN PEAKINT:%d'%len(peakint))
print('NUMBER OF AUTHORS IN PEAKLATE:%d'%len(peaklate))
print('NUMBER OF AUTHORS IN PEAKMUL:%d'%len(peakmul))
print('NUMBER OF AUTHORS IN MONICR:%d'%len(monicr))
print('NUMBER OF AUTHORS IN MONDCR:%d'%len(mondcr))





with open('peaklate20.txt','w') as fp:
    json.dump(peaklate,fp,indent=4)

with open('peakint20.txt','w') as fp:
    json.dump(peakint,fp,indent=4)

with open('peakmul20.txt','w') as fp:
    json.dump(peakmul,fp,indent=4)

with open('monicr20.txt','w') as fp:
    json.dump(monicr,fp,indent=4)

with open('mondcr20.txt','w') as fp:
    json.dump(mondcr,fp,indent=4)

    plt.xlabel('Years')
    plt.ylabel('Normalised Citation count')
    plt.plot([0,1,2,3,4,5,6,7,8],normalised, ':k',label='continuous')
    plt.savefig('/home/saswata/Plot/'+str(key)+'.png')
    plt.clf()
"""
