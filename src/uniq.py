#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys
import math

pre = "";
for line in sys.stdin:
	line = line.strip()
	if pre == "":
		pre = line
	if pre != line:
		print line
		pre = line
