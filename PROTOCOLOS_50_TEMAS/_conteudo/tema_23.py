# -*- coding: utf-8 -*-
"""
TEMA 23. Conhecimentos e praticas das maes e cuidadoras sobre o tratamento da
diarreia infantil com sais de reidratacao oral e zinco (Cidade de Nampula).

Compor e validar:   python -X utf8 _motor/motor.py _conteudo/tema_23.py
Verificar fontes:   python -X utf8 _motor/refs.py verificar _conteudo/tema_23.py
"""
from blocos import (CAMPO, ESCALA, FORMULA, H3, LISTA, NOTA, P, PERG,
                    QUADRO, QUEBRA, TABELA)

NUMERO = 23
SLUG = "Diarreia_SRO_Zinco_Maes_Nampula"
TITULO = ("Conhecimentos e práticas de mães e cuidadoras sobre o tratamento "
          "da diarreia infantil com sais de reidratação oral e zinco na "
          "Cidade de Nampula, 2027")
DESENHO = ("Transversal descritivo e analítico, de base institucional, com "
           "inquérito por entrevista e observação estruturada da preparação "
           "da solução de reidratação oral")

AUTOR = "[Nome do(a) estudante]"
ORIENTADOR = "[Nome e grau académico do(a) orientador(a)]"

# ---------------------------------------------------------------- resumo --
RESUMO = (
    "A diarreia continua a ser uma das principais causas de doença e de morte "
    "nas crianças menores de cinco anos, e a província de Nampula regista "
    "surtos de cólera quase todos os anos. O tratamento recomendado, que "
    "combina a solução de reidratação oral com o zinco durante dez a catorze "
    "dias, depende de a solução ser preparada com o volume de água indicado e "
    "com água segura, de ser deitada fora ao fim de vinte e quatro horas e de "
    "o zinco ser dado até ao fim. Faltam dados moçambicanos sobre o que as "
    "mães sabem e fazem. O estudo tem por objectivo avaliar os "
    "conhecimentos e as práticas das mães e cuidadoras de crianças menores de "
    "cinco anos sobre o tratamento da diarreia com sais de reidratação oral e "
    "zinco, nas consultas da criança das unidades sanitárias da Cidade de "
    "Nampula. Trata-se de um estudo transversal, descritivo e analítico, de "
    "base institucional, com recolha de dados em Março e Abril de 2027. Serão convidadas 648 "
    "cuidadoras, seleccionadas por amostragem em duas etapas em doze unidades "
    "sanitárias. Os dados serão recolhidos por entrevista, com um questionário "
    "traduzido para Emakhuwa, e por observação estruturada da preparação da "
    "solução pela cuidadora, com material fornecido pelo estudo e uma lista "
    "de verificação de dez itens. Os conhecimentos e as práticas serão "
    "classificados pelos pontos de corte de Bloom, e a associação com a "
    "escolaridade e com outros factores será analisada por regressão de "
    "Poisson com variância robusta. Espera-se medir a distância entre o que "
    "as cuidadoras dizem saber e o que fazem, identificar os passos da "
    "preparação que mais falham e as razões do abandono do zinco, e orientar "
    "o aconselhamento nas unidades sanitárias, nas farmácias comunitárias e "
    "pelos agentes polivalentes elementares.")
PALAVRAS_CHAVE = ["cólera", "diarreia infantil", "Moçambique",
                  "solução de reidratação oral", "zinco"]
ABSTRACT = (
    "Diarrhoea remains one of the leading causes of illness and death in "
    "children under five, and Nampula province records cholera outbreaks "
    "almost every year. The recommended treatment, which combines oral "
    "rehydration solution with zinc for ten to fourteen days, depends on the "
    "solution being prepared with the stated volume of water and with safe "
    "water, on its being discarded after twenty-four hours, and on zinc being "
    "given until the end. Mozambican data on what mothers know and do are lacking. The study aims to assess the knowledge and practices of mothers "
    "and caregivers of children under five regarding the treatment of "
    "diarrhoea with oral rehydration salts and zinc, in the child clinics of "
    "health facilities in Nampula City. It is a cross-sectional, descriptive "
    "and analytical, facility-based study, with data collection in March and "
    "April 2027. "
    "A total of 648 caregivers will be invited, selected by two-stage "
    "sampling in twelve health facilities. Data will be collected through "
    "interviews, using a questionnaire translated into Emakhuwa, and through "
    "structured observation of the caregiver preparing the solution, with "
    "materials provided by the study and a ten-item checklist. Knowledge and "
    "practices will be classified using Bloom's cut-off points, and the "
    "association with schooling and other factors will be analysed by "
    "Poisson regression with robust variance. The study is expected to "
    "measure the gap between what caregivers say they know and what they do, "
    "to identify the preparation steps that most often fail and the reasons "
    "for abandoning zinc, and to guide counselling in health facilities, "
    "community pharmacies and by community health workers.")
KEYWORDS = ["childhood diarrhoea", "cholera", "Mozambique",
            "oral rehydration solution", "zinc"]

ABREVIATURAS = [
    ("AIDI", "Atenção Integrada às Doenças da Infância"),
    ("APE", "Agente Polivalente Elementar"),
    ("CAP", "Conhecimentos, atitudes e práticas"),
    ("CIBS-UniLúrio", "Comité Institucional de Bioética para a Saúde da "
                      "Universidade Lúrio"),
    ("DPS", "Direcção Provincial de Saúde"),
    ("IC95%", "Intervalo de confiança a 95%"),
    ("IDS", "Inquérito Demográfico e de Saúde"),
    ("IVC", "Índice de validade de conteúdo"),
    ("KR-20", "Fórmula 20 de Kuder-Richardson"),
    ("MISAU", "Ministério da Saúde"),
    ("OMS", "Organização Mundial da Saúde"),
    ("RP", "Razão de prevalências"),
    ("SDSMAS", "Serviço Distrital de Saúde, Mulher e Acção Social"),
    ("SNS", "Serviço Nacional de Saúde"),
    ("SPSS", "Statistical Package for the Social Sciences"),
    ("SRO", "Sais de reidratação oral"),
    ("STROBE", "Strengthening the Reporting of Observational Studies in "
               "Epidemiology"),
    ("UNICEF", "Fundo das Nações Unidas para a Infância"),
]

# ------------------------------------------------------------ referencias --
FONTES = {
    # -- magnitude global e tratamento
    "gbd2025": "GBD 2021 Diarrhoeal Diseases Collaborators. Global, regional, and national age-sex-specific burden of diarrhoeal diseases, their risk factors, and aetiologies, 1990-2021, for 204 countries and territories: a systematic analysis for the Global Burden of Disease Study 2021. Lancet Infect Dis. 2025;25(5):519-536. doi:10.1016/S1473-3099(24)00691-1. PMID: 39708822.",
    "omsdiarreia2024": "World Health Organization. Diarrhoeal disease: fact sheet [Internet]. Geneva: World Health Organization; 2024 [citado 2026 Set 19]. Disponível em: https://www.who.int/news-room/fact-sheets/detail/diarrhoeal-disease",
    "black2019": "Black R, Fontaine O, Lamberti L, Bhan M, Huicho L, El Arifeen S, et al. Drivers of the reduction in childhood diarrhea mortality 1980-2015 and interventions to eliminate preventable diarrhea deaths by 2030. J Glob Health. 2019;9(2):020801. doi:10.7189/jogh.09.020801. PMID: 31673345.",
    "omsunicef2004": "World Health Organization; United Nations Children's Fund. Clinical management of acute diarrhoea: WHO/UNICEF joint statement (WHO/FCH/CAH/04.7) [Internet]. Geneva; New York: World Health Organization; UNICEF; 2004 [citado 2026 Set 19]. Disponível em: https://www.who.int/publications/i/item/WHO_FCH_CAH_04.7",
    "zubairi2024": "Zubairi MBA, Naqvi SK, Ali AA, Sharif A, Salam RA, Hasnain Z, et al. Low-osmolarity oral rehydration solution for childhood diarrhoea: A systematic review and meta-analysis. J Glob Health. 2024;14:04166. doi:10.7189/jogh.14.04166. PMID: 39641334.",
    "lazzerini2016": "Lazzerini M, Wanzira H. Oral zinc for treating diarrhoea in children. Cochrane Database Syst Rev. 2016;12(12):CD005436. doi:10.1002/14651858.CD005436.pub5. PMID: 27996088.",
    "oms2024": "World Health Organization. Guideline on management of pneumonia and diarrhoea in children up to 10 years of age [Internet]. Geneva: World Health Organization; 2024 [citado 2026 Set 19]. Disponível em: https://www.who.int/publications/i/item/9789240103412",
    "kundu2025": "Kundu S, Das S, Medhagopal RG. An Update on WHO Recommendations on Childhood Pneumonia and Diarrhea (2024). Indian Pediatr. 2025;62(10):775-778. doi:10.1007/s13312-025-00173-8. PMID: 40839064.",
    "dhingra2020": "Dhingra U, Kisenge R, Sudfeld CR, Dhingra P, Somji S, Dutta A, et al. Lower-Dose Zinc for Childhood Diarrhea - A Randomized, Multicenter Trial. N Engl J Med. 2020;383(13):1231-1241. doi:10.1056/NEJMoa1915905. PMID: 32966722.",
    "msf2024": "Médecins Sans Frontières. Essential drugs: practical guidelines. Oral rehydration salts (ORS) [Internet]. Paris: Médecins Sans Frontières; 2024 [citado 2026 Set 19]. Disponível em: https://medicalguidelines.msf.org/en/viewport/EssDr/english/oral-rehydration-salts-ors-16684387.html",
    # -- Africa subsariana: cobertura, adesao e preparacao
    "seifu2024": "Seifu BL, Legesse BT, Yehuala TZ, Kase BF, Asmare ZA, Mulaw GF, et al. Factors associated with the co-utilization of oral rehydration solution and zinc for treating diarrhea among under-five children in 35 sub-saharan Africa countries: a generalized linear mixed effect modeling with robust error variance. BMC Public Health. 2024;24(1):1329. doi:10.1186/s12889-024-18827-w. PMID: 38755544.",
    "pradhan2025": "Pradhan SK, Pati S, Sethy P, Dhusiya HR, Panda A, Pandit D, et al. Adherence to oral zinc supplementation in the management of acute diarrhoeal disease among under-5 children: A systematic review and meta-analysis. Epidemiol Infect. 2025;153:e129. doi:10.1017/S0950268825100733. PMID: 41178278.",
    "greenland2016": "Greenland K, Chipungu J, Chilengi R, Curtis V. Theory-based formative research on oral rehydration salts and zinc use in Lusaka, Zambia. BMC Public Health. 2016;16:312. doi:10.1186/s12889-016-2984-2. PMID: 27067003.",
    "abolurin2021": "Abolurin OO, Olaleye AO, Adekoya AO. Addressing the Sub-Optimal Use of Oral Rehydration Solution for Childhood Diarrhoea in the Tropics: Findings From a Rural Setting in Nigeria. J Trop Pediatr. 2021;67(1). doi:10.1093/tropej/fmaa071. PMID: 33130901.",
    # -- Mocambique e Nampula
    "ine2024": "Instituto Nacional de Estatística; ICF. Moçambique Inquérito Demográfico e de Saúde 2022-23: relatório definitivo [Internet]. Maputo; Rockville: Instituto Nacional de Estatística; ICF; 2024 [citado 2026 Set 19]. Disponível em: https://dhsprogram.com/pubs/pdf/FR389/FR389.pdf",
    "salenciaferrao2025": "Salência-Ferrão J, Chissaque A, Manhique-Coutinho L, Kenga AN, Cassocera M, de Deus N. Inappropriate use of antibiotics in the management of diarrhoea in children under five years admitted with acute diarrhoea in four provinces of Mozambique 2014-2019. BMC Infect Dis. 2025;25(1):209. doi:10.1186/s12879-025-10597-z. PMID: 39939844.",
    "machava2022": "Machava NE, Salvador EM, Mulaudzi F. Assessment of diagnosis and treatment practices of diarrhoea in children under five in Maputo-Mozambique. Int J Afr Nurs Sci. 2022;17:100507. doi:10.1016/j.ijans.2022.100507. PMID: 36518099.",
    "sambo2022": "Sambo J, Bauhofer AFL, Boene SS, Djedje M, Júnior A, Pilale A, et al. Readiness of Mozambique Health Facilities to Address Undernutrition and Diarrhea in Children under Five: Indicators from 2018 and 2021 Survey Data. Healthcare (Basel). 2022;10(7). doi:10.3390/healthcare10071200. PMID: 35885727.",
    "ine2021": "Instituto Nacional de Estatística. IV Recenseamento Geral da População e Habitação 2017: resultados definitivos, província de Nampula [Internet]. Nampula: Instituto Nacional de Estatística; 2021 [citado 2026 Set 19]. Disponível em: http://www.sina.gov.mz/wp-content/uploads/2024/05/NAMPULA-RESUTADOS-DEFINITIVOS-DO-CENSO-2017.pdf",
    "bauhofer2021": "Bauhofer AFL, Cossa-Moiane ILC, Marques SDA, Guimarães ELAM, Munlela BA, Anapakala EM, et al. Intestinal protozoa in hospitalized under-five children with diarrhoea in Nampula - a cross-sectional analysis in a low-income setting in northern Mozambique. BMC Infect Dis. 2021;21(1):201. doi:10.1186/s12879-021-05881-7. PMID: 33622284.",
    "omsdon2023": "World Health Organization. Disease Outbreak News: cholera, Mozambique, 24 February 2023 [Internet]. Geneva: World Health Organization; 2023 [citado 2026 Set 19]. Disponível em: https://www.who.int/emergencies/disease-outbreak-news/item/2023-DON443",
    "sema2017": "Semá Baltazar C, Langa JP, Dengo Baloi L, Wood R, Ouedraogo I, Njanpop-Lafourcade BM, et al. Multi-site cholera surveillance within the African Cholera Surveillance Network shows endemicity in Mozambique, 2011-2015. PLoS Negl Trop Dis. 2017;11(10):e0005941. doi:10.1371/journal.pntd.0005941. PMID: 28991895.",
    "omsafro2024": "World Health Organization Regional Office for Africa. Responding to health needs in Mozambique in wake of Cyclone Chido [Internet]. Brazzaville: WHO Regional Office for Africa; 2024 [citado 2026 Set 19]. Disponível em: https://afro.who.int/countries/mozambique/photo-story/responding-health-needs-mozambique-wake-cyclone-chido",
    "omscolera2026": "World Health Organization. Multi-country outbreak of cholera: epidemiological update n.º 36, 30 April 2026 [Internet]. Geneva: World Health Organization; 2026 [citado 2026 Set 19]. Disponível em: https://cdn.who.int/media/docs/default-source/documents/emergencies/situation-reports/20260430_multi-country_outbreak-of-cholera_epidemiological_update_36.pdf?sfvrsn=562b4e33_3&download=true",
    "yewodiaw2026": "Yewodiaw TK, Getnet M, Bitewa MD, Endale HT. Spatial disparities and multilevel determinants of childhood diarrhea in Mozambique: Evidence from the 2022-2023 Demographic and Health Survey (DHS). PLoS One. 2026;21(5):e0330240. doi:10.1371/journal.pone.0330240. PMID: 42189868.",
    "demolis2018": "Démolis R, Botão C, Heyerdahl LW, Gessner BD, Cavailler P, Sinai C, et al. A rapid qualitative assessment of oral cholera vaccine anticipated acceptability in a context of resistance towards cholera intervention in Nampula, Mozambique. Vaccine. 2018;36(44):6497-6505. doi:10.1016/j.vaccine.2017.10.087. PMID: 29174106.",
    "kallander2019": "Källander K, Counihan H, Cerveau T, Mbofana F. Barriers on the pathway to survival for children dying from treatable illnesses in Inhambane province, Mozambique. J Glob Health. 2019;9(1):010809. doi:10.7189/jogh.09.010809. PMID: 31275569.",
    # -- enquadramento normativo mocambicano
    "misau2014": "Ministério da Saúde, Direcção Nacional de Saúde Pública, Departamento de Saúde da Mulher e Criança. Atenção Integrada às Doenças da Infância (AIDI): caderno de mapas para a atenção integrada à criança doente de 1 semana aos 2 meses e dos 2 meses aos 5 anos [Internet]. Maputo: Ministério da Saúde; 2014 [citado 2026 Set 19]. Disponível em: https://media.path.org/documents/MOH_IMCI_FLIPCHART_June_2015-PORT.pdf",
    "misau2016": "Ministério da Saúde, Direcção Nacional de Saúde Pública, Departamento de Epidemiologia. Manual de prevenção e controlo da cólera e de outras diarreias agudas. 4.ª ed [Internet]. Maputo: Ministério da Saúde; 2016 [citado 2026 Set 19]. Disponível em: https://www.afro.who.int/sites/default/files/2018-07/MANUAL%20DE%20COLERA%202017.pdf",
    "baltazar2022": "Baltazar CS, Pezzoli L, Baloi LD, Luiz N, Chitio JE, Capitine I, et al. Conditions to eliminate cholera in Mozambique - the pathway for the development of the national cholera plan. Pan Afr Med J. 2022;42:279. doi:10.11604/pamj.2022.42.279.36368. PMID: 36405663.",
    "guenther2017": "Guenther T, Sadruddin S, Finnegan K, Wetzler E, Ibo F, Rapaz P, et al. Contribution of community health workers to improving access to timely and appropriate case management of childhood fever in Mozambique. J Glob Health. 2017;7(1):010402. doi:10.7189/jogh.07.010402. PMID: 28400951.",
    "misau2023lnme": "Ministério da Saúde. Diploma Ministerial n.º 52/2023, de 19 de Abril: aprova a Lista Nacional de Medicamentos Essenciais. Boletim da República, I Série, n.º 75 [Internet]. Maputo: Imprensa Nacional de Moçambique; 2023 [citado 2026 Set 19]. Disponível em: https://anarme.gov.mz/download/diploma-ministerial-52-2023-de-19-de-abril-lista-nacional-de-medicamentos-essenciais/",
    "pramestutie2023": "Pramestutie HR, Kristina SA, Lazuardi L, Widayanti AW. Using the Simulated Patient Method to Evaluate the Community Pharmacy Management of Childhood Diarrhoea: A Systematic Review. Malays J Med Sci. 2023;30(5):52-69. doi:10.21315/mjms2023.30.5.5. PMID: 37928786.",
    "abegaz2016": "Abegaz TM, Belachew SA, Abebe TB, Gebresilassie BM, Teni FS, Woldie HG. Management of children's acute diarrhea by community pharmacies in five towns of Ethiopia: simulated client case study. Ther Clin Risk Manag. 2016;12:515-26. doi:10.2147/TCRM.S98474. PMID: 27103810.",
    # -- conhecimentos e praticas das cuidadoras (estado da arte)
    "desta2017": "Desta BK, Assimamaw NT, Ashenafi TD. Knowledge, Practice, and Associated Factors of Home-Based Management of Diarrhea among Caregivers of Children Attending Under-Five Clinic in Fagita Lekoma District, Awi Zone, Amhara Regional State, Northwest Ethiopia, 2016. Nurs Res Pract. 2017;2017:8084548. doi:10.1155/2017/8084548. PMID: 28912970.",
    "mekonnen2018": "Mekonnen GK, Mengistie B, Sahilu G, Mulat W, Kloos H. Caregivers' knowledge and attitudes about childhood diarrhea among refugee and host communities in Gambella Region, Ethiopia. J Health Popul Nutr. 2018;37(1):24. doi:10.1186/s41043-018-0156-y. PMID: 30466488.",
    "dhingra2018": "Dhingra D, Dabas A, Anand T, Pinnamaneni R. Maternal knowledge, attitude and practices during childhood diarrhoea. Trop Doct. 2018;48(4):298-300. doi:10.1177/0049475518787425. PMID: 30012081.",
    "kebede2019": "Kebede Fufa W, Berhe Gebremedhin G, Gebregergs GB, Marama Mokonnon T. Assessment of Poor Home Management Practice of Diarrhea and Associated Factors among Caregivers of Under-Five Years Children in Urban and Rural Residents of Doba Woreda, Ethiopia: Comparative Cross-Sectional Study. Int J Pediatr. 2019;2019:8345245. doi:10.1155/2019/8345245. PMID: 31275402.",
    "amu2022": "Amu EO, Olatona FA, Adeyemi BO, Adegbilero-Iwari OE. Childhood diarrhoea in southwestern Nigeria: Predictors of low osmolarity ORS and zinc use among mothers. J Taibah Univ Med Sci. 2022;17(6):1006-1013. doi:10.1016/j.jtumed.2022.05.003. PMID: 36212577.",
    "atnafu2024": "Atnafu S, Tariku A, Sisay M, Atnafu A. Zinc adherence among caregivers of under five children with diarrhea in Gondar City, Northwest Ethiopia. BMC Res Notes. 2024;17(1):254. doi:10.1186/s13104-024-06909-2. PMID: 39252082.",
    "nuzhat2025": "Nuzhat S, Islam MR, Al Fidah MF, Islam SB, Rahman MM, Paul S, et al. Maternal knowledge, attitude and practice regarding commercial oral rehydration salt solution: experience from a diarrhoeal disease hospital in Bangladesh. BMJ Paediatr Open. 2025;9(1). doi:10.1136/bmjpo-2024-003299. PMID: 39922602.",
    "islam2025": "Islam MR, Al Fidah MF, Bashar SJ, Amin R, Paul S, Kawser CA, et al. Qualitative approach to assess maternal knowledge, attitude and practice regarding oral rehydration solution preparation and administration among under-5 children suffering from diarrhoea in Dhaka, Bangladesh. BMJ Paediatr Open. 2025;9(1). doi:10.1136/bmjpo-2025-003577. PMID: 40835241.",
    "etokidem2023": "Etokidem AJ. AMBA CUP: Ensuring Accuracy in Measurement of Volume of Water for Salt Sugar Solution or Oral Rehydration Solution Preparation in Diarrhea Management. Ann Glob Health. 2023;89(1):65. doi:10.5334/aogh.4301. PMID: 37810607.",
    # -- metodos, estatistica, relato e etica
    "almanasreh2019": "Almanasreh E, Moles R, Chen TF. Evaluation of methods used for estimating content validity. Res Social Adm Pharm. 2019;15(2):214-221. doi:10.1016/j.sapharm.2018.03.066. PMID: 29606610.",
    "tsang2017": "Tsang S, Royse CF, Terkawi AS. Guidelines for developing, translating, and validating a questionnaire in perioperative and pain medicine. Saudi J Anaesth. 2017;11(Suppl 1):S80-S89. doi:10.4103/sja.SJA_203_17. PMID: 28616007.",
    "kuder1937": "Kuder GF, Richardson MW. The Theory of the Estimation of Test Reliability. Psychometrika. 1937;2(3):151-160. doi:10.1007/BF02288391",
    "bizuneh2024": "Bizuneh YB, Ferede YA, Berhe YW, Alemu WM, Zeleke TG. Assessment of knowledge, attitude, and practice regarding medical waste management among operation room personnel in a tertiary hospital. Ann Med Surg (Lond). 2024;86(9):5065-5071. doi:10.1097/MS9.0000000000002212. PMID: 39238965.",
    "elsaed2018": "El-Saed A, Noushad S, Tannous E, Abdirizak F, Arabi Y, Al Azzam S, et al. Quantifying the Hawthorne effect using overt and covert observation of hand hygiene at a tertiary care hospital in Saudi Arabia. Am J Infect Control. 2018;46(8):930-935. doi:10.1016/j.ajic.2018.02.025. PMID: 30072161.",
    "mchugh2012": "McHugh ML. Interrater reliability: the kappa statistic. Biochem Med (Zagreb). 2012;22(3):276-82. PMID: 23092060.",
    "zarei2024": "Zarei F, Dehghani A, Ratansiri A, Ghaffari M, Raina SK, Halimi A, et al. ChecKAP: A Checklist for Reporting a Knowledge, Attitude, and Practice (KAP) Study. Asian Pac J Cancer Prev. 2024;25(7):2573-2577. doi:10.31557/APJCP.2024.25.7.2573. PMID: 39068593.",
    "vonelm2007": "von Elm E, Altman DG, Egger M, Pocock SJ, Gøtzsche PC, Vandenbroucke JP. The Strengthening the Reporting of Observational Studies in Epidemiology (STROBE) statement: guidelines for reporting observational studies. Lancet. 2007;370(9596):1453-7. doi:10.1016/S0140-6736(07)61602-X. PMID: 18064739.",
    "chen2018": "Chen W, Qian L, Shi J, Franklin M. Comparing performance between log-binomial and robust Poisson regression models for estimating risk ratios under model misspecification. BMC Med Res Methodol. 2018;18(1):63. doi:10.1186/s12874-018-0519-5. PMID: 29929477.",
    "peduzzi1996": "Peduzzi P, Concato J, Kemper E, Holford TR, Feinstein AR. A simulation study of the number of events per variable in logistic regression analysis. J Clin Epidemiol. 1996;49(12):1373-9. doi:10.1016/s0895-4356(96)00236-3. PMID: 8970487.",
    "wma2025": "World Medical Association. World Medical Association Declaration of Helsinki: Ethical Principles for Medical Research Involving Human Participants. JAMA. 2025;333(1):71-74. doi:10.1001/jama.2024.21972. PMID: 39425955.",
    "lei3de2023": "República de Moçambique. Lei n.º 3/2023, de 8 de Junho: Lei de Investigação em Saúde Humana [Internet]. Maputo: Imprensa Nacional de Moçambique; 2023 [citado 2026 Set 19]. Disponível em: https://anarme.gov.mz/download/lei-3-2023-de-8-de-junho-lei-de-investigacao-em-saude-humana/",
}

