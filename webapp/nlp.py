import spacy
import json
from pathlib import Path

NER_dir = Path('./content/')
nlp = spacy.load(NER_dir)
#Cria dicionário
def createDict(noticia, url, nlp):
    return {
        "News" : noticia,
        "URL" : url,
        "Entidades" : nlp
    }

#Realiza o reconhecimento de entidades nas notícias       
def nlp_processing():
    all_dicts = []
    try:
        with open('data.json', 'r', encoding="utf8") as all_news:
            news = json.load(all_news)
            for noticia in news:
                palavras_processadas = []
                conteudo = noticia['conteudo']
                text = nlp(conteudo)
                for word in text.ents:
                    string_nlp = f"{word.text} - {word.label_}"
                    palavras_processadas.append(string_nlp)
                dict = createDict(noticia['title'], noticia['url'], palavras_processadas)
                all_dicts.append(dict)
        return all_dicts
    except FileNotFoundError as err:
        print(err)
        return False