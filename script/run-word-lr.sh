#!/bin/bash

project_home=$(readlink -f $(dirname $0))/..
datapath=$project_home/data
modelpath=$project_home/models
srcpath=$project_home/src



data_dir=${datapath}/raw-data
model_dir=${modelpath}/"lr-20140105"

lrpath=$project_home/liblinear-1.94/

if [ -d $model_dir ]
then
	rm -r $model_dir
fi	

mkdir -p $model_dir

cate_label=${datapath}/raw-data/raw-com-data-sort-filtering.cate
keyword_norm=${datapath}/raw-data/keyword.norm
train_data=$model_dir/train_data
cat $cate_label > $train_data

python ${srcpath}/build-word-lr.py $train_data $keyword_norm > $train_data.dat 

#${lrpath}/train -s 0 $train_data.dat


