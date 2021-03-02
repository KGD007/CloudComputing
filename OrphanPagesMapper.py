#!/usr/bin/env python3
import sys

from_link = {}
to_link = {}
for line in sys.stdin:
  key , values = line.split(':')[0], line.split(':')[1]
  from_link[int(key)] = True
  values = values.strip().split(' ')
  for value in values:
    if int(value) != int(key):
      to_link[int(value)] = True

print(str(from_link) + '\t' +str(to_link))
# print('%s\t%s' % (  ,  )) pass this output to reducer