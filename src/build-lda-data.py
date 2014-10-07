#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys
import math

args = []
for arg in sys.argv[1:]:
	args.append(arg)

file = args[0].split("/")[-1]
dat = open(file+"-lda.dat","w")


for line in open(file):
	line = line.strip()
	cols = line.split("\t")
	secs = cols[0].split(chr(1));

	if(secs[1] != ""):
		dat.write(secs[1]+"\n")

dat.close();
