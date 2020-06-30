from __future__ import division
import matplotlib.pyplot as plt
import pprint
import re
import json
import math
import os
import numpy as np
import peakutils
import operator
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


paper_title={}

with open('paper_title.txt','r') as fp:
    paper_title=json.loads(fp.read(),encoding='utf-8')

paper_title=convert(paper_title)
paper_title={int(k):str(v) for k,v in paper_title.items()}

peakmul={}

with open('peaklatepapers20.txt','r') as fp:
    peakmul=json.loads(fp.read(),encoding='utf-8')


peakmul=convert(peakmul)

peakmul={int(k):str(v) for k,v in peakmul.items()}

paper_20years={}

with open('paper_20year.txt','r') as fp:
    paper_20years=json.loads(fp.read(),encoding='utf-8')
paper_20years=convert(paper_20years)
paper_20years={int(k):[int(i) for i in v] for k,v in paper_20years.items()}


mul_paper=[]

mul_cit=[]


for paper in paper_title:
    if paper in paper_20years:
        cit=sum(paper_20years[paper])
        if paper in peakmul:
            mul_paper.append(paper_title[paper])
            mul_cit.append(cit)



dicti={}
for x in range(len(mul_cit)):
    dicti[mul_paper[x]]=mul_cit[x]



sorted_x = sorted(dicti.items(), key=operator.itemgetter(1),reverse=True)
print(sorted_x[0])
print(sorted_x[1])
print(sorted_x[2])
