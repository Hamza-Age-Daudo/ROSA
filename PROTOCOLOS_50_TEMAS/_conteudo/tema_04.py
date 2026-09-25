# -*- coding: utf-8 -*-
"""
Tema 04. Problemas relacionados com medicamentos em doentes internados na
enfermaria de Medicina do Hospital Central de Nampula (classificação PCNE V9.1).

Compor e validar:   python -X utf8 _motor/motor.py _conteudo/tema_04.py
Verificar fontes:   python -X utf8 _motor/refs.py verificar _conteudo/tema_04.py
"""
from blocos import (CAMPO, FORMULA, H3, LISTA, NOTA, P, PERG, QUADRO,
                    TABELA)

NUMERO = 4
SLUG = "PRM_Enfermaria_Medicina_HCN_PCNE"
TITULO = ("Problemas relacionados com medicamentos e contributo potencial do "
          "farmacêutico em doentes internados na enfermaria de Medicina do "
          "Hospital Central de Nampula, 2027")
DESENHO = ("Observacional, prospectivo, descritivo e analítico, com seguimento "
           "diário dos doentes durante o internamento")

AUTOR = "[Nome do(a) estudante]"
ORIENTADOR = "[Nome e grau académico do(a) orientador(a)]"

# ---------------------------------------------------------------- resumo --
RESUMO = (
    "Os problemas relacionados com medicamentos são acontecimentos ou "
    "circunstâncias que envolvem a farmacoterapia e que interferem, de forma "
    "real ou potencial, com os resultados de saúde desejados. Nos doentes "
    "internados em serviços de medicina, a polimedicação, as comorbilidades e "
    "a gravidade clínica tornam-nos frequentes, e estudos africanos referem "
    "que atingem cerca de dois terços destes doentes. Em Moçambique não foram "
    "encontrados estudos publicados sobre este problema em adultos "
    "internados, e o Hospital Central de Nampula, hospital de referência do "
    "norte do país, não dispõe de dados sobre a sua frequência, natureza e "
    "causas. O estudo tem como objectivo avaliar os problemas relacionados "
    "com medicamentos nos doentes adultos internados na enfermaria de "
    "Medicina do Hospital Central de Nampula e o contributo potencial das "
    "intervenções farmacêuticas, de Março a Junho de 2027. Trata-se de um "
    "estudo observacional, prospectivo, descritivo e analítico, com "
    "seguimento diário de cada doente desde a inclusão até à alta. Serão "
    "incluídos 364 doentes com dezoito ou mais anos e pelo menos 48 horas de "
    "internamento, seleccionados de forma consecutiva ou sistemática "
    "consoante o fluxo de admissões. As folhas de prescrição, as folhas de "
    "administração e os processos clínicos em papel serão revistos "
    "diariamente com uma ficha estruturada, e cada problema será classificado "
    "segundo a classificação da Pharmaceutical Care Network Europe, versão "
    "9.1, por dois avaliadores independentes, com medição da concordância. "
    "Serão também registadas as intervenções propostas aos prescritores, a "
    "sua aceitação e o seu impacto clínico potencial. A análise incluirá "
    "estatística descritiva, intervalos de confiança a 95% e regressão "
    "logística múltipla, com nível de significância de 5%. Espera-se obter a "
    "primeira estimativa local da frequência, dos tipos e das causas destes "
    "problemas e dos factores associados, fundamentando a integração do "
    "farmacêutico na equipa clínica do hospital.")
PALAVRAS_CHAVE = ["cuidados farmacêuticos", "doentes internados",
                  "farmácia clínica", "Moçambique",
                  "problemas relacionados com medicamentos"]
ABSTRACT = (
    "Drug-related problems are events or circumstances involving drug "
    "therapy that actually or potentially interfere with desired health "
    "outcomes. Among patients admitted to medical wards, polypharmacy, "
    "comorbidities and clinical severity make them frequent, and African "
    "studies report that they affect about two thirds of these patients. No "
    "published studies on this problem in hospitalised adults were found in "
    "Mozambique, and Nampula Central Hospital, the referral hospital for the "
    "north of the country, has no data on their frequency, nature and causes. "
    "This study aims to assess drug-related problems among adult patients "
    "admitted to the internal medicine ward of Nampula Central Hospital and "
    "the potential contribution of pharmacist interventions, from March to "
    "June 2027. It is an observational, prospective, descriptive and "
    "analytical study, with daily follow-up of each patient from inclusion to "
    "discharge. A total of 364 patients aged eighteen years or older and "
    "hospitalised for at least 48 hours will be included, selected "
    "consecutively or systematically according to the flow of admissions. "
    "Paper prescription charts, medication administration records and "
    "clinical files will be reviewed daily with a structured form, and each "
    "problem will be classified according to the Pharmaceutical Care Network "
    "Europe classification, version 9.1, by two independent reviewers, with "
    "measurement of agreement. The interventions proposed to prescribers, "
    "their acceptance and their potential clinical impact will also be "
    "recorded. The analysis will include descriptive statistics, 95% "
    "confidence intervals and multiple logistic regression, with a 5% "
    "significance level. The study is expected to provide the first local "
    "estimate of the frequency, types and causes of these problems and of "
    "the associated factors, supporting the integration of the pharmacist "
    "into the hospital clinical team.")
KEYWORDS = ["clinical pharmacy", "drug-related problems", "inpatients",
            "Mozambique", "pharmaceutical care"]

ABREVIATURAS = [
    ("ANARME", "Autoridade Nacional Reguladora de Medicamento"),
    ("ATC", "classificação Anatómica Terapêutica Química"),
    ("CIBS-UniLúrio", "Comité Institucional de Bioética para a Saúde da "
                      "Universidade Lúrio"),
    ("CLEO", "Clinical, Economic and Organisational (ferramenta de "
             "avaliação do impacto clínico, económico e organizacional das "
             "intervenções farmacêuticas)"),
    ("CNBS", "Comité Nacional de Bioética para a Saúde"),
    ("DPS", "Direcção Provincial de Saúde"),
    ("FCS", "Faculdade de Ciências de Saúde"),
    ("FNM", "Formulário Nacional de Medicamentos"),
    ("HCN", "Hospital Central de Nampula"),
    ("HIV", "vírus da imunodeficiência humana"),
    ("IC", "intervalo de confiança"),
    ("LNME", "Lista Nacional de Medicamentos Essenciais"),
    ("MISAU", "Ministério da Saúde"),
    ("OMS", "Organização Mundial da Saúde"),
    ("OR", "odds ratio"),
    ("PCNE", "Pharmaceutical Care Network Europe"),
    ("PRM", "problemas relacionados com medicamentos"),
    ("SPSS", "Statistical Package for the Social Sciences"),
    ("STROBE", "Strengthening the Reporting of Observational Studies in "
               "Epidemiology"),
]

# ------------------------------------------------------------ referencias --
FONTES = {
    # -- magnitude global dos danos associados a medicamentos
    "panagioti2019": "Panagioti M, Khan K, Keers RN, Abuzour A, Phipps D, Kontopantelis E, et al. Prevalence, severity, and nature of preventable patient harm across medical care settings: systematic review and meta-analysis. BMJ. 2019;366:l4185. doi:10.1136/bmj.l4185. PMID: 31315828.",
    "hodkinson2020": "Hodkinson A, Tyler N, Ashcroft DM, Keers RN, Khan K, Phipps D, et al. Preventable medication harm across health care settings: a systematic review and meta-analysis. BMC Med. 2020;18(1):313. doi:10.1186/s12916-020-01774-9. PMID: 33153451.",
    "oms2017": "World Health Organization. Medication without harm: WHO global patient safety challenge [Internet]. Geneva: World Health Organization; 2017 [citado 2026 Set 19]. Disponível em: https://www.who.int/publications/i/item/WHO-HIS-SDS-2017.6",
    "oms2021": "World Health Organization. Global patient safety action plan 2021-2030: towards eliminating avoidable harm in health care [Internet]. Geneva: World Health Organization; 2021 [citado 2026 Set 19]. Disponível em: https://www.who.int/publications/i/item/9789240032705",
    "pcne2020": "Pharmaceutical Care Network Europe Association. Classification for drug related problems V9.1 [Internet]. Zuidlaren: PCNE Association; 2020 [citado 2026 Set 19]. Disponível em: https://pcne.org/wp-content/uploads/2026/01/PCNE_classification_V9-1-en-2026.pdf",
    "patel2022": "Patel TK, Patel PB, Bhalla HL, Kishore S. Drug-related deaths among inpatients: a meta-analysis. Eur J Clin Pharmacol. 2022;78(2):267-278. doi:10.1007/s00228-021-03214-w. PMID: 34661726.",
    "masnoon2017": "Masnoon N, Shakib S, Kalisch-Ellett L, Caughey GE. What is polypharmacy? A systematic review of definitions. BMC Geriatr. 2017;17(1):230. doi:10.1186/s12877-017-0621-2. PMID: 29017448.",
    "oms2019": "World Health Organization. Medication safety in polypharmacy: technical report [Internet]. Geneva: World Health Organization; 2019 [citado 2026 Set 19]. Disponível em: https://www.who.int/publications/i/item/WHO-UHC-SDS-2019.11",
    "dawoud2019": "Dawoud DM, Smyth M, Ashe J, Strong T, Wonderling D, Hill J, et al. Effectiveness and cost effectiveness of pharmacist input at the ward level: a systematic review and meta-analysis. Res Social Adm Pharm. 2019;15(10):1212-1222. doi:10.1016/j.sapharm.2018.10.006. PMID: 30389320.",
    # -- Africa
    "mekonnen2018": "Mekonnen AB, Alhawassi TM, McLachlan AJ, Brien JE. Adverse Drug Events and Medication Errors in African Hospitals: A Systematic Review. Drugs Real World Outcomes. 2018;5(1):1-24. doi:10.1007/s40801-017-0125-6. PMID: 29138993.",
    "ayele2021": "Ayele Y, Tesfaye ZT. Drug-related problems in Ethiopian public healthcare settings: Systematic review and meta-analysis. SAGE Open Med. 2021;9:20503121211009728. doi:10.1177/20503121211009728. PMID: 33948177.",
    "kyomya2023": "Kyomya J, Atwiine F, Shegena EA, Muhindo R, Yadesa TM. Drug-related problems and associated factors among patients with kidney dysfunction at a tertiary hospital in southwestern Uganda: a prospective observational study. BMC Nephrol. 2023;24(1):375. doi:10.1186/s12882-023-03437-2. PMID: 38114948.",
    "amankwa2022": "Amankwa Harrison M, Marfo AFA, Buabeng KO, Nkansah FA, Boateng DP, Ankrah DNA. Drug-related problems among hospitalized hypertensive and heart failure patients and physician acceptance of pharmacists' interventions at a teaching hospital in Ghana. Health Sci Rep. 2022;5(5):e786. doi:10.1002/hsr2.786. PMID: 36032513.",
    "belayneh2018": "Belayneh YM, Amberbir G, Agalu A. A prospective observational study of drug therapy problems in medical ward of a referral hospital in northeast Ethiopia. BMC Health Serv Res. 2018;18(1):808. doi:10.1186/s12913-018-3612-x. PMID: 30348153.",
    "bekele2021a": "Bekele F, Tsegaye T, Negash E, Fekadu G. Magnitude and determinants of drug-related problems among patients admitted to medical wards of southwestern Ethiopian hospitals: A multicenter prospective observational study. PLoS One. 2021;16(3):e0248575. doi:10.1371/journal.pone.0248575. PMID: 33725022.",
    "bekele2021b": "Bekele F, Fekadu G, Bekele K, Dugassa D, Sori J. Drug-related problems among patients with infectious disease admitted to medical wards of Wollega University Referral Hospital: Prospective observational study. SAGE Open Med. 2021;9:2050312121989625. doi:10.1177/2050312121989625. PMID: 33552517.",
    "endalifer2025": "Endalifer BL, Ayta YD, Tsigie AW, Wondmkun YT, Kassa MT, Amare GG, et al. Drug-therapy-related problems and pharmacist interventions in the medical ward in northeast Ethiopia: focus on types, acceptability, and impacts. Front Pharmacol. 2025;16:1558864. doi:10.3389/fphar.2025.1558864. PMID: 40260379.",
    "dagnew2022": "Dagnew SB, Binega Mekonnen G, Gebeye Zeleke E, Agegnew Wondm S, Yimer Tadesse T. Clinical Pharmacist Intervention on Drug-Related Problems among Elderly Patients Admitted to Medical Wards of Northwest Ethiopia Comprehensive Specialized Hospitals: A Multicenter Prospective, Observational Study. Biomed Res Int. 2022;2022:8742998. doi:10.1155/2022/8742998. PMID: 35898673.",
    "sefera2022": "Sefera B, Getachew M, Babu Y, Bekele F, Fanta K. Drug-related problems and its predictors among hospitalized heart failure patients at Jimma Medical Center, South West Ethiopia: prospective interventional study. BMC Cardiovasc Disord. 2022;22(1):418. doi:10.1186/s12872-022-02859-4. PMID: 36123632.",
    "eneh2020": "Eneh PC, Hullsiek KH, Kiiza D, Rhein J, Meya DB, Boulware DR, et al. Prevalence and nature of potential drug-drug interactions among hospitalized HIV patients presenting with suspected meningitis in Uganda. BMC Infect Dis. 2020;20(1):572. doi:10.1186/s12879-020-05296-w. PMID: 32758158.",
    # -- outros contextos hospitalares
    "abunahlah2018": "Abunahlah N, Elawaisi A, Velibeyoglu FM, Sancar M. Drug related problems identified by clinical pharmacist at the Internal Medicine Ward in Turkey. Int J Clin Pharm. 2018;40(2):360-367. doi:10.1007/s11096-017-0585-5. PMID: 29380236.",
    "reinau2019": "Reinau D, Furrer C, Stämpfli D, Bornand D, Meier CR. Evaluation of drug-related problems and subsequent clinical pharmacists' interventions at a Swiss university hospital. J Clin Pharm Ther. 2019;44(6):924-931. doi:10.1111/jcpt.13017. PMID: 31408206.",
    # -- Moçambique e Nampula
    "gudo2025": "Gudo ES, McCabe KC, Fazito E, Catano D, Tiberi O, Boothe M, et al. HIV incidence and prevalence among adults in Mozambique: estimates from the Population-based HIV Impact Assessment Survey (INSIDA 2021) and district-level modelling. J Int AIDS Soc. 2025;28(11):e70008. doi:10.1002/jia2.70008. PMID: 41152562.",
    "jessen2018": "Jessen N, Damasceno A, Silva-Matos C, Tuzine E, Madede T, Mahoque R, et al. Hypertension in Mozambique: trends between 2005 and 2015. J Hypertens. 2018;36(4):779-784. doi:10.1097/HJH.0000000000001618. PMID: 29210894.",
    "ins2022": "Instituto Nacional de Saúde (Moçambique). Mozambique Population-based HIV Impact Assessment, INSIDA 2021: summary sheet [Internet]. Maputo: Instituto Nacional de Saúde; 2022 [citado 2026 Set 19]. Disponível em: https://phia.icap.columbia.edu/wp-content/uploads/2022/12/53059_14_INSIDA_Summary-sheet-Web.pdf",
    "belo2017": "Belo C, Naidoo S. Prevalence and risk factors for latent tuberculosis infection among healthcare workers in Nampula Central Hospital, Mozambique. BMC Infect Dis. 2017;17(1):408. doi:10.1186/s12879-017-2516-4. PMID: 28595594.",
    "xavier2022": "Xavier SP, Victor A, Cumaquela G, Vasco MD, Rodrigues OAS. Inappropriate use of antibiotics and its predictors in pediatric patients admitted at the Central Hospital of Nampula, Mozambique. Antimicrob Resist Infect Control. 2022;11(1):79. doi:10.1186/s13756-022-01115-w. PMID: 35655272.",
    "xavier2024": "Xavier SP, da Silva AMC, Victor A. Antibiotic prescribing patterns in pediatric patients using the WHO access, watch, reserve (AWaRe) classification at a quaternary hospital in Nampula, Mozambique. Sci Rep. 2024;14(1):22719. doi:10.1038/s41598-024-72349-4. PMID: 39349590.",
    "bull2017": "Bull ER, Mason C, Junior FD, Santos LV, Scott A, Ademokun D, et al. Developing nurse medication safety training in a health partnership in Mozambique using behavioural science. Global Health. 2017;13(1):45. doi:10.1186/s12992-017-0265-1. PMID: 28676121.",
    "lei12_2017": "República de Moçambique. Lei n.º 12/2017, de 8 de Setembro: Lei de medicamento, vacinas e outros produtos biológicos para o uso humano. Boletim da República, I Série, n.º 141 [Internet]. Maputo: Imprensa Nacional de Moçambique; 2017 [citado 2026 Set 19]. Disponível em: https://anarme.gov.mz/download/lei-12-2017-de-8-de-setembro-lei-de-medicamento/",
    "misau2017": "Ministério da Saúde (Moçambique). Lista nacional de medicamentos essenciais [Internet]. Maputo: Ministério da Saúde, Departamento Farmacêutico; 2017 [citado 2026 Set 19]. Disponível em: https://afro.who.int/sites/default/files/2018-07/LISTA%20NACIONAL%20DE%20MEDICAMENTOS%20ESSENCIAIS%202017.pdf",
    "mboane2025": "Mboane N. MISAU lança Formulário de Medicamentos e Lista de diagnósticos. O País [Internet]. Maputo: O País; 2025 [citado 2026 Set 19]. Disponível em: https://opais.co.mz/misau-lanca-formulario-de-medicamentos-e-lista-de-diagnosticos/",
    "anarme2024": "Autoridade Nacional Reguladora de Medicamento. Farmacovigilância e ensaios clínicos [Internet]. Maputo: ANARME; 2024 [citado 2026 Set 19]. Disponível em: https://anarme.gov.mz/farmacovigilancia-e-ensaios-clinicos/",
    "lei3_2023": "República de Moçambique. Lei n.º 3/2023, de 8 de Junho: Lei de Investigação em Saúde Humana [Internet]. Maputo: Imprensa Nacional de Moçambique; 2023 [citado 2026 Set 19]. Disponível em: https://anarme.gov.mz/download/lei-3-2023-de-8-de-junho-lei-de-investigacao-em-saude-humana/",
    # -- classificação, instrumentos e métodos
    "pcne2021": "Horvat N, Westerlund T, Richling I. Executive summary: online international validation round coding of upgraded PCNE DRP cases using PCNE DRP Classification V9.1 [Internet]. Zuidlaren: Pharmaceutical Care Network Europe Association; 2021 [citado 2026 Set 19]. Disponível em: https://pcne.org/wp-content/uploads/2026/02/International-Validation-Project-2019-2021-Summary.pdf",
    "koubaity2019": "Koubaity M, Lelubre M, Sansterre G, Amighi K, De Vriese C. Adaptation and validation of PCNE drug-related problem classification v6.2 in French-speaking Belgian community pharmacies. Int J Clin Pharm. 2019;41(1):244-250. doi:10.1007/s11096-018-0773-y. PMID: 30610541.",
    "vo2021": "Vo HT, Charpiat B, Chanoine S, Juste M, Roubille R, Rose FX, et al. CLEO: a multidimensional tool to assess clinical, economic and organisational impacts of pharmacists' interventions. Eur J Hosp Pharm. 2021;28(4):193-200. doi:10.1136/ejhpharm-2020-002642. PMID: 33883205.",
    "berger2026": "Berger V, van der Linde A, Cuba L, Horn C, Köster D, Lanzinger H, et al. Nationwide validation of the CLEO tool to evaluate the relevance of pharmacists' interventions in German hospitals. Int J Clin Pharm. 2026;48(3):897-908. doi:10.1007/s11096-025-02085-w. PMID: 41701301.",
    "liverpool2026": "University of Liverpool. Liverpool HIV interactions: drug interaction checker [Internet]. Liverpool: University of Liverpool; 2026 [citado 2026 Set 19]. Disponível em: https://www.hiv-druginteractions.org/",
    "medscape2026": "Medscape. Drug interaction checker [Internet]. New York: WebMD; 2026 [citado 2026 Set 19]. Disponível em: https://reference.medscape.com/drug-interactionchecker",
    "naranjo1981": "Naranjo CA, Busto U, Sellers EM, Sandor P, Ruiz I, Roberts EA, et al. A method for estimating the probability of adverse drug reactions. Clin Pharmacol Ther. 1981;30(2):239-45. doi:10.1038/clpt.1981.154. PMID: 7249508.",
    "cockcroft1976": "Cockcroft DW, Gault MH. Prediction of creatinine clearance from serum creatinine. Nephron. 1976;16(1):31-41. doi:10.1159/000180580. PMID: 1244564.",
    "whocc2026": "WHO Collaborating Centre for Drug Statistics Methodology. ATC/DDD index [Internet]. Oslo: Norwegian Institute of Public Health; 2026 [citado 2026 Set 19]. Disponível em: https://atcddd.fhi.no/atc_ddd_index/",
    "li2023": "Li M, Gao Q, Yu T. Kappa statistic considerations in evaluating inter-rater reliability between two raters: which, when and context matters. BMC Cancer. 2023;23(1):799. doi:10.1186/s12885-023-11325-z. PMID: 37626309.",
    "mchugh2012": "McHugh ML. Interrater reliability: the kappa statistic. Biochem Med (Zagreb). 2012;22(3):276-82. PMID: 23092060.",
    "wang2020": "Wang X, Ji X. Sample Size Estimation in Clinical Research: From Randomized Controlled Trials to Observational Studies. Chest. 2020;158(1S):S12-S20. doi:10.1016/j.chest.2020.03.010. PMID: 32658647.",
    "peduzzi1996": "Peduzzi P, Concato J, Kemper E, Holford TR, Feinstein AR. A simulation study of the number of events per variable in logistic regression analysis. J Clin Epidemiol. 1996;49(12):1373-9. doi:10.1016/s0895-4356(96)00236-3. PMID: 8970487.",
    "vonelm2007": "von Elm E, Altman DG, Egger M, Pocock SJ, Gøtzsche PC, Vandenbroucke JP. The Strengthening the Reporting of Observational Studies in Epidemiology (STROBE) statement: guidelines for reporting observational studies. Lancet. 2007;370(9596):1453-7. doi:10.1016/S0140-6736(07)61602-X. PMID: 18064739.",
    "wma2025": "World Medical Association. World Medical Association Declaration of Helsinki: Ethical Principles for Medical Research Involving Human Participants. JAMA. 2025;333(1):71-74. doi:10.1001/jama.2024.21972. PMID: 39425955.",
}
SEMINAIS = {
    "naranjo1981": ("Artigo original da escala de probabilidade de reacções "
                    "adversas de Naranjo, instrumento de causalidade ainda "
                    "usado nos estudos africanos recentes de PRM e aplicado "
                    "neste protocolo."),
    "cockcroft1976": ("Artigo original da equação de Cockcroft-Gault, base "
                      "dos ajustes posológicos à função renal nos resumos "
                      "das características dos medicamentos."),
    "mchugh2012": ("Artigo de referência para a interpretação do kappa de "
                   "Cohen em investigação em saúde, que fixa o limiar de "
                   "0,60 usado na calibração dos avaliadores."),
    "peduzzi1996": ("Estudo de simulação que fundamenta a regra de pelo "
                    "menos 10 eventos por variável na regressão logística."),
    "vonelm2007": ("Declaração STROBE, norma de relato dos estudos "
                   "observacionais, sem versão posterior que a substitua."),
}

