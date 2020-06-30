import re
import json
import math
authorid_author={}           #authorid->authorname
for line in open('AMiner-Author.txt'):
    if re.match('#index.*',line):
        line=line.rstrip()
        index=int(line[7:])
    if re.match('#n.*',line):
        line=line.rstrip()
        name=line[3:]
        authorid_author[index]=name

authorid_papers={}      #authorid->papers
authorid_years={}       #authorid->years of publications in sorted order.
paper_citations={}      #paperid->citationsid
paper_year={}           #paperid->year
author_paper={}             #authorname->papers

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

authorid_paper={}
authorid_paperyear={}

for key in authorid_author:
    print(key)
    papers=[]
    years=[]
    sortpapers=[]
    sortyears=[]
    search=authorid_author[key]
    if search in author_paper:
        for x in author_paper[search]:
            papers.append(x)
            if x in paper_year:
                years.append(paper_year[x])

        combine=sorted(zip(years,papers),reverse=False)
        sortyears=[e[0] for e in combine]
        sortpapers=[e[1] for e in combine]
        if len(sortyears)>0 and len(sortpapers)>0:
            for xx in sortpapers:
                authorid_paper.setdefault(key,[])
                authorid_paper[key].append(xx)
            for yy in sortyears:
                authorid_paperyear.setdefault(key,[])
                authorid_paperyear[key].append(yy)

with open('authorid_paperyear.txt','w') as fp:
    json.dump(authorid_paperyear,fp,indent=4)

with open('authorid_paper.txt','w') as fp:
    json.dump(authorid_paper,fp,indent=4)
