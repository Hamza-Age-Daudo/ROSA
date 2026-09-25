# -*- coding: utf-8 -*-
"""
Tema 15: Conhecimento das maes e cuidadores sobre os eventos supostamente
atribuiveis a vacinacao ou imunizacao e praticas de notificacao em centros de
saude da cidade de Nampula (Farmacovigilancia e Seguranca do Medicamento).
Estudo transversal analitico, inquerito por entrevista nas consultas de
vacinacao, com componente secundaria censitaria ao pessoal de enfermagem.

Compor e validar:   python _motor/motor.py _conteudo/tema_15.py
Verificar fontes:   python _motor/refs.py verificar _conteudo/tema_15.py
"""
from blocos import (CAMPO, ESCALA, FORMULA, H3, LISTA, NOTA, P, PERG,
                    QUADRO, TABELA)

NUMERO = 15
SLUG = "Eventos_Pos_Vacinais_Maes_Notificacao_Nampula"
TITULO = ("Conhecimento das mães sobre eventos pós-vacinais e práticas de "
          "notificação em centros de saúde da cidade de Nampula, 2027")
DESENHO = ("Transversal analítico, inquérito por entrevista estruturada a mães "
           "e cuidadores nas consultas de vacinação, com componente censitária "
           "ao pessoal de enfermagem do Programa Alargado de Vacinação")

AUTOR = "[Nome do(a) estudante]"
ORIENTADOR = "[Nome e grau académico do(a) orientador(a)]"

# ---------------------------------------------------------------- resumo --
RESUMO = (
    "As vacinas usadas nos programas nacionais de imunização são seguras e "
    "eficazes, mas nenhuma é isenta de risco, e os eventos que surgem depois "
    "da vacinação precisam de ser reconhecidos, tratados e comunicados aos "
    "serviços de saúde. A mãe ou o cuidador é quem primeiro observa esses "
    "eventos na criança, pelo que a vigilância da segurança das vacinas "
    "depende do que estas pessoas sabem, do que fazem quando a criança "
    "adoece depois da vacina e da facilidade com que o serviço recebe e "
    "regista essa informação. Em Moçambique, a proporção de crianças de 12 a "
    "23 meses completamente vacinadas com os antigénios básicos desceu de "
    "66% em 2015 para 38% em 2022 e 2023, e a província de Nampula "
    "apresenta um dos valores mais baixos do país, 25%. Não existe "
    "informação publicada sobre o que as mães de Nampula sabem dos eventos "
    "esperados após as vacinas nem sobre o modo como esses eventos chegam ao "
    "sistema de notificação. O estudo avalia o conhecimento das mães e "
    "cuidadores sobre os eventos que ocorrem depois da vacinação, sobre os "
    "sinais de alarme e sobre o circuito de comunicação, e descreve o "
    "conhecimento e as práticas declaradas do pessoal de enfermagem afecto "
    "às consultas de vacinação. Trata-se de um estudo transversal "
    "analítico, com entrevista estruturada à saída das consultas de "
    "vacinação de seis centros de saúde da cidade de Nampula, em Março e "
    "Abril de 2027, a 600 mães e cuidadores, e com inquérito censitário ao "
    "pessoal de enfermagem dessas consultas. O questionário, adaptado de "
    "instrumentos publicados, será traduzido e retrovertido para a língua "
    "local, validado por um painel de peritos e pré-testado. A análise usará "
    "proporções com intervalos de confiança a 95%, o teste do qui-quadrado e "
    "razões de prevalência ajustadas. Espera-se identificar lacunas de "
    "conhecimento e barreiras concretas à comunicação dos eventos, "
    "informação útil para a formação do pessoal, para o aconselhamento das "
    "famílias e para o reforço da vigilância da segurança das vacinas.")
PALAVRAS_CHAVE = ["cuidadores", "farmacovigilância", "Moçambique",
                  "segurança das vacinas", "vacinação infantil"]
ABSTRACT = (
    "Vaccines used in national immunization programmes are safe and "
    "effective, but no vaccine is free of risk, and events that appear after "
    "vaccination must be recognised, treated and communicated to health "
    "services. The mother or caregiver is the first person to observe such "
    "events in the child, so vaccine safety surveillance depends on what "
    "these people know, on what they do when the child becomes ill after the "
    "vaccine and on how easily the service receives and records that "
    "information. In Mozambique, the proportion of children aged 12 to 23 "
    "months fully vaccinated with the basic antigens fell from 66% in 2015 "
    "to 38% in 2022 and 2023, and Nampula province has one of the lowest "
    "values in the country, 25%. There is no published information on what "
    "mothers in Nampula know about the events expected after vaccines or on "
    "how these events reach the reporting system. The study assesses the "
    "knowledge of mothers and caregivers about events occurring after "
    "vaccination, about danger signs and about the reporting pathway, and "
    "describes the knowledge and self-reported practices of the nursing "
    "staff assigned to vaccination clinics. It is an analytical "
    "cross-sectional study, with structured exit interviews at the "
    "vaccination clinics of six health centres in the city of Nampula, in "
    "March and April 2027, with 600 mothers and caregivers, and a census "
    "survey of the nursing staff of those clinics. The questionnaire, "
    "adapted from published instruments, will be translated and "
    "back-translated into the local language, validated by an expert panel "
    "and pre-tested. The analysis will use proportions with 95% confidence "
    "intervals, the chi-square test and adjusted prevalence ratios. The "
    "study is expected to identify knowledge gaps and concrete barriers to "
    "communicating events, information useful for staff training, for "
    "counselling families and for strengthening vaccine safety "
    "surveillance.")
KEYWORDS = ["caregivers", "child immunization", "Mozambique",
            "pharmacovigilance", "vaccine safety"]

# Só as siglas efectivamente usadas no texto; forma extensa na 1.ª ocorrência.
ABREVIATURAS = [
    ("ANARME", "Autoridade Nacional Reguladora de Medicamento"),
    ("BCG", "bacilo de Calmette e Guérin (vacina contra a tuberculose)"),
    ("ChecKAP", "Checklist for Reporting Items for Knowledge, Attitude and "
                "Practice"),
    ("CIBS-UniLúrio", "Comité Institucional de Bioética para a Saúde da "
                      "Universidade Lúrio"),
    ("CNBS", "Comité Nacional de Bioética para a Saúde"),
    ("DPS", "Direcção Provincial de Saúde"),
    ("DPT-HepB-Hib", "vacina pentavalente contra difteria, tosse convulsa, "
                     "tétano, hepatite B e *Haemophilus influenzae* tipo b"),
    ("ESAVI", "evento supostamente atribuível à vacinação ou imunização"),
    ("FCS", "Faculdade de Ciências de Saúde"),
    ("IC", "intervalo de confiança"),
    ("IVC", "índice de validade de conteúdo"),
    ("KR-20", "fórmula 20 de Kuder-Richardson"),
    ("MISAU", "Ministério da Saúde"),
    ("MR", "vacina contra o sarampo e a rubéola"),
    ("OMS", "Organização Mundial da Saúde"),
    ("OPV", "vacina oral contra a poliomielite"),
    ("OR", "odds ratio"),
    ("ORa", "odds ratio ajustado"),
    ("PAV", "Programa Alargado de Vacinação"),
    ("PCV", "vacina antipneumocócica conjugada"),
    ("RP", "razão de prevalências"),
    ("RPa", "razão de prevalências ajustada"),
    ("SDSMAS", "Serviço Distrital de Saúde, Mulher e Acção Social"),
    ("SNF", "Sistema Nacional de Farmacovigilância"),
    ("SPSS", "Statistical Package for the Social Sciences"),
    ("STROBE", "Strengthening the Reporting of Observational Studies in "
               "Epidemiology"),
    ("UniLúrio", "Universidade Lúrio"),
]

# ------------------------------------------------------------ referencias --
# Todas geradas por refs.py (pmid, doi, web). Nenhum metadado escrito à mão.
FONTES = {
    # -- definicoes, classificacao e enquadramento global da seguranca vacinal
    "omscausalidade2021": "World Health Organization. Causality assessment of an adverse event following immunization (AEFI): user manual for the revised WHO classification, 2nd ed., 2019 update [Internet]. Geneva: World Health Organization; 2021 [citado 2026 Set 19]. Disponível em: https://www.who.int/publications/i/item/9789241516990",
    "omsvigilancia2016": "World Health Organization. Global manual on surveillance of adverse events following immunization, 2016 update [Internet]. Geneva: World Health Organization; 2016 [citado 2026 Set 19]. Disponível em: https://iris.who.int/handle/10665/206144",
    "omsblueprint2022": "World Health Organization. Global vaccine safety blueprint 2.0 (GVSB2.0) 2021-2023 [Internet]. Geneva: World Health Organization; 2022 [citado 2026 Set 19]. Disponível em: https://www.who.int/publications/i/item/9789240036963",
    "omscobertura2026": "World Health Organization. Immunization coverage: fact sheet [Internet]. Geneva: World Health Organization; 2026 [citado 2026 Set 19]. Disponível em: https://www.who.int/news-room/fact-sheets/detail/immunization-coverage",
    "gold2020": "Gold MS, MacDonald NE, McMurtry CM, Balakrishnan MR, Heininger U, Menning L, et al. Immunization stress-related response - Redefining immunization anxiety-related reaction as an adverse event following immunization. Vaccine. 2020;38(14):3015-3020. doi:10.1016/j.vaccine.2020.02.046. PMID: 32131975.",
    "puliyel2018": "Puliyel J, Naik P. Revised World Health Organization (WHO)'s causality assessment of adverse events following immunization-a critique. F1000Res. 2018;7:243. doi:10.12688/f1000research.13694.2. PMID: 30026925.",
    # -- Mocambique e Nampula
    "ine2024ids": "Instituto Nacional de Estatística; Ministério da Saúde. Moçambique. Inquérito Demográfico e de Saúde 2022-23: relatório definitivo [Internet]. Maputo e Rockville: Instituto Nacional de Estatística e ICF; 2024 [citado 2026 Set 19]. Disponível em: https://dhsprogram.com/pubs/pdf/FR389/FR389.pdf",
    "ine2021": "Instituto Nacional de Estatística. IV Recenseamento Geral da População e Habitação 2017: resultados definitivos, província de Nampula [Internet]. Nampula: Instituto Nacional de Estatística; 2021 [citado 2026 Set 19]. Disponível em: http://www.sina.gov.mz/wp-content/uploads/2024/05/NAMPULA-RESUTADOS-DEFINITIVOS-DO-CENSO-2017.pdf",
    "cassocera2020": "Cassocera M, Chissaque A, Martins MRO, Deus N. 40 years of immunization in Mozambique: a narrative review of literature, accomplishments, and perspectives. Cad Saude Publica. 2020;36Suppl 2(Suppl 2):e00038320. doi:10.1590/0102-311X00038320. PMID: 33053042.",
    "cassocera2023": "Cassocera M, Augusto O, Chissaque A, Guimarães EL, Shulock K, de Deus N, et al. Trends and Determinants of Full Immunisation among Children Aged 12-23 Months: Analysis of Pooled Data from Mozambican Household Surveys between 1997 and 2015. Int J Environ Res Public Health. 2023;20(3). doi:10.3390/ijerph20032558. PMID: 36767921.",
    "cassocera2025": "Cassocera M, Bauhofer AFL, Chissaque A, Munlela B, Guimarães E, Isaías T, et al. Regional difference on rotavirus vaccine coverage in children with diarrhea in Mozambique, before and during COVID-19 pandemic: a cross-sectional analysis. BMC Infect Dis. 2025;25(1):382. doi:10.1186/s12879-025-10750-8. PMID: 40108531.",
    "powelson2022": "Powelson J, Magadzire BP, Draiva A, Denno D, Ibraimo A, Benate BBL, et al. Determinants of immunisation dropout among children under the age of 2 in Zambézia province, Mozambique: a community-based participatory research study using Photovoice. BMJ Open. 2022;12(3):e057245. doi:10.1136/bmjopen-2021-057245. PMID: 35292500.",
    "sema2018": "Semá Baltazar C, Rafael F, Langa JPM, Chicumbe S, Cavailler P, Gessner BD, et al. Oral cholera vaccine coverage during a preventive door-to-door mass vaccination campaign in Nampula, Mozambique. PLoS One. 2018;13(10):e0198592. doi:10.1371/journal.pone.0198592. PMID: 30281604.",
    "rafael2017": "Rafael F, Chicumbe S, Cavailler P, Barata A, Langa JPM. Passive, health center-based assessment of adverse events following oral cholera immunization in Nampula city, Mozambique. Vaccine. 2017;35(45):6041-6042. doi:10.1016/j.vaccine.2017.07.033. PMID: 28899627.",
    "shuro2024": "Shuro L, Lawrence E, Knight L, Schneider H, Tabana H. Enhancing childhood immunization coverage in Mozambique and Malawi: Study protocol of a mixed methods evaluation of the 'Let's talk about vaccines' multisite community-based participatory project. PLoS One. 2024;19(11):e0311052. doi:10.1371/journal.pone.0311052. PMID: 39565783.",
    # -- enquadramento normativo mocambicano
    "lei12de2017": "República de Moçambique. Lei n.º 12/2017, de 8 de Setembro: Lei do medicamento, vacinas e outros produtos biológicos para o uso humano [Internet]. Maputo: Imprensa Nacional de Moçambique; 2017 [citado 2026 Set 19]. Disponível em: https://anarme.gov.mz/download/lei-12-2017-de-8-de-setembro-lei-de-medicamento/",
    "snf2023": "República de Moçambique. Diploma Ministerial n.º 3/2023, de 4 de Janeiro: Regulamento do Sistema Nacional de Farmacovigilância [Internet]. Maputo: Autoridade Nacional Reguladora de Medicamento; 2023 [citado 2026 Set 19]. Disponível em: https://anarme.gov.mz/wp-content/uploads/2024/03/Regulamento-do-SNF-1.pdf",
    "lei3de2023": "República de Moçambique. Lei n.º 3/2023, de 8 de Junho: Lei de Investigação em Saúde Humana [Internet]. Maputo: Imprensa Nacional de Moçambique; 2023 [citado 2026 Set 19]. Disponível em: https://anarme.gov.mz/download/lei-3-2023-de-8-de-junho-lei-de-investigacao-em-saude-humana/",
    # -- maes, cuidadores e confianca nas vacinas
    "ansah2025": "Ansah NA, Weibel D, Chatio ST, Oladokun ST, Duah E, Ansah P, et al. Experiences and perceptions about vaccines and reporting of adverse events following immunisation: a qualitative study among mothers in Northern Ghana. BMJ Public Health. 2025;3(2):e001761. doi:10.1136/bmjph-2024-001761. PMID: 40791271.",
    "watyaba2025": "Watyaba B, Chimoyi L, Knezevic I, Malande OO, Kalutte H, Bazira H, et al. Knowledge and reporting of adverse events following childhood immunization (AEFI) among health workers and caregivers at Mengo Hospital (2021), Kampala, Uganda: A mixed-methods study. PLOS Glob Public Health. 2025;5(7):e0004827. doi:10.1371/journal.pgph.0004827. PMID: 40627594.",
    "kajungu2020": "Kajungu D, Muhoozi M, Stark J, Weibel D, Sturkenboom MCJM. Vaccines safety and maternal knowledge for enhanced maternal immunization acceptability in rural Uganda: A qualitative study approach. PLoS One. 2020;15(12):e0243834. doi:10.1371/journal.pone.0243834. PMID: 33301495.",
    "danso2023": "Danso SE, Frimpong A, Seneadza NAH, Ofori MF. Knowledge, attitudes, and practices of caregivers on childhood immunization in Okaikoi sub-metro of Accra, Ghana. Front Public Health. 2023;11:1230492. doi:10.3389/fpubh.2023.1230492. PMID: 37780451.",
    "mbonigaba2024": "Mbonigaba E, Yu F, Reñosa MDC, Cho FN, Chen Q, Denkinger CM, et al. Knowledge and trust of mothers regarding childhood vaccination in Rwanda. BMC Public Health. 2024;24(1):1067. doi:10.1186/s12889-024-18547-1. PMID: 38632541.",
    # -- pessoal de saude e circuito de notificacao
    "gidudu2020": "Gidudu JF, Shaum A, Dodoo A, Bosomprah S, Bonsu G, Amponsa-Achiano K, et al. Barriers to healthcare workers reporting adverse events following immunization in four regions of Ghana. Vaccine. 2020;38(5):1009-1014. doi:10.1016/j.vaccine.2019.11.050. PMID: 31787409.",
    "aborigo2022": "Aborigo RA, Welaga P, Oduro A, Shaum A, Opare J, Dodoo A, et al. Optimising reporting of adverse events following immunisation by healthcare workers in Ghana: A qualitative study in four regions. PLoS One. 2022;17(12):e0277197. doi:10.1371/journal.pone.0277197. PMID: 36538549.",
    "laryea2025": "Laryea S, Blau E, Dodoo A, Addo E, Owusu-Boakye B, Amponsa-Achiano K, et al. Prioritizing interventions to address healthcare worker barriers to reporting adverse events following immunization in Ghana. Vaccine. 2025;60:127324. doi:10.1016/j.vaccine.2025.127324. PMID: 40449279.",
    "omoleke2022": "Omoleke SA, Getachew B, Isyaku A, Aliyu AB, Mustapha AM, Dansanda SM, et al. Understanding and experience of adverse event following immunization (AEFI) and its consequences among healthcare providers in Kebbi State, Nigeria: a qualitative study. BMC Health Serv Res. 2022;22(1):741. doi:10.1186/s12913-022-08133-9. PMID: 35658941.",
    "mehta2026": "Mehta UC, Gomba Y, Salie I, Welte A, Pillay N, Dahlke M, et al. Knowledge, perceptions, and practices of healthcare workers on surveillance of adverse events following maternal immunisation in South Africa. Vaccine. 2026;81:128557. doi:10.1016/j.vaccine.2026.128557. PMID: 41967189.",
    "mehmeti2017": "Mehmeti I, Nelaj E, Simaku A, Tomini E, Bino S. Knowledge, practice and approaches of health professionals to adverse events following immunization and their reporting in Albania. Heliyon. 2017;3(6):e00331. doi:10.1016/j.heliyon.2017.e00331. PMID: 28664193.",
    "erekosima2025": "Erekosima GF, Isiaka SD, Oni F, Garba AR, Bassey O, Asaolu SO, et al. Perception of healthcare administrators on the impediments of optimizing adverse events following immunization e-Reporting in Nigeria. PLoS One. 2025;20(8):e0331093. doi:10.1371/journal.pone.0331093. PMID: 40875746.",
    "byakod2026": "Byakod VR, Deva V, Pandare OS, Bhandari R, Ganachari MS. Knowledge and Perception of Vaccine Pharmacovigilance and Adverse Events Following Immunization Reporting Among Pharmacy Students in India: An Online-Based Cross-Sectional Study. Curr Drug Saf. 2026;21(2):61-67. doi:10.2174/0115748863369626250327083037. PMID: 40304337.",
    # -- sistemas de vigilancia e deteccao activa
    "zvanaka2017": "Zvanaka S, Tsitsi J, Chonzi P, Shambira G, Gombe NT, Tshimanga M. Evaluation of the adverse events following immunizations surveillance system in Harare City, Zimbabwe, 2016: a descriptive cross sectional study. Pan Afr Med J. 2017;28:308. doi:10.11604/pamj.2017.28.308.12730. PMID: 29721138.",
    "constantine2018": "Constantine M, Cremance T, Juru TP, Gerald S, Notion GT, Peter N, et al. Evaluation of the adverse events following immunization surveillance system in Guruve district, Mashonaland Central 2017. Pan Afr Med J. 2018;31:202. doi:10.11604/pamj.2018.31.202.16573. PMID: 31452827.",
    "nyambayo2023": "Nyambayo PPM, Gold MS, Mehta UC, Clarke S, Manyevere R, Chirinda L, et al. Efficacy and feasibility of SMS m-Health for the detection of adverse events following immunisation (AEFIs) in resource-limited setting-The Zimbabwe stimulated telephone assisted rapid safety surveillance (Zm-STARSS) randomised control trial. Vaccine. 2023;41(45):6700-6709. doi:10.1016/j.vaccine.2023.09.037. PMID: 37805357.",
    "cutland2025": "Cutland CL, Gutu K, Yun JA, Izu A, Mahtab S, Peter J, et al. Lessons learnt during establishment of COVID-19 active vaccine safety surveillance in nine African countries. Vaccine. 2025;62:127441. doi:10.1016/j.vaccine.2025.127441. PMID: 40617089.",
    "nambasa2025": "Nambasa VP, Gunter HM, Adeyemo MB, Bhawaneedin NY, Blockman M, Sabblah GT, et al. Empowering African Expertise: Enhancing Safety Data Integration and Signal Detection for COVID-19 Vaccines Through the African Union Smart Safety Surveillance Joint Signal Management Group. Drug Saf. 2025;48(3):233-249. doi:10.1007/s40264-024-01493-7. PMID: 39843797.",
    # -- metodos, instrumentos, estatistica, relato e etica
    "almanasreh2019": "Almanasreh E, Moles R, Chen TF. Evaluation of methods used for estimating content validity. Res Social Adm Pharm. 2019;15(2):214-221. doi:10.1016/j.sapharm.2018.03.066. PMID: 29606610.",
    "taber2018": "Taber KS. The Use of Cronbach's Alpha When Developing and Reporting Research Instruments in Science Education. Res Sci Educ. 2018;48(6):1273-1296. doi:10.1007/s11165-016-9602-2",
    "mchugh2012": "McHugh ML. Interrater reliability: the kappa statistic. Biochem Med (Zagreb). 2012;22(3):276-82. PMID: 23092060.",
    "in2020": "In J, Kang H, Kim JH, Kim TK, Ahn EJ, Lee DK, et al. Tips for troublesome sample-size calculation. Korean J Anesthesiol. 2020;73(2):114-120. doi:10.4097/kja.19497. PMID: 32229812.",
    "chen2018": "Chen W, Qian L, Shi J, Franklin M. Comparing performance between log-binomial and robust Poisson regression models for estimating risk ratios under model misspecification. BMC Med Res Methodol. 2018;18(1):63. doi:10.1186/s12874-018-0519-5. PMID: 29929477.",
    "peduzzi1996": "Peduzzi P, Concato J, Kemper E, Holford TR, Feinstein AR. A simulation study of the number of events per variable in logistic regression analysis. J Clin Epidemiol. 1996;49(12):1373-9. doi:10.1016/s0895-4356(96)00236-3. PMID: 8970487.",
    "zarei2024": "Zarei F, Dehghani A, Ratansiri A, Ghaffari M, Raina SK, Halimi A, et al. ChecKAP: A Checklist for Reporting a Knowledge, Attitude, and Practice (KAP) Study. Asian Pac J Cancer Prev. 2024;25(7):2573-2577. doi:10.31557/APJCP.2024.25.7.2573. PMID: 39068593.",
    "von2007": "von Elm E, Altman DG, Egger M, Pocock SJ, Gøtzsche PC, Vandenbroucke JP. The Strengthening the Reporting of Observational Studies in Epidemiology (STROBE) statement: guidelines for reporting observational studies. Lancet. 2007;370(9596):1453-7. doi:10.1016/S0140-6736(07)61602-X. PMID: 18064739.",
    "world2025": "World Medical Association. World Medical Association Declaration of Helsinki: Ethical Principles for Medical Research Involving Human Participants. JAMA. 2025;333(1):71-74. doi:10.1001/jama.2024.21972. PMID: 39425955.",
}

