#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys
import math

#purchase 
p_count=0
n_count=0

topic_id = -1
for line in sys.stdin:
	cols = line.strip().split("\t")
	if topic_id == -1:
		topic_id = eval(cols[0])
	
	if topic_id != eval(cols[0]):
		print str(topic_id)+"\t"+"0:"+str(n_count)+" "+"1:"+str(p_count)+" "+str(p_count*1.0/n_count)

		topic_id = eval(cols[0])
		p_count=0
		n_count=0
	
	if cols[1] == "0":
		n_count+=1
	elif cols[1] == "1":
		p_count+=1

