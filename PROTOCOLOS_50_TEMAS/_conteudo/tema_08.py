# -*- coding: utf-8 -*-
"""
Tema 08: Prevalencia e determinantes da automedicacao entre estudantes da
Universidade Lurio na cidade de Nampula, com comparacao entre cursos da area
da saude e de outras areas (Farmacoepidemiologia e Uso Racional de
Medicamentos). Estudo transversal analitico, inquerito anonimo em papel,
recolha em Marco e Abril de 2027.

Compor e validar:   python _motor/motor.py _conteudo/tema_08.py
Verificar fontes:   python _motor/refs.py verificar _conteudo/tema_08.py
"""
from blocos import (CAMPO, ESCALA, FORMULA, H3, LISTA, NOTA, P, PERG,
                    QUADRO, TABELA)

NUMERO = 8
SLUG = "Automedicacao_Estudantes_UniLurio_Nampula"
TITULO = ("Prevalência e determinantes da automedicação em estudantes da "
          "Universidade Lúrio, cidade de Nampula: comparação entre cursos da "
          "saúde e de outras áreas, 2027")
DESENHO = ("Transversal analítico, inquérito por questionário anónimo "
           "auto-administrado em papel, com amostragem estratificada por "
           "área, curso e ano curricular")

AUTOR = "[Nome do(a) estudante]"
ORIENTADOR = "[Nome e grau académico do(a) orientador(a)]"

# ---------------------------------------------------------------- resumo --
RESUMO = (
    "A automedicação é frequente entre estudantes universitários e, quando "
    "envolve antibióticos, antimaláricos ou anti-inflamatórios usados sem "
    "orientação profissional, expõe o utilizador a reacções adversas, "
    "atrasa diagnósticos e contribui para a resistência aos antimicrobianos. "
    "Em Moçambique, a evidência provém sobretudo de Maputo e não há "
    "informação publicada sobre esta prática na Universidade Lúrio. O "
    "estudo avalia a "
    "prevalência, o padrão e os determinantes da automedicação entre os "
    "estudantes de licenciatura da Universidade Lúrio na cidade de Nampula, "
    "comparando os cursos da área da saúde com os de outras áreas. Trata-se "
    "de um estudo transversal analítico, com recolha de dados em Março e "
    "Abril de 2027 na Faculdade de Ciências de Saúde, na Faculdade de "
    "Arquitectura e Planeamento Físico e na Escola Superior de Negócios. A "
    "amostra, estratificada por área, curso e ano curricular, prevê 460 "
    "estudantes convidados por área, 920 no total, para obter 391 "
    "respondentes em cada área, número que permite estimar a prevalência "
    "de cada área com margem de erro de cinco pontos percentuais e detectar "
    "entre as áreas uma diferença de dez pontos com poder de 80%. Os dados "
    "serão recolhidos por questionário anónimo em papel, auto-administrado, "
    "depositado em urna selada, validado por um painel de peritos e "
    "pré-testado. A automedicação será medida nos seis meses anteriores ao "
    "inquérito, com descrição do episódio mais recente, dos medicamentos, "
    "das fontes de obtenção e dos motivos. A análise usará estimativas "
    "ponderadas com intervalos de confiança a 95%, o teste do qui-quadrado "
    "e a regressão de Poisson modificada para estimar razões de prevalência "
    "ajustadas. Espera-se uma prevalência elevada nas duas áreas, com "
    "predomínio dos analgésicos e uso relevante de antibióticos e "
    "antimaláricos obtidos em farmácias sem receita, informação que servirá "
    "para orientar a educação para o uso responsável de medicamentos nos "
    "currículos e nos serviços de apoio ao estudante.")
PALAVRAS_CHAVE = ["automedicação", "estudantes universitários", "Moçambique",
                  "resistência antimicrobiana", "uso de medicamentos"]
ABSTRACT = (
    "Self-medication is common among university students and, when it "
    "involves antibiotics, antimalarials or anti-inflammatory drugs used "
    "without professional guidance, it exposes users to adverse reactions, "
    "delays diagnoses and contributes to antimicrobial resistance. In "
    "Mozambique, the evidence comes mainly from Maputo, and there is no "
    "published information on this practice at "
    "Lúrio University. The study assesses the prevalence, pattern and "
    "determinants of self-medication among undergraduate students of Lúrio "
    "University in the city of Nampula, comparing health courses with "
    "courses from other areas. It is an analytical cross-sectional study, "
    "with data collection in March and April 2027 at the Faculty of Health "
    "Sciences, the Faculty of Architecture and Physical Planning and the "
    "School of Business. The sample, stratified by area, course and year of "
    "study, plans 460 invited students per area, 920 in total, to obtain 391 "
    "respondents in each area, a number that allows the prevalence of each "
    "area to be estimated with a margin of error of five percentage points "
    "and a ten-point difference between areas to be detected with 80% "
    "power. Data will be collected with an anonymous, self-administered "
    "paper questionnaire placed in a sealed ballot box, validated by an "
    "expert panel and pre-tested. Self-medication will be measured over the "
    "six months before the survey, with a description of the most recent "
    "episode, the medicines, the sources of supply and the reasons. The "
    "analysis will use weighted estimates with 95% confidence intervals, the "
    "chi-square test and modified Poisson regression to estimate adjusted "
    "prevalence ratios. A high prevalence is expected in both areas, with a "
    "predominance of analgesics and relevant use of antibiotics and "
    "antimalarials obtained from pharmacies without a prescription, "
    "information that will guide education on the responsible use of "
    "medicines in the curricula and in student support services.")
KEYWORDS = ["antimicrobial resistance", "drug utilization", "Mozambique",
            "self-medication", "students"]

# Só as siglas efectivamente usadas no texto; forma extensa na 1.ª ocorrência.
ABREVIATURAS = [
    ("ANARME", "Autoridade Nacional Reguladora de Medicamento"),
    ("ATC", "classificação Anatómica Terapêutica Química"),
    ("AWaRe", "Access, Watch, Reserve (grupos Acesso, Vigilância e Reserva "
              "da classificação de antibióticos da OMS)"),
    ("COVID-19", "doença por coronavírus 2019"),
    ("CIBS-UniLúrio", "Comité Institucional de Bioética para a Saúde da "
                      "Universidade Lúrio"),
    ("CROSS", "Consensus-Based Checklist for Reporting of Survey Studies"),
    ("FAPF", "Faculdade de Arquitectura e Planeamento Físico"),
    ("FCS", "Faculdade de Ciências de Saúde"),
    ("IC", "intervalo de confiança"),
    ("IVC", "índice de validade de conteúdo"),
    ("KR-20", "fórmula 20 de Kuder-Richardson"),
    ("LNME", "Lista Nacional de Medicamentos Essenciais"),
    ("MISAU", "Ministério da Saúde"),
    ("OMS", "Organização Mundial da Saúde"),
    ("OR", "odds ratio"),
    ("ORa", "odds ratio ajustado"),
    ("RAM", "resistência aos antimicrobianos"),
    ("RP", "razão de prevalências"),
    ("RPa", "razão de prevalências ajustada"),
    ("SPSS", "Statistical Package for the Social Sciences"),
    ("STROBE", "Strengthening the Reporting of Observational Studies in "
               "Epidemiology"),
    ("TDR", "teste de diagnóstico rápido"),
    ("UBS", "UniLúrio Business School (Escola Superior de Negócios)"),
    ("UniLúrio", "Universidade Lúrio"),
]

# ------------------------------------------------------------ referencias --
# Todas geradas por refs.py (pmid, doi, web). Nenhum metadado escrito à mão.
FONTES = {
    # -- definicao e magnitude global
    "oms2000": "World Health Organization. Guidelines for the regulatory assessment of medicinal products for use in self-medication (WHO/EDM/QSM/00.1) [Internet]. Geneva: World Health Organization; 2000 [citado 2026 Set 19]. Disponível em: https://iris.who.int/handle/10665/66154",
    "baracaldo2022": "Baracaldo-Santamaría D, Trujillo-Moreno MJ, Pérez-Acosta AM, Feliciano-Alfonso JE, Calderon-Ospina CA, Soler F. Definition of self-medication: a scoping review. Ther Adv Drug Saf. 2022;13:20420986221127501. doi:10.1177/20420986221127501. PMID: 36211626.",
    "behzadifar2020": "Behzadifar M, Behzadifar M, Aryankhesal A, Ravaghi H, Baradaran HR, Sajadi HS, et al. Prevalence of self-medication in university students: systematic review and meta-analysis. East Mediterr Health J. 2020;26(7):846-857. doi:10.26719/emhj.20.052. PMID: 32794171.",
    "gashaw2025": "Gashaw T, Yadeta TA, Weldegebreal F, Demissie L, Jambo A, Assefa N. The global prevalence of antibiotic self-medication among the adult population: systematic review and meta-analysis. Syst Rev. 2025;14(1):49. doi:10.1186/s13643-025-02783-6. PMID: 40012022.",
    "xu2019": "Xu R, Mu T, Wang G, Shi J, Wang X, Ni X. Self-Medication with Antibiotics among University Students in LMIC: A systematic review and meta-analysis. J Infect Dev Ctries. 2019;13(8):678-689. doi:10.3855/jidc.11359. PMID: 32069251.",
    "gbd2024": "GBD 2021 Antimicrobial Resistance Collaborators. Global burden of bacterial antimicrobial resistance 1990-2021: a systematic analysis with forecasts to 2050. Lancet. 2024;404(10459):1199-1226. doi:10.1016/S0140-6736(24)01867-1. PMID: 39299261.",
    "torres2021": "Torres NF, Chibi B, Kuupiel D, Solomon VP, Mashamba-Thompson TP, Middleton LE. The use of non-prescribed antibiotics; prevalence estimates in low-and-middle-income countries. A systematic review and meta-analysis. Arch Public Health. 2021;79(1):2. doi:10.1186/s13690-020-00517-9. PMID: 33390176.",
    # -- Africa e malaria
    "fetensa2021": "Fetensa G, Tolossa T, Etafa W, Fekadu G. Prevalence and predictors of self-medication among university students in Ethiopia: a systematic review and meta-analysis. J Pharm Policy Pract. 2021;14(1):107. doi:10.1186/s40545-021-00391-y. PMID: 34915938.",
    "sisay2018": "Sisay M, Mengistu G, Edessa D. Epidemiology of self-medication in Ethiopia: a systematic review and meta-analysis of observational studies. BMC Pharmacol Toxicol. 2018;19(1):56. doi:10.1186/s40360-018-0248-8. PMID: 30201045.",
    "omsmalariaft2025": "World Health Organization. Malaria: fact sheet [Internet]. Geneva: World Health Organization; 2025 [citado 2026 Set 19]. Disponível em: https://www.who.int/news-room/fact-sheets/detail/malaria",
    "omsmalaria2025": "World Health Organization. World malaria report 2025: addressing the threat of antimalarial drug resistance [Internet]. Geneva: World Health Organization; 2025 [citado 2026 Set 19]. Disponível em: https://www.who.int/publications/i/item/9789240117822",
    "amaka2025": "Amaka JI, MacLeod E, Picozzi K, Fyfe J, Ezenyi IC, Ijaiya IS, et al. Issues associated with malaria self-medication in sub-Saharan Africa: A systematic literature review and meta-analysis. Malariaworld J. 2025;16:16. doi:10.5281/zenodo.17054133. PMID: 40949058.",
    # -- Mocambique e Nampula
    "mate2019": "Mate I, Come CE, Gonçalves MP, Cliff J, Gudo ES. Knowledge, attitudes and practices regarding antibiotic use in Maputo City, Mozambique. PLoS One. 2019;14(8):e0221452. doi:10.1371/journal.pone.0221452. PMID: 31437215.",
    "torres2019": "Torres NF, Solomon VP, Middleton LE. Patterns of self-medication with antibiotics in Maputo City: a qualitative study. Antimicrob Resist Infect Control. 2019;8:161. doi:10.1186/s13756-019-0618-z. PMID: 31649818.",
    "torres2020": "Torres NF, Solomon VP, Middleton LE. Identifying the commonly used antibiotics for self-medication in urban Mozambique: a qualitative study. BMJ Open. 2020;10(12):e041323. doi:10.1136/bmjopen-2020-041323. PMID: 33371035.",
    "torres2020farm": "Torres NF, Solomon VP, Middleton LE. Pharmacists' practices for non-prescribed antibiotic dispensing in Mozambique. Pharm Pract (Granada). 2020 Jul-Set;18(3):1965. Epub 2020 Ago 18. doi:10.18549/PharmPract.2020.3.1965. PMID: 32922571.",
    "do2021": "Do NTT, Vu HTL, Nguyen CTK, Punpuing S, Khan WA, Gyapong M, et al. Community-based antibiotic access and use in six low-income and middle-income countries: a mixed-method approach. Lancet Glob Health. 2021;9(5):e610-e619. doi:10.1016/S2214-109X(21)00024-3. PMID: 33713630.",
    "cambaco2020": "Cambaco O, Alonso Menendez Y, Kinsman J, Sigaúque B, Wertheim H, Do N, et al. Community knowledge and practices regarding antibiotic use in rural Mozambique: where is the starting point for prevention of antibiotic resistance?. BMC Public Health. 2020;20(1):1183. doi:10.1186/s12889-020-09243-x. PMID: 32727445.",
    "rafael2026": "Rafael EJ, Barbosa F, Rugunate S, Hlashwayo DF. Self-medication with herbal remedies and pharmaceuticals for COVID-19 among healthcare students in Maputo. Sci Rep. 2026;16(1). doi:10.1038/s41598-026-53105-2. PMID: 42304086.",
    "ine2021": "Instituto Nacional de Estatística. IV Recenseamento Geral da População e Habitação 2017: resultados definitivos, província de Nampula [Internet]. Nampula: Instituto Nacional de Estatística; 2021 [citado 2026 Set 19]. Disponível em: http://www.sina.gov.mz/wp-content/uploads/2024/05/NAMPULA-RESUTADOS-DEFINITIVOS-DO-CENSO-2017.pdf",
    "unilurio2026": "Universidade Lúrio. Cursos de graduação [Internet]. Nampula: Universidade Lúrio; 2026 [citado 2026 Set 19]. Disponível em: https://www.unilurio.ac.mz/unilurio/pt/ensino/cursos/graduacao",
    "mandane2022": "Mandane ASE, Noormahomed EV. Educação comunitária na promoção da saúde como uma estratégia de formação dos profissionais de saúde. BJDV. 2022;8(11):75603-75613. doi:10.34117/bjdv8n11-324",
    # -- enquadramento normativo mocambicano
    "lei12de2017": "República de Moçambique. Lei n.º 12/2017, de 8 de Setembro: Lei do medicamento, vacinas e outros produtos biológicos para o uso humano. Boletim da República, I Série, n.º 141 [Internet]. Maputo: Imprensa Nacional de Moçambique; 2017 [citado 2026 Set 19]. Disponível em: https://anarme.gov.mz/download/lei-12-2017-de-8-de-setembro-lei-de-medicamento/",
    "misau2023lnme": "Ministério da Saúde. Diploma Ministerial n.º 52/2023, de 19 de Abril: aprova a Lista Nacional de Medicamentos Essenciais. Boletim da República, I Série, n.º 75 [Internet]. Maputo: Imprensa Nacional de Moçambique; 2023 [citado 2026 Set 19]. Disponível em: https://anarme.gov.mz/download/diploma-ministerial-52-2023-de-19-de-abril-lista-nacional-de-medicamentos-essenciais/",
    "misau2023prescricao": "Ministério da Saúde. Diplomas Ministeriais n.º 2, 3 e 4/2023: normas de prescrição e dispensa, Sistema Nacional de Farmacovigilância e reconhecimento de outras autoridades reguladoras [Internet]. Maputo: Autoridade Nacional Reguladora de Medicamento; 2023 [citado 2026 Set 19]. Disponível em: https://anarme.gov.mz/download/dm-2-3-e-4-2023-normas-de-prescricao-e-dispensa-sistema-nacional-de-farmacovigilancia-e-reconhecimento-de-outras-reguladoras/",
    "misau2019": "Ministério da Saúde; Ministério da Agricultura e Segurança Alimentar. Plano Nacional de Acção Contra a Resistência Antimicrobiana 2019-2023 [Internet]. Maputo: Ministério da Saúde; 2019 [citado 2026 Set 19]. Disponível em: https://cdn.who.int/media/docs/default-source/antimicrobial-resistance/amr-spc-npm/nap-library/nap_20_11_2018---mozambique---2019-2023.pdf",
    "lei3de2023": "República de Moçambique. Lei n.º 3/2023, de 8 de Junho: Lei de Investigação em Saúde Humana [Internet]. Maputo: Imprensa Nacional de Moçambique; 2023 [citado 2026 Set 19]. Disponível em: https://anarme.gov.mz/download/lei-3-2023-de-8-de-junho-lei-de-investigacao-em-saude-humana/",
    # -- estudos empiricos com estudantes (estado da arte)
    "tesfaye2020": "Tesfaye ZT, Ergena AE, Yimer BT. Self-Medication among Medical and Nonmedical Students at the University of Gondar, Northwest Ethiopia: A Cross-Sectional Study. Scientifica (Cairo). 2020;2020:4021586. doi:10.1155/2020/4021586. PMID: 32676214.",
    "zewdie2020": "Zewdie S, Andargie A, Kassahun H. Self-Medication Practices among Undergraduate University Students in Northeast Ethiopia. Risk Manag Healthc Policy. 2020;13:1375-1381. doi:10.2147/RMHP.S266329. PMID: 32922102.",
    "zeru2020": "Zeru N, Fetene D, Geberu DM, Melesse AW, Atnafu A. Self-Medication Practice and Associated Factors Among University of Gondar College of Medicine and Health Sciences Students: A Cross-Sectional Study. Patient Prefer Adherence. 2020;14:1779-1790. doi:10.2147/PPA.S274634. PMID: 33061320.",
    "kifle2021": "Kifle ZD, Mekuria AB, Anteneh DA, Enyew EF. Self-medication Practice and Associated Factors among Private Health Sciences Students in Gondar Town, North West Ethiopia. A Cross-sectional Study. Inquiry. 2021;58:469580211005188. doi:10.1177/00469580211005188. PMID: 33759621.",
    "shitindi2023": "Shitindi L, Issa O, Poyongo BP, Horumpende PG, Kagashe GA, Sangeda RZ. Comparison of knowledge, attitude, practice and predictors of self-medication with antibiotics among medical and non-medical students in Tanzania. Front Pharmacol. 2023;14:1301561. doi:10.3389/fphar.2023.1301561. PMID: 38273839.",
    "chuwa2021": "Chuwa BB, Njau LA, Msigwa KI, Shao E. Prevalence and factors associated with self medication with antibiotics among University students in Moshi Kilimanjaro Tanzania. Afr Health Sci. 2021;21(2):633-639. doi:10.4314/ahs.v21i2.19. PMID: 34795717.",
    "amponsah2022": "Amponsah SK, Odamtten G, Adams I, Kretchy IA. A comparative analysis of pattern and attitude towards self-medication among pharmacy and non-pharmacy students in University of Ghana. Pan Afr Med J. 2022;41:254. PMID: 35734338.",
    "akandesholabi2021": "Akande-Sholabi W, Ajamu AT, Adisa R. Prevalence, knowledge and perception of self-medication practice among undergraduate healthcare students. J Pharm Policy Pract. 2021;14(1):49. doi:10.1186/s40545-021-00331-w. PMID: 34112249.",
    "esan2018": "Esan DT, Fasoro AA, Odesanya OE, Esan TO, Ojo EF, Faeji CO. Assessment of Self-Medication Practices and Its Associated Factors among Undergraduates of a Private University in Nigeria. J Environ Public Health. 2018;2018:5439079. doi:10.1155/2018/5439079. PMID: 30671097.",
    "ikwara2023": "Ikwara AE, Atwijukiire H. Self-medication and medication storage practices among Lira University students in Lira city, Northern Uganda. Front Public Health. 2023;11:1259279. doi:10.3389/fpubh.2023.1259279. PMID: 38026339.",
    "tuyishimire2019": "Tuyishimire J, Okoya F, Adebayo AY, Humura F, Lucero-Prisno Iii DE. Assessment of self-medication practices with antibiotics among undergraduate university students in Rwanda. Pan Afr Med J. 2019;33:307. doi:10.11604/pamj.2019.33.307.18139. PMID: 31692864.",
    "gebregziabher2024": "Gebregziabher NK, Netsereab TB, Franchesko BT, Ghebreamlak HH, Yihdego NM. Prevalence of self-medication practices with antibiotics and associated factors among students in five colleges in Eritrea: a cross-sectional study. Antimicrob Resist Infect Control. 2024;13(1):106. doi:10.1186/s13756-024-01466-6. PMID: 39300551.",
    "mudenda2023": "Mudenda S, Chisha P, Chabalenge B, Daka V, Mfune RL, Kasanga M, et al. Antimicrobial stewardship: knowledge, attitudes and practices regarding antimicrobial use and resistance among non-healthcare students at the University of Zambia. JAC Antimicrob Resist. 2023;5(6):dlad116. doi:10.1093/jacamr/dlad116. PMID: 37954639.",
    "helal2017": "Helal RM, Abou-ElWafa HS. Self-Medication in University Students from the City of Mansoura, Egypt. J Environ Public Health. 2017;2017:9145193. doi:10.1155/2017/9145193. PMID: 28479921.",
    "hassan2025": "Hassan NM, Koabar SMM. Self-medication pattern among medical students in Middle Delta, Egypt. BMC Med Educ. 2025;25(1):99. doi:10.1186/s12909-025-06678-x. PMID: 39838435.",
    "alkubaisi2022": "Al-Kubaisi KA, Hassanein MM, Abduelkarem AR. Prevalence and associated risk factors of self-medication with over-the-counter medicines among university students in the United Arab Emirates. Pharm Pract (Granada). 2022;20(3):2679. doi:10.18549/PharmPract.2022.3.2679. PMID: 36733517.",
    "enuagwuna2025": "Enuagwuna FC, Tobin-West CI, Dappa FA, Bethel TC. Prevalence and Pattern of Analgesic Abuse Among Undergraduate Students of University of Port Harcourt, Rivers State, Nigeria. Niger Med J. 2025;66(1):142-155. doi:10.71480/nmj.v66i1.647. PMID: 40309525.",
    # -- classificacao de medicamentos
    "whocc2026": "WHO Collaborating Centre for Drug Statistics Methodology. Guidelines for ATC classification and DDD assignment [Internet]. Oslo: Norwegian Institute of Public Health; 2026 [citado 2026 Set 19]. Disponível em: https://atcddd.fhi.no/atc_ddd_index_and_guidelines/guidelines/",
    "omsaware2025": "World Health Organization. The selection and use of essential medicines, 2025: WHO AWaRe (Access, Watch, Reserve) classification of antibiotics for evaluation and monitoring of use [Internet]. Geneva: World Health Organization; 2025 [citado 2026 Set 19]. Disponível em: https://www.who.int/publications/i/item/B09489",
    # -- metodos, estatistica, relato e etica
    "almanasreh2019": "Almanasreh E, Moles R, Chen TF. Evaluation of methods used for estimating content validity. Res Social Adm Pharm. 2019;15(2):214-221. doi:10.1016/j.sapharm.2018.03.066. PMID: 29606610.",
    "taber2018": "Taber KS. The Use of Cronbach's Alpha When Developing and Reporting Research Instruments in Science Education. Res Sci Educ. 2018;48(6):1273-1296. doi:10.1007/s11165-016-9602-2",
    "mchugh2012": "McHugh ML. Interrater reliability: the kappa statistic. Biochem Med (Zagreb). 2012;22(3):276-82. PMID: 23092060.",
    "in2020": "In J, Kang H, Kim JH, Kim TK, Ahn EJ, Lee DK, et al. Tips for troublesome sample-size calculation. Korean J Anesthesiol. 2020;73(2):114-120. doi:10.4097/kja.19497. PMID: 32229812.",
    "chen2018": "Chen W, Qian L, Shi J, Franklin M. Comparing performance between log-binomial and robust Poisson regression models for estimating risk ratios under model misspecification. BMC Med Res Methodol. 2018;18(1):63. doi:10.1186/s12874-018-0519-5. PMID: 29929477.",
    "peduzzi1996": "Peduzzi P, Concato J, Kemper E, Holford TR, Feinstein AR. A simulation study of the number of events per variable in logistic regression analysis. J Clin Epidemiol. 1996;49(12):1373-9. doi:10.1016/s0895-4356(96)00236-3. PMID: 8970487.",
    "sharma2021": "Sharma A, Minh Duc NT, Luu Lam Thang T, Nam NH, Ng SJ, Abbas KS, et al. A Consensus-Based Checklist for Reporting of Survey Studies (CROSS). J Gen Intern Med. 2021;36(10):3179-3187. doi:10.1007/s11606-021-06737-1. PMID: 33886027.",
    "vonelm2007": "von Elm E, Altman DG, Egger M, Pocock SJ, Gøtzsche PC, Vandenbroucke JP. The Strengthening the Reporting of Observational Studies in Epidemiology (STROBE) statement: guidelines for reporting observational studies. Lancet. 2007;370(9596):1453-7. doi:10.1016/S0140-6736(07)61602-X. PMID: 18064739.",
    "wma2025": "World Medical Association. World Medical Association Declaration of Helsinki: Ethical Principles for Medical Research Involving Human Participants. JAMA. 2025;333(1):71-74. doi:10.1001/jama.2024.21972. PMID: 39425955.",
}

