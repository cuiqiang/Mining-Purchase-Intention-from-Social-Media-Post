#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys
import math

args = []
for arg in sys.argv[1:]:
	args.append(arg)

model_file = args[0]
topics_num = eval(args[1])


for line in open(model_file):
	secs = line.strip().split(" ")

	topic_count={}
	for i in range(len(secs)):
		v = secs[i].split(":")
		if topic_count.has_key(eval(v[1])):
			topic_count[eval(v[1])]+=1
		else:
			topic_count[eval(v[1])]=1
	
	topic_vector=""
	for i in range(1,topics_num+1):
		if topic_count.has_key(i):
			topic_vector+=str(i)+":"+str(topic_count[i])+" "
		else:
			topic_vector+=str(i)+":0 "
	
	print topic_vector