SEMINAIS = {
    "peduzzi1996": ("Estudo de simulação que fundamenta a regra de pelo menos "
                    "dez eventos por variável nos modelos de regressão para "
                    "desfechos binários."),
    "mchugh2012": ("Artigo de referência sobre a interpretação do kappa de "
                   "Cohen em investigação em saúde, usado na concordância "
                   "entre codificadores e no teste-reteste."),
    "von2007": ("Declaração original STROBE, norma de relato dos estudos "
                "observacionais ainda em vigor."),
}

# ----------------------------------------------------- 1. introducao --------
INTRODUCAO = [
    P("A vacinação é uma das intervenções de saúde pública com melhor relação "
      "entre custo e benefício, mas o seu efeito depende de uma cobertura "
      "elevada e sustentada. Em 2025, a cobertura mundial com a terceira dose "
      "da vacina contra a difteria, o tétano e a tosse convulsa manteve-se em "
      "85%, e 13,5 milhões de crianças não receberam nenhuma dose de qualquer "
      "vacina, a que se somam cerca de 6 milhões parcialmente vacinadas "
      "{omscobertura2026}. Ao contrário da maioria dos medicamentos, as "
      "vacinas são administradas a pessoas saudáveis, sobretudo a lactentes, "
      "o que torna a tolerância social ao risco muito menor e faz da "
      "vigilância da segurança uma condição do próprio programa. A "
      "Organização Mundial da Saúde (OMS) define evento supostamente "
      "atribuível à vacinação ou imunização (ESAVI) como qualquer ocorrência "
      "médica indesejável que surge depois da imunização e que não tem "
      "necessariamente uma relação causal com a vacina, podendo consistir num "
      "sinal desfavorável, num achado laboratorial anormal, num sintoma ou "
      "numa doença {omscausalidade2021}."),
    P("A classificação da OMS distingue cinco categorias de ESAVI segundo a "
      "causa: reacção relacionada com o produto vacinal, reacção relacionada "
      "com um defeito de qualidade do produto, reacção relacionada com um "
      "erro de imunização, resposta relacionada com o *stress* da imunização "
      "e evento coincidente {gold2020}. Esta distinção tem consequências "
      "práticas imediatas, porque só a investigação de cada caso permite "
      "separar a reacção esperada e transitória da falha de conservação ou de "
      "técnica que pode ser corrigida, e da doença que teria acontecido de "
      "qualquer modo. O manual global de vigilância da OMS organiza esse "
      "trabalho em notificação, investigação, análise, classificação de "
      "causalidade e comunicação {omsvigilancia2016}, e o plano global para a "
      "segurança das vacinas recomenda que os países integrem a vigilância "
      "das vacinas nos sistemas nacionais de farmacovigilância em vez de "
      "criarem estruturas paralelas {omsblueprint2022}."),
    P("Nos países de rendimento baixo e médio, a etapa que falha com mais "
      "frequência é a primeira. Num inquérito a 306 profissionais de saúde de "
      "quatro regiões do Gana, 57,5% já tinham encontrado um ESAVI, mas "
      "apenas 55,0% dos que o encontraram no último ano o comunicaram e "
      "somente 31,7% preencheram a ficha de notificação; nesse país, a razão "
      "de notificação era de 1,56 por 100.000 lactentes sobreviventes, muito "
      "abaixo do mínimo de 10 recomendado {gidudu2020}. No distrito de Guruve, "
      "no Zimbabwe, 39% dos cuidadores tinham tido filhos com um evento "
      "pós-vacinal e 45% dos profissionais tinham encontrado ESAVI, mas "
      "nenhum caso foi notificado, por receio de consequências pessoais entre "
      "os profissionais e por os cuidadores considerarem o evento pouco grave "
      "{constantine2018}. Na cidade de Harare, onde o conhecimento dos "
      "profissionais era elevado, os motivos apontados para a subnotificação "
      "foram a ausência de retorno de informação (47,1%), o receio de "
      "represálias (31,4%) e a sobrecarga de trabalho (21,6%) {zvanaka2017}."),
    P("A cadeia de notificação começa, porém, fora da unidade sanitária. "
      "Quem observa a febre, a tumefacção no local da injecção ou o choro "
      "persistente é a mãe ou o cuidador, em casa, nas horas seguintes à "
      "consulta. Num estudo com 388 cuidadores no Uganda, um terço (33,5%) "
      "referiu que o filho tinha sofrido um evento pós-vacinal e o comunicou "
      "à unidade sanitária, e a probabilidade de comunicar aumentou com a "
      "escolaridade, com razão de possibilidades ajustada de 3,56 para o "
      "ensino secundário e de 8,52 para o ensino superior {watyaba2025}. Em "
      "grupos focais com mães do Norte do Gana, a ausência de resposta dos "
      "profissionais depois da comunicação de um evento, a ideia de que os "
      "eventos são banais e a informação insuficiente sobre o que esperar "
      "depois da vacina explicavam a não comunicação, e o medo de eventos "
      "graves chegava a afastar as famílias da vacinação {ansah2025}."),
    P("Em Moçambique, o Programa Alargado de Vacinação (PAV) foi implantado "
      "em 1979 e permitiu reduzir a mortalidade e a morbilidade infantis "
      "{cassocera2020}. O calendário nacional inclui a vacina contra a "
      "tuberculose (BCG), a vacina oral contra a poliomielite (OPV) e a "
      "vacina inactivada contra a poliomielite (IPV), a vacina pentavalente "
      "contra difteria, tosse convulsa, tétano, hepatite B e *Haemophilus "
      "influenzae* tipo b (DPT-HepB-Hib), a vacina antipneumocócica conjugada "
      "(PCV), a vacina contra o rotavírus e a vacina contra o sarampo e a "
      "rubéola (MR) {ine2024ids}. O desempenho recente é preocupante: a "
      "proporção de crianças de 12 a 23 meses completamente vacinadas com os "
      "antigénios básicos subiu de 47% em 1997 para 66% em 2015 e caiu para "
      "38% em 2022 e 2023, enquanto a proporção de crianças sem qualquer "
      "vacina, que tinha descido de 20% para 5%, voltou a subir para 14% "
      "{cassocera2023,ine2024ids}."),
    P("Nampula é a província mais populosa do país, com 5.758.920 habitantes "
      "no recenseamento de 2017 {ine2021}, e uma das que apresenta pior "
      "cobertura vacinal: 25% das crianças de 12 a 23 meses estavam "
      "completamente vacinadas com os antigénios básicos, valor apenas "
      "superior ao da Zambézia (13%) e muito distante de Inhambane e da "
      "Cidade de Maputo (77% cada) {ine2024ids}. A experiência local de "
      "vigilância da segurança das vacinas resume-se à campanha de vacinação "
      "oral contra a cólera de 2016 na cidade de Nampula, em que 10% das 451 "
      "pessoas vacinadas inquiridas referiram queixas ligeiras e "
      "inespecíficas e 17,3% declararam não ter recebido qualquer informação "
      "antes da campanha {sema2018}, acompanhada de uma avaliação passiva dos "
      "eventos pós-vacinais nos centros de saúde da mesma cidade "
      "{rafael2017}."),
    P("A pesquisa bibliográfica feita para este protocolo não encontrou "
      "nenhum estudo que descreva o que as mães e os cuidadores de Nampula "
      "sabem sobre os eventos esperados depois das vacinas do calendário "
      "infantil, o que fazem quando esses eventos surgem e por que via essa "
      "informação chega, ou não chega, ao sistema de notificação. Também não "
      "foi encontrada informação sobre o conhecimento do pessoal de "
      "enfermagem das consultas de vacinação quanto às definições e ao "
      "circuito de notificação. O presente estudo procura preencher essa "
      "lacuna, avaliando o conhecimento e as práticas das mães e dos "
      "cuidadores nas consultas de vacinação de centros de saúde da cidade de "
      "Nampula e descrevendo, como componente complementar, o conhecimento e "
      "as práticas declaradas do pessoal de enfermagem que aí trabalha."),
]

