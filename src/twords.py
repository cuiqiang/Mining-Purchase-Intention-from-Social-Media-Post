#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys
import math

args = []
for arg in sys.argv[1:]:
	args.append(arg)

model_file = args[0]
dic_file=args[1]

def argmin(**dic):
    min_idx = -1
    min_value = 1000

    for (k,v) in dic.items():
        if v < value:
            min_idx = k

    return min_idx

#word 
w_dic={}

for line in open(dic_file):
    cols = line.strip().split(" ")
    if len(cols) == 2: 
        w_dic[eval(cols[1])]=cols[0]

line_num = 0
ntopics = 0
ntwords = 20
for line in open(model_file):
    line_num = line_num+1
    if line_num == 2:
        cols = line.strip().split(": ")
        ntopics = eval(cols[1])

    if line_num > 5 and line_num < 6+ntopics:
        min_heap={}
        secs = line.strip().split(" ")
        for i in range(len(secs)):
            if len(min_heap) < ntwords:
#                print "add "+str(i)+": "+str(secs[i])
                min_heap[i] = eval(secs[i])
                continue
            else:
                min_idx = -1
                min_value = 1000
                for (k,v) in min_heap.items():
                    if v < min_value:
                        min_idx = k
                        min_value = v

#                min_idx = argmin(**min_heap)

                if(eval(secs[i]) > min_heap[min_idx]):
#                    print "del "+str(min_idx)+": "+str(min_heap[min_idx])
                    del min_heap[min_idx]
                    min_heap[i]=eval(secs[i])
        sorted_min_heap = sorted(min_heap.iteritems(),key=lambda d:d[1], reverse=True)
        print str(line_num-6)+" topic\n"
        for (k,v) in sorted_min_heap:
            if(k == 1571):
                    continue
            print w_dic[k]+" "+str(v)

