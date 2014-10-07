#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys
import math

args = []
for arg in sys.argv[1:]:
	args.append(arg)

file = args[0]
feat_file=args[1]
idx=eval(args[2])
dat = open(file+".nf","w")

#word 
word_dic={}

for line in open(feat_file):
	line = line.strip()
	cols = line.split("\t")
	word_dic[cols[0]]=idx
	idx+=1


for line in open(file):
	line = line.strip()
	cols = line.split("\t")
	secs = cols[1].split(" ")

	word_vec = {}
	for i in range(len(secs)):
		if word_vec.has_key(secs[i]):
			word_vec[secs[i]]+=1
		else:
			word_vec[secs[i]]=1

	word_fea = {}
	for word in word_dic:
		if word_vec.has_key(word):
			word_fea[word_dic[word]]=word_vec[word]
	if len(word_fea) == 0:
		continue

	word_fea_sort=sorted(word_fea.iteritems(),key=lambda d:d[0])
	for (k,v) in word_fea_sort:
		dat.write(str(k)+":"+str(v)+" ")
	dat.write("\n");

dat.close();
