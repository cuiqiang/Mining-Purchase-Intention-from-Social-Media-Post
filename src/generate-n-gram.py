#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys
import math

args = []
for arg in sys.argv[1:]:
	args.append(arg)

file = args[0]
n=2

for line in open(file):
	line = line.strip()
	cols = line.split("\t")

	word_vector=cols[1].split(" ")
	n_gram_vector=""
	for i in range(len(word_vector)):
		if i > n-2:
			n_gram_vector+=word_vector[i-1]+"_"+word_vector[i]+" "
	
	print cols[0]+"\t"+n_gram_vector
