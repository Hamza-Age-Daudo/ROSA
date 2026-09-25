# -*- coding: utf-8 -*-
"""
TEMA 48. Intoxicações agudas atendidas no Banco de Socorros do Hospital
Central de Nampula: agentes envolvidos, perfil das vítimas e disponibilidade
de antídotos (estudo documental retrospectivo, 2025-2026).

Compor e validar:   python -X utf8 _motor/motor.py _conteudo/tema_48.py
Verificar fontes:   python -X utf8 _motor/refs.py verificar _conteudo/tema_48.py
"""
from blocos import (CAMPO, FORMULA, H3, LISTA, NOTA, P, PERG, QUADRO,
                    TABELA)

NUMERO = 48
SLUG = "Intoxicacoes_Agudas_Banco_Socorros_HCN_Nampula"
TITULO = ("Intoxicações agudas atendidas no Banco de Socorros do Hospital "
          "Central de Nampula: agentes envolvidos, perfil das vítimas e "
          "disponibilidade de antídotos, 2025 a 2026")
DESENHO = ("Observacional descritivo e analítico, retrospectivo, documental "
           "(censo dos episódios de 2025 e 2026)")

AUTOR = "[Nome do(a) estudante]"
ORIENTADOR = "[Nome e grau académico do(a) orientador(a)]"

# ---------------------------------------------------------------- resumo --
RESUMO = (
    "As intoxicações agudas são uma causa frequente de atendimento urgente "
    "em África e resultam da exposição acidental ou intencional a "
    "medicamentos, pesticidas, petróleo de iluminação, outros produtos "
    "domésticos, plantas, preparações tradicionais e álcool. Moçambique não "
    "dispõe de centro de informação antivenenos nem de dados publicados "
    "sobre estes casos no norte do país, o que deixa sem base local a "
    "prevenção e o aprovisionamento de antídotos. O estudo pretende caracterizar as intoxicações "
    "agudas atendidas no Banco de Socorros do Hospital Central de Nampula "
    "entre 1 de Janeiro de 2025 e 31 de Dezembro de 2026 e confrontar os "
    "agentes encontrados com a disponibilidade dos antídotos "
    "correspondentes. Trata-se de um estudo observacional, descritivo e "
    "analítico, retrospectivo e documental, cuja unidade de análise é o "
    "episódio de atendimento. Será feito o censo dos episódios elegíveis, "
    "excluídos os envenenamentos por animais peçonhentos, identificados "
    "nos livros de registo e nos processos clínicos, com "
    "amostragem sistemática de 700 episódios se o total exceder esse "
    "número. Os dados serão extraídos numa ficha sem identificadores, "
    "testada em 30 registos de 2024, com dupla extracção de 10%. Os "
    "agentes serão classificados pela décima revisão da Classificação "
    "Internacional de Doenças e pelas classificações da Organização Mundial "
    "da Saúde para medicamentos e pesticidas; a intencionalidade será "
    "atribuída por dois classificadores independentes, com kappa de Cohen. "
    "A disponibilidade dos antídotos será verificada na lista nacional de "
    "medicamentos essenciais e nos registos da farmácia hospitalar. A análise incluirá proporções com intervalos de "
    "confiança a 95%, testes do qui-quadrado ou exacto de Fisher e "
    "regressão logística quando o número de eventos o permitir. Espera-se "
    "conhecer os agentes predominantes por grupo etário, a proporção de "
    "intoxicações autoprovocadas, a letalidade por agente e as lacunas entre "
    "a necessidade e a disponibilidade de antídotos, úteis para a prevenção "
    "e para a preparação do hospital.")
PALAVRAS_CHAVE = ["antídotos", "intoxicação", "Moçambique", "pesticidas",
                  "serviço de urgência"]
ABSTRACT = (
    "Acute poisoning is a frequent cause of emergency care in Africa and "
    "results from accidental or intentional exposure to medicines, "
    "pesticides, lamp paraffin, other household products, plants, "
    "traditional preparations and alcohol. Mozambique has neither a poison "
    "information centre nor published data on these cases in the north of "
    "the country, which leaves prevention and antidote procurement without "
    "a local basis. The study aims to characterise acute poisonings attended at the "
    "emergency department of Nampula Central Hospital between 1 January 2025 "
    "and 31 December 2026 and to compare the agents found with the "
    "availability of the corresponding antidotes. It is an observational, "
    "descriptive and analytical, retrospective, record-based study whose "
    "unit of analysis is the care episode. All eligible episodes, excluding "
    "envenomation by venomous animals, identified in the registration books "
    "and clinical files will be included, with "
    "systematic sampling of 700 episodes if the total exceeds that number. "
    "Data will be extracted onto a form without identifiers, previously "
    "tested on 30 records from 2024, with double extraction of 10% of the "
    "records. Agents will be classified by the tenth revision of the "
    "International Classification of Diseases and by the World Health "
    "Organization classifications for medicines and pesticides; intent will "
    "be assigned by two independent classifiers, "
    "with Cohen's kappa. Antidote availability will be checked against the "
    "national essential medicines list and the hospital pharmacy records. The analysis will include proportions "
    "with 95% confidence intervals, chi-square or Fisher's exact tests and "
    "logistic regression when the number of events allows. The study is "
    "expected to show the predominant agents in each age group, the "
    "proportion of self-inflicted poisonings, case fatality by agent and the "
    "gaps between need for and availability of antidotes, information "
    "useful for prevention and for hospital preparedness.")
KEYWORDS = ["antidotes", "emergency service", "Mozambique", "pesticides",
            "poisoning"]

ABREVIATURAS = [
    ("ATC", "classificação Anatómica, Terapêutica e Química"),
    ("CIBS-UniLúrio", "Comité Institucional de Bioética para a Saúde da "
                      "Universidade Lúrio"),
    ("CID", "Classificação Internacional de Doenças"),
    ("FCS", "Faculdade de Ciências de Saúde"),
    ("HCN", "Hospital Central de Nampula"),
    ("IC95%", "intervalo de confiança a 95%"),
    ("IIQ", "intervalo interquartil"),
    ("LNME", "Lista Nacional de Medicamentos Essenciais"),
    ("MISAU", "Ministério da Saúde"),
    ("OMS", "Organização Mundial da Saúde"),
    ("OR", "odds ratio"),
    ("PSS", "Poisoning Severity Score (escala de gravidade da intoxicação)"),
    ("RECORD", "REporting of studies Conducted using Observational "
               "Routinely-collected health Data"),
    ("SPSS", "Statistical Package for the Social Sciences"),
    ("STROBE", "Strengthening the Reporting of Observational Studies in "
               "Epidemiology"),
    ("UCI", "unidade de cuidados intensivos"),
    ("UniLúrio", "Universidade Lúrio"),
]

# ------------------------------------------------------------ referencias --
FONTES = {
    # -- magnitude global, suicídio e pesticidas
    "omspc2020": "World Health Organization. Guidelines for establishing a poison centre [Internet]. Geneva: World Health Organization; 2020 [citado 2026 Set 19]. Disponível em: https://www.who.int/publications/i/item/9789240009523",
    "omsghomort2024": "World Health Organization. Poisoning (unintentional): attributed mortality rate (per 100 000 population). The Global Health Observatory [Internet]. Geneva: World Health Organization; 2024 [citado 2026 Set 19]. Disponível em: https://www.who.int/data/gho/data/indicators/indicator-details/GHO/mortality-rate-attributed-to-unintentional-poisoning-%28per-100-000-population%29",
    "omssuicidio2026": "World Health Organization. Suicide: fact sheet [Internet]. Geneva: World Health Organization; 2026 [citado 2026 Set 19]. Disponível em: https://www.who.int/news-room/fact-sheets/detail/suicide",
    "mew2017": "Mew EJ, Padmanathan P, Konradsen F, Eddleston M, Chang SS, Phillips MR, et al. The global burden of fatal self-poisoning with pesticides 2006-15: Systematic review. J Affect Disord. 2017;219:93-104. doi:10.1016/j.jad.2017.05.002. PMID: 28535450.",
    "karunarathne2020": "Karunarathne A, Gunnell D, Konradsen F, Eddleston M. How many premature deaths from pesticide suicide have occurred since the agricultural Green Revolution?. Clin Toxicol (Phila). 2020;58(4):227-232. doi:10.1080/15563650.2019.1662433. PMID: 31500467.",
    "boedeker2020": "Boedeker W, Watts M, Clausing P, Marquez E. The global distribution of acute unintentional pesticide poisoning: estimations based on a systematic review. BMC Public Health. 2020;20(1):1875. doi:10.1186/s12889-020-09939-0. PMID: 33287770.",
    # -- estudos hospitalares africanos
    "zgambo2016": "Z'gambo J, Siulapwa Y, Michelo C. Pattern of acute poisoning at two urban referral hospitals in Lusaka, Zambia. BMC Emerg Med. 2016;16:2. doi:10.1186/s12873-016-0068-3. PMID: 26748777.",
    "adinew2017": "Adinew GM, Woredekal AT, DeVos EL, Birru EM, Abdulwahib MB. Poisoning cases and their management in emergency centres of government hospitals in northwest Ethiopia. Afr J Emerg Med. 2017;7(2):74-78. doi:10.1016/j.afjem.2017.04.005. PMID: 30456112.",
    "asrie2024": "Asrie AB, Atnafie SA, Getahun KA, Birru EM, Mekonnen GB, Alemayehu GA, et al. Poisoning cases and their management in Amhara National Regional State, Ethiopia: Hospital-based prospective study. PLoS One. 2024;19(5):e0303438. doi:10.1371/journal.pone.0303438. PMID: 38820326.",
    "mbongwe2020": "Mbongwe B, Moinami J, Masupe T, Tapera R, Molefe T, Erick P, et al. Nature and sources of poisoning in patients admitted to a referral hospital in Gaborone, Botswana; findings and implications. Hosp Pract (1995). 2020;48(2):100-107. doi:10.1080/21548331.2020.1739415. PMID: 32133895.",
    "pillay2026": "Pillay S. Profile of deliberate self-poisoning admissions in KwaZulu-Natal Province, South Africa (2018 - 2023) and the impact of COVID-19. S Afr Med J. 2026;116(1):e3710. doi:10.7196/SAMJ.2026.v116i1.3710. PMID: 42246795.",
    "areprekumor2024": "Areprekumor TE, Joboy-Okei E, Amadin NO, Kalu SU. Patterns and clinical outcomes of childhood poisoning presenting to a children's emergency department in Yenagoa, Nigeria: a 10-year retrospective study. BMJ Paediatr Open. 2024;8(1). doi:10.1136/bmjpo-2023-002433. PMID: 38754895.",
    "nigussie2022": "Nigussie S, Demeke F, Getachew M, Amare F. Treatment outcome and associated factors among patients admitted with acute poisoning in a tertiary hospital in Eastern Ethiopia: A cross-sectional study. SAGE Open Med. 2022;10:20503121221078155. doi:10.1177/20503121221078155. PMID: 35198211.",
    "laher2022": "Laher AE, Motara F, Gihwala R, Moolla M. The profile of patients presenting with intentional self-poisoning to the Charlotte Maxeke Johannesburg Academic Hospital emergency department, South Africa. S Afr Med J. 2022;112(5):347-351. PMID: 35587248.",
    "molla2022": "Molla YM, Belachew KD, Ayehu GW, Teshome AA. Acute poisoning in children in Ethiopia: a cross-sectional study. Sci Rep. 2022;12(1):18750. doi:10.1038/s41598-022-23193-x. PMID: 36335242.",
    "ajeigbe2023": "Ajeigbe AK, Adedeji TA, Jeje OA, Olukoyejo OE, Bello MB, Ogra VO, et al. Profile of Acute Poisoning among Adult Patients at the Emergency Room of a Tertiary Hospital, South-western Nigeria. West Afr J Med. 2023;40(9):920-924. PMID: 37767751.",
    "bruins2019": "Bruins J, Menezes CN, Wong ML. Organophosphate poisoning at Chris Hani Baragwanath Academic Hospital 2012 - 2015. Afr J Thorac Crit Care Med. 2019;25(3). PMID: 34286262.",
    "davies2023": "Davies B, Hlela MBKM, Rother HA. Child and adolescent mortality associated with pesticide toxicity in Cape Town, South Africa, 2010-2019: a retrospective case review. BMC Public Health. 2023;23(1):792. doi:10.1186/s12889-023-15652-5. PMID: 37118778.",
    # -- antídotos e preparação hospitalar
    "omsghopc2023": "World Health Organization. Poison control and unintentional poisoning. The Global Health Observatory [Internet]. Geneva: World Health Organization; 2023 [citado 2026 Set 19]. Disponível em: https://www.who.int/data/gho/data/themes/topics/indicator-groups/poison-control-and-unintentional-poisoning",
    "dart2018": "Dart RC, Goldfrank LR, Erstad BL, Huang DT, Todd KH, Weitz J, et al. Expert Consensus Guidelines for Stocking of Antidotes in Hospitals That Provide Emergency Care. Ann Emerg Med. 2018;71(3):314-325.e1. doi:10.1016/j.annemergmed.2017.05.021. PMID: 28669553.",
    "harnett2021": "Harnett JT, Vithlani S, Sobhdam S, Kent J, McClure L, Thomas SH, et al. National audit of antidote stocking in UK emergency departments. Eur J Hosp Pharm. 2021;28(4):217-222. doi:10.1136/ejhpharm-2019-001988. PMID: 34162673.",
    "rodrigues2017": "Rodrigues Fernandes LC, Galvão TF, Toledo Ricardi AS, De Capitani EM, Hyslop S, Bucaretchi F. Antidote availability in the municipality of Campinas, São Paulo, Brazil. Sao Paulo Med J. 2017;135(1):15-22. doi:10.1590/1516-3180.2016.00171120816. PMID: 28301629.",
    "altaweel2022": "Al-Taweel D, Koshy S, Al-Ansari S, Al-Haqan A, Qabazard B. Expert consensus for a national essential antidote list: E-Delphi method. PLoS One. 2022;17(6):e0269456. doi:10.1371/journal.pone.0269456. PMID: 35709136.",
    "omseml2025": "World Health Organization. The selection and use of essential medicines, 2025: WHO Model List of Essential Medicines, 24th list [Internet]. Geneva: World Health Organization; 2025 [citado 2026 Set 19]. Disponível em: https://www.who.int/publications/i/item/B09474",
    # -- Moçambique e Nampula
    "wagenaar2016": "Wagenaar BH, Raunig-Berhó M, Cumbe V, Rao D, Napúa M, Sherr K. Suicide Attempts and Deaths in Sofala, Mozambique, From 2011 to 2014. Crisis. 2016;37(6):445-453. doi:10.1027/0227-5910/a000383. PMID: 27245814.",
    "gudo2018": "Gudo ES, Cook K, Kasper AM, Vergara A, Salomão C, Oliveira F, et al. Description of a Mass Poisoning in a Rural District in Mozambique: The First Documented Bongkrekic Acid Poisoning in Africa. Clin Infect Dis. 2018;66(9):1400-1406. doi:10.1093/cid/cix1005. PMID: 29155976.",
    "asnake2025": "Asnake AA, Seifu BL, Fente BM, Asebe HA, Bezie MM, Negussie YM, et al. Multilevel analysis of factors associated with suicide attempts: Evidence from 2022/2023 Mozambique Demographic and Health Survey. PLoS One. 2025;20(2):e0315648. doi:10.1371/journal.pone.0315648. PMID: 39903720.",
    "misau2023": "Ministério da Saúde. Diploma Ministerial n.º 52/2023, de 19 de Abril: aprova a Lista Nacional de Medicamentos Essenciais. Boletim da República, I Série, n.º 75 [Internet]. Maputo: Imprensa Nacional de Moçambique; 2023 [citado 2026 Set 19]. Disponível em: https://cdn.who.int/media/docs/default-source/essential-medicines/national-essential-medicines-lists-(neml)/afro_neml/mozambique-updated-lista-nacional-de-medicamentos-essenciais-2023.pdf",
    "amado2023": "Amado V, Couto MT, Filipe M, Möller J, Wallis L, Laflamme L. Assessment of critical resource gaps in pediatric injury care in Mozambique's four largest Hospitals. PLoS One. 2023;18(6):e0286288. doi:10.1371/journal.pone.0286288. PMID: 37262032.",
    "xavier2024": "Xavier SP, da Silva AMC, Victor A. Antibiotic prescribing patterns in pediatric patients using the WHO access, watch, reserve (AWaRe) classification at a quaternary hospital in Nampula, Mozambique. Sci Rep. 2024;14(1):22719. doi:10.1038/s41598-024-72349-4. PMID: 39349590.",
    "miguel2025": "Miguel AR, Conceição ED, Alfredo C, Miguel PN, Kaiser H. Snakebite in Nicoadala District, central Mozambique: a first assessment based on hospital records. Trans R Soc Trop Med Hyg. 2025;119(8):872-880. doi:10.1093/trstmh/traf033. PMID: 40151012.",
    # -- agentes específicos
    "tenenbaum2021": "Tenenbaum A, Rephaeli R, Cohen-Cymberknoh M, Aberbuch D, Rekhtman D. Hydrocarbon Intoxication in Children: Clinical and Sociodemographic Characteristics. Pediatr Emerg Care. 2021;37(10):502-506. doi:10.1097/PEC.0000000000002111. PMID: 32433458.",
    "rostrup2016": "Rostrup M, Edwards JK, Abukalish M, Ezzabi M, Some D, Ritter H, et al. The Methanol Poisoning Outbreaks in Libya 2013 and Kenya 2014. PLoS One. 2016;11(3):e0152676. doi:10.1371/journal.pone.0152676. PMID: 27030969.",
    # -- classificações e métodos
    "omscid2022": "World Health Organization. International Classification of Diseases (ICD) [Internet]. Geneva: World Health Organization; 2022 [citado 2026 Set 19]. Disponível em: https://www.who.int/standards/classifications/classification-of-diseases",
    "omscid10": "World Health Organization. International Statistical Classification of Diseases and Related Health Problems 10th Revision (ICD-10), version 2019 [Internet]. Geneva: World Health Organization; 2019 [citado 2026 Set 19]. Disponível em: https://icd.who.int/browse10/2019/en",
    "whocc2026": "WHO Collaborating Centre for Drug Statistics Methodology. ATC/DDD Index 2026 [Internet]. Oslo: Norwegian Institute of Public Health; 2026 [citado 2026 Set 19]. Disponível em: https://atcddd.fhi.no/atc_ddd_index/",
    "omspest2020": "World Health Organization. The WHO recommended classification of pesticides by hazard and guidelines to classification, 2019 edition [Internet]. Geneva: World Health Organization; 2020 [citado 2026 Set 19]. Disponível em: https://www.who.int/publications/i/item/9789240005662",
    "persson1998": "Persson HE, Sjöberg GK, Haines JA, Pronczuk de Garbino J. Poisoning severity score. Grading of acute poisoning. J Toxicol Clin Toxicol. 1998;36(3):205-13. doi:10.3109/15563659809028940. PMID: 9656975.",
    "mchugh2012": "McHugh ML. Interrater reliability: the kappa statistic. Biochem Med (Zagreb). 2012;22(3):276-82. PMID: 23092060.",
    "peduzzi1996": "Peduzzi P, Concato J, Kemper E, Holford TR, Feinstein AR. A simulation study of the number of events per variable in logistic regression analysis. J Clin Epidemiol. 1996;49(12):1373-9. doi:10.1016/s0895-4356(96)00236-3. PMID: 8970487.",
    "vonelm2007": "von Elm E, Altman DG, Egger M, Pocock SJ, Gøtzsche PC, Vandenbroucke JP. Strengthening the Reporting of Observational Studies in Epidemiology (STROBE) statement: guidelines for reporting observational studies. BMJ. 2007;335(7624):806-8. doi:10.1136/bmj.39335.541782.AD. PMID: 17947786.",
    "benchimol2015": "Benchimol EI, Smeeth L, Guttmann A, Harron K, Moher D, Petersen I, et al. The REporting of studies Conducted using Observational Routinely-collected health Data (RECORD) statement. PLoS Med. 2015;12(10):e1001885. doi:10.1371/journal.pmed.1001885. PMID: 26440803.",
    # -- ética
    "wma2025": "World Medical Association. World Medical Association Declaration of Helsinki: Ethical Principles for Medical Research Involving Human Participants. JAMA. 2025;333(1):71-74. doi:10.1001/jama.2024.21972. PMID: 39425955.",
    "lei3de2023": "República de Moçambique. Lei n.º 3/2023, de 8 de Junho: Lei de Investigação em Saúde Humana [Internet]. Maputo: Imprensa Nacional de Moçambique; 2023 [citado 2026 Set 19]. Disponível em: https://anarme.gov.mz/download/lei-3-2023-de-8-de-junho-lei-de-investigacao-em-saude-humana/",
    "omsmedia2023": "World Health Organization. Preventing suicide: a resource for media professionals, update 2023 [Internet]. Geneva: World Health Organization; 2023 [citado 2026 Set 19]. Disponível em: https://www.who.int/publications/i/item/9789240076846",
}
SEMINAIS = {
    "persson1998": ("Artigo original da Poisoning Severity Score, escala de "
                    "gravidade desenvolvida com o Programa Internacional de "
                    "Segurança Química e usada para graduar a gravidade a "
                    "partir dos registos."),
    "mchugh2012": ("Artigo metodológico de referência sobre a interpretação "
                   "do kappa de Cohen em estudos de saúde, usado para fixar "
                   "o limiar de concordância entre classificadores."),
    "peduzzi1996": ("Estudo de simulação que fundamenta a regra de pelo "
                    "menos 10 eventos por variável na regressão logística."),
    "vonelm2007": ("Declaração STROBE original, norma de relato dos estudos "
                   "observacionais."),
    "benchimol2015": ("Declaração RECORD original, extensão da STROBE para "
                      "estudos com dados de saúde recolhidos por rotina."),
}

