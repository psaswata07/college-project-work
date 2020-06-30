from __future__ import division
import matplotlib.pyplot as plt
import pprint
import re
import json
import math
import os
import numpy
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





author_paper={}
paper_citations={}
authorid_author={}           #authorid->authorname
paper_author={}
for line in open('AMiner-Author.txt'):
    if re.match('#index.*',line):
        line=line.rstrip()
        index=int(line[7:])
    if re.match('#n.*',line):
        line=line.rstrip()
        name=line[3:]
        authorid_author[index]=name



for line in open('AMiner-Paper.txt'):
    if re.match('#index.*',line):
        line=line.rstrip()
        index=int(line[6:])
    if re.match('#@.*',line):
        line=line.rstrip()
        authors=line[2:]
        templist=authors.split(';')
        for x in templist:
            x=x.rstrip()
            if x !="":
                author_paper.setdefault(x,[])
                author_paper[x].append(index)
                paper_author.setdefault(index,[])
                paper_author[index].append(x)
    if re.match('#%.*',line):
        line=line.rstrip()
        cit=int(line[2:])
        paper_citations.setdefault(cit,[])
        paper_citations[cit].append(index)


print('========================================================================>')

peakint={}
peaklate={}
peakmul={}
monicr={}
mondcr={}
authorid_10pubs={}



icr=[]
dcr=[]
mul=[]
late=[]
init=[]



with open('authorid_10pubs.txt','r') as fp:
    authorid_10pubs=json.loads(fp.read(),encoding='utf-8')

with open('peakint.txt','r') as fp:
    peakint=json.loads(fp.read(),encoding='utf-8')

with open('peaklate.txt','r') as fp:
    peaklate=json.loads(fp.read(),encoding='utf-8')

with open('peakmul.txt','r') as fp:
    peakmul=json.loads(fp.read(),encoding='utf-8')

with open('monicr.txt','r') as fp:
    monicr=json.loads(fp.read(),encoding='utf-8')

with open('mondcr.txt','r') as fp:
    mondcr=json.loads(fp.read(),encoding='utf-8')



authorid_10pubs=convert(authorid_10pubs)
peakint=convert(peakint)
peakmul=convert(peakmul)
monicr=convert(monicr)
mondcr=convert(mondcr)
peaklate=convert(peaklate)



peakint={int(k):str(v) for k,v in peakint.items()}
peakmul={int(k):str(v) for k,v in peakmul.items()}
peaklate={int(k):str(v) for k,v in peaklate.items()}
monicr={int(k):str(v) for k,v in monicr.items()}
mondcr={int(k):str(v) for k,v in mondcr.items()}
authorid_10pubs={int(k):[int(i) for i in v] for k,v in authorid_10pubs.items()}


print('========================================================================>')


for key in authorid_10pubs:
    print(key)
    search=authorid_author[key]
    count=0
    if key in peakint:
        if search in author_paper:
            paper=author_paper[search]
            for x in paper:
                if x in paper_citations:
                    lis=paper_citations[x]
                    for y in lis:
                        if y in paper_author:
                            names=paper_author[y]
                            if search in names:
                                count=count+1
            init.append(count)
    elif key in peakmul:
        if search in author_paper:
            paper=author_paper[search]
            for x in paper:
                if x in paper_citations:
                    lis=paper_citations[x]
                    for y in lis:
                        if y in paper_author:
                            names=paper_author[y]
                            if search in names:
                                count=count+1
            mul.append(count)
    elif key in peaklate:
        if search in author_paper:
            paper=author_paper[search]
            for x in paper:
                if x in paper_citations:
                    lis=paper_citations[x]
                    for y in lis:
                        if y in paper_author:
                            names=paper_author[y]
                            if search in names:
                                count=count+1
            late.append(count)
    elif key in monicr:
        if search in author_paper:
            paper=author_paper[search]
            for x in paper:
                if x in paper_citations:
                    lis=paper_citations[x]
                    for y in lis:
                        if y in paper_author:
                            names=paper_author[y]
                            if search in names:
                                count=count+1
            icr.append(count)
    elif key in mondcr:
        if search in author_paper:
            paper=author_paper[search]
            for x in paper:
                if x in paper_citations:
                    lis=paper_citations[x]
                    for y in lis:
                        if y in paper_author:
                            names=paper_author[y]
                            if search in names:
                                count=count+1
            dcr.append(count)



mean_init=numpy.mean(init)
mean_late=numpy.mean(late)
mean_icr=numpy.mean(icr)
mean_dcr=numpy.mean(dcr)
mean_mul=numpy.mean(mul)

std_init=numpy.std(init)
std_late=numpy.std(late)
std_mul=numpy.std(mul)
std_icr=numpy.std(icr)
std_dcr=numpy.std(dcr)

print('\n')
print('\n')
print('MEAN IN PEAKLATE:')
print(mean_late)
print('MEAN IN PEAKINT:')
print(mean_init)
print('MEAN IN PEAKMUL:')
print(mean_mul)
print('MEAN IN MONDCR:')
print(mean_dcr)
print('MEAN IN MONICR:')
print(mean_icr)

print('\n')
print('\n')
print('STD IN PEAKLATE')
print(std_late)
print('STD IN PEAKINT')
print(std_init)
print('STD IN PEAKMUL')
print(std_mul)
print('STD IN MONDCR')
print(std_dcr)
print('STD IN MONICR')
print(std_icr)
