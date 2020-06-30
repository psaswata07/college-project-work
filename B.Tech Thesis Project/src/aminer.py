#Program For Parsing The Dataset.

import re
import json
import pprint
import math

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
            paper_year.setdefault(index,[])
            paper_year[index].append(year)
        except Exception:
            pass
    if re.match('#%.*',line):
        line=line.rstrip()
        cit=int(line[2:])
        paper_citations.setdefault(cit,[])
        paper_citations[cit].append(index)


authorid_author={}           #authorid->authorname
authorid_pubs={}             #authorid->number of publications
for line in open('AMiner-Author.txt'):
    if re.match('#index.*',line):
        line=line.rstrip()
        index=int(line[7:])
    if re.match('#n.*',line):
        line=line.rstrip()
        name=line[3:]
        authorid_author[index]=name


authorid_hindex={}
authorid_gindex={}
authorid_h2index={}
authorid_aindex={}
authorid_rindex={}


authorid_citations={}
for paper in paper_citations:
    if paper in paper_author.keys():
        print(paper)
        templist=paper_author[paper]
        for x in templist:
            authorid_citations.setdefault(x,[])
            authorid_citations[x].append(paper_citations[paper])


for key in authorid_author:
    print(key)
    hcount=[]
    gcount=[]
    hcount=authorid_citations[key]
    hcount.sort(reverse=True)
    h_index=0
    g_index=0
    h2_index=0
    a_index=0
    r_index=0
    #Calculation For H-Index
    for x in range(len(hcount)):
        if hcount[x]>=(x+1):
            h_index=x+1
        else:
            break
    #Calculation For G-Index
    s=0
    for x in range(len(hcount)):
        s=s+hcount[x]
        gcount.append(s)

    for x in range(len(gcount)):
        if gcount[x]>=((x+1)*(x+1)):
            g_index=x+1
        else:
            break
    #Calculation for H(2)-Index
    for x in range(len(hcount)):
        if hcount[x]>=((x+1)*(x+1)):
            h2_index=x+1
        else:
            break
     #Calculation for A-Index
    x=0
    while x<h_index:
         a_index=a_index+hcount[x]
         x=x+1
    r_index=a_index

    if h_index!=0:
        a_index=a_index/h_index
    #Calculation for R-Index
    r_index=math.sqrt(r_index)

    print('h-index of this author is %d'%h_index)
    authorid_hindex[key]=h_index
    print('g-index of this author is %d'%g_index)
    authorid_gindex[key]=g_index
    print('h(2)-index of this author is %d'%h2_index)
    authorid_h2index[key]=h2_index
    print('a-index of this author is %d'%a_index)
    authorid_aindex[key]=a_index
    print('r-index of this author is %d'%r_index)
    authorid_rindex[key]=r_index


with open('hindex','w') as fp:
    json.dump(authorid_hindex,fp,indent=4)

with open('gindex','w') as fp:
    json.dump(authorid_gindex,fp,indent=4)

with open('h2index','w') as fp:
    json.dump(authorid_h2index,fp,indent=4)

with open('aindex','w') as fp:
    json.dump(authorid_aindex,fp,indent=4)

with open('rindex','w') as fp:
    json.dump(authorid_rindex,fp,indent=4)
