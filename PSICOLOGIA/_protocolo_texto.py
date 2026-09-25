"""Elementos pre-textuais e seccoes 1 a 6 do protocolo (introducao a revisao da literatura)."""
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Cm, Pt

from _protocolo_amostra import DEFF_SENSIBILIDADE, POPULACOES, amostra_para

TITULO_ESTUDO = ("FACTORES PSICOSSOCIAIS RELACIONADOS AO COMPORTAMENTO AGRESSIVO EM "
                 "ADOLESCENTES DOS 10 AOS 19 ANOS: CASO DA ESCOLA SECUNDÁRIA DE MUATALA, "
                 "CIDADE DE NAMPULA, SEGUNDO SEMESTRE DE 2026")

# Identificacao da estudante e do orientador (dados fornecidos em 23/09/2026).
ESTUDANTE = "Eunice Carlos Marcelino"
BI_ESTUDANTE = "030105324374B"
NUMERO_ESTUDANTE = "20220108005"
ORIENTADOR = "Armando Salvador Cumbe"
ORIENTADOR_COM_GRAU = f"Mestre {ORIENTADOR}"

TITULO_CORRENTE = ("Factores psicossociais relacionados ao comportamento agressivo em adolescentes "
                   "dos 10 aos 19 anos: caso da Escola Secundária de Muatala, cidade de Nampula, "
                   "segundo semestre de 2026")

ABREVIATURAS = [
    "ACE-IQ = Adverse Childhood Experiences International Questionnaire;",
    "aOR = odds ratio ajustado (adjusted odds ratio);",
    "APGAR = escala de funcionamento familiar de Smilkstein;",
    "BPAQ = Buss-Perry Aggression Questionnaire;",
    "BPAQ-SF = Buss-Perry Aggression Questionnaire, forma reduzida;",
    "CIBS = Comité Institucional de Bioética para a Saúde;",
    "CNBS = Comité Nacional de Bioética para a Saúde;",
    "CRIES-8 = Children's Revised Impact of Event Scale, versão de oito itens;",
    "deff = efeito de desenho (design effect);",
    "DERS-SF = Difficulties in Emotion Regulation Scale, forma reduzida;",
    "FCS = Faculdade de Ciências de Saúde;",
    "GSHS = Global School-based Student Health Survey;",
    "IC = intervalo de confiança;",
    "INSPIRE = pacote de sete estratégias da Organização Mundial da Saúde para pôr fim à "
    "violência contra as crianças;",
    "MEC = Ministério da Educação e Cultura;",
    "MISAU = Ministério da Saúde;",
    "MZN = metical moçambicano;",
    "OMS = Organização Mundial da Saúde;",
    "OR = odds ratio;",
    "RPQ = Reactive-Proactive Aggression Questionnaire;",
    "SAAJ = Serviços Amigos dos Adolescentes e Jovens;",
    "SDQ = Strengths and Difficulties Questionnaire;",
    "SPSS = Statistical Package for the Social Sciences;",
    "STROBE = Strengthening the Reporting of Observational Studies in Epidemiology;",
    "TCLE = termo de consentimento livre e esclarecido;",
    "UniLúrio = Universidade Lúrio;",
    "VACS = Violence Against Children and Youth Survey.",
]

