import spacy
import random
from spacy.training.example import Example
from pathlib import Path
model = "pt_core_news_md"
nlp = spacy.load(model)
print(f"Loaded model {model}")
#Caso o modelo por algum motivo não tiver "pipe" de NER
if 'ner' not in nlp.pipe_names:
    ner = nlp.create_pipe('ner')
    nlp.add_pipe(ner, last=True)
else:
  ner = nlp.get_pipe("ner")
#Para não afetar outros pipes
other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
#Definição das labels
LABEL = "AÇÃO"
LABEL_PESSOA = 'PER'
LABEL_ORG = 'ORG'
LABEL_LOCAL = 'LOC'
LABEL_PRECO = 'PREÇO'
LABEL_PERCENT = 'PORCENTAGEM'
ner.add_label(LABEL)
ner.add_label(LABEL_PRECO)
ner.add_label(LABEL_PERCENT)
optimizer = nlp.resume_training()

#Data usada para treinar o modelo
TRAIN_DATA = [
    (
        "O BTG tem recomendação de “compra” para a ação CYRE3 com preço-alvo de R$ 37",
        {"entities": [(47, 52, LABEL), (2, 5, LABEL_ORG), (71, 76, LABEL_PRECO)]}
    ),
    (
        "A Eztec (EZTC3) vai recomprar até 5.035.897 de ações ordinárias.",
        {"entities": [(9, 14, LABEL), (2, 7, LABEL_ORG)]}
    ),
    (
        "A Braskem (BRKM5) prestou esclarecimentos na noite desta sexta-feira",
        {"entities": [(11, 16, LABEL), (2, 9, LABEL_ORG)]}
    ),
    (
        "O Morgan Stanley reduziu participação na MRV (MRVE3).",
        {"entities": [(46, 51, LABEL), (2,16, LABEL_PESSOA), (41, 44, LABEL_ORG)]}
    ),
    (
        "O Itaú (ITUB4) informou na noite de sexta, 20, que a assembleia para deliberar incorporação da XPart pela XP será em 1 de outubro deste ano.",
        {"entities": [(8, 13, LABEL), (2,6, LABEL_ORG), (95, 100, LABEL_ORG)]}
    ),
    (
        "O BTG Pactual tem classificação de “compra” para a BR Malls (BRML3).",
        {"entities": [(61, 66, LABEL), (2, 5, LABEL_ORG), (51, 59, LABEL_ORG)]}
    ),
    (
        "Depois da forte queda da véspera, as ações Vale (VALE3) operavam no positivo neste começo de pregão",
        {"entities": [(49, 54, LABEL), (43, 47, LABEL_ORG)]}
    ),
    (
        "A Lojas Renner (LREN3) informou nesta sexta-feira, 20, que as equipes permanecem trabalhando para restabelecer o e-commerce em breve",
        {"entities": [(16, 21, LABEL), (2, 14, LABEL_ORG)]}
    ),
    (
        "As ações da Sabesp (SBSP3) dispararam nesta manhã e chegaram a entrar em leilão",
        {"entities": [(20, 25, LABEL), (12, 18, LABEL_ORG)]}
    ),
    (
        "A Eletrobras (ELET3, ELET6) informou na noite desta quinta-feira, 19, em complemento ao aviso aos acionistas do dia 11 de agosto de 2021",
        {"entities": [(14, 19, LABEL), (21, 26, LABEL), (2, 12, LABEL_ORG)]}
    ),
    (
        "A Alliar (AALR3) informou na noite desta quinta-feira, 19, que fundos de investimentos geridos pelo Pátria",
        {"entities": [(10, 15, LABEL), (2, 8, LABEL_ORG)]}
    ),
    (
        "A Oceanpact Serviços Marítimos (OPCT3) informou na noite desta sexta, 20, que engajou o Banco Itaú BBA",
        {"entities": [(32, 37, LABEL), (2, 30, LABEL_ORG), (94, 98, LABEL_ORG)]}
    ),
    (
        "A Bemobi (BMOB3) teve lucro líquido ajustado no valor de R$ 18 milhões no 2T21",
        {"entities": [(10, 15, LABEL), (2, 8, LABEL_ORG), (57, 70, LABEL_PRECO)]}
    ),
    (
        "Para os analistas da XP, os resultados da Yduqs (YDUQ3) no segundo trimestre vieram em linha com o esperado",
        {"entities": [(49, 54, LABEL), (21, 23, LABEL_ORG), (42, 47, LABEL_ORG)]}
    ),
    (
        "A Cemig (CMIG4) divulgou na noite desta segunda-feira, 16, o resultado do 2T21",
        {"entities": [(9, 14, LABEL), (2, 7, LABEL_ORG)]}
    ),
    (
        "A BRF (BRFS3) celebrou acordo para a constituição de uma joint venture com uma subsidiária da AES Brasil Energia (AESB3) para construção de um parque",
        {"entities": [(7, 12, LABEL), (114, 119, LABEL), (2, 5, LABEL_ORG), (94, 112, LABEL_ORG)]}
    ),
    (
        "A Yduqs Participações (YDUQ3), uma das maiores organizações privadas no setor de ensino superior no Brasil",
        {"entities": [(23, 28, LABEL), (100,106, LABEL_LOCAL), (2, 21, LABEL_ORG)]}
    ),
    (
        "A GP Investments (GPIV33), cujas ações classe A são negociadas na B3 por meio de Brazilian Depositary Receipts (BDRs), informou na noite desta terça",
        {"entities": [(18, 24, LABEL), (2, 16, LABEL_ORG)]}
    ),
    (
        "A JBS (JBSS3) informa na noite desta terça-feira, 17, que, em complemento ao aviso aos acionistas divulgado no último dia 11",
        {"entities": [(7, 12, LABEL), (2, 5, LABEL_ORG)]}
    ),
    (
        "O conselho de administração da JHSF (JHSF3) aprovou um novo programa de recompra de ações de sua própria emissão",
        {"entities": [(37, 42, LABEL), (31, 35, LABEL_ORG)]}
    ),
    (
        "A Irani Papel e Embalagem (RANI3) informou neste domingo, 15, a aprovação, por seu conselho de administração",
        {"entities": [(27, 32, LABEL), (2, 25, LABEL_ORG)]}
    ),
    (
        "O Itaú BBA cortou as recomendações das ações da CSN (CSNA3) e da Usiminas (USIM5) em uma revisão de seus modelos",
        {"entities": [(53, 58, LABEL), (75,80, LABEL), (2, 6, LABEL_ORG), (48, 51, LABEL_ORG), (65, 73, LABEL_ORG)]}
    ),
    (
        "As ações da Alliar (AALR3) saltavam +18% às 10h50 desta segunda-feira depois de a Rede D’Or (RDOR3) anunciar uma OPA",
        {"entities": [(20, 25, LABEL), (93,98, LABEL), (36, 40, LABEL_PERCENT), (12, 18, LABEL_ORG)]}
    ),
    (
        "Os papéis da Vale (VALE3), CSN (CSNA3) e da Usiminas (USIM5) tinham queda com dados abaixo do esperado na economia da China",
        {"entities": [(19, 24, LABEL), (32,37, LABEL), (54,59, LABEL), (13, 17, LABEL_ORG), (27, 30, LABEL_ORG), (44, 52, LABEL_ORG), (118, 123, LABEL_LOCAL)]}
    ),
    (
        "As ações da Minerva (BEEF3) devolviam parte dos ganhos obtidos no pregão da véspera",
        {"entities": [(21, 26, LABEL), (12, 19, LABEL_ORG)]}
    ),
    (
        "A Qualicorp (QUAL3) celebrou contrato para comprar 100% do capital social da Elo Administradora de Benefícios",
        {"entities": [(13, 18, LABEL), (2, 11, LABEL_ORG), (51, 55, LABEL_PERCENT), (77, 109, LABEL_ORG)]}
    ),
    (
        "O Magazine Luiza (MGLU3) divulgou na noite desta quinta, 12, o resultado do 2T21",
        {"entities": [(18, 23, LABEL), (2, 16, LABEL_ORG)]}
    ),
    (
        "A Unipar (UNIP3, UNIP5 e UNIP6) informou na noite desta quinta-feira, 12, que seu conselho de administração aprovou a distribuição e o pagamento de dividendos",
        {"entities": [(10, 15, LABEL), (17, 22, LABEL), (25,30, LABEL), (2, 8, LABEL_ORG)]}
    ),
    (
        "O conselho de administração da Energisa (ENGI11) aprovou o pagamento de dividendos no montante de R$ 235.292.554,25",
        {"entities": [(41, 47, LABEL), (31, 39, LABEL_ORG), (98, 115, LABEL_PRECO)]},
    ),
    (
        "A Energia (ENGI3) registrou lucro líquido consolidado de R$ 749,0 milhões no 2T21",
        {"entities": [(11, 16, LABEL), (2, 9, LABEL_ORG), (57, 73, LABEL_PRECO)]},
    ),
    (
        "A BRF (BRFS3) divulgou na noite desta quinta-feira, 12, seus resultados",
        {"entities": [(7, 12, LABEL), (2, 5, LABEL_ORG)]},
    ),
    (
        'A Minerva (BEEF3) voltou a afirmar que “não há intenção de promover o fechamento de capital”',
        {"entities": [(11, 16, LABEL), (2, 9, LABEL_ORG)]},
    ),
    (
        "A BR Malls (BRML3) teve prejuízo de R$ 112,9 milhões no 2T21",
        {"entities": [(11, 17, LABEL), (2, 10, LABEL_ORG), (36, 52, LABEL_PRECO)]},
    ),
    (
        "A Lojas Americanas (LAME4) contratou o BTG Pactual Corretora de Títulos e Valores Mobiliários para exercer a função de Formador de Mercado",
        {"entities": [(20, 25, LABEL), (2, 18, LABEL_ORG)]},
    ),
    (
        "A Cyrela Brazil Realty (CYRE3) divulgou na noite desta quinta-feira, 12, o resultado do segundo trimestre de 2021 (2T21)",
        {"entities": [(24, 29, LABEL), (2, 22, LABEL_ORG)]},
    ),
    (
        "Para o BTG, a Ser Educacional (SEER3) publicou resultados sem muita expressão no segundo trimestre",
        {"entities": [(31, 36, LABEL), (7, 10, LABEL_ORG), (14, 29, LABEL_ORG)]},
    ),
    (
        "A EDP – Energias do Brasil (ENBR3) apresentou pedido de incorporação ao mercado para listagem de suas ações ordinárias na Latibex",
        {"entities": [(28, 33, LABEL), (2, 26, LABEL_ORG), (122, 129, LABEL_ORG)]},
    ),
    (
        "A Santos Brasil (STBP3) celebrou com a União, por intermédio do Ministério da Infraestrutura contratos de arrendamento",
        {"entities": [(17, 22, LABEL), (2, 15, LABEL_ORG)]},
    ),
    (
        "O estado de Goiás, possui uma empresa eletríca estatal. A (Bahia), também possui uma empresa fornecedora de energia (COELBA)",
        {"entities": [(12, 17, LABEL_LOCAL), (59, 64, LABEL_LOCAL), (117, 123, LABEL_ORG)]},
    ),
    (
        "A Eztec (EZTC3) anunciou, na noite desta quarta-feira, 30 de junho, o lançamento do empreendimento EZ Infinity",
        {"entities": [(9, 14, LABEL), (2, 7, LABEL_ORG)]},
    ),
    (
        "A JBS (JBSS3) comunicou nesta quarta-feira, 30 de junho, que antecipou de 2030 para 2025 sua meta de desmatamento ilegal zero",
        {"entities": [(7, 12, LABEL), (2, 5, LABEL_ORG)]},
    ),
    (
        "A Petrobras (Petr4) informou que realizou nesta quarta-feira, 30, a liquidação antecipada do saldo devedor do Instrumento Particular de Parcelamento de Dívida",
        {"entities": [(13, 18, LABEL), (2, 11, LABEL_ORG)]},
    ),
    (
        "A agência de classificação de risco Moody’s avalia que a aquisição da Elizabeth Cimentos por R$ 1,08 bilhão é positiva para as perspectivas de crédito da CSN (CSNA3) já que ajuda a diversificar o fluxo de caixa sem afetar sua liquidez",
        {"entities": [(159, 164, LABEL), (36, 43, LABEL_ORG), (70, 88, LABEL_ORG), (93, 107, LABEL_PRECO), (154, 157, LABEL_ORG)]},
    ),
    (
        "A Hapvida (HAPV3) informou na noite desta quarta-feira, 30, que seu conselho de administração  aprovou o pagamento de juros sobre capital próprio (JCP)",
        {"entities": [(11, 16, LABEL), (2, 9, LABEL_ORG)]},
    ),
    (
        "A Usiminas (USIM5) informou na noite desta quarta-feira, 30, que, em razão da decisão tomada pelo Supremo Tribunal Federal em 13/05/21",
        {"entities": [(12, 17, LABEL), (2, 10, LABEL_ORG)]},
    ),
    (
        "A ação da BR Distribuidora (BRDT3) teve preço fixado em R$ 26 no ‘follow-on’. A operação marca a saída total da Petrobras da distribuidora com a venda dos 37,5%",
        {"entities": [(28, 33, LABEL), (10, 26, LABEL_ORG), (56, 61, LABEL_PRECO), (155, 160, LABEL_PERCENT)]},
    ),
    (
        "O conselho de administração do Magazine Luiza (MGLU3) aprovou a distribuição de juros sobre o capital próprio",
        {"entities": [(47, 52, LABEL), (31, 45, LABEL_ORG)]},
    ),
    (
        "A Telefônica Brasil (VIVT3) informou depois do pregão desta quarta-feira, 30, que os valores por ação referente aos Juros Sobre Capital Próprio",
        {"entities": [(21, 26, LABEL), (2, 19, LABEL_ORG)]},
    ),
    (
        "A Qualicorp (QUAL3) informou na noite desta quarta-feira, 30, que seu conselho de administração aprovou o pagamento de Juros sobre o Capital Próprio (JCP)",
        {"entities": [(13, 18, LABEL), (2, 11, LABEL_ORG)]},
    ),
    (
        "O banco Safra iniciou a cobertura da Totvs (TOTS3). A recomendação é “compra”. O preço-alvo é projetado em R$ 45 para 2021",
        {"entities": [(44, 49, LABEL), (8, 13, LABEL_ORG), (37, 42, LABEL_ORG), (107, 112, LABEL_PRECO)]},
    ),
    (
        "Com isso, os papéis da G2D Investments (G2DI33) saltavam 7,20% às 13h, cotados em R$ 7,15.",
        {"entities": [(40, 46, LABEL), (23, 38, LABEL_ORG), (57, 62, LABEL_PERCENT), (82, 89, LABEL_PRECO)]},
    ),
    (
        "Analistas do Itaú BBA atualizaram seus modelos para as companhias do setor de papel e celulose  Klabin (KLBN11) e Suzano (SUZB3)",
        {"entities": [(104, 110, LABEL), (122,127, LABEL), (13, 17, LABEL_ORG), (96, 102, LABEL_ORG), (114, 120, LABEL_ORG)]},
    ),
    (
        "A Tupy (TUPY3) celebrou com a Stellantis, sucessora da Fiat Chrysler Automobiles, e com a Teksid, subsidiária integral da Stellantis",
        {"entities": [(8, 13, LABEL), (2, 6, LABEL_ORG), (30, 40, LABEL_ORG), (55, 80, LABEL_ORG), (90, 96, LABEL_ORG), (122, 132, LABEL_ORG)]},
    ),
    (
        "A Rumo (RAIL3) divulgou um comunicado na noite desta quinta-feira, 1, para esclarecer as informações veiculadas na matéria divulgada hoje pelo Valor Econômico",
        {"entities": [(8, 13, LABEL), (2, 6, LABEL_ORG)]},
    ),
    (
        "A Yduqs Participações (YDUQ3; OTC: YDUQY) informou na noite desta quinta-feira, 1, que concluiu, nesta data",
        {"entities": [(23, 28, LABEL), (2, 21, LABEL_ORG)]},
    ),
    (
        "A Wilson Sons Limited (WSON33) informou que foi apresentado, nesta quinta-feira, 1, por sua subsidiária controlada, Wilson Sons Holdings Brasil",
        {"entities": [(23, 29, LABEL), (2, 21, LABEL_ORG)]},
    ),
    (
        "O conselho de administração do Grupo Fleury (FLRY3) aprovou a realização da sua 6ª emissão de debêntures simples",
        {"entities": [(45, 50, LABEL), (31, 43, LABEL_ORG)]},
    ),
    (
        "A Gol (GOLL4) recebeu correspondência de seu acionista Capital International Investors (CII)",
        {"entities": [(7, 12, LABEL), (2, 5, LABEL_ORG), (55, 86, LABEL_ORG)]},
    ),
    (
        "A Itaúsa (ITSA4) concluiu o investimento na Aegea. A informação foi divulgada após o fechamento do mercado nesta quinta-feira",
        {"entities": [(10, 15, LABEL), (2, 8, LABEL_ORG), (44, 49, LABEL_ORG)]},
    ),
    (
        "A construtora MRV (MRVE3) informou na noite desta quinta, 1, que vendeu por US$ 37 milhões, dois empreendimentos nos Estados Unidos",
        {"entities": [(19, 24, LABEL), (14, 17, LABEL_ORG), (76, 90, LABEL_PRECO), (117, 131, LABEL_LOCAL)]},
    ),
    (
        "A Petrobras (PETR4) informou que iniciou a etapa de divulgação da oportunidade (teaser)",
        {"entities": [(13, 18, LABEL), (2, 11, LABEL_ORG)]},
    ),
    (
        "A Vale (VALE3) informou na manhã desta sexta-feira, 2, que está comissionando suas atividades de carregamento no carregador de navios 6 (CN6)",
        {"entities": [(8, 13, LABEL), (2, 6, LABEL_ORG)]},
    ),
    (
        "O Banco BTG Pactual (BPAC11) vendeu a totalidade de sua participação na Credpago Serviços de Cobrança, correspondente a 49% do capital social",
        {"entities": [(21, 27, LABEL), (2, 19, LABEL_ORG), (72, 101, LABEL_ORG), (120, 123, LABEL_PERCENT)]},
    ),
    (
        "O mercado repercute nesta sexta-feira a informação revelada pela Simpar (SIMH3). A companhia informou nesta sexta-feira que a sua controlada JSL (JSLG3)",
        {"entities": [(73, 78, LABEL), (146,151, LABEL), (65, 71, LABEL_ORG), (141, 144, LABEL_ORG)]},
    ),
    (
        "A Engie Brasil (EGIE3) informou após o fechamento do pregão nesta quinta-feira, 1, que sua diretoria definiu a data de 12 de julho de 2021 para o pagamento dos dividendos",
        {"entities": [(16, 21, LABEL), (2, 14, LABEL_ORG)]},
    ),
    (
        "A Notre Dame Intermédica Participações (GNDI3) distribuirá aos seus acionistas, a título de dividendo mínimo obrigatório",
        {"entities": [(40, 45, LABEL), (2, 38, LABEL_ORG)]},
    ),
    (
        "O Banco BTG Pactual tem recomendação de “compra” para a Vamos (VAMO3), principal locadora de caminhões, máquinas e equipamentos do Brasil",
        {"entities": [(63, 68, LABEL), (2, 19, LABEL_ORG), (56, 61, LABEL_ORG), (131, 137, LABEL_LOCAL)]},
    ),
    (
        "A saída definitiva da Petrobras (PETR3, PETR4) da BR (BRDT3) deve impulsionar a valorização das ações da distribuidora",
        {"entities": [(33, 38, LABEL), (40,45, LABEL), (54,59, LABEL), (22, 31, LABEL_ORG)]},
    ),
    (
        "A Eztec (EZTC3) anunciou, na noite desta quarta-feira, 30 de junho, o lançamento do empreendimento EZ Infinity",
        {"entities": [(9, 14, LABEL), (2, 7, LABEL_ORG)]},
    ),
    (
        "China (Shanghai Comp.): +0,44% (pregão encerrado)Japão (Nikkei 225): -0,64% (pregão encerrado)Alemanha (DAX): +0,12% Londres (FTSE 100): +0,34% Petróleo Brent: +0,35% (US$ 76,46). O brent é referência para a Petrobras.Petróleo WTI: +0,37% (US$ 75,44).O contrato futuro mais líquido do minério de ferro negociado na bolsa de Dalian, na China, fechou em alta de 5,51% cotado em 1225 iuanes (US$ 189,6). A cotação em Dalian pode impactar os papéis da brasileira Vale (VALE3), CSN (CSNA3) e CSN Mineração (CMIN3)",
        {"entities": [(0,5, LABEL_LOCAL), (24, 30, LABEL_PERCENT), (69, 75, LABEL_PERCENT), (110,116, LABEL_PERCENT), (137, 143, LABEL_PERCENT), (160, 166, LABEL_PERCENT),
                      (168, 177, LABEL_PRECO), (232, 238, LABEL_PERCENT)]},
    ),
    (
        "O Banco BMG (BMGB4) divulgou depois do fechamento do mercado nesta sexta-feira, 2, que fez um acordo de investimentos para a aquisição de participação acionária",
        {"entities": [(13, 18, LABEL), (2, 11, LABEL_ORG)]},
    ),
    (
        "A Via, novo nome da Via Varejo (VVAR3), informou na noite desta sexta-feira, 2, que concluiu nesta data a formalização de todas as etapas legais",
        {"entities": [(32, 37, LABEL), (20, 30, LABEL_ORG)]},
    ),
    (
        "Em relatório divulgado na semana passada, o BTG Pactual reforçou a recomendação de “compra” para as units do Inter (BIDI11)",
        {"entities": [(116, 122, LABEL), (44, 55, LABEL_ORG), (109, 114, LABEL_ORG)]},
    ),
    (
        "A Vale (VALE3) informou nesta segunda-feira, 5, que iniciará a realização de atividades com equipamentos não tripulados (sem pessoas)",
        {"entities": [(8, 13, LABEL), (2, 6, LABEL_ORG)]},
    ),
    (
        "A JHSF Participações (JHSF3) concluiu a assinatura de um Term Sheet com a totalidade dos acionistas da Usina São Paulo SPE.",
        {"entities": [(22, 27, LABEL), (2, 6, LABEL_ORG), (103, 122 , LABEL_ORG)]},
    ),
    (
        "A Gol Linhas Aéreas (GOLL4), a maior companhia aérea doméstica do Brasil, divulgou após o fechamento do mercado os números prévios de tráfego do mês de junho de 2021.",
        {"entities": [(21, 26, LABEL), (2, 19, LABEL_ORG), (66, 72, LABEL_LOCAL)]},
    ),
    (
        "As ações ordinárias do BTG Pactual (BPAC3) subiam às 14h desta terça-feira, 6, +16,7% (R$ 24,36) e em julho acumulam alta de 33%.",
        {"entities": [(36, 41, LABEL), (23, 34, LABEL_ORG), (79, 85, LABEL_PERCENT), (87, 95, LABEL_PRECO), (125, 128, LABEL_PERCENT)]},
    ),
    (
        "A Petrobras (PETR4) informou que o encerramento da oferta pública de distribuição secundária de ações ordinárias de emissão da BR Distribuidora (BRDT3)",
        {"entities": [(13, 18, LABEL), (145,150, LABEL), (2, 11, LABEL_ORG), (127, 143, LABEL_ORG)]},
    ),
    (
        "A Petrobras (PETR4, PETR3) informou nesta segunda-feira, 5, que assinou hoje com a empresa Petromais Global Exploração e Produção S.A. (Petro+)",
        {"entities": [(13, 18, LABEL), (20, 25, LABEL), (2, 11, LABEL_ORG), (91, 134, LABEL_ORG)]},
    ),
    (
        "A BRF (BRFS3) informou nesta quarta-feira, 7, que participou na rodada de investimentos promovida pela Aleph Farms, no montante de US$ 2,5 milhões.",
        {"entities": [(7, 12, LABEL), (2, 5, LABEL_ORG), (103, 114, LABEL_ORG), (131, 146, LABEL_PRECO)]},
    ),
    (
        "O conselho de administração do IRB (IRBR3) aprovou a convocação da assembleia geral extraordinária (AGE) para o próximo dia 28 de julho.",
        {"entities": [(36, 41, LABEL), (31, 34, LABEL_ORG)]},
    ),
    (
        "A Minerva (BEEF3), líder em exportação de carne bovina na América do Sul, informou na noite desta terça-feira, 6, que a sua subsidiária Minerva Luxembourg",
        {"entities": [(11, 16, LABEL), (2, 9, LABEL_ORG), (136, 154, LABEL_ORG)]},
    ),
    (
        "A Petrobras (PETR4) informou na noite desta terça-feira, 6, que ajustará, a partir de 01/08/2021, os preços de venda de gás natural para as distribuidoras.",
        {"entities": [(13, 18, LABEL), (2, 11, LABEL_ORG)]},
    ),
    (
        "O Banco Bradesco (BBDC4) informou seu compromisso de descarbonizar suas carteiras de crédito e investimentos até 2050",
        {"entities": [(18, 23, LABEL), (2, 16, LABEL_ORG)]},
    ),
    (
        "O Safra iniciou a cobertura de Dasa (DASA3) com rating de “compra” e preço-alvo de R$ 78 por ação para 2021.",
        {"entities": [(37, 42, LABEL), (2, 7, LABEL_ORG), (31, 35, LABEL_ORG), (83, 88, LABEL_PRECO)]},
    ),
    (
        "A Hapvida (HAPV3) informou nesta quarta-feira, 7, que celebrou com a diretoria do Grupo HB Saúde uma proposta vinculante para a aquisição de até 100% do grupo",
        {"entities": [(11, 16, LABEL), (2, 9, LABEL_ORG), (145, 149, LABEL_PERCENT)]},
    ),
    (
        "O conselho de administração da Méliuz (CASH3), em reunião realizada nesta quarta-feira, 7,  aprovou a realização da oferta pública de distribuição primária e secundária",
        {"entities": [(39, 44, LABEL), (31, 37, LABEL_ORG)]},
    ),
    (
        "O Itaú Unibanco (ITUB4) lançou a plataforma de compensação de carbono para alavancar a transparência no Mercado de Carbono Voluntário",
        {"entities": [(17, 22, LABEL), (2, 15, LABEL_ORG)]},
    ),
    (
        "A Ecorodovias (ECOR3) informou nesta quarta-feira, 7, que a movimentação nas estradas que administra cresceu 30,6% em junho de 2021",
        {"entities": [(15, 20, LABEL), (2, 13, LABEL_ORG), (109, 114, LABEL_PERCENT)]},
    ),
    (
        "O Magazine Luiza (MGLU3) informou após o fechamento do mercado nesta quarta-feira, 7, que concluiu a aquisição da empresa Juni Marketing Digital",
        {"entities": [(18, 23, LABEL), (2, 16, LABEL_ORG), (122, 144, LABEL_ORG)]},
    ),
    (
        "O Magazine Luiza (MGLU3) confirmou que iniciou os investimentos para abrir 50 lojas no Rio de Janeiro este ano, sendo 23 delas no início de julho",
        {"entities": [(18,23, LABEL), (2, 16, LABEL_ORG), (87, 101, LABEL_ORG)]}
    ),
    (
        "A Telefônica Brasil (VIVT3) informou depois do pregão desta quarta-feira, 30, que os valores por ação referente aos Juros Sobre Capital Próprio",
        {"entities": [(21,26, LABEL), (2, 19, LABEL_ORG)]}
    ),
    (
        
        "A Qualicorp (QUAL3) informou na noite desta quarta-feira, 30, que seu conselho de administração aprovou o pagamento de Juros sobre o Capital Próprio (JCP)",
        {"entities": [(13,18, LABEL), (2, 11, LABEL_ORG)]}
    ),
    (
        "Às 10h35 o Ibovespa tinha queda de 1,38% aos 124.220 pontos. A sessão é marcada pela forte aversão ao risco nas Bolsas pelo mundo",
        {"entities": [(35,40, LABEL_PERCENT)]}
    ),
    (
        "Depois de ter sido autorizada pelo Banco Central a iniciar a operação da financeira digital BNQI, a Via, novo nome da Via Varejo (VVAR3)",
        {"entities": [(130,135, LABEL), (92, 96, LABEL_ORG), (100, 103, LABEL_ORG), (118, 128, LABEL_ORG)]}
    ),
    (
        "A Petrobras Distribuidora (BRDT3) está listada pelo segundo ano consecutivo no índice FTSE4Good",
        {"entities": [(2,25, LABEL_ORG), (27, 32, LABEL)]}
    ),
    (
        "A Cemig (CMIG4) informou na noite desta segunda-feira, 19, que foi iniciada a oferta de aquisição em dinheiro, por sua controlada Cemig GT",
        {"entities": [(2,7, LABEL_ORG), (9, 14, LABEL), (130, 138, LABEL_ORG)]}
    ),
    (
        "China (Shanghai Comp.): +1,11% (pregão encerrado), Japão (Nikkei 225): +0,59% (pregão encerrado), Hong Kong (Hang Seng): +0,47% (pregão encerrado), Alemanha (DAX): -0,09%",
        {"entities": [(0,5, LABEL_LOCAL), (24, 30, LABEL_PERCENT), (51, 56, LABEL_LOCAL), (71, 77, LABEL_PERCENT), (98, 107, LABEL_LOCAL), (121, 127, LABEL_PERCENT), (148, 156, LABEL_LOCAL), (164, 170, LABEL_PERCENT)]}
    ),
    (
        "A Cemig (CMIG4) informou na noite desta segunda-feira, 19, que foi iniciada a oferta de aquisição em dinheiro, por sua controlada Cemig GT",
        {"entities": [(2,7, LABEL_ORG), (9, 14, LABEL), (130, 138, LABEL_ORG)]}
    ),
    (
        "O conselho de administração elegeu  Jayme Pinto Junior para o cargo de Diretor de Comércio Exterior e Corporate Bank e Pedro Bramont para o cargo de Diretor de Negócios Digitais.",
        {"entities" : [(36, 54, LABEL_PESSOA), (119, 132, LABEL_PESSOA)]}
    ),
    (
        "A Cielo (B3: CIEL3 / OTC Nasdaq International: CIOXY) informou na noite desta quarta-feira, 19, que Paulo Rogério Caffarelli apresentou nesta data sua carta de renúncia",
        {"entities" : [(2, 7, LABEL_ORG), (13, 18, LABEL), (100, 124, LABEL_PESSOA)]}
    ),
    (
        "Após a afirmação do presidente Jair Bolsonaro de que o novo presidente da estatal está finalizando estudos",
        {"entities" : [(31, 45, LABEL_PESSOA)]}
    ),
    (
        "A Petrobras Distribuidora (BRDT3) está listada pelo segundo ano consecutivo no índice FTSE4Good. Seu dono, Cleison Silva, está otimista.",
        {"entities": [(2,25, LABEL_ORG), (27, 32, LABEL), (107, 120, LABEL_PESSOA)]}
    ),
    (
        "O Safra iniciou a cobertura de Dasa (DASA3) com rating de “compra” e preço-alvo de R$ 78 por ação para 2021. Empresa essa cujo dono é Edmond Safra",
        {"entities": [(37, 42, LABEL), (2, 7, LABEL_ORG), (31, 35, LABEL_ORG), (83, 88, LABEL_PRECO), (134, 146, LABEL_PESSOA)]}
    ),
    (
        "O presidente Jair Bolsonaro sancionou a Medida Provisória (MP) que viabiliza a privatização da Eletrobras",
        {"entities": [(13, 27, LABEL_PESSOA), (95, 105, LABEL_ORG)]}
    ),
    (
        "Guilherme Alexandre Rossi foi eleito para o cargo de Diretor Comercial Alto Varejo e Rodrigo Mulinari para o cargo de Diretor de Tecnologia.",
        {"entities": [(0, 25, LABEL_PESSOA), (85, 101, LABEL_PESSOA)]}
    ),
    (
        "Enquanto que Thaila Ayala escolheu Francisco para o primogênito, o casal Fabiula Nascimento e Emilio Dantas escolheram Roque e Raul para os gêmeos",
        {"entities": [(13, 25, LABEL_PESSOA), (35, 44, LABEL_PESSOA), (73, 91, LABEL_PESSOA), (94, 107, LABEL_PESSOA), (119, 124, LABEL_PESSOA), (127, 131, LABEL_PESSOA)]}
    ),
    (
        "O valor do JCP complementar referente ao 2º trimestre de 2021 atualizado pela taxa Selic até 23.08.2021 (data-base) é de R$ 0,34787265629.",
        {"entities": [(121, 137, LABEL_PRECO)]}
    )
]
#Inicio do treinamento, declaro quais pipes não serão utilizados, estabeleço um número de iterações, dou um "shuffle" a cada iteração.
with nlp.disable_pipes(*other_pipes):
    for itn in range(300):
        print(itn)
        random.shuffle(TRAIN_DATA)
        losses = {}
        for text, annotations in TRAIN_DATA:
            doc = nlp.make_doc(text)
            example = Example.from_dict(doc, annotations)
            nlp.update([example], drop=0.35, sgd=optimizer, losses=losses)
        print(losses)

#Salvo o modelo na posta content.
output_dir=Path('./content/')
if not output_dir.exists():
  output_dir.mkdir()
nlp.meta['nome'] = 'my_ner' 
nlp.to_disk(output_dir)
print("Saved model to", output_dir)
