import re
import json
import math

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

print('-------------------------------------------------------------------------')


paper_author={}
with open('paper_author.txt','r') as fp:
    paper_author=json.loads(fp.read(),encoding='utf-8')

paper_author=convert(paper_author)
paper_author={int(k):[str(i) for i in v] for k,v in paper_author.items()}



print('-------------------------------------------------------------------------')

authorid_10years={}
authorid_10pubs={}

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



print('-------------------------------------------------------------------------')

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
        for x in sortpapers:
            authorid_papers.setdefault(key,[])
            authorid_papers[key].append(x)
        for x in sortyears:
            authorid_years.setdefault(key,[])
            authorid_years[key].append(x)

        if len(sortyears)>0 and len(sortpapers)>0:
            first_year=sortyears[0]
            last_year=sortyears[-1]
            window=first_year+10
            year_citations={}          #yearwise citations since first year
            year_pubs={}
                           #yearwise publications since first year
            x=first_year
            while x<window+1:
                year_citations[x]=0
                x=x+1

            x=first_year
            while x<window+1:
                year_pubs[x]=0
                x=x+1

            while x<=last_year:
                year_pubs[x]=0
                x=x+1


            for xx in sortpapers:
                if xx in paper_year:
                    year_pubs[paper_year[xx]]=year_pubs[paper_year[xx]]+1




            for xx in range(len(sortpapers)):
                if sortyears[xx]<=window:
                    if sortpapers[xx] in paper_citations:
                        for citer in paper_citations[sortpapers[xx]]:
                            if citer in paper_author:
                                if search not in paper_author[citer]:
                                    if citer in paper_year:
                                        if paper_year[citer]<=window:
                                            if paper_year[citer] in year_citations:
                                                year_citations[paper_year[citer]]=year_citations[paper_year[citer]]+1

            total=0
            arryear=[]
            for y in year_citations:
                total=total+year_citations[y]
                arryear.append(year_citations[y])

            arrpub=[]
            for y in year_pubs:
                arrpub.append(year_pubs[y])

            if (total/10) > 0:
                print(authorid_author[key])
                for xx in arryear:
                    authorid_10years.setdefault(key,[])
                    authorid_10years[key].append(xx)

                for y in arrpub:
                    authorid_10pubs.setdefault(key,[])
                    authorid_10pubs[key].append(y)



with open('authoridself_10pubs.txt','w') as fp:
    json.dump(authorid_10pubs,fp,indent=4)

with open('authoridself_10years.txt','w') as fp:
    json.dump(authorid_10years,fp,indent=4)
