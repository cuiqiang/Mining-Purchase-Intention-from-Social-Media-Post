#!/bin/bash

project_home=$(readlink -f $(dirname $0))/..
modelpath=$project_home/models
alpha=0.5
beta=0.1
ntopics=100
niters=100
twords=20

ldapath=$project_home/GibbsLDA++-0.2/src/lda

model_dir=${modelpath}/"lda-"$alpha"-"$beta"-"$ntopics"-"$niters
train_data=$model_dir/train_data.dat

${ldapath} -est -alpha $alpha -beta $beta -ntopics $ntopics -niters $niters -twords $twords -dfile $train_data