ESTADO_DA_ARTE = [
    ["Amu et al., 2020 [[amu2020]]", "Moçambique",
     "Transversal, inquérito global de saúde escolar de 2015, 1.918 adolescentes escolarizados",
     "Sofrimento psicossocial em 21,2%; associado a lutas físicas (aOR 1,38), a agressão física "
     "sofrida (aOR 1,80) e a bullying (aOR 1,45); ter amigos próximos foi protector (aOR 0,50)"],
    ["King et al., 2026 [[king2026]]", "Moçambique (cidade de Maputo)",
     "Transversal com entrevista diagnóstica, 488 estudantes de 12 a 19 anos",
     "Perturbação mental em 23,0%, sobretudo ansiedade (17,8%) e depressão (8,6%); só 2,7% dos "
     "afectados procuraram cuidados"],
    ["Instituto Nacional de Saúde et al., 2022 [[vacs2019]]", "Moçambique",
     "Inquérito nacional VACS de 2019, 13 a 24 anos",
     "Violência física antes dos 18 anos em 23,9% das raparigas e 34,1% dos rapazes; 27,5% e "
     "38,2% testemunharam violência física em casa"],
    ["Miedema et al., 2026 [[miedema2026]]", "8 países, incluindo Moçambique",
     "Inquéritos VACS, homens de 18 a 24 anos",
     "Violência sofrida ou testemunhada na infância associada a mais perpetração de violência; "
     "em Moçambique, perpetração de 21,0%"],
    ["Aboagye et al., 2021 [[aboagye2021a]]", "8 países da África subsariana",
     "Transversal, 14.967 adolescentes de 10 a 19 anos",
     "Violência interpessoal 53,7%; associada a bullying (aOR 2,52), consumo de álcool (aOR 1,49) "
     "e absentismo (aOR 1,51)"],
    ["Han et al., 2019 [[han2019]]", "68 países de baixo e médio rendimento",
     "Transversal, 164.633 adolescentes de 12 a 15 anos",
     "Lutas físicas 36,4% (45,5% nos rapazes e 26,9% nas raparigas); agressão física sofrida "
     "35,6%; bullying 34,4%, sem diferença entre sexos"],
    ["Hecker et al., 2014 [[hecker2014]]", "Tanzânia", "Transversal, 409 alunos do ensino primário",
     "Castigo físico quase universal em casa e na escola; o castigo pelos pais associou-se a mais "
     "problemas externalizantes"],
    ["Ugwu et al., 2024 [[ugwu2024]]", "África do Sul",
     "Transversal, 769 alunos do ensino secundário",
     "Adversidade na infância associada à perpetração de bullying, com mediação pela influência "
     "dos pares e moderação por traços de personalidade"],
    ["Brown et al., 2024 [[brown2024]]", "5 países subsarianos, incluindo Moçambique",
     "Inquéritos VACS, 11.498 jovens de 18 a 24 anos",
     "Relação gradual entre experiências adversas acumuladas e sofrimento mental, consumo de "
     "substâncias e perpetração de violência"],
    ["Blum et al., 2019 [[blum2019]]", "14 países de vários continentes",
     "Transversal, 1.284 adolescentes de 10 a 14 anos",
     "Experiências adversas na infância associadas a sintomas depressivos e à perpetração de "
     "violência"],
    ["Dodge et al., 2015 [[dodge2015]]", "9 países, 12 grupos culturais, incluindo o Quénia",
     "Longitudinal, 1.299 crianças seguidas durante 4 anos",
     "A atribuição de intenção hostil predisse a agressão reactiva em todos os grupos e a "
     "agressividade crónica, controlando a agressão anterior"],
    ["McLaughlin et al., 2011 [[mclaughlin2011]]", "Estados Unidos",
     "Prospectivo, 1.065 adolescentes avaliados com sete meses de intervalo",
     "A desregulação emocional predisse o aumento do comportamento agressivo; a agressividade "
     "não predisse o aumento da desregulação"],
    ["Heleniak et al., 2016 [[heleniak2016]]", "Estados Unidos",
     "Dois estudos, 167 e 439 adolescentes, o segundo com seguimento de 5 anos",
     "Os maus-tratos associaram-se a reactividade emocional, ruminação e impulsividade, que "
     "intermediaram a relação com a psicopatologia externalizante"],
    ["Verhoef et al., 2019 [[verhoef2019]]", "Meta-análise internacional",
     "111 estudos, 29.272 participantes",
     "Atribuição de intenção hostil associada à agressão, mais fortemente nas situações de maior "
     "envolvimento emocional"],
    ["Fowler et al., 2009 [[fowler2009]]", "Meta-análise internacional", "114 estudos",
     "Exposição à violência comunitária com efeitos mais fortes no stress pós-traumático e nos "
     "problemas externalizantes, sobretudo nos adolescentes"],
    ["Donnellan et al., 2005 [[donnellan2005]]", "Estados Unidos e Nova Zelândia",
     "Três estudos transversais e longitudinais, adolescentes e universitários",
     "Baixa auto-estima associada à agressão e à delinquência, independentemente do narcisismo"],
    ["Gershoff e Grogan-Kaylor, 2016 [[gershoff2016]]", "Meta-análise internacional",
     "75 estudos, mais de 160 mil crianças",
     "Castigo físico associado a maior agressividade e a mais problemas de comportamento, sem "
     "qualquer benefício documentado"],
    ["Murray et al., 2015 [[murray2015]]", "Zâmbia",
     "Ensaio clínico aleatorizado, 257 crianças e adolescentes",
     "Terapia cognitivo-comportamental focada no trauma, por conselheiros leigos, reduziu os "
     "sintomas traumáticos em 81,9%, contra 21,1% no tratamento habitual"],
]