# ----------------------------------------------------- 2. problema ----------
PROBLEMA = [
    P("Nos centros de saúde da cidade de Nampula, as consultas de vacinação "
      "atendem diariamente dezenas de crianças. O contacto entre o "
      "profissional e a mãe é curto e concentra-se na administração das doses "
      "e no registo no cartão de saúde; a informação sobre o que pode "
      "acontecer nas horas seguintes, sobre o que é normal e sobre o que "
      "obriga a voltar à unidade sanitária depende do tempo disponível e da "
      "iniciativa de cada profissional. Quando a criança tem febre ou uma "
      "tumefacção no braço nessa noite, a decisão de regressar, de recorrer a "
      "um tratamento caseiro ou de nada fazer cabe inteiramente à família. "
      "Nenhuma dessas decisões é registada, pelo que o sistema de vigilância "
      "só vê os casos que voltam espontaneamente e que o profissional "
      "reconhece e regista."),
    P("A consequência tem duas faces. Do lado da segurança, os eventos que "
      "não chegam ao serviço não são investigados nem classificados quanto à "
      "causalidade, e por isso um erro de imunização repetido, um problema de "
      "conservação num lote ou um agrupamento de casos numa sessão podem "
      "passar despercebidos durante meses {omsvigilancia2016}. A "
      "subnotificação documentada em países vizinhos mostra que este não é um "
      "risco teórico: em Guruve nenhum dos eventos observados por cuidadores "
      "e profissionais foi notificado {constantine2018}. Do lado da "
      "confiança, uma mãe que não foi avisada de que a febre é esperada e "
      "que não obtém explicação quando volta tende a interpretar o episódio "
      "como prova de que a vacina fez mal à criança. Em Zambézia, a "
      "preocupação com os efeitos secundários foi um dos quatro padrões de "
      "barreiras que conduziam ao abandono do calendário vacinal "
      "{powelson2022}, e em Nampula a cobertura completa é de apenas 25% "
      "{ine2024ids}."),
    P("O problema tem ainda uma dimensão de sistema. O Regulamento do Sistema "
      "Nacional de Farmacovigilância (SNF) abrange expressamente as vacinas e "
      "assenta na notificação espontânea de suspeitas de reacção adversa "
      "pelos profissionais de saúde e pelos próprios doentes {snf2023}. Na "
      "prática, a mãe não é destinatária de nenhuma mensagem sobre este "
      "direito, e o profissional de enfermagem das consultas de vacinação "
      "acumula a administração das vacinas, o registo, a educação para a "
      "saúde e a notificação, sem que se saiba se conhece as definições, os "
      "prazos e a ficha a usar. Estudos africanos mostram que o conhecimento "
      "dos profissionais sobre a definição e a classificação dos eventos é "
      "frequentemente insuficiente {omoleke2022} e que a incerteza sobre se "
      "um evento é ou não notificável é a principal barreira declarada "
      "{mehta2026}."),
    P("Falta, por isso, saber qual é o nível de conhecimento das mães e dos "
      "cuidadores de Nampula sobre os eventos esperados depois das vacinas, "
      "sobre os sinais que exigem regresso imediato à unidade sanitária e "
      "sobre a possibilidade de comunicar esses eventos; que proporção "
      "relatou um evento na criança e o que fez nessa altura; que factores se "
      "associam ao conhecimento e à comunicação; e o que o pessoal de "
      "enfermagem sabe e declara fazer. Sem esta informação, qualquer acção "
      "de melhoria da vigilância na cidade continuará a ser desenhada a "
      "partir de dados de outros países."),
]
PERGUNTA = ("Qual é o nível de conhecimento das mães e cuidadores que "
            "frequentam as consultas de vacinação de centros de saúde da "
            "cidade de Nampula sobre os eventos supostamente atribuíveis à "
            "vacinação ou imunização e sobre o circuito de notificação, que "
            "práticas adoptam quando esses eventos ocorrem na criança e que "
            "factores se associam a esse conhecimento e a essas práticas?")
DELIMITACAO = [
    P("O estudo decorre na cidade de Nampula, em seis centros de saúde "
      "urbanos com consulta diária de vacinação, seleccionados a partir da "
      "lista de unidades sanitárias do Serviço Distrital de Saúde, Mulher e "
      "Acção Social (SDSMAS) da Cidade de Nampula [confirmar junto do SDSMAS "
      "da Cidade de Nampula a lista de unidades com consulta diária de "
      "vacinação e o volume mensal de atendimentos]. A população principal é "
      "constituída pelas mães e pelos cuidadores que levam crianças com menos "
      "de 24 meses a essas consultas durante o período de recolha, em Março e "
      "Abril de 2027. A população secundária é o pessoal de enfermagem e os "
      "agentes de medicina preventiva afectos às consultas de vacinação "
      "dessas mesmas unidades."),
    P("O objecto do estudo é o conhecimento sobre os eventos que ocorrem "
      "depois da vacinação de rotina do calendário infantil, os sinais de "
      "alarme, as práticas adoptadas pela família quando esses eventos "
      "surgem e o circuito de comunicação e notificação. Ficam fora do "
      "estudo a verificação clínica dos eventos relatados, a atribuição de "
      "causalidade a qualquer caso concreto, a avaliação da qualidade da "
      "cadeia de frio e dos lotes de vacina, a medição da cobertura vacinal "
      "da cidade, as vacinas administradas em campanhas de massa e a "
      "vacinação de adultos e de grávidas. Fica igualmente fora a auditoria "
      "das fichas de notificação arquivadas, porque o estudo mede o que as "
      "pessoas sabem e declaram, não o desempenho documental do sistema."),
]

# ----------------------------------------------------- 3. objectivos --------
OBJECTIVO_GERAL = (
    "Avaliar o conhecimento das mães e cuidadores sobre os eventos "
    "supostamente atribuíveis à vacinação ou imunização e as suas práticas de "
    "comunicação desses eventos, e descrever o conhecimento e as práticas "
    "declaradas do pessoal de enfermagem das consultas de vacinação, em "
    "centros de saúde da cidade de Nampula, em 2027.")
OBJECTIVOS_ESPECIFICOS = [
    "Caracterizar as mães e cuidadores que frequentam as consultas de "
    "vacinação quanto aos factores sociodemográficos, ao historial vacinal da "
    "criança e à informação recebida no serviço sobre os eventos esperados "
    "depois da vacina.",
    "Determinar o nível de conhecimento das mães e cuidadores sobre os "
    "eventos esperados depois da vacinação, sobre os sinais de alarme que "
    "exigem regresso imediato à unidade sanitária e sobre a possibilidade de "
    "comunicar o evento ao serviço.",
    "Estimar a proporção de mães e cuidadores que relatam um evento "
    "pós-vacinal na criança nos doze meses anteriores e descrever as práticas "
    "adoptadas, incluindo a comunicação do evento à unidade sanitária, o uso "
    "de medicamentos e o recurso a tratamentos caseiros ou tradicionais.",
    "Analisar a associação entre o nível de conhecimento, os factores "
    "sociodemográficos e a informação recebida no serviço, por um lado, e a "
    "comunicação do evento pós-vacinal à unidade sanitária, por outro.",
    "Descrever o conhecimento do pessoal de enfermagem afecto às consultas de "
    "vacinação sobre as definições, a classificação e o circuito de "
    "notificação dos eventos pós-vacinais, e as suas práticas declaradas de "
    "aconselhamento às mães e de preenchimento da ficha de notificação.",
]

# ----------------------------------------------------- 4. hipoteses ---------
HIPOTESES_INTRO = [
    P("As hipóteses referem-se à componente analítica do estudo, isto é, ao "
      "objectivo específico 4. São bilaterais e testadas ao nível de "
      "significância de 5%. Os objectivos específicos 1, 2, 3 e 5 são "
      "descritivos e dão origem às questões de investigação apresentadas a "
      "seguir às hipóteses."),
]
HIPOTESES = [
    ("H0 (objectivo específico 4, conhecimento)",
     "a proporção de mães e cuidadores que comunicaram à unidade sanitária o "
     "evento pós-vacinal observado na criança não difere entre os que têm "
     "conhecimento bom e os que têm conhecimento moderado ou fraco sobre os "
     "eventos pós-vacinais."),
    ("H1 (objectivo específico 4, conhecimento)",
     "a proporção de mães e cuidadores que comunicaram à unidade sanitária o "
     "evento pós-vacinal observado na criança difere entre os que têm "
     "conhecimento bom e os que têm conhecimento moderado ou fraco sobre os "
     "eventos pós-vacinais."),
    ("H0 (objectivo específico 4, informação recebida)",
     "ter recebido no serviço informação sobre os eventos esperados depois da "
     "vacina não se associa à comunicação do evento à unidade sanitária."),
    ("H1 (objectivo específico 4, informação recebida)",
     "ter recebido no serviço informação sobre os eventos esperados depois da "
     "vacina associa-se à comunicação do evento à unidade sanitária."),
    ("H0 (objectivo específico 4, modelo ajustado)",
     "a escolaridade, a idade, a residência, o número de filhos, a distância "
     "até à unidade sanitária, a informação recebida e o nível de "
     "conhecimento não se associam à comunicação do evento pós-vacinal, "
     "depois de ajustamento mútuo."),
    ("H1 (objectivo específico 4, modelo ajustado)",
     "pelo menos um destes factores associa-se à comunicação do evento "
     "pós-vacinal, depois de ajustamento mútuo."),
]
QUESTOES = [
    "Que características sociodemográficas, que historial vacinal da criança "
    "e que informação recebida no serviço caracterizam as mães e cuidadores "
    "que frequentam as consultas de vacinação na cidade de Nampula?",
    "Que proporção destas mães e cuidadores tem conhecimento bom, moderado ou "
    "fraco sobre os eventos esperados depois da vacinação, sobre os sinais de "
    "alarme e sobre a possibilidade de comunicar o evento ao serviço?",
    "Que proporção relata um evento pós-vacinal na criança nos doze meses "
    "anteriores, que eventos são esses e que práticas foram adoptadas pela "
    "família, incluindo a comunicação ao serviço e o recurso a medicamentos "
    "ou a tratamentos caseiros?",
    "Que conhecimento tem o pessoal de enfermagem das consultas de vacinação "
    "sobre as definições, a classificação e o circuito de notificação dos "
    "eventos pós-vacinais, e que práticas declara quanto ao aconselhamento "
    "das mães e ao preenchimento da ficha de notificação?",
]

# ----------------------------------------------------- 5. justificativa -----
JUSTIFICATIVA_INTRO = [
    P("O estudo justifica-se por três razões convergentes: a vigilância dos "
      "eventos pós-vacinais depende, na sua primeira etapa, de pessoas que "
      "não são profissionais de saúde e cujo conhecimento nunca foi medido em "
      "Nampula; a cobertura vacinal da província é das mais baixas do país e "
      "a preocupação com os efeitos secundários é um dos motivos de abandono "
      "documentados em Moçambique {ine2024ids,powelson2022}; e o "
      "enquadramento legal moçambicano já prevê a notificação de suspeitas de "
      "reacção adversa a vacinas por profissionais e por utentes, sem que "
      "exista informação sobre o funcionamento real desse circuito {snf2023}. "
      "As relevâncias científica, académica, social e política são "
      "desenvolvidas a seguir."),
]
JUSTIFICATIVA = {
    "cientifica": [
        P("O estudo produz a primeira medida do conhecimento das mães e "
          "cuidadores moçambicanos sobre os eventos supostamente atribuíveis "
          "à vacinação e das práticas que adoptam quando esses eventos "
          "ocorrem. A evidência africana disponível vem sobretudo do Gana, do "
          "Uganda, do Zimbabwe e da Nigéria, é maioritariamente qualitativa "
          "ou centrada nos profissionais {ansah2025,omoleke2022,gidudu2020}, "
          "e o único estudo que inquiriu simultaneamente cuidadores e "
          "profissionais foi feito num hospital de Kampala {watyaba2025}. A "
          "evidência moçambicana sobre segurança vacinal limita-se à "
          "campanha de vacinação oral contra a cólera na cidade de Nampula "
          "{sema2018,rafael2017} e não abrange a vacinação de rotina."),
        P("O desenho acrescenta ainda valor metodológico. O instrumento é "
          "adaptado de questionários publicados, traduzido e retrovertido "
          "para emakhuwa, submetido a validação de conteúdo por peritos e a "
          "pré-teste com estimativa de fiabilidade, o que produz uma "
          "ferramenta reutilizável em Moçambique para medir o conhecimento "
          "sobre eventos pós-vacinais em populações com baixa escolaridade. "
          "A medição em simultâneo dos dois lados do balcão, a mãe e o "
          "profissional de enfermagem, permite confrontar o que é dito no "
          "aconselhamento com o que é recordado pela família."),
    ],
    "academica": [
        P("Para a Faculdade de Ciências de Saúde (FCS) da Universidade Lúrio "
          "(UniLúrio), o protocolo constitui um exercício completo de "
          "farmacovigilância aplicada, área em que a formação em Farmácia "
          "tem de intervir para além do medicamento dispensado ao balcão. Os "
          "resultados servem de base para incluir nos conteúdos de "
          "farmacovigilância e de saúde pública a vigilância específica das "
          "vacinas, as definições de caso e a classificação de causalidade, "
          "matéria em que a literatura mostra lacunas mesmo entre estudantes "
          "de Farmácia {byakod2026}. Para os serviços de saúde da cidade, o "
          "relatório final funciona como diagnóstico de necessidades de "
          "formação do pessoal de enfermagem das consultas de vacinação."),
    ],
    "social": [
        P("A mãe que sabe o que esperar depois de uma vacina trata melhor a "
          "criança em casa, distingue a febre transitória do sinal que exige "
          "regresso imediato ao serviço e não abandona o calendário vacinal "
          "por causa de um episódio que interpretou mal. Os relatos de mães "
          "do Norte do Gana mostram que a falta de explicação sobre os "
          "eventos e a ausência de resposta quando o evento é comunicado "
          "afastam as famílias da vacinação {ansah2025}, e em Zambézia a "
          "preocupação com os efeitos secundários foi identificada como "
          "barreira directa à conclusão do calendário {powelson2022}. Todas "
          "as participantes deste estudo recebem, no fim da entrevista, um "
          "folheto ilustrado com os eventos esperados, os cuidados em casa, "
          "os sinais de alarme e o convite explícito a comunicar qualquer "
          "ocorrência ao serviço, pelo que o estudo devolve um benefício "
          "imediato à população inquirida."),
        P("O estudo tem também um efeito sobre a equidade. As mães com menos "
          "escolaridade são as que menos comunicam os eventos "
          "{watyaba2025} e são, em Nampula, a maioria. Identificar os grupos "
          "em que o conhecimento é mais fraco permite dirigir a educação para "
          "a saúde a quem dela mais precisa, em emakhuwa e com materiais que "
          "não dependam da leitura."),
    ],
    "politica": [
        P("A Lei n.º 12/2017 abrange expressamente as vacinas e os produtos "
          "biológicos para uso humano {lei12de2017} e o Regulamento do SNF, "
          "aprovado em 2023, determina que o sistema assenta na notificação "
          "espontânea de suspeitas de reacção adversa a medicamentos e "
          "vacinas pelos profissionais de saúde e pelos doentes, e atribui ao "
          "Centro Nacional de Farmacovigilância da Autoridade Nacional "
          "Reguladora de Medicamento (ANARME) a recolha e a avaliação dessas "
          "notificações {snf2023}. Os resultados deste estudo indicam onde "
          "esse circuito se interrompe do lado do utente e do lado do "
          "profissional de primeira linha, informação directamente "
          "utilizável pela ANARME e pelo Ministério da Saúde (MISAU)."),
        P("À escala regional, a OMS recomenda que a segurança das vacinas "
          "seja monitorizada dentro dos sistemas nacionais de "
          "farmacovigilância {omsblueprint2022}, e a experiência recente de "
          "vigilância activa em países africanos mostrou que os sistemas "
          "existentes precisam de investimento continuado para detectar "
          "sinais {cutland2025,nambasa2025}. Um diagnóstico local do "
          "conhecimento e das práticas é o primeiro passo barato e realista "
          "para melhorar a sensibilidade do sistema em Nampula, e pode "
          "orientar decisões sobre mensagens padronizadas no aconselhamento "
          "pós-vacinal e sobre a simplificação da ficha de notificação, "
          "medidas propostas noutros contextos africanos "
          "{aborigo2022,laryea2025}."),
    ],
}

