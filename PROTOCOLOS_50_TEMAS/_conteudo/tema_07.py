# -*- coding: utf-8 -*-
"""
Tema 07: Prescricao de antibioticos em criancas menores de cinco anos
atendidas nos centros de saude publicos da cidade de Nampula
(Farmacoepidemiologia e Uso Racional de Medicamentos). Estudo documental
retrospectivo, dados de 2026, recolha em 2027. Classificacao AWaRe da OMS e
adequacao as normas nacionais de AIDI.

Compor e validar:   python _motor/motor.py _conteudo/tema_07.py
Verificar fontes:   python _motor/refs.py verificar _conteudo/tema_07.py
"""
from blocos import (CAMPO, FORMULA, H3, LISTA, NOTA, P, PERG, QUADRO,
                    TABELA)

NUMERO = 7
SLUG = "Prescricao_Antibioticos_Menores_Cinco_Anos_Nampula"
TITULO = ("Prescrição de antibióticos e adequação às normas nacionais em "
          "crianças menores de cinco anos atendidas nos centros de saúde "
          "públicos da cidade de Nampula, 2026")
DESENHO = ("Transversal retrospectivo, descritivo e analítico, documental "
           "(livros de registo da consulta da criança doente e receitas)")

AUTOR = "[Nome do(a) estudante]"
ORIENTADOR = "[Nome e grau académico do(a) orientador(a)]"

# ---------------------------------------------------------------- resumo --
RESUMO = (
    "A prescrição de antibióticos a crianças menores de cinco anos com "
    "infecções respiratórias, diarreia ou febre é frequente nos cuidados de "
    "saúde primários da África subsariana e excede muitas vezes as "
    "indicações das normas clínicas, com risco de efeitos adversos e de "
    "resistência aos antimicrobianos. Em Nampula, a "
    "evidência disponível provém de crianças internadas no hospital de "
    "referência e não se encontrou nenhum estudo publicado sobre a "
    "prescrição de antibióticos nos centros de saúde da cidade. O estudo tem "
    "como objectivo avaliar a prescrição de antibióticos em crianças menores "
    "de cinco anos atendidas nas consultas da criança doente dos centros de "
    "saúde públicos da cidade de Nampula, quanto à frequência, ao perfil "
    "segundo a classificação Acesso, Vigilância e Reserva da Organização "
    "Mundial da Saúde e à adequação às normas nacionais de atenção integrada "
    "às doenças da infância. Trata-se de um estudo transversal, "
    "retrospectivo, descritivo e analítico, de base documental, que abrange "
    "as consultas realizadas de 1 de Janeiro a 31 de Dezembro de 2026, com "
    "recolha de dados em 2027. Serão analisadas 643 consultas, "
    "seleccionadas por amostragem sistemática estratificada por centro de "
    "saúde, com alocação proporcional ao volume anual. Os dados serão "
    "extraídos dos livros de registo e das receitas para uma ficha "
    "estruturada sem identificadores, com dupla extracção de uma parte dos "
    "registos, e a adequação será classificada por dois avaliadores "
    "independentes, com medição da concordância. A análise incluirá "
    "proporções com intervalos de confiança a 95%, o teste do qui-quadrado e "
    "a regressão logística multinível, com nível de significância de 5%. "
    "Espera-se uma proporção elevada de consultas com antibiótico, sobretudo "
    "nas infecções respiratórias altas e na diarreia sem sangue, e um "
    "predomínio de antibióticos do grupo Acesso. Os resultados apoiarão a "
    "supervisão clínica, a formação dos prescritores e a gestão de "
    "antimicrobianos na cidade.")
PALAVRAS_CHAVE = ["antibacterianos", "criança", "Moçambique",
                  "prescrições de medicamentos",
                  "uso racional de medicamentos"]
ABSTRACT = (
    "Antibiotic prescribing for children under five years of age with "
    "respiratory infections, diarrhoea or fever is common in primary health "
    "care in sub-Saharan Africa and often exceeds the indications of "
    "clinical guidelines, with a risk of adverse effects and of "
    "antimicrobial resistance. In Nampula, the available "
    "evidence comes from children admitted to the referral hospital, and no "
    "published study was found on antibiotic prescribing in the city's "
    "health centres. The study aims to assess antibiotic prescribing for "
    "children under five years of age seen at the sick child consultations "
    "of the public health centres of Nampula city, regarding its frequency, "
    "its profile according to the World Health Organization Access, Watch "
    "and Reserve classification, and its appropriateness to the national "
    "guidelines for the integrated management of childhood illness. This is "
    "a cross-sectional, retrospective, descriptive and analytical "
    "record-based study covering consultations held from 1 January to 31 "
    "December 2026, with data collection in 2027. A total of 643 "
    "consultations will be analysed, selected by systematic sampling "
    "stratified by health centre, with allocation proportional to the "
    "annual volume. Data will be extracted from the registers and "
    "prescriptions into a structured form without identifiers, with double "
    "extraction of part of the records, and appropriateness will be "
    "classified by two independent raters, with measurement of agreement. "
    "The analysis will include proportions with 95% confidence intervals, "
    "the chi-square test and multilevel logistic regression, with a 5% "
    "significance level. A high proportion of consultations with an "
    "antibiotic is expected, especially for upper respiratory infections "
    "and non-bloody diarrhoea, together with a predominance of Access group "
    "antibiotics. The results will support clinical supervision, prescriber "
    "training and antimicrobial stewardship in the city.")
KEYWORDS = ["anti-bacterial agents", "child", "drug prescriptions",
            "Mozambique", "rational drug use"]

# Só as siglas efectivamente usadas no texto; forma extensa na 1.ª ocorrência.
ABREVIATURAS = [
    ("AIDI", "Atenção Integrada às Doenças da Infância"),
    ("ATC", "classificação Anatómica Terapêutica Química"),
    ("AWaRe", "Access, Watch, Reserve (grupos Acesso, Vigilância e "
              "Reserva da classificação de antibióticos da Organização "
              "Mundial da Saúde)"),
    ("CIBS-UniLúrio", "Comité Institucional de Bioética para a Saúde da "
                      "Universidade Lúrio"),
    ("CNBS", "Comité Nacional de Bioética para a Saúde"),
    ("DCI", "denominação comum internacional"),
    ("DPS", "Direcção Provincial de Saúde"),
    ("FCS", "Faculdade de Ciências de Saúde"),
    ("CCI", "coeficiente de correlação intraclasse"),
    ("DEFF", "efeito de desenho (do inglês design effect)"),
    ("IC", "intervalo de confiança"),
    ("IDS", "Inquérito Demográfico e de Saúde"),
    ("LNME", "Lista Nacional de Medicamentos Essenciais"),
    ("MISAU", "Ministério da Saúde"),
    ("OMS", "Organização Mundial da Saúde"),
    ("OR", "odds ratio"),
    ("ORa", "odds ratio ajustado"),
    ("RAM", "resistência aos antimicrobianos"),
    ("RECORD-PE", "REporting of studies Conducted using Observational "
                  "Routinely-collected health Data, extensão para a "
                  "farmacoepidemiologia"),
    ("SDSMAS", "Serviço Distrital de Saúde, Mulher e Acção Social"),
    ("SPSS", "Statistical Package for the Social Sciences"),
    ("STROBE", "Strengthening the Reporting of Observational Studies in "
               "Epidemiology"),
    ("TDR", "teste de diagnóstico rápido da malária"),
]

