#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys
import math

args = []
for arg in sys.argv[1:]:
	args.append(arg)

file = args[0]
word_feat=args[1]
ngram_feat=args[2]
dat = open(file+".feat","w")

word_flag=0
ngram_flag=1
topic_flag=1

idx=1
#word 
word_dic={}
ngram_dic={}

if word_flag == 1:
	for line in open(word_feat):
		line = line.strip()
		word_dic[line]=idx
		idx+=1

if ngram_flag == 1:
	for line in open(ngram_feat):
		line = line.strip()
		ngram_dic[line]=idx
		idx+=1

for line in open(file):
	line = line.strip()
	cols = line.split("\t")

	dat.write(cols[0])
	dat.write("\t")

	#word feat
	if word_flag == 1:
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
		if len(word_fea) != 0:
			word_fea_sort=sorted(word_fea.iteritems(),key=lambda d:d[0])
			for (k,v) in word_fea_sort:
				dat.write(str(k)+":"+str(v)+" ")

	#ngram feat
	if ngram_flag == 1:
		secs = cols[3].split(" ")
		word_vec = {}
		for i in range(len(secs)):
			if word_vec.has_key(secs[i]):
				word_vec[secs[i]]+=1
			else:
				word_vec[secs[i]]=1

		word_fea = {}
		for word in ngram_dic:
			if word_vec.has_key(word):
				word_fea[ngram_dic[word]]=word_vec[word]
		if len(word_fea) != 0:
			word_fea_sort=sorted(word_fea.iteritems(),key=lambda d:d[0])
			for (k,v) in word_fea_sort:
				dat.write(str(k)+":"+str(v)+" ")

	#topic feat
	if topic_flag == 1:
		secs = cols[4].split(" ")
		for i in range(len(secs)):
			v = secs[i].split(":")
			dat.write(str(idx+eval(v[0])-1)+":"+str(v[1])+" ")

	dat.write("\n");
dat.close();
