from __future__ import division
import matplotlib.pyplot as plt
import pprint
import re
import json
import math
import os
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

with open('authorid_10pubs.txt','r') as fp:
    authorid_10pubs=json.loads(fp.read(),encoding='utf-8')

with open('authorid_10years.txt','r') as fp:
    authorid_10years=json.loads(fp.read(),encoding='utf-8')

authorid_10pubs=convert(authorid_10pubs)
authorid_10years=convert(authorid_10years)

authorid_10pubs={int(k):[int(i) for i in v] for k,v in authorid_10pubs.items()}
authorid_10years={int(k):[int(i) for i in v] for k,v in authorid_10years.items()}



total=len(authorid_10pubs)
key=960217
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

print(normalised)

