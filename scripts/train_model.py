import spacy
from spacy.training.example import Example
import random


TRAIN_DATA = [
              ("Publicado às 15h50", {"entities": [(13, 18, "DATA")]}),
              ("Às 8h16 tinha queda de", {"entities": [(3, 7, "DATA")]}),
              ("contrato com vencimento para 14 de agosto/20", {"entities": [(29, 44, "DATA")]}),
              ("Publicado às 12h13 A Alpargatas", {"entities": [(13, 18, "DATA"), (21, 31, "ORG")]}),
              ("31 de julho, o resultado do", {"entities": [(0, 11, "DATA")]}),
             ("10 de agosto, foi o dia de", {"entities": [(0, 12, "DATA")]}),
             ("às 8h15  Usiminas reporta lucro líquido", {"entities": [(3, 7, "DATA"), (9, 17, "ORG")]}),
             ("nesta sexta-feira, 30, os resultados do", {"entities": [(6, 17, "DATA")]}),
             ("receita líquida trimestral da Usiminas, com alta", {"entities": [(30, 38, "ORG")]}),
             ("lucro líquido de R$ 1,2 bilhões. A Usiminas (USIM2) divulgou nesta sexta-feira", {"entities": [(17, 31, "MONEY"), (35, 43, "ORG"), (67, 78, "DATA"), (45,50, "COD") ]}),
             ("a companhia registrou lucro líquido de R$ 7,1 bilhões, 277% superior", {"entities": [(39, 53, "MONEY")]}),
             ("representando o maior lucro líquido trimestral da Usiminas", {"entities": [(50, 58, "ORG")]}),
            ("os investimentos totais da Usiminas, que permanecem em R$111 milhões e R$9.100 milhões, respectivamente", {"entities": [(27, 35, "ORG"), (55, 68, "MONEY"), (71, 86, "MONEY")]}),
            ("A Ambipar Participações e Empreendimentos (AMBP1) informou", {"entities": [(2, 41, "ORG"), (43, 48, "COD")]}),
            ("A Méliuz (CASH7) informou", {"entities": [(2, 8, "ORG"),(10, 15, "COD")]}),
            ("A Alter, que possui um time de 24 pessoas", {"entities": [(2, 7, "ORG")]}),
            ("primeiro semestre de 2020 um volume de R$ 124 milhões em negociações", {"entities": [(21, 25, "DATA"),(39, 53, "MONEY")]}),
            ("A Alter é uma empresa", {"entities": [(2, 7, "ORG")]}),
            ("contrato com os sócios da Alter Pagamentos para comprar", {"entities": [(26, 31, "ORG")]})
]

if __name__ == "__main__":

    nlp = spacy.load('pt_core_news_sm')
    nlp.disable_pipes(['morphologizer', 'parser', 'attribute_ruler', 'lemmatizer', "tok2vec"])

    for iteration in range(70):

        random.shuffle(TRAIN_DATA)
        losses = {}

        for batch in spacy.util.minibatch(TRAIN_DATA, size=3):
            
            for text, annotations in batch:
                
                doc = nlp.make_doc(text)
                example = Example.from_dict(doc, annotations)

                # atualizando o modelo 
                nlp.update([example], losses=losses, drop=0.8)

    nlp.to_disk("model/")