SEMINAIS = {
    "omsunicef2004": ("Declaração conjunta da OMS e da UNICEF que introduziu a "
                      "SRO de baixa osmolaridade e a suplementação de zinco "
                      "como tratamento-padrão da diarreia infantil; é a norma "
                      "internacional de referência que o estudo usa para "
                      "definir as respostas correctas."),
    "misau2014": ("Caderno de mapas da AIDI do MISAU (Maio de 2014), norma "
                  "nacional em vigor para o tratamento da diarreia na criança "
                  "(Plano A e zinco durante 14 dias), que define as respostas "
                  "correctas do questionário."),
    "vonelm2007": ("Declaração original STROBE, norma de relato dos estudos "
                   "observacionais ainda em vigor."),
    "mchugh2012": ("Artigo de referência sobre a interpretação do kappa de "
                   "Cohen, usado para a concordância entre observadores na "
                   "lista de verificação da preparação."),
    "kuder1937": ("Artigo original que define a fórmula 20 de "
                  "Kuder-Richardson, usada para a fiabilidade da escala de "
                  "conhecimentos com itens dicotómicos."),
    "peduzzi1996": ("Estudo de simulação que fundamenta a regra de pelo menos "
                    "10 eventos por variável nos modelos de regressão para "
                    "desfechos binários."),
}

# ----------------------------------------------------- 1. introducao --------
INTRODUCAO = [
    P("A diarreia aguda continua a ser uma das principais causas de doença e "
      "de morte na infância. Segundo o estudo Global Burden of Disease de "
      "2021, as doenças diarreicas causaram nesse ano cerca de 1,17 milhões "
      "de mortes em todas as idades, menos 60,3% do que em 1990, e a descida "
      "foi mais acentuada nas crianças menores de cinco anos, com uma redução "
      "de 79,2% das mortes; ainda assim, dos 59,0 milhões de anos de vida "
      "ajustados por incapacidade atribuídos à diarreia, 30,9 milhões "
      "recaíram nesta faixa etária {gbd2025}. A Organização Mundial da Saúde "
      "(OMS) estima que a diarreia mate todos os anos cerca de 443.832 "
      "crianças menores de cinco anos, que seja a terceira causa de morte "
      "entre um e 59 meses de idade e que ocorram perto de 1,7 mil milhões de "
      "episódios infantis por ano {omsdiarreia2024}."),
    P("A descida da mortalidade deve-se em boa parte a intervenções simples "
      "e baratas. Uma modelação para 50 países de rendimento baixo e médio "
      "atribuiu 49,7% da redução da mortalidade por diarreia entre 1980 e "
      "2015 ao tratamento, que inclui os sais de reidratação oral (SRO), o "
      "zinco e os antibióticos para a disenteria, e à vacina contra o "
      "rotavírus, e estimou que levar estas "
      "intervenções a 90% de cobertura reduziria em 74,1% as mortes infantis "
      "por diarreia até 2030 {black2019}. Desde 2004, a OMS e o Fundo das "
      "Nações Unidas para a Infância (UNICEF) recomendam a combinação da SRO "
      "de baixa osmolaridade com a suplementação de zinco {omsunicef2004}. A "
      "SRO de baixa osmolaridade reduz a duração da diarreia aguda em relação "
      "à fórmula anterior {zubairi2024}, e o zinco encurta em cerca de meio "
      "dia a duração média dos episódios nas crianças com mais de seis meses "
      "e diminui a proporção de diarreias que persistem até ao sétimo dia "
      "{lazzerini2016}. Estes benefícios dependem, porém, de a solução ser "
      "preparada com o volume de água indicado e com água segura, e de o "
      "zinco ser tomado até ao fim do esquema."),
    P("Na África subsariana, a cobertura do tratamento recomendado continua "
      "baixa. Numa análise dos inquéritos demográficos e de saúde de 35 "
      "países, com 44.341 crianças com diarreia, só 43,58% receberam SRO e "
      "zinco em conjunto, e a co-utilização dependeu, entre outros factores, da escolaridade materna, da riqueza do agregado e da distância percebida à unidade sanitária {seifu2024}. Uma meta-análise estimou a adesão ao zinco em 63,45% "
      "no esquema de dez dias e em apenas 34,58% no de catorze dias "
      "{pradhan2025}. A qualidade da preparação é ainda menos conhecida: em "
      "Lusaka, só quatro de catorze cuidadoras observadas em casa prepararam "
      "correctamente a solução, sobretudo por erros na medição da água "
      "{greenland2016}, e numa zona rural da Nigéria apenas 22,1% das mães "
      "que afirmavam saber preparar a SRO o fizeram correctamente "
      "{abolurin2021}."),
    P("Em Moçambique, o Inquérito Demográfico e de Saúde (IDS) de 2022-23 "
      "encontrou diarreia nas duas semanas anteriores em 9% das crianças "
      "menores de cinco anos, com um pico de 15% entre os 12 e os 23 meses. "
      "Das crianças com diarreia, 49,8% receberam SRO, 42,9% receberam zinco "
      "e apenas 29,4% receberam os dois; 20,5% não receberam qualquer "
      "tratamento e só 10% beberam mais líquidos do que o habitual, como se "
      "recomenda {ine2024}. Nos serviços, os dados mostram desvios às normas: "
      "numa vigilância hospitalar em quatro províncias, 93,2% das crianças "
      "internadas com diarreia aguda receberam antibióticos "
      "{salenciaferrao2025}, e nos registos de Maputo de 2015 a 2019 a SRO "
      "foi o tratamento principal em 79% dos casos e os antibióticos em 21% "
      "{machava2022}. Na avaliação de 2018 das 1.644 unidades sanitárias "
      "públicas, a pontuação mediana de prontidão dos serviços de diarreia "
      "infantil foi de 72,2%, com as maiores falhas em recursos humanos, "
      "normas e formação {sambo2022}."),
    P("Nampula é a província mais populosa do país, com 5.758.920 habitantes "
      "recenseados em 2017, 20,6% da população nacional {ine2021}. No IDS de "
      "2022-23, a prevalência da diarreia na província foi de 6,4% e "
      "procurou-se aconselhamento ou tratamento para 73% das crianças "
      "doentes, mas só 32,6% receberam SRO e zinco e 22,9% não receberam "
      "tratamento algum {ine2024}. A cólera acrescenta um risco "
      "próprio: é endémica no país, com surtos anuais na estação quente e "
      "chuvosa, de Outubro a Abril, sobretudo nas províncias de Nampula, Cabo "
      "Delgado, Sofala e Tete {omsdon2023}, e na vigilância de 2011 a 2015 "
      "residir no distrito da Cidade de Nampula foi um factor "
      "independentemente associado à cólera confirmada {sema2017}. Em "
      "28 de Outubro de 2024 foi declarado na província um surto que, na nota da OMS de 31 de Dezembro, somava 260 casos e 20 óbitos {omsafro2024} e, nos 28 dias anteriores a 29 de Março de 2026, Nampula concentrou 45% dos "
      "casos de cólera notificados no país {omscolera2026}."),
    P("Os estudos moçambicanos disponíveis medem a cobertura declarada do "
      "tratamento em inquéritos domiciliários ou descrevem a prática dos "
      "serviços a partir de registos; nenhum dos encontrados avaliou o que as "
      "mães sabem sobre a SRO e o zinco, nem observou o modo como preparam a "
      "solução. A distinção importa, porque o conhecimento declarado pode "
      "esconder erros práticos: em Daca, 97,4% das mães afirmavam conhecer o "
      "modo de preparar a SRO, mas só 2,9% conheciam todos os passos "
      "recomendados {nuzhat2025}. O presente estudo propõe-se avaliar os "
      "conhecimentos e as práticas das mães e cuidadoras de crianças menores "
      "de cinco anos sobre o tratamento da diarreia com SRO e zinco, "
      "combinando um inquérito nas consultas da criança com a observação "
      "estruturada da preparação da solução."),
]

