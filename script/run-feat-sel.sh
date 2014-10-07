#!/bin/bash

project_home=$(readlink -f $(dirname $0))/..
datapath=$project_home/data
modelpath=$project_home/models
srcpath=$project_home/src



data_dir=${datapath}/raw-data
model_dir=${modelpath}/"cross-category-lr-20140105"

raw_data=$data_dir/raw-data-2.uniq

python ${srcpath}/feat-mutual-info.py $raw_data | sort -k1n -k3nr > $raw_data.mi

python ${srcpath}/feat-topk.py $raw_data.mi 20 > $raw_data.feat

python ${srcpath}/build-pair-feat.py $raw_data.mi 20 > $raw_data.pairfeat
