"""Elementos pre-textuais e seccoes 1 a 6 do protocolo (introducao a revisao da literatura)."""
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Cm, Pt

from _protocolo_amostra import POPULACOES, amostra_para

TITULO_ESTUDO = ("FACTORES PSICOSSOCIAIS RELACIONADOS AO COMPORTAMENTO AGRESSIVO EM "
                 "ADOLESCENTES DOS 10 AOS 19 ANOS: CASO DA ESCOLA SECUNDÁRIA DE MUATALA, "
                 "CIDADE DE NAMPULA, SEGUNDO SEMESTRE DE 2026")

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
    "deff = efeito de desenho (design effect);",
    "FCS = Faculdade de Ciências de Saúde;",
    "GSHS = Global School-based Student Health Survey;",
    "IC = intervalo de confiança;",
    "INSPIRE = pacote de sete estratégias da Organização Mundial da Saúde para pôr fim à "
    "violência contra as crianças;",
    "MINEDH = Ministério da Educação e Desenvolvimento Humano;",
    "MISAU = Ministério da Saúde;",
    "MZN = metical moçambicano;",
    "OMS = Organização Mundial da Saúde;",
    "OR = odds ratio;",
    "RPQ = Reactive-Proactive Aggression Questionnaire;",
    "SDQ = Strengths and Difficulties Questionnaire;",
    "SPSS = Statistical Package for the Social Sciences;",
    "STROBE = Strengthening the Reporting of Observational Studies in Epidemiology;",
    "TCLE = termo de consentimento livre e esclarecido;",
    "UniLúrio = Universidade Lúrio;",
    "VACS = Violence Against Children and Youth Survey.",
]

