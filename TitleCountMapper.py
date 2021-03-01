#!/usr/bin/env python3

import sys
import string

stopWordsPath = sys.argv[1]
delimitersPath = sys.argv[2]

StopWord = {}
mapped_delimiters = ""
delimiters  = ""
# TODO
with open(stopWordsPath) as f:
    words = f.readlines()
    for word in words:
        StopWord[word.strip().lower()] = True


with open(delimitersPath) as f:
    delimiters = f.readline()
    mapped_delimiters = " " * len(delimiters)

for line in sys.stdin:
    line = line.strip()
    replace_map = str.maketrans(delimiters, mapped_delimiters)
    line = line.translate(replace_map)
    line = line.split()
    for word in line:
        if word.lower() not in StopWord and word.lower() not in delimiters:
            print(word.lower())
    # print('%s\t%s' % (  ,  )) pass this output to reducer


