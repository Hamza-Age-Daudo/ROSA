# -*- coding: utf-8 -*-
"""
Tema 33 (Farmacognosia e Plantas Medicinais). Uso concomitante de plantas
medicinais e potencial de interacção com anti-hipertensores em doentes
hipertensos internados nos Departamentos de Medicina I e II do Hospital
Central de Nampula. Referências geradas por _motor/refs.py (pmid, doi ou web).

Compor e validar:   python -X utf8 _motor/motor.py _conteudo/tema_33.py
Verificar fontes:   python -X utf8 _motor/refs.py verificar _conteudo/tema_33.py
"""
from blocos import (CAMPO, ESCALA, FORMULA, H3, LISTA, NOTA, P, PERG,
                    QUADRO, QUEBRA, TABELA)

NUMERO = 33
SLUG = "Plantas_Medicinais_Interacoes_Hipertensos_Internados_HCN_Nampula"
TITULO = ("Uso concomitante de plantas medicinais e potencial de interacção "
          "com anti-hipertensores em doentes internados nos Departamentos de "
          "Medicina I e II, Hospital Central de Nampula, 2027")
DESENHO = ("Transversal descritivo e analítico, de base hospitalar, com "
           "entrevista estruturada e componente etnofarmacológica "
           "(identificação botânica e classificação do potencial de "
           "interacção)")

AUTOR = "[Nome do(a) estudante]"
ORIENTADOR = "[Nome e grau académico do(a) orientador(a)]"

# ---------------------------------------------------------------- resumo --
RESUMO = (
    "O uso de plantas medicinais em simultâneo com medicamentos "
    "convencionais é frequente entre doentes hipertensos da África "
    "subsariana, raramente é comunicado aos profissionais de saúde e "
    "associa-se a maior gravidade da hipertensão e a mais complicações, "
    "sobretudo renais. Em Moçambique, a hipertensão é uma das principais "
    "causas de internamento na medicina interna, mas não existem dados "
    "sobre o uso concomitante de plantas entre doentes hipertensos "
    "internados, nem sobre o potencial de interacção com os "
    "anti-hipertensores prescritos. O estudo avalia esse uso concomitante, "
    "a sua comunicação aos profissionais de saúde, o potencial de "
    "interacção das combinações e a associação entre o uso e a gravidade da "
    "apresentação clínica, em adultos internados por hipertensão ou por uma "
    "complicação hipertensiva nos departamentos de medicina interna do "
    "Hospital Central de Nampula. É um estudo transversal, descritivo e "
    "analítico, de base hospitalar, com componente etnofarmacológica, "
    "recolha de Março a Junho de 2027, entrevista consecutiva dos doentes "
    "elegíveis, cerca de 205 adultos, e questionário adaptado de "
    "instrumentos internacionais sobre medicina complementar, validado por "
    "painel de peritos, traduzido para emakhuwa e pré-testado. As plantas "
    "mais citadas serão identificadas por botânicos a partir de exemplares "
    "de herbário ou fotografias, e o potencial de interacção de cada "
    "combinação será classificado por dois avaliadores independentes com "
    "base em monografias, estudos farmacocinéticos e farmacodinâmicos e "
    "literatura revista por pares. A análise incluirá proporções com "
    "intervalos de confiança a 95%, o coeficiente kappa de Cohen e a "
    "regressão de Poisson com variância robusta. Espera-se estimar a "
    "frequência do uso concomitante, descrever as espécies e preparações "
    "usadas, quantificar a não revelação, identificar combinações com "
    "potencial de interacção descrito e verificar se o uso é mais frequente "
    "nos internados por complicação hipertensiva, o que fundamenta a "
    "inclusão da pergunta sobre medicina tradicional na anamnese "
    "farmacêutica hospitalar."
)
PALAVRAS_CHAVE = ["doentes internados", "hipertensão arterial",
                  "interacções entre plantas e medicamentos", "Moçambique",
                  "plantas medicinais"]
ABSTRACT = (
    "The use of medicinal plants together with conventional medicines is "
    "common among hypertensive patients in sub-Saharan Africa, is seldom "
    "disclosed to health professionals and is associated with greater "
    "severity of hypertension and more complications, particularly renal. "
    "In Mozambique, hypertension is one of the leading causes of admission "
    "to internal medicine wards, but there are no data on the concomitant "
    "use of plants among hospitalized hypertensive patients, nor on the "
    "interaction potential with the prescribed antihypertensive drugs. The "
    "study assesses this concomitant use, its disclosure to health "
    "professionals, the interaction potential of the combinations and the "
    "association between use and the severity of the clinical "
    "presentation, among adults admitted for hypertension or a "
    "hypertensive complication to the internal medicine departments of "
    "Hospital Central de Nampula. It is a cross-sectional, descriptive and "
    "analytical, hospital-based study with an ethnopharmacological "
    "component, with data collection from March to June 2027, consecutive "
    "interviews of eligible patients, about 205 adults, and a questionnaire "
    "adapted from international instruments on complementary medicine, "
    "validated by an expert panel, translated into Emakhuwa and pretested. "
    "The most frequently cited plants will be identified by botanists from "
    "herbarium specimens or photographs, and the interaction potential of "
    "each combination will be classified by two independent assessors "
    "based on monographs, pharmacokinetic and pharmacodynamic studies and "
    "peer-reviewed literature. The analysis will include proportions with "
    "95% confidence intervals, Cohen's kappa coefficient and Poisson "
    "regression with robust variance. The study is expected to estimate "
    "the frequency of concomitant use, describe the species and "
    "preparations used, quantify non-disclosure, identify combinations "
    "with a described interaction potential and determine whether use is "
    "more frequent among patients admitted for a hypertensive complication, "
    "which supports the systematic inclusion of a question on traditional "
    "medicine in the hospital pharmaceutical medication history."
)
KEYWORDS = ["herb-drug interactions", "hospitalized patients", "hypertension",
            "medicinal plants", "Mozambique"]

ABREVIATURAS = [
    ("ANARME", "Autoridade Nacional Reguladora de Medicamento, Instituto "
               "Público"),
    ("AVC", "acidente vascular cerebral"),
    ("CIBS-UniLúrio", "Comité Institucional de Bioética para a Saúde da "
                      "Universidade Lúrio"),
    ("ConSEFS", "Consensus Statement on Ethnopharmacological Field Studies "
                "(declaração de consenso sobre estudos etnofarmacológicos de "
                "campo)"),
    ("HCN", "Hospital Central de Nampula"),
    ("HIV", "vírus da imunodeficiência humana"),
    ("I-CAM-Q", "International Complementary and Alternative Medicine "
                "Questionnaire (questionário internacional sobre o uso de "
                "medicina complementar e alternativa)"),
    ("IC95%", "intervalo de confiança a 95%"),
    ("IECA", "inibidor da enzima de conversão da angiotensina"),
    ("IMT", "Instituto de Medicina Tradicional"),
    ("INS", "Instituto Nacional de Saúde"),
    ("IVC", "índice de validade de conteúdo"),
    ("MISAU", "Ministério da Saúde"),
    ("OMS", "Organização Mundial da Saúde"),
    ("OR", "odds ratio (razão de possibilidades)"),
    ("RP", "razão de prevalências"),
    ("RPa", "razão de prevalências ajustada"),
    ("SPSS", "Statistical Package for the Social Sciences"),
    ("STROBE", "Strengthening the Reporting of Observational Studies in "
               "Epidemiology"),
]

# ------------------------------------------------------------ referencias --
# Todas geradas por _motor/refs.py (pmid, doi ou web); nada escrito à mão.
FONTES = {
    "oms2025": "World Health Organization. Global traditional medicine strategy 2025-2034 [Internet]. Geneva: World Health Organization; 2025 [citado 2026 Set 19]. Disponível em: https://www.who.int/publications/i/item/9789240113176",
    "sulola2025": "Sulola MA, Sibai AM, Damasceno A, Issanov A, Sarria-Santamera A, Orazumbekova B, et al. Use of traditional medicine for hypertension, diabetes and hypercholesterolaemia measured in 71 surveys. Bull World Health Organ. 2025;103(11):662-674. doi:10.2471/BLT.25.293665. PMID: 41180269.",
    "foley2019": "Foley H, Steel A, Cramer H, Wardle J, Adams J. Disclosure of complementary medicine use to medical providers: a systematic review and meta-analysis. Sci Rep. 2019;9(1):1573. doi:10.1038/s41598-018-38279-8. PMID: 30733573.",
    "awortwe2018": "Awortwe C, Makiwane M, Reuter H, Muller C, Louw J, Rosenkranz B. Critical evaluation of causality assessment of herb-drug interactions in patients. Br J Clin Pharmacol. 2018;84(4):679-693. doi:10.1111/bcp.13490. PMID: 29363155.",
    "lassale2022": "Lassale C, Gaye B, Diop IB, Mipinda JB, Kramoh KE, Kouam Kouam C, et al. Use of traditional medicine and control of hypertension in 12 African countries. BMJ Glob Health. 2022;7(6). doi:10.1136/bmjgh-2021-008138. PMID: 35654446.",
    "jessen2018": "Jessen N, Damasceno A, Silva-Matos C, Tuzine E, Madede T, Mahoque R, et al. Hypertension in Mozambique: trends between 2005 and 2015. J Hypertens. 2018;36(4):779-784. doi:10.1097/HJH.0000000000001618. PMID: 29210894.",
    "madede2024": "Madede T, Mavume Mangunyane E, Munguambe K, Govo V, Beran D, Levitt N, et al. Human resources challenges in the management of diabetes and hypertension in Mozambique. PLoS One. 2024;19(3):e0297676. doi:10.1371/journal.pone.0297676. PMID: 38551894.",
    "mocumbi2019a": "Mocumbi AO, Langa DC, Chicumbe S, Schumacher AE, Al-Delaimy WK. Incorporating selected non-communicable diseases into facility-based surveillance systems from a resource-limited setting in Africa. BMC Public Health. 2019;19(1):147. doi:10.1186/s12889-019-6473-2. PMID: 30717732.",
    "mocumbi2019b": "Mocumbi AO, Cebola B, Muloliwa A, Sebastião F, Sitefane SJ, Manafe N, et al. Differential patterns of disease and injury in Mozambique: New perspectives from a pragmatic, multicenter, surveillance study of 7809 emergency presentations. PLoS One. 2019;14(7):e0219273. doi:10.1371/journal.pone.0219273. PMID: 31291292.",
    "sitoe2024": "Sitoe E, Van Wyk BE. An inventory and analysis of the medicinal plants of Mozambique. J Ethnopharmacol. 2024;319(Pt 2):117137. doi:10.1016/j.jep.2023.117137. PMID: 37783405.",
    "barbosa2020": "Barbosa F, Hlashwayo D, Sevastyanov V, Chichava V, Mataveia A, Boane E, et al. Medicinal plants sold for treatment of bacterial and parasitic diseases in humans in Maputo city markets, Mozambique. BMC Complement Med Ther. 2020;20(1):19. doi:10.1186/s12906-019-2809-9. PMID: 32020866.",
    "manuel2020": "Manuel L, Bechel A, Noormahomed EV, Hlashwayo DF, Madureira MDC. Ethnobotanical study of plants used by the traditional healers to treat malaria in Mogovolas district, northern Mozambique. Heliyon. 2020;6(12):e05746. doi:10.1016/j.heliyon.2020.e05746. PMID: 33364508.",
    "misau2010": "Moçambique. Ministério da Saúde. Diploma Ministerial n.º 52/2010, de 23 de Março, que cria o Instituto de Medicina Tradicional. Boletim da República, I Série, n.º 11, 3.º Suplemento [Internet]. Maputo: Imprensa Nacional de Moçambique; 2010 [citado 2026 Set 19]. Disponível em: https://faolex.fao.org/docs/pdf/moz208698.pdf",
    "das2018": "Das Neves Martins Pires PH, Marega A, Creagh JM. Contributions des tradipraticiens de santé au traitement antirétroviral : Étude de cas à Nampula, Mozambique. Afr J Prim Health Care Fam Med. 2018;10(1):e1-e6. doi:10.4102/phcfm.v10i1.1031. PMID: 30456971.",
    "thin2022": "Thin SM, Thet D, Li JY, Nakpun T, Nitadpakorn S, Phanudulkitti C, et al. A systematic review of community pharmacist practices in complementary medicine. Pharm Pract (Granada). 2022;20(3):2697. doi:10.18549/PharmPract.2022.3.2697. PMID: 36733509.",
    "asfaw2016": "Asfaw Erku D, Basazn Mekuria A. Prevalence and Correlates of Complementary and Alternative Medicine Use among Hypertensive Patients in Gondar Town, Ethiopia. Evid Based Complement Alternat Med. 2016;2016:6987636. doi:10.1155/2016/6987636. PMID: 27843480.",
    "james2018": "James PB, Kamara H, Bah AJ, Steel A, Wardle J. Herbal medicine use among hypertensive patients attending public and private health facilities in Freetown Sierra Leone. Complement Ther Clin Pract. 2018;31:7-15. doi:10.1016/j.ctcp.2018.01.001. PMID: 29705483.",
    "phan2026": "Phan ADT, Vo TH, Luu TNN, Ngo HTT, Heinrich M, Kongkaew C. Herbal medicine use disclosure, database-flagged potential herb-drug interactions, and inter - interaction database concordance among patients with non-communicable diseases in Vietnam: A multicenter cross-sectional study. PLoS One. 2026;21(7):e0355046. doi:10.1371/journal.pone.0355046. PMID: 42536629.",
    "decreto2023": "Moçambique. Conselho de Ministros. Decreto n.º 19/2023, de 2 de Maio, que aprova o Regulamento para a Autorização de Introdução no Mercado de Produtos de Saúde, Medicamentos Fitoterápicos e Homeopáticos. Boletim da República, I Série, n.º 83 [Internet]. Maputo: Imprensa Nacional de Moçambique; 2023 [citado 2026 Set 19]. Disponível em: https://archive.gazettes.africa/archive/mz/2023/mz-government-gazette-series-i-dated-2023-05-02-no-83.pdf",
    "hlashwayo2026": "Hlashwayo D, Barbosa F, Martins A, Mussá T, Furvela A, Magaia T, et al. Transforming Healthcare: Mozambique's Pioneering Integrative Medicine Course. Ann Glob Health. 2026;92(1):15. doi:10.5334/aogh.4785. PMID: 41694800.",
    "lei2017": "Moçambique. Assembleia da República. Lei n.º 12/2017, de 8 de Setembro, Lei do Medicamento, Vacinas e outros Produtos Biológicos para Uso Humano [Internet]. Maputo: Imprensa Nacional de Moçambique; 2017 [citado 2026 Set 19]. Disponível em: https://anarme.gov.mz/download/lei-12-2017-de-8-de-setembro-lei-de-medicamento/",
    "liwa2017": "Liwa A, Roediger R, Jaka H, Bougaila A, Smart L, Langwick S, et al. Herbal and Alternative Medicine Use in Tanzanian Adults Admitted with Hypertension-Related Diseases: A Mixed-Methods Study. Int J Hypertens. 2017;2017:5692572. doi:10.1155/2017/5692572. PMID: 28634545.",
    "azizah2021": "Azizah N, Halimah E, Puspitasari IM, Hasanah AN. Simultaneous Use of Herbal Medicines and Antihypertensive Drugs Among Hypertensive Patients in the Community: A Review. J Multidiscip Healthc. 2021;14:259-270. doi:10.2147/JMDH.S289156. PMID: 33568913.",
    "tseletebakang2023": "Tsele-Tebakang T, Morris-Eyton H, Pretorius E. Concurrent use of herbal and prescribed medicine by patients in primary health care clinics, South Africa. Afr J Prim Health Care Fam Med. 2023;15(1):e1-e7. doi:10.4102/phcfm.v15i1.3829. PMID: 37403682.",
    "asmelashe2017": "Asmelashe Gelayee D, Binega Mekonnen G, Asrade Atnafe S, Birarra MK, Asrie AB. Herbal Medicines: Personal Use, Knowledge, Attitude, Dispensing Practice, and the Barriers among Community Pharmacists in Gondar, Northwest Ethiopia. Evid Based Complement Alternat Med. 2017;2017:6480142. doi:10.1155/2017/6480142. PMID: 28904558.",
    "nurfaradilla2020": "Nurfaradilla SA, Saputri FC, Harahap Y. Pharmacokinetic Herb-Drug Interaction between Hibiscus sabdariffa Calyces Aqueous Extract and Captopril in Rats. Evid Based Complement Alternat Med. 2020;2020:5013898. doi:10.1155/2020/5013898. PMID: 32655663.",
    "alam2021": "Alam MA, Bin Jardan YA, Alzenaidy B, Raish M, Al-Mohizea AM, Ahad A, et al. Effect of Hibiscus sabdariffa and Zingiber officinale on pharmacokinetics and pharmacodynamics of amlodipine. J Pharm Pharmacol. 2021;73(9):1151-1160. doi:10.1093/jpp/rgaa062. PMID: 34383955.",
    "ried2020": "Ried K. Garlic lowers blood pressure in hypertensive subjects, improves arterial stiffness and gut microbiota: A review and meta-analysis. Exp Ther Med. 2020;19(2):1472-1478. doi:10.3892/etm.2019.8374. PMID: 32010325.",
    "nyirenda2025": "Nyirenda KK, Mponda J, Chikowe I, Kawonga E, Gomani Phiri NT, Msukwa M, et al. An exploratory evaluation of the interaction risk between herbal products and pharmaceutical medicines used concurrently for disease management in Blantyre, Malawi. Pharm Biol. 2025;63(1):877-895. doi:10.1080/13880209.2025.2586351. PMID: 41259156.",
    "oms1999": "World Health Organization. WHO monographs on selected medicinal plants. Volume 1 [Internet]. Geneva: World Health Organization; 1999 [citado 2026 Set 19]. Disponível em: https://www.who.int/publications/i/item/9241545178",
    "quandt2009": "Quandt SA, Verhoef MJ, Arcury TA, Lewith GT, Steinsbekk A, Kristoffersen AE, et al. Development of an international questionnaire to measure use of complementary and alternative medicine (I-CAM-Q). J Altern Complement Med. 2009;15(4):331-9. doi:10.1089/acm.2008.0521. PMID: 19388855.",
    "esteban2016": "Esteban S, Vázquez Peña F, Terrasa S. Translation and cross-cultural adaptation of a standardized international questionnaire on use of alternative and complementary medicine (I-CAM - Q) for Argentina. BMC Complement Altern Med. 2016;16:109. doi:10.1186/s12906-016-1074-4. PMID: 27029211.",
    "heinrich2018": "Heinrich M, Lardos A, Leonti M, Weckerle C, Willcox M, Applequist W, et al. Best practice in research: Consensus Statement on Ethnopharmacological Field Studies - ConSEFS. J Ethnopharmacol. 2018;211:329-339. doi:10.1016/j.jep.2017.08.015. PMID: 28818646.",
    "govaerts2021": "Govaerts R, Nic Lughadha E, Black N, Turner R, Paton A. The World Checklist of Vascular Plants, a continuously updated resource for exploring global plant diversity. Sci Data. 2021;8(1):215. doi:10.1038/s41597-021-00997-6. PMID: 34389730.",
    "borsch2020": "Borsch T, Berendsohn W, Dalcin E, Delmas M, Demissew S, Elliott A, et al. World Flora Online: Placing taxonomists at the heart of a definitive and comprehensive global resource on the world's plants. TAXON. 2020;69(6):1311-1341. doi:10.1002/tax.12373",
    "almanasreh2019": "Almanasreh E, Moles R, Chen TF. Evaluation of methods used for estimating content validity. Res Social Adm Pharm. 2019;15(2):214-221. doi:10.1016/j.sapharm.2018.03.066. PMID: 29606610.",
    "tsang2017": "Tsang S, Royse CF, Terkawi AS. Guidelines for developing, translating, and validating a questionnaire in perioperative and pain medicine. Saudi J Anaesth. 2017;11(Suppl 1):S80-S89. doi:10.4103/sja.SJA_203_17. PMID: 28616007.",
    "mchugh2012": "McHugh ML. Interrater reliability: the kappa statistic. Biochem Med (Zagreb). 2012;22(3):276-82. PMID: 23092060.",
    "peduzzi1996": "Peduzzi P, Concato J, Kemper E, Holford TR, Feinstein AR. A simulation study of the number of events per variable in logistic regression analysis. J Clin Epidemiol. 1996;49(12):1373-9. doi:10.1016/s0895-4356(96)00236-3. PMID: 8970487.",
    "vonelm2007": "von Elm E, Altman DG, Egger M, Pocock SJ, Gøtzsche PC, Vandenbroucke JP. The Strengthening the Reporting of Observational Studies in Epidemiology (STROBE) statement: guidelines for reporting observational studies. Lancet. 2007;370(9596):1453-7. doi:10.1016/S0140-6736(07)61602-X. PMID: 18064739.",
    "helsinki2025": "World Medical Association. World Medical Association Declaration of Helsinki: Ethical Principles for Medical Research Involving Human Participants. JAMA. 2025;333(1):71-74. doi:10.1001/jama.2024.21972. PMID: 39425955.",
}

