import os
import codecs
from collections import defaultdict

from tqdm import tqdm
import spacy
import pickle
from pathlib import Path
import sys


english_stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
sentence_id = 0


def get_list_of_files(dirName):
    # create a list of file and sub directories
    # names in the given directory
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(fullPath):
            allFiles = allFiles + get_list_of_files(fullPath)
        else:
            allFiles.append(fullPath)

    return allFiles


def get_article_text(path_to_json, nlp, noun_phrases_counter,output_folder):
    global sentence_id
    bla = path_to_json.split("extracted")
    path_to_output = output_folder+"corpus"+bla[1].replace("\\","_")
    output = codecs.open(path_to_output,"w","utf-8")

    for line in codecs.open(path_to_json,"r","utf-8"):
        tmp_json = eval(line)
        url = tmp_json['url']
        text = tmp_json['text']
        text = text.replace("\n"," ")
        text = text.replace('="',"")
        text = text.replace('">#REDIRECT', "")
        try:
            doc = nlp(text)
            for x in doc.sents:
                number_tokens_per_sentence = len(x)
                if number_tokens_per_sentence > 5:
                    sentence_id += 1
                    output.write(str(sentence_id)+"\t"+str(x)+"\n")
                    for phrase in [chunk.text for chunk in x.noun_chunks]:
                        if phrase.lower() not in english_stopwords:
                            noun_phrases_counter[phrase.lower()].add(sentence_id)

        except:
            print("error with article %s during spacy nlp service in file %s"%(url,path_to_json))
    output.close()


def get_processed_files():
    processed_files = []
    try:
        f_input = open("processed_files.txt", "r")
        for line in f_input:
            line = line.replace("\n", "")
            tmp = line.split("\t")
            processed_files.append(tmp)
        f_input.close()
    except:
        pass
    return processed_files


def save_processed_file_path(x):
    list_processed_files = get_processed_files()
    list_processed_files.append([x,sentence_id])
    f_output = open("processed_files.txt", "w")
    for p in list_processed_files:
        f_output.write(p[0]+"\t"+str(p[1])+"\n")
    f_output.close()


def main():
    nlp = spacy.load("en_core_web_sm")
    files = get_list_of_files("F:\wikipedia_en\extracted")
    noun_phrases_counter = defaultdict(set)
    highest_loaded_sentence_id = 0
    try:
        processed_files_with_max_doc_id = get_processed_files()
        processed_files = set()
        for x in processed_files_with_max_doc_id:
            local_sentence_id = int(x[1])
            if local_sentence_id>highest_loaded_sentence_id:
                highest_loaded_sentence_id = local_sentence_id
                print(highest_loaded_sentence_id)
            processed_files.add(x[0])
    except:
        print("Unexpected error:", sys.exc_info()[0])
        processed_files = set()
    global sentence_id
    sentence_id = highest_loaded_sentence_id
    print(processed_files)
    output_path = "extracted\\"

    for x in files[:3000]:
        if "wiki" in x and x not in processed_files:
            bla = x.split("extracted")
            bla = bla[1].split("\\")
            output_path_local = output_path+bla[1]+"\\"
            Path(output_path_local).mkdir(parents=True, exist_ok=True)
            get_article_text(x, nlp,noun_phrases_counter,output_path_local)
            save_processed_file_path(x)
            print("processed %s"%x)
            pickled_file = open('pickled_file.pickle', 'wb')
            pickle.dump(noun_phrases_counter, pickled_file)
            pickled_file.close()
            print("updated index \n")

    pickled_file = open('pickled_file.pickle', 'wb')
    pickle.dump(noun_phrases_counter, pickled_file)
    pickled_file.close()

if __name__ == '__main__':
    main()
