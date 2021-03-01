#!/usr/bin/env python3
import sys
import math


words = {}
allvalues = []
for line in sys.stdin:
    words = eval(line)
    for key, value in words.items():
        allvalues.append(int(value))

#TODO
mean =  math.floor(sum(allvalues) / 10)
variance = math.floor(sum([ (mean - i)**2 for i in allvalues]))
print('Mean'+ '\t' + str(mean))
print('Sum'+ '\t' + str(sum(allvalues)))
print('Min'+ '\t' + str(min(allvalues)))
print('Max'+ '\t' + str(max(allvalues)))
print('Var'+ '\t' + str(variance))


# print('%s\t%s' % (  ,  )) print as final output