ESTADO_DA_ARTE = [
    ["Han et al., 2019 [[han2019]]", "68 países de baixo e médio rendimento",
     "Transversal, 164.633 adolescentes de 12 a 15 anos",
     "Luta física 36,4%; agressão física sofrida 35,6%; bullying 34,4%; prevalências superiores "
     "nos rapazes"],
    ["Aboagye et al., 2021 [[aboagye2021a]]", "8 países da África subsariana",
     "Transversal, 14.967 adolescentes de 10 a 19 anos",
     "Violência interpessoal 53,7%; associada a bullying (aOR 2,52), consumo de álcool (aOR 1,49) "
     "e absentismo (aOR 1,51)"],
    ["Aboagye et al., 2021 [[aboagye2021b]]", "11 países da África subsariana",
     "Transversal, 25.454 adolescentes escolarizados",
     "Vitimização por bullying 38,8%; associada a solidão, ansiedade e consumo de canábis; apoio "
     "dos pares como factor protector"],
    ["Ameli et al., 2017 [[ameli2017]]", "Malawi", "Transversal, adolescentes escolarizados",
     "Castigo físico na escola em 42,4% das raparigas e 36,4% dos rapazes; associação com "
     "problemas de externalização"],
    ["Tarafa et al., 2022 [[tarafa2022]]", "Etiópia (Illu Abba Bor)",
     "Transversal, adolescentes escolarizados",
     "Vitimização por bullying associada ao sexo masculino, ao consumo de substâncias e à "
     "disfunção familiar"],
    ["Ugwu et al., 2024 [[ugwu2024]]", "Nigéria", "Transversal, adolescentes escolarizados",
     "Adversidade na infância associada à perpetração de bullying, com mediação pela influência "
     "dos pares"],
    ["Tian et al., 2019 [[tian2019]]", "China", "Transversal, 1.108 adolescentes",
     "Controlo psicológico parental associado à agressividade, mediado pela associação a pares "
     "desviantes e moderado pela ligação à escola"],
    ["Zhu et al., 2016 [[zhu2016]]", "China", "Longitudinal, adolescentes",
     "Vitimização pelos pares prediz comportamento agressivo, com mediação por pares desviantes e "
     "moderação pela impulsividade"],
    ["Gershoff e Grogan-Kaylor, 2016 [[gershoff2016]]", "Meta-análise internacional",
     "Meta-análise de 75 estudos, mais de 160 mil crianças",
     "Castigo físico associado a maior agressividade e a mais problemas de comportamento, sem "
     "qualquer benefício documentado"],
    ["Elgar et al., 2018 [[elgar2018]]", "88 países", "Estudo ecológico, 403.604 adolescentes",
     "Países com proibição total do castigo corporal apresentam 69% da taxa de lutas frequentes "
     "nos rapazes e 42% nas raparigas"],
    ["Blum et al., 2019 [[blum2019]]", "14 países de vários continentes",
     "Transversal, adolescentes de 10 a 14 anos",
     "Experiências adversas na infância associadas a sintomas depressivos e à perpetração de "
     "violência"],
    ["Brown et al., 2024 [[brown2024]]", "África subsariana",
     "Análise multipaís dos inquéritos VACS",
     "Experiências adversas na infância associadas a sofrimento mental, consumo de substâncias e "
     "perpetração de violência"],
    ["Governo de Moçambique, 2022 [[vacs2019]]", "Moçambique",
     "Inquérito nacional VACS, 13 a 24 anos",
     "Violência física antes dos 18 anos em 23,9% das raparigas e 34,1% dos rapazes; 27,5% e "
     "38,2% testemunharam violência física em casa"],
    ["Semá Baltazar et al., 2025 [[sema2025]]", "Moçambique", "Análise secundária do VACS 2019",
     "Consumo de álcool 29,7% e de drogas 22,5% entre os 13 e os 24 anos"],
    ["King et al., 2026 [[king2026]]", "Moçambique (cidade de Maputo)",
     "Transversal com entrevista diagnóstica, 488 estudantes de 12 a 19 anos",
     "Perturbações mentais em 23,0%; apenas 2,7% procuraram cuidados no ano anterior"],
    ["Igreja et al., 2024 [[igreja2024]]", "Moçambique (Gorongosa)",
     "Transversal em agregados e escolas, jovens",
     "Problemas de saúde mental frequentes, associados à exposição a violência e a dificuldades "
     "socioeconómicas"],
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
    h.paragrafo(doc, "_" * 45, WD_ALIGN_PARAGRAPH.CENTER, depois=Pt(2))
    h.paragrafo(doc, "(nome completo do estudante)", WD_ALIGN_PARAGRAPH.CENTER,
                tamanho=Pt(11), depois=Pt(72))
    h.paragrafo(doc, "Nampula", WD_ALIGN_PARAGRAPH.CENTER, depois=Pt(2))
    h.paragrafo(doc, "2026", WD_ALIGN_PARAGRAPH.CENTER, depois=Pt(0))
    h.quebra_pagina(doc)



def _folha_de_rosto(h, doc):
    h.paragrafo(doc, "_" * 45, WD_ALIGN_PARAGRAPH.CENTER, depois=Pt(2))
    h.paragrafo(doc, "(nome completo do estudante)", WD_ALIGN_PARAGRAPH.CENTER,
                tamanho=Pt(11), depois=Pt(60))
    h.paragrafo(doc, TITULO_ESTUDO, WD_ALIGN_PARAGRAPH.CENTER, negrito=True,
                tamanho=Pt(13), depois=Pt(48))
    par = h.paragrafo(doc, "Protocolo de investigação apresentado à Faculdade de Ciências de "
                      "Saúde da Universidade Lúrio, como parte dos requisitos para a elaboração "
                      "do Trabalho de Conclusão de Curso conducente à obtenção do grau de "
                      "licenciado em Psicologia.", WD_ALIGN_PARAGRAPH.JUSTIFY,
                      tamanho=Pt(11), espaco=1.0, depois=Pt(36))
    par.paragraph_format.left_indent = Cm(8)
    h.paragrafo(doc, "Orientador: ______________________________", WD_ALIGN_PARAGRAPH.LEFT,
                depois=Pt(6))
    h.paragrafo(doc, "Co-orientador: ___________________________", WD_ALIGN_PARAGRAPH.LEFT,
                depois=Pt(48))
    h.paragrafo(doc, "Nampula", WD_ALIGN_PARAGRAPH.CENTER, depois=Pt(2))
    h.paragrafo(doc, "2026", WD_ALIGN_PARAGRAPH.CENTER, depois=Pt(0))
    h.quebra_pagina(doc)



def _declaracao_do_orientador(h, doc):
    """Texto-modelo da FCS: aptidao para apresentacao e defesa em provas publicas."""
    h.titulo(doc, "DECLARAÇÃO DO ORIENTADOR", 1)
    h.paragrafo(doc, "Declaro, para os devidos efeitos, que o protocolo de investigação intitulado "
                f"«{TITULO_CORRENTE}», da autoria de (nome completo do "
                "estudante), estudante do Curso de Psicologia da Faculdade de "
                "Ciências de Saúde da Universidade Lúrio, foi elaborado sob a minha orientação e "
                "encontra-se, do ponto de vista estrutural e metodológico, em condições de ser "
                "apresentado e defendido em provas públicas, nos termos do regulamento em vigor.")
    h.paragrafo(doc, "", depois=Pt(24))
    h.paragrafo(doc, "Nampula, ____ de ______________ de 2026.", WD_ALIGN_PARAGRAPH.LEFT,
                depois=Pt(36))
    for texto, depois in (("O Orientador", Pt(30)), ("_" * 38, Pt(2)),
                          ("(nome completo e grau académico)", Pt(0))):
        h.paragrafo(doc, texto, WD_ALIGN_PARAGRAPH.CENTER, espaco=1.15, depois=depois)
    h.quebra_pagina(doc)


def _amostra_prevista():
    """Menor e maior amostra final dos cenarios da Tabela 1, para o resumo."""
    return amostra_para(min(POPULACOES))[1], amostra_para(max(POPULACOES))[1]


def _resumo(e, h, doc):
    """Paragrafo unico de 250 a 300 palavras, sem citacoes nem siglas (norma da FCS)."""
    minimo, maximo = _amostra_prevista()
    h.titulo(doc, "RESUMO", 1)
    e.p("O comportamento agressivo na adolescência é um problema de saúde pública e de saúde "
        "mental, com consequências duradouras para quem agride, para quem é vitimado e para o "
        "ambiente escolar. Nos países de baixo e médio rendimento, mais de um terço dos "
        "adolescentes escolarizados relata envolvimento em lutas físicas e, na África "
        "subsariana, mais de metade refere alguma forma de violência interpessoal. Em "
        "Moçambique, os dados nacionais mostram uma exposição precoce e generalizada à violência, "
        "mas não existem estudos locais que relacionem os factores psicossociais com a "
        "agressividade dos adolescentes escolarizados na cidade de Nampula. Este estudo tem como "
        "objectivo analisar os factores psicossociais relacionados ao comportamento agressivo em "
        "adolescentes dos 10 aos 19 anos da Escola Secundária de Muatala, no segundo semestre de "
        "2026. Trata-se de um estudo transversal, analítico e quantitativo, com amostragem "
        "probabilística estratificada por classe e selecção aleatória de turmas, numa amostra "
        f"estimada entre {minimo} e {maximo} alunos, consoante o número de alunos elegíveis. O "
        "comportamento agressivo será medido pela forma reduzida do Questionário de Agressividade "
        "de Buss e Perry e pelo Questionário de Agressão Reactiva e Proactiva, ambos com versão "
        "portuguesa validada. Os factores familiares, escolares, do grupo de pares e comunitários "
        "serão avaliados por módulos de instrumentos validados, reunidos num questionário anónimo "
        "de auto-preenchimento, que será submetido a um painel de peritos, a um pré-teste "
        "cognitivo e a um estudo-piloto para estimar a fiabilidade. A análise incluirá "
        "estatística descritiva, testes de comparação e de correlação e modelos de regressão "
        "linear múltipla e logística binária ajustados ao desenho amostral, com um nível de "
        "significância de 5 por cento. Espera-se identificar os factores psicossociais "
        "independentemente associados ao comportamento agressivo e fundamentar um programa "
        "escolar de prevenção alinhado com as estratégias da Organização Mundial da Saúde para "
        "pôr fim à violência contra as crianças.")
    e.p("Palavras-chave: adolescente, agressividade, factores psicossociais, Moçambique, "
        "violência.")
    h.quebra_pagina(doc)


def _abstract(e, h, doc):
    minimo, maximo = _amostra_prevista()
    h.titulo(doc, "ABSTRACT", 1)
    e.p("Aggressive behaviour in adolescence is a public health and mental health problem, with "
        "lasting consequences for those who aggress, for those who are victimised and for the "
        "school environment. In low- and middle-income countries, more than one third of "
        "school-going adolescents report involvement in physical fights and, in sub-Saharan "
        "Africa, more than half report some form of interpersonal violence. In Mozambique, "
        "national data show early and widespread exposure to violence, but there are no local "
        "studies relating psychosocial factors to aggression among school-going adolescents in "
        "Nampula city. This study aims to analyse the psychosocial factors related to aggressive "
        "behaviour among adolescents aged 10 to 19 years at Muatala Secondary School during the "
        "second semester of 2026. It is a cross-sectional, analytical and quantitative study, "
        "with probability sampling stratified by grade and random selection of classes, in an "
        f"estimated sample of {minimo} to {maximo} students, depending on the number of eligible "
        "students. Aggressive behaviour will be measured with the short form of the Buss-Perry "
        "Aggression Questionnaire and with the Reactive-Proactive Aggression Questionnaire, both "
        "with validated Portuguese versions. Family, school, peer and community factors will be "
        "assessed with modules of validated instruments, combined into an anonymous "
        "self-administered questionnaire that will undergo expert review, cognitive pre-testing "
        "and a pilot study to estimate reliability. Analysis will include descriptive statistics, "
        "comparison and correlation tests, and multiple linear and binary logistic regression "
        "models adjusted for the sampling design, with a 5 per cent significance level. The study "
        "is expected to identify the psychosocial factors independently associated with "
        "aggressive behaviour and to support a school-based prevention programme aligned with "
        "the World Health Organization strategies for ending violence against children.")
    e.p("Keywords: adolescent, aggression, Mozambique, psychosocial factors, violence.")
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
        "padrões de relacionamento que acompanham o indivíduo na vida adulta [[oms_adolescente]]. "
        "É também o período em que se tornam mais visíveis os comportamentos externalizantes, "
        "entre os quais o comportamento agressivo ocupa lugar central, pelo peso que tem no "
        "percurso escolar, na saúde mental e na integração social do jovem [[scott2018]].")
    e.p("Na literatura psicológica, o comportamento agressivo é entendido como qualquer conduta "
        "dirigida a outrem com a intenção de causar dano, distinguindo-se da violência pela "
        "gravidade e pela intencionalidade lesiva do acto [[krug2002]]. O modelo mais usado na "
        "avaliação da agressividade, proposto por Buss e Perry, organiza o construto em quatro "
        "dimensões: a agressão física, a agressão verbal, a ira e a hostilidade, sendo as duas "
        "primeiras de natureza instrumental e as duas últimas, respectivamente, de natureza "
        "emocional e cognitiva [[buss1992]]. A esta leitura acrescenta-se a distinção funcional "
        "entre a agressão reactiva, que surge como resposta defensiva a uma provocação percebida, "
        "e a agressão proactiva, deliberada e orientada para um objectivo, com correlatos "
        "psicossociais distintos [[raine2006]].")