# ------------------------------------------------------------ referencias --
FONTES = {
    # ---- resistencia e uso de antibioticos: global
    "gbd2024": "GBD 2021 Antimicrobial Resistance Collaborators. Global burden of bacterial antimicrobial resistance 1990-2021: a systematic analysis with forecasts to 2050. Lancet. 2024;404(10459):1199-1226. doi:10.1016/S0140-6736(24)01867-1. PMID: 39299261.",
    "omsunga2024": "World Health Organization. World leaders commit to decisive action on antimicrobial resistance [Internet]. Geneva: World Health Organization; 2024 [citado 2026 Set 19]. Disponível em: https://www.who.int/news/item/26-09-2024-world-leaders-commit-to-decisive-action-on-antimicrobial-resistance",
    "sulis2020": "Sulis G, Adam P, Nafade V, Gore G, Daniels B, Daftary A, et al. Antibiotic prescription practices in primary care in low- and middle-income countries: A systematic review and meta-analysis. PLoS Med. 2020;17(6):e1003139. doi:10.1371/journal.pmed.1003139. PMID: 32544153.",
    "allwellbrown2020": "Allwell-Brown G, Hussain-Alkhateeb L, Kitutu FE, Strömdahl S, Mårtensson A, Johansson EW. Trends in reported antibiotic use among children under 5 years of age with fever, diarrhoea, or cough with fast or difficult breathing across low-income and middle-income countries in 2005-17: a systematic analysis of 132 national surveys from 73 countries. Lancet Glob Health. 2020;8(6):e799-e807. doi:10.1016/S2214-109X(20)30079-6. PMID: 32446345.",
    "fink2020": "Fink G, D'Acremont V, Leslie HH, Cohen J. Antibiotic exposure among children younger than 5 years in low-income and middle-income countries: a cross-sectional study of nationally representative facility-based and household-based surveys. Lancet Infect Dis. 2020;20(2):179-187. doi:10.1016/S1473-3099(19)30572-9. PMID: 31843383.",
    "rogawski2017": "Rogawski ET, Platts-Mills JA, Seidman JC, John S, Mahfuz M, Ulak M, et al. Use of antibiotics in children younger than two years in eight countries: a prospective cohort study. Bull World Health Organ. 2017;95(1):49-61. doi:10.2471/BLT.16.176123. PMID: 28053364.",
    "hopkins2017": "Hopkins H, Bruxvoort KJ, Cairns ME, Chandler CI, Leurent B, Ansah EK, et al. Impact of introduction of rapid diagnostic tests for malaria on antibiotic prescribing: analysis of observational and randomised studies in public and private healthcare settings. BMJ. 2017;356:j1054. doi:10.1136/bmj.j1054. PMID: 28356302.",
    "kapitotembo2020": "Kapito-Tembo A, Mathanga D, Bauleni A, Nyirenda O, Pensulo P, Ali D, et al. Prevalence and Clinical Management of Non-malarial Febrile Illnesses among Outpatients in the Era of Universal Malaria Testing in Malawi. Am J Trop Med Hyg. 2020;103(2):887-893. doi:10.4269/ajtmh.18-0800. PMID: 32588795.",
    # ---- AWaRe
    "sharland2022": "Sharland M, Zanichelli V, Ombajo LA, Bazira J, Cappello B, Chitatanga R, et al. The WHO essential medicines list AWaRe book: from a list to a quality improvement system. Clin Microbiol Infect. 2022;28(12):1533-1535. doi:10.1016/j.cmi.2022.08.009. PMID: 36007869.",
    "moja2024": "Moja L, Zanichelli V, Mertz D, Gandra S, Cappello B, Cooke GS, et al. WHO's essential medicines and AWaRe: recommendations on first- and second-choice antibiotics for empiric treatment of clinical infections. Clin Microbiol Infect. 2024;30 Suppl 2:S1-S51. doi:10.1016/j.cmi.2024.02.003. PMID: 38342438.",
    "funiciello2024": "Funiciello E, Lorenzetti G, Cook A, Goelen J, Moore CE, Campbell SM, et al. Identifying AWaRe indicators for appropriate antibiotic use: a narrative review. J Antimicrob Chemother. 2024;79(12):3063-3077. doi:10.1093/jac/dkae370. PMID: 39422368.",
    "omsaware2025": "World Health Organization. The selection and use of essential medicines, 2025: WHO AWaRe (Access, Watch, Reserve) classification of antibiotics for evaluation and monitoring of use [Internet]. Geneva: World Health Organization; 2025 [citado 2026 Set 19]. Disponível em: https://www.who.int/publications/i/item/B09489",
    "omsaware2022": "World Health Organization. The WHO AWaRe (Access, Watch, Reserve) antibiotic book [Internet]. Geneva: World Health Organization; 2022 [citado 2026 Set 19]. Disponível em: https://www.who.int/publications/i/item/9789240062382",
    # ---- normas clinicas da crianca
    "oms2024": "World Health Organization. Guideline on management of pneumonia and diarrhoea in children up to 10 years of age [Internet]. Geneva: World Health Organization; 2024 [citado 2026 Set 19]. Disponível em: https://www.who.int/publications/i/item/9789240103412",
    "kundu2025": "Kundu S, Das S, Medhagopal RG. An Update on WHO Recommendations on Childhood Pneumonia and Diarrhea (2024). Indian Pediatr. 2025;62(10):775-778. doi:10.1007/s13312-025-00173-8. PMID: 40839064.",
    "misau2014": "Ministério da Saúde, Direcção Nacional de Saúde Pública. Atenção Integrada às Doenças da Infância (AIDI): caderno de mapas para a atenção integrada à criança doente de 1 semana aos 2 meses e dos 2 meses aos 5 anos [Internet]. Maputo: Ministério da Saúde; 2014 [citado 2026 Set 19]. Disponível em: https://media.path.org/documents/MOH_IMCI_FLIPCHART_June_2015-PORT.pdf",
    "carai2021": "Carai S, Kuttumuratova A, Boderscova L, Khachatryan H, Lejnev I, Monolbaev K, et al. The integrated management of childhood illness (IMCI) and its potential to reduce the misuse of antibiotics. J Glob Health. 2021;11:04030. doi:10.7189/jogh.11.04030. PMID: 34055327.",
    # ---- estudos africanos em criancas
    "gres2024": "Gres E, Diallo IS, Besnier C, Diakité AA, Zair Z, Ouédraogo Yugbaré S, et al. Antibiotic prescribing practices according to the AWaRe classification among children under 5 of age attending public primary care centres in four West African countries: a cross-sectional study (AIRE project, 2021-2022). BMJ Paediatr Open. 2024;8(1). doi:10.1136/bmjpo-2024-002833. PMID: 39477340.",
    "manirakiza2025": "Manirakiza A, Maru SM, Nyamu DG, Bizimana T, Nimpagaritse M. Antimicrobial prescribing patterns among pediatric outpatient encounters in primary healthcare centers in Bujumbura Mairie, Burundi. BMC Prim Care. 2025;26(1):236. doi:10.1186/s12875-025-02944-5. PMID: 40750850.",
    "okello2020": "Okello N, Oloro J, Kyakwera C, Kumbakumba E, Obua C. Antibiotic prescription practices among prescribers for children under five at public health centers III and IV in Mbarara district. PLoS One. 2020;15(12):e0243868. doi:10.1371/journal.pone.0243868. PMID: 33370280.",
    "mabilika2022": "Mabilika RJ, Shirima G, Mpolya E. Prevalence and Predictors of Antibiotic Prescriptions at Primary Healthcare Facilities in the Dodoma Region, Central Tanzania: A Retrospective, Cross-Sectional Study. Antibiotics (Basel). 2022;11(8). doi:10.3390/antibiotics11081035. PMID: 36009904.",
    "tsige2020": "Tsige AG, Nedi T, Bacha T. Assessment of the Management of Diarrhoea Among Children Under Five in Addis Ababa, Ethiopia. Pediatric Health Med Ther. 2020;11:135-143. doi:10.2147/PHMT.S243513. PMID: 32440249.",
    "awuor2023": "Awuor AO, Ogwel B, Powell H, Verani JR, Sow SO, Hossain MJ, et al. Antibiotic-Prescribing Practices for Management of Childhood Diarrhea in 3 Sub-Saharan African Countries: Findings From the Vaccine Impact on Diarrhea in Africa (VIDA) Study, 2015-2018. Clin Infect Dis. 2023;76(76 Suppl1):S32-S40. doi:10.1093/cid/ciac980. PMID: 37074427.",
    "gelagay2025": "Gelagay AA, Azale T, Gezie LD, Tigabu Z, Alemu K. Correct diagnostic classification and treatment of pneumonia symptoms in under-five children, northwest Ethiopia: a cross-sectional study. BMJ Paediatr Open. 2025;9(1). doi:10.1136/bmjpo-2025-003311. PMID: 40316407.",
    "hooft2021": "Hooft AM, Ndenga B, Mutuku F, Otuka V, Ronga C, Chebii PK, et al. High Frequency of Antibiotic Prescription in Children With Undifferentiated Febrile Illness in Kenya. Clin Infect Dis. 2021;73(7):e2399-e2406. doi:10.1093/cid/ciaa1305. PMID: 32882032.",
    "opoku2020": "Opoku MM, Bonful HA, Koram KA. Antibiotic prescription for febrile outpatients: a health facility-based secondary data analysis for the Greater Accra region of Ghana. BMC Health Serv Res. 2020;20(1):978. doi:10.1186/s12913-020-05771-9. PMID: 33109158.",
    "tan2024": "Tan R, Kavishe G, Luwanda LB, Kulinkina AV, Renggli S, Mangu C, et al. A digital health algorithm to guide antibiotic prescription in pediatric outpatient care: a cluster randomized controlled trial. Nat Med. 2024;30(1):76-84. doi:10.1038/s41591-023-02633-9. PMID: 38110580.",
    "gres2025": "Gres E, Brigadoi G, Zamperetti E, Dramowski A, Dahourou D, Mavoko HM, et al. Antibiotic stewardship and point-of-care testing for children in 25 low-income and lower-middle-income countries: a systematic review and meta-analysis. EClinicalMedicine. 2025;90:103667. doi:10.1016/j.eclinm.2025.103667. PMID: 41377907.",
    # ---- Mocambique e Nampula
    "ids2024": "Instituto Nacional de Estatística; ICF. Inquérito Demográfico e de Saúde em Moçambique 2022-23: relatório definitivo [Internet]. Maputo e Rockville: Instituto Nacional de Estatística e ICF; 2024 [citado 2026 Set 19]. Disponível em: https://dhsprogram.com/pubs/pdf/FR389/FR389.pdf",
    "ine2021": "Instituto Nacional de Estatística. IV Recenseamento Geral da População e Habitação 2017: resultados definitivos, província de Nampula [Internet]. Nampula: Instituto Nacional de Estatística; 2021 [citado 2026 Set 19]. Disponível em: http://www.sina.gov.mz/wp-content/uploads/2024/05/NAMPULA-RESUTADOS-DEFINITIVOS-DO-CENSO-2017.pdf",
    "xavier2022": "Xavier SP, Victor A, Cumaquela G, Vasco MD, Rodrigues OAS. Inappropriate use of antibiotics and its predictors in pediatric patients admitted at the Central Hospital of Nampula, Mozambique. Antimicrob Resist Infect Control. 2022;11(1):79. doi:10.1186/s13756-022-01115-w. PMID: 35655272.",
    "xavier2024": "Xavier SP, da Silva AMC, Victor A. Antibiotic prescribing patterns in pediatric patients using the WHO access, watch, reserve (AWaRe) classification at a quaternary hospital in Nampula, Mozambique. Sci Rep. 2024;14(1):22719. doi:10.1038/s41598-024-72349-4. PMID: 39349590.",
    "salenciaferrao2025": "Salência-Ferrão J, Chissaque A, Manhique-Coutinho L, Kenga AN, Cassocera M, de Deus N. Inappropriate use of antibiotics in the management of diarrhoea in children under five years admitted with acute diarrhoea in four provinces of Mozambique 2014-2019. BMC Infect Dis. 2025;25(1):209. doi:10.1186/s12879-025-10597-z. PMID: 39939844.",
    "machava2022": "Machava NE, Salvador EM, Mulaudzi F. Assessment of diagnosis and treatment practices of diarrhoea in children under five in Maputo-Mozambique. Int J Afr Nurs Sci. 2022;17:100507. doi:10.1016/j.ijans.2022.100507. PMID: 36518099.",
    "faiela2022": "Faiela C, Sevene E. Antibiotic prescription for HIV-positive patients in primary health care in Mozambique: A cross-sectional study. S Afr J Infect Dis. 2022;37(1):340. doi:10.4102/sajid.v37i1.340. PMID: 35284563.",
    "mate2019": "Mate I, Come CE, Gonçalves MP, Cliff J, Gudo ES. Knowledge, attitudes and practices regarding antibiotic use in Maputo City, Mozambique. PLoS One. 2019;14(8):e0221452. doi:10.1371/journal.pone.0221452. PMID: 31437215.",
    "vubil2018": "Vubil D, Balleste-Delpierre C, Mabunda R, Acácio S, Garrine M, Nhampossa T, et al. Antibiotic resistance and molecular characterization of shigella isolates recovered from children aged less than 5 years in Manhiça, Southern Mozambique. Int J Antimicrob Agents. 2018;51(6):881-887. doi:10.1016/j.ijantimicag.2018.02.005. PMID: 29448013.",
    "massinga2021": "Massinga AJ, Garrine M, Messa A Jr, Nobela NA, Boisen N, Massora S, et al. Klebsiella spp. cause severe and fatal disease in Mozambican children: antimicrobial resistance profile and molecular characterization. BMC Infect Dis. 2021;21(1):526. doi:10.1186/s12879-021-06245-x. PMID: 34090384.",
    "misau2019": "Ministério da Saúde; Ministério da Agricultura e Segurança Alimentar. Plano Nacional de Acção Contra a Resistência Antimicrobiana 2019-2023 [Internet]. Maputo: Ministério da Saúde; 2019 [citado 2026 Set 19]. Disponível em: https://cdn.who.int/media/docs/default-source/antimicrobial-resistance/amr-spc-npm/nap-library/nap_20_11_2018---mozambique---2019-2023.pdf",
    "misau2017": "Ministério da Saúde. Lista Nacional de Medicamentos Essenciais [Internet]. Maputo: Ministério da Saúde; 2017 [citado 2026 Set 19]. Disponível em: https://www.afro.who.int/sites/default/files/2018-07/LISTA%20NACIONAL%20DE%20MEDICAMENTOS%20ESSENCIAIS%202017.pdf",
    "lei12de2017": "República de Moçambique. Lei n.º 12/2017, de 8 de Setembro: Lei do medicamento, vacinas e outros produtos biológicos para o uso humano. Boletim da República, I Série, n.º 141 [Internet]. Maputo: Imprensa Nacional de Moçambique; 2017 [citado 2026 Set 19]. Disponível em: https://anarme.gov.mz/download/lei-12-2017-de-8-de-setembro-lei-de-medicamento/",
    "mboane2025": "Mboane N. MISAU lança Formulário de Medicamentos e Lista de diagnósticos. O País [Internet]. Maputo: O País; 2025 [citado 2026 Set 19]. Disponível em: https://opais.co.mz/misau-lanca-formulario-de-medicamentos-e-lista-de-diagnosticos/",
    "lei3de2023": "República de Moçambique. Lei n.º 3/2023, de 8 de Junho: Lei de Investigação em Saúde Humana [Internet]. Maputo: Imprensa Nacional de Moçambique; 2023 [citado 2026 Set 19]. Disponível em: https://anarme.gov.mz/download/lei-3-2023-de-8-de-junho-lei-de-investigacao-em-saude-humana/",
    # ---- metodos, relato e etica
    "whocc2026": "WHO Collaborating Centre for Drug Statistics Methodology. Guidelines for ATC classification and DDD assignment [Internet]. Oslo: Norwegian Institute of Public Health; 2026 [citado 2026 Set 19]. Disponível em: https://atcddd.fhi.no/atc_ddd_index_and_guidelines/guidelines/",
    "langan2018": "Langan SM, Schmidt SA, Wing K, Ehrenstein V, Nicholls SG, Filion KB, et al. The reporting of studies conducted using observational routinely collected health data statement for pharmacoepidemiology (RECORD-PE). BMJ. 2018;363:k3532. doi:10.1136/bmj.k3532. PMID: 30429167.",
    "vonelm2007": "von Elm E, Altman DG, Egger M, Pocock SJ, Gøtzsche PC, Vandenbroucke JP. The Strengthening the Reporting of Observational Studies in Epidemiology (STROBE) statement: guidelines for reporting observational studies. Lancet. 2007;370(9596):1453-7. doi:10.1016/S0140-6736(07)61602-X. PMID: 18064739.",
    "mchugh2012": "McHugh ML. Interrater reliability: the kappa statistic. Biochem Med (Zagreb). 2012;22(3):276-82. PMID: 23092060.",
    "serdar2021": "Serdar CC, Cihan M, Yücel D, Serdar MA. Sample size, power and effect size revisited: simplified and practical approaches in pre-clinical, clinical and laboratory studies. Biochem Med (Zagreb). 2021;31(1):010502. doi:10.11613/BM.2021.010502. PMID: 33380887.",
    "peduzzi1996": "Peduzzi P, Concato J, Kemper E, Holford TR, Feinstein AR. A simulation study of the number of events per variable in logistic regression analysis. J Clin Epidemiol. 1996;49(12):1373-9. doi:10.1016/s0895-4356(96)00236-3. PMID: 8970487.",
    "austin2017": "Austin PC, Merlo J. Intermediate and advanced topics in multilevel logistic regression analysis. Stat Med. 2017;36(20):3257-3277. doi:10.1002/sim.7336. PMID: 28543517.",
    "wma2025": "World Medical Association. World Medical Association Declaration of Helsinki: Ethical Principles for Medical Research Involving Human Participants. JAMA. 2025;333(1):71-74. doi:10.1001/jama.2024.21972. PMID: 39425955.",
}
# Referências anteriores a 2016: só fontes seminais, com o motivo.
SEMINAIS = {
    "misau2014": ("Caderno de mapas nacional de Atenção Integrada às Doenças "
                  "da Infância em vigor em Moçambique; é o padrão de "
                  "referência da adequação da prescrição avaliada no "
                  "estudo."),
    "vonelm2007": ("Declaração original STROBE, norma de relato dos estudos "
                   "observacionais, sem versão posterior que a substitua."),
    "mchugh2012": ("Artigo de referência sobre a interpretação do kappa de "
                   "Cohen em investigação em saúde, que fundamenta o limiar "
                   "de concordância entre avaliadores."),
    "peduzzi1996": ("Estudo de simulação que fundamenta a regra de pelo "
                    "menos dez eventos por variável na regressão "
                    "logística."),
}

# ----------------------------------------------------- 1. introducao --------
INTRODUCAO = [
    P("A resistência aos antimicrobianos (RAM) é uma das ameaças mais sérias "
      "à saúde pública deste século. Em 2021, estimaram-se 4,71 milhões de "
      "mortes associadas à RAM bacteriana, das quais 1,14 milhões lhe foram "
      "directamente atribuíveis, e as previsões apontam para 1,91 milhões de "
      "mortes atribuíveis em 2050 se a tendência actual se mantiver "
      "{gbd2024}. O uso inadequado de antibióticos, sem necessidade ou com "
      "espectro mais largo do que o necessário, é um dos factores "
      "modificáveis da RAM {sharland2022}. Por essa "
      "razão, a declaração política aprovada na Assembleia Geral das Nações "
      "Unidas em Setembro de 2024 "
      "fixou duas metas para 2030: reduzir em 10% as 4,95 milhões de mortes "
      "anuais associadas à RAM e garantir que pelo menos 70% dos antibióticos "
      "usados em saúde humana pertençam ao grupo Acesso da classificação "
      "AWaRe (Access, Watch, Reserve, ou seja, Acesso, Vigilância e Reserva) "
      "da Organização Mundial da Saúde (OMS) {omsunga2024}."),
    P("As crianças menores de cinco anos são o grupo populacional mais "
      "exposto a antibióticos. Nos países de baixo e médio rendimento, o uso "
      "referido de antibióticos em crianças doentes desta idade passou de "
      "36,8% em 2005 para 43,1% em 2017, numa análise de 132 inquéritos "
      "nacionais de 73 países {allwellbrown2020}. Em oito desses países, a "
      "observação directa de 22.519 consultas mostrou que os antibióticos "
      "foram prescritos a 80,5% das crianças com doença respiratória, a "
      "50,1% das crianças com diarreia e a 28,3% das crianças com malária, e "
      "que uma criança recebe, em média, 24,5 prescrições de antibióticos "
      "entre o nascimento e os cinco anos {fink2020}. Numa coorte de oito "
      "países, 44,2% dos episódios de diarreia sem sangue e 39,5% das "
      "infecções respiratórias altas foram tratados com antibióticos, apesar "
      "de as recomendações internacionais não o preverem {rogawski2017}. Nos "
      "cuidados de saúde primários destes países, a proporção global de "
      "doentes com antibiótico prescrito ronda os 52% {sulis2020}."),
    P("Na África subsariana, os estudos nos centros de saúde repetem este "
      "padrão. Num estudo em 16 centros de saúde de quatro países da África "
      "Ocidental, com 14.886 crianças dos 2 aos 59 meses, entre 36% e 71% das "
      "crianças receberam pelo menos um antibiótico, embora 93% dos "
      "antibióticos pertencessem ao grupo Acesso {gres2024}. Em Bujumbura, "
      "62,1% das receitas pediátricas continham antimicrobianos e a "
      "proporção de antibióticos do grupo Vigilância chegou a 25,3% "
      "{manirakiza2025}. No distrito de Mbarara, no Uganda, 68,4% das "
      "prescrições de antibióticos a crianças menores de cinco anos foram "
      "consideradas irracionais {okello2020}. A introdução do teste de "
      "diagnóstico rápido da malária (TDR), desejável para evitar "
      "antimaláricos desnecessários, deslocou parte do problema: numa análise "
      "de 522.480 doentes, receberam antibiótico 69% dos doentes com TDR "
      "negativo e 40% dos doentes com TDR positivo {hopkins2017}."),
    P("Em Moçambique, a mortalidade infanto-juvenil desceu para 60 mortes por "
      "1.000 nascidos vivos nos cinco anos anteriores ao inquérito mais "
      "recente, e na província de Nampula foi de 72 por 1.000 nos dez anos "
      "anteriores; a prevalência de malária nas crianças dos 6 aos 59 meses, "
      "medida por TDR, é de 54,7% nesta província, a mais alta do país, "
      "segundo o Inquérito Demográfico e de Saúde (IDS) de 2022-23 {ids2024}. "
      "O mesmo inquérito registou que 28,8% das crianças menores de cinco "
      "anos com febre tomaram antibióticos, com 39,0% na área urbana e 13,3% "
      "na província de Nampula {ids2024}. Nos serviços de saúde, a evidência "
      "nacional descreve sobretudo crianças internadas: 93,2% das crianças "
      "hospitalizadas com diarreia aguda em quatro províncias receberam "
      "antibióticos {salenciaferrao2025}. Ao mesmo tempo, os agentes "
      "bacterianos das infecções infantis mostram resistências elevadas aos "
      "antibióticos de primeira linha, como a resistência de 92,5% dos "
      "isolados de *Shigella* ao cotrimoxazol em Manhiça {vubil2018}, e o "
      "Plano Nacional de Acção Contra a Resistência Antimicrobiana reconhece "
      "que a maioria dos antibióticos é usada de forma empírica {misau2019}."),
    P("A cidade de Nampula, que coincide com o distrito de Nampula, tinha "
      "798.462 habitantes no recenseamento de 2017 e concentra 13,9% da "
      "população da província {ine2021}. Os dois estudos publicados sobre a "
      "prescrição de antibióticos em crianças na cidade foram realizados no "
      "Hospital Central de Nampula: o primeiro encontrou antibióticos em "
      "97,5% das crianças internadas e erros em 36,5% das prescrições "
      "{xavier2022}; o segundo classificou 74,8% dos antibióticos no grupo "
      "Acesso e 23,7% no grupo Vigilância, com 96,2% administrados por via "
      "injectável {xavier2024}. Estes resultados dizem respeito a doentes "
      "graves de um hospital quaternário e não se estendem às consultas "
      "externas dos centros de saúde, onde é atendida a maior parte das "
      "crianças doentes: das crianças com diarreia para as quais se procurou "
      "tratamento, 92,5% recorreram ao sector público e 78,6% a centros e "
      "postos de saúde {ids2024}."),
    P("Nos centros de saúde, a consulta da criança doente segue a estratégia "
      "de Atenção Integrada às Doenças da Infância (AIDI), aplicada em "
      "Moçambique desde 1998, cujo caderno de mapas define, para cada "
      "classificação clínica, se a criança deve ou não receber antibiótico, "
      "qual, em que dose e durante quantos dias {misau2014}. Esta norma "
      "permite avaliar a adequação da prescrição com critérios explícitos, "
      "enquanto a classificação AWaRe lê o risco de resistência "
      "associado aos antibióticos escolhidos {sharland2022}. Não se "
      "encontrou nenhum estudo publicado que aplique estas duas grelhas às "
      "consultas de crianças menores de cinco anos nos centros de saúde da "
      "cidade de Nampula, lacuna que este estudo preenche avaliando a "
      "frequência, o perfil AWaRe e a adequação às normas nacionais da "
      "prescrição nas consultas de 2026."),
]