SEMINAIS = {
    "oms2000": ("Documento da OMS que fixa a definição de automedicação usada "
                "internacionalmente e os critérios de classificação dos "
                "medicamentos para uso sem receita; continua a ser a "
                "referência citada pelas revisões recentes."),
    "peduzzi1996": ("Estudo de simulação que fundamenta a regra de pelo "
                    "menos 10 eventos por variável nos modelos de regressão "
                    "para desfechos binários."),
    "vonelm2007": ("Declaração original STROBE, norma de relato dos estudos "
                   "observacionais ainda em vigor."),
    "mchugh2012": ("Artigo de referência sobre a interpretação do kappa de "
                   "Cohen em investigação em saúde, usado para a "
                   "concordância entre codificadores e no teste-reteste."),
    "torres2020farm": ("Falso positivo do validador: o artigo é de 2020 e "
                       "1965 é o número do artigo na revista, não o ano; "
                       "estudo moçambicano sobre a dispensa de antibióticos "
                       "sem receita, essencial para o enquadramento local."),
}

# ----------------------------------------------------- 1. introducao --------
INTRODUCAO = [
    P("A Organização Mundial da Saúde (OMS) define automedicação como a "
      "selecção e o uso de medicamentos pelo próprio indivíduo para tratar "
      "doenças ou sintomas que ele próprio reconhece {oms2000}. A prática "
      "tem uma face útil, porque permite resolver queixas ligeiras com "
      "medicamentos seguros e poupa recursos aos serviços de saúde, e uma "
      "face de risco, porque o uso sem orientação profissional se associa a "
      "reacções adversas, interacções, atraso no diagnóstico e resistência "
      "aos antimicrobianos (RAM) {baracaldo2022}. Os estudantes "
      "universitários são um grupo particularmente exposto: vivem muitas "
      "vezes longe da família, têm pouco tempo para consultas e acesso fácil "
      "a informação e a farmácias. Uma meta-análise de 89 estudos, com "
      "60.938 estudantes de vários continentes, estimou uma prevalência "
      "global de automedicação de 70,1%, com intervalo de confiança a 95% "
      "(IC 95%) de 64,3% a 75,4%, mais alta nas estudantes do sexo feminino "
      "e muito superior nos estudantes de medicina (97,2%) do que nos de "
      "outras áreas (44,7%) {behzadifar2020}."),
    P("A automedicação com antibióticos merece atenção própria. A revisão "
      "sistemática mais recente, com 71 estudos e 63.251 participantes, "
      "estimou uma prevalência global de 43,0%, que sobe para 55,2% na "
      "África subsariana e para 62,1% entre estudantes; o conhecimento "
      "prévio dos antibióticos, a experiência anterior bem-sucedida e a "
      "percepção de que a doença é ligeira foram os motivos mais invocados "
      "{gashaw2025}. Este comportamento alimenta a RAM, que em 2021 esteve "
      "associada a 4,71 milhões de mortes e foi directamente responsável por "
      "1,14 milhões, com projecção de 1,91 milhões de mortes atribuíveis em "
      "2050 {gbd2024}. Nos países de rendimento baixo e médio, as fontes de "
      "antibióticos sem receita identificadas foram as farmácias, a família "
      "e os amigos, as receitas antigas e as sobras guardadas em casa "
      "{torres2021}."),
    P("Na África subsariana, a automedicação cruza-se com a malária. Em "
      "2024 registaram-se cerca de 282 milhões de casos e 610 mil mortes por "
      "malária no mundo, 95% dos quais na Região Africana da OMS, e a "
      "resistência parcial à artemisinina já foi confirmada na Eritreia, no "
      "Ruanda, no Uganda e na Tanzânia {omsmalariaft2025}. Moçambique "
      "pertence ao grupo de onze países africanos de elevado fardo que "
      "concentram cerca de dois terços dos casos e das mortes "
      "{omsmalaria2025}. Uma meta-análise de 27 estudos estimou em 55,3% a "
      "prevalência da automedicação com antimaláricos na região, "
      "impulsionada pelo baixo rendimento, pela disponibilidade de "
      "medicamentos baratos sem receita e pelo difícil acesso aos serviços "
      "formais {amaka2025}. Entre estudantes "
      "universitários africanos, a automedicação com antibióticos atingiu "
      "55,3%, o valor mais alto entre as regiões analisadas numa "
      "meta-análise de países de rendimento baixo e médio {xu2019}, e a "
      "automedicação em geral foi estimada em 49,4% entre universitários "
      "etíopes {fetensa2021}."),
    P("Em Moçambique, os antibióticos estão classificados como "
      "medicamentos sujeitos a receita, mas a regra não é aplicada com "
      "rigor, o que permite ao público obtê-los sem prescrição "
      "{torres2019}. Num inquérito a 1.091 adultos de Maputo, 20,9% tinham "
      "usado antibióticos sem receita e 87,3% destes compraram-nos em "
      "farmácias {mate2019}; em nove farmácias privadas da mesma cidade, 15 "
      "de 17 farmacêuticos admitiram dispensar antibióticos sem receita "
      "{torres2020farm}. Um estudo em seis países de rendimento baixo e "
      "médio encontrou, porém, uma proporção de antibióticos dispensados "
      "sem receita de 8,0% em Moçambique, muito abaixo da do Vietname "
      "(55,2%), o que mostra que o fenómeno varia com o contexto e precisa "
      "de ser medido localmente {do2021}. Entre estudantes, o único estudo "
      "moçambicano encontrado envolveu 390 estudantes de cursos da saúde de "
      "Maputo: 83,6% automedicaram-se para a doença por coronavírus 2019 "
      "(COVID-19), 34,9% usaram medicamentos convencionais e a azitromicina "
      "foi o medicamento convencional mais referido (20,3%) {rafael2026}."),
    P("Nampula é a província mais populosa do país, com 5.758.920 "
      "habitantes no recenseamento de 2017, 20,6% da população nacional "
      "{ine2021}. Na cidade de Nampula, a Universidade Lúrio (UniLúrio) "
      "forma estudantes da Faculdade de Ciências de Saúde (FCS), da "
      "Faculdade de Arquitectura e Planeamento Físico (FAPF) e da UniLúrio "
      "Business School (UBS) {unilurio2026}. Muitos destes estudantes são já "
      "hoje conselheiros informais das suas famílias sobre "
      "medicamentos. A pesquisa bibliográfica feita para este protocolo não "
      "encontrou nenhum estudo publicado sobre a automedicação de "
      "estudantes universitários em Nampula nem na região Norte do país."),
    P("A literatura também não responde de forma consistente à pergunta "
      "sobre o efeito da formação em saúde. Há estudos em que os estudantes "
      "da saúde se automedicam mais {behzadifar2020,amponsah2022}, outros "
      "em que se automedicam menos {tesfaye2020,shitindi2023} e outros sem "
      "diferença {chuwa2021}. A comparação entre cursos da mesma "
      "universidade, sujeitos ao mesmo mercado de medicamentos, é o modo "
      "mais directo de esclarecer esta questão no contexto moçambicano. Por "
      "isso, o presente estudo pretende avaliar a prevalência, o padrão e os "
      "determinantes da automedicação entre os estudantes de licenciatura "
      "da UniLúrio na cidade de Nampula, comparando os cursos da área da "
      "saúde com os de outras áreas."),
]

# ----------------------------------------------------- 2. problema ----------
PROBLEMA = [
    P("Os estudantes da UniLúrio em Nampula vivem numa cidade onde os "
      "medicamentos circulam por farmácias privadas, por farmácias "
      "públicas, por vendedores informais e pelas redes de familiares e "
      "colegas. A Lei do Medicamento determina que os medicamentos só podem "
      "ser vendidos mediante receita, com excepção dos que constam de uma "
      "lista de medicamentos não sujeitos a receita médica {lei12de2017}, "
      "mas os estudos de Maputo mostram que os antibióticos se obtêm sem "
      "receita pelo nome genérico, pela embalagem vazia, pela descrição dos "
      "sintomas, com receitas antigas ou por partilha entre familiares e "
      "vizinhos {torres2019}. É plausível que o mesmo aconteça em "
      "Nampula, mas não há dados que o confirmem nem que mostrem com que "
      "frequência os estudantes recorrem a estes circuitos."),
    P("A consequência do problema é dupla. No plano individual, a "
      "automedicação com antimaláricos sem teste de confirmação contraria a "
      "recomendação de confirmar parasitologicamente todos os casos "
      "suspeitos de malária {omsmalariaft2025} e pode ocultar outras causas "
      "de febre; a automedicação com antibióticos, frequentemente amoxicilina "
      "e cotrimoxazol {torres2020}, expõe a doses e durações inadequadas; e "
      "os analgésicos, o grupo mais usado pelos estudantes em vários estudos "
      "{tesfaye2020,zewdie2020}, causam danos quando tomados em excesso ou "
      "sem atenção às contra-indicações. Num estudo com estudantes de "
      "medicina egípcios, 30,2% referiram efeitos adversos da automedicação "
      "{hassan2025}. No plano colectivo, cada tratamento "
      "antibiótico desnecessário contribui para a RAM {gbd2024}."),
    P("O problema tem uma dimensão formativa própria. Os estudantes da "
      "saúde adquirem conhecimentos de farmacologia que podem torná-los mais "
      "prudentes ou, pelo contrário, mais confiantes para se tratarem sem "
      "consulta; o conhecimento dos medicamentos foi, aliás, o motivo mais "
      "invocado para a automedicação com antibióticos na revisão global "
      "mais recente {gashaw2025}. O Plano Nacional de Acção Contra a "
      "Resistência Antimicrobiana prevê a inclusão da RAM nos currículos dos "
      "cursos de saúde e campanhas dirigidas aos estudantes {misau2019}, "
      "mas a UniLúrio não dispõe de uma linha de base que lhe diga quantos "
      "dos seus estudantes se automedicam, com que medicamentos, onde os "
      "obtêm e por que razão, nem se a formação em saúde muda esse padrão."),
    P("Falta, por isso, saber qual é a prevalência da automedicação entre "
      "os estudantes da UniLúrio em Nampula, que medicamentos, fontes e "
      "motivos a caracterizam, em que medida difere entre as duas áreas de "
      "formação e que factores sociodemográficos, académicos e de acesso "
      "se lhe associam. Sem esta informação, as intervenções "
      "educativas e de serviços de saúde ao estudante continuarão a ser "
      "desenhadas com base em estudos de outros países."),
]
PERGUNTA = ("Qual é a prevalência da automedicação nos seis meses anteriores "
            "ao inquérito entre os estudantes de licenciatura da "
            "Universidade Lúrio na cidade de Nampula, que medicamentos, "
            "fontes e motivos a caracterizam, e em que medida difere entre "
            "os cursos da área da saúde e os de outras áreas?")