def _introducao_magnitude_e_lacuna(e):
    e.p("A magnitude do problema é considerável. A violência juvenil figura entre as principais "
        "causas de morte e de incapacidade em adolescentes e adultos jovens em todo o mundo, e por "
        "cada jovem que morre muitos outros são atendidos por ferimentos resultantes de agressões "
        "[[oms_violencia_jovem]]. A análise do inquérito global de saúde escolar (Global "
        "School-based Student Health Survey, GSHS), realizada em 68 países de baixo e médio "
        "rendimento, estimou que 36,4 por cento dos adolescentes dos 12 "
        "aos 15 anos se envolveram em lutas físicas e 34,4 por cento foram alvo de bullying nos "
        "períodos de referência, com prevalências consistentemente superiores nos rapazes "
        "[[han2019]]. Na África subsariana os valores são ainda mais elevados: numa análise "
        "agrupada de oito países, envolvendo 14.967 adolescentes dos 10 aos 19 anos, a prevalência "
        "de violência interpessoal foi de 53,7 por cento, e num conjunto de onze países a "
        "vitimização por bullying atingiu 38,8 por cento [[aboagye2021a,aboagye2021b]].")
    e.p("Em Moçambique, o Inquérito Nacional sobre a Violência Contra as Crianças e os Jovens "
        "(Violence Against Children and Youth Survey, VACS), realizado em 2019, mostrou que 23,9 por cento das raparigas e 34,1 por cento dos rapazes "
        "dos 18 aos 24 anos sofreram violência física antes dos 18 anos, e que 27,5 por cento das "
        "raparigas e 38,2 por cento dos rapazes testemunharam violência física dentro de casa no "
        "mesmo período [[vacs2019]]. Entre os adolescentes dos 13 aos 17 anos, 8,2 por cento das "
        "raparigas e 16,8 por cento dos rapazes referiram violência física praticada por pares nos "
        "doze meses anteriores, e cerca de um terço, em ambos os sexos, presenciou violência física "
        "na comunidade no mesmo intervalo [[vacs2019]]. A análise multipaís dos mesmos inquéritos "
        "na África subsariana confirma que a exposição à violência na infância é a regra e não a "
        "excepção, com mais de sete em cada dez inquiridos a relatar pelo menos uma experiência "
        "adversa [[amene2024]].")
    e.p("A estes dados junta-se um padrão preocupante de consumo de substâncias e de sofrimento "
        "psicológico. Ainda a partir do inquérito nacional de 2019, a prevalência de consumo de "
        "álcool entre os 13 e os 24 anos foi de 29,7 por cento e a de consumo de drogas de 22,5 "
        "por cento [[sema2025]]. Num estudo conduzido em duas escolas da cidade de Maputo com "
        "entrevista diagnóstica estruturada, 23,0 por cento dos 488 estudantes dos 12 aos 19 anos "
        "apresentavam uma perturbação mental, sobretudo do espectro ansioso e depressivo, e apenas "
        "2,7 por cento tinham procurado cuidados de saúde mental no ano anterior [[king2026]]. Em "
        "distritos marcados por conflito armado, como Gorongosa, os problemas de saúde mental dos "
        "jovens aparecem associados à exposição à violência e às dificuldades socioeconómicas do "
        "agregado [[igreja2024]].")


