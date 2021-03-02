#!/usr/bin/env python3
import sys

links = {}

# input comes from STDIN
for line in sys.stdin:
    dictionary = eval(line)
    for key, value in dictionary.items():
        if key not in links:
            links[key] = int(value)
        else:
            links[key] += int(value)

links = sorted(links.items(), key = lambda x : x[1])
for i ,  j in links[-10:]:
    print(i + '\t' + str(j))

    # print('%s\t%s' % (  ,  )) print as final output
