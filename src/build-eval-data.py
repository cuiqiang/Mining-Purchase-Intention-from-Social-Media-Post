#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys
import math

args = []
for arg in sys.argv[1:]:
	args.append(arg)

sample_file = args[0]
raw_file=args[1]

dic={}

for line in open(sample_file):
    cols = line.strip().split("\t")
    dic[cols[1]]=1

for line in open(raw_file):
    secs = line.strip().split(chr(1))
    if dic.has_key(secs[1]):
    	print line.strip()