# ----------------------------------------------------- 2. problema ----------
PROBLEMA = [
    P("Nos centros de saúde da cidade de Nampula, a decisão de prescrever um "
      "antibiótico a uma criança menor de cinco anos é tomada em consulta "
      "externa por agentes de medicina, enfermeiros, técnicos de medicina ou "
      "médicos, sem apoio de exames microbiológicos e com base na "
      "classificação clínica proposta pelos mapas de AIDI {misau2014, "
      "misau2017}. A norma é clara em várias situações frequentes: a tosse ou "
      "constipação sem sinais de pneumonia, a diarreia sem sangue, a malária "
      "confirmada sem outra infecção e a doença febril sem malária não exigem "
      "antibiótico {misau2014}. A literatura de países vizinhos mostra, "
      "contudo, que estas são precisamente as situações em que mais "
      "antibióticos são prescritos sem indicação: no Uganda, as infecções "
      "respiratórias altas receberam a maior parte das prescrições de "
      "antibióticos {okello2020}; na Etiópia, 73,2% das crianças com "
      "diarreia atendidas em centros de saúde receberam pelo menos um "
      "antimicrobiano {tsige2020}; e, num estudo na Gâmbia, no Mali e no "
      "Quénia, 77,3% das crianças com "
      "diarreia sem indicação para antibiótico receberam-no {awuor2023}."),
    P("A prescrição desnecessária tem consequências para a criança, para a "
      "unidade sanitária e para a comunidade. A criança fica exposta a "
      "efeitos adversos sem benefício clínico; a farmácia do centro de saúde "
      "consome antibióticos que fazem falta às crianças com pneumonia ou "
      "disenteria; e a pressão selectiva acelera a resistência em agentes "
      "que em Moçambique já mostram multirresistência, como *Shigella* "
      "{vubil2018} e *Klebsiella*, "
      "responsável por doença invasiva fatal com resistência à ceftriaxona "
      "{massinga2021}. O uso de antibióticos do grupo Vigilância, de espectro "
      "mais largo, tem maior potencial de seleccionar resistências "
      "{sharland2022}. Em sentido inverso, a omissão do antibiótico numa "
      "criança com pneumonia também é um erro de prescrição, porque a "
      "pneumonia e a diarreia continuam a causar 23% das mortes de crianças "
      "menores de cinco anos no mundo {oms2024}."),
    P("Falta conhecer, para a cidade de Nampula, quatro aspectos essenciais: "
      "com que frequência se prescrevem antibióticos às crianças atendidas "
      "nos centros de saúde; que antibióticos se prescrevem e como se "
      "distribuem pelos grupos AWaRe; em que medida a prescrição respeita as "
      "normas de AIDI quanto à indicação, à escolha, à dose e à duração; e "
      "que características da criança, da consulta e do prescritor se "
      "associam a essa prescrição. O inquérito nacional mede o uso referido "
      "pelas mães, mas não o motivo nem a adequação {ids2024}; os estudos da "
      "cidade descrevem crianças internadas {xavier2022, xavier2024}. Sem "
      "uma linha de base local, o Serviço Distrital de Saúde, Mulher e Acção "
      "Social (SDSMAS) da Cidade de Nampula não consegue dirigir a supervisão "
      "clínica nem acompanhar a meta de 70% de antibióticos do grupo Acesso "
      "{omsunga2024}, e as acções pediátricas previstas no plano nacional "
      "contra a RAM ficam sem dados que as orientem {misau2019}."),
]
PERGUNTA = ("Qual é a frequência da prescrição de antibióticos, como se "
            "distribuem os antibióticos prescritos pelos grupos AWaRe, em que "
            "medida a prescrição é adequada às normas nacionais de AIDI e que "
            "factores se associam à prescrição de antibióticos nas consultas "
            "de crianças menores de cinco anos dos centros de saúde públicos "
            "da cidade de Nampula, em 2026?")
DELIMITACAO = [
    P("O estudo decorre nos centros de saúde públicos da cidade de Nampula "
      "que prestam a consulta da criança doente e incide sobre as primeiras "
      "consultas de episódios de doença de crianças com idade inferior a 60 "
      "meses, realizadas de 1 de Janeiro a 31 de Dezembro de 2026, com "
      "consulta dos arquivos entre Março e Maio de 2027. O objecto é a "
      "prescrição de antibacterianos de uso sistémico da "
      "classificação Anatómica Terapêutica Química (ATC) {whocc2026}, a que "
      "se junta o metronidazol oral, contado entre os antibióticos "
      "prescritos a doentes febris noutros estudos "
      "{hopkins2017}. Ficam de fora os hospitais, as "
      "clínicas e farmácias privadas, as crianças internadas, as consultas "
      "de reavaliação do mesmo episódio, a consulta da criança sadia, os "
      "antibióticos de uso tópico e oftálmico, os antimaláricos, os "
      "antituberculosos e o cotrimoxazol profiláctico das crianças expostas "
      "ao vírus da imunodeficiência humana, que o caderno de mapas de AIDI "
      "prevê como profilaxia e não como tratamento {misau2014}. O estudo "
      "também não mede o uso de antibióticos obtidos sem receita, fenómeno "
      "documentado em Maputo {mate2019}, nem a evolução clínica das "
      "crianças."),
]

# ----------------------------------------------------- 3. objectivos --------
OBJECTIVO_GERAL = (
    "Avaliar a prescrição de antibióticos em crianças menores de cinco anos "
    "atendidas nas consultas da criança doente dos centros de saúde públicos "
    "da cidade de Nampula, de 1 de Janeiro a 31 de Dezembro de 2026, quanto "
    "à frequência, ao perfil segundo a classificação AWaRe e à adequação às "
    "normas nacionais de AIDI.")
OBJECTIVOS_ESPECIFICOS = [
    "Caracterizar as consultas de crianças menores de cinco anos segundo a "
    "idade e o sexo da criança, a classificação clínica registada, a febre e "
    "o resultado do TDR, a categoria profissional do prescritor, a estação "
    "do ano e o número de medicamentos prescritos.",
    "Determinar a proporção de consultas com pelo menos um antibiótico "
    "prescrito, no conjunto e por grupo de classificação clínica.",
    "Descrever os antibióticos prescritos segundo a denominação comum "
    "internacional (DCI), o código ATC, a via de administração, o grupo "
    "AWaRe e a conformidade com a lista nacional de medicamentos "
    "essenciais, e estimar a proporção de antibióticos do grupo Acesso.",
    "Avaliar a adequação das prescrições de antibióticos às normas "
    "nacionais de AIDI quanto à indicação, à escolha do antibiótico, à dose "
    "e à duração, e a omissão de antibiótico nas classificações que o "
    "exigem.",
    "Analisar a associação entre as características da criança, da consulta "
    "e do prescritor e a prescrição de antibióticos.",
]

# ----------------------------------------------------- 4. hipoteses ---------
HIPOTESES_INTRO = [
    P("As hipóteses referem-se à componente analítica do estudo (objectivo "
      "específico 5). Serão testadas pelo teste do qui-quadrado de Pearson "
      "na análise bivariada e pela regressão logística multinível na análise "
      "multivariável, com nível de significância de 5% (p<0,05)."),
]
HIPOTESES = [
    ("H0 (objectivo específico 5, conjunto das consultas)",
     "a prescrição de pelo menos um antibiótico não está associada à idade e "
     "ao sexo da criança, ao grupo de classificação clínica, ao número de "
     "classificações registadas, à febre e ao resultado do TDR, à categoria "
     "profissional do prescritor e à estação do ano;"),
    ("H1 (objectivo específico 5, conjunto das consultas)",
     "a prescrição de pelo menos um antibiótico está associada a pelo menos "
     "uma destas características;"),
    ("H0 (objectivo específico 5, crianças com febre testadas)",
     "entre as crianças com febre e TDR registado, a proporção de consultas "
     "com antibiótico não difere entre as que têm resultado negativo e as "
     "que têm resultado positivo;"),
    ("H1 (objectivo específico 5, crianças com febre testadas)",
     "entre as crianças com febre e TDR registado, a proporção de consultas "
     "com antibiótico difere entre as que têm resultado negativo e as que "
     "têm resultado positivo."),
]
QUESTOES = [
    "Qual é o perfil das consultas quanto à idade, ao sexo, à classificação "
    "clínica, à febre e ao resultado do TDR, à categoria do prescritor e à "
    "estação do ano?",
    "Em que proporção das consultas, no conjunto e em cada grupo de "
    "classificação clínica, é prescrito pelo menos um antibiótico?",
    "Que antibióticos são prescritos, como se distribuem pelos grupos "
    "Acesso, Vigilância e Reserva, e a proporção do grupo Acesso atinge os "
    "limiares de 60% e de 70% da OMS?",
    "Em que proporção as prescrições cumprem as normas de "
    "AIDI quanto à indicação, à escolha, à dose e à duração, e em que "
    "proporção é omitido o antibiótico nas classificações que o exigem?",
]

# ----------------------------------------------------- 5. justificativa -----
JUSTIFICATIVA_INTRO = [
    P("A escolha do tema resulta da convergência de três factos. As crianças "
      "menores de cinco anos são o grupo com maior exposição a antibióticos "
      "{fink2020}; a província de Nampula tem a prevalência de malária "
      "infantil mais alta do país {ids2024}; e o plano nacional contra a RAM "
      "elegeu "
      "como acções prioritárias a elaboração de protocolos nacionais de "
      "tratamento das infecções comuns adquiridas na comunidade por "
      "lactentes e crianças menores de cinco anos e as auditorias do uso de "
      "medicamentos {misau2019}. Um estudo documental nos centros de saúde "
      "da cidade "
      "responde a estas prioridades com baixo custo e sem intervir nos "
      "cuidados."),
]
JUSTIFICATIVA = {
    "cientifica": [
        P("A evidência moçambicana sobre antibióticos em crianças provém de "
          "doentes internados {xavier2022, xavier2024, salenciaferrao2025}, "
          "de registos de diarreia em Maputo {machava2022} ou de inquéritos "
          "domiciliários que não identificam a indicação {ids2024}, e nenhum "
          "estudo descreve, nos cuidados primários, a "
          "prescrição a crianças menores de cinco anos com "
          "a classificação AWaRe e a adequação às normas de AIDI. A "
          "combinação das duas leituras é o contributo metodológico central: "
          "a classificação AWaRe mostra que antibiótico foi escolhido, "
          "enquanto a comparação com a norma mostra se a criança precisava "
          "dele, dimensão que a maioria dos indicadores existentes ainda não "
          "incorpora {funiciello2024}. Ao usar as mesmas métricas que os "
          "estudos africanos recentes {gres2024, manirakiza2025}, os "
          "resultados tornam-se directamente comparáveis."),
    ],
    "academica": [
        P("O estudo aplica, num trabalho de fim de curso da Licenciatura em "
          "Farmácia da Faculdade de Ciências de Saúde (FCS) da Universidade "
          "Lúrio, os métodos da farmacoepidemiologia descritiva e analítica: "
          "codificação ATC, classificação AWaRe, avaliação da adequação com "
          "critérios explícitos, concordância entre avaliadores e regressão "
          "logística multinível. Dá continuidade aos estudos do Departamento "
          "de Farmácia da FCS sobre antibióticos em crianças internadas no "
          "Hospital Central de Nampula {xavier2022}, alargando-os ao nível "
          "primário, e deixa uma ficha de extracção e um quadro de critérios "
          "que outros estudantes poderão reutilizar em estudos de seguimento "
          "ou noutros distritos."),
    ],
    "social": [
        P("Cada prescrição desnecessária expõe uma criança a efeitos adversos "
          "e contribui para que, no futuro, as infecções comuns deixem de "
          "responder aos antibióticos baratos e disponíveis nos centros de "
          "saúde. Em Nampula, onde 72 em cada 1.000 crianças morrem antes dos "
          "cinco anos {ids2024}, a boa prescrição tem dois lados: poupar "
          "antibióticos quando não são necessários e garanti-los quando a "
          "criança tem pneumonia ou disenteria. Os resultados serão "
          "devolvidos aos centros de saúde de forma agregada e não punitiva, "
          "para que a supervisão e a formação se concentrem nas "
          "classificações clínicas em que a prescrição mais se afasta da "
          "norma."),
    ],
    "politica": [
        P("O estudo produz dados que servem instrumentos de política em "
          "vigor. O plano nacional contra a RAM prevê programas de gestão de "
          "antibióticos com intervenções no ponto de atendimento e auditorias "
          "do uso de medicamentos pelos comités de terapêutica e farmácia "
          "{misau2019}; a Lei "
          "n.º 12/2017 enquadra a regulação dos medicamentos de uso humano "
          "{lei12de2017}; a Lista Nacional de Medicamentos Essenciais (LNME) "
          "fixa os níveis de prescrição de cada antibiótico {misau2017}; e o "
          "Ministério da Saúde (MISAU) lançou em 2025 o Formulário Nacional de "
          "Medicamentos {mboane2025}. No plano internacional, a meta de 70% "
          "de antibióticos do grupo Acesso {omsunga2024} e a actualização "
          "das recomendações da OMS para a pneumonia e a diarreia infantis "
          "{oms2024} tornam oportuno verificar como está a ser aplicado o "
          "caderno de mapas de AIDI, que data de 2014 {misau2014}, e reunir "
          "evidência local para a sua revisão."),
    ],
}