# Referências anteriores a 2016: só fontes seminais, com o motivo.
SEMINAIS = {
    "oms1999": "Monografias da OMS sobre plantas medicinais seleccionadas, "
               "fonte de referência sobre qualidade, segurança e interacções "
               "usada na classificação do potencial de interacção.",
    "misau2010": "Diploma que cria o Instituto de Medicina Tradicional ao "
                 "abrigo da Política da Medicina Tradicional de 2004; norma "
                 "institucional em vigor que enquadra o estudo.",
    "quandt2009": "Artigo original do questionário internacional I-CAM-Q, "
                  "instrumento de base adaptado neste estudo.",
    "mchugh2012": "Referência metodológica para a interpretação do "
                  "coeficiente kappa de Cohen usado na concordância entre "
                  "avaliadores.",
    "peduzzi1996": "Estudo de simulação que estabeleceu a regra de pelo "
                   "menos 10 eventos por variável nos modelos de regressão.",
    "vonelm2007": "Declaração STROBE, norma de relato em vigor para estudos "
                  "observacionais.",
    "asfaw2016": "Estudo de 2016 (não anterior a 2016); registado aqui porque "
                 "o número de artigo 6987636 pode ser lido como ano.",
    "liwa2017": "Estudo de 2017; registado porque o número de artigo 5692572 "
                "pode ser lido como ano.",
    "asmelashe2017": "Estudo de 2017; registado porque o número de artigo "
                     "6480142 pode ser lido como ano.",
}

# ----------------------------------------------------- 1. introducao --------
INTRODUCAO = [
    P("A medicina tradicional continua a ser, em grande parte do mundo, uma "
      "fonte de cuidados de primeira linha e um complemento dos serviços de "
      "saúde convencionais. A estratégia mundial da Organização Mundial da "
      "Saúde (OMS) para a medicina tradicional no período de 2025 a 2034 "
      "pede uma oferta segura e eficaz, regulada e integrada nos sistemas de "
      "saúde, e inclui entre as acções a formação dos profissionais de saúde "
      "sobre as potenciais interacções com os tratamentos biomédicos "
      "{oms2025}. Na hipertensão arterial, a doença crónica não transmissível "
      "mais frequente, a análise conjunta de 71 inquéritos nacionais de "
      "países de baixo e médio rendimento, com 309.745 pessoas, mostrou que "
      "8,1% das pessoas com hipertensão diagnosticada recorriam à medicina "
      "tradicional para tratar a doença {sulola2025}."),
    P("A coexistência dos dois sistemas terapêuticos só é segura quando o "
      "profissional de saúde sabe o que o doente toma, e o risco é maior "
      "quando o doente já está gravemente doente. Uma meta-análise de "
      "estudos publicados entre 2003 e 2016 estimou que apenas 33% dos "
      "utilizadores de produtos de origem biológica, como as plantas, "
      "revelavam esse uso ao médico (intervalo de confiança a 95% (IC95%): "
      "24% a 43%), e identificou a falta de pergunta por parte do "
      "profissional entre as razões para o silêncio {foley2019}. As "
      "consequências clínicas não são teóricas: uma revisão de relatos de "
      "reacções adversas atribuídas a interacções entre plantas e "
      "medicamentos reuniu 49 casos clínicos, com predomínio de doença "
      "cardiovascular {awortwe2018}."),
    P("Na África subsariana, entre 2.128 doentes hipertensos seguidos em "
      "serviços de cardiologia de 12 países, incluindo Moçambique, 24% "
      "declararam usar medicina tradicional, com variação entre 10% no "
      "Congo e 48% na Guiné; o uso associou-se a maior probabilidade de "
      "hipertensão grave (odds ratio (OR) 1,34) e de complicações (OR "
      "1,27), sobretudo renais (OR 1,57) {lassale2022}. Obtido em consulta "
      "externa de cardiologia, este achado sugere que o uso concomitante "
      "pode ser ainda mais relevante nos doentes já internados por uma "
      "complicação, o que fundamenta o desenho do presente estudo: num "
      "hospital da Tanzânia, entre 213 adultos internados por doença "
      "relacionada com hipertensão, 24,4% tinham usado plantas no mês "
      "anterior e 22,1% em simultâneo com os anti-hipertensores prescritos "
      "{liwa2017}."),
    P("Em Moçambique, a prevalência de hipertensão nos adultos de 25 a 64 "
      "anos subiu de 33,1% em 2005 para 38,9% em 2014-2015, e só 44,5% dos "
      "tratados tinham a pressão controlada {jessen2018}, o que deixa uma "
      "grande proporção de doentes expostos a complicações; a formação dos "
      "profissionais continua orientada para as doenças infecciosas, com "
      "competências, equipamento e medicamentos insuficientes para a "
      "hipertensão {madede2024}. Dados hospitalares recentes, detalhados na "
      "revisão da literatura, confirmam que a hipertensão é uma causa "
      "relevante de agravamento agudo e de admissão hospitalar no país, "
      "incluindo no Hospital Central de Nampula (HCN) "
      "{mocumbi2019a,mocumbi2019b}."),
    P("O país tem, ao mesmo tempo, uma flora medicinal rica e em uso: um "
      "inventário bibliográfico registou 731 espécies e táxones "
      "infra-específicos de plantas medicinais em Moçambique, 81% das quais "
      "indígenas {sitoe2024}, e, no distrito de Mogovolas, na província de "
      "Nampula, 16 praticantes de medicina tradicional citaram 37 plantas só "
      "para a malária, o que ilustra a extensão do conhecimento local sobre "
      "plantas {manuel2020}. O Estado reconhece esta realidade: ao abrigo da "
      "Política da Medicina Tradicional, aprovada em 2004, foi criado em "
      "2010 o Instituto de Medicina Tradicional (IMT), na dependência do "
      "Ministério da Saúde (MISAU) {misau2010}."),
    P("Na província de Nampula, os praticantes de medicina tradicional "
      "entrevistados junto de cinco centros de saúde declararam usar "
      "sobretudo plantas medicinais e mostraram-se disponíveis para "
      "colaborar com o sistema de saúde {das2018}. Falta, porém, o outro "
      "lado da questão, precisamente onde a literatura africana sugere que "
      "o risco é maior: nenhum estudo mediu, entre os hipertensos "
      "internados nos Departamentos de Medicina I e II do HCN, quantos "
      "combinam plantas com os anti-hipertensores prescritos, se o dizem "
      "aos profissionais e, sobretudo, que combinações têm potencial de "
      "interacção descrito. O presente estudo propõe-se responder a estas "
      "perguntas, com identificação botânica e classificação sistemática "
      "do potencial de interacção, e verificar se o uso concomitante é "
      "mais frequente nos doentes com uma complicação hipertensiva, para "
      "fundamentar a inclusão da pergunta sobre medicina tradicional na "
      "anamnese farmacêutica hospitalar."),
]

# ----------------------------------------------------- 2. problema ----------
PROBLEMA = [
    P("Nos Departamentos de Medicina I e II do HCN, o doente admitido por "
      "hipertensão arterial ou por uma complicação hipertensiva entra numa "
      "rotina centrada nos medicamentos convencionais: história clínica, "
      "prescrição, reconciliação terapêutica à admissão e alta. A pergunta "
      "sobre plantas e preparações tradicionais não faz parte de nenhum "
      "formulário de admissão conhecido, pelo que o uso fica, em regra, por "
      "registar. Em hipertensos africanos de ambulatório, entre 70,2% e "
      "85,1% dos utilizadores não tinham revelado o uso ao profissional "
      "{asfaw2016,james2018}; num estudo recente com 658 doentes crónicos no "
      "Vietname, 96% dos utilizadores não o tinham revelado {phan2026}. No "
      "internamento do HCN, a dimensão deste silêncio é desconhecida."),
    P("A consequência é uma zona cega na segurança da terapêutica, tanto "
      "mais grave quanto mais doente está o utente. Quando a equipa não "
      "sabe que o doente tomou uma decocção ou um chá junto com o "
      "anti-hipertensor, uma pressão descontrolada, uma alteração renal ou "
      "a própria complicação que motivou o internamento pode ser atribuída "
      "apenas a má adesão prévia. As associações já descritas entre o uso "
      "de medicina tradicional e a hipertensão grave e as complicações "
      "renais {lassale2022} tornam este risco plausível precisamente no "
      "doente internado, que os familiares podem "
      "continuar a expor à planta durante o internamento, por confiarem "
      "nela mais do que no medicamento, o que só é detectado se alguém "
      "perguntar."),
    P("O problema tem ainda uma dificuldade técnica própria. Os doentes "
      "referem as plantas pelo nome vernáculo, e o mesmo nome pode designar "
      "espécies diferentes, tal como a mesma espécie pode ter vários nomes. "
      "Sem identificação botânica, não é possível consultar a literatura "
      "sobre interacções com rigor, e mesmo quando a espécie é conhecida, "
      "as bases de dados cobrem mal as plantas africanas: no estudo "
      "vietnamita, várias espécies indígenas não constavam de nenhuma das "
      "quatro bases consultadas e só 0,7% das interacções eram descritas de "
      "forma concordante em todas {phan2026}. Falta, portanto, saber, entre "
      "os hipertensos internados no HCN, qual é a frequência do uso "
      "concomitante, que espécies estão em causa, se o uso é comunicado e "
      "perguntado, que combinações com os anti-hipertensores prescritos "
      "têm potencial de interacção descrito e se esse uso é mais "
      "frequente nos doentes internados por uma complicação."),
]
PERGUNTA = ("Qual é a proporção de adultos internados por hipertensão "
            "arterial ou por uma complicação hipertensiva nos Departamentos "
            "de Medicina I e II do Hospital Central de Nampula que usam "
            "plantas medicinais em simultâneo com os anti-hipertensores "
            "prescritos, em que medida revelam esse uso aos profissionais de "
            "saúde, que combinações apresentam potencial de interacção "
            "descrito na literatura e esse uso é mais frequente entre os "
            "doentes com uma complicação hipertensiva?")
DELIMITACAO = [
    P("O estudo decorre nos Departamentos de Medicina I e II do HCN, "
      "hospital de referência central para a província de Nampula. A "
      "população é constituída por adultos com 18 ou mais anos, internados "
      "nestes departamentos por hipertensão arterial ou por uma complicação "
      "atribuída à hipertensão, com pelo menos um anti-hipertensor "
      "prescrito antes ou durante o internamento. A recolha de dados junto "
      "dos doentes decorre de 1 de Março a 30 de Junho de 2027, e o uso de "
      "plantas refere-se aos 30 dias anteriores à admissão e aos 12 meses "
      "anteriores à entrevista. O objecto de estudo é o uso concomitante, a "
      "identidade botânica das espécies mais citadas, a comunicação com os "
      "profissionais, o potencial de interacção das combinações com os "
      "anti-hipertensores e a associação entre o uso e a gravidade do "
      "quadro que motivou o internamento."),
    P("Ficam fora do âmbito as crianças, as grávidas, os doentes seguidos "
      "apenas em consulta externa ou noutros departamentos, os doentes "
      "diabéticos ou em tratamento anti-retroviral sem hipertensão, as "
      "clínicas privadas, a perspectiva dos praticantes de medicina "
      "tradicional, só contactados para a recolha de exemplares, a eficácia "
      "farmacológica das plantas, a análise química dos produtos e a "
      "demonstração clínica de interacções em cada doente, que exigiria "
      "medições próprias, fora do alcance de uma licenciatura. O estudo "
      "identifica combinações com potencial de interacção descrito na "
      "literatura; não prova que a interacção ocorreu no doente "
      "individual."),
]

# ----------------------------------------------------- 3. objectivos --------
OBJECTIVO_GERAL = (
    "Avaliar o uso concomitante de plantas medicinais e anti-hipertensores, "
    "a sua comunicação aos profissionais de saúde, o potencial de "
    "interacção das combinações e a associação entre o uso e a gravidade da "
    "apresentação clínica em adultos internados por hipertensão arterial ou "
    "por uma complicação hipertensiva nos Departamentos de Medicina I e II "
    "do Hospital Central de Nampula, em 2027.")