# ----------------------------------------------------- 2. problema ----------
PROBLEMA = [
    P("O problema que o estudo aborda é a distância, provavelmente grande, "
      "entre a disponibilidade do tratamento da diarreia e a sua utilização "
      "correcta em casa. Segundo o programa nacional descrito no IDS, os "
      "pacotes de SRO e zinco são distribuídos em todas as unidades "
      "sanitárias, farmácias e agentes de saúde comunitários do país "
      "{ine2024}, e a norma nacional de Atenção Integrada às Doenças da "
      "Infância (AIDI) manda ensinar à mãe as quatro regras do tratamento em "
      "casa: dar líquidos adicionais, dar zinco durante 14 dias, continuar a "
      "alimentar e saber quando voltar {misau2014}. Contudo, na província de "
      "Nampula, só um terço das crianças com diarreia recebe os dois "
      "medicamentos e mais de um quinto não recebe tratamento {ine2024}. "
      "Mesmo quando a SRO chega a casa, ignora-se se é bem preparada, bem "
      "conservada e dada na quantidade certa."),
    P("Uma solução mal preparada perde segurança ou eficácia. Os erros de "
      "medição descritos em Lusaka produziram sobretudo soluções demasiado "
      "concentradas {greenland2016}, e foi a preocupação com a carga de sódio "
      "e com casos de hipernatremia que levou à substituição da SRO padrão "
      "pela fórmula de baixa osmolaridade {zubairi2024}; uma solução "
      "demasiado diluída, pelo contrário, repõe menos sais do que o "
      "necessário. A água não tratada e o recipiente destapado podem "
      "contaminar a solução, e a solução preparada deve ser usada dentro de 24 "
      "horas {msf2024}. Numa cidade em que a cólera é endémica, estes erros "
      "domésticos somam-se à transmissão pela água e pelas mãos. O abandono "
      "precoce do zinco, frequente quando o esquema é de 14 dias "
      "{pradhan2025}, reduz por sua vez o benefício do tratamento."),
    P("O contexto social torna o problema mais sensível. Em Nampula, durante "
      "campanhas anteriores de cloração de poços, agentes de saúde foram "
      "atacados por serem acusados de espalhar a cólera {demolis2018}, o que "
      "mostra que a compreensão comunitária do tratamento e da prevenção da "
      "diarreia pesa na resposta aos surtos. Em Inhambane, 9,4% das mortes de "
      "crianças por doença aguda foram atribuídas à diarreia e, em 35,3% dos "
      "casos, a cuidadora só se apercebeu da doença quando surgiram sinais de "
      "gravidade {kallander2019}, o que aponta o domicílio como o lugar onde "
      "se perde mais tempo e onde o conhecimento da cuidadora decide o "
      "desfecho."),
    P("Faltam, portanto, quatro informações para orientar o aconselhamento: "
      "o nível de conhecimentos das cuidadoras sobre a diarreia, a "
      "desidratação, a SRO e o zinco; a proporção que prepara correctamente a "
      "solução e os passos que mais falham; a cobertura do tratamento "
      "combinado e a adesão ao zinco no último episódio, com as razões do "
      "abandono; e os factores associados a um bom conhecimento e a uma "
      "preparação correcta, em particular a escolaridade materna e o facto de "
      "a cuidadora ter assistido alguma vez a uma demonstração por um "
      "profissional. Sem estes dados, as unidades sanitárias, as farmácias "
      "comunitárias e os agentes polivalentes elementares (APE) não sabem que "
      "mensagens reforçar nem a quem dirigi-las."),
]
PERGUNTA = ("Qual é o nível de conhecimentos das mães e cuidadoras de crianças "
            "menores de cinco anos sobre o tratamento da diarreia com sais de "
            "reidratação oral e zinco, com que exactidão preparam a solução de "
            "reidratação oral quando observadas, e que factores se associam a "
            "estes resultados, nas consultas da criança da Cidade de Nampula, "
            "em 2027?")
DELIMITACAO = [
    P("O estudo realiza-se nas unidades sanitárias do Serviço Nacional de "
      "Saúde (SNS) da Cidade de Nampula que oferecem consultas da criança "
      "sadia e da criança doente, seleccionadas conforme descrito na "
      "metodologia. A população é constituída pelas mães e outras cuidadoras "
      "principais, com 18 ou mais anos, de crianças menores de cinco anos "
      "atendidas nessas consultas. A recolha decorre em Março e Abril de "
      "2027, num estudo que se estende de Outubro de 2026 a Setembro de "
      "2027."),
    P("O objecto são os conhecimentos das cuidadoras sobre a diarreia e o seu "
      "tratamento com SRO e zinco, a preparação da solução observada durante "
      "uma demonstração, as práticas declaradas no último episódio de "
      "diarreia dos três meses anteriores e a adesão ao zinco nesse episódio. "
      "Ficam de fora a qualidade farmacêutica dos SRO e do zinco disponíveis "
      "no mercado, a prática dos profissionais de saúde e das farmácias, as "
      "crianças internadas e a observação do tratamento no domicílio, que "
      "exigiria outro desenho."),
]

# ----------------------------------------------------- 3. objectivos --------
OBJECTIVO_GERAL = (
    "Avaliar os conhecimentos e as práticas das mães e cuidadoras de crianças "
    "menores de cinco anos sobre o tratamento da diarreia com sais de "
    "reidratação oral e zinco, nas consultas da criança das unidades "
    "sanitárias da Cidade de Nampula, em 2027.")
OBJECTIVOS_ESPECIFICOS = [
    "Determinar o nível de conhecimentos das cuidadoras sobre a diarreia, os "
    "sinais de desidratação e de perigo e o tratamento com sais de "
    "reidratação oral e zinco, segundo os pontos de corte de Bloom.",
    "Determinar a proporção de cuidadoras que preparam correctamente a "
    "solução de reidratação oral, por observação estruturada, e descrever os "
    "erros em cada passo da preparação.",
    "Estimar a cobertura do tratamento com sais de reidratação oral e zinco e "
    "a adesão ao zinco entre as cuidadoras cuja criança teve diarreia nos "
    "três meses anteriores, e identificar as razões da não adesão.",
    "Analisar a associação entre a escolaridade materna, a demonstração "
    "prévia por um profissional de saúde e outras características das "
    "cuidadoras e o nível bom de conhecimentos e a preparação correcta da "
    "solução.",
]

# ----------------------------------------------------- 4. hipoteses ---------
HIPOTESES_INTRO = [
    P("As hipóteses referem-se à componente analítica, isto é, ao objectivo "
      "específico 4. A literatura associa de forma consistente a escolaridade "
      "materna e o aconselhamento recebido a melhores conhecimentos e "
      "práticas {desta2017,atnafu2024,nuzhat2025}, mas não há dados sobre a "
      "preparação observada em Moçambique; por isso, as hipóteses "
      "alternativas são bilaterais e serão testadas ao nível de significância "
      "de 5%. Os objectivos 1 a 3 são descritivos e orientam-se pelas "
      "questões de investigação apresentadas a seguir."),
]
HIPOTESES = [
    ("H0 (objectivo específico 4, escolaridade)",
     "a proporção de cuidadoras que preparam correctamente a solução de "
     "reidratação oral não difere entre as que têm escolaridade secundária ou "
     "superior e as que têm escolaridade primária ou nenhuma."),
    ("H1 (objectivo específico 4, escolaridade)",
     "a proporção de cuidadoras que preparam correctamente a solução difere "
     "entre os dois grupos de escolaridade."),
    ("H0 (objectivo específico 4, demonstração prévia)",
     "a proporção de preparação correcta não difere entre as cuidadoras que "
     "já assistiram a uma demonstração feita por um profissional de saúde e "
     "as que nunca assistiram."),
    ("H1 (objectivo específico 4, demonstração prévia)",
     "a proporção de preparação correcta difere entre os dois grupos."),
    ("H0 (objectivo específico 4, conhecimentos e prática)",
     "o nível bom de conhecimentos não se associa à preparação correcta da "
     "solução, depois de ajustamento para a escolaridade, a demonstração "
     "prévia e as restantes variáveis do modelo."),
    ("H1 (objectivo específico 4, conhecimentos e prática)",
     "o nível bom de conhecimentos associa-se à preparação correcta da "
     "solução, depois do mesmo ajustamento."),
]
QUESTOES = [
    "Que proporção das cuidadoras tem conhecimentos bons, moderados e fracos "
    "sobre a diarreia, a desidratação, a SRO e o zinco, e que itens são "
    "menos conhecidos?",
    "Que proporção prepara correctamente a solução quando observada, e em "
    "que passos (higiene, água, volume, saqueta, dissolução, conservação) se "
    "concentram os erros?",
    "No último episódio de diarreia, quantas crianças receberam SRO e zinco, "
    "quantas completaram o zinco e por que razões o interromperam?",
]

# ----------------------------------------------------- 5. justificativa -----
JUSTIFICATIVA_INTRO = [
    P("A escolha do tema responde a uma combinação rara de peso da doença, "
      "tratamento barato e eficaz e ausência de dados locais sobre o elo mais "
      "frágil da cadeia, que é a execução do tratamento pela cuidadora. A "
      "diarreia continua a matar crianças que poderiam ser tratadas em casa "
      "{omsdiarreia2024} e, em Nampula, a cólera torna cada episódio de "
      "diarreia aquosa uma questão de saúde pública {omsdon2023}."),
]
JUSTIFICATIVA = {
    "cientifica": [
        P("Os inquéritos demográficos e de saúde medem se a criança recebeu "
          "SRO e zinco, mas não se a solução foi bem preparada nem se o zinco "
          "foi tomado até ao fim {ine2024,seifu2024}. A evidência sobre a "
          "exactidão da preparação vem de poucos estudos, quase todos "
          "baseados na declaração da mãe e realizados na Ásia ou na Nigéria "
          "{nuzhat2025,abolurin2021}, e a única observação directa encontrada "
          "na África Austral envolveu catorze cuidadoras {greenland2016}. Um "
          "estudo com observação estruturada, numa amostra com poder "
          "calculado, produz a primeira estimativa moçambicana da "
          "preparação correcta e permite medir a distância entre o que a mãe "
          "diz saber e o que faz."),
        P("O estudo chega também num momento de transição normativa: a OMS "
          "baixou em Dezembro de 2024 a dose de zinco recomendada, por "
          "provocar menos vómitos {oms2024,dhingra2020}, enquanto a "
          "norma nacional "
          "mantém meio comprimido ou um comprimido durante 14 dias "
          "{misau2014}. Conhecer as razões actuais do abandono do zinco, entre "
          "as quais os vómitos, ajuda a avaliar o impacto esperado da mudança "
          "de dose quando for adoptada no país."),
    ],
    "academica": [
        P("Para a Licenciatura em Farmácia da Faculdade de Ciências de Saúde "
          "da Universidade Lúrio (UniLúrio), o tema cruza a farmácia comunitária, a "
          "saúde pública e o uso racional do medicamento. A SRO e o zinco "
          "são medicamentos essenciais cuja eficácia depende do "
          "aconselhamento na dispensa, e os estudos com cliente simulado "
          "mostram que as farmácias nem sempre recomendam a SRO nem dão a informação necessária "
          "{pramestutie2023,abegaz2016}. O protocolo treina o estudante na "
          "construção e validação de um instrumento, na observação "
          "estruturada com controlo da concordância entre observadores e na "
          "análise de dados de uma amostra por conglomerados."),
    ],
    "social": [
        P("O benefício social é directo. Todas as cuidadoras observadas "
          "recebem, no fim, aconselhamento correctivo e uma demonstração da "
          "preparação correcta, e as crianças com sinais de desidratação são "
          "encaminhadas de imediato ao clínico. Os resultados indicarão às "
          "unidades sanitárias os passos da preparação que mais falham, "
          "permitindo mensagens mais curtas e mais precisas nas palestras e "
          "nas consultas, e poderão alimentar materiais em Emakhuwa para as "
          "mães sem escolaridade secundária, cujos filhos receberam o "
          "tratamento combinado com menos frequência no IDS {ine2024}."),
    ],
    "politica": [
        P("O estudo produz indicadores úteis para o programa de saúde da "
          "criança e para a resposta à cólera. O plano nacional de "
          "eliminação da cólera, alinhado com o roteiro global para 2030, "
          "assenta na água e saneamento, nos cuidados de saúde, na vigilância "
          "e na promoção da saúde e da higiene {baltazar2022}, e o manual "
          "nacional de controlo da cólera exige que o técnico explique à "
          "família como preparar a solução no momento da alta {misau2016}. A "
          "proporção de cuidadoras que prepara a solução correctamente é um "
          "indicador directo da eficácia desse aconselhamento. Os resultados "
          "serão devolvidos à Direcção Provincial de Saúde (DPS) e ao Serviço "
          "Distrital de Saúde, Mulher e Acção Social (SDSMAS) da Cidade de "
          "Nampula para apoiar a formação dos profissionais e dos APE na "
          "AIDI."),
    ],
}