# ----------------------------------------------------- 6. revisao -----------
REVISAO = [
    ("Conceito, classificação e definição operacional dos eventos "
     "pós-vacinais", [
        P("A OMS define evento supostamente atribuível à vacinação ou "
          "imunização como qualquer ocorrência médica indesejável que surge "
          "depois da imunização e que não tem necessariamente uma relação "
          "causal com o uso da vacina; o evento pode consistir num sinal "
          "desfavorável ou não intencional, num achado laboratorial anormal, "
          "num sintoma ou numa doença {omscausalidade2021}. A definição é "
          "deliberadamente ampla, porque a vigilância tem de recolher "
          "primeiro e julgar depois: a decisão sobre a causa é tomada no fim, "
          "por um processo formal de avaliação de causalidade, e não pelo "
          "profissional que recebe o caso."),
        P("A classificação por causa distingue cinco categorias: a reacção "
          "relacionada com o produto vacinal, provocada por uma propriedade "
          "inerente à vacina; a reacção relacionada com um defeito de "
          "qualidade do produto, incluindo o dispositivo de administração; a "
          "reacção relacionada com um erro de imunização, causada por "
          "manuseamento, prescrição ou administração incorrectos e, por "
          "isso, evitável; a resposta relacionada com o *stress* da "
          "imunização, que substituiu a antiga designação de reacção de "
          "ansiedade e abrange as manifestações desencadeadas pela própria "
          "situação de vacinação; e o evento coincidente, causado por algo "
          "que não a vacina, o erro ou o *stress*, mas associado no tempo à "
          "imunização {gold2020}. Esta grelha foi definida pelo grupo de "
          "trabalho do Conselho das Organizações Internacionais de Ciências "
          "Médicas e da OMS e é a base da avaliação de causalidade "
          "{omscausalidade2021}."),
        P("A avaliação de causalidade da OMS, na versão revista, conduz a "
          "quatro resultados possíveis: associação causal consistente com a "
          "imunização, associação causal inconsistente com a imunização, "
          "resultado indeterminado e caso não classificável "
          "{omscausalidade2021,puliyel2018}. Uma crítica publicada a esta "
          "classificação assinala que a exigência de evidência prévia "
          "publicada dificulta o reconhecimento de um evento novo como "
          "relacionado com a vacina e que a definição restritiva de "
          "associação causal, que exclui os casos em que intervém outro "
          "factor, pode deixar de fora reacções ocorridas em crianças com "
          "doença prévia {puliyel2018}; a controvérsia reforça a importância "
          "de recolher e investigar bem cada caso antes de qualquer juízo. "
          "Do ponto de vista da gravidade, o evento "
          "é considerado grave quando provoca a morte, põe a vida em perigo, "
          "exige internamento ou o prolonga, causa incapacidade persistente "
          "ou uma anomalia congénita, distinção que não se confunde com a "
          "intensidade do sintoma {omsvigilancia2016}."),
        P("Neste estudo, e para efeitos de recolha, considera-se evento "
          "pós-vacinal qualquer alteração de saúde observada pela mãe ou pelo "
          "cuidador na criança nos sete dias seguintes à administração de uma "
          "vacina do calendário infantil, independentemente de ter sido "
          "confirmada por um profissional e independentemente da causa. O "
          "estudo não atribui causalidade a nenhum caso, apenas regista o que "
          "foi observado e o que foi feito, e classifica os relatos em "
          "eventos ligeiros esperados (febre, dor, rubor ou tumefacção no "
          "local da injecção, irritabilidade, perda de apetite) e em sinais "
          "de alarme (convulsão, choro persistente por mais de três horas, "
          "abcesso ou secreção no local da injecção, dificuldade "
          "respiratória, inchaço da face, perda de consciência e febre alta "
          "que não cede), segundo a lista de eventos do manual global de "
          "vigilância {omsvigilancia2016}."),
    ]),
    ("Frequência dos eventos pós-vacinais e subnotificação", [
        P("Os eventos ligeiros são a regra e os graves são raros, mas a "
          "frequência medida depende inteiramente do método de detecção. Na "
          "avaliação do sistema de vigilância do distrito de Guruve, a "
          "frequência dos eventos pós-vacinais foi situada entre 13% e 34% "
          "das crianças vacinadas, e 39% dos cuidadores entrevistados "
          "referiram que o filho tinha sofrido um evento; ainda assim, entre "
          "Janeiro de 2016 e meados de 2017 nenhum caso foi notificado no "
          "distrito {constantine2018}. Na campanha de vacinação oral contra a "
          "cólera da cidade de Nampula, 10% das 451 pessoas vacinadas "
          "inquiridas relataram queixas ligeiras e inespecíficas {sema2018}, "
          "valor que reflecte uma recolha activa domiciliária e não a "
          "capacidade do sistema de rotina."),
        P("A diferença entre o que acontece e o que é notificado é o problema "
          "central da vigilância passiva. No Gana, a razão de notificação de "
          "1,56 por 100.000 lactentes sobreviventes contrastava com o mínimo "
          "de 10 usado como indicador global, e apenas 31,7% dos "
          "profissionais que tinham encontrado um evento no último ano "
          "chegaram a preencher a ficha {gidudu2020}. O ensaio aleatorizado "
          "conduzido no Zimbabwe com 4.560 participantes ilustra bem o "
          "fenómeno: o grupo submetido a mensagens de texto seguidas de "
          "entrevista telefónica gerou uma taxa de detecção de eventos com "
          "procura de cuidados de 2%, enquanto no grupo de vigilância passiva "
          "não foi notificado nenhum evento {nyambayo2023}."),
        P("A vigilância activa é possível em contextos de recursos "
          "limitados, mas é exigente. A implantação de vigilância activa da "
          "segurança das vacinas contra a doença por coronavírus em nove "
          "países africanos mostrou que a criação de locais sentinela é "
          "exequível, embora a ausência de registos clínicos electrónicos "
          "limite o acesso e a disponibilidade dos dados, e concluiu que as "
          "autoridades reguladoras e os programas de imunização têm de "
          "financiar de forma continuada estes sistemas {cutland2025}. A "
          "experiência do grupo conjunto de gestão de sinais da União "
          "Africana confirma que a capacidade de detecção de sinais na "
          "região depende da integração e da partilha de dados entre "
          "autoridades nacionais {nambasa2025}. Enquanto essa capacidade não "
          "existir de forma sistemática, a notificação espontânea, "
          "alimentada por quem observa o evento, continua a ser a principal "
          "fonte."),
    ]),
    ("Conhecimento e práticas das mães e cuidadores", [
        P("O estudo de Kampala é, até à data, o que mais se aproxima do "
          "desenho aqui proposto. Envolveu 388 entrevistas presenciais a "
          "cuidadores que acompanhavam as crianças às consultas de vacinação "
          "de rotina, três grupos focais e oito entrevistas a profissionais. "
          "Cerca de um terço dos cuidadores (130, 33,5%) declarou que o filho "
          "tinha tido um evento pós-vacinal e que o comunicou à unidade "
          "sanitária. Na análise ajustada, a comunicação associou-se ao "
          "ensino secundário (razão de possibilidades ajustada, ORa, de 3,56; "
          "IC 95% 1,12-11,30), ao ensino superior (ORa 8,52; IC 95% "
          "2,09-34,81), a ter mais de 35 anos (ORa 18,77; IC 95% "
          "2,34-150,60) e a não ser casado (ORa 3,27; IC 95% 1,51-7,12). Os "
          "profissionais, apesar de bom conhecimento geral, desconheciam o "
          "sistema nacional de notificação {watyaba2025}."),
        P("A investigação qualitativa acrescenta as razões. Em dez grupos "
          "focais com mães de cinco regiões do Norte do Gana, as "
          "participantes compreendiam a necessidade da vacinação, mas "
          "algumas desconheciam que doenças as vacinas previnem, "
          "preocupavam-se com a dor e o desconforto da criança e "
          "justificavam a não comunicação dos eventos com a ausência de "
          "resposta dos profissionais depois de comunicações anteriores, com "
          "a ideia de que os eventos são banais e com experiências "
          "anteriores de vacinação; o receio de eventos graves, como a "
          "paralisia, associado à explicação insuficiente dos benefícios, "
          "podia levar os pais a não autorizar a vacinação {ansah2025}. No "
          "meio rural do Uganda, as preocupações com eventos pós-vacinais "
          "expressas pelas grávidas e pelos maridos, a par de ideias erradas "
          "sobre a finalidade das vacinas, condicionavam a aceitação da "
          "imunização materna, e a decisão de procurar cuidados dependia "
          "largamente do marido {kajungu2020}."),
        P("Os estudos de conhecimentos, atitudes e práticas sobre vacinação "
          "infantil dão o pano de fundo. Em Accra, num inquérito a 120 "
          "cuidadores de crianças de 12 a 23 meses, 53,3% tinham cumprido "
          "integralmente o calendário e o principal factor associado à "
          "vacinação incompleta foi o conhecimento materno insuficiente "
          "(58%), seguido da falta de tempo (25,8%) e do esquecimento "
          "(17,5%) {danso2023}. No Ruanda, um inquérito a 2.126 pais "
          "encontrou proporções muito altas de bom conhecimento (95,5%) e de "
          "boa confiança (91,4%) na vacinação infantil, com os profissionais "
          "de saúde (91,8%) e os meios de comunicação de massas (28,9%) como "
          "principais fontes de informação {mbonigaba2024}. Esta variação "
          "entre países mostra que os resultados de um contexto não se "
          "transpõem para outro e reforça a necessidade de medir localmente."),
        P("Em Moçambique, a evidência disponível é indirecta mas convergente. "
          "O estudo participativo conduzido nos distritos de Namarroi e Gilé, "
          "na província da Zambézia, onde cerca de 19% das crianças com menos "
          "de dois anos começam mas não completam o calendário, identificou "
          "quatro padrões de barreiras ao abandono: normas sociais que fazem "
          "recair a responsabilidade da vacinação sobre a mãe, percepção de "
          "má qualidade dos serviços que reduz a confiança, preocupação com "
          "os efeitos secundários e hesitação das cuidadoras em procurar e "
          "reivindicar a vacinação por causa do desequilíbrio de poder face "
          "aos profissionais {powelson2022}. O projecto de intervenção "
          "comunitária em curso em Moçambique e no Malawi parte do mesmo "
          "diagnóstico, ao propor o diálogo comunitário como via para "
          "aumentar a cobertura {shuro2024}."),
    ]),
    ("O profissional de saúde e o circuito de notificação", [
        P("O conhecimento dos profissionais sobre as definições é desigual. "
          "Num estudo qualitativo com 28 profissionais do estado de Kebbi, no "
          "Noroeste da Nigéria, o nível de conhecimento sobre a definição e a "
          "classificação dos eventos era variável e subóptimo, e o erro "
          "durante a vacinação foi a causa mais frequentemente apontada; os "
          "eventos relatados na experiência profissional eram o choro "
          "persistente, a febre, o desmaio e a tumefacção e dor no local da "
          "injecção, e as consequências descritas incluíam a recusa colectiva "
          "da vacinação, a queda da adesão, a perda de confiança no programa "
          "e até agressões aos vacinadores {omoleke2022}. Em Tirana, num "
          "inquérito a 102 profissionais com um questionário estruturado de "
          "68 perguntas, o conhecimento sobre a vigilância era globalmente "
          "fraco, sobretudo quanto ao papel dos diferentes intervenientes; "
          "70,5% tinham encontrado um evento na sua prática e 68,6% nunca "
          "tinham recebido formação sobre o tema {mehmeti2017}."),
        P("As barreiras à notificação repetem-se de país para país. No Gana, "
          "os motivos mais frequentes foram o receio de consequências "
          "pessoais (44,1%), a falta de conhecimento ou de formação (25,2%) e "
          "a convicção de que o evento não era suficientemente grave (22,2%); "
          "a discussão do tema na última visita de supervisão associou-se "
          "fortemente à notificação no ano anterior (OR 7,39; p<0,001) "
          "{gidudu2020}. As 116 entrevistas a informantes-chave conduzidas "
          "nas mesmas regiões acrescentaram a falta de informação sobre quais "
          "os eventos notificáveis e sobre as estruturas de notificação, a "
          "sobrecarga de trabalho, o custo de notificar, o receio de "
          "censura pelos supervisores, a falta de motivação e a ausência de "
          "retorno de informação {aborigo2022}. Em 2021, os intervenientes "
          "ganeses seleccionaram quatro estratégias para responder a estas "
          "barreiras, entre elas um conjunto de instrumentos e um auxiliar de "
          "trabalho para a notificação, uma política de protecção do "
          "profissional e um módulo de formação para os recém-admitidos "
          "{laryea2025}."),
        P("Estudos mais recentes mostram que o problema persiste mesmo em "
          "sistemas mais estruturados. Num inquérito electrónico a 361 "
          "médicos e enfermeiros de 35 unidades públicas de sete províncias "
          "da África do Sul, 59,7% demonstraram conhecimento moderado, mas "
          "apenas 25,8% reconheciam que nem todos os eventos são evitáveis e "
          "apenas 28,8% identificavam correctamente os eventos graves; 31% "
          "tinham encontrado um evento, mas só 19,7% alguma vez notificaram, "
          "e a principal barreira declarada foi a incerteza sobre se o evento "
          "estava ou não relacionado com a vacina ou com a imunização "
          "{mehta2026}. Na Nigéria, a análise das barreiras à notificação "
          "electrónica identificou a insuficiência de conhecimento e o medo "
          "dos profissionais, as limitações de infra-estrutura técnica, a "
          "fragilidade dos sistemas de notificação e a inconstância do "
          "compromisso governamental {erekosima2025}."),
        P("A formação inicial é parte do problema. Num inquérito a estudantes "
          "de Farmácia da Índia, 82,7% nunca tinham notificado um evento "
          "pós-vacinal, metade afirmou que a farmacovigilância das vacinas "
          "não estava coberta no plano de estudos e 66,3% declararam não ter "
          "sido treinados para notificar, ainda que 96,9% considerassem que "
          "os farmacêuticos devem participar nessa notificação "
          "{byakod2026}. Esta observação é directamente pertinente para um "
          "trabalho de culminação do curso de Farmácia, porque situa a "
          "farmacovigilância das vacinas como competência a desenvolver na "
          "formação e não apenas como atribuição do programa de imunização."),
    ]),
    ("Enquadramento normativo e programático em Moçambique", [
        P("A Lei n.º 12/2017, de 8 de Setembro, é a lei do medicamento, "
          "vacinas e outros produtos biológicos para uso humano e criou a "
          "ANARME, com funções de regulação, supervisão e fiscalização "
          "{lei12de2017}. Em 2023, o Diploma Ministerial n.º 3/2023, de 4 de "
          "Janeiro, aprovou o Regulamento do SNF, que revogou o regulamento "
          "de 2010. O regulamento aplica-se à monitorização das reacções "
          "adversas e dos problemas relacionados com medicamentos, vacinas, "
          "produtos biológicos e de saúde para uso humano, bem como a todos "
          "os profissionais de saúde, e determina que o sistema assenta "
          "essencialmente na notificação espontânea de suspeitas de reacção "
          "adversa pelos profissionais de saúde e pelos pacientes. O Centro "
          "Nacional de Farmacovigilância, serviço da ANARME, é o "
          "destinatário das notificações, que devem ser transmitidas no "
          "prazo máximo de quinze dias quando se trate de suspeitas de "
          "reacções adversas graves {snf2023}."),
        P("Merece registo que o regulamento não usa a designação de evento "
          "supostamente atribuível à vacinação nem descreve um circuito "
          "específico para os eventos pós-vacinais, embora abranja as vacinas "
          "de forma expressa {snf2023}. Na prática, os eventos pós-vacinais "
          "seguem dois caminhos que se cruzam: o do programa de imunização, "
          "que investiga e classifica os casos segundo as orientações "
          "internacionais {omsvigilancia2016}, e o da farmacovigilância "
          "regulamentar. A OMS recomenda exactamente a convergência destes "
          "dois caminhos num sistema comum, com métodos partilhados de "
          "recolha e de gestão de dados, ainda que a avaliação do "
          "benefício-risco e a comunicação de risco das vacinas exijam "
          "tratamento próprio {omsblueprint2022}."),
        P("Do lado do programa, o PAV funciona desde 1979 e o calendário "
          "nacional cobre BCG, OPV, IPV, DPT-HepB-Hib, PCV, rotavírus e MR, "
          "com as doses primárias administradas às 6, 10 e 14 semanas de "
          "idade e a primeira dose contra o sarampo a partir dos 9 meses "
          "{cassocera2020,ine2024ids}. A vacinação é quase exclusivamente "
          "pública: 99% das crianças de 12 a 23 meses receberam as vacinas no "
          "sector público {ine2024ids}. Esta concentração num único prestador "
          "simplifica a organização da vigilância, porque o ponto de contacto "
          "com a família é sempre a unidade sanitária, e justifica que o "
          "estudo se realize à saída das consultas de vacinação."),
        P("Os dados nacionais mostram, contudo, um recuo preocupante. A "
          "cobertura completa com antigénios básicos nas crianças de 12 a 23 "
          "meses passou de 47% em 1997 para 66% em 2015 e caiu para 38% em "
          "2022 e 2023, enquanto a proporção sem qualquer vacina subiu de 5% "
          "para 14% {cassocera2023,ine2024ids}. Entre as crianças sem "
          "qualquer vacina, 26% das mães declararam desconhecer a necessidade "
          "da vacinação, e entre as crianças com vacinação incompleta as duas "
          "razões mais citadas foram a falta de vacinas na unidade sanitária "
          "e a distância, ambas com 17% {ine2024ids}. Em Nampula, a cobertura "
          "completa é de 25%, a segunda mais baixa do país {ine2024ids}, e a "
          "cobertura do rotavírus medida na vigilância sentinela nacional foi "
          "de 68,6% antes da pandemia de doença por coronavírus e de 77,3% "
          "durante a pandemia {cassocera2025}."),
    ]),
    ("Instrumentos de medida do conhecimento e das práticas", [
        P("Não existe um instrumento universalmente aceite para medir o "
          "conhecimento das mães sobre eventos pós-vacinais. Os estudos "
          "publicados usam questionários próprios, construídos a partir das "
          "definições e das listas de eventos dos manuais da OMS e adaptados "
          "ao calendário local. O inquérito de Kampala usou um questionário "
          "administrado por entrevistador a cuidadores nas consultas de "
          "vacinação, com secções sobre características "
          "sociodemográficas, conhecimento dos eventos e comportamento de "
          "comunicação {watyaba2025}; o de Accra usou um questionário "
          "estruturado com perguntas abertas e fechadas sobre conhecimento, "
          "atitudes e práticas de vacinação {danso2023}; e o inquérito "
          "ruandês mediu conhecimento e confiança com um questionário "
          "auto-administrado {mbonigaba2024}. Do lado dos profissionais, o "
          "questionário albanês de 68 perguntas {mehmeti2017} e o inquérito "
          "sul-africano, que cobria conhecimento dos conceitos, requisitos de "
          "notificação, percepções e práticas {mehta2026}, oferecem "
          "estruturas testadas."),
        P("A adaptação de um instrumento exige verificação formal. A validade "
          "de conteúdo avalia-se por painel de peritos, com cálculo do índice "
          "de validade de conteúdo (IVC) por item e para a escala; a "
          "literatura metodológica descreve os métodos de cálculo e os "
          "critérios de decisão sobre revisão ou eliminação de itens "
          "{almanasreh2019}. A consistência interna de escalas com itens "
          "dicotómicos mede-se pela fórmula 20 de Kuder-Richardson e a de "
          "escalas com respostas graduadas pelo alfa de Cronbach, com um "
          "valor mínimo habitualmente fixado em 0,70 {taber2018}. A "
          "estabilidade das respostas avalia-se por reteste, com o kappa de "
          "Cohen como medida de concordância, cuja interpretação por "
          "intervalos está estabelecida {mchugh2012}."),
        P("A tradução para a língua falada pela população é condição de "
          "validade, não um pormenor operacional. Em Nampula, o emakhuwa é a "
          "língua predominante e a escolaridade das mães é baixa "
          "{ine2021,ine2024ids}, o que impõe tradução e retroversão "
          "independentes, harmonização por comité e verificação da "
          "compreensão no pré-teste. A administração por entrevistador, em "
          "vez do questionário auto-preenchido, é a única opção compatível "
          "com esta realidade e é também a usada nos estudos africanos "
          "comparáveis {watyaba2025,danso2023}."),
        P("O relato de estudos deste tipo tem agora uma norma própria. A "
          "lista ChecKAP, com 46 itens distribuídos por oito domínios, "
          "destina-se especificamente aos estudos de conhecimentos, atitudes "
          "e práticas e cobre a definição dos construtos, a construção e "
          "validação do instrumento, a pontuação e os pontos de corte "
          "{zarei2024}. Para a componente observacional transversal, "
          "mantém-se a declaração STROBE {von2007}. O uso conjunto das duas "
          "listas assegura que o relatório final descreva com transparência "
          "tanto a amostragem e a análise como a construção da medida de "
          "conhecimento."),
    ]),
]