# ----------------------------------------------------- 1. introducao --------
INTRODUCAO = [
    P("Os medicamentos são a intervenção terapêutica mais usada nos "
      "hospitais e, ao mesmo tempo, uma das fontes mais frequentes de dano "
      "evitável. Uma meta-análise de 70 estudos, com 337.025 doentes, "
      "estimou que cerca de um em cada 20 doentes sofre dano evitável nos "
      "cuidados de saúde, que 12% desses danos são graves ou fatais e que os "
      "incidentes relacionados com medicamentos representam 25% do total "
      "{panagioti2019}. Uma revisão posterior, restrita aos medicamentos, "
      "encontrou dano evitável em 3% e dano de qualquer natureza em 9% dos "
      "registos analisados {hodkinson2020}. Perante esta dimensão, a "
      "Organização Mundial da Saúde (OMS) lançou em 2017 o desafio global "
      "para a segurança do doente «Medicação sem danos», com a meta de "
      "reduzir em 50%, em cinco anos, os danos graves e evitáveis associados "
      "aos medicamentos {oms2017}, e adoptou depois o plano de acção global "
      "para a segurança do doente de 2021 a 2030, orientado para a "
      "eliminação dos danos evitáveis nos cuidados de saúde {oms2021}."),
    P("Uma parte substancial destes danos resulta de problemas relacionados "
      "com medicamentos (PRM), definidos pela Pharmaceutical Care Network "
      "Europe (PCNE) como acontecimentos ou circunstâncias que envolvem a "
      "farmacoterapia e que interferem, de forma real ou potencial, com os "
      "resultados de saúde desejados {pcne2020}. Os doentes internados em "
      "serviços de medicina interna reúnem as condições que os favorecem: "
      "doenças múltiplas, tratamento simultâneo com vários medicamentos, "
      "alterações da função renal e hepática e mudanças frequentes da "
      "prescrição ao longo do internamento {masnoon2017,oms2019}. Uma "
      "meta-análise de 23 estudos atribuiu aos medicamentos 5,6% das mortes "
      "hospitalares e considerou evitáveis 45,2% dessas mortes "
      "{patel2022}. Em contrapartida, os ensaios aleatorizados sobre a "
      "integração do farmacêutico na equipa da enfermaria mostram redução "
      "média de 1,74 dias no internamento e maior satisfação dos doentes, "
      "com relação custo-efectividade favorável quando a presença é regular "
      "{dawoud2019}."),
    P("Em África a evidência é mais escassa e desigualmente distribuída. "
      "Uma revisão sistemática de 51 estudos hospitalares, provenientes de "
      "apenas nove dos 54 países do continente, encontrou erros de "
      "prescrição numa mediana de 57,4% das prescrições avaliadas e "
      "problemas de dose em 15,5%, e considerou evitáveis 43,5% dos "
      "acontecimentos adversos a medicamentos {mekonnen2018}. Na Etiópia, "
      "país que concentra a maior parte dos estudos africanos sobre o tema, "
      "uma meta-análise de 17 estudos estimou que 69,4% dos doentes "
      "apresentam pelo menos um PRM {ayele2021}. No Uganda, 79,3% dos "
      "doentes com disfunção renal seguidos num hospital regional de "
      "referência tinham PRM {kyomya2023} e, no "
      "Gana, foram identificados em média 1,84 PRM por doente internado com "
      "hipertensão ou insuficiência cardíaca {amankwa2022}."),
    P("Moçambique acumula condições que tornam a farmacoterapia hospitalar "
      "particularmente complexa. A prevalência do vírus da imunodeficiência "
      "humana (HIV) nos adultos era de 12,5% em 2021, e estima-se que cerca "
      "de 2,2 milhões de adultos vivessem com a infecção em 2023 "
      "{gudo2025}. Em paralelo, a hipertensão arterial atingia 38,9% dos "
      "adultos de 25 a 64 anos em 2014-2015, e apenas 14,5% dos hipertensos "
      "conheciam o diagnóstico {jessen2018}. A coexistência de doenças "
      "infecciosas e crónicas traduz-se em esquemas com anti-retrovirais, "
      "antibacilares, antibióticos e medicamentos cardiovasculares, entre os "
      "quais as interacções clinicamente relevantes são frequentes "
      "{eneh2020}. O quadro normativo nacional, definido pela Lei n.º "
      "12/2017, atribui aos prescritores e aos que dispensam medicamentos o "
      "dever de contribuir para o seu uso racional e cria a Autoridade "
      "Nacional Reguladora de Medicamento (ANARME) {lei12_2017}, e o "
      "Ministério da Saúde (MISAU) publicou a Lista Nacional de "
      "Medicamentos Essenciais (LNME) em 2017 e lançou uma nova edição do "
      "Formulário Nacional de Medicamentos (FNM) em Maio de 2025 "
      "{misau2017,mboane2025}."),
    P("O Hospital Central de Nampula (HCN) é a unidade terciária de "
      "referência para as províncias de Nampula, Cabo Delgado e Niassa, "
      "servindo uma população estimada em 8,5 milhões de habitantes, com "
      "cerca de 500 camas {belo2017}. Na província de Nampula, a prevalência "
      "do HIV nos adultos era de 10,0% em 2021, mas apenas 47,9% dos adultos "
      "que viviam com a infecção tinham carga viral suprimida, contra 64,1% "
      "no conjunto do país {ins2022}, o que faz prever que a enfermaria de "
      "Medicina receba doentes com infecções oportunistas e tratamentos "
      "complexos. Os únicos estudos publicados sobre a utilização de "
      "medicamentos no HCN referem-se a crianças internadas: 97,5% recebiam "
      "antibióticos, quase sempre por via injectável, e a prescrição de três "
      "ou mais antibióticos associou-se a utilização inadequada "
      "{xavier2022,xavier2024}."),
    P("As pesquisas bibliográficas efectuadas não identificaram estudos "
      "publicados sobre PRM em adultos internados em Moçambique, nem dados "
      "sobre a frequência, a natureza e as causas destes problemas na "
      "enfermaria de Medicina do HCN. O trabalho publicado mais próximo é "
      "uma parceria internacional que desenvolveu, no Hospital Central da "
      "Beira, formação contínua em cálculo de doses para enfermeiros, "
      "aplicada a 87 e depois a 36 profissionais, e que assinalou as "
      "barreiras de oportunidade à segurança da medicação e a dificuldade "
      "de medir os erros de medicação no país {bull2017}. Esta lacuna "
      "impede o hospital de "
      "dimensionar e orientar um serviço de farmácia clínica e impede a "
      "comparação com os estudos de outros países africanos, que usam cada "
      "vez mais a classificação da PCNE como linguagem comum. O presente "
      "estudo propõe-se avaliar, de forma prospectiva e com revisão diária "
      "das folhas de prescrição e dos processos clínicos, os PRM dos doentes "
      "adultos internados nesta enfermaria entre Março e Junho de 2027, "
      "classificá-los segundo a versão 9.1 da classificação da PCNE, "
      "identificar os factores associados à sua ocorrência e documentar o "
      "contributo potencial das intervenções farmacêuticas propostas à "
      "equipa clínica."),
]

# ----------------------------------------------------- 2. problema ----------
PROBLEMA = [
    P("Na enfermaria de Medicina do HCN convergem adultos referidos de três "
      "províncias, muitos com doenças avançadas e várias condições em "
      "simultâneo, tratados com prescrições manuscritas em folhas de papel, "
      "sem apoio informático à decisão e com a verificação da terapêutica "
      "dependente da atenção individual de cada profissional. Nestas "
      "condições, a dose calculada sem ajuste à função renal, a duplicação "
      "de medicamentos da mesma classe, a interacção entre anti-retrovirais "
      "e antibacilares ou a omissão de um tratamento indicado podem passar "
      "despercebidas durante dias. A Lei n.º 12/2017 proíbe que os "
      "profissionais de farmácia modifiquem uma prescrição sem autorização "
      "expressa do prescritor {lei12_2017}, pelo que a correcção de um PRM "
      "detectado pelo farmacêutico depende sempre de comunicação estruturada "
      "com a equipa médica, que não está descrita, tanto quanto foi "
      "possível apurar, em nenhum estudo publicado sobre este hospital."),
    P("As consequências destes problemas são clínicas, económicas e "
      "sanitárias. Os PRM não resolvidos traduzem-se em tratamentos "
      "ineficazes, reacções adversas, internamentos mais longos e mortes "
      "evitáveis {patel2022,hodkinson2020}. Nos estudos africanos, os "
      "antibióticos, em particular a ceftriaxona, figuram entre os "
      "medicamentos mais envolvidos {belayneh2018,bekele2021a}, e no próprio "
      "HCN a utilização de antibióticos em crianças internadas mostrou "
      "padrões de uso inadequado {xavier2022}, o que acrescenta aos danos "
      "individuais o risco colectivo da resistência aos antimicrobianos. "
      "Sem dados locais, a direcção do hospital não dispõe de fundamento "
      "para decidir onde colocar farmacêuticos, que classes de medicamentos "
      "vigiar em primeiro lugar ou que tipo de formação dirigir às equipas "
      "clínicas e de enfermagem."),
    P("Falta, por isso, conhecer quantos doentes internados na enfermaria de "
      "Medicina apresentam PRM, que tipos de problemas e que causas "
      "predominam, que medicamentos estão mais envolvidos, que factores se "
      "associam à sua ocorrência e em que medida as intervenções propostas "
      "por um farmacêutico seriam aceites e úteis. A revisão sistemática "
      "etíope sublinhou que a heterogeneidade dos sistemas de classificação "
      "dificulta a comparação entre estudos e recomendou a adopção de uma "
      "classificação uniforme {ayele2021}. A classificação PCNE, que separa "
      "o problema das suas causas e regista a intervenção, a aceitação e o "
      "estado final de cada problema {pcne2020}, responde a essa exigência e "
      "permite medir, além da frequência dos PRM, o contributo potencial do "
      "farmacêutico."),
]
PERGUNTA = ("Qual é a frequência, a natureza e as causas dos problemas "
            "relacionados com medicamentos, segundo a classificação da "
            "Pharmaceutical Care Network Europe, nos doentes adultos "
            "internados na enfermaria de Medicina do Hospital Central de "
            "Nampula entre Março e Junho de 2027, que factores se associam à "
            "sua ocorrência e que contributo potencial têm as intervenções "
            "farmacêuticas para a sua resolução?")
