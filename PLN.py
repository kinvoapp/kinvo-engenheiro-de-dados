# para rodar o programa:
# pip install spacy
# python -m spacy download en_core_web_sm

import spacy

pln = spacy.load('en_core_web_sm')
#processamento de documentos.
texto = ('Totvs vai pagar juros sobre o capital'
         'Irani lucra R$ 67,7 milhões no 2T21'
         'São Martinho vai pagar dividendos'
         'Alpargatas tem lucro de R$ 107,5 milhões no 2T21'
         'CSN reporta lucro de R$ 5,51 bi e vai pagar dividendo de R$ 1,26 por ação')

documento = pln(texto)
for entidade in documento.ents:
    print(entidade.text, entidade.label_)
