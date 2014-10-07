#!/bin/bash

project_home=$(readlink -f $(dirname $0))/..
datapath=$project_home/data
modelpath=$project_home/models
srcpath=$project_home/src



data_dir=${datapath}/raw-data
model_dir=${modelpath}/"category-lr-20140105"

lrpath=$project_home/liblinear-1.94/

if [ -d $model_dir ]
then
	rm -r $model_dir
fi	

mkdir -p $model_dir

category=$data_dir/raw-train-data.dat
train_data=$model_dir/train_data
cat $category > $train_data

cd $model_dir

for cate_id in {1..46}
do
	python ${srcpath}/build-category-train.py $train_data $cate_id > $cate_id.dat
	${lrpath}/train -s 0 $cate_id.dat

done