DELIMITACAO = [
    P("O estudo decorre na enfermaria de Medicina do HCN, na cidade de "
      "Nampula, e abrange os doentes com dezoito ou mais anos nela "
      "internados durante pelo menos 48 horas, incluídos entre 1 de Março e "
      "30 de Junho de 2027 e seguidos até à alta, ao óbito ou à "
      "transferência. O objecto de estudo são os PRM identificados na "
      "prescrição, na administração e na monitorização da terapêutica "
      "durante o internamento, classificados segundo os cinco domínios da "
      "versão 9.1 da classificação da PCNE (problemas, causas, intervenções "
      "planeadas, aceitação e estado do problema), e o impacto clínico "
      "potencial das intervenções propostas à equipa médica."),
    P("Ficam fora do âmbito os serviços de Pediatria, Cirurgia, Ginecologia "
      "e Obstetrícia e os cuidados intensivos, os doentes da consulta "
      "externa e as grávidas, cujo tratamento obedece a normas próprias. O "
      "estudo não avalia o efeito das intervenções sobre a mortalidade, a "
      "duração do internamento ou os custos, porque não inclui grupo de "
      "comparação, não aprecia o desempenho individual de médicos, "
      "enfermeiros ou farmacêuticos e não inclui a fase posterior à alta. O "
      "uso de medicamentos tradicionais é registado apenas como informação "
      "referida pelo doente, sem identificação das plantas."),
]

# ----------------------------------------------------- 3. objectivos --------
OBJECTIVO_GERAL = (
    "Avaliar os problemas relacionados com medicamentos nos doentes adultos "
    "internados na enfermaria de Medicina do Hospital Central de Nampula, "
    "segundo a classificação da PCNE versão 9.1, e o contributo potencial das "
    "intervenções farmacêuticas, entre Março e Junho de 2027.")
OBJECTIVOS_ESPECIFICOS = [
    "Caracterizar o perfil sociodemográfico, clínico e farmacoterapêutico "
    "dos doentes incluídos.",
    "Determinar a proporção de doentes com pelo menos um PRM durante o "
    "internamento, o número de PRM por doente e a taxa de PRM por 100 "
    "doentes-dia.",
    "Classificar os PRM identificados segundo os domínios de problemas e de "
    "causas da classificação da PCNE, versão 9.1, e identificar os grupos "
    "terapêuticos e os medicamentos mais envolvidos.",
    "Descrever as intervenções farmacêuticas propostas, a sua aceitação pelos "
    "prescritores, o estado final dos PRM e o impacto clínico potencial das "
    "intervenções.",
    "Analisar a associação entre a polimedicação e outros factores "
    "sociodemográficos e clínicos e a ocorrência de pelo menos um PRM.",
]

# ----------------------------------------------------- 4. hipoteses ---------
HIPOTESES_INTRO = [
    P("As hipóteses referem-se ao objectivo específico 5, única componente "
      "analítica do estudo, e serão testadas por regressão logística "
      "múltipla. O primeiro par diz respeito à polimedicação, factor "
      "principal para o qual foi verificado o poder do estudo; o segundo par "
      "abrange os restantes factores incluídos no modelo."),
]
HIPOTESES = [
    ("H0", "não existe associação estatisticamente significativa entre a "
           "polimedicação (cinco ou mais medicamentos em simultâneo) e a "
           "ocorrência de pelo menos um PRM durante o internamento, após "
           "ajustamento para os restantes factores."),
    ("H1", "existe associação estatisticamente significativa entre a "
           "polimedicação e a ocorrência de pelo menos um PRM durante o "
           "internamento, após ajustamento para os restantes factores."),
    ("H0", "nenhum dos factores idade igual ou superior a 60 anos, sexo, "
           "duas ou mais comorbilidades, infecção por HIV, função renal "
           "diminuída, sinais de gravidade à admissão e internamento "
           "superior a sete dias se associa de forma estatisticamente "
           "significativa à ocorrência de pelo menos um PRM."),
    ("H1", "pelo menos um destes factores associa-se de forma "
           "estatisticamente significativa à ocorrência de pelo menos um "
           "PRM."),
]
QUESTOES = [
    "Qual é o perfil sociodemográfico, clínico e farmacoterapêutico dos "
    "doentes internados na enfermaria de Medicina do HCN?",
    "Que proporção de doentes apresenta pelo menos um PRM e quantos PRM "
    "ocorrem por doente e por 100 doentes-dia de internamento?",
    "Que domínios de problemas e de causas da classificação PCNE predominam "
    "e que grupos terapêuticos estão mais envolvidos?",
    "Que intervenções farmacêuticas são propostas, com que taxa de aceitação "
    "e de resolução e com que impacto clínico potencial?",
]

# ----------------------------------------------------- 5. justificativa -----
JUSTIFICATIVA_INTRO = [
    P("O estudo justifica-se pela combinação de três circunstâncias: a "
      "elevada frequência de PRM documentada nos hospitais africanos, a "
      "ausência de qualquer estimativa moçambicana em adultos internados e a "
      "existência de um quadro legal que já atribui aos profissionais de "
      "saúde deveres de uso racional e de farmacovigilância sem que se "
      "conheça a dimensão do problema que esses deveres pretendem resolver "
      "{ayele2021,lei12_2017}."),
]
JUSTIFICATIVA = {
    "cientifica": [
        P("O estudo produz a primeira estimativa local, com intervalos de "
          "confiança, da frequência, dos tipos e das causas dos PRM em "
          "adultos internados num hospital central moçambicano, com uma "
          "classificação comparável à dos estudos etíopes, ugandeses e "
          "ganenses que usam a PCNE {bekele2021a,kyomya2023,amankwa2022}. "
          "O desenho prospectivo, com comparação diária entre a folha de "
          "prescrição e a folha de administração, permite captar causas "
          "ligadas à administração pelos profissionais, que os estudos "
          "retrospectivos não conseguem observar. Acresce a medição formal "
          "da concordância entre avaliadores, necessária porque a própria "
          "ronda internacional de validação da versão 9.1 obteve uma "
          "consistência média de codificação de 76%, abaixo do limiar de "
          "80% fixado pela PCNE {pcne2021}, e a avaliação do impacto "
          "clínico potencial das intervenções com uma ferramenta validada "
          "{vo2021}."),
    ],
    "academica": [
        P("Para a Faculdade de Ciências de Saúde (FCS) da Universidade "
          "Lúrio, o protocolo introduz no trabalho de fim de curso da "
          "licenciatura em Farmácia uma actividade de farmácia clínica "
          "exercida à cabeceira do doente, em articulação com médicos e "
          "enfermeiros, e deixa instrumentos reutilizáveis: a ficha de "
          "seguimento, as regras operacionais de identificação dos PRM e o "
          "procedimento de comunicação com o prescritor. Prolonga ainda a "
          "linha de investigação iniciada por docentes da própria "
          "universidade sobre a utilização de antibióticos no HCN "
          "{xavier2022,xavier2024}, alargando-a aos adultos e ao conjunto "
          "da farmacoterapia."),
    ],
    "social": [
        P("Os doentes da enfermaria de Medicina, muitos com HIV, "
          "tuberculose ou doenças cardiovasculares, dependem de esquemas "
          "longos e complexos em que um erro de dose ou uma interacção não "
          "detectada pode comprometer o tratamento e prolongar o "
          "internamento, com custos para as famílias que acompanham o "
          "doente {eneh2020,patel2022}. Durante o próprio estudo, os PRM "
          "validados serão comunicados à equipa clínica, o que confere aos "
          "participantes um benefício directo. A médio prazo, a redução "
          "de antibióticos desnecessários contribui para travar a "
          "resistência aos antimicrobianos, um bem colectivo "
          "{xavier2022}."),
    ],
    "politica": [
        P("A Lei n.º 12/2017 obriga os profissionais de saúde a comunicar "
          "as reacções adversas, torna obrigatória a prescrição pela "
          "denominação comum internacional, restringe o sector público aos "
          "medicamentos do FNM e da LNME e confere à ANARME a promoção do "
          "uso racional do medicamento {lei12_2017}. O estudo fornece ao "
          "MISAU, à ANARME e à direcção do HCN indicadores objectivos para "
          "concretizar estas disposições no meio hospitalar e para "
          "responder à meta da OMS de reduzir para metade os danos graves e "
          "evitáveis associados aos medicamentos {oms2017,oms2021}. Os "
          "resultados sobre a aceitação das intervenções servem ainda de "
          "base para definir a função do farmacêutico hospitalar nas "
          "enfermarias, que a evidência internacional associa a menor "
          "duração do internamento {dawoud2019}."),
    ],
}

