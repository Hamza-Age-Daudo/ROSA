# -*- coding: utf-8 -*-
"""
Tema 12: Reaccoes adversas aos medicamentos antituberculosos de primeira linha
nos centros de saude da cidade de Nampula (Farmacovigilancia e Seguranca do
Medicamento). Coorte retrospectiva documental das fichas de tratamento de 2026,
com entrevista aos doentes ainda em tratamento, recolha em 2027.

Compor e validar:   python _motor/motor.py _conteudo/tema_12.py
Verificar fontes:   python _motor/refs.py verificar _conteudo/tema_12.py
"""
from blocos import (CAMPO, ESCALA, FORMULA, H3, LISTA, NOTA, P, PERG, QUADRO,
                    TABELA)

NUMERO = 12
SLUG = "Reaccoes_Adversas_Antituberculosos_Nampula"
TITULO = ("Reacções adversas aos medicamentos antituberculosos de primeira "
          "linha em adultos tratados nos centros de saúde da cidade de "
          "Nampula, 2026-2027")
DESENHO = ("Coorte retrospectiva documental (fichas de tratamento), com "
           "componente transversal de entrevista aos doentes ainda em "
           "seguimento")

AUTOR = "[Nome do(a) estudante]"
ORIENTADOR = "[Nome e grau académico do(a) orientador(a)]"

# ---------------------------------------------------------------- resumo --
RESUMO = (
    "O tratamento da tuberculose junta quatro medicamentos tomados todos os "
    "dias durante seis meses e provoca com frequência reacções adversas que "
    "levam à perda de doses, à mudança do esquema e ao abandono. Os estudos "
    "que perguntam ao doente encontram reacções em mais de metade dos casos, "
    "enquanto os que se limitam aos registos clínicos encontram proporções "
    "muito menores, o que sugere um sub-registo importante. Em Moçambique, "
    "onde cerca de um quarto dos doentes notificados também vive com o vírus "
    "da imunodeficiência humana, não se encontrou nenhum estudo publicado "
    "sobre a frequência destas reacções. O estudo tem como objectivo "
    "determinar a incidência das reacções adversas aos medicamentos "
    "antituberculosos de primeira linha e os factores a ela associados, em "
    "adultos que iniciaram tratamento nos centros de saúde da cidade de "
    "Nampula entre o primeiro dia de Janeiro e o último dia de Dezembro de "
    "2026. Trata-se de uma coorte retrospectiva construída a partir das "
    "fichas de tratamento, completada por entrevista aos doentes ainda em "
    "tratamento no momento da recolha, que decorre em 2027, depois da "
    "aprovação ética. Serão estudadas 600 fichas escolhidas por amostragem "
    "sistemática e realizadas cerca de 115 entrevistas. Uma ficha de "
    "extracção sem identificadores, verificada em trinta registos do ano "
    "anterior, e um guião adaptado de instrumentos publicados e traduzido "
    "para a língua local recolhem o tipo de reacção, a data de início, a "
    "gravidade e a conduta adoptada. Dois avaliadores independentes "
    "classificam a causalidade, com medida da concordância corrigida para o "
    "acaso. A análise estima a incidência acumulada e a taxa por pessoa-mês, "
    "compara os doentes com e sem o vírus e modela o tempo até à primeira "
    "reacção. Espera-se quantificar o sub-registo e orientar a vigilância da "
    "segurança do tratamento.")
PALAVRAS_CHAVE = ["farmacovigilância", "hepatotoxicidade", "Moçambique",
                  "reacções adversas a medicamentos", "tuberculose"]
ABSTRACT = (
    "Tuberculosis treatment combines four medicines taken every day for six "
    "months and often causes adverse reactions that lead to missed doses, "
    "regimen changes and treatment abandonment. Studies that ask patients "
    "directly find reactions in more than half of the cases, whereas those "
    "relying only on clinical records find much lower proportions, which "
    "suggests substantial under-recording. In Mozambique, where about one "
    "quarter of notified patients also live with the human immunodeficiency "
    "virus, no published study on the frequency of these reactions was "
    "found. The study aims to determine the incidence of adverse reactions "
    "to first-line antituberculosis medicines and the factors associated "
    "with it, among adults who started treatment in the health centres of "
    "the city of Nampula between the first day of January and the last day "
    "of December 2026. It is a retrospective cohort built from treatment "
    "cards, complemented by interviews with patients still on treatment at "
    "the time of data collection, which takes place in 2027 after ethical "
    "approval. A total of 600 treatment cards selected by systematic "
    "sampling will be studied and about 115 interviews conducted. A data "
    "extraction form without identifiers, tested on thirty records from the "
    "previous year, and an interview guide adapted from published "
    "instruments and translated into the local language will record the type "
    "of reaction, date of onset, severity and management. Two independent "
    "assessors will classify causality, with chance-corrected agreement "
    "measured. The analysis will estimate cumulative incidence and rates per "
    "person-month, compare patients with and without the virus and model the "
    "time to the first reaction. The study is expected to quantify "
    "under-recording and to guide safety monitoring of treatment.")
KEYWORDS = ["adverse drug reactions", "antitubercular agents",
            "hepatotoxicity", "Mozambique", "pharmacovigilance"]

ABREVIATURAS = [
    ("ALT", "alanina aminotransferase"),
    ("ANARME", "Autoridade Nacional Reguladora de Medicamentos"),
    ("AST", "aspartato aminotransferase"),
    ("CD4", "linfócitos T auxiliares que expressam o antigénio CD4"),
    ("CIBS-UniLúrio", "Comité Institucional de Bioética para a Saúde da "
                      "Universidade Lúrio"),
    ("CNBS", "Comité Nacional de Bioética para a Saúde"),
    ("CTCAE", "Common Terminology Criteria for Adverse Events (critérios "
              "terminológicos comuns para acontecimentos adversos)"),
    ("FCS", "Faculdade de Ciências de Saúde"),
    ("HIV", "vírus da imunodeficiência humana"),
    ("HR", "razão de riscos instantâneos"),
    ("HRa", "razão de riscos instantâneos ajustada"),
    ("IC95%", "intervalo de confiança a 95%"),
    ("IIQ", "intervalo interquartil"),
    ("IMC", "índice de massa corporal"),
    ("MISAU", "Ministério da Saúde"),
    ("OMS", "Organização Mundial da Saúde"),
    ("PNCT", "Programa Nacional de Controlo da Tuberculose"),
    ("RAM", "reacção adversa a medicamentos"),
    ("RECORD", "REporting of studies Conducted using Observational "
               "Routinely-collected health Data"),
    ("SDSMAS", "Serviço Distrital de Saúde, Mulher e Acção Social"),
    ("SPSS", "Statistical Package for the Social Sciences"),
    ("STROBE", "Strengthening the Reporting of Observational Studies in "
               "Epidemiology"),
    ("TARV", "tratamento anti-retroviral"),
    ("UniLúrio", "Universidade Lúrio"),
    ("WHO-UMC", "sistema de avaliação da causalidade da Organização Mundial "
                "da Saúde e do Centro de Monitorização de Uppsala"),
]