def _capa(h, doc):
    for texto, tamanho, negrito in (
            ("UNIVERSIDADE LÚRIO", Pt(14), True),
            ("FACULDADE DE CIÊNCIAS DE SAÚDE", Pt(13), True),
            ("CURSO DE PSICOLOGIA", Pt(13), True)):
        h.paragrafo(doc, texto, WD_ALIGN_PARAGRAPH.CENTER, negrito, tamanho=tamanho,
                    espaco=1.5, depois=Pt(2))
    h.paragrafo(doc, "", WD_ALIGN_PARAGRAPH.CENTER, depois=Pt(48))
    h.paragrafo(doc, "Protocolo de Investigação", WD_ALIGN_PARAGRAPH.CENTER,
                tamanho=Pt(13), depois=Pt(24))
    h.paragrafo(doc, TITULO_ESTUDO, WD_ALIGN_PARAGRAPH.CENTER, negrito=True,
                tamanho=Pt(14), depois=Pt(60))
    h.paragrafo(doc, ESTUDANTE, WD_ALIGN_PARAGRAPH.CENTER, depois=Pt(80))
    h.paragrafo(doc, "Nampula", WD_ALIGN_PARAGRAPH.CENTER, depois=Pt(2))
    h.paragrafo(doc, "2026", WD_ALIGN_PARAGRAPH.CENTER, depois=Pt(0))
    h.quebra_pagina(doc)



def _folha_de_rosto(h, doc):
    h.paragrafo(doc, ESTUDANTE, WD_ALIGN_PARAGRAPH.CENTER, depois=Pt(60))
    h.paragrafo(doc, TITULO_ESTUDO, WD_ALIGN_PARAGRAPH.CENTER, negrito=True,
                tamanho=Pt(13), depois=Pt(48))
    par = h.paragrafo(doc, "Protocolo de investigação apresentado à Faculdade de Ciências de "
                      "Saúde da Universidade Lúrio, como parte dos requisitos para a elaboração "
                      "do Trabalho de Conclusão de Curso conducente à obtenção do grau de "
                      "licenciada em Psicologia.", WD_ALIGN_PARAGRAPH.JUSTIFY,
                      tamanho=Pt(11), espaco=1.0, depois=Pt(36))
    par.paragraph_format.left_indent = Cm(8)
    h.paragrafo(doc, f"Orientador: {ORIENTADOR_COM_GRAU}", WD_ALIGN_PARAGRAPH.LEFT,
                depois=Pt(72))
    h.paragrafo(doc, "Nampula", WD_ALIGN_PARAGRAPH.CENTER, depois=Pt(2))
    h.paragrafo(doc, "2026", WD_ALIGN_PARAGRAPH.CENTER, depois=Pt(0))
    h.quebra_pagina(doc)