# ----------------------------------------------------- 6. revisao -----------
REVISAO = [
    ("Conceitos e definições operacionais", [
        P("Neste estudo, antibiótico designa qualquer antibacteriano de uso "
          "sistémico do subgrupo correspondente da classificação ATC, que "
          "organiza os "
          "fármacos por órgão ou sistema, grupo terapêutico, farmacológico e "
          "químico e substância {whocc2026}, acrescido do metronidazol oral. O "
          "uso racional de medicamentos exige que os doentes recebam "
          "medicamentos apropriados às suas necessidades clínicas "
          "{okello2020}; aplicado aos antibióticos, significa prescrever só "
          "quando há indicação, escolher o fármaco recomendado e ajustar a "
          "dose e a duração ao doente. A unidade de observação é a consulta, "
          "entendida como a primeira consulta de um episódio de doença, e a "
          "prescrição de antibiótico define-se como o registo, nessa consulta, "
          "de pelo menos um antibiótico para tratamento."),
        P("A prescrição é considerada adequada quando cumpre, "
          "cumulativamente, quatro condições avaliáveis: existe uma "
          "classificação clínica registada que, segundo o caderno de mapas de "
          "AIDI, exige antibiótico; o antibiótico é o de primeira escolha ou a "
          "alternativa prevista; a dose por toma e a frequência correspondem "
          "à faixa de idade ou de peso indicada; e a duração corresponde à "
          "recomendada {misau2014}. É inadequada quando falha uma destas "
          "condições. A omissão de antibiótico numa classificação que o "
          "exige, como a pneumonia ou a disenteria, é registada como um erro "
          "distinto, por defeito. Quando a norma nacional e a orientação da "
          "OMS de 2024 divergem, como na duração do tratamento da pneumonia "
          "com respiração rápida, aceita-se como adequada a prescrição "
          "conforme a qualquer uma delas {oms2024}."),
        P("A classificação AWaRe agrupa os antibióticos segundo o espectro de "
          "actividade e o potencial de seleccionar resistências: o grupo "
          "Acesso reúne antibióticos de espectro estreito e baixo potencial, "
          "o grupo Vigilância antibióticos de espectro mais largo e maior "
          "potencial, e o grupo Reserva antibióticos de último recurso "
          "{sharland2022}; o estudo usa a versão de 2025 da lista "
          "{omsaware2025}. A AIDI é uma abordagem da "
          "OMS e do Fundo das Nações Unidas para a Infância que avalia a "
          "criança doente de forma integrada, classifica os problemas por "
          "sinais clínicos e associa a cada classificação um tratamento "
          "{misau2014}. A classificação AIDI não é um diagnóstico "
          "etiológico, o que explica parte da incerteza com que o prescritor "
          "decide sobre o antibiótico."),
    ]),
    ("Magnitude e consequências da prescrição de antibióticos em crianças "
     "menores de cinco anos", [
        P("A exposição das crianças a antibióticos é elevada e crescente nos "
          "países de baixo e médio rendimento, com a subida mais acentuada "
          "nos países de rendimento baixo {allwellbrown2020}. A média de "
          "24,5 prescrições por criança até aos cinco anos esconde uma "
          "variação grande entre países, de 7,1 no Senegal a 59,1 no Uganda "
          "{fink2020}, e a coorte que seguiu 2.134 crianças nos dois "
          "primeiros anos de vida registou 4,9 cursos de antibiótico por "
          "criança e por ano {rogawski2017}. Nos cuidados primários, a "
          "revisão de 48 estudos de 27 países que estimou a proporção de 52% "
          "de doentes com antibiótico encontrou, nos nove estudos que "
          "avaliaram a racionalidade, proporções de prescrição inadequada "
          "entre 8% e 100% {sulis2020}."),
        P("Nos centros de saúde africanos, a frequência é igualmente alta. Na "
          "região de Dodoma, na Tanzânia, 76,3% das 1.021 consultas "
          "analisadas tinham antibiótico e só 45% das prescrições seguiam as "
          "normas nacionais de tratamento {mabilika2022}. Em Acra, no Gana, "
          "70,1% dos doentes febris em ambulatório receberam antibiótico, com "
          "uma odds 60% inferior nos doentes com cinco ou mais anos "
          "{opoku2020}, e, no "
          "Quénia, 68% de 5.735 crianças febris receberam antibiótico, embora "
          "apenas 28% tivessem um diagnóstico bacteriano {hooft2021}."),
        P("Em Moçambique, o uso referido pelas mães em crianças com febre é "
          "mais alto nos menores de seis "
          "meses (46,7%) do que nas crianças dos 48 aos 59 meses (19,3%), e "
          "6% das crianças com diarreia foram tratadas com antibióticos "
          "{ids2024}. Nos serviços, o quadro é "
          "diferente: 93,2% das 2.028 crianças internadas com diarreia aguda "
          "em seis sítios sentinela receberam antibióticos, 49,1% destas mais "
          "do que um, sobretudo ampicilina, gentamicina e cotrimoxazol "
          "{salenciaferrao2025}; em Maputo, 21% dos 9.041 casos de diarreia "
          "registados em livros de consulta foram tratados com antibiótico, "
          "quase sempre sem exame das fezes {machava2022}; e nos cuidados "
          "primários do sul do país, 65,9% das prescrições a doentes com "
          "infecção pelo vírus da imunodeficiência humana incluíam "
          "antibióticos {faiela2022}."),
        P("As consequências mais graves são microbiológicas. Em crianças "
          "menores de cinco anos de Manhiça, 92,5% dos isolados de *Shigella* "
          "eram resistentes ao cotrimoxazol, 50,7% à ampicilina e 55,2% eram "
          "multirresistentes {vubil2018}. Os isolados de *Klebsiella* "
          "recolhidos após a morte de crianças eram resistentes à "
          "ceftriaxona em 69,6% dos casos e a letalidade da infecção foi de "
          "30,7% {massinga2021}. A mortalidade por RAM nas crianças menores "
          "de cinco anos desceu mais de 50% entre 1990 e 2021, o que mostra "
          "que a melhoria dos cuidados reduz as mortes {gbd2024}."),
    ]),
    ("A classificação AWaRe e as metas de uso de antibióticos", [
        P("A classificação AWaRe foi introduzida em 2017 na Lista Modelo de "
          "Medicamentos Essenciais da OMS como resposta à RAM e tem por "
          "objectivo encorajar o uso de antibióticos do grupo Acesso, ou de "
          "nenhum antibiótico, quando apropriado {moja2024}. O livro de "
          "antibióticos AWaRe, publicado em 2022, traduz a classificação em "
          "orientações práticas de primeira e segunda escolha, dose e "
          "duração para as infecções mais comuns, incluindo as da criança "
          "{omsaware2022}. A meta inicial da OMS era que, até 2023, pelo menos "
          "60% dos antibióticos prescritos no mundo pertencessem ao grupo "
          "Acesso {sharland2022}; em 2024, a declaração política das Nações "
          "Unidas elevou-a para 70% até 2030 {omsunga2024}."),
        P("A aplicação da classificação em crianças atendidas em cuidados "
          "primários mostra proporções de Acesso geralmente acima do limiar "
          "de 60%. No estudo da África Ocidental, 93% dos 9.630 antibióticos prescritos a "
          "crianças dos 2 aos 59 meses eram do grupo Acesso, sobretudo "
          "amoxicilina, e não houve prescrição de antibióticos do grupo "
          "Reserva {gres2024}. Em Bujumbura, a proporção de Acesso foi de "
          "71,3%, mas a de Vigilância, de 25,3%, ultrapassou o limite "
          "recomendado de 20%, e 3,4% correspondiam a combinações de dose fixa "
          "não recomendadas pela OMS {manirakiza2025}. Na revisão de Sulis e "
          "colaboradores, o grupo Acesso representou mais de 60% dos "
          "antibióticos em 12 dos 15 países com dados {sulis2020}."),
        P("A proporção de Acesso tem, contudo, um limite que justifica o "
          "desenho deste estudo: uma amoxicilina prescrita a uma criança com "
          "constipação conta como Acesso, embora seja desnecessária, e uma "
          "ciprofloxacina, do grupo Vigilância, é a escolha correcta na "
          "disenteria {misau2014}. Uma revisão identificou 773 indicadores de "
          "qualidade do uso de antibióticos, dos quais só 8 (1%) citavam a "
          "classificação AWaRe, embora 445 (57,6%) reflectissem as "
          "orientações do livro AWaRe; cerca de metade dos indicadores "
          "específicos de infecção dizia respeito às infecções "
          "respiratórias {funiciello2024}. Os autores concluem pela "
          "necessidade de indicadores baseados na classificação AWaRe que "
          "combinem o antibiótico escolhido com a indicação, o que este "
          "estudo operacionaliza ao cruzar o grupo AWaRe com a adequação à "
          "norma de AIDI."),
    ]),
    ("Determinantes da prescrição de antibióticos em crianças", [
        P("O primeiro determinante é a incerteza diagnóstica perante a febre. "
          "Com a generalização do TDR, o risco global de prescrição de "
          "antibiótico foi 21% mais alto nos "
          "grupos com teste {hopkins2017}. No Malawi, 72% das crianças "
          "menores de cinco anos com febre tinham doença febril não "
          "palúdica, e o cotrimoxazol e a amoxicilina eram usados em quase "
          "todas as classificações {kapitotembo2020}; no Quénia, o TDR "
          "negativo foi um dos factores associados à prescrição "
          "{hooft2021}. Esta relação tem particular interesse em Nampula: a "
          "prevalência de malária infantil é de 54,7% na província, mas de "
          "12,0% na área urbana do país {ids2024}, pelo que, na cidade, "
          "muitas crianças febris terão TDR negativo."),
        P("O segundo grupo de determinantes é clínico e demográfico. A tosse "
          "multiplicou por 3,5 a odds de antibiótico em doentes febris no "
          "Gana {opoku2020} e associou-se à prescrição em crianças "
          "com diarreia na Gâmbia e no Quénia {awuor2023}; a idade mais baixa "
          "aumenta a probabilidade de antibiótico {opoku2020, ids2024}. O "
          "terceiro grupo diz respeito ao prescritor e ao serviço. Na "
          "Tanzânia, os técnicos de medicina prescreveram antibióticos com um "
          "odds ratio (OR) de 2,55 face aos médicos {mabilika2022}; na Etiópia, a consulta "
          "do caderno de mapas, com odds ratio ajustado (ORa) de 3,9, a "
          "formação em AIDI (ORa 2,4) e a "
          "menor carga de doentes (ORa 1,7) associaram-se à classificação e "
          "ao tratamento correctos da pneumonia {gelagay2025}. No Gana, "
          "porém, a formação em AIDI associou-se a mais prescrição "
          "{opoku2020}, e no Uganda nenhum factor do prescritor ou da unidade "
          "se associou à prescrição irracional {okello2020}, divergências "
          "que exigem dados locais."),
        P("Há ainda determinantes do sistema e da comunidade. Numa análise da "
          "AIDI em 16 países, a melhoria da prescrição logo após a formação "
          "não se manteve no tempo, contrariada pela pressão dos pais, pelo "
          "marketing farmacêutico, por incentivos financeiros e pelo acesso a "
          "antibióticos sem receita {carai2021}. Em Maputo, 20,9% dos adultos "
          "tinham usado antibióticos sem receita, adquiridos sobretudo em "
          "farmácias {mate2019}. As intervenções que actuam sobre a decisão "
          "clínica são eficazes: na Tanzânia, um algoritmo digital com testes "
          "no local de atendimento reduziu a prescrição de antibióticos em "
          "consultas pediátricas de 70,1% para 23,2%, sem aumento da falência "
          "clínica {tan2024}, e uma revisão de 78 relatos em 25 países "
          "confirmou que os sistemas de apoio à decisão clínica reduzem a "
          "prescrição nos cuidados primários (OR 0,17) {gres2025}."),
    ]),
    ("Enquadramento normativo moçambicano", [
        P("A Lei n.º 12/2017 regula os medicamentos, as vacinas e os outros "
          "produtos biológicos para uso humano em Moçambique {lei12de2017}. A LNME de 2017 organiza o "
          "Serviço Nacional de Saúde em quatro níveis de cuidados, de que os "
          "centros de saúde constituem o primário, e define cinco níveis de "
          "prescrição: o nível 0, dos medicamentos dispensados pelo agente "
          "polivalente elementar; o nível 1, prescritos por agentes de "
          "medicina, enfermeiros e categorias superiores; o nível 2, por "
          "técnicos de medicina geral e superiores; o nível 3, por médicos "
          "generalistas e superiores; e o nível 4, por especialistas "
          "{misau2017}. A amoxicilina em comprimido dispersível é de nível 0, a "
          "ciprofloxacina em comprimido e a gentamicina injectável de nível 1, "
          "a amoxicilina com ácido clavulânico em comprimido de nível 2 e a "
          "ceftriaxona injectável de nível 3 {misau2017}. Em Maio de 2025, o "
          "MISAU lançou o Formulário Nacional de Medicamentos e a Lista "
          "Nacional de Testes e Diagnósticos Essenciais {mboane2025}."),
        P("O caderno de mapas de AIDI, publicado pelo MISAU em 2014, é a norma "
          "clínica da consulta da criança doente dos 2 meses aos 5 anos e do "
          "lactente de 1 semana aos 2 meses {misau2014}. Para a tosse ou a "
          "dificuldade respiratória, a pneumonia, definida por respiração "
          "rápida ou tiragem subcostal, trata-se com amoxicilina durante 5 "
          "dias, enquanto a classificação «sem pneumonia: tosse ou "
          "constipação» recebe apenas tratamento sintomático; a pneumonia "
          "grave ou doença muito grave recebe a primeira dose de penicilina "
          "cristalina, ou de ampicilina com gentamicina, por via "
          "intramuscular, e é transferida com urgência. Na diarreia, a "
          "criança sem sangue nas fezes recebe sais de reidratação oral e "
          "zinco, e a disenteria recebe ciprofloxacina durante 3 dias. Na "
          "febre, todas as crianças devem fazer TDR; a malária trata-se com "
          "antimalárico e a doença febril sem malária com paracetamol e "
          "reavaliação. A infecção aguda do ouvido recebe amoxicilina durante "
          "10 dias; a faringoamigdalite aguda supurada, a desnutrição aguda "
          "grave sem complicação e a infecção bacteriana localizada do "
          "lactente recebem amoxicilina durante 5 dias; e o "
          "impetigo com lesões extensas recebe cloxacilina durante 5 dias "
          "{misau2014}."),
        P("A orientação da OMS de 2024 para a pneumonia e a diarreia, que "
          "estima em 1,17 milhões as mortes de crianças menores de cinco anos "
          "por estas duas causas, recomenda amoxicilina oral "
          "durante três ou cinco dias na pneumonia com respiração rápida e "
          "durante cinco dias, em ambulatório e em vez de antibióticos "
          "injectáveis, na pneumonia com tiragem subcostal {oms2024}. "
          "Desaconselha antibióticos na diarreia aquosa aguda, mantém a "
          "ciprofloxacina como primeira escolha na diarreia com sangue visível "
          "e reduz a dose de zinco para 5 mg por dia durante até 14 dias "
          "{kundu2025}. O plano nacional contra a RAM de 2019-2023, por seu "
          "lado, prevê protocolos nacionais de tratamento para lactentes e "
          "crianças menores de cinco anos com infecções comuns adquiridas na "
          "comunidade, formação dos profissionais na sua aplicação e "
          "auditorias do uso de medicamentos pelos comités de terapêutica e "
          "farmácia {misau2019}."),
    ]),
    ("Métodos de medida da prescrição e da adequação em estudos documentais",
     [
        P("A maioria dos estudos sobre antibióticos nos cuidados primários "
          "dos países de baixo e médio rendimento assenta na extracção de "
          "dados de processos clínicos ou na auditoria de receitas "
          "{sulis2020}. Para os indicadores de uso de medicamentos, as "
          "orientações da OMS recomendam uma amostra mínima de 600 receitas "
          "ou consultas {manirakiza2025}. As medidas mais usadas são a "
          "proporção de consultas com antibiótico, o número médio de "
          "antibióticos por consulta, a distribuição pelos grupos AWaRe e os "
          "indicadores específicos de síndroma, como a proporção de "
          "infecções respiratórias altas ou de diarreias aquosas tratadas com "
          "antibiótico {funiciello2024}. A codificação dos antibióticos pela "
          "classificação ATC garante a comparabilidade entre estudos "
          "{whocc2026}."),
        P("A avaliação da adequação pode seguir critérios implícitos, em que "
          "um perito julga cada caso, ou critérios explícitos, em que se "
          "compara a prescrição com uma norma escrita. Os critérios explícitos "
          "são mais reprodutíveis, mas continuam a exigir julgamento, por "
          "exemplo quando a classificação registada é ambígua ou coexistem "
          "duas classificações. Por isso, recomenda-se que dois avaliadores "
          "classifiquem os casos de forma independente e que a concordância "
          "seja medida pelo kappa de Cohen, que corrige a concordância "
          "esperada ao acaso; a interpretação proposta por Cohen pode ser "
          "demasiado permissiva em saúde, ao admitir valores tão baixos como "
          "0,41 {mchugh2012}. A qualidade dos registos é a principal "
          "limitação destes estudos: em Bujumbura, 26,2% das receitas não "
          "tinham a indicação documentada {manirakiza2025}, e em Maputo quase "
          "nenhuma criança com diarreia teve exame das fezes {machava2022}, "
          "o que obriga a verificar a fonte antes da recolha."),
        P("Os estudos com dados de rotina devem seguir normas de relato "
          "próprias. A declaração Strengthening the Reporting of "
          "Observational Studies in Epidemiology (STROBE) fixa os itens "
          "mínimos do relato dos estudos observacionais {vonelm2007}, e a "
          "extensão REporting of studies Conducted using Observational "
          "Routinely-collected health Data for pharmacoepidemiology "
          "(RECORD-PE) acrescenta os itens próprios dos dados de rotina e "
          "dos estudos sobre medicamentos {langan2018}. O cumprimento destas "
          "normas facilita a apreciação crítica e a síntese futura dos "
          "resultados."),
    ]),
]

