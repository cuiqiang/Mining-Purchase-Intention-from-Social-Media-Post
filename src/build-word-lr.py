#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys
import math

args = []
for arg in sys.argv[1:]:
	args.append(arg)

file = args[0]
dat = open(file+".dat","w")

#word 
word_dic={}

for line in open(args[1]):
	line =  line.strip()
	cols = line.split("\t")
	word_dic[cols[0]]=eval(cols[2])


for line in open(file):
	line = line.strip()
	cols = line.split("\t")
	secs = cols[1].split(chr(1))[1].split(" ")

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

	label_secs = cols[2].split(" ")
	for i in range(len(label_secs)):
		if i > 0:
			v = label_secs[i].split("\"")
			dat.write(v[0]+"\""+v[2]+",")

	dat.write("\t")
	
	word_fea_sort=sorted(word_fea.iteritems(),key=lambda d:d[0])
	for (k,v) in word_fea_sort:
		dat.write(str(k)+":"+str(v)+" ")
	dat.write("\n");

dat.close();
