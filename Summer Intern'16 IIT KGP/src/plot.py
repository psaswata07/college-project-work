from __future__ import division
import matplotlib.pyplot as plt
import numpy as np

minutes=[]
activity=[]
number=[]

for line in open('/home/saswata/Activity/Activity Data/User 6/Modified/activity_details_25th_May.txt'):
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



for x in range(len(minutes)):
    minutes[x]=minutes[x]/60









activities=[]
activities.append('1.Tilting')
activities.append('2.InVehicle')
activities.append('3.OnFoot')
activities.append('4.Still')
activities.append('5.Walking')
activities.append('6.OnBicycle')
activities.append('7.Running')
activities.append('8.Unknown')


plt.xlabel('Time In Hours')
plt.ylabel('Activity Being Performed')
plt.plot(minutes,number,'ro')
plt.xlim(min(minutes),max(minutes))
plt.ylim(0,8)
plt.annotate('1.Tilting 2.InVehicle 3.OnFoot 4.Walking 5.Still 6.OnBicycle 7.Running 8.Unknown', xy=(0.3, 1.0), xycoords='axes fraction')
fig=plt.gcf()
fig.set_size_inches(20,10.5)
fig.savefig('/home/saswata/Activity/Activity Data/User 6/Modified/Activity_Graph_25_May.png')
#plt.savefig('Activity_Graph_16_May.png')
plt.clf()




"""
ticks=np.arange(900,1440,)
labels=range(ticks.size)
plt.axis([min(minutes),max(minutes),1,8])
plt.xticks(ticks,labels)
ax = plt.gca()
ax.set_autoscale_on(False)
"""
