from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import csv
import math
import copy


with open('/home/saswata/Activity/Activity Data/User 9/869071023132955_05302016_Ent_Mat(0-1).csv','rb') as f:
    reader=csv.reader(f)
    ent_mat1=list(reader)

with open('/home/saswata/Activity/Activity Data/User 9/869071023132955_05312016_Ent_Mat(0-1).csv','rb') as f:
    reader=csv.reader(f)
    ent_mat2=list(reader)

with open('/home/saswata/Activity/Activity Data/User 9/869071023132955_06012016_Ent_Mat(0-1).csv','rb') as f:
    reader=csv.reader(f)
    ent_mat3=list(reader)

with open('/home/saswata/Activity/Activity Data/User 9/869071023132955_06022016_Ent_Mat(0-1).csv','rb') as f:
    reader=csv.reader(f)
    ent_mat4=list(reader)

with open('/home/saswata/Activity/Activity Data/User 9/869071023132955_06032016_Ent_Mat(0-1).csv','rb') as f:
    reader=csv.reader(f)
    ent_mat5=list(reader)

with open('/home/saswata/Activity/Activity Data/User 9/869071023132955_06062016_Ent_Mat(0-1).csv','rb') as f:
    reader=csv.reader(f)
    ent_mat6=list(reader)

with open('/home/saswata/Activity/Activity Data/User 9/869071023132955_06072016_Ent_Mat(0-1).csv','rb') as f:
    reader=csv.reader(f)
    ent_mat7=list(reader)



min_time=0
max_time=1439

cols=max_time-min_time+1+1
rows=12
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



x=1
while x<9:
    y=1
    uu=min_time
    while uu<=max_time:
        ent_mat[x][y]=int(ent_mat1[x][y])+int(ent_mat2[x][y])+int(ent_mat3[x][y])+int(ent_mat4[x][y])+int(ent_mat5[x][y])+int(ent_mat6[x][y])+int(ent_mat7[x][y])+ent_mat[x][y]
        ent_mat[x][y]=ent_mat[x][y]/float(7)
        uu=uu+1
        y=y+1
    x=x+1

ent_mat[9][0]='Rank 1'
ent_mat[10][0]='Rank 2'
ent_mat[11][0]='Rank 3'

min_time=0
max_time=1439

uu=min_time
yy=1
while uu<=max_time:
    content=[]
    xx=1
    while xx<9:
        content.append(ent_mat[xx][yy])
        xx=xx+1
    acti=copy.copy(activities)
    z=zip(content,acti)
    z.sort(reverse=True)
    rr=[e[0] for e in z]
    tt=[e[1] for e in z]
    ent_mat[9][yy]=tt[0]
    if rr[1]>0:
        ent_mat[10][yy]=tt[1]
    else:
        ent_mat[10][yy]='-'
    if rr[2]>0:
        ent_mat[11][yy]=tt[2]
    else:
        ent_mat[11][yy]='-'
    del(content)
    del(acti)
    del(rr)
    del(tt)
    uu=uu+1
    yy=yy+1

with open('/home/saswata/Activity/Activity Data/User 9/869071023132955_fuse_mat_(30,31,1,2,3,6,7)_Mean_May_June.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(ent_mat)
