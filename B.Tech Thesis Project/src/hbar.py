#Script To Calculate The Hbar index of All Authors.
import re
import json
import pprint
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

authorid_hindex={}            #authorid->h_index
authorid_hbarindex={}         #authorid->h_barindex
authorid_author={}            #authorid->authorname
authorname_hindex={}          #authorname->h_index
paper_citations={}            #paperindex->citations
author_paper={}               #authorname->paperindex
paper_author={}               #paperindex->authors

with open('h_index.txt','r') as fp:
    authorid_hindex=json.loads(fp.read(),encoding='utf-8')

with open('authorid_author.txt','r') as fp:
    authorid_author=json.loads(fp.read(),encoding='utf-8')

with open('paper_citations.txt','r') as fp:
    paper_citations=json.loads(fp.read(),encoding='utf-8')

with open('author_paper.txt','r') as fp:
    author_paper=json.loads(fp.read(),encoding='utf-8')

with open('paper_author.txt','r') as fp:
    paper_author=json.loads(fp.read(),encoding='utf-8')


authorid_hindex=convert(authorid_hindex)
authorid_author=convert(authorid_author)
paper_citations=convert(paper_citations)
author_paper=convert(author_paper)
paper_author=convert(paper_author)

authorid_author={int(k):str(v) for k,v in authorid_author.items()}
authorid_hindex={int(k):int(v) for k,v in authorid_hindex.items()}
paper_citations={int(k):[int(i) for i in v] for k,v in paper_citations.items()}
author_paper={str(k):[int(i) for i in v] for k,v in author_paper.items()}
paper_author={int(k):[str(i) for i in v] for k,v in paper_author.items()}

print('------------------------------------------------------------------------')

for key in authorid_author:
    authorname_hindex[authorid_author[key]]=authorid_hindex[key]


print('------------------------------------------------------------------------')
#Code To Calculate hbar_index
for key in authorid_author:
    print(key)
    search=authorid_author[key]
    pubs=[]
    citcount=[]
    if search in author_paper:
        for x in author_paper[search]:
            if x in paper_citations:
                citcount.append(len(paper_citations[x]))
                pubs.append(x)
            else:
                citcount.append(0)
                pubs.append(x)


    combine=sorted(zip(citcount,pubs),reverse=True)
    sortedcit=[e[0] for e in combine]
    modpubs=[e[1] for e in combine]

    h_index=authorid_hindex[key]
    temp=h_index-1
    count=0
    h_bar=0
    ## FIRST ITERATION FOR H-BAR
    while temp>=0:
        if (modpubs[temp] in paper_author):
            templist=paper_author[modpubs[temp]]
            for x in templist:
                if x in authorname_hindex and x is not authorid_author[key]:
                    if authorname_hindex[x]>sortedcit[temp]:
                        count=count-1
                        break
        temp=temp-1
    nex=0

    if count==0:
        h_bar=h_index
    else:
        temp=h_index
        ## SECOND ITERATION FOR H-BAR
        while temp<len(sortedcit):
            if sortedcit[temp]>=(h_index+count):
                if(modpubs[temp] in paper_author):
                    templist=paper_author[modpubs[temp]]
                    flag=1
                    for x in templist:
                        if x in authorname_hindex and x is not authorid_author[key]:
                            if authorname_hindex[x]>sortedcit[temp]:
                                flag=0
                                break
                    if flag==1:
                        nex=nex+1
                    else:
                        flag=1
            temp=temp+1
        h_bar=h_index+count+nex


    authorid_hbarindex[key]=h_bar

with open('hbar_index.txt','w') as fp:
    json.dump(authorid_hbarindex,fp,indent=4)

with open('authorname_hindex.txt','w') as fp:
    json.dump(authorname_hindex,fp,indent=4)