# ----------------------------------------------------- 1. introducao --------
INTRODUCAO = [
    P("A intoxicação aguda resulta da exposição, num curto intervalo de "
      "tempo, a uma substância em quantidade ou em circunstâncias capazes de "
      "causar dano, e continua a ser um problema de saúde pública com dupla "
      "face, acidental e intencional. A Organização Mundial da Saúde (OMS) "
      "estimou que, em 2016, as intoxicações não intencionais causaram "
      "106.683 mortes e a perda de 6,3 milhões de anos de vida saudável "
      "{omspc2020}. A taxa de mortalidade atribuída a intoxicações não "
      "intencionais, indicador do Objectivo de Desenvolvimento Sustentável "
      "3.9.3, era em 2021 de 0,7 por 100.000 habitantes no mundo, de 1,2 na "
      "Região Africana e de 1,5 (intervalo de incerteza de 0,7 a 2,8) em "
      "Moçambique {omsghomort2024}. A estas mortes somam-se as da face "
      "intencional: mais de 720.000 pessoas morrem por suicídio todos os "
      "anos, 73% delas em países de baixo e médio rendimento, e o suicídio "
      "foi em 2021 a terceira causa de morte entre os 15 e os 29 anos "
      "{omssuicidio2026}."),
    P("Nos países de baixo rendimento, os pesticidas ocupam um lugar à "
      "parte. Uma revisão sistemática estimou cerca de 110.000 mortes anuais "
      "por auto-envenenamento com pesticidas entre 2010 e 2014 e reconheceu "
      "que os dados de África eram escassos e provavelmente subestimados "
      "{mew2017}. O total "
      "acumulado desde 1960 foi estimado entre 14,3 e 14,9 milhões de "
      "mortes, em grande parte actos impulsivos cujos autores, na ausência "
      "de um pesticida altamente perigoso, teriam muitas vezes sobrevivido "
      "{karunarathne2020}. Do lado não intencional, calcula-se que ocorram "
      "385 milhões de intoxicações agudas por pesticidas por ano, com a "
      "África Oriental entre as regiões com mais casos não fatais "
      "{boedeker2020}."),
    P("Os estudos hospitalares da África subsariana mostram que o perfil dos "
      "agentes varia de um país para outro e que só o conhecimento local "
      "permite orientar a resposta. Em dois hospitais de referência de "
      "Lusaka, os pesticidas estiveram presentes em 57% dos 873 casos "
      "{zgambo2016}; no noroeste da Etiópia predominaram os "
      "organofosforados e a lixívia {adinew2017}, e na região de Amhara os "
      "fosfetos metálicos causaram a maioria das 78 mortes registadas entre "
      "442 doentes {asrie2024}. No Botswana, pelo contrário, metade das "
      "intoxicações foi causada por medicamentos {mbongwe2020}, e num "
      "hospital terciário da província sul-africana de KwaZulu-Natal os "
      "medicamentos, incluindo os anti-retrovirais, estiveram em 81% dos "
      "auto-envenenamentos {pillay2026}. Nas crianças nigerianas, o "
      "querosene foi responsável pela maior parte dos óbitos "
      "{areprekumor2024}."),
    P("A capacidade de resposta dos sistemas de saúde depende de dois "
      "recursos que a literatura trata em conjunto: os centros de informação "
      "antivenenos e os antídotos. Em 1 de Janeiro de 2023, apenas 47% dos "
      "Estados-Membros da OMS tinham um centro antivenenos, e o directório "
      "mundial não inclui nenhum em Moçambique, embora inclua a África do "
      "Sul, a Tanzânia, o Zimbabué e Angola {omsghopc2023}. Quanto aos "
      "antídotos, um consenso de peritos aconselhou cada hospital com "
      "urgência a basear o seu stock numa avaliação formal dos riscos "
      "locais {dart2018}, o que exige conhecer os agentes que chegam de "
      "facto à urgência."),
    P("Em Moçambique, a evidência disponível é fragmentária mas "
      "preocupante. No Hospital Central da Beira, 18,0% das consultas "
      "psiquiátricas de urgência corresponderam a tentativas de suicídio, e "
      "o veneno para ratos foi usado em 66% delas {wagenaar2016}. Em 2015, "
      "em Chitima, a ingestão de pombe, uma bebida tradicional contaminada "
      "com ácido bongcréquico, fez 234 doentes e 75 mortos {gudo2018}. No "
      "Inquérito Demográfico e de Saúde de 2022-2023, 3,6% dos jovens de 15 "
      "a 29 anos referiram ter considerado seriamente uma tentativa de "
      "suicídio nos 12 meses anteriores {asnake2025}. A Lista Nacional de "
      "Medicamentos Essenciais (LNME) aprovada em 2023 dedica um capítulo "
      "aos antídotos {misau2023}, mas não garante a sua presença nas "
      "urgências."),
    P("O Hospital Central de Nampula (HCN) é um hospital de nível "
      "quaternário {xavier2024} e a referência da região norte, que assiste "
      "as províncias de Cabo Delgado, Nampula e Niassa {amado2023}. O seu "
      "Banco de Socorros recebe intoxicados da cidade e doentes referidos dos "
      "distritos, sem apoio de um centro antivenenos. As pesquisas feitas "
      "para este protocolo não encontraram nenhum estudo publicado sobre os "
      "agentes, a intencionalidade ou a evolução das intoxicações agudas no "
      "HCN ou no norte de Moçambique, e um estudo documental moçambicano "
      "sobre mordeduras de cobra, feito em centros de saúde da Zambézia, "
      "mostrou que os livros de registo omitem com frequência o tratamento "
      "e a evolução {miguel2025}. É esta a lacuna que o estudo pretende "
      "preencher."),
    P("O presente protocolo propõe, por isso, caracterizar as intoxicações "
      "agudas atendidas no Banco de Socorros do HCN em 2025 e 2026 e "
      "confrontar os agentes encontrados com a inclusão dos antídotos "
      "correspondentes na LNME e com a sua disponibilidade na farmácia do "
      "hospital, para orientar a prevenção e a preparação do HCN em "
      "antídotos."),
]

# ----------------------------------------------------- 2. problema ----------
PROBLEMA = [
    P("No Banco de Socorros do HCN, o clínico que recebe um intoxicado tem "
      "de decidir em minutos a descontaminação, o antídoto e o destino do "
      "doente, muitas vezes sem saber com certeza qual foi a substância e "
      "sem um centro antivenenos que possa consultar {omsghopc2023}. A decisão depende de o antídoto certo estar "
      "na farmácia nesse momento. Os estudos africanos mostram que esta "
      "cadeia falha com frequência: no noroeste da Etiópia só 45,5% dos "
      "intoxicados por organofosforados receberam atropina {adinew2017}, e "
      "numa urgência pediátrica nigeriana os antídotos foram usados em "
      "15,9% dos casos, com os autores a apontarem a disponibilidade como "
      "obstáculo {areprekumor2024}. No próprio HCN, em Novembro de 2020, "
      "faltavam na urgência pediátrica 9 dos 11 medicamentos para "
      "intoxicações da lista de verificação da OMS, a proporção mais alta "
      "dos quatro hospitais centrais avaliados {amado2023}, mas não se sabe "
      "se os antídotos que faltam são precisamente os que os agentes locais "
      "exigem."),
    P("O problema tem duas consequências práticas. A primeira é clínica: "
      "sem conhecer os agentes mais frequentes e os mais letais, o hospital "
      "não consegue priorizar o stock de antídotos, arriscando manter "
      "produtos pouco usados que caducam e deixar em ruptura os que "
      "salvariam vidas, como sucede mesmo em países de alto rendimento, onde "
      "só 41,7% dos hospitais do Reino Unido cumpriam as recomendações para "
      "os antídotos de uso imediato {harnett2021}. A segunda é preventiva: as "
      "medidas que reduzem as intoxicações, como a restrição do acesso aos "
      "pesticidas mais perigosos, o armazenamento seguro do petróleo de "
      "iluminação e o apoio à saúde mental, dependem de saber que produtos "
      "estão envolvidos, em que idades e com que intenção "
      "{omssuicidio2026,davies2023}."),
    P("Falta, por isso, conhecimento sobre quatro aspectos no HCN: que "
      "agentes causam as intoxicações atendidas e como se distribuem por "
      "idade e sexo; que proporção é autoprovocada, acidental ou infligida "
      "por terceiros; que tratamento, incluindo antídotos, é registado e com "
      "que evolução; e se os antídotos correspondentes aos agentes "
      "encontrados constam da LNME e estiveram disponíveis no hospital. A "
      "ausência de dados moçambicanos publicados sobre estes aspectos e a "
      "qualidade incerta dos registos {miguel2025} obrigam a um estudo "
      "documental que verifique primeiro a qualidade da fonte e só depois a "
      "explore."),
]
PERGUNTA = ("Quais são os agentes envolvidos, o perfil das vítimas, a "
            "intencionalidade, o tratamento e a evolução clínica das "
            "intoxicações agudas atendidas no Banco de Socorros do Hospital "
            "Central de Nampula em 2025 e 2026, e em que medida os antídotos "
            "correspondentes aos agentes encontrados estavam previstos na "
            "lista nacional de medicamentos essenciais e disponíveis no "
            "hospital?")
DELIMITACAO = [
    P("O estudo decorre no Banco de Socorros do HCN, na cidade de Nampula, "
      "entendido como o conjunto das portas de urgência de adultos e de "
      "pediatria que registam atendimentos. A população é constituída pelos "
      "episódios de atendimento por intoxicação aguda, em doentes de "
      "qualquer idade, registados entre 1 de Janeiro de 2025 e 31 de "
      "Dezembro de 2026; a consulta dos arquivos faz-se em 2027. O objecto "
      "de estudo são os agentes, as características das vítimas, a "
      "intencionalidade, o tratamento, a evolução clínica e a "
      "disponibilidade documental dos antídotos."),
    P("Ficam de fora os envenenamentos por animais peçonhentos (mordeduras "
      "de cobra, picadas de escorpião, de abelhas ou de outros insectos), "
      "que seguem um circuito assistencial próprio, com soros "
      "antivenenosos, e já são objecto de estudos específicos em Moçambique "
      "{miguel2025}; as reacções "
      "adversas a medicamentos em dose terapêutica; as intoxicações "
      "crónicas; as toxinfecções alimentares de origem infecciosa; os casos "
      "atendidos apenas noutras unidades sanitárias; e os óbitos ocorridos "
      "antes da chegada ao hospital. O estudo não avalia a qualidade global "
      "da conduta clínica segundo protocolos, nem confirma os agentes por "
      "análise laboratorial, e não inventaria fisicamente os stocks: a "
      "disponibilidade dos antídotos é estudada nos documentos existentes."),
]

# ----------------------------------------------------- 3. objectivos --------
OBJECTIVO_GERAL = (
    "Caracterizar as intoxicações agudas atendidas no Banco de Socorros do "
    "Hospital Central de Nampula entre 1 de Janeiro de 2025 e 31 de Dezembro "
    "de 2026, quanto aos agentes envolvidos, ao perfil das vítimas, à "
    "intencionalidade, ao tratamento e à evolução clínica, e confrontar os "
    "agentes encontrados com a disponibilidade dos antídotos "
    "correspondentes.")
