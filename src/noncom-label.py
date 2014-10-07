#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys
import math


line_num = 0
for line in sys.stdin:
	line = line.strip()
	cols = line.split("\t")
	secs = cols[1].split(chr(1));

	if((line_num%8) == 7) and secs[1] != "":
		print secs[1]+"\t"+"0"
	line_num=line_num+1