# ------------------------------------------------------------ referencias --
FONTES = {
    # -- carga da tuberculose e tratamento
    "who_gtb2025": "World Health Organization. Global tuberculosis report 2025 [Internet]. Geneva: World Health Organization; 2025 [citado 2026 Set 19]. Disponível em: https://www.who.int/teams/global-programme-on-tuberculosis-and-lung-health/tb-reports/global-tuberculosis-report-2025",
    "who_mod4_2025": "World Health Organization. WHO consolidated guidelines on tuberculosis: module 4: treatment and care [Internet]. Geneva: World Health Organization; 2025 [citado 2026 Set 19]. Disponível em: https://www.who.int/publications/i/item/9789240107243",
    "gbd2026": "GBD 2023 TB HIV Collaborators. Global, regional, and national burden of tuberculosis and multidrug-resistant tuberculosis by HIV status, 1990-2023: a systematic analysis for the Global Burden of Disease Study 2023. Lancet Infect Dis. 2026. doi:10.1016/S1473-3099(26)00295-1. PMID: 42385762.",
    # -- reaccoes adversas ao tratamento antituberculoso
    "edwards2000": "Edwards IR, Aronson JK. Adverse drug reactions: definitions, diagnosis, and management. Lancet. 2000;356(9237):1255-9. doi:10.1016/S0140-6736(00)02799-9. PMID: 11072960.",
    "choi2022": "Choi H, Park HA, Hyun IG, Kim JH, Hwang YI, Jang SH, et al. Incidence and outcomes of adverse drug reactions to first-line anti-tuberculosis drugs and their effects on the quality of life: A multicenter prospective cohort study. Pharmacoepidemiol Drug Saf. 2022;31(11):1153-1163. doi:10.1002/pds.5513. PMID: 35909258.",
    "elhamdouni2020": "El Hamdouni M, Ahid S, Bourkadi JE, Benamor J, Hassar M, Cherrah Y. Incidence of adverse reactions caused by first-line anti-tuberculosis drugs and treatment outcome of pulmonary tuberculosis patients in Morocco. Infection. 2020;48(1):43-50. doi:10.1007/s15010-019-01324-3. PMID: 31165445.",
    "amalba2021": "Amalba A, Bugri AA. Assessing the prevalence and effect of adverse drug reactions among patients receiving first line anti-tubercular medicines in the Tamale Teaching Hospital, Ghana. Pan Afr Med J. 2021;38:191. doi:10.11604/pamj.2021.38.191.24301. PMID: 33995797.",
    "tzelios2025": "Tzelios CA, Malatesta S, Carney T, White LF, Weber SE, Thomson S, et al. Patient Determinants and Effects on Adherence of Adverse Drug Reactions to Tuberculosis Treatment: A Prospective Cohort Analysis. Clin Infect Dis. 2025;81(1):167-175. doi:10.1093/cid/ciae642. PMID: 39973802.",
    "sant2023": "Sant Anna FM, Araújo-Pereira M, Schmaltz CAS, Arriaga MB, Andrade BB, Rolla VC. Impact of adverse drug reactions on the outcomes of tuberculosis treatment. PLoS One. 2023;18(2):e0269765. doi:10.1371/journal.pone.0269765. PMID: 36749743.",
    "dixon2025": "Dixon EG, Biraua E, Brencsēns E, Pašuks V, Riekstina V, Šperberga A, et al. Adverse drug reactions, particularly liver disorders, drive interruptions in anti-tuberculosis treatment: A retrospective cohort study. Br J Clin Pharmacol. 2025;91(12):3461-3470. doi:10.1002/bcp.70197. PMID: 40785321.",
    "chung2022": "Chung SJ, Byeon SJ, Choi JH. Analysis of Adverse Drug Reactions to First-Line Anti-Tuberculosis Drugs Using the Korea Adverse Event Reporting System. J Korean Med Sci. 2022;37(16):e128. doi:10.3346/jkms.2022.37.e128. PMID: 35470602.",
    "mishra2023": "Mishra P, Bhat J, Yadav R, Sharma RK, Rao VG. Adverse Drug Reaction Patterns of First-line Anti-tubercular Drugs among Saharia Tuberculosis Patients: An Observational Study in Particularly Vulnerable Tribal Group of Madhya Pradesh, India. Indian J Public Health. 2023;67(4):542-545. doi:10.4103/ijph.ijph_865_22. PMID: 38934815.",
    "zhu2025": "Zhu L, Xu Y, Chen T, Lin D, Lin Q. Adverse Reactions and Clinical Outcomes of First-line Antituberculosis Drugs in Elderly Patients with Tuberculosis. Niger J Clin Pract. 2025;28(11):1305-1313. doi:10.4103/njcp.njcp_745_24. PMID: 41317053.",
    "he2026": "He K, Zhang J, Du X, He X, Zeng Y, Liu M. Common Adverse Reactions and Management Strategies of First-Line Anti-Tuberculosis Drugs. Infect Drug Resist. 2026;19:564580. doi:10.2147/IDR.S564580. PMID: 41939271.",
    "prasad2019": "Prasad R, Singh A, Gupta N. Adverse drug reactions in tuberculosis and management. Indian J Tuberc. 2019;66(4):520-532. doi:10.1016/j.ijtb.2019.11.005. PMID: 31813444.",
    # -- hepatotoxicidade
    "petros2025": "Petros Z, Tamirat A, Assefa W. Antitubercular drug induced liver injury among tuberculosis patients in central Ethiopia. Sci Rep. 2025;15(1):31309. doi:10.1038/s41598-025-15855-3. PMID: 40854941.",
    "nyangwara2025": "Nyangwara V, Waja Z, Thelingwani R, Osman R, Pretorius Z, Majoro K, et al. Incidence and associated risk factors of anti-tuberculosis drug induced liver injury among TB patients. BMC Infect Dis. 2025;25(1):1400. doi:10.1186/s12879-025-11796-4. PMID: 41137008.",
    "wondwossen2016": "Wondwossen Abera, Waqtola Cheneke, Gemeda Abebe. Incidence of antituberculosis-drug-induced hepatotoxicity and associated risk factors among tuberculosis patients in Dawro Zone, South Ethiopia: A cohort study. Int J Mycobacteriol. 2016;5(1):14-20. doi:10.1016/j.ijmyco.2015.10.002. PMID: 26927985.",
    "atuel2026": "Atuel RCG, Gutierrez EA, Hiranburana N, Apornpong T, Ubolyam S, Gler MTS, et al. Incidence, risk factors, and outcomes of anti-tuberculosis drug-induced hepatotoxicity in people with and without HIV in Thailand and the Philippines. Asian Biomed (Res Rev News). 2026;20(3):170-181. doi:10.2478/abm-2026-0020. PMID: 42541216.",
    "kumarmeta2025": "Kumar R, Kumar A, Patel R, Prakash SS, Kumar S, Surya H, et al. Incidence and risk factors of antituberculosis drug-induced liver injury in India: A systematic review and meta-analysis. Indian J Gastroenterol. 2025;44(1):35-46. doi:10.1007/s12664-024-01643-w. PMID: 39225936.",
    "kumarfalencia2025": "Kumar R, Kumar A, Kumar S. Acute liver failure from anti-tuberculosis drug-induced liver injury: An update. World J Hepatol. 2025;17(5):106618. doi:10.4254/wjh.v17.i5.106618. PMID: 40501479.",
    "lewis2024": "Lewis JH, Korkmaz SY, Rizk CA, Copeland MJ. Diagnosis, prevention and risk-management of drug-induced liver injury due to medications used to treat mycobacterium tuberculosis. Expert Opin Drug Saf. 2024;23(9):1093-1107. doi:10.1080/14740338.2024.2399074. PMID: 39212296.",
    "ali2020": "Ali N, Gupta N, Saravu K. Malnutrition as an important risk factor for drug-induced liver injury in patients on anti-tubercular therapy: an experience from a tertiary care center in South India. Drug Discov Ther. 2020;14(3):135-138. doi:10.5582/ddt.2020.03029. PMID: 32669522.",
    # -- co-infeccao pelo HIV e reaccoes cutaneas
    "boonyagars2017": "Boonyagars L, Hirunwiwatkul P, Hurst CP. CD4 count and risk of anti-tuberculosis drug-associated cutaneous reactions in HIV-infected Thai patients. Int J Tuberc Lung Dis. 2017;21(3):338-344. doi:10.5588/ijtld.16.0425. PMID: 28225346.",
    "schnippel2017": "Schnippel K, Firnhaber C, Berhanu R, Page-Shipp L, Sinanovic E. Adverse drug reactions during drug-resistant TB treatment in high HIV prevalence settings: a systematic review and meta-analysis. J Antimicrob Chemother. 2017;72(7):1871-1879. doi:10.1093/jac/dkx107. PMID: 28419314.",
    "merid2019": "Merid MW, Gezie LD, Kassa GM, Muluneh AG, Akalu TY, Yenit MK. Incidence and predictors of major adverse drug events among drug-resistant tuberculosis patients on second-line anti-tuberculosis treatment in Amhara regional state public hospitals; Ethiopia: a retrospective cohort study. BMC Infect Dis. 2019;19(1):286. doi:10.1186/s12879-019-3919-1. PMID: 30917788.",
    # -- farmacovigilancia, causalidade e gravidade
    "umc_causalidade": "Uppsala Monitoring Centre. The use of the WHO-UMC system for standardised case causality assessment [Internet]. Uppsala: Uppsala Monitoring Centre; 2018 [citado 2026 Set 19]. Disponível em: https://www.who.int/docs/default-source/medicines/pharmacovigilance/whocausality-assessment.pdf",
    "naranjo1981": "Naranjo CA, Busto U, Sellers EM, Sandor P, Ruiz I, Roberts EA, et al. A method for estimating the probability of adverse drug reactions. Clin Pharmacol Ther. 1981;30(2):239-45. doi:10.1038/clpt.1981.154. PMID: 7249508.",
    "more2024": "More SA, Atal S, Mishra PS. Inter-rater agreement between WHO- Uppsala Monitoring Centre system and Naranjo algorithm for causality assessment of adverse drug reactions. J Pharmacol Toxicol Methods. 2024;127:107514. doi:10.1016/j.vascn.2024.107514. PMID: 38768933.",
    "pandit2024": "Pandit S, Soni D, Krishnamurthy B, Belhekar MN. Comparison of WHO-UMC and Naranjo Scales for Causality Assessment of Reported Adverse Drug Reactions. J Patient Saf. 2024;20(4):236-239. doi:10.1097/PTS.0000000000001213. PMID: 38345209.",
    "ctcae2017": "National Cancer Institute. Common Terminology Criteria for Adverse Events (CTCAE) version 5.0 [Internet]. Bethesda: National Institutes of Health; 2017 [citado 2026 Set 19]. Disponível em: https://dctd.cancer.gov/research/ctep-trials/for-sites/adverse-events/ctcae-v5-8x11.pdf",
    "who_adsm2015": "World Health Organization. Active tuberculosis drug-safety monitoring and management (aDSM): framework for implementation [Internet]. Geneva: World Health Organization; 2015 [citado 2026 Set 19]. Disponível em: https://www.who.int/publications/i/item/WHO-HTM-TB-2015.28",
    "tiemersma2019": "Tiemersma E, van den Hof S, Dravniece G, Wares F, Molla Y, Permata Y, et al. Integration of drug safety monitoring in tuberculosis treatment programmes: country experiences. Eur Respir Rev. 2019;28(153). doi:10.1183/16000617.0115-2018. PMID: 31604816.",
    "tiemersma2021": "Tiemersma EW, Ali I, Alemu A, Avong YK, Duga A, Elagbaje C, et al. Baseline assessment of pharmacovigilance activities in four sub-Saharan African countries: a perspective on tuberculosis. BMC Health Serv Res. 2021;21(1):1062. doi:10.1186/s12913-021-07043-6. PMID: 34625085.",
    "kampichit2024": "Kampichit S, Srisuriyachanchai W, Pratipanawatr T, Jarernsiripornkul N. Accuracy in patient-reported adverse drug reactions and their recognition: a mixed-methods study. Int J Clin Pharm. 2024;46(2):401-410. doi:10.1007/s11096-023-01669-8. PMID: 38151687.",
    # -- Mocambique e Nampula
    "misau_pnct2019": "Ministério da Saúde (Moçambique), Programa Nacional de Controlo da Tuberculose. Protocolos nacionais: avaliação e manejo de pacientes com tuberculose. Versão 2 [Internet]. Maputo: Ministério da Saúde; 2019 [citado 2026 Set 19]. Disponível em: https://comitetarvmisau.co.mz/docs/orientacoes_nacionais/Gui%C3%A3o_Normas_cl%C3%ADnicas_PNCT_Dez19.pdf",
    "misau_pnct2021": "Ministério da Saúde (Moçambique), Direcção Nacional de Saúde Pública, Programa Nacional de Controlo da Tuberculose. Relatório anual do programa 2020 [Internet]. Maputo: Ministério da Saúde; 2021 [citado 2026 Set 19]. Disponível em: https://docs.bvsalud.org/biblioref/2021/11/1344394/relatorio-anual-do-pnct-2020_final_v23062021.pdf",
    "garciabasteiro2016": "García-Basteiro AL, Respeito D, Augusto OJ, López-Varela E, Sacoor C, Sequera VG, et al. Poor tuberculosis treatment outcomes in Southern Mozambique (2011-2012). BMC Infect Dis. 2016;16:214. doi:10.1186/s12879-016-1534-y. PMID: 27198545.",
    "osorio2022": "Osório D, Munyangaju I, Nacarapa E, Nhangave AV, Ramos-Rincon JM. Predictors of unfavourable tuberculosis treatment outcome in Bilene District, Gaza Province, Mozambique: A retrospective analysis, 2016 - 2019. S Afr Med J. 2022;112(3):234-239. PMID: 35380527.",
    "nacarapa2020": "Nacarapa E, Muchiri E, Moon TD, Charalambous S, Verdu ME, Ramos JM, et al. Effect of Xpert MTB/RIF testing introduction and favorable outcome predictors for tuberculosis treatment among HIV infected adults in rural southern Mozambique. A retrospective cohort study. PLoS One. 2020;15(3):e0229995. doi:10.1371/journal.pone.0229995. PMID: 32150595.",
    "ndhlovu2026": "Ndhlovu M, Wuethrich L, Huwa J, Thawani A, Chiwaya G, Kudzala A, et al. Evaluating tuberculosis treatment outcomes and predictors in five Southern African countries: A multi-country cohort analysis. medRxiv. 2026. doi:10.64898/2026.03.18.26348675. PMID: 41891031.",
    "xavier2022": "Xavier SP, Victor A, Cumaquela G, Vasco MD, Rodrigues OAS. Inappropriate use of antibiotics and its predictors in pediatric patients admitted at the Central Hospital of Nampula, Mozambique. Antimicrob Resist Infect Control. 2022;11(1):79. doi:10.1186/s13756-022-01115-w. PMID: 35655272.",
    "ine2021": "Instituto Nacional de Estatística (Moçambique). IV Recenseamento Geral da População e Habitação 2017: resultados definitivos, província de Nampula [Internet]. Nampula: Instituto Nacional de Estatística; 2021 [citado 2026 Set 19]. Disponível em: http://www.sina.gov.mz/wp-content/uploads/2024/05/NAMPULA-RESUTADOS-DEFINITIVOS-DO-CENSO-2017.pdf",
    "lei3de2023": "República de Moçambique. Lei n.º 3/2023, de 8 de Junho: Lei de Investigação em Saúde Humana [Internet]. Maputo: Imprensa Nacional de Moçambique; 2023 [citado 2026 Set 19]. Disponível em: https://anarme.gov.mz/download/lei-3-2023-de-8-de-junho-lei-de-investigacao-em-saude-humana/",
    # -- metodo, relato e etica
    "vonelm2007": "von Elm E, Altman DG, Egger M, Pocock SJ, Gøtzsche PC, Vandenbroucke JP. Strengthening the Reporting of Observational Studies in Epidemiology (STROBE) statement: guidelines for reporting observational studies. BMJ. 2007;335(7624):806-8. doi:10.1136/bmj.39335.541782.AD. PMID: 17947786.",
    "benchimol2015": "Benchimol EI, Smeeth L, Guttmann A, Harron K, Moher D, Petersen I, et al. The REporting of studies Conducted using Observational Routinely-collected health Data (RECORD) statement. PLoS Med. 2015;12(10):e1001885. doi:10.1371/journal.pmed.1001885. PMID: 26440803.",
    "peduzzi1996": "Peduzzi P, Concato J, Kemper E, Holford TR, Feinstein AR. A simulation study of the number of events per variable in logistic regression analysis. J Clin Epidemiol. 1996;49(12):1373-9. doi:10.1016/s0895-4356(96)00236-3. PMID: 8970487.",
    "mchugh2012": "McHugh ML. Interrater reliability: the kappa statistic. Biochem Med (Zagreb). 2012;22(3):276-82. PMID: 23092060.",
    "wma2025": "World Medical Association. World Medical Association Declaration of Helsinki: Ethical Principles for Medical Research Involving Human Participants. JAMA. 2025;333(1):71-74. doi:10.1001/jama.2024.21972. PMID: 39425955.",
}

