#!/usr/bin/env python3
import sys


leaguePath = sys.argv[1]

links = {}
test = []
with open(leaguePath) as f:
       words = f.readlines()
       for word in words:
              test.append(word.strip())


for line in sys.stdin:
       dictionary = eval(line)
       for key , value in dictionary.items():
              if key not in links:
                     links[key] = int(value)
              else:
                     links[key] += int(value)

output = {}
for key in test:
       if key in links:
              output[key] = links[key]
       else:
              output[key] = 0
print(output)
