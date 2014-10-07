#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys
import math


line_num = 0
for line in sys.stdin:
	if(line_num%9) == 7:
		print line.strip()
	line_num=line_num+1