# ----------------------------------------------------- 7. estado da arte ----
ESTADO_ARTE = [
    P("O [[quadro:estado_arte]] sintetiza catorze estudos empíricos "
      "publicados entre 2020 e 2025 sobre a prescrição de antibióticos a "
      "crianças em África, incluindo quatro realizados em Moçambique, dois "
      "dos quais na cidade de Nampula."),
    QUADRO("estado_arte",
           "Síntese de estudos sobre a prescrição de antibióticos a crianças "
           "em África (estado da arte)",
           ["Autor (ano)", "Local", "Desenho (n)", "Principais resultados"],
           [
               ["Gres et al. (2024) {gres2024}",
                "Burkina Faso, Guiné, Mali e Níger (16 centros de saúde)",
                "Transversal (14.886 crianças de 2-59 meses)",
                "Pelo menos um antibiótico em 71%, 66%, 63% e 36% das "
                "crianças; 93% dos 9.630 antibióticos do grupo Acesso; "
                "nenhum do grupo Reserva."],
               ["Manirakiza et al. (2025) {manirakiza2025}",
                "Bujumbura, Burundi (20 centros de saúde)",
                "Transversal retrospectivo (800 receitas pediátricas)",
                "Antimicrobianos em 62,1% das receitas; Acesso 71,3% e "
                "Vigilância 25,3%; 26,2% sem indicação documentada."],
               ["Okello et al. (2020) {okello2020}",
                "Mbarara, Uganda",
                "Transversal retrospectivo (1.218 registos de menores de "
                "cinco anos)",
                "Infecção respiratória alta como diagnóstico mais frequente e "
                "com mais antibióticos (53%); 68,4% das prescrições "
                "irracionais."],
               ["Mabilika et al. (2022) {mabilika2022}",
                "Dodoma, Tanzânia",
                "Transversal retrospectivo (1.021 consultas; 474 de menores "
                "de cinco anos)",
                "Antibiótico em 76,3%; 45% conformes com as normas; técnicos "
                "de medicina com OR 2,55 face aos médicos."],
               ["Tsige et al. (2020) {tsige2020}",
                "Adis Abeba, Etiópia (centros de saúde)",
                "Transversal retrospectivo (803 registos de diarreia)",
                "Antimicrobiano em 73,2%; manejo inadequado em 54,4%; sais "
                "de reidratação em 66,7% e zinco em 47,5%."],
               ["Awuor et al. (2023) {awuor2023}",
                "Gâmbia, Mali e Quénia",
                "Caso-controlo (4.840 casos de diarreia moderada a grave)",
                "Dos 1.757 casos sem indicação, 77,3% receberam antibiótico; "
                "a tosse associou-se à prescrição."],
               ["Gelagay et al. (2025) {gelagay2025}",
                "South Gondar, Etiópia (20 centros de saúde)",
                "Transversal (1.564 crianças)",
                "Classificação e tratamento correctos dos sintomas de "
                "pneumonia em 35,6%; uso do caderno de mapas com ORa 3,9."],
               ["Hooft et al. (2021) {hooft2021}",
                "Quénia (5 unidades)",
                "Coorte (5.735 crianças febris)",
                "Antibiótico em 68%, com diagnóstico bacteriano em 28%; TDR "
                "negativo associado à prescrição."],
               ["Opoku et al. (2020) {opoku2020}",
                "Grande Acra, Gana (6 unidades)",
                "Transversal com dados secundários (2.519 doentes febris)",
                "Antibiótico em 70,1%; idade de cinco ou mais anos com ORa "
                "0,40; formação em AIDI com OR 2,3."],
               ["Tan et al. (2024) {tan2024}",
                "Tanzânia (40 centros de saúde)",
                "Ensaio aleatorizado por conglomerados (44.306 consultas)",
                "Algoritmo digital reduziu a prescrição de antibióticos de "
                "70,1% para 23,2%, sem aumento da falência clínica."],
               ["Xavier et al. (2022) {xavier2022}",
                "Hospital Central de Nampula, Moçambique",
                "Transversal retrospectivo (464 antibióticos em crianças "
                "internadas)",
                "Uso de antibióticos em 97,5%; erros em 36,5% das "
                "prescrições, sobretudo de duração (74,0%) e dose (24,4%)."],
               ["Xavier et al. (2024) {xavier2024}",
                "Hospital Central de Nampula, Moçambique",
                "Retrospectivo (464 antibióticos em crianças internadas)",
                "Acesso 74,8%, Vigilância 23,7%, sem Reserva; 1,51 "
                "antibióticos por receita; 96,2% injectáveis."],
               ["Salência-Ferrão et al. (2025) {salenciaferrao2025}",
                "Seis sítios sentinela em quatro províncias de Moçambique",
                "Transversal de vigilância (2.028 crianças internadas com "
                "diarreia)",
                "Antibióticos em 93,2%; mais de um em 49,1%; ampicilina "
                "46,2%, gentamicina 38,4% e cotrimoxazol 30,5%."],
               ["Machava et al. (2022) {machava2022}",
                "Maputo, Moçambique",
                "Retrospectivo em livros de registo (9.041 casos de "
                "diarreia)",
                "Antibiótico em 21%; sangue nas fezes em 22%; exame das "
                "fezes em cerca de 1%."],
           ],
           larguras=[3.3, 2.9, 3.4, 6.4],
           fonte="Elaboração própria (2026), a partir das fontes citadas."),
    P("A leitura do quadro revela um padrão consistente: nos cuidados "
      "primários africanos, entre um terço e três quartos das crianças "
      "recebem antibiótico, e a maior parte da prescrição sem indicação "
      "concentra-se nas infecções respiratórias altas, na diarreia sem "
      "sangue e na febre com TDR negativo {okello2020, awuor2023, "
      "hooft2021}. A proporção de antibióticos do grupo Acesso é em geral "
      "alta {gres2024, xavier2024}, o que confirma que este indicador, "
      "isolado, não chega para avaliar a qualidade da prescrição. Os "
      "resultados divergem quanto ao papel do prescritor e da formação em "
      "AIDI {mabilika2022, opoku2020, gelagay2025}, e os estudos que "
      "medem a adequação usam critérios diferentes, o que limita a "
      "comparação."),
    P("Em Moçambique, os estudos disponíveis incidem sobre crianças "
      "internadas {xavier2022, xavier2024, salenciaferrao2025} ou sobre a "
      "diarreia em Maputo {machava2022}, e nenhum descreve a prescrição nas "
      "consultas externas dos centros de saúde, em particular na cidade de "
      "Nampula, nem cruza a classificação AWaRe com a norma de AIDI. O "
      "presente estudo preenche esta "
      "lacuna com uma amostra probabilística, critérios explícitos de "
      "adequação e dupla avaliação independente, e mede a relação entre o "
      "resultado do TDR e a prescrição num contexto de malária endémica."),
]
ESQUEMA_TEXTO = [
    P("A [[figura:esquema]] representa as relações que o estudo examina. "
      "As características da criança, as clínicas registadas "
      "e as do prescritor e do serviço são as variáveis "
      "independentes; o desfecho é a prescrição de antibióticos, lida em "
      "três dimensões: a presença de antibiótico na consulta, o grupo AWaRe "
      "do antibiótico e a adequação à norma de AIDI. Os factores que "
      "influenciam a prescrição mas não constam dos registos, como a pressão "
      "dos cuidadores, a formação do prescritor em AIDI e a carga de "
      "trabalho {carai2021, gelagay2025}, figuram como confundimento "
      "residual, cuja influência será discutida e parcialmente captada pelo "
      "efeito aleatório do centro de saúde."),
]
ESQUEMA_TITULO = ("Esquema conceptual da prescrição de antibióticos em "
                  "crianças menores de cinco anos")
ESQUEMA = {
    "contexto": ("Consultas da criança doente nos centros de saúde públicos "
                 "da cidade de Nampula, 1 de Janeiro a 31 de Dezembro de "
                 "2026"),
    "blocos": [
        ("Características da criança",
         ["idade em meses", "sexo", "peso registado"]),
        ("Características clínicas registadas",
         ["classificação AIDI principal", "número de classificações",
          "febre e resultado do TDR", "sinais de gravidade e transferência"]),
        ("Prescritor e serviço",
         ["categoria profissional do prescritor", "centro de saúde",
          "estação do ano", "ruptura de stock de amoxicilina"]),
    ],
    "desfecho": ("Prescrição de antibióticos",
                 ["pelo menos um antibiótico na consulta",
                  "grupo AWaRe (Acesso, Vigilância, Reserva)",
                  "adequação às normas de AIDI"]),
    "moderadores": ("Confundimento residual não registado",
                    ["pressão dos cuidadores", "formação em AIDI",
                     "carga de trabalho do prescritor",
                     "acesso a antibióticos sem receita"]),
}