def _introducao_teoria_e_lacuna(e):
    e.p("A explicação para estas condutas raramente é individual. A teoria da aprendizagem social "
        "demonstrou, desde os trabalhos clássicos de Bandura, que a criança aprende a agredir "
        "observando e imitando modelos agressivos do seu meio, sobretudo quando esses modelos são "
        "recompensados [[bandura1961]]. O modelo ecológico adoptado pela OMS organiza os "
        "determinantes da violência em quatro níveis que interagem entre si, o individual, o "
        "relacional, o comunitário e o social, e é hoje a moldura de referência para o desenho de "
        "intervenções preventivas [[krug2002]]. A tradução operacional desta moldura consta do "
        "relatório global sobre a prevenção da violência contra as crianças e do pacote da OMS "
        "para pôr fim à violência contra as crianças (INSPIRE), que reúne sete estratégias de "
        "eficácia comprovada, entre as quais a educação parental, a "
        "criação de ambientes escolares seguros e o desenvolvimento de competências "
        "socioemocionais [[oms_status2020,inspire2016]].")
    e.p("Apesar da relevância do tema, a investigação moçambicana sobre a agressividade em "
        "adolescentes escolarizados é escassa e concentra-se na região sul do país. Na cidade de "
        "Nampula, onde se situa a Escola Secundária de Muatala, não se conhecem estudos que "
        "tenham medido o comportamento agressivo com instrumentos psicométricos validados nem que "
        "tenham examinado os factores psicossociais a ele associados. Este protocolo propõe-se "
        "colmatar essa lacuna, analisando os factores psicossociais relacionados ao comportamento "
        "agressivo nos adolescentes dos 10 aos 19 anos daquela escola, durante o segundo semestre "
        "de 2026, com vista a fundamentar uma intervenção preventiva ajustada ao contexto local.")


