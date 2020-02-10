#!/usr/bin/env python
# coding: utf8
"""Example of training spaCy's named entity recognizer, starting off with an
existing model or a blank model.

For more details, see the documentation:
* Training: https://spacy.io/usage/training
* NER: https://spacy.io/usage/linguistic-features#named-entities

Compatible with: spaCy v2.0.0+
Last tested with: v2.1.0
"""
from __future__ import unicode_literals, print_function

import plac
import random
from pathlib import Path
import spacy
from spacy.util import minibatch, compounding


# training data
TRAIN_DATA = [
    ("Cotas do FII CAP REIT começam a ser negociadas na B3",{'entities':[(9,20,"PRODUCT"),(22,28,"EVENT"),(36,45,"EVENT"),(50,51,"PER")]}),
    ("Ibovespa registra novo recorde e marca 117.203 pontos",{'entities':[(0,7,"ORG"),(9,16,"EVENT"),(23,29,"EVENT"),(39,45,"MONEY")]}),
    ("Cotas do FII HEDGELOG começam a ser negociadas na B3",{'entities':[(9,20,"PRODUCT"),(22,28,"EVENT"),(36,45,"EVENT"),(50,51,"PER")]}),
    ("Cotas do FII HEDGE RE começam a ser negociadas na B3",{'entities':[(9,20,"PRODUCT"),(22,28,"EVENT"),(36,45,"EVENT"),(50,51,"PER")]}),
    ("Cotas do FII LGCP INT começam a ser negociadas na B3",{'entities':[(9,20,"PRODUCT"),(22,28,"EVENT"),(36,45,"EVENT"),(50,51,"PER")]}),
    ("Ibovespa registra novo recorde e marca 115.131 pontos",{'entities':[(0,7,"ORG"),(9,16,"EVENT"),(23,29,"EVENT"),(39,45,"MONEY")]}),
    ("Linhas de transmissão e subestações leiloadas pela Aneel atrairão investimentos de mais de R$ 4 bi",{'entities':[(36,44,"EVENT"),(51,55,"ORG"),(91,97,"MONEY")]}),
    ("B3 registra recorde de volume financeiro em dia de exercício de opções sobre o Ibovespa",{'entities':[(0,1,"PER"),(3,10,"EVENT"),(79,86,"ORG")]}),
    ("Natura &Co conclui processo de incorporação de ações da Natura Cosméticos e inicia negociação na B3",{'entities':[(0,9,"PER"),(11,17,"EVENT"),(56,72,"PER"),(97,98,"PER")]}),
    ("Ibovespa registra novo recorde e marca 112.615 pontos",{'entities':[(0,7,"ORG"),(9,16,"EVENT"),(23,29,"EVENT"),(39,45,"MONEY")]}),
    ("Cotas do FII RB TFO começam a ser negociadas na B3",{'entities':[(9,18,"PRODUCT"),(20,26,"EVENT"),(34,43,"EVENT"),(48,49,"PER")]}),
    ("Cotas do FII XP CRED começam a ser negociadas na B3",{'entities':[(9,19,"PRODUCT"),(21,27,"EVENT"),(35,44,"EVENT"),(49,50,"PER")]}),
    ("Exercício de opções sobre ações movimenta mais de R$ 12,12 bilhões na B3",{'entities':[(50,65,"MONEY"),(70,71,"PER")]}),
    ("LIG ultrapassa R$ 10 bi de estoque na B3 no primeiro ano",{'entities':[(0,2,"PRODUCT"),(4,13,"EVENT"),(15,22,"MONEY"),(38,39,"PER")]}),
    ("B3 divulga a segunda prévia do Ibovespa e demais índices",{'entities':[(0,1,"PER"),(3,9,"EVENT"),(31,38,"ORG")]}),
    ("Consórcio de empresas da China e Luxemburgo vence leilão da ponte Salvador-Itaparica na B3",{'entities':[(44,48,"EVENT"),(88,89,"PER")]}),
    ("Estudo avalia impacto de classe diferenciada de ações na governança de empresas",{'entities':[(7,12,"EVENT")]}),
    ("B3 é reconhecida como uma das melhores empresas para se trabalhar pelo Glassdoor em 2020",{'entities':[(0,1,"PER"),(5,15,"EVENT"),(71,79,"ORG")]}),
    ("B3 recebe dois ETFs de renda fixa desenvolvidos pela Bradesco Asset Management",{'entities':[(0,1,"PER"),(3,8,"EVENT"),(15,18,"PRODUCT")]}),
    ("B3 é eleita a bolsa de valores do ano pelo  Global Investor Group, com sede em Londres",{'entities':[(0,1,"PER"),(5,10,"EVENT"),(44,64,"ORG")]}),
    ("Cotas do BRAD IMA-B5M começam a ser negociadas na B3",{'entities':[(9,20,"PRODUCT"),(22,28,"EVENT"),(36,45,"EVENT"),(50,51,"PER")]}),
    ("Cotas do BRAD IMA-B começam a ser negociadas na B3",{'entities':[(9,18,"PRODUCT"),(20,26,"EVENT"),(34,43,"EVENT"),(48,49,"PER")]}),
]


