#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys
import math

args = []
for arg in sys.argv[1:]:
	args.append(arg)

file = args[0]

cat_stat={}
buffer=[]
for line in open(file):
	line = line.strip()
	buffer.append(line)
	cols = line.split("\t")

	if cat_stat.has_key(cols[0]):
		cat_stat[cols[0]]+=1
	else:
		cat_stat[cols[0]]=1

	predict=""
	for (k,v) in cat_stat.iteritems():
		predict+=k+"\""+str(v)+","	

for line in buffer:
	print predict+"\t"+line
