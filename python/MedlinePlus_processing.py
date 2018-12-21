import os
import codecs


def create_text_dataset_medlineplus_by_files(medical_es_path, output_path):
    
    
    doc_id = output_path.split("/")[-1].replace("_dataset", "")
    for filename in os.listdir(medical_es_path):
        if not filename.endswith(".txt"):
            continue
        
        file_path = os.path.join(medical_es_path,filename)
        op = os.path.join(output_path, doc_id + "_" + filename.replace(".txt", "") )
        ofile = codecs.open(op + ".txt", "w", "utf-8")
        
        for lin in file(file_path):
            if lin == "\n":
                continue
            lin = lin.strip().decode('utf8')
            if lin.startswith("T Referenc"):
                break
            if lin.startswith("P ") or lin.startswith("P ") or lin.startswith("- ") or lin.startswith("t ") or lin.startswith("T "):
                lin = lin[2:]
            
            ofile.write(lin + "\n")
        
        ofile.write("\n")
        ofile.flush() 
        
        ofile.close()


if __name__ == '__main__':
    input_path = "/home/upf/corpora/MedlinePlus-TEI-Sp-En/TEI_EN/"
    ouput_path = "/home/upf/corpora/MedlinePlus-TEI-Sp-En/TEI_EN/"
    
    
    medical_es_path_list = []
    medical_es_path_list.append(input_path + "ency/article/")
    medical_es_path_list.append(input_path + "ency/patientinstructions/")
    medical_es_path_list.append(input_path + "health_topics/")
    medical_es_path_list.append(input_path + "labtests/")
    medical_es_path_list.append(input_path + "druginfo/meds/")
    medical_es_path_list.append(input_path + "druginfo/natural/")
    
    if not os.path.exists(ouput_path):
        os.makedirs(ouput_path)
    
    for medical_es_path in medical_es_path_list:
        
        opath = os.path.join(ouput_path,medical_es_path.replace(input_path, "").replace("/", "_") + "dataset")
        
        if not os.path.exists(opath):
            os.makedirs(opath)
        create_text_dataset_medlineplus_by_files(medical_es_path, opath)
