#!/usr/bin/env python3
import sys


from_link = {}
to_link = {}
output = []
for line in sys.stdin:
  key, values = line.strip().split('\t')[0], line.strip().split('\t')[1]
  from_link.update(eval(key))
  to_link.update(eval(values))

for key in from_link.keys():
  if key not in to_link.keys():
    output.append(int(key))
output = sorted(output)
for i in output:
  print(i)
# print(xx) print as final output