#!/bin/bash

project_home=$(readlink -f $(dirname $0))/..
datapath=$project_home/data
modelpath=$project_home/models
srcpath=$project_home/src



data_dir=${datapath}/raw-data
model_dir=${modelpath}/"baseline-20140220"

lrpath=$project_home/liblinear-1.94/

if [ -d $model_dir ]
then
	rm -r $model_dir
fi	

mkdir -p $model_dir

cd $model_dir

raw_data=$data_dir/raw-data-2.uniq
python ${srcpath}/baseline.py $raw_data
