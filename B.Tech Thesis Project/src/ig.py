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



#Declarations of Data structures
paper_year={ }              #paperindex->paperyear
paper_author={ }            #paperindex->authors
paper_citations= { }        #paperindex->citations
paper_title={ }             #paperindex->papername

authorid_author={}           #authorid->authorname
authorid_pubs={}             #authorid->number of publications






# Reading from json Files
with open('paper_year.txt','r') as fp:
    paper_year=json.loads(fp.read(),encoding='utf-8')

with open('paper_author.txt','r') as fp:
    paper_author=json.loads(fp.read(),encoding='utf-8')

with open('paper_title.txt','r') as fp:
    paper_title=json.loads(fp.read(),encoding='utf-8')

with open('paper_citations.txt','r') as fp:
    paper_citations=json.loads(fp.read(),encoding='utf-8')

with open('authorid_author.txt','r') as fp:
    authorid_author=json.loads(fp.read(),encoding='utf-8')

with open('authorid_pubs.txt','r') as fp:
    authorid_pubs=json.loads(fp.read(),encoding='utf-8')





#ConverSion Phase
paper_author=convert(paper_author)
paper_year=convert(paper_year)
paper_title=convert(paper_title)
paper_citations=convert(paper_citations)
authorid_author=convert(authorid_author)
authorid_pubs=convert(authorid_pubs)




#Maitaining uniformity among the data structures
paper_year= {int(k):int(v) for k,v in paper_year.items()}
paper_author= {int(k):[str(i) for i in v] for k,v in paper_author.items()}
paper_citations={int(k):[int(i) for i in v] for k,v in paper_citations.items()}
paper_title={int(k):str(v) for k,v in paper_title.items()}
authorid_pubs={int(k):int(v) for k,v in authorid_pubs.items()}
authorid_author={int(k):str(v) for k,v in authorid_author.items()}


pprint.pprint(authorid_author)








































"""
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
    print('m-index of this author is %d'%m_index)
    authorid_mindex[key]=m_index
    print('m-quotient of this author is %d'%m_quo)
    authorid_mqou[key]=m_quo
"""
