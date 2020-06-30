from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import csv

minutes=[]
activity=[]
number=[]

for line in open('/home/saswata/Activity/Activity Data/New/User 6/869071023132955_06092016_finalfile.txt'):
    content=line.split(',')
    minutes.append(content[0])
    activity.append(content[1])


minutes=map(int,minutes)


for x in activity:
    if x=='Tilting\n':
        number.append(1)
    elif x=='InVehicle\n':
        number.append(2)
    elif x=='OnFoot\n':
        number.append(3)
    elif x=='Still\n':
        number.append(5)
    elif x=='Walking\n':
        number.append(4)
    elif x=='OnBicycle\n':
        number.append(6)
    elif x=='Running\n':
        number.append(7)
    elif x=='Unknown\n':
        number.append(8)
    else:
        print(x)

minutes1=[]
number1=[]

max_time=max(minutes)
min_time=min(minutes)

x=0
while min_time<=max_time:
    if min_time not in minutes:
        minutes.insert(x,min_time)
        number.insert(x,number[x-1])
    x=x+1
    min_time=min_time+1


min_time=0
max_time=1439

uu=0
while uu<=max_time:
    if uu in minutes:
        minutes1.append(uu)
        ind=minutes.index(uu)
        number1.append(number[ind])
    else:
        minutes1.append(uu)
        number1.append(5)
    uu=uu+1

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
    if uu in minutes1:
        ind=minutes1.index(uu)
        ent_mat[number1[ind]][i]=1
    i=i+1
    uu=uu+1

with open('/home/saswata/Activity/Activity Data/New/User 6/869071023132955_06092016_Ent_Mat(0-1).csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(ent_mat)
