import spacy
from spacy import displacy
nlp = spacy.load('pt_core_news_sm')
import json
from collections import Counter

def getEntity(url):
    with open('data/noticias'+url+'.json') as json_file:
        data = json.load(json_file)
        content = []
        for noticia in data:
            entidades = []
            
            id = noticia['id']
            title = noticia['title']
            texto = noticia['texto']

            entidadesTexto = nlp(texto)



            
            for entity in entidadesTexto.ents:
               
                #criando objeto entidade e o tipo
                entity = {
                   'entidade': entity.text,
                   'tipo': entity.label_
                }

                entidades.append(entity)
                
            #Item final

            item = {
                
                'entidades': entidades,
                'id': id,
                'title': title
            }
            content.append(item)


        with open('data/noticias'+url+'Entities.json', 'w') as json_file:
            json.dump(content, json_file, ensure_ascii=False)

        return content

          
                     