OBJECTIVOS_ESPECIFICOS = [
    "Caracterizar o perfil sociodemográfico das vítimas e as circunstâncias "
    "da exposição, incluindo a via, o local e o tempo decorrido até à "
    "admissão.",
    "Determinar a distribuição dos agentes envolvidos, classificados pela "
    "décima revisão da Classificação Internacional de Doenças (CID-10), "
    "pela classificação Anatómica, Terapêutica e Química (ATC) e "
    "pela classificação de perigosidade dos pesticidas da OMS, e da "
    "intencionalidade da exposição, por grupo etário e sexo.",
    "Descrever o tratamento registado, incluindo a descontaminação e os "
    "antídotos administrados, a gravidade e a evolução clínica dos "
    "episódios (alta, internamento, transferência ou óbito).",
    "Confrontar os agentes encontrados com a inclusão dos antídotos "
    "correspondentes na LNME e com a sua disponibilidade mensal no registo "
    "de existências da farmácia do HCN durante o período do estudo.",
    "Analisar a associação entre o tipo de agente e a intencionalidade e "
    "entre o tipo de agente e a evolução clínica (internamento e óbito).",
]

# ----------------------------------------------------- 4. hipoteses ---------
HIPOTESES_INTRO = [
    P("As hipóteses referem-se à componente analítica do estudo, isto é, ao "
      "objectivo específico 5, e serão testadas com um nível de "
      "significância de 5%. Os objectivos 1 a 4 são descritivos e orientam-se "
      "pelas questões de investigação apresentadas a seguir."),
]
HIPOTESES = [
    ("H0 (intencionalidade)",
     "não existe associação estatisticamente significativa entre o tipo de "
     "agente e a intencionalidade da exposição."),
    ("H1 (intencionalidade)",
     "existe associação estatisticamente significativa entre o tipo de "
     "agente e a intencionalidade da exposição."),
    ("H0 (internamento)",
     "a proporção de episódios que terminam em internamento não difere de "
     "forma estatisticamente significativa entre os tipos de agente."),
    ("H1 (internamento)",
     "a proporção de episódios que terminam em internamento difere de forma "
     "estatisticamente significativa entre os tipos de agente."),
    ("H0 (óbito)",
     "a letalidade não difere de forma estatisticamente significativa entre "
     "os tipos de agente."),
    ("H1 (óbito)",
     "a letalidade difere de forma estatisticamente significativa entre os "
     "tipos de agente."),
]
QUESTOES = [
    "Qual é o perfil etário, por sexo e por proveniência das vítimas de "
    "intoxicação aguda atendidas no HCN, por que via e em que local ocorre a "
    "exposição, e quanto tempo decorre até à admissão?",
    "Que agentes estão envolvidos, com que frequência em cada grupo etário e "
    "com que intencionalidade?",
    "Que descontaminação, que antídotos e que medidas de suporte são "
    "registados, com que gravidade chegam os doentes e como evoluem?",
    "Os antídotos que os agentes encontrados exigem constam da LNME e "
    "estiveram disponíveis na farmácia do HCN em cada mês do período?",
]

# ----------------------------------------------------- 5. justificativa -----
JUSTIFICATIVA_INTRO = [
    P("A escolha do tema responde a uma lacuna concreta: Moçambique tem "
      "uma taxa estimada de mortalidade por intoxicação não intencional "
      "superior, na estimativa pontual, à média africana {omsghomort2024}, "
      "não dispõe de centro antivenenos {omsghopc2023} e não tem estudos "
      "publicados sobre as intoxicações atendidas no maior hospital do norte "
      "do país. Um estudo documental de dois anos, feito "
      "com recursos modestos, pode fornecer ao HCN e ao sector farmacêutico "
      "a informação de base de que hoje carecem."),
]
JUSTIFICATIVA = {
    "cientifica": [
        P("Do ponto de vista científico, o estudo acrescenta dados "
          "moçambicanos a uma literatura africana dominada pela Etiópia, pela "
          "Nigéria e pela África do Sul, onde o perfil dos agentes difere "
          "muito entre países {zgambo2016,mbongwe2020,asrie2024}. Introduz "
          "ainda duas exigências metodológicas raras na literatura regional: "
          "a verificação prévia da qualidade da fonte e a classificação da "
          "intencionalidade por dois classificadores independentes, com "
          "medida da concordância {mchugh2012}."),
    ],
    "academica": [
        P("No plano académico, o trabalho aplica, num problema real, os "
          "conteúdos de toxicologia, farmacologia, farmácia hospitalar e "
          "epidemiologia da Licenciatura em Farmácia da Faculdade de Ciências "
          "de Saúde (FCS) da Universidade Lúrio (UniLúrio), incluindo o uso "
          "de classificações internacionais, a gestão de stocks de "
          "medicamentos essenciais e a análise de dados de rotina segundo as "
          "declarações Strengthening the Reporting of Observational Studies "
          "in Epidemiology (STROBE) e REporting of studies Conducted using "
          "Observational Routinely-collected health Data (RECORD) "
          "{vonelm2007,benchimol2015}. Deixa ainda uma ficha de extracção e "
          "um manual de classificação reutilizáveis em estudos futuros e na "
          "vigilância hospitalar."),
    ],
    "social": [
        P("A relevância social decorre das vítimas. As intoxicações atingem "
          "sobretudo crianças pequenas, por exposição acidental a produtos "
          "guardados em casa {zgambo2016,areprekumor2024}, e adultos jovens, "
          "com predomínio das mulheres, nos actos autoprovocados "
          "{mbongwe2020,laher2022}. Conhecer estes padrões em Nampula "
          "permite dirigir a educação "
          "sobre o armazenamento seguro de pesticidas, de petróleo de "
          "iluminação e de medicamentos e reforçar a articulação entre o "
          "Banco de Socorros e os serviços de saúde mental."),
    ],
    "politica": [
        P("A relevância política prende-se com o medicamento. A LNME "
          "condiciona o que o Serviço Nacional de Saúde adquire e é revista "
          "de três em três anos {misau2023}, e a lista modelo da OMS dedica "
          "uma secção própria aos antídotos {omseml2025}. "
          "Dados sobre os agentes que efectivamente chegam ao HCN e sobre a "
          "disponibilidade dos antídotos correspondentes podem apoiar a "
          "revisão da LNME, a definição de um stock mínimo de antídotos para "
          "os hospitais de referência, à semelhança das listas nacionais "
          "construídas por consenso noutros países {altaweel2022}, e a "
          "discussão sobre a criação de um centro antivenenos nacional "
          "{omspc2020}."),
    ],
}

# ----------------------------------------------------- 6. revisao -----------
REVISAO = [
    ("Conceitos, definições e classificação das intoxicações", [
        P("O estudo distingue a exposição, que é o contacto com uma "
          "substância por ingestão, inalação, via cutânea ou injecção, da "
          "intoxicação, que é a exposição acompanhada de efeitos nocivos, e "
          "considera aguda a "
          "intoxicação resultante de uma exposição única ou de exposições "
          "repetidas num intervalo até 24 horas, por oposição à intoxicação "
          "crónica. A Classificação Internacional de "
          "Doenças (CID) organiza estas situações em dois eixos. Na CID-10, o "
          "capítulo XIX descreve a natureza do dano, com "
          "os blocos T36 a T50, intoxicações por medicamentos e substâncias "
          "biológicas, e T51 a T65, efeitos tóxicos de substâncias de origem "
          "sobretudo não medicinal, como o álcool, os derivados do petróleo, "
          "os corrosivos, os pesticidas e as plantas; o capítulo XX descreve a causa externa e, com ela, a "
          "intenção {omscid10}."),
        P("A intencionalidade é codificada na CID-10 em quatro grupos: "
          "intoxicação acidental (X40 a X49), auto-intoxicação intencional "
          "(X60 a X69), agressão por drogas, medicamentos e outras "
          "substâncias (X85 a X90) e intoxicação de intenção não determinada "
          "(Y10 a Y19) {omscid10}. O mesmo sistema separa as intoxicações dos "
          "efeitos adversos de medicamentos correctamente prescritos e "
          "administrados em dose terapêutica, codificados à parte (Y40 a "
          "Y59). Esta distinção é decisiva para o estudo: uma reacção "
          "adversa à dose habitual é um problema de farmacovigilância, "
          "enquanto a sobredosagem, a toma da substância errada ou a "
          "ingestão deliberada são intoxicações. A CID-11, adoptada em 2019, "
          "está em vigor desde 1 de Janeiro de 2022 {omscid2022}, mas o estudo "
          "codifica os episódios com a CID-10 por duas razões: é a versão "
          "usada pela literatura africana de comparação e não se encontrou "
          "documentação da implantação da CID-11 nos hospitais moçambicanos, "
          "pelo que se presume que o diagnóstico surja em CID-10 ou em texto "
          "livre, o que a verificação prévia confirmará. Os códigos são "
          "atribuídos pelos "
          "classificadores a partir da descrição registada, que é transcrita "
          "e permite a conversão futura para a CID-11."),
        P("A definição operacional adoptada considera intoxicação aguda todo "
          "o episódio de atendimento em que o registo refere a exposição a "
          "uma substância identificada ou suspeita nas 72 horas anteriores, "
          "com sinais atribuídos a essa exposição ou com uma intervenção "
          "dirigida a ela, excluindo as reacções adversas em dose "
          "terapêutica, os animais peçonhentos (T63 e X20 a X27) e as "
          "intoxicações crónicas. Para os medicamentos, o estudo usa a "
          "classificação ATC, que agrupa as substâncias por órgão, acção "
          "terapêutica e estrutura química e reúne os antídotos no grupo "
          "V03AB {whocc2026}; para os pesticidas, a classificação da OMS "
          "por perigosidade, que distribui os princípios activos pelas "
          "classes Ia (extremamente perigoso), Ib (altamente perigoso), II "
          "(moderadamente perigoso), III (ligeiramente perigoso) e U "
          "(improvável que apresente perigo agudo), a partir da dose letal "
          "50 oral e cutânea no rato {omspest2020}."),
    ]),
    ("Magnitude e consequências das intoxicações agudas", [
        P("A mortalidade atribuída às intoxicações não intencionais é mais "
          "alta em África do que na média mundial, e em Moçambique foi "
          "estimada, em 2021, em 1,7 mortes por 100.000 habitantes nos homens "
          "e 1,2 nas mulheres {omsghomort2024}. As intoxicações "
          "intencionais pesam tanto ou mais: o auto-envenenamento com "
          "pesticidas representou pelo menos 13,7% dos suicídios no mundo "
          "entre 2010 e 2014, e a proporção sobe para 19,7% quando se "
          "corrige o sub-registo da Índia {mew2017}."),
        P("Nos hospitais africanos, as intoxicações representam uma fracção "
          "pequena mas exigente da actividade das urgências. No noroeste da "
          "Etiópia corresponderam a 1,1% das 48.619 visitas às urgências "
          "{adinew2017}, e numa urgência pediátrica nigeriana a 0,8% das "
          "admissões {areprekumor2024}. A letalidade hospitalar é, contudo, "
          "muito variável: 0,7% nos auto-envenenamentos de KwaZulu-Natal, "
          "quase todos por medicamentos {pillay2026}, 1,5% no Botswana "
          "{mbongwe2020}, 2,6% "
          "em Lusaka {zgambo2016}, 4,5% nos auto-envenenamentos de "
          "Joanesburgo {laher2022}, 16,7% no leste da Etiópia {nigussie2022}, "
          "17,6% em Amhara {asrie2024} e 20,8% numa pequena série de adultos "
          "do sudoeste da Nigéria {ajeigbe2023}. Estas diferenças reflectem "
          "sobretudo o agente: os organofosforados e os fosfetos metálicos "
          "concentram as mortes e as admissões em cuidados intensivos "
          "{laher2022,asrie2024}."),
        P("As consequências ultrapassam o episódio agudo. As intoxicações "
          "graves por organofosforados exigiram ventilação mecânica em 99,2% "
          "dos doentes admitidos em cuidados intensivos ou intermédios num "
          "hospital de Joanesburgo, com estadia média de 6,8 dias na unidade "
          "de cuidados intensivos (UCI) {bruins2019}. Nos actos autoprovocados, o episódio é também um "
          "marcador de risco de suicídio que só é aproveitado se o hospital "
          "encaminhar o doente para apoio psicológico e psiquiátrico "
          "{omssuicidio2026}. Em Moçambique, a mortalidade por suicídio é "
          "descrita como das mais elevadas de África, e na Beira as mulheres "
          "recorrem mais a substâncias tóxicas, enquanto os homens morrem "
          "mais por métodos de maior letalidade {wagenaar2016}."),
    ]),
    ("Agentes envolvidos e factores associados", [
        P("Os medicamentos são o principal agente nos países de rendimento "
          "médio da África Austral: metade dos casos no Botswana, com o "
          "paracetamol à cabeça {mbongwe2020}, e 81% dos auto-envenenamentos "
          "num hospital de KwaZulu-Natal, onde os anti-retrovirais surgiram em 16,8% dos "
          "casos, quase tanto como o paracetamol (17,6%) {pillay2026}. Os "
          "pesticidas dominam "
          "nos contextos agrícolas: 57% em Lusaka {zgambo2016}, 41,5% de "
          "organofosforados entre adultos no sudoeste da Nigéria, com o "
          "paraquate associado a letalidade elevada {ajeigbe2023}, e "
          "organofosforados e fosfetos metálicos em Amhara, obtidos em casa "
          "em 55% dos casos e comprados em lojas locais em 36% {asrie2024}. "
          "Na Cidade do Cabo, o terbufos, um pesticida agrícola altamente "
          "perigoso vendido ilegalmente para uso doméstico, foi a substância "
          "mais detectada nas mortes de crianças e adolescentes "
          "{davies2023}."),
        P("O petróleo de iluminação e os outros derivados do petróleo são o "
          "agente típico das crianças pequenas. Na urgência pediátrica de "
          "Yenagoa, o querosene esteve em 20,3% das intoxicações e foi a "
          "principal causa das mortes, que atingiram 8,7% das crianças "
          "{areprekumor2024}. O mecanismo é conhecido: o produto é guardado "
          "em garrafas ou recipientes de fácil acesso, e a aspiração provoca "
          "pneumonite química {tenenbaum2021}. Entre os outros produtos "
          "domésticos, a lixívia foi o segundo agente no noroeste da Etiópia, "
          "com 25% dos casos {adinew2017}, e os produtos de uso doméstico "
          "representaram 22% das admissões no Botswana {mbongwe2020}."),
        P("As plantas, as preparações tradicionais e as bebidas alcoólicas "
          "artesanais formam um grupo mal estudado. No surto de Chitima, em "
          "Tete, a investigação analisou plantas medicinais locais e "
          "pesticidas comerciais antes de identificar o ácido bongcréquico e "
          "a *Burkholderia gladioli* na farinha da bebida {gudo2018}. As intoxicações por metanol em bebidas "
          "adulteradas causaram letalidades de 21% e 29% em dois surtos "
          "quenianos de 2014, e o atraso no reconhecimento foi o principal "
          "obstáculo {rostrup2016}. O álcool surge também isoladamente, como "
          "em 9,5% dos adultos intoxicados no estudo nigeriano "
          "{ajeigbe2023}."),
        P("Os factores associados repetem-se entre estudos. A idade separa "
          "dois padrões: nas crianças predominam as exposições acidentais, "
          "que em Lusaka foram 65% dos casos abaixo dos 13 anos {zgambo2016}; "
          "nos adolescentes e adultos jovens predominam os actos "
          "autoprovocados, mais frequentes nas mulheres, que no Botswana "
          "tiveram odds de intoxicação intencional 4,53 vezes superiores às "
          "dos homens, após ajustamento {mbongwe2020}. A residência rural associou-se a "
          "maior mortalidade nas crianças etíopes {molla2022}, e o atraso na "
          "chegada ao hospital, superior a duas horas em 68,1% das crianças "
          "nigerianas, é comum {areprekumor2024}. A intoxicação autoprovocada "
          "e a intoxicação por medicamentos associaram-se a pior desfecho no "
          "leste da Etiópia {nigussie2022}."),
    ]),
    ("Tratamento, antídotos e preparação hospitalar", [
        P("O tratamento das intoxicações agudas assenta no suporte das "
          "funções vitais, na descontaminação e, quando existe, no antídoto "
          "específico. A lista modelo de "
          "medicamentos essenciais da OMS de 2025 reúne numa secção própria o "
          "carvão activado, como agente não específico, nove antídotos "
          "específicos, entre os quais a acetilcisteína, a atropina, a "
          "naloxona e o azul de metileno, e cinco antídotos na lista "
          "complementar; a imunoglobulina antiveneno e a fitomenadiona "
          "figuram noutras secções {omseml2025}."),
        P("A disponibilidade destes medicamentos é um problema mundial. Um "
          "painel de peritos de várias especialidades considerou 45 antídotos, "
          "recomendou 44 e fixou para 23 a disponibilidade imediata e para 14 "
          "a disponibilidade no prazo de uma hora {dart2018}. No Reino Unido, "
          "só 10,1% dos hospitais cumpriam simultaneamente as recomendações "
          "para os antídotos de uso imediato e de uso na primeira hora "
          "{harnett2021}. Em Campinas, no Brasil, nenhum dos 14 serviços de "
          "urgência tinha todos os antídotos recomendados e, nos 10 "
          "hospitais, só um quarto dos antídotos existia em quantidade "
          "suficiente para 24 horas de tratamento {rodrigues2017}. A resposta proposta nesses contextos "
          "foi a construção de listas nacionais de antídotos essenciais por "
          "consenso, como a lista de 43 antídotos do Kuwait, e a "
          "monitorização contínua da incidência local de intoxicações "
          "{altaweel2022}."),
        P("Nos hospitais africanos, os dados de utilização sugerem que o "
          "problema é mais grave. Em Amhara, a atropina foi o único antídoto "
          "usado {asrie2024}; no leste da Etiópia, 30 dos 150 doentes "
          "receberam antídoto, 18 deles atropina {nigussie2022}. Nos hospitais "
          "centrais moçambicanos, os medicamentos para intoxicações em falta "
          "incluíam a difenidramina, a neostigmina e um antídoto para a "
          "exposição ao chumbo {amado2023}. Faltam, porém, estudos que cruzem, no mesmo "
          "hospital, os agentes encontrados com os antídotos disponíveis."),
    ]),
    ("Enquadramento normativo e institucional em Moçambique", [
        P("A LNME em vigor foi aprovada pelo Ministério da Saúde (MISAU) "
          "através do Diploma Ministerial n.º 52/2023, de 19 de Abril, que "
          "revogou a lista de 2016, determina que o "
          "Serviço Nacional de Saúde adquira apenas os medicamentos nela "
          "incluídos, com excepção dos medicamentos de especialidade "
          "avaliados caso a caso, e atribui à Autoridade Nacional Reguladora "
          "de Medicamento a sua actualização trienal, ouvida a comissão de "
          "revisão {misau2023}. O capítulo dos antídotos da lista de "
          "medicamentos essenciais inclui a acetilcisteína, o carvão "
          "activado, o azul de metileno, o flumazenil, o fomepizol, o azul "
          "da Prússia, a naloxona e o sulfato de protamina; a lista de "
          "medicamentos de especialidade acrescenta, entre outros, a "
          "pralidoxima, o glicopirrolato, o nitrito e o tiossulfato de "
          "sódio, o dimercaprol, o edetato de cálcio, a penicilamina e a "
          "desferroxamina. A atropina injectável figura entre os adjuvantes "
          "da anestesia, o soro antiofídico polivalente entre os "
          "imunológicos e a fitomenadiona no capítulo das vitaminas "
          "{misau2023}."),
        P("As orientações da OMS descrevem os centros antivenenos como fontes de conhecimento toxicológico "
          "especializado para os profissionais e como parte da capacidade de "
          "vigilância e resposta a eventos químicos exigida pelo Regulamento "
          "Sanitário Internacional {omspc2020}. Na ausência de um centro "
          "nacional, a "
          "informação sobre intoxicações fica dispersa pelos livros de "
          "registo das unidades sanitárias, e não se encontrou documentação "
          "pública de um sistema nacional de notificação específico para as "
          "intoxicações."),
        P("Dois outros instrumentos enquadram o estudo. A OMS coloca a "
          "limitação do acesso aos meios de suicídio, "
          "com destaque para os pesticidas e certos medicamentos, entre as "
          "intervenções prioritárias {omssuicidio2026}, e a classificação de "
          "perigosidade dos pesticidas da OMS é a referência para "
          "identificar os produtos cuja restrição traria mais benefício "
          "{omspest2020}. No plano ético e legal, a Lei n.º 3/2023, de 8 de "
          "Junho, regula a investigação em saúde humana em Moçambique "
          "{lei3de2023} e aplica-se aos estudos com dados de processos "
          "clínicos."),
    ]),
    ("Métodos de medida nos estudos documentais de intoxicações", [
        P("Os estudos retrospectivos de intoxicações dependem da qualidade "
          "dos registos, e a literatura africana mostra perdas "
          "consideráveis. No noroeste da Etiópia, só 344 dos 543 casos "
          "registados (63,4%) tinham dados completos {adinew2017}; no leste "
          "do mesmo país, 150 dos 175 processos revistos puderam ser "
          "analisados {nigussie2022}; e na Zambézia os livros de registo das "
          "mordeduras de cobra não documentavam o tempo até aos cuidados, o "
          "tratamento, a evolução nem a espécie {miguel2025}. Estas perdas "
          "justificam a verificação prévia da fonte adoptada neste "
          "protocolo."),
        P("A gravidade é graduada, nos estudos de toxicologia clínica, pela "
          "Poisoning Severity Score (PSS), desenvolvida com o Programa "
          "Internacional de Segurança Química, que classifica cada caso em "
          "cinco graus, de 0 a 4 (nenhuma, ligeira, moderada, grave e fatal), "
          "pela manifestação mais grave observada {persson1998}. A escala foi "
          "testada por 14 centros sobre os processos clínicos de 371 casos, "
          "com concordância aceitável em 80% ou mais dos casos, e pode "
          "aplicar-se à admissão ou ao longo do episódio, desde que o momento "
          "seja declarado {persson1998}; a aplicação retrospectiva é, pois, "
          "possível, mas só quando o registo descreve as manifestações "
          "clínicas. "
          "Como a atribuição da gravidade e da intencionalidade a partir de "
          "um registo envolve julgamento, a concordância entre "
          "classificadores deve ser medida pelo kappa de Cohen, que corrige "
          "o acordo esperado pelo acaso; a interpretação que aceita valores "
          "de 0,41 é considerada demasiado permissiva em estudos de saúde "
          "{mchugh2012}."),
        P("Na análise, os estudos africanos combinam a descrição de "
          "frequências com testes do qui-quadrado e regressão logística "
          "{nigussie2022,asrie2024,pillay2026}, mas os resumos não informam "
          "se o número de eventos bastava para os modelos ajustados. A regra de pelo "
          "menos 10 eventos por parâmetro, derivada de estudos de simulação, "
          "protege contra estimativas enviesadas e intervalos de confiança "
          "enganadores {peduzzi1996}, e é particularmente restritiva quando o "
          "desfecho é o óbito. O relato destes estudos segue a declaração "
          "STROBE {vonelm2007} e a sua extensão RECORD, uma lista de 13 itens para os estudos que usam "
          "dados recolhidos por rotina com fins administrativos e clínicos, "
          "sem objectivos de investigação definidos à partida "
          "{benchimol2015}."),
    ]),
]