# ----------------------------------------------------- 8. metodologia -------
METODOLOGIA = [
    ("Tipo e desenho do estudo", [
        P("Trata-se de um estudo observacional, transversal, retrospectivo, "
          "descritivo e analítico, de base documental e abordagem "
          "quantitativa. É transversal porque cada consulta é observada uma "
          "única vez, no momento da prescrição; é retrospectivo porque "
          "analisa registos de 2026 consultados em 2027; é descritivo nos "
          "objectivos específicos 1 a 4 e analítico no objectivo específico "
          "5. Não há contacto com as crianças nem com os cuidadores, nem "
          "qualquer intervenção nos cuidados."),
        P("A opção pelo desenho documental retrospectivo tem duas razões: a "
          "observação prospectiva alteraria o comportamento dos "
          "prescritores, que tenderiam a seguir a norma por "
          "se saberem observados, e exigiria o consentimento de cada "
          "cuidador; a revisão de registos já existentes evita esse viés, "
          "cobre as duas estações do ano e tem um custo compatível com um "
          "trabalho de fim de curso. A contrapartida é a dependência da "
          "qualidade dos registos, tratada na verificação prévia das fontes e "
          "nas regras de decisão descritas adiante. O relato seguirá a "
          "declaração STROBE e a sua extensão RECORD-PE para estudos de "
          "farmacoepidemiologia com dados de rotina {vonelm2007, "
          "langan2018}."),
    ]),
    ("Local e período do estudo", [
        P("O estudo realiza-se na cidade de Nampula, capital da província do "
          "mesmo nome, no norte de Moçambique, que coincide com o distrito de "
          "Nampula e tinha 798.462 habitantes no recenseamento de 2017 "
          "{ine2021}. Os cuidados de saúde primários públicos da cidade são "
          "prestados por centros de saúde sob a gestão do SDSMAS da Cidade de "
          "Nampula, que oferecem a consulta da criança doente segundo a "
          "estratégia AIDI, dispõem de TDR e de farmácia própria e transferem "
          "as crianças graves para os hospitais da cidade {misau2014}. O "
          "número de centros de saúde públicos com consulta da criança doente "
          "em funcionamento em 2026 será confirmado no início do estudo "
          "[confirmar junto do SDSMAS da Cidade de Nampula]. O clima define "
          "uma estação quente e chuvosa, de Novembro a Março, e uma estação "
          "seca, de Abril a Outubro {ids2024}."),
        P("O período de referência dos dados vai de 1 de Janeiro a 31 de "
          "Dezembro de 2026, o que cobre um ano completo e as duas estações. "
          "O estudo decorre de Outubro de 2026 a Setembro de 2027: a "
          "verificação prévia das fontes realiza-se em Fevereiro de 2027, "
          "depois da aprovação ética, com registos de Dezembro de 2025, "
          "exteriores ao período de referência, e a recolha de dados "
          "propriamente dita decorre de Março a Maio de 2027."),
    ]),
    ("População e unidade de análise", [
        P("A população-alvo são as consultas de crianças com idade inferior "
          "a 60 meses atendidas nas consultas da criança doente dos centros de "
          "saúde públicos da cidade de Nampula. A população de estudo são as "
          "primeiras consultas de episódios de doença registadas nos livros "
          "de registo da consulta da criança doente desses centros entre 1 de "
          "Janeiro e 31 de Dezembro de 2026. A unidade de análise principal é "
          "a consulta, usada nos objectivos específicos 1, 2, 4 e 5. No "
          "objectivo específico 3 e nas dimensões de escolha, dose e duração "
          "do objectivo específico 4, a unidade é o antibiótico prescrito, e "
          "uma consulta com dois antibióticos contribui com dois itens; a "
          "adequação global é depois agregada à consulta, que só é adequada "
          "se todos os antibióticos o forem."),
        P("A mesma criança pode ter vários episódios de doença no ano, e cada "
          "primeira consulta de um episódio é elegível. Para preservar a "
          "independência das observações, se a mesma criança for seleccionada "
          "duas vezes, identificada no local pelo nome, pela data de "
          "nascimento e pelo número do processo, sem transcrição destes "
          "dados, mantém-se apenas a primeira consulta e a segunda é "
          "substituída pela linha elegível seguinte. As consultas de "
          "reavaliação do mesmo episódio são excluídas porque a prescrição "
          "nelas registada continua, em regra, a da primeira consulta. A "
          "ligação entre a linha do livro e a receita arquivada na farmácia "
          "faz-se no local, pela data, pelo centro e pela identificação da "
          "criança, e só o código do estudo é transcrito para a ficha."),
    ]),
    ("Amostra e cálculo do tamanho da amostra", [
        H3("Estratégia de amostragem"),
        P("Todos os centros de saúde públicos da cidade com consulta da "
          "criança doente são incluídos e funcionam como estratos. Dentro de "
          "cada centro, as consultas são seleccionadas por amostragem "
          "aleatória sistemática ao longo dos doze meses, com alocação "
          "proporcional ao número de primeiras consultas de crianças menores "
          "de cinco anos registadas em 2026, o que torna a amostra "
          "auto-ponderada. Caso a autorização abranja apenas parte dos "
          "centros, estes serão sorteados com probabilidade proporcional ao "
          "volume e passarão a ser conglomerados, com o efeito de desenho "
          "indicado mais abaixo para esse cenário."),
        H3("Tamanho da amostra para a estimativa principal"),
        P("O tamanho mínimo foi calculado para estimar a proporção de "
          "consultas com pelo menos um antibiótico (objectivo específico 2), "
          "pela fórmula de uma proporção {serdar2021}:"),
        FORMULA("n<sub>0</sub> = Z<sup>2</sup> × p × (1 - p) / "
                "d<sup>2</sup>"),
        P("Em que Z = 1,96 corresponde a um nível de confiança de 95%; p é a "
          "proporção esperada, fixada em 0,50, porque os estudos africanos em "
          "cuidados primários apontam para valores entre 36% e 76% "
          "{gres2024, mabilika2022} e não existe estimativa para Nampula, e "
          "porque este valor maximiza o tamanho da amostra; e d = 0,05 é a "
          "margem de erro absoluta admitida. Substituindo, n<sub>0</sub> = "
          "1,96<sup>2</sup> × 0,50 × 0,50 / 0,05<sup>2</sup> = 3,8416 × 0,25 "
          "/ 0,0025 = 384,16, arredondado para 385 consultas."),
        P("O número anual de primeiras consultas elegíveis (N) só será "
          "conhecido na fase preparatória [confirmar junto do SDSMAS e dos "
          "centros de saúde]. A [[tabela:cenarios_amostra]] mostra que a "
          "correcção para população finita, n = n<sub>0</sub> / [1 + "
          "(n<sub>0</sub> - 1) / N], reduziria pouco a amostra para os "
          "volumes plausíveis; por prudência, adopta-se n<sub>0</sub> = 385 "
          "sem correcção. O coeficiente de correlação intraclasse (CCI) mede "
          "a semelhança entre consultas do mesmo centro e do mesmo "
          "prescritor, e o efeito de desenho (DEFF) é dado por 1 + (m - 1) × "
          "CCI, em que m é o número de consultas por centro {austin2017}. A "
          "estratificação exaustiva por centro retira do erro a variação "
          "entre centros, mas a semelhança entre consultas do mesmo "
          "prescritor mantém-se, pelo que se adopta, por prudência, um DEFF "
          "de 1,5. Acrescenta-se 10% para compensar linhas "
          "ilegíveis, rasuradas ou sem tratamento legível:"),
        FORMULA("n = n<sub>0</sub> × DEFF / (1 - r) = 385 × 1,5 / 0,90"),
        P("O produto 385 × 1,5 = 577,5 é arredondado para 578 consultas "
          "analisáveis, e 578 / 0,90 = 642,2 dá uma amostra final de 643 "
          "consultas, que supera o mínimo de 600 consultas recomendado pela "
          "OMS para os indicadores de uso de medicamentos {manirakiza2025}. "
          "No cenário de autorização parcial, com conglomerados, usa-se DEFF "
          "= 2,0 e a amostra sobe para 385 × 2,0 / 0,90 = 855,6, ou seja, "
          "856 consultas."),
        TABELA("cenarios_amostra",
               "Tamanho da amostra segundo o número anual de consultas "
               "elegíveis e o efeito de desenho",
               ["N anual de consultas elegíveis",
                "n com correcção para população finita",
                "n × DEFF", "n final (÷ 0,90)"],
               [["5.000", "358", "537", "597"],
                ["10.000", "371", "557", "619"],
                ["20.000", "378", "567", "630"],
                ["50.000", "383", "575", "639"],
                ["Desconhecido ou muito grande (adoptado, DEFF 1,5)", "385",
                 "578", "643"],
                ["Autorização parcial, conglomerados (DEFF 2,0)", "385",
                 "770", "856"]],
               larguras=[5.6, 3.8, 2.8, 3.8],
               fonte="Elaboração própria (2026). DEFF: efeito de desenho; "
                     "nas quatro primeiras linhas, DEFF = 1,5."),
        H3("Alocação e selecção das consultas"),
        P("Em cada centro i, o número de consultas a seleccionar é n<sub>i"
          "</sub> = 643 × N<sub>i</sub> / N, arredondado para cima, em que "
          "N<sub>i</sub> é o número de primeiras consultas de crianças "
          "menores de cinco anos registadas no centro em 2026, contado nos "
          "resumos mensais na fase preparatória. O intervalo de "
          "amostragem é k<sub>i</sub> = N<sub>i</sub> / n<sub>i</sub>; o ponto "
          "de partida é sorteado entre 1 e k<sub>i</sub> com um gerador de "
          "números aleatórios, e seleccionam-se as linhas de k<sub>i</sub> em "
          "k<sub>i</sub>, do primeiro ao último livro do ano, o que distribui "
          "a amostra pelos doze meses. Quando a linha seleccionada não for "
          "elegível, toma-se a linha elegível seguinte; o número de "
          "substituições e os seus motivos serão registados e apresentados "
          "num diagrama de fluxo."),
        H3("Poder para a componente analítica"),
        P("Para as comparações de dois grupos do objectivo específico 5, "
          "usa-se a fórmula de duas proporções, com nível de significância de "
          "5% (Z<sub>1-α/2</sub> = 1,96) e poder de 80% (Z<sub>1-β</sub> = "
          "0,84) {serdar2021}:"),
        FORMULA("n por grupo = [Z<sub>1-α/2</sub> × √(2 × p<sub>m</sub> × "
                "(1 - p<sub>m</sub>)) + Z<sub>1-β</sub> × √(p<sub>1</sub> × "
                "(1 - p<sub>1</sub>) + p<sub>2</sub> × (1 - p<sub>2</sub>))]"
                "<sup>2</sup> / (p<sub>1</sub> - p<sub>2</sub>)<sup>2</sup>"),
        P("Em que p<sub>1</sub> e p<sub>2</sub> são as proporções de consultas "
          "com antibiótico nos dois grupos e p<sub>m</sub> a sua média. Para "
          "detectar uma diferença de 15 pontos percentuais (60% contra 45%) "
          "são necessárias 173 consultas por grupo, ou 260 com DEFF de 1,5; "
          "as exposições com grupos equilibrados, como o sexo ou a estação do "
          "ano, cumprem este requisito com as 578 consultas analisáveis. Para "
          "a hipótese sobre o TDR, as proporções de 69% e 40% observadas em "
          "doentes com resultado negativo e positivo {hopkins2017} exigem 46 "
          "crianças por grupo, ou 69 com DEFF. Nas categorias com poucas "
          "consultas, como a dos médicos, só serão detectáveis diferenças de "
          "pelo menos 20 pontos percentuais (97 consultas por grupo, ou 146 "
          "com DEFF), limitação que será declarada. Para a regressão "
          "logística, exige-se pelo menos dez eventos por parâmetro "
          "{peduzzi1996}: com uma proporção de 50%, esperam-se cerca de 289 "
          "consultas com antibiótico, o que permite até 28 parâmetros; o "
          "modelo previsto tem cerca de 14, o que exige pelo menos 140 "
          "eventos, isto é, uma proporção de consultas com antibiótico de "
          "pelo menos 24%. Se for inferior, as categorias serão agrupadas. "
          "Para o objectivo específico 4, as cerca de 289 consultas com "
          "antibiótico permitem estimar uma proporção de 50% com uma "
          "semi-amplitude do intervalo de confiança a 95% (IC 95%) de 5,8 "
          "pontos percentuais, ou de 7,1 "
          "pontos com DEFF."),
    ]),
    ("Critérios de inclusão e de exclusão", [
        H3("Critérios de inclusão"),
        LISTA([
            "Primeira consulta de um episódio de doença de criança com idade "
            "de 0 a 59 meses, registada no livro de registo da consulta da "
            "criança doente de um centro de saúde público da cidade de "
            "Nampula entre 1 de Janeiro e 31 de Dezembro de 2026.",
            "Registo com a data da consulta, a idade da criança e pelo menos "
            "uma classificação clínica ou um tratamento legíveis.",
        ]),
        H3("Critérios de exclusão"),
        LISTA([
            "Consultas de reavaliação ou de seguimento de um episódio já "
            "registado.",
            "Consultas da criança sadia, de vacinação ou de rastreio "
            "nutricional sem queixa de doença.",
            "Crianças transferidas de outra unidade sanitária com tratamento "
            "antibiótico já em curso.",
            "Segunda consulta seleccionada da mesma criança no ano.",
            "Linhas ilegíveis ou rasuradas de modo que impeça a leitura da "
            "classificação e do tratamento, mesmo depois da consulta da "
            "receita.",
        ]),
    ]),
    ("Variáveis e definições operacionais", [
        P("O [[quadro:variaveis]] apresenta as variáveis do estudo, o seu tipo, "
          "a definição operacional com as categorias e o objectivo específico "
          "a que servem. As classificações clínicas seguem os termos do "
          "caderno de mapas de AIDI {misau2014}; os códigos dos antibióticos "
          "seguem a classificação ATC {whocc2026}, os grupos AWaRe a lista de "
          "2025 {omsaware2025} e os níveis de prescrição a LNME "
          "{misau2017}."),
        QUADRO("variaveis", "Variáveis do estudo e definições operacionais",
               ["Variável", "Tipo", "Definição operacional e categorias",
                "Objectivo"],
               [
                   ["Idade", "Independente, quantitativa (categorizada)",
                    "Meses completos na data da consulta; menos de 2 meses; "
                    "2-11; 12-23; 24-59 meses", "1, 5"],
                   ["Sexo", "Independente, nominal",
                    "Masculino; feminino", "1, 5"],
                   ["Peso registado", "Descritiva, nominal",
                    "Sim (em kg, usado na avaliação da dose); não", "1, 4"],
                   ["Classificação clínica principal",
                    "Independente, nominal",
                    "Tosse ou constipação sem pneumonia; pneumonia; pneumonia "
                    "grave ou doença muito grave; diarreia sem sangue; "
                    "disenteria; malária; doença febril sem malária; "
                    "infecção aguda do ouvido; faringoamigdalite aguda "
                    "supurada; infecção da pele; desnutrição aguda; infecção "
                    "bacteriana do lactente; outras; não registada",
                    "1, 2, 5"],
                   ["Número de classificações", "Independente, ordinal",
                    "Uma; duas; três ou mais", "1, 5"],
                   ["Febre e resultado do TDR", "Independente, nominal",
                    "Sem febre registada; febre com TDR positivo; febre com "
                    "TDR negativo; febre sem TDR registado", "1, 5"],
                   ["Sinais de gravidade ou transferência",
                    "Independente, nominal",
                    "Sim (sinal geral de perigo ou transferência registada); "
                    "não", "1, 4"],
                   ["Categoria profissional do prescritor",
                    "Independente, nominal",
                    "Agente de medicina; enfermeiro(a); técnico(a) de "
                    "medicina; médico(a); não registada", "1, 5"],
                   ["Estação do ano", "Independente, nominal",
                    "Chuvosa (Novembro a Março); seca (Abril a Outubro)",
                    "1, 5"],
                   ["Centro de saúde", "Estrato e efeito aleatório, nominal",
                    "Código do centro (A, B, C...)", "1, 5"],
                   ["Número de medicamentos na consulta",
                    "Descritiva, quantitativa discreta",
                    "Contagem de medicamentos prescritos", "1"],
                   ["Prescrição de antibiótico", "Dependente, dicotómica",
                    "Sim (pelo menos um antibacteriano de uso sistémico ou "
                    "metronidazol oral, para tratamento); não", "2, 5"],
                   ["Número de antibióticos na consulta",
                    "Descritiva, quantitativa discreta",
                    "0; 1; 2 ou mais", "2"],
                   ["Antibiótico prescrito", "Descritiva, nominal",
                    "DCI e código ATC de nível 5", "3"],
                   ["Grupo AWaRe", "Descritiva, nominal",
                    "Acesso; Vigilância; Reserva; não classificado", "3"],
                   ["Via e forma farmacêutica", "Descritiva, nominal",
                    "Oral (comprimido dispersível, comprimido ou cápsula, "
                    "suspensão ou xarope); injectável", "3"],
                   ["Conformidade com a LNME", "Descritiva, nominal",
                    "Antibiótico na LNME (sim; não); categoria do prescritor "
                    "compatível com o nível de prescrição (sim; não; "
                    "indeterminado)", "3"],
                   ["Adequação da indicação", "Dependente, dicotómica",
                    "Adequada se a classificação registada exige antibiótico "
                    "segundo o quadro de critérios; inadequada se não exige",
                    "4"],
                   ["Adequação da escolha", "Dependente, dicotómica",
                    "Adequada se o antibiótico é o de primeira escolha ou a "
                    "alternativa prevista para a classificação; inadequada "
                    "no caso contrário", "4"],
                   ["Adequação da dose", "Dependente, dicotómica",
                    "Adequada se a dose por toma e a frequência diária estão "
                    "dentro de ±20% do valor da faixa de idade ou de peso do "
                    "caderno de AIDI; inadequada fora deste intervalo", "4"],
                   ["Adequação da duração", "Dependente, dicotómica",
                    "Adequada se a duração difere no máximo um dia da "
                    "recomendada; inadequada no caso contrário", "4"],
                   ["Adequação global", "Dependente, dicotómica",
                    "Adequada se todas as dimensões avaliáveis de todos os "
                    "antibióticos da consulta são adequadas; inadequada se "
                    "falha pelo menos uma", "4"],
                   ["Omissão de antibiótico indicado",
                    "Dependente, dicotómica",
                    "Sim (classificação que exige antibiótico sem antibiótico "
                    "prescrito); não", "4"],
                   ["Ruptura de stock de amoxicilina no mês",
                    "Confundidora, nominal",
                    "Sim; não; sem registo (fichas de stock da farmácia)",
                    "5"],
               ],
               larguras=[3.4, 3.0, 7.8, 1.8]),
    ]),
    ("Instrumentos de recolha de dados e respectivas fontes", [
        P("São usadas quatro fontes documentais em cada centro de saúde: o "
          "livro de registo da consulta da criança doente, com a data, "
          "a idade, o sexo, a classificação e o tratamento, cujos campos "
          "exactos serão confirmados na verificação prévia; as receitas "
          "aviadas arquivadas na farmácia, que confirmam a DCI, a "
          "dose, a frequência e a duração; as fichas de stock da "
          "amoxicilina, para identificar os meses de ruptura; e os resumos "
          "mensais, para contar as consultas elegíveis. Os dados são "
          "transcritos para dois instrumentos construídos para o estudo."),
        P("A ficha de extracção de dados (Apêndice A) reúne, sem "
          "identificadores, as variáveis do [[quadro:variaveis]] e segue a "
          "estrutura das classificações de AIDI e dos indicadores de uso de "
          "antibióticos {misau2014, funiciello2024}. "
          "Por não ser uma escala psicométrica, não se lhe aplicam medidas de "
          "consistência interna; a validade de conteúdo será avaliada por "
          "um painel de cinco peritos (farmacêutico, médico com "
          "experiência em AIDI, técnico de medicina da consulta da criança "
          "doente, docente de farmacoepidemiologia e estatístico), que "
          "classificarão cada item quanto à relevância e à clareza numa "
          "escala de quatro pontos, e os itens com índice de validade de "
          "conteúdo inferior a 0,80 serão revistos. A ficha será pré-testada "
          "em 65 registos de Dezembro de 2025, cerca de 10% da amostra e "
          "exteriores ao período de referência, para medir "
          "o tempo de preenchimento, o grau de preenchimento das fontes e a "
          "clareza das instruções."),
        P("A ficha de avaliação da adequação (Apêndice B) é preenchida por "
          "cada avaliador para as consultas com antibiótico e para as "
          "consultas com classificação que exige antibiótico. O padrão de "
          "referência é o caderno de mapas de AIDI {misau2014}, completado "
          "pela orientação da OMS de 2024 para a pneumonia e a diarreia "
          "{oms2024} e, nas infecções que o caderno não cobre, pelo livro de "
          "antibióticos AWaRe {omsaware2022}. O [[quadro:criterios]] resume os "
          "critérios. A tolerância de ±20% na dose, que absorve o "
          "fraccionamento de comprimidos, e a de um dia na duração são regras "
          "da equipa de investigação que serão submetidas ao painel de "
          "peritos antes da recolha."),
        QUADRO("criterios",
               "Critérios de adequação da prescrição de antibióticos segundo "
               "a classificação clínica registada",
               ["Classificação registada", "Antibiótico indicado",
                "Primeira escolha e duração", "Fonte"],
               [
                   ["Tosse ou constipação sem pneumonia", "Não",
                    "Nenhum; tratamento sintomático",
                    "AIDI {misau2014}"],
                   ["Pneumonia (respiração rápida ou tiragem subcostal)",
                    "Sim",
                    "Amoxicilina oral, 5 dias; 3 dias aceites na respiração "
                    "rápida isolada",
                    "AIDI {misau2014}; OMS {oms2024}"],
                   ["Pneumonia grave ou doença muito grave", "Sim",
                    "Primeira dose de penicilina cristalina, ou de ampicilina "
                    "com gentamicina, por via intramuscular, e transferência",
                    "AIDI {misau2014}"],
                   ["Diarreia sem sangue, com ou sem desidratação", "Não",
                    "Nenhum; sais de reidratação oral e zinco",
                    "AIDI {misau2014}; OMS {kundu2025}"],
                   ["Disenteria (sangue nas fezes)", "Sim",
                    "Ciprofloxacina oral, 3 dias",
                    "AIDI {misau2014}; OMS {kundu2025}"],
                   ["Malária (febre e TDR positivo) sem outra classificação "
                    "bacteriana", "Não", "Nenhum; antimalárico de primeira "
                    "linha", "AIDI {misau2014}"],
                   ["Doença febril sem malária (TDR negativo, sem sinais de "
                    "perigo nem foco)", "Não",
                    "Nenhum; paracetamol e reavaliação em 2 dias",
                    "AIDI {misau2014}"],
                   ["Infecção aguda do ouvido", "Sim",
                    "Amoxicilina oral, 10 dias", "AIDI {misau2014}"],
                   ["Faringoamigdalite aguda supurada", "Sim",
                    "Amoxicilina oral, 5 dias", "AIDI {misau2014}"],
                   ["Impetigo ou foliculite com lesões extensas, nódulos ou "
                    "abcessos múltiplos", "Sim", "Cloxacilina oral, 5 dias",
                    "AIDI {misau2014}"],
                   ["Desnutrição aguda grave sem complicação", "Sim",
                    "Amoxicilina oral, 5 dias", "AIDI {misau2014}"],
                   ["Infecção bacteriana localizada do lactente de 1 semana "
                    "a 2 meses", "Sim", "Amoxicilina oral, 5 dias",
                    "AIDI {misau2014}"],
                   ["Outras infecções sem critério no caderno de AIDI",
                    "Conforme a infecção",
                    "Primeira ou segunda escolha do livro AWaRe",
                    "OMS {omsaware2022}"],
               ],
               larguras=[4.6, 2.2, 6.0, 3.2],
               fonte="Elaboração própria (2026), a partir das fontes "
                     "citadas.",
               nota="Quando coexistem várias classificações, a indicação é "
                    "avaliada pela classificação que exige antibiótico, se "
                    "existir. A dose é comparada com a tabela por idade ou "
                    "peso do caderno de AIDI."),
        P("Cada antibiótico será classificado pela DCI e pela via de "
          "administração no grupo AWaRe da lista de 2025 {omsaware2025}; os "
          "que nela não constarem serão registados como não classificados. O "
          "código ATC de nível 5 será atribuído segundo o índice do centro "
          "colaborador da OMS {whocc2026}, e a presença na LNME e o nível de "
          "prescrição segundo a lista nacional em vigor {misau2017}."),
    ]),
    ("Procedimentos de recolha de dados e controlo de qualidade", [
        P("A recolha começa só depois do parecer favorável do Comité "
          "Institucional de Bioética para a Saúde da Universidade Lúrio "
          "(CIBS-UniLúrio) e das autorizações da Direcção Provincial de Saúde "
          "(DPS) de Nampula, do SDSMAS da Cidade de Nampula e da direcção de "
          "cada centro de saúde. Em cada centro, o investigador apresenta o "
          "estudo à direcção e ao responsável da farmácia, acorda os horários "
          "de acesso ao arquivo e conta as primeiras consultas de 2026 para "
          "calcular n<sub>i</sub> e k<sub>i</sub>. Os documentos são "
          "consultados numa sala indicada pela direcção e nunca saem do "
          "centro."),
        P("Em Fevereiro de 2027, a verificação prévia das fontes nos 65 "
          "registos de Dezembro de 2025 aplica regras de decisão escritas: "
          "uma variável com menos de 60% de preenchimento sai dos objectivos "
          "e é declarada como limitação. Assim, se o peso tiver menos de 60% "
          "de preenchimento, a dose passa a ser avaliada pela faixa de idade; "
          "se a categoria do prescritor tiver menos de 60%, sai do modelo do "
          "objectivo específico 5; se o resultado do TDR estiver registado em "
          "menos de 60% das crianças febris, a segunda hipótese passa a "
          "exploratória, testada só no subconjunto com registo; e se o "
          "tratamento não constar do livro nem puder ser ligado à receita em "
          "pelo menos 60% das linhas, a avaliação da dose e da duração "
          "restringe-se às consultas com receita ligada."),
        P("A extracção é feita pelo investigador e por um assistente, "
          "estudante finalista de Farmácia, formados durante dois dias com um "
          "manual de preenchimento e exercícios sobre registos do pré-teste. "
          "Uma amostra aleatória de 10% das consultas (65) é extraída de novo, "
          "de forma independente, pelo outro extractor; exige-se uma "
          "concordância de pelo menos 95% nas variáveis-chave (classificação, "
          "antibiótico, dose, frequência e duração) e, se não for atingida "
          "num centro, todas as fichas desse centro são revistas. O "
          "investigador revê diariamente as fichas e o orientador, "
          "semanalmente, uma amostra. Os dados são digitados numa base "
          "com regras de validação (EpiData Entry ou equivalente de acesso "
          "livre), com dupla digitação de 10% das "
          "fichas e correcção das discrepâncias a partir do papel."),
        P("A adequação é classificada por dois avaliadores independentes, o "
          "investigador e um farmacêutico ou clínico com formação em AIDI, "
          "que não conhecem o centro nem o prescritor, porque as fichas só "
          "contêm códigos. Antes da recolha, os dois avaliadores calibram-se "
          "nas prescrições com antibiótico do pré-teste; só se avança com um "
          "kappa de Cohen de pelo menos 0,60 em cada dimensão, com meta de "
          "0,80, tendo em conta que valores mais baixos seriam permissivos "
          "em investigação em saúde {mchugh2012}. As discordâncias são "
          "resolvidas por consenso e, na sua falta, por um terceiro avaliador "
          "(pediatra ou o orientador). O kappa final de cada dimensão será "
          "apresentado com o IC 95%."),
    ]),
    ("Processamento e análise dos dados", [
        P("A análise será feita no Statistical Package for the Social "
          "Sciences (SPSS), versão 26 ou superior, ou no R, com nível de "
          "significância de 5% (p<0,05) e "
          "IC 95%. As estimativas para a cidade terão em conta a "
          "estratificação por centro de saúde; como a alocação é "
          "proporcional, não são necessárias ponderações. As variáveis "
          "categóricas serão descritas por frequências e proporções com IC 95% "
          "pelo método de Wilson, e a idade e o número de medicamentos por "
          "mediana e intervalo interquartil (objectivo específico 1)."),
        P("Para o objectivo específico 2, estimam-se a proporção de consultas "
          "com pelo menos um antibiótico, no conjunto e por classificação, o "
          "número médio de antibióticos por consulta e quatro indicadores "
          "específicos de síndroma: as proporções "
          "de consultas com antibiótico entre as classificadas como tosse ou "
          "constipação, diarreia sem sangue, malária sem outra classificação "
          "bacteriana e doença febril sem malária {funiciello2024}. No "
          "objectivo específico 3, a unidade é o antibiótico: descrevem-se a "
          "DCI, o código ATC, a via, o grupo AWaRe e a conformidade com a "
          "LNME e o nível de prescrição, e estima-se a proporção "
          "do grupo Acesso com IC 95% ajustado à agregação por consulta, "
          "comparada com os limiares de 60% e 70% {sharland2022, "
          "omsunga2024} pela posição do IC 95% e por um teste binomial exacto "
          "unilateral."),
        P("Para o objectivo específico 4, estimam-se as proporções de "
          "prescrições adequadas em cada dimensão e a adequação global por "
          "consulta, com IC 95%, a distribuição dos tipos de erro e a "
          "proporção de omissão de antibiótico entre as consultas com "
          "classificação que o exige. Para o objectivo específico 5, a análise "
          "bivariada usa o teste do qui-quadrado de Pearson, ou o teste exacto "
          "de Fisher quando algum valor esperado for inferior a 5, com odds "
          "ratio (OR) bruto e IC 95%. Entram no modelo multivariável as "
          "variáveis com p<0,20 na análise bivariada e, por razões teóricas, a "
          "idade, a classificação clínica e a febre com o resultado do TDR. O "
          "modelo é uma regressão logística multinível com intercepto "
          "aleatório por centro de saúde, que fornece o odds ratio ajustado "
          "(ORa) com IC 95%, o CCI e o odds "
          "ratio mediano {austin2017}; se houver menos de dez centros, o "
          "centro entra como efeito fixo e usam-se erros-padrão robustos. A "
          "colinearidade é verificada pelo factor de inflação da variância "
          "(limite de 5) e o ajustamento pelo critério de informação de "
          "Akaike. A segunda hipótese é testada nas crianças com febre e TDR "
          "registado, pelo teste do qui-quadrado e por um OR ajustado para a "
          "idade e a classificação respiratória."),
        P("A proporção de dados em falta será apresentada para cada "
          "variável. Com menos de 5% de falta, usa-se a análise de casos "
          "completos; acima disso, a categoria «não registado» é mantida no "
          "modelo e faz-se uma análise de sensibilidade que a exclui. Estão "
          "previstas mais três: a adequação avaliada "
          "só pelo caderno de AIDI, sem a tolerância da orientação da OMS de "
          "2024; a exclusão das consultas com mais de uma classificação; e o "
          "modelo do objectivo específico 5 sem os meses com ruptura de stock "
          "de amoxicilina. Os resultados serão apresentados em tabelas e "
          "gráficos, com o diagrama de fluxo da selecção."),
    ]),
    ("Limitações do estudo e estratégias de mitigação", [
        P("O [[quadro:limitacoes]] identifica as principais limitações "
          "previstas, a sua consequência provável sobre os resultados e a "
          "estratégia adoptada para as reduzir."),
        QUADRO("limitacoes", "Limitações previstas e estratégias de mitigação",
               ["Limitação", "Consequência", "Mitigação"],
               [
                   ["Registos incompletos, ilegíveis ou sem tratamento",
                    "Viés de informação e perda de precisão",
                    "Verificação prévia em 65 registos com regra dos 60%; "
                    "margem de 10%; ficha padronizada; consulta da receita"],
                   ["Classificação registada diferente dos sinais clínicos "
                    "reais", "Adequação sobrestimada quando a classificação é "
                    "escolhida para justificar o antibiótico",
                    "Descrever a adequação como relativa à classificação "
                    "registada; análise de sensibilidade sem as consultas "
                    "com várias classificações"],
                   ["Receitas não ligáveis às linhas do livro",
                    "Dose e duração não avaliáveis numa parte das consultas",
                    "Ligação no local por data e identificação; dimensões "
                    "avaliadas só onde há dados, com denominador declarado"],
                   ["Antibióticos obtidos fora da consulta", "Subestimação da "
                    "exposição total das crianças",
                    "Delimitação explícita do objecto; comparação com os "
                    "dados do IDS"],
                   ["Autorização apenas de parte dos centros",
                    "Viés de selecção e menor generalização",
                    "Sorteio com probabilidade proporcional ao volume; DEFF "
                    "de 2,0 e amostra de 856 consultas"],
                   ["Julgamento da adequação", "Erro de classificação",
                    "Critérios explícitos; dois avaliadores cegos para o "
                    "centro; kappa de Cohen; terceiro avaliador"],
                   ["Poucas consultas em algumas categorias do prescritor",
                    "Erro do tipo II", "Agrupamento de categorias; declaração "
                    "da diferença mínima detectável"],
                   ["Norma nacional de 2014 anterior à orientação da OMS de "
                    "2024", "Classificação da adequação dependente da norma "
                    "adoptada", "Aceitar a conformidade com qualquer das "
                    "duas; análise de sensibilidade só com a norma nacional"],
                   ["Rupturas de stock de antibióticos",
                    "Escolhas inadequadas por falta do fármaco de primeira "
                    "escolha", "Registo mensal das rupturas de amoxicilina e "
                    "análise de sensibilidade"],
                   ["Desenho transversal", "Impossibilidade de inferência "
                    "causal", "Interpretação em termos de associação"],
               ],
               larguras=[4.6, 4.8, 6.6]),
    ]),
    ("Considerações éticas", [
        P("O protocolo será submetido ao CIBS-UniLúrio e, se este o "
          "determinar, ao Comité Nacional de Bioética para a Saúde (CNBS), e "
          "nenhum registo será consultado antes do parecer favorável. O "
          "estudo respeita a Declaração de Helsínquia na revisão de 2024 "
          "{wma2025} e a Lei n.º 3/2023, de Investigação em Saúde Humana "
          "{lei3de2023}, e só se inicia com as autorizações escritas da DPS "
          "de Nampula, do SDSMAS da Cidade de Nampula e da direcção de cada "
          "centro de saúde (Apêndice D)."),
        P("Pede-se ao CIBS-UniLúrio a dispensa do consentimento informado "
          "(Apêndice C), porque o estudo usa apenas registos de consultas já "
          "realizadas, com risco mínimo para as crianças, e porque seria "
          "impraticável localizar os cuidadores de 643 crianças atendidas "
          "ao longo de 2026, sem que o contacto trouxesse qualquer benefício. "
          "A confidencialidade é garantida pelas medidas seguintes:"),
        LISTA([
            "A ficha não contém nomes, números de processo, endereços nem "
            "outros identificadores da criança ou do cuidador; a verificação "
            "de duplicados faz-se no local, sem transcrição.",
            "Os centros de saúde são identificados por letras e os "
            "prescritores apenas pela categoria profissional; nenhum "
            "resultado será apresentado por prescritor individual.",
            "Os dados digitais são guardados em computador protegido por "
            "palavra-passe e em suporte externo cifrado, acessíveis só ao "
            "investigador e ao orientador, e as fichas em papel em armário "
            "fechado na FCS, durante cinco anos, após o que serão destruídas.",
            "A equipa de recolha assina um termo de compromisso de "
            "confidencialidade (Apêndice E).",
        ]),
        P("O estudo não traz benefício directo às crianças cujos registos são "
          "analisados, mas os resultados poderão melhorar a prescrição para "
          "as crianças atendidas no futuro. O risco é o de quebra de "
          "confidencialidade, reduzido pelas medidas acima. A devolução dos "
          "resultados é agregada e não punitiva, e os dados não serão usados "
          "para avaliação disciplinar dos profissionais. Como via de "
          "referenciação, se a extracção detectar um padrão de prescrição "
          "potencialmente perigoso e ainda em curso, como doses muito acima "
          "das recomendadas ou cotrimoxazol em lactentes com menos de quatro "
          "semanas, contrariando o caderno de AIDI {misau2014}, o "
          "investigador informa o orientador em 48 horas e ambos comunicam o "
          "padrão, sem identificar a criança por escrito, à direcção do "
          "centro e ao responsável de supervisão clínica do SDSMAS, para "
          "correcção imediata. Os investigadores declaram não ter conflitos "
          "de interesses."),
    ]),
]

