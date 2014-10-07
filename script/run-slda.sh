#!/bin/bash

project_home=$(readlink -f $(dirname $0))/..
datapath=$project_home/data
modelpath=$project_home/models
srcpath=$project_home/src
alpha=0.5
ntopics=250

data_dir=${datapath}/raw-data
model_dir=${modelpath}/"slda-"$alpha"-"$ntopics

sldapath=$project_home/slda/

#if [ -d $model_dir ]
#then
#	rm -r $model_dir
#else
#	mkdir -p $model_dir
#fi

#com_weibo=${datapath}/raw-data/raw-com-data-sort-filtering.label
#noncom_weibo=${datapath}/raw-data/raw-noncom-data.label
train_data=$model_dir/train_data
#cat $com_weibo $noncom_weibo > $train_data

#python ${srcpath}/build-slda-data.py $train_data 

${sldapath}/slda est $train_data"-doc" $train_data"-label" ${sldapath}/settings.txt $alpha $ntopics random $model_dir





#mv $purchase_history-sort-* ${datapath}/id_data
