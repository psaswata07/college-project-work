import re
import json
import pprint
import math
import dateparser
import time
import datetime
import numpy as np
import csv

# The following dictionaries store records of confidence values of events in each category against time stamps where time stamps are the keys
tilt_confidence={}  # For Tilting
vehicle_confidence={} # For InVehicle
bicycle_confidence={} # For OnBicycle
walk_confidence={} # For Walking
foot_confidence={} # For OnFoot
run_confidence={} # For Running
still_confidence={} # For Still
un_confidence={} # For Unknown

str1='Confidence:'
str2='Time:'

alltime=[] # A list to store all timestamps across all the eight categories

for line in open('/home/saswata/Activity/911310450659249_05162016_Activity.txt'):
    if('Tilting' in line):
        ind1=line.index(str1)
        ind2=line.index(str2)
        confidence=line[ind1+11:ind2-1] # Stores the confidence value
        datetimestring=(line[ind2+6:len(line)])   # Stores the time value
        timestamp=int(time.mktime(time.strptime(datetimestring,'%a %b %d %H:%M:%S GMT+05:30 %Y\n')))
        #print(time.ctime(timestamp)) To Be Used On Later
        alltime.append(timestamp)
        if timestamp in tilt_confidence:
            print('Occuring At Same Time')
            if tilt_confidence[timestamp]<confidence:
                tilt_confidence[timestamp]=confidence
        else:
            tilt_confidence[timestamp]=confidence
    elif('InVehicle' in line):
        ind1=line.index(str1)
        ind2=line.index(str2)
        confidence=line[ind1+11:ind2-1] # Stores the confidence value
        datetimestring=(line[ind2+6:len(line)])   # Stores the time value
        timestamp=int(time.mktime(time.strptime(datetimestring,'%a %b %d %H:%M:%S GMT+05:30 %Y\n')))
        alltime.append(timestamp)
        if timestamp in vehicle_confidence:
            print('Occuring At Same Time')
            if vehicle_confidence[timestamp]<confidence:
                vehicle_confidence[timestamp]=confidence
        else:
            vehicle_confidence[timestamp]=confidence
    elif('Still' in line):
        ind1=line.index(str1)
        ind2=line.index(str2)
        confidence=line[ind1+11:ind2-1] # Stores the confidence value
        datetimestring=(line[ind2+6:len(line)])   # Stores the time value
        timestamp=int(time.mktime(time.strptime(datetimestring,'%a %b %d %H:%M:%S GMT+05:30 %Y\n')))
        alltime.append(timestamp)
        if timestamp in still_confidence:
            print('Occuring At Same Time')
            if still_confidence[timestamp]<confidence:
                still_confidence[timestamp]=confidence
        else:
            still_confidence[timestamp]=confidence
    elif('Unknown' in line):
        ind1=line.index(str1)
        ind2=line.index(str2)
        confidence=line[ind1+11:ind2-1] # Stores the confidence value
        datetimestring=(line[ind2+6:len(line)])   # Stores the time value
        timestamp=int(time.mktime(time.strptime(datetimestring,'%a %b %d %H:%M:%S GMT+05:30 %Y\n')))
        alltime.append(timestamp)
        if timestamp in un_confidence:
            print('Occuring At Same Time')
            if un_confidence[timestamp]<confidence:
                un_confidence[timestamp]=confidence
        else:
            un_confidence[timestamp]=confidence
    elif('OnBicycle' in line):
        ind1=line.index(str1)
        ind2=line.index(str2)
        confidence=line[ind1+11:ind2-1] # Stores the confidence value
        datetimestring=(line[ind2+6:len(line)])   # Stores the time value
        timestamp=int(time.mktime(time.strptime(datetimestring,'%a %b %d %H:%M:%S GMT+05:30 %Y\n')))
        alltime.append(timestamp)
        if timestamp in bicycle_confidence:
            print('Occuring At Same Time')
            if bicycle_confidence[timestamp]<confidence:
                bicycle_confidence[timestamp]=confidence
        else:
            bicycle_confidence[timestamp]=confidence
    elif('Walking' in line):
        ind1=line.index(str1)
        ind2=line.index(str2)
        confidence=line[ind1+11:ind2-1] # Stores the confidence value
        datetimestring=(line[ind2+6:len(line)])   # Stores the time value
        timestamp=int(time.mktime(time.strptime(datetimestring,'%a %b %d %H:%M:%S GMT+05:30 %Y\n')))
        alltime.append(timestamp)
        if timestamp in walk_confidence:
            print('Occuring At Same Time')
            if walk_confidence[timestamp]<confidence:
                walk_confidence[timestamp]=confidence
        else:
            walk_confidence[timestamp]=confidence
    elif('OnFoot' in line):
        ind1=line.index(str1)
        ind2=line.index(str2)
        confidence=line[ind1+11:ind2-1] # Stores the confidence value
        datetimestring=(line[ind2+6:len(line)])   # Stores the time value
        timestamp=int(time.mktime(time.strptime(datetimestring,'%a %b %d %H:%M:%S GMT+05:30 %Y\n')))
        alltime.append(timestamp)
        if timestamp in foot_confidence:
            print('Occuring At Same Time')
            if foot_confidence[timestamp]<confidence:
                foot_confidence[timestamp]=confidence
        else:
            foot_confidence[timestamp]=confidence
    elif('Running' in line):
        ind1=line.index(str1)
        ind2=line.index(str2)
        confidence=line[ind1+11:ind2-1] # Stores the confidence value
        datetimestring=(line[ind2+6:len(line)])   # Stores the time value
        timestamp=int(time.mktime(time.strptime(datetimestring,'%a %b %d %H:%M:%S GMT+05:30 %Y\n')))
        alltime.append(timestamp)
        if timestamp in run_confidence:
            print('Occuring At Same Time')
            if run_confidence[timestamp]<confidence:
                run_confidence[timestamp]=confidence
        else:
            run_confidence[timestamp]=confidence

