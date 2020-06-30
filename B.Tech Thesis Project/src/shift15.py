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
others={}

peakmul15={}
peaklate15={}
peakint15={}
monicr15={}
mondcr15={}
others15={}

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

with open('others.txt','r') as fp:
    others=json.loads(fp.read(),encoding='utf-8')




with open('peakmul15.txt','r') as fp:
    peakmul15=json.loads(fp.read(),encoding='utf-8')

with open('peaklate15.txt','r') as fp:
    peaklate15=json.loads(fp.read(),encoding='utf-8')

with open('peakint15.txt','r') as fp:
    peakint15=json.loads(fp.read(),encoding='utf-8')

with open('monicr15.txt','r') as fp:
    monicr15=json.loads(fp.read(),encoding='utf-8')

with open('mondcr15.txt','r') as fp:
    mondcr15=json.loads(fp.read(),encoding='utf-8')

with open('others15.txt','r') as fp:
    others15=json.loads(fp.read(),encoding='utf-8')




peakmul=convert(peakmul)
peaklate=convert(peaklate)
peakint=convert(peakint)
monicr=convert(monicr)
mondcr=convert(mondcr)
others=convert(others)


peakmul15=convert(peakmul15)
peaklate15=convert(peaklate15)
peakint15=convert(peakint15)
monicr15=convert(monicr15)
mondcr15=convert(mondcr15)
others15=convert(others15)

peakmul={int(k):str(v) for k,v in peakmul.items()}
peaklate={int(k):str(v) for k,v in peaklate.items()}
peakint={int(k):str(v) for k,v in peakint.items()}
monicr={int(k):str(v) for k,v in monicr.items()}
mondcr={int(k):str(v) for k,v in mondcr.items()}
others={int(k):str(v) for k,v in others.items()}

peakmul15={int(k):str(v) for k,v in peakmul15.items()}
peaklate15={int(k):str(v) for k,v in peaklate15.items()}
peakint15={int(k):str(v) for k,v in peakint15.items()}
monicr15={int(k):str(v) for k,v in monicr15.items()}
mondcr15={int(k):str(v) for k,v in mondcr15.items()}
others15={int(k):str(v) for k,v in others15.items()}



int_int_keys=len(set.intersection(*tuple(set(d.keys()) for d in [peakint,peakint15])))
int_late_keys=len(set.intersection(*tuple(set(d.keys()) for d in [peakint,peaklate15])))
int_mul_keys=len(set.intersection(*tuple(set(d.keys()) for d in [peakint,peakmul15])))
int_icr_keys=len(set.intersection(*tuple(set(d.keys()) for d in [peakint,monicr15])))
int_dcr_keys=len(set.intersection(*tuple(set(d.keys()) for d in [peakint,mondcr15])))
int_oth_keys=len(set.intersection(*tuple(set(d.keys()) for d in [peakint,others15])))

late_int_keys=len(set.intersection(*tuple(set(d.keys()) for d in [peaklate,peakint15])))
late_mul_keys=len(set.intersection(*tuple(set(d.keys()) for d in [peaklate,peakmul15])))
late_late_keys=len(set.intersection(*tuple(set(d.keys()) for d in [peaklate,peaklate15])))
late_icr_keys=len(set.intersection(*tuple(set(d.keys()) for d in [peaklate,monicr15])))
late_dcr_keys=len(set.intersection(*tuple(set(d.keys()) for d in [peaklate,mondcr15])))
late_oth_keys=len(set.intersection(*tuple(set(d.keys()) for d in [peaklate,others15])))

mul_mul_keys=len(set.intersection(*tuple(set(d.keys()) for d in [peakmul,peakmul15])))
mul_late_keys=len(set.intersection(*tuple(set(d.keys()) for d in [peakmul,peaklate15])))
mul_int_keys=len(set.intersection(*tuple(set(d.keys()) for d in [peakmul,peakint15])))
mul_icr_keys=len(set.intersection(*tuple(set(d.keys()) for d in [peakmul,monicr15])))
mul_dcr_keys=len(set.intersection(*tuple(set(d.keys()) for d in [peakmul,mondcr15])))
mul_oth_keys=len(set.intersection(*tuple(set(d.keys()) for d in [peakmul,others15])))

icr_icr_keys=len(set.intersection(*tuple(set(d.keys()) for d in [monicr,monicr15])))
icr_dcr_keys=len(set.intersection(*tuple(set(d.keys()) for d in [monicr,mondcr15])))
icr_mul_keys=len(set.intersection(*tuple(set(d.keys()) for d in [monicr,peakmul15])))
icr_int_keys=len(set.intersection(*tuple(set(d.keys()) for d in [monicr,peakint15])))
icr_late_keys=len(set.intersection(*tuple(set(d.keys()) for d in [monicr,peaklate15])))
icr_oth_keys=len(set.intersection(*tuple(set(d.keys()) for d in [monicr,others15])))