DELIMITACAO = [
    P("O estudo decorre na cidade de Nampula, nas unidades orgânicas da "
      "UniLúrio que aí leccionam cursos de licenciatura: a FCS, no Campus de "
      "Marrere, com os cursos de Medicina, Medicina Dentária, Farmácia, "
      "Nutrição, Optometria, Enfermagem, Administração e Gestão em Saúde e "
      "Psicologia Clínica; a FAPF, com os cursos de Arquitectura e "
      "Planeamento Físico e de Urbanismo e Ordenamento do Território; e a "
      "UBS, também no Campus de Marrere, com os cursos de Contabilidade, "
      "Fiscalidade e Auditoria, de Economia e de Gestão Empresarial "
      "{unilurio2026}. A população é constituída pelos estudantes de "
      "licenciatura, com 18 ou mais anos, matriculados no primeiro semestre "
      "do ano lectivo de 2027. A recolha de dados decorre em Março e Abril "
      "de 2027 e o período de referência da automedicação são os seis meses "
      "anteriores ao preenchimento do questionário."),
    P("O objecto do estudo é a automedicação com medicamentos "
      "industrializados, isto é, o uso de pelo menos um medicamento sem "
      "prescrição nem consulta de um profissional de saúde habilitado para "
      "o problema em causa, na acepção operacional fixada na revisão da "
      "literatura. Ficam fora da definição principal "
      "os remédios tradicionais e à base de plantas, registados à parte "
      "como variável descritiva, as alterações de dose de tratamentos "
      "prescritos em curso e o uso de substâncias sem finalidade "
      "terapêutica. Ficam igualmente fora os estudantes da Faculdade de "
      "Ciências Sociais e Humanas, na Ilha de Moçambique, e das faculdades "
      "de Pemba e de Unango, os estudantes de pós-graduação, a observação "
      "da dispensa nas farmácias e a verificação clínica dos episódios "
      "relatados."),
]

# ----------------------------------------------------- 3. objectivos --------
OBJECTIVO_GERAL = (
    "Avaliar a prevalência, o padrão e os determinantes da automedicação "
    "entre os estudantes de licenciatura da Universidade Lúrio na cidade de "
    "Nampula, comparando os cursos da área da saúde com os de outras áreas, "
    "em 2027.")
OBJECTIVOS_ESPECIFICOS = [
    "Determinar a prevalência da automedicação nos seis meses anteriores ao "
    "inquérito, no conjunto dos estudantes e por área de formação, curso e "
    "ano curricular.",
    "Identificar os grupos terapêuticos e os medicamentos usados em "
    "automedicação, com destaque para analgésicos e anti-inflamatórios, "
    "antibióticos e antimaláricos, as queixas que a motivaram e as práticas "
    "de uso no episódio mais recente.",
    "Descrever as fontes de obtenção dos medicamentos, as fontes de "
    "informação e os motivos invocados para a automedicação.",
    "Comparar a prevalência da automedicação, e da automedicação com "
    "antibióticos e com antimaláricos, entre os estudantes dos cursos da "
    "área da saúde e os dos cursos de outras áreas.",
    "Analisar a associação entre a automedicação e os factores "
    "sociodemográficos, académicos, de acesso aos medicamentos e de "
    "conhecimento sobre o uso responsável de medicamentos.",
]

# ----------------------------------------------------- 4. hipoteses ---------
HIPOTESES_INTRO = [
    P("As hipóteses referem-se às componentes analíticas, isto é, aos "
      "objectivos específicos 4 e 5. Como a literatura aponta em sentidos "
      "opostos quanto ao efeito da formação em saúde "
      "{behzadifar2020,tesfaye2020}, as hipóteses alternativas são "
      "bilaterais e serão testadas ao nível de significância de 5%."),
]
HIPOTESES = [
    ("H0 (objectivo específico 4)",
     "a prevalência da automedicação nos seis meses anteriores não difere "
     "entre os estudantes dos cursos da área da saúde e os dos cursos de "
     "outras áreas."),
    ("H1 (objectivo específico 4)",
     "a prevalência da automedicação nos seis meses anteriores difere entre "
     "os estudantes dos cursos da área da saúde e os dos cursos de outras "
     "áreas."),
    ("H0 (objectivo específico 4, antibióticos e antimaláricos)",
     "a prevalência da automedicação com antibióticos, e com antimaláricos, "
     "não difere entre as duas áreas de formação."),
    ("H1 (objectivo específico 4, antibióticos e antimaláricos)",
     "a prevalência da automedicação com antibióticos, ou com "
     "antimaláricos, difere entre as duas áreas de formação."),
    ("H0 (objectivo específico 5)",
     "o sexo, a idade, o ano curricular, a residência, o rendimento "
     "disponível, a existência de medicamentos guardados, a proximidade de "
     "uma farmácia e o nível de conhecimento não se associam à "
     "automedicação, depois de ajustamento mútuo e para a área de formação."),
    ("H1 (objectivo específico 5)",
     "pelo menos um destes factores associa-se à automedicação, depois de "
     "ajustamento mútuo e para a área de formação."),
]
QUESTOES = [
    "Qual é a prevalência da automedicação nos seis meses anteriores ao "
    "inquérito entre os estudantes da UniLúrio em Nampula, no conjunto e por "
    "curso e ano curricular?",
    "Que grupos terapêuticos e que medicamentos são usados em "
    "automedicação, para que queixas e com que práticas de dose, duração e "
    "leitura do folheto informativo?",
    "Onde obtêm os estudantes os medicamentos, quem os aconselha e por que "
    "razões se automedicam?",
]

# ----------------------------------------------------- 5. justificativa -----
JUSTIFICATIVA_INTRO = [
    P("O estudo justifica-se pela combinação de três condições: a "
      "automedicação é frequente entre universitários em todo o mundo e em "
      "África {behzadifar2020,fetensa2021}; envolve medicamentos cujo uso "
      "indevido tem consequências individuais e colectivas, como os "
      "antibióticos e os antimaláricos {gashaw2025,amaka2025}; e não existe "
      "informação sobre esta prática entre os estudantes da UniLúrio, uma "
      "instituição que forma profissionais de saúde para o Norte de "
      "Moçambique. As relevâncias científica, académica, social e política "
      "são desenvolvidas a seguir."),
]
JUSTIFICATIVA = {
    "cientifica": [
        P("O estudo produz a primeira estimativa da prevalência da "
          "automedicação entre universitários de Nampula e uma das poucas de "
          "Moçambique, onde a evidência sobre antibióticos sem receita vem "
          "de adultos e farmácias de Maputo {mate2019,torres2019} e a única "
          "evidência com estudantes se refere à doença por coronavírus 2019 "
          "{rafael2026}. Acrescenta a comparação entre áreas de formação "
          "dentro da mesma universidade, com poder estatístico calculado "
          "para esse fim, numa questão em que os estudos africanos divergem "
          "{tesfaye2020,amponsah2022,chuwa2021}."),
        P("A codificação dos medicamentos pela classificação Anatómica "
          "Terapêutica Química (ATC) e dos antibióticos pelos grupos Acesso, "
          "Vigilância e Reserva (AWaRe) da OMS {whocc2026,omsaware2025} "
          "torna os resultados comparáveis com estudos de utilização de "
          "medicamentos de outros países e permite perceber em que grupos, "
          "definidos pela OMS segundo o impacto de cada antibiótico na "
          "resistência, se concentram os antibióticos usados sem receita."),
    ],
    "academica": [
        P("Para a FCS, os resultados servem de diagnóstico para rever os "
          "conteúdos de farmacologia, de farmácia clínica e de saúde pública "
          "sobre uso responsável de medicamentos e RAM, em linha com o "
          "currículo padrão previsto no plano nacional {misau2019}. Para a "
          "FAPF e a UBS, mostram se os seus estudantes precisam de acções de "
          "educação para a saúde que hoje não constam dos seus planos de "
          "estudo. Para o curso de Farmácia, o protocolo constitui um "
          "exercício completo de farmacoepidemiologia descritiva e analítica, "
          "com validação de instrumento, amostragem estratificada e análise "
          "ponderada."),
    ],
    "social": [
        P("Os estudantes universitários são intermediários entre o sistema "
          "de saúde e as famílias, sobretudo quando estudam cursos da saúde. "
          "Hábitos de automedicação adquiridos na universidade tendem a "
          "reproduzir-se na orientação que dão aos familiares e, no caso dos "
          "futuros profissionais, na prática clínica e na dispensa "
          "{rafael2026}. O programa Um Estudante, Uma Família, da FCS, "
          "assenta nessa ponte entre os estudantes e as famílias "
          "{mandane2022}. Conhecer esses hábitos é o primeiro passo para os "
          "corrigir. Todos os estudantes convidados, participem ou não, "
          "recebem um folheto sobre automedicação responsável, pelo que o "
          "estudo tem um benefício imediato para a comunidade académica."),
    ],
    "politica": [
        P("A Lei do Medicamento, a Lista Nacional de Medicamentos "
          "Essenciais (LNME) e as normas de prescrição e "
          "dispensa de 2023 definem quem pode vender e dispensar cada "
          "medicamento {lei12de2017,misau2023lnme,misau2023prescricao}. Os "
          "resultados sobre as fontes de obtenção indicam onde essas regras "
          "falham na prática e oferecem à Autoridade Nacional Reguladora de "
          "Medicamento (ANARME) e ao Ministério da Saúde (MISAU) dados "
          "concretos para a inspecção e para a comunicação com o público. "
          "Para a UniLúrio, apoiam decisões sobre os serviços de saúde ao "
          "estudante e sobre campanhas de sensibilização dirigidas a esta "
          "população, previstas no plano nacional contra a RAM "
          "{misau2019}."),
    ],
}

