#!/usr/bin/env python3
import sys

links = {}
# input comes from STDIN
for line in sys.stdin:
    values = line.strip().split(':')
    for value in values:
        if value.strip() in links.keys():
            links[value.strip()] += 1
        else:
            links[value.strip()] = 1

print(links)
# print('%s\t%s' % (  ,  )) print as final output