dcr_dcr_keys=len(set.intersection(*tuple(set(d.keys()) for d in [mondcr,mondcr15])))
dcr_icr_keys=len(set.intersection(*tuple(set(d.keys()) for d in [mondcr,monicr15])))
dcr_int_keys=len(set.intersection(*tuple(set(d.keys()) for d in [mondcr,peakint15])))
dcr_mul_keys=len(set.intersection(*tuple(set(d.keys()) for d in [mondcr,peakmul15])))
dcr_late_keys=len(set.intersection(*tuple(set(d.keys()) for d in [mondcr,peaklate15])))
dcr_oth_keys=len(set.intersection(*tuple(set(d.keys()) for d in [mondcr,others15])))



oth_dcr_keys=len(set.intersection(*tuple(set(d.keys()) for d in [others,mondcr15])))
oth_icr_keys=len(set.intersection(*tuple(set(d.keys()) for d in [others,monicr15])))
oth_int_keys=len(set.intersection(*tuple(set(d.keys()) for d in [others,peakint15])))
oth_mul_keys=len(set.intersection(*tuple(set(d.keys()) for d in [others,peakmul15])))
oth_late_keys=len(set.intersection(*tuple(set(d.keys()) for d in [others,peaklate15])))
oth_oth_keys=len(set.intersection(*tuple(set(d.keys()) for d in [others,others15])))



oth_total=oth_int_keys+oth_late_keys+oth_mul_keys+oth_oth_keys+oth_icr_keys+oth_dcr_keys
int_total=int_int_keys+int_late_keys+int_mul_keys+int_icr_keys+int_dcr_keys+int_oth_keys
late_total=late_icr_keys+late_int_keys+late_dcr_keys+late_mul_keys+late_late_keys+late_oth_keys
mul_total=mul_icr_keys+mul_int_keys+mul_dcr_keys+mul_mul_keys+mul_late_keys+mul_oth_keys
icr_total=icr_int_keys+icr_dcr_keys+icr_icr_keys+icr_mul_keys+icr_late_keys+icr_oth_keys
dcr_total=dcr_int_keys+dcr_icr_keys+dcr_mul_keys+dcr_late_keys+dcr_dcr_keys+dcr_oth_keys

oth_icr_keys=oth_icr_keys/oth_total
oth_dcr_keys=oth_dcr_keys/oth_total
oth_int_keys=oth_int_keys/oth_total
oth_mul_keys=oth_mul_keys/oth_total
oth_late_keys=oth_late_keys/oth_total
oth_oth_keys=oth_oth_keys/oth_total

int_int_keys=int_int_keys/int_total
int_late_keys=int_late_keys/int_total
int_mul_keys=int_mul_keys/int_total
int_icr_keys=int_icr_keys/int_total
int_dcr_keys=int_dcr_keys/int_total
int_oth_keys=int_oth_keys/int_total

late_int_keys=late_int_keys/late_total
late_icr_keys=late_icr_keys/late_total
late_dcr_keys=late_dcr_keys/late_total
late_mul_keys=late_mul_keys/late_total
late_late_keys=late_late_keys/late_total
late_oth_keys=late_oth_keys/late_total

mul_mul_keys=mul_mul_keys/mul_total
mul_int_keys=mul_int_keys/mul_total
mul_late_keys=mul_late_keys/mul_total
mul_icr_keys=mul_icr_keys/mul_total
mul_dcr_keys=mul_dcr_keys/mul_total
mul_oth_keys=mul_oth_keys/mul_total


icr_icr_keys=icr_icr_keys/icr_total
icr_late_keys=icr_late_keys/icr_total
icr_mul_keys=icr_mul_keys/icr_total
icr_int_keys=icr_int_keys/icr_total
icr_dcr_keys=icr_dcr_keys/icr_total
icr_oth_keys=icr_oth_keys/icr_total


dcr_dcr_keys=dcr_dcr_keys/dcr_total
dcr_icr_keys=dcr_icr_keys/dcr_total
dcr_int_keys=dcr_int_keys/dcr_total
dcr_late_keys=dcr_late_keys/dcr_total
dcr_mul_keys=dcr_mul_keys/dcr_total
dcr_oth_keys=dcr_oth_keys/dcr_total

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

print('int-oth')
print(int_oth_keys)


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

print('late-oth')
print(late_oth_keys)



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

print('mul-oth')
print(mul_oth_keys)


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

print('icr-oth')
print(icr_oth_keys)


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

print('dcr-oth')
print(dcr_oth_keys)


print('oth_int')
print(oth_int_keys)

print('oth_late')
print(oth_late_keys)

print('oth_mul')
print(oth_mul_keys)

print('oth_icr')
print(oth_icr_keys)

print('oth_dcr')
print(oth_dcr_keys)

print('oth_oth')
print(oth_oth_keys)