SEMINAIS = {
    "edwards2000": ("Artigo de referência que fixa a definição e a "
                    "classificação das reacções adversas a medicamentos "
                    "usada na farmacovigilância contemporânea; é a definição "
                    "operacional adoptada pelo estudo."),
    "naranjo1981": ("Publicação original do algoritmo de Naranjo, "
                    "instrumento de avaliação da causalidade aplicado no "
                    "estudo; não foi substituído por versão posterior."),
    "vonelm2007": ("Declaração STROBE original, norma de relato dos estudos "
                   "observacionais que a extensão RECORD complementa."),
    "benchimol2015": ("Declaração RECORD, norma de relato específica dos "
                      "estudos que usam dados de saúde recolhidos por "
                      "rotina, como as fichas de tratamento da tuberculose."),
    "peduzzi1996": ("Estudo de simulação que fundamenta a regra de pelo "
                    "menos 10 eventos por parâmetro nos modelos "
                    "multivariáveis, usada no planeamento da análise."),
    "mchugh2012": ("Artigo metodológico de referência sobre a interpretação "
                   "do kappa de Cohen em investigação em saúde, usado para "
                   "fixar o limiar de concordância entre avaliadores."),
    "who_adsm2015": ("Quadro de referência da Organização Mundial da Saúde "
                     "que define a monitorização activa da segurança dos "
                     "medicamentos antituberculosos e os conceitos de "
                     "acontecimento adverso e de acontecimento adverso "
                     "grave usados no estudo; mantém-se em vigor."),
}