# ----------------------------------------------------- 6. revisao -----------
REVISAO = [
    ("Conceitos e definições operacionais", [
        P("A PCNE define PRM como um acontecimento ou circunstância que "
          "envolve a farmacoterapia e que interfere, de forma real ou "
          "potencial, com os resultados de saúde desejados, e distingue o "
          "problema, que é o efeito real ou esperado sobre o doente, da "
          "causa, que é a acção ou a omissão que o origina {pcne2020}. O "
          "documento de apoio da classificação sublinha que a causa "
          "corresponde muitas vezes ao que outros autores designam erro de "
          "medicação, mas que um erro não gera necessariamente um PRM e que "
          "pode existir PRM sem erro, como sucede com uma reacção adversa "
          "numa dose correcta {pcne2020}. O problema é classificado como "
          "potencial quando ainda não produziu efeito no doente e como "
          "manifesto quando esse efeito já é observável."),
        P("A polimedicação não tem definição consensual: uma revisão "
          "sistemática reuniu 138 definições em 110 artigos, das quais a "
          "mais frequente é o uso diário de cinco ou mais medicamentos "
          "{masnoon2017}. A OMS reconhece que o número de medicamentos, só "
          "por si, não distingue a polimedicação apropriada da inadequada, "
          "e recomenda a revisão sistemática da medicação centrada no "
          "doente {oms2019}. Estes conceitos convertem-se, neste estudo, em "
          "definições operacionais precisas, descritas na metodologia."),
        P("Para efeitos do estudo, considera-se PRM toda a situação "
          "identificada pelo primeiro avaliador e confirmada pelo segundo, "
          "ou decidida por consenso, que satisfaça um dos critérios "
          "operacionais do [[quadro:definicoes_prm]], classificada segundo "
          "a versão 9.1 da PCNE. A polimedicação corresponde ao uso "
          "simultâneo de cinco ou mais medicamentos prescritos no mesmo dia "
          "de internamento, excluindo soluções de hidratação sem fármaco, "
          "oxigénio e sangue. A unidade de contagem é o problema, pelo que "
          "um doente pode ter vários PRM e um PRM pode ter mais do que uma "
          "causa e originar mais do que uma intervenção {pcne2020}."),
    ]),
    ("Sistemas de classificação e a classificação PCNE versão 9.1", [
        P("A classificação PCNE nasceu em 1999 e é revista periodicamente; a "
          "versão 9.1 resultou de uma ronda de validação e de uma reunião de "
          "peritos em Fevereiro de 2020 e é compatível, com adaptações, com "
          "a versão 8 {pcne2020}. Organiza-se em três domínios primários de "
          "problemas (efectividade do tratamento, segurança do tratamento e "
          "outros), nove domínios de causas (selecção do medicamento, forma "
          "farmacêutica, selecção da dose, duração do tratamento, dispensa, "
          "processo de uso, doente, transferência do doente e outras), cinco "
          "domínios de intervenções planeadas, três de aceitação e quatro de "
          "estado do problema, desdobrados em 6 subdomínios de problemas, "
          "38 de causas, 17 de intervenções e 10 de aceitação {pcne2020}."),
        P("Os tipos de PRM que motivam este estudo encontram na versão 9.1 "
          "códigos próprios, reproduzidos no quadro de critérios "
          "operacionais da metodologia. A dose demasiado baixa e a dose "
          "demasiado alta pertencem ao domínio de selecção da dose (C3); a "
          "duplicação inadequada de grupo terapêutico ou de substância "
          "activa e a combinação inadequada de medicamentos, ou de "
          "medicamentos com plantas ou suplementos, ao domínio de selecção "
          "do medicamento (C1); e a indicação não tratada é um problema de "
          "efectividade (P1) cuja causa se situa nesse mesmo domínio, por "
          "ausência de tratamento apesar de existir indicação {pcne2020}. "
          "A classificação inclui ainda o domínio C6, "
          "relativo à administração por profissionais de saúde, e o domínio "
          "C8, relativo à reconciliação da medicação na transferência entre "
          "níveis de cuidados, ambos pertinentes num internamento."),
        P("Outros sistemas coexistem na literatura africana, em particular a "
          "classificação de Cipolle e Strand, usada na meta-análise etíope e "
          "em vários estudos da Etiópia {ayele2021,dagnew2022}. Essa "
          "meta-análise documentou relato inconsistente dos PRM entre "
          "estudos e recomendou a adopção de uma abordagem uniforme "
          "{ayele2021}. A escolha da PCNE neste "
          "protocolo assenta em três vantagens: separa o problema da causa, "
          "o que orienta a intervenção; regista a aceitação e o desfecho de "
          "cada intervenção, o que permite medir o contributo do "
          "farmacêutico; e é a classificação usada pelos estudos mais "
          "recentes em enfermarias africanas {bekele2021a,endalifer2025,"
          "kyomya2023}."),
        P("A fiabilidade da classificação é o seu ponto mais sensível. Na "
          "ronda internacional de validação da versão 9.1, 158 "
          "farmacêuticos de dez países codificaram 20 casos padronizados, "
          "com consistência média de 76%: 80% nos problemas, 75% nas "
          "intervenções e 73% nas causas, face ao limiar de 80% considerado "
          "satisfatório {pcne2021}. Na adaptação belga da versão 6.2, 74 "
          "dos 83 itens mostraram elevada consistência de codificação e a "
          "resolução de cada PRM exigiu em média cinco minutos "
          "{koubaity2019}. Estes resultados justificam a formação prévia dos "
          "avaliadores, a codificação independente por dois avaliadores e a "
          "medição da concordância previstas neste protocolo."),
    ]),
    ("Magnitude, natureza e consequências dos PRM em doentes internados", [
        P("Os PRM são frequentes em qualquer sistema de saúde. Numa "
          "enfermaria de medicina interna de Istambul, dois farmacêuticos "
          "clínicos e um internista encontraram pelo menos um PRM potencial "
          "em 80% de 100 doentes, com 1,6 problemas por doente, e as causas "
          "mais frequentes foram a selecção do medicamento (44,78%) e a "
          "selecção da dose (27,61%) {abunahlah2018}. Num hospital "
          "universitário suíço, as rondas interdisciplinares de medicina "
          "interna identificaram 5.024 PRM em 5.441 doentes, sendo a dose "
          "inadequada a causa principal, e 97,8% das intervenções aceites "
          "tinham benefício clínico esperado, 11,1% dele considerado "
          "importante {reinau2019}."),
        P("Nas enfermarias de medicina africanas, as proporções de doentes "
          "com PRM situam-se habitualmente entre dois terços e três quartos. "
          "Num hospital de referência do nordeste da Etiópia, 75,51% de 147 "
          "doentes tiveram pelo menos um problema, sobretudo necessidade de "
          "tratamento adicional (35,85%) e tratamento desnecessário "
          "(30,19%), e os antibióticos estiveram envolvidos em 40,32% dos "
          "casos {belayneh2018}. Num estudo multicêntrico em três hospitais "
          "do sudoeste etíope, com a classificação PCNE, a proporção foi de "
          "67,7% em 313 doentes, com 1,06 PRM por doente e predomínio da "
          "prescrição desnecessária (27,79%) {bekele2021a}. Em doentes "
          "internados por doenças infecciosas, a proporção atingiu 71,51% "
          "{bekele2021b}."),
        P("Nem todos os estudos convergem. Num hospital etíope que usou a "
          "versão 9.1 da PCNE e dois farmacêuticos clínicos, apenas 27,3% dos "
          "183 doentes tiveram PRM, embora com 2,36 problemas por doente "
          "afectado {endalifer2025}. A diferença ilustra o peso das "
          "decisões metodológicas: a inclusão ou não de problemas "
          "potenciais, a contagem da não adesão anterior ao internamento, o "
          "perfil dos avaliadores e o sistema de classificação alteram a "
          "estimativa. Quanto às consequências, a revisão africana de "
          "Mekonnen e colaboradores estimou que 43,5% dos acontecimentos "
          "adversos a medicamentos eram evitáveis {mekonnen2018}, e uma "
          "meta-análise internacional atribuiu aos medicamentos 5,6% da "
          "mortalidade hospitalar {patel2022}."),
    ]),
    ("Determinantes dos PRM", [
        P("A polimedicação é o determinante mais consistente. No estudo "
          "multicêntrico do sudoeste etíope, associou-se aos PRM com "
          "*odds ratio* (OR) ajustado de 3,23, e o internamento superior a "
          "sete dias com OR ajustado de 9,79 {bekele2021a}. Em idosos "
          "internados no noroeste da Etiópia, a polimedicação (OR ajustado "
          "de 3,06), o número de comorbilidades (1,48 por comorbilidade), a "
          "duração do internamento (2,32) e o consumo de álcool (2,2) "
          "associaram-se aos PRM {dagnew2022}; em doentes com insuficiência "
          "cardíaca, a polimedicação (2,94), as comorbilidades (2,59) e o "
          "internamento superior a 18 dias (3,77) tiveram o mesmo papel "
          "{sefera2022}. A meta-análise etíope confirma a idade, a "
          "polimedicação, as comorbilidades e a duração do internamento como "
          "os factores mais relatados {ayele2021}."),
        P("A função renal é um determinante específico do meio hospitalar. "
          "No Uganda, 79,3% dos doentes com disfunção renal tinham PRM, com "
          "predomínio da indicação não tratada (35,6%) e dos acontecimentos "
          "adversos possíveis (28,3%), e os antimicrobianos eram os "
          "medicamentos mais envolvidos no tratamento desnecessário e no "
          "tratamento subóptimo {kyomya2023}. Na Turquia, o número de PRM "
          "correlacionou-se com a idade, o número de medicamentos, a "
          "duração do internamento e a função renal {abunahlah2018}. Como a maioria dos medicamentos de eliminação "
          "renal exige ajuste pela depuração da creatinina, a ausência de "
          "creatinina sérica ou de peso nos processos limita a detecção "
          "destes problemas, aspecto que o estudo terá de medir."),
        P("A infecção por HIV acrescenta um determinante próprio: as "
          "interacções. Em 1.074 doentes com HIV internados no Uganda com "
          "suspeita de meningite, foram identificadas em média 4,27 "
          "interacções potenciais por doente, 11,3% delas contra-indicadas e "
          "66,4% graves, envolvendo sobretudo fluconazol, cotrimoxazol, "
          "efavirenz e rifampicina, com discordância entre as bases de "
          "interacções consultadas {eneh2020}. Importa notar que a duração "
          "do internamento pode ser simultaneamente factor de risco e "
          "consequência dos PRM, o que exige prudência na interpretação da "
          "sua associação e justifica uma análise de sensibilidade sem esta "
          "variável."),
    ]),
    ("O farmacêutico na equipa clínica e a avaliação das intervenções", [
        P("A presença do farmacêutico na equipa da enfermaria tem evidência "
          "experimental: numa revisão de 18 ensaios aleatorizados, a "
          "intervenção regular do farmacêutico reduziu a duração do "
          "internamento em 1,74 dias e aumentou a satisfação dos doentes e "
          "cuidadores (risco relativo de 1,49), sendo custo-efectiva quando "
          "assegurada ao longo de todo o internamento {dawoud2019}. Nos "
          "hospitais africanos, a aceitação das intervenções pelos "
          "prescritores é elevada: 84,7% em idosos etíopes, com 67,4% dos "
          "PRM totalmente resolvidos {dagnew2022}, 71,6% num hospital "
          "universitário do Gana {amankwa2022} e cerca de três quartos (106 "
          "de 143 intervenções) num hospital do nordeste etíope "
          "{endalifer2025}."),
        P("A aceitação, porém, não mede o valor clínico da intervenção. A "
          "ferramenta CLEO (Clinical, Economic and Organisational), "
          "desenvolvida pela Sociedade Francesa de Farmácia Clínica, avalia "
          "três dimensões independentes, e a dimensão clínica usa uma "
          "escala de seis níveis, de -1 (intervenção prejudicial) a 4 "
          "(prevenção de uma consequência fatal) {vo2021}. Na validação "
          "original, a fiabilidade entre avaliadores da dimensão clínica foi "
          "boa, com coeficientes de correlação intraclasse de 0,693 na fase "
          "interna e 0,649 na externa {vo2021}. Numa validação nacional "
          "alemã com 79 farmacêuticos de 56 hospitais, a fiabilidade entre "
          "avaliadores foi fraca nas três dimensões, embora a fiabilidade "
          "intra-avaliador tenha sido boa {berger2026}."),
        P("No hospital etíope que aplicou a ferramenta CLEO, 36,4% das "
          "intervenções tiveram impacto clínico menor, 8,4% impacto "
          "importante e 4,9% impacto negativo {endalifer2025}. Estes "
          "resultados, juntamente com a fraca concordância observada na "
          "Alemanha, mostram que o impacto clínico deve ser atribuído por "
          "mais do que um avaliador, com consenso final, e interpretado como "
          "impacto potencial e não como efeito demonstrado. É com esta "
          "reserva que o presente estudo usa o termo «contributo "
          "potencial» do farmacêutico."),
    ]),
    ("Enquadramento normativo moçambicano", [
        P("A Lei n.º 12/2017, de 8 de Setembro, revogou a Lei n.º 4/98 e "
          "estabelece as regras de produção, distribuição, uso e garantia "
          "de qualidade dos medicamentos, vacinas e produtos biológicos e de "
          "saúde {lei12_2017}. Entre os seus objectivos figura o "
          "estabelecimento de um sistema de farmacovigilância eficiente, "
          "destinado a detectar precocemente os efeitos adversos, e a lei "
          "cria a ANARME, a quem compete, entre outras funções, elaborar e "
          "manter actualizados o FNM e a LNME, garantir a farmacovigilância "
          "e promover o uso racional do medicamento {lei12_2017}."),
        P("No capítulo sobre prescrição e utilização, a lei determina que "
          "no Serviço Nacional de Saúde apenas se utilizem os medicamentos "
          "do FNM ou da LNME, torna obrigatória a prescrição pela "
          "denominação comum internacional, proíbe a modificação ou a "
          "substituição de uma prescrição pelos profissionais de farmácia "
          "sem autorização expressa do prescritor e atribui aos que "
          "prescrevem e aos que dispensam o dever especial de contribuir "
          "para o uso racional {lei12_2017}. Determina ainda que os "
          "profissionais de saúde dos sectores público e privado comuniquem "
          "as reacções adversas e os problemas de eficácia ou de qualidade de "
          "que tenham conhecimento {lei12_2017}."),
        P("A LNME de 2017 é de uso obrigatório pelos profissionais de saúde "
          "em todo o processo de aquisição, distribuição e prescrição no "
          "Serviço Nacional de Saúde, organiza os medicamentos em 31 grupos "
          "terapêuticos com o respectivo nível de prescrição e reserva "
          "alguns ao nível 4, por exigirem meios de diagnóstico ou cuidados "
          "especializados {misau2017}. A nova edição do FNM, "
          "lançada em Maio de 2025, destina-se a facilitar o acesso dos "
          "profissionais à informação sobre todos os medicamentos aprovados "
          "no Sistema Nacional de Saúde e a apoiar o controlo das "
          "prescrições e o uso racional {mboane2025}. Estes dois documentos "
          "constituem, por isso, a referência primária do estudo para "
          "apreciar a selecção e a dose dos medicamentos."),
        P("O Sistema Nacional de Farmacovigilância, gerido pela ANARME, "
          "integra um centro e uma comissão nacionais, responsáveis de "
          "farmacovigilância provinciais, distritais e das unidades "
          "sanitárias, os profissionais de saúde e os próprios doentes "
          "{anarme2024}. A investigação que envolve seres humanos rege-se "
          "pela Lei n.º 3/2023, de 8 de Junho, Lei de Investigação em "
          "Saúde Humana {lei3_2023}. Estes instrumentos definem o circuito "
          "pelo qual as reacções adversas detectadas no estudo serão "
          "notificadas e o enquadramento em que o protocolo será apreciado."),
    ]),
    ("Métodos de identificação dos PRM e fontes de referência", [
        P("Os PRM podem ser identificados por revisão da documentação "
          "clínica, por entrevista ao doente, por análise de resultados "
          "laboratoriais ou pela combinação destes métodos, com critérios "
          "explícitos ou por julgamento clínico implícito. Os estudos "
          "africanos recentes recorrem à revisão dos processos durante o "
          "internamento, complementada por instrumentos normalizados para a "
          "adesão, a causalidade das reacções adversas e as interacções "
          "{bekele2021a,dagnew2022}. A revisão prospectiva tem a "
          "vantagem de permitir confrontar a prescrição com a administração "
          "e de comunicar os problemas enquanto ainda podem ser corrigidos."),
        P("Para as interacções, a escolha da fonte altera o resultado, "
          "porque as bases disponíveis não classificam da mesma forma a "
          "mesma combinação {eneh2020}. A base de interacções da "
          "Universidade de Liverpool, de acesso livre, é a referência "
          "habitual para os anti-retrovirais {liverpool2026,eneh2020}, e o "
          "verificador de interacções da Medscape, também de acesso livre e "
          "usado em estudos etíopes {dagnew2022}, classifica as combinações "
          "em contra-indicadas, graves com recomendação de alternativa, "
          "significativas com necessidade de monitorização e menores "
          "{medscape2026}. Para reduzir a subjectividade, o estudo considera "
          "PRM apenas as interacções das categorias mais graves e aquelas "
          "cuja monitorização recomendada não esteja documentada."),
        P("A causalidade das suspeitas de reacção adversa será apreciada "
          "com a escala de Naranjo, de dez perguntas, que classifica a "
          "relação como definida, provável, possível ou duvidosa "
          "{naranjo1981} e que é usada nos estudos africanos de PRM "
          "{bekele2021a,dagnew2022}. A função renal será estimada pela "
          "depuração da creatinina segundo a equação de Cockcroft-Gault "
          "{cockcroft1976}, e os medicamentos serão agrupados segundo a "
          "classificação Anatómica Terapêutica Química (ATC) da OMS "
          "{whocc2026}. Como a identificação e a classificação dependem de "
          "julgamento, a concordância entre dois avaliadores será medida "
          "pelo kappa de Cohen nas variáveis nominais e pelo kappa ponderado "
          "nas ordinais {li2023}; valores inferiores a 0,60 indicam "
          "concordância inadequada {mchugh2012}."),
    ]),
]

# ----------------------------------------------------- 7. estado da arte ----
ESTADO_ARTE = [
    P("O [[quadro:estado_arte]] sintetiza os estudos empíricos mais "
      "relevantes dos últimos dez anos sobre PRM em doentes internados, com "
      "destaque para as enfermarias de medicina africanas, e inclui o único "
      "conjunto de estudos moçambicanos sobre utilização de medicamentos no "
      "HCN, embora dirigido a crianças e apenas aos antibióticos."),
    QUADRO("estado_arte",
           "Síntese de estudos sobre problemas relacionados com medicamentos "
           "em doentes internados (estado da arte)",
           ["Autor (ano)", "Local", "Desenho (n)", "Principais resultados"],
           [["Belayneh et al. (2018) {belayneh2018}",
             "Etiópia, Dessie, enfermaria de medicina",
             "Observacional prospectivo (147)",
             "75,51% com pelo menos um problema; 159 problemas; necessidade "
             "de tratamento adicional 35,85%; antibióticos em 40,32%; "
             "ceftriaxona o medicamento mais envolvido (25,81%)."],
            ["Bekele et al. (2021) {bekele2021a}",
             "Etiópia, três hospitais do sudoeste",
             "Prospectivo multicêntrico, PCNE (313)",
             "67,7% com PRM; 1,06 PRM por doente; prescrição desnecessária "
             "27,79%; internamento superior a sete dias (OR ajustado 9,79) "
             "e polimedicação (3,23) associados."],
            ["Bekele et al. (2021) {bekele2021b}",
             "Etiópia, Nekemte, doenças infecciosas",
             "Prospectivo, PCNE (172)",
             "71,51% com PRM; necessidade de tratamento adicional 22,77%; "
             "internamento de sete ou mais dias (OR ajustado 4,40) e "
             "comorbilidade (2,11) associados."],
            ["Dagnew et al. (2022) {dagnew2022}",
             "Etiópia, noroeste, idosos",
             "Prospectivo multicêntrico, Cipolle (389)",
             "68,4% com PRM; 1,32 por doente; dose demasiado alta 21,5%; "
             "polimedicação (OR ajustado 3,06); 84,7% das intervenções "
             "aceites e 67,4% dos PRM resolvidos."],
            ["Sefera et al. (2022) {sefera2022}",
             "Etiópia, Jimma, insuficiência cardíaca",
             "Prospectivo de intervenção, PCNE V9.0 (237)",
             "66,2% com PRM; problemas de efectividade 55,48%; "
             "polimedicação (OR ajustado 2,94), comorbilidade (2,59) e "
             "internamento superior a 18 dias (3,77)."],
            ["Endalifer et al. (2025) {endalifer2025}",
             "Etiópia, Debre Berhan, enfermaria de medicina",
             "Prospectivo de intervenção, PCNE V9.1 e CLEO (183)",
             "27,3% com PRM; 2,36 por doente afectado; 143 intervenções, "
             "106 aceites; impacto clínico menor 36,4%, importante 8,4% e "
             "negativo 4,9%."],
            ["Kyomya et al. (2023) {kyomya2023}",
             "Uganda, Mbarara, disfunção renal",
             "Observacional prospectivo, PCNE V9.1 (174)",
             "79,3% com PRM; 219 problemas; indicação não tratada 35,6%; "
             "internamento de cinco ou mais dias (OR ajustado 6,39)."],
            ["Amankwa Harrison et al. (2022) {amankwa2022}",
             "Gana, Acra, hipertensão e insuficiência cardíaca",
             "Transversal prospectivo, PCNE V8.02 (134)",
             "247 PRM em 134 doentes; 1,84 por doente; interacções 10,5%; "
             "erros de administração 10,1%; aceitação pelos médicos "
             "71,6%."],
            ["Eneh et al. (2020) {eneh2020}",
             "Uganda, Kampala, HIV com suspeita de meningite",
             "Retrospectivo (1.074)",
             "4,27 interacções potenciais por doente; 11,3% contra-indicadas "
             "e 66,4% graves; fluconazol em 58,4%; discordância entre bases "
             "de interacções."],
            ["Abunahlah et al. (2018) {abunahlah2018}",
             "Turquia, Istambul, medicina interna",
             "Transversal, PCNE V7.0 (100)",
             "80% com PRM potencial; 1,6 por doente; causas: selecção do "
             "medicamento 44,78% e da dose 27,61%."],
            ["Reinau et al. (2019) {reinau2019}",
             "Suíça, Basileia, medicina interna",
             "Retrospectivo (5.441)",
             "5.024 PRM; dose inadequada a causa principal; 97,8% das "
             "intervenções aceites com benefício clínico esperado, 11,1% "
             "importante."],
            ["Ayele e Tesfaye (2021) {ayele2021}",
             "Etiópia",
             "Revisão sistemática e meta-análise (17 estudos)",
             "Proporção agregada de 69,4% (IC 95% 61,5-77,4); factores: "
             "idade, polimedicação, comorbilidades e duração do "
             "internamento."],
            ["Mekonnen et al. (2018) {mekonnen2018}",
             "África (9 países)",
             "Revisão sistemática (51 estudos)",
             "Erros de prescrição em mediana de 57,4% das prescrições; "
             "problemas de dose em 15,5%; 43,5% dos acontecimentos adversos "
             "evitáveis."],
            ["Xavier et al. (2022) {xavier2022}",
             "Moçambique, HCN, Pediatria",
             "Transversal retrospectivo, 464 antibióticos",
             "97,5% das crianças com antibiótico; três ou mais antibióticos "
             "(OR 2,83) e internamento curto (OR 1,88) associados a uso "
             "inadequado."],
            ],
           larguras=[3.3, 2.8, 3.0, 6.9],
           fonte="Elaboração própria (2026), a partir das fontes citadas."),
    P("A leitura do quadro revela um padrão consistente: nas enfermarias de "
      "medicina africanas, entre dois terços e quatro quintos dos doentes "
      "têm pelo menos um PRM, com predomínio das falhas de selecção do "
      "medicamento e da dose, forte envolvimento dos antibióticos e "
      "associação reiterada com a polimedicação, as comorbilidades e a "
      "duração do internamento {ayele2021,bekele2021a,dagnew2022,"
      "kyomya2023}. As intervenções dos farmacêuticos são aceites em 70% a "
      "85% dos casos {amankwa2022,dagnew2022,endalifer2025}. A divergência "
      "mais marcada, a proporção de 27,3% num hospital etíope "
      "{endalifer2025}, mostra que a definição de caso, a inclusão de "
      "problemas potenciais e o perfil dos avaliadores pesam tanto como o "
      "contexto, o que reforça a necessidade de critérios operacionais "
      "explícitos e de medição da concordância."),
    P("A evidência está concentrada na Etiópia e, em menor grau, no Uganda "
      "e no Gana; não foi encontrado nenhum estudo moçambicano sobre PRM em "
      "adultos internados, e os estudos do HCN limitam-se aos antibióticos "
      "em crianças {xavier2022,xavier2024}. Poucos estudos africanos "
      "avaliam o impacto clínico das intervenções com uma ferramenta "
      "validada ou medem a concordância entre avaliadores. O presente "
      "estudo preenche estas lacunas ao produzir dados locais, com a versão "
      "9.1 da PCNE, dupla avaliação independente, critérios operacionais "
      "explícitos e avaliação do impacto clínico potencial das "
      "intervenções."),
]
ESQUEMA_TEXTO = [
    P("A [[figura:esquema]] representa o modelo que orienta o estudo. Os "
      "factores sociodemográficos, clínicos, farmacoterapêuticos e do "
      "processo de cuidados actuam sobre a ocorrência de PRM, o desfecho "
      "principal, que se desdobra no número, no tipo, na causa e na "
      "resolução dos problemas. A gravidade clínica à admissão e o mês de "
      "inclusão, que pode reflectir a aprendizagem da equipa com as "
      "intervenções comunicadas, são tratados como variáveis de "
      "confundimento a controlar na análise."),
]
ESQUEMA_TITULO = ("Esquema conceptual dos factores associados aos problemas "
                  "relacionados com medicamentos em doentes internados")