OBJECTIVOS_ESPECIFICOS = [
    "Determinar a proporção de doentes internados que usaram plantas "
    "medicinais ou preparações tradicionais em simultâneo com os "
    "anti-hipertensores prescritos.",
    "Caracterizar as plantas e preparações usadas quanto ao nome vernáculo "
    "em emakhuwa e em português, à identidade botânica, à parte usada, à "
    "forma de preparação e à via, bem como os motivos do uso, a fonte de "
    "obtenção, o custo e as alterações do tratamento anti-hipertensor "
    "atribuídas a esse uso.",
    "Determinar a proporção de utilizadores que revelaram o uso aos "
    "profissionais de saúde, as razões da não revelação e a proporção de "
    "doentes a quem esse uso foi perguntado, e analisar a relação entre a "
    "pergunta e a revelação.",
    "Identificar as combinações entre as espécies citadas e os "
    "anti-hipertensores em uso com potencial de interacção farmacocinética "
    "ou farmacodinâmica descrito na literatura e classificá-las segundo o "
    "nível de evidência.",
    "Analisar a associação entre o uso concomitante e a gravidade da "
    "apresentação clínica que motivou o internamento (hipertensão sem "
    "complicação confirmada ou complicação hipertensiva com lesão de "
    "órgão-alvo), a escolaridade e o tempo desde o diagnóstico de "
    "hipertensão.",
]

# ----------------------------------------------------- 4. hipoteses ---------
HIPOTESES_INTRO = [
    P("As hipóteses referem-se às duas componentes analíticas do estudo: a "
      "relação entre a pergunta do profissional e a revelação do uso "
      "(objectivo 3) e a associação com a gravidade da apresentação clínica "
      "(objectivo 5). Os objectivos 1, 2 e 4 são descritivos e orientam-se "
      "pelas questões de investigação a seguir."),
]
HIPOTESES = [
    ("H0", "entre os utilizadores de plantas, a proporção que revelou o uso "
           "a um profissional de saúde não difere entre aqueles a quem o uso "
           "foi perguntado e aqueles a quem não foi perguntado."),
    ("H1", "entre os utilizadores de plantas, a proporção que revelou o uso "
           "é diferente entre aqueles a quem o uso foi perguntado e aqueles "
           "a quem não foi perguntado."),
    ("H0", "a proporção de uso concomitante de plantas medicinais não "
           "difere entre os doentes internados por hipertensão sem "
           "complicação confirmada e os internados por uma complicação "
           "hipertensiva com lesão de órgão-alvo."),
    ("H1", "a proporção de uso concomitante de plantas medicinais é maior "
           "entre os doentes internados por uma complicação hipertensiva com "
           "lesão de órgão-alvo do que entre os internados por hipertensão "
           "sem complicação confirmada."),
]
QUESTOES = [
    "Com que frequência os doentes internados por hipertensão nos "
    "Departamentos de Medicina I e II do HCN usam plantas medicinais em "
    "simultâneo com os anti-hipertensores prescritos?",
    "Que espécies, partes da planta e formas de preparação são usadas, com "
    "que finalidade, onde são obtidas e quanto custam?",
    "Que combinações entre as espécies identificadas e os anti-hipertensores "
    "em uso têm potencial de interacção descrito, com que mecanismo e com "
    "que nível de evidência?",
]

# ----------------------------------------------------- 5. justificativa -----
JUSTIFICATIVA_INTRO = [
    P("A escolha do tema responde a uma lacuna concreta e com consequências "
      "clínicas imediatas. O doente hipertenso internado é o utente em que "
      "uma interacção entre uma planta e o anti-hipertensor tem maior "
      "probabilidade de se traduzir num agravamento mensurável, e o "
      "farmacêutico hospitalar está em melhor posição para a detectar na "
      "reconciliação terapêutica. Saber se e o que os doentes combinam com "
      "plantas é condição para uma prescrição e dispensa hospitalares "
      "seguras, e a resposta não se encontra na literatura sobre o HCN."),
]
JUSTIFICATIVA = {
    "cientifica": [
        P("O estudo produz a primeira estimativa, para o HCN, da frequência "
          "do uso concomitante de plantas medicinais e anti-hipertensores "
          "entre doentes hipertensos internados, com definições operacionais "
          "explícitas de uso, de revelação e de pergunta pelo profissional. "
          "A meta-análise sobre revelação atribuiu parte da heterogeneidade "
          "entre estudos à falta de uma medida padronizada {foley2019}; "
          "medir a revelação e a pergunta com itens definidos a priori "
          "permite comparações futuras, e centrar o estudo numa só doença "
          "aprofunda a componente de interacções, pouco sistematizada nos "
          "estudos de prevalência revistos {nyirenda2025,phan2026}."),
        P("A componente etnofarmacológica acrescenta valor próprio. O "
          "inventário nacional de plantas medicinais foi compilado a partir "
          "de 29 fontes bibliográficas {sitoe2024}, e os estudos de campo "
          "publicados no norte do país centram-se em praticantes e em "
          "doenças infecciosas {manuel2020,das2018}. Ligar os nomes "
          "vernáculos citados por doentes hipertensos internados a espécies "
          "confirmadas por exemplar de herbário, e classificar cada "
          "combinação com os anti-hipertensores por dois avaliadores "
          "independentes com base em evidência farmacocinética e "
          "farmacodinâmica {nurfaradilla2020,alam2021}, gera dados "
          "verificáveis que outros investigadores podem reutilizar."),
    ],
    "academica": [
        P("Para a Licenciatura em Farmácia da Universidade Lúrio, o tema "
          "junta a farmacognosia, a farmacologia cardiovascular e a "
          "farmacovigilância hospitalar num problema real do serviço. O "
          "interesse académico pela medicina integrativa em Moçambique é "
          "recente: no primeiro curso deste tipo na Universidade Eduardo "
          "Mondlane, 134 dos 164 estudantes inscritos concluíram a formação "
          "e a fitoterapia foi o tema mais relevante {hlashwayo2026}. O "
          "questionário traduzido para emakhuwa, a ficha de identificação "
          "botânica e o protocolo de classificação do potencial de "
          "interacção ficam disponíveis para trabalhos posteriores do "
          "curso."),
    ],
    "social": [
        P("Os doentes que combinam plantas com anti-hipertensores fazem-no, "
          "em geral, por razões compreensíveis, que vão da crença na "
          "eficácia à falta de medicamento na unidade sanitária. Um estudo "
          "que pergunta sem julgar, aconselha e encaminha quem reduziu o "
          "tratamento, e devolve os resultados às associações de "
          "praticantes, contribui para uma relação de confiança entre "
          "doentes, famílias, praticantes e a equipa hospitalar. Na "
          "província de Nampula, os praticantes entrevistados mostraram-se "
          "disponíveis para colaborar com o sistema de saúde {das2018}; "
          "conhecer as práticas dos doentes internados é o primeiro passo "
          "para uma articulação semelhante ao nível hospitalar."),
    ],
    "politica": [
        P("O IMT vela pelo uso apropriado e seguro da medicina tradicional e "
          "promove a formação dos técnicos de saúde nesta matéria "
          "{misau2010}, e o regulamento de 2023 dispensa do registo as "
          "preparações extemporâneas e artesanais em pequena escala "
          "{decreto2023}, precisamente as que os doentes obtêm de "
          "praticantes e mercados; para estes produtos, a anamnese "
          "hospitalar e a farmacovigilância são as principais salvaguardas. "
          "Os resultados servem a Direcção Clínica do HCN, o Departamento "
          "de Farmácia e as estruturas do MISAU responsáveis pela medicina "
          "tradicional na decisão de incluir a pergunta sobre plantas na "
          "ficha de admissão e na reconciliação terapêutica, em linha com a "
          "estratégia da OMS {oms2025}."),
    ],
}

# ----------------------------------------------------- 6. revisao -----------
REVISAO = [
    ("Conceitos, definições operacionais e magnitude da hipertensão "
     "internada", [
        P("Na estratégia para 2025-2034, a OMS define a medicina "
          "tradicional como o conjunto de sistemas, codificados ou não, de "
          "cuidados de saúde e bem-estar, com práticas, competências e "
          "conhecimentos originados em contextos históricos e culturais "
          "distintos da biomedicina, tratada em conjunto com a medicina "
          "complementar e integrativa {oms2025}. Neste estudo, planta "
          "medicinal é qualquer planta, ou parte dela, usada com intenção "
          "terapêutica, e preparação tradicional é qualquer produto obtido "
          "a partir de plantas por decocção, infusão, maceração, "
          "pulverização ou mistura, fornecido por praticante, comprado em "
          "mercado ou preparado em casa. A legislação moçambicana define "
          "medicamento fitoterápico como o que tem exclusivamente "
          "substâncias derivadas de plantas como substâncias activas "
          "{decreto2023}; os produtos fitoterápicos embalados vendidos em "
          "farmácias ou ervanárias contam também como uso de plantas."),
        P("Define-se uso concomitante como o uso de pelo menos uma planta "
          "medicinal ou preparação tradicional, com finalidade de saúde, nos "
          "30 dias anteriores à admissão hospitalar, por um doente que, no "
          "mesmo período, tinha pelo menos um anti-hipertensor prescrito. "
          "Plantas consumidas apenas como alimento (folhas cozinhadas, "
          "fruta, condimentos) não contam, excepto quando o doente as toma "
          "com intenção terapêutica, como o alho ou o hibisco para baixar a "
          "tensão. O período de 30 dias anteriores à admissão é a medida "
          "principal, por ser o mais relevante para a interacção que pode "
          "ter contribuído para o internamento e o menos sujeito a "
          "esquecimento; o uso nos 12 meses anteriores é medida secundária."),
        P("Revelação é a declaração do doente de que informou pelo menos um "
          "profissional de saúde sobre o uso de plantas nos 12 meses "
          "anteriores, por iniciativa própria ou em resposta a pergunta. "
          "Pergunta pelo profissional é a declaração de que, no mesmo "
          "período, algum profissional lhe perguntou se usava plantas ou "
          "medicamentos tradicionais. Anamnese farmacêutica hospitalar é a "
          "recolha estruturada, pelo farmacêutico, da história de medicação "
          "do doente à admissão, que alimenta a reconciliação terapêutica."),
        P("Hipertensão arterial é definida, para efeitos de elegibilidade, "
          "pelo diagnóstico registado no processo clínico à admissão, "
          "independentemente dos valores tensionais no momento da "
          "entrevista. Complicação hipertensiva com lesão de órgão-alvo é o "
          "diagnóstico de admissão, registado pelo clínico assistente, de "
          "acidente vascular cerebral (AVC), insuficiência cardíaca "
          "descompensada, lesão renal aguda ou agudização de doença renal "
          "crónica, encefalopatia hipertensiva ou outra lesão de órgão "
          "atribuída à hipertensão; hipertensão sem complicação confirmada "
          "designa os restantes internamentos, incluindo a crise "
          "hipertensiva sem lesão de órgão-alvo documentada. Esta distinção "
          "segue a lógica da associação já descrita entre uso de medicina "
          "tradicional e hipertensão grave ou complicada {lassale2022}, "
          "adaptada ao diagnóstico de admissão disponível no processo."),
        P("A hipertensão é uma causa importante e crescente de doença e de "
          "internamento em Moçambique, com a prevalência e o controlo já "
          "referidos {jessen2018}. Num hospital urbano do país, foi o "
          "diagnóstico mais frequente entre as doenças crónicas não "
          "transmissíveis vigiadas "
          "(37,3% de 6.423 casos), e as emergências hipertensivas foram a "
          "principal causa de transferência urgente e de óbito à entrada "
          "entre essas doenças {mocumbi2019a}; num estudo de vigilância em "
          "três hospitais de referência, incluindo o HCN, as doenças "
          "crónicas não transmissíveis corresponderam a um quarto das 7.809 "
          "urgências amostradas, mais frequentes com a idade {mocumbi2019b}. "
          "Estes dados não isolam o internamento por hipertensão nos "
          "Departamentos de Medicina do HCN, o que justifica a estimativa "
          "própria do tamanho da população elegível apresentada na "
          "metodologia."),
    ]),
    ("Flora medicinal e práticas de medicina tradicional em Moçambique", [
        P("O inventário nacional de plantas medicinais, já referido, "
          "distribui as 731 espécies por 447 géneros e 120 famílias; 590 "
          "são indígenas e 87 são exóticas, naturalizadas ou cultivadas, e "
          "494 são também usadas como medicinais na África do Sul, "
          "sobretudo na província vizinha de KwaZulu-Natal {sitoe2024}. "
          "Esta partilha de espécies e usos com a região sugere que a "
          "literatura sul-africana sobre interacções pode ser útil, mas não "
          "dispensa a confirmação da identidade das plantas usadas em "
          "Nampula."),
        P("O comércio de plantas é visível nas cidades: nos mercados de "
          "Maputo, os vendedores listaram 64 espécies de 32 famílias para "
          "doenças bacterianas e parasitárias, com predomínio das raízes "
          "{barbosa2020}. No distrito de Mogovolas, na província de "
          "Nampula, 16 praticantes citaram 37 plantas para a malária, "
          "preparadas sobretudo a partir de folhas, raízes e casca do "
          "caule, com exemplares depositados no herbário da Universidade "
          "Eduardo Mondlane {manuel2020}; embora a indicação seja outra, o "
          "estudo mostra que o recurso a raízes e cascas é comum na região "
          "e reforça a necessidade de identificação botânica antes de "
          "avaliar qualquer interacção. Junto de cinco centros de saúde de "
          "distritos da província, 79 praticantes de medicina tradicional "
          "declararam usar principalmente plantas e já referiam os casos "
          "complicados ao centro de saúde {das2018}; nenhum destes estudos "
          "mediu o uso pelos próprios doentes, do lado da procura, que é o "
          "que este estudo acrescenta."),
    ]),
    ("Determinantes e motivos do uso em doentes hipertensos", [
        P("Os factores associados ao uso de plantas em hipertensos variam "
          "entre contextos. Nos inquéritos nacionais de países de baixo e "
          "médio rendimento, o uso para a hipertensão na região africana da "
          "OMS foi mais frequente nos homens e nas pessoas com menor "
          "escolaridade {sulola2025}. Em 12 países africanos, os "
          "utilizadores eram mais frequentemente homens, residentes em meio "
          "rural e com pior adesão ao tratamento, muitas vezes por causa do "
          "custo {lassale2022}. Na Tanzânia, entre hipertensos internados, a "
          "menor escolaridade, o emprego não qualificado e a falta de "
          "seguro de saúde associaram-se ao uso, sem associação com pior "
          "adesão {liwa2017}. Em Freetown, o uso associou-se a não ter "
          "emprego formal e a percepcionar a hipertensão como incurável "
          "{james2018}. Esta divergência sobre a escolaridade justifica "
          "testá-la sem assumir a direcção do efeito."),
        P("A revisão de 15 estudos sobre o uso simultâneo de plantas e "
          "anti-hipertensores identificou como factores a idade, o sexo, a "
          "escolaridade, o rendimento e a residência, e verificou que o "
          "alho era a planta mais referida, recomendada sobretudo por "
          "amigos, ervanários e profissionais de saúde {azizah2021}. Em "
          "Gondar, o receio dos efeitos secundários e a percepção de maior "
          "segurança estiveram entre os motivos mais citados pelos "
          "hipertensos utilizadores {asfaw2016}, e na África do Sul os "
          "doentes referiram insatisfação com os medicamentos prescritos e "
          "desconhecimento do risco de interacção {tseletebakang2023}."),
        P("A fonte de obtenção e o custo raramente são medidos, apesar de "
          "condicionarem o risco: as preparações de praticantes ou mercados "
          "têm composição desconhecida, as plantas cultivadas são mais "
          "fáceis de identificar e os produtos embalados trazem, pelo "
          "menos, um rótulo. A falta de equipamento e de medicamentos para "
          "a hipertensão nas unidades moçambicanas {madede2024} pode "
          "empurrar os doentes para estas fontes; por isso o estudo regista "
          "a fonte, o custo mensal e a ruptura de acesso ao "
          "anti-hipertensor."),
    ]),
    ("Comunicação do uso aos profissionais de saúde e farmácia hospitalar", [
        P("A revelação do uso é baixa e depende da forma como o profissional "
          "comunica. A meta-análise de Foley e colaboradores encontrou, além "
          "da taxa global de 33% já referida, valores entre 7% e 80% nos "
          "estudos individuais, e identificou como razões da não revelação "
          "a ausência de pergunta, o receio da desaprovação e a convicção "
          "de que as plantas são seguras; inversamente, a pergunta do "
          "profissional foi uma das razões para revelar {foley2019}, "
          "relação que é a base da hipótese do objectivo específico 3."),
        P("Nos estudos africanos com hipertensos, a não revelação é a regra "
          "e abrange entre sete e nove em cada dez utilizadores "
          "{asfaw2016,james2018}, embora em Freetown 92,7% dos inquiridos "
          "considerassem as plantas benéficas se recomendadas por um "
          "profissional {james2018}. Na África do Sul, os doentes apontaram "
          "as atitudes dos enfermeiros e a falta de tempo como obstáculos à "
          "conversa {tseletebakang2023}. Nenhum destes estudos foi feito no "
          "momento da admissão hospitalar, quando a reconciliação "
          "terapêutica cria uma oportunidade estruturada para a pergunta "
          "que não existe na consulta externa."),
        P("O farmacêutico hospitalar está numa posição privilegiada para "
          "fazer a pergunta, mas a evidência disponível sobre a prática "
          "farmacêutica em geral mostra uma lacuna: numa revisão de 23 "
          "estudos sobre farmácia comunitária, menos de metade dos "
          "farmacêuticos perguntava ou aconselhava sobre medicina "
          "complementar {thin2022}, e em Gondar 72,4% dos farmacêuticos "
          "comunitários classificaram o seu conhecimento sobre plantas como "
          "fraco ou apenas aceitável {asmelashe2017}. Medir, no HCN, a "
          "proporção de doentes internados a quem nenhum profissional "
          "perguntou pelo uso de plantas dá a medida da lacuna que a "
          "reconciliação terapêutica hospitalar pode fechar."),
    ]),
    ("Interacções entre plantas medicinais e anti-hipertensores: "
     "mecanismos, evidência e fontes", [
        P("As interacções entre plantas e medicamentos podem ser "
          "farmacocinéticas, quando constituintes da planta alteram a "
          "absorção, o metabolismo ou a eliminação do medicamento, por "
          "exemplo por inibição ou indução de isoenzimas do citocromo P-450 "
          "ou de transportadores de efluxo, ou farmacodinâmicas, quando a "
          "planta soma ou opõe o seu efeito ao do medicamento, como um "
          "efeito hipotensor aditivo ou um distúrbio electrolítico que "
          "potencia a toxicidade. Na revisão de causalidade já referida, "
          "com predomínio de doentes com doença cardiovascular entre os "
          "casos analisados, a avaliação usou escalas de probabilidade de "
          "interacção {awortwe2018}."),
        P("Para os anti-hipertensores, há evidência específica por classe. "
          "Com os inibidores da enzima de conversão da angiotensina (IECA), "
          "um estudo farmacocinético em ratos mostrou que o extracto aquoso "
          "de *Hibiscus sabdariffa* L. reduziu a área sob a curva do "
          "captopril para cerca de um quinto e aumentou a sua depuração "
          "corporal aparente, fora do intervalo de bioequivalência, o que "
          "sugere risco de perda de eficácia anti-hipertensora "
          "{nurfaradilla2020}. Com os bloqueadores dos canais de cálcio, a "
          "co-administração de *H. sabdariffa* ou de *Zingiber officinale* "
          "Roscoe com amlodipina, em ratos hipertensos, potenciou a redução "
          "da pressão arterial em relação à amlodipina isolada e alterou a "
          "sua farmacocinética, com aumento da área sob a curva "
          "{alam2021}; a direcção aqui é de reforço aditivo do efeito, com "
          "risco de hipotensão. Para o alho, uma meta-análise de 12 ensaios "
          "clínicos em 553 hipertensos mostrou uma redução média da pressão "
          "sistólica de 8,3 mmHg, semelhante à de um anti-hipertensor de "
          "primeira linha, o que configura um efeito farmacodinâmico "
          "aditivo plausível com qualquer classe de anti-hipertensor "
          "{ried2020}. O alcaçuz, constituinte comum de misturas de "
          "ervanária, actua por mecanismo distinto: a inibição da enzima "
          "que inactiva o cortisol nos rins causa retenção de sódio, perda "
          "de potássio e subida da pressão arterial, o que pode agravar a "
          "hipocaliemia induzida pelos diuréticos tiazídicos, mecanismo "
          "farmacodinâmico conhecido embora não estudado com estes "
          "anti-hipertensores em Moçambique."),
        P("Os estudos em doentes crónicos africanos começam a classificar "
          "sistematicamente este potencial. Em Blantyre, 301 doentes usavam "
          "alho, gengibre, quiabo, limão, manga e moringa com "
          "hidroclorotiazida, enalapril e amlodipina, entre outros, e uma "
          "revisão dirigida da literatura indicou, nalgumas combinações, "
          "potencial relevante de interacção, sem verificação clínica "
          "{nyirenda2025}. No Vietname, as interacções potenciais "
          "identificadas com quatro bases de dados atingiam 31,3% dos "
          "utilizadores de plantas, com concordância quase nula entre bases "
          "{phan2026}."),
        P("Daqui decorre que nenhuma fonte isolada basta para classificar o "
          "potencial de interacção com um anti-hipertensor: as monografias "
          "da OMS descrevem precauções conhecidas {oms1999}, os estudos "
          "farmacocinéticos e farmacodinâmicos por classe, como os já "
          "citados, fornecem o mecanismo e a direcção do efeito, e a "
          "literatura revista por pares, pesquisada por espécie e por "
          "classe farmacológica, cobre as combinações ausentes das bases "
          "estruturadas. É esta combinação de fontes, aplicada por dois "
          "avaliadores independentes, que a metodologia adopta para "
          "reforçar a componente de interacções."),
    ]),
    ("Enquadramento normativo e institucional moçambicano", [
        P("A Política da Medicina Tradicional e a Estratégia da sua "
          "Implementação foram aprovadas pela Resolução n.º 11/2004, de 14 "
          "de Abril, e, ao seu abrigo, o Diploma Ministerial n.º 52/2010 "
          "criou o IMT na dependência do Ministro da Saúde, para onde "
          "transitaram as competências do Instituto Nacional de Saúde (INS) "
          "sobre plantas medicinais. Entre as funções do IMT contam-se velar "
          "pelo uso apropriado e seguro da medicina tradicional, obter a "
          "colaboração dos praticantes nos programas do MISAU e promover a "
          "formação dos técnicos de saúde nesta matéria {misau2010}."),
        P("No plano farmacêutico, a Lei n.º 12/2017 estabelece o regime dos "
          "medicamentos, vacinas e outros produtos biológicos para uso "
          "humano {lei2017}. Ao seu abrigo, o Decreto n.º 19/2023 aprovou o "
          "regulamento de autorização de introdução no mercado de "
          "medicamentos fitoterápicos, atribuiu a sua aplicação à Autoridade "
          "Nacional Reguladora de Medicamento (ANARME) e isentou de registo "
          "as preparações extemporâneas e artesanais em pequena escala "
          "{decreto2023}. Os produtos embalados ficam, assim, sob controlo "
          "regulamentar, enquanto as decocções e misturas fornecidas por "
          "praticantes e vendedores escapam ao registo; é sobre estas que o "
          "doente precisa de ser interrogado, e a anamnese farmacêutica com "
          "uma pergunta explícita sobre plantas é a forma mais simples de o "
          "saber e de canalizar as suspeitas de reacção adversa para a "
          "farmacovigilância."),
    ]),
    ("Instrumentos de medida e identificação botânica", [
        P("O questionário internacional sobre o uso de medicina complementar "
          "e alternativa (I-CAM-Q) tem quatro secções: visitas a "
          "prestadores, tratamentos complementares recebidos de médicos, uso "
          "de plantas e suplementos, e práticas de auto-cuidado, com espaços "
          "para acrescentar práticas locais {quandt2009}. A sua adaptação "
          "transcultural na Argentina usou tradução e retroversão, consulta "
          "de 17 peritos pelo método Delphi e entrevistas cognitivas a 18 "
          "doentes, e mostrou que a flexibilidade do instrumento permite "
          "acrescentar prestadores e práticas locais {esteban2016}."),
        P("A validade de conteúdo avalia-se por painel de peritos, com o "
          "índice de validade de conteúdo (IVC) calculado por item "
          "{almanasreh2019}, e a tradução para outra língua exige tradução "
          "directa por dois tradutores, síntese, retroversão cega e "
          "pré-teste com entrevista cognitiva {tsang2017}. Quando os itens "
          "são factuais e dicotómicos, como o uso de plantas, a fiabilidade "
          "mede-se melhor pela concordância teste-reteste, com o "
          "coeficiente kappa {mchugh2012}, do que por coeficientes de "
          "consistência interna, próprios de escalas."),
        P("A identificação botânica é o ponto crítico dos estudos "
          "etnofarmacológicos. A declaração de consenso sobre estudos "
          "etnofarmacológicos de campo (ConSEFS) estabelece uma lista de "
          "verificação de boas práticas {heinrich2018}, e os estudos "
          "moçambicanos seguem a prática de depositar exemplares em "
          "herbário para identificação científica {manuel2020}. O nome "
          "aceite e a autoridade de cada espécie são confirmados na World "
          "Checklist of Vascular Plants, mantida pelos Jardins Botânicos "
          "Reais de Kew {govaerts2021}, e no World Flora Online "
          "{borsch2020}."),
    ]),
]

