#!/bin/bash

project_home=$(readlink -f $(dirname $0))/..
datapath=$project_home/data
modelpath=$project_home/models
srcpath=$project_home/src


data_dir=${datapath}/raw-data
model_dir=${modelpath}/lda-0.5-0.1-50-100
model_name=model-final

lrpath=$project_home/liblinear-1.94/
train_data=$model_dir/train_data

python ${srcpath}/build-topic-feat.py $model_dir/$model_name.tassign 50 > $model_dir/topic-lr-train 

#${lrpath}/train -s 0 $model_dir/topic-lr-train


