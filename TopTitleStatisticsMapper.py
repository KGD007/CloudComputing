#!/usr/bin/env python3
import sys

words = {}
for line in sys.stdin:
    words[line.split()[0]] = line.split()[1]
    
    # print('%s\t%s' % (  ,  )) pass this output to reducer
print(words)