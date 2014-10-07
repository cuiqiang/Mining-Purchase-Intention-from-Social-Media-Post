#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys
import math

args = []
for arg in sys.argv[1:]:
	args.append(arg)

file = args[0]
wd_f = open(file+".wd","w")
dat = open(file+".dat","w")

#word 
w_dic={}
w_idx=0

for line in open(file):
	line = line.strip()
	cols = line.split("\t")
	secs = cols[0].split(" ")


	w_idx_v = {}
	for i in range(len(secs)):
		if(w_dic.has_key(secs[i])):
			idx = w_dic[secs[i]];			
			if(w_idx_v.has_key(idx)):
				w_idx_v[idx]+=1
			else:
				w_idx_v[idx]=1
		else:
			w_dic[secs[i]]=w_idx
			w_idx_v[w_idx]=1
			w_idx=w_idx+1

	dat.write(str(len(w_idx_v))+"\t")
	dat.write(cols[1]+"\t")
	for (k,v) in w_idx_v.items():
		dat.write(str(k)+":"+str(v)+"\t")
	dat.write("\n");

dat.close();
			
for (k,v) in w_dic.items():
	wd_f.write(str(k)+" "+str(v)+"\n");
wd_f.close()