# ----------------------------------------------------- 7. estado da arte ----
ESTADO_ARTE = [
    P("O [[quadro:estado_arte]] sintetiza os estudos empíricos mais próximos "
      "do objecto deste protocolo publicados nos últimos dez anos, com "
      "prioridade para os hospitalares da África subsariana e para os "
      "moçambicanos."),
    QUADRO("estado_arte",
           "Síntese de estudos sobre intoxicações agudas em hospitais "
           "africanos (estado da arte)",
           ["Autor (ano)", "Local", "Desenho (n)", "Principais resultados"],
           [
               ["Z'gambo et al. (2016) {zgambo2016}", "Lusaka, Zâmbia",
                "Transversal retrospectivo, 2 hospitais (873)",
                "Pesticidas 57%, medicamentos 13%; 36% dos casos entre 0 e "
                "12 anos; 65% acidentais abaixo dos 13 anos; letalidade de "
                "2,6 por 100 casos."],
               ["Adinew et al. (2017) {adinew2017}", "Noroeste da Etiópia",
                "Retrospectivo, 3 urgências (344 de 543 registados)",
                "Dados completos em 63,4%; 1,1% das visitas às urgências; "
                "60% mulheres; organofosforados 35%, lixívia 25%; atropina "
                "em 45,5% dos organofosforados."],
               ["Wagenaar et al. (2016) {wagenaar2016}",
                "Beira, Moçambique",
                "Retrospectivo, consultas psiquiátricas (898) e autópsias "
                "(1.173)",
                "Tentativas de suicídio em 18,0% das consultas, 68,3% em "
                "mulheres; veneno para ratos em 66% das tentativas."],
               ["Gudo et al. (2018) {gudo2018}", "Chitima, Moçambique",
                "Investigação de surto (234)",
                "Bebida tradicional contaminada; 75 óbitos (32%); ácido "
                "bongcréquico e *Burkholderia gladioli* identificados."],
               ["Bruins et al. (2019) {bruins2019}",
                "Joanesburgo, África do Sul",
                "Retrospectivo em cuidados intensivos e intermédios (129)",
                "Organofosforados; 68,2% homens; ventilação em 99,2%; "
                "letalidade de 5,4%."],
               ["Mbongwe et al. (2020) {mbongwe2020}",
                "Gaborone, Botswana", "Retrospectivo, 6 anos (408)",
                "53% intencionais; medicamentos 50%, produtos domésticos "
                "22%; paracetamol 30% dos medicamentos; letalidade de 1,5%."],
               ["Laher et al. (2022) {laher2022}",
                "Joanesburgo, África do Sul",
                "Transversal retrospectivo, 12 meses (288)",
                "Auto-envenenamento; 62,8% mulheres; organofosforados e "
                "carbamatos 25,3%, com 69,2% dos óbitos; letalidade de 4,5%."],
               ["Nigussie et al. (2022) {nigussie2022}", "Harar, Etiópia",
                "Transversal retrospectivo, 5 anos (150 de 175)",
                "Organofosforados em 62 casos; antídoto em 30 doentes; "
                "letalidade de 16,7%; auto-intoxicação com OR de 2,44 para "
                "pior desfecho."],
               ["Molla et al. (2022) {molla2022}", "Gondar, Etiópia",
                "Retrospectivo pediátrico, 4 anos (82)",
                "Veneno animal 26,8%; via oral 70,7%; 65,9% de origem "
                "rural; morte mais provável na residência rural (OR "
                "ajustado de 2,9)."],
               ["Davies et al. (2023) {davies2023}",
                "Cidade do Cabo, África do Sul",
                "Retrospectivo de autópsias, 10 anos (54)",
                "Terbufos em 29 mortes; pesticidas agrícolas vendidos "
                "ilegalmente; 42,6% abaixo dos 5 anos."],
               ["Ajeigbe et al. (2023) {ajeigbe2023}", "Sudoeste da Nigéria",
                "Retrospectivo de adultos, 5 anos (53)",
                "Organofosforados 41,5%, paraquate 11,3%, álcool 9,5%; "
                "letalidade de 20,8%."],
               ["Areprekumor et al. (2024) {areprekumor2024}",
                "Yenagoa, Nigéria",
                "Transversal retrospectivo pediátrico, 10 anos (69)",
                "Organofosforados 21,7%, querosene 20,3%; 72,5% acidentais; "
                "atraso superior a 2 horas em 68,1%; antídotos em 15,9%; "
                "letalidade de 8,7%."],
               ["Asrie et al. (2024) {asrie2024}", "Amhara, Etiópia",
                "Prospectivo multicêntrico, 1 ano (442)",
                "Organofosforados 32,8%, fosfetos metálicos 26,0%; origem "
                "doméstica 55%; atropina único antídoto; letalidade de "
                "17,6%."],
               ["Pillay (2026) {pillay2026}", "KwaZulu-Natal, África do Sul",
                "Retrospectivo, 1 hospital terciário, 6 anos (716)",
                "Medicamentos 81%, paracetamol 17,6%, anti-retrovirais "
                "16,8%; 64,7% mulheres; letalidade de 0,7%."],
           ],
           larguras=[3.4, 2.6, 3.4, 6.6],
           fonte="Elaboração própria (2026), a partir das fontes citadas.",
           nota="OR: odds ratio."),
    P("A leitura do quadro revela um padrão recorrente e uma divergência. "
      "O padrão é a dupla distribuição etária, com exposições acidentais nas "
      "crianças pequenas e actos autoprovocados nos adultos jovens, sobretudo "
      "mulheres, e a concentração da letalidade nos pesticidas "
      "anticolinesterásicos, nos fosfetos e no paraquate. A divergência está "
      "no agente dominante, que passa dos pesticidas, na Zâmbia, na Etiópia "
      "e na Nigéria, para os medicamentos, no Botswana e em KwaZulu-Natal, o "
      "que impede transpor para Nampula as prioridades de outro país. Os "
      "estudos também divergem na forma de classificar os agentes e a "
      "intencionalidade: os resumos raramente indicam o sistema de "
      "classificação usado, nenhum refere a medida da concordância entre "
      "classificadores e alguns incluem os envenenamentos por animais "
      "{zgambo2016,molla2022}, que este protocolo exclui."),
    P("A lacuna é dupla. Não se encontraram estudos hospitalares de "
      "intoxicações agudas no norte de Moçambique, e os dois estudos "
      "moçambicanos disponíveis tratam de um subgrupo, as tentativas de "
      "suicídio {wagenaar2016}, e de um surto {gudo2018}. Além disso, nenhum "
      "dos estudos africanos identificados confronta os agentes com a "
      "disponibilidade dos antídotos no mesmo hospital, embora um aponte "
      "essa disponibilidade como obstáculo {areprekumor2024} e outro registe "
      "a atropina como único antídoto usado {asrie2024}. O presente estudo preenche as "
      "duas lacunas, com classificações citáveis, medida de concordância e "
      "verificação documental dos antídotos."),
]
ESQUEMA_TEXTO = [
    P("A [[figura:esquema]] representa o modelo que orienta o estudo. As "
      "características da vítima e da exposição determinam o agente e a "
      "intencionalidade; o acesso aos cuidados e a resposta do hospital, "
      "incluindo a disponibilidade e a administração do antídoto, medeiam a "
      "evolução clínica, que é o desfecho. A idade, o sexo, o tempo até à "
      "admissão e a referência de outra unidade funcionam como variáveis de "
      "confundimento nas associações do objectivo específico 5; a gravidade "
      "à chegada é descrita, mas não entra nos modelos, porque se situa no "
      "caminho entre o agente e a evolução."),
]
ESQUEMA_TITULO = ("Esquema conceptual das intoxicações agudas atendidas no "
                  "Banco de Socorros do HCN")
ESQUEMA = {
    "contexto": "Banco de Socorros do HCN, episódios de 2025 e 2026",
    "blocos": [
        ("Características da vítima", ["idade e sexo", "proveniência",
                                       "antecedentes psiquiátricos"]),
        ("Características da exposição", ["agente (CID-10, ATC, classe OMS)",
                                          "via e local",
                                          "intencionalidade"]),
        ("Acesso e resposta do hospital", ["tempo até à admissão",
                                           "descontaminação",
                                           "antídoto e sua disponibilidade"]),
    ],
    "desfecho": ("Evolução clínica", ["alta do Banco de Socorros",
                                      "internamento", "transferência",
                                      "óbito"]),
    "moderadores": ("Variáveis de confundimento", ["idade", "sexo",
                                                   "tempo até à admissão",
                                                   "referência de outra "
                                                   "unidade"]),
}

