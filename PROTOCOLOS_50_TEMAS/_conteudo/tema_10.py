# -*- coding: utf-8 -*-
"""
Tema 10: Conformidade do diagnostico e do tratamento da malaria nao
complicada com as normas nacionais em centros de saude da cidade de Nampula
(Farmacoepidemiologia e Uso Racional de Medicamentos). Estudo documental
retrospectivo, dados de 2026, recolha em 2027.

Compor e validar:   python _motor/motor.py _conteudo/tema_10.py
Verificar fontes:   python _motor/refs.py verificar _conteudo/tema_10.py
"""
from blocos import (CAMPO, FORMULA, H3, LISTA, NOTA, P, PERG, QUADRO,
                    TABELA)

NUMERO = 10
SLUG = "Conformidade_Diagnostico_Tratamento_Malaria_Centros_Saude_Nampula"
TITULO = ("Conformidade do diagnóstico e do tratamento da malária não "
          "complicada com as normas nacionais nos centros de saúde públicos "
          "da cidade de Nampula, 2026")
DESENHO = ("Transversal retrospectivo, descritivo e analítico, documental "
           "(livros de registo de consultas externas e de laboratório e "
           "receitas arquivadas)")

AUTOR = "[Nome do(a) estudante]"
ORIENTADOR = "[Nome e grau académico do(a) orientador(a)]"

# ---------------------------------------------------------------- resumo --
RESUMO = (
    "A malária é a causa mais frequente de procura das consultas externas em "
    "Moçambique, e as normas nacionais exigem que o tratamento antimalárico "
    "seja precedido de confirmação parasitológica e que a dose de "
    "arteméter-lumefantrina corresponda ao peso ou à idade do doente. "
    "Estudos feitos noutras províncias encontraram doentes com teste "
    "negativo tratados com antimaláricos e doentes incapazes de repetir as "
    "instruções de dose, mas não se encontrou nenhuma avaliação publicada "
    "destas práticas nos centros de saúde da cidade de Nampula, capital da "
    "província com a prevalência de malária infantil mais elevada do país. "
    "O estudo tem como objectivo avaliar a conformidade do diagnóstico e do "
    "tratamento da malária não complicada com as normas nacionais nos "
    "centros de saúde públicos da cidade de Nampula. Trata-se de um estudo "
    "transversal, retrospectivo, descritivo e analítico, baseado nos livros "
    "de registo das consultas externas e do laboratório e nas receitas "
    "arquivadas, relativos ao período de 1 de Janeiro a 31 de Dezembro de "
    "2026, com recolha em 2027. Serão analisados 1.081 episódios, "
    "seleccionados por amostragem sistemática estratificada por centro e "
    "por mês: 641 episódios com prescrição de antimalárico e 440 episódios "
    "com teste negativo, números que incluem um efeito de desenho de 1,5 e "
    "uma margem de 10% para registos inutilizáveis. Os dados serão "
    "registados numa ficha sem identificadores, validada por um painel de "
    "peritos, com dupla extracção de 10% dos episódios. Serão estimadas, com "
    "intervalos de confiança a 95%, as proporções de tratamentos "
    "confirmados, de doentes com teste negativo tratados e de prescrições "
    "com dose conforme, e os factores associados ao sobretratamento e aos "
    "erros de dose serão analisados por regressão logística multinível. "
    "Espera-se obter uma linha de base local que oriente a formação, a "
    "supervisão e o abastecimento de testes e de antimaláricos.")
PALAVRAS_CHAVE = ["arteméter-lumefantrina", "malária", "Moçambique",
                  "testes de diagnóstico rápido",
                  "uso racional de medicamentos"]
ABSTRACT = (
    "Malaria is the most frequent reason for outpatient visits in "
    "Mozambique, and the national guidelines require antimalarial treatment "
    "to be preceded by parasitological confirmation and the "
    "artemether-lumefantrine dose to match the patient's weight or age. "
    "Studies in other provinces found patients with negative tests treated "
    "with antimalarials and patients unable to repeat the dosing "
    "instructions, but no published assessment of these practices was found "
    "for the health centres of Nampula City, capital of the province with "
    "the highest childhood malaria prevalence in the country. This study "
    "aims to assess the conformity of the diagnosis and treatment of "
    "uncomplicated malaria with the national guidelines in the public health "
    "centres of Nampula City. It is a cross-sectional, retrospective, "
    "descriptive and analytical study based on the outpatient and laboratory "
    "registers and on archived prescriptions for the period from 1 January "
    "to 31 December 2026, with data collection in 2027. A total of 1,081 "
    "episodes will be analysed, selected by systematic sampling stratified "
    "by health centre and month: 641 episodes with an antimalarial "
    "prescription and 440 episodes with a negative test, figures that "
    "include a design effect of 1.5 and a 10% margin for unusable records. "
    "Data will be recorded on a form without identifiers, validated by an "
    "expert panel, with double extraction of 10% of the episodes. The "
    "proportions of confirmed treatments, of test-negative patients treated "
    "and of prescriptions with a conforming dose will be estimated with 95% "
    "confidence intervals, and the factors associated with overtreatment "
    "and dosing errors will be analysed by multilevel logistic regression. "
    "The study is expected to provide a local baseline to guide training, "
    "supervision and the supply of tests and antimalarials.")
KEYWORDS = ["artemether-lumefantrine", "malaria", "Mozambique",
            "rapid diagnostic tests", "rational drug use"]

# Só as siglas efectivamente usadas no texto; forma extensa na 1.ª ocorrência.
ABREVIATURAS = [
    ("AL", "arteméter-lumefantrina"),
    ("ASAQ", "artesunato-amodiaquina"),
    ("CCI", "coeficiente de correlação intraclasse"),
    ("CIBS-UniLúrio", "Comité Institucional de Bioética para a Saúde da "
                      "Universidade Lúrio"),
    ("CIOMS", "Council for International Organizations of Medical Sciences "
              "(Conselho das Organizações Internacionais de Ciências "
              "Médicas)"),
    ("CNBS", "Comité Nacional de Bioética para a Saúde"),
    ("DEFF", "efeito de desenho (do inglês design effect)"),
    ("DPS", "Direcção Provincial de Saúde"),
    ("HRP2", "proteína rica em histidina 2 (do inglês histidine-rich "
             "protein 2)"),
    ("IC95%", "intervalo de confiança a 95%"),
    ("IDS", "Inquérito Demográfico e de Saúde"),
    ("IVC", "índice de validade de conteúdo"),
    ("OMS", "Organização Mundial da Saúde"),
    ("OR", "odds ratio (razão de possibilidades)"),
    ("ORa", "odds ratio ajustado"),
    ("PNCM", "Programa Nacional de Controlo da Malária"),
    ("RECORD", "REporting of studies Conducted using Observational "
               "Routinely-collected health Data"),
    ("SDSMAS", "Serviço Distrital de Saúde, Mulher e Acção Social"),
    ("SPSS", "Statistical Package for the Social Sciences"),
    ("STROBE", "Strengthening the Reporting of Observational Studies in "
               "Epidemiology"),
    ("TCA", "terapia combinada à base de artemisinina"),
    ("TDR", "teste de diagnóstico rápido"),
]

# ------------------------------------------------------------ referencias --
# Geradas por _motor/refs.py (doi, pmid, web). Não editar à mão.
FONTES = {
    # --- documentos oficiais --------------------------------------------
    "oms_wmr2025": "World Health Organization. World malaria report 2025: addressing the threat of antimalarial drug resistance [Internet]. Geneva: World Health Organization; 2025 [citado 2026 Set 19]. Disponível em: https://www.who.int/teams/global-malaria-programme/reports/world-malaria-report-2025",
    "oms_directrizes2026": "World Health Organization. WHO guidelines for malaria, 10 September 2026 [Internet]. Geneva: World Health Organization; 2026 [citado 2026 Set 19]. Disponível em: https://www.who.int/publications/i/item/guidelines-for-malaria",
    "misau_normas2017": "Ministério da Saúde de Moçambique, Programa Nacional de Controlo da Malária. Normas de tratamento da malária em Moçambique. 3.ª ed [Internet]. Maputo: Ministério da Saúde; 2017 [citado 2026 Set 19]. Disponível em: https://platform.who.int/docs/default-source/mca-documents/policy-documents/guideline/MOZ-CH-33-01-GUIDELINE-2017-prt-Normas-Tratamento-Malaria.pdf",
    "misau_manual2017": "Ministério da Saúde de Moçambique, Programa Nacional de Controlo da Malária. Manejo de casos de malária em Moçambique: manual do participante [Internet]. Maputo: Ministério da Saúde; 2017 [citado 2026 Set 19]. Disponível em: https://docs.bvsalud.org/biblioref/2021/11/1344376/manejo-de-casos-de-malaria-em-mocambique.pdf",
    "ine_ids2024": "Instituto Nacional de Estatística, ICF. Moçambique Inquérito Demográfico e de Saúde 2022-23: relatório definitivo [Internet]. Maputo e Rockville: Instituto Nacional de Estatística e ICF; 2024 [citado 2026 Set 19]. Disponível em: https://dhsprogram.com/publications/publication-FR389-DHS-Final-Reports.cfm",
    "cioms2016": "Council for International Organizations of Medical Sciences. International ethical guidelines for health-related research involving humans [Internet]. Geneva: CIOMS; 2016 [citado 2026 Set 19]. Disponível em: https://cioms.ch/publications/product/international-ethical-guidelines-for-health-related-research-involving-humans/",
    # --- Moçambique -----------------------------------------------------
    "candrinho2019": "Candrinho B, Plucinski MM, Colborn JM, da Silva M, Mathe G, Dimene M, et al. Quality of malaria services offered in public health facilities in three provinces of Mozambique: a cross-sectional study. Malar J. 2019;18(1):162. doi:10.1186/s12936-019-2796-9. PMID: 31060605.",
    "colborn2020": "Colborn JM, Zulliger R, Da Silva M, Mathe G, Chico AR, Castel-Branco AC, et al. Quality of malaria data in public health facilities in three provinces of Mozambique. PLoS One. 2020;15(4):e0231358. doi:10.1371/journal.pone.0231358. PMID: 32310983.",
    "baraka2023": "Baraka V, Nhama A, Aide P, Bassat Q, David A, Gesase S, et al. Prescription patterns and compliance with World Health Organization recommendations for the management of uncomplicated and severe malaria: A prospective, real-world study in sub-Saharan Africa. Malar J. 2023;22(1):215. doi:10.1186/s12936-023-04650-y. PMID: 37491295.",
    "dasilva2024": "da Silva C, Tembisse D, Cisteró P, Rovira-Vallbona E, Canana N, da Costa P, et al. Molecular surveillance of Plasmodium falciparum histidine-rich protein 2/3 gene deletions in Mozambique, 2023. Malar J. 2024;23(1):402. doi:10.1186/s12936-024-05230-4. PMID: 39725959.",
    "nhama2025": "Nhama A, Chidimatembue A, Nhamussua L, Bassat Q, da Silva C, Nhacolo A, et al. Efficacy of artemether-lumefantrine, artesunate-amodiaquine, dihydroartemisinin-piperaquine and artesunate-pyronaridine for the treatment of uncomplicated Plasmodium falciparum malaria in Mozambique, 2022. Malar J. 2025;24(1):231. doi:10.1186/s12936-025-05473-9. PMID: 40660279.",
    "nhama2026": "Nhama A, Aide P, Torres-Fernandez D, Varo R, Nhacolo A, Bassat Q. Efficacy of artemether-lumefantrine for uncomplicated plasmodium falciparum malaria treatment in mozambique: a systematic review and meta-analysis. Malar J. 2026;25(1). doi:10.1186/s12936-026-05931-y. PMID: 42174576.",
    "baker2025": "Baker K, Pulido Tarquino IA, Aide P, Bonnington C, Rassi C, Richardson S, et al. Phase one of a hybrid effectiveness-implementation study to assess the feasibility, acceptability and effectiveness of implementing seasonal malaria chemoprevention in Nampula Province, Mozambique. Malar J. 2025;24(1):56. doi:10.1186/s12936-024-05229-x. PMID: 39985013.",
    "cassy2019": "Cassy A, Saifodine A, Candrinho B, Martins MDR, da Cunha S, Pereira FM, et al. Care-seeking behaviour and treatment practices for malaria in children under 5 years in Mozambique: a secondary analysis of 2011 DHS and 2015 IMASIDA datasets. Malar J. 2019;18(1):115. doi:10.1186/s12936-019-2751-9. PMID: 30940127.",
    "siyam2021": "Siyam A, Ir P, York D, Antwi J, Amponsah F, Rambique O, et al. The burden of recording and reporting health data in primary health care facilities in five low- and lower-middle income countries. BMC Health Serv Res. 2021;21(Suppl 1):691. doi:10.1186/s12913-021-06652-5. PMID: 34511083.",
    "xavier2022": "Xavier SP, Victor A, Cumaquela G, Vasco MD, Rodrigues OAS. Inappropriate use of antibiotics and its predictors in pediatric patients admitted at the Central Hospital of Nampula, Mozambique. Antimicrob Resist Infect Control. 2022;11(1):79. doi:10.1186/s13756-022-01115-w. PMID: 35655272.",
    # --- África subsariana ----------------------------------------------
    "davlantes2019": "Davlantes E, Camara A, Guilavogui T, Fofana A, Balde M, Diallo T, et al. Quality of Malaria Case Management and Reporting at Public Health Facilities in Six Health Districts in Guinea, 2018. Am J Trop Med Hyg. 2019;101(1):148-156. doi:10.4269/ajtmh.19-0150. PMID: 31074408.",
    "worges2019": "Worges M, Celone M, Finn T, Chisha Z, Winters A, Winters B, et al. Malaria case management in Zambia: A cross-sectional health facility survey. Acta Trop. 2019;195:83-89. doi:10.1016/j.actatropica.2019.04.032. PMID: 31054287.",
    "amboko2022": "Amboko B, Stepniewska K, Machini B, Bejon P, Snow RW, Zurovac D. Factors influencing health workers' compliance with outpatient malaria 'test and treat' guidelines during the plateauing performance phase in Kenya, 2014-2016. Malar J. 2022;21(1):68. doi:10.1186/s12936-022-04093-x. PMID: 35241074.",
    "amboko2021": "Amboko B, Stepniewska K, Malla L, Machini B, Bejon P, Snow RW, et al. Determinants of improvement trends in health workers' compliance with outpatient malaria case-management guidelines at health facilities with available 'test and treat' commodities in Kenya. PLoS One. 2021;16(11):e0259020. doi:10.1371/journal.pone.0259020. PMID: 34739519.",
    "chukwuka2024": "Chukwuka UB, Ibeh CC, Adogu PO, Chukwuka JO. Funding and compliance to Test-Before-Treat recommendation in management of uncomplicated malaria among primary health care workers in Anambra State, Nigeria - a cross-sectional comparative study. Pan Afr Med J. 2024;49:65. doi:10.11604/pamj.2024.49.65.41337. PMID: 39958569.",
    "camara2019": "Camara A, Moriarty LF, Guilavogui T, Diakité PS, Zoumanigui JS, Sidibé S, et al. Prescriber practices and patient adherence to artemisinin-based combination therapy for the treatment of uncomplicated malaria in Guinea, 2016. Malar J. 2019;18(1):23. doi:10.1186/s12936-019-2664-7. PMID: 30683128.",
    "mpimbaza2022": "Mpimbaza A, Babikako H, Rutazanna D, Karamagi C, Ndeezi G, Katahoire A, et al. Adherence to malaria management guidelines by health care workers in the Busoga sub-region, eastern Uganda. Malar J. 2022;21(1):25. doi:10.1186/s12936-022-04048-2. PMID: 35078479.",
    "klootwijk2019": "Klootwijk L, Chirwa AE, Kabaghe AN, van Vugt M. Challenges affecting prompt access to adequate uncomplicated malaria case management in children in rural primary health facilities in Chikhwawa Malawi. BMC Health Serv Res. 2019;19(1):735. doi:10.1186/s12913-019-4544-9. PMID: 31640676.",
    "koliopoulos2024": "Koliopoulos P, Kayange N, Jensen C, Gröndahl B, Eichmann J, Daniel T, et al. Challenges in Diagnosing and Treating Acutely Febrile Children with Suspected Malaria at Health Care Facilities in the Lake Mwanza Region of Tanzania. Am J Trop Med Hyg. 2024;110(2):202-208. doi:10.4269/ajtmh.23-0254. PMID: 38150741.",
    "atobatele2025": "Atobatele S, Sampson S, Orya E, Okoro O, Akpiroroh E, Okagbue H, et al. Accuracy of recording and reporting of malaria rapid diagnostic tests in Nigeria. Malar J. 2025;24(1):383. doi:10.1186/s12936-025-05601-5. PMID: 41204290.",
    "bediatanoh2026": "Bedia-Tanoh VA, Konaté-Touré A, Kangah-Kouakou OMA, Mian ANN, Tanoh AM, Humes M, et al. Accuracy of recording of malaria rapid diagnostic tests in Côte d'Ivoire. Malar J. 2026;25(1):80. doi:10.1186/s12936-025-05766-z. PMID: 41501730.",
    "nauzo2020": "Na'uzo AM, Tukur D, Sufiyan MB, Stephen AA, Ajayi I, Bamgboye E, et al. Adherence to malaria rapid diagnostic test result among healthcare workers in Sokoto metropolis, Nigeria. Malar J. 2020;19(1):2. doi:10.1186/s12936-019-3094-2. PMID: 31898498.",
    "akinyode2018": "Akinyode AO, Ajayi IO, Ibrahim MS, Akinyemi JO, Ajumobi OO. Practice of antimalarial prescription to patients with negative rapid test results and associated factors among health workers in Oyo State, Nigeria. Pan Afr Med J. 2018;30:229. doi:10.11604/pamj.2018.30.229.13231. PMID: 30574247.",
    # --- evidência global -----------------------------------------------
    "maze2018": "Maze MJ, Bassat Q, Feasey NA, Mandomando I, Musicha P, Crump JA. The epidemiology of febrile illness in sub-Saharan Africa: implications for diagnosis and management. Clin Microbiol Infect. 2018;24(8):808-814. doi:10.1016/j.cmi.2018.02.011. PMID: 29454844.",
    "bruxvoort2017": "Bruxvoort KJ, Leurent B, Chandler CIR, Ansah EK, Baiden F, Björkman A, et al. The Impact of Introducing Malaria Rapid Diagnostic Tests on Fever Case Management: A Synthesis of Ten Studies from the ACT Consortium. Am J Trop Med Hyg. 2017;97(4):1170-1179. doi:10.4269/ajtmh.16-0955. PMID: 28820705.",
    "hopkins2017": "Hopkins H, Bruxvoort KJ, Cairns ME, Chandler CI, Leurent B, Ansah EK, et al. Impact of introduction of rapid diagnostic tests for malaria on antibiotic prescribing: analysis of observational and randomised studies in public and private healthcare settings. BMJ. 2017;356:j1054. doi:10.1136/bmj.j1054. PMID: 28356302.",
    "zhang2024": "Zhang H, Fink G, Cohen J. Malaria Rapid Tests, Febrile Illness Management, and Child Mortality Across Sub-Saharan African Countries. JAMA. 2024;332(15):1270-1281. doi:10.1001/jama.2024.12589. PMID: 39292453.",
    "kloprogge2018": "Kloprogge F, Workman L, Borrmann S, Tékété M, Lefèvre G, Hamed K, et al. Artemether-lumefantrine dosing for malaria treatment in young children and pregnant women: A pharmacokinetic-pharmacodynamic meta-analysis. PLoS Med. 2018;15(6):e1002579. doi:10.1371/journal.pmed.1002579. PMID: 29894518.",
    "martinezvega2026": "Martinez-Vega R, Ishengoma DS, Gosling R. Emerging Artemisinin Partial Resistance in Southern Africa. Am J Trop Med Hyg. 2026. doi:10.4269/ajtmh.25-0417. PMID: 41843934.",
    # --- métodos e ética --------------------------------------------------
    "helsinki2025": "World Medical Association. World Medical Association Declaration of Helsinki: Ethical Principles for Medical Research Involving Human Participants. JAMA. 2025;333(1):71-74. doi:10.1001/jama.2024.21972. PMID: 39425955.",
    "strobe2007": "von Elm E, Altman DG, Egger M, Pocock SJ, Gøtzsche PC, Vandenbroucke JP. The Strengthening the Reporting of Observational Studies in Epidemiology (STROBE) statement: guidelines for reporting observational studies. PLoS Med. 2007;4(10):e296. doi:10.1371/journal.pmed.0040296. PMID: 17941714.",
    "record2015": "Benchimol EI, Smeeth L, Guttmann A, Harron K, Moher D, Petersen I, et al. The REporting of studies Conducted using Observational Routinely-collected health Data (RECORD) statement. PLoS Med. 2015;12(10):e1001885. doi:10.1371/journal.pmed.1001885. PMID: 26440803.",
    "landis1977": "Landis JR, Koch GG. The Measurement of Observer Agreement for Categorical Data. Biometrics. 1977;33(1):159. doi:10.2307/2529310",
    "peduzzi1996": "Peduzzi P, Concato J, Kemper E, Holford TR, Feinstein AR. A simulation study of the number of events per variable in logistic regression analysis. J Clin Epidemiol. 1996;49(12):1373-9. doi:10.1016/s0895-4356(96)00236-3. PMID: 8970487.",
    "serdar2021": "Serdar CC, Cihan M, Yücel D, Serdar MA. Sample size, power and effect size revisited: simplified and practical approaches in pre-clinical, clinical and laboratory studies. Biochem Med (Zagreb). 2021;31(1):010502. doi:10.11613/BM.2021.010502. PMID: 33380887.",
    "almanasreh2019": "Almanasreh E, Moles R, Chen TF. Evaluation of methods used for estimating content validity. Res Social Adm Pharm. 2019;15(2):214-221. doi:10.1016/j.sapharm.2018.03.066. PMID: 29606610.",
}
# Referências anteriores a 2016: só fontes seminais, com o motivo.
SEMINAIS = {
    "strobe2007": "Declaração de relato de estudos observacionais em vigor, "
                  "base da extensão RECORD",
    "record2015": "Declaração de relato em vigor para estudos com dados de "
                  "saúde colhidos por rotina (desenho deste estudo)",
    "landis1977": "Artigo original da escala de interpretação do kappa de "
                  "Cohen usada no controlo de qualidade",
    "peduzzi1996": "Estudo de simulação que fundamenta o critério de 10 "
                   "eventos por variável na regressão logística",
}

