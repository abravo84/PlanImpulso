import nltk, random
from nltk import trigrams
from collections import defaultdict
import csv


def create_model(file_path, csv_flag = False):
    model = defaultdict(lambda: defaultdict(lambda: 0))
    if csv_flag:
        with open(file_path) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                sent_text = row[-2].decode('utf-8')
                sentence = nltk.word_tokenize(sent_text)
                for w1, w2, w3 in trigrams(sentence, pad_right=True, pad_left=True):
                    model[(w1, w2)][w3] += 1
                    
    else:
    
        for text in file(file_path):
        
            sentences = nltk.sent_tokenize(text.decode('utf-8'))
            for sent_text in sentences:
                sentence = nltk.word_tokenize(sent_text)
                for w1, w2, w3 in trigrams(sentence, pad_right=True, pad_left=True):
                    model[(w1, w2)][w3] += 1
    
    for w1_w2 in model:
        total_count = float(sum(model[w1_w2].values()))
        for w3 in model[w1_w2]:
            model[w1_w2][w3] /= total_count
                    
    return model               
if __name__ == '__main__':
    
    input_path = "/home/upf/corpora/umls_embeddings/orig/medlineplus_EN.txt"
    csv_flag = False
    model = create_model(input_path, csv_flag) 
    
    i=0
    while i < 50:
        text = [None, None]
     
        sentence_finished = False
         
        while not sentence_finished:
            r = random.random()
            accumulator = .0
         
            for word in model[tuple(text[-2:])].keys():
                accumulator += model[tuple(text[-2:])][word]
         
                if accumulator >= r:
                    text.append(word)
                    break
         
            if text[-2:] == [None, None]:
                sentence_finished = True
         
        print ' '.join([t for t in text if t])
        i+=1
        

