import spacy

class EntityFinder(object):
    
    def __init__(self):
        
        self.nlp = spacy.load('pt_core_news_md')

    def get_entities(self, text):
        
        return self.nlp(text).ents