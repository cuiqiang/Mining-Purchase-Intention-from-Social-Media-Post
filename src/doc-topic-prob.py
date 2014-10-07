#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys
import math

args = []
for arg in sys.argv[1:]:
	args.append(arg)

model_file = args[0]
doc_file=args[1]

#purchase 
doc_buy={}

idx=0
for line in open(doc_file):
    cols = line.strip().split("\t")
    doc_buy[idx]=cols[1]
    idx=idx+1

line_num = 0
for line in open(model_file):
    secs = line.strip().split(" ")
    for i in range(len(secs)):
        print str(i)+"\t"+doc_buy[line_num]+"\t"+secs[i]
    
    line_num=line_num+1