# ----------------------------------------------------- 7. estado da arte ----
ESTADO_ARTE = [
    P("O [[quadro:estado_arte]] sintetiza 12 estudos empíricos publicados "
      "desde 2016 sobre o uso de plantas medicinais por doentes hipertensos, "
      "a sua revelação e o potencial de interacção com anti-hipertensores "
      "específicos, incluindo o estudo multinacional com doentes "
      "moçambicanos, o estudo de vigilância hospitalar com o HCN e o estudo "
      "com praticantes de Nampula."),
    QUADRO("estado_arte",
           "Síntese de estudos sobre o uso concomitante de plantas "
           "medicinais e anti-hipertensores, e sobre interacções descritas "
           "com anti-hipertensores (estado da arte)",
           ["Autor (ano)", "Local", "Desenho (n)", "Principais resultados"],
           [
               ["Sulola et al. (2025) {sulola2025}",
                "Países de baixo e médio rendimento",
                "Análise conjunta de 71 inquéritos nacionais (309.745)",
                "Uso de medicina tradicional em 8,1% das pessoas com "
                "hipertensão diagnosticada; na região africana, maior uso "
                "nos homens e na menor escolaridade."],
               ["Lassale et al. (2022) {lassale2022}",
                "12 países africanos, incluindo Moçambique",
                "Transversal em serviços de cardiologia (2.128 hipertensos)",
                "24% usavam medicina tradicional (10% a 48% entre países); "
                "uso associado a hipertensão grave (OR 1,34) e a "
                "complicações (OR 1,27), sobretudo renais (OR 1,57)."],
               ["Mocumbi et al. (2019) {mocumbi2019b}",
                "Maputo, Beira e Nampula (HCN), Moçambique",
                "Vigilância multicêntrica, urgências (7.809)",
                "Doenças crónicas não transmissíveis em 25,1% das "
                "urgências, mais frequentes com a idade."],
               ["Das Neves Martins Pires et al. (2018) {das2018}",
                "Província de Nampula, Moçambique",
                "Misto, praticantes de medicina tradicional (79)",
                "Uso principal de plantas; referiam casos complicados ao "
                "centro de saúde e aceitavam colaborar com o sistema de "
                "saúde."],
               ["Liwa et al. (2017) {liwa2017}",
                "Tanzânia",
                "Misto, hipertensos internados (213)",
                "24,4% usaram plantas no mês anterior e 22,1% em simultâneo "
                "com anti-hipertensores; menor escolaridade associada ao "
                "uso; sem associação com pior adesão."],
               ["James et al. (2018) {james2018}",
                "Freetown, Serra Leoa",
                "Transversal, hipertensos (260)",
                "56,9% usavam plantas (mel, moringa e alho as mais citadas); "
                "85,1% dos utilizadores não revelaram o uso."],
               ["Asfaw Erku e Basazn Mekuria (2016) {asfaw2016}",
                "Gondar, Etiópia",
                "Transversal, hipertensos em ambulatório (423)",
                "67,8% usavam medicina complementar, sobretudo plantas; "
                "70,2% não revelaram o uso ao médico."],
               ["Nyirenda et al. (2025) {nyirenda2025}",
                "Blantyre, Malawi",
                "Misto, diabéticos e hipertensos (301)",
                "Uso de alho, gengibre, quiabo e moringa com "
                "hidroclorotiazida, enalapril e amlodipina; potencial de "
                "interacção relevante nalgumas combinações, sem verificação "
                "clínica."],
               ["Nurfaradilla et al. (2020) {nurfaradilla2020}",
                "Indonésia (estudo em ratos)",
                "Farmacocinético, captopril e *Hibiscus sabdariffa*",
                "Extracto de hibisco reduziu a área sob a curva do "
                "captopril para cerca de 17% do valor isolado; interacção "
                "com inibidor da enzima de conversão da angiotensina."],
               ["Alam et al. (2021) {alam2021}",
                "Arábia Saudita (estudo em ratos)",
                "Farmacocinético e farmacodinâmico, amlodipina, hibisco e "
                "gengibre",
                "Hibisco e gengibre potenciaram a redução da pressão "
                "arterial da amlodipina; interacção com bloqueador dos "
                "canais de cálcio."],
               ["Ried (2020) {ried2020}",
                "Revisão internacional (ensaios de 1955 a 2018)",
                "Meta-análise, hipertensos (12 ensaios, 553 participantes)",
                "Alho reduziu a pressão sistólica em 8,3 mmHg e a "
                "diastólica em 5,5 mmHg, efeito semelhante a um "
                "anti-hipertensor de primeira linha."],
               ["Phan et al. (2026) {phan2026}",
                "Vietname",
                "Transversal multicêntrico, doentes crónicos (658)",
                "48,6% usavam plantas e 96% não o revelaram; interacções "
                "potenciais em 31,3% dos utilizadores; concordância quase "
                "nula entre quatro bases de dados."],
           ],
           larguras=[3.4, 2.8, 3.6, 6.2],
           fonte="Elaboração própria (2026), a partir das fontes citadas."),
    P("Três padrões atravessam os estudos. O primeiro é a variação da "
      "frequência entre 8% e 68% consoante a população e a definição de "
      "uso, mais estreita quando o estudo separa o uso concomitante do uso "
      "em qualquer momento {liwa2017}. O segundo é a não revelação, acima "
      "de dois terços dos utilizadores em todos os estudos que a mediram. O "
      "terceiro, do lado das interacções, é que os poucos estudos "
      "farmacocinéticos e farmacodinâmicos por classe de anti-hipertensor "
      "mostram efeitos consistentes de reforço, farmacocinético "
      "{nurfaradilla2020}, farmacodinâmico {ried2020} ou ambos {alam2021}: "
      "há, para algumas combinações comuns, mecanismo descrito e coerente "
      "com um risco real."),
    P("As lacunas são igualmente claras. Nenhum dos estudos de prevalência "
      "do quadro refere a confirmação das espécies por exemplar de herbário "
      "antes da avaliação das interacções; só o do Malawi e o do Vietname "
      "classificaram o potencial de interacção ao nível do doente, e nenhum "
      "mediu a concordância entre avaliadores nem a proporção de doentes a "
      "quem o profissional perguntou pelo uso. Os estudos experimentais "
      "sobre interacções com anti-hipertensores existem, mas nenhum os liga "
      "a doentes reais de um serviço africano. Em Moçambique, a evidência "
      "sobre hipertensos limita-se ao estudo multinacional em cardiologia e "
      "aos dados hospitalares gerais sobre a carga da hipertensão; nenhum "
      "estudo mediu o uso concomitante em internados. O presente estudo "
      "preenche estas lacunas ao centrar-se numa só doença e num só "
      "serviço, com identificação botânica, classificação independente do "
      "potencial de interacção por classe de anti-hipertensor e análise da "
      "associação com a gravidade do internamento."),
]
ESQUEMA_TEXTO = [
    P("A [[figura:esquema]] representa as relações que o estudo analisa. Os "
      "factores sociodemográficos, clínicos e terapêuticos e a ruptura do "
      "anti-hipertensor podem influenciar o uso concomitante de plantas, "
      "caracterizado pelas espécies, fonte, custo e consulta a praticante; a "
      "comunicação com os profissionais determina se esse uso é conhecido "
      "e, portanto, se as combinações com potencial de interacção são "
      "detectadas. A gravidade da apresentação clínica que motivou o "
      "internamento é tratada como possível consequente do uso concomitante "
      "e como eixo da comparação do objectivo 5; a idade e o sexo são "
      "tratados como possíveis confundidores na análise multivariável."),
]
ESQUEMA_TITULO = ("Esquema conceptual do uso concomitante de plantas "
                  "medicinais e anti-hipertensores em doentes internados")