# ----------------------------------------------------- 7. estado da arte ----
ESTADO_ARTE = [
    P("O [[quadro:estado_arte]] reúne treze estudos empíricos publicados nos "
      "últimos dez anos sobre o conhecimento e as práticas relativas aos "
      "eventos pós-vacinais, à sua notificação e à vacinação infantil, com "
      "indicação do local, do desenho, do número de participantes e dos "
      "principais resultados numéricos."),
    QUADRO("estado_arte",
           "Síntese de estudos sobre conhecimento e notificação de eventos "
           "pós-vacinais e sobre vacinação infantil (estado da arte)",
           ["Autor (ano)", "Local", "Desenho (n)", "Principais resultados"],
           [
               ["Watyaba et al. (2025) {watyaba2025}",
                "Kampala, Uganda",
                "Transversal de métodos mistos, cuidadores e profissionais "
                "(388 entrevistas)",
                "33,5% dos cuidadores referiram evento pós-vacinal no filho "
                "e comunicaram-no; comunicação associada ao ensino "
                "secundário (ORa 3,56), superior (ORa 8,52), idade acima de "
                "35 anos (ORa 18,77) e estado civil de não casado (ORa "
                "3,27); profissionais com bom conhecimento mas sem "
                "conhecimento do sistema nacional de notificação."],
               ["Ansah et al. (2025) {ansah2025}",
                "Norte do Gana (cinco regiões)",
                "Qualitativo, dez grupos focais com mães",
                "Mães conhecem a utilidade das vacinas, algumas desconhecem "
                "as doenças prevenidas; não comunicam por ausência de "
                "resposta dos profissionais, por considerarem os eventos "
                "banais e por experiências anteriores; medo de eventos "
                "graves afasta da vacinação."],
               ["Constantine et al. (2018) {constantine2018}",
                "Distrito de Guruve, Zimbabwe",
                "Avaliação de sistema de vigilância (31 profissionais, 33 "
                "cuidadores)",
                "Frequência de eventos situada entre 13% e 34%; 39% dos "
                "cuidadores com filho afectado e 45% dos profissionais com "
                "eventos encontrados, mas nenhuma notificação em cerca de "
                "18 meses; receio de consequências pessoais e percepção de "
                "pouca gravidade."],
               ["Zvanaka et al. (2017) {zvanaka2017}",
                "Cidade de Harare, Zimbabwe",
                "Transversal descritivo, profissionais de 21 clínicas (51)",
                "98% conheciam a finalidade do sistema e 77% a data correcta "
                "de envio da ficha; subnotificação atribuída à ausência de "
                "retorno (47,1%), ao receio de represálias (31,4%) e à "
                "sobrecarga (21,6%); custo de uma notificação estimado em "
                "22,30 dólares."],
               ["Gidudu et al. (2020) {gidudu2020}",
                "Quatro regiões do Gana",
                "Transversal, profissionais de 169 unidades (306)",
                "Razão de notificação de 1,56 por 100.000 lactentes "
                "sobreviventes contra um mínimo de 10; 57,5% já tinham "
                "encontrado um evento; dos que o encontraram no último ano, "
                "55,0% comunicaram e 31,7% preencheram a ficha; supervisão "
                "associada à notificação (OR 7,39)."],
               ["Aborigo et al. (2022) {aborigo2022}",
                "Quatro regiões do Gana",
                "Qualitativo, entrevistas a informantes-chave (116)",
                "Subnotificação explicada por falta de informação sobre "
                "eventos notificáveis e estruturas, sobrecarga, custo de "
                "notificar, receio de censura, falta de motivação e ausência "
                "de retorno de informação."],
               ["Mehta et al. (2026) {mehta2026}",
                "África do Sul (35 unidades, sete províncias)",
                "Transversal, inquérito electrónico a médicos e enfermeiros "
                "(361)",
                "59,7% com conhecimento moderado; 25,8% sabiam que nem todos "
                "os eventos são evitáveis e 28,8% identificavam os eventos "
                "graves; 31% tinham encontrado um evento e 19,7% alguma vez "
                "notificaram; principal barreira foi a incerteza sobre a "
                "relação com a vacina."],
               ["Mehmeti et al. (2017) {mehmeti2017}",
                "Distrito de Tirana, Albânia",
                "Transversal, profissionais de centros de saúde (102)",
                "Conhecimento globalmente fraco sobre a vigilância, "
                "sobretudo quanto ao papel dos intervenientes; 70,5% tinham "
                "encontrado um evento; 68,6% nunca tiveram formação sobre o "
                "tema."],
               ["Omoleke et al. (2022) {omoleke2022}",
                "Estado de Kebbi, Nigéria",
                "Qualitativo fenomenológico, profissionais e responsáveis do "
                "programa (28)",
                "Conhecimento variável e subóptimo sobre definição e "
                "classificação; erro de vacinação apontado como causa mais "
                "frequente; consequências descritas incluem recusa colectiva "
                "da vacinação e perda de confiança no programa."],
               ["Nyambayo et al. (2023) {nyambayo2023}",
                "Zimbabwe",
                "Ensaio aleatorizado de detecção por mensagem de texto e "
                "entrevista telefónica (4.560)",
                "Taxa de detecção de eventos com procura de cuidados de 2% "
                "no grupo de vigilância activa e nenhuma notificação no "
                "grupo de vigilância passiva; apenas 31% responderam às "
                "mensagens."],
               ["Danso et al. (2023) {danso2023}",
                "Okaikoi, Accra, Gana",
                "Transversal, cuidadores de crianças de 12-23 meses (120)",
                "53,3% das crianças com calendário completo; principal "
                "factor associado à vacinação incompleta foi o conhecimento "
                "materno insuficiente (58%), seguido da falta de tempo "
                "(25,8%) e do esquecimento (17,5%)."],
               ["Mbonigaba et al. (2024) {mbonigaba2024}",
                "Ruanda (nacional)",
                "Transversal, pais e cuidadores (2.126)",
                "95,5% com bom conhecimento e 91,4% com boa confiança na "
                "vacinação infantil; fontes de informação principais foram "
                "os profissionais de saúde (91,8%) e os meios de "
                "comunicação de massas (28,9%)."],
               ["Powelson et al. (2022) {powelson2022}",
                "Namarroi e Gilé, Zambézia, Moçambique",
                "Qualitativo participativo, cuidadores (32) e profissionais "
                "(12)",
                "Quatro padrões de barreiras ao abandono do calendário: "
                "responsabilidade da vacinação atribuída só à mãe, "
                "percepção de má qualidade dos serviços, preocupação com os "
                "efeitos secundários e desequilíbrio de poder face aos "
                "profissionais."],
               ["Semá Baltazar et al. (2018) {sema2018}",
                "Cidade de Nampula, Moçambique",
                "Inquérito populacional após campanha de vacinação oral "
                "contra a cólera (636)",
                "Cobertura com pelo menos uma dose de 69,5% e com duas doses "
                "de 51,2%; entre 451 vacinados, 10% referiram queixas "
                "ligeiras e inespecíficas e 17,3% não receberam qualquer "
                "informação antes da campanha."],
           ],
           larguras=[3.2, 2.6, 3.2, 7.0],
           fonte="Elaboração própria (2026), a partir das fontes citadas."),
    P("A leitura do quadro revela três regularidades. A primeira é a "
      "distância sistemática entre a frequência dos eventos e o número de "
      "notificações: onde se procurou activamente, encontraram-se eventos em "
      "proporções entre 10% e 39% das crianças ou das pessoas vacinadas "
      "{constantine2018,sema2018}, ao passo que a vigilância passiva produziu "
      "razões de notificação muito abaixo do mínimo recomendado ou mesmo "
      "nenhuma notificação {gidudu2020,constantine2018,nyambayo2023}. A "
      "segunda é a natureza das barreiras: nos profissionais predominam o "
      "receio de consequências pessoais, a ausência de retorno de informação, "
      "a sobrecarga e a incerteza sobre o que é notificável "
      "{gidudu2020,zvanaka2017,aborigo2022,mehta2026}, e nas famílias "
      "predominam a percepção de que o evento é banal, a falta de informação "
      "prévia e a experiência de não obter resposta quando comunicam "
      "{ansah2025,constantine2018}. A terceira é o papel da escolaridade e da "
      "informação recebida, que aparecem como os factores mais consistentes "
      "do lado dos cuidadores {watyaba2025,danso2023}."),
    P("As divergências situam-se no nível de conhecimento medido, que varia "
      "de 95,5% de bom conhecimento no Ruanda {mbonigaba2024} a "
      "conhecimento materno insuficiente em 58% dos casos em Accra "
      "{danso2023}, diferença que decorre em grande parte de instrumentos e "
      "pontos de corte distintos e que aconselha a descrever com rigor a "
      "construção da medida. A lacuna é clara: não existe nenhum estudo "
      "moçambicano sobre o conhecimento das mães quanto aos eventos "
      "pós-vacinais da vacinação de rotina nem sobre o circuito pelo qual "
      "esses eventos chegam ao sistema, e a única informação de Nampula "
      "refere-se a uma campanha de vacinação contra a cólera de 2016 "
      "{sema2018,rafael2017}. O presente estudo preenche essa lacuna, com "
      "uma amostra por conglomerados em centros de saúde da cidade, um "
      "instrumento validado em emakhuwa e a medição simultânea, ainda que "
      "assimétrica, dos dois lados do circuito de notificação."),
]
ESQUEMA_TEXTO = [
    P("A [[figura:esquema]] representa o modelo que orienta a recolha e a "
      "análise. O conhecimento da mãe ou do cuidador sobre os eventos "
      "pós-vacinais é tratado como resultado de factores "
      "sociodemográficos, de factores ligados à experiência de vacinação e, "
      "sobretudo, da informação efectivamente recebida no serviço, que é a "
      "variável sobre a qual o sistema de saúde pode agir. Esse conhecimento, "
      "combinado com factores de acesso, determina a prática da família "
      "quando o evento ocorre, e é essa prática, a comunicação do evento à "
      "unidade sanitária, que constitui o desfecho principal do estudo. A "
      "prática do pessoal de enfermagem, medida na componente secundária, "
      "actua como contexto de serviço: é ela que produz, ou não, a informação "
      "dada à mãe e que transforma, ou não, a comunicação da família numa "
      "notificação registada. A escolaridade, a idade e a paridade são "
      "tratadas como potenciais factores de confusão da associação entre "
      "conhecimento e comunicação."),
]
ESQUEMA_TITULO = ("Esquema conceptual do conhecimento e da comunicação dos "
                  "eventos pós-vacinais pelas mães e cuidadores, cidade de "
                  "Nampula, 2027")
