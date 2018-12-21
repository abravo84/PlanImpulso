#!/bin/bash


MM_OPT="-y -@ 127.0.0.1 --conj -r 800 -k acty,amas,bhvr,bmod,clas,cnce,crbs,dora,evnt,ftcn,gngm,gora,grpa,hcro,idcn,inbe,inpr,lang,mcha,mosq,nusq,ocac,ocdi,orgt,pros,qlco,qnco,rnlw,shro,socb,spco,tmco"

MM_OPT="-y -@ 127.0.0.1 --conj -r 800 -R SNOMEDCT_US,MDR,MSH -k acty,amas,bhvr,bmod,clas,cnce,crbs,dora,evnt,ftcn,gngm,gora,grpa,hcro,idcn,inbe,inpr,lang,mcha,mosq,nusq,ocac,ocdi,orgt,pros,qlco,qnco,rnlw,shro,socb,spco,tmco"



INPUT_PATH="/mnt/vmdata/scipub/abravo/corpora/COPPA/EN/medical_patents_en_dataset"
OUTPUT_PATH="/mnt/vmdata/scipub/abravo/corpora/COPPA/EN/medical_patents_en_results"


INPUT_PATH="/mnt/vmdata/scipub/abravo/corpora/MedlinePlus-TEI-Sp-En/TEI_EN/documents"
OUTPUT_PATH="/mnt/vmdata/scipub/abravo/corpora/MedlinePlus-TEI-Sp-En/TEI_EN/mm_resuls"

INPUT_PATH="/mnt/vmdata/scipub/abravo/corpora/mantra"
OUTPUT_PATH="/mnt/vmdata/scipub/abravo/corpora/mantra_out"

java -jar mm.jar "$MM_OPT" $INPUT_PATH $OUTPUT_PATH

