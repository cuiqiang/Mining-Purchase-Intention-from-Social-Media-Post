#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys
import math

args = []
for arg in sys.argv[1:]:
	args.append(arg)

file = args[0]
top_k = eval(args[1])


NDCG=0
total=0

for line in open(file):
	line = line.strip()
	cols = line.split("\t")
	p_secs = cols[0].split(",");
	t_secs = cols[1].split(",");
	
	predict={}	
	target={}

	IDCG=0
	for i in range(len(t_secs)):
		if t_secs[i] != "":
			v = t_secs[i].split("\"")
			target[v[0]]=eval(v[1])
			IDCG+=eval(v[1])/math.log(i+2)
	
	for i in range(len(p_secs)):
		if p_secs[i] != "":
			v = p_secs[i].split("\"")
			if v[1] != "":
				predict[v[0]]=eval(v[1])

	predict_sort=sorted(predict.iteritems(),key=lambda d:d[1])
	k=0
	DCG=0
	for (key,value) in predict_sort:
		if k < top_k:
			if target.has_key(key):
				DCG+=target.get(key)/math.log(i+2)
			else:
				break
		k+=1
	
	total+=1
	NDCG+=DCG/IDCG

print "NDCG at "+str(top_k)+":"+str(NDCG*1.0/total)
