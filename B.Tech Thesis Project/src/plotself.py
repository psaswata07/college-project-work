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
authorid_author={}

with open('authoridself_10pubs.txt','r') as fp:
    authorid_10pubs=json.loads(fp.read(),encoding='utf-8')

with open('authoridself_10years.txt','r') as fp:
    authorid_10years=json.loads(fp.read(),encoding='utf-8')


with open('authorid_author.txt','r') as fp:
    authorid_author=json.loads(fp.read(),encoding='utf-8')


authorid_10pubs=convert(authorid_10pubs)
authorid_10years=convert(authorid_10years)
authorid_author=convert(authorid_author)



authorid_10pubs={int(k):[int(i) for i in v] for k,v in authorid_10pubs.items()}
authorid_10years={int(k):[int(i) for i in v] for k,v in authorid_10years.items()}
authorid_author={int(k):str(v) for k,v in authorid_author.items()}


total=len(authorid_10pubs)

authorid_normalised={}

peakmul={}
peaklate={}
peakint={}
monicr={}
mondcr={}



for key in authorid_10pubs:
    #print(key)
    citations=authorid_10years[key]
    pubs=authorid_10pubs[key]
    cumu=[]
    if pubs[0]==0:
        pubs[0]=1
    cumu.append(citations[0])
    x=1
    while x<11:
        cumu.append(cumu[x-1]+citations[x])
        x=x+1

    x=0
    while x<=9:
        pubs[x+1]=pubs[x]+pubs[x+1]
        x=x+1

    normalised=[]
    x=2
    while x<11:
        normalised.append(cumu[x]/pubs[x])
        x=x+1

    s=normalised[0]
    for y in range(len(normalised)):
        if s<normalised[y]:
            s=normalised[y]


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






with open('peaklateself.txt','w') as fp:
    json.dump(peaklate,fp,indent=4)

with open('peakintself.txt','w') as fp:
    json.dump(peakint,fp,indent=4)

with open('peakmulself.txt','w') as fp:
    json.dump(peakmul,fp,indent=4)

with open('monicrself.txt','w') as fp:
    json.dump(monicr,fp,indent=4)

with open('mondcrself.txt','w') as fp:
    json.dump(mondcr,fp,indent=4)



"""
    plt.xlabel('Years')
    plt.ylabel('Normalised Citation count')
    plt.plot([0,1,2,3,4,5,6,7,8],normalised, ':k',label='continuous')
    plt.savefig('/home/saswata/Plot/'+str(key)+'.png')
    plt.clf()
"""
