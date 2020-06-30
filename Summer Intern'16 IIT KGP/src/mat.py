from collections import Counter
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
confi=[]
seconds=[]
activity=[]

minute_activity={}  #MinuteStamp to Activity Name
minute_confidence={} #MinuteStamp to Confidence of Corressponding Activity
minute_time={}       #Minutestamp to Exact SecondStamp of Corressponding Activity

str1='Confidence:'
str2='Time:'

for line in open('/home/saswata/Activity/Activity Data/User 5/911310450659249_06132016_Activity.txt'):
    if('Tilting' in line):
                ind1=line.index(str1)
                ind2=line.index(str2)
                confidence=int(line[ind1+11:ind2-1]) # Stores the confidence value
                datetimestring=(line[ind2+6:len(line)])   # Stores the time value
                t=time.strptime(datetimestring,'%a %b %d %H:%M:%S GMT+05:30 %Y\n')
                minute=(t.tm_hour*60) + t.tm_min
                minute_activity.setdefault(minute,[])
                minute_activity[minute].append('Tilting')
                minute_confidence.setdefault(minute,[])
                minute_confidence[minute].append(confidence)
                minute_time.setdefault(minute,[])
                minute_time[minute].append((t.tm_hour)*3600+(t.tm_min)*60+t.tm_sec)
    if('InVehicle' in line):
                ind1=line.index(str1)
                ind2=line.index(str2)
                confidence=int(line[ind1+11:ind2-1]) # Stores the confidence value
                datetimestring=(line[ind2+6:len(line)])   # Stores the time value
                t=time.strptime(datetimestring,'%a %b %d %H:%M:%S GMT+05:30 %Y\n')
                minute=(t.tm_hour*60) + t.tm_min
                minute_activity.setdefault(minute,[])
                minute_activity[minute].append('InVehicle')
                minute_confidence.setdefault(minute,[])
                minute_confidence[minute].append(confidence)
                minute_time.setdefault(minute,[])
                minute_time[minute].append((t.tm_hour)*3600+(t.tm_min)*60+t.tm_sec)

    if('OnFoot' in line):
                ind1=line.index(str1)
                ind2=line.index(str2)
                confidence=int(line[ind1+11:ind2-1]) # Stores the confidence value
                datetimestring=(line[ind2+6:len(line)])   # Stores the time value
                t=time.strptime(datetimestring,'%a %b %d %H:%M:%S GMT+05:30 %Y\n')
                minute=(t.tm_hour*60) + t.tm_min
                minute_activity.setdefault(minute,[])
                minute_activity[minute].append('OnFoot')
                minute_confidence.setdefault(minute,[])
                minute_confidence[minute].append(confidence)
                minute_time.setdefault(minute,[])
                minute_time[minute].append((t.tm_hour)*3600+(t.tm_min)*60+t.tm_sec)

    if('Walking' in line):
                ind1=line.index(str1)
                ind2=line.index(str2)
                confidence=int(line[ind1+11:ind2-1]) # Stores the confidence value
                datetimestring=(line[ind2+6:len(line)])   # Stores the time value
                t=time.strptime(datetimestring,'%a %b %d %H:%M:%S GMT+05:30 %Y\n')
                minute=(t.tm_hour*60) + t.tm_min
                minute_activity.setdefault(minute,[])
                minute_activity[minute].append('Walking')
                minute_confidence.setdefault(minute,[])
                minute_confidence[minute].append(confidence)
                minute_time.setdefault(minute,[])
                minute_time[minute].append((t.tm_hour)*3600+(t.tm_min)*60+t.tm_sec)

    if('Running' in line):
                ind1=line.index(str1)
                ind2=line.index(str2)
                confidence=int(line[ind1+11:ind2-1]) # Stores the confidence value
                datetimestring=(line[ind2+6:len(line)])   # Stores the time value
                t=time.strptime(datetimestring,'%a %b %d %H:%M:%S GMT+05:30 %Y\n')
                minute=(t.tm_hour*60) + t.tm_min
                minute_activity.setdefault(minute,[])
                minute_activity[minute].append('Running')
                minute_confidence.setdefault(minute,[])
                minute_confidence[minute].append(confidence)
                minute_time.setdefault(minute,[])
                minute_time[minute].append((t.tm_hour)*3600+(t.tm_min)*60+t.tm_sec)

    if('Still' in line):
                ind1=line.index(str1)
                ind2=line.index(str2)
                confidence=int(line[ind1+11:ind2-1]) # Stores the confidence value
                datetimestring=(line[ind2+6:len(line)])   # Stores the time value
                t=time.strptime(datetimestring,'%a %b %d %H:%M:%S GMT+05:30 %Y\n')
                minute=(t.tm_hour*60) + t.tm_min
                minute_activity.setdefault(minute,[])
                minute_activity[minute].append('Still')
                minute_confidence.setdefault(minute,[])
                minute_confidence[minute].append(confidence)
                minute_time.setdefault(minute,[])
                minute_time[minute].append((t.tm_hour)*3600+(t.tm_min)*60+t.tm_sec)

    if('OnBicycle' in line):
                ind1=line.index(str1)
                ind2=line.index(str2)
                confidence=int(line[ind1+11:ind2-1]) # Stores the confidence value
                datetimestring=(line[ind2+6:len(line)])   # Stores the time value
                t=time.strptime(datetimestring,'%a %b %d %H:%M:%S GMT+05:30 %Y\n')
                minute=(t.tm_hour*60) + t.tm_min
                minute_activity.setdefault(minute,[])
                minute_activity[minute].append('OnBicycle')
                minute_confidence.setdefault(minute,[])
                minute_confidence[minute].append(confidence)
                minute_time.setdefault(minute,[])
                minute_time[minute].append((t.tm_hour)*3600+(t.tm_min)*60+t.tm_sec)

    if('Unknown' in line):
                ind1=line.index(str1)
                ind2=line.index(str2)
                confidence=int(line[ind1+11:ind2-1]) # Stores the confidence value
                datetimestring=(line[ind2+6:len(line)])   # Stores the time value
                t=time.strptime(datetimestring,'%a %b %d %H:%M:%S GMT+05:30 %Y\n')
                minute=(t.tm_hour*60) + t.tm_min
                minute_activity.setdefault(minute,[])
                minute_activity[minute].append('Unknown')
                minute_confidence.setdefault(minute,[])
                minute_confidence[minute].append(confidence)
                minute_time.setdefault(minute,[])
                minute_time[minute].append((t.tm_hour)*3600+(t.tm_min)*60+t.tm_sec)

