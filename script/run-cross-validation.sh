#!/bin/bash

project_home=$(readlink -f $(dirname $0))/..
datapath=$project_home/data/
modelpath=$project_home/models/
srcpath=$project_home/src/

data_dir=${datapath}/raw-data
raw_data=${datapath}/raw-data/raw-data-2.uniq.raw.feat
prefix=part.

#python ${srcpath}/build-word-lr-2.py $raw_data $raw_data.feat

for i in {0..9}
do
	rm $data_dir/$prefix$i
	touch $data_dir/$prefix$i
done

for cat_id in {1..45}
do
	awk -F "\t" '{if($1 == '$cat_id')print $0}' $raw_data > $raw_data.$cat_id
	#split data set into 10 parts
	line_num=`wc -l $raw_data.$cat_id | awk '{print $1}'`
	split_num=`expr $line_num / 10 + 1`
	split -a 1 -d -l $split_num $raw_data.$cat_id $data_dir/tmp.

	for i in {0..9}
	do
		cat $data_dir/tmp.$i >> $data_dir/$prefix$i
		rm $data_dir/tmp.$i 
	done
done

#make model dir
model_dir=${modelpath}/"cross-category-lr-20140218"
lrpath=$project_home/liblinear-1.94/

if [ -d $model_dir ]
then
	rm -r $model_dir
fi	
mkdir -p $model_dir
cd $model_dir

touch result.final

#10 fold cross validation
for num in {0..9}
do
	fold_model=$model_dir/$num
	mkdir -p $fold_model
	cd $fold_model

	train_data=$fold_model/raw-train.$num
	test_data=$fold_model/raw-test.$num

	cp $data_dir/$prefix* ./ 

	mv $prefix$num $test_data
	cat $prefix* > $train_data

	rm $prefix*

	mkdir -p $fold_model/model
	cd $fold_model/model	

	awk -F "\t" '{print "1",$2}' $test_data > test.$num

	for cate_id in {1..45}
	do
		python ${srcpath}/build-category-train-2.py $train_data $cate_id > $cate_id.dat
		${lrpath}/train -s 0 $cate_id.dat
		${lrpath}/predict -b 1 test.$num $cate_id.dat.model $cate_id.dat.predict
		awk '{OFS="\"";if(NR > 1) print '$cate_id',$2}' $cate_id.dat.predict > $cate_id.score
	done

	paste -d, *.score > test.predict

	cd $fold_model
	paste -d "\t" $fold_model/model/test.predict $test_data > result.$num
	cat result.$num >> ../result.final
done