def _declaracao_do_orientador(h, doc):
    """Texto-modelo da FCS (o mesmo do protocolo da Muanchura): o orientador atesta a
    aptidao para provas publicas e identifica a estudante pelo bilhete e pelo numero."""
    h.titulo(doc, "DECLARAÇÃO DO ORIENTADOR", 1)
    h.paragrafo(doc, f"Eu, {ORIENTADOR}, Mestre, portador do Bilhete de Identidade n.º "
                "____________________, docente da Faculdade de Ciências de Saúde da Universidade "
                "Lúrio, venho por este meio atestar que o protocolo de investigação da estudante "
                f"{ESTUDANTE}, portadora do Bilhete de Identidade n.º {BI_ESTUDANTE} e com o "
                f"número de estudante {NUMERO_ESTUDANTE}, do Curso de Psicologia, intitulado "
                f"«{TITULO_CORRENTE}», foi elaborado sob a minha orientação e se encontra, do "
                "ponto de vista estrutural e metodológico, em condições de ser apresentado e "
                "defendido em provas públicas, nos termos do regulamento em vigor.")
    h.paragrafo(doc, "", depois=Pt(24))
    h.paragrafo(doc, "Nampula, ____ de ______________ de 2026.", WD_ALIGN_PARAGRAPH.LEFT,
                depois=Pt(36))
    for texto, depois in (("O Orientador", Pt(30)), ("_" * 38, Pt(2)),
                          (f"({ORIENTADOR_COM_GRAU})", Pt(0))):
        h.paragrafo(doc, texto, WD_ALIGN_PARAGRAPH.CENTER, espaco=1.15, depois=depois)
    h.quebra_pagina(doc)


def _amostra_prevista():
    """Menor e maior amostra final dos cenarios da Tabela 1, incluindo a coluna de
    sensibilidade com efeito de desenho de 2,0, para o resumo."""
    return (amostra_para(min(POPULACOES))[1],
            amostra_para(max(POPULACOES), DEFF_SENSIBILIDADE)[1])


def _resumo(e, h, doc):
    """Paragrafo unico de 250 a 300 palavras, sem citacoes nem siglas (norma da FCS)."""
    minimo, maximo = _amostra_prevista()
    h.titulo(doc, "RESUMO", 1)
    e.p("O comportamento agressivo na adolescência é um problema de saúde pública, "
        "frequentemente associado a sofrimento psicológico, com consequências duradouras para "
        "quem agride, para quem é vitimado e para a comunidade escolar. Do ponto de vista clínico, não é apenas uma conduta a corrigir: pode exprimir "
        "dificuldades de regulação das emoções, impulsividade, sintomas emocionais ou "
        "pós-traumáticos e experiências de violência. Em Moçambique, "
        "os dados nacionais mostram uma exposição precoce e generalizada à violência e uma "
        "frequência elevada de sofrimento psicológico nos adolescentes escolarizados, mas não "
        "existem estudos em Nampula que relacionem estes factores com a agressividade medida por "
        "instrumentos validados. Este estudo tem como objectivo analisar os factores "
        "psicossociais, com destaque para os factores psicológicos individuais, relacionados ao "
        "comportamento agressivo em adolescentes dos 10 aos 19 anos da Escola Secundária de "
        "Muatala, no segundo semestre de 2026. Trata-se de um estudo transversal, analítico e "
        "quantitativo, com amostragem probabilística de turmas estratificada por classe, numa "
        "amostra mínima estimada entre "
        f"{minimo} e {maximo} alunos. O "
        "comportamento agressivo será medido pela forma reduzida do Questionário de "
        "Agressividade de Buss e Perry e pelo Questionário de Agressão Reactiva e Proactiva. O "
        "funcionamento psicológico será avaliado pelo Questionário de Capacidades e de "
        "Dificuldades, pela forma reduzida da Escala de Dificuldades de Regulação Emocional, pela "
        "Escala de Auto-Estima de Rosenberg e por uma escala de rastreio do stress "
        "pós-traumático, e os contextos familiar, escolar e comunitário por módulos de inquéritos "
        "validados, num questionário confidencial de auto-preenchimento. A análise incluirá "
        "regressão linear múltipla por blocos, modelos separados para a agressão reactiva e para "
        "a proactiva e uma análise exploratória de mediação pela regulação emocional, ajustadas "
        "ao desenho amostral. Espera-se identificar os factores psicológicos e psicossociais "
        "associados à agressividade e fundamentar a detecção, o encaminhamento e a intervenção "
        "psicológica dirigidos aos adolescentes da escola.")
    e.p("Palavras-chave: adolescente, agressividade, factores psicossociais, psicopatologia, "
        "regulação emocional.")
    h.quebra_pagina(doc)


