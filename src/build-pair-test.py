#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys
import math

args = []
for arg in sys.argv[1:]:
	args.append(arg)

file = args[0]
cat_id = args[2]


feat_dic={}
for line in open(args[1]):
	line = line.strip()
	cols = line.split("\t")
	feat_dic[cols[0]]=eval(cols[1])

for line in open(file):
	line = line.strip()
	cols = line.split("\t")
	secs = cols[1].split(" ")

	word_vec = {}
	for i in range(len(secs)):
		v = secs[i].split(":")
		word_vec[cat_id+"_"+v[0]]=eval(v[1])

	word_fea = {}
	for feat in feat_dic:
		if word_vec.has_key(feat):
			word_fea[feat_dic[feat]]=word_vec[feat]
	if len(word_fea) == 0:
		continue
	
	output=""

	label = "1"
	output += label

	output += "\t"
	
	word_fea_sort=sorted(word_fea.iteritems(),key=lambda d:d[0])
	for (k,v) in word_fea_sort:
		output += str(k)+":"+str(v)+" "
	print output
