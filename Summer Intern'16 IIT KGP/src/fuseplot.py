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
import matplotlib.pyplot as plt



with open('/home/saswata/Activity/Activity Data/New/User 6/869071023132955_fuse_mat_(31,7)_May_June_Tuesdays.csv','rb') as f:
    reader=csv.reader(f)
    ent_mat=list(reader)

activities=['Tilting','InVehicle','OnFoot','Walking','Still','OnBicycle','Running','Unknown']

minutes=map(int,ent_mat[0][1:])

tilt=map(float,ent_mat[1][1:])
vehicle=map(float,ent_mat[2][1:])
foot=map(float,ent_mat[3][1:])
walk=map(float,ent_mat[4][1:])
still=map(float,ent_mat[5][1:])
bicycle=map(float,ent_mat[6][1:])
run=map(float,ent_mat[7][1:])
un=map(float,ent_mat[8][1:])

pump=100

tilt=[x*pump for x in tilt]
vehicle=[x*pump for x in vehicle]
foot=[x*pump for x in foot]
walk=[x* pump for x in walk]
still=[x* pump for x in still]
bicycle=[x*pump for x in bicycle]
run=[x*pump for x in run]
un=[x*pump for x in un]

tilt_avg=np.mean(tilt)
vehicle_avg=np.mean(vehicle)
foot_avg=np.mean(foot)
walk_avg=np.mean(walk)
still_avg=np.mean(still)
bicycle_avg=np.mean(bicycle)
run_avg=np.mean(run)
un_avg=np.mean(un)


num1=[]
num2=[]
num3=[]
num4=[]
num5=[]
num6=[]
num7=[]
num8=[]




min1=[]
min2=[]
min3=[]
min4=[]
min5=[]
min6=[]
min7=[]
min8=[]

for x in range(len(minutes)):

    if(tilt[x]>=tilt_avg and tilt[x]):
        num1.append(1)
        min1.append(minutes[x]/60)
    if(vehicle[x]>=vehicle_avg and vehicle[x]):
        num2.append(2)
        min2.append(minutes[x]/60)
    if(foot[x]>=foot_avg and foot[x]):
        num3.append(3)
        min3.append(minutes[x]/60)
    if(walk[x]>=walk_avg and walk[x]):
        num4.append(4)
        min4.append(minutes[x]/60)
    if(still[x]>=still_avg and still[x]):
        num5.append(5)
        min5.append(minutes[x]/60)
    if(bicycle[x]>=bicycle_avg and bicycle[x]):
        num6.append(6)
        min6.append(minutes[x]/60)
    if(run[x]>=run_avg and run[x] and run[x]):
        num7.append(7)
        min7.append(minutes[x]/60)
    if(un[x]>=un_avg and un[x]):
        num8.append(8)
        min8.append(minutes[x]/60)

plt.xlabel('Time In Hours')
plt.ylabel('Activity Being Performed')

if len(num1):
    plt.scatter(min1,num1, s=10, c='r')
if len(num2):
    plt.scatter(min2,num2, s=10, c='g')
if len(num3):
    plt.scatter(min3,num3, s=10, c='b')
if len(num4):
    plt.scatter(min4,num4, s=10, c='c')
if len(num5):
    plt.scatter(min5,num5, s=10, c='y')
if len(num6):
    plt.scatter(min6,num6, s=10, c='b')
if len(num7):
    plt.scatter(min7,num7, s=10, c='r')
if len(num8):
    plt.scatter(min8,num8, s=10, c='m')

plt.xlim(0,24)
plt.ylim(0,8)
plt.annotate('1.Tilting 2.InVehicle 3.OnFoot 4.Walking 5.Still 6.OnBicycle 7.Running 8.Unknown', xy=(0.3, 1.0), xycoords='axes fraction')
fig=plt.gcf()
fig.set_size_inches(20,10.5)

fig.savefig('/home/saswata/Activity/Activity Data/New/User 6/869071023132955_fuse_mat_(31,7)_May_June_Tuesdays_Activity_Graph.png')


"""
Tilting->Red
InVehicle->Green
OnBicycle->Cyan
Still->Yellow
Walk->Blue
Unknown->Black
OnFoot->White
Running->Magneta


plt.xlabel('Time In Hours')
plt.ylabel('Nature of Activity Above Threshold')
plt.plot(min1,tilt.values(),'r',label='continuous')
plt.plot(min2,vehicle.values(),'g',label='continuous')
plt.plot(min3,bicycle.values(),'c',label='continuous')
plt.plot(min4,still.values(),'y',label='continuous')
plt.plot(min5,walk.values(),'b',label='continuous')
plt.plot(min6,un.values(),'k',label='continuous')
plt.plot(min7,foot.values(),'w*',label='continuous')
plt.plot(min8,run.values(),'m',label='continuous')
plt.xlim(0,24)
plt.ylim(0,1.1)
fig=plt.gcf()
ax = plt.subplot(111)
fig.set_size_inches(20,5)
box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.1,box.width, box.height * 0.9])
ax.legend([x for x in activities],loc='upper center', bbox_to_anchor=(0.5, -0.05),fancybox=True, shadow=True, ncol=4)
fig.savefig('/home/saswata/Activity/Activity Data/User 9/869071023132955_Fuse_Graph.png')
plt.clf()
"""
