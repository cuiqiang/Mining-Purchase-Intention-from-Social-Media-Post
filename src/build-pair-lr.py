#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys
import math

args = []
for arg in sys.argv[1:]:
	args.append(arg)

file = args[0]
dat = open(file+".pair.dat","w")

#word 
feat_dic={}
for line in open(args[1]):
	line = line.strip()
	cols = line.split("\t")
	feat_dic[cols[0]]=eval(cols[1])

label_dic={}
for line in open(args[2]):
	line = line.strip()
	label_dic[line]=1

for line in open(file):
	line = line.strip()
	cols = line.split("\t")
	secs = cols[1].split(" ")

	word_fea = {}
	for i in range(len(secs)):
		v = secs[i].split(":")
		word_fea[feat_dic[cols[0]+"_"+v[0]]]=eval(v[1])

	if len(word_fea) == 0:
		continue

	label = "1"
	dat.write(label)

	dat.write("\t")
	
	word_fea_sort=sorted(word_fea.iteritems(),key=lambda d:d[0])
	for (k,v) in word_fea_sort:
		dat.write(str(k)+":"+str(v)+" ")
	dat.write("\n");

	for l in label_dic:
		if l!=cols[0]:
			word_fea = {}
			for i in range(len(secs)):
				v = secs[i].split(":")
				word_fea[feat_dic[l+"_"+v[0]]]=eval(v[1])

			if len(word_fea) == 0:
				continue

			label = "-1"
			dat.write(label)

			dat.write("\t")
	
			word_fea_sort=sorted(word_fea.iteritems(),key=lambda d:d[0])
			for (k,v) in word_fea_sort:
				dat.write(str(k)+":"+str(v)+" ")
			dat.write("\n");

dat.close();
