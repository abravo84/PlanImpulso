import os, codecs
from bs4 import BeautifulSoup
import xml.etree.ElementTree


def add_one_dictionary(dictionary, key):
    if key in dictionary:
        aux = dictionary.get(key)
        dictionary[key] = aux + 1
    else:
        dictionary[key] = 1
    return dictionary 

def create_text_dataset(medical_es_path, output_path):
    
    
    ofile = codecs.open(output_path, "w", "utf-8")
    for lin in file(medical_es_path):
        fields = lin.strip().split("\t")
        
        medical_en_path = fields[-1]
        
        e = xml.etree.ElementTree.parse(medical_en_path).getroot()
        sentences = []
        
        body = e.find("text/body")
        
        title = body.find("head")
        title_text = title.text.strip()
        if title_text[-1] != '.':
            title_text+="."
        
        sentences.append(title_text.title())
        
        for abstract in body.findall("div"):
            for p in abstract.findall('p'):
                for s in p.findall('s'):
                    sentences.append(s.text.strip())
        
        ofile.write("\n".join(sentences) + "\n\n")
        
    ofile.close()
    
def split_dataset_by_files(ipath, ofolder):
    
    
    records = open(ipath).read().split("\n\n")

    for rec in records:
        lines = rec.split("\n")
        fname = lines[0].replace("#", "") + ".txt"
        ofile = open(os.path.join(ofolder, fname), "w")
        ofile.write("\n".join(lines[1:]))
        ofile.flush()
        ofile.close()
        
def create_text_dataset_by_files(medical_es_path, output_path, lng):
    
    
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    
    for lin in file(medical_es_path):
        fields = lin.strip().split("\t")
        
        medical_en_path = fields[-1]
        if lng == "en":
            medical_en_path = medical_en_path.replace("/es/", "/en/")
        e = xml.etree.ElementTree.parse(medical_en_path).getroot()
        sentences = []
        
        doc_id = e.get("id")
        
        #sentences.append(doc_id + ".")
        body = e.find("text/body")
        
        title = body.find("head")
        title_text = title.text.strip()
        if title_text[-1] != '.':
            title_text+="."
        
        sentences.append(title_text.title())
        
        for abstract in body.findall("div"):
            for p in abstract.findall('p'):
                for s in p.findall('s'):
                    sentences.append(s.text.strip())
        
        new_file = os.path.join(output_path, doc_id+".txt")
        ofile = codecs.open(new_file, "w", "utf-8")
        ofile.write("\n".join(sentences) + "\n\n")
        
        ofile.close()
        

def extract_medical_patents(es_docs_path, medical_patents_path):
    medical_docs = open(medical_patents_path, "w")
    
    documents = []
    cat_dict = {}
    for dir1 in os.listdir(es_docs_path):
        dir1_path = os.path.join(es_docs_path, dir1)
        for dir2 in os.listdir(dir1_path):
            dir2_path = os.path.join(dir1_path, dir2)
            for dir3 in os.listdir(dir2_path):
                dir3_path = os.path.join(dir2_path, dir3)
                for dir4 in os.listdir(dir3_path):
                    xml_path = os.path.join(dir3_path, dir4)
                    xml_text = open(xml_path).read()
                    soup_text = BeautifulSoup(xml_text,'lxml')
                    
                    tag = "note"
                    attr= {}
                    attr["type"] = "IC"
                    
                    category = soup_text.find(tag, attr)
                    
                    write_flag = False
                    
                    if category:
                        cat_text = str(category.text)
                        if "A61" in cat_text:
                            add_one_dictionary(cat_dict, "A61")
                            write_flag = True
                        if "C12N" in cat_text:
                            add_one_dictionary(cat_dict, "C12N")
                            write_flag = True
                        if "C12P" in cat_text:
                            add_one_dictionary(cat_dict, "C12P")
                            write_flag = True
                        
                        if write_flag:  
                            medical_docs.write(dir4 + "\t" + cat_text + "\t" + xml_path + "\n")
                            medical_docs.flush()
    medical_docs.close()

if __name__ == '__main__':
    
    es_docs_path = "/home/upf/Lote1/tei/Xml/en/"
    medical_patents_path = "/home/upf/medical_patents_en.txt"
    medical_patents_processed_path = "/home/upf/medical_patents_en_full_dataset.txt"
    
    extract_medical_patents(es_docs_path, medical_patents_path)
    create_text_dataset(medical_patents_path, medical_patents_processed_path) 