def _abstract(e, h, doc):
    minimo, maximo = _amostra_prevista()
    h.titulo(doc, "ABSTRACT", 1)
    e.p("Aggressive behaviour in adolescence is a public health problem, often associated with "
        "psychological distress, with lasting consequences for perpetrators, for victims and "
        "for the school community. From "
        "a clinical point of view, it is not merely conduct to be corrected: it may express "
        "difficulties in regulating emotions, impulsivity, emotional or post-traumatic symptoms "
        "and experiences of violence. In Mozambique, national "
        "data show early and widespread exposure to violence and a high frequency of "
        "psychological distress among school-going adolescents, but no studies in Nampula have "
        "related these factors to aggression measured with validated instruments. This study "
        "aims to analyse the psychosocial factors, with emphasis on individual psychological "
        "factors, related to aggressive behaviour among adolescents aged 10 to 19 years at "
        "Muatala Secondary School during the second semester of 2026. It is a cross-sectional, "
        "analytical and quantitative study, with probability sampling of classes stratified by "
        f"grade, in an estimated minimum sample of {minimo} to {maximo} students. "
        "Aggressive behaviour will be measured with the short form of the Buss-Perry Aggression "
        "Questionnaire and with the Reactive-Proactive Aggression Questionnaire. Psychological "
        "functioning will be assessed with the Strengths and Difficulties Questionnaire, the "
        "short form of the Difficulties in Emotion Regulation Scale, the Rosenberg Self-Esteem "
        "Scale and a post-traumatic stress screening scale, and the family, school and community "
        "contexts with modules of validated surveys, in a confidential self-administered "
        "questionnaire. Analysis will include hierarchical multiple linear regression, separate "
        "models for reactive and proactive aggression and an exploratory mediation analysis "
        "through emotion regulation, adjusted for the sampling design. The study is expected to "
        "identify the psychological and psychosocial factors associated with aggression and to "
        "support the detection, referral and psychological intervention directed at the "
        "school's adolescents.")
    e.p("Keywords: adolescent, aggression, emotion regulation, psychopathology, psychosocial "
        "factors.")
    h.quebra_pagina(doc)


def _abreviaturas_e_indice(h, doc):
    """Lista de abreviaturas e indice automatico; o indice nao se lista a si proprio."""
    h.titulo(doc, "LISTA DE ABREVIATURAS E SIGLAS", 1)
    for linha in ABREVIATURAS:
        h.paragrafo(doc, linha, WD_ALIGN_PARAGRAPH.LEFT, espaco=1.15, depois=Pt(2))
    h.quebra_pagina(doc)

    par = h.paragrafo(doc, "ÍNDICE", WD_ALIGN_PARAGRAPH.LEFT, negrito=True, tamanho=Pt(13),
                      depois=Pt(6))
    par.paragraph_format.space_before = Pt(12)
    h.indice_automatico(doc)


def escrever_pre_textuais(e, h, doc):
    """Capa, folha de rosto, declaracao, resumo, abstract, abreviaturas e indice.

    Termina sem quebra de pagina: o construtor abre a seguir a seccao do corpo do texto,
    com numeracao arabe a comecar em 1.
    """
    _capa(h, doc)
    _folha_de_rosto(h, doc)
    _declaracao_do_orientador(h, doc)
    _resumo(e, h, doc)
    _abstract(e, h, doc)
    _abreviaturas_e_indice(h, doc)