# ----------------------------------------------------- 6. revisao -----------
REVISAO = [
    ("Diarreia aguda na criança: conceito, formas clínicas e definições "
     "operacionais", [
        P("A OMS define diarreia como a emissão de três ou mais dejecções "
          "moles ou líquidas por dia, ou mais frequentes do que o habitual "
          "para a pessoa, e distingue três formas clínicas: a diarreia aquosa "
          "aguda, que inclui a cólera, a diarreia sanguinolenta aguda ou "
          "disenteria, e a diarreia persistente, que dura 14 dias ou mais. A "
          "ameaça mais grave é a desidratação, resultante da perda de água e "
          "de sais pelas fezes e pelos vómitos {omsdiarreia2024}. A norma "
          "nacional classifica a criança com diarreia pelo grau de "
          "desidratação, a partir de sinais como a letargia, os olhos "
          "encovados, a capacidade de beber e o sinal da prega, e associa a "
          "cada classificação um plano de tratamento: o Plano A, em casa, para "
          "a criança sem desidratação; o Plano B, com SRO na unidade "
          "sanitária, para a criança com sinais de desidratação; e o Plano C, com líquidos "
          "por via endovenosa, para a desidratação grave {misau2014}."),
        P("Para este estudo, episódio de diarreia é o que a cuidadora refere "
          "como três ou mais dejecções moles ou líquidas em 24 horas na "
          "criança índice, nos três meses anteriores à entrevista. Tratamento "
          "combinado é a administração de SRO e de zinco no mesmo episódio. "
          "Adesão ao zinco é a toma diária durante pelo menos 10 dias, o "
          "limite inferior das durações fixadas pelas normas nacionais, de 10 "
          "a 14 dias {misau2014,misau2016}. "
          "Preparação correcta da solução é o cumprimento simultâneo dos "
          "cinco itens críticos da lista de verificação descrita na "
          "metodologia."),
    ]),
    ("Magnitude, causas e consequências da diarreia infantil", [
        P("Apesar da descida da mortalidade, a diarreia continua a figurar "
          "entre as maiores causas de perda de saúde infantil. Em 2021, os "
          "principais factores de risco dos anos de vida ajustados por "
          "incapacidade perdidos por diarreia foram o baixo peso ao nascer e "
          "a prematuridade nos recém-nascidos, a falha de crescimento nas "
          "crianças pequenas e a água insegura e o saneamento deficiente nas "
          "crianças mais velhas e nos adultos; nas crianças "
          "menores de cinco anos, o rotavírus foi responsável por 35,2% das "
          "mortes por diarreia e *Shigella* por 24,0% {gbd2025}. A OMS estima "
          "que o zinco reduza em 25% a duração dos episódios e em 30% o volume "
          "das fezes {omsdiarreia2024}, e a revisão Cochrane indica que o "
          "efeito é maior nas crianças com sinais de desnutrição, em quem a "
          "diarreia encurta cerca de um dia {lazzerini2016}."),
        P("Em Moçambique, a diarreia e a desnutrição alimentam-se "
          "mutuamente. Numa vigilância hospitalar de 2014 a 2019 em quatro "
          "províncias, 28,8% das crianças internadas com diarreia tinham "
          "baixo peso e 49,4% tinham menos de um ano {salenciaferrao2025}. No "
          "Hospital Central de Nampula, *Cryptosporidium* (13,9%) e *Giardia "
          "lamblia* (9,1%) foram os protozoários mais frequentes nas crianças "
          "internadas com diarreia, e o primeiro associou-se ao analfabetismo "
          "da cuidadora e à desnutrição {bauhofer2021}. Na análise multinível do IDS de "
          "2022-23, a escolaridade materna associou-se a menor probabilidade "
          "de diarreia {yewodiaw2026}."),
        P("A cólera é a forma de diarreia aquosa com maior impacto nos "
          "serviços. O manual nacional descreve epidemias de grande dimensão, "
          "como a de 2009, com 19.549 casos, e refere que a doença se "
          "concentra em distritos endémicos, entre os quais a Cidade de "
          "Nampula, onde foi administrada pela primeira vez no país a vacina "
          "oral contra a cólera, em 2016, em bairros com casos e óbitos "
          "repetidos {misau2016}. A vigilância de 2011 a 2015 registou uma "
          "letalidade de 1,2% nos casos suspeitos e identificou a fonte de "
          "água de beber como factor de risco {sema2017}."),
    ]),
    ("Tratamento da diarreia com SRO e zinco: normas e evidência", [
        P("A declaração conjunta da OMS e da UNICEF de 2004 introduziu a SRO "
          "de baixa osmolaridade e o zinco como tratamento-padrão "
          "{omsunicef2004}, com 20 mg de zinco por dia durante 10 a 14 dias "
          "{dhingra2020}. A revisão sistemática encomendada pela OMS para a "
          "actualização das directrizes confirmou que a SRO com osmolaridade "
          "de 245 ou menos reduz a duração da diarreia e o consumo de SRO em "
          "relação à fórmula de 311 {zubairi2024}. A SRO não trava a diarreia, "
          "repõe a água e os sais perdidos, e só o faz com a concentração "
          "prevista; as instruções de uso mandam dissolver a saqueta num "
          "litro de água limpa e usar a solução dentro de 24 horas {msf2024}. "
          "Na falta de SRO, o manual "
          "nacional ensina uma mistura caseira de um litro de água com oito "
          "colheres de chá de açúcar e meia colher de chá de sal "
          "{misau2016}."),
        P("A dose e a duração do zinco variam entre documentos, o que tem "
          "consequências para a definição das respostas correctas. O caderno "
          "de mapas da AIDI indica meio comprimido por dia até aos seis meses "
          "e um comprimido a partir dos seis meses, durante 14 dias "
          "{misau2014}, sem indicar a dosagem do comprimido; o manual "
          "nacional da cólera fixa 10 mg por dia abaixo dos seis meses e 20 mg "
          "a partir dessa idade, durante 10 dias {misau2016}, o que "
          "corresponde ao meio comprimido e ao comprimido de 20 mg. Em "
          "Dezembro de 2024, a OMS publicou uma nova directriz {oms2024} que "
          "sugere, para as crianças até aos 10 anos com diarreia aquosa aguda "
          "ou persistente, 5 mg de zinco por dia até 14 dias, uma "
          "recomendação condicional com evidência de baixa certeza "
          "{kundu2025}. A mudança apoia-se num ensaio com 4.500 crianças dos "
          "6 aos 59 meses da Índia e da Tanzânia, em que os vómitos nos 30 "
          "minutos seguintes à toma ocorreram em 19,3% com 20 mg e em 13,7% "
          "com 5 mg, sem perda de eficácia {dhingra2020}. Como as normas "
          "moçambicanas em vigor à data do protocolo são as da AIDI e do "
          "manual da cólera, o estudo aceita como correcta a resposta de 10 a "
          "14 dias, regista o número exacto referido e usa o mesmo intervalo "
          "na definição de adesão."),
        P("Nas quatro regras do tratamento em casa da AIDI, os líquidos "
          "adicionais incluem a SRO, dada com copo em pequenos goles após cada dejecção, "
          "e a amamentação mais frequente; o zinco pode ser dissolvido em "
          "leite materno, SRO ou água limpa {misau2014}. Os antibióticos "
          "reservam-se para a disenteria e para a cólera, e a sua utilização "
          "generalizada nos serviços moçambicanos {salenciaferrao2025} sugere "
          "que também as famílias podem esperar um antibiótico em vez da SRO, "
          "como descrito no Bangladesh, onde 24,6% das mães consideravam os "
          "antibióticos mais úteis do que a SRO {nuzhat2025}."),
    ]),
    ("Enquadramento normativo e serviços em Moçambique", [
        P("O tratamento da diarreia infantil em Moçambique segue a AIDI do "
          "Ministério da Saúde (MISAU), aplicada nas consultas da criança das "
          "unidades sanitárias do SNS {misau2014}. Desde 2010, a gestão comunitária "
          "integrada de casos é assegurada pelos APE, que tratam a diarreia, "
          "a malária e a pneumonia nas comunidades afastadas; na província de "
          "Nampula, 87,1% das crianças com febre levadas a tratamento nas "
          "áreas abrangidas foram primeiro a um APE {guenther2017}. Os APE são "
          "por isso uma via essencial para o aconselhamento sobre a SRO e o "
          "zinco, sobretudo na periferia da cidade."),
        P("A Lista Nacional de Medicamentos Essenciais, aprovada em 2023, "
          "define os medicamentos que o SNS adquire e distribui por nível de "
          "atenção {misau2023lnme}. A forma farmacêutica e a dosagem do zinco "
          "e dos SRO efectivamente disponíveis nas unidades seleccionadas "
          "serão confirmadas na fase de preparação, porque a mudança de dose "
          "proposta pela OMS {oms2024} poderá exigir revisão da lista e dos "
          "materiais de aconselhamento. No IDS, entre as crianças com diarreia "
          "levadas a aconselhamento ou tratamento, a fonte foi o sector "
          "público em 92,5% dos casos, o médico tradicional em 4,6% e a "
          "farmácia privada em 1,7% {ine2024}."),
        P("A farmácia comunitária pode ter, ainda assim, um papel maior do que essa proporção sugere, porque é uma fonte alternativa de SRO e de zinco quando a unidade sanitária está em ruptura e porque nela se decide a dispensa de outros medicamentos para a diarreia. Uma revisão de "
          "estudos com cliente simulado verificou que só em três de oito "
          "estudos os farmacêuticos recomendaram a SRO para a diarreia "
          "infantil {pramestutie2023}, e na Etiópia 85,0% das visitas "
          "simuladas terminaram com dispensa de pelo menos um medicamento, "
          "com uma média de 1,99 medicamentos por visita {abegaz2016}. O "
          "estudo regista, por isso, a fonte de obtenção da SRO e do zinco e "
          "quem ensinou a cuidadora a preparar a solução."),
    ]),
    ("Conhecimentos e práticas das cuidadoras e seus determinantes", [
        P("Os estudos africanos descrevem um conhecimento parcial e uma "
          "prática ainda pior. Na Etiópia, 56,2% das cuidadoras de uma "
          "consulta de menores de cinco anos tinham bom conhecimento e só "
          "37,6% boa prática no tratamento domiciliário, ambos definidos por "
          "uma pontuação igual ou superior à média; apenas 18,1% "
          "sabiam que a SRO repõe os líquidos perdidos, e 64,6% julgavam que "
          "ela trava a diarreia {desta2017}. Num estudo comparativo, a má "
          "prática domiciliária atingiu 55,8% das cuidadoras urbanas e 85,6% "
          "das rurais, e a dificuldade em preparar a SRO associou-se a má "
          "prática nos dois meios {kebede2019}. Em Lagos, só 10,4% das mães "
          "conheciam a SRO de baixa osmolaridade, e 53,3% conheciam o zinco "
          "{amu2022}."),
        P("A preparação da solução é o ponto mais frágil. Na Índia, só 50,4% "
          "das mães sabiam prepará-la e 55,2% administrá-la {dhingra2018}; no "
          "Bangladesh, entrevistas em profundidade revelaram mães que não "
          "sabiam a quantidade de pó nem a de água a usar {islam2025}. O "
          "recipiente de medida é parte do problema: as garrafas de "
          "refrigerante, muito usadas para medir um litro, são difíceis de "
          "limpar e mudam de tamanho com frequência, o que confunde as "
          "cuidadoras com menor numeracia {etokidem2023}."),
        P("Quanto ao zinco, a adesão ao esquema completo é o maior desafio. Em "
          "Gondar, só 35% das cuidadoras completaram o zinco; o bom "
          "conhecimento e o aconselhamento recebido associaram-se a maior "
          "adesão, e os efeitos adversos a menor adesão {atnafu2024}. A "
          "meta-análise de dez estudos identificou como determinantes a "
          "escolaridade da cuidadora, o aconselhamento pelo profissional, a "
          "aceitabilidade do medicamento e as dificuldades económicas "
          "{pradhan2025}. A interrupção quando a diarreia pára, os vómitos e "
          "a recusa da criança são, por isso, as razões a explorar."),
        P("Os determinantes repetem-se entre estudos. A escolaridade materna "
          "associa-se ao conhecimento, à prática e à co-utilização de SRO e "
          "zinco {desta2017,nuzhat2025,seifu2024}; a informação recebida numa "
          "unidade sanitária associa-se a melhor conhecimento "
          "{mekonnen2018}; e a exposição aos meios de comunicação, a riqueza e "
          "a proximidade dos serviços influenciam o uso do tratamento "
          "{seifu2024}. Em Moçambique, a co-utilização de SRO e zinco foi de "
          "24,9% nos filhos de mães com escolaridade primária e de 39,3% nos "
          "de mães com escolaridade secundária {ine2024}, uma diferença que "
          "fundamenta a hipótese sobre a escolaridade e o cálculo do poder."),
    ]),
    ("Medição de conhecimentos e práticas: instrumentos, validação e "
     "observação", [
        P("Os inquéritos de conhecimentos, atitudes e práticas (CAP) são o desenho mais usado neste tema. A lista ChecKAP "
          "reúne 46 itens de relato de um estudo CAP, distribuídos por oito "
          "domínios, 11 dos quais sobre o método {zarei2024}. A validade de conteúdo "
          "é habitualmente avaliada por um painel de peritos com o índice de "
          "validade de conteúdo (IVC), calculado por item e para a escala "
          "{almanasreh2019}. A tradução deve seguir a tradução directa por "
          "dois tradutores independentes, a síntese, a retroversão também "
          "independente e a revisão por um comité, seguidas de pré-teste na "
          "população-alvo {tsang2017}."),
        P("A fiabilidade de uma escala de itens dicotómicos, como as "
          "perguntas de conhecimento pontuadas como certas ou erradas, "
          "estima-se pela fórmula 20 de Kuder-Richardson (KR-20) {kuder1937}, "
          "caso particular do alfa de Cronbach, com um valor mínimo "
          "habitualmente aceite de 0,70 {tsang2017}. Para classificar os "
          "resultados, os estudos CAP usam os pontos de corte de Bloom: bom "
          "com 80% ou mais das respostas correctas, moderado de 60% a 79% e "
          "fraco abaixo de 60% {bizuneh2024}; no estudo do Bangladesh sobre a "
          "SRO usou-se uma versão modificada, com 80% para o conhecimento "
          "adequado e 75% para a prática {nuzhat2025}."),
        P("A observação directa é o método de referência para medir uma "
          "prática, mas tem limites conhecidos. O mais importante é o efeito "
          "de Hawthorne, a mudança de comportamento de quem se sabe observado: "
          "num hospital, a adesão à higiene das mãos foi de 87,1% com "
          "observação aberta e de 44,9% com observação encoberta "
          "{elsaed2018}. Numa demonstração pedida à cuidadora este efeito "
          "tende a sobrestimar a qualidade da preparação, pelo que o "
          "resultado deve ser lido como o melhor desempenho de que a "
          "cuidadora é capaz. A concordância entre dois observadores que "
          "pontuam a mesma demonstração mede-se pelo kappa de Cohen, "
          "considerando-se aceitável um valor de 0,60 ou mais {mchugh2012}."),
    ]),
]

# ----------------------------------------------------- 7. estado da arte ----
ESTADO_ARTE = [
    P("O [[quadro:estado_arte]] sintetiza catorze estudos empíricos "
      "publicados nos últimos dez anos sobre conhecimentos e práticas das "
      "cuidadoras no tratamento da diarreia com SRO e zinco e sobre o "
      "tratamento da diarreia infantil em Moçambique, seleccionados pela "
      "proximidade do desenho e do contexto."),
    QUADRO("estado_arte",
           "Síntese de estudos sobre conhecimentos e práticas no tratamento "
           "da diarreia infantil com SRO e zinco (estado da arte)",
           ["Autor (ano)", "Local", "Desenho (n)", "Principais resultados"],
           [
               ["Greenland et al. (2016) {greenland2016}", "Zâmbia, Lusaka",
                "Formativo, ensaios comportamentais com observação e vídeo "
                "(14)",
                "Só 4 de 14 cuidadoras prepararam correctamente a SRO; erros "
                "sobretudo na medição da água, com solução demasiado "
                "concentrada; zinco desconhecido na população."],
               ["Desta et al. (2017) {desta2017}", "Etiópia, Amhara",
                "Transversal institucional (370)",
                "Bom conhecimento em 56,2% e boa prática em 37,6% (corte na "
                "média); só 18,1% "
                "sabiam que a SRO repõe líquidos e 64,6% julgavam que trava "
                "a diarreia."],
               ["Mekonnen et al. (2018) {mekonnen2018}", "Etiópia, Gambella",
                "Transversal comunitário (1.667)",
                "Mau conhecimento em 38,0% (633); associado à falta de educação "
                "formal e de informação dada na unidade sanitária."],
               ["Dhingra et al. (2018) {dhingra2018}", "Índia",
                "Transversal hospitalar (280)",
                "Só 50,4% das mães sabiam preparar e 55,2% administrar a "
                "SRO; um terço tratava a água de beber."],
               ["Kebede Fufa et al. (2019) {kebede2019}", "Etiópia, Doba",
                "Transversal comparativo comunitário (559)",
                "Má prática domiciliária em 55,8% (urbano) e 85,6% (rural); "
                "a dificuldade em preparar a SRO associou-se a má prática "
                "(razão de chances ajustada de 4,0 e 2,4)."],
               ["Abolurin et al. (2021) {abolurin2021}", "Nigéria, meio rural",
                "Transversal (400)",
                "15,3% desconheciam a SRO; entre as que diziam saber "
                "prepará-la, só 22,1% o fizeram correctamente; 4 em cada 10 "
                "crianças recusavam ou aceitavam mal a SRO."],
               ["Amu et al. (2022) {amu2022}", "Nigéria, Lagos",
                "Transversal, amostragem multietápica (336)",
                "10,4% conheciam a SRO de baixa osmolaridade e 6,5% usaram-na; "
                "53,3% conheciam o zinco e 42% usaram-no."],
               ["Machava et al. (2022) {machava2022}", "Moçambique, Maputo",
                "Retrospectivo de registos, 2015-2019 (9.041)",
                "SRO como tratamento principal em 79% e antibióticos em 21%; "
                "análise laboratorial das fezes em apenas 5 casos."],
               ["Seifu et al. (2024) {seifu2024}", "35 países da África "
                "subsariana", "Análise de inquéritos demográficos e de saúde "
                "(44.341)",
                "Co-utilização de SRO e zinco em 43,58%; associada à "
                "escolaridade e ao emprego maternos, à riqueza, aos meios de "
                "comunicação e à distância percebida."],
               ["Atnafu et al. (2024) {atnafu2024}", "Etiópia, Gondar",
                "Transversal institucional (405)",
                "Adesão ao zinco em 35%; bom conhecimento (razão de chances "
                "ajustada de 3,01) e aconselhamento (8,4) aumentaram a "
                "adesão; efeitos adversos reduziram-na (0,35)."],
               ["Salência-Ferrão et al. (2025) {salenciaferrao2025}",
                "Moçambique, quatro províncias",
                "Vigilância hospitalar, 2014-2019 (2.028)",
                "Antibióticos em 93,2% das crianças internadas com diarreia "
                "aguda; 49,1% destas receberam mais de um antibiótico."],
               ["Nuzhat et al. (2025) {nuzhat2025}", "Bangladesh, Daca",
                "Transversal hospitalar (350)",
                "Conhecimento inadequado em 88,0% e prática imprópria em "
                "72,5% (Bloom modificado); 97,4% diziam saber preparar a SRO, mas só "
                "2,9% conheciam todos os passos."],
               ["Islam et al. (2025) {islam2025}", "Bangladesh, Daca",
                "Qualitativo, entrevistas em profundidade (31)",
                "Dez mães não sabiam a quantidade de pó e nove a quantidade "
                "de água; só 15 seguiam a alimentação recomendada."],
               ["Yewodiaw et al. (2026) {yewodiaw2026}", "Moçambique",
                "Análise multinível do IDS 2022-23 (9.799)",
                "Prevalência de diarreia de 8,8%, máxima no Niassa (14,5%); "
                "maior risco aos 12-23 meses e menor com a escolaridade "
                "materna."],
           ],
           larguras=[3.3, 2.5, 3.2, 7.0],
           fonte="Elaboração própria (2026), a partir das fontes citadas."),
    P("A leitura do quadro mostra um padrão constante: a maioria das "
      "cuidadoras conhece a SRO, mas muitas desconhecem a sua função, o "
      "volume de água ou a quantidade de pó, e a prática fica sempre abaixo "
      "do conhecimento declarado. A escolaridade materna e o aconselhamento "
      "recebido aparecem como os determinantes mais consistentes, enquanto o "
      "efeito da idade da cuidadora e da residência varia entre estudos. As "
      "divergências de magnitude reflectem sobretudo diferenças de método, "
      "porque a maioria dos estudos mede a prática pela declaração e aplica "
      "pontos de corte diferentes, o que torna a comparação frágil."),
    P("A lacuna é clara. Os três estudos moçambicanos do quadro descrevem a "
      "prevalência da diarreia, a cobertura declarada do tratamento ou a "
      "prática dos serviços, mas nenhum avaliou os conhecimentos das "
      "cuidadoras, observou a preparação da solução ou mediu a adesão ao "
      "zinco, e nenhum estudo deste tipo foi encontrado para Nampula. O "
      "presente estudo preenche essa lacuna com um instrumento validado e "
      "traduzido, uma observação estruturada com controlo da concordância e "
      "uma amostra com poder calculado para a componente analítica."),
]
ESQUEMA_TEXTO = [
    P("A [[figura:esquema]] representa as relações que o estudo examina. As "
      "características sociodemográficas da cuidadora, o contacto prévio com "
      "os serviços e as condições do domicílio influenciam os conhecimentos, "
      "e estes, juntamente com os mesmos factores, influenciam a preparação "
      "da solução e as práticas no último episódio. A idade da criança, o "
      "tipo de consulta e a unidade sanitária entram como variáveis de "
      "ajustamento, e o efeito de "
      "Hawthorne e o viés de recordação são considerados na interpretação."),
]
ESQUEMA_TITULO = ("Esquema conceptual dos factores associados aos "
                  "conhecimentos e às práticas das cuidadoras no tratamento da "
                  "diarreia com SRO e zinco")
ESQUEMA = {
    "contexto": ("Consultas da criança das unidades sanitárias da Cidade de "
                 "Nampula, Março e Abril de 2027"),
    "blocos": [
        ("Características da cuidadora", ["idade", "escolaridade",
                                          "leitura", "língua falada em casa",
                                          "ocupação", "número de filhos"]),
        ("Contacto com os serviços", ["demonstração prévia da SRO",
                                      "exposição a mensagens",
                                      "tempo até à unidade sanitária"]),
        ("Condições do domicílio", ["fonte de água de beber",
                                    "tratamento da água em casa"]),
    ],
    "desfecho": ("Conhecimentos e práticas", [
        "conhecimentos (Bloom)", "preparação correcta observada",
        "SRO e zinco no último episódio", "adesão ao zinco"]),
    "moderadores": ("Ajustamento e vieses", [
        "idade da criança", "tipo de consulta",
        "unidade sanitária (conglomerado)",
        "efeito de Hawthorne", "viés de recordação"]),
}