# ----------------------------------------------------- 1. introducao --------
INTRODUCAO = [
    P("A malária continua a ser uma das principais causas de doença e de "
      "morte evitáveis no mundo. Segundo o relatório mundial da malária de "
      "2025 da Organização Mundial da Saúde (OMS), registaram-se em 2024 "
      "cerca de 282 milhões de casos e 610 mil mortes, mais do que os 273 "
      "milhões de casos de 2023 {oms_wmr2025}. A Região Africana da OMS "
      "concentrou 94% dos casos e 95% das mortes, e três em cada quatro "
      "mortes na região ocorreram em crianças com menos de 5 anos. Cerca de "
      "dois terços dos casos e das mortes do mundo concentram-se em onze "
      "países africanos de alta carga, entre os quais Moçambique "
      "{oms_wmr2025}, que responde sozinho por cerca de 4% dos casos globais "
      "{baker2025}."),
    P("O manejo de casos é, a par da prevenção, o pilar que mais "
      "directamente reduz a mortalidade. Como os sinais e sintomas da "
      "malária são inespecíficos, a OMS recomenda que todos os casos "
      "suspeitos façam um teste parasitológico, por microscopia ou por teste "
      "de diagnóstico rápido (TDR), que o tratamento antimalárico se limite "
      "aos casos com teste positivo e que os doentes com teste negativo sejam "
      "reavaliados à procura de outras causas de febre {oms_directrizes2026}. "
      "A recomendação tem razão de ser: nos doentes ambulatórios da África "
      "subsariana, as infecções respiratórias virais e as arboviroses de "
      "evolução benigna estão presentes em até 60% das crianças atendidas nos "
      "centros de saúde, e as infecções bacterianas graves exigem tratamento "
      "específico {maze2018}. Confirmado o diagnóstico, a eficácia da terapia "
      "combinada à base de artemisinina (TCA) depende de doses correctas, "
      "calculadas pelo peso, e do cumprimento das seis tomas do tratamento "
      "com arteméter-lumefantrina (AL) {oms_directrizes2026}."),
    P("A introdução dos TDR não eliminou, contudo, o tratamento "
      "desnecessário. Numa síntese de dez estudos de um consórcio "
      "internacional de investigação, com 562.368 consultas, houve contextos "
      "em que mais de 30% dos doentes com teste negativo receberam uma TCA, "
      "e a redução dos antimaláricos foi em parte compensada por mais "
      "antibióticos {bruxvoort2017}; nesses estudos, 69% dos doentes com "
      "teste negativo receberam antibiótico {hopkins2017}. À escala do "
      "continente, a maior distribuição de TDR associou-se a mais testes e a "
      "uma redução modesta da mortalidade infantil, mas também a mais "
      "antibióticos {zhang2024}. Estas práticas pesam mais num momento em "
      "que a resistência parcial à artemisinina está confirmada na Eritreia, "
      "no Ruanda, no Uganda e na Tanzânia {oms_wmr2025} e em que surgiu um "
      "novo foco no sul do continente, em Angola, na Namíbia e na Zâmbia "
      "{martinezvega2026}: cada tratamento desnecessário ou em dose "
      "insuficiente aumenta a pressão de selecção sobre os poucos "
      "medicamentos eficazes de que o país dispõe."),
    P("Em Moçambique, a malária é a causa mais frequente de procura de "
      "cuidados nas consultas externas e no internamento {misau_normas2017} "
      "e a principal causa de morte nas crianças com menos de 5 anos "
      "{ine_ids2024}. No Inquérito Demográfico e de Saúde (IDS) de 2022-23, "
      "32% das crianças de 6 a 59 meses tinham malária pelo TDR, com 40% na "
      "área rural e 12% na área urbana, e Nampula foi a província com a "
      "prevalência mais alta, 55% {ine_ids2024}. As Normas de Tratamento da "
      "Malária em Moçambique, na terceira edição, de 2017, determinam que o "
      "TDR seja feito a todos os doentes com febre ou suspeita de malária, "
      "que o antimalárico seja dispensado apenas aos doentes com resultado "
      "positivo, salvo quando não houver meios de diagnóstico, e que o AL "
      "seja administrado de 12 em 12 horas durante três dias, em dose "
      "ajustada ao peso ou à idade {misau_normas2017}. O AL mantém-se eficaz "
      "no país, com uma eficácia agregada, corrigida por genotipagem, de "
      "98,3% {nhama2026}, o que coloca na qualidade da prescrição, e não na "
      "escolha do medicamento, o ponto crítico do manejo."),
    P("A evidência moçambicana sobre a qualidade deste manejo é escassa e "
      "tem quase uma década. Num inquérito de 2018 em 117 unidades sanitárias "
      "das províncias de Maputo, Zambézia e Cabo Delgado, apenas 49% a 52% "
      "dos casos febris confirmados das duas províncias de alta transmissão "
      "foram manejados de forma adequada, isto é, testados e tratados com a "
      "dose correcta, e entre 8% e 22% dos doentes com teste negativo "
      "receberam antimalárico {candrinho2019}. O mesmo inquérito mostrou que "
      "os livros de registo das unidades omitem muitos testes negativos e "
      "divergem dos dados agregados do sistema de informação {colborn2020}. "
      "Nenhum destes estudos incluiu a província de Nampula, e não se "
      "encontrou avaliação publicada da conformidade do diagnóstico e do "
      "tratamento da malária nos centros de saúde da cidade de Nampula."),
    P("Este protocolo propõe um estudo documental retrospectivo nos centros "
      "de saúde públicos da cidade de Nampula, com base nos livros de "
      "registo das consultas externas e do laboratório e nas receitas "
      "arquivadas relativos a 2026, para verificar se o tratamento "
      "antimalárico foi precedido de confirmação parasitológica, se os "
      "doentes com teste negativo foram poupados a antimaláricos e se a dose "
      "de AL correspondeu ao peso ou à idade do doente. Na perspectiva da "
      "farmácia, o estudo incide sobre o uso racional de um medicamento "
      "essencial e sobre erros de medicação evitáveis, que o farmacêutico "
      "pode ajudar a detectar e a corrigir no momento da dispensa."),
]

# ----------------------------------------------------- 2. problema ----------
PROBLEMA = [
    P("Os centros de saúde da cidade de Nampula atendem, nas consultas "
      "externas, um grande número de doentes com febre, vindos de bairros "
      "urbanos e periurbanos de uma província em que a malária é endémica e "
      "em que a prevalência infantil é a mais alta do país {ine_ids2024}. "
      "Numa cidade, porém, a transmissão é mais baixa do que no meio rural, e "
      "uma parte considerável das febres tem outra causa. É nestas condições "
      "que a regra de testar antes de tratar tem maior valor e, também, que é "
      "mais desrespeitada: no Quénia, a melhoria do cumprimento do «testar e "
      "tratar» foi mais lenta nas zonas de baixo risco {amboko2021}, e em "
      "Moçambique a província de baixa transmissão, Maputo, teve a proporção "
      "mais baixa de casos bem manejados, 14% {candrinho2019}. Muitos "
      "profissionais continuam a acreditar que um TDR negativo pode falhar a "
      "malária e que o tratamento ainda se justifica {bediatanoh2026}. O "
      "resultado é o sobretratamento: o doente recebe AL, a causa verdadeira "
      "da febre fica por tratar, os stocks de antimaláricos esgotam-se mais "
      "depressa e os dados de vigilância ficam distorcidos, porque o teste "
      "de quem recebe antimalárico tende a ser registado como positivo "
      "{colborn2020,atobatele2025}."),
    P("O segundo problema é a dose. As normas nacionais definem quatro "
      "faixas de peso, com correspondência aproximada em idade, para 1, 2, 3 "
      "ou 4 comprimidos por toma {misau_normas2017}, mas a OMS adverte que a "
      "dosagem pela idade pode causar subdosagem ou sobredosagem, porque a "
      "relação entre idade e peso varia entre populações "
      "{oms_directrizes2026}. No modelo de registo ensinado aos profissionais "
      "moçambicanos, a idade é assinalada em grupos largos (0-4, 5-15 e mais "
      "de 15 anos) e não há campo para o peso {misau_manual2017}. Uma "
      "subdose tem consequências mensuráveis: mesmo com a dose padrão, a "
      "concentração de lumefantrina ao sétimo dia é 24,2% mais baixa nas "
      "crianças com menos de 15 kg do que nos adultos {kloprogge2018}, pelo "
      "que cada comprimido a menos agrava uma exposição que já é limite. Em "
      "Moçambique, só 58% a 62% dos doentes a quem foi prescrito um "
      "antimalárico sabiam repetir correctamente as instruções de dose "
      "{candrinho2019}, e em Nampula mais de um terço das prescrições de "
      "antibióticos num serviço de pediatria continha erros, sobretudo de "
      "duração e de dose {xavier2022}."),
    P("Falta, assim, conhecer a dimensão local do problema. Não se sabe que "
      "proporção dos tratamentos antimaláricos prescritos nos centros de "
      "saúde da cidade é precedida de teste positivo, quantos doentes com "
      "teste negativo recebem AL, com que frequência a dose prescrita não "
      "corresponde ao peso ou à idade, nem se estas falhas se concentram em "
      "certos grupos etários, épocas do ano, métodos de diagnóstico ou meses "
      "de ruptura de stock. Os livros de registo das consultas e do "
      "laboratório, preenchidos todos os dias para a notificação, contêm "
      "grande parte desta informação, mas não são usados para auditar a "
      "qualidade da prescrição. Sem esta linha de base, a formação, a "
      "supervisão e a distribuição de TDR e de AL continuam a ser planeadas "
      "sem saber o que acontece no gabinete de consulta e na farmácia."),
]
PERGUNTA = ("Em que medida o diagnóstico e o tratamento da malária não "
            "complicada registados nas consultas externas dos centros de "
            "saúde públicos da cidade de Nampula em 2026 estão conformes com "
            "as normas nacionais, e que factores se associam ao "
            "sobretratamento de doentes com teste negativo e aos erros de "
            "dose de arteméter-lumefantrina?")