# ----------------------------------------------------- 1. introducao --------
INTRODUCAO = [
    P("A tuberculose continua a ser uma das principais causas de morte por um "
      "único agente infeccioso. Em 2024 adoeceram com tuberculose cerca de "
      "10,7 milhões de pessoas em todo o mundo, incluindo 5,8 milhões de "
      "homens, 3,7 milhões de mulheres e 1,2 milhões de crianças e "
      "adolescentes, e a doença causou 1,23 milhões de mortes, das quais "
      "150.000 em pessoas que vivem com o vírus da imunodeficiência humana "
      "(HIV); as pessoas com HIV representaram 5,8% do total de casos e cerca "
      "de 619.000 delas desenvolveram tuberculose {who_gtb2025}. O tratamento "
      "da forma sensível assenta num esquema de seis meses com rifampicina, "
      "isoniazida, pirazinamida e etambutol na fase intensiva, seguido de "
      "rifampicina e isoniazida na fase de manutenção, e alcança uma taxa de "
      "sucesso de 88% a nível mundial {who_gtb2025,who_mod4_2025}."),
    P("A eficácia deste esquema tem como contrapartida uma exposição diária a "
      "quatro medicamentos durante meses, com um perfil de toxicidade "
      "conhecido: lesão hepática pela isoniazida, pela rifampicina e pela "
      "pirazinamida, neuropatia periférica pela isoniazida, reacções "
      "cutâneas por qualquer um deles, perturbações gastrointestinais e "
      "neurite óptica pelo etambutol {prasad2019,he2026}. A frequência "
      "medida depende sobretudo do modo como se procuram as reacções. Nos "
      "estudos prospectivos que interrogam o doente de forma sistemática, "
      "67,8% de 410 doentes coreanos tiveram pelo menos uma reacção de grau "
      "2 ou superior {choi2022} e 78,6% de 550 doentes de um centro de "
      "referência brasileiro tiveram reacções adversas {sant2023}. Nos "
      "estudos que se limitam ao que está escrito nos processos, os valores "
      "são muito menores: numa coorte de 2.532 doentes tratados em 18 "
      "centros de Marrocos, apenas 10,0% tinham reacções adversas "
      "registadas, sendo 7,4% gastrointestinais, 3,7% cutâneas e 2,0% "
      "hepáticas {elhamdouni2020}."),
    P("A diferença entre estes dois retratos não é académica. As reacções "
      "adversas fazem perder doses e podem levar à interrupção do "
      "tratamento: numa coorte retrospectiva de 174 adultos, 54 (31,0%) "
      "perderam doses por causa de reacções adversas, e as perturbações "
      "hepatobiliares foram o grupo que causou as interrupções mais longas, "
      "com uma mediana de 15,0 dias {dixon2025}. Num inquérito mensal a 286 "
      "doentes da África do Sul, cerca de metade teve reacções adversas e, "
      "entre os que tiveram reacções moderadas ou graves, a infecção pelo "
      "HIV com contagem de linfócitos T auxiliares que expressam o antigénio "
      "CD4 (CD4) inferior a 200 células por microlitro associou-se a mais "
      "doses perdidas {tzelios2025}. Em Tamale, no Gana, 77% dos doentes "
      "referiram reacções adversas, as queixas gastrointestinais foram as "
      "mais frequentes (80%) e mais de metade dos que tiveram reacções "
      "alterou a forma como tomava os medicamentos {amalba2021}."),
    P("Em África, a evidência concentra-se na hepatotoxicidade e é "
      "heterogénea. Numa coorte prospectiva de 219 doentes seguidos em "
      "centros de saúde da Etiópia central, 16,0% desenvolveram lesão "
      "hepática, associada ao sexo, à idade, ao índice de massa corporal "
      "(IMC) e ao estado serológico para o HIV, com uma razão de "
      "possibilidades ajustada de 6,73 para a infecção pelo HIV "
      "{petros2025}; noutra coorte etíope, a incidência foi de 8% e a "
      "mediana do tempo até à lesão hepática foi de 26 dias "
      "{wondwossen2016}; num estudo sul-africano com 610 doentes, a "
      "incidência foi de apenas 2,1%, valor que os autores atribuem à falta "
      "de definições padronizadas entre estudos {nyangwara2025}. As reacções "
      "cutâneas são também frequentes nos doentes com co-infecção: numa "
      "coorte retrospectiva de 307 adultos com tuberculose e HIV, "
      "ocorreram em 48 doentes, com uma taxa de 0,41 acontecimentos por "
      "pessoa-ano {boonyagars2017}. Os sistemas nacionais de "
      "farmacovigilância da região permanecem frágeis, com sobreposição de "
      "papéis e tarefas por cumprir, entre as quais a avaliação da "
      "causalidade {tiemersma2021}."),
    P("Moçambique faz parte da lista de países com alta carga de "
      "tuberculose, de co-infecção e de tuberculose resistente. Em 2020 "
      "foram notificados 97.093 casos de todas as formas, o que corresponde "
      "a uma taxa de notificação de 323 casos por 100.000 habitantes, a taxa "
      "de sucesso do tratamento da forma sensível foi de 92% e, dos 26.354 "
      "doentes co-infectados notificados, 95% estavam em tratamento "
      "anti-retroviral (TARV) {misau_pnct2021}. Os protocolos nacionais do "
      "Programa Nacional de Controlo da Tuberculose (PNCT) dedicam um "
      "capítulo aos efeitos adversos, classificam-nos em graus, fixam a "
      "conduta para cada um e determinam que todas as reacções adversas "
      "sejam notificadas na ficha própria do sector de farmacovigilância "
      "{misau_pnct2019}."),
    P("A província de Nampula é a mais populosa do país, com 5.758.920 "
      "habitantes no censo de 2017, 20,6% da população nacional {ine2021}, e "
      "notificou 11.805 casos de tuberculose em 2020, o terceiro maior "
      "número do país, embora com uma das taxas de notificação mais baixas, "
      "o que aponta para casos não detectados; nesse ano a província "
      "alcançou 83% da meta de notificação, 92% de sucesso do tratamento e "
      "97% de cobertura do TARV nos doentes co-infectados {misau_pnct2021}. "
      "Não se encontrou nenhum estudo publicado sobre reacções adversas aos "
      "medicamentos antituberculosos em Moçambique, e o único estudo "
      "publicado sobre o uso de medicamentos em Nampula analisou "
      "antibióticos em crianças internadas {xavier2022}."),
    P("Sem uma medida local, o programa não sabe quantos doentes "
      "interrompem ou perdem doses por causa da toxicidade, que reacções "
      "predominam, quão graves são, se a conduta segue o protocolo nacional "
      "e se chegam a ser notificadas. O presente estudo determina a "
      "incidência das reacções adversas aos medicamentos antituberculosos de "
      "primeira linha e os factores a ela associados nos adultos que "
      "iniciaram tratamento nos centros de saúde da cidade de Nampula em "
      "2026, juntando aos registos das fichas de tratamento a informação "
      "obtida junto dos doentes ainda em seguimento, de modo a estimar "
      "também o que fica por registar."),
]

# ----------------------------------------------------- 2. problema ----------
PROBLEMA = [
    P("Nos centros de saúde da cidade de Nampula, o doente com tuberculose "
      "recebe todos os dias, durante seis meses, uma associação de "
      "medicamentos em dose fixa combinada, e a ficha de tratamento é o "
      "documento onde se anota a evolução, incluindo os efeitos adversos. O "
      "protocolo nacional manda perguntar, em cada consulta, pelos sintomas "
      "de toxicidade, nomeadamente formigueiro ou dor nos membros "
      "inferiores e cansaço, náuseas, vómitos e dor abdominal, e manda "
      "graduar e notificar as reacções encontradas {misau_pnct2019}. "
      "Desconhece-se, porém, com que frequência estas perguntas se traduzem "
      "num registo, e a experiência de outros países mostra que a distância "
      "entre o que o doente sente e o que fica escrito é grande: a "
      "proporção medida por entrevista chega a ser sete vezes superior à "
      "proporção registada nos processos {choi2022,elhamdouni2020}."),
    P("As consequências desta lacuna somam-se. Quando a reacção não é "
      "reconhecida, o doente reduz ou suspende as tomas por iniciativa "
      "própria, como fizeram 84,6% dos doentes ganeses que referiram ter "
      "alterado a medicação por causa de reacções adversas {amalba2021}; "
      "quando é reconhecida tarde, a lesão hepática pode evoluir para "
      "insuficiência hepática aguda, cuja mortalidade permanece elevada "
      "{kumarfalencia2025}. As interrupções prolongam a doença, favorecem a "
      "transmissão e associam-se a desfechos desfavoráveis, que em "
      "Moçambique atingiram proporções preocupantes em coortes do sul do "
      "país {garciabasteiro2016,osorio2022}. E, se as reacções não são "
      "notificadas, o sistema nacional de farmacovigilância fica sem "
      "informação para agir, o que é comum na região {tiemersma2021}."),
    P("Falta saber, para a cidade de Nampula, quantos doentes tiveram "
      "reacções adversas durante o tratamento, que órgãos e sistemas foram "
      "atingidos, em que momento do tratamento, com que gravidade, com que "
      "relação de causalidade com os medicamentos, que conduta foi adoptada "
      "e que proporção foi notificada. Falta também saber se os doentes com "
      "co-infecção pelo HIV, os mais velhos e os que iniciam o tratamento "
      "com desnutrição têm maior risco, como sugerem estudos africanos e "
      "asiáticos {petros2025,ali2020,zhu2025}, e quanto do que os doentes "
      "sentem escapa à ficha de tratamento. O número de centros de saúde "
      "com tratamento da tuberculose na cidade e o número de adultos que "
      "iniciaram tratamento em 2026 não estão publicados e terão de ser "
      "obtidos no início da recolha [confirmar junto do Serviço Distrital "
      "de Saúde, Mulher e Acção Social (SDSMAS) da Cidade de Nampula]."),
]
PERGUNTA = ("Qual é a incidência das reacções adversas aos medicamentos "
            "antituberculosos de primeira linha nos adultos que iniciaram "
            "tratamento nos centros de saúde da cidade de Nampula entre 1 de "
            "Janeiro e 31 de Dezembro de 2026, e que factores se associam à "
            "sua ocorrência?")
DELIMITACAO = [
    P("O estudo decorre nos centros de saúde da cidade de Nampula que têm "
      "tratamento da tuberculose e abrange os adultos com 18 ou mais anos "
      "que iniciaram um esquema de primeira linha para tuberculose sensível "
      "entre 1 de Janeiro e 31 de Dezembro de 2026. O seguimento de cada "
      "doente vai da primeira toma até ao fim do tratamento, com o máximo de "
      "oito meses, e a consulta das fichas decorre entre Março e Maio de "
      "2027. A unidade de análise é o episódio de tratamento. O objecto é a "
      "ocorrência de reacções adversas, caracterizada pelo tipo, pela data "
      "de início, pela fase do tratamento, pela gravidade, pela causalidade, "
      "pela conduta adoptada e pela notificação, e os factores do doente e "
      "do tratamento que a ela se associam."),
    P("A entrevista abrange apenas os doentes da amostra que ainda estavam "
      "em tratamento durante o período de recolha e que comparecem ao centro "
      "de saúde, e destina-se a medir o que não ficou registado, não a "
      "refazer a história clínica de todo o ano. Ficam fora do estudo as "
      "crianças e os adolescentes, os doentes em tratamento de tuberculose "
      "resistente, cujo esquema e cujo perfil de toxicidade são diferentes "
      "{schnippel2017,merid2019}, o tratamento preventivo com isoniazida, as "
      "reacções adversas a medicamentos que não sejam antituberculosos, a "
      "determinação de concentrações séricas e a caracterização genética do "
      "metabolismo dos fármacos, que exigiria um laboratório de genética não "
      "disponível."),
]

# ----------------------------------------------------- 3. objectivos --------
OBJECTIVO_GERAL = (
    "Determinar a incidência das reacções adversas aos medicamentos "
    "antituberculosos de primeira linha e os factores a ela associados, em "
    "adultos que iniciaram tratamento nos centros de saúde da cidade de "
    "Nampula entre 1 de Janeiro e 31 de Dezembro de 2026.")
OBJECTIVOS_ESPECIFICOS = [
    "Caracterizar os adultos que iniciaram o tratamento antituberculoso de "
    "primeira linha quanto às variáveis sociodemográficas, clínicas, "
    "nutricionais e terapêuticas;",
    "Determinar a incidência acumulada e a taxa de incidência por "
    "pessoa-mês da hepatotoxicidade, da neuropatia periférica, das reacções "
    "cutâneas e das perturbações gastrointestinais registadas nas fichas de "
    "tratamento;",
    "Classificar as reacções adversas identificadas quanto à gravidade, à "
    "causalidade e à conduta adoptada, e determinar a proporção que foi "
    "notificada ao sector de farmacovigilância;",
    "Estimar a proporção de reacções adversas referidas pelos doentes ainda "
    "em tratamento que não constam da respectiva ficha de tratamento;",
    "Analisar a associação entre a co-infecção pelo vírus da "
    "imunodeficiência humana, a idade, o estado nutricional e outros "
    "factores e o tempo até à primeira reacção adversa.",
]

