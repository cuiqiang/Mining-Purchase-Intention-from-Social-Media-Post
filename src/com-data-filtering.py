#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys
import math

pre_post = "";
product_list = ""
for line in sys.stdin:
	cols = line.strip().split("\t")
	secs = cols[0].split(chr(1))

	if secs[1] == "":
		continue
		
	#if secs[2] == "女装/女士精品" \
	if secs[2] == "移动/联通/电信充值中心" \
	or secs[2] == "吃喝玩乐折扣券" \
	or secs[2] == "本地生活团购" \
	or secs[2] == "房产/租房/新房/二手房/委托服务" \
	or secs[2] == "装修设计" \
	or secs[2] == "休闲娱乐/购物卡" \
	or secs[2] == "新车/二手车" \
	or secs[2] == "网络设备/网络相关" or secs[2] == "网店/网络服务/软件" \
	or secs[2] == "外卖/外送/订餐服务" or secs[2] == "外卖/外送/订餐服务（垂直市场）" \
	or secs[2] == "手机号码/套餐/增值业务" \
	or secs[2] == "其他" \
	or secs[2] == "理财" or secs[2] == "基金" \
	or secs[2] == "电子凭证" \
	or secs[2] == "成人用品/避孕/计生用品" \
	or secs[2] == "自用闲置转让" \
	or secs[2] == "网络店铺代金/优惠劵" \
	or secs[2] == "腾讯QQ专区" \
	or secs[2] == "淘花娱乐" \
	or secs[2] == "台式机/一体机/服务器" \
	or secs[2] == "轻音后台一级类目" \
	or secs[2] == "交通票" \
	or secs[2] == "OTC药品/医疗器械/隐形眼镜/计生用品" \
	or secs[2] == "餐饮美食/面包券":
		continue
	
	if pre_post == "":
		pre_post = secs[1]
	if pre_post != secs[1]:
		print secs[0]+chr(1)+secs[1]+chr(1)+product_list+chr(1)+cols[1]
		pre_post = secs[1]
		product_list = ""
	product_list += secs[2]+":"+secs[3]+chr(2)
