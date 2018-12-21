#!/bin/bash


for folderpath in ../../corpora/MedlinePlus-TEI-Sp-En/TEI_EN/*_dataset; do
	for filepath in $folderpath/*; do
		name=$(basename "$filepath")
		abs_path=$(pwd)/$filepath
		echo $filepath

		if [[ ! -f "./med_res_en/$name" ]]
		then
			echo $name
			cat $filepath | java -jar ixa-pipe-tok-1.8.5-exec.jar tok -l en | java -jar ixa-pipe-pos-1.5.1-exec.jar tag -m morph-models-1.5.0/en/en-pos-perceptron-autodict01-conll09.bin -lm morph-models-1.5.0/en/en-lemma-perceptron-conll09.bin | java -jar ixa-pipe-chunk-1.1.1-exec.jar tag -m chunk-models-1.1.0/en-perceptron-conll00.bin > ./med_res_en/$name
		fi
		


	done
done

cat ../../corpora/MedlinePlus-TEI-Sp-En/TEI_EN/health_topics_dataset/health_topics_abortion.txt | java -jar ixa-pipe-tok-1.8.5-exec.jar tok -l en | java -jar ixa-pipe-pos-1.5.1-exec.jar tag -m morph-models-1.5.0/en/en-pos-perceptron-autodict01-conll09.bin -lm morph-models-1.5.0/en/en-lemma-perceptron-conll09.bin | java -jar ixa-pipe-chunk-1.1.1-exec.jar tag -m chunk-models-1.1.0/en-perceptron-conll00.bin > resen.xml




