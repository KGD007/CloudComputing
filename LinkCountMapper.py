#!/usr/bin/env python3
import sys
output = ""
for line in sys.stdin:
  key , values = line.split(':')[0], line.split(':')[1]
  for value in values.strip().split(' '):
    output += key + ':'
print(output)
