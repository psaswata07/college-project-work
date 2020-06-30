from __future__ import division
import matplotlib.pyplot as plt
import numpy as np

minutes=[]
activity=[]
number=[]

for line in open('/media/saswata/AC1A-5D1D/plotting2_modified.txt'):
    content=line.split(',')
    minutes.append(content[0])
    activity.append(content[1])

minutes=map(int,minutes)
number=activity
number=map(int,number)

"""
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
"""
minutes1=[]
minutes2=[]

number1=[]
number2=[]

max_time=max(minutes)
min_time=min(minutes)




x=0
while min_time<=max_time:
    if min_time not in minutes:
        minutes.insert(x,min_time)
        number.insert(x,number[x-1])
        print(min_time)
    x=x+1
    min_time=min_time+1


min_time=0
max_time=1439


uu=0

while uu<=max_time:
    if uu <= 720:
        if uu in minutes:
            minutes1.append(uu)
            ind=minutes.index(uu)
            number1.append(number[ind])
        else:
            minutes1.append(uu)
            number1.append(5)
    else:
        if uu in minutes:
            minutes2.append(uu)
            ind=minutes.index(uu)
            number2.append(number[ind])
        else:
            minutes2.append(uu)
            number2.append(5)
    uu=uu+1

for x in range(len(minutes1)):
    minutes1[x]=minutes1[x]/60

for y in range(len(minutes2)):
    minutes2[y]=minutes2[y]/60




plt.xlabel('Time In Hours')
plt.ylabel('Activity Being Performed')
plt.scatter(minutes2,number2, s=10, c='r')
#plt.plot(minutes2,number2,'ro')
plt.xlim(min(minutes2),max(minutes2))
plt.ylim(0,8)
plt.annotate('1.Tilting 2.InVehicle 3.OnFoot 4.Walking 5.Still 6.OnBicycle 7.Running 8.Unknown', xy=(0.3, 1.0), xycoords='axes fraction')
fig=plt.gcf()
fig.set_size_inches(20,10.5)
fig.savefig('/media/saswata/AC1A-5D1D/Activity_Graph.png')
#plt.savefig('Activity_Graph_16_May.png')
plt.clf()
