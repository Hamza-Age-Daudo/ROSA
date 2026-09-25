# -*- coding: utf-8 -*-
"""
Tema 26 (Controlo de Qualidade e Análise de Medicamentos).
Qualidade farmacopeica e intercambialidade in vitro de marcas de comprimidos
de paracetamol 500 mg vendidas em farmácias comunitárias da cidade de Nampula.

Compor e validar:   python _motor/motor.py _conteudo/tema_26.py
Verificar fontes:   python _motor/refs.py verificar _conteudo/tema_26.py
"""
from blocos import (CAMPO, FORMULA, H3, LISTA, NOTA, P, PERG, QUADRO,
                    TABELA)

NUMERO = 26
SLUG = "Qualidade_Marcas_Paracetamol_Nampula"
TITULO = ("Avaliação da qualidade e da intercambialidade de marcas de "
          "comprimidos de paracetamol de 500 mg comercializadas em farmácias "
          "comunitárias da cidade de Nampula, 2027")
DESENHO = ("Estudo laboratorial transversal, analítico e comparativo "
           "(ensaios farmacopeicos e perfis de dissolução)")

AUTOR = "[Nome do(a) estudante]"
ORIENTADOR = "[Nome e grau académico do(a) orientador(a)]"

# ---------------------------------------------------------------- resumo --
RESUMO = (
    "Os medicamentos de qualidade inferior comprometem a eficácia e a "
    "segurança dos tratamentos e afectam sobretudo os países de baixo e médio "
    "rendimento. O paracetamol é um dos medicamentos mais usados no mundo, é "
    "dispensado sem receita e circula em Moçambique sob várias marcas e a "
    "preços diferentes, mas não existem dados sobre a conformidade "
    "farmacopeica nem sobre a intercambialidade destes produtos na cidade de "
    "Nampula. O estudo tem como objectivo avaliar a qualidade farmacêutica e "
    "a intercambialidade *in vitro* das marcas de comprimidos de paracetamol "
    "de 500 miligramas comercializadas nas farmácias comunitárias da cidade "
    "de Nampula. Trata-se de um estudo laboratorial transversal, analítico e "
    "comparativo, com recolha e ensaios entre Fevereiro e Junho de 2027. Um "
    "levantamento nas farmácias comunitárias licenciadas identificará as "
    "marcas disponíveis e serão adquiridos até dois lotes de cada marca, com "
    "cento e cinquenta comprimidos por lote, prevendo-se, no cenário central, "
    "dez marcas genéricas e o produto de referência. Cada lote será submetido "
    "aos ensaios da Farmacopeia Internacional: inspecção visual, uniformidade "
    "de massa, resistência ao esmagamento, friabilidade, desagregação, "
    "identificação, pureza, doseamento por espectrofotometria de ultravioleta "
    "e dissolução. Os perfis de dissolução de cada marca serão comparados com "
    "os do produto de referência em três meios de pH fisiológico, através do "
    "factor de semelhança. A análise incluirá a proporção de lotes conformes "
    "com intervalos de confiança a noventa e cinco por cento, a análise de "
    "variância ou o teste de Kruskal-Wallis entre marcas e o teste exacto de "
    "Fisher para a associação entre o preço e a conformidade, com nível de "
    "significância de cinco por cento. Espera-se produzir a primeira "
    "evidência local sobre a qualidade e a intercambialidade do paracetamol, "
    "útil à autoridade reguladora, aos farmacêuticos e aos utentes.")
PALAVRAS_CHAVE = ["controlo de qualidade", "intercambialidade",
                  "medicamentos genéricos", "Moçambique", "paracetamol"]
ABSTRACT = (
    "Substandard medicines compromise the efficacy and safety of treatment "
    "and mainly affect low- and middle-income countries. Paracetamol is one "
    "of the most widely used medicines in the world, is dispensed without a "
    "prescription and is sold in Mozambique under several brands and at "
    "different prices, but there are no data on the pharmacopoeial "
    "compliance or on the interchangeability of these products in Nampula "
    "City. This study aims to assess the pharmaceutical quality and the "
    "*in vitro* interchangeability of the brands of paracetamol 500 "
    "milligram tablets marketed in community pharmacies of Nampula City. It "
    "is a cross-sectional, analytical and comparative laboratory study, with "
    "sampling and testing between February and June 2027. A survey of "
    "licensed community pharmacies will identify the available brands, and "
    "up to two batches of each brand will be purchased, with one hundred and "
    "fifty tablets per batch; the central scenario foresees ten generic "
    "brands and the reference product. Each batch will undergo the tests of "
    "The International Pharmacopoeia: visual inspection, uniformity of mass, "
    "resistance to crushing, friability, disintegration, identification, "
    "purity, assay by ultraviolet spectrophotometry and dissolution. The "
    "dissolution profiles of each brand will be compared with those of the "
    "reference product in three media of physiological pH, using the "
    "similarity factor. The analysis will include the proportion of "
    "compliant batches with ninety-five per cent confidence intervals, "
    "analysis of variance or the Kruskal-Wallis test across brands and "
    "Fisher's exact test for the association between price and compliance, "
    "with a significance level of five per cent. The study is expected to "
    "provide the first local evidence on the quality and interchangeability "
    "of paracetamol, useful to the regulatory authority, pharmacists and "
    "patients.")