ESQUEMA = {
    "contexto": ("Enfermaria de Medicina do Hospital Central de Nampula, "
                 "adultos internados, Março a Junho de 2027"),
    "blocos": [
        ("Factores sociodemográficos",
         ["idade", "sexo", "escolaridade", "residência"]),
        ("Factores clínicos",
         ["número de comorbilidades", "infecção por HIV e tuberculose",
          "função renal (depuração da creatinina)"]),
        ("Factores farmacoterapêuticos",
         ["número de medicamentos (polimedicação)",
          "anti-infecciosos e anti-retrovirais", "via parenteral"]),
        ("Factores do processo de cuidados",
         ["duração do internamento", "transferência entre serviços",
          "disponibilidade dos medicamentos"]),
    ],
    "desfecho": ("Problemas relacionados com medicamentos (PCNE V9.1)",
                 ["ocorrência (sim ou não)", "número por doente",
                  "problema e causa", "intervenção, aceitação e estado"]),
    "moderadores": ("Variáveis de confundimento",
                    ["gravidade clínica à admissão", "mês de inclusão"]),
}

# ----------------------------------------------------- 8. metodologia -------
METODOLOGIA = [
    ("Tipo e desenho do estudo", [
        P("Trata-se de um estudo observacional, prospectivo, de base "
          "hospitalar e abordagem quantitativa, com uma componente "
          "descritiva, correspondente aos objectivos específicos 1 a 4, e "
          "uma componente analítica, correspondente ao objectivo 5. Cada "
          "doente incluído é seguido diariamente desde a inclusão até à "
          "alta, ao óbito, à transferência ou ao trigésimo dia de "
          "internamento, o que configura uma coorte de internamento em que "
          "o desfecho principal é a ocorrência de pelo menos um PRM durante "
          "a estadia."),
        P("O desenho prospectivo foi preferido ao retrospectivo por três "
          "razões. Os processos em papel raramente registam de forma "
          "completa a administração e as alterações da prescrição, o que "
          "tornaria invisíveis as causas ligadas ao processo de uso; a "
          "revisão diária permite detectar problemas potenciais antes de "
          "causarem dano; e só a observação em tempo real permite propor "
          "intervenções e verificar a sua aceitação, condição para medir o "
          "contributo potencial do farmacêutico. O estudo não é um ensaio de "
          "intervenção: não tem grupo de comparação nem avalia o efeito das "
          "intervenções sobre desfechos clínicos. A comunicação dos PRM "
          "validados à equipa clínica decorre de um dever ético e "
          "profissional e é registada nos domínios de intervenção, "
          "aceitação e estado da classificação PCNE {pcne2020}. O relato "
          "seguirá a declaração STROBE (Strengthening the Reporting of "
          "Observational Studies in Epidemiology) {vonelm2007}."),
    ]),
    ("Local e período do estudo", [
        P("O estudo decorrerá na enfermaria de Medicina do HCN, na cidade "
          "de Nampula, hospital classificado como quaternário no Serviço "
          "Nacional de Saúde {xavier2024} e unidade de referência para as "
          "províncias de Nampula, Cabo Delgado e Niassa {belo2017}. A "
          "enfermaria recebe adultos com doenças médicas agudas e crónicas, "
          "provenientes da urgência, da consulta externa e de outras "
          "unidades sanitárias da região. A organização da enfermaria em "
          "secções, o número de camas e o número médio mensal de admissões "
          "serão confirmados antes do início do estudo [confirmar junto da "
          "Direcção Clínica e do serviço de estatística do HCN]."),
        P("O protocolo abrange o período de Outubro de 2026 a Setembro de "
          "2027. A inclusão de doentes decorrerá de 1 de Março a 30 de Junho "
          "de 2027, depois da aprovação ética e das autorizações "
          "institucionais e de um mês de preparação, calibração e pré-teste "
          "em Fevereiro de 2027. O seguimento dos últimos doentes incluídos "
          "prolonga-se, no máximo, até 30 de Julho de 2027, por efeito do "
          "limite de 30 dias de seguimento por doente."),
    ]),
    ("População e unidade de análise", [
        P("A população-alvo é constituída pelos adultos internados na "
          "enfermaria de Medicina do HCN; a população acessível, pelos que "
          "forem internados entre 1 de Março e 30 de Junho de 2027 e "
          "permanecerem pelo menos 48 horas na enfermaria. A unidade de "
          "análise é o doente, isto é, o episódio de internamento, para os "
          "objectivos 1, 2 e 5; o PRM validado para o objectivo 3; e a "
          "intervenção proposta para o objectivo 4."),
        P("Cada doente entra no estudo uma única vez. As readmissões do "
          "mesmo doente no período não são incluídas, e são identificadas "
          "pelo número do processo, registado apenas na lista de "
          "correspondência guardada separadamente das fichas. Se o doente "
          "for transferido para outro serviço, o seguimento termina na data "
          "da transferência e não é retomado se regressar à enfermaria. Os "
          "doentes-dia de seguimento, denominador da taxa de PRM, contam-se "
          "desde a inclusão até ao fim do seguimento, com o máximo de 30 "
          "dias por doente."),
    ]),
    ("Amostra e cálculo do tamanho da amostra", [
        P("O tamanho da amostra foi calculado para estimar a proporção de "
          "doentes com pelo menos um PRM, principal parâmetro descritivo, "
          "pela fórmula de uma proporção {wang2020}:"),
        FORMULA("n<sub>0</sub> = Z<sup>2</sup> × p × (1 - p) / "
                "d<sup>2</sup>"),
        P("Em que n<sub>0</sub> é o tamanho mínimo da amostra; Z é o valor "
          "da distribuição normal padrão para uma confiança de 95% (1,96); p "
          "é a proporção esperada de doentes com pelo menos um PRM, fixada "
          "em 0,694, valor agregado da meta-análise etíope de 17 estudos, a "
          "estimativa africana mais sólida disponível {ayele2021}; e d é a "
          "margem de erro absoluta admitida, de 0,05. Substituindo os "
          "valores:"),
        FORMULA("n<sub>0</sub> = 1,96<sup>2</sup> × 0,694 × 0,306 / "
                "0,05<sup>2</sup> = 3,8416 × 0,2124 / 0,0025 = 326,3"),
        P("Arredondando para 327 doentes e acrescentando 10% para compensar "
          "retiradas de consentimento, transferências precoces e fichas "
          "incompletas, obtém-se a amostra final de 364 doentes (327 / "
          "0,90 = 363,3). Não se aplica a correcção para população finita, "
          "porque a população acessível é um fluxo aberto de admissões e o "
          "seu número exacto só será conhecido no fim do período; a título "
          "ilustrativo, com 800 admissões elegíveis a correcção reduziria "
          "n<sub>0</sub> para 232 doentes, mas comprometeria o poder da "
          "componente analítica. O tamanho de 364 doentes é, por isso, uma "
          "opção conservadora."),
        P("Para o objectivo 5, verificou-se o poder para comparar a "
          "proporção de doentes com PRM entre os doentes com e sem "
          "polimedicação, pela fórmula de duas proporções com nível de "
          "significância de 5% bilateral e poder de 80% {wang2020}:"),
        FORMULA("n<sub>g</sub> = [Z<sub>α/2</sub> × √(2 × p<sub>m</sub> × "
                "(1 - p<sub>m</sub>)) + Z<sub>β</sub> × √(p<sub>1</sub> × "
                "(1 - p<sub>1</sub>) + p<sub>2</sub> × (1 - p<sub>2</sub>))]"
                "<sup>2</sup> / (p<sub>2</sub> - p<sub>1</sub>)<sup>2</sup>"),
        P("Admitindo, como diferença mínima com relevância clínica, 15 "
          "pontos percentuais em torno da proporção agregada de 69,4% "
          "(p<sub>1</sub> = 0,60 sem polimedicação e p<sub>2</sub> = 0,75 "
          "com polimedicação; p<sub>m</sub> = 0,675), com Z<sub>α/2</sub> = "
          "1,96 e Z<sub>β</sub> = 0,84, obtém-se n<sub>g</sub> = 152 "
          "doentes por grupo, ou 304 no total. Com os 327 doentes "
          "analisáveis, o poder é de 82,8% se os grupos forem iguais e de "
          "81,7% se a polimedicação atingir 60% dos doentes; se atingir "
          "70%, o poder desce para 76,9% e a diferença detectável sobe para "
          "16 pontos, limitação que será declarada."),
        P("Para a regressão logística, adopta-se a regra de pelo menos 10 "
          "eventos por parâmetro na categoria menos frequente do desfecho "
          "{peduzzi1996}. O modelo admite no máximo oito parâmetros, "
          "escolhidos entre a polimedicação, a idade e o mês de inclusão, "
          "fixados à partida, e as candidatas sexo, número de "
          "comorbilidades, infecção por HIV, função renal, sinais de "
          "gravidade à admissão e duração do internamento, o que exige 80 "
          "doentes sem PRM; com uma proporção esperada de 30,6% sem PRM, "
          "são necessários 262 doentes analisáveis (80 / 0,306). Os 327 "
          "doentes analisáveis fornecem cerca de 100 doentes sem PRM, isto "
          "é, 12,5 eventos por parâmetro, pelo que a amostra de 364 "
          "satisfaz os três requisitos."),
        P("A selecção dos doentes adapta-se ao fluxo de admissões, "
          "estimado a partir do registo de internamentos de Março a Junho "
          "de 2026 [confirmar junto do serviço de estatística do HCN]. A "
          "regra é a seguinte: calcula-se k, parte inteira da divisão do "
          "número previsto de admissões elegíveis em quatro meses por 364; "
          "se k for inferior a 2, incluem-se consecutivamente todos os "
          "doentes elegíveis até perfazer 364; se k for igual ou superior a "
          "2, aplica-se amostragem sistemática no livro de admissões da "
          "enfermaria, com início aleatório entre 1 e k, o que distribui a "
          "amostra pelos quatro meses e mantém a carga diária de seguimento "
          "compatível com a equipa. Quando um doente seleccionado não for "
          "elegível ou recusar, convida-se o doente elegível seguinte. A "
          "[[tabela:cenarios]] mostra a aplicação da regra a seis cenários "
          "de fluxo."),
        TABELA("cenarios",
               "Cenários de fluxo de admissões, estratégia de selecção e "
               "precisão esperada",
               ["Admissões elegíveis por mês", "Elegíveis em quatro meses",
                "Tempo para incluir 364", "Estratégia de selecção",
                "Doentes analisáveis e margem de erro"],
               [["60", "240", "6,1 meses",
                 "Todos os elegíveis durante os quatro meses",
                 "cerca de 216; ± 6,1 pontos"],
                ["90", "360", "4,0 meses", "Consecutiva, todos os elegíveis",
                 "cerca de 324; ± 5,0 pontos"],
                ["120", "480", "3,0 meses", "Consecutiva até 364",
                 "327; ± 5,0 pontos"],
                ["180", "720", "2,0 meses", "Consecutiva até 364",
                 "327; ± 5,0 pontos"],
                ["240", "960", "1,5 meses", "Sistemática, k = 2",
                 "327; ± 5,0 pontos"],
                ["360", "1.440", "1,0 mês", "Sistemática, k = 3",
                 "327; ± 5,0 pontos"]],
               larguras=[2.6, 2.6, 2.6, 4.2, 4.0],
               fonte="Elaboração própria (2026).",
               nota=("Margem de erro para p = 0,694 com intervalo de "
                     "confiança a 95% (IC 95%), após 10% de perdas. No "
                     "primeiro cenário, além de a precisão diminuir, o "
                     "número de doentes analisáveis fica abaixo dos 262 "
                     "exigidos pela regressão logística e dos 304 exigidos "
                     "pela comparação de duas proporções, pelo que a "
                     "componente analítica perde poder e o estudo passa a "
                     "ser sobretudo descritivo, o que será declarado.")),
    ]),
    ("Critérios de inclusão e de exclusão", [
        H3("Critérios de inclusão"),
        LISTA([
            "Idade igual ou superior a 18 anos.",
            "Internamento na enfermaria de Medicina do HCN entre 1 de Março "
            "e 30 de Junho de 2027, com permanência de pelo menos 48 horas.",
            "Pelo menos um medicamento prescrito durante o internamento.",
            "Consentimento livre e esclarecido do doente ou, quando este não "
            "tiver capacidade para decidir, do representante legal ou do "
            "familiar responsável, com confirmação pelo doente logo que "
            "recupere essa capacidade.",
        ]),
        H3("Critérios de exclusão"),
        LISTA([
            "Gravidez confirmada ou referida.",
            "Readmissão de um doente já incluído no período do estudo.",
            "Participação na fase de pré-teste.",
            "Processo clínico e folhas de prescrição indisponíveis para "
            "consulta durante mais de 48 horas consecutivas.",
            "Recusa de participação ou retirada do consentimento, caso em "
            "que os dados já recolhidos não serão analisados se o "
            "participante assim o pedir.",
        ]),
    ]),
    ("Variáveis e definições operacionais", [
        P("O [[quadro:variaveis]] apresenta as variáveis do estudo, o seu "
          "tipo, a definição operacional com as respectivas categorias e o "
          "objectivo específico a que respondem. A variável dependente do "
          "objectivo 5 é a ocorrência de pelo menos um PRM validado durante "
          "o seguimento; as variáveis de classificação seguem os códigos da "
          "versão 9.1 da PCNE {pcne2020}, e o impacto clínico potencial "
          "segue a dimensão clínica da ferramenta CLEO {vo2021}."),
        QUADRO("variaveis", "Variáveis do estudo e definições operacionais",
               ["Variável", "Tipo", "Definição operacional e categorias",
                "Objectivo"],
               [["Idade", "Independente, quantitativa",
                 "Anos completos; categorias 18-39, 40-59 e 60 ou mais",
                 "1, 5"],
                ["Sexo", "Independente, nominal", "Masculino; feminino",
                 "1, 5"],
                ["Escolaridade", "Descritiva, ordinal",
                 "Nenhuma; primária; secundária; superior", "1"],
                ["Residência", "Descritiva, nominal",
                 "Cidade de Nampula; outro distrito de Nampula; outra "
                 "província", "1"],
                ["Grupo diagnóstico principal", "Descritiva, nominal",
                 "Infeccioso; cardiovascular; renal; metabólico; "
                 "respiratório; neurológico; outro", "1"],
                ["Número de comorbilidades", "Independente, quantitativa",
                 "Doenças registadas além do diagnóstico principal; 0-1 e 2 "
                 "ou mais", "1, 5"],
                ["Infecção por HIV", "Independente, nominal",
                 "Positiva com tratamento anti-retroviral; positiva sem "
                 "tratamento; negativa; desconhecida", "1, 5"],
                ["Função renal", "Independente, ordinal",
                 "Depuração da creatinina (Cockcroft-Gault): 60 ou mais; "
                 "30-59; menos de 30 mL/min; não avaliável", "1, 5"],
                ["Sinais de gravidade à admissão", "Confundimento, nominal",
                 "Pelo menos um de: alteração da consciência, pressão "
                 "arterial sistólica inferior a 90 mmHg, necessidade de "
                 "oxigénio; sim ou não", "1, 5"],
                ["Polimedicação", "Independente, nominal",
                 "Cinco ou mais medicamentos prescritos em simultâneo em "
                 "pelo menos um dia; sim ou não (registo também do número "
                 "máximo diário)", "1, 5"],
                ["Duração do internamento", "Independente, quantitativa",
                 "Dias desde a admissão até ao fim do seguimento; até 7 e "
                 "mais de 7 dias", "1, 5"],
                ["Mês de inclusão", "Confundimento, ordinal",
                 "Março; Abril; Maio; Junho", "5"],
                ["Ocorrência de PRM", "Dependente, nominal",
                 "Pelo menos um PRM validado durante o seguimento; sim ou "
                 "não", "2, 5"],
                ["Número de PRM e taxa", "Dependente, quantitativa",
                 "PRM validados por doente; PRM por 100 doentes-dia", "2"],
                ["Problema (domínio P)", "Descritiva, nominal",
                 "P1 efectividade; P2 segurança; P3 outros; subdomínios da "
                 "versão 9.1", "3"],
                ["Causa (domínio C)", "Descritiva, nominal",
                 "C1 a C9 e subdomínios da versão 9.1; mais de uma causa "
                 "por PRM quando aplicável", "3"],
                ["Natureza do PRM", "Descritiva, nominal",
                 "Potencial; manifesto", "3"],
                ["Medicamento envolvido", "Descritiva, nominal",
                 "Denominação comum internacional; grupo ATC de nível 1 e 2",
                 "3"],
                ["Intervenção planeada (domínio I)", "Descritiva, nominal",
                 "I0 a I4 e subdomínios", "4"],
                ["Aceitação (domínio A)", "Descritiva, nominal",
                 "A1 aceite; A2 não aceite; A3 outra situação", "4"],
                ["Estado do PRM (domínio O)", "Descritiva, nominal",
                 "O0 desconhecido; O1 resolvido; O2 parcialmente "
                 "resolvido; O3 não resolvido", "4"],
                ["Impacto clínico potencial (CLEO)", "Descritiva, ordinal",
                 "-1 prejudicial; 0 nulo; 1 menor; 2 moderado; 3 "
                 "importante; 4 evita consequência fatal", "4"],
                ],
               larguras=[3.4, 2.9, 7.7, 2.0]),
        P("Os critérios usados para reconhecer cada tipo de PRM estão "
          "definidos no [[quadro:definicoes_prm]], que liga os tipos "
          "enunciados no tema aos códigos da PCNE e às fontes de referência. "
          "Estes critérios foram escritos para reduzir o peso do julgamento "
          "individual; as situações não previstas serão decididas por "
          "consenso e acrescentadas ao quadro, com registo da data da "
          "alteração."),
        QUADRO("definicoes_prm",
               "Critérios operacionais de identificação dos PRM e "
               "correspondência com a classificação da PCNE, versão 9.1",
               ["Tipo de PRM", "Códigos PCNE", "Critério operacional",
                "Fonte de referência"],
               [["Dose demasiado baixa", "P1.2; C3.1",
                 "Dose ou frequência inferior à recomendada para a "
                 "indicação, o peso ou a idade", "FNM; normas do MISAU"],
                ["Dose demasiado alta ou sem ajuste renal", "P2.1; C3.2 ou "
                 "C3.4", "Dose acima da máxima recomendada ou não ajustada a "
                 "depuração da creatinina inferior a 60 mL/min quando o "
                 "ajuste é exigido", "FNM; equação de Cockcroft-Gault"],
                ["Duplicação terapêutica", "P2.1 ou P3.1; C1.4",
                 "Dois medicamentos do mesmo grupo ATC de nível 4 ou com a "
                 "mesma substância activa, em simultâneo, sem justificação "
                 "registada", "Classificação ATC"],
                ["Interacção clinicamente relevante", "P2.1 ou P1.2; C1.3",
                 "Combinação contra-indicada ou grave com recomendação de "
                 "alternativa, ou que exija evitar a co-administração ou "
                 "ajustar a dose, sem ajuste registado",
                 "Base da Universidade de Liverpool; Medscape"],
                ["Monitorização em falta", "P2.1 ou P1.2; C9.1",
                 "Interacção ou medicamento que exige vigilância "
                 "laboratorial ou clínica sem esse registo no processo",
                 "Medscape; FNM"],
                ["Indicação não tratada", "P1.3; C1.5",
                 "Condição registada com indicação terapêutica segundo as "
                 "normas nacionais sem tratamento prescrito",
                 "Normas do MISAU; LNME"],
                ["Medicamento sem indicação", "P3.1; C1.2",
                 "Medicamento sem diagnóstico, sintoma ou objectivo "
                 "registado que o justifique", "Processo clínico"],
                ["Duração inadequada", "P1.2 ou P3.1; C4.1 ou C4.2",
                 "Duração inferior ou superior à recomendada, sem "
                 "reavaliação registada", "FNM; normas do MISAU"],
                ["Falha de administração", "P1.2; C6.1 a C6.6",
                 "Diferença entre a prescrição e a folha de administração "
                 "(dose omitida, dose a mais, horário, via ou medicamento "
                 "errado)", "Folhas de prescrição e de administração"],
                ["Medicamento indisponível", "P1.2 ou P1.3; C5.1",
                 "Medicamento prescrito não administrado por falta na "
                 "farmácia", "Folha de administração; farmácia"],
                ["Omissão de medicamento habitual", "P1.3; C8.1",
                 "Medicamento crónico referido na entrevista, sem registo "
                 "de suspensão intencional, não prescrito no internamento",
                 "Entrevista ao doente ou acompanhante"],
                ["Reacção adversa", "P2.1 manifesto",
                 "Reacção com causalidade possível, provável ou definida na "
                 "escala de Naranjo", "Escala de Naranjo"],
                ],
               larguras=[3.2, 2.6, 6.6, 3.6],
               fonte=("Elaboração própria (2026), a partir da classificação "
                      "da PCNE, versão 9.1 {pcne2020}."),
               nota=("A duplicação e a interacção entre medicamentos de uso "
                     "concomitante justificado, com monitorização "
                     "registada, não são consideradas PRM.")),
    ]),
    ("Instrumentos de recolha de dados e fontes de referência", [
        P("A recolha usará uma ficha de seguimento farmacoterapêutico e de "
          "registo de PRM (Apêndice A), construída pelos investigadores a "
          "partir da classificação básica e do documento de apoio da versão "
          "9.1 da PCNE {pcne2020}. A ficha tem sete secções: identificação "
          "codificada e inclusão; dados sociodemográficos; dados clínicos "
          "à admissão; história medicamentosa anterior ao internamento; "
          "registo diário da farmacoterapia; registo de cada PRM; e fim do "
          "seguimento. Os códigos da PCNE são reproduzidos sem alteração, com "
          "tradução portuguesa dos rótulos; a escala de Naranjo é "
          "reproduzida em tradução portuguesa, sem alteração dos itens nem "
          "da pontuação {naranjo1981}; e os níveis de impacto clínico são "
          "os da dimensão clínica da ferramenta CLEO {vo2021}."),
        P("A validade de conteúdo da ficha será apreciada por um painel de "
          "cinco peritos (dois farmacêuticos hospitalares, um médico "
          "internista, um docente de farmácia clínica e um epidemiologista), "
          "que classificarão a relevância de cada item numa escala de quatro "
          "pontos; os itens com índice de validade de conteúdo inferior a "
          "0,80 serão revistos ou retirados. A folha de informação e o termo "
          "de consentimento serão traduzidos para Emakhuwa e retrovertidos "
          "para português por um segundo tradutor independente, e as "
          "divergências serão resolvidas antes do pré-teste."),
        P("As fontes de referência para apreciar cada caso são, por ordem: "
          "a edição em vigor do FNM e a LNME de 2017 {mboane2025,misau2017}; "
          "as normas clínicas nacionais do MISAU em vigor para o HIV, a "
          "tuberculose e as restantes doenças prevalentes, obtidas junto da "
          "Direcção Clínica do HCN; a base de interacções da Universidade "
          "de Liverpool para os anti-retrovirais {liverpool2026} e o "
          "verificador de interacções da Medscape para as restantes "
          "combinações {medscape2026}; a equação de Cockcroft-Gault para a "
          "função renal {cockcroft1976}; e o índice ATC da OMS para o "
          "agrupamento dos medicamentos {whocc2026}. Quando as fontes "
          "divergirem, prevalece a norma nacional e, na sua falta, a "
          "classificação mais grave, decisão que será registada."),
    ]),
    ("Procedimentos de recolha de dados e controlo de qualidade", [
        H3("Equipa, formação e calibração"),
        P("A equipa é formada pelo investigador principal, estudante "
          "finalista de Farmácia e primeiro avaliador; por um farmacêutico "
          "hospitalar do HCN ou docente farmacêutico da FCS, segundo "
          "avaliador, designado com o orientador; por um médico internista "
          "do Serviço de Medicina, terceiro avaliador, que decide os "
          "desacordos persistentes; e por um assistente de recolha, "
          "finalista de Farmácia, que transcreve os dados sociodemográficos "
          "e o registo diário da medicação. Em Fevereiro de 2027, a equipa "
          "receberá 16 horas de formação sobre a classificação PCNE, os "
          "critérios do [[quadro:definicoes_prm]], as fontes de referência, "
          "a escala de Naranjo, a ferramenta CLEO e as regras de "
          "confidencialidade, com exercícios em 20 casos fictícios "
          "preparados pela equipa."),
        H3("Verificação prévia da fonte e pré-teste"),
        P("Na primeira semana de Fevereiro de 2027, serão examinados 30 "
          "processos de doentes internados, sem extracção de dados "
          "pessoais, para medir o preenchimento do peso, da creatinina "
          "sérica, do diagnóstico, das alergias e da folha de "
          "administração. A regra de decisão é escrita antes do exame: a "
          "variável com menos de 60% de preenchimento sai da componente "
          "analítica e passa a ser apenas descrita; se isso suceder com a "
          "creatinina, a função renal sai do modelo de regressão e os PRM "
          "de ajuste renal são relatados apenas para os doentes com "
          "creatinina disponível. Segue-se o pré-teste em 36 doentes "
          "consentidos (cerca de 10% da amostra), excluídos da amostra "
          "final, revistos de forma independente pelos dois avaliadores; "
          "se o kappa para a detecção de PRM ou para os domínios primários "
          "de problemas e causas for inferior a 0,60 {mchugh2012}, a "
          "formação é repetida e realiza-se nova ronda em 15 doentes."),
        H3("Inclusão e seguimento diário"),
        P("De segunda-feira a sábado, o assistente consulta o livro de "
          "admissões da enfermaria e lista os novos internamentos; às 48 "
          "horas, o investigador verifica os critérios, aplica a regra de "
          "selecção e obtém o consentimento. Na inclusão, preenchem-se as "
          "secções I a IV da ficha, incluindo uma entrevista breve, de "
          "cerca de dez minutos, ao doente ou ao acompanhante sobre os "
          "medicamentos habituais e o uso de medicamentos tradicionais. "
          "Diariamente, depois da visita médica, revêem-se a folha de "
          "prescrição, a folha de administração, as notas clínicas e os "
          "resultados laboratoriais, e registam-se todos os medicamentos e "
          "alterações; a revisão de segunda-feira abrange os registos de "
          "domingo. Cada PRM identificado é descrito na secção VI."),
        H3("Validação, comunicação e registo das intervenções"),
        P("Cada PRM identificado pelo primeiro avaliador é resumido num caso "
          "anónimo e codificado de forma independente pelo segundo "
          "avaliador no próprio dia ou nas 24 horas seguintes, sem acesso aos "
          "códigos atribuídos pelo primeiro (problema, causa e nível de "
          "impacto clínico). Os desacordos são discutidos e, se persistirem, "
          "decididos pelo terceiro avaliador. O PRM validado é comunicado ao "
          "médico responsável pelo doente, verbalmente na visita seguinte e "
          "por escrito na nota de intervenção farmacêutica (Apêndice D), "
          "pelo segundo avaliador ou pelo investigador na sua presença. A "
          "nota é uma proposta e a decisão pertence ao prescritor, como "
          "determina a Lei n.º 12/2017 {lei12_2017}. Quando o impacto "
          "clínico potencial for importante ou fatal (níveis 3 ou 4), a "
          "comunicação ao médico de serviço é imediata, sem esperar pela "
          "validação."),
        P("A aceitação é verificada na folha de prescrição nas 48 horas "
          "seguintes e codificada no domínio A; o estado do problema é "
          "codificado no domínio O no fim do seguimento {pcne2020}. As "
          "suspeitas de reacção adversa com causalidade possível ou "
          "superior na escala de Naranjo são notificadas ao Sistema Nacional "
          "de Farmacovigilância através do responsável de farmacovigilância "
          "do hospital [confirmar a designação junto da Direcção de "
          "Farmácia do HCN], e a notificação é registada na ficha como "
          "intervenção de comunicação da reacção adversa à autoridade "
          "(domínio I4) {lei12_2017,anarme2024}."),
        H3("Concordância na detecção e controlo de qualidade"),
        P("Para medir a concordância na detecção, 20% dos doentes incluídos "
          "(cerca de 73) serão sorteados antes do início, por lista de "
          "números aleatórios associada à ordem de inclusão, e terão o "
          "processo revisto na íntegra, no mesmo dia, pelo segundo "
          "avaliador, sem acesso às notas do primeiro; os PRM encontrados "
          "por qualquer dos dois seguem para validação conjunta. O "
          "investigador confere diariamente o preenchimento das fichas, o "
          "orientador reúne semanalmente com a equipa, e 10% das fichas, "
          "sorteadas, serão digitadas duas vezes; uma taxa de discrepância "
          "superior a 1% obriga à revisão de todas as fichas. As fichas "
          "usam apenas o código do doente."),
    ]),
    ("Processamento e análise dos dados", [
        P("Os dados serão introduzidos numa base com regras de validação "
          "(intervalos admissíveis e campos obrigatórios) e analisados no "
          "programa Statistical Package for the Social Sciences (SPSS), "
          "versão 26 ou superior, ou no programa R, de acesso livre, com "
          "nível de significância de 5% (p<0,05) e intervalos de confiança "
          "a 95% (IC 95%). As variáveis categóricas serão descritas por "
          "frequências e proporções com IC 95%, e as quantitativas por média "
          "e desvio-padrão ou por mediana e intervalo interquartil, conforme "
          "a normalidade avaliada pelo teste de Shapiro-Wilk (objectivo 1)."),
        P("Para o objectivo 2, calculam-se a proporção de doentes com pelo "
          "menos um PRM, com IC 95%, a média e a mediana de PRM por doente e "
          "a taxa de PRM por 100 doentes-dia, com IC 95% baseado na "
          "distribuição de Poisson. Para o objectivo 3, descrevem-se as "
          "frequências dos domínios e subdomínios de problemas e de causas, "
          "a proporção de problemas potenciais e manifestos e os "
          "medicamentos e grupos ATC mais envolvidos, também expressos por "
          "100 medicamentos prescritos. Para o objectivo 4, descrevem-se as "
          "intervenções por domínio, a taxa de aceitação, calculada sobre "
          "as intervenções com resposta conhecida (A1 sobre A1 e A2), o "
          "estado final dos PRM e a distribuição do impacto clínico "
          "potencial."),
        P("A concordância entre avaliadores será medida pelo kappa de Cohen, "
          "com IC 95%, para a detecção de PRM por doente e para os "
          "domínios primários de problemas e causas, e pelo kappa ponderado "
          "para o nível de impacto clínico, que é ordinal {li2023}; "
          "valores inferiores a 0,60 serão relatados como concordância "
          "inadequada {mchugh2012}."),
        P("Para o objectivo 5, a associação entre cada factor e a ocorrência "
          "de PRM será testada pelo qui-quadrado de Pearson, ou pelo teste "
          "exacto de Fisher quando alguma frequência esperada for inferior "
          "a 5, com OR bruto e IC 95%. Entram no modelo de regressão "
          "logística múltipla a polimedicação e a idade, fixadas *a "
          "priori*, "
          "o mês de inclusão, para controlar a aprendizagem da equipa, e as "
          "restantes variáveis candidatas com p<0,20 na análise bivariada, "
          "sem ultrapassar oito parâmetros {peduzzi1996}. Verificam-se a "
          "colinearidade (factor de inflação da variância inferior a 5), o "
          "ajustamento (teste de Hosmer-Lemeshow) e a discriminação (área "
          "sob a curva característica de operação do receptor), e "
          "apresentam-se os OR ajustados com IC 95%."),
        P("Serão feitas duas análises de sensibilidade: o modelo sem a "
          "duração do internamento, que pode ser consequência e não apenas "
          "causa dos PRM, e o modelo por regressão de Poisson com variância "
          "robusta, que estima razões de prevalência, mais adequadas a um "
          "desfecho frequente. A tendência mensal da proporção de doentes "
          "com PRM será testada pelo qui-quadrado de tendência. Os dados em "
          "falta serão descritos por variável e a análise principal usará "
          "os casos completos."),
    ]),
    ("Limitações do estudo e estratégias de mitigação", [
        P("O [[quadro:limitacoes]] resume as limitações previstas, as suas "
          "consequências para a validade dos resultados e as estratégias "
          "adoptadas para as reduzir."),
        QUADRO("limitacoes", "Limitações previstas e estratégias de mitigação",
               ["Limitação", "Consequência", "Mitigação"],
               [["Estudo num único hospital e numa só enfermaria",
                 "Generalização limitada a outros hospitais",
                 "Descrição detalhada do contexto; comparação com estudos "
                 "africanos que usam a PCNE; relato segundo a declaração "
                 "STROBE"],
                ["Processos em papel incompletos (peso, creatinina, "
                 "administração)",
                 "Subestimação dos PRM de dose, de ajuste renal e de "
                 "administração",
                 "Verificação prévia da fonte; categoria «não avaliável»; "
                 "regra dos 60% de preenchimento"],
                ["Comunicação dos PRM altera a prescrição posterior",
                 "Diminuição da frequência de PRM nos últimos meses",
                 "Registo no momento da identificação; mês de inclusão no "
                 "modelo; teste de tendência"],
                ["Identificação e classificação dependentes de julgamento",
                 "Classificação errada e baixa reprodutibilidade",
                 "Critérios operacionais escritos; dois avaliadores "
                 "independentes; kappa; terceiro avaliador"],
                ["Discordância entre bases de interacções",
                 "Sobrestimação ou subestimação das interacções",
                 "Regras explícitas de gravidade; fonte específica para "
                 "anti-retrovirais; registo das divergências"],
                ["Distribuição desigual da polimedicação",
                 "Menor poder para a comparação principal",
                 "Cálculo do poder em cenários; relato dos IC 95% e da "
                 "diferença detectável"],
                ["Duração do internamento como causa e consequência",
                 "OR enviesado para esta variável",
                 "Análise de sensibilidade sem a variável; interpretação "
                 "como associação"],
                ["Exclusão de doentes graves sem representante",
                 "Viés de selecção para doentes menos graves",
                 "Consentimento por representante; comparação da idade, "
                 "sexo e diagnóstico com os não incluídos do livro de "
                 "admissões"],
                ["Revisão de segunda-feira a sábado",
                 "Perda de problemas transitórios ao domingo",
                 "Revisão à segunda-feira dos registos de domingo; "
                 "comunicação imediata dos casos graves"],
                ],
               larguras=[4.8, 4.6, 6.6]),
    ]),
    ("Considerações éticas", [
        P("O protocolo será submetido ao Comité Institucional de Bioética "
          "para a Saúde da Universidade Lúrio (CIBS-UniLúrio) e, quando "
          "aplicável, ao Comité Nacional de Bioética para a Saúde (CNBS), e "
          "a recolha só começará depois do parecer favorável e das "
          "autorizações da Direcção Provincial de Saúde (DPS) de Nampula e "
          "da Direcção-Geral do HCN. O estudo respeita a Declaração de "
          "Helsínquia na revisão de 2024 {wma2025} e a Lei n.º 3/2023, de "
          "Investigação em Saúde Humana {lei3_2023}. Os princípios "
          "aplicados são os seguintes:"),
        LISTA([
            "Consentimento: participação voluntária, com folha de informação "
            "e termo de consentimento em português e Emakhuwa (Apêndices B e "
            "C); quem não souber ler assina por impressão digital na "
            "presença de uma testemunha imparcial; para doentes sem "
            "capacidade de decisão, consente o representante legal ou o "
            "familiar responsável, e o doente confirma quando recuperar a "
            "capacidade.",
            "Dispensa de consentimento limitada à verificação prévia de 30 "
            "processos, que regista apenas o preenchimento de campos, sem "
            "dados pessoais, e que será pedida expressamente ao comité.",
            "Confidencialidade: fichas identificadas apenas por código; "
            "lista de correspondência guardada em armário fechado, separada "
            "das fichas e destruída no fim do estudo; base de dados "
            "protegida por palavra-passe; nomes de doentes, médicos e "
            "enfermeiros nunca registados nas fichas nem nos relatórios.",
            "Riscos e benefícios: risco mínimo, limitado ao tempo da "
            "entrevista e à possível quebra de confidencialidade, que as "
            "medidas acima previnem; benefício directo pela comunicação dos "
            "PRM validados à equipa clínica durante o internamento.",
            "Via de referenciação: qualquer PRM com impacto clínico "
            "potencial importante ou fatal é comunicado de imediato ao "
            "médico de serviço, e as suspeitas de reacção adversa são "
            "notificadas ao Sistema Nacional de Farmacovigilância "
            "{anarme2024}.",
            "Carácter não punitivo: os resultados são apresentados de forma "
            "agregada, sem identificar profissionais ou turnos, e servem "
            "para melhorar processos e não para avaliar desempenhos "
            "individuais.",
            "Ausência de custos e de compensação: a participação não tem "
            "custos nem pagamento, e a recusa ou a retirada não afecta os "
            "cuidados prestados.",
        ]),
    ]),
]

