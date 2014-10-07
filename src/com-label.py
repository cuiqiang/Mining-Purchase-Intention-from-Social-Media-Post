#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys
import math


for line in sys.stdin:
	line = line.strip()
	cols = line.split("\t")
	secs = cols[0].split(chr(1));

	if(secs[1] != ""):
		print secs[1]+"\t"+"1"