KEYWORDS = ["acetaminophen", "generic drugs", "interchangeability",
            "Mozambique", "quality control"]

ABREVIATURAS = [
    ("ANARME", "Autoridade Nacional Reguladora de Medicamento"),
    ("ANOVA", "análise de variância"),
    ("CCF", "cromatografia em camada fina"),
    ("CIBS-UniLúrio", "Comité Institucional de Bioética para a Saúde da "
                      "Universidade Lúrio"),
    ("CNBS", "Comité Nacional de Bioética para a Saúde"),
    ("CV", "coeficiente de variação"),
    ("DCI", "denominação comum internacional"),
    ("DPS", "Direcção Provincial de Saúde"),
    ("FCS", "Faculdade de Ciências de Saúde"),
    ("IC95%", "intervalo de confiança a 95%"),
    ("ICH", "International Council for Harmonisation of Technical "
            "Requirements for Pharmaceuticals for Human Use"),
    ("INE", "Instituto Nacional de Estatística"),
    ("JASP", "Jeffreys's Amazing Statistics Program"),
    ("LNME", "Lista Nacional de Medicamentos Essenciais"),
    ("MEDQUARG", "Medicine Quality Assessment Reporting Guidelines"),
    ("OMS", "Organização Mundial da Saúde"),
    ("SDSMAS", "Serviço Distrital de Saúde, Mulher e Acção Social"),
    ("SPSS", "Statistical Package for the Social Sciences"),
    ("UV", "ultravioleta"),
]