# ----------------------------------------------------- 6. revisao -----------
REVISAO = [
    ("Conceito de automedicação e definição operacional adoptada", [
        P("Na definição da OMS, a automedicação é a selecção e o uso de "
          "medicamentos pelo próprio indivíduo para tratar doenças ou "
          "sintomas por ele reconhecidos {oms2000}. O mesmo documento "
          "enquadra a automedicação responsável, que assenta em medicamentos "
          "com perfil de segurança conhecido, aprovados para uso sem receita "
          "e acompanhados de informação suficiente para o utilizador. A "
          "definição é, porém, aplicada de forma muito diversa: uma revisão "
          "de âmbito que reuniu 65 estudos encontrou grande heterogeneidade, "
          "com definições baseadas no modo de obtenção do medicamento, na "
          "ausência de um profissional de saúde, na fonte do medicamento e "
          "no motivo do uso, e com autores que incluem também a "
          "reutilização de medicamentos guardados, a partilha e o empréstimo "
          "de medicamentos, o autocuidado e a não adesão a uma prescrição "
          "{baracaldo2022}. Esta diversidade explica "
          "parte da variação das prevalências publicadas e obriga cada "
          "estudo a declarar com precisão o que mede."),
        P("A legislação moçambicana oferece o quadro de referência para a "
          "distinção entre uso legítimo e uso indevido. A Lei n.º 12/2017 "
          "considera medicamentos não sujeitos a receita médica os que "
          "constam de uma lista aprovada e actualizada periodicamente pela "
          "autoridade reguladora, que podem ser dispensados sem prescrição, "
          "admite que estabelecimentos da rede comercial geral, "
          "devidamente licenciados, vendam uma lista ainda mais restrita e "
          "determina que todos os restantes medicamentos só podem ser "
          "vendidos e dispensados mediante receita {lei12de2017}. A "
          "automedicação com um analgésico de venda livre e a automedicação "
          "com um antibiótico, sujeito a receita, são portanto situações "
          "diferentes do ponto de vista legal e sanitário, ainda que ambas "
          "caibam na definição da OMS."),
        P("Para este estudo, considera-se automedicação o uso, pelo "
          "estudante e para si próprio, de pelo menos um medicamento "
          "industrializado sem prescrição nem consulta de um profissional "
          "habilitado a prescrever para o problema em causa, nos seis meses "
          "anteriores ao inquérito. Incluem-se os medicamentos comprados sem "
          "receita, mesmo quando aconselhados na farmácia, as sobras "
          "guardadas em casa, os medicamentos cedidos por familiares ou "
          "colegas e a reutilização de uma receita antiga; excluem-se os "
          "tratamentos prescritos em curso, os remédios tradicionais e à "
          "base de plantas, registados à parte, e os medicamentos "
          "administrados por um profissional. A automedicação com "
          "antibióticos e a automedicação com antimaláricos são "
          "subconjuntos desta definição, identificados pelo nome do "
          "medicamento e confirmados pela classificação ATC {whocc2026}. O conselho do farmacêutico "
          "ou do técnico de farmácia não retira o episódio da definição, mas "
          "é registado como fonte de informação, o que permite distinguir a "
          "automedicação orientada da totalmente autónoma."),
    ]),
    ("Magnitude da automedicação em estudantes universitários", [
        P("A automedicação é, entre os estudantes universitários, mais "
          "frequente do que na população geral. A meta-análise de "
          "Behzadifar e colaboradores estimou 70,1% em 60.938 estudantes de "
          "89 estudos, com risco maior nas mulheres, com odds ratio (OR) de "
          "1,45 e IC 95% de 1,17 a 1,79 {behzadifar2020}. Para os "
          "antibióticos, a revisão global mais recente identificou os "
          "estudantes como o grupo com maior prevalência, 62,1% "
          "{gashaw2025}, e uma meta-análise restrita a universitários de "
          "países de rendimento baixo e médio estimou 46,0%, com valores "
          "entre 11,1% no Brasil e 90,7% no Congo {xu2019}."),
        P("Em África, os dados mais sistematizados vêm da Etiópia. Entre "
          "universitários etíopes, 13 estudos com 5.377 participantes "
          "deram uma prevalência combinada de 49,41%, com extremos de 19,87% "
          "na Universidade de Gondar e de 77,01% na Universidade de Arsi "
          "{fetensa2021}. Na população etíope em geral, 27 estudos com 9.586 "
          "participantes estimaram 44,0%, e os profissionais de saúde e os "
          "estudantes foram os grupos que mais se automedicavam "
          "{sisay2018}. A amplitude destes valores reflecte diferenças de "
          "definição, de período recordatório e de população, o que torna "
          "arriscado transpor uma estimativa estrangeira para Nampula."),
        P("Em Moçambique, a evidência é sobretudo qualitativa ou "
          "comunitária. Em Maputo, 20,9% de 1.091 adultos tinham usado "
          "antibióticos sem receita {mate2019}; no distrito semi-rural da "
          "Manhiça, os entrevistados relataram automedicação, partilha de "
          "medicamentos e interrupção de tratamentos {cambaco2020}; e o "
          "estudo em seis países que incluiu Moçambique encontrou 8,0% de "
          "antibióticos dispensados sem receita, valor baixo quando "
          "comparado com o de outros países {do2021}. O único dado com "
          "estudantes vem de 390 estudantes da saúde de Maputo, 83,6% dos "
          "quais se automedicaram para a COVID-19, sobretudo com plantas "
          "medicinais (78,7%) {rafael2026}. Não foram encontrados dados "
          "sobre a automedicação por qualquer causa entre universitários "
          "moçambicanos, nem sobre estudantes de áreas não ligadas à saúde."),
    ]),
    ("Medicamentos usados em automedicação e riscos associados", [
        P("Os analgésicos são o grupo dominante. Na Etiópia, a proporção "
          "combinada de uso de analgésicos em automedicação foi de 46,1%, a "
          "de antimicrobianos de 28,2% e a de medicamentos gastrintestinais "
          "de 14,9% {sisay2018}. Entre estudantes, os analgésicos "
          "representaram 56,28% dos medicamentos usados na Universidade de "
          "Wollo, seguidos dos antibióticos com 35,9% {zewdie2020}; numa "
          "universidade nigeriana, os analgésicos (30,1%) e os antimaláricos "
          "(30,0%) surgiram lado a lado, seguidos dos antibióticos (15,5%) "
          "{akandesholabi2021}; e noutra, 71% dos estudantes tinham usado "
          "analgésicos, 33% antimaláricos e 10,5% antibióticos sem receita "
          "no mês anterior, sendo o paracetamol o medicamento mais usado "
          "(75,1%) {esan2018}. O uso frequente não é inócuo: em Port "
          "Harcourt, 9,1% dos estudantes preenchiam critérios de abuso de "
          "analgésicos, sobretudo de paracetamol {enuagwuna2025}."),
        P("Os antibióticos são o grupo com maior impacto colectivo. Em "
          "Maputo, os clientes de farmácias usavam sobretudo amoxicilina, "
          "conhecida como «duas cores», cotrimoxazol e amoxicilina com ácido "
          "clavulânico, e em menor número tetraciclina, ciprofloxacina, "
          "azitromicina, doxiciclina, eritromicina, metronidazol e "
          "fenoximetilpenicilina, para queixas como dor de garganta, febre, "
          "tosse, gripe, corrimento vaginal, infecções urinárias, feridas e "
          "dor de dentes, muitas das quais não exigem antibiótico "
          "{torres2020}. A amoxicilina foi também o antibiótico mais usado "
          "por universitários ruandeses (59,42%) {tuyishimire2019} e "
          "tanzanianos (32,08%) {chuwa2021}. A classificação AWaRe da OMS "
          "agrupa os antibióticos em Acesso, Vigilância e Reserva segundo o "
          "seu impacto na resistência e é o instrumento proposto para "
          "monitorizar o uso e definir metas {omsaware2025}; aplicá-la aos "
          "antibióticos usados sem receita mostra se essa automedicação "
          "recai sobre moléculas de maior risco."),
        P("Os antimaláricos são o terceiro grupo de interesse em Nampula. A "
          "prevalência combinada de automedicação com antimaláricos na "
          "África subsariana foi de 55,3% {amaka2025}. O tratamento em África "
          "assenta em combinações terapêuticas com artemisinina, cujos "
          "medicamentos parceiros são sobretudo a lumefantrina e a "
          "amodiaquina, e a resistência parcial à artemisinina já "
          "foi confirmada em quatro países africanos e é suspeita noutros "
          "quatro {omsmalaria2025}. A OMS recomenda que todos os casos "
          "suspeitos sejam confirmados por microscopia ou por teste de "
          "diagnóstico rápido (TDR) antes do tratamento {omsmalariaft2025}; "
          "a automedicação salta esta etapa, trata como malária febres com "
          "outras causas e favorece doses incompletas. Os efeitos adversos "
          "da automedicação estão documentados entre estudantes: em Moshi, "
          "4,55% dos que usaram antibióticos sem receita referiram "
          "agravamento da doença e 2,67% erupções cutâneas {chuwa2021}, e em "
          "Tanta, no Egipto, 30,2% dos estudantes de medicina referiram "
          "efeitos adversos {hassan2025}."),
    ]),
    ("Fontes de obtenção, fontes de informação e motivos", [
        P("As farmácias são a principal porta de entrada. Em Maputo, 87,3% "
          "dos antibióticos usados sem receita foram comprados em farmácias, "
          "mas a proporção de uso sem receita foi muito maior entre quem "
          "comprava no mercado informal (82,6%) ou em lojas de bairro "
          "(66,7%) do que entre quem comprava em farmácias (24,6%) "
          "{mate2019}. Entre universitários, a farmácia comunitária foi a "
          "fonte de 59,4% dos estudantes nigerianos {akandesholabi2021} e de "
          "72,42% dos ruandeses que se automedicaram com antibióticos "
          "{tuyishimire2019}, e 93,4% dos estudantes da Universidade de Lira "
          "guardavam medicamentos em casa {ikwara2023}, reserva que alimenta "
          "a reutilização de sobras e a partilha."),
        P("A dispensa sem receita tem razões do lado de quem vende. Os "
          "farmacêuticos de Maputo atribuíram-na à procura e às expectativas "
          "dos clientes, às práticas de prescrição dos médicos, à pressão "
          "dos proprietários para obter lucro, à fraca fiscalização e à "
          "falta de mecanismos de responsabilização {torres2020farm}. O "
          "farmacêutico é também uma fonte de informação: entre estudantes "
          "de medicina egípcios, a recomendação do farmacêutico foi o "
          "principal determinante da escolha do medicamento (43,6%) "
          "{hassan2025}, enquanto nos Emirados Árabes Unidos os estudantes "
          "de medicina consultavam o farmacêutico menos do que os de outras "
          "áreas {alkubaisi2022}."),
        P("Os motivos repetem-se de estudo para estudo. A doença percebida "
          "como ligeira e a insatisfação com os serviços de saúde foram os "
          "motivos principais em Wollo (34,13% e 26,34%) {zewdie2020}; a "
          "atitude pouco amistosa dos profissionais da clínica "
          "universitária (27,7%), a falta de tempo (26,7%) e a distância da "
          "clínica (15,3%) foram os mais citados numa universidade "
          "nigeriana {esan2018}; e o alívio rápido dos sintomas foi o "
          "motivo de 62,2% dos estudantes de farmácia e de 56,2% dos de "
          "outros cursos no Gana {amponsah2022}. Entre os estudantes da "
          "saúde, pesa o sentimento de saber tratar-se: 22,5% dos "
          "estudantes nigerianos da saúde afirmaram ter conhecimento médico "
          "suficiente {akandesholabi2021} e, na revisão global, o "
          "conhecimento dos antibióticos foi o motivo mais frequente "
          "(46,19%) {gashaw2025}. Em Maputo, 26,8% dos adultos que usaram "
          "antibióticos sem receita consideravam desnecessário ir a uma "
          "unidade sanitária {mate2019}."),
    ]),
    ("Determinantes da automedicação e papel da formação em saúde", [
        P("O modelo comportamental de Andersen, que agrupa os determinantes "
          "do uso de cuidados em factores predisponentes, capacitantes e de "
          "necessidade, foi usado para construir o questionário de um "
          "inquérito a 2.355 universitários dos Emirados Árabes Unidos, "
          "57,5% dos quais tinham usado medicamentos de venda livre nos 90 "
          "dias anteriores {alkubaisi2022}. O mesmo modelo organiza o "
          "esquema conceptual deste protocolo e permite situar a área de "
          "formação entre os factores predisponentes de natureza académica."),
        P("Entre os factores predisponentes, o sexo feminino associou-se à "
          "automedicação na meta-análise global {behzadifar2020} e em "
          "Gondar, com odds ratio ajustado (ORa) de 1,48 entre estudantes "
          "de medicina e ciências da saúde {zeru2020} e de 3,11 entre "
          "estudantes de ciências da saúde de instituições privadas "
          "{kifle2021}, mas não na meta-análise etíope {fetensa2021}. O ano "
          "curricular mostra efeitos opostos: os estudantes do sexto ano de "
          "Gondar tinham ORa de 8,71 {zeru2020}, enquanto no Gana o avanço "
          "no curso reduziu a automedicação em estudantes de farmácia (OR "
          "0,442) e de outras áreas (OR 0,671) {amponsah2022}."),
        P("Entre os factores capacitantes, o rendimento associou-se à "
          "automedicação na meta-análise etíope (OR 0,67) {fetensa2021}; a "
          "acessibilidade de uma farmácia (ORa 4,85) e a proximidade de uma "
          "unidade sanitária a menos de 30 minutos (ORa 2,79) associaram-se "
          "à prática em Gondar {kifle2021}; viver em residência estudantil "
          "associou-se à automedicação com antibióticos na Eritreia (ORa "
          "2,42) {gebregziabher2024}; e ter medicamentos guardados em casa "
          "associou-se de forma independente à automedicação em Mansoura "
          "{helal2017}. O conhecimento também conta: desconhecer a "
          "resistência aos antibióticos associou-se a maior automedicação "
          "com antibióticos (ORa 2,41) {gebregziabher2024}."),
        P("A área de formação é o determinante mais controverso. Ser "
          "estudante de medicina associou-se de forma independente à "
          "automedicação no Egipto {helal2017}; os estudantes de farmácia "
          "(ORa 3,72) {kifle2021} e os do curso de oficial de saúde (ORa "
          "2,36) {zeru2020} automedicavam-se mais do que os colegas de "
          "outros cursos da saúde; e em Wollo os estudantes de agricultura "
          "tinham menor probabilidade de automedicação do que os de medicina "
          "e ciências da saúde (ORa 0,163) {zewdie2020}. Em sentido "
          "contrário, em Gondar a prevalência foi de 59,7% nos estudantes "
          "de medicina e de 69,0% nos de outras áreas {tesfaye2020} e na "
          "Tanzânia a automedicação com antibióticos foi de 49,1% nos cursos "
          "médicos e de 59,2% nos restantes, embora o modelo ajustado tenha "
          "invertido o sentido da diferença (ORa 1,6) {shitindi2023}; em "
          "Moshi não houve diferença {chuwa2021}. Nos "
          "estudantes zambianos de áreas não ligadas à saúde, a "
          "automedicação com antibióticos chegou a 76,7% {mudenda2023}. Como "
          "os estudantes da saúde diferem dos restantes também na idade, no "
          "sexo e na duração do curso, a comparação exige ajustamento para "
          "estes factores."),
    ]),
    ("Enquadramento normativo e programático em Moçambique", [
        P("A Lei n.º 12/2017 criou a ANARME, com funções de regulação, "
          "supervisão, fiscalização e sancionamento, fixou o regime de "
          "comercialização dos medicamentos, definiu os medicamentos não "
          "sujeitos a receita e tornou obrigatória a prescrição pela "
          "denominação comum internacional {lei12de2017}. O Diploma "
          "Ministerial n.º 52/2023 aprovou a LNME em vigor, que indica o nível de prescrição de cada "
          "medicamento, restringe as aquisições do Serviço Nacional de "
          "Saúde aos medicamentos da lista e atribui à ANARME a sua "
          "actualização trienal {misau2023lnme}. Em 2023 foram também "
          "aprovadas as normas de prescrição e dispensa de medicamentos e o "
          "regulamento do Sistema Nacional de Farmacovigilância, que "
          "enquadra a notificação de reacções adversas "
          "{misau2023prescricao}."),
        P("No plano programático, o Plano Nacional de Acção Contra a "
          "Resistência Antimicrobiana 2019-2023 previu campanhas de "
          "sensibilização e educação para reduzir o uso inapropriado de "
          "antibióticos, um currículo padrão sobre RAM para os cursos de "
          "formação de médicos, enfermeiros, farmacêuticos e técnicos de "
          "saúde e de farmácia, campanhas dirigidas ao público, aos "
          "profissionais e aos estudantes, e incentivos para que estudantes "
          "da saúde investiguem o uso de antimicrobianos e os "
          "comportamentos a ele associados {misau2019}. Apesar deste "
          "quadro, os estudos de Maputo mostram que a classificação dos "
          "antibióticos como medicamentos sujeitos a receita não é aplicada "
          "com rigor {torres2019,torres2020farm}. O presente estudo "
          "responde directamente à linha de investigação prevista no plano "
          "e produz informação útil para as suas acções educativas."),
    ]),
    ("Medição da automedicação em inquéritos a estudantes", [
        P("Os estudos com universitários usam quase sempre questionários "
          "auto-administrados, elaborados pelos autores a partir de estudos "
          "anteriores e pré-testados {zewdie2020,zeru2020}, e diferem "
          "sobretudo no período recordatório: um mês {esan2018}, dois meses "
          "{amponsah2022}, seis meses {tuyishimire2019,gebregziabher2024} ou "
          "doze meses {tesfaye2020}. A escolha pesa no resultado: na "
          "Eritreia, 67,1% dos respondentes referiram automedicação com "
          "antibióticos em algum momento, mas apenas 34,3% nos seis meses "
          "anteriores {gebregziabher2024}. Um período de seis meses capta "
          "episódios suficientes, incluindo uma estação chuvosa, e limita o "
          "esquecimento; os pormenores de dose, duração e fonte pedem-se só "
          "para o episódio mais recente, que é o mais bem recordado."),
        P("Um instrumento construído ou adaptado para uma nova população "
          "precisa de evidência de validade de conteúdo. A abordagem "
          "recomendada recorre a um painel de peritos que classifica a "
          "relevância de cada item e quantifica o acordo pelo índice de "
          "validade de conteúdo (IVC) do item e da escala, em três etapas: "
          "desenvolvimento, julgamento e quantificação, e revisão "
          "{almanasreh2019}. Para as componentes de conhecimento com itens "
          "dicotómicos, a consistência interna estima-se pela fórmula 20 de "
          "Kuder-Richardson (KR-20), caso particular do alfa de Cronbach, "
          "cujo valor deve ser interpretado à luz do número de itens e da "
          "finalidade do instrumento e não como limiar mecânico "
          "{taber2018}. A estabilidade das respostas de prática pode ser "
          "avaliada por teste-reteste com o kappa de Cohen, para o qual se "
          "recomendam em investigação em saúde limiares mais exigentes do "
          "que os propostos originalmente {mchugh2012}."),
        P("Os comportamentos relatados estão sujeitos a esquecimento e a "
          "desejabilidade social, que tende a baixar a prevalência declarada "
          "sobretudo entre estudantes da saúde, que sabem o que deveriam "
          "fazer. O anonimato real, a auto-administração sem a presença de "
          "docentes e a entrega em urna selada reduzem este viés. A "
          "qualidade do relato é orientada pela declaração Strengthening the "
          "Reporting of Observational Studies in Epidemiology (STROBE) "
          "{vonelm2007} e pela Consensus-Based Checklist for Reporting of "
          "Survey Studies (CROSS), construída por consenso para inquéritos "
          "{sharma2021}; ambas pedem a descrição do instrumento, da "
          "amostragem, da taxa de resposta e do tratamento dos dados em "
          "falta."),
    ]),
]

# ----------------------------------------------------- 7. estado da arte ----
ESTADO_ARTE = [
    P("O [[quadro:estado_arte]] reúne quinze estudos empíricos publicados "
      "desde 2018 sobre automedicação em estudantes universitários de "
      "países africanos, com prioridade para os que comparam cursos da "
      "saúde com cursos de outras áreas, e o principal estudo quantitativo "
      "moçambicano sobre antibióticos sem receita. Os números são os "
      "referidos pelas fontes."),
    QUADRO("estado_arte",
           "Síntese de estudos empíricos sobre automedicação em estudantes "
           "universitários africanos e em Moçambique (estado da arte)",
           ["Autor (ano)", "Local", "Desenho (n)", "Principais resultados"],
           [
               ["Esan et al. (2018) {esan2018}", "Nigéria, universidade "
                "privada", "Transversal (384)",
                "Automedicação em 81,8%; no mês anterior, analgésicos em "
                "cerca de 71%, antimaláricos em 33% e antibióticos em 10,5%; "
                "paracetamol em 75,1%; associação com idade, sexo, colégio e "
                "ano; atitude pouco amistosa da clínica universitária "
                "invocada por 27,7%."],
               ["Mate et al. (2019) {mate2019}", "Maputo, Moçambique "
                "(adultos da comunidade)", "Transversal por conglomerados "
                "(1.091)",
                "20,9% usaram antibióticos sem receita; 87,3% compraram-nos "
                "em farmácias; uso sem receita associado ao sexo masculino, "
                "à compra em mercados informais e ao fraco conhecimento."],
               ["Tuyishimire et al. (2019) {tuyishimire2019}", "Huye, "
                "Ruanda", "Transversal, amostragem aleatória (570)",
                "Automedicação com antibióticos nos seis meses em 12,1%; "
                "doença considerada pouco grave (50,72%); amoxicilina "
                "(59,42%); farmácia comunitária como fonte (72,42%)."],
               ["Tesfaye et al. (2020) {tesfaye2020}", "Gondar, Etiópia",
                "Transversal comparativo (213 de medicina e 212 de outras "
                "áreas)",
                "Nos 12 meses, 64,5% entre os que usaram medicamentos; 59,7% "
                "em medicina e 69,0% nas outras áreas; maior prática no "
                "quinto ano e nas outras áreas (p<0,05); analgésicos e "
                "antipiréticos mais usados."],
               ["Zewdie et al. (2020) {zewdie2020}", "Universidade de "
                "Wollo, nordeste da Etiópia", "Transversal, amostragem aleatória "
                "simples (341)",
                "Automedicação em 64,98%; analgésicos (56,28%) e antibióticos "
                "(35,9%); estudantes de agricultura com menor probabilidade "
                "do que os da saúde (ORa 0,163)."],
               ["Zeru et al. (2020) {zeru2020}", "Gondar, Etiópia",
                "Transversal, estudantes de medicina e ciências da saúde "
                "(792)",
                "Automedicação em 52,4% (IC 95% 49-56); sexo feminino (ORa "
                "1,48), sexto ano (ORa 8,71) e curso de oficial de saúde (ORa "
                "2,36) associados à prática."],
               ["Chuwa et al. (2021) {chuwa2021}", "Moshi, Tanzânia",
                "Transversal em duas universidades, uma médica e outra não "
                "(374)",
                "Automedicação com antibióticos em 57%; amoxicilina "
                "(32,08%); sem diferença entre estudantes médicos e não "
                "médicos (p=0,676)."],
               ["Akande-Sholabi et al. (2021) {akandesholabi2021}",
                "Nigéria", "Transversal, estudantes de medicina, enfermagem "
                "e farmácia (866)",
                "Automedicação em 54,6%; analgésicos (30,1%), antimaláricos "
                "(30,0%) e antibióticos (15,5%); farmácia comunitária como "
                "fonte (59,4%)."],
               ["Kifle et al. (2021) {kifle2021}", "Gondar, Etiópia",
                "Transversal, instituições privadas de ciências da saúde "
                "(554)",
                "Automedicação em 78,2%; sexo feminino (ORa 3,11), estudantes "
                "de farmácia (ORa 3,72) e farmácia acessível (ORa 4,85) "
                "associados à prática."],
               ["Amponsah et al. (2022) {amponsah2022}", "University of "
                "Ghana, Gana", "Transversal comparativo (163 de farmácia e "
                "174 de outros cursos)",
                "Nos dois meses anteriores, 55,2% em farmácia e 51,1% nos "
                "outros cursos; analgésicos como grupo principal; o avanço "
                "no curso reduziu a prática nos dois grupos."],
               ["Ikwara e Atwijukiire (2023) {ikwara2023}", "Lira, Uganda",
                "Transversal (422)",
                "Automedicação em 74,2%; antibióticos em 69,2%; 93,4% "
                "guardavam medicamentos em casa; associação com a "
                "faculdade (p=0,015)."],
               ["Mudenda et al. (2023) {mudenda2023}", "University of "
                "Zambia, Zâmbia", "Transversal, estudantes de áreas não "
                "ligadas à saúde (443)",
                "Automedicação com antibióticos em 76,7%; pontuações "
                "moderadas de conhecimento, atitudes e práticas sobre o uso "
                "de antimicrobianos e a RAM."],
               ["Shitindi et al. (2023) {shitindi2023}", "Dar es Salaam, "
                "Tanzânia", "Transversal comparativo (400 de cursos "
                "médicos e 429 de outros cursos)",
                "Automedicação com antibióticos em 49,1% nos cursos médicos "
                "e 59,2% nos outros, mas ORa de 1,6 a favor dos cursos "
                "médicos depois do ajustamento; acesso sem receita e "
                "proximidade das farmácias como factores principais."],
               ["Gebregziabher et al. (2024) {gebregziabher2024}",
                "Eritreia, cinco colégios", "Transversal (375 "
                "respondentes)",
                "Automedicação com antibióticos em 67,1% alguma vez e 34,3% "
                "nos seis meses; residência estudantil (ORa 2,42) e "
                "desconhecimento da resistência (ORa 2,41) associados."],
               ["Rafael et al. (2026) {rafael2026}", "Maputo, Moçambique "
                "(três instituições)", "Transversal em linha, estudantes "
                "da saúde (390)",
                "83,6% automedicaram-se para a COVID-19; plantas medicinais "
                "(78,7%); medicamentos convencionais (34,9%), com a "
                "azitromicina como o mais referido (20,3%)."],
           ],
           larguras=[3.4, 2.6, 3.4, 6.6],
           fonte="Elaboração própria (2026), a partir das fontes citadas."),
    P("A leitura do quadro mostra três regularidades. A automedicação "
      "atinge entre cerca de metade e mais de quatro quintos dos "
      "estudantes quando se considera qualquer medicamento "
      "{zeru2020,esan2018}; os analgésicos dominam, os antibióticos surgem "
      "entre os grupos mais usados e, nos estudos nigerianos, os "
      "antimaláricos aproximam-se dos analgésicos "
      "{akandesholabi2021,esan2018}; e a farmácia comunitária é a fonte "
      "principal, ao lado da reserva doméstica de medicamentos "
      "{tuyishimire2019,ikwara2023}. O período recordatório varia entre um "
      "e doze meses, o que explica parte da dispersão dos valores e "
      "aconselha cautela nas comparações directas."),
    P("A divergência está na área de formação: na prevalência bruta, os "
      "cursos da saúde automedicam-se menos em Gondar e na Tanzânia "
      "{tesfaye2020,shitindi2023}, mais no Gana e em Wollo "
      "{amponsah2022,zewdie2020} e de forma semelhante em Moshi "
      "{chuwa2021}, e poucos estudos ajustaram a comparação para a idade, "
      "o sexo e o ano curricular. A evidência moçambicana limita-se a "
      "adultos de Maputo e ao uso de antibióticos {mate2019} e a estudantes "
      "da saúde no contexto da COVID-19 {rafael2026}; não há estudos no "
      "Norte do país nem com estudantes de áreas não ligadas à saúde. O "
      "presente estudo preenche esta lacuna com uma amostra estratificada "
      "das duas áreas da mesma universidade, com poder calculado para a "
      "comparação e com ajustamento para os factores de confusão."),
]
ESQUEMA_TEXTO = [
    P("A [[figura:esquema]] representa o modelo que orienta a recolha e a "
      "análise, construído a partir do modelo comportamental de Andersen "
      "aplicado à automedicação {alkubaisi2022} e dos determinantes "
      "identificados na revisão. A área de formação ocupa o lugar de "
      "exposição principal, ao lado dos restantes factores predisponentes, "
      "dos factores capacitantes, que facilitam o acesso aos medicamentos, "
      "e dos factores de necessidade, que desencadeiam o episódio. O "
      "conhecimento sobre o uso responsável de medicamentos é tratado como "
      "factor intermédio, porque a formação em saúde pode agir através dele. "
      "O desfecho principal é a automedicação nos seis meses anteriores, "
      "com os subconjuntos de antibióticos e antimaláricos; a idade, o "
      "sexo e o ano curricular são tratados como potenciais factores de "
      "confusão da comparação entre áreas."),
]
ESQUEMA_TITULO = ("Esquema conceptual dos determinantes da automedicação em "
                  "estudantes da UniLúrio, cidade de Nampula, 2027")
