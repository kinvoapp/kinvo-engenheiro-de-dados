import pandas as pd
import spacy


class noticias():

    def __init__(self) -> None:

        self.news = pd.read_csv('../news/noticias_extraidas.csv')
        self.nlp = spacy.load("../model/")


    def main(self):

        dados = list()

        for posicao in range(self.news.shape[0]):
            content_news = self.news.iloc[posicao]
            news = self.puxa_noticia(content_news)
            
            self.link = self.puxa_link(content_news)
            self.titulo = self.puxa_titulo(content_news)
            self.entidades = self.puxa_entidades(news)

            dados.append(self.imprime_entidades())
        return {"noticias": dados}

    def imprime_entidades(self):

        return {"titulo":self.titulo,
                "link": self.link,
                "entidades": self.entidades}

    def puxa_noticia(self, content_news):
        return content_news['noticia']

    def puxa_link(self, content_news):
        return content_news['link']

    def puxa_titulo(self, content_news ):
        return content_news['titulo']

    def puxa_entidades(self, news):

        texto = self.nlp(news)
        enti = list()

        for entidade in texto.ents:
            enti.append({"trexo": entidade.text, "entidade": entidade.label_}) 
        
        return enti

