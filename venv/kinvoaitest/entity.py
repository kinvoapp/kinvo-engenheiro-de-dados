import spacy
import csv
import json
from spacy import displacy
from collections import Counter
import en_core_web_sm

#Utilizando arquivo de saida scrapy e car
file_path = (r'C:\Users\brito\OneDrive\Documentos\Data_Science\10 - GIT_Repositories\02 - Kinvo\venv\kinvoaitest\finewsraw.csv')
noticias = []
with open(file_path, newline='', encoding='utf-8') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        noticias.append(row["Acao"])
        noticias.append(row["Notícia"])
words = " ".join(noticias)
words = words.split(',')
print(words)
print("\b\b\b")
with open('processado.csv', 'w', encoding='UTF-8') as f:
    # create the csv writer
    writer = csv.writer(f)

    # write a row to the csv file
    writer.writerow(words)

nlp = en_core_web_sm.load()

lista =list()
with open(r'C:\Users\brito\OneDrive\Documentos\Data_Science\10 - GIT_Repositories\02 - Kinvo\venv\processado.csv',encoding='utf-8') as f:
    words = csv.reader(f)
    for row in f:
        lista.append(row)

lista_str = ','.join(lista)
doc = nlp(lista_str)
print([(X.text, X.label_) for X in doc.ents])