# ----------------------------------------------------- 8. metodologia -------
METODOLOGIA = [
    ("Tipo e desenho do estudo", [
        P("Trata-se de um estudo observacional, transversal, descritivo e "
          "analítico, de base institucional, com duas componentes aplicadas à "
          "mesma participante na mesma visita: a observação estruturada da "
          "preparação da solução de reidratação oral, numa demonstração "
          "pedida à cuidadora com material fornecido pelo estudo, e uma "
          "entrevista estruturada sobre as suas características, os seus "
          "conhecimentos e as práticas no último episódio de diarreia da "
          "criança. A componente descritiva responde aos objectivos "
          "específicos 1 a 3 e a componente analítica ao objectivo 4. O "
          "desenho transversal é adequado para estimar proporções e "
          "associações num momento definido, sem permitir conclusões "
          "causais. O relato seguirá a declaração STROBE (Strengthening the "
          "Reporting of Observational Studies in Epidemiology) {vonelm2007} e "
          "a lista ChecKAP para inquéritos de conhecimentos, atitudes e "
          "práticas {zarei2024}."),
    ]),
    ("Local e período do estudo", [
        P("O estudo decorre na Cidade de Nampula, capital da província, nas "
          "unidades sanitárias do SNS sob gestão do SDSMAS da Cidade de "
          "Nampula que oferecem consulta da criança sadia (vigilância do "
          "crescimento e vacinação) e consulta da criança doente, onde se "
          "aplica a AIDI {misau2014}. O número destas unidades e o volume "
          "mensal de atendimentos de crianças menores de cinco anos não estão "
          "publicados e serão obtidos antes do sorteio, a partir dos registos "
          "de rotina [confirmar junto do SDSMAS da Cidade de Nampula]."),
        P("O estudo estende-se de Outubro de 2026 a Setembro de 2027. A "
          "recolha realiza-se em Março e Abril de 2027, depois da aprovação "
          "ética e das autorizações institucionais. Este período coincide com "
          "o fim da estação chuvosa e com a época habitual dos surtos de "
          "cólera, de Outubro a Abril {omsdon2023}; por isso, a situação "
          "epidemiológica da cólera na cidade será registada semanalmente, a "
          "partir dos boletins do SDSMAS, e usada como variável de contexto "
          "na análise."),
    ]),
    ("População, unidade de análise e base de amostragem", [
        P("A população de estudo é constituída pelas cuidadoras principais "
          "de crianças dos 0 aos 59 meses atendidas nas consultas da criança "
          "das unidades seleccionadas. Considera-se cuidadora principal a "
          "pessoa com 18 ou mais anos que cuida habitualmente da criança e lhe "
          "dá os medicamentos em casa, em regra a mãe, mas também a avó, outra "
          "familiar ou o pai. Usa-se o termo cuidadora por ser o caso mais "
          "frequente, sem excluir os cuidadores do sexo masculino."),
        P("A unidade de análise é a cuidadora, para todos os objectivos, e "
          "cada cuidadora entra no estudo uma única vez. Quando traz mais do "
          "que uma criança menor de cinco anos, escolhe-se uma criança índice, "
          "a que teve o episódio de diarreia mais recente nos três meses "
          "anteriores ou, se nenhuma teve diarreia, a mais nova; em gémeos, a "
          "escolha faz-se por sorteio. As perguntas sobre o último episódio, a "
          "idade da criança e a quantidade de SRO correcta referem-se sempre "
          "à criança índice. Quando a criança vem acompanhada por duas "
          "cuidadoras, é entrevistada a que habitualmente lhe dá os "
          "medicamentos. Para impedir a reinclusão na mesma ou noutra unidade, "
          "pergunta-se à cuidadora se já participou e mantém-se, separado dos "
          "questionários, um registo com um código formado pelas iniciais, "
          "pelo ano de nascimento e pelo bairro."),
        P("A base de amostragem tem dois níveis: a lista das unidades "
          "sanitárias elegíveis com o respectivo volume de consultas, obtida "
          "no SDSMAS, e, em cada dia de recolha, a ordem de chegada das "
          "cuidadoras à consulta da criança, dada pelas senhas ou pelo livro "
          "de registo da unidade."),
    ]),
    ("Amostra e cálculo do tamanho da amostra", [
        P("O tamanho da amostra foi calculado para dois requisitos, "
          "adoptando-se o maior: a precisão das estimativas descritivas "
          "(objectivos 1 e 2) e o poder da comparação entre grupos de "
          "escolaridade (objectivo 4). Para a precisão usou-se a fórmula da "
          "estimativa de uma proporção:"),
        FORMULA("n<sub>0</sub> = Z<sup>2</sup> × p × (1 - p) / d<sup>2</sup>"),
        P("em que Z = 1,96 corresponde a uma confiança de 95%, d = 0,05 é a "
          "margem de erro absoluta aceite e p = 0,5 é a proporção esperada de "
          "cuidadoras com bom conhecimento. Usa-se o valor de variância "
          "máxima porque não há uma estimativa comparável: os 56,2% de bom "
          "conhecimento observados numa consulta de menores de cinco anos da "
          "Etiópia resultam de um corte na média da pontuação {desta2017}, e "
          "não dos pontos de corte de Bloom, e no Bangladesh, com um limiar de "
          "80%, só 12,0% das mães tinham conhecimento adequado {nuzhat2025}. "
          "A substituição dá n<sub>0</sub> = 3,8416 × 0,5 × 0,5 / 0,0025 = "
          "0,9604 / 0,0025 = 384,2, isto é, 385 cuidadoras. O mesmo valor "
          "cobre a proporção de preparação correcta, que a literatura situa "
          "longe de 0,5 {greenland2016,abolurin2021}."),
        P("Como a amostragem é por conglomerados (unidades sanitárias), "
          "aplicou-se um efeito de desenho de 1,5, o que dá 385 × 1,5 = 577,5, "
          "isto é, 578 respondentes; com cerca de 49 respondentes por unidade, "
          "este valor corresponde a um coeficiente de correlação intraclasse "
          "de cerca de 0,01, e o valor observado será relatado. Para compensar "
          "recusas, desistências antes do fim da observação e questionários "
          "incompletos, aplicou-se uma taxa de não resposta de 10%, superior "
          "às perdas de 2,1% registadas no estudo etíope {desta2017}, porque "
          "aqui a participação inclui uma demonstração:"),
        FORMULA("n<sub>c</sub> = n / (1 - t<sub>nr</sub>) = 578 / 0,90 = "
                "642,2"),
        P("arredondado para 648, para que o número seja igual nas doze "
          "unidades: 54 convites por unidade, com 583 respondentes esperados "
          "(648 × 0,90)."),
        P("Para o poder da componente analítica usou-se a fórmula de duas "
          "proporções independentes com grupos de tamanho diferente, com teste "
          "bilateral:"),
        FORMULA("n<sub>1</sub> = [Z<sub>1-α/2</sub> × √(p<sub>m</sub> × (1 - "
                "p<sub>m</sub>) × (1 + 1/k)) + Z<sub>1-β</sub> × "
                "√(p<sub>1</sub> × (1 - p<sub>1</sub>) + p<sub>2</sub> × (1 - "
                "p<sub>2</sub>) / k)]<sup>2</sup> / (p<sub>1</sub> - "
                "p<sub>2</sub>)<sup>2</sup>"),
        P("em que Z<sub>1-α/2</sub> = 1,96 (α de 5%), Z<sub>1-β</sub> = 0,84 "
          "(poder de 80%), p<sub>1</sub> = 0,20 é a proporção de preparação "
          "correcta esperada nas cuidadoras com escolaridade primária ou "
          "nenhuma, próxima dos 22,1% observados na Nigéria entre as mães que "
          "diziam saber preparar a SRO {abolurin2021}, p<sub>2</sub> = 0,33 é "
          "a proporção nas cuidadoras com escolaridade secundária ou "
          "superior, k = 0,667 é a razão entre o segundo e o primeiro grupo "
          "(40% contra 60%) e p<sub>m</sub> = 0,252 é a proporção média "
          "ponderada. A diferença de 13 pontos é ligeiramente inferior à de "
          "14,4 pontos na co-utilização de SRO e zinco entre os filhos de mães "
          "com escolaridade primária e secundária no IDS {ine2024}. A "
          "substituição dá n<sub>1</sub> = [1,96 × √0,4712 + 0,84 × "
          "√0,4917]<sup>2</sup> / 0,0169 = (1,3455 + 0,5890)<sup>2</sup> / "
          "0,0169 = 3,7422 / 0,0169 = 221,4, isto é, 222 e 148 cuidadoras nos "
          "dois grupos, 370 no total e 555 depois do efeito de desenho, abaixo "
          "dos 578 exigidos pela precisão. O poder foi recalculado sobre os "
          "583 respondentes esperados, e não sobre os convites, com o mesmo "
          "efeito de desenho (tamanho efectivo de 389): é de 82% para esta "
          "diferença e de 91% para uma diferença de 20% para 35%. Se só 30% "
          "das cuidadoras tiverem escolaridade secundária ou superior, o poder "
          "desce para 77% e 87%, e com os 26% observados no país entre as mães "
          "de crianças com diarreia {ine2024}, para 75% e 85%, limitação que "
          "será declarada."),
        P("Como o número de cuidadoras elegíveis distintas que frequentarão "
          "as unidades seleccionadas durante as oito semanas de recolha (N) "
          "só será conhecido antes do sorteio, a [[tabela:cenarios]] "
          "apresenta o efeito da correcção para população finita, n = "
          "n<sub>0</sub> / [1 + (n<sub>0</sub> - 1) / N], em vários cenários. "
          "Em todos eles, os convites necessários ficam abaixo dos 648 "
          "calculados sem correcção, que cobrem também os 617 convites "
          "exigidos pela componente analítica (555 / 0,90); mantêm-se por "
          "isso os 648 convites, e quando N for pequeno a correcção melhora a "
          "precisão, como mostra a última coluna."),
        TABELA("cenarios",
               "Cenários de população elegível, tamanho da amostra corrigido "
               "e precisão esperada",
               ["Cuidadoras elegíveis em oito semanas (N)",
                "n corrigido para N", "Com efeito de desenho 1,5",
                "Convites necessários (10% de não resposta)",
                "Margem de erro com 583 respondentes (pontos)"],
               [["1.000", "279", "419", "466", "3,2"],
                ["2.000", "323", "485", "539", "4,2"],
                ["4.000", "352", "528", "587", "4,6"],
                ["8.000", "368", "552", "614", "4,8"],
                ["16.000", "376", "564", "627", "4,9"]],
               larguras=[3.6, 2.6, 3.0, 3.6, 3.2],
               fonte="Elaboração própria (2026).",
               nota="Valores de N hipotéticos, para p = 0,5. O volume real "
                    "de consultas será obtido no SDSMAS da Cidade de Nampula "
                    "antes do sorteio. Em todos os cenários mantêm-se 648 "
                    "convites. A margem de erro inclui o efeito de desenho "
                    "e a correcção para população finita."),
        P("Para a regressão multivariável, com uma prevalência de preparação "
          "correcta de 20% a 25%, esperam-se 117 a 146 eventos entre os 583 "
          "respondentes, o que permite 11 a 14 parâmetros segundo a regra de "
          "pelo menos dez eventos por variável {peduzzi1996}; o modelo será "
          "limitado a dez parâmetros. No modelo do bom conhecimento, dez "
          "parâmetros exigem pelo menos 100 eventos, isto é, uma proporção de "
          "17% ou mais; se for inferior, o número de parâmetros é reduzido "
          "pela mesma regra."),
    ]),
    ("Técnica de amostragem e selecção das participantes", [
        P("A amostragem é por conglomerados, em duas etapas. Na primeira, "
          "seleccionam-se doze unidades sanitárias com probabilidade "
          "proporcional ao volume de consultas de crianças menores de cinco "
          "anos, por selecção sistemática a partir da lista ordenada por posto "
          "administrativo, com início aleatório gerado por computador na "
          "presença do orientador. Com um número fixo de 54 convites por "
          "unidade, a amostra fica auto-ponderada. Se a cidade tiver doze ou "
          "menos unidades elegíveis, incluem-se todas, os convites são "
          "distribuídos em proporção ao volume de consultas e a unidade passa "
          "a ser tratada como estrato na análise. O pré-teste realiza-se numa "
          "unidade não seleccionada, de dimensão semelhante."),
        P("Na segunda etapa, em cada dia de recolha, calcula-se o intervalo k "
          "dividindo o número médio diário de cuidadoras atendidas no mês "
          "anterior pelo número de participantes previsto para o dia, cerca de "
          "seis por inquiridor, e sorteia-se um número inicial entre 1 e k. As "
          "cuidadoras são convidadas pela ordem de chegada, depois de "
          "terminada a consulta da criança, para não atrasar os cuidados. Não "
          "há substituição: cada cuidadora elegível sorteada conta como "
          "convite, as recusas e as inelegibilidades são registadas para o "
          "cálculo da "
          "taxa de resposta, e a recolha termina em cada unidade quando se "
          "atingem os 54 convites, o que exige três a quatro dias por unidade "
          "e cerca de oito semanas no total."),
    ]),
    ("Critérios de inclusão e de exclusão", [
        H3("Critérios de inclusão"),
        LISTA([
            "Ser a cuidadora principal, com 18 ou mais anos, de uma criança "
            "dos 0 aos 59 meses atendida no dia na consulta da criança sadia ou "
            "da criança doente de uma unidade seleccionada.",
            "Residir na Cidade de Nampula há pelo menos seis meses.",
            "Comunicar em Português ou em Emakhuwa.",
            "Aceitar participar, com assinatura do termo de consentimento ou "
            "impressão digital na presença de uma testemunha imparcial.",
        ]),
        H3("Critérios de exclusão"),
        LISTA([
            "Criança com sinais gerais de perigo ou com desidratação grave no "
            "dia, que precise de cuidados urgentes, internamento ou "
            "transferência; a prioridade é o tratamento da criança, e a "
            "cuidadora não é convidada.",
            "Cuidadora que trabalhe como profissional de saúde, APE ou em "
            "farmácia, pela formação específica no tema.",
            "Participação no pré-teste ou participação anterior no estudo com "
            "outra criança.",
            "Incapacidade física ou mental que impeça a entrevista ou a "
            "demonstração.",
        ]),
    ]),
    ("Variáveis e definições operacionais", [
        P("O [[quadro:variaveis]] apresenta as variáveis do estudo, o seu "
          "tipo, a definição operacional com as categorias e o objectivo "
          "específico a que servem. Os pontos de corte de Bloom aplicam-se de "
          "forma idêntica às duas pontuações: na escala de 20 itens de "
          "conhecimentos, bom corresponde a 16 ou mais respostas correctas "
          "(80% ou mais), moderado a 12-15 (60-79%) e fraco a 11 ou menos "
          "(abaixo de 60%); na lista de 10 itens da observação, boa prática "
          "corresponde a 8 ou mais itens cumpridos (80% ou mais), moderada a "
          "6-7 (60-79%) e fraca a 5 ou menos (abaixo de 60%) {bizuneh2024}. A "
          "preparação correcta, desfecho principal da observação, exige o "
          "cumprimento dos cinco itens críticos, porque basta falhar um deles "
          "para a solução ficar insegura ou ineficaz."),
        QUADRO("variaveis", "Variáveis do estudo e definições operacionais",
               ["Variável", "Tipo", "Definição operacional e categorias",
                "Objectivo"],
               [
                   ["Nível de conhecimentos", "Dependente, ordinal",
                    "Soma dos 20 itens da secção C (0-20): bom, 16-20 (80% ou "
                    "mais); moderado, 12-15 (60-79%); fraco, 0-11 (abaixo de "
                    "60%)", "1, 4"],
                   ["Conhecimento bom", "Dependente, dicotómica",
                    "Pontuação de 16 ou mais na secção C: sim; não", "4"],
                   ["Conhecimento por item", "Descritiva, dicotómica",
                    "Resposta correcta ou incorrecta em cada item, de C1 a C20",
                    "1"],
                   ["Preparação correcta da solução", "Dependente principal, "
                    "dicotómica",
                    "Cumprimento simultâneo dos cinco itens críticos da lista "
                    "de observação (E1 a E5): sim; não", "2, 4"],
                   ["Pontuação de práticas observadas", "Dependente, ordinal",
                    "Soma dos 10 itens da lista (0-10): boa, 8-10 (80% ou "
                    "mais); moderada, 6-7 (60-79%); fraca, 0-5 (abaixo de 60%)",
                    "2"],
                   ["Volume relativo da solução", "Descritiva, quantitativa",
                    "Volume final medido dividido pelo volume indicado no "
                    "rótulo, em percentagem: concentrada (abaixo de 90%); "
                    "dentro da tolerância (90-110%); diluída (acima de 110%)",
                    "2"],
                   ["Erros por passo", "Descritiva, dicotómica",
                    "Incumprimento de cada item da lista, de E1 a E10", "2"],
                   ["Concordância entre o declarado e o observado",
                    "Descritiva, pareada",
                    "Tipo de água e volume declarados (C8 e C7) comparados com "
                    "os observados (E1 e E2): concordante; discordante", "2"],
                   ["Episódio de diarreia nos três meses", "Filtro, "
                    "dicotómica",
                    "Três ou mais dejecções moles ou líquidas em 24 horas na "
                    "criança índice, referidas pela cuidadora: sim; não", "3"],
                   ["Tratamento combinado no último episódio", "Dependente, "
                    "nominal",
                    "SRO e zinco; só SRO; só zinco; nenhum dos dois", "3"],
                   ["Adesão ao zinco", "Dependente, dicotómica",
                    "Toma diária declarada durante 10 ou mais dias (D9), limite "
                    "inferior das normas nacionais: sim; não "
                    "(sensibilidade com 14 ou mais dias)", "3"],
                   ["Razões da não adesão", "Descritiva, resposta múltipla",
                    "A diarreia parou; vómitos; recusa da criança; "
                    "esquecimento; acabaram os comprimidos; não sabia a "
                    "duração; custo; outra", "3"],
                   ["Outras práticas no episódio", "Descritiva, nominal",
                    "Mais líquidos do que o habitual; alimentação continuada; "
                    "antibiótico ou antidiarreico; remédio tradicional; fonte "
                    "da SRO e do zinco (unidade sanitária, APE, farmácia "
                    "privada, mercado, outra)", "3"],
                   ["Escolaridade da cuidadora", "Independente principal, "
                    "ordinal",
                    "Nenhuma; primária; secundária; superior; agrupada em "
                    "nenhuma ou primária e secundária ou superior", "4"],
                   ["Demonstração prévia", "Independente principal, "
                    "dicotómica",
                    "Ter visto alguma vez um profissional de saúde ou um APE "
                    "preparar a SRO: sim; não", "4"],
                   ["Leitura funcional", "Independente, dicotómica",
                    "Lê a frase do rótulo da saqueta sem erro (A5): sim; não, se lê "
                    "com dificuldade ou não lê",
                    "4"],
                   ["Idade da cuidadora", "Independente, quantitativa",
                    "Anos completos; 18-24; 25-34; 35 ou mais", "4"],
                   ["Relação com a criança", "Independente, nominal",
                    "Mãe; avó; outra familiar; pai; outra", "4"],
                   ["Língua falada em casa", "Independente, nominal",
                    "Emakhuwa; Português; outra", "4"],
                   ["Filhos menores de cinco anos", "Independente, discreta",
                    "1; 2; 3 ou mais", "4"],
                   ["Exposição a mensagens", "Independente, dicotómica",
                    "Ouviu nos seis meses anteriores mensagens sobre diarreia "
                    "ou cólera (rádio, televisão, palestra, igreja ou mesquita, "
                    "APE): sim; não", "4"],
                   ["Tempo até à unidade sanitária", "Independente, ordinal",
                    "30 minutos ou menos; mais de 30 minutos", "4"],
                   ["Tratamento da água em casa", "Independente, dicotómica",
                    "Ferve ou trata com cloro a água de beber: sim; não", "4"],
                   ["Outras características", "Descritivas, nominais",
                    "Estado civil, ocupação e pessoas no agregado (A3, A7, "
                    "A9); sexo, diarreia no dia e fonte da água (B2, B4, "
                    "B5); demonstração vista no dia e fonte habitual da SRO "
                    "(B8, B9)", "4"],
                   ["Idade da criança índice", "Ajustamento, quantitativa",
                    "Meses completos; 0-5; 6-11; 12-23; 24-59", "3, 4"],
                   ["Tipo de consulta", "Ajustamento, dicotómica",
                    "Criança sadia; criança doente", "4"],
                   ["Unidade sanitária", "Conglomerado",
                    "Código da unidade, de 1 a 12", "1, 2, 3, 4"],
               ],
               larguras=[3.4, 2.8, 8.0, 1.8]),
    ]),
]

