from __future__ import division
import matplotlib.pyplot as plt
import pprint
import re
import json
import math
import os
import numpy as np
import peakutils
# ImPortant Function
def convert(input):
    if isinstance(input, dict):
        return {convert(key): convert(value) for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [convert(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input

peakmul={}
peaklate={}
peakint={}
monicr={}
mondcr={}

peakmul15={}
peaklate15={}
peakint15={}
monicr15={}
mondcr15={}

with open('peakmul.txt','r') as fp:
    peakmul=json.loads(fp.read(),encoding='utf-8')

with open('peaklate.txt','r') as fp:
    peaklate=json.loads(fp.read(),encoding='utf-8')

with open('peakint.txt','r') as fp:
    peakint=json.loads(fp.read(),encoding='utf-8')

with open('monicr.txt','r') as fp:
    monicr=json.loads(fp.read(),encoding='utf-8')

with open('mondcr.txt','r') as fp:
    mondcr=json.loads(fp.read(),encoding='utf-8')



with open('peakmul20.txt','r') as fp:
    peakmul15=json.loads(fp.read(),encoding='utf-8')

with open('peaklate20.txt','r') as fp:
    peaklate15=json.loads(fp.read(),encoding='utf-8')

with open('peakint20.txt','r') as fp:
    peakint15=json.loads(fp.read(),encoding='utf-8')

with open('monicr20.txt','r') as fp:
    monicr15=json.loads(fp.read(),encoding='utf-8')

with open('mondcr20.txt','r') as fp:
    mondcr15=json.loads(fp.read(),encoding='utf-8')



peakmul=convert(peakmul)
peaklate=convert(peaklate)
peakint=convert(peakint)
monicr=convert(monicr)
mondcr=convert(mondcr)


peakmul15=convert(peakmul15)
peaklate15=convert(peaklate15)
peakint15=convert(peakint15)
monicr15=convert(monicr15)
mondcr15=convert(mondcr15)


peakmul={int(k):str(v) for k,v in peakmul.items()}
peaklate={int(k):str(v) for k,v in peaklate.items()}
peakint={int(k):str(v) for k,v in peakint.items()}
monicr={int(k):str(v) for k,v in monicr.items()}
mondcr={int(k):str(v) for k,v in mondcr.items()}


peakmul15={int(k):str(v) for k,v in peakmul15.items()}
peaklate15={int(k):str(v) for k,v in peaklate15.items()}
peakint15={int(k):str(v) for k,v in peakint15.items()}
monicr15={int(k):str(v) for k,v in monicr15.items()}
mondcr15={int(k):str(v) for k,v in mondcr15.items()}


int_int_keys=len(set.intersection(*tuple(set(d.keys()) for d in [peakint,peakint15])))
int_late_keys=len(set.intersection(*tuple(set(d.keys()) for d in [peakint,peaklate15])))
int_mul_keys=len(set.intersection(*tuple(set(d.keys()) for d in [peakint,peakmul15])))
int_icr_keys=len(set.intersection(*tuple(set(d.keys()) for d in [peakint,monicr15])))
int_dcr_keys=len(set.intersection(*tuple(set(d.keys()) for d in [peakint,mondcr15])))

late_int_keys=len(set.intersection(*tuple(set(d.keys()) for d in [peaklate,peakint15])))
late_mul_keys=len(set.intersection(*tuple(set(d.keys()) for d in [peaklate,peakmul15])))
late_late_keys=len(set.intersection(*tuple(set(d.keys()) for d in [peaklate,peaklate15])))
late_icr_keys=len(set.intersection(*tuple(set(d.keys()) for d in [peaklate,monicr15])))
late_dcr_keys=len(set.intersection(*tuple(set(d.keys()) for d in [peaklate,mondcr15])))

mul_mul_keys=len(set.intersection(*tuple(set(d.keys()) for d in [peakmul,peakmul15])))
mul_late_keys=len(set.intersection(*tuple(set(d.keys()) for d in [peakmul,peaklate15])))
mul_int_keys=len(set.intersection(*tuple(set(d.keys()) for d in [peakmul,peakint15])))
mul_icr_keys=len(set.intersection(*tuple(set(d.keys()) for d in [peakmul,monicr15])))
mul_dcr_keys=len(set.intersection(*tuple(set(d.keys()) for d in [peakmul,mondcr15])))

icr_icr_keys=len(set.intersection(*tuple(set(d.keys()) for d in [monicr,monicr15])))
icr_dcr_keys=len(set.intersection(*tuple(set(d.keys()) for d in [monicr,mondcr15])))
icr_mul_keys=len(set.intersection(*tuple(set(d.keys()) for d in [monicr,peakmul15])))
icr_int_keys=len(set.intersection(*tuple(set(d.keys()) for d in [monicr,peakint15])))
icr_late_keys=len(set.intersection(*tuple(set(d.keys()) for d in [monicr,peaklate15])))

dcr_dcr_keys=len(set.intersection(*tuple(set(d.keys()) for d in [mondcr,mondcr15])))
dcr_icr_keys=len(set.intersection(*tuple(set(d.keys()) for d in [mondcr,monicr15])))
dcr_int_keys=len(set.intersection(*tuple(set(d.keys()) for d in [mondcr,peakint15])))
dcr_mul_keys=len(set.intersection(*tuple(set(d.keys()) for d in [mondcr,peakmul15])))
dcr_late_keys=len(set.intersection(*tuple(set(d.keys()) for d in [mondcr,peaklate15])))


int_total=int_int_keys+int_late_keys+int_mul_keys+int_icr_keys+int_dcr_keys
late_total=late_icr_keys+late_int_keys+late_dcr_keys+late_mul_keys+late_late_keys
mul_total=mul_icr_keys+mul_int_keys+mul_dcr_keys+mul_mul_keys+mul_late_keys
icr_total=icr_int_keys+icr_dcr_keys+icr_icr_keys+icr_mul_keys+icr_late_keys
dcr_total=dcr_int_keys+dcr_icr_keys+dcr_mul_keys+dcr_late_keys+dcr_dcr_keys


int_int_keys=int_int_keys/len(peakint)
int_late_keys=int_late_keys/len(peakint)
int_mul_keys=int_mul_keys/len(peakint)
int_icr_keys=int_icr_keys/len(peakint)
int_dcr_keys=int_dcr_keys/len(peakint)

late_int_keys=late_int_keys/len(peaklate)
late_icr_keys=late_icr_keys/len(peaklate)
late_dcr_keys=late_dcr_keys/len(peaklate)
late_mul_keys=late_mul_keys/len(peaklate)
late_late_keys=late_late_keys/len(peaklate)

mul_mul_keys=mul_mul_keys/len(peakmul)
mul_int_keys=mul_int_keys/len(peakmul)
mul_late_keys=mul_late_keys/len(peakmul)
mul_icr_keys=mul_icr_keys/len(peakmul)
mul_dcr_keys=mul_dcr_keys/len(peakmul)


icr_icr_keys=icr_icr_keys/len(monicr)
icr_late_keys=icr_late_keys/len(monicr)
icr_mul_keys=icr_mul_keys/len(monicr)
icr_int_keys=icr_int_keys/len(monicr)
icr_dcr_keys=icr_dcr_keys/len(monicr)


dcr_dcr_keys=dcr_dcr_keys/len(mondcr)
dcr_icr_keys=dcr_icr_keys/len(mondcr)
dcr_int_keys=dcr_int_keys/len(mondcr)
dcr_late_keys=dcr_late_keys/len(mondcr)
dcr_mul_keys=dcr_mul_keys/len(mondcr)

print('int-late')
print(int_late_keys)

print('int-mul')
print(int_mul_keys)

print('int-int')
print(int_int_keys)

print('int-icr')
print(int_icr_keys)

print('int-dcr')
print(int_dcr_keys)



print('late-late')
print(late_late_keys)

print('late-mul')
print(late_mul_keys)

print('late-int')
print(late_int_keys)

print('late-icr')
print(late_icr_keys)

print('late-dcr')
print(late_dcr_keys)




print('mul-late')
print(mul_late_keys)

print('mul-mul')
print(mul_mul_keys)

print('mul-int')
print(mul_int_keys)

print('mul-icr')
print(mul_icr_keys)

print('mul-dcr')
print(mul_dcr_keys)



print('icr-late')
print(icr_late_keys)

print('icr-mul')
print(icr_mul_keys)

print('icr-int')
print(icr_int_keys)

print('icr-icr')
print(icr_icr_keys)

print('icr-dcr')
print(icr_dcr_keys)


print('dcr-late')
print(dcr_late_keys)

print('dcr-mul')
print(dcr_mul_keys)

print('dcr-int')
print(dcr_int_keys)

print('dcr-icr')
print(dcr_icr_keys)

print('dcr-dcr')
print(dcr_dcr_keys)
