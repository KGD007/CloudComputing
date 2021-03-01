#!/usr/bin/env python3
import sys
import json

topTitle = {}
# input comes from STDIN
for line in sys.stdin:
    topTitle = eval(line)

topTitle = sorted(topTitle.items(), key= lambda x : -x[1])
for i, j in topTitle[:10]:
    print(i+ "  " + str(j))

    # print('%s\t%s' % (  ,  )) print as final output