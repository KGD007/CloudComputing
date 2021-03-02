#!/usr/bin/env python3
import sys
links = {}
local = {}
# input comes from STDIN
for line in sys.stdin:
    local.update(eval(line))

for key, value in local.items():
    if int(value) != 0:
        links[key] = int(value)

links = sorted(links.items(), key = lambda x : x[1])
output = []
output.append((links[0][0], 0))

for i in range(1, len(links)):
    if links[i][1] == links[i-1][1]:
        output.append((links[i][0], output[i-1][1]))
    else:
        output.append((links[i][0], i))
output = [(int(i), int(j)) for i , j in output]
output = sorted(output, key = lambda x: x[0])
for i, j in output:
    print(str(i) + '\t' + str(j))