DELIMITACAO = [
    P("O estudo decorre nos centros de saúde públicos da cidade de Nampula "
      "geridos pelo Serviço Distrital de Saúde, Mulher e Acção Social "
      "(SDSMAS) da Cidade de Nampula que tenham consulta externa e "
      "diagnóstico da malária por TDR ou por microscopia. A população são os "
      "episódios de consulta externa de doentes de todas as idades, "
      "registados entre 1 de Janeiro e 31 de Dezembro de 2026, em que foi "
      "prescrito um antimalárico oral ou em que o teste de malária foi "
      "negativo; a consulta dos arquivos decorre em 2027. O objecto é a "
      "conformidade da prescrição registada com as normas nacionais em três "
      "dimensões: a confirmação parasitológica antes do tratamento, a "
      "resposta ao teste negativo e a escolha e a dose do antimalárico."),
    P("Ficam fora do estudo a malária grave e os doentes internados ou "
      "transferidos, as grávidas, para quem as normas nacionais prevêem "
      "outra escolha de medicamento, os casos manejados por agentes "
      "polivalentes "
      "elementares na comunidade, o sector privado, as farmácias comerciais e "
      "os hospitais. O estudo não avalia a adesão do doente ao tratamento, a "
      "evolução clínica, a qualidade técnica da execução dos testes nem os "
      "doentes com teste positivo que não receberam antimalárico, que "
      "exigiriam outro desenho."),
]

# ----------------------------------------------------- 3. objectivos --------
OBJECTIVO_GERAL = (
    "Avaliar a conformidade do diagnóstico e do tratamento da malária não "
    "complicada com as normas nacionais nas consultas externas dos centros "
    "de saúde públicos da cidade de Nampula, entre 1 de Janeiro e 31 de "
    "Dezembro de 2026.")
OBJECTIVOS_ESPECIFICOS = [
    "Caracterizar os episódios de consulta com prescrição de antimalárico ou "
    "com teste de malária negativo segundo o sexo, o grupo etário, o centro "
    "de saúde, a estação do ano e o método de diagnóstico;",
    "Determinar a proporção de tratamentos antimaláricos precedidos de "
    "confirmação parasitológica por TDR ou microscopia e a proporção de "
    "doentes com teste negativo que receberam antimalárico;",
    "Determinar a proporção de prescrições de arteméter-lumefantrina com "
    "dose conforme ao peso ou à idade do doente e descrever os tipos de erro "
    "de dose;",
    "Analisar a associação do sexo, do grupo etário, da estação do ano, do "
    "método de diagnóstico, da base de dosagem e das rupturas de stock com o "
    "sobretratamento de doentes com teste negativo e com os erros de dose de "
    "arteméter-lumefantrina.",
]

# ----------------------------------------------------- 4. hipoteses ---------
HIPOTESES_INTRO = [
    P("As hipóteses referem-se ao objectivo específico 4 e serão testadas "
      "com um nível de significância de 5%, primeiro por análise bivariada e "
      "depois por regressão logística multinível."),
]
HIPOTESES = [
    ("H0 (sobretratamento)",
     "a prescrição de antimalárico a doentes com teste negativo não está "
     "associada ao sexo, ao grupo etário, à estação do ano, ao método de "
     "diagnóstico nem à ruptura de stock de TDR no mês da consulta;"),
    ("H1 (sobretratamento)",
     "pelo menos um destes factores está associado à prescrição de "
     "antimalárico a doentes com teste negativo;"),
    ("H0 (erro de dose)",
     "o erro de dose de AL não está associado ao sexo, ao grupo etário, à "
     "estação do ano, à base de dosagem registada (peso, idade exacta ou "
     "grupo etário) nem à ruptura de stock de AL no mês da consulta;"),
    ("H1 (erro de dose)",
     "pelo menos um destes factores está associado ao erro de dose de AL."),
]
QUESTOES = [
    "Como se distribuem os episódios com prescrição de antimalárico e com "
    "teste negativo por sexo, grupo etário, centro de saúde, estação do ano "
    "e método de diagnóstico?",
    "Que proporção dos tratamentos antimaláricos registados foi precedida de "
    "um teste positivo, e que proporção dos doentes com teste negativo "
    "recebeu antimalárico?",
    "Que proporção das prescrições de AL tem dose conforme ao peso ou à "
    "idade, e qual é o tipo de erro de dose mais frequente?",
]

# ----------------------------------------------------- 5. justificativa -----
JUSTIFICATIVA_INTRO = [
    P("A escolha do tema responde a uma lacuna concreta: as normas "
      "nacionais existem desde 2017 e os TDR e o AL fazem parte da rotina "
      "das consultas externas, mas não há medição local de como a regra de "
      "testar antes de tratar e a tabela de doses são cumpridas nos centros "
      "de saúde de Nampula. A pertinência do estudo articula-se em quatro "
      "dimensões complementares."),
]
JUSTIFICATIVA = {
    "cientifica": [
        P("O estudo produz a primeira estimativa, para a cidade de Nampula, "
          "de três indicadores de qualidade do manejo da malária: a "
          "confirmação antes do tratamento, o sobretratamento de doentes com "
          "teste negativo e a conformidade da dose de AL. A evidência "
          "moçambicana disponível provém de um inquérito de 2018 em três "
          "outras províncias {candrinho2019} e de um estudo prospectivo em "
          "seis países africanos, entre os quais Moçambique, centrado nos "
          "padrões de prescrição {baraka2023}. Acresce um contributo "
          "metodológico: ao ligar o livro de registo à receita e ao comparar "
          "a classificação da dose pelo peso e pela idade, o estudo testa a "
          "utilidade dos registos de rotina para auditar a prescrição, cuja "
          "validade tem sido questionada {colborn2020,bediatanoh2026}."),
    ],
    "academica": [
        P("Para a Licenciatura em Farmácia da Universidade Lúrio, o estudo "
          "aplica os métodos da farmacoepidemiologia (amostragem de "
          "registos, definições operacionais, dupla extracção, concordância "
          "entre avaliadores e regressão multinível) a um problema de uso "
          "racional de medicamentos de grande frequência. A ficha de "
          "extracção e as regras de classificação da dose ficam disponíveis "
          "para estudos noutros distritos e para o ensino da dispensa e da "
          "farmácia clínica."),
    ],
    "social": [
        P("Um doente com febre sem malária que recebe AL fica sem tratamento "
          "para a causa real da febre, que pode ser uma infecção bacteriana "
          "grave {maze2018}, e o dinheiro público gasto em antimaláricos e "
          "em antibióticos desnecessários {hopkins2017} deixa de estar "
          "disponível para outros cuidados. Nas crianças, a subdose reduz a "
          "exposição à lumefantrina num grupo que já tem concentrações mais "
          "baixas {kloprogge2018}, e a sobredose aumenta a exposição a efeitos "
          "adversos sem benefício. Identificar estes erros permite corrigi-los "
          "onde acontecem, no gabinete de consulta e no balcão da farmácia, "
          "em benefício directo dos utentes dos centros de saúde da cidade."),
    ],
    "politica": [
        P("Os resultados interessam ao Programa Nacional de Controlo da "
          "Malária (PNCM), à Direcção Provincial de Saúde (DPS) de Nampula e "
          "ao SDSMAS, que planeiam a formação, a supervisão e as necessidades "
          "de TDR e de AL. O relatório mundial de 2025 regista uma queda de "
          "21% da ajuda pública ao desenvolvimento destinada à malária e o "
          "consequente risco de rupturas de stock {oms_wmr2025}, o que torna "
          "cada tratamento desnecessário um desperdício que o país não pode "
          "suportar. Os dados servem ainda a actualização das normas "
          "nacionais de 2017, que prevêem quinino oral no primeiro trimestre "
          "da gravidez e o manejo como malária grave das crianças com menos "
          "de 5 kg {misau_normas2017}, pontos em que as directrizes da OMS "
          "mudaram entretanto, com o AL recomendado no primeiro trimestre "
          "desde 2022 e uma formulação própria para lactentes com menos de "
          "5 kg {oms_directrizes2026}."),
    ],
}