@plac.annotations(
    model=("Model name. Defaults to blank 'en' model.", "option", "m", str),
    output_dir=("Optional output directory", "option", "o", Path),
    n_iter=("Number of training iterations", "option", "n", int),
)
def main(model=None, output_dir=None, n_iter=100):
    """Load the model, set up the pipeline and train the entity recognizer."""
    if model is not None:
        nlp = spacy.load(model)  # load existing spaCy model
        print("Loaded model '%s'" % model)
    else:
        nlp = spacy.blank("pt")  # create blank Language class
        print("Created blank 'en' model")

    # create the built-in pipeline components and add them to the pipeline
    # nlp.create_pipe works for built-ins that are registered with spaCy
    if "ner" not in nlp.pipe_names:
        ner = nlp.create_pipe("ner")
        nlp.add_pipe(ner, last=True)
    # otherwise, get it so we can add labels
    else:
        ner = nlp.get_pipe("ner")

    # add labels
    for _, annotations in TRAIN_DATA:
        for ent in annotations.get("entities"):
            ner.add_label(ent[2])

    # get names of other pipes to disable them during training
    pipe_exceptions = ["ner", "trf_wordpiecer", "trf_tok2vec"]
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe not in pipe_exceptions]
    with nlp.disable_pipes(*other_pipes):  # only train NER
        # reset and initialize the weights randomly – but only if we're
        # training a new model
        if model is None:
            nlp.begin_training()
        for itn in range(n_iter):
            random.shuffle(TRAIN_DATA)
            losses = {}
            # batch up the examples using spaCy's minibatch
            batches = minibatch(TRAIN_DATA, size=compounding(4.0, 32.0, 1.001))
            for batch in batches:
                texts, annotations = zip(*batch)
                nlp.update(
                    texts,  # batch of texts
                    annotations,  # batch of annotations
                    drop=0.5,  # dropout - make it harder to memorise data
                    losses=losses,
                )
            print("Losses", losses)

    # test the trained model
    for text, _ in TRAIN_DATA:
        doc = nlp(text)
        print("Entities", [(ent.text, ent.label_) for ent in doc.ents])
        print("Tokens", [(t.text, t.ent_type_, t.ent_iob) for t in doc])

    # save model to output directory
    if output_dir is not None:
        output_dir = Path(output_dir)
        if not output_dir.exists():
            output_dir.mkdir()
        nlp.to_disk(output_dir)
        print("Saved model to", output_dir)

        # test the saved model
        print("Loading from", output_dir)
        nlp2 = spacy.load(output_dir)
        for text, _ in TRAIN_DATA:
            doc = nlp2(text)
            print("Entities", [(ent.text, ent.label_) for ent in doc.ents])
            print("Tokens", [(t.text, t.ent_type_, t.ent_iob) for t in doc])


if __name__ == "__main__":
    plac.call(main)

    # Expected output:
    # Entities [('Shaka Khan', 'PERSON')]
    # Tokens [('Who', '', 2), ('is', '', 2), ('Shaka', 'PERSON', 3),
    # ('Khan', 'PERSON', 1), ('?', '', 2)]
    # Entities [('London', 'LOC'), ('Berlin', 'LOC')]
    # Tokens [('I', '', 2), ('like', '', 2), ('London', 'LOC', 3),
    # ('and', '', 2), ('Berlin', 'LOC', 3), ('.', '', 2)]