# ----------------------------------------------------- 8. metodologia -------
METODOLOGIA = [
    ("Tipo e desenho do estudo", [
        P("Trata-se de um estudo observacional, descritivo e analítico, "
          "retrospectivo, de base documental e abordagem quantitativa. A "
          "componente descritiva responde aos objectivos específicos 1 a 4 e "
          "a componente analítica ao objectivo 5. O desenho retrospectivo foi escolhido por três "
          "razões: permite reunir em poucos meses dois anos de episódios, o "
          "que é necessário porque as intoxicações representam uma fracção "
          "pequena dos atendimentos urgentes {adinew2017} e os agentes mais "
          "letais são ainda mais raros; não interfere com a prática clínica "
          "nem altera o registo; e é exequível com os recursos de um trabalho "
          "de licenciatura. A contrapartida é a dependência da qualidade dos "
          "registos, tratada pela verificação prévia da fonte, pela dupla "
          "extracção e pela classificação independente. O relato seguirá as "
          "declarações STROBE e RECORD {vonelm2007,benchimol2015}, incluindo "
          "o diagrama de fluxo dos episódios identificados, excluídos, "
          "perdidos e analisados."),
    ]),
    ("Local e período do estudo", [
        P("O estudo realiza-se no HCN, na cidade de Nampula, hospital de "
          "referência da região norte {amado2023}. Envolve o Banco de "
          "Socorros, com as suas portas de urgência de adultos e de "
          "pediatria, o arquivo clínico, os serviços de internamento que "
          "recebem os intoxicados (medicina, pediatria e UCI), o registo de "
          "óbitos e a farmácia hospitalar. A forma como os atendimentos "
          "urgentes de adultos e de crianças são registados, num único livro "
          "ou em livros separados, será confirmada antes da recolha "
          "[confirmar junto da direcção clínica do HCN]."),
        P("O período de referência dos dados vai de 1 de Janeiro de 2025 a 31 "
          "de Dezembro de 2026. Optou-se por dois anos porque o volume anual "
          "de intoxicações no HCN não é conhecido e, com as frequências "
          "descritas noutros hospitais africanos, um só ano poderia não "
          "fornecer episódios suficientes para estimar a letalidade por "
          "agente e para as comparações do objectivo 5; dois anos cobrem "
          "também duas estações chuvosas e duas campanhas agrícolas, com as "
          "suas variações no uso de pesticidas. A verificação prévia decorre "
          "em Fevereiro de 2027, em episódios de 2024, e a consulta dos "
          "arquivos entre Março e Maio de 2027, depois da aprovação ética e "
          "das autorizações institucionais."),
    ]),
    ("População, unidade de análise e fontes documentais", [
        P("A população-alvo são as pessoas com intoxicação aguda atendidas no "
          "HCN; a população de estudo são os episódios de atendimento por "
          "intoxicação aguda registados no Banco de Socorros no período de "
          "referência. A unidade de análise é o episódio de atendimento, "
          "definido como o conjunto dos cuidados prestados desde a chegada ao "
          "Banco de Socorros até ao fim do contacto com o hospital, que pode "
          "ser a alta do Banco de Socorros, a alta do internamento, a "
          "transferência para outra unidade, o abandono ou o óbito."),
        P("Os registos múltiplos seguem regras fixadas à partida. O regresso "
          "ao Banco de Socorros nas 72 horas seguintes à alta, com queixas "
          "atribuídas à mesma exposição, é integrado no episódio original, "
          "que assume a evolução do último contacto. Uma nova exposição da "
          "mesma pessoa, com data ou agente diferentes, constitui um novo "
          "episódio, assinalado como repetido através da lista-chave guardada "
          "em separado, o que permite uma análise de sensibilidade restrita "
          "ao primeiro episódio de cada pessoa. Os doentes referidos de outra "
          "unidade sanitária são incluídos, sendo o episódio o atendimento no "
          "HCN, com registo da proveniência e dos tratamentos anteriores. A "
          "passagem para uma enfermaria ou para a UCI conta como internamento "
          "e o processo é seguido até ao fim; a transferência para outra "
          "unidade sanitária é um desfecho próprio. Os doentes que chegam sem "
          "vida, sem qualquer atendimento, não entram no estudo; os óbitos "
          "ocorridos no Banco de Socorros entram."),
        P("As fontes documentais são o livro ou livros de registo do Banco de "
          "Socorros, que constituem a base de identificação e fornecem a "
          "data, a idade, o sexo, a proveniência, o diagnóstico e o destino; "
          "a ficha de urgência e o processo clínico, com a história, o "
          "agente, as horas da exposição e da chegada, os sinais, o "
          "tratamento e a evolução; os livros de admissão das enfermarias e "
          "da UCI e o registo de óbitos, usados para completar a evolução e "
          "para encontrar episódios não identificados no livro do Banco de "
          "Socorros; e as guias de transferência. Para o objectivo 4, as "
          "fontes são o texto da LNME {misau2023} e os registos de "
          "existências da farmácia do HCN (fichas de existências em papel ou "
          "registos informáticos de movimento de stock) de cada antídoto, "
          "nos 24 meses do período."),
    ]),
    ("Amostra e cálculo do tamanho da amostra", [
        H3("Censo e regra de amostragem sistemática"),
        P("O número de episódios de intoxicação aguda atendidos no HCN nos "
          "dois anos (N) não está publicado e será obtido na fase de "
          "identificação dos casos [confirmar junto da direcção clínica do "
          "HCN]. Os hospitais africanos descrevem volumes muito díspares, de "
          "873 casos num ano em dois hospitais de Lusaka {zgambo2016} a 175 "
          "em cinco anos em Harar "
          "{nigussie2022}, pelo que se adopta o censo de todos os episódios "
          "elegíveis dos dois anos, com uma regra alternativa para o caso de "
          "o número exceder o exequível."),
        P("O limite de exequibilidade foi fixado em 700 processos, "
          "correspondentes a cerca de 60 dias úteis de recolha por dois "
          "extractores, a seis processos por dia e por extractor, tempo que "
          "inclui a procura no arquivo e será confirmado na verificação "
          "prévia. Se o total de episódios elegíveis for igual ou inferior a "
          "700, todos são incluídos. Se for superior, seleccionam-se 700 por "
          "amostragem sistemática, com intervalo k = N/700 (fraccionário "
          "quando necessário) e início aleatório entre 1 e k, sobre a lista "
          "ordenada pela data e hora do atendimento, o que distribui a "
          "amostra pelos 24 meses e preserva a sazonalidade. Prevê-se uma "
          "perda de 15% por processos não localizados ou sem os dados "
          "mínimos, próxima dos 14,3% de processos excluídos por informação "
          "incompleta no leste da Etiópia {nigussie2022}, embora no noroeste "
          "do mesmo país tenha chegado a 36,6% {adinew2017}; a verificação "
          "prévia dará a estimativa local. Com 15%, o número de episódios "
          "analisáveis será cerca de 0,85 vezes o número seleccionado."),
        H3("Precisão esperada das proporções principais"),
        P("A precisão com que o estudo estima as proporções principais, como "
          "a proporção de cada categoria de agente, de actos autoprovocados "
          "ou de internamentos, é dada pela semi-amplitude do intervalo de "
          "confiança a 95% (IC95%):"),
        FORMULA("d = Z × √[p × (1 - p) / n]"),
        P("em que Z = 1,96, p é a proporção esperada e n o número de "
          "episódios analisáveis. Para o pior caso, p = 0,50, e para o "
          "cenário de 700 episódios seleccionados (595 analisáveis), a "
          "substituição dá:"),
        FORMULA("d = 1,96 × √(0,50 × 0,50 / 595) = 1,96 × 0,0205 = 0,040, "
                "ou seja, ±4,0 pontos percentuais"),
        P("A [[tabela:cenarios]] apresenta a precisão para as proporções de "
          "50% e 20% e o intervalo exacto de Clopper-Pearson para uma "
          "letalidade de cerca de 5%, em seis cenários de N. Não se aplica a "
          "correcção para população finita: no censo, o intervalo exprime a "
          "incerteza sobre o processo que gera as intoxicações, e nos "
          "cenários com amostragem a omissão torna os intervalos "
          "conservadores. Com 425 ou mais episódios analisáveis, qualquer "
          "proporção é estimada com precisão de ±4,8 pontos ou melhor; no "
          "cenário de 100 episódios, a precisão de ±10,6 pontos só serve as "
          "proporções globais, e as análises por grupo etário usarão "
          "categorias mais largas."),
        TABELA("cenarios",
               "Cenários de aplicação do plano de amostragem e precisão "
               "esperada segundo o número de episódios elegíveis em dois "
               "anos (N)",
               ["N em dois anos", "Estratégia", "Seleccionados / "
                "analisáveis", "Semi-amplitude para p = 50%",
                "Semi-amplitude para p = 20%",
                "IC95% exacto para letalidade de cerca de 5%"],
               [["100", "Censo", "100 / 85", "±10,6", "±8,5",
                 "4/85: 1,3 a 11,6%"],
                ["250", "Censo", "250 / 212", "±6,7", "±5,4",
                 "11/212: 2,6 a 9,1%"],
                ["500", "Censo", "500 / 425", "±4,8", "±3,8",
                 "21/425: 3,1 a 7,5%"],
                ["700", "Censo", "700 / 595", "±4,0", "±3,2",
                 "30/595: 3,4 a 7,1%"],
                ["1.000", "Sistemática, k = 1,43", "700 / 595", "±4,0",
                 "±3,2", "30/595: 3,4 a 7,1%"],
                ["2.000", "Sistemática, k = 2,86", "700 / 595", "±4,0",
                 "±3,2", "30/595: 3,4 a 7,1%"]],
               larguras=[2.2, 2.9, 2.6, 2.6, 2.6, 3.1],
               fonte="Elaboração própria (2026).",
               nota=("Semi-amplitudes em pontos percentuais, sem correcção "
                     "para população finita. Os valores de N são cenários "
                     "de planeamento; o valor real será obtido nos livros de "
                     "registo.")),
        H3("Poder para a componente analítica (objectivo específico 5)"),
        P("As associações do objectivo 5 comparam proporções entre tipos de "
          "agente. Para avaliar o poder, toma-se a comparação entre os dois "
          "grupos de agentes mais frequentes, com a fórmula para duas "
          "proporções independentes, nível de significância de 5% "
          "(Z<sub>α/2</sub> = 1,96) e poder de 80% (Z<sub>β</sub> = 0,8416):"),
        FORMULA("n por grupo = [Z<sub>α/2</sub> × √(2 × p<sub>m</sub> × "
                "(1 - p<sub>m</sub>)) + Z<sub>β</sub> × √(p<sub>1</sub> × "
                "(1 - p<sub>1</sub>) + p<sub>2</sub> × (1 - p<sub>2</sub>))]"
                "<sup>2</sup> / (p<sub>1</sub> - p<sub>2</sub>)<sup>2</sup>"),
        P("em que p<sub>m</sub> é a média das duas proporções. Fixa-se como "
          "diferença mínima com relevância prática, para a intencionalidade "
          "e para o internamento, 20 pontos percentuais. Como não há dados "
          "locais sobre as proporções de partida, usa-se o cenário mais "
          "exigente para essa diferença, centrado em 50% (p<sub>1</sub> = "
          "0,40 e p<sub>2</sub> = 0,60; p<sub>m</sub> = 0,50), em que a "
          "variância é máxima. A substituição dá:"),
        FORMULA("n = [1,96 × √(2 × 0,50 × 0,50) + 0,8416 × √(0,40 × 0,60 + "
                "0,60 × 0,40)]<sup>2</sup> / 0,20<sup>2</sup> = (1,3859 + "
                "0,5831)<sup>2</sup> / 0,04 = 96,9, ou seja, 97 por grupo"),
        P("Com 425 episódios analisáveis, cada um dos dois grupos comparados "
          "terá de reunir pelo menos 22,8% dos casos (97/425) e, com 595, "
          "pelo menos 16,3% (97/595); abaixo destes valores, o poder para "
          "esta diferença será inferior a 80%, o que será declarado. Para o "
          "óbito, toma-se uma letalidade de 5%, próxima das descritas em "
          "Lusaka e Joanesburgo {zgambo2016,laher2022}, e outra de 15%, "
          "próxima das observadas nos hospitais etíopes onde predominam os "
          "organofosforados e os fosfetos metálicos {nigussie2022,asrie2024}; "
          "detectar essa diferença exigiria:"),
        FORMULA("n = [1,96 × √(2 × 0,10 × 0,90) + 0,8416 × √(0,05 × 0,95 + "
                "0,15 × 0,85)]<sup>2</sup> / 0,10<sup>2</sup> = (0,8316 + "
                "0,3521)<sup>2</sup> / 0,01 = 140,1, ou seja, 141 por grupo"),
        P("Mesmo no cenário máximo, só os dois grupos de agentes mais "
          "frequentes poderão aproximar-se de 141 episódios cada, e o número "
          "de óbitos será provavelmente pequeno, pelo que o poder para "
          "comparar a letalidade será limitado. Essa limitação será "
          "declarada: a letalidade por agente será apresentada com IC95% "
          "exactos e comparada pelo teste exacto de Fisher, com leitura "
          "exploratória."),
        P("A regressão logística só será ajustada quando houver pelo menos "
          "10 eventos por parâmetro na categoria menos frequente do desfecho "
          "{peduzzi1996}. Para o internamento, o modelo completo prevê dez "
          "parâmetros: tipo de agente em cinco categorias (medicamentos, "
          "pesticidas, derivados do petróleo, outros produtos domésticos e "
          "restantes agrupados; quatro parâmetros), grupo etário em três "
          "(menos de 15, 15 a 24 e 25 ou mais anos; dois parâmetros), sexo, "
          "intencionalidade autoprovocada, tempo até à admissão superior a "
          "seis horas e referência de outra unidade. Exige, por isso, pelo "
          "menos 100 eventos; com 50 a 99, usa-se um modelo reduzido a cinco "
          "parâmetros (medicamentos, pesticidas e outros; menos de 15 e 15 ou "
          "mais anos; sexo; intencionalidade); com menos de 50, a análise "
          "fica pela comparação bivariada. O modelo da intencionalidade "
          "autoprovocada inclui o tipo de agente, o grupo etário e o sexo "
          "(sete parâmetros, pelo menos 70 eventos). Para o óbito não se "
          "ajustará nenhum modelo multivariável se houver menos de 10 óbitos "
          "por parâmetro."),
    ]),
    ("Critérios de inclusão e de exclusão", [
        H3("Critérios de inclusão"),
        LISTA([
            "Episódio registado no Banco de Socorros do HCN, na urgência de "
            "adultos ou de pediatria, entre 1 de Janeiro de 2025 e 31 de "
            "Dezembro de 2026.",
            "Diagnóstico registado ou história clínica que refira exposição "
            "aguda, nas 72 horas anteriores à chegada, a um medicamento, "
            "pesticida, derivado do petróleo, outro produto doméstico, planta "
            "ou preparação tradicional, bebida alcoólica, gás ou outra "
            "substância química, identificado ou suspeito.",
            "Presença de sinais ou sintomas atribuídos à exposição ou de uma "
            "intervenção dirigida a ela (descontaminação, antídoto ou "
            "vigilância motivada pela exposição).",
            "Intoxicação alcoólica aguda quando for o motivo registado do "
            "atendimento ou quando o álcool for ingerido com outro agente.",
            "Doentes de qualquer idade e sexo, residentes ou não na cidade de "
            "Nampula, incluindo os referidos de outras unidades sanitárias.",
        ]),
        H3("Critérios de exclusão"),
        LISTA([
            "Envenenamento por animais peçonhentos (mordeduras de cobra, "
            "picadas de escorpião, de abelhas ou de outros insectos; T63 e "
            "X20 a X27 da CID-10).",
            "Reacção adversa ou alérgica a medicamento administrado em dose "
            "terapêutica, sem sobredosagem nem erro de substância.",
            "Intoxicação crónica ou exposição sem episódio agudo nas 72 horas "
            "anteriores.",
            "Toxinfecção alimentar de origem infecciosa, sem suspeita de "
            "substância tóxica.",
            "Álcool como achado acessório num doente atendido por outro "
            "motivo, como traumatismo.",
            "Doente que chega sem vida e sem qualquer atendimento.",
            "Reatendimento pela mesma exposição nas 72 horas seguintes à alta, "
            "que é integrado no episódio original.",
        ]),
        P("Os episódios elegíveis cujo processo não seja localizado após duas "
          "procuras em dias diferentes, ou que não tenham registo do agente e "
          "da evolução, não são excluídos em silêncio: contam como perdas, "
          "são descritos pela idade, pelo sexo e pelo agente constantes do "
          "livro e comparados com os episódios analisados."),
    ]),
    ("Variáveis e definições operacionais", [
        P("O [[quadro:variaveis]] apresenta as variáveis, o seu tipo, as "
          "definições operacionais e o objectivo específico a que "
          "respondem. O [[quadro:agentes]] define as categorias de agente "
          "com os códigos da CID-10 {omscid10}, a classificação ATC para os "
          "medicamentos {whocc2026} e a classificação de perigosidade para "
          "os pesticidas {omspest2020}; o [[quadro:intencao]] define as "
          "categorias de intencionalidade e os critérios de atribuição. Em "
          "episódios com vários agentes, regista-se cada um e designa-se "
          "como agente principal o que os classificadores considerarem "
          "responsável pelo quadro clínico mais grave."),
        QUADRO("variaveis", "Variáveis do estudo e definições operacionais",
               ["Variável", "Tipo", "Definição operacional e categorias",
                "Objectivo"],
               [
                   ["Idade", "Independente, quantitativa",
                    "Anos completos (meses nas crianças com menos de um ano); "
                    "grupos: menos de 5, 5 a 14, 15 a 24, 25 a 44, 45 ou mais",
                    "1, 2, 5"],
                   ["Sexo", "Independente, qualitativa",
                    "Masculino; feminino", "1, 2, 5"],
                   ["Proveniência", "Independente, qualitativa",
                    "Cidade de Nampula; outro distrito da província; outra "
                    "província; sem registo", "1"],
                   ["Referência de outra unidade", "Independente, qualitativa",
                    "Sim (tipo de unidade); não; sem registo", "1, 5"],
                   ["Antecedentes registados", "Independente, qualitativa",
                    "Doença psiquiátrica ou tentativa anterior: sim; não; "
                    "sem registo", "1"],
                   ["Via e local da exposição", "Descritiva, qualitativa",
                    "Via oral, inalatória, cutânea, ocular, injectável ou "
                    "múltipla; domicílio, campo ou local de trabalho, escola, "
                    "outro", "1"],
                   ["Tempo até à admissão", "Independente, quantitativa",
                    "Horas entre a exposição e a chegada ao HCN; categorias: "
                    "menos de 2, 2 a 6, mais de 6 a 24, mais de 24", "1, 5"],
                   ["Intervenções antes da chegada", "Descritiva, qualitativa",
                    "Indução do vómito, leite ou outros líquidos, preparação "
                    "tradicional, tratamento noutra unidade, nenhuma", "1, 3"],
                   ["Agente principal", "Independente, qualitativa",
                    "Categoria do quadro de agentes e código da CID-10",
                    "2, 5"],
                   ["Medicamento", "Descritiva, qualitativa",
                    "Denominação comum internacional e código ATC (grupo "
                    "principal e substância)", "2, 4"],
                   ["Pesticida", "Descritiva, qualitativa",
                    "Tipo e classe de perigosidade da OMS (Ia, Ib, II, III, "
                    "U, não determinável)", "2, 4"],
                   ["Número de agentes", "Descritiva, qualitativa",
                    "Um; dois ou mais; co-ingestão de álcool (sim, não)", "2"],
                   ["Intencionalidade", "Dependente, qualitativa",
                    "Acidental; autoprovocada; homicida ou agressão; "
                    "indeterminada, segundo o quadro de critérios", "2, 5"],
                   ["Descontaminação", "Descritiva, qualitativa",
                    "Carvão activado; lavagem gástrica; lavagem da pele ou "
                    "dos olhos; nenhuma; sem registo", "3"],
                   ["Antídoto administrado", "Descritiva, qualitativa",
                    "Substância, dose, via e horas desde a chegada; nenhum",
                    "3, 4"],
                   ["Gravidade (PSS)", "Descritiva, ordinal",
                    "0 nenhuma, 1 ligeira, 2 moderada, 3 grave, 4 fatal, à "
                    "admissão e máxima no episódio; não graduável", "3"],
                   ["Evolução clínica", "Dependente, qualitativa",
                    "Alta do Banco de Socorros; internamento (enfermaria ou "
                    "UCI); transferência externa; abandono ou alta a pedido; "
                    "óbito", "3, 5"],
                   ["Internamento", "Dependente, qualitativa",
                    "Permanência em enfermaria ou UCI depois do Banco de "
                    "Socorros (sim, não)", "3, 5"],
                   ["Óbito", "Dependente, qualitativa",
                    "Morte durante o episódio (sim, não) e local", "3, 5"],
                   ["Encaminhamento para saúde mental", "Descritiva, "
                    "qualitativa", "Nos actos autoprovocados: pedido de "
                    "psicologia ou psiquiatria registado (sim, não)", "3"],
                   ["Antídoto indicado", "Descritiva, qualitativa",
                    "Antídoto correspondente ao agente segundo o quadro de "
                    "correspondência; nenhum", "4"],
                   ["Inclusão na LNME", "Descritiva, qualitativa",
                    "Lista de medicamentos essenciais; lista de "
                    "especialidade; não incluído", "4"],
                   ["Disponibilidade mensal", "Descritiva, qualitativa",
                    "Disponível todo o mês; com ruptura; não armazenado; sem "
                    "informação, em cada um dos 24 meses", "4"],
               ],
               larguras=[3.3, 2.6, 8.3, 1.8]),
        QUADRO("agentes",
               "Categorias de agente adoptadas pelo estudo e correspondência "
               "com as classificações internacionais",
               ["Categoria", "Códigos da CID-10", "Subclassificação",
                "Exemplos"],
               [
                   ["Medicamentos", "T36 a T50",
                    "Classificação ATC: grupo principal e substância",
                    "Paracetamol (N02BE01), anti-retrovirais, antimaláricos, "
                    "benzodiazepinas"],
                   ["Pesticidas", "T60",
                    "Organofosforados e carbamatos, raticidas, piretróides, "
                    "herbicidas, outros; classe de perigosidade da OMS",
                    "Veneno para ratos de composição desconhecida, "
                    "insecticidas agrícolas, paraquate"],
                   ["Petróleo de iluminação e outros derivados do petróleo",
                    "T52.0", "Produto", "Querosene, gasolina, gasóleo"],
                   ["Outros produtos domésticos", "T52 (excepto T52.0), T53, "
                    "T54, T55", "Corrosivos, sabões e detergentes, solventes",
                    "Lixívia, soda cáustica, detergentes"],
                   ["Plantas e preparações tradicionais", "T62.2; T65.9 se a "
                    "composição for desconhecida", "Planta identificada ou "
                    "preparação de composição desconhecida",
                    "Raízes, folhas ou preparados de medicina tradicional"],
                   ["Álcool", "T51; F10.0 quando registado como intoxicação "
                    "aguda pelo álcool", "Etanol, metanol, bebida "
                    "tradicional ou adulterada", "Aguardente artesanal, "
                    "bebidas fermentadas"],
                   ["Gases e fumos", "T58, T59", "Monóxido de carbono, outros",
                    "Fumo de braseiros ou fogareiros em espaço fechado"],
                   ["Outros e desconhecido", "T56, T57, T61, T62 (excepto "
                    "T62.2), T64, T65 (T65.9 sem menção de preparação "
                    "tradicional)", "Metais, alimentos tóxicos, "
                    "substância não identificada", "Cogumelos, substância "
                    "desconhecida"],
               ],
               larguras=[3.4, 3.0, 4.8, 4.8],
               fonte="Elaboração própria (2026), a partir das "
                     "classificações citadas no texto.",
               nota=("A categoria é atribuída pela descrição do agente no "
                     "registo. T63 (animais peçonhentos) fica excluído do "
                     "estudo.")),
        QUADRO("intencao",
               "Categorias de intencionalidade e critérios de atribuição a "
               "partir do registo",
               ["Categoria", "Códigos da CID-10", "Critérios de atribuição"],
               [
                   ["Acidental", "X40 a X49",
                    "O registo descreve uma circunstância acidental: "
                    "ingestão por criança, confusão de recipiente, exposição "
                    "doméstica, agrícola ou ocupacional, erro de dose ou de "
                    "medicamento, consumo recreativo ou de bebida adulterada "
                    "sem menção de auto-agressão. Nas crianças com menos de "
                    "10 anos sem menção de intenção, presume-se acidental "
                    "(regra testada em análise de sensibilidade)"],
                   ["Autoprovocada", "X60 a X69",
                    "O registo refere tentativa de suicídio, auto-agressão, "
                    "ingestão voluntária para se magoar ou declaração do "
                    "doente ou do acompanhante nesse sentido. O pedido de "
                    "avaliação psiquiátrica, por si só, não basta, para não "
                    "tornar circular a análise do encaminhamento"],
                   ["Homicida ou agressão", "X85 a X90",
                    "O registo refere administração por terceiros com "
                    "intenção de causar dano ou suspeita de envenenamento "
                    "criminoso, incluindo participação policial por esse "
                    "motivo"],
                   ["Indeterminada", "Y10 a Y19",
                    "Doente com 10 ou mais anos sem qualquer menção de "
                    "circunstância ou intenção; ou menções contraditórias "
                    "que não se resolvem pela regra da fonte mais "
                    "pormenorizada (o processo clínico prevalece sobre o "
                    "livro de registo)"],
               ],
               larguras=[3.2, 2.6, 10.2],
               fonte="Elaboração própria (2026), a partir da CID-10."),
        P("A intencionalidade e a gravidade dependem de julgamento sobre o "
          "registo e, por isso, são atribuídas por dois classificadores "
          "independentes, como se descreve nos procedimentos. A gravidade "
          "segue a PSS, aplicada à admissão e ao pior momento do episódio "
          "{persson1998}, mas só quando a ficha de urgência ou o processo "
          "descrevem as manifestações clínicas: o livro de registo, sozinho, "
          "não permite graduá-la, e o episódio fica «não graduável». Se os "
          "sinais à chegada estiverem preenchidos em menos de 60% dos "
          "episódios da verificação prévia, a PSS sai do objectivo 3 e passa "
          "às limitações. Um episódio com indicação de antídoto é aquele cujo "
          "agente principal ou secundário corresponde a um antídoto no "
          "[[quadro:antidotos]]. As correspondências seguem o anexo das "
          "orientações da OMS para centros antivenenos que associa cada "
          "antídoto da lista modelo à sua indicação principal {omspc2020}, "
          "actualizado pela lista de 2025 {omseml2025}; para a pralidoxima, o "
          "glicopirrolato e o flumazenil, ausentes da lista modelo, segue-se a "
          "LNME {misau2023}. O quadro é validado, antes da recolha, pelo "
          "painel de peritos, que pode acrescentar pares relevantes para os "
          "agentes encontrados na verificação prévia."),
        QUADRO("antidotos",
               "Correspondência entre agentes e antídotos e situação na lista "
               "nacional de medicamentos essenciais de 2023",
               ["Agente ou grupo de agentes", "Antídoto", "Situação na LNME"],
               [
                   ["Organofosforados e carbamatos",
                    "Atropina; pralidoxima (organofosforados); glicopirrolato",
                    "Atropina 0,5 mg/mL entre os adjuvantes da anestesia; "
                    "pralidoxima e glicopirrolato na lista de especialidade"],
                   ["Paracetamol", "Acetilcisteína",
                    "Capítulo dos antídotos"],
                   ["Opióides", "Naloxona", "Capítulo dos antídotos"],
                   ["Benzodiazepinas", "Flumazenil", "Capítulo dos antídotos"],
                   ["Metanol e etilenoglicol", "Fomepizol",
                    "Capítulo dos antídotos"],
                   ["Cianeto", "Nitrito de sódio e tiossulfato de sódio",
                    "Lista de especialidade"],
                   ["Agentes metemoglobinizantes", "Azul de metileno",
                    "Capítulo dos antídotos"],
                   ["Raticidas anticoagulantes e varfarina",
                    "Fitomenadiona", "Capítulo das vitaminas"],
                   ["Heparina", "Sulfato de protamina",
                    "Capítulo dos antídotos"],
                   ["Ferro", "Desferroxamina", "Lista de especialidade"],
                   ["Chumbo, arsénio e mercúrio",
                    "Dimercaprol, edetato de cálcio, ácido "
                    "dimercaptosuccínico, penicilamina",
                    "Lista de especialidade"],
                   ["Tálio", "Azul da Prússia", "Capítulo dos antídotos"],
                   ["Bloqueadores dos canais de cálcio", "Gluconato de cálcio",
                    "Capítulo das vitaminas e sais minerais"],
                   ["Isoniazida", "Piridoxina", "Capítulo das vitaminas"],
                   ["Ingestão oral recente de agente adsorvível",
                    "Carvão activado (não específico)",
                    "Capítulo dos antídotos"],
               ],
               larguras=[4.4, 4.8, 6.8],
               fonte="Elaboração própria (2026), a partir do anexo sobre "
                     "antídotos das orientações da OMS para centros "
                     "antivenenos, da lista modelo da OMS de 2025 e da LNME "
                     "de 2023; correspondências a validar pelo painel de "
                     "peritos."),
    ]),
    ("Instrumentos de recolha de dados e respectivas fontes", [
        P("São usados quatro instrumentos, todos construídos para este "
          "estudo. A ficha de extracção de dados (Apêndice A) reúne as "
          "variáveis do [[quadro:variaveis]], com campos codificados e campos "
          "de texto livre onde o extractor transcreve, sem identificadores, "
          "o diagnóstico e as circunstâncias da exposição tal como constam do "
          "registo; parte das variáveis dos estudos africanos do "
          "[[quadro:estado_arte]], que usaram fichas semelhantes testadas "
          "previamente {zgambo2016}. A grelha de verificação prévia da "
          "qualidade da fonte (Apêndice B) regista o preenchimento de cada "
          "variável nos 30 episódios de 2024. A grelha de disponibilidade de "
          "antídotos (Apêndice C) regista, para cada antídoto, a situação na "
          "LNME e o estado de cada um dos 24 meses. O manual de preenchimento "
          "e classificação contém as definições, a lista de palavras-chave "
          "para a identificação dos casos, as regras de codificação dos "
          "agentes, os critérios do [[quadro:intencao]] e a tabela da PSS."),
        P("A validade de conteúdo da ficha, do manual e do quadro de "
          "correspondência dos antídotos é avaliada por um painel de três "
          "peritos (um médico do Banco de Socorros, um farmacêutico "
          "hospitalar e um docente de farmacologia ou toxicologia), que "
          "classifica a pertinência de cada item numa escala de quatro "
          "pontos; os itens com índice de validade de conteúdo inferior a "
          "0,80 são revistos. A ficha é depois testada na verificação "
          "prévia, que serve também de pré-teste fora da amostra final e de "
          "treino dos extractores."),
    ]),
    ("Procedimentos de recolha de dados e controlo de qualidade", [
        H3("Verificação prévia da qualidade da fonte"),
        P("Antes da recolha, os dois extractores identificam no livro do "
          "Banco de Socorros 30 episódios consecutivos de intoxicação aguda "
          "de Outubro a Dezembro de 2024 (recuando a meses anteriores se não "
          "houver 30), procuram os respectivos processos e registam na grelha "
          "do Apêndice B se cada variável está preenchida, ilegível ou "
          "ausente, o sistema em que o diagnóstico é registado (CID-10 ou "
          "texto livre) e o tempo gasto por processo. A regra "
          "de decisão está escrita à partida: a variável preenchida em 80% ou "
          "mais dos episódios mantém-se; a preenchida em 60% a 79% mantém-se, "
          "com a categoria «sem registo» apresentada em todas as tabelas; a "
          "preenchida em menos de 60% sai dos objectivos e passa a ser "
          "relatada como limitação, com a sua taxa de preenchimento, como "
          "poderá suceder ao tempo até à admissão. O agente e a evolução são "
          "excepção, porque sustentam o estudo: se algum deles ficar abaixo "
          "de 60%, a pesquisa é alargada aos livros das enfermarias e ao "
          "registo de óbitos e, se o problema persistir, o orientador e o "
          "Comité Institucional de Bioética para a Saúde da Universidade "
          "Lúrio (CIBS-UniLúrio) são informados e os objectivos reformulados "
          "antes da recolha. A verificação prévia serve ainda para completar "
          "a lista de palavras-chave com termos locais."),
        H3("Identificação dos casos e selecção"),
        P("Os extractores lêem, página a página, todas as entradas dos livros "
          "de registo do Banco de Socorros de 2025 e 2026 e listam as que "
          "contêm no diagnóstico ou na observação uma das palavras-chave do "
          "manual (por exemplo, intoxicação, envenenamento, ingestão, veneno, "
          "raticida, pesticida, petróleo, lixívia, sobredosagem, tentativa de "
          "suicídio, embriaguez ou síndrome colinérgica). A lista é cruzada "
          "com os livros de admissão da medicina, da pediatria e da UCI e com "
          "o registo de óbitos, para acrescentar episódios de intoxicação que "
          "não tenham sido identificados como tal no Banco de Socorros, e são "
          "eliminados os duplicados. Cada episódio recebe um código "
          "sequencial; a correspondência entre o código e o número do "
          "processo fica numa lista-chave guardada em separado. Aplica-se "
          "então o censo ou, se o total exceder 700, a amostragem "
          "sistemática."),
        H3("Extracção, dupla extracção e classificação"),
        P("A extracção decorre no arquivo do HCN, a partir do processo "
          "clínico, da ficha de urgência e das guias de transferência, sem "
          "fotografar nem copiar documentos; o estudante revê as fichas no "
          "próprio dia e assinala os campos em falta para nova consulta do "
          "processo. Os dois extractores são o estudante e um profissional de "
          "saúde com experiência de urgência. Cada um volta a extrair, de "
          "forma independente e sem acesso à primeira ficha, uma parte dos "
          "episódios extraídos pelo outro, até perfazer 10% dos episódios "
          "incluídos (70 no cenário de 700), sorteados por números aleatórios "
          "depois de fechada a lista. A concordância é calculada por variável, "
          "pelo kappa de Cohen para as variáveis qualitativas e pela "
          "proporção de valores idênticos para as quantitativas; o objectivo "
          "é um kappa de 0,80 ou mais nas variáveis principais (agente, "
          "evolução, antídoto) e, se alguma ficar abaixo de 0,60, essa "
          "variável é revista em todos os episódios já extraídos e os "
          "extractores são retreinados."),
        P("A intencionalidade, o agente principal e a gravidade são "
          "atribuídos em todos os episódios por dois classificadores "
          "independentes, o estudante e o segundo extractor, a partir dos campos "
          "codificados e "
          "textuais da ficha, sem conhecerem a classificação um do outro. A concordância é medida pelo kappa de "
          "Cohen com IC95% (ponderado para a PSS, que é ordinal). Em coerência "
          "com a crítica aos limiares permissivos {mchugh2012}, adopta-se o "
          "mínimo de 0,60: "
          "abaixo dele, o manual é revisto e todos os episódios são "
          "reclassificados. As discordâncias finais são resolvidas por "
          "consenso e, na sua falta, pelo orientador como terceiro "
          "classificador."),
        H3("Consulta da lista nacional e dos registos de existências"),
        P("O levantamento da disponibilidade dos antídotos é documental e não "
          "um inventário físico. Para cada antídoto do [[quadro:antidotos]], "
          "regista-se na grelha do Apêndice C a situação na LNME de 2023 "
          "{misau2023}, a forma farmacêutica e a dosagem nela previstas. Em "
          "seguida, com autorização da direcção da farmácia do HCN, "
          "consultam-se os registos de existências dos 24 meses e "
          "classifica-se cada mês como disponível (saldo positivo em todo o "
          "mês), com ruptura (saldo nulo em algum momento do mês), não "
          "armazenado (sem ficha de existências nem entrada registada no "
          "período) ou sem informação. Os episódios com indicação de antídoto que não o "
          "receberam são depois cruzados com o estado do antídoto no mês do "
          "atendimento."),
    ]),
    ("Processamento e análise dos dados", [
        P("As fichas são digitadas duas vezes, por pessoas diferentes, no "
          "programa EpiData, de acesso livre, e as discordâncias entre as duas "
          "digitações são corrigidas por consulta da ficha em papel. A base é "
          "depois exportada para o Statistical Package for the Social "
          "Sciences (SPSS) Statistics, versão 26 ou superior, ou para o R, e "
          "submetida a verificações de amplitude e de coerência. O nível de "
          "significância é de 5% (p<0,05)."),
        P("Para os objectivos 1 a 3, as variáveis qualitativas são descritas "
          "por frequências absolutas e relativas com IC95% pelo método de "
          "Wilson, e as quantitativas pela mediana e pelo intervalo "
          "interquartil (IIQ), ou pela média e pelo desvio-padrão quando a "
          "distribuição for simétrica. Os agentes são apresentados por "
          "categoria do [[quadro:agentes]], por grupo terapêutico ATC e por "
          "classe de perigosidade, e tanto os agentes como a intencionalidade "
          "são cruzados com o grupo etário e o sexo. A letalidade por agente é apresentada com IC95% exactos de "
          "Clopper-Pearson."),
        P("Para o objectivo 4, constrói-se uma matriz que associa a cada "
          "antídoto o número de episódios com indicação, a proporção dos que "
          "o receberam, com IC95%, a situação na LNME e o número de meses, em "
          "24, com disponibilidade, ruptura ou ausência de informação. A "
          "proporção de episódios com indicação que não receberam o antídoto "
          "num mês de ruptura é apresentada como indicador da necessidade não "
          "satisfeita atribuível ao aprovisionamento."),
        P("Para o objectivo 5, a associação entre o tipo de agente e a "
          "intencionalidade é testada pelo qui-quadrado de Pearson ou, se mais "
          "de 20% das frequências esperadas forem inferiores a 5, pelo teste "
          "exacto de Fisher-Freeman-Halton; a força da associação é medida "
          "pelo V de Cramér e os resíduos ajustados estandardizados indicam "
          "as células que contribuem para ela. A associação entre o tipo de "
          "agente e o internamento é testada da mesma forma e expressa pelo "
          "risco relativo com IC95%, tendo os medicamentos como categoria de "
          "referência; a letalidade é comparada pelo teste exacto de Fisher. "
          "Quando a regra dos eventos por parâmetro o permitir, ajustam-se "
          "modelos de regressão logística para o internamento e para a "
          "intencionalidade autoprovocada, com odds ratio (OR) brutos e "
          "ajustados e IC95%, verificação da colinearidade pelo factor de "
          "inflação da variância (valores abaixo de 5) e do ajustamento pelo "
          "teste de Hosmer-Lemeshow."),
        P("Os dados em falta são descritos por variável e não são imputados; "
          "as análises usam os casos completos em cada variável. Três "
          "análises de sensibilidade testam a estabilidade dos resultados "
          "principais: a restrição ao primeiro episódio de cada pessoa; a "
          "reatribuição dos episódios de intencionalidade indeterminada, "
          "primeiro todos como autoprovocados e depois todos como acidentais; "
          "e a exclusão da regra de presunção nas crianças com menos de 10 "
          "anos."),
    ]),
    ("Limitações do estudo e estratégias de mitigação", [
        P("O [[quadro:limitacoes]] resume as limitações previstas, as suas "
          "consequências e as estratégias adoptadas para as reduzir. A "
          "principal é a dependência de registos clínicos que não foram "
          "concebidos para a investigação, problema bem documentado nos "
          "estudos africanos e moçambicanos {adinew2017,miguel2025}."),
        QUADRO("limitacoes", "Limitações previstas e estratégias de mitigação",
               ["Limitação", "Consequência", "Mitigação"],
               [
                   ["Registos incompletos, ilegíveis ou processos não "
                    "localizados", "Perda de informação e possível viés se as "
                    "perdas forem selectivas",
                    "Verificação prévia com regra dos 60%; cruzamento de "
                    "fontes; descrição e comparação das perdas"],
                   ["Casos registados sob sintomas ou diagnósticos vagos",
                    "Subestimação do número de episódios",
                    "Lista de palavras-chave com termos locais; cruzamento "
                    "com livros de internamento e registo de óbitos"],
                   ["Agente sem confirmação analítica ou desconhecido",
                    "Classificação errada do agente",
                    "Categoria «desconhecido»; regras escritas de "
                    "codificação; dois classificadores"],
                   ["Gravidade graduada a posteriori a partir do registo",
                    "Gravidade subestimada ou impossível de graduar",
                    "PSS só com sinais registados; categoria «não "
                    "graduável»; regra dos 60%; kappa ponderado"],
                   ["Sub-registo dos actos autoprovocados por estigma",
                    "Subestimação da intencionalidade autoprovocada",
                    "Critérios explícitos; categoria indeterminada; análises "
                    "de sensibilidade"],
                   ["Só se estudam os casos que chegam ao HCN",
                    "Perfil e letalidade não generalizáveis à população",
                    "Descrição da proveniência e da referência; leitura "
                    "cautelosa dos resultados"],
                   ["Evolução desconhecida após transferência ou abandono",
                    "Possível subestimação da letalidade",
                    "Categoria própria; análise com e sem estes episódios"],
                   ["Número reduzido de óbitos", "Poder limitado para a "
                    "comparação da letalidade", "IC95% exactos; teste exacto "
                    "de Fisher; leitura exploratória; sem modelos abaixo de "
                    "10 eventos por parâmetro"],
                   ["Registos de existências incompletos",
                    "Estimativa errada da disponibilidade dos antídotos",
                    "Categoria «sem informação»; confronto com a "
                    "administração registada nos processos"],
                   ["Episódios repetidos da mesma pessoa",
                    "Falta de independência entre observações",
                    "Análise de sensibilidade com o primeiro episódio"],
                   ["Estudo num único hospital", "Validade externa limitada",
                    "Descrição pormenorizada do contexto e das fontes"],
               ],
               larguras=[5.0, 4.6, 6.4]),
    ]),
    ("Considerações éticas", [
        P("O protocolo será submetido ao CIBS-UniLúrio e a recolha só começa "
          "depois da sua aprovação e da autorização da direcção do HCN, com "
          "conhecimento da Direcção Provincial de Saúde de Nampula. O estudo "
          "segue a Declaração de Helsínquia na revisão de 2024 {wma2025} e a "
          "Lei n.º 3/2023, que regula a investigação em saúde humana em "
          "Moçambique {lei3de2023}."),
        P("Pede-se ao CIBS-UniLúrio a dispensa do consentimento informado "
          "(Apêndice D), com quatro fundamentos: o estudo usa apenas "
          "registos já produzidos na assistência e não envolve qualquer "
          "intervenção ou contacto com os doentes; seria impraticável obter o "
          "consentimento das pessoas atendidas ao longo de dois anos, muitas "
          "delas referidas de outras províncias e algumas falecidas; a "
          "tentativa de contactar vítimas de actos autoprovocados ou as suas "
          "famílias poderia, por si só, expor um acontecimento que desejam "
          "manter reservado; e o risco é mínimo, porque os dados são "
          "extraídos sem identificadores e apresentados de forma agregada. "
          "O benefício esperado é colectivo, na prevenção e na preparação do "
          "hospital. O pedido e a autorização abrangem também os 30 episódios "
          "de 2024 da verificação prévia, que são tratados com as mesmas "
          "garantias e não entram na análise."),
        P("As intoxicações autoprovocadas e as agressões são dados sensíveis "
          "e recebem cuidados adicionais. A ficha não contém nome, número de "
          "processo, endereço nem telefone; cada episódio tem um código "
          "sequencial, e a lista-chave é guardada em separado e destruída "
          "depois da validação dos dados. A base de dados é cifrada e "
          "protegida por palavra-passe. Os resultados são apresentados só de "
          "forma agregada, sem células com menos de cinco episódios quando o "
          "cruzamento de variáveis (idade, sexo, proveniência e mês) puder "
          "permitir a identificação. O relato não descreve os métodos de "
          "auto-envenenamento de forma pormenorizada nem associa produtos "
          "comerciais a locais ou datas, seguindo as recomendações da OMS "
          "para prevenir comportamentos imitativos {omsmedia2023}. Não há contacto com as "
          "vítimas nem com as famílias."),
        P("Como o estudo é retrospectivo, não detecta problemas de saúde em "
          "participantes que possam ser referenciados individualmente. Se, "
          "durante a recolha, surgir informação que exija acção imediata, "
          "como rupturas repetidas de um antídoto vital ou um conjunto de "
          "intoxicações pelo mesmo produto que sugira um surto ou uma bebida "
          "adulterada, o estudante e o orientador informam de imediato a "
          "direcção do HCN, de forma agregada e sem identificar doentes. Os "
          "registos da farmácia são tratados como informação de gestão, sem "
          "avaliação individual de profissionais. Os investigadores declaram "
          "não ter conflitos de interesse."),
    ]),
]

