'''
pip install -U pip setuptools wheel
pip install -U spacy[cuda102,transformers,lookups]
python -m spacy download pt_core_news_lg
'''


import pandas as pd
import spacy


df = pd.read_csv('news.csv', encoding = 'utf8')

nlp = spacy.load("pt_core_news_lg")

out={}
for i in df.index:
    #print(str(df["titulo"][i]) + ":" + str(df["descricao"][i]))
    doc = nlp(str(df["titulo"][i]) + ":" + str(df["descricao"][i]))
    for ent in doc.ents:
        #print(ent.text, ent.start_char, ent.end_char, ent.label_)
        out[ent.text] = ent.label_
print(out)
df_out = pd.DataFrame.from_dict(out, orient='index')
print(df_out)

