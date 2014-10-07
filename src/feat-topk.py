#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys
import math

args = []
for arg in sys.argv[1:]:
	args.append(arg)

file = args[0]
topk = eval(args[1])

pre_class = ""
k = 0
feat_num=1
for line in open(file):
	line = line.strip()
	cols = line.split("\t")

	if pre_class == "":
		pre_class = cols[0]
	if pre_class != cols[0]:
		pre_class = cols[0]
		k = 0

	if k < topk:
		print cols[1]+"\t"+str(feat_num)
		feat_num+=1
		k+=1
