#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys
import math

args = []
for arg in sys.argv[1:]:
	args.append(arg)

file = args[0]
cate_id = args[1]
dat = open(cate_id+".dat","w")

for line in open(file):
	line = line.strip()
	cols = line.split("\t")
	secs = cols[0].split(",")

	label = ""
	for i in range(len(secs)):
		v = secs[i].split("\"")
		if v[0] == cate_id:
			label=v[1]

	if label != "":
		dat.write(label+" ")
	else:
		continue

	dat.write(cols[1])
	dat.write("\n");

dat.close();
