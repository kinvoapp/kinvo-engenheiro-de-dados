import spacy
#import spacy.displacy as displacy

# loading do pacote pre treinado
nlp = spacy.load('pt_core_news_lg')

# lendo as noticias obtidas e alimentando a nlp com elas
index = open("\kinvo-ia-test\\b3StockNews\content.txt", "r")
doc = nlp(index.read())

# display das entidades extraidas
for ent in doc.ents:
    print(ent.text, ent.label_)

# display for the kicks

#displacy.serve(doc, style='ent')
#displacy.render(doc, style='dep', jupyter=True, options={'distance': 90})
# colors = {'per': 'linear-gradient(90deg, #aa9cde, #dc9ce7)',
#          'tim': 'radial-gradient(white,red)'}
#options = {'ents': ['per' 'tim'], 'colors': colors}
#displacy.render(doc, style='ent', options=options)