# ----------------------------------------------------- 6. revisao -----------
REVISAO = [
    ("Malária não complicada: conceito, definições de caso e definição "
     "operacional", [
        P("A malária é uma doença infecciosa causada por protozoários do "
          "género *Plasmodium*, transmitidos pela picada de mosquitos do "
          "género *Anopheles*; das quatro espécies que infectam habitualmente "
          "o ser humano, *Plasmodium falciparum* é responsável pela maioria "
          "dos casos graves e das mortes {misau_normas2017}. A malária não "
          "complicada define-se como a infecção sintomática sem sinais de "
          "gravidade nem evidência clínica ou laboratorial de disfunção de "
          "órgão vital. Manifesta-se por febre, com temperatura axilar igual "
          "ou superior a 37,5 °C, ou história de febre, cefaleias, mialgias, "
          "arrepios, vómitos ou diarreia, e nenhuma combinação destes sinais "
          "a distingue de forma fiável de outras doenças febris; por isso, o "
          "diagnóstico apenas clínico tem especificidade muito baixa e leva "
          "ao sobretratamento {misau_normas2017,oms_directrizes2026}."),
        P("Para o registo e a notificação, o PNCM adoptou as definições de "
          "caso da OMS. Caso suspeito é o doente com sintomas sugestivos de "
          "malária; caso confirmado, o que tem microscopia ou TDR positivos; "
          "malária clínica ou presuntiva, o doente que não foi testado por "
          "falta de meios mas foi tratado com antimaláricos; e «não é "
          "malária», o doente com sintomas sugestivos e teste negativo "
          "{misau_manual2017}. Estas categorias permitem classificar cada "
          "episódio a partir do livro de registo, sem observar a consulta, e "
          "são a base das definições deste estudo."),
        P("Neste estudo, conformidade é a correspondência entre o diagnóstico "
          "e a prescrição registados e o que as normas nacionais determinam "
          "para o mesmo doente. Define-se sobretratamento como a prescrição "
          "de antimalárico a um doente com teste negativo; tratamento "
          "presuntivo, como a prescrição sem teste registado, justificada "
          "apenas quando houver ruptura de TDR documentada; e erro de dose, "
          "como a prescrição de AL com um número de comprimidos por toma "
          "diferente do previsto para o peso ou a idade, ou com menos de seis "
          "tomas. Os critérios completos constam do [[quadro:criterios]], na "
          "metodologia."),
    ]),
    ("Magnitude do problema e consequências do sobretratamento e dos erros "
     "de dose", [
        P("A prevalência da malária nas crianças moçambicanas com menos de "
          "5 anos manteve-se entre 38% e 40% de 2011 a 2018 e desceu para 32% "
          "em 2022-23, mantendo-se mais de três vezes maior na área rural do "
          "que na área urbana {ine_ids2024}. Entre as crianças com "
          "febre nas duas semanas "
          "anteriores ao inquérito, 51% tiveram sangue colhido para teste, e "
          "94% das que procuraram cuidados recorreram ao sector público "
          "{ine_ids2024}; a procura de cuidados para a febre infantil "
          "rondava os dois terços em 2011 e 2015, sobretudo em unidades "
          "públicas {cassy2019}. É, portanto, nas unidades sanitárias "
          "públicas que se decide a maior parte do diagnóstico e do "
          "tratamento."),
        P("O sobretratamento tem três tipos de consequência. Para o doente, "
          "atrasa o diagnóstico da causa verdadeira da febre, que nos "
          "ambulatórios é muitas vezes viral mas pode ser uma bacteriemia ou "
          "uma zoonose {maze2018}. Para o sistema de saúde, desloca o "
          "consumo para medicamentos desnecessários: quando o antimalárico é "
          "retirado, tende a ser substituído por antibióticos, prescritos a "
          "69% dos doentes com teste negativo nos estudos do consórcio atrás "
          "referido {hopkins2017}. Para a vigilância, inflaciona os casos "
          "confirmados, porque os profissionais tendem a registar como "
          "positivo o teste de quem recebeu antimalárico "
          "{atobatele2025,bediatanoh2026}, e os dados de rotina passam a "
          "sobrestimar a carga de malária."),
        P("Os erros de dose têm consequências farmacológicas previsíveis. A "
          "eficácia do AL depende de concentrações de lumefantrina "
          "suficientes durante tempo suficiente; a absorção da lumefantrina "
          "é limitada pela dose {kloprogge2018} e melhora quando o comprimido "
          "é tomado com alimentos gordos {misau_normas2017}. A subdose e o "
          "esquema incompleto favorecem a falência terapêutica e a selecção "
          "de parasitas resistentes, razão pela qual as normas nacionais "
          "incluem a dose insuficiente entre as causas de falência "
          "{misau_normas2017} e a OMS exige que o regime garanta exposição "
          "semelhante em todos os grupos de doentes {oms_directrizes2026}. "
          "A sobredose não traz benefício terapêutico e aumenta a exposição "
          "aos efeitos adversos descritos para o medicamento, como dor "
          "abdominal, náuseas, vómitos, cefaleias e tonturas "
          "{misau_normas2017}."),
    ]),
    ("Diagnóstico parasitológico: testes de diagnóstico rápido e "
     "microscopia", [
        P("O diagnóstico parasitológico faz-se por microscopia óptica da "
          "gota espessa e do esfregaço ou por TDR imunocromatográficos, e "
          "ambos devem estar sujeitos a um programa de garantia de qualidade "
          "{oms_directrizes2026}. Em Moçambique, dada a predominância de "
          "*P. falciparum*, as normas preferem os TDR baseados na proteína "
          "rica em histidina 2 (HRP2), que devem ser feitos no ponto de "
          "entrada do doente, na triagem ou no banco de socorros; a "
          "microscopia fica reservada para a suspeita de malária grave, o "
          "seguimento de internados, a suspeita de falência terapêutica e os "
          "doentes com TDR negativo e sintomas persistentes "
          "{misau_normas2017}. Como o TDR baseado na HRP2 pode manter-se "
          "positivo até quatro semanas depois do tratamento, não serve para "
          "controlar a cura {misau_normas2017}."),
        P("A qualidade do teste condiciona a confiança do clínico. Na "
          "Tanzânia, em crianças febris, a microscopia de rotina teve "
          "sensibilidade de 33% e o TDR de 87%, tomando como referência um "
          "método molecular; onde o tratamento seguia o TDR, 7% das crianças "
          "sem malária receberam antimaláricos, contra 75% nas unidades que "
          "usavam a microscopia {koliopoulos2024}. Na Zâmbia, os técnicos de "
          "laboratório tiveram sensibilidade de 65,5% e especificidade de "
          "86,0% na microscopia {worges2019}. A deleção dos genes *pfhrp2* e "
          "*pfhrp3* pode produzir falsos negativos no TDR; foi descrita em 42 "
          "países endémicos, e a OMS recomenda mudar de teste quando a sua "
          "prevalência ultrapassa 5% {oms_wmr2025}. Em Moçambique, no "
          "inquérito molecular de 2023, a prevalência de deleções confirmadas "
          "foi de 0,16% nas seis províncias estudadas e de 0,27% em Nampula, "
          "muito abaixo desse limiar {dasilva2024}, pelo que as deleções não "
          "explicam, no país, a desconfiança nos resultados negativos."),
        P("A resposta ao teste negativo é o elo mais frágil do manejo. A "
          "proporção de doentes com teste negativo que recebe antimaláricos "
          "ultrapassou 30% em vários contextos estudados {bruxvoort2017}. Os "
          "factores associados à prescrição a doentes negativos incluem a "
          "falta de formação em TDR e o conhecimento insuficiente das causas "
          "de febre {akinyode2018}; a adesão aos resultados associa-se à "
          "formação em manejo de casos, à presença de febre e às expectativas "
          "do doente {nauzo2020}; e, na Costa do Marfim, a maioria dos "
          "profissionais acreditava que um TDR negativo podia falhar a "
          "malária {bediatanoh2026}. São factores modificáveis por formação e "
          "supervisão, mas a sua expressão local tem de ser medida antes de "
          "se desenhar a intervenção."),
    ]),
    ("Tratamento com arteméter-lumefantrina e fundamentos da dose", [
        P("O AL é o tratamento de eleição da malária não complicada em "
          "Moçambique; o artesunato-amodiaquina (ASAQ) é a alternativa, e o "
          "quinino oral fica reservado, nas normas de 2017, para o primeiro "
          "trimestre da gravidez e para as contra-indicações dos outros "
          "medicamentos {misau_normas2017}. Cada comprimido contém 20 mg de "
          "arteméter e 120 mg de lumefantrina; o tratamento dura três dias, "
          "com seis tomas de 12 em 12 horas, depois de alimentos com gordura, "
          "e a toma repete-se se o doente vomitar na primeira meia hora "
          "{misau_normas2017}. O [[quadro:doses]] reproduz a correspondência "
          "entre peso, idade e número de comprimidos por toma fixada nas "
          "normas nacionais, que é o padrão contra o qual este estudo "
          "classifica a dose prescrita."),
        QUADRO("doses",
               "Dose de arteméter-lumefantrina por peso e por idade segundo "
               "as normas nacionais de tratamento da malária",
               ["Peso (kg)", "Idade (anos)", "Comprimidos por toma",
                "Total de comprimidos em três dias"],
               [
                   ["Menos de 5", "Não aplicável",
                    "Tratar como malária grave", "Não aplicável"],
                   ["5 a menos de 15", "Menos de 3", "1", "6"],
                   ["15 a menos de 25", "3 a menos de 9", "2", "12"],
                   ["25 a menos de 35", "9 a menos de 15", "3", "18"],
                   ["35 ou mais", "15 ou mais", "4", "24"],
               ],
               larguras=[3.4, 3.4, 4.6, 4.6],
               fonte="Adaptado das Normas de Tratamento da Malária em "
                     "Moçambique, 3.ª edição {misau_normas2017}.",
               nota="Cada comprimido contém 20 mg de arteméter e 120 mg de "
                    "lumefantrina. As seis tomas fazem-se de 12 em 12 horas "
                    "durante três dias, após alimentos com gordura; a toma "
                    "repete-se se houver vómito na primeira meia hora. Para "
                    "as crianças com menos de 25 kg existem comprimidos "
                    "dispersíveis. A faixa etária só se usa quando o peso do "
                    "doente é desconhecido."),
        P("A tabela nacional segue as faixas de peso da OMS (5 a menos de "
          "15 kg, 15 a menos de 25 kg, 25 a menos de 35 kg e 35 kg ou mais) "
          "e acrescenta faixas etárias equivalentes (menos de 3 anos, 3 a "
          "menos de 9, 9 a menos de 15 e 15 ou mais) para quando o peso é "
          "desconhecido {misau_normas2017,oms_directrizes2026}. A OMS "
          "reconhece que a dosagem pela idade é prática nas crianças, mas "
          "adverte que pode resultar em subdose ou sobredose sempre que a "
          "relação entre idade e peso da população difira da pressuposta, e "
          "as suas recomendações de dose baseiam-se no peso "
          "{oms_directrizes2026}. As próprias normas nacionais recomendam que "
          "a administração dos antimaláricos se faça com base no peso do "
          "doente, para reduzir as reacções adversas {misau_normas2017}. Os "
          "adultos corpulentos correm "
          "também risco de subdose quando tratados pela idade ou com "
          "embalagens padrão {oms_directrizes2026}."),
        P("A dose padrão já deixa alguns grupos no limite da exposição "
          "adequada: numa meta-análise de farmacocinética com 4.122 doentes, "
          "a concentração de lumefantrina ao sétimo dia foi 24,2% e 13,4% "
          "mais baixa nas crianças com menos de 15 kg e com 15 a 25 kg, e "
          "20,2% mais baixa nas grávidas, do que nos adultos não grávidos "
          "{kloprogge2018}. Em Moçambique, o AL manteve eficácia corrigida "
          "entre 97,6% e 100% nos cinco locais sentinela avaliados em 2022, "
          "com seguimento de 28 dias {nhama2025}. Esta eficácia só se "
          "reproduz na rotina se a prescrição e a dispensa forem correctas, e "
          "a resistência parcial à artemisinina, confirmada na Tanzânia e "
          "provável na Zâmbia, ambas vizinhas de Moçambique "
          "{oms_wmr2025,martinezvega2026}, faz da dose correcta uma medida de "
          "protecção do próprio medicamento."),
    ]),
    ("Determinantes da conformidade do manejo", [
        P("A conformidade depende, antes de mais, da disponibilidade dos "
          "meios. No Quénia, entre 2010 e 2016, a melhoria do cumprimento "
          "associou-se à ausência de rupturas prévias de TDR, ao acesso às "
          "directrizes e ao conhecimento correcto da política, e foi maior "
          "nas unidades que dispunham apenas de TDR do que nas que dependiam "
          "só da microscopia {amboko2021}. No Uganda, o AL estava disponível "
          "em 76,5% das unidades, e a proporção de doentes que recebeu o "
          "medicamento na própria unidade acompanhou o nível de stock "
          "{mpimbaza2022}. No Malawi, cinco de seis unidades tiveram rupturas "
          "temporárias de AL {klootwijk2019}. É plausível que a falta de uma "
          "apresentação pediátrica leve a improvisar com outras embalagens, "
          "hipótese que este estudo pode examinar ao cruzar os erros de dose "
          "com as rupturas de stock de AL."),
        P("Pesam também características do profissional e do doente. A "
          "formação em manejo de casos e o conhecimento das causas de febre "
          "aumentam a adesão aos resultados negativos "
          "{nauzo2020,akinyode2018}, e em Moçambique a formação e a "
          "supervisão eram baixas fora da Zambézia {candrinho2019}. A idade "
          "do doente influencia a decisão de testar, e as queixas principais "
          "de tosse ou de erupção cutânea associam-se a menos testes "
          "{amboko2022}. Nas províncias moçambicanas estudadas, os factores "
          "associados ao manejo correcto variaram de província para "
          "província e incluíram a idade do doente, o tipo de unidade, a "
          "disponibilidade de testes e de tratamento, a supervisão e a "
          "formação {candrinho2019}."),
        P("O contexto epidemiológico modifica o comportamento. Nas zonas de "
          "baixo risco do Quénia, a melhoria foi mais lenta {amboko2021}, e "
          "em Moçambique a pior conformidade registou-se na província de "
          "baixa transmissão {candrinho2019}. No país, a estação quente e "
          "chuvosa vai de Novembro a Março e a seca de Abril a Outubro "
          "{ine_ids2024}; na época seca, com menos testes positivos, é de "
          "esperar maior tentação de tratar febres com teste negativo, "
          "hipótese que o estudo examina ao incluir a estação do ano entre as "
          "variáveis explicativas."),
    ]),
    ("Enquadramento normativo moçambicano e o papel da farmácia", [
        P("O manejo da malária em Moçambique rege-se pelas Normas de "
          "Tratamento da Malária, terceira edição, de Novembro de 2017, "
          "elaboradas pelo PNCM e revistas pela Comissão Técnica de "
          "Terapêutica e Farmácia, que se dirigem a todos os profissionais "
          "envolvidos no diagnóstico e no tratamento e têm como finalidade "
          "declarada garantir o uso racional dos medicamentos "
          "{misau_normas2017}. O fluxograma das normas resume a regra: doente "
          "com febre, teste; positivo, AL; negativo, procurar e tratar outras "
          "causas de febre {misau_normas2017}. O manual de formação acrescenta "
          "as definições de caso e o modo de registar no livro o resultado do "
          "teste, a microscopia e o tratamento {misau_manual2017}."),
        P("Desde 2017, a OMS actualizou recomendações com impacto nesta "
          "avaliação: em 2022 passou a recomendar o AL no primeiro trimestre "
          "da gravidez e, em 2026, uma nova formulação de AL para lactentes "
          "com menos de 5 kg {oms_directrizes2026}, quando as normas de 2017 "
          "prevêem, respectivamente, quinino oral e o manejo como malária "
          "grave {misau_normas2017}. Por isso, a conformidade será avaliada "
          "face à versão das normas nacionais em vigor em 2026, e as "
          "divergências com a OMS serão descritas sem serem contadas como "
          "erro."),
        P("O farmacêutico e o técnico de farmácia intervêm no último ponto de "
          "controlo antes de o medicamento chegar ao doente: verificam se a "
          "apresentação dispensada corresponde à dose, explicam as seis tomas "
          "e a toma com alimentos e notificam as reacções adversas, a que as "
          "normas dedicam um capítulo de farmacovigilância "
          "{misau_normas2017}. Em Moçambique, só 58% a 62% dos doentes com "
          "antimalárico prescrito sabiam repetir as instruções "
          "{candrinho2019}, e a OMS pede que os prescritores expliquem por "
          "que razão o tratamento deve ser completado {oms_directrizes2026}. "
          "Auditar a prescrição a partir dos registos é, por isso, auditar "
          "também esta última barreira farmacêutica."),
    ]),
    ("Medição da conformidade: inquéritos às unidades e revisão de "
     "registos", [
        P("A qualidade do manejo da malária mede-se de duas formas. Os "
          "inquéritos às unidades sanitárias combinam entrevistas à saída, "
          "reexame dos doentes, entrevistas aos profissionais e inventário "
          "de medicamentos, e são a referência {candrinho2019,davlantes2019}; "
          "exigem, porém, equipas treinadas e presença prolongada nas "
          "unidades, e cobrem poucas semanas. A revisão de registos de rotina "
          "é mais barata, cobre períodos longos e capta a sazonalidade, e tem "
          "sido usada para auditar o cumprimento da regra de testar antes de "
          "tratar {chukwuka2024,camara2019}."),
        P("A validade dos registos é a sua principal fraqueza. Em Moçambique, "
          "a sensibilidade do livro para os TDR negativos foi de apenas 9,7% "
          "na província de Maputo, e o registo foi mais completo quando o "
          "doente tinha sido manejado de acordo com as normas {colborn2020}. "
          "Na Nigéria e na Costa do Marfim, a concordância entre o resultado "
          "registado e a leitura independente do teste foi elevada, com "
          "kappa de 0,80 e 0,83, mas os erros de registo inclinaram-se para o "
          "positivo quando havia prescrição de antimalárico "
          "{atobatele2025,bediatanoh2026}. O registo compete com o tempo "
          "clínico: nos cuidados primários de cinco países, incluindo "
          "Moçambique, cada linha de livro tinha pelo menos 20 campos e o "
          "registo ocupava cerca de um terço do tempo de consulta "
          "{siyam2021}. As estimativas de sobretratamento obtidas nos livros "
          "devem, por isso, ser lidas como limites inferiores."),
        P("As boas práticas para estudos com dados de rotina pedem a "
          "descrição da fonte e da sua qualidade, a verificação da completude "
          "antes da recolha, definições operacionais explícitas e a dupla "
          "extracção com medida da concordância, e o relato segundo a "
          "declaração REporting of studies Conducted using Observational "
          "Routinely-collected health Data (RECORD), extensão da declaração "
          "Strengthening the Reporting of Observational Studies in "
          "Epidemiology (STROBE) {record2015,strobe2007}. A concordância entre "
          "extractores mede-se pelo kappa de Cohen, interpretado segundo a "
          "escala de Landis e Koch {landis1977}, e a validade de conteúdo de "
          "uma ficha nova pelo índice de validade de conteúdo (IVC), "
          "calculado a partir das avaliações de um painel de peritos "
          "{almanasreh2019}."),
    ]),
]

