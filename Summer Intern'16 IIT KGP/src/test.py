from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import csv
import math

minutes=[]
activity=[]
number=[]

for line in open('/home/saswata/Activity/Activity Data/User 5/Modified/activity_details_19th_May.txt','r'):
        content=line.split(',')
        minutes.append(content[1])
        activity.append(content[2])

minutes=map(int,minutes)

for x in activity:
    if x=='Tilting':
        number.append(1)
    elif x=='InVehicle':
        number.append(2)
    elif x=='OnFoot':
        number.append(3)
    elif x=='Still':
        number.append(5)
    elif x=='Walking':
        number.append(4)
    elif x=='OnBicycle':
        number.append(6)
    elif x=='Running':
        number.append(7)
    elif x=='Unknown':
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



out_format_str="{:<10}"*2 + "\n"   # 2 columns with 10 character width
with open("/home/saswata/Activity/Activity Data/User 5/Modified/911310450659249_05192016.txt", 'w') as of:
    for x in zip(minutes1,number1):
        of.write(out_format_str.format(*x))