# ----------------------------------------------------- 4. hipoteses ---------
HIPOTESES_INTRO = [
    P("As hipóteses referem-se ao objectivo específico 5, a única componente "
      "analítica do estudo, e serão testadas com um nível de significância "
      "de 5%. Os objectivos 1 a 4 são descritivos e orientam-se pelas "
      "questões de investigação apresentadas a seguir."),
]
HIPOTESES = [
    ("H0 (co-infecção pelo HIV)",
     "a incidência de reacções adversas aos medicamentos antituberculosos "
     "não difere de forma estatisticamente significativa entre os doentes "
     "com e sem co-infecção pelo HIV."),
    ("H1 (co-infecção pelo HIV)",
     "a incidência de reacções adversas aos medicamentos antituberculosos é "
     "significativamente maior nos doentes com co-infecção pelo HIV do que "
     "nos doentes sem co-infecção."),
    ("H0 (idade, estado nutricional e outros factores)",
     "a idade, o índice de massa corporal no início do tratamento, o sexo, o "
     "consumo de álcool registado e a categoria de tratamento não se "
     "associam de forma estatisticamente significativa ao tempo até à "
     "primeira reacção adversa."),
    ("H1 (idade, estado nutricional e outros factores)",
     "pelo menos um destes factores associa-se de forma estatisticamente "
     "significativa ao tempo até à primeira reacção adversa."),
]
QUESTOES = [
    "Quais são as características sociodemográficas, clínicas, nutricionais "
    "e terapêuticas dos adultos que iniciaram o tratamento antituberculoso "
    "de primeira linha na cidade de Nampula em 2026?",
    "Qual é a incidência acumulada e a taxa de incidência por pessoa-mês de "
    "cada grupo de reacções adversas registadas nas fichas de tratamento, e "
    "em que fase do tratamento surgem?",
    "Como se distribuem as reacções adversas pela gravidade, pela categoria "
    "de causalidade e pela conduta adoptada, e que proporção foi notificada "
    "ao sector de farmacovigilância?",
    "Que proporção das reacções adversas referidas pelos doentes ainda em "
    "tratamento não consta da respectiva ficha, e qual é a concordância "
    "entre as duas fontes?",
]

# ----------------------------------------------------- 5. justificativa -----
JUSTIFICATIVA_INTRO = [
    P("A segurança do tratamento antituberculoso é uma condição da sua "
      "eficácia: um esquema que o doente não tolera é um esquema que o "
      "doente não toma. Medir as reacções adversas num programa que trata "
      "milhares de pessoas por ano é, por isso, uma forma directa de "
      "proteger o resultado do tratamento, e não exige tecnologia nova, mas "
      "apenas método. O estudo justifica-se por quatro razões "
      "complementares."),
]
JUSTIFICATIVA = {
    "cientifica": [
        P("O estudo produz os primeiros dados moçambicanos sobre a "
          "frequência, a gravidade e a causalidade das reacções adversas aos "
          "medicamentos antituberculosos de primeira linha. A literatura "
          "africana disponível concentra-se na hepatotoxicidade e em coortes "
          "prospectivas de um único hospital {wondwossen2016,petros2025}, "
          "enquanto os dados de rotina raramente são analisados com "
          "critérios explícitos. Ao aplicar definições operacionais "
          "ancoradas no protocolo nacional {misau_pnct2019}, ao classificar "
          "a causalidade por dois avaliadores independentes com dois "
          "instrumentos reconhecidos {umc_causalidade,naranjo1981} e ao "
          "confrontar o registo com o relato do doente, o estudo mede "
          "também o sub-registo, que é uma incógnita reconhecida da "
          "farmacovigilância em programas de saúde pública "
          "{tiemersma2019,kampichit2024}."),
    ],
    "academica": [
        P("Para a Licenciatura em Farmácia da Faculdade de Ciências de Saúde "
          "(FCS) da Universidade Lúrio (UniLúrio), o trabalho exercita "
          "competências centrais do farmacêutico: identificação e "
          "classificação de reacções adversas, avaliação da causalidade, "
          "leitura crítica de registos clínicos, análise de sobrevivência e "
          "notificação em farmacovigilância. Deixa ainda dois instrumentos "
          "validados, uma ficha de extracção e um guião de entrevista "
          "traduzido para a língua local, que podem ser reutilizados noutros "
          "programas de tratamento prolongado, como o tratamento "
          "anti-retroviral, e numa segunda medição depois de uma "
          "intervenção."),
    ],
    "social": [
        P("Os doentes com tuberculose da cidade de Nampula tomam medicamentos "
          "durante meses, muitas vezes ao mesmo tempo que o tratamento "
          "anti-retroviral, e suportam sozinhos sintomas que podem ser "
          "aliviados com medidas simples previstas no protocolo nacional, "
          "como a metoclopramida antes da toma, o aumento da piridoxina "
          "para 100 mg por dia na neuropatia periférica, ou 200 mg por dia "
          "nos doentes com HIV, e os anti-histamínicos no prurido "
          "{misau_pnct2019}. Reconhecer a reacção cedo evita o sofrimento "
          "desnecessário, evita as perdas de doses que prolongam o "
          "tratamento {dixon2025} e evita a progressão para formas graves. "
          "Num contexto em que a doença já é motivo de estigma, poupar ao "
          "doente sintomas visíveis, como a icterícia ou a erupção cutânea, "
          "tem também um valor social."),
    ],
    "politica": [
        P("O protocolo nacional determina que todas as reacções adversas "
          "sejam notificadas ao sector de farmacovigilância do Departamento "
          "Farmacêutico, através de uma ficha própria {misau_pnct2019}, e a "
          "Organização Mundial da Saúde (OMS) recomenda que a "
          "monitorização activa da segurança faça parte da prestação de "
          "cuidados aos doentes com tuberculose {who_adsm2015}. A avaliação "
          "de base dos sistemas de farmacovigilância de quatro países da "
          "África subsariana mostrou que a repartição de tarefas entre o "
          "programa de tuberculose e a autoridade reguladora não é clara e "
          "que a avaliação da causalidade fica frequentemente por fazer "
          "{tiemersma2021}. Ao medir a proporção notificada e ao devolver "
          "os resultados ao PNCT provincial, ao SDSMAS e à Autoridade "
          "Nacional Reguladora de Medicamentos (ANARME), o estudo oferece "
          "uma base para fixar metas de notificação e para decidir onde "
          "reforçar a formação."),
    ],
}