# ----------------------------------------------------- 7. estado da arte ----
ESTADO_ARTE = [
    P("O [[quadro:estado_arte]] reúne treze estudos empíricos publicados "
      "entre 2019 e 2026 sobre o diagnóstico e o tratamento da malária não "
      "complicada em unidades sanitárias africanas, incluindo os dois "
      "estudos moçambicanos com dados colhidos nas unidades."),
    QUADRO("estado_arte",
           "Síntese de estudos sobre a conformidade do diagnóstico e do "
           "tratamento da malária não complicada (estado da arte)",
           ["Autor (ano)", "Local", "Desenho (n)", "Principais resultados"],
           [
               ["Candrinho et al. (2019) {candrinho2019}",
                "Moçambique (Maputo, Zambézia, Cabo Delgado)",
                "Transversal, entrevistas à saída e reexame em 117 unidades "
                "(1.840 doentes)",
                "Manejo adequado dos casos febris confirmados em 52% "
                "(Zambézia), 49% (Cabo Delgado) e 14% (Maputo); antimalárico "
                "a 8% a 22% dos doentes com teste negativo; só 58-62% "
                "repetiam correctamente as instruções de dose."],
               ["Colborn et al. (2020) {colborn2020}",
                "Moçambique (mesmas províncias)",
                "Comparação entre entrevista ou reexame e livros de registo "
                "(1.840 doentes)",
                "Sensibilidade baixa do livro em todos os indicadores; TDR "
                "negativos registados com sensibilidade de 9,7% em Maputo e "
                "positivos até 75% em Cabo Delgado; discrepâncias entre "
                "livros e dados agregados."],
               ["Baraka et al. (2023) {baraka2023}",
                "Seis países, incluindo Moçambique",
                "Observacional prospectivo multicêntrico (1.001 doentes)",
                "73,4% com malária confirmada; 72,5% dos confirmados testados "
                "por TDR; nos casos não complicados, TCA em 94,3%, sobretudo "
                "AL (82,3%)."],
               ["Davlantes et al. (2019) {davlantes2019}",
                "Guiné (seis distritos)",
                "Inquérito em 126 unidades, 939 entrevistas à saída "
                "comparadas com os livros",
                "Manejo correcto de 85% nos estratos de melhor desempenho e "
                "52% no pior; concordância entre entrevista e livro mais "
                "baixa onde o manejo era pior."],
               ["Worges et al. (2019) {worges2019}",
                "Zâmbia (quatro províncias)",
                "Inquérito em 29 unidades (286 doentes)",
                "Teste pedido a 37,0% dos febris; adesão global ao manejo "
                "recomendado de 30,5%; microscopia com sensibilidade de "
                "65,5% e especificidade de 86,0%."],
               ["Amboko et al. (2022) {amboko2022}",
                "Quénia",
                "Quatro inquéritos nacionais, 2014-2016 (2.752 febris em 486 "
                "unidades)",
                "Teste em 65-69% dos febris; ausência de antimalárico nos "
                "negativos em 90-92%; formação e conhecimento da política "
                "associados à adesão aos negativos."],
               ["Klootwijk et al. (2019) {klootwijk2019}",
                "Malawi (Chikhwawa)",
                "Transversal em seis unidades (256 crianças)",
                "21% dos febris sem teste; adesão aos resultados positivos de "
                "99,4% e aos negativos de 97%; AL na dose recomendada pelo "
                "peso em 92,2%; rupturas de AL em cinco de seis unidades."],
               ["Camara et al. (2019) {camara2019}",
                "Guiné",
                "Revisão de registos e inquéritos em unidades públicas "
                "(1.830 doentes)",
                "35,8% das consultas registadas como malária; 26,6% destes "
                "casos diagnosticados clinicamente, sem confirmação "
                "documentada; TCA em 83,5% dos casos não complicados."],
               ["Mpimbaza et al. (2022) {mpimbaza2022}",
                "Uganda (Busoga)",
                "Inquérito em 392 unidades (3.936 doentes)",
                "Manejo adequado em 86,9% dos doentes e em 50,7% nos "
                "prestadores privados; AL em stock em 76,5% das unidades."],
               ["Chukwuka et al. (2024) {chukwuka2024}",
                "Nigéria (Anambra)",
                "Auditoria retrospectiva de 1.536 processos em 32 centros",
                "Cumprimento de «testar antes de tratar» em 99% nos centros "
                "com apoio externo e em 84% nos centros apenas com apoio "
                "governamental."],
               ["Koliopoulos et al. (2024) {koliopoulos2024}",
                "Tanzânia (Mwanza)",
                "Prospectivo em crianças febris (698)",
                "Sensibilidade de 33% da microscopia e de 87% do TDR; "
                "antimalárico a 7% das crianças sem malária onde se seguia o "
                "TDR, contra 75% onde se usava a microscopia."],
               ["Atobatele et al. (2025) {atobatele2025}",
                "Nigéria (Oyo e Sokoto)",
                "Observacional em 16 unidades (18.319 testes)",
                "6,2% dos TDR registados erradamente como positivos e 3,7% "
                "como negativos; kappa agregado de 0,80, com variação entre "
                "unidades."],
               ["Bedia-Tanoh et al. (2026) {bediatanoh2026}",
                "Costa do Marfim",
                "Observacional em 16 unidades (11.161 testes)",
                "Kappa de 0,83 entre livro e painel; negativos ou inválidos "
                "registados como positivos em 5,9%, contra 2,0% no sentido "
                "inverso; erros mais frequentes quando havia prescrição de "
                "antimalárico."],
           ],
           larguras=[3.2, 2.5, 3.3, 7.0],
           fonte="Elaboração própria (2026), a partir das fontes citadas."),
    P("O padrão é consistente. Onde há testes, a maioria dos doentes com "
      "teste negativo não recebe antimalárico, mas persiste uma fracção "
      "variável, de poucos por cento a mais de um quinto, que é tratada "
      "{candrinho2019,amboko2022,klootwijk2019}; antes disso, a falha mais "
      "frequente é não testar todos os febris {worges2019,klootwijk2019}; e "
      "a conformidade piora com a microscopia de má qualidade e nos "
      "contextos de baixa transmissão {koliopoulos2024,candrinho2019}. A "
      "dose raramente é medida como resultado próprio: o estudo do Malawi "
      "avaliou-a pelo peso, com 92,2% de prescrições correctas numa "
      "população pediátrica rural {klootwijk2019}, e o estudo moçambicano "
      "incluiu-a num indicador composto de manejo adequado "
      "{candrinho2019}."),
    P("Há também divergências de método. Os estudos com entrevista à saída e "
      "reexame medem a prática real mas cobrem um ou dois meses "
      "{candrinho2019,davlantes2019}; as auditorias de registos cobrem o ano "
      "inteiro mas dependem da qualidade do registo, que tende a inflacionar "
      "os positivos e a omitir os negativos {colborn2020,bediatanoh2026}. Em "
      "Moçambique, os dados sobre a qualidade do manejo vêm de um inquérito "
      "de 2018 em três províncias, nenhuma delas Nampula, e não há estudos em "
      "centros de saúde urbanos. O presente estudo preenche esta lacuna com "
      "um desenho documental de um ano completo, com verificação prévia da "
      "fonte, ligação à receita e dupla extracção, e com a dose de AL como "
      "resultado próprio."),
]
ESQUEMA_TEXTO = [
    P("A [[figura:esquema]] representa o modelo conceptual do estudo. As "
      "características do doente, o contexto do serviço (centro, estação do "
      "ano e rupturas de stock) e o processo de diagnóstico (método, "
      "resultado e base de dosagem) influenciam o desfecho, a conformidade "
      "com as normas nacionais, medida pela confirmação antes do tratamento, "
      "pelo sobretratamento de doentes com teste negativo e pela dose de AL. "
      "A qualidade do registo modera a relação observada, porque um teste "
      "negativo não registado ou um positivo registado por conveniência "
      "alteram a classificação do episódio {colborn2020,atobatele2025}."),
]
ESQUEMA_TITULO = ("Esquema conceptual da conformidade do diagnóstico e do "
                  "tratamento da malária não complicada")
ESQUEMA = {
    "contexto": "Consultas externas dos centros de saúde públicos da cidade "
                "de Nampula, 1 de Janeiro a 31 de Dezembro de 2026",
    "blocos": [
        ("Características do doente",
         ["sexo", "grupo etário", "peso registado"]),
        ("Contexto do serviço",
         ["centro de saúde", "estação do ano",
          "ruptura de stock de TDR ou de AL"]),
        ("Processo de diagnóstico e prescrição",
         ["método (TDR ou microscopia)", "resultado registado",
          "base de dosagem (peso ou idade)"]),
    ],
    "desfecho": ("Conformidade com as normas nacionais",
                 ["confirmação antes do tratamento",
                  "sobretratamento de teste negativo",
                  "dose de AL conforme"]),
    "moderadores": ("Qualidade do registo",
                    ["preenchimento dos campos", "legibilidade",
                     "omissão de testes negativos"]),
}