def _introducao_conceitos(e):
    e.p("A adolescência, definida pela Organização Mundial da Saúde (OMS) como o período que vai "
        "dos 10 aos 19 anos de idade, é a fase em que se consolidam a identidade, a autonomia e os "
        "padrões de comportamento que acompanham o indivíduo na vida adulta [[oms_adolescente]]. "
        "É também uma fase de vulnerabilidade psicológica: cerca de um em cada sete adolescentes "
        "vive com uma perturbação mental, e as perturbações do comportamento, marcadas pela "
        "agressividade e pela violação persistente de regras, afectam 3,3 por cento dos "
        "adolescentes dos 10 aos 14 anos e 1,8 por cento dos 15 aos 19 anos "
        "[[oms_saude_mental]].")
    e.p("Na literatura psicológica, o comportamento agressivo é entendido como qualquer conduta "
        "dirigida a outra pessoa com a intenção imediata de lhe causar dano, e a violência como a "
        "forma de agressão que visa um dano extremo, como lesão grave ou morte [[anderson2002]]. "
        "Buss e Perry distinguem quatro dimensões da agressividade, a agressão física, a agressão "
        "verbal, a ira e a hostilidade [[buss1992]], e Dodge e Coie duas funções, a reactiva, "
        "resposta impulsiva a uma provocação percebida, e a proactiva, deliberada e orientada "
        "para um objectivo [[dodge1987,raine2006]].")
    e.p("Do ponto de vista clínico, a agressividade não é, em si mesma, um diagnóstico, mas uma "
        "manifestação transdiagnóstica. É critério central da perturbação do comportamento, que "
        "inclui agressão a pessoas e a animais, e da perturbação explosiva intermitente; na "
        "perturbação de oposição e desafio, cujos critérios não incluem agressão física, surge "
        "sob a forma de humor zangado e irritável, de discussões com figuras de autoridade e de "
        "comportamento vingativo. Acompanha com frequência a perturbação de hiperactividade e "
        "défice de atenção e surge também em quadros depressivos, ansiosos e pós-traumáticos, "
        "sob a forma de irritabilidade e de explosões de raiva [[apa2022,fairchild2019]]. Perante "
        "um adolescente agressivo, a pergunta clínica não é apenas o que ele faz, mas o que está "
        "por detrás do que faz: que emoções não consegue regular, que intenções atribui aos "
        "outros, que experiências viveu e que sofrimento a agressão exprime.")


def _introducao_magnitude_e_lacuna(e):
    e.p("A magnitude do problema é considerável. A violência juvenil figura entre as principais "
        "causas de morte e de incapacidade dos jovens dos 15 aos 29 anos em todo o mundo, e por "
        "cada jovem que morre muitos outros são tratados por ferimentos resultantes de agressões "
        "[[oms_violencia_jovem]]. A análise do inquérito global de saúde escolar (Global "
        "School-based Student Health Survey, GSHS), realizada em 68 países de baixo e médio "
        "rendimento, estimou que 36,4 por cento dos adolescentes dos 12 aos 15 anos se envolveram "
        "em lutas físicas, mais os rapazes do que as raparigas, e que 34,4 por cento foram alvo "
        "de bullying, sem diferença entre os sexos [[han2019]]. Na África subsariana, numa análise "
        "agrupada de oito países, a prevalência de violência interpessoal entre adolescentes "
        "escolarizados dos 10 aos 19 anos foi de 53,7 por cento [[aboagye2021a]].")
    e.p("Em Moçambique, o Inquérito Nacional sobre a Violência Contra as Crianças e os Jovens "
        "(Violence Against Children and Youth Survey, VACS), realizado em 2019, mostrou que 23,9 "
        "por cento das raparigas e 34,1 por cento dos rapazes dos 18 aos 24 anos sofreram "
        "violência física antes dos 18 anos, e que 27,5 por cento das raparigas e 38,2 por cento "
        "dos rapazes testemunharam violência física dentro de casa [[vacs2019]]. A exposição à "
        "violência tem expressão psicológica: num estudo com entrevista diagnóstica estruturada em "
        "duas escolas da cidade de Maputo, 23,0 por cento dos 488 estudantes dos 12 aos 19 anos "
        "apresentavam uma perturbação mental, sobretudo ansiosa e depressiva, e apenas 2,7 por "
        "cento dos que tinham uma perturbação tinham procurado cuidados [[king2026]]. Em "
        "distritos marcados por conflito armado, como Gorongosa, os problemas de saúde mental dos "
        "jovens aparecem associados à exposição à violência e às dificuldades socioeconómicas do "
        "agregado [[igreja2024]].")