ESQUEMA = {
    "contexto": "Estudantes de licenciatura da UniLúrio, cidade de Nampula, "
                "Março e Abril de 2027",
    "blocos": [
        ("Factores académicos", ["área de formação (saúde ou outras)",
                                 "curso", "ano curricular",
                                 "farmacologia concluída"]),
        ("Factores predisponentes", ["sexo", "idade", "residência",
                                     "profissional de saúde na família"]),
        ("Factores capacitantes", ["rendimento disponível",
                                   "medicamentos guardados",
                                   "farmácia próxima",
                                   "tempo até unidade sanitária"]),
        ("Necessidade e conhecimento", ["saúde percebida",
                                        "doença crónica",
                                        "conhecimento sobre uso "
                                        "responsável"]),
    ],
    "desfecho": ("Automedicação nos seis meses anteriores",
                 ["qualquer medicamento (sim ou não)",
                  "com antibióticos", "com antimaláricos"]),
    "moderadores": ("Factores de confusão da comparação entre áreas",
                    ["idade", "sexo", "ano curricular"]),
}

# ----------------------------------------------------- 8. metodologia -------
METODOLOGIA = [
    ("Tipo e desenho do estudo", [
        P("Trata-se de um estudo observacional, transversal e analítico, de "
          "base institucional, com recolha de dados por questionário anónimo "
          "auto-administrado em papel. A componente descritiva responde aos "
          "objectivos específicos 1 a 3 e a componente analítica, "
          "comparativa entre áreas de formação e de procura de factores "
          "associados, responde aos objectivos 4 e 5. O desenho transversal "
          "é o adequado para estimar a prevalência de um comportamento "
          "num período definido e para descrever as suas associações, sem "
          "pretensão de estabelecer relações causais. O relato seguirá a "
          "declaração STROBE {vonelm2007} e a lista CROSS {sharma2021}."),
    ]),
    ("Local e período do estudo", [
        P("O estudo realiza-se na cidade de Nampula, sede da UniLúrio. A FCS "
          "e a UBS funcionam no Campus de Marrere, na Rua n.º 4250, "
          "quilómetro 2,3, e a FAPF funciona também na cidade de Nampula. Os "
          "cursos de licenciatura abrangidos são os oito da FCS, os dois da "
          "FAPF e os três da UBS, indicados na delimitação "
          "{unilurio2026}. Os cursos que, à data da recolha, ainda não "
          "tenham estudantes matriculados em algum ano entram apenas com os "
          "anos em funcionamento."),
        P("O estudo decorre de Outubro de 2026 a Setembro de 2027. A recolha "
          "de dados realiza-se em Março e Abril de 2027, depois da aprovação "
          "pelo Comité Institucional de Bioética para a Saúde da Universidade "
          "Lúrio (CIBS-UniLúrio) e das autorizações institucionais, em datas "
          "acertadas com as direcções das faculdades fora dos períodos de "
          "avaliação. O período de referência da automedicação, os seis "
          "meses anteriores ao preenchimento, cobre aproximadamente os "
          "meses de Setembro de 2026 a Abril de 2027 e inclui a estação "
          "chuvosa, de maior transmissão da malária, o que será tido em "
          "conta na interpretação da automedicação com antimaláricos."),
    ]),
    ("População, unidade de análise e base de amostragem", [
        P("A população de estudo é constituída pelos estudantes de "
          "licenciatura dos cursos acima indicados, com 18 ou mais anos, "
          "matriculados no primeiro semestre do ano lectivo de 2027. O "
          "número de matriculados nas três unidades orgânicas não está "
          "publicado, pelo que o número de estudantes por curso e ano "
          "curricular será obtido junto dos serviços académicos antes do "
          "sorteio [confirmar junto dos serviços de registo académico da "
          "UniLúrio]."),
        P("A base de amostragem são as listas nominais de estudantes "
          "matriculados, por curso e ano curricular, com o número de "
          "estudante. As listas servem apenas para o sorteio e o convite, "
          "ficam guardadas à parte pelo investigador e são destruídas no fim "
          "da recolha, sem nunca serem associadas aos questionários."),
        P("O estudo tem três unidades de análise. O estudante é a unidade "
          "para a prevalência, para a comparação entre áreas e para os "
          "factores associados (objectivos 1, 4 e 5); cada estudante conta "
          "uma só vez em cada grupo de medicamentos usado nos seis meses, "
          "independentemente do número de episódios. O episódio mais "
          "recente de automedicação, um por estudante que se automedicou, é "
          "a unidade para as queixas, as práticas, as fontes e os motivos "
          "(objectivos 2 e 3). O medicamento referido nesse episódio, que "
          "pode ser mais do que um, é a unidade para a classificação ATC e "
          "AWaRe."),
    ]),
    ("Amostra e cálculo do tamanho da amostra", [
        P("O tamanho da amostra foi calculado para dois requisitos, e "
          "adoptou-se o maior: a precisão da prevalência em cada área de "
          "formação (objectivo 1) e o poder para comparar as duas áreas "
          "(objectivo 4) {in2020}. Para a precisão usou-se a fórmula da "
          "estimativa de uma proporção:"),
        FORMULA("n<sub>0</sub> = Z<sup>2</sup> × p × (1 - p) / d<sup>2</sup>"),
        P("em que Z = 1,96 corresponde a uma confiança de 95%, d = 0,05 é a "
          "margem de erro absoluta aceite e p = 0,50 é a prevalência "
          "esperada. As prevalências publicadas para estudantes africanos "
          "variam entre cerca de 52% e 82% para qualquer medicamento "
          "{zeru2020,esan2018} e dependem muito do período recordatório "
          "{gebregziabher2024}; como não há dados moçambicanos para um "
          "período de seis meses, adoptou-se o valor que maximiza a "
          "variância. A substituição dá n<sub>0</sub> = 3,8416 × 0,50 × 0,50 "
          "/ 0,0025 = 384,2, isto é, 385 respondentes por área."),
        P("Para a comparação entre áreas usou-se a fórmula para duas "
          "proporções independentes, com teste bilateral:"),
        FORMULA("n = [Z<sub>1-α/2</sub> × √(2 × p<sub>m</sub> × (1 - "
                "p<sub>m</sub>)) + Z<sub>1-β</sub> × √(p<sub>1</sub> × (1 - "
                "p<sub>1</sub>) + p<sub>2</sub> × (1 - p<sub>2</sub>))]"
                "<sup>2</sup> / (p<sub>1</sub> - p<sub>2</sub>)<sup>2</sup>"),
        P("em que Z<sub>1-α/2</sub> = 1,96 (α de 5%), Z<sub>1-β</sub> = 0,84 "
          "(poder de 80%), p<sub>1</sub> e p<sub>2</sub> são as prevalências "
          "nas duas áreas e p<sub>m</sub> é a sua média. Fixou-se em dez "
          "pontos percentuais a menor diferença com interesse prático, valor "
          "próximo das diferenças observadas entre áreas em Gondar (9,3 "
          "pontos) e na Tanzânia (10,1 pontos) {tesfaye2020,shitindi2023}. "
          "Como o sentido da diferença é desconhecido, a diferença foi "
          "centrada em 50%, com p<sub>1</sub> = 0,45 e p<sub>2</sub> = 0,55, "
          "o cenário de maior variância. A substituição dá n = [1,96 × "
          "√0,50 + 0,84 × √0,495]<sup>2</sup> / 0,01 = [1,96 × 0,7071 + "
          "0,84 × 0,7036]<sup>2</sup> / 0,01 = (1,3859 + 0,5910)<sup>2</sup> "
          "/ 0,01 = 3,9082 / 0,01 = 390,8, isto é, 391 respondentes por "
          "área. Este valor é superior aos 385 exigidos pela precisão e é o "
          "adoptado; com 391 respondentes, a margem de erro da prevalência "
          "em cada área fica em 4,96 pontos percentuais."),
        P("Para compensar ausências no dia da sessão, recusas e "
          "questionários inutilizáveis, aplicou-se uma taxa de não resposta "
          "de 15%, superior às perdas de 1,3% a 7,7% registadas em "
          "inquéritos semelhantes a estudantes {kifle2021,gebregziabher2024}, "
          "porque aqui inclui também a ausência às aulas:"),
        FORMULA("n<sub>c</sub> = n / (1 - t<sub>nr</sub>) = 391 / 0,85 = "
                "460"),
        P("São, portanto, convidados 460 estudantes por área, 920 no total, "
          "para obter 782 respondentes. Não se aplica efeito de desenho de "
          "conglomerados, porque os estudantes são seleccionados "
          "individualmente a partir das listas e não por turmas inteiras; a "
          "estratificação com afectação proporcional dentro de cada área não "
          "aumenta a variância. A estimativa global, que junta duas áreas "
          "com o mesmo número de respondentes mas com populações de "
          "tamanho diferente, é ponderada e o seu intervalo de confiança "
          "incorpora a perda de precisão devida à ponderação; sem esse "
          "efeito, 782 respondentes dariam uma margem de erro global de "
          "cerca de 3,5 pontos."),
        P("Como o número de estudantes elegíveis em cada área "
          "(N<sub>h</sub>) só será conhecido antes do sorteio, a "
          "[[tabela:cenarios]] apresenta a regra de decisão para vários "
          "cenários. Quando os 460 convites representam metade ou mais dos "
          "estudantes elegíveis da área, isto é, quando N<sub>h</sub> não "
          "excede 920, convidam-se todos os estudantes da área (censo), "
          "porque a amostragem pouparia pouco e o censo elimina o erro de "
          "amostragem nesse estrato; caso contrário, seleccionam-se 460 "
          "estudantes com fracção de amostragem f<sub>h</sub> = 460 / "
          "N<sub>h</sub>. Em ambos os casos, a análise aplica a correcção "
          "para população finita:"),
        FORMULA("d = 1,96 × √[p × (1 - p) / r × (1 - r / N<sub>h</sub>)]"),
        P("em que r é o número de respondentes esperado. O efeito desta "
          "correcção sobre a margem de erro esperada consta da última "
          "coluna da tabela."),
        TABELA("cenarios",
               "Cenários de tamanho da população por área de formação, "
               "decisão de amostragem e precisão esperada",
               ["Estudantes elegíveis na área (N<sub>h</sub>)",
                "Fracção 460 / N<sub>h</sub>", "Decisão",
                "Convidados", "Respondentes esperados (85%)",
                "Margem de erro esperada (pontos)"],
               [["600", "0,77", "Censo da área", "600", "510", "1,7"],
                ["900", "0,51", "Censo da área", "900", "765", "1,4"],
                ["1.200", "0,38", "Amostra sistemática, intervalo 2,6",
                 "460", "391", "4,1"],
                ["1.800", "0,26", "Amostra sistemática, intervalo 3,9",
                 "460", "391", "4,4"],
                ["2.400", "0,19", "Amostra sistemática, intervalo 5,2",
                 "460", "391", "4,5"]],
               larguras=[3.0, 2.2, 3.8, 2.2, 2.6, 2.2],
               fonte="Elaboração própria (2026).",
               nota="Valores de N<sub>h</sub> hipotéticos. Margem de erro "
                    "para p = 0,50, com correcção para população finita. O "
                    "número real de estudantes elegíveis por curso e ano "
                    "será obtido nos serviços académicos antes do sorteio."),
        P("Com 391 respondentes por área, o estudo tem também poder de "
          "cerca de 90% para detectar diferenças de 20% para 30% na "
          "automedicação com antibióticos e de 10% para 18% na "
          "automedicação com antimaláricos. Para a regressão multivariável "
          "(objectivo 5), mesmo que a prevalência seja de 30% ou de 70%, a "
          "categoria menos frequente terá cerca de 235 estudantes, o que "
          "permite até 23 parâmetros segundo a regra de pelo menos dez "
          "eventos por variável {peduzzi1996}; o modelo será limitado a 15 "
          "parâmetros. Nos modelos secundários para antibióticos e "
          "antimaláricos, o número de parâmetros será limitado ao número de "
          "eventos dividido por dez, e o poder mais baixo para estes "
          "desfechos será declarado."),
    ]),
    ("Técnica de amostragem e selecção dos participantes", [
        P("A amostragem é aleatória estratificada. Os estratos principais "
          "são as duas áreas de formação, saúde (cursos da FCS) e outras "
          "áreas (cursos da FAPF e da UBS), com o mesmo número de convites, "
          "o que optimiza a comparação. Dentro de cada área, os 460 convites "
          "distribuem-se pelos subestratos de curso e ano curricular em "
          "proporção ao número de estudantes de cada um, com arredondamento "
          "por excesso, de modo que a amostra de cada área seja "
          "auto-ponderada."),
        P("Antes do sorteio principal, sorteiam-se aleatoriamente nas "
          "listas 92 estudantes para o pré-teste, 46 de cada área, que são "
          "retirados da base de amostragem. Em cada lista de curso e ano, "
          "ordenada pelo número de estudante, aplica-se depois a selecção "
          "sistemática com intervalo k = N<sub>h</sub> / 460 e início "
          "aleatório entre 1 e k, gerado por computador na presença do "
          "orientador. Nas áreas em que se aplique o censo, todos os "
          "estudantes das listas são convidados. Não há substituição: o "
          "estudante seleccionado que falte à sessão é procurado em até duas "
          "visitas adicionais e, se não for encontrado, conta como não "
          "respondente. A composição da amostra e as taxas de resposta são "
          "registadas por subestrato para o cálculo dos pesos."),
    ]),
    ("Critérios de inclusão e de exclusão", [
        H3("Critérios de inclusão"),
        LISTA([
            "Estar matriculado, no primeiro semestre de 2027, num curso de "
            "licenciatura leccionado na cidade de Nampula pela FCS, pela "
            "FAPF ou pela UBS.",
            "Ter 18 ou mais anos de idade.",
            "Ter sido seleccionado no sorteio ou pertencer a uma área em que "
            "se aplique o censo.",
            "Aceitar participar, assinalando a declaração de consentimento "
            "anónimo na primeira página do questionário.",
        ]),
        H3("Critérios de exclusão"),
        LISTA([
            "Ter participado no pré-teste ou no reteste do questionário.",
            "Integrar a equipa de investigação ou de recolha de dados.",
            "Estar em estágio ou mobilidade fora da cidade de Nampula durante "
            "todo o período de recolha.",
            "Ter a matrícula anulada ou suspensa à data da recolha.",
        ]),
    ]),
    ("Variáveis e definições operacionais", [
        P("O [[quadro:variaveis]] apresenta as variáveis do estudo, o seu "
          "tipo, a definição operacional com as categorias e o objectivo "
          "específico a que servem. A classificação dos medicamentos segue "
          "o sistema ATC {whocc2026} e a dos antibióticos segue a "
          "classificação AWaRe de 2025 {omsaware2025}. Os pontos de corte "
          "do conhecimento (bom com 80% ou mais de respostas correctas, "
          "moderado de 60% a 79% e fraco abaixo de 60%) aplicam-se à escala "
          "de dez itens descrita no instrumento."),
        QUADRO("variaveis", "Variáveis do estudo e definições operacionais",
               ["Variável", "Tipo", "Definição operacional e categorias",
                "Objectivo"],
               [
                   ["Automedicação nos seis meses", "Dependente, "
                    "qualitativa dicotómica",
                    "Uso, para si próprio, de pelo menos um medicamento "
                    "industrializado sem prescrição nem consulta de "
                    "profissional habilitado, nos seis meses anteriores "
                    "(pergunta B2): sim; não", "1, 4, 5"],
                   ["Automedicação com antibióticos", "Dependente, "
                    "dicotómica",
                    "Pelo menos um antibacteriano sistémico (ATC J01) ou "
                    "metronidazol oral em automedicação nos seis meses, "
                    "pela lista B3 ou pelo nome referido: sim; não", "2, 4"],
                   ["Automedicação com antimaláricos", "Dependente, "
                    "dicotómica",
                    "Pelo menos um antimalárico (ATC P01B) em automedicação "
                    "nos seis meses: sim; não", "2, 4"],
                   ["Grupos terapêuticos usados", "Descritiva, resposta "
                    "múltipla",
                    "Analgésicos e antipiréticos; anti-inflamatórios não "
                    "esteróides; antibióticos; antimaláricos; "
                    "antiparasitários; antialérgicos; antiácidos; "
                    "antidiarreicos; medicamentos para tosse e constipação; "
                    "vitaminas e suplementos; medicamentos para dormir ou "
                    "para a ansiedade; estimulantes da concentração; outros. "
                    "Confirmação pelo nível 2 da ATC", "2"],
                   ["Grupo AWaRe do antibiótico", "Descritiva, nominal",
                    "Acesso; Vigilância; Reserva; não classificado", "2"],
                   ["Queixa do episódio mais recente", "Descritiva, "
                    "nominal",
                    "Cefaleia; febre; outras dores; sintomas respiratórios; "
                    "diarreia ou dor abdominal; suspeita de malária; queixas "
                    "urinárias ou genitais; dor de dentes; dor menstrual; "
                    "problemas de pele; outra", "2"],
                   ["Práticas no episódio mais recente", "Descritivas, "
                    "nominais",
                    "Leitura do folheto (sim; não); dose conforme o folheto "
                    "ou a indicação recebida (sim; não; não sabe); duração "
                    "em dias; interrupção antes do fim (sim; não); teste de "
                    "malária antes do antimalárico (sim; não); reacção "
                    "adversa (sim; não); procura posterior de cuidados (sim; "
                    "não)", "2"],
                   ["Fonte de obtenção", "Descritiva, nominal",
                    "Farmácia privada; farmácia de unidade sanitária "
                    "pública; vendedor informal ou mercado; loja ou banca de "
                    "bairro; sobras em casa; família, amigos ou colegas; "
                    "outra", "3"],
                   ["Fonte de informação", "Descritiva, resposta múltipla",
                    "Conhecimento próprio; matérias do curso; farmacêutico "
                    "ou técnico de farmácia; família; amigos ou colegas; "
                    "receita antiga; internet ou redes sociais; folheto; "
                    "outra", "3"],
                   ["Motivos", "Descritiva, resposta múltipla",
                    "Doença ligeira; experiência anterior; falta de tempo; "
                    "espera longa; custo; distância; confiança nos "
                    "conhecimentos; mau atendimento; alívio rápido; outro",
                    "3"],
                   ["Área de formação", "Independente principal, "
                    "dicotómica",
                    "Saúde (cursos da FCS); outras áreas (cursos da FAPF e "
                    "da UBS)", "1, 4, 5"],
                   ["Curso", "Independente, nominal",
                    "Um dos 13 cursos de licenciatura", "1"],
                   ["Ano curricular", "Independente, ordinal",
                    "1.º a 6.º; agrupado em 1.º e 2.º, 3.º e 4.º, 5.º e 6.º",
                    "1, 4, 5"],
                   ["Farmacologia concluída", "Independente, dicotómica",
                    "Ter concluído pelo menos uma unidade curricular de "
                    "farmacologia: sim; não", "5"],
                   ["Sexo", "Independente, dicotómica",
                    "Masculino; feminino", "4, 5"],
                   ["Idade", "Independente, quantitativa",
                    "Anos completos; categorias 18-20, 21-23, 24 ou mais",
                    "4, 5"],
                   ["Residência no ano lectivo", "Independente, nominal",
                    "Com a família; residência estudantil; casa arrendada, "
                    "só ou com colegas; outra", "5"],
                   ["Profissional de saúde no agregado", "Independente, "
                    "dicotómica", "Sim; não", "5"],
                   ["Valor mensal disponível", "Independente, ordinal",
                    "Menos de 1.000 MT; 1.000-2.999 MT; 3.000-4.999 MT; "
                    "5.000 MT ou mais", "5"],
                   ["Medicamentos guardados", "Independente, dicotómica",
                    "Ter medicamentos guardados no local onde vive: sim; "
                    "não", "5"],
                   ["Farmácia próxima", "Independente, dicotómica",
                    "Farmácia a 15 minutos ou menos, a pé, do local onde "
                    "vive: sim; não", "5"],
                   ["Tempo até à unidade sanitária", "Independente, "
                    "dicotómica", "30 minutos ou menos; mais de 30 minutos",
                    "5"],
                   ["Saúde percebida", "Independente, ordinal",
                    "Boa; razoável; má", "5"],
                   ["Doença crónica", "Independente, dicotómica",
                    "Diagnóstico médico de doença crónica: sim; não", "5"],
                   ["Conhecimento sobre uso responsável", "Independente, "
                    "ordinal",
                    "Soma de 10 itens (0 a 10): bom, 8 a 10 (80% ou mais); "
                    "moderado, 6 a 7 (60-79%); fraco, 0 a 5 (menos de 60%)",
                    "5"],
                   ["Remédios tradicionais", "Descritiva, dicotómica",
                    "Uso de remédios tradicionais ou à base de plantas nos "
                    "seis meses: sim; não", "2"],
               ],
               larguras=[3.4, 2.8, 8.0, 1.8],
               fonte="Elaboração própria (2026). MT: metical."),
    ]),
    ("Instrumento de recolha de dados, validação e pré-teste", [
        P("O instrumento é um questionário em português, auto-administrado, "
          "com seis secções e cerca de 20 minutos de preenchimento "
          "(Apêndice A): dados sociodemográficos e académicos; uso de "
          "medicamentos e automedicação nos seis meses, com a lista de "
          "grupos terapêuticos; episódio mais recente, com a queixa, os "
          "medicamentos, a fonte, a informação, os motivos e as práticas; "
          "antibióticos e antimaláricos; conhecimento sobre o uso "
          "responsável de medicamentos; e remédios tradicionais. As "
          "perguntas de prática foram construídas a partir da estrutura dos "
          "questionários usados com universitários africanos "
          "{tesfaye2020,zewdie2020,akandesholabi2021} e dos factores do "
          "modelo de Andersen {alkubaisi2022}. Os dez itens de conhecimento, "
          "de resposta verdadeiro, falso ou não sei, foram redigidos para "
          "este estudo a partir das recomendações sobre antibióticos, "
          "malária e analgésicos e dos domínios de conhecimento avaliados em "
          "Maputo e na Tanzânia {mate2019,shitindi2023}; não reproduzem "
          "nenhuma escala validada, pelo que o instrumento é submetido a "
          "validação completa. Não se prevê tradução para emakhuwa, porque "
          "o português é a língua de ensino de todos os participantes, mas o "
          "pré-teste verifica a compreensão de cada pergunta. Um cartão de "
          "apoio com os nomes genéricos mais comuns de cada grupo "
          "terapêutico, sem marcas comerciais, ajuda a identificar os "
          "medicamentos."),
        P("A validade de conteúdo é avaliada por um painel de cinco peritos: "
          "dois docentes de Farmácia, um médico com experiência em "
          "farmacologia, um docente de saúde pública e um docente da FAPF ou "
          "da UBS, que avalia a clareza para estudantes de outras áreas. "
          "Cada perito classifica a relevância de cada item numa escala de "
          "quatro pontos; o IVC de cada item é a proporção de peritos que o "
          "classificam como bastante ou muito relevante {almanasreh2019}. "
          "Itens com IVC inferior a 0,80, isto é, aprovados por menos de "
          "quatro dos cinco peritos, são revistos ou retirados, e a média do "
          "IVC da escala deve atingir pelo menos 0,90."),
        P("O pré-teste envolve os 92 estudantes sorteados para o efeito, "
          "cerca de 10% da amostra, 46 de cada área, em sessões iguais às "
          "da recolha principal. Avalia o tempo de preenchimento, a "
          "proporção de respostas em falta por item e a compreensão, "
          "através de uma conversa de verificação com dez voluntários depois "
          "da entrega. A consistência interna dos itens de conhecimento é "
          "estimada pelo KR-20, com valor mínimo de 0,70 {taber2018}; se "
          "ficar abaixo, os itens com correlação item-total inferior a 0,20 "
          "são revistos e o KR-20 volta a ser calculado na amostra "
          "principal. A estabilidade das respostas de prática é avaliada por "
          "reteste ao fim de 14 dias nos estudantes do pré-teste que "
          "aceitem, emparelhados por um código anónimo gerado pelo próprio "
          "estudante (duas primeiras letras do nome da mãe, dia de "
          "nascimento e duas primeiras letras do bairro de nascimento); "
          "exige-se kappa de Cohen de pelo menos 0,60 para a automedicação "
          "nos seis meses e para o uso de antibióticos e de antimaláricos "
          "{mchugh2012}. As categorias de valor mensal disponível podem ser "
          "ajustadas se mais de metade das respostas do pré-teste cair numa "
          "só categoria."),
    ]),
    ("Procedimentos de recolha de dados e controlo de qualidade", [
        P("A recolha é feita pelo investigador e por dois assistentes, "
          "estudantes finalistas de outro curso ou recém-licenciados, que "
          "não são docentes nem colegas de turma dos convidados, formados "
          "durante um dia sobre o protocolo, o guião de apresentação, o "
          "anonimato e o manuseamento das urnas. As sessões são marcadas "
          "com as direcções e com os chefes de turma no fim de uma aula, sem "
          "a presença do docente. O assistente lê o número de estudante dos "
          "seleccionados, que se juntam numa sala próxima, e lê a folha de "
          "informação (Apêndice B). Cada convidado recebe um envelope com a "
          "folha de informação, o questionário e o folheto sobre "
          "automedicação responsável (Apêndice F), senta-se afastado dos "
          "colegas, preenche o questionário sem nome nem número, fecha o "
          "envelope e deposita-o numa urna selada. Quem não quiser "
          "participar deposita o envelope com o questionário em branco, "
          "pelo que ninguém sabe quem aceitou ou recusou."),
        P("As urnas são seladas com fita de segurança numerada e só são "
          "abertas no fim de cada dia pelo investigador, na presença de um "
          "assistente, com registo na ficha de controlo da sessão (Apêndice "
          "E): turma, data, número de seleccionados, presentes, envelopes "
          "entregues e envelopes devolvidos preenchidos e em branco, e "
          "número do selo. Os questionários recebem nesse momento um "
          "número sequencial. Para evitar contaminação, as sessões de cada "
          "faculdade concentram-se na mesma semana e pede-se aos "
          "participantes que não comentem o conteúdo com colegas ainda por "
          "inquirir. São contados como não resposta os envelopes em branco "
          "e os questionários sem resposta à pergunta principal (B2)."),
        P("Os nomes de medicamentos são codificados de forma independente "
          "por dois codificadores, o investigador e um docente farmacêutico, "
          "segundo a ATC até ao nível da substância e segundo a "
          "classificação AWaRe; as respostas abertas de motivos e queixas "
          "são codificadas nas categorias do quadro de variáveis. A "
          "concordância é medida pelo kappa de Cohen, com valor mínimo de "
          "0,60 {mchugh2012}, e as discordâncias são resolvidas por consenso "
          "ou, na falta dele, pelo orientador. Todos os questionários são "
          "digitados duas vezes, por pessoas diferentes, no programa "
          "EpiData, com limites de valores e regras de consistência "
          "(por exemplo, quem responde não na pergunta B2 não pode ter "
          "respostas nas perguntas B3 a D3); as discrepâncias entre as duas "
          "digitações "
          "são corrigidas pelo questionário em papel."),
    ]),
    ("Processamento e análise dos dados", [
        P("A análise será feita no programa Statistical Package for the "
          "Social Sciences (SPSS), da IBM, versão 26 ou superior, com o "
          "módulo de amostras "
          "complexas, ou no programa R, com o pacote survey, ambos capazes "
          "de incorporar os estratos, os pesos e a correcção para população "
          "finita. O peso de cada respondente é o número de estudantes "
          "elegíveis do seu subestrato de curso e ano dividido pelo número "
          "de respondentes desse subestrato. O nível de significância é de "
          "5% e todas as estimativas são apresentadas com intervalo de "
          "confiança a 95% (IC 95%). O [[quadro:analise]] resume a análise "
          "prevista para cada objectivo."),
        P("A prevalência global é ponderada e as prevalências por área, "
          "curso e ano são auto-ponderadas dentro de cada área. As taxas "
          "de resposta são apresentadas por subestrato, como pede a lista "
          "CROSS {sharma2021}. Os grupos terapêuticos são apresentados como "
          "percentagem de todos os respondentes, o que dá a prevalência de "
          "automedicação com cada grupo, e como percentagem dos que se "
          "automedicaram; nas perguntas de resposta múltipla, a soma pode "
          "exceder 100%. Os antibióticos são distribuídos pelos grupos AWaRe."),
        P("A comparação entre áreas (objectivo 4) usa o teste do "
          "qui-quadrado com correcção de Rao-Scott para o desenho e "
          "apresenta a diferença de prevalências e a razão de prevalências "
          "(RP) com IC 95%. Como a automedicação é um desfecho frequente, a "
          "odds ratio sobrestimaria a associação, pelo que a medida "
          "principal é a RP, estimada por regressão de Poisson com "
          "variância robusta, ou regressão de Poisson modificada, que "
          "mantém bom desempenho mesmo quando o modelo não está "
          "perfeitamente especificado {chen2018}. A RP da área é ajustada "
          "para idade, sexo e ano curricular, e a interacção entre área e "
          "ano curricular é testada pelo teste de Wald. Uma análise de "
          "sensibilidade substitui a área pela variável farmacologia "
          "concluída."),
        P("Para o objectivo 5, cada factor é primeiro analisado com o teste "
          "do qui-quadrado, ou com o teste exacto de Fisher quando mais de "
          "20% das frequências esperadas forem inferiores a cinco, e com a "
          "RP bruta. Entram no modelo multivariável de Poisson modificada "
          "os factores com p<0,20 na análise bivariada e, obrigatoriamente, "
          "a área, o sexo, a idade e o ano curricular. A colinearidade é "
          "verificada pelo factor de inflação da variância, retirando-se uma "
          "das variáveis quando este exceder cinco. O modelo final apresenta "
          "razões de prevalência ajustadas (RPa) com IC 95%; como análise de "
          "sensibilidade e para comparação com a literatura, estima-se "
          "também o modelo de regressão logística, com odds ratio "
          "ajustados. O conhecimento é analisado pelas três categorias "
          "definidas e, em alternativa, pela pontuação contínua."),
        P("As respostas em falta são descritas por variável. Se nenhuma "
          "variável do modelo final tiver mais de 5% de dados em falta, "
          "usa-se a análise de casos completos; se tiver, repete-se o modelo "
          "com imputação múltipla por equações encadeadas, com 20 "
          "conjuntos imputados, como análise de sensibilidade. O uso de "
          "remédios tradicionais é descrito à parte e não entra no desfecho "
          "principal."),
        QUADRO("analise", "Plano de análise por objectivo específico",
               ["Objectivo", "Indicador ou desfecho", "Denominador",
                "Análise estatística"],
               [
                   ["1", "Prevalência da automedicação nos seis meses, "
                    "global e por área, curso e ano",
                    "Todos os respondentes",
                    "Proporções ponderadas com IC 95%; taxas de resposta "
                    "por subestrato"],
                   ["2", "Grupos terapêuticos, grupos AWaRe, queixas e "
                    "práticas do episódio mais recente",
                    "Todos os respondentes (grupos) e estudantes que se "
                    "automedicaram (episódio)",
                    "Frequências absolutas e relativas com IC 95%; kappa "
                    "entre codificadores"],
                   ["3", "Fontes de obtenção, fontes de informação e "
                    "motivos", "Estudantes que se automedicaram",
                    "Frequências com IC 95%, por área"],
                   ["4", "Diferença entre áreas na automedicação global, "
                    "com antibióticos e com antimaláricos",
                    "Todos os respondentes",
                    "Qui-quadrado de Rao-Scott; diferença e RP com IC 95%; "
                    "RPa por idade, sexo e ano (Poisson modificada); "
                    "interacção área e ano"],
                   ["5", "Factores associados à automedicação",
                    "Todos os respondentes",
                    "RP bruta; Poisson modificada multivariável com RPa e "
                    "IC 95%; regressão logística com odds ratio ajustados "
                    "(ORa) como sensibilidade"],
               ],
               larguras=[1.8, 4.6, 3.8, 5.8],
               fonte="Elaboração própria (2026)."),
    ]),
    ("Limitações do estudo e estratégias de mitigação", [
        P("O [[quadro:limitacoes]] apresenta as limitações previsíveis, a "
          "sua consequência para os resultados e as medidas adoptadas para "
          "as reduzir. A mais relevante para a comparação entre áreas é a "
          "desejabilidade social, porque pode afectar de forma diferente os "
          "estudantes da saúde, e por isso o anonimato foi desenhado para "
          "ser verificável pelo próprio participante."),
        QUADRO("limitacoes", "Limitações previstas e estratégias de "
               "mitigação",
               ["Limitação", "Consequência", "Mitigação"],
               [
                   ["Esquecimento de episódios e de nomes de medicamentos",
                    "Subestimação da prevalência e classificação errada dos "
                    "grupos terapêuticos",
                    "Período de seis meses; pormenores apenas do episódio "
                    "mais recente; cartão de apoio com nomes genéricos; "
                    "codificação dupla pelo nome"],
                   ["Desejabilidade social, maior nos cursos da saúde",
                    "Subestimação diferencial, que enviesaria a comparação "
                    "entre áreas",
                    "Questionário sem identificação; urna selada; ausência de "
                    "docentes; devolução de envelopes em branco; assistentes "
                    "externos às turmas"],
                   ["Não resposta e ausência às sessões",
                    "Viés de selecção se os ausentes diferirem dos "
                    "presentes, por exemplo por doença",
                    "Até duas visitas adicionais; pesos por subestrato; "
                    "comparação das taxas de resposta por curso e ano"],
                   ["Desenho transversal",
                    "Impossibilidade de inferir causalidade e ambiguidade "
                    "temporal entre conhecimento e prática",
                    "Interpretar associações como tais; conhecimento tratado "
                    "como factor intermédio"],
                   ["Confusão na comparação entre áreas",
                    "Diferença atribuída à área que se deve à idade, ao "
                    "sexo ou ao ano curricular",
                    "Ajustamento multivariável; teste da interacção entre "
                    "área e ano; análise de sensibilidade com farmacologia "
                    "concluída"],
                   ["Poder limitado para diferenças pequenas e para cursos "
                    "isolados",
                    "Diferenças inferiores a dez pontos podem não ser "
                    "detectadas",
                    "Declarar o poder; apresentar IC 95%; não fazer testes "
                    "de hipóteses curso a curso"],
                   ["Sazonalidade da malária",
                    "Automedicação com antimaláricos dependente da época do "
                    "ano",
                    "Declarar o período de referência e interpretar à luz da "
                    "estação chuvosa"],
                   ["Contaminação entre turmas",
                    "Respostas influenciadas por conversas prévias",
                    "Sessões de cada faculdade na mesma semana; pedido de "
                    "reserva aos participantes"],
                   ["Validade externa limitada",
                    "Resultados não generalizáveis a Pemba, Unango, Ilha de "
                    "Moçambique ou a outras instituições",
                    "Descrição completa do contexto e comparação com a "
                    "literatura"],
               ],
               larguras=[4.4, 5.2, 6.4],
               fonte="Elaboração própria (2026)."),
    ]),
    ("Considerações éticas", [
        P("O protocolo será submetido ao CIBS-UniLúrio e a recolha só "
          "começa depois da sua aprovação, em conformidade com a Lei de "
          "Investigação em Saúde Humana {lei3de2023} e com a Declaração de "
          "Helsínquia na revisão de 2024 {wma2025}. Serão pedidas "
          "autorizações à Reitoria da UniLúrio, às direcções da FCS, da "
          "FAPF e da UBS e aos serviços de registo académico, para o acesso "
          "às listas nominais (Apêndice D). Por se tratar de um inquérito a "
          "estudantes da própria universidade sobre um comportamento que "
          "pode ser visto como incorrecto, sobretudo nos cursos da saúde, o "
          "desenho ético centra-se em três riscos: a pressão para "
          "participar, a identificação das respostas e o receio de "
          "consequências académicas."),
        LISTA([
            "Participação voluntária, sem incentivos e sem qualquer efeito "
            "nas avaliações; os docentes não estão presentes nas sessões e "
            "não têm acesso aos questionários nem à base de dados.",
            "Anonimato: o questionário não tem nome, número de estudante nem "
            "assinatura; o consentimento é dado por uma declaração anónima "
            "assinalada na primeira página, e pede-se ao CIBS-UniLúrio a "
            "dispensa do consentimento escrito assinado, porque a assinatura "
            "seria o único elo entre o participante e as respostas "
            "(Apêndice C).",
            "Urna selada e devolução de envelopes em branco por quem não "
            "quiser participar, para que ninguém saiba quem aceitou ou "
            "recusou.",
            "As listas nominais servem só para o sorteio e o convite, são "
            "guardadas à parte e destruídas no fim da recolha; nunca são "
            "associadas aos questionários.",
            "Os resultados são divulgados apenas de forma agregada, nunca "
            "por turma nem para grupos com menos de dez respondentes.",
            "Os questionários em papel são guardados numa caixa fechada à "
            "chave e destruídos cinco anos após a defesa; a base de dados, "
            "sem identificadores, é protegida por palavra-passe e só o "
            "investigador e o orientador lhe têm acesso.",
            "Os riscos são mínimos (tempo de preenchimento e eventual "
            "desconforto em perguntas sobre medicamentos para dormir ou "
            "estimulantes); o participante pode deixar qualquer pergunta "
            "sem resposta.",
            "Todos os convidados recebem o folheto sobre automedicação "
            "responsável, com os sinais que exigem consulta, e os resultados "
            "agregados são devolvidos às faculdades e à associação de "
            "estudantes numa sessão não punitiva.",
        ]),
        P("Como o questionário é anónimo, o estudo não consegue identificar "
          "um participante que relate uma reacção adversa ou uma prática de "
          "risco. Por isso, a via de referenciação é universal: a folha de "
          "informação e o folheto indicam os sinais de alarme, recomendam a "
          "consulta na unidade sanitária mais próxima e dão o contacto do "
          "investigador; o estudante que o procure por iniciativa própria "
          "é orientado para uma consulta e informado sobre a notificação de "
          "reacções adversas ao Sistema Nacional de Farmacovigilância "
          "{misau2023prescricao}. O investigador declara não ter conflitos de "
          "interesses e o estudo não recebe financiamento de empresas "
          "farmacêuticas."),
    ]),
]

