#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys
import math

args = []
for arg in sys.argv[1:]:
	args.append(arg)

feat_idx = eval(args[1])

label_dic={}
for line in open(args[0]):
	line = line.strip()
	label_dic[line]=1


feat_num=1
for i in label_dic:
	for j in range(1,feat_idx+1):
		print str(i)+"_"+str(j)+"\t"+str(feat_num)
		feat_num+=1