def _introducao_teoria_e_lacuna(e):
    e.p("A explicação para o comportamento agressivo raramente é única. A teoria da aprendizagem "
        "social demonstrou, desde os trabalhos clássicos de Bandura, que a criança aprende a "
        "agredir observando e imitando modelos agressivos do seu meio [[bandura1961]]. O Modelo "
        "Geral da Agressão integra esta e outras teorias: os factores da pessoa e da situação "
        "influenciam o comportamento através do estado interno do indivíduo, feito de "
        "pensamentos hostis, de raiva e de activação fisiológica, e dos processos de avaliação e "
        "de decisão que se seguem [[anderson2002,allen2018]]. Nesta perspectiva, os factores "
        "psicossociais do contexto, como a violência em casa, o castigo físico ou a vitimização "
        "pelos pares, actuam em grande parte através de características psicológicas do "
        "adolescente, como as dificuldades de regulação emocional, o enviesamento de atribuição "
        "hostil, a impulsividade e os sintomas de stress pós-traumático, que são precisamente os "
        "alvos da avaliação e da intervenção em psicologia clínica [[roberton2012,xu2024]]. O "
        "modelo ecológico adoptado pela OMS permanece útil para organizar esses contextos nos "
        "níveis individual, relacional, comunitário e social [[krug2002]].")
    e.p("Apesar da relevância do tema, a investigação moçambicana sobre a agressividade em "
        "adolescentes escolarizados é escassa, concentra-se nas regiões sul e centro do país e "
        "raramente "
        "examina os factores psicológicos que a acompanham. Na cidade de Nampula, onde se situa a "
        "Escola Secundária de Muatala, não se conhecem estudos que tenham medido o comportamento "
        "agressivo com instrumentos psicométricos validados nem que tenham avaliado, em conjunto, "
        "o funcionamento psicológico dos adolescentes e os contextos em que vivem. Este protocolo "
        "propõe-se colmatar essa lacuna, analisando os factores psicossociais associados ao "
        "comportamento agressivo nos adolescentes dos 10 aos 19 anos daquela escola, durante o "
        "segundo semestre de 2026, com particular atenção aos factores psicológicos individuais, "
        "de modo a fundamentar a avaliação, o encaminhamento e a intervenção psicológica "
        "ajustados ao contexto local.")


def escrever_introducao(e):
    e.h1("1. INTRODUÇÃO")
    _introducao_conceitos(e)
    _introducao_magnitude_e_lacuna(e)
    _introducao_teoria_e_lacuna(e)