METODOLOGIA += [
    ("Instrumentos de recolha de dados e respectivas fontes", [
        P("Usam-se dois instrumentos em papel. O questionário estruturado "
          "(Apêndice A) tem quatro secções: características da cuidadora "
          "(secção A); criança índice, domicílio e contacto com os serviços "
          "(secção B); conhecimentos, com 20 itens pontuados como certos ou "
          "errados (secção C); e práticas no último episódio de diarreia dos "
          "três meses anteriores (secção D). Os itens foram adaptados dos "
          "questionários publicados sobre o tratamento domiciliário da "
          "diarreia e a adesão ao zinco {desta2017,kebede2019,atnafu2024,"
          "nuzhat2025} e redigidos a partir das mensagens do Plano A da AIDI "
          "{misau2014}, da declaração conjunta da OMS e da UNICEF "
          "{omsunicef2004} e do manual nacional da cólera {misau2016}; não "
          "reproduzem uma escala validada, pelo que a validação é feita neste "
          "estudo. A resposta correcta de cada item está fixada na chave de "
          "correcção do apêndice."),
        P("A lista de verificação da observação (Apêndice B) tem dez itens, "
          "nove observados e um declarado: cinco críticos (água segura, volume dentro "
          "da tolerância, saqueta inteira, nenhum ingrediente acrescentado e "
          "dissolução completa) e cinco complementares (lavagem das mãos, "
          "medição da água num recipiente de volume conhecido, recipiente "
          "limpo e tapado, administração com copo ou colher e, declarado à "
          "pergunta do observador, deitar fora em casa ao fim de 24 horas). Os itens seguem os passos da preparação indicados "
          "nas normas {misau2014,msf2024} e os erros descritos na observação "
          "de Lusaka {greenland2016}, e o conjunto de recipientes oferecidos "
          "inclui os que as famílias usam para medir a água {etokidem2023}. A "
          "tolerância de 10% no volume é uma convenção do estudo, a validar "
          "pelo painel de peritos, e será testada em análise de "
          "sensibilidade."),
        P("A validação decorre em quatro passos. Primeiro, um painel de seis "
          "peritos (um médico ou técnico de medicina com experiência em AIDI, "
          "um farmacêutico, uma enfermeira de saúde materno-infantil, um "
          "docente de saúde pública, um profissional de promoção da saúde e um "
          "falante nativo de Emakhuwa com formação em saúde) classifica a "
          "relevância de cada item numa escala de quatro pontos; calcula-se o "
          "IVC por item, exigindo-se pelo menos 0,80, o que com seis peritos "
          "corresponde a cinco concordâncias, e a média da escala, exigindo-se "
          "pelo menos 0,90; os itens abaixo do limiar são revistos ou "
          "retirados {almanasreh2019}. Segundo, a versão portuguesa é "
          "traduzida para Emakhuwa por dois tradutores independentes, as "
          "traduções são sintetizadas, a síntese é retrovertida para "
          "Português por outros dois tradutores sem conhecimento do original e "
          "um comité formado pelo estudante, pelo orientador e pelos "
          "tradutores resolve as discrepâncias {tsang2017}."),
        P("Terceiro, o pré-teste é aplicado a 60 cuidadoras, cerca de 10% da "
          "amostra, na unidade não seleccionada, e essas cuidadoras não entram "
          "na amostra final. Avaliam-se a compreensão dos itens, o tempo de "
          "aplicação e a fiabilidade da escala de conhecimentos pela KR-20, "
          "exigindo-se pelo menos 0,70 {kuder1937,tsang2017}; se o valor for "
          "inferior, revêem-se os itens com correlação item-total abaixo de "
          "0,20. Quarto, em 30 demonstrações do pré-teste, dois observadores "
          "pontuam em simultâneo e de forma independente a mesma preparação, e "
          "calcula-se o kappa de Cohen para cada item crítico, exigindo-se "
          "pelo menos 0,60 {mchugh2012}; os itens abaixo do limiar são "
          "clarificados no manual e a formação é repetida."),
        P("São fontes secundárias o livro de registo da consulta da criança, "
          "para calcular o intervalo de selecção e estimar N, e o cartão de "
          "saúde da criança, consultado com autorização da cuidadora para "
          "verificar o registo de SRO ou de zinco no último episódio."),
    ]),
    ("Procedimentos de recolha de dados e controlo de qualidade", [
        P("A equipa é formada pelo estudante e por dois assistentes, "
          "finalistas de cursos de saúde ou enfermeiros sem vínculo às "
          "unidades seleccionadas, fluentes em Português e Emakhuwa. A "
          "formação dura quatro dias e inclui o protocolo, a ética, os sinais "
          "gerais de perigo e de desidratação da AIDI, a técnica de "
          "entrevista, o guião da observação, a medição do volume e exercícios "
          "de dramatização, seguidos do pré-teste. Cada participante passa "
          "pela mesma sequência, num espaço reservado cedido pela unidade."),
        LISTA([
            "Convite depois da consulta, verificação da elegibilidade, leitura "
            "da folha de informação e consentimento.",
            "Verificação rápida dos sinais gerais de perigo e de desidratação "
            "na criança índice; perante qualquer sinal, a criança é levada de "
            "imediato ao clínico de serviço.",
            "Observação da preparação, feita antes da entrevista para que as "
            "perguntas de conhecimentos não ensinem as respostas.",
            "Entrevista (secções A a D), com cerca de 25 minutos.",
            "Aconselhamento correctivo, demonstração da preparação correcta e "
            "entrega de um folheto ilustrado em Português e Emakhuwa.",
            "Revisão do questionário e da lista antes de a cuidadora sair.",
        ], numerada=True),
        P("A demonstração segue um guião fixo. A mesa tem uma bacia com jarro "
          "de água e sabão, dois jarros iguais apresentados oralmente como "
          "«água da torneira da unidade sanitária» e «água fervida e deixada "
          "arrefecer», cuja posição alterna entre participantes pares e "
          "ímpares, recipientes domésticos comuns (garrafas vazias de 0,5, 1 "
          "e 1,5 litros, um copo, uma caneca, um jarro sem marcas, um "
          "recipiente com tampa e outro sem tampa), uma colher limpa, um copo "
          "para administração e uma saqueta de SRO de baixa osmolaridade da "
          "apresentação distribuída pelo SNS, cujo volume de diluição (V) é "
          "registado a partir do rótulo. O observador diz: «Imagine que a sua "
          "criança está com diarreia em casa. Mostre-me, com este material, "
          "como prepara o soro de pacote. Faça como faz em casa.» Durante a "
          "preparação não ajuda nem comenta. No fim, transfere a solução para "
          "um jarro graduado com divisões de 50 ml, regista o volume, pergunta-lhe "
          "o que faz em casa à solução que sobra no dia seguinte e pede à "
          "cuidadora "
          "que mostre como a daria, sem a dar à criança. A solução é deitada "
          "fora diante da cuidadora, com a explicação de que serviu apenas "
          "para a demonstração."),
        P("O controlo de qualidade inclui a revisão diária de todos os "
          "questionários pelo estudante, a dupla observação independente de "
          "cerca de 10% das demonstrações (uma em cada dez) durante a recolha, "
          "para recalcular o kappa, e visitas de supervisão do orientador. "
          "Para limitar a contaminação entre participantes, a demonstração e a "
          "entrevista fazem-se longe da sala de espera, pede-se reserva às "
          "cuidadoras e pergunta-se a cada uma se viu alguém demonstrar a "
          "preparação nesse dia. Os dados são introduzidos duas vezes, por "
          "dois digitadores independentes, no programa de acesso livre "
          "EpiData, com regras de amplitude e de consistência; as "
          "discordâncias são corrigidas a partir do papel."),
    ]),
    ("Processamento e análise dos dados", [
        P("A análise será feita no Statistical Package for the Social "
          "Sciences (SPSS), versão 26 ou superior, com o módulo de amostras "
          "complexas, ou no R com o pacote survey, considerando a unidade "
          "sanitária como conglomerado e aplicando pesos iguais ao inverso da "
          "probabilidade de selecção, ajustados para a não resposta. As "
          "proporções serão apresentadas com intervalos de confiança a 95% "
          "(IC95%) calculados por linearização de Taylor, e o nível de significância será de 5% (p<0,05)."),
        P("Para o objectivo 1, calculam-se a média e o desvio-padrão da "
          "pontuação de conhecimentos, a distribuição pelas três categorias de "
          "Bloom e a proporção de respostas correctas em cada item. Para o "
          "objectivo 2, estimam-se a proporção de preparação correcta, a "
          "distribuição da pontuação de práticas pelas categorias de Bloom, a "
          "proporção de incumprimento de cada item e a mediana, com intervalo "
          "interquartil, do volume relativo, separando as soluções "
          "concentradas das diluídas. A distância entre o que a cuidadora diz "
          "e o que faz é medida comparando, na mesma pessoa, o volume e o tipo "
          "de água declarados com os observados, pelo teste de McNemar. Para o "
          "objectivo 3, calculam-se, entre as cuidadoras cuja criança teve "
          "diarreia nos três meses, as proporções de tratamento combinado, de "
          "adesão ao zinco entre as crianças que o receberam e de cada razão "
          "de não adesão."),
        P("Para o objectivo 4, a associação entre cada factor e os dois "
          "desfechos dicotómicos (conhecimento bom e preparação correcta) é "
          "testada pelo qui-quadrado com a correcção de Rao-Scott. Os factores "
          "com p<0,20 e as variáveis definidas à partida (escolaridade, "
          "demonstração prévia, idade da criança e tipo de consulta) entram "
          "num modelo de regressão de Poisson com erros-padrão corrigidos "
          "para o conglomerado, que estima razões de prevalências (RP) "
          "ajustadas com IC95%, preferíveis à razão de chances quando o "
          "desfecho é frequente; o Poisson robusto dá estimativas não "
          "enviesadas mesmo quando o modelo log-binomial está mal "
          "especificado {chen2018}. No modelo da preparação correcta "
          "entra também o nível de conhecimentos, para testar a terceira "
          "hipótese. A colinearidade é verificada pelo factor de inflação da "
          "variância, que deve ficar abaixo de 5, e testa-se a interacção "
          "entre escolaridade e demonstração prévia."),
        P("Com menos de 5% de dados em falta numa variável, a análise usa os "
          "casos completos; acima disso, repete-se a análise com imputação "
          "múltipla. As análises de sensibilidade usam tolerâncias de volume "
          "de 5% e de 20%, a adesão com 14 ou mais dias, a exclusão das "
          "cuidadoras que viram uma demonstração no próprio dia e a exclusão "
          "das semanas com surto de cólera activo na cidade."),
    ]),
    ("Limitações do estudo e estratégias de mitigação", [
        P("O [[quadro:limitacoes]] resume as limitações previstas, a sua "
          "consequência e a estratégia de mitigação. A mais importante é o "
          "efeito de Hawthorne, discutido na revisão da literatura "
          "{elsaed2018}."),
        QUADRO("limitacoes", "Limitações previstas e estratégias de mitigação",
               ["Limitação", "Consequência", "Mitigação"],
               [
                   ["Efeito de Hawthorne na demonstração",
                    "Sobrestimação da preparação correcta",
                    "Observação antes da entrevista; frase padronizada «faça "
                    "como faz em casa»; observador silencioso; interpretação "
                    "como limite superior"],
                   ["Situação artificial (material fornecido, espaço da "
                    "unidade)",
                    "Diferenças face à preparação em casa",
                    "Recipientes domésticos comuns; pergunta sobre o "
                    "recipiente e a água usados em casa"],
                   ["Desejabilidade social nas práticas declaradas",
                    "Sobrestimação da cobertura e da adesão",
                    "Assistentes sem vínculo às unidades; linguagem neutra; "
                    "confidencialidade garantida"],
                   ["Viés de recordação (três meses)",
                    "Erro na cobertura e na adesão ao zinco",
                    "Período curto; verificação no cartão de saúde; análise "
                    "dos episódios do último mês"],
                   ["Selecção de utentes dos serviços",
                    "Resultados mais favoráveis do que na comunidade",
                    "Declaração explícita; comparação com o IDS de 2022-23"],
                   ["Doze conglomerados e heterogeneidade entre unidades",
                    "Menor precisão",
                    "Efeito de desenho de 1,5; erros-padrão corrigidos; "
                    "relato da correlação intraclasse"],
                   ["Transição normativa da dose de zinco",
                    "Classificação incorrecta das respostas sobre a dose",
                    "Correcção pela norma nacional em vigor; duração de 10 a "
                    "14 dias aceite; registo do texto exacto"],
                   ["Surto de cólera durante a recolha",
                    "Mudança dos conhecimentos ou suspensão da recolha",
                    "Registo semanal da situação; análise de sensibilidade; "
                    "reprogramação acordada com a unidade"],
                   ["Tradução para Emakhuwa",
                    "Perda de equivalência de sentido",
                    "Tradução e retroversão independentes; comité; pré-teste"],
                   ["Exclusão das mães adolescentes",
                    "Resultados não aplicáveis às cuidadoras com menos de 18 "
                    "anos",
                    "Declaração explícita; estudo futuro com assentimento "
                    "próprio"],
                   ["Desenho transversal",
                    "Impossibilidade de inferir causalidade",
                    "Linguagem de associação; ajustamento multivariável"],
               ],
               larguras=[4.8, 4.6, 6.6],
               fonte="Elaboração própria (2026)."),
    ]),
    ("Considerações éticas", [
        P("O protocolo será submetido ao Comité Institucional de Bioética "
          "para a Saúde da Universidade Lúrio (CIBS-UniLúrio) e a recolha só "
          "começa depois da sua aprovação, em conformidade com a Lei de "
          "Investigação em Saúde Humana {lei3de2023} e com a Declaração de "
          "Helsínquia na revisão de 2024 {wma2025}. Serão pedidas "
          "autorizações à DPS de Nampula, ao SDSMAS da Cidade de Nampula e à "
          "direcção de cada unidade sanitária seleccionada (Apêndice E). O "
          "estudo não envolve a administração de medicamentos: a solução "
          "preparada na demonstração é deitada fora e nunca é dada à "
          "criança."),
        LISTA([
            "Consentimento livre e esclarecido, escrito, depois da leitura da "
            "folha de informação na língua preferida da cuidadora (Apêndices "
            "C e D); quem não sabe ler nem escrever dá o consentimento por "
            "impressão digital, na presença de uma testemunha imparcial, "
            "escolhida pela cuidadora e alheia à equipa, que assina o termo.",
            "Só participam cuidadoras com 18 ou mais anos; as mães "
            "adolescentes ficam de fora por exigirem um procedimento de "
            "assentimento próprio.",
            "Participação voluntária, sem efeito nos cuidados prestados à "
            "criança; a cuidadora pode interromper a qualquer momento e "
            "recusar qualquer pergunta ou a demonstração.",
            "Confidencialidade: os questionários têm apenas um código; os "
            "termos de consentimento e o registo de códigos ficam numa caixa "
            "fechada, separados dos questionários; a base de dados, sem "
            "nomes, é protegida por palavra-passe e só o estudante e o "
            "orientador lhe têm acesso; o papel é destruído cinco anos depois "
            "da defesa.",
            "Riscos mínimos, limitados ao tempo (cerca de 45 minutos) e a "
            "algum embaraço na demonstração, reduzido pelo espaço reservado e "
            "pelo tom não avaliativo; o benefício directo é o aconselhamento "
            "individual e o folheto.",
            "As unidades sanitárias são identificadas apenas por código nos "
            "relatórios públicos.",
        ]),
        P("A via de referenciação é explícita. Os membros da equipa são "
          "treinados para reconhecer os sinais gerais de perigo (não consegue "
          "beber ou mamar, vomita tudo, convulsões, letargia) e os sinais de "
          "desidratação da AIDI {misau2014}. Se, antes ou durante a "
          "entrevista, a criança apresentar algum destes sinais, ou se a "
          "cuidadora referir sangue nas fezes, diarreia há 14 dias ou mais ou "
          "uma diarreia actual sem tratamento, a entrevista é interrompida e a "
          "criança é levada de imediato ao clínico de serviço, retomando-se só "
          "se a cuidadora o desejar depois do atendimento. Todas as "
          "cuidadoras, e não apenas as que erraram, recebem no fim o "
          "aconselhamento correctivo e a demonstração da preparação correcta; "
          "as práticas perigosas observadas ou referidas, como diluir a "
          "saqueta num volume errado, usar água não tratada, dar SRO por "
          "biberão, interromper a amamentação ou dar antibióticos sem receita, "
          "são corrigidas nesse momento, sem juízo de valor."),
        P("Dado o historial de desconfiança perante as intervenções contra a "
          "cólera em Nampula {demolis2018}, a equipa usa identificação da "
          "UniLúrio e das autorizações, os líderes comunitários das áreas das "
          "unidades são informados do estudo pelas direcções das unidades, e "
          "fica claro que o estudo não distribui nem coloca qualquer produto "
          "na água. O estudante declara não ter conflitos de interesses e o "
          "estudo não recebe financiamento de fabricantes de medicamentos."),
    ]),
]