alltime=list(set(alltime))
min_timestamp=min(alltime)
max_timestamp=max(alltime)

cols=len(alltime)+1
rows=9
ent_mat=[[0 for x in range(cols)] for y in range(rows)]

uu=1
ent_mat[0][0]='Act/Time'
for k in range(len(alltime)):
    ent_mat[0][uu]=alltime[k]
    uu=uu+1


activities=['Tilting','InVehicle','OnBicyle','Walking','Running','OnFoot','Still','Unknown']

uu=1
for k in range(len(activities)):
    ent_mat[uu][0]=activities[k]
    uu=uu+1


#Tilting
uu=1
index=0
max_conf=-1
for k in range(len(alltime)):
    if alltime[k] in tilt_confidence:
        if max_conf<tilt_confidence[alltime[k]]:
            max_conf=tilt_confidence[alltime[k]]
            index=1
    if alltime[k] in vehicle_confidence:
        if max_conf<vehicle_confidence:
            max_conf=vehicle_confidence[alltime[k]]
            index=2
    if alltime[k] in run_confidence:
        if max_conf<run_confidence[alltime[k]]:
            max_conf=run_confidence[alltime[k]]
            index=5
    if alltime[k] in still_confidence:
        if max_conf<still_confidence[alltime[k]]:
            max_conf=still_confidence[alltime[k]]
            index=7
    if alltime[k] in foot_confidence:
        if max_conf<foot_confidence[alltime[k]]:
            max_conf=foot_confidence[alltime[k]]
            index=6
    if alltime[k] in walk_confidence:
        if max_conf<walk_confidence[alltime[k]]:
            max_conf=walk_confidence[alltime[k]]
            index=4
    if alltime[k] in bicycle_confidence:
        if max_conf<bicycle_confidence[alltime[k]]:
            max_conf=bicycle_confidence[alltime[k]]
            index=3
    if alltime[k] in un_confidence:
        if max_conf<un_confidence[alltime[k]]:
            max_conf=un_confidence[alltime[k]]
            index=8
    max_conf=-1
    ent_mat[index][uu]=1
    uu=uu+1
    index=0


with open('ent_mat_15_May.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(ent_mat)

print('\n'.join([''.join(['{:4}'.format(item) for item in row])
      for row in ent_mat]))