# ----------------------------------------------------- 9 e 10 ---------------
RESULTADOS_ESPERADOS = [
    P("Os resultados esperados seguem a ordem dos objectivos específicos, "
      "com a direcção provável apoiada na literatura e a utilidade prática "
      "de cada um."),
    LISTA([
        "Objectivo 1: um perfil com dois grupos etários predominantes, as "
        "crianças pequenas e os adultos jovens, com predomínio feminino "
        "nestes últimos {mbongwe2020,laher2022}, uma fracção importante de "
        "doentes referidos dos distritos e das províncias vizinhas e atrasos "
        "frequentes na chegada {areprekumor2024}. Orienta a educação "
        "preventiva por grupo etário e a melhoria da referência.",
        "Objectivo 2: os agentes predominantes em cada grupo etário, com a "
        "expectativa de que os pesticidas, incluindo o veneno para ratos, e "
        "os medicamentos ocupem os primeiros lugares nos adolescentes e "
        "adultos, e o petróleo de iluminação e os produtos domésticos nas "
        "crianças {wagenaar2016,areprekumor2024}, bem como a proporção de "
        "actos autoprovocados. A distribuição por classe de perigosidade "
        "indicará os pesticidas cuja restrição teria maior impacto.",
        "Objectivo 3: a proporção de episódios descontaminados e dos que "
        "receberam antídoto, a gravidade e a letalidade por agente, "
        "previsivelmente concentrada nos pesticidas anticolinesterásicos "
        "{laher2022,asrie2024}, o que fundamenta um protocolo hospitalar de "
        "abordagem do intoxicado e a melhoria do registo.",
        "Objectivo 4: um mapa que associa cada agente ao antídoto "
        "correspondente, à sua situação na LNME e aos meses de "
        "disponibilidade e de ruptura no HCN, com o número de episódios em "
        "que a falta do antídoto coincidiu com a necessidade. Sustenta uma "
        "lista hospitalar de antídotos com quantidades mínimas e a revisão "
        "trienal da LNME.",
        "Objectivo 5: a associação entre o tipo de agente e a "
        "intencionalidade e entre o tipo de agente e o internamento, "
        "previsivelmente com os pesticidas e os medicamentos ligados aos "
        "actos autoprovocados e os derivados do petróleo às exposições "
        "acidentais {zgambo2016}; a comparação da letalidade terá carácter "
        "exploratório. Estas associações apoiam a triagem no Banco de "
        "Socorros e o planeamento das camas de internamento.",
    ]),
]
DIVULGACAO = [
    P("Os resultados serão apresentados na defesa pública da monografia na "
      "FCS da UniLúrio e entregues, num relatório técnico, à direcção do "
      "HCN, ao Banco de Socorros, à farmácia hospitalar e à Direcção "
      "Provincial de Saúde de Nampula, com uma sessão de devolução no "
      "hospital centrada no stock de antídotos e no registo dos casos. Um "
      "resumo dirigido à revisão da LNME será enviado à autoridade "
      "reguladora e ao MISAU. Prevê-se a apresentação numa jornada "
      "científica da UniLúrio ou num congresso nacional e a submissão de um "
      "artigo a uma revista com revisão por pares. Os actos autoprovocados "
      "serão sempre tratados de forma agregada e sem pormenores sobre os "
      "métodos {omsmedia2023}. A devolução à comunidade far-se-á através de "
      "mensagens sobre o armazenamento seguro de pesticidas, de petróleo de "
      "iluminação e de medicamentos, preparadas com o sector de educação "
      "para a saúde do hospital."),
]

