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
for line in open('/home/saswata/Activity/ToBeUploaded_final/865980023587063_05162016_Activity.txt'):
    content=line.split(',')
    activity1.append(content[2])
    seconds1.append(content[1])
seconds1=map(int,seconds1)


max_time=1439
min_time=0

#Matrix Formation Begins From Here.
cols=max_time-min_time+1+1
rows=9
ent_mat=[[0 for x in range(cols)] for y in range(rows)]

ent_mat[0][0]='Act/Time'

uu=min_time
i=1
while uu<=max_time:
    ent_mat[0][i]=uu
    uu=uu+1
    i=i+1

activities=['Tilting','InVehicle','OnFoot','Walking','Still','OnBicycle','Running','Unknown']
uu=1
for k in range(len(activities)):
    ent_mat[uu][0]=activities[k]
    uu=uu+1

uu=min_time
i=1
while uu<=max_time:
    if uu in seconds1:
        ind=seconds1.index(uu)
        if(activity1[ind]=='Tilting'):
            ent_mat[1][i]=1
        elif(activity1[ind]=='InVehicle'):
            ent_mat[2][i]=1
        elif(activity1[ind]=='OnBicycle'):
            ent_mat[3][i]=1
        elif(activity1[ind]=='Walking'):
            ent_mat[4][i]=1
        elif(activity1[ind]=='Running'):
            ent_mat[5][i]=1
        elif(activity1[ind]=='OnFoot'):
            ent_mat[6][i]=1
        elif(activity1[ind]=='Still'):
            ent_mat[7][i]=1
        elif(activity1[ind]=='Unknown'):
            ent_mat[8][i]=1
    else:
        ent_mat[7][i]=1
    i=i+1
    uu=uu+1

with open('/home/saswata/Activity/ToBeUploaded_final/.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(ent_mat)