# ----------------------------------------------------- 9 e 10 ---------------
RESULTADOS_ESPERADOS = [
    P("Os resultados esperados seguem a ordem dos objectivos específicos; "
      "não se antecipam valores numéricos, mas a literatura citada permite "
      "prever a direcção provável de cada um e a sua utilidade prática."),
    LISTA([
        "Objectivo específico 1: espera-se maior número de consultas nos "
        "dois primeiros anos de vida, idades em que a febre e a diarreia são "
        "mais frequentes {ids2024}, e um predomínio das classificações de "
        "tosse ou constipação, malária, doença febril sem malária e diarreia "
        "sem sangue, com muitas crianças febris com TDR negativo, dado o "
        "carácter urbano da cidade. Este perfil orienta a formação dos "
        "prescritores e a previsão das necessidades de antibióticos e de TDR "
        "dos centros de saúde.",
        "Objectivo específico 2: espera-se que a proporção de consultas com "
        "antibiótico se situe entre um terço e três quartos, como nos "
        "cuidados primários de outros países africanos {gres2024, "
        "mabilika2022}, com os valores mais altos nas classificações "
        "respiratórias. O resultado constitui a linha de base do SDSMAS "
        "para monitorizar a prescrição de antibióticos às crianças.",
        "Objectivo específico 3: espera-se o predomínio da amoxicilina e do "
        "cotrimoxazol {okello2020, kapitotembo2020} e uma proporção de "
        "antibióticos do grupo Acesso acima de 60% {gres2024, sulis2020}, "
        "com os antibióticos do grupo Vigilância concentrados na "
        "ciprofloxacina e na ceftriaxona. O resultado permite acompanhar a "
        "meta de 70% do grupo Acesso ao nível dos cuidados primários.",
        "Objectivo específico 4: espera-se que a principal causa de "
        "inadequação seja a prescrição sem indicação na tosse ou constipação "
        "e na diarreia sem sangue, seguida de erros de duração "
        "{okello2020, tsige2020, xavier2022}, e que exista alguma omissão de "
        "antibiótico na pneumonia. O resultado indica em que classificações "
        "a supervisão e a formação em AIDI devem concentrar-se.",
        "Objectivo específico 5: espera-se associação da prescrição com o "
        "TDR negativo, com as classificações respiratórias e com a idade mais "
        "baixa {hopkins2017, opoku2020}, sendo incerta a direcção do efeito "
        "da categoria do prescritor. O resultado identifica os grupos de "
        "crianças e de profissionais a que devem dirigir-se as acções de "
        "gestão de antimicrobianos.",
    ]),
]
DIVULGACAO = [
    P("Os resultados serão apresentados em defesa pública na FCS da "
      "Universidade Lúrio e entregues, num relatório com sumário "
      "de duas páginas, ao SDSMAS da Cidade de Nampula, à DPS de Nampula e à "
      "direcção de cada centro de saúde, com os resultados do centro "
      "comparados, de forma codificada, com os da cidade. Será proposta uma "
      "sessão de devolução com os prescritores e os responsáveis das "
      "farmácias, centrada nas classificações com maior prescrição "
      "inadequada e sem carácter disciplinar. Seguem-se a submissão a uma "
      "revista com revisão por pares, de preferência de acesso aberto, a "
      "apresentação nas jornadas científicas da Universidade Lúrio e em "
      "reuniões nacionais, e o envio de um resumo aos responsáveis pelo "
      "plano nacional contra a RAM, para apoiar "
      "os protocolos pediátricos nele previstos {misau2019}. Não se prevê "
      "devolução directa à comunidade, por não haver participantes "
      "contactados, mas será proposto ao SDSMAS um folheto sobre o uso "
      "responsável de antibióticos para as salas de espera."),
]