def escrever_problema(e):
    e.h1("2. IDENTIFICAÇÃO E FORMULAÇÃO DO PROBLEMA")
    e.p("As escolas secundárias moçambicanas convivem com episódios frequentes de agressão entre "
        "alunos, que vão da injúria e da ameaça às agressões físicas e ao bullying persistente. "
        "Estes episódios associam-se ao absentismo [[aboagye2021a]] e ao abandono escolar "
        "[[oms_violencia_jovem]] e a sofrimento psicológico tanto nos adolescentes que se "
        "envolvem em lutas como nos que são agredidos ou vítimas de bullying [[amu2020]]. A resposta habitual é disciplinar: advertências, suspensões "
        "e, por vezes, castigos físicos. Essa resposta trata a agressividade como um problema de "
        "conduta a corrigir e deixa por avaliar o que, do ponto de vista clínico, ela pode "
        "sinalizar: dificuldades de regulação das emoções, sintomas depressivos, ansiosos ou "
        "pós-traumáticos, baixa auto-estima ou uma história de violência sofrida em casa "
        "[[fairchild2019,roberton2012]]. Em duas escolas de Maputo, só 2,7 por cento dos "
        "adolescentes com perturbação mental tinham procurado cuidados [[king2026]], o que "
        "sugere que esse sofrimento tende a passar despercebido.")
    e.p("A literatura identifica de forma consistente dois grupos de factores associados ao "
        "comportamento agressivo. No plano psicológico individual, destacam-se as dificuldades "
        "de regulação emocional, a impulsividade, o enviesamento de atribuição hostil, os "
        "sintomas de stress pós-traumático e os traços de insensibilidade emocional "
        "[[roberton2012,xu2024,frick2014]]. No plano do contexto, contam-se o castigo físico e a "
        "violência "
        "vividos ou testemunhados em casa, a fraca supervisão parental e a disfunção familiar, a "
        "vitimização por bullying, a associação a pares desviantes, o consumo de substâncias e a "
        "exposição à violência comunitária [[gershoff2016,tian2019,zhu2016,brown2024]]. Em "
        "Moçambique, os determinantes do contexto estão bem documentados, entre eles a elevada "
        "exposição infantil à violência física e sexual, incluindo em ambiente escolar, e o "
        "legado da violência política em várias regiões do país [[vacs2019,matsinhe2024,"
        "vigneri2026]]. O que falta é a articulação local entre esses determinantes, o "
        "funcionamento psicológico dos adolescentes e a medida psicométrica da sua agressividade.")
    e.p("A Escola Secundária de Muatala reúne alunos provenientes de um bairro periurbano da "
        "cidade de Nampula, caracterizado por elevada densidade populacional, rendimento familiar "
        "baixo e acesso limitado a serviços de saúde mental. Em 2025, a comunidade escolar "
        "registou numerosos episódios de agressividade entre alunos, facto que motivou este "
        "estudo. Não existe, porém, na escola nem na cidade, qualquer avaliação sistemática do "
        "comportamento agressivo dos seus adolescentes, dos factores psicológicos que o "
        "acompanham nem dos contextos em que ocorre. Sem essa avaliação, qualquer resposta, "
        "disciplinar, preventiva ou clínica, assentaria em pressupostos e não na realidade dos "
        "alunos. Perante o exposto, formula-se a seguinte pergunta de partida:")
    e.p("«Quais são os factores psicossociais, e em particular os factores psicológicos "
        "individuais, relacionados com o comportamento agressivo nos adolescentes dos 10 aos 19 "
        "anos da Escola Secundária de Muatala, na cidade de Nampula, no segundo semestre de "
        "2026?»")
    e.h2("2.1. Delimitação do problema")
    e.p("O estudo circunscreve-se aos adolescentes dos 10 aos 19 anos regularmente matriculados na "
        "Escola Secundária de Muatala, bairro de Muatala, cidade de Nampula, província de Nampula, "
        "no segundo semestre de 2026. O objecto de estudo é o comportamento "
        "agressivo auto-relatado, nas dimensões física, verbal, de ira e de hostilidade e nas "
        "formas reactiva e proactiva. Os factores associados são analisados em dois planos. O "
        "plano psicológico individual abrange a regulação emocional, a hiperactividade e "
        "desatenção, os sintomas emocionais e de stress pós-traumático, a auto-estima e o "
        "comportamento pró-social. O plano do contexto abrange a família, a escola, o grupo de "
        "pares e a comunidade. As medidas psicológicas têm carácter de rastreio. Ficam fora do "
        "âmbito do estudo o diagnóstico clínico individual de perturbações mentais, que exigiria "
        "entrevista clínica estruturada, a agressão praticada por adultos da escola e qualquer "
        "avaliação de eficácia de intervenções, que exigiria um desenho longitudinal ou "
        "experimental.")
