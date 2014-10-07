#!/bin/bash

project_home=$(readlink -f $(dirname $0))/..
datapath=$project_home/data
modelpath=$project_home/models
srcpath=$project_home/src



data_dir=${datapath}/raw-data
raw_data=$data_dir/raw-data-2

#cat $raw_data | ${srcpath}/data-preprocess.py | ${srcpath}/uniq.py > $raw_data.uniq

#word feat
python ${srcpath}/word-mutual-info.py $raw_data.uniq 20 > $raw_data.uniq.wfeat

#n-gram feat
python ${srcpath}/generate-n-gram.py $raw_data.uniq > $raw_data.uniq.ng
python ${srcpath}/ngram-mutual-info.py $raw_data.uniq.ng 20 > $raw_data.uniq.nfeat

#topic feat
#model_dir=${modelpath}/lda-0.5-0.1-50-100
#model_name=model-final
#python ${srcpath}/build-topic-feat.py $model_dir/$model_name.tassign 50 > $raw_data.uniq.tfeat

#merge feats
paste -d'\t' $raw_data.uniq $raw_data.uniq.ng $raw_data.uniq.tfeat > $raw_data.uniq.raw

python ${srcpath}/build-feat.py $raw_data.uniq.raw $raw_data.uniq.wfeat $raw_data.uniq.nfeat
exit 0
paste -d'\t' $raw_data.uniq.label $raw_data.uniq.wf > tmp.paste
paste -d' ' tmp.paste $raw_data.uniq.ng.nf > $raw_data.uniq.dat
