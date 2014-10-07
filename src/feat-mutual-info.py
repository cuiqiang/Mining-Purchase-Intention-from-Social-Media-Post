#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys
import math

args = []
for arg in sys.argv[1:]:
	args.append(arg)

file = args[0]
topk = eval(args[1])
#dat = open(cate_id+".dat","w")

word_class_count={}
word_count={}
class_count={}

for line in open(file):
	line = line.strip()
	cols = line.split("\t")

	if class_count.has_key(cols[0]):
		class_count[cols[0]]+=1
	else:
		class_count[cols[0]]=1
	
	word_vector=cols[1].split(" ")
	word_dic={}
	for i in range(len(word_vector)):
		word_dic[word_vector[i]]=1
	for word in word_dic:
		if word_count.has_key(word):
			word_count[word]+=1
		else:
			word_count[word]=1

		if word_class_count.has_key(cols[0]+chr(1)+word):
			word_class_count[cols[0]+chr(1)+word]+=1
		else:
			word_class_count[cols[0]+chr(1)+word]=1

feat_mi={}

for (k,v) in word_class_count.items():
	pair = k.split(chr(1))
	cc = class_count[pair[0]]
	wc = word_count[pair[1]]
	mi = v*1.0/(wc*cc)
	if wc > 1:
		if feat_mi.has_key(pair[0]):
			feat_mi[pair[0]][pair[1]]=mi
		else:
			feat_mi[pair[0]]={}
			feat_mi[pair[0]][pair[1]]=mi

for k in feat_mi:
	sort=sorted(feat_mi[k].iteritems(),key=lambda d:d[1],reverse=True)
	idx=0
	for (key,value) in sort:
		if idx < topk:
			print key
		idx+=1
