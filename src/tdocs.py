#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys
import math

args = []
for arg in sys.argv[1:]:
	args.append(arg)

model_file = args[0]
dic_file=args[1]

#purchase 
doc_buy={}

idx=0
for line in open(dic_file):
    cols = line.strip().split("\t")
    secs = cols[0].split(chr(1))
    doc_buy[idx]=secs[2]+chr(1)+secs[3]
    idx=idx+1

line_num = 0
for line in open(model_file):
    max_idx=-1
    max_value=-1
    secs = line.strip().split(" ")
    for i in range(len(secs)):
        if(eval(secs[i]) > max_value):
#           print "del "+str(min_idx)+": "+str(min_heap[min_idx])
            max_idx=i
            max_value=eval(secs[i])
    
    print str(max_idx)+"\t"+doc_buy[line_num]
    line_num=line_num+1