# ----------------------------------------------------- 9 e 10 ---------------
RESULTADOS_ESPERADOS = [
    P("Os resultados esperados correspondem, pela mesma ordem, aos "
      "objectivos específicos. A direcção indicada apoia-se na literatura "
      "citada e não antecipa valores do estudo."),
    LISTA([
        "Objectivo 1: descrição de uma população adulta com peso elevado de "
        "HIV, tuberculose e doenças cardiovasculares e com polimedicação "
        "frequente {gudo2025,jessen2018}, que servirá ao HCN para planear a "
        "revisão da medicação por grupos de doentes.",
        "Objectivo 2: proporção de doentes com PRM previsivelmente próxima "
        "dos dois terços descritos noutras enfermarias africanas "
        "{ayele2021,bekele2021a}, com a respectiva precisão, e taxa por 100 "
        "doentes-dia, primeiro indicador local de segurança da "
        "farmacoterapia.",
        "Objectivo 3: predomínio esperado de causas ligadas à selecção do "
        "medicamento e da dose e de antibióticos entre os medicamentos "
        "envolvidos {abunahlah2018,bekele2021a,kyomya2023}, informação que "
        "orienta a formação dos prescritores e as prioridades da comissão "
        "de medicamentos do hospital.",
        "Objectivo 4: taxa de aceitação das intervenções previsivelmente "
        "elevada, como nos hospitais etíopes e ganenses "
        "{amankwa2022,dagnew2022,endalifer2025}, e perfil do impacto "
        "clínico potencial, que fundamentam a integração do farmacêutico na "
        "visita médica.",
        "Objectivo 5: associação esperada da polimedicação, das "
        "comorbilidades e da duração do internamento com a ocorrência de "
        "PRM {bekele2021a,dagnew2022,sefera2022}, que permitirá definir "
        "critérios para priorizar os doentes a rever quando o número de "
        "farmacêuticos for limitado.",
    ]),
]
DIVULGACAO = [
    P("Os resultados serão apresentados na defesa pública do trabalho de "
      "fim de curso na FCS e num relatório escrito, com síntese executiva, "
      "entregue à Direcção-Geral, à Direcção Clínica, ao Serviço de "
      "Medicina e à Direcção de Farmácia do HCN, à DPS de Nampula e à "
      "ANARME. No HCN será realizada uma sessão de devolução à equipa da "
      "enfermaria, com os resultados agregados e as propostas de melhoria. "
      "Prevê-se ainda a submissão de um artigo a uma revista com revisão "
      "por pares e a apresentação em jornadas científicas da Universidade "
      "Lúrio e do sector da saúde, seguindo a declaração STROBE "
      "{vonelm2007}."),
]

