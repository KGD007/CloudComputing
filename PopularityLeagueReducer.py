#!/usr/bin/env python3
import sys
links = {}

# input comes from STDIN
for line in sys.stdin:
    links.update(eval(line))

for key, value in links.items():
    links[key] = int(value)

links = sorted(links.items(), key = lambda x : x[1])
output = []
output.append((links[0], 0))

for i in range(1, len(links)):
    if links[i][1] == links[i-1][1]:
        output.append((links[i], output[i-1][1]))
    else:
        output.append((links[i], i))

output = sorted(output, lambda x: int(x[0]))
for i, j in output:
    print(str(i) + '\t' + str(j))
# print('%s\t%s' % (  ,  )) print as final output