# ----------------------------------------------------- 6. revisao -----------
REVISAO = [
    ("Tuberculose e tratamento de primeira linha: esquema, doses e "
     "enquadramento normativo moçambicano", [
        P("A tuberculose é uma doença infecciosa causada pelo *Mycobacterium "
          "tuberculosis*, de transmissão aérea e evolução prolongada, que em "
          "2024 fez adoecer 10,7 milhões de pessoas e matou 1,23 milhões "
          "{who_gtb2025}. A carga concentra-se em poucos países e mantém uma "
          "relação estreita com a infecção pelo HIV, que multiplica o risco "
          "de progressão da infecção latente para doença activa; em 2024, "
          "cerca de 619.000 pessoas com HIV desenvolveram tuberculose e "
          "150.000 morreram com as duas doenças {who_gtb2025}. As "
          "estimativas do estudo da carga global de doença confirmam que a "
          "tuberculose continua a ser, entre as doenças infecciosas, uma das "
          "principais causas de anos de vida perdidos, com a África "
          "subsariana a suportar uma parte desproporcionada do peso "
          "{gbd2026}."),
        P("O tratamento da tuberculose sensível aos medicamentos assenta, na "
          "recomendação da OMS, num esquema de seis meses com quatro "
          "fármacos na fase intensiva, rifampicina, isoniazida, pirazinamida "
          "e etambutol, seguidos de dois fármacos na fase de manutenção "
          "{who_mod4_2025}. Em Moçambique, o PNCT adopta este esquema em "
          "doses fixas combinadas, com dois meses de rifampicina, "
          "isoniazida, pirazinamida e etambutol e quatro meses de "
          "rifampicina e isoniazida, e fixa as doses diárias por quilograma "
          "de peso: 15 mg de rifampicina, com o máximo de 600 mg; 10 mg de "
          "isoniazida, com o máximo de 300 mg; 35 mg de pirazinamida, com o "
          "máximo de 2.000 mg; e 20 mg de etambutol, com o máximo de 1.200 "
          "mg {misau_pnct2019}. A todos os adultos é recomendada piridoxina "
          "numa dose fixa de 50 mg por dia para prevenir a neuropatia "
          "periférica pela isoniazida, e 5 a 10 mg por dia nas crianças "
          "{misau_pnct2019}."),
        P("Os protocolos nacionais acrescentam a este esquema um conjunto de "
          "instruções sobre a monitorização do doente. Em cada consulta "
          "mensal, o profissional deve perguntar pela presença de sintomas "
          "de toxicidade, em particular formigueiro ou dor nos membros "
          "inferiores, que sugerem neuropatia periférica, e cansaço, "
          "náuseas, vómitos e dor abdominal, que sugerem hepatite "
          "{misau_pnct2019}. A vigilância laboratorial é selectiva: os "
          "doentes com doença hepática de base fazem alanina "
          "aminotransferase (ALT) e bilirrubina total de dois em dois meses, "
          "enquanto os restantes são monitorizados apenas clinicamente "
          "{misau_pnct2019}. Esta opção, comum nos programas de países de "
          "rendimento baixo, tem uma consequência metodológica directa: "
          "numa coorte construída a partir das fichas, a hepatotoxicidade "
          "que se pode medir é sobretudo a que foi reconhecida pela clínica "
          "e não a que seria detectada por rastreio bioquímico sistemático "
          "{lewis2024}."),
    ]),
    ("Reacção adversa a medicamentos: definição, gravidade e seriedade", [
        P("Entende-se por reacção adversa a medicamentos (RAM) uma resposta "
          "nociva e não intencional a um medicamento administrado em doses "
          "habituais para profilaxia, diagnóstico ou tratamento, definição "
          "que distingue a reacção adversa do acontecimento adverso, "
          "conceito mais amplo que abrange qualquer ocorrência desfavorável "
          "durante o tratamento, independentemente da relação com o "
          "medicamento {edwards2000}. A distinção é operacionalmente "
          "importante num estudo documental: as fichas registam "
          "acontecimentos, e é a avaliação da causalidade que transforma "
          "alguns deles em reacções adversas. No quadro de referência da "
          "monitorização activa da segurança dos medicamentos "
          "antituberculosos, a OMS mantém esta separação e reserva a "
          "designação de acontecimento adverso grave para as situações que "
          "levam à morte, põem a vida em risco, exigem ou prolongam a "
          "hospitalização, causam incapacidade persistente ou anomalia "
          "congénita, ou constituem um acontecimento médico importante "
          "{who_adsm2015}."),
        P("A gravidade, que mede a intensidade da manifestação, não se "
          "confunde com a seriedade, que mede a consequência. A escala mais "
          "usada para graduar a intensidade é a dos critérios "
          "terminológicos comuns para acontecimentos adversos (CTCAE), que "
          "classifica cada manifestação em cinco graus: ligeira e "
          "assintomática ou com sintomas ligeiros que não exigem "
          "intervenção; moderada, que limita as actividades instrumentais do "
          "dia a dia; grave ou clinicamente significativa, que não põe "
          "imediatamente a vida em risco mas limita o autocuidado; com risco "
          "de vida, que exige intervenção urgente; e morte relacionada com o "
          "acontecimento {ctcae2017}. Os protocolos moçambicanos usam uma "
          "versão condensada da mesma lógica, ao distinguir efeitos de grau "
          "1, ligeiros, de grau 2, moderados, e de graus 3 e 4, graves, e "
          "ao determinar que a graduação preceda a decisão de conduta "
          "{misau_pnct2019}."),
        P("A ficha nacional de notificação de reacções adversas aos "
          "medicamentos e vacinas, anexa aos protocolos do PNCT, recolhe "
          "exactamente estes elementos: a descrição da reacção, a data de "
          "início, os medicamentos suspeitos por ordem de suspeita, o "
          "desfecho da reacção, a conduta adoptada e os critérios de "
          "seriedade, entre os quais o risco de vida, a hospitalização, o "
          "prolongamento da hospitalização, o acontecimento médico "
          "importante, a malformação congénita e a morte {misau_pnct2019}. "
          "Ao adoptar como definições operacionais as que constam deste "
          "documento e da escala dos critérios terminológicos, o estudo "
          "garante que os seus resultados são directamente comparáveis com "
          "os dados que o próprio sistema nacional recolhe."),
    ]),
    ("Perfil de toxicidade dos medicamentos antituberculosos de primeira "
     "linha", [
        P("A hepatotoxicidade é a reacção adversa mais temida, porque pode "
          "evoluir para insuficiência hepática aguda e morte. É atribuída "
          "sobretudo à isoniazida, à rifampicina e à pirazinamida "
          "{prasad2019,he2026}. A incidência varia muito com a definição e "
          "com o rastreio: uma meta-análise de 43 estudos indianos, com "
          "12.041 doentes, estimou uma incidência agregada de 12,6% (IC95% "
          "9,9-15,3%), com maior frequência nos esquemas diários do que nos "
          "esquemas de três tomas por semana, 16,5% contra 3,5%, e estimou "
          "ainda que 6,78% dos doentes com lesão hepática evoluíram para "
          "insuficiência hepática aguda, cuja letalidade foi de 71,8% "
          "{kumarmeta2025}. Nos casos que progridem, a sobrevivência depende "
          "da suspensão precoce dos fármacos e do apoio em unidade "
          "diferenciada {kumarfalencia2025}. Os protocolos moçambicanos "
          "definem hepatite aguda induzida por medicamentos pela presença de "
          "ALT superior a 120 unidades por litro num doente sintomático, ALT "
          "superior a 200 unidades por litro num doente assintomático ou "
          "bilirrubina total igual ou superior a 40 micromoles por litro, e "
          "mandam parar o tratamento, internar e reintroduzir os fármacos de "
          "forma faseada quando a ALT descer abaixo de 100 unidades por "
          "litro {misau_pnct2019}."),
        P("A neuropatia periférica manifesta-se por formigueiro, "
          "dormência ou dor nos pés e nas mãos e resulta da interferência da "
          "isoniazida com o metabolismo da piridoxina; por isso a "
          "prevenção passa pela suplementação sistemática e a conduta, "
          "quando a neuropatia surge, consiste em aumentar a piridoxina para "
          "100 mg por dia, ou 200 mg por dia nos doentes com HIV, e "
          "acrescentar analgesia {misau_pnct2019,prasad2019}. Ao contrário "
          "das reacções gastrointestinais e cutâneas, que aparecem cedo, a "
          "neuropatia tende a surgir mais tarde: na base nacional de "
          "notificações da Coreia do Sul, a maioria das reacções foi "
          "comunicada no primeiro mês, mas a neuropatia, as parestesias e as "
          "alterações hematológicas, renais e hepáticas foram "
          "frequentemente notificadas depois do segundo mês {chung2022}. "
          "Esta diferença de calendário justifica que a incidência seja "
          "medida com base no tempo de observação e não apenas como "
          "proporção."),
        P("As reacções cutâneas vão do prurido isolado à dermatite "
          "esfoliativa e às reacções de hipersensibilidade graves. Os "
          "protocolos nacionais recordam que a erupção cutânea aparece "
          "habitualmente três a quatro semanas depois do início do "
          "tratamento, que nem todos os problemas cutâneos se devem aos "
          "medicamentos antituberculosos, uma vez que a nevirapina, o "
          "efavirenz e o cotrimoxazol também os causam, e graduam a resposta "
          "em três níveis, desde o anti-histamínico no prurido sem lesão até "
          "à suspensão do tratamento e ao esquema alternativo na erupção "
          "eritematosa com febre ou na dermatite esfoliativa com "
          "envolvimento das mucosas {misau_pnct2019}. Nos doentes com "
          "co-infecção, a distinção entre a reacção aos antituberculosos e a "
          "reacção aos anti-retrovirais é particularmente difícil: numa "
          "coorte de 307 adultos com tuberculose e HIV, as reacções "
          "cutâneas ocorreram em 48 doentes, com uma taxa de 0,41 "
          "acontecimentos por pessoa-ano, e o uso concomitante de "
          "cotrimoxazol associou-se ao seu aparecimento {boonyagars2017}."),
        P("As perturbações gastrointestinais, náuseas, vómitos, dor "
          "abdominal e anorexia, são as queixas mais frequentes em quase "
          "todos os estudos que interrogam o doente. Em Marrocos, "
          "representaram 7,4% dos 10,0% de doentes com reacções registadas "
          "{elhamdouni2020}; na base coreana de notificações, as "
          "perturbações gastrointestinais foram o grupo mais comunicado, com "
          "32,0%, seguidas das cutâneas, com 25,9%, e das hepatobiliares, "
          "com 14,2% {chung2022}; no Gana, 80% dos doentes que referiram "
          "reacções adversas apontaram sintomas gastrointestinais "
          "{amalba2021}. Embora raramente graves, estas queixas pesam na "
          "adesão, porque acompanham cada toma, e o protocolo nacional "
          "prevê metoclopramida antes da toma, antiácidos e a exclusão de "
          "hepatite quando os vómitos persistem {misau_pnct2019}. Completam "
          "o quadro as artralgias pela pirazinamida, a neurite óptica pelo "
          "etambutol, que obriga a suspensão definitiva do fármaco, e a "
          "púrpura pela rifampicina {misau_pnct2019,he2026}."),
    ]),
    ("Determinantes das reacções adversas: co-infecção pelo vírus da "
     "imunodeficiência humana, idade e estado nutricional", [
        P("A co-infecção pelo HIV é o determinante mais estudado e o mais "
          "discutido. Numa coorte prospectiva de 219 doentes seguidos em "
          "centros de saúde da Etiópia central, o estado serológico "
          "positivo multiplicou por 6,73 as probabilidades de lesão hepática "
          "induzida pelos antituberculosos, num modelo que ajustou também "
          "para o sexo, a idade e o IMC {petros2025}; numa coorte "
          "sul-africana, o estado serológico manteve-se associado à lesão "
          "hepática na análise multivariável {nyangwara2025}; e, num centro "
          "de referência brasileiro, os doentes com HIV tiveram com mais "
          "frequência reacções de grau 3 ou 4, 18,36%, e a contagem de CD4 "
          "abaixo de 100 células por microlitro associou-se à "
          "hepatotoxicidade {sant2023}. Nem todos os estudos encontram o "
          "mesmo: numa coorte de 222 adultos da Tailândia e das Filipinas, a "
          "hepatotoxicidade ocorreu em 13,8% dos doentes com HIV e em 9,5% "
          "dos doentes sem HIV, diferença que não atingiu significado "
          "estatístico (p=0,35) {atuel2026}, e num inquérito mensal a 286 "
          "doentes sul-africanos o estado serológico não se associou à "
          "ocorrência de reacções, embora, entre os doentes com reacções "
          "moderadas ou graves, a infecção com CD4 abaixo de 200 células por "
          "microlitro se associasse a mais doses perdidas, com uma razão de "
          "taxas de 1,71 {tzelios2025}."),
        P("A divergência tem explicações plausíveis. O efeito do HIV "
          "confunde-se com o do tratamento anti-retroviral concomitante, "
          "com o do cotrimoxazol e com o das co-infecções víricas do fígado, "
          "e depende do grau de imunossupressão, de tal modo que estudos com "
          "doentes já estabilizados em TARV encontram menos toxicidade do "
          "que estudos com doentes que iniciam os dois tratamentos ao mesmo "
          "tempo {boonyagars2017,sant2023}. Numa amostra em que a maioria "
          "dos doentes co-infectados já está em TARV, como acontece em "
          "Moçambique, onde 95% dos doentes co-infectados notificados "
          "estavam em tratamento anti-retroviral {misau_pnct2021}, a "
          "associação esperada é mais modesta do que a descrita na Etiópia. "
          "Esta é uma razão adicional para medir o fenómeno localmente em "
          "vez de o importar da literatura."),
        P("A idade avançada surge de forma consistente como factor de "
          "risco. Na coorte prospectiva coreana, a idade associou-se de "
          "forma independente à ocorrência de reacções, e os doentes mais "
          "velhos tiveram mais anorexia, dispepsia, exantema, tonturas, "
          "anemia e alterações das provas hepáticas e renais {choi2022}; na "
          "base nacional de notificações do mesmo país, 48,5% dos casos "
          "respeitavam a doentes com 60 ou mais anos {chung2022}; e num "
          "estudo dedicado aos idosos, as reacções adversas foram "
          "frequentes e condicionaram o resultado do tratamento {zhu2025}. "
          "Numa coorte retrospectiva etíope com 570 doentes seguidos "
          "durante 5.045,09 pessoas-mês, a idade entre 25 e 49 anos e a "
          "idade igual ou superior a 50 anos multiplicaram o risco "
          "instantâneo de acontecimentos adversos major por 3,36 e por 5,60, "
          "respectivamente, a par das comorbilidades e da anemia "
          "{merid2019}."),
        P("O estado nutricional é o terceiro determinante e o mais "
          "relevante num contexto de pobreza. A meta-análise indiana "
          "identificou o IMC baixo como factor de risco de lesão hepática, "
          "com uma razão de possibilidades de 3,8, a par da "
          "hipoalbuminemia, com 3,09 {kumarmeta2025}; na coorte etíope, "
          "cada unidade adicional de IMC reduziu as probabilidades de lesão "
          "hepática, com uma razão de possibilidades ajustada de 0,81 "
          "{petros2025}; e na coorte da Tailândia e das Filipinas, em que a "
          "mediana do IMC foi de 18,2 quilogramas por metro quadrado, cada "
          "unidade adicional reduziu as probabilidades em 0,78 {atuel2026}. "
          "Num estudo indiano dedicado ao tema, a desnutrição destacou-se "
          "como factor de risco importante de lesão hepática nos doentes em "
          "tratamento antituberculoso {ali2020}. A explicação proposta "
          "combina a depleção de glutatião, a redução da albumina e a "
          "alteração da distribuição dos fármacos, todas mais prováveis no "
          "doente desnutrido {lewis2024}."),
    ]),
    ("Avaliação da causalidade e concordância entre avaliadores", [
        P("Nenhuma reacção adversa se confirma por um exame único, pelo que "
          "a atribuição da responsabilidade a um medicamento assenta num "
          "juízo estruturado. O sistema desenvolvido pela OMS com o Centro "
          "de Monitorização de Uppsala (WHO-UMC) classifica cada caso em "
          "seis categorias, certa, provável, possível, improvável, "
          "condicional ou não classificada e não avaliável, a partir da "
          "relação temporal com a toma, da possibilidade de explicação por "
          "outra doença ou outro medicamento, da resposta à suspensão e, "
          "nas categorias mais fortes, da resposta à reintrodução "
          "{umc_causalidade}. O próprio documento reconhece que nenhum "
          "sistema produz uma estimativa quantitativa fiável da "
          "probabilidade da relação, e que o que a avaliação da causalidade "
          "consegue é reduzir o desacordo entre avaliadores, classificar a "
          "verosimilhança e melhorar a avaliação científica, e não provar a "
          "ligação entre o fármaco e o acontecimento {umc_causalidade}."),
        P("O algoritmo de Naranjo aborda o mesmo problema por pontuação: "
          "dez perguntas sobre relatos anteriores, sequência temporal, "
          "resposta à suspensão e à reintrodução, causas alternativas, "
          "resposta ao placebo, concentrações do fármaco, relação com a "
          "dose, história de reacção semelhante e confirmação objectiva "
          "geram um total que classifica a reacção em definida, provável, "
          "possível ou duvidosa {naranjo1981}. Os dois instrumentos são os "
          "mais usados na prática e têm sido comparados em séries "
          "hospitalares, que descrevem concordância apenas parcial entre "
          "eles e recomendam declarar qual foi utilizado "
          "{pandit2024,more2024}. Por serem complementares, o presente "
          "estudo aplica os dois e apresenta os resultados em paralelo."),
        P("Como a classificação depende de julgamento, a fiabilidade tem de "
          "ser medida. O procedimento habitual consiste em fazer avaliar os "
          "mesmos casos por dois avaliadores independentes e calcular o "
          "kappa de Cohen, que corrige a concordância observada pela "
          "concordância esperada ao acaso; a interpretação original, que "
          "admite valores tão baixos como 0,41 como aceitáveis, é "
          "considerada demasiado permissiva para a investigação em saúde, "
          "onde se exigem valores mais altos {mchugh2012}. Nos estudos de "
          "farmacovigilância baseados em bases de notificação, é frequente "
          "restringir a análise aos casos classificados como possíveis, "
          "prováveis ou certos pelo sistema WHO-UMC, como fez a análise da "
          "base nacional coreana {chung2022}, critério que este estudo "
          "também adopta para a estimativa principal."),
    ]),
    ("Farmacovigilância em programas de saúde pública, sub-registo e "
     "métodos de medição", [
        P("A notificação espontânea é a base da farmacovigilância, mas "
          "subestima de forma sistemática a frequência das reacções "
          "adversas, sobretudo quando depende de profissionais sobrecarregados "
          "e sem retorno de informação. No Gana, apenas 39,2% dos doentes "
          "que tiveram reacções adversas as comunicaram a um profissional de "
          "saúde, enquanto 60,8% não o fizeram {amalba2021}. A avaliação de "
          "base dos sistemas de farmacovigilância de quatro países da África "
          "subsariana mostrou que a maioria dispõe de leis e directrizes, "
          "mas que a divisão de responsabilidades entre o programa de "
          "tuberculose e a autoridade reguladora nem sempre é clara, o que "
          "gera duplicação e tarefas por cumprir, entre elas a avaliação da "
          "causalidade {tiemersma2021}. A experiência de vários países "
          "mostra que a integração da monitorização da segurança nos "
          "programas de tratamento é exequível quando se define quem "
          "recolhe, quem avalia e quem devolve a informação "
          "{tiemersma2019,who_adsm2015}."),
        P("Existem três formas de medir as reacções adversas num programa. "
          "A análise das notificações espontâneas descreve o perfil dos "
          "casos comunicados, mas não fornece denominador nem incidência "
          "{chung2022}. A coorte prospectiva com inquérito periódico ao "
          "doente é o método mais sensível, e é por isso que os seus valores "
          "são os mais altos, entre metade e quatro quintos dos doentes "
          "{choi2022,sant2023,tzelios2025}. A coorte retrospectiva "
          "construída a partir dos registos de rotina é a mais exequível e "
          "permite abranger todo um ano de tratamento, mas depende da "
          "qualidade do registo e produz estimativas muito inferiores, como "
          "os 10,0% observados em Marrocos {elhamdouni2020}. O presente "
          "estudo combina a terceira abordagem com uma entrevista aos "
          "doentes ainda em tratamento, precisamente para estimar a "
          "distância entre as duas."),
        P("O relato do doente tem, por sua vez, limitações conhecidas. Um "
          "estudo de métodos mistos mostrou que a exactidão com que os "
          "doentes identificam e atribuem sintomas aos medicamentos é "
          "variável e depende da informação que receberam "
          "{kampichit2024}, o que obriga a usar um guião com sintomas "
          "definidos, a registar as datas e a submeter cada relato à mesma "
          "avaliação de causalidade aplicada aos registos. A escolha da "
          "medida de frequência é igualmente decisiva: como o tempo em "
          "tratamento difere entre doentes que curam, morrem, abandonam ou "
          "são transferidos, e como as diferentes reacções surgem em "
          "momentos distintos, a incidência deve ser apresentada em "
          "proporção acumulada e em taxa por pessoa-tempo, como fez a coorte "
          "etíope que descreveu 5,79 acontecimentos adversos major por 100 "
          "pessoas-mês e mostrou que a taxa era maior nos primeiros meses "
          "{merid2019}. O relato de estudos com dados de rotina segue a "
          "declaração STROBE {vonelm2007} e a sua extensão RECORD "
          "{benchimol2015}."),
    ]),
]