# ----------------------------------------------------- 9 e 10 ---------------
RESULTADOS_ESPERADOS = [
    P("Os resultados esperados seguem a ordem dos objectivos específicos. "
      "Não se antecipam valores, mas a literatura permite indicar a "
      "direcção provável de cada resultado e a sua utilidade prática."),
    LISTA([
        "Objectivo 1: uma estimativa da prevalência da automedicação nos "
        "seis meses, global e por área, curso e ano, com IC 95%. Espera-se "
        "uma prevalência elevada, na faixa de metade a quatro quintos dos "
        "estudantes descrita em universidades africanas "
        "{zeru2020,esan2018}, possivelmente mais baixa do que nos estudos "
        "com período recordatório de doze meses. A estimativa servirá de "
        "linha de base para a UniLúrio monitorizar o efeito de futuras "
        "intervenções.",
        "Objectivo 2: o perfil dos medicamentos usados, com predomínio "
        "provável dos analgésicos, seguidos dos antibióticos e dos "
        "antimaláricos {zewdie2020,akandesholabi2021}, e com a amoxicilina "
        "como antibiótico mais frequente {torres2020,tuyishimire2019}. A "
        "distribuição dos antibióticos pelos grupos AWaRe e a proporção de "
        "estudantes que tomaram antimaláricos sem teste de confirmação "
        "indicarão as mensagens prioritárias da educação para o uso "
        "responsável e os medicamentos a vigiar em farmacovigilância.",
        "Objectivo 3: a identificação das fontes e dos motivos, com as "
        "farmácias privadas, a reserva doméstica e os colegas como fontes "
        "prováveis {akandesholabi2021,ikwara2023} e a doença considerada "
        "ligeira e a experiência anterior como motivos principais "
        "{zewdie2020,gashaw2025}. Estes dados orientam a inspecção da "
        "dispensa sem receita e a formação dos farmacêuticos para o "
        "aconselhamento, e mostram se o acesso aos serviços de saúde pesa "
        "na decisão dos estudantes.",
        "Objectivo 4: a resposta à pergunta sobre o efeito da formação em "
        "saúde, seja uma diferença estatisticamente significativa, com o "
        "seu sentido e a RP ajustada, seja a demonstração de que a "
        "diferença, se existir, é inferior a dez pontos. Qualquer dos "
        "resultados é útil: indica se as acções devem concentrar-se nos "
        "currículos da saúde ou abranger todos os estudantes.",
        "Objectivo 5: a identificação dos factores associados, com "
        "associações prováveis com o sexo feminino, a residência sem a "
        "família, a existência de medicamentos guardados, a proximidade de "
        "uma farmácia e o nível de conhecimento "
        "{zeru2020,kifle2021,gebregziabher2024,helal2017}. Estes factores "
        "definem os subgrupos a quem dirigir as acções de sensibilização "
        "previstas no plano nacional contra a RAM {misau2019}.",
    ]),
]
DIVULGACAO = [
    P("Os resultados serão apresentados na defesa pública do trabalho de "
      "culminação do curso, na FCS. Um relatório com os resultados "
      "agregados será entregue ao CIBS-UniLúrio, à Reitoria e às direcções "
      "da FCS, da FAPF e da UBS, acompanhado de uma síntese de uma página "
      "com recomendações para os currículos e para os serviços de apoio ao "
      "estudante. Os resultados serão devolvidos à comunidade estudantil "
      "numa sessão aberta, organizada com a associação de estudantes, em "
      "tom informativo e não punitivo, sem apresentação de dados por "
      "turma."),
    P("Será preparado um artigo para uma revista com revisão por pares, de "
      "preferência de acesso aberto, redigido segundo a declaração STROBE e "
      "a lista CROSS, e uma comunicação para as jornadas científicas da "
      "UniLúrio e para encontros científicos nacionais de saúde. Os dados "
      "sobre fontes de obtenção de antibióticos e antimaláricos sem receita "
      "serão partilhados com a ANARME, em forma agregada, como contributo "
      "para a fiscalização e para a comunicação com o público."),
]

