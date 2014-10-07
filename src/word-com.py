#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys
import math

#purchase 
p_count=0
n_count=0

word = ""
for line in sys.stdin:
	cols = line.strip().split("\t")
	if(len(cols) == 1):
		continue
	if word == "":
		word = cols[0]
	
	if word != cols[0] and p_count+n_count > 500:
		print word+"\t"+"0:"+str(n_count)+" "+"1:"+str(p_count)+" "+str(p_count*1.0/(p_count+n_count))

		word = cols[0]
		p_count=0
		n_count=0
	
	if cols[1] == "0":
		n_count+=1
	elif cols[1] == "1":
		p_count+=1

