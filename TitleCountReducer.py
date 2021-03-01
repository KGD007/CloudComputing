#!/usr/bin/env python3
from operator import itemgetter
import sys

#TODO
words = {}
# input comes from STDIN
for line in sys.stdin:
    line = line.strip()
    if line in words:
        words[line] += 1
    else:
        words[line] = 1


print(words)
# print('%s\t%s' % (  ,  )) print as final output