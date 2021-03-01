#!/usr/bin/env python3
import sys

# TODO

wordsCount = {}
for line in sys.stdin:
       words = eval(line)
       for key, value in words.items():
              if key not in wordsCount:
                     wordsCount[key] = int(value)
              else:
                     wordsCount[key] += int(value)

#TODO
print(wordsCount)
# print('%s\t%s' % (  ,  )) pass this output to reducer