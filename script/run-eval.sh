#!/bin/bash

project_home=$(readlink -f $(dirname $0))/..
datapath=$project_home/data
modelpath=$project_home/models
srcpath=$project_home/src



data_dir=${datapath}/raw-data
model_dir=${modelpath}/cross-category-lr-20140218
#model_dir=${modelpath}/pair-cross-20140218
eval_data=${datapath}/raw-data/raw-data-2.uniq.baseline

eval_data=$model_dir/result.final

for topk in {3,5,10}
do
	echo "evaluation top "$topk":"
	python ${srcpath}/eval.py $eval_data $topk

done