# ----------------------------------------------------- 7. estado da arte ----
ESTADO_ARTE = [
    P("O [[quadro:estado_arte]] reúne 15 estudos empíricos dos últimos dez "
      "anos sobre reacções adversas aos medicamentos antituberculosos, com "
      "prioridade para os estudos africanos e para os que distinguem "
      "doentes com e sem co-infecção pelo HIV, e inclui os desenhos que "
      "este protocolo combina, a coorte a partir de registos de rotina e o "
      "inquérito ao doente."),
    QUADRO("estado_arte",
           "Síntese de estudos sobre reacções adversas aos medicamentos "
           "antituberculosos (estado da arte)",
           ["Autor (ano)", "Local", "Desenho (n)", "Principais resultados"],
           [
               ["Wondwossen Abera et al. (2016) {wondwossen2016}",
                "Etiópia, Dawro", "Coorte prospectiva (124)",
                "Hepatotoxicidade em 8%; início entre 13 e 58 dias (mediana "
                "26); consumo elevado de álcool associado (razão de "
                "possibilidades 9,3)."],
               ["Boonyagars et al. (2017) {boonyagars2017}",
                "Tailândia, Banguecoque",
                "Coorte retrospectiva (307 com co-infecção)",
                "Reacções cutâneas em 48 doentes, 0,41 acontecimentos por "
                "pessoa-ano; exantema maculopapular o mais frequente; "
                "contagem baixa de CD4 não associada."],
               ["Schnippel et al. (2017) {schnippel2017}",
                "Contextos de alta prevalência de HIV",
                "Revisão sistemática e meta-análise",
                "Sintetiza as reacções adversas ao tratamento da tuberculose "
                "resistente em populações com elevada co-infecção e a "
                "necessidade de vigilância estruturada."],
               ["Merid et al. (2019) {merid2019}", "Etiópia, Amhara",
                "Coorte retrospectiva (570; 5.045,09 pessoas-mês)",
                "Taxa de 5,79 acontecimentos adversos major por 100 "
                "pessoas-mês; idade de 25 a 49 anos e de 50 ou mais, "
                "comorbilidades e anemia como preditores."],
               ["El Hamdouni et al. (2020) {elhamdouni2020}",
                "Marrocos, 18 centros", "Coorte observacional (2.532)",
                "Reacções registadas em 10,0%: 7,4% gastrointestinais, 3,7% "
                "cutâneas, 2,0% hepáticas; sucesso do tratamento de 79,1%."],
               ["Amalba e Bugri (2021) {amalba2021}", "Gana, Tamale",
                "Transversal por entrevista (66)",
                "77% referiram reacções; 80% sintomas gastrointestinais; "
                "84,6% dos afectados falharam tomas; 60,8% não comunicaram "
                "a um profissional."],
               ["Chung et al. (2022) {chung2022}",
                "Coreia do Sul, base nacional de notificações",
                "Análise de 17.843 notificações",
                "Perturbações gastrointestinais 32,0%, cutâneas 25,9%, "
                "hepatobiliares 14,2%; 48,5% em doentes com 60 ou mais anos; "
                "maioria no primeiro mês."],
               ["Choi et al. (2022) {choi2022}",
                "Coreia do Sul, cinco hospitais", "Coorte prospectiva (410)",
                "67,8% com reacção de grau 2 ou superior; mudança de esquema "
                "em 9,5%; idade e sexo masculino associados; pior qualidade "
                "de vida nos afectados."],
               ["Sant'Anna et al. (2023) {sant2023}",
                "Brasil, Rio de Janeiro", "Coorte prospectiva (550)",
                "Reacções em 78,6%; doentes com HIV com mais reacções de "
                "grau 3 ou 4 (18,36%); contagem de CD4 abaixo de 100 "
                "associada a hepatotoxicidade."],
               ["Kumar et al. (2025) {kumarmeta2025}",
                "Índia, revisão sistemática",
                "Meta-análise (43 estudos; 12.041 doentes)",
                "Lesão hepática em 12,6% (IC95% 9,9-15,3%); índice de massa "
                "corporal baixo (3,8) e hipoalbuminemia (3,09) como factores "
                "de risco; 6,78% evoluíram para insuficiência hepática "
                "aguda."],
               ["Petros et al. (2025) {petros2025}",
                "Etiópia central, três centros de saúde",
                "Coorte prospectiva (219)",
                "Lesão hepática em 16,0%, grave em 5,7%; associada ao sexo "
                "(2,57), à idade (1,05), ao índice de massa corporal (0,81) "
                "e à infecção pelo HIV (6,73)."],
               ["Nyangwara et al. (2025) {nyangwara2025}", "África do Sul",
                "Coorte ambispectiva (610)",
                "Incidência de lesão hepática de 2,1%; mediana de 30 dias "
                "até ao início; sexo feminino, estado serológico e álcool "
                "associados."],
               ["Tzelios et al. (2025) {tzelios2025}",
                "África do Sul, Worcester",
                "Coorte prospectiva com inquérito mensal (286)",
                "Cerca de metade com reacções; ter pelo menos uma "
                "comorbilidade aumentou o risco em 46%; entre reacções "
                "moderadas ou graves, CD4 abaixo de 200 associado a mais "
                "doses perdidas (1,71)."],
               ["Dixon et al. (2025) {dixon2025}", "Letónia, Riga",
                "Coorte retrospectiva (174)",
                "31,0% perderam doses por reacções adversas; as perturbações "
                "hepatobiliares foram o principal grupo, com mediana de 15,0 "
                "dias de doses perdidas."],
               ["Atuel et al. (2026) {atuel2026}", "Tailândia e Filipinas",
                "Coorte (222: 138 com HIV, 84 sem HIV)",
                "Hepatotoxicidade em 13,8% dos doentes com HIV e 9,5% dos "
                "doentes sem HIV (p=0,35); índice de massa corporal baixo "
                "associado (0,78 por unidade)."],
           ],
           larguras=[3.3, 2.6, 3.4, 6.7],
           fonte="Elaboração própria (2026), a partir das fontes citadas."),
    P("A leitura do quadro mostra, antes de mais, que o método determina a "
      "magnitude. Onde se perguntou ao doente, a proporção com reacções "
      "adversas situou-se entre metade e quatro quintos; onde se leram "
      "registos clínicos, ficou em torno de um décimo; e onde se contaram "
      "notificações espontâneas, não há sequer denominador. Segue-se que "
      "comparar países ou serviços sem atender ao método é enganador, e que "
      "qualquer estimativa baseada em registos deve ser acompanhada de uma "
      "medida do que escapa ao registo. Em segundo lugar, os determinantes "
      "não se comportam todos da mesma maneira: a idade avançada e o "
      "estado nutricional deficiente aparecem associados à toxicidade de "
      "forma consistente em contextos muito diferentes, enquanto o efeito "
      "da co-infecção pelo HIV é forte nuns estudos e nulo noutros, "
      "provavelmente porque se confunde com o grau de imunossupressão, com "
      "o tratamento anti-retroviral concomitante e com as hepatites "
      "víricas. Em terceiro lugar, o calendário das reacções é "
      "reconhecível: as queixas gastrointestinais e cutâneas concentram-se "
      "nas primeiras semanas e a neuropatia periférica surge mais tarde, o "
      "que recomenda medidas de incidência que incorporem o tempo de "
      "observação."),
    P("A lacuna é dupla. Nenhum dos estudos africanos identificados "
      "confronta, nos mesmos doentes, o que está escrito na ficha de "
      "tratamento com o que o doente relata, de modo a quantificar o "
      "sub-registo; e nenhum estudo publicado descreve a situação em "
      "Moçambique, onde a investigação sobre tuberculose se concentrou nos "
      "desfechos do tratamento no sul do país "
      "{garciabasteiro2016,nacarapa2020,osorio2022,ndhlovu2026} e onde a "
      "única avaliação publicada do uso de medicamentos em Nampula incidiu "
      "sobre antibióticos em crianças internadas {xavier2022}. O presente "
      "estudo preenche as duas lacunas com um desenho exequível num "
      "trabalho de licenciatura."),
]
ESQUEMA_TEXTO = [
    P("A [[figura:esquema]] representa as relações que o estudo examina. As "
      "características do doente, o seu estado clínico e nutricional e as "
      "características do tratamento e do serviço influenciam a ocorrência "
      "das reacções adversas aos medicamentos antituberculosos, que "
      "constituem o desfecho, caracterizado pelo tipo, pela gravidade, pela "
      "categoria de causalidade e pela conduta adoptada. O mês de início do "
      "tratamento, o centro de saúde e a qualidade do preenchimento da "
      "ficha são tratados como variáveis de confundimento, porque afectam "
      "simultaneamente a probabilidade de uma reacção ser detectada e a "
      "probabilidade de ficar registada."),
]
ESQUEMA_TITULO = ("Esquema conceptual dos factores associados às reacções "
                  "adversas aos medicamentos antituberculosos")
ESQUEMA = {
    "contexto": ("Adultos em tratamento antituberculoso de primeira linha "
                 "nos centros de saúde da cidade de Nampula, 1 de Janeiro a "
                 "31 de Dezembro de 2026"),
    "blocos": [
        ("Características do doente",
         ["idade e sexo", "escolaridade e ocupação",
          "consumo de álcool registado", "distância e transporte"]),
        ("Estado clínico e nutricional",
         ["co-infecção pelo HIV e contagem de CD4",
          "índice de massa corporal no início",
          "comorbilidades e gravidez",
          "forma e extensão da tuberculose"]),
        ("Tratamento e medicamentos concomitantes",
         ["dose por escalão de peso", "fase do tratamento",
          "piridoxina", "tratamento anti-retroviral e cotrimoxazol"]),
    ],
    "desfecho": ("Reacções adversas aos medicamentos antituberculosos",
                 ["hepatotoxicidade", "neuropatia periférica",
                  "reacções cutâneas", "perturbações gastrointestinais",
                  "gravidade, causalidade e conduta"]),
    "moderadores": ("Variáveis de confundimento",
                    ["mês de início do tratamento", "centro de saúde",
                     "qualidade do registo na ficha"]),
}