ESQUEMA = {
    "contexto": "Doentes internados por hipertensão nos Departamentos de "
                "Medicina I e II do HCN, Março a Junho de 2027",
    "blocos": [
        ("Factores sociodemográficos", ["escolaridade", "ocupação e "
                                        "rendimento", "estado civil",
                                        "residência"]),
        ("Factores clínicos e terapêuticos", ["tempo desde o diagnóstico "
                                              "de hipertensão",
                                              "número de anti-hipertensores",
                                              "percepção do controlo"]),
        ("Acesso ao tratamento convencional", ["ruptura do "
                                               "anti-hipertensor nos "
                                               "últimos 3 meses"]),
        ("Comunicação com os profissionais", ["pergunta do profissional",
                                              "revelação do uso",
                                              "registo no processo"]),
    ],
    "desfecho": ("Uso concomitante, gravidade e potencial de interacção",
                 ["uso nos 30 dias anteriores à admissão: sim; não",
                  "espécies, fonte, custo e consulta a praticante",
                  "gravidade do internamento: sem complicação; com "
                  "complicação",
                  "combinações por nível de evidência (categorias 1 a 5)"]),
    "moderadores": ("Variáveis de confundimento", ["idade", "sexo",
                                                   "departamento (Medicina "
                                                   "I ou II)"]),
}