# ----------------------------------------------------- 8. metodologia -------
METODOLOGIA = [
    ("Tipo e desenho do estudo", [
        P("Trata-se de um estudo observacional, transversal, retrospectivo e "
          "documental, de abordagem quantitativa, com uma componente "
          "descritiva, correspondente aos objectivos específicos 1 a 3, e "
          "uma componente analítica, correspondente ao objectivo específico "
          "4. A informação provém exclusivamente de registos produzidos na "
          "rotina dos serviços em 2026, sem qualquer contacto com os "
          "doentes e sem interferência no atendimento, pelo que a medição é "
          "feita depois de os cuidados terem sido prestados e não pode "
          "alterar a prática observada."),
        P("A opção pelo desenho documental decorre da pergunta de "
          "investigação: o objecto é a conformidade documentada da "
          "prescrição ao longo de um ano inteiro, com a sua variação "
          "sazonal, e não a exactidão do teste nem o comportamento do "
          "doente, para o que a fonte de rotina é adequada desde que a "
          "completude seja verificada antes da recolha e os resultados "
          "sejam lidos como limites inferiores do incumprimento "
          "{colborn2020,camara2019}. O protocolo e o "
          "relatório final seguem as declarações STROBE e RECORD "
          "{strobe2007,record2015}."),
    ]),
    ("Local e período do estudo", [
        P("O estudo decorre na cidade de Nampula, capital da província de "
          "Nampula, no norte de Moçambique, e abrange todos os centros de "
          "saúde públicos geridos pelo Serviço Distrital de Saúde, Mulher e "
          "Acção Social da Cidade de Nampula que tenham consulta externa e "
          "diagnóstico da malária por teste de diagnóstico rápido ou por "
          "microscopia. A lista e o número exacto de centros elegíveis serão "
          "obtidos no início do trabalho de campo [confirmar a lista das "
          "unidades sanitárias junto do SDSMAS da Cidade de Nampula]. Trata-"
          "se de um contexto urbano e periurbano de transmissão mais baixa "
          "do que a do meio rural da mesma província, situação em que a "
          "regra de testar antes de tratar tem maior valor clínico e em que "
          "o incumprimento tem sido maior {amboko2021,candrinho2019}."),
        P("O período dos dados é de 1 de Janeiro a 31 de Dezembro de 2026, "
          "um ano civil completo, escolhido para cobrir as duas estações: a "
          "chuvosa, de Novembro a Março, e a seca, de Abril a Outubro "
          "{ine_ids2024}. A consulta dos arquivos decorre em 2027, depois da "
          "aprovação pelo comité de bioética e das autorizações "
          "institucionais, entre Março e Junho, conforme o cronograma. A "
          "verificação prévia da qualidade da fonte faz-se em Fevereiro de "
          "2027, em registos de 2025, para não gastar registos do período de "
          "estudo."),
    ]),
    ("População, unidade de análise e fontes de dados", [
        P("A população de estudo são os episódios de consulta externa "
          "registados nos centros elegíveis entre 1 de Janeiro e 31 de "
          "Dezembro de 2026 em que foi prescrito um antimalárico oral ou em "
          "que foi registado um resultado negativo de teste de malária, em "
          "doentes de todas as idades. A unidade de análise é o episódio de "
          "consulta, isto é, a linha do livro de registo de doentes "
          "correspondente a um atendimento, e não o doente: os livros não "
          "contêm um identificador único que permita ligar de forma fiável "
          "visitas repetidas da mesma pessoa, pelo que as proporções são "
          "estimadas por episódio e não por doente. Episódios sucessivos do "
          "mesmo doente, quando identificáveis pelo nome e pela idade na "
          "mesma unidade, são assinalados numa variável de possível "
          "repetição e a sua influência é examinada em análise de "
          "sensibilidade."),
        P("A população divide-se em dois estratos com denominadores "
          "diferentes, porque os indicadores medem coisas distintas. O "
          "estrato A reúne os episódios com prescrição de antimalárico oral, "
          "e serve para estimar a proporção de tratamentos precedidos de "
          "confirmação parasitológica e a conformidade da dose. O estrato B "
          "reúne os episódios com teste de malária negativo, e serve para "
          "estimar o sobretratamento. Os episódios que pertencem aos dois "
          "estratos, ou seja, os doentes com teste negativo que receberam "
          "antimalárico, são extraídos uma única vez e contam para os dois "
          "denominadores, e a base de amostragem é depurada de linhas "
          "duplicadas pela combinação de centro, data e número de ordem."),
        P("Três fontes documentais alimentam cada episódio. O livro de "
          "registo de doentes da consulta externa fornece a data, o sexo, a "
          "coluna de idade, o diagnóstico, o resultado do teste e o "
          "tratamento, nos termos do modelo nacional {misau_manual2017}. O "
          "livro de registo do laboratório fornece o método de diagnóstico e "
          "o resultado, e permite recuperar testes negativos omitidos no "
          "livro da consulta. As receitas arquivadas ou, quando existam, os "
          "duplicados das requisições de medicamentos fornecem o medicamento, "
          "a apresentação e a quantidade dispensada, que é a base do cálculo "
          "da dose por toma. O mapa mensal de existências da farmácia de cada "
          "centro fornece as rupturas de stock de testes e de "
          "arteméter-lumefantrina."),
    ]),
    ("Amostra e cálculo do tamanho da amostra", [
        P("O tamanho da amostra é calculado separadamente para cada estrato, "
          "pela fórmula da estimativa de uma proporção em população "
          "considerada grande {serdar2021}:"),
        FORMULA("n<sub>0</sub> = Z<sup>2</sup> × p × (1 - p) / d<sup>2</sup>"),
        P("em que Z é 1,96, valor da distribuição normal padrão para um "
          "nível de confiança de 95%, p é a proporção esperada do desfecho e "
          "d é a precisão absoluta, fixada em 5 pontos percentuais, "
          "suficiente para orientar decisões de formação e de abastecimento "
          "ao nível da cidade. No estrato A estimam-se dois desfechos com "
          "proporções esperadas muito diferentes, a confirmação antes do "
          "tratamento, que na Guiné deixou 26,6% dos casos registados como "
          "malária sem confirmação laboratorial documentada {camara2019}, e "
          "a conformidade da dose, que atingiu 92,2% no Malawi "
          "{klootwijk2019}; como um único p não serve os dois, adopta-se p "
          "de 0,5, que maximiza a variância e cobre ambos, e obtém-se "
          "n<sub>0</sub> igual a 384,16. No estrato B estima-se um só "
          "desfecho, e usa-se p de 0,22, o "
          "valor mais alto de doentes com teste negativo tratados com "
          "antimalárico observado nas províncias moçambicanas estudadas "
          "{candrinho2019}, o que dá n<sub>0</sub> igual a 263,7."),
        P("Todos os centros elegíveis entram no estudo e a amostra é "
          "estratificada por centro, pelo que a variância não é inflacionada "
          "pela amostragem de conglomerados; ainda assim, os episódios do "
          "mesmo centro assemelham-se entre si e podem repetir o mesmo "
          "doente, e a análise multinível perde eficiência em relação à "
          "amostragem aleatória simples. Aplica-se por isso um efeito de "
          "desenho (DEFF) de 1,5, valor conservador do intervalo de 1,5 a 2 "
          "usado quando há correlação dentro dos agrupamentos. "
          "Acrescenta-se uma margem r de 10% "
          "para linhas ilegíveis, rasuradas ou incompletas ao ponto de não "
          "permitirem classificar o episódio, proporção compatível com a "
          "qualidade de preenchimento descrita para os livros moçambicanos "
          "{colborn2020}:"),
        FORMULA("n = n<sub>0</sub> × DEFF / (1 - r)"),
        P("No estrato A, 384,16 multiplicado por 1,5 dá 576,2, que dividido "
          "por 0,90 dá 640,3, arredondado para 641 episódios com prescrição "
          "de antimalárico. No estrato B, 263,7 multiplicado por 1,5 dá "
          "395,5, que dividido por 0,90 dá 439,5, arredondado para 440 "
          "episódios com teste negativo. O total é de 1.081 episódios."),
        P("O número de episódios elegíveis do ano só será conhecido quando a "
          "base de amostragem estiver construída. O [[quadro:cenarios]] "
          "mostra o efeito da correcção para população finita, "
          "n<sub>c</sub> = n<sub>0</sub> / [1 + (n<sub>0</sub> - 1) / N], "
          "aplicada a n<sub>0</sub> antes do efeito de desenho e da margem, "
          "em quatro cenários de volume anual. Mesmo no cenário mais pequeno "
          "a correcção reduz o total em menos de um sexto, pelo que o estudo "
          "adopta o valor não corrigido de 1.081 episódios, que garante a "
          "precisão pretendida em qualquer dos cenários; se um estrato tiver "
          "menos episódios elegíveis do que os exigidos, é estudado por "
          "censo."),
        QUADRO("cenarios",
               "Tamanho da amostra por estrato segundo o número de episódios "
               "elegíveis no ano, com correcção para população finita",
               ["Episódios elegíveis no ano (N)",
                "Estrato A: episódios com antimalárico",
                "Estrato B: episódios com teste negativo",
                "Total de episódios"],
               [
                   ["2.000", "538", "389", "927"],
                   ["5.000", "595", "418", "1.013"],
                   ["10.000", "617", "429", "1.046"],
                   ["20.000", "629", "434", "1.063"],
                   ["Sem correcção (opção adoptada)", "641", "440", "1.081"],
               ],
               larguras=[4.6, 4.0, 4.2, 3.2],
               nota="Todos os valores já incluem o efeito de desenho de 1,5 "
                    "e a margem de 10% para registos inutilizáveis."),
        P("Dentro de cada estrato, a "
          "amostra é repartida pelos centros proporcionalmente ao número de "
          "episódios elegíveis de cada um, com um mínimo de 20 episódios por "
          "centro e por estrato para permitir a comparação entre centros, e "
          "dentro de cada centro é repartida igualmente pelos 12 meses, para "
          "garantir a representação das duas estações. Se forem 12 os centros "
          "elegíveis, cabem em média 53 episódios do estrato A e 37 do "
          "estrato B a cada centro, ou seja, cerca de quatro e três por mês. "
          "A selecção dentro de cada célula de centro e mês é sistemática: "
          "calcula-se o intervalo k dividindo o número de episódios "
          "elegíveis da célula pelo número a extrair, sorteia-se um ponto de "
          "partida entre 1 e k com números aleatórios, e retira-se cada "
          "k-ésima linha; esgotada a célula, a diferença é reposta na célula "
          "seguinte do mesmo centro."),
        P("O poder foi verificado para a componente analítica e não apenas "
          "para as estimativas descritivas, tomando por base os episódios "
          "que se espera poder classificar, ou seja, 90% de cada estrato. "
          "Com 396 episódios de teste negativo repartidos por dois grupos de "
          "198, por exemplo estação chuvosa e estação seca, o estudo detecta, "
          "com significância de 5% e poder de 80%, uma diferença entre 22% e "
          "35% na proporção de doentes com teste negativo tratados. Com 577 "
          "episódios do estrato A repartidos por dois grupos de cerca de 288, "
          "detecta uma diferença entre 8% e 16% na proporção de doses não "
          "conformes. Para a regressão logística, o critério é de pelo menos "
          "dez eventos por variável {peduzzi1996}: esperam-se cerca de 87 "
          "episódios de sobretratamento, o que comporta até oito termos no "
          "modelo, mas apenas cerca de 45 doses não conformes se a não "
          "conformidade rondar os 8% do estudo do Malawi {klootwijk2019}, o "
          "que limita o modelo da dose a quatro termos fixados à partida, "
          "grupo etário, base de dosagem, ruptura de stock de "
          "arteméter-lumefantrina e estação do ano, e reduz o poder para "
          "detectar associações fracas, limitação declarada nos resultados."),
    ]),
    ("Critérios de inclusão e de exclusão", [
        H3("Critérios de inclusão dos centros de saúde"),
        LISTA([
            "Centro de saúde público da cidade de Nampula gerido pelo SDSMAS "
            "da Cidade de Nampula;",
            "Com consulta externa em funcionamento durante todo o ano de "
            "2026;",
            "Com diagnóstico da malária disponível por teste de diagnóstico "
            "rápido, por microscopia ou por ambos;",
            "Com os livros de registo de doentes e do laboratório de 2026 "
            "arquivados e acessíveis em 2027.",
        ]),
        H3("Critérios de inclusão dos episódios"),
        LISTA([
            "Episódio de consulta externa registado entre 1 de Janeiro e 31 "
            "de Dezembro de 2026;",
            "Com prescrição de antimalárico oral registada, qualquer que "
            "seja o resultado do teste (estrato A), ou com resultado "
            "negativo de teste de malária registado, tenha ou não havido "
            "prescrição (estrato B);",
            "Com a linha do livro legível no que respeita à data, à idade, "
            "ao diagnóstico e ao tratamento.",
        ]),
        H3("Critérios de exclusão dos episódios"),
        LISTA([
            "Episódios de malária grave ou complicada e episódios que "
            "terminaram em internamento ou em transferência, por seguirem "
            "outra norma de tratamento;",
            "Episódios de mulheres assinaladas como grávidas no registo, "
            "sejam ou não seguidas na consulta pré-natal, por as normas "
            "nacionais preverem para elas outra escolha de medicamento no "
            "primeiro trimestre;",
            "Episódios com antimalárico injectável apenas, sem prescrição "
            "oral;",
            "Episódios manejados por agentes polivalentes elementares na "
            "comunidade e episódios registados fora da consulta externa;",
            "Linhas duplicadas do mesmo atendimento e linhas em que o campo "
            "do tratamento esteja em branco e não exista receita "
            "correspondente.",
        ]),
    ]),
    ("Variáveis, definições operacionais e critérios de conformidade", [
        P("A conformidade é julgada contra a versão das normas nacionais em "
          "vigor em 2026 [confirmar junto do PNCM se houve edição posterior à "
          "terceira, de 2017]. "
          "O [[quadro:criterios]] traduz cada regra das normas num critério "
          "verificável na documentação e na classificação que dela resulta; "
          "o [[quadro:variaveis]] lista as variáveis, as suas categorias e o "
          "objectivo específico que servem. Nenhuma classificação depende do "
          "julgamento clínico do extractor: onde o registo não permite "
          "decidir, o episódio é classificado como indeterminado e essa "
          "categoria é relatada, em vez de ser tratada como conformidade ou "
          "como erro."),
        QUADRO("criterios",
               "Critérios de conformidade do diagnóstico e do tratamento da "
               "malária não complicada aplicados aos registos",
               ["Dimensão", "O que determinam as normas nacionais",
                "Critério verificado no registo", "Classificação do episódio"],
               [
                   ["Confirmação antes do tratamento",
                    "Todo o caso suspeito é testado antes de receber "
                    "antimalárico; o tratamento presuntivo só se admite "
                    "quando não há meio de diagnóstico "
                    "{misau_normas2017,misau_manual2017}",
                    "Existe resultado de teste registado na linha do "
                    "episódio ou no livro do laboratório do mesmo dia e "
                    "doente",
                    "Confirmado; presuntivo justificado, com ruptura de "
                    "testes documentada no mês; presuntivo injustificado"],
                   ["Resposta ao teste negativo",
                    "O doente com teste negativo não recebe antimalárico e é "
                    "investigado para outras causas de febre "
                    "{misau_normas2017}",
                    "Ausência de antimalárico oral no campo do tratamento do "
                    "episódio com teste negativo",
                    "Conforme; sobretratamento"],
                   ["Escolha do antimalárico",
                    "Arteméter-lumefantrina é o medicamento de eleição; "
                    "artesunato-amodiaquina e quinino oral só em "
                    "indisponibilidade, contra-indicação ou alergia "
                    "{misau_normas2017}",
                    "Substância registada no campo do tratamento e na "
                    "receita arquivada",
                    "Conforme; alternativa sem justificação registada; não "
                    "avaliável"],
                   ["Dose por toma",
                    "Um, dois, três ou quatro comprimidos por toma consoante "
                    "o peso ou, na sua falta, a idade ([[quadro:doses]])",
                    "Quantidade total dispensada comparada com o total "
                    "previsto para o peso registado ou, na sua falta, para a "
                    "idade (6, 12, 18 ou 24 comprimidos)",
                    "Conforme; subdose, se corresponder a uma faixa inferior; "
                    "sobredose, se corresponder a uma faixa superior; "
                    "indeterminada"],
                   ["Número de tomas e duração",
                    "Seis tomas de 12 em 12 horas durante três dias "
                    "{misau_normas2017}",
                    "Quantidade total dispensada múltipla de seis; quando "
                    "não o é, não cobre as seis tomas previstas",
                    "Conforme; esquema incompleto; esquema excessivo; "
                    "indeterminado"],
                   ["Completude do registo",
                    "A idade, o diagnóstico, o resultado do teste e o "
                    "tratamento são escritos no livro de registo de doentes "
                    "{misau_manual2017}",
                    "Campos de idade, diagnóstico, resultado do teste e "
                    "tratamento preenchidos e legíveis na linha do episódio",
                    "Completo; incompleto"],
               ],
               larguras=[2.8, 4.6, 4.2, 4.4],
               fonte="Elaboração própria (2026), a partir das normas "
                     "nacionais {misau_normas2017,misau_manual2017}."),
        QUADRO("variaveis",
               "Variáveis do estudo, definições operacionais e objectivos "
               "que servem",
               ["Variável", "Tipo", "Definição operacional e categorias",
                "Objectivo"],
               [
                   ["Sexo", "Independente, qualitativa nominal",
                    "Sexo registado no livro: masculino; feminino; não "
                    "registado", "1, 4"],
                   ["Grupo etário", "Independente, qualitativa ordinal",
                    "Coluna de idade do livro nacional: 0-4 anos; 5-15 anos; "
                    "mais de 15 anos", "1, 4"],
                   ["Peso registado",
                    "Independente, qualitativa nominal e quantitativa "
                    "contínua",
                    "Presença de peso em quilogramas na linha do episódio ou "
                    "na receita: sim, com o valor em quilogramas; não", "1, 3"],
                   ["Centro de saúde",
                    "Independente, qualitativa nominal (segundo nível do "
                    "modelo)",
                    "Código atribuído a cada centro elegível, sem menção do "
                    "nome nos relatórios públicos", "1, 4"],
                   ["Mês do episódio", "Independente, qualitativa ordinal",
                    "Mês da data da consulta, de Janeiro a Dezembro de 2026",
                    "1, 4"],
                   ["Estação do ano", "Independente, qualitativa nominal",
                    "Chuvosa, de Novembro a Março; seca, de Abril a Outubro "
                    "{ine_ids2024}", "1, 4"],
                   ["Método de diagnóstico",
                    "Independente, qualitativa nominal",
                    "Teste de diagnóstico rápido; microscopia; ambos; nenhum "
                    "registado", "1, 2, 4"],
                   ["Resultado do teste", "Independente, qualitativa nominal",
                    "Positivo; negativo; inválido; não registado", "1, 2"],
                   ["Antimalárico prescrito",
                    "Independente, qualitativa nominal",
                    "Arteméter-lumefantrina; artesunato-amodiaquina; quinino "
                    "oral; outro; nenhum", "1, 3"],
                   ["Base de dosagem", "Independente, qualitativa nominal",
                    "Peso em quilogramas; idade em anos; grupo etário do "
                    "livro; indeterminada", "3, 4"],
                   ["Ruptura de stock no mês",
                    "Independente, qualitativa nominal",
                    "Existência nula de testes ou de arteméter-lumefantrina "
                    "em alguma semana do mês, no mapa de existências do "
                    "centro: sim; não; sem informação", "4"],
                   ["Tratamento precedido de confirmação",
                    "Dependente, qualitativa dicotómica",
                    "Sim, quando há resultado de teste registado para o "
                    "episódio tratado; não, nos restantes casos", "2"],
                   ["Sobretratamento de teste negativo",
                    "Dependente, qualitativa dicotómica",
                    "Sim, quando o episódio com teste negativo tem "
                    "antimalárico oral prescrito", "2, 4"],
                   ["Conformidade da dose de arteméter-lumefantrina",
                    "Dependente, qualitativa nominal",
                    "Conforme; subdose; sobredose; esquema incompleto; "
                    "indeterminada, segundo o quadro de critérios", "3, 4"],
                   ["Completude do registo do episódio",
                    "Dependente, qualitativa dicotómica",
                    "Linha com idade, diagnóstico, resultado do teste e "
                    "tratamento preenchidos e legíveis", "1"],
               ],
               larguras=[3.4, 3.0, 7.4, 2.2]),
    ]),
    ("Instrumentos de recolha de dados e respectivas fontes", [
        P("O instrumento é uma ficha de extracção estruturada, reproduzida "
          "no Apêndice A, com cinco secções: identificação do episódio por "
          "código, características do doente, diagnóstico, tratamento e "
          "qualidade do registo. Os campos reproduzem as colunas do livro de "
          "registo de doentes do modelo nacional, que inclui a idade em três "
          "grupos, o diagnóstico e o tratamento mas não tem campo para o "
          "peso {misau_manual2017}, acrescidos dos campos recolhidos na "
          "receita e no mapa de existências. A ficha não recolhe nome, "
          "número de processo nem morada; cada episódio recebe um código "
          "sequencial composto pelo código do centro, pelo mês e por um "
          "número de ordem. Um manual de preenchimento, com as regras de "
          "classificação do [[quadro:criterios]] e exemplos resolvidos, "
          "acompanha a ficha."),
        P("A validade de conteúdo é avaliada por um painel de cinco peritos, "
          "um clínico com experiência em manejo da malária, um farmacêutico, "
          "um técnico de laboratório, um epidemiologista e um docente da "
          "Faculdade de Ciências de Saúde, que classificam a pertinência de "
          "cada item numa escala de quatro níveis; retêm-se os itens com IVC "
          "igual ou superior a 0,80 e "
          "reformulam-se ou eliminam-se os restantes {almanasreh2019}. "
          "Segue-se um pré-teste em 30 registos de 2025 de um centro "
          "elegível, fora da amostra final, que serve simultaneamente de "
          "verificação prévia da fonte e de ensaio do tempo de "
          "preenchimento; o resultado do pré-teste conduz ao ajuste dos "
          "campos e à versão final da ficha, também submetida ao comité de "
          "bioética."),
    ]),
    ("Procedimentos de recolha de dados e controlo de qualidade", [
        P("A recolha começa apenas depois da aprovação ética e das "
          "autorizações institucionais. A primeira etapa é a verificação "
          "prévia da fonte: nos mesmos 30 registos de 2025 do pré-teste, "
          "calcula-se a percentagem de preenchimento de cada campo. A regra "
          "de decisão está escrita antes da recolha: uma variável preenchida "
          "em menos de 60% dos registos é retirada dos objectivos "
          "analíticos, sendo apenas descrita como lacuna de registo, e o "
          "peso, previsivelmente o campo mais incompleto, terá o seu "
          "tratamento decidido nesta etapa. Se a completude dos campos "
          "essenciais, data, idade, resultado do teste e tratamento, ficar "
          "abaixo de 60% em algum centro, esse centro é descrito à parte e a "
          "sua contribuição para as estimativas globais é avaliada em "
          "análise de sensibilidade."),
        P("A segunda etapa é a construção da base de amostragem, por "
          "transcrição, para uma folha de cálculo, do centro, da data e do "
          "número de ordem de todas as linhas elegíveis de cada estrato, sem "
          "qualquer outro dado. A terceira etapa é a extracção propriamente "
          "dita, feita por dois extractores, o estudante e um colega "
          "finalista de Farmácia, formados em duas sessões de calibração "
          "sobre as normas nacionais, o manual de preenchimento e a "
          "classificação da dose. As primeiras 20 fichas de cada extractor "
          "são verificadas na totalidade pelo orientador, e a supervisão "
          "mantém-se semanal."),
        P("O controlo de qualidade assenta em três medidas. Uma amostra "
          "aleatória de 10% dos episódios, ou seja, 109 fichas, é extraída "
          "de forma independente pelos dois extractores, e a concordância é "
          "medida pelo kappa de Cohen nas variáveis categóricas e pelo "
          "coeficiente de correlação intraclasse (CCI) nas quantitativas, "
          "exigindo-se valores iguais ou superiores a 0,80, interpretados "
          "segundo a escala de Landis e Koch {landis1977}; abaixo desse "
          "valor, o manual é revisto, os extractores são recalibrados e as "
          "fichas já preenchidas são reextraídas. A classificação da "
          "conformidade da dose e da justificação do tratamento presuntivo é "
          "feita por dois avaliadores independentes, com as discordâncias "
          "resolvidas por consenso e, persistindo, por um terceiro avaliador. "
          "A digitação faz-se em dupla entrada no EpiData, com comparação "
          "automática dos dois ficheiros e resolução das discrepâncias "
          "contra a ficha em papel."),
    ]),
    ("Processamento e análise dos dados", [
        P("Os dados serão analisados no Statistical Package for the Social "
          "Sciences (SPSS), versão 26 ou superior, ou no programa R, de "
          "acesso livre, com nível de significância de 5% e intervalos de "
          "confiança a 95% (IC95%). As variáveis qualitativas são descritas "
          "por frequências absolutas e relativas e as quantitativas por "
          "média e desvio-padrão ou, quando a distribuição for assimétrica, "
          "por mediana e intervalo interquartil. O objectivo específico 1 é "
          "respondido pela distribuição dos episódios de cada estrato por "
          "sexo, grupo etário, centro, mês, estação e método de diagnóstico, "
          "acompanhada da completude de cada campo, que é ao mesmo tempo "
          "resultado descritivo e indicador da qualidade da fonte."),
        P("Para o objectivo específico 2, estimam-se a proporção de "
          "tratamentos antimaláricos precedidos de confirmação "
          "parasitológica, tendo por denominador os episódios do estrato A, "
          "e a proporção de doentes com teste negativo que receberam "
          "antimalárico, tendo por denominador os episódios do estrato B, "
          "ambas com IC95% pelo método de Wilson, que se comporta melhor com "
          "proporções próximas dos extremos. Para o objectivo específico 3, "
          "estima-se a proporção de prescrições de arteméter-lumefantrina "
          "com dose conforme, também com IC95%, e descreve-se a distribuição "
          "dos tipos de erro, subdose, sobredose e esquema incompleto, no "
          "conjunto e por grupo etário; as classificações feitas pelo peso e "
          "pela idade são comparadas nos episódios em que ambos constam, "
          "para quantificar a discordância entre as duas bases de dosagem. "
          "As estimativas são apresentadas para a cidade e por centro."),
        P("O objectivo específico 4 é respondido em dois passos. Primeiro, a "
          "associação de cada variável explicativa com o sobretratamento e "
          "com o erro de dose é examinada pelo teste do qui-quadrado de "
          "Pearson, ou pelo teste exacto de Fisher quando mais de 20% das "
          "frequências esperadas forem inferiores a 5, com cálculo do odds "
          "ratio (OR) bruto e do respectivo IC95%. Depois, as variáveis com "
          "p inferior a 0,20 na análise bivariada, mais o grupo etário e a "
          "estação do ano, retidos por decisão prévia, entram numa regressão "
          "logística multinível com intercepto aleatório para o centro de "
          "saúde, que respeita o agrupamento dos episódios e produz o odds "
          "ratio ajustado (ORa) com IC95%; o CCI do modelo quantifica a "
          "fracção da variação atribuível ao centro. O número de termos "
          "respeita o limite de dez eventos por variável fixado no cálculo da "
          "amostra, oito no modelo do sobretratamento e quatro no da dose "
          "{peduzzi1996}, e a "
          "qualidade do ajuste é avaliada pelo teste de Hosmer e Lemeshow e "
          "pela área sob a curva de características operativas do receptor."),
        P("Três análises de sensibilidade acompanham os resultados "
          "principais. Na primeira, os episódios sem resultado de teste "
          "registado são tratados sucessivamente como não testados e como "
          "testados, para definir um intervalo em torno da proporção de "
          "tratamentos confirmados. Na segunda, exclui-se o centro com a "
          "completude de registo mais baixa. Na terceira, restringe-se a "
          "análise aos episódios classificados pelo peso, para verificar se "
          "a conformidade da dose muda quando não se recorre à idade. Os "
          "valores em falta são declarados por variável e a análise principal "
          "é feita com casos completos, uma vez que a ausência de registo é "
          "ela própria um resultado do estudo e não um dado a imputar."),
    ]),
    ("Limitações do estudo e estratégias de mitigação", [
        P("O [[quadro:limitacoes]] reúne as limitações previstas, a "
          "consequência de cada uma para a interpretação e a medida adoptada "
          "para a reduzir. A mais pesada é a dependência da qualidade do "
          "registo, que em Moçambique já se mostrou baixa para os testes "
          "negativos {colborn2020}, e que empurra as estimativas de "
          "incumprimento para baixo."),
        QUADRO("limitacoes",
               "Limitações previstas e estratégias de mitigação",
               ["Limitação", "Consequência", "Mitigação"],
               [
                   ["Omissão de testes negativos no livro da consulta",
                    "Subestimação do sobretratamento e sobrestimação da "
                    "confirmação",
                    "Cruzamento com o livro do laboratório; verificação "
                    "prévia da completude; apresentação dos resultados como "
                    "limites inferiores"],
                   ["Ausência de campo para o peso no livro nacional",
                    "Classificação da dose pela idade numa parte dos "
                    "episódios, com risco de classificação errada",
                    "Registo da base de dosagem como variável; procura do "
                    "peso na receita; análise separada dos episódios com "
                    "peso registado"],
                   ["Registo escrito à mão, com abreviaturas e rasuras",
                    "Perda de episódios e erro de leitura",
                    "Margem de 10% na amostra; manual de abreviaturas; dupla "
                    "extracção de 10% com kappa igual ou superior a 0,80"],
                   ["Ausência de contacto com o doente",
                    "Não se sabe se houve febre, nem se o teste foi feito e "
                    "não registado, nem o que foi dispensado e tomado",
                    "Delimitação explícita do objecto à conformidade "
                    "documentada; discussão comparada com estudos de "
                    "entrevista à saída {candrinho2019}"],
                   ["Desenho transversal e retrospectivo",
                    "Não permite estabelecer relações de causa e efeito "
                    "entre os factores e o incumprimento",
                    "Resultados apresentados como associações; hipóteses "
                    "formuladas em termos de associação"],
                   ["Estudo limitado a uma cidade e ao sector público",
                    "Validade externa restrita; não cobre farmácias "
                    "comerciais nem o meio rural",
                    "Delimitação declarada; comparação com estudos de outras "
                    "províncias e países {candrinho2019,mpimbaza2022}"],
                   ["Possível repetição de episódios do mesmo doente",
                    "Correlação intra-doente não modelada, com intervalos de "
                    "confiança demasiado estreitos",
                    "Variável de possível repetição; efeito de desenho de "
                    "1,5; intercepto aleatório por centro e análise de "
                    "sensibilidade"],
               ],
               larguras=[4.2, 5.4, 6.4]),
    ]),
    ("Considerações éticas", [
        P("O estudo respeita a Declaração de Helsínquia na revisão de 2024 "
          "{helsinki2025} e as directrizes éticas internacionais para "
          "investigação relacionada com a saúde em seres humanos do Conselho "
          "das Organizações Internacionais de Ciências Médicas (CIOMS) "
          "{cioms2016}, que tratam expressamente da investigação com dados "
          "já recolhidos. O protocolo será submetido ao Comité Institucional "
          "de Bioética para a Saúde da Universidade Lúrio (CIBS-UniLúrio) e, "
          "se este o determinar, ao Comité Nacional de Bioética para a Saúde "
          "(CNBS). Serão pedidas autorizações à Direcção Provincial de Saúde "
          "de Nampula, ao SDSMAS da Cidade de Nampula e à direcção de cada "
          "centro de saúde [preencher os contactos telefónicos e os "
          "endereços das instituições]. A recolha só começa depois de todas "
          "as aprovações estarem escritas."),
        P("Pede-se dispensa de consentimento informado, nos termos do "
          "Apêndice C, com quatro fundamentos: o estudo é retrospectivo e "
          "recai sobre atendimentos de 2026, cujos doentes seria "
          "impraticável localizar em número de mais de mil; os livros não "
          "contêm contactos que permitam esse convite; a ficha de extracção "
          "não recolhe nome, número de processo, morada nem qualquer outro "
          "identificador, pelo que o risco de quebra de confidencialidade é "
          "mínimo; e exigir o consentimento inviabilizaria uma avaliação de "
          "qualidade de cuidados de interesse público, situação prevista nas "
          "directrizes internacionais {cioms2016}. Nenhum benefício directo "
          "é prometido aos doentes cujos registos são consultados."),
        P("A protecção dos dados é assegurada por procedimentos escritos. As "
          "fichas em papel são guardadas em caixa fechada à chave, a que só "
          "o estudante e o orientador têm acesso; o ficheiro electrónico é "
          "cifrado e guardado em dois suportes; os livros de registo nunca "
          "saem da unidade sanitária e são consultados em espaço cedido pela "
          "direcção, fora das horas de maior movimento, para não perturbar o "
          "serviço. Os dados serão conservados durante cinco anos após a "
          "defesa e depois destruídos. Os centros e os profissionais não são "
          "identificados: cada centro recebe um código e os resultados "
          "publicados são agregados, de modo que o estudo não sirva para "
          "atribuir culpas individuais."),
        P("Como o estudo não tem contacto com doentes, não existe via de "
          "referenciação clínica individual. Prevê-se, em contrapartida, uma "
          "via institucional: se a extracção revelar num centro um padrão "
          "sistemático de erro com potencial de dano, como a prescrição "
          "repetida de doses acima do previsto a crianças ou o tratamento "
          "generalizado de doentes com teste negativo, a direcção do centro "
          "e o SDSMAS são informados por escrito ainda durante o trabalho de "
          "campo, sem esperar pelo relatório final, e a devolução dos "
          "resultados é feita em sessão conjunta, com finalidade formativa e "
          "não punitiva. O estudante declara não ter conflito de interesses "
          "e nenhum financiamento da indústria farmacêutica."),
    ]),
]

