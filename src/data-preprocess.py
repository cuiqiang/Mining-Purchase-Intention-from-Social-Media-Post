#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys
import math


for line in sys.stdin:
	line = line.strip()
	cols = line.split("\t")

	if cols[1] == "1":
		print cols[0]+"\t"+cols[2]
