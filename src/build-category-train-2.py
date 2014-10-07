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

	if cols[0] == cate_id:
		label="1"
	else:
		label="-1"

	if label != "":
		dat.write(label+" ")
	else:
		continue

	dat.write(cols[1])
	dat.write("\n");

dat.close();
