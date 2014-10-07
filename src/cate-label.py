#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys
import math


line_num=0
for line in sys.stdin:

	line_num+=1;

	line = line.strip()
	cols = line.split("\t")
	secs = cols[0].split(chr(1));

	dic = {}
	cateList = secs[2].split(chr(2))
	for cate in cateList:
		if cate != "":
			cate = cate.split(":")[0];
			dic[cate] = 1
		
	for cate in dic.keys():
		if secs[1] != "":
			if cate == "宠物/宠物食品及用品":
				print secs[1]+"\t"+"1"
			elif line_num%80 == 7:
				print secs[1]+"\t"+"0"
