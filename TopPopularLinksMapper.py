#!/usr/bin/env python3
import sys


links = {}

for line in sys.stdin:
       dictionary = eval(line)
       for key, value in dictionary.items():
              if key not in links:
                     links[key] = int(value)
              else:
                     links[key] += int(value)


print(links)
# print('%s\t%s' % (  ,  )) pass this output to reducer