for key in minute_activity:
    allacti=minute_activity[key]
    confidence_list=minute_confidence[key]
    frequency=Counter(allacti)
    max_frequency=frequency[max(frequency,key=lambda i:frequency[i])]
    if key == 1164:
        print(minute_activity[1164])
        print(minute_confidence[1164])
    max_confidence=0
    for x in range(len(allacti)):
        if allacti[x]!='o':
            if (frequency[allacti[x]])==max_frequency:
                indices = [i for i, y in enumerate(allacti) if y == allacti[x]]
                s=0
                for y in indices:
                    s=s+confidence_list[y]
                s=s/len(indices)
                if(s>=max_confidence):
                    max_confidence=s
                    candidate=allacti[x]
                for y in indices:
                    allacti[y]='o'

    seconds.append(key)
    confi.append(max_confidence)
    activity.append(candidate)


zipped=zip(seconds,confi,activity)
zipped.sort()

seconds=[e[0] for e in zipped]
confi=[e[1] for e in zipped]
activity=[e[2] for e in zipped]




activity2=copy.copy(activity)
seconds2=copy.copy(seconds)
confi2=copy.copy(confi)



length=len(activity)
uu=1
while uu<length:
    if(confi[uu]<50 and uu+1<length and uu>0):
        if(confi[uu-1]>=50 and confi[uu+1]>=50):
            if confi[uu-1]>=confi[uu+1]:
                confi2[uu]=confi[uu-1]
                activity2[uu]=activity[uu-1]
            else:
                confi2[uu]=confi[uu+1]
                activity2[uu]=activity[uu+1]
    uu=uu+1



corel1=0
for xx in range(len(activity2)):
    if(activity[xx]==activity2[xx]):
        corel1=corel1+1


print(corel1)
print(length)
corel1=corel1/float(length)
print(corel1)



f=open('/home/saswata/Activity/Activity Data/User 5/911310450659249_06132016_activity_details.txt','w')
for x in range(len(activity2)):
    f.write(str(confi2[x]))
    f.write(',')
    f.write(str(seconds2[x]))
    f.write(',')
    f.write(str(activity2[x]))
    f.write(',')
    f.write('\n')
f.close()
