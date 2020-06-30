#Supporting Script to calculate important indexes of Authors.

from __future__ import division
import re
import json
import pprint
import math
paper_year={ }              #paperindex->paperyear
paper_author={ }            #paperindex->authors
paper_citations= { }        #paperindex->citations
paper_title={ }             #paperindex->papername
author_paper={}             #authorname->papers
for line in open('AMiner-Paper.txt'):
    if re.match('#index.*',line):
        line=line.rstrip()
        index=int(line[6:])
    if re.match('(#)(\*).*',line):
        line=line.rstrip()
        title=line[2:]
        paper_title[index]=title
    if re.match('#@.*',line):
        line=line.rstrip()
        authors=line[2:]
        templist=authors.split(';')
        for x in templist:
            x=x.rstrip()
            paper_author.setdefault(index,[])
            paper_author[index].append(x)
            if x !=" ":
                author_paper.setdefault(x,[])
                author_paper[x].append(index)
    if re.match('#t.*',line):
        line=line.rstrip()
        line=re.sub(r'\s+', '',line)
        try:
            year=int(line[2:])
            paper_year[index]=year
        except Exception:
            pass
    if re.match('#%.*',line):
        line=line.rstrip()
        cit=int(line[2:])
        paper_citations.setdefault(cit,[])
        paper_citations[cit].append(index)


authorid_author={}           #authorid->authorname
authorid_pubs={}             #authorid->number of publications
authorid_fyear={}              #authorid->First Year of Publication
authorid_lyear={}              #authorid->Last Year Of Publication
for line in open('AMiner-Author.txt'):
    if re.match('#index.*',line):
        line=line.rstrip()
        index=int(line[7:])
    if re.match('#n.*',line):
        line=line.rstrip()
        name=line[3:]
        authorid_author[index]=name
    if re.match('#pc.*',line):
        line=line.rstrip()
        p=int(line[4:])
        authorid_pubs[index]=p




authorid_hindex={}
authorid_gindex={}
authorid_h2index={}
authorid_aindex={}
authorid_rindex={}
authorid_mqou={}
authorid_arindex={}
authorid_mindex={}


for key in authorid_author:
    print(key)
    search=authorid_author[key]
    pubs=[]
    citcount=[]
    mini=10000
    maxi=0
    if search in author_paper:
        for x in author_paper[search]:
            if x in paper_year:
                if mini>paper_year[x]:
                    mini=paper_year[x]
                if maxi<paper_year[x]:
                    maxi=paper_year[x]
            if x in paper_citations:
                citcount.append(len(paper_citations[x]))
                pubs.append(x)
            else:
                citcount.append(0)
                pubs.append(x)
    authorid_fyear[key]=mini
    authorid_lyear[key]=maxi
    combine=sorted(zip(citcount,pubs),reverse=True)
    sortedcit=[e[0] for e in combine]
    modpubs=[e[1] for e in combine]

    h_index=0
    g_index=0
    h2_index=0
    a_index=0
    r_index=0
    m_quo=0
    ar_index=0
    m_index=0
    gcount=[]

    #Calculation For h-index
    for x in range(len(sortedcit)):
        if sortedcit[x]>=(x+1):
            h_index=x+1
        else:
            break

    #Calculation For g-index
    s=0
    for x in range(len(sortedcit)):
        s=s+sortedcit[x]
        gcount.append(s)

    for x in range(len(gcount)):
        if gcount[x]>=((x+1)*(x+1)):
            g_index=x+1
        else:
            break

    #Calculation For h(2)-index
    for x in range(len(sortedcit)):
        if sortedcit[x]>=((x+1)*(x+1)):
            h2_index=x+1
        else:
            break

    #Calculation For a-index
    x=0
    while x<h_index:
         a_index=a_index+sortedcit[x]
         x=x+1
    r_index=a_index

    if h_index!=0:
        a_index=(a_index/(h_index))

    #Calculation For r-index
    r_index=math.sqrt(r_index)

    #Calculation For M-QUOTIENT
    if(authorid_lyear[key]-authorid_fyear[key]!=0 and authorid_lyear[key]!=0 and authorid_fyear[key]!=10000):
        m_quo=(h_index/(authorid_lyear[key]-authorid_fyear[key]))

    #Calculation For ar-index

    #Calculation For m-index
    x=0
    arr=[]
    while x < h_index:
        arr.append(sortedcit[x])
        x=x+1

    arr.sort(reverse=False)
    if h_index==0:
        m_index=0
    elif (h_index%2)==0:
        yy=h_index
        m_index=(arr[ (yy-1) //2 ] + arr[( (yy-1)//2 ) + 1 ])//2
    else:
        yy=h_index
        m_index=arr[(yy-1)//2]


    authorid_hindex[key]=h_index
    authorid_gindex[key]=g_index
    authorid_h2index[key]=h2_index
    authorid_rindex[key]=r_index
    authorid_aindex[key]=a_index
    authorid_mindex[key]=m_index
    authorid_mqou[key]=m_quo

with open('h_index.txt','w') as fp:
    json.dump(authorid_hindex,fp,indent=4)

with open('g_index.txt','w') as fp:
    json.dump(authorid_gindex,fp,indent=4)

with open('h2_index.txt','w') as fp:
    json.dump(authorid_h2index,fp,indent=4)

with open('a_index.txt','w') as fp:
    json.dump(authorid_aindex,fp,indent=4)

with open('r_index.txt','w') as fp:
    json.dump(authorid_rindex,fp,indent=4)

with open('m_index.txt','w') as fp:
    json.dump(authorid_mindex,fp,indent=4)

with open('m_quo.txt','w') as fp:
    json.dump(authorid_mqou,fp,indent=4)

with open('authorid_lyear.txt','w') as fp:
	json.dump(authorid_lyear,fp,indent=4)

with open('authorid_fyear.txt','w') as fp:
	json.dump(authorid_fyear,fp,indent=4)

with open('author_paper.txt','w') as fp:
    json.dump(author_paper,fp,indent=4)
