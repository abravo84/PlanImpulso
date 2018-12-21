#!/bin/bash


for folderpath in ../../corpora/MedlinePlus-TEI-Sp-En/TEI_ES/*_dataset; do
	for filepath in $folderpath/*; do
		name=$(basename "$filepath")
		abs_path=$(pwd)/$filepath
		echo $filepath

		if [[ ! -f "./med_res_es_2/$name" ]]
		then
			echo $name
			cat $filepath | java -jar ixa-pipe-tok-1.8.5-exec.jar tok -l es | java -jar ixa-pipe-pos-1.5.1-exec.jar tag -m morph-models-1.5.0/es/es-pos-perceptron-autodict01-ancora-2.0.bin -lm morph-models-1.5.0/es/es-lemma-perceptron-ancora-2.0.bin | java -jar ixa-pipe-nerc-1.6.1-exec.jar tag -m nerc-models-1.6.1/es/es-6-class-clusters-ancora.bin> ./med_res_es_2/$name
		fi
		


	done
done

cat ../../corpora/MedlinePlus-TEI-Sp-En/TEI_ES/health_topics_dataset/health_topics_dataset_abortion | java -jar ixa-pipe-tok-1.8.5-exec.jar tok -l es | java -jar ixa-pipe-pos-1.5.1-exec.jar tag -m morph-models-1.5.0/es/es-pos-perceptron-autodict01-ancora-2.0.bin -lm morph-models-1.5.0/es/es-lemma-perceptron-ancora-2.0.bin > res.xml





