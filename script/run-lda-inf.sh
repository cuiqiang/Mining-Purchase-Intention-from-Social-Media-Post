#!/bin/bash

project_home=$(readlink -f $(dirname $0))/..
modelpath=$project_home/models
ldapath=$project_home/GibbsLDA++-0.2/src/lda

niters=100
twords=20
model_dir=${modelpath}/lda-0.5-0.1-250-100
model_name=model-final
eval_data=eval-data

${ldapath} -inf -dir $model_dir -model $model_name -niters $niters -twords $twords -dfile $eval_data