# ----------------------------------------------------- 9 e 10 ---------------
RESULTADOS_ESPERADOS = [
    P("Não se antecipam valores; a literatura indica a direcção provável "
      "de cada resultado, pela ordem dos objectivos específicos."),
    LISTA([
        "Objectivo 1: a distribuição das cuidadoras pelos níveis de "
        "conhecimento e o mapa dos itens menos conhecidos. Espera-se que a "
        "maioria conheça a SRO, mas que a sua função, a quantidade a dar após "
        "cada dejecção, o prazo de 24 horas e a duração do zinco sejam os "
        "pontos fracos, como nos estudos da Etiópia, da Nigéria e do "
        "Bangladesh {desta2017,amu2022,nuzhat2025}. O mapa dos itens orientará "
        "as mensagens do aconselhamento nas consultas e nas farmácias.",
        "Objectivo 2: a primeira estimativa moçambicana da proporção de "
        "cuidadoras que preparam correctamente a solução, com a identificação "
        "dos passos que mais falham. Espera-se uma proporção baixa, com erros "
        "concentrados na medição da água e na escolha da água segura "
        "{greenland2016,abolurin2021}, e uma distância entre o que as cuidadoras declaram e o que fazem, semelhante à observada no Bangladesh entre o conhecimento declarado e o conhecimento real dos passos {nuzhat2025}. Estes resultados "
        "indicarão se é preciso substituir a explicação verbal por uma "
        "demonstração feita pela própria mãe e se convém recomendar um "
        "recipiente de medida padronizado.",
        "Objectivo 3: a cobertura do tratamento combinado e a adesão ao zinco "
        "no último episódio, com as razões do abandono. Espera-se uma "
        "cobertura próxima ou pouco superior à observada na província no IDS "
        "{ine2024} e uma adesão incompleta, entre os 35% de Gondar e os 63% "
        "estimados para o esquema de 10 dias {atnafu2024,pradhan2025}, com "
        "a paragem da "
        "diarreia, os vómitos e a recusa da criança entre as razões "
        "principais. A frequência dos vómitos como motivo de abandono ajudará "
        "a antecipar o efeito da dose mais baixa proposta pela OMS "
        "{oms2024,dhingra2020}.",
        "Objectivo 4: a estimativa das RP ajustadas da escolaridade, da "
        "demonstração prévia e do nível de conhecimentos sobre a preparação "
        "correcta e sobre o conhecimento bom. Espera-se uma associação "
        "positiva com a escolaridade e com o aconselhamento recebido "
        "{desta2017,atnafu2024,nuzhat2025} e uma associação apenas moderada entre saber e fazer. Os resultados indicarão os grupos a "
        "quem dirigir as demonstrações, em particular as cuidadoras com menor "
        "escolaridade, e mostrarão se a demonstração prática vale mais do que "
        "a informação verbal.",
    ]),
]
DIVULGACAO = [
    P("Os resultados serão apresentados na defesa pública do trabalho de "
      "culminação do curso, na Faculdade de Ciências de Saúde da UniLúrio. Um "
      "relatório com os resultados agregados, acompanhado de uma síntese de "
      "uma página com recomendações práticas, será entregue ao CIBS-UniLúrio, "
      "à DPS de Nampula, ao SDSMAS da Cidade de Nampula e às direcções das "
      "unidades participantes, com os resultados de cada unidade entregues "
      "apenas à respectiva direcção."),
    P("A devolução às comunidades faz-se nas palestras das unidades "
      "participantes, com o folheto ilustrado em Português e Emakhuwa e com a "
      "demonstração dos passos que mais falharam. Será preparado um artigo "
      "para uma revista com revisão por pares, de preferência de acesso "
      "aberto, redigido segundo a declaração STROBE e a lista ChecKAP, e uma "
      "comunicação para as jornadas científicas da UniLúrio e para encontros "
      "nacionais de saúde pública. Os dados sobre a fonte da SRO e do zinco "
      "serão partilhados com as associações profissionais de farmácia, como "
      "contributo para o aconselhamento na dispensa."),
]

# ----------------------------------------------------- 11. cronograma -------
CRONOGRAMA_TEXTO = [
    P("O [[quadro:cronograma]] distribui as actividades pelos doze meses do "
      "estudo, de Outubro de 2026 a Setembro de 2027. A validação de conteúdo "
      "e a tradução decorrem em paralelo com a submissão ao CIBS-UniLúrio, "
      "porque não envolvem participantes; o pré-teste realiza-se em Fevereiro "
      "de 2027, depois da aprovação ética, e a recolha principal em Março e "
      "Abril de 2027, dentro das oito semanas previstas."),
]
CRONOGRAMA = {
    "inicio": (2026, 10),
    "n_meses": 12,
    "actividades": [
        ("Revisão da literatura e redacção do protocolo", [1, 2]),
        ("Validação de conteúdo pelo painel de peritos", [2, 3]),
        ("Submissão ao CIBS-UniLúrio e pedidos de autorização", [3, 4]),
        ("Tradução e retroversão do questionário para Emakhuwa", [3, 4]),
        ("Lista das unidades, sorteio e formação dos assistentes", [5]),
        ("Pré-teste, concordância entre observadores e versão final", [5]),
        ("Recolha de dados nas doze unidades sanitárias", [6, 7]),
        ("Dupla digitação e limpeza dos dados", [7, 8]),
        ("Análise dos dados", [8, 9]),
        ("Redacção do relatório final", [9, 10]),
        ("Revisão pelo orientador e entrega", [11]),
        ("Defesa pública e devolução dos resultados", [12]),
    ],
}

# ----------------------------------------------------- 12. orcamento --------
ORCAMENTO_TEXTO = [
    P("A [[tabela:orcamento]] apresenta o orçamento estimado. As quantidades "
      "de impressão correspondem a 720 exemplares: 648 para a recolha "
      "principal, 60 para o pré-teste e 12 de reserva. A rubrica maior é "
      "o subsídio dos dois assistentes durante as oito semanas de recolha, "
      "indispensável para que as entrevistas e as observações sejam feitas "
      "por pessoas sem vínculo às unidades e fluentes em Emakhuwa; seguem-se a impressão dos instrumentos, o transporte da equipa, as saquetas de SRO para as demonstrações "
      "e o material da estação de observação, que é o que distingue este "
      "estudo de um inquérito comum. O estudo será financiado com recursos "
      "próprios do estudante, sem prejuízo de um pedido de apoio à Faculdade "
      "de Ciências de Saúde; não haverá financiamento de fabricantes de "
      "medicamentos."),
]
ORCAMENTO = [
    ("Impressão do questionário e da lista de observação (10 páginas)",
     "página", 7200, 2),
    ("Impressão da folha de informação e do termo de consentimento, em "
     "duplicado", "página", 2880, 2),
    ("Folheto ilustrado de aconselhamento, a cores, em Português e Emakhuwa",
     "unidade", 720, 10),
    ("Saquetas de SRO para as demonstrações e o pré-teste", "saqueta", 720,
     12),
    ("Chaleira eléctrica para ferver a água das demonstrações", "unidade", 3,
     1200),
    ("Jarro graduado de 2 litros, com divisões de 50 ml", "unidade", 3, 400),
    ("Conjunto de recipientes para a demonstração (dois jarros iguais com "
     "tampa, garrafas, copo, caneca, jarro sem marcas, recipientes com e sem "
     "tampa)", "conjunto", 3, 1400),
    ("Água em bidões de 20 litros para as unidades sem água canalizada", "bidão",
     24, 50),
    ("Bacia e jarro para lavagem das mãos", "conjunto", 3, 500),
    ("Sabão e toalhetes de papel para a estação de demonstração", "global", 1,
     1200),
    ("Copos e colheres descartáveis", "unidade", 1300, 3),
    ("Subsídio dos assistentes na recolha (2 assistentes, 40 dias)", "dia",
     80, 500),
    ("Subsídio dos assistentes no pré-teste (2 assistentes, 4 dias)", "dia",
     8, 500),
    ("Subsídio de formação dos assistentes (2 assistentes, 4 dias)", "dia", 8,
     400),
    ("Tradução e retroversão para Emakhuwa (4 tradutores)", "tradutor", 4,
     1500),
    ("Comunicação e deslocação do painel de peritos", "perito", 6, 500),
    ("Transporte da equipa (3 pessoas, 44 dias)", "pessoa-dia", 132, 70),
    ("Comunicações telefónicas (12 meses)", "mês", 12, 250),
    ("Segunda digitação independente dos questionários", "questionário",
     648, 12),
    ("Material de escritório (pranchetas, canetas, pastas, envelopes)",
     "global", 1, 3000),
    ("Caixa com cadeado para os termos de consentimento", "unidade", 1, 1000),
    ("Impressão e encadernação do relatório final", "exemplar", 4, 800),
]
ORCAMENTO_IMPREVISTOS = 0.10

# ----------------------------------------------------- apendices ------------
_SIM_NAO = ["Sim (1)", "Não (0)"]
_SIM_NAO_NS = ["Sim (1)", "Não (0)", "Não sabe (9)"]
_CUMPRE = ["Cumpre (1)", "Não cumpre (0)"]