# ------------------------------------------------------------ referencias --
FONTES = {
    # --- qualidade dos medicamentos: magnitude, conceitos e determinantes
    "oms2024sf": "World Health Organization. Substandard and falsified medical products: fact sheet [Internet]. Geneva: World Health Organization; 2024 [citado 2026 Set 19]. Disponível em: https://www.who.int/news-room/fact-sheets/detail/substandard-and-falsified-medical-products",
    "ozawa2018": "Ozawa S, Evans DR, Bessias S, Haynie DG, Yemeke TT, Laing SK, et al. Prevalence and Estimated Economic Burden of Substandard and Falsified Medicines in Low- and Middle-Income Countries: A Systematic Review and Meta-analysis. JAMA Netw Open. 2018;1(4):e181662. doi:10.1001/jamanetworkopen.2018.1662. PMID: 30646106.",
    "ozawa2022": "Ozawa S, Chen HH, Lee YA, Higgins CR, Yemeke TT. Characterizing Medicine Quality by Active Pharmaceutical Ingredient Levels: A Systematic Review and Meta-Analysis across Low- and Middle-Income Countries. Am J Trop Med Hyg. 2022;106(6):1778-1790. doi:10.4269/ajtmh.21-1123. PMID: 35895431.",
    "asrade2024": "Asrade Mekonnen B, Getie Yizengaw M, Chanie Worku M. Prevalence of substandard, falsified, unlicensed and unregistered medicine and its associated factors in Africa: a systematic review. J Pharm Policy Pract. 2024;17(1):2375267. doi:10.1080/20523211.2024.2375267. PMID: 39015754.",
    "tegegne2024": "Tegegne AA, Feissa AB, Godena GH, Tefera Y, Hassen HK, Ozalp Y, et al. Substandard and falsified antimicrobials in selected east African countries: A systematic review. PLoS One. 2024;19(1):e0295956. doi:10.1371/journal.pone.0295956. PMID: 38277385.",
    "petersen2017": "Petersen A, Held N, Heide L. Surveillance for falsified and substandard medicines in Africa and Asia by local organizations using the low-cost GPHF Minilab. PLoS One. 2017;12(9):e0184165. doi:10.1371/journal.pone.0184165. PMID: 28877208.",
    "hauk2021": "Hauk C, Hagen N, Heide L. Identification of Substandard and Falsified Medicines: Influence of Different Tolerance Limits and Use of Authenticity Inquiries. Am J Trop Med Hyg. 2021;104(5):1936-1945. doi:10.4269/ajtmh.20-1612. PMID: 33788775.",
    "gabel2024": "Gabel J, Martus P, Heide L. Relationship between Prices and Quality of Essential Medicines from Different Manufacturers Collected in Cameroon, the Democratic Republic of the Congo, and Nigeria. Am J Trop Med Hyg. 2024;111(6):1378-1395. doi:10.4269/ajtmh.24-0309. PMID: 39378886.",
    "maria2025": "Maria V, Tjandrawidjaya WN, Rahmawati A, Sarnianto P, Anggriani Y, Pisani E. Are quality medicines affordable? Evidence from a large survey of medicine price and quality in Indonesia. BMJ Glob Health. 2025;10(5). doi:10.1136/bmjgh-2024-015416. PMID: 40412815.",
    "chabalenge2025": "Chabalenge B, Sahota T, Ermolina I, Tanna S. Substandard and falsified medicines in Africa: healthcare systems challenges, supply chain issues, regulatory challenges and strategies to increase access to quality medicines. Front Pharmacol. 2025;16:1708784. doi:10.3389/fphar.2025.1708784. PMID: 41341026.",
    "khuluza2023": "Khuluza F, Chiumia FK, Nyirongo HM, Kateka C, Hosea RA, Mkwate W. Temperature variations in pharmaceutical storage facilities and knowledge, attitudes, and practices of personnel on proper storage conditions for medicines in southern Malawi. Front Public Health. 2023;11:1209903. doi:10.3389/fpubh.2023.1209903. PMID: 37808988.",
    "bassat2016": "Bassat Q, Tanner M, Guerin PJ, Stricker K, Hamed K. Combating poor-quality anti-malarial medicines: a call to action. Malar J. 2016;15:302. doi:10.1186/s12936-016-1357-8. PMID: 27251199.",
    # --- paracetamol
    "chidiac2023": "Chidiac AS, Buckley NA, Noghrehchi F, Cairns R. Paracetamol (acetaminophen) overdose and hepatotoxicity: mechanism, treatment, prevention measures, and estimates of burden of disease. Expert Opin Drug Metab Toxicol. 2023;19(5):297-317. doi:10.1080/17425255.2023.2223959. PMID: 37436926.",
    "abdel2021": "Abdel Shaheed C, Ferreira GE, Dmitritchenko A, McLachlan AJ, Day RO, Saragiotto B, et al. The efficacy and safety of paracetamol for pain relief: an overview of systematic reviews. Med J Aust. 2021;214(7):324-331. doi:10.5694/mja2.50992. PMID: 33786837.",
    "bos2017": "Bos JC, Mistício MC, Nunguiane G, Mathôt RAA, van Hest RM, Prins JM. Paracetamol clinical dosing routine leads to paracetamol underexposure in an adult severely ill sub-Saharan African hospital population: a drug concentration measurement study. BMC Res Notes. 2017;10(1):671. doi:10.1186/s13104-017-3016-8. PMID: 29202789.",
    "kalantzi2006": "Kalantzi L, Reppas C, Dressman JB, Amidon GL, Junginger HE, Midha KK, et al. Biowaiver monographs for immediate release solid oral dosage forms: acetaminophen (paracetamol). J Pharm Sci. 2006;95(1):4-14. doi:10.1002/jps.20477. PMID: 16307451.",
    "oms2025lme": "World Health Organization. The selection and use of essential medicines, 2025: WHO Model List of Essential Medicines, 24th list [Internet]. Geneva: World Health Organization; 2025 [citado 2026 Set 19]. Disponível em: https://www.who.int/publications/i/item/B09474",
    # --- estudos empíricos sobre marcas de paracetamol
    "abebe2020": "Abebe K, Beressa TB, Yimer BT. In-vitro Evaluations of Quality Control Parameters of Paracetamol Tablets Marketed in Gondar City, Northwest Ethiopia. Drug Healthc Patient Saf. 2020;12:273-279. doi:10.2147/DHPS.S282420. PMID: 33376411.",
    "idris2021": "Idris IM, Hassan DN, Hassen HA, Araya RZ, Weldemariam DG. Consumers' Perception of Generic Medicines and Evaluation of In Vitro Quality Control Parameters of Locally Manufactured Paracetamol Tablets in Asmara, Eritrea: A Cross-Sectional Study. Biomed Res Int. 2021;2021:6642826. doi:10.1155/2021/6642826. PMID: 34150909.",
    "alswayeh2021": "AlSwayeh R, Alvi SN, Hammami MM. Quality assessment of nine paracetamol 500 mg tablet brands marketed in Saudi Arabia. BMC Res Notes. 2021;14(1):254. doi:10.1186/s13104-021-05672-y. PMID: 34193274.",
    "rahman2021": "Rahman M, Akter K, Sarker MS, Sharna JF, Wahed MII. In vitro Comparative Quality Evaluation of Different Brands of Marketed Paracetamol Tablets Available in Bangladesh. JPRI. 2021:26-32. doi:10.9734/jpri/2021/v33i38a32056",
    "zeeshan2020": "Zeeshan F, Lin PY, Sheshala R. Application of Similarity Factor (f2) and Time Required to Drug Release (t%) Indicators for Dissolution Profiles Comparison of Paracetamol Tablets. IJPER. 2020;54(3):647-653. doi:10.5530/ijper.54.3.114",
    "alwadi2022": "Alwadi AY, Arafeh GM, Almehlesi MS, Maswadeh HM, Salman IM, Ameer OZ. Comparative Analysis of Commercially Available Acetaminophen Tablets in Saudi Arabia. Dissolution Technol. 2022;29(3). doi:10.14227/dt290322pgc2",
    "vandy2024": "Vandy A, Conteh E, Lahai M, Kolipha-Kamara M, Marah M, Marah F, et al. Physicochemical quality assessment of various brands of paracetamol tablets sold in Freetown Municipality. Heliyon. 2024;10(3):e25502. doi:10.1016/j.heliyon.2024.e25502. PMID: 38356517.",
    "marisa2024": "Marisa G, Kapala J, Mafuru T, Matinde R, Kimaro E, Kaale E. Quality Evaluation of Locally Manufactured Paracetamol Tablets in East Africa. Biomed Res Int. 2024;2024:9437835. doi:10.1155/2024/9437835. PMID: 39310289.",
    "elbaroudi2024": "Zaema Elbaroudi. Post-Marketing Quality Control of Different Brands of Paracetamol and Paracetamol Plus Caffeine Tablets Available in Libyan Markets. Alq J Med App Sci. 2024:1558-1565. doi:10.54361/ajmas.247489",
    "kamour2024": "Kamour R, El-Sharaa E, Eswayah A. Physical and Chemical Evaluation of Different Brands of Paracetamol Tablets. Alq J Med App Sci. 2024:257-260. doi:10.54361/ajmas.2472009",
    "mathias2026": "E. Mathias I, Emmanuel H. Comparative Evaluation of the Physicomechanical Quality of Commercially Available Paracetamol Tablets Marketed in Gombe Metropolis, Nigeria. BF. 2026;6(1):8-13. doi:10.51470/bf.2026.6.1.08",
    "khawory2026": "Khawory MH, Nordin N, Subki MFM, Ghani NIA, Zulkifli Z, Azmy INW, et al. Physicochemical Characterization and Bibliometric Analysis of Malaysian Paracetamol Tablets in Compliance With MS ISO/IEC 17025 Standards. ScientificWorldJournal. 2026;2026(1):e6619616. doi:10.1155/tswj/6619616. PMID: 42708550.",
    "khuluza2014": "Khuluza F. In-vitro evaluation of the quality of paracetamol and co-trimoxazole tablets used in Malawi based on pharmacopoeial standards. Malawi Med J. 2014;26(2):38-41. PMID: 25157315.",
    # --- Moçambique e Nampula
    "mocambique2017lei": "Moçambique. Assembleia da República. Lei n.º 12/2017, de 8 de Setembro: Lei do medicamento, vacinas e outros produtos biológicos para o uso humano. Boletim da República, I Série, n.º 141 [Internet]. Maputo: Imprensa Nacional de Moçambique; 2017 [citado 2026 Set 19]. Disponível em: https://anarme.gov.mz/download/lei-12-2017-de-8-de-setembro-lei-de-medicamento/",
    "misau2023lnme": "Moçambique. Ministério da Saúde. Diploma Ministerial n.º 52/2023, de 19 de Abril: aprova a Lista Nacional de Medicamentos Essenciais. Boletim da República, I Série, n.º 75 [Internet]. Maputo: Imprensa Nacional de Moçambique; 2023 [citado 2026 Set 19]. Disponível em: https://cdn.who.int/media/docs/default-source/essential-medicines/national-essential-medicines-lists-(neml)/afro_neml/mozambique-updated-lista-nacional-de-medicamentos-essenciais-2023.pdf",
    "anarme2026": "Autoridade Nacional Reguladora de Medicamento. Medicamentos e vacinas: base de dados de produtos registados [Internet]. Maputo: ANARME; 2026 [citado 2026 Set 19]. Disponível em: https://anarme.gov.mz/medicamentos-e-vacinas/",
    "ine2021": "Instituto Nacional de Estatística. IV Recenseamento Geral da População e Habitação 2017: resultados definitivos, província de Nampula [Internet]. Nampula: Instituto Nacional de Estatística; 2021 [citado 2026 Set 19]. Disponível em: http://www.sina.gov.mz/wp-content/uploads/2024/05/NAMPULA-RESUTADOS-DEFINITIVOS-DO-CENSO-2017.pdf",
    "wiseman2025": "Wiseman R, Truter I. Drug utilisation research and medicine access in Mozambique: An overview. Explor Res Clin Soc Pharm. 2025;17:100548. doi:10.1016/j.rcsop.2024.100548. PMID: 39759955.",
    "torres2019": "Torres NF, Solomon VP, Middleton LE. Patterns of self-medication with antibiotics in Maputo City: a qualitative study. Antimicrob Resist Infect Control. 2019;8:161. doi:10.1186/s13756-019-0618-z. PMID: 31649818.",
    # --- farmacopeia, métodos e intercambialidade
    "phint2025par": "World Health Organization. Paracetamol tablets (Paracetamoli compressi). In: The International Pharmacopoeia. 13th ed [Internet]. Geneva: World Health Organization; 2025 [citado 2026 Set 19]. Disponível em: https://digicollections.net/phint/pdf/b/6.2.2.114.Paracetamol-tablets-(Paracetamoli-compressi).pdf",
    "phint2025comp": "World Health Organization. Tablets. In: The International Pharmacopoeia. 13th ed [Internet]. Geneva: World Health Organization; 2025 [citado 2026 Set 19]. Disponível em: https://digicollections.net/phint/pdf/b/6.2.1.8.Tablets.pdf",
    "phint2025massa": "World Health Organization. 5.2 Uniformity of mass for single-dose preparations. In: The International Pharmacopoeia. 13th ed [Internet]. Geneva: World Health Organization; 2025 [citado 2026 Set 19]. Disponível em: https://digicollections.net/phint/pdf/b/7.5.3.5.2-Uniformity-of-mass-for-single-dose-preparations.pdf",
    "phint2025desag": "World Health Organization. 5.3 Disintegration test for tablets and capsules. In: The International Pharmacopoeia. 13th ed [Internet]. Geneva: World Health Organization; 2025 [citado 2026 Set 19]. Disponível em: https://digicollections.net/phint/pdf/b/7.5.4.5.3-Disintegration-test-for-tablets-and-capsules.pdf",
    "phint2025friab": "World Health Organization. Tablet friability. In: The International Pharmacopoeia. 13th ed [Internet]. Geneva: World Health Organization; 2025 [citado 2026 Set 19]. Disponível em: https://digicollections.net/phint/pdf/b/10.4.5.Tablet-friability.pdf",
    "phint2025esmag": "World Health Organization. Resistance to crushing of tablets. In: The International Pharmacopoeia. 13th ed [Internet]. Geneva: World Health Organization; 2025 [citado 2026 Set 19]. Disponível em: https://digicollections.net/phint/pdf/b/10.4.3.Resistance-to-crushing-of-tablets.pdf",
    "phint2025dissol": "World Health Organization. Dissolution testing of tablets and capsules. In: The International Pharmacopoeia. 13th ed [Internet]. Geneva: World Health Organization; 2025 [citado 2026 Set 19]. Disponível em: https://digicollections.net/phint/pdf/b/10.3.1.Dissolution-testing-of-tablets-and-capsules.pdf",
    "phint2019diss": "World Health Organization. 5.5 Dissolution test for solid oral dosage forms. In: The International Pharmacopoeia. 9th ed [Internet]. Geneva: World Health Organization; 2019 [citado 2026 Set 19]. Disponível em: https://digicollections.net/phint/pdf/b.2019/7.5.6.5.5-Dissolution-test-for-solid-oral-dosage-forms.pdf",
    "oms2016inq": "World Health Organization. Guidelines on the conduct of surveys of the quality of medicines. In: WHO Expert Committee on Specifications for Pharmaceutical Preparations: fiftieth report. WHO Technical Report Series, No. 996, Annex 7 [Internet]. Geneva: World Health Organization; 2016 [citado 2026 Set 19]. Disponível em: https://www.who.int/docs/default-source/medicines/norms-and-standards/guidelines/distribution/trs966-annex7-who-guidelines-on-the-conduct-of-surveys-of-the-quality-of-medicines.pdf",
    "oms2024int": "World Health Organization. Multisource (generic) pharmaceutical products: guidelines on registration requirements to establish interchangeability. In: WHO Expert Committee on Specifications for Pharmaceutical Preparations: fifty-seventh report. WHO Technical Report Series, No. 1052, Annex 8 [Internet]. Geneva: World Health Organization; 2024 [citado 2026 Set 19]. Disponível em: https://cdn.who.int/media/docs/default-source/medicines/norms-and-standards/guidelines/regulatory-standards/trs1052_annex8.pdf",
    "oms2024bio": "World Health Organization. WHO Biowaiver List: proposal to waive in vivo bioequivalence requirements for WHO Model List of Essential Medicines immediate-release, solid oral dosage forms. In: WHO Expert Committee on Specifications for Pharmaceutical Preparations: fifty-seventh report. WHO Technical Report Series, No. 1052, Annex 6 [Internet]. Geneva: World Health Organization; 2024 [citado 2026 Set 19]. Disponível em: https://cdn.who.int/media/docs/default-source/medicines/norms-and-standards/guidelines/regulatory-standards/trs1052_annex6.pdf",
    "ich2019m9": "International Council for Harmonisation of Technical Requirements for Pharmaceuticals for Human Use. ICH harmonised guideline M9: biopharmaceutics classification system-based biowaivers [Internet]. Geneva: ICH; 2019 [citado 2026 Set 19]. Disponível em: https://database.ich.org/sites/default/files/M9_Guideline_Step4_2019_1116.pdf",
    "ich2023q2": "International Council for Harmonisation of Technical Requirements for Pharmaceuticals for Human Use. ICH harmonised guideline Q2(R2): validation of analytical procedures [Internet]. Geneva: ICH; 2023 [citado 2026 Set 19]. Disponível em: https://database.ich.org/sites/default/files/ICH_Q2%28R2%29_Guideline_2023_1130.pdf",
    "muselik2021": "Muselík J, Komersová A, Kubová K, Matzick K, Skalická B. A Critical Overview of FDA and EMA Statistical Methods to Compare In Vitro Drug Dissolution Profiles of Pharmaceutical Products. Pharmaceutics. 2021;13(10). doi:10.3390/pharmaceutics13101703. PMID: 34683995.",
    "noce2020": "Noce L, Gwaza L, Mangas-Sanjuan V, Garcia-Arieta A. Comparison of free software platforms for the calculation of the 90% confidence interval of f(2) similarity factor by bootstrap analysis. Eur J Pharm Sci. 2020;146:105259. doi:10.1016/j.ejps.2020.105259. PMID: 32058055.",
    "newton2009": "Newton PN, Lee SJ, Goodman C, Fernández FM, Yeung S, Phanouvong S, et al. Guidelines for field surveys of the quality of medicines: a proposal. PLoS Med. 2009;6(3):e52. doi:10.1371/journal.pmed.1000052. PMID: 19320538.",
    "helsinquia2025": "World Medical Association. World Medical Association Declaration of Helsinki: Ethical Principles for Medical Research Involving Human Participants. JAMA. 2025;333(1):71-74. doi:10.1001/jama.2024.21972. PMID: 39425955.",
}

SEMINAIS = {
    "kalantzi2006": ("Monografia de bioisenção do paracetamol, ainda a "
                     "referência que fundamenta a classificação "
                     "biofarmacêutica e a aceitação de dados de dissolução "
                     "para este fármaco"),
    "newton2009": ("Proposta original das orientações de relato de "
                   "inquéritos de qualidade de medicamentos (MEDQUARG), "
                   "norma de relato adoptada pelo estudo"),
    "khuluza2014": ("Único estudo publicado sobre a conformidade "
                    "farmacopeica de comprimidos de paracetamol num país "
                    "vizinho de Moçambique (Malawi)"),
}