# ----------------------------------------------------- 11. cronograma -------
CRONOGRAMA_TEXTO = [
    P("O [[quadro:cronograma]] distribui as actividades pelos doze meses do "
      "estudo, de Outubro de 2026 a Setembro de 2027. A submissão ao "
      "CIBS-UniLúrio e os pedidos de autorização decorrem de Novembro de "
      "2026 a Janeiro de 2027; a verificação prévia das fontes, o pré-teste "
      "e a calibração dos avaliadores realizam-se em Fevereiro de 2027, já "
      "com o parecer ético; e a recolha de dados decorre de Março a Maio de "
      "2027, seguida da análise, da redacção e da defesa em Setembro de "
      "2027."),
]
CRONOGRAMA = {
    "inicio": (2026, 10),
    "n_meses": 12,
    "actividades": [
        ("Revisão da literatura e redacção do protocolo", [1, 2]),
        ("Submissão ao CIBS-UniLúrio e pedidos de autorização (DPS, SDSMAS "
         "e centros de saúde)", [2, 3, 4]),
        ("Validação da ficha pelo painel de peritos e manual de "
         "preenchimento", [3, 4]),
        ("Verificação prévia das fontes, pré-teste e calibração dos "
         "avaliadores", [5]),
        ("Contagem das consultas por centro e sorteio da amostra", [5, 6]),
        ("Recolha de dados nos centros de saúde, com dupla extracção de "
         "10%", [6, 7, 8]),
        ("Avaliação independente da adequação e digitação dos dados",
         [7, 8, 9]),
        ("Processamento e análise estatística", [9, 10]),
        ("Redacção do relatório final", [10, 11]),
        ("Revisão pelo orientador, correcções e entrega", [11]),
        ("Defesa pública e devolução dos resultados às instituições", [12]),
    ],
}

# ----------------------------------------------------- 12. orcamento --------
ORCAMENTO_TEXTO = [
    P("A [[tabela:orcamento]] apresenta os custos previstos, em meticais, "
      "com 10% de imprevistos. O estudo será financiado com fundos próprios "
      "do investigador, sem prejuízo de um pedido de apoio à FCS da "
      "Universidade Lúrio. As rubricas maiores são o transporte urbano e a "
      "alimentação durante os cerca de três meses de recolha, e os "
      "subsídios ao assistente, que "
      "assegura a dupla extracção e a dupla digitação, e ao segundo "
      "avaliador da adequação, condição do controlo de qualidade. A análise "
      "usa a licença institucional do SPSS ou o R, de acesso livre, sem "
      "custo. Se o CIBS-UniLúrio cobrar taxa de apreciação, será coberta "
      "pela rubrica de imprevistos [confirmar o valor junto do "
      "CIBS-UniLúrio]."),
]
ORCAMENTO = [
    ("Impressão da ficha de extracção (2 páginas por ficha, 720 fichas)",
     "página", 1440, 5),
    ("Impressão da ficha de avaliação da adequação (2 avaliadores)",
     "página", 800, 5),
    ("Impressão e encadernação do protocolo, dos pedidos e do relatório "
     "final", "exemplar", 6, 600),
    ("Material de escritório (pastas, canetas, blocos, clipes)",
     "conjunto", 2, 750),
    ("Dispositivo de armazenamento externo cifrado", "unidade", 1, 1200),
    ("Subsídio ao assistente de recolha (dupla extracção e digitação)",
     "dia", 20, 500),
    ("Subsídio ao segundo avaliador da adequação", "consulta avaliada", 330,
     25),
    ("Subsídio ao terceiro avaliador (casos discordantes)", "sessão", 4,
     1000),
    ("Painel de peritos para a validação da ficha", "perito", 5, 1000),
    ("Transporte urbano para os centros de saúde (investigador e "
     "assistente)", "deslocação", 120, 100),
    ("Alimentação durante o trabalho de campo", "dia-pessoa", 80, 150),
    ("Comunicação (telemóvel e internet)", "mês", 12, 500),
    ("Sessão de devolução dos resultados (materiais e lanche)", "sessão", 1,
     3000),
    ("Impressão de cartaz para jornadas científicas", "unidade", 1, 2000),
]
ORCAMENTO_IMPREVISTOS = 0.10

# ----------------------------------------------------- apendices ------------
APENDICES = [
    ("Ficha de extracção de dados da consulta", [
        NOTA("Instruções ao extractor: preencher uma ficha por consulta "
             "seleccionada. Não transcrever nomes, números de processo, "
             "endereços nem qualquer outro identificador da criança ou do "
             "cuidador. A verificação de duplicados faz-se no local, sem "
             "registo. Quando um campo não constar do livro nem da receita, "
             "assinalar «não registado» e nunca inferir o valor."),
        H3("Secção I. Identificação da ficha"),
        CAMPO("Código da ficha: __________    Código do centro de saúde: "
              "____"),
        CAMPO("Mês da consulta: ______    Número de ordem da linha "
              "seleccionada no livro: ______"),
        CAMPO("Código do extractor: ____    Data da extracção: ___/___/2027"),
        PERG("A linha foi substituída?",
             ["Não", "Sim, por reavaliação", "Sim, por idade de 60 meses ou "
              "mais", "Sim, por ilegibilidade", "Sim, por duplicado da mesma "
              "criança"]),
        H3("Secção II. Dados da criança"),
        PERG("Idade em meses completos na data da consulta:"),
        PERG("Sexo:", ["Masculino", "Feminino", "Não registado"]),
        PERG("Peso registado:", ["Sim, ______ kg", "Não"]),
        H3("Secção III. Dados clínicos"),
        PERG("Febre registada (história de febre ou temperatura axilar de "
             "37,5 °C ou mais):", ["Sim", "Não", "Não registado"]),
        PERG("Resultado do TDR:", ["Positivo", "Negativo", "Não realizado",
                                   "Não registado"]),
        PERG("Classificações registadas (assinalar todas):",
             ["Tosse ou constipação sem pneumonia", "Pneumonia",
              "Pneumonia grave ou doença muito grave", "Diarreia sem sangue",
              "Disenteria", "Malária", "Doença febril sem malária",
              "Infecção aguda do ouvido", "Faringoamigdalite aguda supurada",
              "Infecção da pele", "Desnutrição aguda",
              "Infecção bacteriana do lactente", "Outra: __________",
              "Não registada"]),
        PERG("Classificação principal (a primeira registada): __________"),
        PERG("Número de classificações registadas:",
             ["Uma", "Duas", "Três ou mais"]),
        PERG("Sinal geral de perigo ou transferência registada:",
             ["Sim", "Não"]),
        H3("Secção IV. Prescrição"),
        PERG("Número total de medicamentos prescritos na consulta:"),
        PERG("Foi prescrito pelo menos um antibiótico para tratamento?",
             ["Sim", "Não"]),
        NOTA("Se sim, preencher uma linha por antibiótico. A DCI, a dose, a "
             "frequência e a duração são copiadas do livro ou da receita; o "
             "código ATC, o grupo AWaRe e o nível da LNME são preenchidos "
             "depois, no escritório."),
        TABELA(None, "", ["N.º", "Antibiótico (DCI)", "Forma e dosagem",
                          "Dose por toma", "Tomas por dia", "Duração (dias)",
                          "Via", "ATC", "AWaRe", "LNME (nível)"],
               [["1", "", "", "", "", "", "", "", "", ""],
                ["2", "", "", "", "", "", "", "", "", ""],
                ["3", "", "", "", "", "", "", "", "", ""]],
               larguras=[0.9, 2.6, 2.0, 1.5, 1.3, 1.4, 1.2, 1.6, 1.6, 1.9],
               fonte=""),
        PERG("Outros medicamentos prescritos (assinalar):",
             ["Sais de reidratação oral", "Zinco", "Antimalárico",
              "Paracetamol", "Cotrimoxazol profiláctico", "Outro: ______"]),
        PERG("Fonte dos dados do tratamento:",
             ["Livro de registo", "Receita", "Livro e receita"]),
        PERG("Categoria profissional do prescritor:",
             ["Agente de medicina", "Enfermeiro(a)", "Técnico(a) de medicina",
              "Médico(a)", "Não registada"]),
        PERG("Ruptura de stock de amoxicilina no mês da consulta (ficha de "
             "stock):", ["Sim", "Não", "Sem registo"]),
        CAMPO("Observações: ____________________________________________"),
    ]),
    ("Ficha de avaliação da adequação da prescrição de antibióticos", [
        NOTA("Instruções ao avaliador: avaliar de forma independente, sem "
             "consultar o outro avaliador, as consultas com antibiótico e as "
             "consultas com classificação que exige antibiótico, usando o "
             "quadro de critérios do protocolo. As fichas só contêm códigos; "
             "não procurar identificar o centro nem o prescritor."),
        CAMPO("Código da ficha avaliada: __________    Código do avaliador: "
              "____    Data: ___/___/2027"),
        PERG("Classificação de referência usada na avaliação: __________"),
        PERG("A classificação de referência exige antibiótico segundo o "
             "quadro de critérios?", ["Sim", "Não"]),
        PERG("Indicação:", ["Adequada", "Inadequada (antibiótico sem "
                                         "indicação)", "Não avaliável"]),
        PERG("Escolha do antibiótico:", ["Adequada (primeira escolha ou "
                                         "alternativa prevista)", "Inadequada",
                                         "Não avaliável"]),
        PERG("Dose por toma e frequência (tolerância de ±20%):",
             ["Adequada", "Subdose", "Sobredose", "Frequência incorrecta",
              "Não avaliável"]),
        PERG("Duração (tolerância de um dia):",
             ["Adequada", "Curta", "Longa", "Não registada"]),
        PERG("Omissão de antibiótico indicado:",
             ["Sim", "Não", "Não aplicável"]),
        PERG("Classificação global da consulta:",
             ["Adequada", "Inadequada", "Não avaliável"]),
        CAMPO("Justificação em caso de dúvida: ____________________________"),
    ]),
    ("Pedido de dispensa do consentimento informado", [
        CAMPO("Ao Comité Institucional de Bioética para a Saúde da "
              "Universidade Lúrio"),
        CAMPO("Nampula, ___ de __________ de 2026"),
        P("Assunto: pedido de dispensa do consentimento informado no estudo "
          "«Prescrição de antibióticos e adequação às normas nacionais em "
          "crianças menores de cinco anos atendidas nos centros de saúde "
          "públicos da cidade de Nampula, 2026»."),
        P("Eu, [Nome do(a) estudante], estudante da Licenciatura em Farmácia "
          "da Faculdade de Ciências de Saúde da Universidade Lúrio, sob a "
          "orientação de [Nome e grau académico do(a) orientador(a)], venho "
          "solicitar a dispensa do consentimento informado para o estudo "
          "acima referido, pelos motivos seguintes: o estudo é documental e "
          "retrospectivo e usa apenas os livros de registo da consulta da "
          "criança doente, as receitas e as fichas de stock de 2026; não há "
          "qualquer contacto com as crianças nem com os cuidadores, nem "
          "intervenção nos cuidados; o risco limita-se à quebra de "
          "confidencialidade, prevenida por uma ficha sem identificadores, "
          "por códigos para os centros e pela guarda segura dos dados; e "
          "seria impraticável localizar os cuidadores de 643 crianças "
          "atendidas ao longo de um ano, sem benefício para elas."),
        P("Comprometo-me a não iniciar a consulta dos registos antes do "
          "parecer favorável deste Comité e das autorizações institucionais, "
          "a respeitar a Declaração de Helsínquia e a legislação moçambicana "
          "sobre investigação em saúde humana, e a comunicar ao Comité "
          "qualquer alteração ao protocolo."),
        CAMPO("Assinatura do(a) estudante: _______________________________"),
        CAMPO("Assinatura do(a) orientador(a): ___________________________"),
        CAMPO("Contacto do(a) estudante: telefone +258 [preencher]; "
              "correio electrónico [preencher]"),
    ]),
    ("Pedido de autorização institucional", [
        CAMPO("Ao Senhor Director do Serviço Distrital de Saúde, Mulher e "
              "Acção Social da Cidade de Nampula"),
        CAMPO("C/c: Direcção Provincial de Saúde de Nampula; direcções dos "
              "centros de saúde"),
        CAMPO("Nampula, ___ de __________ de 2026"),
        P("Assunto: pedido de autorização para a realização de um estudo "
          "documental nos centros de saúde públicos da cidade de Nampula."),
        P("Eu, [Nome do(a) estudante], estudante da Licenciatura em Farmácia "
          "da Faculdade de Ciências de Saúde da Universidade Lúrio, venho "
          "solicitar autorização para consultar, nos centros de saúde "
          "públicos da cidade de Nampula com consulta da criança doente, os "
          "livros de registo dessa consulta, as receitas aviadas arquivadas "
          "nas farmácias, as fichas de stock da amoxicilina e os resumos "
          "mensais de 2026, e os registos de Dezembro de 2025 para o "
          "pré-teste. O estudo tem como objectivo avaliar a prescrição de "
          "antibióticos em crianças menores de cinco anos quanto à "
          "frequência, à classificação AWaRe da Organização Mundial da Saúde "
          "e à adequação às normas nacionais de Atenção Integrada às Doenças "
          "da Infância."),
        P("A consulta dos arquivos decorrerá de Fevereiro a Maio de 2027, "
          "com a verificação prévia e o pré-teste em Fevereiro e a recolha "
          "de Março a Maio, em horário "
          "acordado com cada direcção, sem retirar documentos das unidades e "
          "sem perturbar o atendimento. Não serão transcritos nomes nem "
          "números de processo; os centros serão identificados por letras e "
          "os prescritores apenas pela categoria profissional. O estudo só se "
          "iniciará depois do parecer favorável do Comité Institucional de "
          "Bioética para a Saúde da Universidade Lúrio, cuja cópia será "
          "anexada. Os resultados serão devolvidos ao SDSMAS e a cada centro "
          "num relatório e numa sessão de apresentação, de forma agregada e "
          "não punitiva."),
        CAMPO("Assinatura do(a) estudante: _______________________________"),
        CAMPO("Assinatura do(a) orientador(a): ___________________________"),
        CAMPO("Contacto: telefone +258 [preencher]"),
    ]),
    ("Termo de compromisso de confidencialidade da equipa de recolha", [
        P("Eu, abaixo assinado(a), membro da equipa de recolha do estudo "
          "sobre a prescrição de antibióticos em crianças menores de cinco "
          "anos nos centros de saúde da cidade de Nampula, comprometo-me a: "
          "não transcrever, fotografar nem divulgar nomes, números de "
          "processo ou outros dados que permitam identificar crianças, "
          "cuidadores ou profissionais de saúde; não retirar documentos das "
          "unidades sanitárias; guardar as fichas preenchidas em local "
          "fechado e entregá-las ao investigador no fim de cada dia; e não "
          "comentar fora da equipa qualquer informação a que tenha acesso "
          "durante a recolha. Tomei conhecimento de que a violação deste "
          "compromisso implica o meu afastamento imediato do estudo."),
        CAMPO("Nome: _________________________________________________"),
        CAMPO("Função no estudo: ______________________________________"),
        CAMPO("Assinatura: ______________________    Data: ___/___/2027"),
    ]),
]
