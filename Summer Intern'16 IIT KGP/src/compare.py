from __future__ import division
import re
import json
import pprint
import math
import dateparser
import time
import datetime
import numpy as np
import csv
import itertools
import copy

activity1=[]
seconds1=[]
confi1=[]

activity2=[]
seconds2=[]
confi2=[]

activity3=[]
seconds3=[]
confi3=[]

for line in open('/home/saswata/Activity/activity_details_12th_May.txt'):
    content=line.split(',')
    activity1.append(content[2])
    seconds1.append(content[1])
    confi1.append(content[0])


confi1=map(int,confi1)



activity2=copy.copy(activity1)
seconds2=copy.copy(seconds1)
confi2=copy.copy(confi1)

activity3=copy.copy(activity1)
seconds3=copy.copy(seconds1)
confi3=copy.copy(confi1)


length=len(activity1)
uu=1
while uu<length:
    if(confi1[uu]<50):
        if(confi1[uu-1]>=50 and confi1[uu+1]>=50):
            if confi1[uu-1]>=confi1[uu+1]:
                confi2[uu]=confi1[uu-1]
                activity2[uu]=activity1[uu-1]
            else:
                confi2[uu]=confi1[uu+1]
                activity2[uu]=activity1[uu+1]
    uu=uu+1



corel1=0
for xx in range(len(activity2)):
    if(activity1[xx]==activity2[xx]):
        corel1=corel1+1


print(corel1)
print(length)
corel1=corel1/length
print(corel1)

corel2=0
for xx in range(len(activity3)):
    if(confi3[xx]>=50):
        corel2=corel2+1
corel2=corel2/length
print(corel2)
