#!/bin/bash

project_home=$(readlink -f $(dirname $0))/..
datapath=$project_home/data
modelpath=$project_home/models
srcpath=$project_home/src



data_dir=${datapath}/raw-data
model_dir=${modelpath}/"pair-lr-20140127"

lrpath=$project_home/liblinear-1.94/

if [ -d $model_dir ]
then
	rm -r $model_dir
fi	

mkdir -p $model_dir

category=$data_dir/train-20140127
python ${srcpath}/build-pair-lr.py $category $category.pairfeat $category.label

#cat $category.dat > $model_dir

cd $model_dir

${lrpath}/train -s 0 $category.pair.dat 