# ----------------------------------------------------- 11. cronograma -------
CRONOGRAMA_TEXTO = [
    P("O [[quadro:cronograma]] distribui as actividades pelos doze meses do "
      "estudo, de Outubro de 2026 a Setembro de 2027. A inclusão de doentes "
      "só começa em Março de 2027, depois da aprovação ética e da "
      "preparação de Fevereiro; se a aprovação se atrasar, todas as "
      "actividades seguintes deslocam-se pelo mesmo número de meses."),
]
CRONOGRAMA = {
    "inicio": (2026, 10),
    "n_meses": 12,
    "actividades": [
        ("Revisão da literatura e redacção do protocolo", [1, 2]),
        ("Submissão ao CIBS-UniLúrio e pedidos de autorização (DPS e HCN)",
         [3, 4]),
        ("Validação de conteúdo da ficha e tradução para Emakhuwa", [3, 4]),
        ("Formação, calibração, verificação da fonte e pré-teste", [5]),
        ("Inclusão de doentes e seguimento diário", [6, 7, 8, 9]),
        ("Seguimento dos últimos doentes incluídos", [10]),
        ("Validação das fichas, dupla digitação e limpeza da base",
         [6, 7, 8, 9, 10]),
        ("Processamento e análise estatística", [10, 11]),
        ("Redacção do relatório final", [10, 11]),
        ("Revisão pelo orientador e entrega", [11, 12]),
        ("Defesa pública", [12]),
        ("Devolução dos resultados ao HCN e relatório às instituições", [12]),
    ],
}

# ----------------------------------------------------- 12. orcamento --------
ORCAMENTO_TEXTO = [
    P("A [[tabela:orcamento]] apresenta o orçamento estimado, em meticais, "
      "para os 400 doentes previstos (364 da amostra e 36 do pré-teste). O "
      "estudo será financiado com recursos próprios do estudante, "
      "complementados por apoio a solicitar à Universidade Lúrio. As "
      "rubricas maiores são a alimentação e o transporte nos cerca de 130 "
      "dias de presença no hospital, impostos pelo seguimento diário, o "
      "subsídio ao assistente de recolha durante os quatro meses de "
      "inclusão e a impressão das fichas e dos documentos de consentimento "
      "em duas línguas. Os programas estatísticos não têm custo, porque se "
      "usará a licença institucional ou o programa R."),
]
ORCAMENTO = [
    ("Impressão da ficha de seguimento (6 páginas por doente)", "página",
     2400, 5),
    ("Impressão da folha de informação e do termo de consentimento, "
     "em duas vias e duas línguas", "página", 2400, 5),
    ("Impressão das notas de intervenção farmacêutica (duplicado)",
     "página", 1000, 5),
    ("Tradução e retroversão para Emakhuwa", "serviço", 1, 6000),
    ("Material de escritório (pastas, esferográficas, blocos)", "conjunto",
     1, 3500),
    ("Armário com fechadura para as fichas", "unidade", 1, 4500),
    ("Disco externo encriptado para a base de dados", "unidade", 1, 3000),
    ("Transporte urbano do investigador (ida e volta)", "dia", 130, 60),
    ("Transporte urbano do assistente de recolha (ida e volta)", "dia", 105,
     60),
    ("Subsídio ao assistente de recolha", "mês", 4, 4000),
    ("Alimentação nos dias de recolha (investigador e assistente)",
     "refeição", 235, 100),
    ("Formação e calibração da equipa (lanche e materiais)", "sessão", 2,
     2500),
    ("Reunião do painel de peritos (validade de conteúdo)", "sessão", 1,
     2500),
    ("Comunicações (telemóvel e internet)", "mês", 10, 500),
    ("Impressão e encadernação do relatório final", "exemplar", 4, 1200),
    ("Sessão de devolução dos resultados no HCN", "sessão", 1, 5000),
    ("Cartaz para jornada científica", "unidade", 1, 3000),
]
ORCAMENTO_IMPREVISTOS = 0.10

# ----------------------------------------------------- apendices ------------
_LINHAS_VAZIAS = [["", "", "", "", "", "", ""] for _ in range(6)]

