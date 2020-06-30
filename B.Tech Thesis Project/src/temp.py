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
            paper_year[index]=year
        except Exception:
            pass
    if re.match('#%.*',line):
        line=line.rstrip()
        cit=int(line[2:])
        paper_citations.setdefault(cit,[])
        paper_citations[cit].append(index)


authorid_author={}           #authorid->authorname
for line in open('AMiner-Author.txt'):
    if re.match('#index.*',line):
        line=line.rstrip()
        index=int(line[7:])
    if re.match('#n.*',line):
        line=line.rstrip()
        name=line[3:]
        authorid_author[index]=name






























"""
    ### CODE TO CALCULATE Hbar-INDEX
    h_index=authorid_hindex[key]
    temp=h_index-1
    count=0
    h_bar=0
    ## FIRST ITERATION FOR H-BAR
    while temp>=0:
        if (modpubs[temp] in paper_author.keys()):
            templist=paper_author[modpubs[temp]]
            for x in templist:
                if x in authorname_hindex.keys() and x is not authorid_author[key]:
                    if authorname_hindex[x]>sortedcit[temp]:
                        count=count-1
                        break
        temp=temp-1



    if count==0:
        h_bar=h_index
    else:
        temp=h_index
        ## SECOND ITERATION FOR H-BAR
        while temp<len(sortedcit):
            if sortedcit[temp]>=(h_index-count):
                if(modpubs[temp] in paper_author.keys()):
                    templist=paper_author[modpubs[temp]]
                    flag=1
                    for x in templist:
                        if x in authorname_hindex.keys() and x is not authorid_author[key]:
                            if authorname_hindex[x]>sortedcit[temp]:
                                flag=0
                                break
                    if flag==1:
                        count=count+1
                    else:
                        flag=1
            temp=temp+1
        h_bar=h_index-count
"""