# ----------------------------------------------------- 11. cronograma -------
CRONOGRAMA_TEXTO = [
    P("O [[quadro:cronograma]] distribui as actividades por 12 meses, de "
      "Outubro de 2026 a Setembro de 2027. A verificação prévia, em "
      "episódios de 2024, só começa em Fevereiro de 2027, depois da "
      "aprovação ética, e a recolha nos processos de 2025 e 2026 ocupa "
      "Março a Maio de 2027."),
]
CRONOGRAMA = {
    "inicio": (2026, 10),
    "n_meses": 12,
    "actividades": [
        ("Revisão da literatura e redacção do protocolo", [1, 2]),
        ("Submissão ao CIBS-UniLúrio e pedidos de autorização ao HCN",
         [3, 4]),
        ("Validação da ficha, do manual e do quadro de antídotos pelo painel "
         "de peritos; formação dos extractores", [4, 5]),
        ("Verificação prévia em 30 episódios de 2024 e ajuste da ficha", [5]),
        ("Identificação dos episódios nos livros de 2025 e 2026 e selecção",
         [6]),
        ("Extracção dos dados, com dupla extracção de 10%", [6, 7, 8]),
        ("Classificação independente da intencionalidade, do agente e da "
         "gravidade; cálculo do kappa", [7, 8]),
        ("Consulta da LNME e dos registos de existências de antídotos", [8]),
        ("Digitação dupla, limpeza e análise dos dados", [9, 10]),
        ("Redacção da monografia", [10, 11]),
        ("Revisão pelo orientador, correcções e entrega", [11]),
        ("Defesa pública e devolução dos resultados ao HCN", [12]),
    ],
}

# ----------------------------------------------------- 12. orcamento --------
ORCAMENTO_TEXTO = [
    P("A [[tabela:orcamento]] apresenta as rubricas em meticais, com 10% de "
      "imprevistos. O estudo será financiado pelo estudante, com pedido de "
      "apoio à FCS da UniLúrio para a impressão e a divulgação. As rubricas "
      "maiores são a alimentação e as deslocações ao HCN, calculadas para "
      "cerca de 65 dias de trabalho de cada um dos dois extractores "
      "(verificação prévia, identificação dos casos e extracção), e a "
      "impressão de 800 fichas de "
      "extracção de quatro páginas (700 do cenário máximo, 70 de dupla "
      "extracção e 30 da verificação prévia). O valor da taxa de submissão "
      "ao CIBS-UniLúrio é uma estimativa [confirmar o valor em vigor junto "
      "do CIBS-UniLúrio]. Não há custos de licenças, porque a digitação usa "
      "o EpiData e a análise pode fazer-se no R, ambos gratuitos."),
]
ORCAMENTO = [
    ("Impressão das fichas de extracção (800 fichas de 4 páginas)",
     "página", 3200, 5),
    ("Impressão das folhas de identificação dos casos nos livros",
     "página", 150, 5),
    ("Impressão do manual de preenchimento, das grelhas e do quadro de "
     "antídotos", "página", 100, 5),
    ("Impressão e encadernação do protocolo e dos pedidos de autorização",
     "exemplar", 5, 400),
    ("Material de escritório (pastas, canetas, lápis, blocos, agrafador)",
     "conjunto", 1, 1500),
    ("Caixa de arquivo com fechadura para guarda das fichas", "unidade", 1,
     2500),
    ("Disco externo cifrado para cópia de segurança dos dados", "unidade", 1,
     2500),
    ("Deslocações ao HCN dos dois extractores", "viagem de ida e volta", 130,
     100),
    ("Subsídio de alimentação durante a recolha", "dia por pessoa", 130, 200),
    ("Subsídio ao segundo extractor e classificador independente", "mês", 3,
     3000),
    ("Reunião do painel de peritos para validação dos instrumentos",
     "sessão", 1, 2000),
    ("Sessão de formação e calibração dos extractores", "sessão", 1, 1000),
    ("Comunicações e pacotes de internet", "mês", 12, 500),
    ("Taxa de submissão ao CIBS-UniLúrio (estimativa)", "taxa", 1, 2500),
    ("Impressão e encadernação da monografia final", "exemplar", 4, 800),
    ("Relatório técnico e material da sessão de devolução no HCN",
     "exemplar", 5, 300),
    ("Póster e inscrição em jornada científica", "unidade", 1, 5000),
]
ORCAMENTO_IMPREVISTOS = 0.10