ESQUEMA = {
    "contexto": "Mães e cuidadores nas consultas de vacinação de seis centros "
                "de saúde da cidade de Nampula, Março e Abril de 2027",
    "blocos": [
        ("Factores sociodemográficos", ["idade", "escolaridade",
                                        "língua materna", "ocupação",
                                        "número de filhos"]),
        ("Experiência de vacinação", ["idade da criança",
                                      "doses já recebidas",
                                      "evento pós-vacinal anterior",
                                      "posse do cartão de saúde"]),
        ("Informação recebida no serviço", ["aviso sobre eventos esperados",
                                            "aviso sobre sinais de alarme",
                                            "convite a comunicar o evento",
                                            "fonte principal de informação"]),
        ("Acesso e apoio", ["tempo até à unidade sanitária",
                            "custo do transporte",
                            "decisão partilhada com o companheiro",
                            "apoio familiar"]),
        ("Contexto de serviço (pessoal de enfermagem)",
         ["conhecimento das definições", "conhecimento do circuito",
          "prática de aconselhamento", "formação recebida"]),
    ],
    "desfecho": ("Comunicação do evento pós-vacinal à unidade sanitária",
                 ["comunicou", "não comunicou",
                  "nível de conhecimento (bom, moderado, fraco)"]),
    "moderadores": ("Variáveis de confundimento",
                    ["escolaridade", "idade da mãe ou cuidador",
                     "número de filhos"]),
}

