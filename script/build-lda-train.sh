#!/bin/bash

project_home=$(readlink -f $(dirname $0))/..
datapath=$project_home/data/
scriptpath=$project_home/script/
srcpath=$project_home/src/
modelpath=$project_home/models
alpha=0.5
beta=0.1
ntopics=50
niters=100
twords=20
ldapath=$project_home/GibbsLDA++-0.2/src/lda

raw_data=${datapath}/raw-data/raw-data-2.uniq
model_dir=${modelpath}/"lda-"$alpha"-"$beta"-"$ntopics"-"$niters

if [ -d $model_dir ]
then
	rm -r $model_dir
fi	

mkdir -p $model_dir


train_data=$model_dir/train_data

cat $raw_data > $train_data

wc -l $train_data | awk '{print $1}' > $train_data.head

awk -F "\t" '{print $2}' $train_data > $train_data.nolabel

cat $train_data.head $train_data.nolabel > $train_data.dat

${ldapath} -est -alpha $alpha -beta $beta -ntopics $ntopics -niters $niters -twords $twords -dfile $train_data.dat

