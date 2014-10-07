#!/bin/bash

project_home=$(readlink -f $(dirname $0))/..
datapath=$project_home/data
modelpath=$project_home/models
srcpath=$project_home/src
labels=2
fold=5
initial_C=16
l=1
k=250


data_dir=${datapath}/raw-data
model_dir=${modelpath}/"medlda-"$fold"-"$initial_C"-"$l"-"$k

medldapath=$project_home/medlda/

#if [ -d $model_dir ]
#then
#	rm -r $model_dir
#fi	

#mkdir -p $model_dir

#com_weibo=${datapath}/raw-data/raw-com-data-sort-filtering.label
#noncom_weibo=${datapath}/raw-data/raw-noncom-data.label
train_data=$model_dir/train_data
#cat $com_weibo $noncom_weibo > $train_data

#python ${srcpath}/build-medlda-data.py $train_data 

${medldapath}/MedLDA est $k $labels $fold $initial_C $l ${medldapath}/settings.txt $model_dir random


