#!/bin/bash

project_home=$(readlink -f $(dirname $0))/..
datapath=$project_home/data/
scriptpath=$project_home/script/
srcpath=$project_home/src/

com_weibo=${datapath}/raw-data/raw-com-data

#sort -k1 -t  $com_weibo > $com_weibo-sort

#cat $com_weibo-sort | python $srcpath/com-data-filtering.py > $com_weibo-sort-filtering 

cat $com_weibo-sort-filtering | python $srcpath/cate-label.py > $com_weibo-sort-filtering.cate