# ----------------------------------------------------- 9 e 10 ---------------
RESULTADOS_ESPERADOS = [
    P("Do primeiro objectivo espera-se um retrato dos episódios de febre "
      "atendidos nos centros de saúde da cidade, com a repartição por sexo, "
      "grupo etário, centro, mês, estação e método de diagnóstico, e com a "
      "medida da completude de cada campo do livro. É provável que a "
      "concentração de episódios na estação chuvosa seja acentuada e que o "
      "teste de diagnóstico rápido domine sobre a microscopia, como acontece "
      "na rede pública moçambicana {candrinho2019}. Este retrato dá ao "
      "Serviço Distrital a distribuição real da procura ao longo do ano, "
      "base para dimensionar a encomenda de testes e de "
      "arteméter-lumefantrina mês a mês."),
    P("Do segundo objectivo esperam-se duas proporções com intervalo de "
      "confiança: a dos tratamentos antimaláricos precedidos de confirmação "
      "parasitológica e a dos doentes com teste negativo que ainda assim "
      "receberam antimalárico. À luz do que se observou noutras províncias "
      "moçambicanas e em países vizinhos, é de esperar que a maioria dos "
      "tratamentos esteja confirmada mas que persista uma fracção "
      "apreciável de sobretratamento, maior nos meses de ruptura de testes "
      "{candrinho2019,bruxvoort2017}. Sendo uma estimativa obtida em "
      "registos, deve ser lida como limite inferior. O valor serve de linha "
      "de base para medir o efeito de qualquer formação ou supervisão "
      "futura."),
    P("Do terceiro objectivo espera-se a proporção de prescrições de "
      "arteméter-lumefantrina com dose conforme e a descrição dos tipos de "
      "erro. Espera-se que a maior parte das prescrições esteja conforme, "
      "como no Malawi {klootwijk2019}, e que os erros se concentrem nas "
      "crianças e nos episódios classificados apenas pela idade, por ser aí "
      "que a correspondência entre idade e peso falha {oms_directrizes2026}. "
      "A comparação entre a classificação pelo peso e pela idade nos "
      "episódios em que ambos constam quantifica, pela primeira vez no "
      "contexto local, o custo de dosear sem balança, argumento directo para "
      "acrescentar o peso ao livro de registo e para o reforçar na dispensa."),
    P("Do quarto objectivo esperam-se os factores associados ao "
      "sobretratamento e ao erro de dose, com razões ajustadas e intervalos "
      "de confiança. A literatura sugere que a estação seca, a ruptura de "
      "testes, o recurso à microscopia e a dosagem pela idade aumentem a "
      "probabilidade de incumprimento {amboko2021,koliopoulos2024}. "
      "Confirmadas ou não, estas associações dizem ao Programa Nacional de "
      "Controlo da Malária e à Direcção Provincial onde intervir primeiro, e "
      "a variação entre centros medida pelo modelo indica se o problema é "
      "geral da cidade ou concentrado em poucas unidades, o que muda a "
      "escolha entre formação alargada e supervisão dirigida."),
]
DIVULGACAO = [
    P("Os resultados serão apresentados em defesa pública na Faculdade de "
      "Ciências de Saúde da Universidade Lúrio, perante júri, e a "
      "monografia ficará depositada na biblioteca da instituição. Será "
      "entregue um relatório técnico, em português e com linguagem "
      "acessível, ao Serviço Distrital de Saúde, Mulher e Acção Social da "
      "Cidade de Nampula, à Direcção Provincial de Saúde de Nampula e à "
      "direcção de cada centro de saúde participante, acompanhado de uma "
      "sessão de devolução conjunta, de carácter formativo, em que cada "
      "centro recebe os seus próprios números e os compara com a média da "
      "cidade sem ser identificado perante os outros."),
    P("Está prevista a submissão de um artigo a uma revista científica com "
      "revisão por pares, de preferência de acesso aberto, e a apresentação "
      "de uma comunicação nas jornadas "
      "científicas da Universidade Lúrio. A ficha de extracção e o manual de "
      "classificação serão disponibilizados como material suplementar, para "
      "que a auditoria possa ser repetida noutros distritos. Não haverá "
      "divulgação de dados que permitam identificar doentes, profissionais "
      "ou unidades sanitárias."),
]

# ----------------------------------------------------- 11. cronograma -------
CRONOGRAMA_TEXTO = [
    P("O [[quadro:cronograma]] distribui as actividades por 12 meses, de "
      "Outubro de 2026 a Setembro de 2027. A submissão ao CIBS-UniLúrio e os "
      "pedidos de autorização ocupam Dezembro de 2026 e Janeiro de 2027; a "
      "verificação prévia em registos de 2025 faz-se em Fevereiro de 2027, "
      "já depois da aprovação; a recolha nos registos de 2026 decorre de "
      "Março a Junho de 2027, seguida da análise, da redacção e da defesa em "
      "Setembro de 2027."),
]
CRONOGRAMA = {
    "inicio": (2026, 10),
    "n_meses": 12,
    "actividades": [
        ("Revisão da literatura e redacção do protocolo", [1, 2]),
        ("Submissão ao CIBS-UniLúrio e pedidos de autorização ao SDSMAS e "
         "aos centros", [3, 4]),
        ("Validação da ficha pelo painel de peritos e formação dos "
         "extractores", [4, 5]),
        ("Verificação prévia em 30 registos de 2025 e ajuste da ficha", [5]),
        ("Construção da base de amostragem e selecção sistemática dos "
         "episódios", [5, 6]),
        ("Recolha nos registos de 2026, com dupla extracção de 10%",
         [6, 7, 8, 9]),
        ("Classificação independente da conformidade e cálculo do kappa",
         [8, 9]),
        ("Digitação dupla, limpeza e análise dos dados", [9, 10]),
        ("Redacção da monografia", [10, 11]),
        ("Revisão pelo orientador, correcções e entrega", [11]),
        ("Defesa pública e devolução dos resultados ao SDSMAS e aos centros",
         [12]),
    ],
}