APENDICES = [
    ("Questionário sobre conhecimentos e práticas no tratamento da diarreia "
     "com SRO e zinco", [
        NOTA("Instruções ao entrevistador: aplicar só depois do consentimento "
             "e da observação da preparação (Apêndice B). Ler as perguntas "
             "tal como estão escritas, em Português ou em Emakhuwa, conforme "
             "a preferência da cuidadora. Na secção C não ler as opções: "
             "assinalar a resposta dada espontaneamente. Os números entre "
             "parênteses são os códigos de digitação. Se, em qualquer "
             "momento, surgir um sinal de perigo na criança, interromper e "
             "levar a criança ao clínico de serviço."),
        CAMPO("Código da participante: ________   Unidade (1 a 12): ____   "
              "Data: ___/___/2027   Entrevistador: ____"),
        H3("Secção A. Características da cuidadora"),
        PERG("A1. Relação com a criança índice:",
             ["Mãe (1)", "Avó (2)", "Outra familiar (3)", "Pai (4)",
              "Outra (5)"]),
        PERG("A2. Idade em anos completos: ______"),
        PERG("A3. Estado civil:",
             ["Solteira (1)", "Casada ou em união (2)",
              "Divorciada ou separada (3)", "Viúva (4)"]),
        PERG("A4. Nível de escolaridade mais alto que frequentou:",
             ["Nenhum (0)", "Primário (1)", "Secundário (2)",
              "Superior (3)"]),
        PERG("A5. Leitura funcional (observada): pedir à cuidadora que leia a "
             "frase de instruções do rótulo da saqueta.",
             ["Lê a frase completa sem erro (1)",
              "Lê com dificuldade ou só em parte (2)", "Não lê (0)"]),
        PERG("A6. Língua mais falada em casa:",
             ["Emakhuwa (1)", "Português (2)", "Outra (3): ________"]),
        PERG("A7. Ocupação principal:",
             ["Doméstica (1)", "Comércio ou venda (2)", "Agricultura (3)",
              "Trabalho assalariado (4)", "Estudante (5)", "Outra (6)"]),
        PERG("A8. Número de filhos menores de cinco anos: ______"),
        PERG("A9. Número de pessoas que vivem na casa: ______"),
        PERG("A10. Nos últimos seis meses, ouviu ou viu mensagens sobre a "
             "diarreia ou a cólera?", _SIM_NAO,
             instrucao="Se Sim: onde? Rádio; televisão; palestra na unidade "
                       "sanitária; APE ou activista; igreja ou mesquita; "
                       "líder comunitário; outro (assinalar todos)."),
        PERG("A11. Quanto tempo leva de casa até esta unidade sanitária?",
             ["30 minutos ou menos (1)", "Mais de 30 minutos (2)"]),
        H3("Secção B. Criança índice, domicílio e contacto com os serviços"),
        PERG("B1. Idade da criança índice em meses completos: ______"),
        PERG("B2. Sexo da criança:", ["Masculino (1)", "Feminino (2)"]),
        PERG("B3. Consulta de hoje:",
             ["Criança sadia (1)", "Criança doente (2)"]),
        PERG("B4. A criança tem diarreia hoje?", _SIM_NAO),
        PERG("B5. Principal fonte da água de beber da casa:",
             ["Água canalizada em casa ou no quintal (1)",
              "Fontanário público (2)", "Furo ou poço protegido (3)",
              "Poço não protegido (4)", "Rio ou lagoa (5)",
              "Água comprada (6)", "Outra (7)"]),
        PERG("B6. O que faz à água de beber em casa? (assinalar todas)",
             ["Ferve (1)", "Trata com cloro, como a Certeza (2)",
              "Coa com pano (3)", "Deixa repousar (4)", "Nada (0)"]),
        PERG("B7. Alguma vez viu um profissional de saúde ou um APE preparar "
             "a SRO para lhe mostrar como se faz?", _SIM_NAO,
             instrucao="Se Sim: quem? Enfermeira ou clínico; APE; "
                       "farmácia; palestra; outro."),
        PERG("B8. Hoje, antes desta entrevista, viu alguém demonstrar a "
             "preparação da SRO?", _SIM_NAO),
        PERG("B9. Onde costuma obter a SRO quando a criança precisa?",
             ["Unidade sanitária (1)", "APE (2)", "Farmácia privada (3)",
              "Mercado ou vendedor (4)", "Nunca obteve (5)", "Outro (6)"]),
        H3("Secção C. Conhecimentos (não ler as opções)"),
        PERG("C1. Na sua opinião, quando é que uma criança tem diarreia?",
             ["Três ou mais dejecções moles ou líquidas num dia (1)",
              "Outra resposta (0)", "Não sabe (9)"]),
        PERG("C2. Qual é o maior perigo da diarreia para a criança?",
             ["Perder água e sais, ficar desidratada (1)",
              "Outra resposta (0)", "Não sabe (9)"]),
        PERG("C3. Que sinais mostram que uma criança com diarreia está a "
             "ficar desidratada? (assinalar todos os referidos)",
             ["Olhos encovados", "Sede, bebe com avidez",
              "Pele da barriga volta devagar quando beliscada",
              "Muito mole ou sonolenta", "Boca e língua secas",
              "Urina pouco", "Outro", "Não sabe"]),
        PERG("C4. Em que situações deve levar a criança com diarreia "
             "imediatamente à unidade sanitária? (assinalar todas as "
             "referidas)",
             ["Não consegue beber ou mamar", "Vomita tudo",
              "Sangue nas fezes", "Febre", "Piora ou fica muito mole",
              "Convulsões", "Outra", "Não sabe"]),
        PERG("C5. Para que serve a SRO?",
             ["Repõe a água e os sais perdidos (1)",
              "Pára a diarreia (0)", "Mata os micróbios (0)",
              "Outra resposta (0)", "Não sabe (9)"]),
        PERG("C6. Quando se deve começar a dar a SRO?",
             ["Logo que começa a diarreia (1)",
              "Só quando a criança está fraca (0)",
              "Só com indicação do clínico (0)", "Não sabe (9)"]),
        PERG("C7. Com quanta água se prepara uma saqueta de SRO?",
             ["Com o volume indicado no rótulo da saqueta (1)",
              "Outro volume: ________ (0)", "Não sabe (9)"],
             instrucao="Registar o volume referido, em mililitros ou no "
                       "recipiente indicado: ________"),
        PERG("C8. Que água se deve usar para preparar a SRO?",
             ["Fervida e arrefecida, ou tratada com cloro (1)",
              "Qualquer água que pareça limpa (0)", "Outra (0)",
              "Não sabe (9)"]),
        PERG("C9. Depois de preparada, durante quanto tempo se pode usar a "
             "SRO?",
             ["Até 24 horas, depois deita-se fora (1)",
              "Mais de 24 horas ou até acabar (0)", "Não sabe (9)"]),
        PERG("C10. Quanta SRO se deve dar à criança depois de cada dejecção "
             "líquida?",
             ["Quantidade certa para a idade da criança índice (1)",
              "Outra quantidade (0)", "Não sabe (9)"]),
        PERG("C11. Se a criança vomitar a SRO, o que se deve fazer?",
             ["Esperar cerca de 10 minutos e continuar mais devagar (1)",
              "Parar a SRO (0)", "Outra (0)", "Não sabe (9)"]),
        PERG("C12. Durante a diarreia, a criança deve continuar a mamar e a "
             "comer?",
             ["Sim, continuar (1)", "Não, deve parar ou comer menos (0)",
              "Não sabe (9)"]),
        PERG("C13. Se não houver SRO, como se prepara a mistura caseira?",
             ["Um litro de água, oito colherinhas de açúcar e meia colherinha "
              "de sal (1)", "Outra (0)", "Não sabe (9)"]),
        PERG("C14. Para que serve o zinco na diarreia?",
             ["Faz a diarreia passar mais depressa ou torna-a menos grave "
              "(1)", "Repõe a água (0)", "Outra (0)",
              "Não sabe (9)"]),
        PERG("C15. Durante quantos dias se deve dar o zinco?",
             ["10 a 14 dias (1)", "Outro número (0)", "Não sabe (9)"],
             instrucao="Registar o número de dias referido: ______"),
        PERG("C16. Se a diarreia parar antes, deve continuar a dar o zinco?",
             ["Sim, até completar os dias (1)", "Não (0)", "Não sabe (9)"]),
        PERG("C17. Quanto zinco se dá por dia a uma criança da idade da "
             "criança índice?",
             ["Dose certa para a idade (1)", "Outra (0)", "Não sabe (9)"]),
        PERG("C18. Como se dá o zinco a um bebé?",
             ["Dissolvido numa colher de leite materno, SRO ou água limpa "
              "(1)", "Outra (0)", "Não sabe (9)"]),
        PERG("C19. Todas as diarreias precisam de antibiótico?",
             ["Não, só quando o clínico indica, como no sangue nas fezes ou "
              "na cólera (1)", "Sim (0)", "Não sabe (9)"]),
        PERG("C20. Como se apanha a cólera?",
             ["Por água ou alimentos contaminados e mãos sujas (1)",
              "Outra (0)", "Não sabe (9)"]),
        NOTA("Chave de correcção: cada item vale 1 ponto se a resposta for a "
             "codificada com (1); as outras, incluindo «não sabe», valem 0. "
             "Em C3 e C4, vale 1 ponto a referência espontânea de pelo menos "
             "dois sinais. Em C7, a resposta certa é o volume do rótulo da "
             "saqueta usada no estudo. Em C10, a quantidade certa é de 50 a "
             "100 ml abaixo dos 2 anos e de 100 a 200 ml a partir dos 2 anos. "
             "Em C17, a dose certa segue a norma nacional em vigor à data da "
             "recolha, que na AIDI é meio comprimido de 20 mg até aos 6 meses "
             "e um comprimido a partir dos 6 meses; se a norma mudar antes do "
             "pré-teste, a chave é actualizada. Pontuação de 0 a 20: bom, "
             "16-20; moderado, 12-15; fraco, 0-11."),
        H3("Secção D. Último episódio de diarreia (criança índice)"),
        PERG("D1. Nos últimos três meses, esta criança teve diarreia (três ou "
             "mais dejecções moles ou líquidas num dia)?", _SIM_NAO,
             instrucao="Se Não, terminar a entrevista e passar ao "
                       "aconselhamento."),
        PERG("D2. Há quanto tempo começou o último episódio?",
             ["Menos de 2 semanas (1)", "2 a 4 semanas (2)",
              "1 a 3 meses (3)"]),
        PERG("D3. Onde procurou ajuda ou tratamento? (assinalar todos)",
             ["Unidade sanitária (1)", "APE (2)", "Farmácia privada (3)",
              "Mercado ou vendedor (4)", "Médico tradicional (5)",
              "Não procurou (0)"]),
        PERG("D4. Deu à criança SRO de pacote?", _SIM_NAO_NS,
             instrucao="Se Sim: onde obteve? Unidade sanitária; APE; "
                       "farmácia privada; mercado; já tinha em casa; outro."),
        PERG("D5. Deu mistura caseira de água, açúcar e sal?", _SIM_NAO_NS),
        PERG("D6. Quanto deu de beber em comparação com o habitual?",
             ["Mais (1)", "O mesmo (2)", "Menos (3)", "Não sabe (9)"]),
        PERG("D7. Durante a diarreia, a criança comeu ou mamou:",
             ["Mais ou o mesmo (1)", "Menos (2)", "Nada (3)"]),
        PERG("D8. Deu comprimidos de zinco?", _SIM_NAO_NS,
             instrucao="Se Não ou Não sabe, passar a D12. Se Sim: onde "
                       "obteve? Unidade sanitária; APE; farmácia privada; "
                       "outro."),
        PERG("D9. Durante quantos dias deu o zinco? ______ dias"),
        PERG("D10. A criança tomou o zinco todos os dias até ao fim do "
             "tratamento indicado?", _SIM_NAO,
             instrucao="Se Sim, passar a D12."),
        PERG("D11. Se parou antes do fim, porquê? (assinalar todas)",
             ["A diarreia parou (1)", "A criança vomitava (2)",
              "A criança recusava (3)", "Esqueceu-se (4)",
              "Acabaram os comprimidos (5)",
              "Não sabia durante quantos dias (6)",
              "Não tinha dinheiro para comprar mais (7)", "Outra (8)"]),
        PERG("D12. Deu outro medicamento ou remédio para a diarreia? "
             "(assinalar todos)",
             ["Antibiótico (1)", "Medicamento para parar a diarreia (2)",
              "Remédio tradicional ou caseiro (3)", "Outro (4)",
              "Nenhum (0)"],
             instrucao="Nome do medicamento, se o souber: ________"),
        PERG("D13. Cartão de saúde da criança (observado com autorização):",
             ["Regista SRO ou zinco neste episódio (1)", "Não regista (2)",
              "Cartão não disponível (9)"]),
        CAMPO("Encaminhamento ao clínico de serviço: ( ) Não  ( ) Sim, "
              "motivo: ____________________"),
        CAMPO("Aconselhamento correctivo feito e folheto entregue: ( ) Sim   "
              "Hora de fim: ____:____"),
    ]),
    ("Lista de verificação da observação da preparação da solução de "
     "reidratação oral", [
        NOTA("Preparação da mesa antes de cada participante: bacia com jarro "
             "de água e sabão; dois jarros iguais, um com água da torneira da "
             "unidade e outro com água fervida e arrefecida no próprio dia "
             "(jarro de água fervida à esquerda para códigos pares e à direita "
             "para ímpares); garrafas vazias de 0,5, 1 e 1,5 litros, um copo, "
             "uma caneca, um jarro sem marcas, um recipiente com tampa e outro "
             "sem tampa; colher limpa; copo para administração; uma saqueta de "
             "SRO fechada. Guião: apresentar os dois jarros dizendo «Este tem "
             "água da torneira da unidade sanitária e este tem água que foi "
             "fervida e deixada arrefecer» e depois «Imagine que a sua criança "
             "está com diarreia em casa. Mostre-me, com este material, como "
             "prepara o soro de pacote. Faça como faz em casa.» Não ajudar, "
             "não comentar e não corrigir durante a preparação."),
        CAMPO("Código da participante: ________   Unidade: ____   "
              "Observador: ____   Segundo observador (dupla observação): ____"),
        CAMPO("Jarro de água fervida: ( ) à esquerda  ( ) à direita     "
              "Volume indicado no rótulo (V): ______ ml"),
        H3("Itens críticos"),
        PERG("E1. Usa a água fervida e arrefecida, ou refere espontaneamente "
             "que a trataria com cloro.", _CUMPRE),
        PERG("E2. Volume final medido no jarro graduado: ______ ml. O volume "
             "está entre 90% e 110% de V?", _CUMPRE),
        PERG("E3. Usa todo o conteúdo de uma única saqueta, sem fraccionar "
             "nem juntar outra.", _CUMPRE),
        PERG("E4. Não acrescenta nem pede açúcar, sal, sumo ou outro "
             "ingrediente, nem refere que o faria.", _CUMPRE),
        PERG("E5. Mistura até à dissolução completa, sem pó visível no "
             "fundo.", _CUMPRE),
        H3("Itens complementares"),
        PERG("E6. Lava as mãos com água e sabão antes de começar.", _CUMPRE),
        PERG("E7. Mede a água numa garrafa de volume conhecido, em vez de a "
             "estimar num recipiente sem medida.",
             _CUMPRE,
             instrucao="Recipiente usado: garrafa de 0,5 L; garrafa de 1 L; "
                       "garrafa de 1,5 L; copo; caneca; jarro sem marcas."),
        PERG("E8. Guarda a solução num recipiente limpo e tapado (escolhe o "
             "recipiente com tampa ou tapa-o).", _CUMPRE),
        PERG("E9. Declarado (não observável): à pergunta «Em casa, o que faz "
             "à solução que sobra no dia seguinte?», responde que a deita "
             "fora ao fim de 24 horas ou antes.", _CUMPRE),
        PERG("E10. Quando lhe é pedido, mostra que daria a solução com copo "
             "ou colher, em pequenos goles, sem biberão.", _CUMPRE),
        PERG("E11. Em casa, com que recipiente mede a água para a SRO? "
             "(registo, não pontuado): ____________________"),
        NOTA("Variáveis derivadas: preparação correcta quando E1 a E5 são "
             "todos cumpridos; pontuação de práticas igual à soma de E1 a "
             "E10, classificada como boa (8-10), moderada (6-7) ou fraca "
             "(0-5). No fim da observação, deitar fora a solução diante da "
             "cuidadora e explicar que serviu apenas para a demonstração, "
             "sem a corrigir; a demonstração correcta e as quatro regras do "
             "tratamento em casa ficam para o fim da entrevista."),
    ]),
    ("Folha de informação à participante", [
        P("Título do estudo: Conhecimentos e práticas de mães e cuidadoras "
          "sobre o tratamento da diarreia infantil com sais de reidratação "
          "oral e zinco na Cidade de Nampula, 2027. Investigador: [Nome do(a) "
          "estudante], estudante da Licenciatura em Farmácia da Faculdade de "
          "Ciências de Saúde da Universidade Lúrio, sob orientação de [Nome e "
          "grau académico do(a) orientador(a)]."),
        P("Estamos a convidá-la a participar num estudo sobre o modo como as "
          "famílias tratam a diarreia das crianças em casa com o soro de "
          "pacote (SRO) e com o zinco. Queremos saber o que as mães e as "
          "cuidadoras sabem e como preparam o soro, para melhorar os conselhos "
          "dados nas unidades sanitárias. Não se trata de um exame, e ninguém "
          "vai ser avaliado ou criticado."),
        P("Se aceitar, vamos pedir-lhe que nos mostre como prepara o soro, "
          "com material que lhe damos, e depois vamos fazer-lhe perguntas "
          "sobre si, sobre a criança e sobre a diarreia. Tudo demora cerca de "
          "45 minutos e acontece depois da consulta da criança. O soro "
          "preparado não é dado à criança e é deitado fora no fim. Podemos "
          "pedir-lhe para ver o cartão de saúde da criança, se concordar."),
        P("Participar não tem riscos para a sua saúde nem para a da criança; o "
          "único incómodo é o tempo. No fim, receberá conselhos sobre a forma "
          "correcta de preparar e dar o soro e o zinco, e um folheto com "
          "desenhos. Se a criança mostrar sinais de doença grave, será levada "
          "de imediato ao clínico de serviço. Não receberá dinheiro por "
          "participar."),
        P("A sua participação é voluntária. Pode recusar ou desistir a "
          "qualquer momento, sem dar razões, e isso não muda em nada o "
          "atendimento da criança nesta unidade. O seu nome não aparece no "
          "questionário, que tem apenas um número, e os resultados serão "
          "apresentados em conjunto, sem identificar ninguém. O estudo foi "
          "aprovado pelo Comité Institucional de Bioética para a Saúde da "
          "Universidade Lúrio e autorizado pelos serviços de saúde. Para "
          "qualquer dúvida pode contactar o investigador, o orientador ou o "
          "comité pelos contactos indicados no fim desta folha."),
        CAMPO("Contactos: investigador [preencher]; orientador [preencher]; "
              "CIBS-UniLúrio [preencher]"),
    ]),
    ("Termo de consentimento livre e esclarecido", [
        P("Declaro que me foi lida e explicada, numa língua que compreendo, a "
          "folha de informação sobre o estudo «Conhecimentos e práticas de "
          "mães e cuidadoras sobre o tratamento da diarreia infantil com sais "
          "de reidratação oral e zinco na Cidade de Nampula, 2027». "
          "Compreendi o objectivo do estudo, o que me é pedido, os riscos e os "
          "benefícios, e sei que posso desistir a qualquer momento sem "
          "prejuízo para o atendimento da criança. Tive a oportunidade de "
          "fazer perguntas e as minhas dúvidas foram esclarecidas. Aceito "
          "participar de livre vontade e recebo uma cópia deste termo."),
        CAMPO("Código da participante: ________   Data: ___/___/2027"),
        CAMPO("Assinatura da participante: ________________________________"),
        CAMPO("Impressão digital (se não sabe escrever):   [          ]"),
        NOTA("Para participantes que não sabem ler nem escrever: a testemunha "
             "imparcial, escolhida pela participante e alheia à equipa do "
             "estudo, assistiu à leitura completa da folha de informação e "
             "confirma que a participante compreendeu e deu o seu acordo "
             "livremente."),
        CAMPO("Nome da testemunha: ______________________   Assinatura: "
              "_______________"),
        CAMPO("Nome de quem obteve o consentimento: __________________   "
              "Assinatura: ____________"),
    ]),
    ("Pedido de autorização institucional", [
        P("Exmo(a). Senhor(a) Director(a) do Serviço Distrital de Saúde, "
          "Mulher e Acção Social da Cidade de Nampula (com cópia à Direcção "
          "Provincial de Saúde de Nampula e às direcções das unidades "
          "sanitárias seleccionadas)."),
        P("Assunto: pedido de autorização para a realização de um estudo nas "
          "consultas da criança das unidades sanitárias da Cidade de "
          "Nampula."),
        P("[Nome do(a) estudante], estudante da Licenciatura em Farmácia da "
          "Faculdade de Ciências de Saúde da Universidade Lúrio, vem por este "
          "meio solicitar a V. Exa. autorização para realizar o estudo "
          "«Conhecimentos e práticas de mães e cuidadoras sobre o tratamento "
          "da diarreia infantil com sais de reidratação oral e zinco na Cidade "
          "de Nampula, 2027», sob orientação de [Nome e grau académico do(a) "
          "orientador(a)], como trabalho de culminação do curso."),
        P("O estudo envolve 648 cuidadoras de crianças menores de cinco anos, "
          "em doze unidades sanitárias sorteadas, em Março e Abril de 2027. "
          "Cada participante, depois de dar o seu consentimento, mostra como "
          "prepara a solução de reidratação oral com material fornecido pelo "
          "estudo e responde a uma entrevista, num espaço reservado e depois "
          "da consulta da criança, sem interferir no funcionamento dos "
          "serviços. Solicita-se ainda o acesso aos dados agregados do volume "
          "de consultas da criança do ano de 2026, necessários ao sorteio, e a "
          "cedência de um espaço em cada unidade durante três a quatro dias."),
        P("O protocolo foi submetido ao Comité Institucional de Bioética "
          "para a Saúde da Universidade Lúrio e a recolha só começa depois "
          "da sua aprovação. As "
          "unidades e as participantes não serão identificadas nos relatórios "
          "públicos, as crianças com sinais de doença grave serão encaminhadas "
          "de imediato ao clínico de serviço e todas as cuidadoras receberão "
          "aconselhamento. Os resultados serão entregues a V. Exa. e às "
          "direcções das unidades, com recomendações para o aconselhamento "
          "sobre a SRO e o zinco. Junta-se o protocolo e, logo que emitido, o "
          "parecer ético."),
        CAMPO("Nampula, ___ de ____________ de 2027"),
        CAMPO("O(A) estudante: ______________________   O(A) orientador(a): "
              "______________________"),
    ]),
]