# ----------------------------------------------------- 11. cronograma -------
CRONOGRAMA_TEXTO = [
    P("O [[quadro:cronograma]] distribui as actividades pelos doze meses do "
      "estudo, de Outubro de 2026 a Setembro de 2027. A validação de "
      "conteúdo pelo painel de peritos decorre em paralelo com a submissão "
      "ao CIBS-UniLúrio, porque não envolve participantes; o pré-teste e a "
      "recolha só começam depois da aprovação ética e das autorizações, "
      "com o pré-teste em Fevereiro e Março e a recolha principal em Março "
      "e Abril de 2027, ajustadas ao calendário académico."),
]
CRONOGRAMA = {
    "inicio": (2026, 10),
    "n_meses": 12,
    "actividades": [
        ("Revisão da literatura e redacção do protocolo", [1, 2]),
        ("Validação de conteúdo do questionário pelo painel de peritos",
         [2, 3]),
        ("Submissão ao CIBS-UniLúrio e pedidos de autorização", [3, 4]),
        ("Obtenção das listas, sorteio e formação dos assistentes", [5]),
        ("Pré-teste, reteste e versão final do questionário", [5, 6]),
        ("Recolha de dados nas três unidades orgânicas", [6, 7]),
        ("Codificação, dupla digitação e limpeza dos dados", [7, 8]),
        ("Análise dos dados", [8, 9]),
        ("Redacção do relatório final", [9, 10]),
        ("Revisão pelo orientador e entrega", [11]),
        ("Defesa pública e devolução dos resultados", [12]),
    ],
}

# ----------------------------------------------------- 12. orcamento --------
ORCAMENTO_TEXTO = [
    P("A [[tabela:orcamento]] apresenta o orçamento estimado. As "
      "quantidades de impressão correspondem a 1.100 exemplares: 920 para "
      "a recolha principal, 92 para o pré-teste e uma reserva para o "
      "reteste e para inutilizações. As rubricas maiores são a impressão "
      "dos questionários, necessária por se tratar de um inquérito em "
      "papel que garante o anonimato, e o trabalho dos dois assistentes "
      "durante 15 dias cada, indispensável para que nenhum docente ou "
      "colega de turma aplique os questionários. A segunda digitação "
      "assegura a qualidade dos dados. O estudo será financiado com "
      "recursos próprios do estudante, sem prejuízo de um pedido de apoio "
      "à FCS; não haverá financiamento de empresas farmacêuticas."),
]
ORCAMENTO = [
    ("Impressão do questionário (6 páginas por exemplar)", "página", 6600, 4),
    ("Impressão da folha de informação ao participante", "página", 1100, 4),
    ("Impressão do folheto sobre automedicação responsável", "exemplar",
     1100, 5),
    ("Cartão de apoio plastificado com nomes genéricos", "unidade", 40, 150),
    ("Envelopes A4", "unidade", 1100, 5),
    ("Urnas de cartão com ranhura", "unidade", 6, 400),
    ("Fita de segurança numerada para selagem das urnas", "rolo", 6, 250),
    ("Esferográficas", "unidade", 500, 10),
    ("Assistentes de recolha de dados (2 assistentes, 15 dias cada)",
     "dia de trabalho", 30, 500),
    ("Formação dos assistentes (materiais)", "sessão", 1, 1500),
    ("Segunda digitação dos questionários", "questionário", 920, 10),
    ("Transporte urbano entre os locais de recolha", "dia", 40, 200),
    ("Comunicações (telefone e internet)", "mês", 8, 500),
    ("Impressão e encadernação do protocolo e do relatório final",
     "exemplar", 4, 1500),
    ("Caixa com fechadura para arquivo dos questionários", "unidade", 1,
     2500),
    ("Dispositivo de armazenamento encriptado", "unidade", 1, 1000),
]
ORCAMENTO_IMPREVISTOS = 0.10

