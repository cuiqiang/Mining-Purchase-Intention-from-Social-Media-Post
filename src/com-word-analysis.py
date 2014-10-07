#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys
import math

args = []
for arg in sys.argv[1:]:
	args.append(arg)

doc_file=args[0]

for line in open(doc_file):
    cols = line.strip().split("\t")
    secs = cols[0].split(" ")
    for i in range(len(secs)):
    	print secs[i]+"\t"+cols[1]