# ----------------------------------------------------- 8. metodologia -------
METODOLOGIA = [
    ("Tipo e desenho do estudo", [
        P("Trata-se de um estudo observacional, transversal e analítico, de "
          "base institucional, com recolha de dados por entrevista "
          "estruturada face a face. A componente principal decorre à saída "
          "das consultas de vacinação e responde aos objectivos específicos "
          "1 a 4. A componente secundária é um inquérito censitário, também "
          "por entrevista estruturada, ao pessoal de enfermagem e aos agentes "
          "de medicina preventiva afectos a essas consultas, e responde ao "
          "objectivo específico 5; é deliberadamente delimitada, porque o "
          "objecto do estudo é a família e não a avaliação do desempenho "
          "profissional."),
        P("O desenho transversal é o adequado para medir conhecimento e "
          "práticas declaradas num momento definido e para descrever as suas "
          "associações, sem pretensão de estabelecer relações causais. A "
          "entrevista à saída da consulta, e não no domicílio, foi escolhida "
          "porque a vacinação infantil em Moçambique é quase exclusivamente "
          "pública, com 99% das crianças de 12 a 23 meses vacinadas no sector "
          "público {ine2024ids}, o que torna a consulta o ponto de contacto "
          "universal com a população-alvo. O relato seguirá a lista ChecKAP "
          "para a componente de conhecimentos e práticas {zarei2024} e a "
          "declaração STROBE para a componente observacional {von2007}."),
    ]),
    ("Local e período do estudo", [
        P("O estudo realiza-se na cidade de Nampula, capital da província "
          "mais populosa de Moçambique, com 5.758.920 habitantes na província "
          "no recenseamento de 2017 {ine2021}. Serão incluídos oito centros "
          "de saúde urbanos com consulta de vacinação em funcionamento "
          "regular, seleccionados a partir da lista oficial de unidades "
          "sanitárias do SDSMAS da Cidade de Nampula [confirmar junto do "
          "SDSMAS da Cidade de Nampula a lista de unidades com consulta de "
          "vacinação e o volume mensal de atendimentos de crianças com menos "
          "de 24 meses]. Não se nomeiam aqui as unidades porque a lista e o "
          "volume de atendimentos só serão conhecidos depois da autorização "
          "institucional; a regra de selecção é apresentada na subsecção da "
          "amostra."),
        P("O estudo decorre de Outubro de 2026 a Setembro de 2027. A recolha "
          "de dados realiza-se ao longo de oito semanas, em Março e Abril de "
          "2027, depois da aprovação pelo Comité Institucional de Bioética "
          "para a Saúde da Universidade Lúrio (CIBS-UniLúrio) e das "
          "autorizações institucionais. O período de referência para o relato "
          "de eventos pós-vacinais são os doze meses anteriores à entrevista, "
          "intervalo que cobre um ciclo completo de vacinação de um lactente "
          "e que corresponde ao usado em estudos comparáveis "
          "{constantine2018,watyaba2025}. Os dias de recolha distribuem-se "
          "por todos os dias úteis da semana em que há consulta de vacinação, "
          "para evitar o enviesamento associado a um único dia fixo."),
    ]),
    ("População, unidade de análise e base de amostragem", [
        P("A população principal é constituída pelas mães e pelos cuidadores "
          "que levam crianças com menos de 24 meses às consultas de vacinação "
          "dos centros de saúde seleccionados, durante o período de recolha. "
          "A população secundária é constituída pelo pessoal de enfermagem "
          "materno-infantil e pelos agentes de medicina preventiva que "
          "administram vacinas nessas consultas, seja de forma permanente "
          "seja em escala rotativa."),
        P("A unidade de análise da componente principal é a mãe ou o "
          "cuidador, e não a criança nem a dose administrada. Cada pessoa é "
          "entrevistada uma única vez em todo o estudo; a primeira pergunta "
          "da triagem verifica se já participou, e a equipa mantém, em cada "
          "unidade, uma lista de controlo com o código da criança presente no "
          "cartão de saúde, usada exclusivamente para evitar duplicações e "
          "destruída no fim da recolha. Quando uma mãe traz mais do que uma "
          "criança com menos de 24 meses à mesma consulta, as perguntas sobre "
          "historial e eventos referem-se à criança mais nova. A unidade de "
          "análise da componente secundária é o profissional."),
        P("A base de amostragem da componente principal é o fluxo de saída "
          "da sala de vacinação em cada sessão, sistematizado pelo registo "
          "diário de atendimentos da unidade; não existe lista nominal "
          "prévia, pelo que a selecção é sistemática dentro de cada sessão, "
          "como se descreve adiante. A base de amostragem da componente "
          "secundária é a escala de pessoal afecto à vacinação, fornecida "
          "pela direcção de cada unidade."),
    ]),
    ("Amostra e cálculo do tamanho da amostra", [
        P("O tamanho da amostra foi calculado para dois requisitos, "
          "adoptando-se o maior: a precisão da estimativa do conhecimento "
          "(objectivos 1 a 3) e o poder para a comparação prevista no "
          "objectivo 4 {in2020}. Para a precisão usou-se a fórmula da "
          "estimativa de uma proporção em população infinita:"),
        FORMULA("n<sub>0</sub> = Z<sup>2</sup> × p × (1 - p) / d<sup>2</sup>"),
        P("em que Z = 1,96 corresponde a uma confiança de 95%, d = 0,05 é a "
          "margem de erro absoluta aceite e p = 0,50 é a proporção esperada "
          "de mães com conhecimento bom. Adoptou-se p = 0,50 porque não "
          "existe nenhuma estimativa moçambicana e porque os valores "
          "publicados variam entre um conhecimento materno insuficiente em "
          "58% dos casos em Accra {danso2023} e 95,5% de bom conhecimento no "
          "Ruanda {mbonigaba2024}; na ausência de uma referência local, o "
          "valor de 0,50 maximiza a variância. A substituição dá "
          "n<sub>0</sub> = 3,8416 × 0,50 × 0,50 / 0,0025 = 384,2, isto é, "
          "385 respondentes."),
        P("Como a selecção é feita dentro de centros de saúde, que funcionam "
          "como conglomerados, aplicou-se um efeito de desenho de 1,5, valor "
          "conservador para oito conglomerados com cerca de cem entrevistas "
          "cada e para variáveis de conhecimento, que tendem a ser "
          "homogéneas dentro da área de influência de cada unidade:"),
        FORMULA("n<sub>1</sub> = n<sub>0</sub> × deff = 385 × 1,5 = 577,5 "
                "≅ 578"),
        P("O número total de atendimentos de crianças com menos de 24 meses "
          "nos oito centros durante as oito semanas de recolha "
          "(N) só será conhecido depois da autorização institucional, pelo "
          "que a [[tabela:cenarios]] apresenta a correcção para população "
          "finita e a margem de erro esperada em cinco cenários. A correcção "
          "aplicada é:"),
        FORMULA("n<sub>c</sub> = n<sub>1</sub> / [1 + (n<sub>1</sub> - 1) / "
                "N]"),
        P("e o acréscimo para não resposta, fixado em 10%, superior às perdas "
          "habituais em entrevistas de saída, em que a recusa é rara mas "
          "ocorre por pressa ou por criança a chorar, obtém-se por "
          "n<sub>f</sub> = n<sub>c</sub> / 0,90. Em todos os cenários "
          "considerados, o requisito de precisão fica satisfeito com menos de "
          "630 convites."),
        TABELA("cenarios",
               "Cenários de volume de atendimentos, correcção para população "
               "finita e precisão esperada com 800 respondentes",
               ["Atendimentos no período (N)",
                "Amostra exigida pela precisão (n<sub>c</sub>)",
                "Convites exigidos pela precisão",
                "Margem de erro com 800 respondentes (pontos)"],
               [["3.000", "485", "539", "3,8"],
                ["5.000", "519", "577", "4,3"],
                ["8.000", "540", "600", "4,0"],
                ["12.000", "552", "614", "4,4"],
                ["16.000", "558", "620", "4,5"]],
               larguras=[3.6, 3.6, 3.6, 4.2],
               fonte="Elaboração própria (2026).",
               nota="Valores de N hipotéticos, a substituir pelo volume real "
                    "confirmado junto do SDSMAS da Cidade de Nampula. Cálculo "
                    "para p = 0,50, efeito de desenho de 1,5 e confiança de "
                    "95%. A margem de erro da última coluna incorpora o "
                    "efeito de desenho e a correcção para população finita; "
                    "para N = 5.000 a fracção de amostragem é elevada e a "
                    "margem apresentada já lhe desconta o efeito."),
        P("O requisito determinante é, porém, o do objectivo 4. A comparação "
          "prevista opõe, entre as mães que relataram um evento pós-vacinal, "
          "as que têm conhecimento bom e as que têm conhecimento moderado ou "
          "fraco, quanto à proporção que comunicou o evento à unidade "
          "sanitária. Usou-se a fórmula para duas proporções independentes, "
          "com teste bilateral:"),
        FORMULA("n = [Z<sub>1-α/2</sub> × √(2 × p<sub>m</sub> × (1 - "
                "p<sub>m</sub>)) + Z<sub>1-β</sub> × √(p<sub>1</sub> × (1 - "
                "p<sub>1</sub>) + p<sub>2</sub> × (1 - p<sub>2</sub>))]"
                "<sup>2</sup> / (p<sub>1</sub> - p<sub>2</sub>)<sup>2</sup>"),
        P("com Z<sub>1-α/2</sub> = 1,96, Z<sub>1-β</sub> = 0,84 (poder de "
          "80%), p<sub>1</sub> = 0,30 e p<sub>2</sub> = 0,50, valores que "
          "enquadram a proporção de 33,5% de cuidadores que comunicaram o "
          "evento em Kampala {watyaba2025} e fixam em 20 pontos percentuais "
          "a menor diferença com interesse prático. A substituição dá n = "
          "[1,96 × √0,48 + 0,84 × √0,46]<sup>2</sup> / 0,04 = (1,3579 + "
          "0,5697)<sup>2</sup> / 0,04 = 3,7158 / 0,04 = 92,9, isto é, 93 "
          "mães por grupo em amostragem simples e 140 por grupo depois de "
          "aplicado o efeito de desenho de 1,5, ou seja 280 mães com evento "
          "relatado."),
        P("Admitindo que 35% das mães relatam um evento pós-vacinal nos doze "
          "meses anteriores, proporção intermédia entre os 33,5% de Kampala "
          "{watyaba2025} e os 39% de Guruve {constantine2018}, são "
          "necessários 280 / 0,35 = 800 respondentes. Adopta-se, portanto, "
          "uma amostra de 800 mães e cuidadores, distribuída por oito "
          "conglomerados com 100 entrevistas cada, e convidam-se 880 pessoas, "
          "110 por centro, para compensar 10% de recusas e entrevistas "
          "incompletas. Com 800 respondentes, a margem de erro das "
          "estimativas de conhecimento fica entre 3,8 e 4,5 pontos "
          "percentuais, conforme o cenário da [[tabela:cenarios]]."),
        P("Se a repartição entre os dois grupos de conhecimento for "
          "desequilibrada, por exemplo de 40% e 60%, os grupos efectivos "
          "passam a ter cerca de 75 e 112 mães e o poder para a diferença de "
          "20 pontos mantém-se próximo de 80%. Para o modelo multivariável do "
          "objectivo 4, o número esperado de acontecimentos é de cerca de 140 "
          "mães que comunicaram o evento, ou 93 depois do efeito de desenho, "
          "o que permite no máximo nove parâmetros pela regra de pelo menos "
          "dez acontecimentos por variável {peduzzi1996}; o modelo final será "
          "limitado a oito variáveis e essa restrição será declarada no "
          "relatório. A componente do pessoal de enfermagem é censitária e "
          "não gera testes de hipóteses."),
        P("Para a componente secundária aplica-se o censo. O número de "
          "profissionais afectos às consultas de vacinação dos oito centros "
          "não está publicado e estima-se, para efeitos de planeamento, entre "
          "30 e 60 [confirmar junto do SDSMAS da Cidade de Nampula]. Todos "
          "são convidados, sem sorteio. Sendo um censo, não há erro de "
          "amostragem, e a precisão depende apenas da taxa de resposta, que "
          "será apresentada; se o número de elegíveis exceder 80, mantém-se "
          "ainda assim o censo, por ser um universo pequeno e por o custo "
          "marginal de cada entrevista ser reduzido."),
    ]),
    ("Técnica de amostragem e selecção dos participantes", [
        P("A selecção dos centros de saúde é estratificada por volume de "
          "atendimentos. Depois de obtida a lista do SDSMAS com o volume "
          "mensal de crianças com menos de 24 meses vacinadas em cada "
          "unidade, as unidades são ordenadas por volume e divididas em dois "
          "estratos, de volume alto e de volume médio ou baixo; sorteiam-se "
          "quatro unidades em cada estrato, por sorteio simples com números "
          "aleatórios gerados por computador na presença do orientador. Se o "
          "número de unidades elegíveis for inferior a oito, incluem-se todas "
          "e as 800 entrevistas são redistribuídas em proporção ao volume de "
          "cada uma, sem que nenhuma ultrapasse 160 entrevistas."),
        P("Dentro de cada centro, a recolha decorre em dez dias úteis "
          "distribuídos pelas oito semanas, com uma quota de dez entrevistas "
          "por dia. Em cada sessão, a equipa conta as mães que saem da sala "
          "de vacinação e selecciona sistematicamente uma em cada k, sendo "
          "k o quociente entre o número médio de atendimentos diários da "
          "unidade e a quota diária, arredondado por defeito, com início "
          "aleatório entre 1 e k. Quando a pessoa seleccionada recusa ou não "
          "é elegível, a equipa convida a pessoa imediatamente seguinte no "
          "fluxo e regista a substituição na ficha de controlo da sessão. Se "
          "no fim do dia a quota não estiver preenchida por baixo movimento, "
          "o défice é transferido para o dia seguinte da mesma unidade."),
        P("A entrevista realiza-se sempre depois de administrada a vacina e "
          "fora da sala de vacinação, num espaço reservado cedido pela "
          "direcção da unidade, de modo que a decisão de participar não tenha "
          "qualquer relação com o acto vacinal. Os profissionais da consulta "
          "não seleccionam nem indicam participantes e não estão presentes na "
          "entrevista."),
    ]),
    ("Critérios de inclusão e de exclusão", [
        H3("Critérios de inclusão, mães e cuidadores"),
        LISTA([
            "Ser mãe, pai ou cuidador principal de uma criança com menos de "
            "24 meses de idade levada à consulta de vacinação de uma das "
            "unidades seleccionadas durante o período de recolha.",
            "Ter 18 ou mais anos de idade, ou ter entre 15 e 17 anos e ser "
            "mãe da criança, caso em que se aplica o regime de consentimento "
            "descrito nas considerações éticas.",
            "Ser residente na cidade de Nampula há pelo menos seis meses.",
            "Aceitar participar e assinar, ou marcar com impressão digital "
            "na presença de testemunha, o termo de consentimento informado.",
        ]),
        H3("Critérios de exclusão, mães e cuidadores"),
        LISTA([
            "Já ter sido entrevistado no âmbito deste estudo, em qualquer "
            "unidade, ou ter participado no pré-teste.",
            "Acompanhar a criança sem com ela conviver diariamente, por não "
            "poder informar sobre o que aconteceu depois das vacinas "
            "anteriores.",
            "Apresentar, no momento, condição que impeça a entrevista, "
            "nomeadamente criança em situação clínica que exija atendimento "
            "imediato ou estado de saúde da própria pessoa que o "
            "desaconselhe.",
            "Ser profissional de saúde em exercício, por o conhecimento "
            "técnico invalidar a medida pretendida.",
        ]),
        H3("Critérios de inclusão e de exclusão, pessoal de enfermagem"),
        LISTA([
            "Incluem-se os enfermeiros, os técnicos de enfermagem de saúde "
            "materno-infantil e os agentes de medicina preventiva que "
            "administram vacinas nas unidades seleccionadas, com pelo menos "
            "três meses de exercício na consulta de vacinação.",
            "Excluem-se os profissionais em férias ou ausentes durante todo o "
            "período de recolha, os que participaram no pré-teste e os que "
            "integrem a equipa de investigação.",
        ]),
    ]),
    ("Variáveis e definições operacionais", [
        P("O [[quadro:variaveis]] apresenta as variáveis do estudo, o seu "
          "tipo, a definição operacional com as categorias e o objectivo "
          "específico a que servem. A classificação dos relatos em eventos "
          "ligeiros esperados e em sinais de alarme segue a lista de eventos "
          "do manual global de vigilância {omsvigilancia2016}. Os pontos de "
          "corte do conhecimento seguem a regra usada em todo o protocolo: "
          "bom com 80% ou mais de respostas correctas, moderado de 60% a 79% "
          "e fraco abaixo de 60%; aplicados à escala de doze itens das mães, "
          "correspondem a 10 a 12 pontos, 8 a 9 pontos e 0 a 7 pontos, e "
          "aplicados à escala de quinze itens do pessoal de enfermagem "
          "correspondem a 12 a 15 pontos, 9 a 11 pontos e 0 a 8 pontos."),
        QUADRO("variaveis", "Variáveis do estudo e definições operacionais",
               ["Variável", "Tipo", "Definição operacional e categorias",
                "Objectivo"],
               [
                   ["Comunicação do evento pós-vacinal à unidade sanitária",
                    "Dependente, qualitativa dicotómica",
                    "Ter levado a criança à unidade sanitária ou informado um "
                    "profissional de saúde sobre o evento pós-vacinal mais "
                    "recente, nos doze meses anteriores (pergunta D6): sim; "
                    "não", "3, 4"],
                   ["Nível de conhecimento sobre eventos pós-vacinais",
                    "Independente principal, qualitativa ordinal",
                    "Soma de 12 itens de resposta certa, errada ou não sei "
                    "(0 a 12): bom, 10 a 12 (80% ou mais); moderado, 8 a 9 "
                    "(60-79%); fraco, 0 a 7 (menos de 60%)", "2, 4"],
                   ["Relato de evento pós-vacinal",
                    "Dependente, qualitativa dicotómica",
                    "Ter observado na criança qualquer alteração de saúde "
                    "nos sete dias seguintes a uma vacina, nos doze meses "
                    "anteriores (pergunta D1): sim; não", "3"],
                   ["Tipo de evento relatado", "Descritiva, nominal de "
                    "resposta múltipla",
                    "Febre; dor, rubor ou tumefacção no local da injecção; "
                    "irritabilidade ou choro; perda de apetite; abcesso ou "
                    "secreção no local; convulsão; choro persistente por mais "
                    "de três horas; dificuldade respiratória; inchaço da "
                    "face; perda de consciência; outro", "3"],
                   ["Reconhecimento de sinais de alarme",
                    "Descritiva, quantitativa discreta",
                    "Número de sinais de alarme correctamente identificados "
                    "entre os seis apresentados (0 a 6)", "2"],
                   ["Prática adoptada no evento mais recente",
                    "Descritiva, nominal de resposta múltipla",
                    "Nada; medidas caseiras não medicamentosas; paracetamol "
                    "ou outro antipirético; remédio tradicional ou de "
                    "plantas; aplicação local; ida à unidade sanitária; "
                    "contacto com agente comunitário; outra", "3"],
                   ["Informação recebida no serviço sobre eventos esperados",
                    "Independente, qualitativa dicotómica",
                    "Ter recebido de um profissional, em qualquer consulta de "
                    "vacinação, informação sobre o que pode acontecer depois "
                    "da vacina: sim; não", "1, 4"],
                   ["Informação recebida sobre sinais de alarme",
                    "Independente, dicotómica",
                    "Ter sido informado sobre os sinais que obrigam a voltar "
                    "de imediato à unidade sanitária: sim; não", "1, 4"],
                   ["Convite explícito a comunicar o evento",
                    "Independente, dicotómica",
                    "Ter sido dito, por um profissional, que devia informar o "
                    "serviço caso surgisse algum problema após a vacina: sim; "
                    "não", "1, 4"],
                   ["Fonte principal de informação sobre vacinas",
                    "Descritiva, nominal",
                    "Profissional de saúde; agente comunitário; rádio ou "
                    "televisão; familiares ou vizinhos; líder comunitário ou "
                    "religioso; telemóvel e redes sociais; nenhuma", "1"],
                   ["Idade da mãe ou cuidador", "Independente, quantitativa",
                    "Anos completos; categorias 15-19, 20-24, 25-34, 35 ou "
                    "mais", "1, 4"],
                   ["Escolaridade", "Independente, ordinal",
                    "Nenhuma; primária incompleta; primária completa; "
                    "secundária; superior", "1, 4"],
                   ["Relação com a criança", "Independente, nominal",
                    "Mãe; pai; avó ou avô; outro cuidador principal", "1, 4"],
                   ["Número de filhos vivos", "Independente, quantitativa "
                    "discreta", "Número; categorias 1, 2-3, 4 ou mais",
                    "1, 4"],
                   ["Língua principal falada em casa", "Independente, "
                    "nominal", "Emakhuwa; português; outra", "1, 4"],
                   ["Ocupação", "Descritiva, nominal",
                    "Doméstica; agricultura; comércio informal; emprego "
                    "assalariado; estudante; outra", "1"],
                   ["Tempo até à unidade sanitária", "Independente, "
                    "dicotómica", "30 minutos ou menos; mais de 30 minutos",
                    "1, 4"],
                   ["Idade da criança", "Descritiva, quantitativa",
                    "Meses completos; categorias 0-5, 6-11, 12-23", "1"],
                   ["Vacinação em dia segundo o cartão", "Descritiva, "
                    "dicotómica",
                    "Doses registadas compatíveis com a idade, verificadas no "
                    "cartão de saúde apresentado: sim; não; cartão não "
                    "apresentado", "1"],
                   ["Conhecimento do pessoal de enfermagem",
                    "Descritiva, ordinal",
                    "Soma de 15 itens (0 a 15): bom, 12 a 15 (80% ou mais); "
                    "moderado, 9 a 11 (60-79%); fraco, 0 a 8 (menos de 60%)",
                    "5"],
                   ["Prática declarada de notificação",
                    "Descritiva, dicotómica",
                    "Ter alguma vez preenchido uma ficha de notificação de "
                    "evento pós-vacinal: sim; não", "5"],
                   ["Prática declarada de aconselhamento",
                    "Descritiva, ordinal",
                    "Frequência com que informa a mãe sobre os eventos "
                    "esperados: sempre; quase sempre; às vezes; raramente; "
                    "nunca", "5"],
                   ["Formação sobre eventos pós-vacinais",
                    "Descritiva, dicotómica",
                    "Ter recebido formação específica sobre eventos "
                    "pós-vacinais nos últimos três anos: sim; não", "5"],
                   ["Barreiras declaradas à notificação",
                    "Descritiva, nominal de resposta múltipla",
                    "Falta de tempo; falta de fichas; desconhecimento do "
                    "circuito; dúvida sobre se o evento é notificável; receio "
                    "de consequências pessoais; ausência de retorno de "
                    "informação; considerar o evento pouco grave; outra",
                    "5"],
               ],
               larguras=[3.4, 2.8, 8.0, 1.8],
               fonte="Elaboração própria (2026)."),
    ]),
    ("Instrumentos de recolha de dados, validação e pré-teste", [
        P("O instrumento principal é um questionário administrado por "
          "entrevistador, com cerca de 25 minutos de duração e cinco secções "
          "(Apêndice A): identificação da entrevista e triagem; "
          "características sociodemográficas da mãe ou cuidador e da criança; "
          "informação recebida no serviço e fontes de informação; "
          "conhecimento sobre eventos pós-vacinais e sinais de alarme; e "
          "relato de eventos e práticas adoptadas. A estrutura e as perguntas "
          "de prática foram adaptadas do questionário aplicado a cuidadores "
          "nas consultas de vacinação de Kampala {watyaba2025} e dos "
          "instrumentos de conhecimentos, atitudes e práticas usados em Accra "
          "e no Ruanda {danso2023,mbonigaba2024}; os itens de conhecimento "
          "foram redigidos para este estudo a partir das definições e da "
          "lista de eventos dos manuais da OMS "
          "{omsvigilancia2016,omscausalidade2021}. Nenhum item reproduz uma "
          "escala validada existente, pelo que o instrumento é submetido a "
          "validação completa."),
        P("O instrumento secundário é um questionário ao pessoal de "
          "enfermagem, com cerca de 20 minutos e quatro secções (Apêndice B): "
          "caracterização profissional e formação; conhecimento das "
          "definições, da classificação por causa e dos critérios de "
          "gravidade; conhecimento do circuito de notificação, dos "
          "destinatários e dos prazos; e práticas declaradas de "
          "aconselhamento, de registo e de notificação, com as barreiras "
          "percebidas. As perguntas foram adaptadas do questionário "
          "estruturado aplicado a profissionais em Tirana {mehmeti2017}, do "
          "inquérito sul-africano sobre conhecimento e práticas de "
          "notificação {mehta2026} e da lista de barreiras identificadas no "
          "Gana {gidudu2020,aborigo2022}, e ajustadas ao circuito previsto no "
          "Regulamento do SNF {snf2023}."),
        P("Ambos os questionários são redigidos em português e traduzidos "
          "para emakhuwa por um tradutor, retrovertidos para português por um "
          "segundo tradutor independente que desconhece a versão original, e "
          "harmonizados por um comité formado pelo investigador, pelo "
          "orientador e pelos dois tradutores, que resolve as discrepâncias e "
          "fixa a versão final. A entrevista decorre na língua escolhida pela "
          "participante e o entrevistador usa sempre a versão escrita "
          "correspondente, para que a formulação seja idêntica em todas as "
          "entrevistas."),
        P("A validade de conteúdo é avaliada por um painel de cinco peritos: "
          "dois docentes de Farmácia com experiência em farmacovigilância, um "
          "médico pediatra ou de saúde pública, um responsável provincial do "
          "PAV e um docente de enfermagem materno-infantil. Cada perito "
          "classifica a relevância de cada item numa escala de quatro pontos; "
          "o IVC de cada item é a proporção de peritos que o classificam como "
          "bastante ou muito relevante {almanasreh2019}. Itens com IVC "
          "inferior a 0,80, isto é, aprovados por menos de quatro dos cinco "
          "peritos, são revistos ou retirados, e a média do IVC da escala "
          "deve atingir pelo menos 0,90. O painel avalia também a "
          "neutralidade da formulação, para que nenhuma pergunta sugira que "
          "as vacinas são perigosas."),
        P("O pré-teste envolve 80 mães e cuidadores, 10% da amostra, numa "
          "unidade sanitária da cidade não incluída no estudo, e cinco "
          "profissionais dessa mesma unidade. Avalia o tempo de "
          "preenchimento, a proporção de respostas em falta por item, a "
          "compreensão das perguntas em emakhuwa e a adequação das categorias "
          "de resposta. A consistência interna das escalas de conhecimento, "
          "compostas por itens dicotomizados, é estimada pelo KR-20, com "
          "valor mínimo de 0,70 {taber2018}; se ficar abaixo, os itens com "
          "correlação item-total inferior a 0,20 são revistos e o KR-20 volta "
          "a ser calculado na amostra principal. A estabilidade das respostas "
          "é avaliada por reteste ao fim de 10 a 14 dias em 30 participantes "
          "do pré-teste que aceitem e forneçam contacto, com exigência de "
          "kappa de Cohen de pelo menos 0,60 para o relato de evento e para a "
          "comunicação do evento {mchugh2012}. Os participantes do pré-teste "
          "não entram na amostra final."),
    ]),
    ("Procedimentos de recolha de dados e controlo de qualidade", [
        P("A recolha é feita pelo investigador e por três assistentes com "
          "formação em saúde, fluentes em emakhuwa e em português, que não "
          "são funcionários das unidades sanitárias envolvidas nem têm "
          "qualquer relação hierárquica com elas. A formação dura dois dias e "
          "cobre o protocolo, o guião de entrevista, a tradução acordada de "
          "cada termo, a neutralidade da formulação, o consentimento "
          "informado, o procedimento de encaminhamento clínico e o "
          "preenchimento da ficha de controlo da sessão (Apêndice E). Cada "
          "assistente realiza duas entrevistas supervisionadas antes de "
          "trabalhar sozinho."),
        P("Em cada sessão, o assistente aborda a pessoa seleccionada à saída "
          "da sala de vacinação, apresenta-se, explica o estudo com a folha "
          "de informação (Apêndice C), obtém o consentimento e conduz a "
          "entrevista num espaço reservado. As respostas são registadas em "
          "papel; a idade da criança e as doses administradas são copiadas do "
          "cartão de saúde sempre que este esteja disponível, e a ausência do "
          "cartão é registada como tal. Nenhum nome é escrito no "
          "questionário, que recebe apenas um código composto pelo número da "
          "unidade, pela data e por um número sequencial."),
        P("O controlo de qualidade assenta em quatro medidas. O investigador "
          "verifica todos os questionários no próprio dia, quanto a "
          "completude e consistência interna, e devolve ao assistente os que "
          "tenham incoerências para correcção imediata, antes de a "
          "participante sair sempre que possível. O investigador observa "
          "presencialmente pelo menos 10% das entrevistas de cada assistente, "
          "distribuídas ao longo do período, com grelha de observação do "
          "cumprimento do guião. As descrições abertas dos eventos são "
          "codificadas de forma independente por dois codificadores, o "
          "investigador e um docente da FCS, nas categorias de evento ligeiro "
          "esperado, sinal de alarme e outro; a concordância é medida pelo "
          "kappa de Cohen, com valor mínimo de 0,60 {mchugh2012}, e as "
          "discordâncias são resolvidas por consenso ou pelo orientador. "
          "Todos os questionários são digitados duas vezes, por pessoas "
          "diferentes, no programa EpiData, com limites de valores e regras "
          "de salto, e as discrepâncias são corrigidas pelo questionário em "
          "papel."),
        P("A componente do pessoal de enfermagem decorre nas duas últimas "
          "semanas da recolha em cada unidade, em horário acordado com a "
          "direcção e fora do período de atendimento, para que a consulta não "
          "seja perturbada. A entrevista é conduzida pelo investigador, em "
          "local reservado, sem a presença de chefias, e os questionários não "
          "contêm nome nem categoria profissional individualizada que permita "
          "identificação em unidades com poucos profissionais."),
    ]),
    ("Processamento e análise dos dados", [
        P("A análise será feita no programa Statistical Package for the "
          "Social Sciences (SPSS), da IBM, versão 26 ou superior, com o "
          "módulo de amostras complexas, ou no programa R com o pacote "
          "survey, ambos capazes de incorporar os estratos de volume, os "
          "conglomerados e a correcção para população finita. O nível de "
          "significância é de 5% e todas as estimativas são apresentadas com "
          "intervalo de confiança (IC) a 95%. O [[quadro:analise]] resume a "
          "análise prevista para cada objectivo específico."),
        P("A descrição das participantes e das crianças usa frequências "
          "absolutas e relativas para as variáveis qualitativas e média com "
          "desvio-padrão, ou mediana com intervalo interquartílico quando a "
          "distribuição for assimétrica, para as quantitativas. As "
          "proporções são apresentadas com IC 95% calculados para o desenho "
          "por conglomerados, e a taxa de resposta é apresentada por unidade "
          "sanitária, como exige a lista ChecKAP {zarei2024}. A pontuação de "
          "conhecimento é descrita pela média e pela distribuição pelas três "
          "categorias, e a consistência interna observada na amostra final é "
          "relatada pelo KR-20."),
        P("A comparação prevista no objectivo 4 usa o teste do qui-quadrado "
          "com correcção de Rao-Scott para o desenho, ou o teste exacto de "
          "Fisher quando mais de 20% das frequências esperadas forem "
          "inferiores a cinco, e apresenta a diferença de proporções e a "
          "razão de prevalências (RP) com IC 95%. Como a comunicação do "
          "evento é um desfecho frequente, a odds ratio (OR) sobrestimaria a "
          "associação, pelo que a medida principal é a RP, estimada por "
          "regressão de Poisson com variância robusta, que mantém bom "
          "desempenho mesmo quando o modelo não está perfeitamente "
          "especificado {chen2018}."),
        P("Entram no modelo multivariável os factores com p<0,20 na análise "
          "bivariada e, obrigatoriamente, a escolaridade, a idade e o número "
          "de filhos, tratados como potenciais factores de confusão, e a "
          "informação recebida no serviço; o total é limitado a oito "
          "variáveis, pelas razões de poder já expostas. A colinearidade é "
          "verificada pelo factor de inflação da variância, retirando-se uma "
          "das variáveis quando este exceder cinco. O modelo final apresenta "
          "razões de prevalência ajustadas (RPa) com IC 95%; como análise de "
          "sensibilidade e para comparação com a literatura, estima-se também "
          "o modelo de regressão logística, com odds ratio ajustados (ORa), "
          "por ser a medida usada nos estudos comparáveis {watyaba2025}. O "
          "conhecimento é analisado pelas três categorias definidas e, em "
          "alternativa, pela pontuação contínua."),
        P("A componente do pessoal de enfermagem é analisada apenas de forma "
          "descritiva, com frequências e proporções e com a distribuição das "
          "barreiras declaradas, sem testes de hipóteses, dado o número "
          "reduzido de profissionais. Como análise complementar, as respostas "
          "das mães sobre a informação recebida são confrontadas com as "
          "práticas de aconselhamento declaradas pelos profissionais da mesma "
          "unidade, ao nível agregado da unidade e sem qualquer emparelhamento "
          "individual. As respostas em falta são descritas por variável; se "
          "nenhuma variável do modelo final tiver mais de 5% de dados em "
          "falta, usa-se a análise de casos completos, e se tiver, o modelo é "
          "repetido com imputação múltipla por equações encadeadas, com 20 "
          "conjuntos imputados, como análise de sensibilidade."),
        QUADRO("analise", "Plano de análise por objectivo específico",
               ["Objectivo", "Indicador ou desfecho", "Denominador",
                "Análise estatística"],
               [
                   ["1", "Características sociodemográficas, historial "
                    "vacinal da criança e informação recebida no serviço",
                    "Todas as mães e cuidadores respondentes (800)",
                    "Frequências e proporções com IC 95% ajustados ao "
                    "desenho; taxas de resposta por unidade"],
                   ["2", "Pontuação de conhecimento e distribuição pelas "
                    "categorias bom, moderado e fraco; sinais de alarme "
                    "reconhecidos",
                    "Todas as mães e cuidadores respondentes",
                    "Média e desvio-padrão; proporções com IC 95%; KR-20 na "
                    "amostra final"],
                   ["3", "Proporção com relato de evento pós-vacinal nos doze "
                    "meses, tipo de evento e práticas adoptadas",
                    "Todos os respondentes (relato) e mães com evento "
                    "relatado (práticas)",
                    "Proporções com IC 95%; kappa entre codificadores dos "
                    "relatos abertos"],
                   ["4", "Comunicação do evento à unidade sanitária segundo "
                    "o nível de conhecimento e a informação recebida",
                    "Mães com evento relatado (cerca de 280)",
                    "Qui-quadrado de Rao-Scott; diferença de proporções e RP "
                    "com IC 95%; RPa por regressão de Poisson modificada com "
                    "até oito variáveis; ORa como sensibilidade"],
                   ["5", "Conhecimento, práticas declaradas e barreiras do "
                    "pessoal de enfermagem",
                    "Pessoal de enfermagem respondente (censo)",
                    "Frequências e proporções; sem testes de hipóteses; "
                    "confronto agregado com as respostas das mães da mesma "
                    "unidade"],
               ],
               larguras=[1.8, 4.6, 3.8, 5.8],
               fonte="Elaboração própria (2026)."),
    ]),
    ("Limitações do estudo e estratégias de mitigação", [
        P("O [[quadro:limitacoes]] apresenta as limitações previsíveis, a sua "
          "consequência para os resultados e as medidas adoptadas para as "
          "reduzir. As duas mais relevantes são a selecção de uma população "
          "que já usa o serviço, que exclui precisamente as famílias que não "
          "vacinam, e a dependência do relato materno, sem confirmação "
          "clínica dos eventos."),
        QUADRO("limitacoes", "Limitações previstas e estratégias de mitigação",
               ["Limitação", "Consequência", "Mitigação"],
               [
                   ["Selecção de mães que comparecem à consulta de vacinação",
                    "Exclusão das famílias que abandonaram ou nunca "
                    "iniciaram o calendário, provavelmente as de menor "
                    "conhecimento, com sobrestimação do conhecimento médio",
                    "Declarar a população como utilizadora do serviço; "
                    "interpretar os resultados como limite superior; propor "
                    "um estudo comunitário complementar"],
                   ["Relato materno sem confirmação clínica do evento",
                    "Classificação incorrecta do tipo e da gravidade do "
                    "evento e impossibilidade de avaliar causalidade",
                    "Definição operacional explícita que não atribui causa; "
                    "codificação dupla dos relatos abertos com kappa; "
                    "consulta do cartão de saúde quando disponível"],
                   ["Viés de memória para eventos ocorridos até doze meses "
                    "antes",
                    "Subestimação da proporção de eventos, sobretudo dos "
                    "ligeiros e mais antigos",
                    "Pormenores pedidos apenas para o evento mais recente; "
                    "ancoragem da recordação na dose registada no cartão"],
                   ["Desejabilidade social na entrevista dentro da unidade "
                    "sanitária",
                    "Sobredeclaração da informação recebida e das práticas "
                    "consideradas correctas",
                    "Entrevistadores externos ao serviço; entrevista fora da "
                    "sala de vacinação e sem profissionais presentes; "
                    "garantia explícita de que as respostas não são "
                    "mostradas à equipa da unidade"],
                   ["Desenho transversal",
                    "Impossibilidade de inferir causalidade e ambiguidade "
                    "temporal entre conhecimento e comunicação do evento",
                    "Interpretar as associações como tais; declarar a "
                    "limitação no relatório e nas conclusões"],
                   ["Poder limitado para o modelo multivariável",
                    "Associações moderadas podem não atingir significância "
                    "estatística",
                    "Limitar o modelo a oito variáveis; apresentar sempre "
                    "IC 95%; declarar o poder disponível"],
                   ["Número reduzido de profissionais de enfermagem",
                    "Estimativas instáveis e risco de identificação "
                    "individual em unidades pequenas",
                    "Censo em vez de amostra; análise apenas descritiva; "
                    "resultados nunca apresentados por unidade nem por "
                    "categoria isolada"],
                   ["Tradução de conceitos técnicos para emakhuwa",
                    "Perda de equivalência semântica e respostas "
                    "influenciadas pela formulação",
                    "Tradução e retroversão independentes; harmonização por "
                    "comité; verificação da compreensão no pré-teste; versão "
                    "escrita única usada por todos os entrevistadores"],
                   ["Risco de a entrevista reforçar receios sobre as vacinas",
                    "Contributo involuntário para a hesitação vacinal",
                    "Formulação neutra validada pelo painel; correcção de "
                    "ideias erradas só no fim da entrevista; entrega de "
                    "folheto informativo a todas as participantes"],
                   ["Validade externa limitada à cidade de Nampula",
                    "Resultados não generalizáveis aos distritos rurais da "
                    "província nem a outras províncias",
                    "Descrição completa do contexto e das unidades; "
                    "comparação com a literatura africana"],
               ],
               larguras=[4.4, 5.2, 6.4],
               fonte="Elaboração própria (2026)."),
    ]),
    ("Considerações éticas", [
        P("O protocolo será submetido ao CIBS-UniLúrio e a recolha só começa "
          "depois da sua aprovação, em conformidade com a Lei de Investigação "
          "em Saúde Humana {lei3de2023} e com a Declaração de Helsínquia na "
          "revisão de 2024 {world2025}. Serão pedidas autorizações à Direcção "
          "Provincial de Saúde (DPS) de Nampula, ao SDSMAS da Cidade de "
          "Nampula e à direcção de cada unidade sanitária (Apêndice F). Por "
          "envolver um programa nacional de saúde e a recolha em unidades "
          "sanitárias públicas, o parecer do Comité Nacional de Bioética para "
          "a Saúde (CNBS) será solicitado se o CIBS-UniLúrio o entender "
          "necessário. Os riscos são mínimos e resumem-se ao tempo da "
          "entrevista e a algum desconforto ao recordar um episódio de doença "
          "da criança."),
        LISTA([
            "Consentimento informado escrito e individual, obtido antes da "
            "entrevista, depois da leitura da folha de informação na língua "
            "escolhida pela participante; quem não sabe ler recebe leitura "
            "integral em voz alta e assina com impressão digital na presença "
            "de uma testemunha maior de idade alheia à equipa, que também "
            "assina (Apêndice D).",
            "A participação não tem qualquer efeito sobre a vacinação da "
            "criança: a entrevista realiza-se sempre depois de administradas "
            "as vacinas, fora da sala de vacinação e sem profissionais do "
            "serviço presentes, e a folha de informação afirma de forma "
            "expressa que recusar não altera o atendimento naquele dia nem "
            "em qualquer visita futura.",
            "Cuidadoras com idade entre 15 e 17 anos que sejam mães da "
            "criança são incluídas com o seu próprio consentimento, por "
            "exercerem a responsabilidade parental e decidirem sobre a saúde "
            "do filho; quando estiverem acompanhadas por um adulto "
            "responsável, este é informado do estudo, mas a decisão é da "
            "própria. Cuidadoras com menos de 15 anos e cuidadoras menores "
            "que não sejam mães da criança não são incluídas. Esta regra é "
            "submetida à apreciação do comité [confirmar junto do "
            "CIBS-UniLúrio o regime aplicável às mães menores de idade].",
            "O estudo não discute a eficácia das vacinas nem apresenta "
            "listas de possíveis danos: as perguntas são neutras, validadas "
            "pelo painel de peritos quanto à formulação, e qualquer ideia "
            "errada manifestada pela participante é corrigida apenas no fim "
            "da entrevista, com informação simples e apoiada no folheto, "
            "nunca durante a recolha das respostas.",
            "Todas as participantes recebem, no fim da entrevista, um "
            "folheto ilustrado com os eventos esperados após cada vacina, os "
            "cuidados a ter em casa, os sinais que obrigam a voltar de "
            "imediato à unidade sanitária e o convite a comunicar qualquer "
            "ocorrência ao serviço (Apêndice G), entregue também a quem "
            "recusar participar.",
            "Encaminhamento clínico obrigatório: se durante a entrevista a "
            "participante descrever um evento activo na criança, "
            "nomeadamente febre no momento, abcesso ou secreção no local da "
            "injecção, choro persistente, convulsão recente, dificuldade "
            "respiratória ou prostração, a entrevista é interrompida e o "
            "entrevistador acompanha de imediato a mãe e a criança ao "
            "profissional de serviço, registando a ocorrência na ficha de "
            "controlo da sessão; a entrevista só é retomada se a mãe o "
            "desejar depois do atendimento.",
            "Os eventos assim detectados são comunicados ao profissional da "
            "unidade, a quem compete a investigação e a notificação pelo "
            "circuito de rotina previsto no Regulamento do SNF {snf2023}; a "
            "equipa de investigação não preenche fichas de notificação nem "
            "substitui o serviço nessa função.",
            "Confidencialidade e anonimato: os questionários não contêm nome, "
            "morada nem número de documento; a lista de controlo usada para "
            "evitar duplicações é guardada em separado e destruída no fim da "
            "recolha; os questionários em papel ficam em caixa fechada à "
            "chave e são destruídos cinco anos após a defesa; a base de "
            "dados, sem identificadores, é protegida por palavra-passe e só "
            "o investigador e o orientador lhe têm acesso.",
            "Para o pessoal de enfermagem, a participação é voluntária e sem "
            "efeito na avaliação profissional; as chefias não têm acesso às "
            "respostas individuais; os resultados são apresentados apenas "
            "agregados, nunca por unidade sanitária nem por profissional, e "
            "a devolução aos serviços é feita em tom formativo e não "
            "punitivo, à semelhança do recomendado para reduzir o receio de "
            "consequências pessoais {aborigo2022,laryea2025}.",
            "Não há pagamento pela participação; as participantes não têm "
            "custos acrescidos, por serem entrevistadas no local e no dia em "
            "que já se deslocaram à unidade sanitária.",
        ]),
        P("O investigador declara não ter conflitos de interesses e o estudo "
          "não recebe financiamento de empresas farmacêuticas nem de "
          "fabricantes de vacinas. Os resultados serão comunicados de forma a "
          "não pôr em causa a confiança da população no PAV: qualquer achado "
          "sobre eventos pós-vacinais será apresentado em conjunto com a "
          "informação sobre os benefícios da vacinação e com a explicação de "
          "que a notificação existe para proteger as crianças e não para "
          "pôr em causa as vacinas {omsblueprint2022}."),
    ]),
]

# ----------------------------------------------------- 9 e 10 ---------------
RESULTADOS_ESPERADOS = [P("PLACEHOLDER")]
DIVULGACAO = [P("PLACEHOLDER")]

# ----------------------------------------------------- 11. cronograma -------
CRONOGRAMA_TEXTO = [P("PLACEHOLDER")]
CRONOGRAMA = {
    "inicio": (2026, 10),
    "n_meses": 12,
    "actividades": [("Revisão da literatura e redacção do protocolo", [1, 2])],
}

# ----------------------------------------------------- 12. orcamento --------
ORCAMENTO_TEXTO = [P("PLACEHOLDER")]
ORCAMENTO = [("Impressão de questionários", "página", 1500, 5)]
ORCAMENTO_IMPREVISTOS = 0.10

# ----------------------------------------------------- apendices ------------
APENDICES = [("Questionário", [P("PLACEHOLDER")])]