# ======================== secções 8 a 12 e apêndices: em redacção ==========
METODOLOGIA = [
    ("Tipo e desenho do estudo", [
        P("Trata-se de um estudo observacional, transversal, descritivo e "
          "analítico, de base hospitalar e abordagem quantitativa, com uma "
          "componente etnofarmacológica. Os dados do doente são recolhidos "
          "num único momento durante o internamento, por entrevista "
          "estruturada, e completados pela verificação do processo clínico; "
          "as plantas mais citadas são depois identificadas por botânicos, e "
          "cada combinação entre uma espécie identificada e um "
          "anti-hipertensor em uso é classificada quanto ao potencial de "
          "interacção farmacocinética ou farmacodinâmica descrito na "
          "literatura. O relato seguirá a declaração Strengthening the "
          "Reporting of Observational Studies in Epidemiology (STROBE) "
          "{vonelm2007} e, na componente etnofarmacológica, a lista de "
          "verificação ConSEFS {heinrich2018}."),
    ]),
    ("Local e período do estudo", [
        P("O estudo decorre nos Departamentos de Medicina I e II do HCN, "
          "hospital de referência central para toda a província de Nampula, "
          "que internam adultos com doenças médicas gerais, incluindo a "
          "hipertensão arterial e as suas complicações "
          "[confirmar junto do Departamento de Medicina I/II e da Direcção "
          "Clínica do HCN o número aproximado de internamentos por "
          "hipertensão arterial, como diagnóstico principal ou como "
          "comorbilidade relevante, no último ano]. O internamento estuda o "
          "doente já hospitalizado e presumivelmente mais grave {lassale2022}, "
          "em que a interacção com o anti-hipertensor tem consequências mais "
          "imediatas."),
        P("A recolha de dados junto dos doentes internados decorre de 1 de "
          "Março a 30 de Junho de 2027 (quatro meses), com recrutamento "
          "consecutivo e exaustivo de todos os doentes elegíveis admitidos "
          "no período. Se o tamanho calculado não for atingido a esse "
          "ritmo, a recolha prolonga-se até 31 de Agosto de 2027. A recolha "
          "e a identificação dos exemplares botânicos decorrem de Abril a "
          "Agosto de 2027, e a classificação do potencial de interacção de "
          "Maio a Agosto. O estudo decorre de Outubro de 2026 a Setembro de "
          "2027, e nenhuma actividade com participantes começa antes da "
          "aprovação do comité de bioética e das autorizações "
          "institucionais."),
    ]),
    ("População e unidade de análise", [
        P("A população-alvo é constituída pelos adultos com hipertensão "
          "arterial internados nos Departamentos de Medicina I e II do HCN. "
          "A população acessível são os adultos admitidos nestes "
          "departamentos durante o período de recolha, com diagnóstico de "
          "admissão de hipertensão arterial ou de uma complicação atribuída "
          "à hipertensão, que cumprem os critérios de elegibilidade."),
        P("A unidade de análise principal é o doente internado, incluído uma "
          "única vez, o que se verifica por uma lista de controlo com o "
          "número do processo dos já entrevistados; uma eventual readmissão "
          "só volta a ser entrevistada se corresponder a um episódio "
          "clinicamente distinto. Os doentes com outra doença crónica "
          "associada, por exemplo diabetes, são incluídos desde que a "
          "hipertensão seja diagnóstico de admissão ou comorbilidade "
          "relevante; a comorbilidade é registada. Para o objectivo "
          "específico 4, a unidade de análise secundária é a combinação "
          "entre uma espécie e um anti-hipertensor; como um doente pode "
          "contribuir com várias combinações, os resultados são "
          "apresentados ao nível da combinação e ao nível do doente."),
    ]),
    ("Amostra e cálculo do tamanho da amostra", [
        P("O tamanho mínimo da amostra para o objectivo específico 1, a "
          "proporção de doentes internados com uso concomitante nos 30 dias "
          "anteriores à admissão, foi calculado pela fórmula para estimar "
          "uma proporção:"),
        FORMULA("n<sub>0</sub> = Z<sup>2</sup> × p × (1 - p) / d<sup>2</sup>"),
        P("Em que Z = 1,96 corresponde a um nível de confiança de 95%; d = "
          "0,05 é a margem de erro absoluta; e p = 0,22 é a proporção "
          "esperada. Este valor corresponde ao uso simultâneo de plantas com "
          "anti-hipertensores entre hipertensos internados na Tanzânia "
          "(22,1%), a definição e o contexto mais próximos deste estudo "
          "{liwa2017}, e é próximo dos 24% de uso de medicina tradicional "
          "entre hipertensos de 12 países africanos, incluindo Moçambique, "
          "seguidos em ambulatório de cardiologia {lassale2022}, o que "
          "reforça a estimativa. Substituindo:"),
        FORMULA("n<sub>0</sub> = 1,96<sup>2</sup> × 0,22 × 0,78 / "
                "0,05<sup>2</sup> = 263,7, arredondado para 264"),
        P("A população de doentes hipertensos internados nos Departamentos "
          "de Medicina I e II do HCN durante um período de recolha de "
          "poucos meses é necessariamente pequena, provavelmente algumas "
          "centenas e não milhares [confirmar junto do Departamento de "
          "Medicina I/II e da Direcção Clínica do HCN o número de "
          "internamentos por hipertensão ou complicação hipertensiva no "
          "último ano], pelo que a correcção para população finita, "
          "n<sub>c</sub> = n<sub>0</sub> / [1 + (n<sub>0</sub> - 1) / N], "
          "tem efeito real. A [[tabela:cenarios_n]] mostra o tamanho "
          "corrigido para vários valores de N, entendido como o número de "
          "doentes elegíveis esperado durante o período de recolha."),
        TABELA("cenarios_n",
               "Tamanho da amostra com correcção para população finita, "
               "segundo o número de doentes elegíveis esperado no período de "
               "recolha",
               ["Doentes elegíveis esperados (N)",
                "Amostra corrigida (n<sub>c</sub>)"],
               [["150", "96"], ["200", "115"], ["250", "129"],
                ["300", "141"], ["400", "160"], ["500", "174"],
                ["600", "184"], ["800", "199"], ["1.000", "210"]],
               larguras=[8.0, 8.0],
               fonte="Elaboração própria (2026). Z = 1,96; p = 0,22; "
                     "d = 0,05; n<sub>c</sub> = n<sub>0</sub> / "
                     "[1 + (n<sub>0</sub> - 1) / N]."),
        P("Adopta-se como cenário central de trabalho N = 600 doentes "
          "elegíveis no período de recolha, uma estimativa prudente para um "
          "serviço de referência central que serve toda a província, "
          "sujeita a confirmação; com este cenário, n<sub>c</sub> = 184. Não "
          "se aplica efeito de desenho por conglomerados, porque os dois "
          "departamentos são recenseados na totalidade, sem amostragem "
          "entre vários. Acrescenta-se uma margem de 10% para recusas e "
          "questionários incompletos:"),
        FORMULA("n<sub>f</sub> = 184 / (1 - 0,10) = 204,4, arredondado para "
                "205"),
        P("O tamanho-alvo é, assim, 205 doentes internados; a taxa de "
          "recrutamento nas primeiras semanas indicará se o cenário real se "
          "aproxima do central. Com 205 doentes e uma proporção esperada de "
          "22%, esperam-se cerca de 45 casos de uso concomitante, o que, "
          "pela regra de pelo menos 10 eventos por parâmetro {peduzzi1996}, "
          "limita a regressão de Poisson do objectivo 5 a cerca de quatro "
          "parâmetros; a limitação é assumida e justificada na secção de "
          "processamento e análise."),
        P("Para o objectivo específico 5, verificou-se o poder para comparar "
          "a proporção de uso concomitante entre os doentes internados por "
          "hipertensão sem complicação confirmada e os internados por uma "
          "complicação hipertensiva com lesão de órgão-alvo, com a fórmula "
          "para duas proporções:"),
        FORMULA("n = [Z<sub>1-α/2</sub> × √(2 × p<sub>m</sub> × (1 - "
                "p<sub>m</sub>)) + Z<sub>1-β</sub> × √(p<sub>1</sub>(1 - "
                "p<sub>1</sub>) + p<sub>2</sub>(1 - p<sub>2</sub>))]<sup>2</sup>"
                " / (p<sub>1</sub> - p<sub>2</sub>)<sup>2</sup>"),
        P("Com α = 0,05 (Z<sub>1-α/2</sub> = 1,96), poder de 80% "
          "(Z<sub>1-β</sub> = 0,84), p<sub>1</sub> = 0,17 nos doentes sem "
          "complicação confirmada e p<sub>2</sub> = 0,32 nos doentes com "
          "complicação, a diferença de 15 pontos percentuais corresponde a "
          "um OR de 2,30, compatível em ordem de grandeza com as "
          "associações já descritas entre uso de medicina tradicional e "
          "hipertensão grave ou complicada {lassale2022}, assumida para "
          "fins de planeamento na ausência de estudos que estratifiquem o "
          "uso concomitante pela gravidade do internamento. Substituindo:"),
        FORMULA("n = [1,96 × √(2 × 0,245 × 0,755) + 0,84 × √(0,1411 + "
                "0,2176)]<sup>2</sup> / 0,15<sup>2</sup> = (1,1921 + "
                "0,5031)<sup>2</sup> / 0,0225 = 127,7"),
        P("São necessários 128 doentes efectivos por grupo, ou 256 no total, "
          "acima dos 205 previstos, e esta comparação fica aquém do poder "
          "de 80% para uma diferença de 15 pontos percentuais. Com os 205 "
          "doentes e uma divisão plausível de 60% sem complicação "
          "confirmada e 40% com complicação, o poder estimado para essa "
          "mesma diferença é de cerca de 70%. A análise é, por isso, "
          "tratada como exploratória, reportada com IC95% e interpretada "
          "com cautela, à semelhança da comparação do objectivo específico "
          "3."),
        H3("Técnica de amostragem"),
        P("A amostragem é consecutiva e exaustiva, e não por quota: o "
          "internamento não tem uma lista antecipada de admissões futuras, "
          "e a população elegível é pequena em relação ao tamanho-alvo. "
          "Todos os dias úteis, o estudante ou o inquiridor assistente "
          "consulta o livro de admissões dos Departamentos de Medicina I e "
          "II, identifica os admitidos com hipertensão ou complicação "
          "hipertensiva desde a última visita e avalia a elegibilidade. "
          "Todo o doente elegível é convidado a participar, sem "
          "substituição; as recusas e os motivos são registados para "
          "calcular a taxa de participação, e os doentes sem capacidade de "
          "responder são reavaliados a cada visita até à alta ou ao limite "
          "do período de recolha."),
    ]),
    ("Critérios de inclusão e de exclusão", [
        H3("Critérios de inclusão"),
        LISTA([
            "Idade igual ou superior a 18 anos.",
            "Internamento nos Departamentos de Medicina I ou II do HCN, com "
            "diagnóstico de admissão de hipertensão arterial ou de uma "
            "complicação atribuída à hipertensão, registado no processo "
            "clínico.",
            "Pelo menos um anti-hipertensor prescrito antes da admissão ou "
            "durante o internamento.",
            "Capacidade de responder à entrevista no momento da abordagem "
            "(orientação na pessoa e no tempo, discurso compreensível); os "
            "doentes sem essa capacidade à admissão são reavaliados em "
            "visitas seguintes, até à alta ou ao limite do período de "
            "recolha.",
            "Consentimento informado, assinado ou confirmado por impressão "
            "digital na presença de testemunha.",
        ]),
        H3("Critérios de exclusão"),
        LISTA([
            "Gravidez declarada ou registada no processo.",
            "Ausência de capacidade para responder até à alta, à "
            "transferência, ao óbito ou ao fim do período de recolha.",
            "Não compreensão de português nem de emakhuwa.",
            "Alta, transferência ou óbito antes da abordagem.",
            "Participação no pré-teste do instrumento ou inclusão anterior "
            "no estudo.",
        ]),
    ]),
    ("Variáveis e definições operacionais", [
        P("O [[quadro:variaveis]] apresenta as variáveis, o tipo, a "
          "definição operacional e o objectivo a que cada uma responde. A "
          "variável dependente principal é o uso concomitante nos 30 dias "
          "anteriores à admissão; as variáveis botânicas e de interacção "
          "são atribuídas depois da entrevista, pelos identificadores e "
          "avaliadores."),
        QUADRO("variaveis", "Variáveis do estudo e definições operacionais",
               ["Variável", "Tipo", "Definição operacional e categorias",
                "Objectivo"],
               [
                   ["Idade", "Independente, quantitativa",
                    "Anos completos; 18-39, 40-59, 60 ou mais", "1, 5"],
                   ["Sexo", "Independente, nominal", "Masculino; feminino",
                    "1, 5"],
                   ["Escolaridade", "Independente, ordinal",
                    "Nenhuma; primária; secundária; superior; para o "
                    "objectivo 5, nenhuma ou primária contra secundária ou "
                    "superior", "1, 5"],
                   ["Ocupação e rendimento", "Independente, nominal",
                    "Com rendimento regular; sem rendimento regular", "1, 5"],
                   ["Estado civil e residência", "Independente, nominal",
                    "Solteiro; casado ou em união; separado ou viúvo; bairro "
                    "urbano ou periurbano", "1, 5"],
                   ["Departamento de internamento", "Independente, nominal",
                    "Medicina I; Medicina II", "1, 5"],
                   ["Gravidade e motivo do internamento", "Independente, "
                    "nominal",
                    "Hipertensão sem complicação confirmada (incluindo crise "
                    "hipertensiva sem lesão de órgão-alvo documentada); "
                    "complicação hipertensiva com lesão de órgão-alvo (AVC, "
                    "insuficiência cardíaca descompensada, lesão renal aguda "
                    "ou agudização de doença renal crónica, encefalopatia "
                    "hipertensiva, outra), pelo diagnóstico de admissão",
                    "5"],
                   ["Tempo desde o diagnóstico de hipertensão",
                    "Independente, quantitativa",
                    "Anos, pelo processo; menos de 5; 5 ou mais", "1, 5"],
                   ["Anti-hipertensores em uso", "Independente, nominal e "
                    "quantitativa",
                    "Nome, dose e classe de cada anti-hipertensor prescrito "
                    "(diurético tiazídico; inibidor da enzima de conversão "
                    "da angiotensina; antagonista dos receptores da "
                    "angiotensina II; bloqueador dos canais de cálcio; "
                    "betabloqueador; outro); número total", "4, 5"],
                   ["Percepção do controlo da hipertensão antes do "
                    "internamento", "Independente, ordinal",
                    "Bem controlada; mais ou menos; mal controlada", "5"],
                   ["Ruptura do anti-hipertensor", "Independente, nominal",
                    "Falta do medicamento na unidade sanitária habitual nos "
                    "últimos 3 meses: sim; não", "2, 5"],
                   ["Consulta a praticante de medicina tradicional",
                    "Descritiva, nominal", "Nos últimos 12 meses: sim; não",
                    "2"],
                   ["Uso concomitante actual", "Dependente, nominal",
                    "Pelo menos uma planta ou preparação com finalidade de "
                    "saúde nos 30 dias anteriores à admissão, com "
                    "anti-hipertensor prescrito: sim; não", "1, 5"],
                   ["Uso nos últimos 12 meses", "Descritiva, nominal",
                    "Sim; não", "1"],
                   ["Nome vernáculo", "Descritiva, nominal",
                    "Nome em emakhuwa e em português, tal como dito pelo "
                    "doente", "2"],
                   ["Identidade botânica", "Descritiva, nominal",
                    "Nome aceite com autoridade e família; nível de "
                    "identificação 1 a 4 (ver texto)", "2, 4"],
                   ["Parte usada, preparação e via", "Descritiva, nominal",
                    "Raiz, casca, folha, fruto, semente, planta inteira; "
                    "decocção, infusão, maceração, pó, sumo; oral, tópica, "
                    "banho, inalação", "2"],
                   ["Frequência e duração do uso", "Descritiva, ordinal",
                    "Diária; semanal; ocasional; meses de uso; toma à mesma "
                    "hora dos anti-hipertensores: sim; não; às vezes", "2"],
                   ["Motivo do uso", "Descritiva, nominal (resposta múltipla)",
                    "Por planta: tratar a hipertensão; aliviar efeitos "
                    "adversos; outro problema; reforçar o organismo; causa "
                    "espiritual; outro. Razões gerais: crença na eficácia; "
                    "controlo insuficiente; efeitos incómodos; falta do "
                    "medicamento; custo; conselho; tradição",
                    "2"],
                   ["Fonte de obtenção e de recomendação", "Descritiva, nominal",
                    "Obtenção: praticante; mercado; cultivo próprio; recolha "
                    "no mato; familiar ou vizinho; farmácia ou ervanária. "
                    "Recomendação: família ou amigos; praticante; outro "
                    "doente; profissional; comunicação social", "2"],
                   ["Custo", "Descritiva, quantitativa",
                    "Meticais gastos por mês com plantas e preparações", "2"],
                   ["Redução ou suspensão do anti-hipertensor e efeitos "
                    "atribuídos", "Descritiva, nominal",
                    "Por causa das plantas, nos últimos 12 meses: sim; não; "
                    "problema de saúde atribuído à combinação: sim; não",
                    "2"],
                   ["Revelação do uso", "Dependente, nominal",
                    "Informou pelo menos um profissional nos últimos 12 "
                    "meses: sim, por iniciativa própria; sim, em resposta a "
                    "pergunta; não; a quem; reacção do profissional", "3"],
                   ["Razões da não revelação", "Descritiva, nominal "
                    "(resposta múltipla)",
                    "Não lhe perguntaram; receio de crítica; achou sem "
                    "importância; o profissional não conhece plantas; falta de "
                    "tempo; planta segura; outra {foley2019}", "3"],
                   ["Pergunta pelo profissional", "Independente, nominal",
                    "Algum profissional perguntou pelo uso nos últimos 12 "
                    "meses: sim; não; quem", "3"],
                   ["Registo no processo clínico", "Descritiva, nominal",
                    "Menção ao uso de medicina tradicional no processo: sim; "
                    "não", "3"],
                   ["Percepção do risco da combinação", "Descritiva, nominal",
                    "Acha que tomar plantas com os anti-hipertensores pode "
                    "fazer mal: sim; não; não sabe", "3"],
                   ["Categoria do potencial de interacção",
                    "Dependente, nominal",
                    "Por combinação: categorias 1 a 5 (ver texto); mecanismo "
                    "e direcção", "4"],
                   ["Doente com potencial de interacção descrito",
                    "Dependente, nominal",
                    "Pelo menos uma combinação de categoria 1 ou 2: sim; não",
                    "4"],
               ],
               larguras=[3.6, 2.8, 7.6, 2.0]),
    ]),
    ("Instrumentos de recolha de dados e respectivas fontes", [
        P("São usados quatro instrumentos. O questionário estruturado, "
          "aplicado por entrevistador (Apêndice A), tem oito secções, da "
          "identificação à verificação do processo clínico. Os itens sobre "
          "frequência e finalidade do uso foram adaptados da secção de "
          "plantas do I-CAM-Q {quandt2009,esteban2016}; os itens sobre "
          "espécies, motivos e revelação seguem os usados em inquéritos a "
          "hipertensos africanos {asfaw2016,james2018,liwa2017}; e as "
          "opções sobre razões da não revelação derivam da meta-análise de "
          "Foley e colaboradores {foley2019}. A ficha de verificação do "
          "processo clínico regista o diagnóstico de admissão e a sua "
          "gravidade, os anti-hipertensores prescritos e qualquer menção ao "
          "uso de medicina tradicional; a ficha de identificação botânica e "
          "a de classificação do potencial de interacção constam do "
          "Apêndice B."),
        P("A validade de conteúdo será avaliada por um painel de seis "
          "peritos: dois farmacêuticos, um com experiência em farmácia "
          "clínica hospitalar e outro em farmacognosia, dois clínicos dos "
          "Departamentos de Medicina I e II, um botânico e um técnico com "
          "experiência em medicina tradicional. Cada perito classifica cada "
          "item quanto à relevância e à clareza numa escala de 1 a 4; o IVC "
          "do item é a proporção de peritos que atribui 3 ou 4 "
          "{almanasreh2019}. Com seis peritos, um item só é mantido sem "
          "revisão se pelo menos cinco o considerarem relevante (IVC de "
          "0,83); os itens abaixo de 0,80 são reformulados ou eliminados, e "
          "o IVC médio do instrumento tem de ser de pelo menos 0,80."),
        P("A versão aprovada será traduzida para emakhuwa por dois tradutores "
          "bilingues independentes, sintetizada numa versão única, "
          "retrovertida para português por outros dois tradutores que não "
          "conhecem o original e comparada com este por uma comissão formada "
          "pelo estudante, pelo orientador e pelos tradutores {tsang2017}. "
          "Os termos «planta medicinal», «remédio tradicional» e «contar ao "
          "profissional» recebem atenção especial. O pré-teste será feito "
          "com cerca de 20 doentes, 10% da amostra planeada, na consulta "
          "externa de hipertensão do HCN, e avalia a compreensão, a "
          "duração, a sequência e o registo dos nomes vernáculos; dez "
          "destes doentes fazem também entrevista cognitiva. Como os itens "
          "principais são factuais e dicotómicos, os coeficientes de "
          "consistência interna não se aplicam: a fiabilidade é medida por "
          "teste-reteste, com 15 participantes do pré-teste reentrevistados "
          "por outro entrevistador 7 a 14 dias depois, presencialmente ou "
          "por telefone, calculando-se o kappa de Cohen para o uso, a "
          "revelação, a pergunta pelo profissional e a redução do "
          "anti-hipertensor; itens com kappa inferior a 0,60 são "
          "reformulados antes da recolha {mchugh2012}."),
    ]),
    ("Procedimentos de recolha de dados e controlo de qualidade", [
        P("A equipa de campo é formada pelo estudante e por um inquiridor "
          "assistente, finalista de um curso da saúde e fluente em emakhuwa, "
          "que não pertencem às equipas clínicas dos Departamentos de "
          "Medicina I e II. A formação dura três dias e cobre o protocolo, a "
          "ética e a confidencialidade, a forma de perguntar sem julgar, o "
          "reconhecimento dos sinais de incapacidade para responder, o "
          "registo dos nomes vernáculos, a fotografia de produtos e o "
          "protocolo de referenciação, com entrevistas simuladas."),
        P("Todos os dias úteis, a equipa percorre os Departamentos de "
          "Medicina I e II, identifica os doentes admitidos desde a última "
          "visita com diagnóstico de hipertensão ou de complicação "
          "hipertensiva e avalia a elegibilidade e a capacidade de "
          "responder. O doente elegível recebe a informação junto ao leito "
          "e, se aceitar, é entrevistado num espaço reservado da enfermaria "
          "ou junto ao leito com a cortina fechada, em horário que não "
          "interfira com os cuidados clínicos. A entrevista dura cerca de "
          "30 a 40 minutos e pode ser repartida em duas sessões se o estado "
          "do doente o exigir. Para reduzir a subnotificação, a pergunta "
          "sobre o uso é precedida de uma frase que normaliza a prática e "
          "acompanhada de exemplos de categorias (chás, raízes, cascas, "
          "pós, misturas, produtos embalados). Os anti-hipertensores "
          "declarados são confirmados no processo clínico e no cartão ou "
          "receita do doente ou da família, que pode fotografar o produto "
          "usado, com autorização."),
        P("O estudante revê todos os questionários no próprio dia quanto a "
          "preenchimento e coerência, e o orientador revê uma amostra "
          "semanal. Em 5% das entrevistas do inquiridor assistente, "
          "sorteadas, o estudante repete junto ao leito ou por telefone, "
          "antes da alta, cinco perguntas-chave para verificar a "
          "concordância. Os questionários são digitados duas vezes, de "
          "forma independente, em EpiData, com regras de validação de "
          "intervalo e de coerência, e as discrepâncias são corrigidas pelo "
          "papel."),
    ]),
    ("Procedimentos de identificação botânica das espécies citadas", [
        P("No fim de cada semana, os nomes vernáculos registados são "
          "agrupados, com ajuda de um tradutor, para juntar variantes de "
          "grafia. Os nomes citados por pelo menos três participantes, até "
          "ao máximo dos 20 mais citados, são prioritários para a recolha "
          "de exemplares, obtidos por compra em mercados como cliente "
          "comum, indicação de doentes que cultivam a planta ou colaboração "
          "de praticantes que aceitem participar, com consentimento prévio "
          "informado."),
        P("Cada exemplar é fotografado, georreferenciado, numerado e "
          "prensado segundo as práticas habituais de herbário, de "
          "preferência com material fértil. As raízes, cascas e pós "
          "comprados no mercado guardam-se como amostra de referência, mas "
          "não bastam para identificar a espécie: o exemplar de herbário "
          "tem de vir da planta viva indicada pelo vendedor, praticante ou "
          "doente. A identificação é feita por um botânico, por comparação "
          "com material de herbário e floras regionais, e o exemplar de "
          "referência é depositado com número de voucher no herbário da "
          "Universidade Eduardo Mondlane, onde foram depositados os "
          "exemplares do estudo de Mogovolas {manuel2020}, ou noutro "
          "herbário acordado [confirmar junto da coordenação do curso o "
          "botânico responsável e o herbário de depósito]."),
        P("Como a atribuição de um nome vernáculo a uma espécie depende de "
          "julgamento, dois identificadores trabalham de forma "
          "independente, sem conhecer o resultado um do outro. A "
          "concordância ao nível da espécie é medida pelo kappa de Cohen e "
          "as discordâncias são resolvidas por exame conjunto ou por um "
          "terceiro especialista. O nome aceite, a autoridade e a família "
          "são confirmados na World Checklist of Vascular Plants "
          "{govaerts2021} e no World Flora Online {borsch2020}, com "
          "registo da data de consulta; os sinónimos são convertidos no "
          "nome aceite."),
        P("Cada registo recebe um nível de identificação: nível 1, espécie "
          "confirmada por exemplar com voucher; nível 2, por fotografia "
          "diagnóstica por ambos os identificadores, admitido para plantas "
          "cultivadas ou alimentares inequívocas, como o alho; nível 3, "
          "correspondência provisória com espécies citadas na literatura "
          "{sitoe2024}, registada como hipótese; nível 4, não identificada. "
          "Nenhum binómio é dado como identificação sem exemplar ou "
          "fotografia, os nomes que designam mais de uma espécie são "
          "assinalados como polissémicos, e as misturas são decompostas nos "
          "componentes "
          "conhecidos."),
    ]),
    ("Métodos de classificação do potencial de interacção", [
        P("Para cada doente, lista-se cada combinação entre uma planta usada "
          "nos 30 dias anteriores à admissão e cada anti-hipertensor em uso. "
          "As combinações com espécies de nível 3 ou 4 ficam na categoria 5; "
          "as de nível 1 ou 2 são pesquisadas em todas as fontes seguintes, "
          "porque a concordância entre bases de dados é fraca {phan2026}: as "
          "monografias da OMS sobre plantas medicinais seleccionadas "
          "{oms1999}; a PubMed, com uma estratégia definida a priori que "
          "combina o nome aceite, os sinónimos e o nome comum em inglês da "
          "espécie com o nome do anti-hipertensor e da sua classe (diurético "
          "tiazídico, inibidor da enzima de conversão da angiotensina, "
          "antagonista dos receptores da angiotensina II, bloqueador dos "
          "canais de cálcio, betabloqueador) e termos de interacção, "
          "farmacocinética e farmacodinâmica {nurfaradilla2020,alam2021}; e "
          "pelo menos uma base de dados de interacções de acesso livre. O "
          "[[quadro:categorias]] define as "
          "categorias, fixadas antes da recolha."),
        QUADRO("categorias",
               "Categorias do potencial de interacção entre planta e "
               "medicamento, definidas a priori",
               ["Categoria", "Definição", "Exemplo de fonte admitida"],
               [["1. Interacção demonstrada em humanos",
                 "Alteração farmacocinética ou clínica descrita em humanos com "
                 "a espécie e o medicamento ou outro da mesma classe",
                 "Ensaio clínico, estudo farmacocinético, relato de caso com "
                 "causalidade avaliada"],
                ["2. Potencial descrito sem demonstração em humanos",
                 "Mecanismo farmacocinético demonstrado *in vitro* ou em "
                 "animais, ou efeito farmacodinâmico aditivo descrito "
                 "(hipoglicemiante, hipotensor, nefrotóxico, hepatotóxico)",
                 "Estudo em células ou em animais, monografia"],
                ["3. Estudada em humanos sem interacção relevante",
                 "Estudo em humanos sem alteração clinicamente significativa",
                 "Estudo farmacocinético com resultado nulo"],
                ["4. Sem informação",
                 "Nenhuma informação encontrada nas fontes consultadas; não "
                 "equivale a segurança",
                 "Pesquisa completa sem resultados"],
                ["5. Não avaliável",
                 "Espécie de nível 3 ou 4, nome polissémico ou mistura de "
                 "composição desconhecida", "Não se aplica"]],
               larguras=[4.2, 7.0, 4.8]),
        P("A categoria 3 existe porque a evidência laboratorial ou em animais "
          "nem sempre se traduz na mesma magnitude no doente, como nos "
          "estudos farmacocinéticos e farmacodinâmicos já citados "
          "{nurfaradilla2020,alam2021}: uma combinação só passa à categoria "
          "1 com estudo em humanos com a espécie e o anti-hipertensor, ou "
          "outro da mesma classe. Quando as fontes divergem, a evidência em "
          "humanos prevalece sobre a laboratorial e, entre estudos em "
          "humanos, o resultado positivo prevalece; um resultado nulo só "
          "vale para o anti-hipertensor estudado; e o uso tradicional da "
          "planta para baixar a tensão não conta, por si só, como evidência "
          "de efeito aditivo. Regista-se ainda o mecanismo (farmacocinético, "
          "farmacodinâmico ou desconhecido), a direcção do efeito e a forma "
          "de preparação estudada na fonte, porque o efeito pode depender "
          "do material {nurfaradilla2020}. Dois avaliadores, o estudante e "
          "um segundo farmacêutico, classificam cada combinação de forma "
          "independente, sem acesso à identidade dos doentes; a "
          "concordância é medida pelo kappa de Cohen, e as discordâncias "
          "são resolvidas por consenso ou por um terceiro avaliador."),
    ]),
    ("Processamento e análise dos dados", [
        P("Os dados digitados em EpiData serão exportados para o "
          "Statistical Package for the Social Sciences (SPSS), versão 26 ou "
          "superior, e para o R, usado na regressão de Poisson do "
          "objectivo 5. O nível de significância é de 5% (p<0,05) e todas as "
          "proporções são apresentadas com IC95%. As características dos "
          "participantes são descritas para o conjunto da amostra e por "
          "departamento de internamento, com frequências, médias e desvios "
          "padrão, ou medianas e intervalos interquartis quando a "
          "distribuição não for normal."),
        P("Para o objectivo 1, estima-se a proporção de uso concomitante nos "
          "30 dias anteriores à admissão e de uso nos últimos 12 meses, no "
          "conjunto e por departamento de internamento; a comparação entre "
          "departamentos usa o teste do qui-quadrado. Para o objectivo 2, "
          "apresentam-se o número de citações por nome vernáculo e por "
          "espécie, a proporção de utilizadores que cita cada espécie, as "
          "partes, preparações, vias, frequências, motivos e fontes, a "
          "proporção que consultou praticantes, o custo mensal em mediana e "
          "intervalo interquartil, a proporção de utilizadores que reduziu "
          "ou suspendeu o anti-hipertensor por causa das plantas, a "
          "distribuição dos níveis de identificação e o kappa entre "
          "identificadores."),
        P("Para o objectivo 3, estimam-se a proporção de utilizadores que "
          "revelaram o uso, a quem o revelaram, as razões da não revelação "
          "(resposta múltipla), a proporção de todos os doentes a quem algum "
          "profissional perguntou, a proporção de processos com registo do "
          "uso e a percepção do risco da combinação. A hipótese deste "
          "objectivo é testada pelo qui-quadrado ou pelo teste exacto de "
          "Fisher, com a razão de prevalências (RP) e o respectivo IC95%, "
          "opondo a revelação quando perguntado à revelação espontânea; a "
          "resposta «não se lembra» é tratada como dado em falta. Para o "
          "objectivo 4, apresentam-se o kappa entre avaliadores, o número de "
          "combinações por categoria e por classe de anti-hipertensor, a "
          "proporção de utilizadores e de todos os doentes com pelo menos "
          "uma combinação de categoria 1 ou 2, acompanhada da proporção com "
          "combinações não avaliáveis, e uma tabela de espécies, "
          "anti-hipertensores, categorias, mecanismos e fontes. A "
          "concordância é interpretada segundo McHugh {mchugh2012}."),
        P("Para o objectivo 5, a associação entre o uso concomitante e a "
          "gravidade do internamento, a escolaridade e o tempo desde o "
          "diagnóstico é testada, na análise bivariada, pelo qui-quadrado "
          "com a RP bruta. Como a proporção esperada de uso é superior a "
          "10%, o OR sobrestimaria a associação, pelo que o modelo principal "
          "é a regressão de Poisson com estimador de variância de Huber e "
          "White, que estima a razão de prevalências ajustada (RPa). Com "
          "cerca de 45 doentes com uso concomitante esperados nos 205 "
          "planeados, a regra de pelo menos 10 eventos por parâmetro "
          "{peduzzi1996} limita o modelo a quatro parâmetros: entram, "
          "fixados a priori por corresponderem aos objectivos analíticos do "
          "estudo, a gravidade do internamento, a escolaridade e o tempo "
          "desde o diagnóstico; a idade entra em quarto lugar apenas se o "
          "número de eventos observado sustentar os quatro parâmetros, caso "
          "contrário o modelo fica com três e a idade é reportada só na "
          "análise bivariada. A colinearidade é verificada pelo factor de "
          "inflação da variância (limite de 5), e a regressão logística é "
          "apresentada como análise de sensibilidade. As variáveis com mais "
          "de 5% de valores em falta são descritas, a análise principal usa "
          "os casos completos e o efeito das perdas é discutido."),
    ]),
    ("Limitações do estudo e estratégias de mitigação", [
        P("O [[quadro:limitacoes]] resume as limitações previstas, a sua "
          "consequência e a forma de as mitigar; a mais importante é a "
          "subnotificação do uso, por receio de que a resposta afecte o "
          "atendimento."),
        QUADRO("limitacoes", "Limitações previstas e estratégias de mitigação",
               ["Limitação", "Consequência", "Mitigação"],
               [["Viés de desejabilidade social e de memória",
                 "Subestimação do uso e da não revelação",
                 "Garantia de ausência de consequências, entrevistadores "
                 "externos, frase de normalização, exemplos, período principal "
                 "de 30 dias"],
                ["Estudo num único hospital e recrutamento apenas de "
                 "internados",
                 "Resultados não generalizáveis à consulta externa nem a "
                 "outras unidades; doentes que morrem ou são transferidos "
                 "antes da entrevista ficam por incluir",
                 "Descrição do HCN e dos dois departamentos; registo dos "
                 "óbitos e transferências precoces; discussão da direcção "
                 "provável do viés"],
                ["Identificação botânica incompleta (produtos secos, misturas, "
                 "nomes polissémicos)",
                 "Espécies não identificadas e combinações não avaliáveis",
                 "Níveis de identificação, voucher, dois identificadores, "
                 "proibição de binómios sem exemplar ou fotografia"],
                ["Fontes de interacção com fraca cobertura de plantas "
                 "africanas e discordantes",
                 "Potencial subestimado ou mal classificado",
                 "Várias fontes por combinação, categoria «sem informação» "
                 "distinta de segurança, dois avaliadores e kappa"],
                ["Desenho transversal",
                 "Sem causalidade nem prova de interacção clínica",
                 "Linguagem de potencial descrito; recomendação de estudos "
                 "clínicos"],
                ["Poder limitado para diferenças pequenas, para o objectivo "
                 "3 e para o objectivo 5",
                 "Associações reais podem não atingir significância",
                 "Declaração do poder, apresentação de IC95%, análise "
                 "exploratória"],
                ["Registo incompleto dos anti-hipertensores ou do "
                 "diagnóstico no processo",
                 "Combinações não detectadas; classificação da gravidade "
                 "imprecisa",
                 "Verificação cruzada com o doente, a família, o cartão e a "
                 "receita; diagnóstico de admissão confirmado pelo clínico "
                 "assistente"]],
               larguras=[5, 5, 6]),
    ]),
    ("Considerações éticas", [
        P("O protocolo será submetido ao Comité Institucional de Bioética "
          "para a Saúde da Universidade Lúrio (CIBS-UniLúrio), e a recolha "
          "só começará depois da aprovação e das autorizações da Direcção "
          "Clínica do HCN e da direcção dos Departamentos de Medicina I e "
          "II. O estudo segue a Declaração de Helsínquia na revisão de 2024 "
          "{helsinki2025}. A participação é voluntária e exige consentimento "
          "informado escrito; quem não souber ler ouve a leitura integral da "
          "folha de informação e confirma o consentimento por impressão "
          "digital, na presença de testemunha imparcial (Apêndices C e D). "
          "O doente sem capacidade para consentir só é convidado depois de "
          "a recuperar, avaliada em cada visita."),
        P("Antes de qualquer pergunta, o entrevistador garante de forma "
          "explícita que a participação e as respostas não têm qualquer "
          "consequência no tratamento, na permanência no internamento ou na "
          "relação com a equipa clínica, e que o estudo não faz juízo sobre "
          "as práticas do doente. A entrevista é feita num espaço tão "
          "reservado quanto a enfermaria permitir. Os questionários usam "
          "apenas códigos; a lista que liga o código ao número do processo "
          "fica guardada à parte, em caixa com cadeado, só serve para "
          "evitar inclusões repetidas e para a referenciação, e é destruída "
          "no fim do estudo. Os resultados são apresentados apenas de forma "
          "agregada. O risco é mínimo, limitado ao tempo da entrevista, e o "
          "benefício directo é o aconselhamento sobre o uso seguro de "
          "plantas com os anti-hipertensores."),
        P("Existe uma via de referenciação definida. Se a entrevista revelar "
          "que o doente reduziu ou suspendeu o anti-hipertensor, ou usa uma "
          "combinação que a lista de referência da equipa indique como "
          "interacção demonstrada em humanos, o entrevistador aconselha a "
          "não suspender o medicamento e, com o acordo do doente, informa "
          "no mesmo dia o clínico responsável, com nota escrita. Se uma "
          "combinação de categoria 1 só for identificada depois da "
          "classificação, já com o doente de alta, e este o tiver "
          "autorizado no consentimento, o investigador informa o clínico "
          "assistente através da direcção do departamento."),
        P("O conhecimento tradicional é tratado com respeito: as receitas e "
          "combinações descritas por doentes, vendedores ou praticantes não "
          "são divulgadas de forma individual nem usadas para fins "
          "comerciais, os praticantes que colaborem na recolha de "
          "exemplares dão consentimento prévio informado, e as colheitas "
          "limitam-se ao material necessário, com autorização de quem "
          "cultiva a planta e licença de colheita, se exigida [confirmar "
          "junto dos serviços provinciais de florestas]."),
    ]),
]
RESULTADOS_ESPERADOS = [
    P("Os resultados esperados seguem a ordem dos objectivos específicos, "
      "sem antecipar valores."),
    LISTA([
        "Objectivo 1: estimativa da proporção de doentes internados com uso "
        "concomitante nos 30 dias anteriores à admissão, que se espera "
        "próxima dos valores observados em hipertensos internados na "
        "Tanzânia e em ambulatório de cardiologia na África "
        "{liwa2017,lassale2022}, e que dimensiona a necessidade de "
        "perguntar pelo uso na admissão de cada doente hipertenso.",
        "Objectivo 2: lista das espécies e preparações usadas, com nome "
        "vernáculo, nome aceite, nível de identificação e número de "
        "voucher, motivos, fontes, custo e proporção de utilizadores que "
        "reduziu ou suspendeu o anti-hipertensor, mistura previsível de "
        "plantas alimentares cultivadas e de espécies nativas de mercado, "
        "estas com maior dificuldade de identificação, servindo de "
        "referência para o Departamento de Farmácia do HCN.",
        "Objectivo 3: proporção de utilizadores que revelaram o uso e de "
        "doentes a quem foi perguntado, esperada baixa como nos estudos "
        "africanos com hipertensos {james2018,asfaw2016}, resultado que "
        "sustenta a inclusão da pergunta na anamnese farmacêutica "
        "hospitalar.",
        "Objectivo 4: tabela de combinações por categoria de potencial de "
        "interacção, esperando-se muitas sem informação ou só com evidência "
        "laboratorial {nyirenda2025,nurfaradilla2020,alam2021} e um número "
        "menor com interacção demonstrada em humanos, o que orienta o "
        "aconselhamento e a farmacovigilância.",
        "Objectivo 5: razão de prevalências ajustada para a gravidade do "
        "internamento, a escolaridade e o tempo desde o diagnóstico; "
        "espera-se, com base na associação já descrita com a hipertensão "
        "complicada {lassale2022}, maior uso concomitante nos doentes "
        "internados por complicação, embora com poder limitado, o que "
        "indica os doentes a quem dirigir a pergunta e o aconselhamento com "
        "prioridade.",
    ]),
]
DIVULGACAO = [
    P("Os resultados serão apresentados na defesa pública do trabalho na "
      "Faculdade de Ciências de Saúde da Universidade Lúrio e num relatório "
      "escrito entregue à Direcção Clínica do HCN, à direcção dos "
      "Departamentos de Medicina I e II e ao Departamento de Farmácia, com a "
      "proposta de uma pergunta padronizada sobre plantas para a ficha de "
      "admissão e a reconciliação terapêutica. A lista de espécies "
      "identificadas, com os números de voucher, será partilhada com o "
      "herbário de depósito. Prevê-se a submissão de um artigo a uma "
      "revista com revisão por pares e a apresentação em jornadas "
      "científicas. A devolução à comunidade inclui um folheto em "
      "português e emakhuwa, distribuído no internamento e na consulta "
      "externa de hipertensão, que convida doentes e famílias a falar das "
      "plantas que usam ao farmacêutico e ao clínico, e uma sessão com "
      "associações de praticantes de medicina tradicional para apresentar "
      "os resultados agregados."),
]
CRONOGRAMA_TEXTO = [
    P("O [[quadro:cronograma]] distribui as actividades pelos 12 meses do "
      "estudo, de Outubro de 2026 a Setembro de 2027. O pré-teste decorre em "
      "Fevereiro, depois da aprovação ética; as entrevistas aos doentes "
      "internados estão planeadas para quatro meses, com possibilidade de "
      "prolongamento até Agosto se o número de internamentos elegíveis for "
      "menor do que o cenário central assumido; a classificação do "
      "potencial de interacção prolonga-se até Agosto, à medida que as "
      "espécies são confirmadas, e a defesa está prevista para Setembro de "
      "2027."),
]
CRONOGRAMA = {
    "inicio": (2026, 10),
    "n_meses": 12,
    "actividades": [
        ("Revisão da literatura e redacção do protocolo", [1, 2]),
        ("Submissão ao CIBS-UniLúrio e pedidos de autorização no HCN", [3]),
        ("Painel de peritos, tradução e retroversão do questionário", [3, 4]),
        ("Formação da equipa, pré-teste e teste-reteste", [5]),
        ("Entrevistas aos doentes internados e verificação dos processos",
         [6, 7, 8, 9]),
        ("Recolha e identificação dos exemplares botânicos",
         [7, 8, 9, 10]),
        ("Classificação do potencial de interacção", [8, 9, 10, 11]),
        ("Dupla digitação, limpeza e processamento", [7, 8, 9, 10]),
        ("Análise estatística", [10, 11]),
        ("Redacção do relatório final", [10, 11]),
        ("Revisão pelo orientador e entrega", [11]),
        ("Defesa pública e devolução dos resultados", [12]),
    ],
}
ORCAMENTO_TEXTO = [
    P("A [[tabela:orcamento]] apresenta o orçamento estimado, em meticais. O "
      "estudo será financiado com recursos próprios do estudante, "
      "complementados por apoio a solicitar à Universidade Lúrio. A rubrica "
      "maior é o subsídio do inquiridor assistente, que entrevista em "
      "emakhuwa nos cerca de 90 dias úteis previstos para a recolha nos "
      "Departamentos de Medicina I e II e nos 5 dias do pré-teste; "
      "seguem-se as fotocópias para os 205 participantes da amostra mais "
      "cerca de 20 do pré-teste, num total de 225 arredondado para 235 por "
      "margem de segurança, e as rubricas botânicas: saídas de campo, "
      "material de herbário, compra de amostras, envio dos exemplares e "
      "apoio aos dois identificadores."),
]
ORCAMENTO = [
    ("Fotocópias de questionários, fichas e termos (12 páginas por "
     "participante)", "página", 2820, 3),
    ("Tradução para emakhuwa e retroversão (dois tradutores em cada "
     "sentido)", "serviço", 4, 2500),
    ("Comunicação com o painel de peritos", "perito", 6, 500),
    ("Formação da equipa de campo", "dia", 3, 1000),
    ("Subsídio do inquiridor assistente", "dia", 95, 450),
    ("Saídas de campo para recolha de exemplares", "saída", 6, 1500),
    ("Compra de amostras de plantas em mercados", "amostra", 30, 100),
    ("Material de herbário (prensa, papel absorvente, etiquetas, sacos)",
     "conjunto", 1, 4000),
    ("Envio de exemplares e depósito de vouchers no herbário", "envio", 2,
     3000),
    ("Apoio aos identificadores botânicos", "identificador", 2, 3000),
    ("Comunicação telefónica (reentrevistas, teste-reteste, contactos)",
     "mês", 8, 500),
    ("Material de escritório (pranchetas, canetas, almofadas de tinta, "
     "envelopes)", "conjunto", 1, 2500),
    ("Caixa com cadeado para arquivo dos termos e da lista de códigos",
     "unidade", 1, 1500),
    ("Disco externo para cópia de segurança encriptada", "unidade", 1, 2000),
    ("Taxa de submissão ao comité de bioética", "taxa", 1, 5000),
    ("Folhetos de devolução em português e emakhuwa", "unidade", 500, 10),
    ("Impressão e encadernação do relatório final", "exemplar", 4, 800),
]
ORCAMENTO_IMPREVISTOS = 0.10
APENDICES = [
    ("Questionário de recolha de dados", [
        NOTA("Instruções ao entrevistador: aplicar apenas depois da "
             "assinatura do consentimento, e depois de confirmar que o "
             "doente tem capacidade para responder (orientação na pessoa e "
             "no tempo, discurso compreensível). Aplicar num espaço tão "
             "reservado quanto a enfermaria permitir, em português ou "
             "emakhuwa, conforme a preferência do participante, sem "
             "interferir com os cuidados clínicos. Ler as perguntas tal como "
             "estão escritas, sem sugerir respostas e sem comentar as "
             "práticas do participante. Registar os nomes das plantas "
             "exactamente como são ditos. Não escrever o nome do "
             "participante em nenhuma folha."),
        H3("Secção I. Identificação"),
        CAMPO("Código do participante: __________     Data da entrevista: "
              "___/___/2027     Entrevistador: __________"),
        PERG("Departamento de internamento:", ["Medicina I", "Medicina II"]),
        CAMPO("Data de admissão: ___/___/2027     N.º de dias entre a "
              "admissão e a entrevista: ______"),
        PERG("Língua da entrevista:", ["Português", "Emakhuwa"]),
        H3("Secção II. Dados sociodemográficos"),
        PERG("Idade em anos completos:"),
        PERG("Sexo:", ["Masculino", "Feminino"]),
        PERG("Estado civil:", ["Solteiro(a)", "Casado(a) ou em união de facto",
                               "Separado(a), divorciado(a) ou viúvo(a)"]),
        PERG("Escolaridade concluída:", ["Nenhuma", "Primária", "Secundária",
                                         "Superior"]),
        PERG("Ocupação principal:", ["Emprego formal", "Conta própria ou "
                                     "comércio", "Agricultura", "Sem ocupação",
                                     "Outra"]),
        PERG("Tem rendimento regular todos os meses?", ["Sim", "Não"]),
        PERG("Bairro de residência:"),
        H3("Secção III. Dados clínicos e terapêuticos (confirmar no "
           "processo)"),
        PERG("Motivo do internamento actual, pelo diagnóstico de admissão:",
             ["Hipertensão sem complicação confirmada (incluindo crise "
              "hipertensiva sem lesão de órgão-alvo documentada)",
              "Complicação hipertensiva com lesão de órgão-alvo (qual? "
              "AVC; insuficiência cardíaca; lesão renal; encefalopatia "
              "hipertensiva; outra) __________"]),
        PERG("Ano do diagnóstico de hipertensão arterial: ________"),
        PERG("Tem outra doença crónica diagnosticada (comorbilidade)?",
             ["Não", "Sim, diabetes mellitus", "Sim, infecção pelo HIV",
              "Sim, outra (qual?) __________"]),
        CAMPO("Anti-hipertensores que tomava antes da admissão (nome, dose, "
              "vezes por dia): 1. ______________ 2. ______________ "
              "3. ______________ 4. ______________ 5. ______________"),
        PERG("Como acha que estava controlada a sua tensão antes deste "
             "internamento?",
             ["Bem controlada", "Mais ou menos", "Mal controlada"]),
        PERG("Nos últimos 3 meses, alguma vez faltou o seu anti-hipertensor "
             "na farmácia da unidade sanitária onde é seguido?",
             ["Sim", "Não"]),
        H3("Secção IV. Uso de plantas medicinais e preparações "
           "tradicionais"),
        NOTA("Ler antes das perguntas: «Muitas pessoas com tensão alta usam "
             "também plantas, chás, raízes, cascas, pós ou remédios "
             "tradicionais, comprados, recebidos ou preparados em casa. "
             "Queremos saber como é consigo. Não há respostas certas nem "
             "erradas, e a sua resposta não muda nada no seu tratamento "
             "aqui no hospital.» Não contam os alimentos comidos só como "
             "comida."),
        PERG("Nos últimos 12 meses, consultou algum praticante de medicina "
             "tradicional?", ["Sim", "Não"]),
        PERG("Nos últimos 12 meses, usou alguma planta, chá, raiz, casca, pó, "
             "mistura ou remédio tradicional para a sua saúde?",
             ["Sim", "Não (passar à Secção VI)"]),
        PERG("Nos 30 dias antes de ser internado, usou alguma dessas plantas "
             "ou remédios?", ["Sim", "Não"]),
        PERG("Por que razão usa plantas além dos anti-hipertensores? (pode "
             "marcar mais de uma)",
             ["Acha que as plantas tratam ou curam a tensão alta",
              "Os medicamentos não chegam para controlar a tensão",
              "Efeitos incómodos dos medicamentos",
              "Falta do medicamento na unidade", "Custo",
              "Conselho da família ou de amigos", "Tradição da família",
              "Outra (qual?) __________"]),
        H3("Secção V. Ficha de cada planta ou preparação (repetir até "
           "cinco)"),
        NOTA("Uma ficha por planta ou preparação usada nos últimos 12 meses, "
             "começando pelas dos últimos 30 dias. Se for uma mistura, "
             "registar os componentes que o participante conheça."),
        CAMPO("Planta n.º ___   Nome em emakhuwa: ______________   Nome em "
              "português: ______________   Outro nome: ______________"),
        PERG("Usou esta planta nos últimos 30 dias?", ["Sim", "Não"]),
        PERG("Parte usada:", ["Raiz", "Casca", "Folha", "Fruto ou semente",
                              "Flor", "Planta inteira",
                              "Não sabe (produto já preparado)"]),
        PERG("Forma de preparação:", ["Fervida (decocção)", "Chá (infusão)",
                                      "Em água fria (maceração)", "Pó",
                                      "Sumo ou fresca", "Mistura já preparada",
                                      "Produto embalado", "Outra"]),
        PERG("Como usa:", ["Bebe ou come", "Aplica na pele", "Banho",
                           "Vapor ou inalação", "Outra"]),
        PERG("Com que frequência:", ["Todos os dias", "Algumas vezes por "
                                     "semana", "De vez em quando"]),
        PERG("Há quantos meses usa esta planta? ______"),
        PERG("Para que usa (pode marcar mais de uma):",
             ["Tratar a hipertensão", "Aliviar efeitos dos "
              "anti-hipertensores", "Outro problema de saúde",
              "Reforçar o organismo", "Problema espiritual ou de "
              "protecção", "Outro"]),
        PERG("Onde obtém:", ["Praticante de medicina tradicional",
                             "Mercado ou vendedor", "Cultiva em casa",
                             "Colhe no mato", "Familiar ou vizinho",
                             "Farmácia ou ervanária", "Outro"]),
        PERG("Quem lhe recomendou:", ["Família ou amigos", "Praticante",
                                      "Outro doente", "Profissional de saúde",
                                      "Rádio, televisão ou redes sociais",
                                      "Ninguém (iniciativa própria)"]),
        PERG("Quanto gasta por mês com esta planta (meticais)? ______"),
        PERG("Toma a planta à mesma hora dos anti-hipertensores?",
             ["Sim", "Não", "Às vezes"]),
        PERG("Tem o produto consigo, ou pode trazê-lo na próxima visita para "
             "ser fotografado?", ["Tem consigo", "Pode trazer", "Não"]),
        H3("Secção VI. Comunicação com os profissionais de saúde"),
        PERG("Nos últimos 12 meses, algum profissional de saúde lhe perguntou "
             "se usava plantas ou remédios tradicionais?",
             ["Sim", "Não", "Não se lembra"]),
        PERG("Se sim, quem perguntou (pode marcar mais de um):",
             ["Clínico ou médico", "Enfermeiro",
              "Farmacêutico ou técnico de farmácia", "Outro"]),
        NOTA("As perguntas seguintes aplicam-se só a quem usou plantas nos "
             "últimos 12 meses."),
        PERG("Nos últimos 12 meses, contou a algum profissional de saúde que "
             "usa plantas?",
             ["Sim, por iniciativa própria", "Sim, porque lhe perguntaram",
              "Não"]),
        PERG("Se contou, a quem:", ["Clínico ou médico", "Enfermeiro",
                                    "Farmacêutico ou técnico de farmácia",
                                    "Outro"]),
        PERG("Se contou, o que fez o profissional:",
             ["Aconselhou a continuar", "Aconselhou a parar",
              "Não disse nada", "Criticou", "Outro"]),
        PERG("Se não contou, porquê? (pode marcar mais de uma)",
             ["Ninguém perguntou", "Receio de ser criticado ou mal atendido",
              "Achou que não era importante",
              "Acha que o profissional não conhece plantas",
              "Não houve tempo na consulta", "Acha que as plantas são seguras",
              "O praticante disse para não contar", "Outra"]),
        PERG("(Todos os participantes) Acha que tomar plantas junto com os "
             "anti-hipertensores pode fazer mal?", ["Sim", "Não", "Não sabe"]),
        H3("Secção VII. Alterações do tratamento anti-hipertensor"),
        NOTA("Só para quem usou plantas nos últimos 12 meses; os restantes "
             "passam à Secção VIII."),
        PERG("Nos últimos 12 meses, deixou de tomar ou reduziu algum "
             "anti-hipertensor por estar a usar plantas?",
             ["Sim (qual e durante quanto tempo?) __________", "Não"]),
        PERG("Teve algum problema de saúde que atribui a tomar plantas com os "
             "anti-hipertensores?", ["Sim (qual?) __________", "Não"]),
        NOTA("Se o participante reduziu ou suspendeu o anti-hipertensor, ou "
             "usa uma combinação que conste da lista de referência como "
             "interacção demonstrada em humanos, aplicar o protocolo de "
             "referenciação: aconselhar a não suspender e a informar o "
             "clínico assistente e, com o acordo do doente, encaminhar no "
             "mesmo dia com nota escrita."),
        H3("Secção VIII. Verificação do processo clínico (entrevistador)"),
        CAMPO("Diagnóstico de admissão: ______________   Gravidade "
              "(sem/com complicação): ______________   Data do diagnóstico "
              "de hipertensão: ___/______   Comorbilidades registadas: "
              "______________"),
        CAMPO("Anti-hipertensores prescritos (nome, dose, frequência): "
              "1. ______________ 2. ______________ 3. ______________ "
              "4. ______________ 5. ______________"),
        PERG("Existe menção ao uso de medicina tradicional no processo?",
             ["Sim", "Não"]),
        PERG("Encaminhamento ao clínico assistente feito hoje?",
             ["Sim (motivo) __________", "Não"]),
    ]),
    ("Fichas de identificação botânica e de classificação do potencial de "
     "interacção", [
        H3("Parte 1. Ficha de identificação botânica (uma por exemplar)"),
        CAMPO("N.º de colheita: ______   Data: ___/___/2027   Colector: "
              "______________"),
        CAMPO("Nome vernáculo em emakhuwa: ______________   Em português: "
              "______________"),
        PERG("Origem do exemplar:", ["Mercado (vendedor)", "Cultivo de "
                                     "participante", "Praticante de medicina "
                                     "tradicional", "Outra"]),
        CAMPO("Local: ______________   Coordenadas: __________ / __________"),
        PERG("Estado do material:", ["Fértil (flor ou fruto)", "Estéril",
                                     "Produto seco ou fragmentado"]),
        CAMPO("Números das fotografias: ______________"),
        CAMPO("Identificador 1, espécie proposta: ______________   "
              "Identificador 2, espécie proposta: ______________"),
        PERG("Concordância entre identificadores:",
             ["Sim", "Não (resolvido por consenso ou terceiro especialista)"]),
        CAMPO("Nome aceite e autoridade: ______________   Família: "
              "______________"),
        CAMPO("Fonte da nomenclatura e data de consulta: ______________   "
              "N.º de voucher e herbário: ______________"),
        PERG("Nível de identificação:",
             ["1. Exemplar com voucher", "2. Fotografia diagnóstica",
              "3. Atribuição provisória pela literatura", "4. Não "
              "identificada"]),
        PERG("Nome vernáculo polissémico (designa mais de uma espécie)?",
             ["Sim", "Não"]),
        H3("Parte 2. Ficha de classificação do potencial de interacção (uma "
           "por combinação)"),
        CAMPO("Código da combinação: ______   Espécie (nome aceite): "
              "______________   Nível de identificação: ___"),
        CAMPO("Anti-hipertensor e classe: ______________   Forma de "
              "preparação usada pelo doente: ______________"),
        CAMPO("Fontes consultadas e resultado: monografia da OMS "
              "__________; PubMed (data e estratégia) __________; estudo "
              "farmacocinético ou farmacodinâmico específico __________; "
              "outra base de acesso livre __________"),
        PERG("Categoria:", ["1. Interacção demonstrada em humanos",
                            "2. Potencial descrito sem demonstração em "
                            "humanos",
                            "3. Estudada em humanos sem interacção relevante",
                            "4. Sem informação", "5. Não avaliável"]),
        PERG("Mecanismo:", ["Farmacocinético", "Farmacodinâmico",
                            "Desconhecido"]),
        PERG("Direcção:", ["Aumento do efeito do anti-hipertensor "
                           "(hipotensão aditiva)",
                           "Redução do efeito do anti-hipertensor",
                           "Distúrbio electrolítico ou outra toxicidade "
                           "aditiva", "Não se aplica"]),
        CAMPO("Avaliador (1 ou 2): ___   Data: ___/___/2027"),
        H3("Parte 3. Consentimento prévio de colaboradores na recolha de "
           "exemplares"),
        P("Eu, abaixo identificado(a), aceito indicar ou fornecer exemplares "
          "de plantas ao estudo, fui informado(a) de que o conhecimento que "
          "partilho não será divulgado de forma individual nem usado para fins "
          "comerciais e de que posso retirar a minha colaboração a qualquer "
          "momento."),
        CAMPO("Nome ou código: ______________   Assinatura ou impressão "
              "digital: ______________   Data: ___/___/2027"),
        PERG("Deseja ser reconhecido(a) pelo nome no relatório?",
             ["Sim", "Não"]),
    ]),
    ("Folha de informação ao participante", [
        P("Título do estudo: Uso concomitante de plantas medicinais e "
          "potencial de interacção com anti-hipertensores em doentes "
          "internados nos Departamentos de Medicina I e II, Hospital "
          "Central de Nampula. Investigador: estudante finalista da "
          "Licenciatura em Farmácia da Faculdade de Ciências de Saúde da "
          "Universidade Lúrio, sob orientação de um docente da mesma "
          "faculdade."),
        P("Estamos a convidá-lo(a) a participar num estudo que quer saber se "
          "as pessoas internadas por tensão alta usam plantas ou remédios "
          "tradicionais junto com os medicamentos para a tensão, porquê, e "
          "se falam disso com os profissionais de saúde. Esta informação vai "
          "ajudar os farmacêuticos e os clínicos deste hospital a aconselhar "
          "melhor os doentes."),
        P("Se aceitar, faremos uma entrevista de 30 a 40 minutos, num "
          "momento e num lugar que não atrapalhem o seu tratamento, e "
          "consultaremos o seu processo clínico para confirmar o diagnóstico "
          "e os medicamentos. Se quiser, poderá mostrar a planta ou o "
          "produto que usa para ser fotografado. Algumas pessoas poderão ser "
          "contactadas por telefone, se o autorizarem, para repetir algumas "
          "perguntas depois da alta."),
        P("A participação é voluntária. Pode recusar ou desistir a qualquer "
          "momento. A sua participação e as suas respostas não têm nenhuma "
          "consequência no seu tratamento, na sua permanência no hospital ou "
          "na relação com a equipa que o(a) trata. Não há respostas certas "
          "nem erradas, e ninguém vai julgar as suas práticas. O seu nome "
          "não será escrito no questionário, e os resultados serão "
          "apresentados só em conjunto."),
        P("O único incómodo previsto é o tempo da entrevista. Se contar que "
          "deixou de tomar algum anti-hipertensor, ou se usar uma combinação "
          "que possa fazer mal, receberá conselho e, se aceitar, o seu "
          "clínico será informado no mesmo dia. Se mais tarde for "
          "identificada uma combinação com risco conhecido, já depois da "
          "alta, o clínico poderá ser informado, apenas se o autorizar no "
          "termo de consentimento."),
        CAMPO("Contactos: estudante [preencher]; orientador(a) [preencher]; "
              "CIBS-UniLúrio [preencher]"),
    ]),
    ("Termo de consentimento livre e esclarecido", [
        P("Declaro que li, ou que me foi lida numa língua que compreendo, a "
          "folha de informação sobre este estudo, que pude fazer perguntas e "
          "que as minhas dúvidas foram esclarecidas. Compreendo que a "
          "participação é voluntária, que posso desistir a qualquer momento e "
          "que a minha decisão não tem consequências no meu tratamento. "
          "Aceito participar."),
        PERG("Autorizo a consulta do meu processo clínico:", ["Sim", "Não"]),
        PERG("Autorizo a fotografia da planta ou do produto que uso:",
             ["Sim", "Não"]),
        PERG("Autorizo que me contactem por telefone para repetir algumas "
             "perguntas:", ["Sim", "Não"]),
        PERG("Autorizo que o meu clínico assistente seja informado se for "
             "identificada uma combinação com risco conhecido:",
             ["Sim", "Não"]),
        CAMPO("Código do participante: __________   Data: ___/___/2027"),
        CAMPO("Assinatura do participante: ____________________   ou "
              "impressão digital: [          ]"),
        NOTA("Para participantes que não sabem ler: a testemunha imparcial "
             "confirma que a folha de informação foi lida na íntegra e que o "
             "participante consentiu livremente."),
        CAMPO("Nome e assinatura da testemunha: ____________________"),
        CAMPO("Nome e assinatura do entrevistador: ____________________"),
    ]),
    ("Pedido de autorização institucional", [
        P("Ex.mo(a) Senhor(a) Director(a) [Clínico(a) do Hospital Central de "
          "Nampula, ou Chefe do Departamento de Medicina I ou II]:"),
        P("Eu, estudante finalista da Licenciatura em Farmácia da Faculdade de "
          "Ciências de Saúde da Universidade Lúrio, venho solicitar "
          "autorização para realizar o estudo intitulado «Uso concomitante "
          "de plantas medicinais e potencial de interacção com "
          "anti-hipertensores em doentes internados nos Departamentos de "
          "Medicina I e II, Hospital Central de Nampula, 2027», junto dos "
          "doentes internados por hipertensão arterial ou por complicação "
          "hipertensiva, de 1 de Março a 30 de Junho de 2027, com "
          "possibilidade de prolongamento até 31 de Agosto de 2027."),
        P("O estudo inclui entrevistas a doentes adultos internados que "
          "consintam em participar e a consulta dos respectivos processos "
          "clínicos, sem interferir nos cuidados clínicos nem na "
          "organização das enfermarias. Os dados serão confidenciais e "
          "apresentados apenas de forma agregada, e o estudo só começará "
          "depois da aprovação do CIBS-UniLúrio, cuja cópia será anexada. Os "
          "resultados serão entregues a esta instituição num relatório "
          "escrito."),
        CAMPO("Nampula, ___ de __________ de 2026"),
        CAMPO("O(A) estudante: ____________________   O(A) orientador(a): "
              "____________________"),
    ]),
]