def escrever_introducao(e):
    e.h1("1. INTRODUÇÃO")
    _introducao_conceitos(e)
    _introducao_magnitude_e_lacuna(e)
    _introducao_teoria_e_lacuna(e)


def escrever_problema(e):
    e.h1("2. IDENTIFICAÇÃO E FORMULAÇÃO DO PROBLEMA")
    e.p("As escolas secundárias moçambicanas convivem com episódios frequentes de agressão entre "
        "alunos, que vão da injúria e da ameaça às agressões físicas e ao bullying persistente. "
        "Estes episódios comprometem o clima de aprendizagem, contribuem para o absentismo e o "
        "abandono escolar e produzem sofrimento psicológico em quem agride e em quem é vitimado "
        "[[aboagye2021a,scott2018]]. A direcção das escolas responde, em regra, com medidas "
        "disciplinares que não actuam sobre as causas, porque estas se situam fora da sala de aula.")
    e.p("A literatura internacional identifica de forma consistente um conjunto de factores "
        "psicossociais associados ao comportamento agressivo: o castigo físico e a violência "
        "vividos ou testemunhados em casa, a fraca supervisão parental e a disfunção familiar, a "
        "vitimização por bullying, a associação a pares desviantes, o insucesso escolar, o consumo "
        "de álcool e de outras substâncias psicoactivas e a exposição à violência comunitária "
        "[[gershoff2016,tian2019,zhu2016,brown2024]]. Em Moçambique, os determinantes distais "
        "estão bem documentados, entre eles a elevada exposição infantil à violência física e "
        "sexual, incluindo em ambiente escolar, e o legado da violência política em várias regiões "
        "do país [[vacs2019,matsinhe2024,vigneri2026]]. O que falta é a articulação local entre "
        "estes determinantes e a medida psicométrica da agressividade dos adolescentes que "
        "frequentam a escola.")
    e.p("A Escola Secundária de Muatala reúne alunos provenientes de um bairro periurbano da "
        "cidade de Nampula, caracterizado por elevada densidade populacional, rendimento familiar "
        "baixo e acesso limitado a serviços de saúde mental. Não existe, na escola nem na cidade, "
        "qualquer diagnóstico sistemático do comportamento agressivo dos seus adolescentes nem dos "
        "factores que o acompanham. Sem esse diagnóstico, qualquer programa de prevenção "
        "assentaria em pressupostos importados e não na realidade dos alunos. Perante o exposto, "
        "formula-se a seguinte pergunta de partida:")
    e.p("«Quais são os factores psicossociais relacionados ao comportamento agressivo nos "
        "adolescentes dos 10 aos 19 anos da Escola Secundária de Muatala, na cidade de Nampula, "
        "no segundo semestre de 2026?»")
    e.h2("2.1. Delimitação do problema")
    e.p("O estudo circunscreve-se aos adolescentes dos 10 aos 19 anos regularmente matriculados na "
        "Escola Secundária de Muatala, bairro de Muatala, cidade de Nampula, província de Nampula, "
        "no segundo semestre do ano lectivo de 2026. O objecto de estudo limita-se ao comportamento "
        "agressivo auto-relatado, nas suas dimensões física, verbal, de ira e de hostilidade, e "
        "nas suas formas reactiva e proactiva, e aos factores psicossociais dos níveis individual, "
        "familiar, escolar e do grupo de pares e comunitário que a literatura identifica como "
        "associados. Ficam fora do âmbito do estudo os comportamentos agressivos com indicação "
        "clínica de perturbação psiquiátrica major, a agressão praticada por adultos da escola e "
        "qualquer avaliação de eficácia de intervenções, que exigiria um desenho longitudinal ou "
        "experimental.")