APENDICES = [
    ("Ficha de seguimento farmacoterapêutico e de registo de PRM", [
        NOTA("Instruções: preencher a esferográfica, sem nomes nem números "
             "de processo; usar apenas o código do doente. Fontes: processo "
             "clínico, folha de prescrição, folha de administração, "
             "resultados laboratoriais e entrevista ao doente ou ao "
             "acompanhante. Os códigos da secção VI são os da classificação "
             "PCNE V9.1, com rótulos traduzidos para português; a escala de "
             "Naranjo é reproduzida em tradução portuguesa, sem alteração dos "
             "itens nem da pontuação; os níveis de impacto clínico são os da "
             "dimensão clínica da ferramenta CLEO."),
        H3("Secção I. Identificação codificada e inclusão"),
        CAMPO("Código do doente: ____________   Data de admissão: ___/___/"
              "______   Data de inclusão: ___/___/______"),
        CAMPO("Secção da enfermaria: ______________   Cama: ______"),
        PERG("Forma de selecção:", ["Consecutiva",
                                    "Sistemática (k = ____)"]),
        PERG("Doente sorteado para dupla revisão integral:", ["Sim", "Não"]),
        PERG("Consentimento dado por:", ["Próprio doente",
                                         "Representante legal ou familiar"]),
        H3("Secção II. Dados sociodemográficos"),
        PERG("Sexo:", ["Masculino", "Feminino"]),
        PERG("Idade em anos completos:"),
        PERG("Escolaridade:", ["Nenhuma", "Primária", "Secundária",
                               "Superior"]),
        PERG("Residência:", ["Cidade de Nampula",
                             "Outro distrito da província de Nampula",
                             "Outra província"]),
        PERG("Proveniência:", ["Urgência", "Consulta externa",
                               "Outra unidade sanitária",
                               "Outro serviço do HCN"]),
        H3("Secção III. Dados clínicos à admissão"),
        PERG("Diagnóstico principal, transcrito do processo:"),
        PERG("Grupo diagnóstico principal:",
             ["Infeccioso", "Cardiovascular", "Renal", "Metabólico",
              "Respiratório", "Neurológico", "Outro"]),
        PERG("Comorbilidades registadas (assinalar todas):",
             ["HIV", "Tuberculose activa", "Hipertensão arterial",
              "Diabetes mellitus", "Insuficiência cardíaca",
              "Doença renal crónica", "Doença hepática crónica",
              "Outra: ____________"]),
        PERG("Estado de HIV:", ["Positivo com tratamento anti-retroviral",
                                "Positivo sem tratamento", "Negativo",
                                "Desconhecido"]),
        PERG("Sinais de gravidade à admissão (assinalar todos):",
             ["Alteração da consciência",
              "Pressão arterial sistólica inferior a 90 mmHg",
              "Necessidade de oxigénio", "Nenhum"]),
        CAMPO("Peso: ______ kg   Fonte: (   ) processo   (   ) referido   "
              "(   ) não disponível"),
        CAMPO("Creatinina sérica: ______ (mg/dL ou µmol/L)   Data: ___/___/"
              "______   Depuração estimada (Cockcroft-Gault): ______ mL/min"),
        PERG("Categoria da função renal:", ["60 ou mais", "30-59",
                                            "Menos de 30", "Não avaliável"]),
        PERG("Alergias a medicamentos:", ["Sim, a: ____________", "Não",
                                          "Desconhecido"]),
        H3("Secção IV. História medicamentosa anterior ao internamento"),
        NOTA("Entrevista breve ao doente ou ao acompanhante, com cerca de "
             "dez minutos, no dia da inclusão."),
        PERG("Tomava medicamentos de forma regular antes do internamento?",
             ["Sim", "Não", "Não sabe"]),
        TABELA(None, "", ["Medicamento habitual", "Dose e frequência",
                          "Continuado no internamento (S/N)"],
               [["", "", ""] for _ in range(4)],
               larguras=[7.0, 5.0, 4.0]),
        PERG("Usou medicamentos tradicionais ou plantas nas duas semanas "
             "anteriores ao internamento?", ["Sim", "Não", "Não sabe"]),
        PERG("Está a tomar no hospital medicamentos trazidos de casa?",
             ["Sim", "Não"]),
        H3("Secção V. Registo diário da farmacoterapia"),
        NOTA("Uma linha por medicamento e por alteração. Na última coluna: "
             "S (administrado conforme prescrito), N (não administrado) ou P "
             "(administração parcial ou fora do horário)."),
        TABELA(None, "", ["Data", "Medicamento (denominação comum "
                          "internacional)", "Dose", "Via", "Frequência",
                          "Início e fim", "Administração"],
               _LINHAS_VAZIAS,
               larguras=[1.8, 4.6, 1.8, 1.4, 2.2, 2.2, 2.0]),
        CAMPO("Número de medicamentos prescritos neste dia: ______"),
        H3("Secção VI. Registo de cada PRM (uma folha por problema)"),
        CAMPO("PRM n.º ______   Data de identificação: ___/___/______   Dia de "
              "internamento: ______"),
        PERG("Medicamento ou medicamentos envolvidos e grupo ATC:"),
        PERG("Descrição objectiva do problema e da fonte consultada:"),
        PERG("Natureza do problema:", ["Potencial", "Manifesto"]),
        PERG("Problema (assinalar um):",
             ["P1.1 Sem efeito do tratamento apesar do uso correcto",
              "P1.2 Efeito do tratamento não óptimo",
              "P1.3 Sintomas ou indicação não tratados",
              "P2.1 Acontecimento adverso (possivelmente) a ocorrer",
              "P3.1 Tratamento medicamentoso desnecessário",
              "P3.2 Problema pouco claro, a esclarecer"]),
        PERG("Causa ou causas (assinalar todas as aplicáveis):",
             ["C1.1 Medicamento inadequado segundo as normas ou o formulário",
              "C1.2 Medicamento sem indicação",
              "C1.3 Combinação inadequada de medicamentos, ou com plantas "
              "ou suplementos",
              "C1.4 Duplicação inadequada de grupo terapêutico ou de "
              "substância activa",
              "C1.5 Tratamento ausente ou incompleto apesar da indicação",
              "C1.6 Demasiados medicamentos para a mesma indicação",
              "C2.1 Forma farmacêutica inadequada para este doente",
              "C3.1 Dose demasiado baixa",
              "C3.2 Dose de uma substância activa demasiado alta",
              "C3.3 Regime posológico pouco frequente",
              "C3.4 Regime posológico demasiado frequente",
              "C3.5 Instruções de horário erradas, pouco claras ou ausentes",
              "C4.1 Duração do tratamento demasiado curta",
              "C4.2 Duração do tratamento demasiado longa",
              "C5.1 Medicamento prescrito indisponível",
              "C6.1 Horário ou intervalo de administração inadequado",
              "C6.2 Medicamento administrado abaixo do prescrito",
              "C6.3 Medicamento administrado acima do prescrito",
              "C6.4 Medicamento não administrado",
              "C6.5 Medicamento errado administrado",
              "C6.6 Via de administração errada",
              "C7.1 Doente toma intencionalmente menos do que o prescrito "
              "ou não toma, por qualquer motivo",
              "C8.1 Problema de reconciliação da medicação",
              "C9.1 Monitorização inexistente ou inadequada",
              "C9.2 Outra causa: ____________",
              "C9.3 Sem causa evidente"]),
        PERG("Intervenção planeada (assinalar todas as aplicáveis):",
             ["I0.1 Sem intervenção",
              "I1.1 Prescritor apenas informado",
              "I1.2 Pedido de informação ao prescritor",
              "I1.3 Intervenção proposta ao prescritor",
              "I1.4 Intervenção discutida com o prescritor",
              "I2.1 Aconselhamento ao doente",
              "I2.4 Conversa com familiar ou cuidador",
              "I3.1 a I3.6 Proposta de alteração do medicamento, da dose, "
              "da forma, das instruções, de suspensão ou de início "
              "(especificar): ____________",
              "I4.1 Outra intervenção: ____________",
              "I4.2 Reacção adversa notificada à autoridade"]),
        PERG("Aceitação (uma por intervenção):",
             ["A1.1 Aceite e totalmente implementada",
              "A1.2 Aceite e parcialmente implementada",
              "A1.3 Aceite mas não implementada",
              "A1.4 Aceite, implementação desconhecida",
              "A2.1 Não aceite: não exequível",
              "A2.2 Não aceite: sem acordo",
              "A2.3 Não aceite: outro motivo",
              "A2.4 Não aceite: motivo desconhecido",
              "A3.1 Proposta, aceitação desconhecida",
              "A3.2 Não proposta"]),
        PERG("Estado do problema no fim do seguimento:",
             ["O0.1 Desconhecido", "O1.1 Totalmente resolvido",
              "O2.1 Parcialmente resolvido",
              "O3.1 Não resolvido, falta de cooperação do doente",
              "O3.2 Não resolvido, falta de cooperação do prescritor",
              "O3.3 Não resolvido, intervenção ineficaz",
              "O3.4 Sem necessidade ou possibilidade de resolver"]),
        PERG("Impacto clínico potencial da intervenção (dimensão clínica "
             "CLEO):", ["-1 Prejudicial", "0 Nulo", "1 Menor", "2 Moderado",
                        "3 Importante", "4 Evita consequência fatal"]),
        CAMPO("Avaliador 1: P______ C______ CLEO____   Avaliador 2: P______ "
              "C______ CLEO____   Decisão final: P______ C______ CLEO____"),
        CAMPO("Comunicado ao prescritor em ___/___/______ às ____h____   "
              "Comunicação imediata (níveis 3 ou 4): (   ) Sim   (   ) Não"),
        NOTA("Escala de probabilidade de reacções adversas de Naranjo, a "
             "preencher apenas quando o problema for P2.1 manifesto. "
             "Pontuação total: 9 ou mais, definida; 5 a 8, provável; 1 a 4, "
             "possível; 0 ou menos, duvidosa."),
        TABELA(None, "", ["N.º", "Pergunta", "Sim", "Não", "Não sabe"],
               [["1", "Há relatos conclusivos anteriores sobre esta "
                 "reacção?", "+1", "0", "0"],
                ["2", "O acontecimento adverso surgiu depois da "
                 "administração do medicamento suspeito?", "+2", "-1", "0"],
                ["3", "O acontecimento adverso melhorou quando o "
                 "medicamento foi suspenso ou quando se administrou um "
                 "antagonista específico?", "+1", "0", "0"],
                ["4", "O acontecimento adverso reapareceu quando o "
                 "medicamento foi readministrado?", "+2", "-1", "0"],
                ["5", "Há causas alternativas que, por si só, poderiam ter "
                 "causado a reacção?", "-1", "+2", "0"],
                ["6", "A reacção reapareceu quando se administrou um "
                 "placebo?", "-1", "+1", "0"],
                ["7", "O medicamento foi detectado no sangue ou noutros "
                 "fluidos em concentrações reconhecidamente tóxicas?", "+1",
                 "0", "0"],
                ["8", "A reacção foi mais grave quando a dose aumentou, ou "
                 "menos grave quando a dose diminuiu?", "+1", "0", "0"],
                ["9", "O doente teve uma reacção semelhante ao mesmo "
                 "medicamento ou a medicamentos semelhantes numa exposição "
                 "anterior?", "+1", "0", "0"],
                ["10", "O acontecimento adverso foi confirmado por alguma "
                 "evidência objectiva?", "+1", "0", "0"]],
               larguras=[1.0, 10.6, 1.4, 1.4, 1.6]),
        CAMPO("Pontuação total: ______   Categoria: (   ) definida   (   ) "
              "provável   (   ) possível   (   ) duvidosa"),
        H3("Secção VII. Fim do seguimento"),
        PERG("Motivo do fim do seguimento:",
             ["Alta", "Óbito", "Transferência", "Abandono",
              "Trigésimo dia de internamento"]),
        CAMPO("Data: ___/___/______   Dias de seguimento: ______   Número "
              "máximo de medicamentos em simultâneo: ______"),
        CAMPO("Número de PRM validados: ______   Assinatura do "
              "investigador: ______________________"),
    ]),
    ("Folha de informação ao participante", [
        P("Título do estudo: Problemas relacionados com medicamentos e "
          "contributo potencial do farmacêutico em doentes internados na "
          "enfermaria de Medicina do Hospital Central de Nampula, 2027."),
        P("Investigador: [Nome do(a) estudante], estudante finalista do curso "
          "de licenciatura em Farmácia da Faculdade de Ciências de Saúde da "
          "Universidade Lúrio, sob orientação de [Nome e grau académico do(a) "
          "orientador(a)]."),
        P("Porque é feito este estudo? Os medicamentos tratam as doenças, "
          "mas às vezes a dose não é a adequada, dois medicamentos não "
          "combinam bem ou falta um tratamento necessário. Queremos saber "
          "com que frequência isto acontece nesta enfermaria e como o "
          "farmacêutico pode ajudar os médicos e enfermeiros a corrigir "
          "estes problemas."),
        P("O que acontece se aceitar participar? Vamos fazer-lhe algumas "
          "perguntas, durante cerca de dez minutos, sobre os medicamentos "
          "que tomava antes de vir ao hospital. Durante o internamento, a "
          "equipa do estudo vai consultar todos os dias o seu processo e as "
          "folhas dos seus medicamentos. Não haverá colheitas de sangue, "
          "exames nem medicamentos a mais por causa do estudo."),
        P("Riscos e benefícios: o estudo não traz riscos para a sua saúde. O "
          "único incómodo é o tempo da entrevista. Se encontrarmos algum "
          "problema com os seus medicamentos, informaremos o médico que o "
          "trata, que decidirá o que fazer. Os resultados vão ajudar a "
          "melhorar o uso dos medicamentos no hospital."),
        P("Confidencialidade: o seu nome não será escrito nas fichas do "
          "estudo; usamos apenas um código. Os dados serão guardados em "
          "armário fechado e numa base protegida, e os resultados serão "
          "apresentados sem identificar ninguém."),
        P("Participação voluntária: pode recusar ou desistir a qualquer "
          "momento, sem dar explicações e sem qualquer prejuízo nos cuidados "
          "que recebe no hospital. Não terá custos nem receberá pagamento. "
          "Se ficar sem capacidade para decidir, pediremos o consentimento a "
          "um familiar responsável e voltaremos a falar consigo quando "
          "estiver melhor."),
        P("Contactos: investigador, telefone +258 [preencher]; Comité "
          "Institucional de Bioética para a Saúde da Universidade Lúrio, "
          "telefone +258 [preencher]. Este estudo foi aprovado por esse "
          "comité e autorizado pela direcção do Hospital Central de "
          "Nampula."),
    ]),
    ("Termo de consentimento livre e esclarecido", [
        P("Eu, abaixo identificado(a), declaro que me foi lida e explicada, "
          "numa língua que compreendo, a folha de informação do estudo "
          "«Problemas relacionados com medicamentos e contributo potencial "
          "do farmacêutico em doentes internados na enfermaria de Medicina "
          "do Hospital Central de Nampula, 2027». Compreendi o objectivo, o "
          "que a participação envolve, os riscos, os benefícios e os meus "
          "direitos. Pude fazer perguntas e obtive respostas. Sei que posso "
          "desistir a qualquer momento sem prejuízo nos meus cuidados. "
          "Aceito participar livremente e autorizo a consulta diária do meu "
          "processo clínico pela equipa do estudo."),
        CAMPO("Código do participante: ____________"),
        CAMPO("Assinatura do participante: _________________________________   "
              "Data: ___/___/______"),
        CAMPO("Impressão digital (para quem não sabe escrever):   [          ]"),
        CAMPO("Testemunha imparcial (nome e assinatura): "
              "_____________________________________"),
        H3("Consentimento do representante (doente sem capacidade de "
           "decisão)"),
        CAMPO("Nome do representante: ______________________________   "
              "Relação com o doente: ________________"),
        CAMPO("Assinatura ou impressão digital do representante: "
              "_____________________   Data: ___/___/______"),
        CAMPO("Confirmação posterior pelo doente: (   ) Sim   (   ) Não   "
              "Data: ___/___/______"),
        H3("Declaração do investigador"),
        CAMPO("Declaro que expliquei o estudo ao participante ou ao seu "
              "representante e respondi às suas perguntas."),
        CAMPO("Assinatura do investigador: ______________________________   "
              "Data: ___/___/______"),
    ]),
    ("Nota de intervenção farmacêutica", [
        NOTA("Nota dirigida ao médico responsável pelo doente. Constitui uma "
             "proposta: a decisão terapêutica pertence ao prescritor. Um "
             "duplicado fica no arquivo do estudo, sem o nome do doente."),
        CAMPO("Data: ___/___/______   Cama: ______   Código do doente no "
              "estudo: ____________"),
        CAMPO("Medicamento ou medicamentos em causa: "
              "_____________________________________________"),
        CAMPO("Problema identificado: "
              "_______________________________________________________"),
        CAMPO("Proposta: "
              "__________________________________________________________"),
        CAMPO("Fundamentação e fonte (FNM, norma do MISAU, base de "
              "interacções): _________________________"),
        PERG("Prioridade:", ["Imediata (impacto potencial importante ou "
                             "fatal)", "Na visita seguinte"]),
        H3("Resposta do prescritor (facultativa)"),
        PERG("Decisão:", ["Aceite", "Aceite com alteração", "Não aceite"]),
        CAMPO("Observações: "
              "_______________________________________________________"),
        CAMPO("Farmacêutico responsável: ______________________   Contacto: "
              "[preencher]"),
    ]),
    ("Pedido de autorização institucional", [
        CAMPO("Exmo(a). Senhor(a) Director(a)-Geral do Hospital Central de "
              "Nampula"),
        CAMPO("C/c: Direcção Clínica, Serviço de Medicina e Direcção de "
              "Farmácia do HCN; Direcção Provincial de Saúde de Nampula"),
        CAMPO("Assunto: Pedido de autorização para a realização de um "
              "estudo de investigação"),
        P("Eu, [Nome do(a) estudante], estudante finalista do curso de "
          "licenciatura em Farmácia da Faculdade de Ciências de Saúde da "
          "Universidade Lúrio, venho por este meio solicitar a Vossa "
          "Excelência autorização para realizar, na enfermaria de Medicina "
          "deste hospital, o estudo intitulado «Problemas relacionados com "
          "medicamentos e contributo potencial do farmacêutico em doentes "
          "internados na enfermaria de Medicina do Hospital Central de "
          "Nampula, 2027», sob orientação de [Nome e grau académico do(a) "
          "orientador(a)]."),
        P("O estudo tem como objectivo avaliar os problemas relacionados com "
          "medicamentos dos doentes adultos internados e o contributo "
          "potencial das intervenções farmacêuticas. Prevê a inclusão de 364 "
          "doentes entre 1 de Março e 30 de Junho de 2027, com o seu "
          "consentimento, e a consulta diária dos processos clínicos, das "
          "folhas de prescrição e das folhas de administração, bem como do "
          "livro de admissões da enfermaria. Os problemas identificados "
          "serão comunicados ao médico responsável como propostas, cabendo "
          "a decisão ao prescritor, e as suspeitas de reacção adversa serão "
          "notificadas através do responsável de farmacovigilância do "
          "hospital."),
        P("Solicita-se ainda a indicação de um farmacêutico do hospital "
          "para segundo avaliador, a colaboração de um médico internista do "
          "Serviço de Medicina e o acesso aos dados agregados de "
          "internamentos de Março a Junho de 2026, necessários ao "
          "planeamento da amostra. O estudo será iniciado apenas após o "
          "parecer favorável do Comité Institucional de Bioética para a "
          "Saúde da Universidade Lúrio. A recolha não perturbará o "
          "funcionamento do serviço, os dados serão tratados de forma "
          "confidencial e sem identificação de doentes ou profissionais, e "
          "os resultados serão devolvidos ao hospital num relatório e numa "
          "sessão com a equipa."),
        CAMPO("Nampula, ____ de ________________ de 2026"),
        CAMPO("O(A) estudante: ________________________________"),
        CAMPO("O(A) orientador(a): ____________________________"),
    ]),
]