# ----------------------------------------------------- 12. orcamento --------
ORCAMENTO_TEXTO = [
    P("A [[tabela:orcamento]] apresenta as rubricas do estudo em meticais, "
      "com 10% de imprevistos. O estudo será financiado pelo próprio "
      "estudante, com pedido de apoio à Faculdade de Ciências de Saúde para "
      "a impressão e para a divulgação. As rubricas maiores são o subsídio "
      "de alimentação e as deslocações dos dois extractores, cada um durante "
      "cerca de 40 dias de trabalho de campo em vários centros dispersos "
      "pela cidade, e a impressão das 1.220 fichas de extracção, que "
      "correspondem aos 1.081 episódios da amostra, às 109 fichas da dupla "
      "extracção e aos 30 registos da verificação prévia. O valor da taxa de "
      "submissão ao comité de bioética é uma estimativa [confirmar o valor "
      "em vigor junto do CIBS-UniLúrio]. Não há custos de licenças "
      "informáticas, porque a digitação usa o EpiData e a análise pode ser "
      "feita no R, ambos gratuitos."),
]
ORCAMENTO = [
    ("Impressão das fichas de extracção (1.220 fichas de 2 páginas)",
     "página", 2440, 5),
    ("Impressão do manual de preenchimento e dos critérios de conformidade",
     "página", 150, 5),
    ("Impressão e encadernação do protocolo e dos pedidos de autorização",
     "exemplar", 6, 400),
    ("Material de escritório (pastas, canetas, blocos, agrafador)",
     "conjunto", 1, 1500),
    ("Caixa de arquivo com fechadura para guarda das fichas", "unidade", 1,
     2500),
    ("Disco externo cifrado para cópias de segurança", "unidade", 1, 2500),
    ("Deslocações dos dois extractores aos centros de saúde",
     "viagem de ida e volta por pessoa", 80, 150),
    ("Subsídio de alimentação durante a verificação prévia e a recolha",
     "dia por pessoa", 80, 250),
    ("Subsídio ao segundo extractor e avaliador independente", "mês", 4,
     3000),
    ("Reunião do painel de peritos para validação da ficha", "sessão", 1,
     2000),
    ("Sessões de formação e calibração dos extractores", "sessão", 2, 1000),
    ("Comunicações e pacotes de internet", "mês", 12, 500),
    ("Taxa de submissão ao CIBS-UniLúrio (estimativa)", "taxa", 1, 2500),
    ("Impressão e encadernação da monografia final", "exemplar", 4, 800),
    ("Relatório técnico e material das sessões de devolução", "exemplar", 20,
     300),
    ("Póster e inscrição em jornada científica", "unidade", 1, 5000),
]
ORCAMENTO_IMPREVISTOS = 0.10

# ----------------------------------------------------- apendices ------------
APENDICES = [
    ("Ficha de extracção de dados dos livros de registo e das receitas", [
        NOTA("Instruções: preencher a esferográfica, uma ficha por episódio, "
             "sem escrever nome, número de processo ou morada. Fontes a "
             "consultar pela ordem indicada: livro de registo de doentes da "
             "consulta externa, livro de registo do laboratório do mesmo dia, "
             "receita ou requisição arquivada e mapa mensal de existências da "
             "farmácia. Campo não encontrado na fonte: assinalar «não "
             "registado»; campo encontrado mas ilegível: assinalar "
             "«ilegível». Não interpretar nem completar por dedução clínica."),
        H3("Secção I. Identificação do episódio"),
        CAMPO("Código do episódio (centro/mês/ordem): ____ / ____ / ______"),
        CAMPO("Data da consulta: ___/___/2026    Número de ordem no livro: "
              "________"),
        PERG("Estrato a que o episódio pertence:",
             ["A: com prescrição de antimalárico oral",
              "B: com teste de malária negativo",
              "A e B: teste negativo com antimalárico prescrito"]),
        PERG("Fontes efectivamente consultadas neste episódio:",
             ["Livro da consulta externa", "Livro do laboratório",
              "Receita ou requisição arquivada",
              "Mapa mensal de existências"],
             instrucao="Assinalar todas as que se aplicam."),
        H3("Secção II. Características do doente"),
        PERG("Sexo:", ["Masculino", "Feminino", "Não registado"]),
        PERG("Grupo etário na coluna do livro:",
             ["0-4 anos", "5-15 anos", "Mais de 15 anos", "Não registado"]),
        CAMPO("Idade exacta, se registada: ______ anos ou ______ meses"),
        CAMPO("Peso, se registado: ______ kg    ( ) Peso não registado"),
        H3("Secção III. Diagnóstico"),
        PERG("Método de diagnóstico registado:",
             ["Teste de diagnóstico rápido", "Microscopia",
              "Teste de diagnóstico rápido e microscopia",
              "Nenhum método registado"]),
        PERG("Resultado registado:",
             ["Positivo", "Negativo", "Inválido", "Não registado"]),
        PERG("O resultado consta do livro do laboratório para o mesmo dia e "
             "doente?", ["Sim", "Não", "Livro do laboratório indisponível"]),
        CAMPO("Diagnóstico escrito na coluna do livro: "
              "_______________________________"),
        H3("Secção IV. Tratamento"),
        PERG("Antimalárico prescrito:",
             ["Arteméter-lumefantrina", "Artesunato-amodiaquina",
              "Quinino oral", "Outro antimalárico oral",
              "Nenhum antimalárico"]),
        CAMPO("Outro antimalárico, qual: _______________________________"),
        CAMPO("Apresentação e dosagem registadas: "
              "_______________________________"),
        CAMPO("Quantidade total dispensada: ______ comprimidos"),
        CAMPO("Total previsto pelas normas para este doente, segundo o peso "
              "ou, na sua falta, a idade: ______ comprimidos (6, 12, 18 ou "
              "24)"),
        PERG("Base disponível para julgar a dose:",
             ["Peso em quilogramas", "Idade exacta em anos",
              "Apenas o grupo etário do livro",
              "Nenhuma: dose indeterminada"]),
        CAMPO("Outros medicamentos prescritos no mesmo episódio: "
              "_______________________________"),
        H3("Secção V. Classificação da conformidade"),
        NOTA("Aplicar o quadro de critérios de conformidade do protocolo. "
             "Cada item é classificado por dois avaliadores em separado; as "
             "discordâncias resolvem-se por consenso e, se persistirem, por "
             "um terceiro avaliador."),
        PERG("Confirmação antes do tratamento:",
             ["Confirmado: há resultado de teste registado",
              "Presuntivo justificado: ruptura de testes documentada no mês",
              "Presuntivo injustificado",
              "Não aplicável: episódio sem antimalárico"]),
        PERG("Resposta ao teste negativo:",
             ["Conforme: sem antimalárico", "Sobretratamento",
              "Não aplicável: teste não negativo"]),
        PERG("Escolha do antimalárico:",
             ["Conforme: arteméter-lumefantrina",
              "Alternativa sem justificação registada", "Não avaliável"]),
        PERG("Dose por toma:",
             ["Conforme", "Subdose", "Sobredose", "Indeterminada"]),
        PERG("Número de tomas e duração:",
             ["Conforme: seis tomas em três dias", "Esquema incompleto",
              "Esquema excessivo", "Indeterminado"]),
        H3("Secção VI. Qualidade do registo e contexto do mês"),
        PERG("Campos de data, idade, diagnóstico, resultado e tratamento "
             "preenchidos e legíveis?",
             ["Todos preenchidos e legíveis", "Um campo em falta ou ilegível",
              "Dois ou mais campos em falta ou ilegíveis"]),
        PERG("Houve existência nula de testes de diagnóstico rápido em alguma "
             "semana do mês, neste centro?",
             ["Sim", "Não", "Sem informação no mapa de existências"]),
        PERG("Houve existência nula de arteméter-lumefantrina em alguma "
             "semana do mês, neste centro?",
             ["Sim", "Não", "Sem informação no mapa de existências"]),
        PERG("Há indício de que este episódio repete um atendimento anterior "
             "do mesmo doente no mesmo centro?", ["Sim", "Não", "Não sei"]),
        CAMPO("Observações: _______________________________________________"),
        CAMPO("Extractor (iniciais): ______    Data: ___/___/2027    "
              "Ficha de dupla extracção: ( ) Sim  ( ) Não"),
    ]),
    ("Ficha de verificação prévia da completude dos registos", [
        NOTA("A verificação prévia faz-se em 30 registos de 2025 de um centro "
             "elegível, antes da recolha definitiva, e destina-se a medir a "
             "completude de cada campo da fonte e a decidir o destino das "
             "variáveis mal preenchidas. Regra de decisão escrita antes da "
             "recolha: campo preenchido em menos de 60% dos registos é "
             "retirado dos objectivos analíticos e passa a ser descrito "
             "apenas como lacuna de registo."),
        CAMPO("Centro de saúde (código): ______    Período dos registos "
              "verificados: ___/2025 a ___/2025"),
        CAMPO("Número de registos verificados: ______    Verificador "
              "(iniciais): ______    Data: ___/___/2027"),
        TABELA(None, None,
               ["Campo da fonte", "Registos preenchidos (n de 30)",
                "Percentagem", "Decisão (mantém, descreve como lacuna)"],
               [["Data da consulta", "", "", ""],
                ["Sexo", "", "", ""],
                ["Grupo etário", "", "", ""],
                ["Idade exacta em anos", "", "", ""],
                ["Peso em quilogramas", "", "", ""],
                ["Método de diagnóstico", "", "", ""],
                ["Resultado do teste", "", "", ""],
                ["Diagnóstico", "", "", ""],
                ["Medicamento prescrito", "", "", ""],
                ["Quantidade dispensada", "", "", ""],
                ["Resultado no livro do laboratório", "", "", ""],
                ["Mapa mensal de existências disponível", "", "", ""]],
               larguras=[5.4, 3.6, 2.6, 4.4]),
        CAMPO("Tempo médio de preenchimento de uma ficha: ______ minutos"),
        CAMPO("Abreviaturas e códigos locais encontrados, a incluir no "
              "manual: _______________________________________________"),
        CAMPO("Decisão final sobre a variável peso: ( ) mantém-se nos "
              "objectivos  ( ) passa a lacuna descrita"),
        CAMPO("Assinatura do investigador: ______________________    "
              "Assinatura do orientador: ______________________"),
    ]),
    ("Pedido de dispensa de consentimento informado", [
        P("Ao Comité Institucional de Bioética para a Saúde da Universidade "
          "Lúrio. O estudante abaixo identificado, do curso de Licenciatura "
          "em Farmácia da Faculdade de Ciências de Saúde da Universidade "
          "Lúrio, solicita a dispensa de obtenção de consentimento informado "
          "dos doentes cujos registos serão consultados no estudo "
          "«Conformidade do diagnóstico e do tratamento da malária não "
          "complicada com as normas nacionais nos centros de saúde públicos "
          "da cidade de Nampula, 2026»."),
        P("Fundamentam o pedido as seguintes razões. O estudo é documental e "
          "retrospectivo e recai sobre atendimentos ocorridos entre 1 de "
          "Janeiro e 31 de Dezembro de 2026, sendo impraticável localizar em "
          "2027 mais de mil doentes atendidos em consulta externa, tanto mais "
          "que os livros de registo não contêm contactos. A ficha de "
          "extracção não recolhe nome, número de processo, morada nem "
          "qualquer outro identificador directo, e cada episódio é "
          "designado por um código composto pelo código do centro, pelo mês "
          "e por um número de ordem, pelo que o risco de quebra de "
          "confidencialidade é mínimo. Não há intervenção sobre os doentes "
          "nem alteração dos cuidados prestados. A exigência de consentimento "
          "individual inviabilizaria uma avaliação de qualidade de cuidados "
          "de interesse público, situação prevista nas directrizes éticas "
          "internacionais para investigação relacionada com a saúde em seres "
          "humanos {cioms2016} e compatível com a Declaração de Helsínquia "
          "na sua revisão de 2024 {helsinki2025}."),
        P("O investigador compromete-se a consultar os livros dentro da "
          "unidade sanitária, sem os retirar, a guardar as fichas em caixa "
          "fechada à chave e os ficheiros em suporte cifrado, a apresentar "
          "resultados apenas agregados e com os centros codificados, a "
          "destruir os dados cinco anos após a defesa e a comunicar por "
          "escrito à direcção do centro e ao Serviço Distrital qualquer "
          "padrão sistemático de erro com potencial de dano detectado durante "
          "o trabalho de campo."),
        CAMPO("Investigador: [Nome do(a) estudante]    Contacto: [preencher]"),
        CAMPO("Orientador: [Nome e grau académico do(a) orientador(a)]    "
              "Contacto: [preencher]"),
        CAMPO("Nampula, ____ de ______________ de 2026    Assinatura: "
              "______________________"),
        CAMPO("Parecer do CIBS-UniLúrio: ( ) Deferido  ( ) Indeferido    "
              "Referência: ____________    Data: ___/___/______"),
    ]),
    ("Pedido de autorização institucional", [
        P("Exmo. Senhor Director do Serviço Distrital de Saúde, Mulher e "
          "Acção Social da Cidade de Nampula (com cópia à Direcção "
          "Provincial de Saúde de Nampula e à direcção de cada centro de "
          "saúde abrangido)."),
        P("O estudante abaixo identificado, do curso de Licenciatura em "
          "Farmácia da Faculdade de Ciências de Saúde da Universidade Lúrio, "
          "vem solicitar autorização para consultar, nos centros de saúde "
          "públicos desta cidade, os livros de registo de doentes da consulta "
          "externa, os livros de registo do laboratório, as receitas "
          "arquivadas e os mapas mensais de existências da farmácia "
          "relativos ao período de 1 de Janeiro a 31 de Dezembro de 2026, "
          "para a realização do estudo acima identificado, aprovado pelo "
          "Comité Institucional de Bioética para a Saúde da Universidade "
          "Lúrio."),
        P("A consulta será feita entre Março e Junho de 2027, em espaço "
          "cedido pela direcção de cada unidade e em horário combinado, de "
          "modo a não perturbar o atendimento; os documentos não sairão da "
          "unidade sanitária. Não serão recolhidos nomes, números de "
          "processo nem quaisquer outros identificadores de doentes ou de "
          "profissionais. Cada centro receberá, no final, um relatório com "
          "os seus próprios indicadores e uma sessão de devolução de "
          "carácter formativo, e os resultados publicados serão agregados e "
          "com os centros codificados."),
        CAMPO("Investigador: [Nome do(a) estudante]    Contacto: [preencher]"),
        CAMPO("Orientador: [Nome e grau académico do(a) orientador(a)]    "
              "Contacto: [preencher]"),
        CAMPO("Referência da aprovação do CIBS-UniLúrio: ________________    "
              "Data: ___/___/______"),
        CAMPO("Nampula, ____ de ______________ de 2027    Assinatura: "
              "______________________"),
        CAMPO("Despacho: ( ) Autorizado  ( ) Não autorizado    Nome e cargo: "
              "____________________    Assinatura e carimbo: "
              "______________________"),
    ]),
]