# ----------------------------------------------------- apendices ------------
APENDICES = [
    ("Questionário sobre automedicação em estudantes da UniLúrio", [
        NOTA("Instruções ao participante: não escreva o seu nome nem o seu "
             "número de estudante em nenhuma folha. Responda sozinho(a), "
             "assinalando com X a opção escolhida. Pode deixar em branco "
             "qualquer pergunta. No fim, coloque o questionário dentro do "
             "envelope, feche-o e deposite-o na urna. Se não quiser "
             "participar, deposite o questionário em branco. Os números "
             "entre parênteses são os códigos usados na digitação."),
        PERG("Declaração de consentimento anónimo:",
             ["Li a folha de informação, compreendi o objectivo do estudo e "
              "aceito participar de forma voluntária e anónima (1)",
              "Não aceito participar e devolvo o questionário em branco "
              "(0)"]),
        H3("Secção A. Dados sociodemográficos e académicos"),
        PERG("A1. Unidade orgânica:",
             ["Faculdade de Ciências de Saúde (1)",
              "Faculdade de Arquitectura e Planeamento Físico (2)",
              "UniLúrio Business School (3)"]),
        PERG("A2. Curso:",
             ["Medicina (1)", "Medicina Dentária (2)", "Farmácia (3)",
              "Nutrição (4)", "Optometria (5)", "Enfermagem (6)",
              "Administração e Gestão em Saúde (7)",
              "Psicologia Clínica (8)",
              "Arquitectura e Planeamento Físico (9)",
              "Urbanismo e Ordenamento do Território (10)",
              "Contabilidade, Fiscalidade e Auditoria (11)",
              "Economia (12)", "Gestão Empresarial (13)"]),
        PERG("A3. Ano curricular em que está matriculado(a):",
             ["1.º (1)", "2.º (2)", "3.º (3)", "4.º (4)", "5.º (5)",
              "6.º (6)"]),
        PERG("A4. Idade em anos completos: ______"),
        PERG("A5. Sexo:", ["Masculino (1)", "Feminino (2)"]),
        PERG("A6. Onde vive durante o ano lectivo?",
             ["Com a família (1)", "Residência estudantil (2)",
              "Casa arrendada, sozinho(a) ou com colegas (3)",
              "Outra (4)"]),
        PERG("A7. Alguém do seu agregado familiar é profissional de saúde "
             "(médico, enfermeiro, farmacêutico ou técnico de saúde)?",
             ["Sim (1)", "Não (0)"]),
        PERG("A8. Valor mensal de que dispõe para despesas pessoais:",
             ["Menos de 1.000 MT (1)", "1.000 a 2.999 MT (2)",
              "3.000 a 4.999 MT (3)", "5.000 MT ou mais (4)",
              "Prefiro não responder (9)"]),
        PERG("A9. Já concluiu com aproveitamento alguma unidade curricular "
             "de farmacologia?", ["Sim (1)", "Não (0)"]),
        PERG("A10. Existe uma farmácia a 15 minutos ou menos, a pé, do "
             "local onde vive?", ["Sim (1)", "Não (0)", "Não sei (9)"]),
        PERG("A11. Quanto tempo leva a chegar à unidade sanitária mais "
             "próxima do local onde vive?",
             ["30 minutos ou menos (1)", "Mais de 30 minutos (2)",
              "Não sei (9)"]),
        PERG("A12. Tem neste momento medicamentos guardados no local onde "
             "vive?", ["Sim (1)", "Não (0)"]),
        PERG("A13. Como classifica o seu estado de saúde?",
             ["Bom (1)", "Razoável (2)", "Mau (3)"]),
        PERG("A14. Tem alguma doença crónica diagnosticada por um médico "
             "(por exemplo, asma, hipertensão, diabetes ou epilepsia)?",
             ["Sim (1)", "Não (0)"]),
        H3("Secção B. Uso de medicamentos nos últimos seis meses"),
        NOTA("Neste questionário, automedicação significa tomar um "
             "medicamento de farmácia (comprimidos, cápsulas, xaropes, "
             "injecções, pomadas ou outros) para si próprio(a), sem receita "
             "nem consulta de um médico ou de outro profissional que possa "
             "receitar. Conta também usar sobras guardadas, medicamentos "
             "dados por outras pessoas ou uma receita antiga, mesmo que o "
             "medicamento tenha sido aconselhado na farmácia. Não conta "
             "tomar um medicamento receitado para o problema actual nem "
             "usar remédios tradicionais."),
        PERG("B1. Nos últimos seis meses, esteve doente ou teve algum "
             "sintoma (dor, febre, tosse, diarreia ou outro)?",
             ["Sim (1)", "Não (0)"]),
        PERG("B2. Nos últimos seis meses, tomou algum medicamento por "
             "automedicação, segundo a definição acima?",
             ["Sim (1)", "Não (0)"],
             instrucao="Se respondeu Não, passe para a Secção E."),
        PERG("B3. Que tipos de medicamentos usou por automedicação nos "
             "últimos seis meses? (assinale todos os que se aplicam; "
             "consulte o cartão de apoio)",
             ["Analgésicos e antipiréticos, por exemplo paracetamol (1)",
              "Anti-inflamatórios, por exemplo ibuprofeno ou diclofenac "
              "(2)",
              "Antibióticos, por exemplo amoxicilina, cotrimoxazol, "
              "azitromicina, ciprofloxacina, doxiciclina ou metronidazol "
              "(3)",
              "Antimaláricos, por exemplo arteméter-lumefantrina, "
              "artesunato-amodiaquina ou quinino (4)",
              "Desparasitantes, por exemplo albendazol ou mebendazol (5)",
              "Antialérgicos, por exemplo clorfeniramina ou loratadina (6)",
              "Antiácidos e medicamentos para a azia e a acidez (7)",
              "Antidiarreicos ou sais de reidratação oral (8)",
              "Xaropes ou medicamentos para a tosse e a constipação (9)",
              "Vitaminas ou suplementos (10)",
              "Medicamentos para dormir ou para a ansiedade (11)",
              "Medicamentos para aumentar a concentração ou manter-se "
              "acordado(a) (12)",
              "Outros; quais? __________________ (13)"]),
        PERG("B4. Quantas vezes se automedicou nos últimos seis meses?",
             ["Uma vez (1)", "Duas ou três vezes (2)",
              "Quatro ou mais vezes (3)"]),
        H3("Secção C. Episódio mais recente de automedicação"),
        NOTA("Responda pensando apenas na última vez em que se automedicou."),
        PERG("C1. Qual foi a principal queixa?",
             ["Dor de cabeça (1)", "Febre (2)", "Outras dores (3)",
              "Tosse, gripe ou constipação (4)",
              "Diarreia ou dor de barriga (5)",
              "Suspeita de malária (6)", "Queixas urinárias ou genitais (7)",
              "Dor de dentes (8)", "Dor menstrual (9)",
              "Problema de pele (10)", "Outra; qual? __________ (11)"]),
        PERG("C2. Escreva o nome de cada medicamento que tomou, tal como "
             "estava na embalagem: 1. ______________ 2. ______________ "
             "3. ______________"),
        PERG("C3. Onde obteve o medicamento? (assinale a principal)",
             ["Farmácia privada (1)",
              "Farmácia de unidade sanitária pública (2)",
              "Vendedor ambulante ou mercado (3)",
              "Loja ou banca do bairro (4)", "Sobras guardadas em casa (5)",
              "Familiar, amigo(a) ou colega (6)",
              "Outra; qual? __________ (7)"]),
        PERG("C4. Quem ou o que o(a) orientou na escolha do medicamento? "
             "(assinale todas as que se aplicam)",
             ["Conhecimento próprio de experiências anteriores (1)",
              "Matérias estudadas no meu curso (2)",
              "Farmacêutico(a) ou técnico(a) de farmácia (3)",
              "Familiar (4)", "Amigo(a) ou colega (5)",
              "Receita antiga (6)", "Internet ou redes sociais (7)",
              "Folheto informativo (8)", "Outra; qual? __________ (9)"]),
        PERG("C5. Por que razão ou razões optou por se automedicar? "
             "(assinale todas as que se aplicam)",
             ["A doença parecia ligeira (1)",
              "Já tinha tido o mesmo problema e o medicamento resultou (2)",
              "Falta de tempo por causa das aulas (3)",
              "Espera longa na unidade sanitária (4)",
              "Custo da consulta ou do transporte (5)",
              "Unidade sanitária distante (6)",
              "Confiança nos meus conhecimentos (7)",
              "Mau atendimento em experiências anteriores (8)",
              "Queria alívio rápido (9)", "Outra; qual? __________ (10)"]),
        PERG("C6. Leu o folheto informativo do medicamento?",
             ["Sim (1)", "Não (0)", "Não havia folheto (8)"]),
        PERG("C7. A dose que tomou foi a indicada no folheto ou por quem o "
             "aconselhou?", ["Sim (1)", "Não (0)", "Não sei (9)"]),
        PERG("C8. Durante quantos dias tomou o medicamento? ______ dias"),
        PERG("C9. Parou o medicamento antes do fim previsto do tratamento?",
             ["Sim (1)", "Não (0)", "Não havia duração definida (8)"]),
        PERG("C10. Teve algum efeito indesejável que atribua ao "
             "medicamento?",
             ["Sim; qual? ______________ (1)", "Não (0)"]),
        PERG("C11. Depois de se automedicar, procurou uma unidade sanitária "
             "ou um profissional de saúde pelo mesmo problema?",
             ["Sim (1)", "Não (0)"]),
        H3("Secção D. Antibióticos e antimaláricos"),
        NOTA("Responda só se usou antibióticos ou antimaláricos por "
             "automedicação nos últimos seis meses; caso contrário, passe "
             "para a Secção E."),
        PERG("D1. Se usou um antibiótico, guardou ou deu a outra pessoa o "
             "que sobrou?", ["Sim (1)", "Não (0)", "Não sobrou (8)"]),
        PERG("D2. Se usou um antimalárico, fez teste de malária (teste "
             "rápido ou análise de sangue) antes de o tomar?",
             ["Sim, e o resultado foi positivo (1)",
              "Sim, e o resultado foi negativo (2)",
              "Não fiz teste (0)"]),
        PERG("D3. Se usou um antimalárico, tomou todas as doses da "
             "embalagem?", ["Sim (1)", "Não (0)"]),
        H3("Secção E. Conhecimento sobre o uso responsável de "
           "medicamentos"),
        NOTA("Para cada afirmação, assinale Verdadeiro (V), Falso (F) ou "
             "Não sei (NS). Cada resposta correcta vale 1 ponto e as "
             "respostas erradas ou Não sei valem 0 (pontuação de 0 a 10; "
             "bom 8 a 10, moderado 6 a 7, fraco 0 a 5). A chave, que não é "
             "impressa na versão entregue aos participantes, é: E1 F, E2 V, "
             "E3 F, E4 V, E5 V, E6 V, E7 F, E8 F, E9 F, E10 V."),
        ESCALA([
            "E1. Os antibióticos curam as infecções causadas por vírus, "
            "como a gripe e a constipação.",
            "E2. Usar antibióticos sem necessidade contribui para que as "
            "bactérias se tornem resistentes.",
            "E3. Um tratamento com antibiótico pode ser interrompido logo "
            "que os sintomas desaparecem.",
            "E4. Antes de tomar um antimalárico, a malária deve ser "
            "confirmada por teste rápido ou análise de sangue.",
            "E5. Tomar paracetamol acima da dose máxima diária pode causar "
            "lesão grave do fígado.",
            "E6. Anti-inflamatórios como o ibuprofeno e o diclofenac podem "
            "causar úlcera ou hemorragia digestiva.",
            "E7. Um medicamento que fez bem a uma pessoa é seguro para outra "
            "pessoa com sintomas parecidos.",
            "E8. Os medicamentos vendidos por vendedores ambulantes têm a "
            "mesma garantia de qualidade que os das farmácias licenciadas.",
            "E9. Um medicamento pode ser usado depois de expirado o prazo "
            "de validade se o aspecto não tiver mudado.",
            "E10. Alguns medicamentos interagem entre si ou com o álcool, "
            "reduzindo o efeito ou causando danos.",
        ], ["V", "F", "NS"]),
        H3("Secção F. Remédios tradicionais"),
        PERG("F1. Nos últimos seis meses, usou remédios tradicionais ou à "
             "base de plantas para tratar algum problema de saúde?",
             ["Sim (1)", "Não (0)"]),
        PERG("F2. Se sim, usou-os ao mesmo tempo que algum medicamento de "
             "farmácia?", ["Sim (1)", "Não (0)"]),
        NOTA("Obrigado pela sua participação. Coloque o questionário no "
             "envelope, feche-o e deposite-o na urna."),
        CAMPO("Número sequencial (atribuído na abertura da urna): ________"),
        NOTA("Na versão do pré-teste acrescenta-se, na primeira página, o "
             "código anónimo de emparelhamento para o reteste: duas "
             "primeiras letras do nome da mãe, dia de nascimento e duas "
             "primeiras letras do bairro de nascimento (por exemplo, "
             "MA-14-NA)."),
    ]),
    ("Folha de informação ao participante", [
        P("Título do estudo: Prevalência e determinantes da automedicação em "
          "estudantes da Universidade Lúrio, cidade de Nampula: comparação "
          "entre cursos da saúde e de outras áreas, 2027. Investigador: "
          "estudante finalista do curso de Licenciatura em Farmácia da "
          "Faculdade de Ciências de Saúde da UniLúrio, sob orientação de um "
          "docente da mesma faculdade."),
        P("Convidamo-lo(a) a participar num estudo que pretende saber com "
          "que frequência os estudantes da UniLúrio em Nampula tomam "
          "medicamentos sem receita nem consulta, que medicamentos usam, "
          "onde os obtêm e por que razões, e comparar os cursos da saúde com "
          "os de outras áreas. O seu nome foi seleccionado por sorteio a "
          "partir da lista de estudantes matriculados, ou toda a sua área "
          "foi convidada. A participação consiste em preencher sozinho(a) "
          "um questionário em papel, durante cerca de 20 minutos."),
        P("O questionário é anónimo: não tem nome, número de estudante nem "
          "assinatura. No fim, colocará o questionário num envelope fechado "
          "e depositá-lo-á numa urna selada, que só será aberta pelo "
          "investigador depois da sessão. Se não quiser participar, basta "
          "depositar o questionário em branco; ninguém saberá quem "
          "respondeu. A participação é voluntária, não tem qualquer efeito "
          "nas suas avaliações e os docentes não terão acesso às respostas. "
          "Pode deixar em branco qualquer pergunta."),
        P("O risco é mínimo: o tempo gasto e algum desconforto com perguntas "
          "sobre medicamentos. Não há pagamento. Todos os convidados "
          "recebem um folheto sobre automedicação responsável. Os "
          "resultados serão apresentados só em conjunto, nunca por turma, e "
          "devolvidos aos estudantes numa sessão aberta. O estudo foi "
          "aprovado pelo Comité Institucional de Bioética para a Saúde da "
          "Universidade Lúrio."),
        P("Se sentir febre alta que não passa, falta de ar, sangue nas fezes "
          "ou no vómito, manchas ou bolhas na pele, inchaço da face ou "
          "qualquer sintoma que piora, procure de imediato a unidade "
          "sanitária mais próxima. Se tiver dúvidas sobre o estudo ou sobre "
          "um efeito indesejável de um medicamento, pode contactar o "
          "investigador, que o(a) orientará."),
        CAMPO("Investigador, telefone: [preencher]"),
        CAMPO("Orientador(a), telefone: [preencher]"),
        CAMPO("CIBS-UniLúrio, telefone ou endereço electrónico: [preencher]"),
    ]),
    ("Declaração de consentimento anónimo e pedido de dispensa do "
     "consentimento escrito assinado", [
        P("A declaração de consentimento consta da primeira página do "
          "questionário e tem a seguinte redacção: «Li a folha de "
          "informação, compreendi o objectivo do estudo e aceito participar "
          "de forma voluntária e anónima.» O participante assinala a opção "
          "de aceitação ou a de recusa; não escreve nome nem assina."),
        P("Ao Comité Institucional de Bioética para a Saúde da Universidade "
          "Lúrio pede-se a dispensa do consentimento escrito assinado, com "
          "os seguintes fundamentos: o estudo é de risco mínimo e não "
          "envolve qualquer intervenção; os participantes são adultos "
          "alfabetizados, que lêem a folha de informação antes de decidir; "
          "a assinatura seria o único documento que ligaria cada estudante "
          "à participação e criaria um risco de identificação que o desenho "
          "procura eliminar; e o depósito do questionário preenchido, "
          "depois da leitura da informação e da assinalação da declaração, "
          "constitui manifestação inequívoca de vontade."),
        CAMPO("Nampula, ____ de ______________ de 2026"),
        CAMPO("O investigador: ______________________________"),
        CAMPO("O(a) orientador(a): __________________________"),
    ]),
    ("Pedido de autorização institucional", [
        P("Ao Magnífico Reitor da Universidade Lúrio, com conhecimento aos "
          "Directores da Faculdade de Ciências de Saúde, da Faculdade de "
          "Arquitectura e Planeamento Físico e da UniLúrio Business School."),
        P("Assunto: pedido de autorização para a realização de um inquérito "
          "anónimo a estudantes e para o acesso às listas de estudantes "
          "matriculados."),
        P("Eu, estudante finalista do curso de Licenciatura em Farmácia da "
          "Faculdade de Ciências de Saúde, venho solicitar autorização para "
          "realizar o estudo «Prevalência e determinantes da automedicação "
          "em estudantes da Universidade Lúrio, cidade de Nampula: "
          "comparação entre cursos da saúde e de outras áreas, 2027», "
          "aprovado pelo Comité Institucional de Bioética para a Saúde da "
          "Universidade Lúrio. O estudo consiste num questionário anónimo "
          "em papel, com cerca de 20 minutos, aplicado em Março e Abril de "
          "2027 a estudantes seleccionados por sorteio, no fim de uma aula "
          "e sem a presença do docente."),
        P("Solicito ainda que os serviços de registo académico forneçam as "
          "listas de estudantes matriculados por curso e ano curricular, "
          "apenas com o número de estudante e o nome, para o sorteio e o "
          "convite. As listas serão usadas exclusivamente para esse fim, "
          "guardadas em local fechado e destruídas no fim da recolha, e "
          "nunca serão associadas aos questionários. Os resultados serão "
          "entregues à Reitoria e às direcções em forma agregada, sem "
          "identificação de estudantes nem de turmas."),
        CAMPO("Nampula, ____ de ______________ de 2026"),
        CAMPO("O(a) estudante: ______________________________"),
        CAMPO("O(a) orientador(a): __________________________"),
        CAMPO("Despacho: ( ) Autorizado   ( ) Não autorizado   Data: ____"
              "/____/______   Assinatura e carimbo: ______________"),
    ]),
    ("Ficha de controlo da sessão de recolha", [
        NOTA("Preenchida pelo assistente em cada sessão e assinada no "
             "momento da abertura da urna. Não contém dados pessoais dos "
             "participantes."),
        CAMPO("Data: ____/____/2027   Hora de início: ______   Hora de fim: "
              "______"),
        CAMPO("Unidade orgânica: ( ) FCS   ( ) FAPF   ( ) UBS"),
        CAMPO("Curso: ______________________   Ano curricular: ______"),
        CAMPO("Visita: ( ) primeira   ( ) segunda   ( ) terceira"),
        CAMPO("Número de estudantes seleccionados: ______   Presentes: "
              "______"),
        CAMPO("Envelopes entregues: ______   Devolvidos preenchidos: "
              "______   Devolvidos em branco: ______"),
        CAMPO("Número da urna: ______   Número do selo de segurança: "
              "______"),
        CAMPO("Ocorrências: ______________________________________"),
        CAMPO("Assistente: ____________________   Testemunha na abertura da "
              "urna: ____________________"),
    ]),
    ("Folheto sobre automedicação responsável", [
        NOTA("Entregue a todos os estudantes convidados, participem ou não. "
             "Uma página, frente e verso."),
        P("Automedicação responsável: o que deve saber."),
        LISTA([
            "Sem receita, use apenas medicamentos de venda livre, para "
            "queixas ligeiras e por pouco tempo; leia sempre o folheto e "
            "respeite a dose.",
            "Os antibióticos só devem ser usados com receita: não tratam "
            "gripes nem constipações, e as sobras não se guardam nem se "
            "partilham.",
            "Com febre, faça o teste de malária antes de tomar um "
            "antimalárico e, se for positivo, tome todas as doses.",
            "Não ultrapasse a dose diária de paracetamol indicada no folheto "
            "e evite o álcool durante o tratamento.",
            "Os anti-inflamatórios podem causar úlcera e hemorragia "
            "digestiva: não os tome em jejum nem se tiver úlcera, e peça "
            "conselho em caso de gravidez.",
            "Compre medicamentos só em farmácias licenciadas e peça "
            "conselho ao farmacêutico; os medicamentos vendidos na rua não "
            "têm qualidade garantida.",
            "Procure a unidade sanitária se a febre não passar, se tiver "
            "falta de ar, sangue nas fezes ou no vómito, manchas ou bolhas "
            "na pele, ou se os sintomas piorarem.",
            "Se suspeitar de um efeito indesejável de um medicamento, fale "
            "com um profissional de saúde, que pode notificá-lo ao Sistema "
            "Nacional de Farmacovigilância.",
        ]),
    ]),
]
