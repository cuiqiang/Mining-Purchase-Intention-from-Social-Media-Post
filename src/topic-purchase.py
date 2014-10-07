#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys
import math

topic=""
text=""
key=-1

for line in sys.stdin:
	cols = line.strip().split("\t")
	secs = cols[1].split(chr(1));

	if key == -1:
		key = eval(cols[0])
	if key != eval(cols[0]):
		if len(topic) != 0 and len(text) != 0:
			print topic+chr(1)+text
		topic=""
		text=""
		key=eval(cols[0])

	if len(secs) == 1:
		topic = cols[1]
	else:
		text = cols[1]
	
