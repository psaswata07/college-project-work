from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import csv
import math
import copy
import pprint
import json


with open('/home/saswata/Activity/Activity Data/User 5/Modified/911310450659249_05192016_Ent_Mat(0-1).csv','rb') as f:
    reader=csv.reader(f)
    ent_mat1=list(reader)

with open('/home/saswata/Activity/Activity Data/User 5/Modified/911310450659249_05202016_Ent_Mat(0-1).csv','rb') as f:
    reader=csv.reader(f)
    ent_mat2=list(reader)

with open('/home/saswata/Activity/Activity Data/User 5/Modified/911310450659249_05212016_Ent_Mat(0-1).csv','rb') as f:
    reader=csv.reader(f)
    ent_mat3=list(reader)

with open('/home/saswata/Activity/Activity Data/User 5/Modified/911310450659249_05222016_Ent_Mat(0-1).csv','rb') as f:
    reader=csv.reader(f)
    ent_mat4=list(reader)

with open('/home/saswata/Activity/Activity Data/User 5/Modified/911310450659249_05232016_Ent_Mat(0-1).csv','rb') as f:
    reader=csv.reader(f)
    ent_mat5=list(reader)

with open('/home/saswata/Activity/Activity Data/User 5/Modified/911310450659249_05242016_Ent_Mat(0-1).csv','rb') as f:
    reader=csv.reader(f)
    ent_mat6=list(reader)

with open('/home/saswata/Activity/Activity Data/User 5/Modified/911310450659249_05252016_Ent_Mat(0-1).csv','rb') as f:
    reader=csv.reader(f)
    ent_mat7=list(reader)


activities=['Tilting','InVehicle','OnFoot','Walking','Still','OnBicycle','Running','Unknown']

min_time=0
max_time=1439

min_first=12*60
max_first=15*60

time_acti={}


uu=min_first+1
while uu<=max_first:
    time_acti.setdefault(min_first,[])
    x=1
    while x<9:
        if(int(ent_mat1[x][uu])==1):
            time_acti[min_first].append(activities[x-1])
        if(int(ent_mat2[x][uu])==1):
            time_acti[min_first].append(activities[x-1])
        if(int(ent_mat3[x][uu])==1):
            time_acti[min_first].append(activities[x-1])
        if(int(ent_mat4[x][uu])==1):
            time_acti[min_first].append(activities[x-1])
        if(int(ent_mat5[x][uu])==1):
            time_acti[min_first].append(activities[x-1])
        if(int(ent_mat6[x][uu])==1):
            time_acti[min_first].append(activities[x-1])
        if(int(ent_mat7[x][uu])==1):
            time_acti[min_first].append(activities[x-1])
        if(int(ent_mat7[x][uu])==1):
            time_acti[min_first].append(activities[x-1])
        x=x+1
    uu=uu+1
    min_first=min_first+1


with open('/home/saswata/Activity/Activity Data/User 5/Modified/911310450659249_Activity_12pm-3pm.txt','w') as fp:
    json.dump(time_acti,fp,indent=4)