# ----------------------------------------------------- apendices ------------
APENDICES = [
    ("Ficha de extracção de dados", [
        NOTA("Instruções: preencher a partir do processo clínico, da ficha de "
             "urgência, das guias de transferência e, quando necessário, dos "
             "livros de internamento e do registo de óbitos. Não registar "
             "nomes, números de processo, endereços nem telefones; usar "
             "apenas o código atribuído na lista de identificação. Registar "
             "as horas no formato de 24 horas (hh:mm). Quando a informação não "
             "existir, escrever «sem registo» (código 99). Transcrever o "
             "diagnóstico e as circunstâncias sem nomes de pessoas nem de "
             "lugares precisos. Não fotografar nem copiar documentos."),
        H3("Secção I. Identificação do registo"),
        CAMPO("Código do episódio: __________   Ano: (   ) 2025   (   ) 2026   "
              "Mês do atendimento: ______"),
        CAMPO("Porta de urgência: (   ) Adultos   (   ) Pediatria   "
              "Extractor: (   ) 1   (   ) 2   Dupla extracção: (   ) Sim   "
              "(   ) Não"),
        CAMPO("Data da extracção: ___/___/2027   Episódio repetido da mesma "
              "pessoa: (   ) Sim   (   ) Não   Reatendimento em 72 horas: "
              "(   ) Sim   (   ) Não"),
        PERG("Documentos disponíveis (assinalar todos):",
             ["Livro do Banco de Socorros", "Ficha de urgência",
              "Processo clínico", "Guia de transferência",
              "Livro de internamento", "Registo de óbito"]),
        PERG("Critérios de exclusão presentes (se algum for assinalado, "
             "parar e registar o motivo):",
             ["Nenhum", "Animal peçonhento", "Reacção adversa em dose "
              "terapêutica", "Intoxicação crónica", "Toxinfecção alimentar "
              "infecciosa", "Álcool como achado acessório",
              "Chegou sem vida sem atendimento"]),
        H3("Secção II. Características da vítima"),
        PERG("Idade (anos completos; meses se menos de um ano):"),
        PERG("Sexo:", ["Masculino", "Feminino"]),
        PERG("Proveniência:", ["Cidade de Nampula", "Outro distrito da "
                               "província de Nampula", "Outra província "
                               "(qual): ______", "Sem registo"]),
        PERG("Referido de outra unidade sanitária:",
             ["Não", "Sim, centro de saúde", "Sim, hospital distrital ou "
              "rural", "Sim, outro: ______", "Sem registo"]),
        PERG("Antecedentes registados:",
             ["Doença psiquiátrica", "Tentativa de suicídio anterior",
              "Consumo nocivo de álcool", "Nenhum", "Sem registo"]),
        H3("Secção III. Exposição e agente"),
        CAMPO("Diagnóstico tal como registado: "
              "________________________________________________"),
        CAMPO("Circunstâncias da exposição tal como registadas: "
              "______________________________________"),
        PERG("Agente principal (categoria):",
             ["Medicamento", "Pesticida", "Petróleo de iluminação ou outro "
              "derivado do petróleo", "Outro produto doméstico", "Planta ou "
              "preparação tradicional", "Álcool", "Gás ou fumo", "Outro",
              "Desconhecido"]),
        CAMPO("Nome do produto ou substância (denominação comum, sem marca "
              "quando possível): ____________________"),
        CAMPO("Se medicamento: substância ______________   código ATC "
              "(preenchido depois) ______   quantidade ingerida ______"),
        PERG("Se pesticida, tipo:",
             ["Organofosforado ou carbamato", "Raticida (veneno para ratos)",
              "Piretróide", "Herbicida", "Outro: ______", "Desconhecido"]),
        CAMPO("Se pesticida: princípio activo ______________   classe da OMS "
              "(preenchida depois): Ia / Ib / II / III / U / não "
              "determinável"),
        PERG("Outros agentes no mesmo episódio:",
             ["Nenhum", "Álcool", "Outro: ______"]),
        PERG("Via de exposição:",
             ["Oral", "Inalatória", "Cutânea", "Ocular", "Injectável",
              "Múltipla", "Sem registo"]),
        PERG("Local da exposição:",
             ["Domicílio", "Campo ou local de trabalho", "Escola", "Outro: "
              "______", "Sem registo"]),
        CAMPO("Data e hora da exposição: ___/___/____  ___:___   Data e hora "
              "da chegada ao HCN: ___/___/____  ___:___"),
        PERG("Intervenções antes da chegada (assinalar todas):",
             ["Indução do vómito", "Leite ou outros líquidos", "Preparação "
              "tradicional", "Tratamento noutra unidade (qual): ______",
              "Nenhuma", "Sem registo"]),
        PERG("Intenção tal como descrita no registo (transcrever a expressão "
             "usada):"),
        H3("Secção IV. Apresentação clínica"),
        PERG("Sinais registados à chegada (assinalar todos):",
             ["Alteração da consciência", "Convulsões", "Miose, sialorreia "
              "ou fasciculações", "Dificuldade respiratória", "Vómitos",
              "Queimaduras da boca ou do esófago", "Hipotensão ou choque",
              "Sem sinais", "Sem registo"]),
        CAMPO("Escala de coma registada (se existir): ______   Saturação de "
              "oxigénio: ______ %   Frequência respiratória: ______"),
        H3("Secção V. Tratamento"),
        PERG("Descontaminação:",
             ["Carvão activado", "Lavagem gástrica", "Lavagem da pele ou dos "
              "olhos", "Nenhuma", "Sem registo"]),
        CAMPO("Antídoto 1: ______________  dose ______  via ______  horas "
              "desde a chegada ______"),
        CAMPO("Antídoto 2: ______________  dose ______  via ______  horas "
              "desde a chegada ______"),
        PERG("Registo de falta de antídoto ou de pedido não satisfeito:",
             ["Sim (qual): ______", "Não", "Sem registo"]),
        PERG("Medidas de suporte (assinalar todas):",
             ["Oxigénio", "Fluidos endovenosos", "Anticonvulsivante",
              "Ventilação mecânica", "Outra: ______"]),
        H3("Secção VI. Evolução"),
        PERG("Destino a partir do Banco de Socorros:",
             ["Alta do Banco de Socorros", "Internamento em enfermaria "
              "(qual): ______", "Internamento na UCI", "Transferência para "
              "outra unidade (qual): ______", "Abandono ou alta a pedido",
              "Óbito no Banco de Socorros"]),
        PERG("Desfecho final do episódio:",
             ["Alta", "Transferência externa", "Abandono ou alta a pedido",
              "Óbito (local): ______", "Sem registo"]),
        CAMPO("Data da alta, da transferência ou do óbito: ___/___/____   "
              "Dias de internamento: ______"),
        PERG("Nos actos autoprovocados, pedido de psicologia ou psiquiatria "
             "registado:", ["Sim", "Não", "Não aplicável"]),
        H3("Secção VII. Classificação (folha separada, um exemplar por "
           "classificador)"),
        CAMPO("Classificador: (   ) 1   (   ) 2   (   ) Terceiro   Código do "
              "episódio: __________"),
        PERG("Intencionalidade:",
             ["Acidental: doméstica", "Acidental: ocupacional",
              "Acidental: erro terapêutico", "Acidental: consumo recreativo",
              "Autoprovocada", "Homicida ou agressão", "Indeterminada"]),
        PERG("Aplicou-se a presunção de acidente por idade inferior a 10 "
             "anos:", ["Sim", "Não"]),
        CAMPO("Agente principal e código da CID-10: ______________   "
              "Antídoto indicado: ______________"),
        CAMPO("Gravidade (PSS) à admissão: 0 / 1 / 2 / 3 / 4 / não graduável   "
              "Gravidade máxima no episódio: 0 / 1 / 2 / 3 / 4 / não "
              "graduável"),
    ]),
    ("Grelha de verificação prévia da qualidade da fonte", [
        NOTA("Aplicar a 30 episódios consecutivos de Outubro a Dezembro de "
             "2024. Em cada coluna de episódio, marcar P (preenchido), I "
             "(ilegível) ou A (ausente). A taxa de preenchimento é o número "
             "de P dividido por 30. Regra de decisão: 80% ou mais, a "
             "variável mantém-se; 60% a 79%, mantém-se com a categoria «sem "
             "registo»; menos de 60%, sai dos objectivos e é relatada como "
             "limitação. O agente e a evolução seguem a regra de excepção "
             "descrita na metodologia."),
        TABELA(None, "Grelha de verificação prévia",
               ["Variável", "Episódios 1 a 10", "Episódios 11 a 20",
                "Episódios 21 a 30", "P / 30 (%)", "Decisão"],
               [["Idade", "", "", "", "", ""],
                ["Sexo", "", "", "", "", ""],
                ["Proveniência", "", "", "", "", ""],
                ["Agente (categoria)", "", "", "", "", ""],
                ["Substância ou produto", "", "", "", "", ""],
                ["Intenção descrita", "", "", "", "", ""],
                ["Hora da exposição", "", "", "", "", ""],
                ["Hora da chegada", "", "", "", "", ""],
                ["Sinais à chegada", "", "", "", "", ""],
                ["Descontaminação", "", "", "", "", ""],
                ["Antídoto (sim, não)", "", "", "", "", ""],
                ["Destino e desfecho", "", "", "", "", ""],
                ["Diagnóstico codificado em CID-10 (sim, não)", "", "", "",
                 "", ""],
                ["Tempo por processo (minutos)", "", "", "", "", ""]],
               larguras=[3.6, 2.6, 2.6, 2.6, 2.2, 2.4],
               fonte="Elaboração própria (2026)."),
        CAMPO("Termos locais encontrados para acrescentar à lista de "
              "palavras-chave: ________________________________"),
    ]),
    ("Grelha de registo da disponibilidade de antídotos", [
        NOTA("Preencher uma linha por antídoto do quadro de correspondência, "
             "acrescentando as linhas necessárias. "
             "Situação na LNME: E (lista de medicamentos essenciais), S "
             "(lista de especialidade), N (não incluído). Em cada mês, a "
             "partir dos registos de existências da farmácia: D (disponível "
             "todo o mês), R (ruptura em algum momento), X (não armazenado), "
             "? (sem informação). Não se faz inventário físico."),
        TABELA(None, "Grelha de disponibilidade mensal",
               ["Antídoto, forma e dosagem", "LNME", "Jan-Jun 2025",
                "Jul-Dez 2025", "Jan-Jun 2026", "Jul-Dez 2026",
                "Meses D / R / X / ?"],
               [["Atropina injectável", "", "", "", "", "", ""],
                ["Pralidoxima injectável", "", "", "", "", "", ""],
                ["Acetilcisteína injectável", "", "", "", "", "", ""],
                ["Naloxona injectável", "", "", "", "", "", ""],
                ["Flumazenil injectável", "", "", "", "", "", ""],
                ["Fitomenadiona injectável", "", "", "", "", "", ""],
                ["Azul de metileno injectável", "", "", "", "", "", ""],
                ["Carvão activado", "", "", "", "", "", ""],
                ["Gluconato de cálcio injectável", "", "", "", "", "", ""],
                ["Outro: ______", "", "", "", "", "", ""]],
               larguras=[3.8, 1.4, 2.2, 2.2, 2.2, 2.2, 2.0],
               fonte="Elaboração própria (2026)."),
        NOTA("Em cada coluna semestral, registar a letra de cada mês pela "
             "ordem (por exemplo, D D R D ? D)."),
    ]),
    ("Pedido de dispensa de consentimento informado ao CIBS-UniLúrio", [
        CAMPO("Ao Presidente do Comité Institucional de Bioética para a "
              "Saúde da Universidade Lúrio"),
        CAMPO("Nampula, ___ de ____________ de 2026"),
        P("Assunto: pedido de dispensa de consentimento informado para o "
          "estudo «Intoxicações agudas atendidas no Banco de Socorros do "
          "Hospital Central de Nampula: agentes envolvidos, perfil das "
          "vítimas e disponibilidade de antídotos, 2025 a 2026»."),
        P("Eu, [Nome do(a) estudante], estudante da Licenciatura em Farmácia "
          "da Faculdade de Ciências de Saúde da Universidade Lúrio, sob "
          "orientação de [Nome e grau académico do(a) orientador(a)], "
          "solicito a dispensa do consentimento informado para o estudo "
          "acima identificado, que analisa retrospectivamente os registos dos "
          "episódios de intoxicação aguda atendidos no Banco de Socorros do "
          "Hospital Central de Nampula entre 1 de Janeiro de 2025 e 31 de "
          "Dezembro de 2026, e ainda de 30 episódios de 2024, usados apenas "
          "na verificação prévia da qualidade da fonte e excluídos da "
          "análise."),
        P("O pedido fundamenta-se no seguinte: o estudo usa apenas registos "
          "já produzidos durante a assistência, sem qualquer intervenção, "
          "entrevista ou contacto com os doentes; seria impraticável obter o "
          "consentimento de pessoas atendidas ao longo de dois anos, muitas "
          "delas referidas de outras províncias e algumas falecidas; o "
          "contacto com vítimas de intoxicações autoprovocadas ou com as suas "
          "famílias poderia expor um acontecimento que desejam manter "
          "reservado; e o risco para os titulares dos dados é mínimo."),
        P("Comprometo-me a cumprir as seguintes garantias: a ficha de "
          "extracção não contém nome, número de processo, endereço nem "
          "telefone; cada episódio é identificado por um código sequencial e "
          "a lista que liga o código ao processo é guardada em separado, sob "
          "a responsabilidade do orientador, e destruída depois da validação "
          "dos dados; a extracção decorre no arquivo do hospital, sem "
          "fotografias nem cópias; a base de dados é cifrada; os resultados "
          "são divulgados apenas de forma agregada, sem células que permitam "
          "identificar pessoas e sem descrição pormenorizada dos métodos de "
          "auto-envenenamento; e nenhuma vítima ou familiar será contactado."),
        P("Junto o protocolo completo, a ficha de extracção e o pedido de "
          "autorização dirigido à direcção do Hospital Central de Nampula."),
        CAMPO("O(A) estudante: ______________________________   Contacto: "
              "[preencher]"),
        CAMPO("O(A) orientador(a): ___________________________   Contacto: "
              "[preencher]"),
    ]),
    ("Pedido de autorização institucional ao Hospital Central de Nampula", [
        CAMPO("Ao Director-Geral do Hospital Central de Nampula"),
        CAMPO("C/c: Direcção Clínica; Direcção da Farmácia; Direcção "
              "Provincial de Saúde de Nampula (para conhecimento)"),
        CAMPO("Nampula, ___ de ____________ de 2026"),
        P("Assunto: pedido de autorização para a realização de um estudo "
          "documental sobre as intoxicações agudas atendidas no Banco de "
          "Socorros."),
        P("Eu, [Nome do(a) estudante], estudante da Licenciatura em Farmácia "
          "da Faculdade de Ciências de Saúde da Universidade Lúrio, venho "
          "solicitar autorização para consultar, entre Fevereiro e Maio de "
          "2027, os livros de registo do Banco de Socorros, os processos "
          "clínicos, os livros de internamento, o registo de óbitos e os "
          "registos de existências de antídotos da farmácia, relativos a 2024 "
          "(verificação prévia de 30 episódios), 2025 e 2026, no âmbito do "
          "trabalho de culminação de curso orientado por [Nome e grau "
          "académico do(a) orientador(a)]."),
        P("O estudo pretende conhecer os agentes, o perfil das vítimas, a "
          "intencionalidade, o tratamento e a evolução das intoxicações "
          "agudas e confrontar os agentes com a disponibilidade dos antídotos "
          "correspondentes, para apoiar a prevenção e a preparação do "
          "hospital. A recolha só começará depois da aprovação do Comité "
          "Institucional de Bioética para a Saúde da Universidade Lúrio. Não "
          "haverá contacto com doentes nem interferência nos serviços; os "
          "dados serão recolhidos sem identificadores, no arquivo, sem "
          "fotografias nem cópias, e os resultados serão devolvidos ao "
          "hospital num relatório técnico e numa sessão de apresentação."),
        CAMPO("O(A) estudante: ______________________________   Contacto: "
              "[preencher]"),
        CAMPO("O(A) orientador(a): ___________________________   Contacto: "
              "[preencher]"),
        CAMPO("Despacho da direcção do HCN: ____________________________"),
    ]),
]
