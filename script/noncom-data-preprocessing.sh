#!/bin/bash

project_home=$(readlink -f $(dirname $0))/..
datapath=$project_home/data/
scriptpath=$project_home/script/
srcpath=$project_home/src/

noncom_weibo=${datapath}/raw-data/raw-noncom-data

cat $noncom_weibo | python $srcpath/noncom-label.py > $noncom_weibo.label 


#mv $purchase_history-sort-* ${datapath}/id_data
