# -*- coding: utf-8 -*-
"""
Tema 06: Padrao de prescricao segundo os indicadores da OMS em centros de
saude da cidade de Nampula (Farmacoepidemiologia e Uso Racional de
Medicamentos). Estudo documental retrospectivo, dados de 2026, recolha 2027.

Compor e validar:   python _motor/motor.py _conteudo/tema_06.py
Verificar fontes:   python _motor/refs.py verificar _conteudo/tema_06.py
"""
from blocos import (CAMPO, FORMULA, H3, LISTA, NOTA, P, PERG, QUADRO,
                    TABELA)

NUMERO = 6
SLUG = "Padrao_Prescricao_Indicadores_OMS_Centros_Saude_Nampula"
TITULO = ("Padrão de prescrição de medicamentos segundo os indicadores da "
          "Organização Mundial da Saúde nos centros de saúde públicos da "
          "cidade de Nampula, 2026")
DESENHO = ("Transversal retrospectivo, descritivo e analítico, documental "
           "(receitas e livros de registo de consultas externas)")

AUTOR = "[Nome do(a) estudante]"
ORIENTADOR = "[Nome e grau académico do(a) orientador(a)]"

# ---------------------------------------------------------------- resumo --
RESUMO = (
    "O uso irracional de medicamentos, sobretudo a prescrição excessiva de "
    "antibióticos e de injectáveis, aumenta os custos, expõe os doentes a "
    "reacções adversas e acelera a resistência aos antimicrobianos. Os "
    "estudos africanos com os indicadores de prescrição da "
    "Organização Mundial da Saúde descrevem consultas com mais medicamentos "
    "e mais antibióticos do que os valores de referência, mas não se "
    "encontrou nenhuma avaliação destes indicadores nos centros de "
    "saúde da cidade de Nampula. O estudo pretende avaliar o "
    "padrão de prescrição nos centros de saúde públicos da cidade, "
    "segundo os indicadores da Organização Mundial da Saúde e da "
    "Rede Internacional para o Uso Racional de Medicamentos. É um "
    "estudo transversal, retrospectivo, descritivo e analítico, baseado nas "
    "receitas e nos livros de registo das consultas externas curativas "
    "de 1 de Janeiro a 31 de Dezembro de 2026, com recolha em "
    "2027. Num cenário de dez centros, serão analisadas 960 "
    "consultas, seleccionadas por amostragem sistemática estratificada por "
    "centro e por mês, número que inclui um efeito de desenho de 2 e uma "
    "margem de 15% para registos inutilizáveis. Será usada uma ficha sem "
    "identificadores, com dupla extracção de 10% das consultas. Serão "
    "calculados o número médio de medicamentos por consulta, as percentagens de consultas com antibiótico e com injectável "
    "e as de medicamentos prescritos pela denominação comum "
    "internacional e constantes da lista nacional de medicamentos "
    "essenciais; os antibióticos serão classificados nos grupos Acesso, "
    "Vigilância e Reserva, e a sua adequação ao diagnóstico será julgada por "
    "dois avaliadores independentes. A análise usará intervalos de confiança "
    "a 95%, testes do qui-quadrado e regressão logística multinível. "
    "Espera-se quantificar os desvios face aos valores de referência e os "
    "factores associados à prescrição de antibióticos e de injectáveis, "
    "criando uma linha de base para as auditorias de prescrição e a gestão "
    "de antimicrobianos.")
PALAVRAS_CHAVE = ["antibióticos", "cuidados de saúde primários",
                  "Moçambique", "prescrição de medicamentos",
                  "uso racional de medicamentos"]
ABSTRACT = (
    "Irrational use of medicines, particularly the overprescription of "
    "antibiotics and injections, raises costs, exposes patients to adverse "
    "reactions and accelerates antimicrobial resistance. African studies "
    "using the World Health Organization prescribing indicators describe "
    "encounters with more medicines and more antibiotics than the reference "
    "values, but no assessment of these indicators in the health "
    "centres of Nampula City was found. The study intends to assess the "
    "prescribing pattern in the public health centres of the city, "
    "according to the indicators of the World Health Organization and the "
    "International Network for Rational Use of Drugs. It is a "
    "cross-sectional, retrospective, descriptive and analytical study based "
    "on the prescriptions and registers of the curative outpatient "
    "consultations from 1 January to 31 December 2026, with data "
    "collection in 2027. In a scenario of ten centres, 960 "
    "encounters will be analysed, selected by systematic sampling stratified "
    "by centre and by month, a number that includes a design effect of 2 and "
    "a 15% allowance for unusable records. A form without identifiers will "
    "be used, with double extraction of 10% of the encounters. "
    "The average number of medicines per encounter, the percentages of "
    "encounters with an antibiotic and with an injection, and those of "
    "medicines prescribed by international nonproprietary "
    "name and included in the national essential medicines list will be "
    "calculated; antibiotics will be classified into the Access, Watch and "
    "Reserve groups, and their appropriateness to the recorded diagnosis "
    "will be judged by two independent assessors. The analysis will use 95% "
    "confidence intervals, chi-square tests and multilevel logistic "
    "regression. The study is expected to quantify the deviations from the "
    "reference values and the factors associated with antibiotic and "
    "injection prescribing, creating a baseline for prescription audits and "
    "antimicrobial stewardship.")
KEYWORDS = ["antibiotics", "drug prescriptions", "Mozambique",
            "primary health care", "rational drug use"]

ABREVIATURAS = [
    ("ANARME", "Autoridade Nacional Reguladora de Medicamento"),
    ("ATC", "classificação Anatómica Terapêutica Química"),
    ("AWaRe", "Access, Watch, Reserve (grupos Acesso, Vigilância e "
              "Reserva da classificação de antibióticos da Organização "
              "Mundial da Saúde)"),
    ("CCI", "coeficiente de correlação intraclasse"),
    ("CIBS-UniLúrio", "Comité Institucional de Bioética para a Saúde da "
                      "Universidade Lúrio"),
    ("CID-10", "Classificação Internacional de Doenças, 10.ª revisão"),
    ("CMAM", "Central de Medicamentos e Artigos Médicos"),
    ("CNBS", "Comité Nacional de Bioética para a Saúde"),
    ("DCI", "denominação comum internacional"),
    ("DEFF", "efeito de desenho (do inglês design effect)"),
    ("DPS", "Direcção Provincial de Saúde"),
    ("FCS", "Faculdade de Ciências de Saúde"),
    ("FNM", "Formulário Nacional de Medicamentos"),
    ("HIV", "vírus da imunodeficiência humana"),
    ("IC", "intervalo de confiança"),
    ("INE", "Instituto Nacional de Estatística"),
    ("INRUD", "International Network for Rational Use of Drugs (Rede "
              "Internacional para o Uso Racional de Medicamentos)"),
    ("J01", "grupo dos antibacterianos de uso sistémico na classificação "
            "Anatómica Terapêutica Química"),
    ("LNME", "Lista Nacional de Medicamentos Essenciais"),
    ("MISAU", "Ministério da Saúde"),
    ("MOR", "mediana do odds ratio"),
    ("OMS", "Organização Mundial da Saúde"),
    ("OR", "odds ratio"),
    ("ORa", "odds ratio ajustado"),
    ("RAM", "resistência aos antimicrobianos"),
    ("RECORD-PE", "REporting of studies Conducted using Observational "
                  "Routinely-collected health Data, extensão para a "
                  "farmacoepidemiologia"),
    ("SDSMAS", "Serviço Distrital de Saúde, Mulher e Acção Social"),
    ("SNS", "Serviço Nacional de Saúde"),
    ("SPSS", "Statistical Package for the Social Sciences"),
    ("STROBE", "Strengthening the Reporting of Observational Studies in "
               "Epidemiology"),
    ("TDR", "teste de diagnóstico rápido"),
    ("UniLúrio", "Universidade Lúrio"),
]

# ------------------------------------------------------------ referencias --
FONTES = {
    # -- magnitude global da RAM e do uso de antibioticos
    "gbd2024": "GBD 2021 Antimicrobial Resistance Collaborators. Global burden of bacterial antimicrobial resistance 1990-2021: a systematic analysis with forecasts to 2050. Lancet. 2024;404(10459):1199-1226. doi:10.1016/S0140-6736(24)01867-1. PMID: 39299261.",
    "omsglass2025": "World Health Organization. WHO warns of widespread resistance to common antibiotics worldwide [Internet]. Geneva: World Health Organization; 2025 [citado 2026 Set 19]. Disponível em: https://www.who.int/news/item/13-10-2025-who-warns-of-widespread-resistance-to-common-antibiotics-worldwide",
    "omsunga2024": "World Health Organization. World leaders commit to decisive action on antimicrobial resistance [Internet]. Geneva: World Health Organization; 2024 [citado 2026 Set 19]. Disponível em: https://www.who.int/news/item/26-09-2024-world-leaders-commit-to-decisive-action-on-antimicrobial-resistance",
    "sulis2020": "Sulis G, Adam P, Nafade V, Gore G, Daniels B, Daftary A, et al. Antibiotic prescription practices in primary care in low- and middle-income countries: A systematic review and meta-analysis. PLoS Med. 2020;17(6):e1003139. doi:10.1371/journal.pmed.1003139. PMID: 32544153.",
    "song2025": "Song Q, Li J, Zhou P, Chen R, Liu Z, Li H, et al. Worldwide antibiotic prescription practices in primary care and associated factors: A systematic review and meta-analysis. Am J Infect Control. 2025;53(11):1137-1143. doi:10.1016/j.ajic.2025.08.009. PMID: 40825457.",
    "hailesilase2024": "Hailesilase GG, Welegebrial BG, Weres MG, Gebrewahd SA. WHO/INRUD prescribing indicators with a focus on antibiotics utilization patterns at outpatient department of Adigrat general hospital, Tigrai, Ethiopia: a retrospective cross-sectional study. Antimicrob Resist Infect Control. 2024;13(1):133. doi:10.1186/s13756-024-01490-6. PMID: 39506819.",
    # -- metodo e indicadores
    "oms1993": "World Health Organization. How to investigate drug use in health facilities: selected drug use indicators (WHO/DAP/93.1) [Internet]. Geneva: World Health Organization; 1993 [citado 2026 Set 19]. Disponível em: https://www.who.int/publications/i/item/who-dap-93.1",
    "oforiasenso2016": "Ofori-Asenso R, Brhlikova P, Pollock AM. Prescribing indicators at primary health care centers within the WHO African region: a systematic analysis (1995-2015). BMC Public Health. 2016;16:724. doi:10.1186/s12889-016-3428-8. PMID: 27545670.",
    "teni2020": "Teni FS, Wubishet BL, Yimenu DK. Assessment of medicine use among outpatients at healthcare facilities in Ethiopia using the WHO's prescribing indicators with a focus on antibiotics: a systematic review and meta-analysis. J Antimicrob Chemother. 2020;75(8):2044-2058. doi:10.1093/jac/dkaa124. PMID: 32437516.",
    "mohammed2021": "Mohammed SA, Faris AG. The Pattern of Medicine Use in Ethiopia Using the WHO Core Drug Use Indicators. Biomed Res Int. 2021;2021:7041926. doi:10.1155/2021/7041926. PMID: 34980999.",
    "atif2016": "Atif M, Sarwar MR, Azeem M, Naz M, Amir S, Nazir K. Assessment of core drug use indicators using WHO/INRUD methodology at primary healthcare centers in Bahawalpur, Pakistan. BMC Health Serv Res. 2016;16(1):684. doi:10.1186/s12913-016-1932-2. PMID: 27931213.",
    "nyabuti2020": "Nyabuti AO, Okalebo FA, Guantai EM. Examination of WHO/INRUD Core Drug Use Indicators at Public Primary Healthcare Centers in Kisii County, Kenya. Adv Pharmacol Pharm Sci. 2020;2020:3173847. doi:10.1155/2020/3173847. PMID: 32647831.",
    "niaz2019": "Niaz Q, Godman B, Massele A, Campbell S, Kurdi A, Kagoya HR, et al. Validity of World Health Organisation prescribing indicators in Namibia's primary healthcare: findings and implications. Int J Qual Health Care. 2019;31(5):338-345. doi:10.1093/intqhc/mzy172. PMID: 30169688.",
    "whocc2026": "WHO Collaborating Centre for Drug Statistics Methodology. Guidelines for ATC classification and DDD assignment [Internet]. Oslo: Norwegian Institute of Public Health; 2026 [citado 2026 Set 19]. Disponível em: https://atcddd.fhi.no/atc_ddd_index_and_guidelines/guidelines/",
    "omscid2019": "World Health Organization. International Statistical Classification of Diseases and Related Health Problems 10th Revision (ICD-10), version 2019 [Internet]. Geneva: World Health Organization; 2019 [citado 2026 Set 19]. Disponível em: https://icd.who.int/browse10/2019/en",
    # -- AWaRe e medicamentos essenciais
    "omsaware2025": "World Health Organization. The selection and use of essential medicines, 2025: WHO AWaRe (Access, Watch, Reserve) classification of antibiotics for evaluation and monitoring of use [Internet]. Geneva: World Health Organization; 2025 [citado 2026 Set 19]. Disponível em: https://www.who.int/publications/i/item/B09489",
    "omsaware2022": "World Health Organization. The WHO AWaRe (Access, Watch, Reserve) antibiotic book [Internet]. Geneva: World Health Organization; 2022 [citado 2026 Set 19]. Disponível em: https://www.who.int/publications/i/item/9789240062382",
    "moja2024": "Moja L, Zanichelli V, Mertz D, Gandra S, Cappello B, Cooke GS, et al. WHO's essential medicines and AWaRe: recommendations on first- and second-choice antibiotics for empiric treatment of clinical infections. Clin Microbiol Infect. 2024;30 Suppl 2:S1-S51. doi:10.1016/j.cmi.2024.02.003. PMID: 38342438.",
    "omseml2025": "World Health Organization. The selection and use of essential medicines, 2025: WHO Model List of Essential Medicines, 24th list [Internet]. Geneva: World Health Organization; 2025 [citado 2026 Set 19]. Disponível em: https://www.who.int/publications/i/item/B09474",
    "funiciello2024": "Funiciello E, Lorenzetti G, Cook A, Goelen J, Moore CE, Campbell SM, et al. Identifying AWaRe indicators for appropriate antibiotic use: a narrative review. J Antimicrob Chemother. 2024;79(12):3063-3077. doi:10.1093/jac/dkae370. PMID: 39422368.",
    "chigome2026": "Chigome AK, Cook A, Johnson Y, Essack S, Brink A, Mendelson M, et al. The Applicability of AWaRe-Based Antibiotic Quality Indicators to Assess the Appropriateness of Antibiotic Prescribing in Primary Healthcare in South Africa: A Multicentre Point Prevalence Study and Implications for the Future. Antibiotics (Basel). 2026;15(6). doi:10.3390/antibiotics15060562. PMID: 42353686.",
    "gres2024": "Gres E, Diallo IS, Besnier C, Diakité AA, Zair Z, Ouédraogo Yugbaré S, et al. Antibiotic prescribing practices according to the AWaRe classification among children under 5 of age attending public primary care centres in four West African countries: a cross-sectional study (AIRE project, 2021-2022). BMJ Paediatr Open. 2024;8(1). doi:10.1136/bmjpo-2024-002833. PMID: 39477340.",
    # -- determinantes
    "hopkins2017": "Hopkins H, Bruxvoort KJ, Cairns ME, Chandler CI, Leurent B, Ansah EK, et al. Impact of introduction of rapid diagnostic tests for malaria on antibiotic prescribing: analysis of observational and randomised studies in public and private healthcare settings. BMJ. 2017;356:j1054. doi:10.1136/bmj.j1054. PMID: 28356302.",
    "fink2020": "Fink G, D'Acremont V, Leslie HH, Cohen J. Antibiotic exposure among children younger than 5 years in low-income and middle-income countries: a cross-sectional study of nationally representative facility-based and household-based surveys. Lancet Infect Dis. 2020;20(2):179-187. doi:10.1016/S1473-3099(19)30572-9. PMID: 31843383.",
    # -- consequencias
    "guido2025": "Guido G, Frallonardo L, Asaduzzaman M, Farkas FB, De Vita E, Seni A, et al. Third-generation Cephalosporin resistance in Sub-Saharan Africa: a systematic review and meta-analysis. Commun Med (Lond). 2025;6(1):10. doi:10.1038/s43856-025-01243-5. PMID: 41258441.",
    "massinga2021": "Massinga AJ, Garrine M, Messa A Jr, Nobela NA, Boisen N, Massora S, et al. Klebsiella spp. cause severe and fatal disease in Mozambican children: antimicrobial resistance profile and molecular characterization. BMC Infect Dis. 2021;21(1):526. doi:10.1186/s12879-021-06245-x. PMID: 34090384.",
    # -- Mocambique e Nampula
    "ine2021": "Instituto Nacional de Estatística. IV Recenseamento Geral da População e Habitação 2017: resultados definitivos, província de Nampula [Internet]. Nampula: Instituto Nacional de Estatística; 2021 [citado 2026 Set 19]. Disponível em: http://www.sina.gov.mz/wp-content/uploads/2024/05/NAMPULA-RESUTADOS-DEFINITIVOS-DO-CENSO-2017.pdf",
    "misau2019": "Ministério da Saúde; Ministério da Agricultura e Segurança Alimentar. Plano Nacional de Acção Contra a Resistência Antimicrobiana 2019-2023 [Internet]. Maputo: Ministério da Saúde; 2019 [citado 2026 Set 19]. Disponível em: https://cdn.who.int/media/docs/default-source/antimicrobial-resistance/amr-spc-npm/nap-library/nap_20_11_2018---mozambique---2019-2023.pdf",
    "lei12de2017": "República de Moçambique. Lei n.º 12/2017, de 8 de Setembro: Lei do medicamento, vacinas e outros produtos biológicos para o uso humano. Boletim da República, I Série, n.º 141 [Internet]. Maputo: Imprensa Nacional de Moçambique; 2017 [citado 2026 Set 19]. Disponível em: https://anarme.gov.mz/download/lei-12-2017-de-8-de-setembro-lei-de-medicamento/",
    "misau2017": "Ministério da Saúde. Lista Nacional de Medicamentos Essenciais [Internet]. Maputo: Ministério da Saúde; 2017 [citado 2026 Set 19]. Disponível em: https://www.afro.who.int/sites/default/files/2018-07/LISTA%20NACIONAL%20DE%20MEDICAMENTOS%20ESSENCIAIS%202017.pdf",
    "mboane2025": "Mboane N. MISAU lança Formulário de Medicamentos e Lista de diagnósticos. O País [Internet]. Maputo: O País; 2025 [citado 2026 Set 19]. Disponível em: https://opais.co.mz/misau-lanca-formulario-de-medicamentos-e-lista-de-diagnosticos/",
    "lei3de2023": "República de Moçambique. Lei n.º 3/2023, de 8 de Junho: Lei de Investigação em Saúde Humana [Internet]. Maputo: Imprensa Nacional de Moçambique; 2023 [citado 2026 Set 19]. Disponível em: https://anarme.gov.mz/download/lei-3-2023-de-8-de-junho-lei-de-investigacao-em-saude-humana/",
    "wiseman2025": "Wiseman R, Truter I. Drug utilisation research and medicine access in Mozambique: An overview. Explor Res Clin Soc Pharm. 2025;17:100548. doi:10.1016/j.rcsop.2024.100548. PMID: 39759955.",
    "faiela2022": "Faiela C, Sevene E. Antibiotic prescription for HIV-positive patients in primary health care in Mozambique: A cross-sectional study. S Afr J Infect Dis. 2022;37(1):340. doi:10.4102/sajid.v37i1.340. PMID: 35284563.",
    "faiela2025": "Faiela C, Cambaco O, Boene H, Monnier AA, Wertheim HFL, Munguambe K, et al. Knowledge and practices of healthcare professionals regarding antibiotic use in a district hospital, Southern Mozambique: a cross-sectional study. Sci Rep. 2025;15(1):14333. doi:10.1038/s41598-025-99030-8. PMID: 40275041.",
    "faiela2026": "Faiela C, Moon TD, Sidat M, Sevene E. De-implementation of unnecessary antibiotic use for upper respiratory tract infections in ambulatory HIV care in Mozambique: a two-arm parallel cluster-randomized controlled hybrid type II trial. Implement Sci Commun. 2026;7(1). doi:10.1186/s43058-026-00957-4. PMID: 42106875.",
    "xavier2022": "Xavier SP, Victor A, Cumaquela G, Vasco MD, Rodrigues OAS. Inappropriate use of antibiotics and its predictors in pediatric patients admitted at the Central Hospital of Nampula, Mozambique. Antimicrob Resist Infect Control. 2022;11(1):79. doi:10.1186/s13756-022-01115-w. PMID: 35655272.",
    "xavier2024": "Xavier SP, da Silva AMC, Victor A. Antibiotic prescribing patterns in pediatric patients using the WHO access, watch, reserve (AWaRe) classification at a quaternary hospital in Nampula, Mozambique. Sci Rep. 2024;14(1):22719. doi:10.1038/s41598-024-72349-4. PMID: 39349590.",
    "mate2019": "Mate I, Come CE, Gonçalves MP, Cliff J, Gudo ES. Knowledge, attitudes and practices regarding antibiotic use in Maputo City, Mozambique. PLoS One. 2019;14(8):e0221452. doi:10.1371/journal.pone.0221452. PMID: 31437215.",
    # -- estudos empiricos africanos e outros (estado da arte)
    "wendie2021": "Wendie TF, Ahmed A, Mohammed SA. Drug use pattern using WHO core drug use indicators in public health centers of Dessie, North-East Ethiopia. BMC Med Inform Decis Mak. 2021;21(1):197. doi:10.1186/s12911-021-01530-w. PMID: 34172067.",
    "mashalla2017": "Mashalla Y, Setlhare V, Massele A, Sepako E, Tiroyakgosi C, Kgatlwane J, et al. Assessment of prescribing practices at the primary healthcare facilities in Botswana with an emphasis on antibiotics: Findings and implications. Int J Clin Pract. 2017;71(12). doi:10.1111/ijcp.13042. PMID: 29178350.",
    "ogaji2023": "Ogaji DS, Nwaejike D, Ebiekuraju O. Quality of Drug Prescribing and Dispensing Practices in Primary Healthcare Centres in an Urban Local Government Area in Nigeria. West Afr J Med. 2023;40(9):925-934. PMID: 37767782.",
    "agahmed2024": "Ag Ahmed MA, Ravinetto R, Diop K, Trasancos Buitrago V, Dujardin C. Evaluation of Rational Medicines Use Based on World Health Organization Core Indicators: A Cross-Sectional Study in Five Health Districts in Mauritania. Integr Pharm Res Pract. 2024;13:17-29. doi:10.2147/IPRP.S447664. PMID: 38566890.",
    "manirakiza2025": "Manirakiza A, Maru SM, Nyamu DG, Bizimana T, Nimpagaritse M. Antimicrobial prescribing patterns among pediatric outpatient encounters in primary healthcare centers in Bujumbura Mairie, Burundi. BMC Prim Care. 2025;26(1):236. doi:10.1186/s12875-025-02944-5. PMID: 40750850.",
    "ahiabu2016": "Ahiabu MA, Tersbøl BP, Biritwum R, Bygbjerg IC, Magnussen P. A retrospective audit of antibiotic prescriptions in primary health-care facilities in Eastern Region, Ghana. Health Policy Plan. 2016;31(2):250-8. doi:10.1093/heapol/czv048. PMID: 26045328.",
    "kilipamwambu2021": "Kilipamwambu A, Bwire GM, Myemba DT, Njiro BJ, Majigo MV. WHO/INRUD core prescribing indicators and antibiotic utilization patterns among primary health care facilities in Ilala district, Tanzania. JAC Antimicrob Resist. 2021;3(2):dlab049. doi:10.1093/jacamr/dlab049. PMID: 34223117.",
    "muwanguzi2021": "Muwanguzi TE, Yadesa TM, Agaba AG. Antibacterial prescription and the associated factors among outpatients diagnosed with respiratory tract infections in Mbarara Municipality, Uganda. BMC Pulm Med. 2021;21(1):374. doi:10.1186/s12890-021-01739-5. PMID: 34781920.",
    "gasson2018": "Gasson J, Blockman M, Willems B. Antibiotic prescribing practice and adherence to guidelines in primary care in the Cape Town Metro District, South Africa. S Afr Med J. 2018;108(4):304-310. doi:10.7196/SAMJ.2017.v108i4.12564. PMID: 29629681.",
    # -- intervencoes
    "foxlee2021": "Foxlee ND, Townell N, Heney C, McIver L, Lau CL. Strategies Used for Implementing and Promoting Adherence to Antibiotic Guidelines in Low- and Lower-Middle-Income Countries: A Systematic Review. Trop Med Infect Dis. 2021;6(3). doi:10.3390/tropicalmed6030166. PMID: 34564550.",
    # -- metodologia, estatistica e etica
    "langan2018": "Langan SM, Schmidt SA, Wing K, Ehrenstein V, Nicholls SG, Filion KB, et al. The reporting of studies conducted using observational routinely collected health data statement for pharmacoepidemiology (RECORD-PE). BMJ. 2018;363:k3532. doi:10.1136/bmj.k3532. PMID: 30429167.",
    "serdar2021": "Serdar CC, Cihan M, Yücel D, Serdar MA. Sample size, power and effect size revisited: simplified and practical approaches in pre-clinical, clinical and laboratory studies. Biochem Med (Zagreb). 2021;31(1):010502. doi:10.11613/BM.2021.010502. PMID: 33380887.",
    "peduzzi1996": "Peduzzi P, Concato J, Kemper E, Holford TR, Feinstein AR. A simulation study of the number of events per variable in logistic regression analysis. J Clin Epidemiol. 1996;49(12):1373-9. doi:10.1016/s0895-4356(96)00236-3. PMID: 8970487.",
    "austin2017": "Austin PC, Merlo J. Intermediate and advanced topics in multilevel logistic regression analysis. Stat Med. 2017;36(20):3257-3277. doi:10.1002/sim.7336. PMID: 28543517.",
    "mchugh2012": "McHugh ML. Interrater reliability: the kappa statistic. Biochem Med (Zagreb). 2012;22(3):276-82. PMID: 23092060.",
    "wma2025": "World Medical Association. World Medical Association Declaration of Helsinki: Ethical Principles for Medical Research Involving Human Participants. JAMA. 2025;333(1):71-74. doi:10.1001/jama.2024.21972. PMID: 39425955.",
}

SEMINAIS = {
    "oms1993": ("Manual original da OMS que define os indicadores de "
                "prescrição, as suas fórmulas e as regras de amostragem; "
                "continua a ser a norma de referência citada pelos estudos "
                "recentes."),
    "peduzzi1996": ("Estudo de simulação que fundamenta a regra de pelo "
                    "menos 10 eventos por variável na regressão logística."),
    "mchugh2012": ("Artigo de referência sobre a interpretação do kappa de "
                   "Cohen em investigação em saúde, usado para a "
                   "concordância entre extractores e entre avaliadores."),
}

# ----------------------------------------------------- 1. introducao --------
INTRODUCAO = [
    P("A prescrição é o acto que encerra a maior parte das consultas "
      "curativas e condiciona tudo o que se segue: o que a farmácia dispensa, "
      "o que o doente toma, quanto custa o tratamento e que riscos corre. A "
      "Organização Mundial da Saúde (OMS) considera que o uso de medicamentos "
      "é racional quando os doentes recebem os medicamentos adequados às suas "
      "necessidades clínicas, em doses ajustadas às suas características "
      "individuais, durante o período necessário e ao menor custo; estima-se, "
      "no entanto, que mais de metade de todos os medicamentos seja "
      "prescrita, dispensada ou vendida de forma inadequada em todo o mundo "
      "{hailesilase2024}. Uma receita com medicamentos a mais, com um "
      "antibiótico sem indicação ou com um injectável evitável repercute-se, "
      "assim, na segurança do doente e na sustentabilidade do sistema de "
      "saúde."),
    P("A consequência mais grave do uso irracional é a resistência aos "
      "antimicrobianos (RAM). A análise do estudo Global Burden of Disease "
      "estimou que, em 2021, 4,71 milhões de mortes estiveram associadas à "
      "RAM bacteriana e 1,14 milhões lhe foram directamente atribuíveis, e "
      "projecta 8,22 milhões de mortes associadas em 2050 {gbd2024}. Segundo "
      "a vigilância da OMS, uma em cada seis infecções bacterianas "
      "confirmadas laboratorialmente no mundo era resistente em 2023, "
      "proporção que sobe para uma em cada cinco na Região Africana, onde a "
      "resistência de *Escherichia coli* e de *Klebsiella pneumoniae* às "
      "cefalosporinas de terceira geração ultrapassa 70% {omsglass2025}. Os "
      "cuidados de saúde primários concentram o maior volume de prescrições: "
      "numa meta-análise de 48 estudos em 27 países de rendimento baixo e "
      "médio, 52% dos doentes atendidos nesse nível receberam um antibiótico "
      "{sulis2020}, e uma revisão mundial de 174 estudos estimou em 57,6% a "
      "proporção de prescrições inadequadas, sem descida significativa da "
      "prescrição em 20 anos {song2025}."),
    P("Para medir estas práticas de forma comparável, a OMS e a "
      "International Network for Rational Use of Drugs (INRUD) publicaram em "
      "1993 um conjunto de indicadores de uso de medicamentos, cinco dos "
      "quais descrevem a prescrição: o número médio de medicamentos por "
      "consulta, as percentagens de consultas com antibiótico e com "
      "injectável e as percentagens de medicamentos prescritos pelo nome "
      "genérico e a partir da lista de medicamentos essenciais {oms1993}. Na "
      "Região Africana da OMS, uma análise de 43 estudos em 11 países, com "
      "141.323 consultas em 572 unidades de cuidados primários, encontrou "
      "valores medianos de 3,1 medicamentos por consulta, antibiótico em "
      "46,8% e injectável em 25,0% das consultas, 68,0% dos medicamentos "
      "prescritos pelo nome genérico e 88,0% constantes da lista, afastados "
      "das metas da OMS e sem tendência consistente entre 1995 e 2015 "
      "{oforiasenso2016}. Revisões mais recentes na Etiópia confirmam a "
      "prescrição excessiva de antibióticos {teni2020,mohammed2021}, que "
      "aumenta com o número de medicamentos por receita {teni2020}."),
    P("Em Moçambique, o quadro legal favorece a prescrição racional: a Lei "
      "n.º 12/2017 determina que o Serviço Nacional de Saúde (SNS) use "
      "apenas medicamentos do Formulário Nacional de Medicamentos (FNM) ou da "
      "lista de medicamentos essenciais e torna obrigatória a prescrição pela "
      "denominação comum internacional (DCI) {lei12de2017}. O Plano Nacional "
      "de Acção Contra a Resistência Antimicrobiana 2019-2023 reconhece, "
      "contudo, que o uso de testes rápidos da malária, sem um teste que "
      "exclua a infecção bacteriana, favorece o uso indiscriminado de "
      "antibióticos nas febres não maláricas {misau2019}. A evidência "
      "nacional sobre a prescrição é escassa e fragmentada: em oito unidades "
      "de cuidados primários do sul do país, "
      "65,9% das receitas de doentes com infecção pelo vírus da "
      "imunodeficiência humana (HIV) incluíam antibióticos {faiela2022}; num "
      "hospital distrital do sul, 88% das receitas tinham pelo menos um "
      "antibiótico {faiela2025}; e, no Hospital Central de Nampula, 97,5% "
      "das crianças internadas receberam antibióticos, quase sempre por via "
      "parentérica {xavier2022}. A investigação de utilização de medicamentos "
      "continua pouco desenvolvida na África subsariana, e Moçambique não é "
      "excepção, pela falta de bases de dados que registem a prescrição "
      "{wiseman2025}."),
    P("A província de Nampula é a mais populosa de Moçambique, com 5.758.920 "
      "habitantes no censo de 2017, o equivalente a 20,6% da população "
      "nacional, e o distrito da cidade de Nampula tinha então 798.462 "
      "residentes, 13,9% do total provincial {ine2021}. Os centros de saúde "
      "públicos da cidade, sob gestão do Serviço Distrital de Saúde, Mulher e "
      "Acção Social (SDSMAS), constituem o nível primário do SNS "
      "{misau2017}. Os estudos publicados sobre prescrição "
      "em Nampula incidem sobre o internamento pediátrico de nível "
      "quaternário {xavier2022,xavier2024}, e não foi encontrado, nas bases "
      "consultadas, nenhum estudo que aplique os indicadores de prescrição da "
      "OMS aos centros de saúde da cidade."),
    P("Este estudo propõe-se avaliar o padrão de prescrição de medicamentos "
      "nos centros de saúde públicos da cidade de Nampula, a partir das "
      "consultas externas curativas realizadas em 2026, com os indicadores de "
      "prescrição da OMS e da INRUD, completados pela classificação dos "
      "antibióticos nos grupos Acesso, Vigilância e Reserva (AWaRe) da OMS, "
      "pela avaliação da adequação da antibioterapia ao diagnóstico registado "
      "e pela análise dos factores associados à prescrição de antibióticos e "
      "de injectáveis. Pretende-se produzir uma linha de base local, "
      "comparável com a literatura africana, que apoie o SDSMAS, a Direcção "
      "Provincial de Saúde (DPS) e os próprios prescritores na melhoria da "
      "prescrição nos cuidados primários."),
]

# ----------------------------------------------------- 2. problema ----------
PROBLEMA = [
    P("Os centros de saúde da cidade de Nampula atendem diariamente adultos "
      "e crianças com queixas agudas. Nos cuidados primários dos países de "
      "rendimento baixo e médio, a febre e a tosse motivam a grande maioria "
      "das consultas de crianças com menos de 5 anos, 85,4% num estudo em "
      "oito países, e os "
      "antibióticos são prescritos a 80,5% das crianças com doença "
      "respiratória, a 50,1% das crianças com diarreia e a 28,3% das crianças "
      "com malária {fink2020}. O prescritor decide frequentemente sem apoio "
      "laboratorial para além do teste de diagnóstico rápido (TDR) da "
      "malária, e um TDR negativo desloca a incerteza diagnóstica para os "
      "antibióticos: numa análise de nove estudos em África e na Ásia, "
      "receberam antibiótico 69% dos doentes com teste negativo e 40% dos "
      "doentes com teste positivo {hopkins2017}. O plano nacional de combate "
      "à RAM identifica exactamente este mecanismo em Moçambique "
      "{misau2019}."),
    P("As consequências são clínicas, económicas e ecológicas. A prescrição "
      "desnecessária de antibióticos selecciona bactérias resistentes num "
      "contexto em que a resistência às cefalosporinas de terceira geração na "
      "África subsariana atingiu 45,3% numa meta-análise de 200 estudos, "
      "tendo subido de 22,8% antes de 2009 para 42,0% entre 2020 e 2024 "
      "{guido2025}. Em crianças moçambicanas com bacteriemia por *Klebsiella*, "
      "48,9% dos isolados de doentes internados e 69,6% dos isolados colhidos "
      "*post mortem* eram resistentes à ceftriaxona, e a letalidade associada "
      "à infecção foi de 30,7% {massinga2021}. A isto somam-se os riscos das injecções "
      "desnecessárias, os custos para o SNS e para as famílias e a mensagem "
      "implícita de que cada queixa exige um medicamento, que alimenta a "
      "automedicação: em Maputo, 20,9% dos adultos inquiridos tinham usado "
      "antibióticos sem receita, adquiridos sobretudo em farmácias "
      "{mate2019}."),
    P("Apesar desta relevância, os serviços de saúde da cidade de Nampula "
      "não dispõem de uma medida sistemática do padrão de prescrição nos "
      "centros de saúde. Não se sabe quantos medicamentos são prescritos, em "
      "média, por consulta, em que proporção das consultas se prescrevem "
      "antibióticos e injectáveis, se a obrigação legal de prescrever pela "
      "DCI e dentro da lista nacional é cumprida, que antibióticos "
      "predominam, em que medida são usados em diagnósticos que não os "
      "justificam, nem que doentes, prescritores e diagnósticos concentram a "
      "prescrição de antibióticos e de injectáveis. Sem esta linha de base, "
      "as auditorias de prescrição e as equipas de gestão de antimicrobianos "
      "previstas no plano nacional {misau2019} não têm onde apoiar as suas "
      "prioridades, e não será possível medir o efeito da nova edição do FNM "
      "apresentada pelo Ministério da Saúde (MISAU) em Maio de 2025 "
      "{mboane2025}."),
]
PERGUNTA = ("Qual é o padrão de prescrição de medicamentos nos centros de "
            "saúde públicos da cidade de Nampula, avaliado pelos indicadores "
            "de prescrição da OMS e da INRUD, e que características do doente, "
            "do prescritor e da consulta se associam à prescrição de "
            "antibióticos e de injectáveis nas consultas externas curativas "
            "realizadas em 2026?")
DELIMITACAO = [
    P("O estudo decorre nos centros de saúde públicos da cidade de Nampula "
      "sob gestão do SDSMAS da Cidade de Nampula que realizem consultas "
      "externas curativas e disponham de farmácia própria. A população de "
      "estudo é constituída pelas consultas externas curativas de adultos e "
      "de crianças realizadas entre 1 de Janeiro e 31 de Dezembro de 2026 e "
      "documentadas nas receitas arquivadas e nos livros de registo de "
      "consultas; a consulta dos arquivos decorrerá entre Fevereiro e Maio de "
      "2027, depois da aprovação ética e das autorizações institucionais. O objecto "
      "de estudo compreende os cinco indicadores de prescrição da OMS e da "
      "INRUD, a composição terapêutica das receitas, a classificação AWaRe dos "
      "antibióticos, a adequação da antibioterapia ao diagnóstico registado e "
      "os factores associados à prescrição de antibióticos e de injectáveis."),
    P("Ficam fora do âmbito os hospitais de qualquer nível, as unidades "
      "privadas e militares, o internamento, a maternidade e as consultas de "
      "programas com esquemas terapêuticos normalizados, como o tratamento "
      "anti-retroviral, a tuberculose, a consulta pré-natal e o planeamento "
      "familiar, cuja inclusão distorceria os indicadores de uma consulta "
      "curativa geral. Ficam igualmente fora os indicadores de cuidados ao "
      "doente e de unidade sanitária da metodologia da OMS, como o tempo de "
      "consulta e de dispensa, a rotulagem, o conhecimento do doente e a "
      "disponibilidade de medicamentos, que exigem observação prospectiva, "
      "bem como a avaliação das doses, da duração dos tratamentos e dos "
      "resultados clínicos."),
]

# ----------------------------------------------------- 3. objectivos --------
OBJECTIVO_GERAL = (
    "Avaliar o padrão de prescrição de medicamentos nos centros de saúde "
    "públicos da cidade de Nampula, segundo os indicadores de prescrição da "
    "OMS e da INRUD, nas consultas externas curativas realizadas entre "
    "Janeiro e Dezembro de 2026.")
OBJECTIVOS_ESPECIFICOS = [
    "Caracterizar as consultas amostradas segundo as características do "
    "doente (idade e sexo), do prescritor (categoria profissional) e da "
    "consulta (centro de saúde, mês e grupo diagnóstico registado).",
    "Determinar os cinco indicadores de prescrição da OMS e da INRUD, no "
    "conjunto e por centro de saúde, compará-los entre centros e confrontá-los "
    "com os valores de referência adoptados na literatura.",
    "Descrever os medicamentos prescritos por grupo terapêutico da "
    "classificação Anatómica Terapêutica Química (ATC) e os antibióticos "
    "segundo os grupos Acesso, Vigilância e Reserva da OMS.",
    "Estimar a proporção de consultas com antibiótico em que o diagnóstico "
    "registado não justifica, em regra, a antibioterapia.",
    "Analisar os factores do doente, do prescritor e da consulta associados "
    "à prescrição de antibióticos e de injectáveis.",
]

# ----------------------------------------------------- 4. hipoteses ---------
HIPOTESES_INTRO = [
    P("As hipóteses referem-se às componentes analíticas do estudo, isto é, "
      "à comparação entre centros de saúde prevista no objectivo específico "
      "2 e aos factores associados previstos no objectivo específico 5, e "
      "serão testadas com um nível de significância de 5%."),
]
HIPOTESES = [
    ("H0 (objectivo específico 2)",
     "o número médio de medicamentos por consulta e as percentagens de "
     "consultas com antibiótico e com injectável não diferem entre os "
     "centros de saúde da cidade de Nampula;"),
    ("H1 (objectivo específico 2)",
     "pelo menos um destes indicadores difere entre os centros de saúde da "
     "cidade de Nampula;"),
    ("H0 (objectivo específico 5, antibióticos)",
     "a prescrição de antibióticos não está associada à idade e ao sexo do "
     "doente, à categoria profissional do prescritor, ao grupo diagnóstico, "
     "à prescrição de antimalárico, ao número de medicamentos não "
     "antibióticos e à estação do ano;"),
    ("H1 (objectivo específico 5, antibióticos)",
     "a prescrição de antibióticos está associada a pelo menos uma destas "
     "características;"),
    ("H0 (objectivo específico 5, injectáveis)",
     "a prescrição de injectáveis não está associada às mesmas "
     "características do doente, do prescritor e da consulta;"),
    ("H1 (objectivo específico 5, injectáveis)",
     "a prescrição de injectáveis está associada a pelo menos uma destas "
     "características."),
]
QUESTOES = [
    "Qual é o perfil das consultas amostradas quanto à idade e ao sexo do "
    "doente, à categoria do prescritor e ao grupo diagnóstico registado?",
    "Que grupos terapêuticos e que antibióticos são mais prescritos, e que "
    "proporção dos antibióticos prescritos pertence ao grupo Acesso?",
    "Em que proporção das consultas com antibiótico o diagnóstico registado "
    "não justifica, em regra, a antibioterapia?",
]

# ----------------------------------------------------- 5. justificativa -----
JUSTIFICATIVA_INTRO = [
    P("A escolha do tema responde a uma lacuna concreta de conhecimento e a "
      "uma prioridade explícita das políticas nacionais de saúde. A "
      "pertinência do estudo organiza-se em quatro dimensões "
      "complementares: científica, académica, social e política."),
]
JUSTIFICATIVA = {
    "cientifica": [
        P("A literatura africana sobre os indicadores de prescrição é "
          "extensa, mas assimétrica: a síntese regional reuniu estudos de "
          "apenas 11 países {oforiasenso2016}, e a Etiópia dispõe de revisões "
          "próprias {teni2020,mohammed2021}. Em Moçambique, os estudos "
          "disponíveis avaliam subgrupos, como os doentes com HIV no sul "
          "{faiela2022}, um hospital distrital {faiela2025} ou o internamento "
          "pediátrico em Nampula {xavier2022,xavier2024}; nenhum mede os "
          "indicadores nos centros de saúde de uma cidade do norte. O estudo "
          "produz, tanto quanto foi possível apurar, a primeira estimativa "
          "local obtida com um método padronizado e comparável com a "
          "literatura regional."),
        P("O estudo acrescenta aos indicadores clássicos duas dimensões que a "
          "literatura recente considera indispensáveis. Os indicadores da OMS "
          "medem o volume e não a adequação e, na Namíbia, mostraram fraca "
          "capacidade para prever o cumprimento das normas terapêuticas "
          "nacionais {niaz2019}. A classificação AWaRe dos antibióticos e a "
          "avaliação da antibioterapia face ao diagnóstico registado, "
          "propostas como base dos novos indicadores de qualidade "
          "{funiciello2024,chigome2026}, permitem distinguir entre muito "
          "antibiótico e antibiótico mal escolhido. A análise multinível dos "
          "factores associados, com o centro de saúde como nível superior, "
          "separa o efeito das características das consultas da variação "
          "entre unidades sanitárias {austin2017}."),
    ],
    "academica": [
        P("Para a Licenciatura em Farmácia da Faculdade de Ciências de Saúde "
          "(FCS) da Universidade Lúrio (UniLúrio), o estudo exercita "
          "competências centrais do farmacêutico em farmacoepidemiologia: a "
          "amostragem de registos clínicos, a classificação ATC e AWaRe dos "
          "medicamentos, a medição da "
          "concordância entre avaliadores e a modelação estatística de dados "
          "agrupados. Prolonga ainda uma linha de investigação do "
          "Departamento de Farmácia da UniLúrio sobre o uso de antibióticos no "
          "Hospital Central de Nampula {xavier2022}, estendendo-a aos cuidados "
          "primários, onde se concentra a maior parte do uso de antibióticos "
          "{gasson2018}."),
        P("A ficha de extracção, o dicionário de classificação dos "
          "medicamentos e o protocolo de amostragem ficam disponíveis para "
          "auditorias periódicas em futuros trabalhos de fim de curso, o que "
          "permitirá construir séries temporais comparáveis e avaliar, ano a "
          "ano, o efeito de intervenções formativas e de mudanças no FNM."),
    ],
    "social": [
        P("A exposição a antibióticos começa cedo: nos países de rendimento "
          "baixo e médio, uma criança recebe em média 24,5 prescrições de "
          "antibióticos até aos 5 anos, grande parte das quais parece "
          "desnecessária {fink2020}. Cada prescrição evitável expõe o doente a "
          "efeitos adversos e a custos e alimenta uma resistência que penaliza "
          "sobretudo quem tem menos alternativas terapêuticas {massinga2021}."),
        P("A prescrição dos serviços públicos repercute-se também na "
          "comunidade: em Maputo, parte dos adultos que usaram antibióticos "
          "sem receita justificou-o com sintomas semelhantes a um episódio "
          "anterior {mate2019}. Ao identificar onde se concentram os desvios, por "
          "centro, por grupo etário e por diagnóstico, o estudo permite "
          "intervenções dirigidas e não punitivas, com benefício directo para "
          "os utentes dos centros de saúde da cidade de Nampula."),
    ],
    "politica": [
        P("O estudo responde a instrumentos normativos concretos. Mede o "
          "cumprimento dos artigos 33 e 34 da Lei n.º 12/2017, que restringem "
          "o sector público aos medicamentos do FNM e da lista de medicamentos "
          "essenciais e tornam obrigatória a prescrição pela DCI "
          "{lei12de2017}, e fornece dados para as auditorias de prescrição e "
          "para as equipas de gestão de antimicrobianos previstas no plano "
          "nacional de combate à RAM {misau2019}. No plano internacional, a "
          "declaração política da Assembleia Geral das Nações Unidas de 2024 "
          "fixou a meta de que pelo menos 70% dos antibióticos usados na saúde "
          "humana pertençam ao grupo Acesso {omsunga2024}; sem medir "
          "a proporção actual, o país não consegue acompanhar esta meta ao "
          "nível dos cuidados primários."),
        P("Os resultados serão úteis ao SDSMAS e à DPS para orientar a "
          "formação contínua dos prescritores e a supervisão das unidades, e à "
          "Central de Medicamentos e Artigos Médicos (CMAM) e à Autoridade "
          "Nacional Reguladora de Medicamento (ANARME) para ajustar a "
          "selecção, a quantificação e a informação sobre os medicamentos "
          "usados nos cuidados primários."),
    ],
}

# ----------------------------------------------------- 6. revisao -----------
REVISAO = [
    ("Uso racional de medicamentos e definições operacionais", [
        P("O uso racional de medicamentos exige que cada doente receba o "
          "medicamento adequado à sua necessidade clínica, na dose e durante "
          "o tempo correctos e ao menor custo {hailesilase2024}. A prescrição "
          "é a etapa em que este princípio se decide. No manual da OMS sobre a investigação do uso "
          "de medicamentos em unidades sanitárias, os indicadores de "
          "prescrição são calculados a partir de uma amostra de consultas, "
          "isto é, de encontros entre doentes e prescritores, numa ou em "
          "várias unidades {oms1993}. Neste estudo, a consulta é "
          "operacionalizada como a receita emitida numa consulta externa "
          "curativa a um doente, numa data, por um prescritor."),
        P("Três definições condicionam o cálculo dos indicadores. Conta-se "
          "como medicamento cada produto distinto prescrito, sendo uma "
          "associação em dose fixa contada como um só medicamento. Considera-se "
          "prescrito pela DCI o medicamento designado pela denominação comum "
          "internacional das suas substâncias activas, ou pela designação "
          "genérica aceite de uma associação, e não por uma marca comercial; "
          "em Moçambique esta forma de prescrição é obrigatória por lei "
          "{lei12de2017}. Considera-se medicamento essencial o que consta da "
          "Lista Nacional de Medicamentos Essenciais (LNME), aprovada pelo "
          "Diploma Ministerial n.º 58/2016 e alterada em 2017, com 406 "
          "substâncias activas e 578 apresentações, das quais 97 substâncias "
          "e 114 apresentações pertencem à lista de medicamentos de "
          "especialidade {misau2017}. A LNME inspira-se na lista modelo da "
          "OMS, cuja 24.ª edição foi publicada em 2025 {omseml2025}."),
        P("Para efeitos deste estudo, o antibiótico é um medicamento do grupo "
          "dos antibacterianos de uso sistémico (J01) da classificação "
          "ATC, a que se juntam o metronidazol e o tinidazol orais, usados nos "
          "cuidados primários sobretudo como antibacterianos; os "
          "antituberculosos, os antimaláricos, os antivirais e os antifúngicos "
          "ficam excluídos, e os antibacterianos tópicos contam como "
          "medicamentos mas não como antibióticos {whocc2026}. A classificação "
          "AWaRe da OMS distribui os antibióticos em três grupos: o grupo "
          "Acesso reúne as opções de primeira e de segunda escolha para as "
          "infecções comuns, com menor potencial de seleccionar resistências; "
          "o grupo Vigilância reúne antibióticos com maior potencial de "
          "resistência, que devem ser prioridade da gestão de antimicrobianos; "
          "e o grupo Reserva reúne os antibióticos de último recurso para "
          "infecções por bactérias multirresistentes {omsaware2025,moja2024}. "
          "A OMS recomenda que o grupo Acesso represente pelo menos 60% dos "
          "antibióticos prescritos {gres2024}, limiar que a declaração das "
          "Nações Unidas de 2024 elevou para 70% {omsunga2024}. "
          "Considera-se injectável todo o medicamento prescrito por via "
          "intramuscular, intravenosa ou subcutânea, com exclusão das vacinas "
          "e dos contraceptivos injectáveis, que não correspondem a uma "
          "decisão terapêutica curativa."),
    ]),
    ("Os indicadores de prescrição da OMS e da INRUD: método, referências e "
     "limitações", [
        P("Os indicadores de prescrição foram concebidos para descrever, com "
          "poucos dados e de forma rápida, a situação do uso de medicamentos "
          "num país, numa região ou numa unidade sanitária {oms1993}. A recolha "
          "pode ser prospectiva ou retrospectiva, a partir de receitas ou de "
          "registos clínicos, e a metodologia recomenda um mínimo de 600 "
          "consultas por inquérito {oms1993,manirakiza2025}. Quando o número de "
          "unidades é pequeno e se pretende comparar unidades entre si, os "
          "estudos recolhem cerca de 90 a 100 consultas por unidade, como "
          "sucedeu no Quénia e no Paquistão {nyabuti2020,atif2016}."),
        P("Os valores de referência usados na literatura para os cinco "
          "indicadores são de 1,6 a 1,8 medicamentos por consulta, de 20,0% a "
          "26,8% de consultas com antibiótico, de 13,4% a 24,1% de consultas "
          "com injectável e de 100% de medicamentos prescritos pela DCI e "
          "constantes da lista de medicamentos essenciais {nyabuti2020,"
          "atif2016}. Estes valores devem ser lidos como marcos de comparação "
          "e não como normas clínicas: uma unidade que atende muitas "
          "infecções bacterianas pode justificadamente exceder o intervalo de "
          "antibióticos, e uma unidade dentro do intervalo pode ainda assim "
          "prescrever o antibiótico errado."),
        P("Esta limitação está documentada. Num estudo com 1.243 receitas na "
          "Namíbia, a maioria dos indicadores da OMS teve baixa sensibilidade "
          "ou especificidade e todos tiveram fraca exactidão para prever o "
          "cumprimento das normas terapêuticas nacionais, sendo o indicador de "
          "antibióticos o único associado de forma independente a esse "
          "cumprimento {niaz2019}. Na Cidade do Cabo, 68,7% das consultas "
          "revistas incluíam antibiótico e apenas 45,1% das prescrições "
          "cumpriam as normas; entre as razões de incumprimento estavam o "
          "diagnóstico não documentado, em 30,5%, e o antibiótico "
          "desnecessário, em 21,6% {gasson2018}. Uma revisão identificou 773 "
          "indicadores de qualidade do uso de antibióticos, dos quais apenas "
          "1% citava directamente a classificação AWaRe, embora 57,6% "
          "reflectissem as orientações do manual AWaRe {funiciello2024}; na "
          "África do Sul, 12 de 13 indicadores AWaRe para infecções "
          "respiratórias mostraram aplicabilidade e mensurabilidade "
          "aceitáveis nos cuidados primários {chigome2026}. Por estas razões, "
          "o estudo complementa os cinco indicadores com a classificação AWaRe "
          "e com a avaliação da antibioterapia face ao diagnóstico."),
    ]),
    ("Magnitude da prescrição irracional no mundo, em África e em "
     "Moçambique", [
        P("A prescrição de antibióticos nos cuidados primários é elevada em "
          "todas as regiões de rendimento baixo e médio. A meta-análise de "
          "Sulis e colaboradores estimou uma prevalência agregada de 52%, com "
          "intervalo de confiança (IC) a 95% de 51% a 53%, e verificou que, nos 15 países com dados "
          "detalhados, o grupo Acesso representava mais de 60% dos "
          "antibióticos prescritos em 12 {sulis2020}."),
        P("Na Região Africana, a síntese de 43 estudos mostrou valores "
          "medianos de 3,1 medicamentos por consulta, 46,8% de consultas com "
          "antibiótico, 25,0% com injectável, 68,0% de prescrição pelo nome "
          "genérico e 88,0% de conformidade com a lista de medicamentos "
          "essenciais, com piores resultados no sector privado "
          "{oforiasenso2016}. Na Etiópia, "
          "uma meta-análise de 26 estudos com mais de 34.000 consultas "
          "encontrou em média dois medicamentos por consulta, 91% dos "
          "medicamentos prescritos pela DCI, 96% constantes da lista, 19% de "
          "consultas com injectável e 58% de consultas com antibiótico nos "
          "estudos de maior dimensão {teni2020}; outra revisão, com 30 "
          "estudos, estimou 2,11 medicamentos por consulta, 57,16% de "
          "consultas com antibiótico e 22,39% com injectável "
          "{mohammed2021}."),
        P("Em Moçambique, os dados publicados provêm de contextos parciais. "
          "Em unidades de cuidados primários do sul, 65,9% das receitas de "
          "doentes com HIV incluíam antibióticos, 30,2% dos quais com fins "
          "profilácticos {faiela2022}. No Hospital Distrital de Manhiça, 88% "
          "das receitas de ambulatório tinham antibiótico, com predomínio do "
          "cotrimoxazol e da amoxicilina e com variação sazonal "
          "{faiela2025}. No Hospital Central de Nampula, 74,8% dos antibióticos "
          "prescritos a crianças internadas pertenciam ao grupo Acesso e "
          "23,7% ao grupo Vigilância, e todos eram prescritos pela DCI e "
          "constavam da lista de medicamentos essenciais {xavier2024}. No "
          "ensaio de desimplementação conduzido em seis unidades de cuidados "
          "primários do sul do país com adultos com HIV, o grupo de controlo "
          "manteve uma taxa de prescrição de antibióticos de 56,3% nas "
          "infecções respiratórias altas {faiela2026}. Nenhum destes "
          "estudos descreve os cinco indicadores nos centros de saúde de uma "
          "cidade do norte do país."),
    ]),
    ("Determinantes da prescrição de antibióticos e de injectáveis", [
        P("As características do doente pesam na decisão de prescrever. Na "
          "Etiópia, ter menos de 18 anos associou-se fortemente à prescrição de "
          "antibiótico, com um odds ratio ajustado (ORa) de 9,83 "
          "{hailesilase2024}. No Uganda, "
          "o sexo feminino associou-se a maior prescrição de antibacterianos "
          "nas infecções respiratórias, com ORa de 1,51 {muwanguzi2021}."),
        P("O diagnóstico e a incerteza diagnóstica são os determinantes mais "
          "consistentes. As doenças do aparelho respiratório associaram-se à "
          "prescrição de antibióticos com ORa de 3,75 na Etiópia "
          "{hailesilase2024}, e a diarreia com ORa de 2,6 na Tanzânia "
          "{kilipamwambu2021}. A introdução dos TDR da malária reduziu os "
          "antimaláricos desnecessários, mas deslocou a prescrição para os "
          "antibióticos, que foram dados a 69% dos doentes com teste negativo "
          "{hopkins2017}; no Gana, a ausência de antimalárico na receita "
          "associou-se à prescrição de antibiótico, com um odds ratio (OR) de "
          "5,05 {ahiabu2016}. O número de "
          "medicamentos por receita associa-se também ao antibiótico, com OR "
          "de 1,85 no Gana {ahiabu2016} e ORa de 2,72 para três ou mais "
          "medicamentos no Uganda {muwanguzi2021}, e explica parte da "
          "variação entre estudos na Etiópia {teni2020}. Esta associação é "
          "em parte mecânica, porque o antibiótico entra na contagem; por "
          "isso, o estudo usa como variável explicativa o número de "
          "medicamentos não antibióticos."),
        P("Pesam ainda os factores do prescritor, da unidade e do sistema. A "
          "prescrição é pior no sector privado {oforiasenso2016} e variou "
          "com o tipo de unidade no Gana, com OR de 2,05 {ahiabu2016}. Em "
          "Manhiça, apesar do bom nível de conhecimento dos profissionais, "
          "foi frequente a prescrição de antibióticos de largo espectro "
          "{faiela2025}, e na "
          "África do Sul nenhum dos profissionais entrevistados conhecia a "
          "classificação AWaRe, citando as rupturas de stock, as expectativas "
          "dos doentes e o medo de complicações como razões para prescrever "
          "{chigome2026}. Nos cuidados primários moçambicanos prescrevem "
          "médicos, técnicos de medicina e enfermeiros {faiela2022}, e a LNME "
          "define cinco níveis de prescrição por categoria profissional, do "
          "agente polivalente elementar ao médico especialista {misau2017}; a "
          "categoria do prescritor é, por isso, uma variável obrigatória da "
          "análise."),
    ]),
    ("Consequências do uso irracional: resistência, danos e custos", [
        P("A relação entre o consumo de antibióticos e a resistência justifica "
          "a atenção dada a este indicador, num contexto de carga crescente de "
          "RAM {gbd2024,omsglass2025}. Na meta-análise africana já referida, a "
          "resistência às cefalosporinas de terceira geração chegou a 57,7% em "
          "*Klebsiella pneumoniae* {guido2025}, e a ceftriaxona, a que "
          "resistiam até 69,6% dos isolados de *Klebsiella* em crianças "
          "moçambicanas {massinga2021}, é um dos antibióticos mais usados em "
          "pediatria no Hospital Central de Nampula {xavier2024}."),
        P("Os danos não se limitam à resistência. Cada medicamento acrescentado "
          "aumenta a probabilidade de interacções, de reacções adversas e de "
          "erros de administração, e dificulta a adesão; cada injectável "
          "desnecessário expõe o doente a dor, a complicações locais e a riscos "
          "de transmissão de infecções quando as práticas de injecção são "
          "inseguras; e cada prescrição fora da lista ou por marca comercial "
          "encarece o tratamento ou deixa-o por dispensar. A síntese africana "
          "sublinhou que os desvios dos indicadores traduzem desperdício de "
          "recursos escassos e consequências negativas para a saúde "
          "{oforiasenso2016}."),
    ]),
    ("Enquadramento normativo e programático em Moçambique", [
        P("A Lei n.º 12/2017, que regula o medicamento, as vacinas e outros "
          "produtos biológicos para uso humano, criou a ANARME e estabelece, "
          "no artigo 33, que no SNS e nos serviços de saúde do sector público "
          "apenas devem ser usados os medicamentos constantes do FNM ou da "
          "lista de medicamentos essenciais, e, no artigo 34, que a prescrição "
          "pela DCI é obrigatória {lei12de2017}. A LNME de 2017 é de uso "
          "obrigatório no processo de procura, aquisição, distribuição e "
          "prescrição no SNS, organiza os medicamentos por nível de "
          "prescrição e determina que a CMAM se baseie na lista em vigor na "
          "selecção e na procura {misau2017}. Em Maio de 2025, o MISAU "
          "apresentou uma nova edição do FNM e uma lista nacional de testes e "
          "diagnósticos essenciais, com o propósito declarado de "
          "controlar a prescrição e promover o uso racional {mboane2025}."),
        P("O Plano Nacional de Acção Contra a Resistência Antimicrobiana "
          "2019-2023, elaborado pelo MISAU e pelo Ministério da Agricultura e "
          "Segurança Alimentar numa abordagem de saúde única, inclui entre os "
          "seus objectivos optimizar o uso de antimicrobianos, rever os "
          "factores que promovem o uso excessivo e criar, nas unidades "
          "sanitárias, equipas de manejo de antibióticos encarregadas de "
          "auditar a prescrição {misau2019}. O plano reconhece que as "
          "infecções adquiridas na comunidade são mais frequentes do que as "
          "hospitalares e que o prestador de cuidados primários é, por isso, "
          "decisivo para o uso racional {misau2019}. A investigação em saúde "
          "humana está regulada pela Lei n.º 3/2023, a cujo regime este "
          "protocolo se submete {lei3de2023}."),
        P("Fora dos serviços públicos, o circuito do antibiótico é pouco "
          "controlado: em Maputo, 87,3% dos antibióticos usados sem receita "
          "foram comprados em farmácias {mate2019}. Na falta de bases de "
          "dados de prescrição {wiseman2025}, as receitas arquivadas e os "
          "livros de registo de consultas dos centros de saúde são a fonte "
          "mais acessível para medir a prescrição nos cuidados primários."),
    ]),
    ("Intervenções para melhorar a prescrição nos cuidados primários", [
        P("Medir a prescrição é o primeiro passo das intervenções que a "
          "melhoram. Numa revisão de 33 estudos em 16 países de rendimento "
          "baixo e médio-baixo, as estratégias para aumentar a adesão às "
          "normas de antibioterapia foram quase sempre multifacetadas, "
          "tiveram efeitos na direcção desejada, e a auditoria com "
          "retroinformação, associada a formação, foi a componente mais usada "
          "{foxlee2021}. Em Moçambique, um ensaio aleatorizado por "
          "conglomerados em seis unidades de cuidados primários, dirigido a "
          "adultos com HIV, que combinou "
          "um algoritmo de decisão clínica, formação e supervisão dos "
          "clínicos e auditorias de receitas, reduziu a prescrição de "
          "antibióticos para infecções respiratórias altas para 23,1%, contra "
          "56,3% no grupo de controlo, com um risco relativo de 0,41 "
          "{faiela2026}."),
        P("O manual AWaRe da OMS oferece orientações para o tratamento "
          "empírico das infecções mais comuns nos cuidados primários e "
          "identifica as situações em que o antibiótico não é necessário "
          "{omsaware2022,moja2024}. Um "
          "retrato fiel da prescrição nos centros de saúde de Nampula é, "
          "portanto, a condição de partida para desenhar, dirigir e mais "
          "tarde avaliar intervenções deste tipo."),
    ]),
]

# ----------------------------------------------------- 7. estado da arte ----
ESTADO_ARTE = [
    P("O [[quadro:estado_arte]] sintetiza 15 estudos empíricos publicados "
      "entre 2016 e 2025 que aplicaram os indicadores de prescrição da OMS e "
      "da INRUD, ou descreveram a prescrição de antibióticos com a "
      "classificação AWaRe, em cuidados primários ou em ambulatório: três "
      "estudos moçambicanos, estudos da África Austral e Oriental "
      "com sistemas de saúde semelhantes e estudos de maior dimensão que "
      "servem de termo de comparação, como os do Botsuana, de Dessie, de "
      "Obio-Akpor e da Mauritânia {mashalla2017,wendie2021,ogaji2023,"
      "agahmed2024}."),
    QUADRO("estado_arte",
           "Síntese de estudos sobre o padrão de prescrição segundo os "
           "indicadores da OMS e a classificação AWaRe (estado da arte)",
           ["Autor (ano)", "Local", "Desenho (n)", "Principais resultados"],
           [
               ["Ahiabu et al. (2016) {ahiabu2016}", "Gana, Região Oriental",
                "Auditoria retrospectiva em 4 unidades (1.600 receitas)",
                "4,01 medicamentos por consulta; antibiótico 59,9%; "
                "injectável 24,2%; genérico 79,2%; lista essencial 88,1%; "
                "ausência de antimalárico associada ao antibiótico (OR 5,05)."],
               ["Atif et al. (2016) {atif2016}", "Paquistão, Bahawalpur",
                "Transversal em 10 centros (1.000 receitas)",
                "3,4 medicamentos; genérico 71,6%; antibiótico 48,9%; "
                "injectável 27,1%; lista essencial 93,4%."],
               ["Mashalla et al. (2017) {mashalla2017}",
                "Botsuana, 19 clínicas urbanas",
                "Transversal retrospectivo de registos de 2013",
                "2,8 medicamentos; antibiótico 42,7%; 78,6% dos antibióticos "
                "pela DCI e 96,1% conformes com a lista essencial; "
                "amoxicilina 28,4% dos antibióticos."],
               ["Gasson et al. (2018) {gasson2018}",
                "África do Sul, Cidade do Cabo",
                "Revisão retrospectiva em 8 unidades (654 processos)",
                "Antibiótico 68,7%; adesão às normas 45,1%; diagnóstico não "
                "documentado em 30,5% e antibiótico desnecessário em 21,6% "
                "das não conformidades."],
               ["Nyabuti et al. (2020) {nyabuti2020}", "Quénia, Kisii",
                "Transversal em 10 centros (900 receitas)",
                "2,9 medicamentos; genérico 27,7%; antibiótico 84,8%; "
                "injectável 24,9%; lista essencial 96,7%."],
               ["Wendie et al. (2021) {wendie2021}", "Etiópia, Dessie",
                "Transversal retrospectivo em centros de saúde (1.500 "
                "receitas)",
                "2,1 medicamentos; antibiótico 44%; injectável 13,9%; "
                "genérico 98%; lista essencial 100%."],
               ["Kilipamwambu et al. (2021) {kilipamwambu2021}",
                "Tanzânia, Ilala",
                "Retrospectivo em 4 unidades (604 receitas)",
                "1,99 medicamentos; 51,9% dos medicamentos eram antibióticos; "
                "84,4% dos antibióticos pela DCI; diarreia com ORa de 2,6."],
               ["Muwanguzi et al. (2021) {muwanguzi2021}",
                "Uganda, Mbarara",
                "Retrospectivo em 4 unidades (780 consultas por infecção "
                "respiratória)",
                "Antibacteriano 77,6%; 2,47 medicamentos; injectável 1,5%; "
                "genérico 79%; três ou mais medicamentos com ORa de 2,72."],
               ["Faiela e Sevene (2022) {faiela2022}",
                "Moçambique, 8 unidades de cuidados primários do sul",
                "Transversal prospectivo (369 receitas de doentes com HIV)",
                "Antibiótico 65,9%; 30,2% dos antibióticos em profilaxia; o "
                "diagnóstico foi a única variável associada."],
               ["Ogaji et al. (2023) {ogaji2023}", "Nigéria, Obio-Akpor",
                "Transversal em 10 centros (1.300 receitas)",
                "2,9 medicamentos; genérico 69,9%; lista essencial 75,6%; "
                "antibiótico 62,6%; injectável 22,3%."],
               ["Ag Ahmed et al. (2024) {agahmed2024}",
                "Mauritânia, 5 distritos",
                "Transversal prospectivo em 31 unidades (1.050 receitas)",
                "2,21 medicamentos; genérico 83,1%; lista essencial 54%; "
                "antibiótico 62,4%; injectável 15,6%."],
               ["Hailesilase et al. (2024) {hailesilase2024}",
                "Etiópia, Adigrat (ambulatório hospitalar)",
                "Transversal retrospectivo (600 receitas)",
                "1,8 medicamentos; antibiótico 44,5%; injectável 7,2%; "
                "Acesso 54,4% e Vigilância 45,6%; idade inferior a 18 anos "
                "com ORa de 9,83."],
               ["Xavier et al. (2024) {xavier2024}",
                "Moçambique, Nampula (pediatria de nível quaternário)",
                "Retrospectivo em processos clínicos (464 antibióticos)",
                "Antibiótico em 97,5% das crianças; 96,2% por injecção; "
                "Acesso 74,8% e Vigilância 23,7%; todos pela DCI e na lista "
                "essencial."],
               ["Faiela et al. (2025) {faiela2025}",
                "Moçambique, Hospital Distrital de Manhiça",
                "Transversal (200 receitas de ambulatório)",
                "Antibiótico em 88%; cotrimoxazol 30,77% e amoxicilina "
                "26,15% dos antibióticos; variação sazonal."],
               ["Manirakiza et al. (2025) {manirakiza2025}",
                "Burundi, Bujumbura",
                "Transversal retrospectivo em 20 centros (800 receitas "
                "pediátricas)",
                "Antimicrobiano 62,1%; genérico 95,0%; lista essencial "
                "95,8%; Acesso 71,3% e Vigilância 25,3%; 26,2% sem indicação "
                "documentada."],
           ],
           larguras=[3.3, 2.8, 3.6, 6.3],
           fonte="Elaboração própria (2026), a partir das fontes citadas."),
    P("A leitura do quadro revela um padrão consistente. O número médio de "
      "medicamentos por consulta variou entre 1,8 e 4,01, quase sempre acima "
      "do limite superior de referência de 1,8; a percentagem de consultas "
      "com antibiótico nas amostras gerais de cuidados primários situou-se "
      "entre 42,7% e 84,8%, muito acima do intervalo de 20,0% a 26,8%; e a "
      "prescrição pela DCI oscilou entre 27,7% e 100%, e a conformidade com a "
      "lista essencial entre 54% e 100%. A percentagem de consultas com "
      "injectável foi o indicador mais heterogéneo, de 1,5% a 27,1%, o que "
      "sugere forte dependência das práticas locais. Nos estudos que usaram a "
      "classificação AWaRe, o grupo Acesso predominou, mas o grupo Vigilância "
      "representou entre 23,7% e 45,6% dos antibióticos. Os factores "
      "associados à prescrição de antibióticos repetem-se de estudo para "
      "estudo: idade jovem, diagnóstico respiratório ou diarreico, maior "
      "número de medicamentos e ausência de antimalárico na receita."),
    P("As divergências e as lacunas são igualmente claras. Os estudos "
      "moçambicanos avaliaram doentes com HIV no sul {faiela2022}, um "
      "hospital distrital {faiela2025} e o internamento pediátrico em "
      "Nampula {xavier2024}; nenhum aplicou o conjunto dos indicadores às "
      "consultas curativas gerais dos centros de saúde de uma cidade do "
      "norte. Poucos estudos avaliaram a adequação da antibioterapia ao "
      "diagnóstico {gasson2018}, e os resumos consultados não referem modelos "
      "que tenham em conta o agrupamento das consultas por unidade "
      "sanitária, nem descrevem procedimentos de controlo de qualidade da "
      "extracção. O presente estudo preenche estas lacunas ao medir os cinco "
      "indicadores em todos os centros de saúde elegíveis da cidade de "
      "Nampula, ao acrescentar a classificação AWaRe e a avaliação da "
      "adequação por dois avaliadores independentes, e ao usar modelos "
      "multinível e dupla extracção."),
]
ESQUEMA_TEXTO = [
    P("A [[figura:esquema]] representa o modelo conceptual que orienta a "
      "selecção das variáveis e a análise. O padrão de prescrição, medido "
      "pelos indicadores da OMS, pela classificação AWaRe e pela adequação da "
      "antibioterapia, resulta da interacção entre características do doente "
      "(idade e sexo), do prescritor (categoria profissional e nível de "
      "prescrição autorizado), da consulta (diagnóstico registado, "
      "prescrição de antimalárico, número de outros medicamentos e estação "
      "do ano) e da unidade sanitária, tratada como nível superior do modelo "
      "multinível. Factores que o estudo não pode medir nos registos, como a "
      "disponibilidade de medicamentos em stock, o resultado do TDR quando "
      "não registado, as expectativas do doente e a formação do prescritor, "
      "são assumidos como fontes de confundimento residual e discutidos na "
      "interpretação {chigome2026,hopkins2017}."),
]
ESQUEMA_TITULO = ("Esquema conceptual dos factores associados ao padrão de "
                  "prescrição nos centros de saúde da cidade de Nampula")
ESQUEMA = {
    "contexto": ("Consultas externas curativas dos centros de saúde públicos "
                 "da cidade de Nampula, Janeiro a Dezembro de 2026"),
    "blocos": [
        ("Factores do doente", ["idade (grupo etário)", "sexo"]),
        ("Factores do prescritor", ["categoria profissional",
                                    "nível de prescrição autorizado na "
                                    "lista nacional"]),
        ("Factores da consulta", ["grupo diagnóstico registado",
                                  "prescrição de antimalárico",
                                  "número de medicamentos não antibióticos",
                                  "estação do ano (chuvosa ou seca)"]),
        ("Factores da unidade sanitária", ["centro de saúde (efeito "
                                           "aleatório)"]),
    ],
    "desfecho": ("Padrão de prescrição", [
        "medicamentos por consulta",
        "consulta com antibiótico",
        "consulta com injectável",
        "prescrição pela denominação comum internacional",
        "medicamento da lista nacional",
        "grupo Acesso, Vigilância ou Reserva",
        "adequação da antibioterapia"]),
    "moderadores": ("Confundimento residual não medido", [
        "stock de medicamentos",
        "resultado do teste rápido não registado",
        "expectativas do doente",
        "formação do prescritor"]),
}

# ----------------------------------------------------- 8. metodologia -------
METODOLOGIA = [
    ("Tipo e desenho do estudo", [
        P("Trata-se de um estudo observacional, transversal e retrospectivo, "
          "de base documental e abordagem quantitativa, com uma componente "
          "descritiva, que responde aos objectivos específicos 1 a 4, e uma "
          "componente analítica, que responde à comparação entre centros do "
          "objectivo específico 2 e aos factores associados do objectivo "
          "específico 5. O desenho transversal retrospectivo é o previsto na "
          "metodologia da OMS para medir os indicadores de prescrição a partir "
          "de registos já existentes {oms1993} e tem duas vantagens neste "
          "contexto: não interfere com a prática dos prescritores, porque as "
          "consultas de 2026 já ocorreram, e permite cobrir um ano completo "
          "com um custo reduzido."),
        P("O relato seguirá a declaração Strengthening the Reporting of "
          "Observational Studies in Epidemiology (STROBE) e a sua extensão "
          "para estudos com dados de saúde recolhidos por rotina aplicada à "
          "farmacoepidemiologia (RECORD-PE), que exige a descrição da origem e "
          "da qualidade dos registos, das definições de exposição e de "
          "desfecho e dos algoritmos de classificação dos medicamentos "
          "{langan2018}."),
    ]),
    ("Local e período do estudo", [
        P("O estudo será realizado na cidade de Nampula, capital da província, "
          "cujo distrito tinha 798.462 residentes no censo de 2017 do "
          "Instituto Nacional de Estatística (INE) {ine2021}. O SNS organiza-se "
          "em quatro níveis de cuidados, cabendo aos centros de saúde o nível "
          "primário {misau2017}. Os centros de saúde públicos da cidade são "
          "geridos pelo SDSMAS da Cidade de Nampula e realizam consultas "
          "externas curativas de adultos e de crianças, cujos medicamentos são "
          "dispensados pela farmácia do próprio centro. O número de centros "
          "elegíveis e o seu volume de consultas em 2026 serão obtidos junto do "
          "SDSMAS antes da amostragem [confirmar junto do SDSMAS da Cidade de "
          "Nampula o número de centros de saúde com consulta externa curativa "
          "e farmácia]. Nos relatórios públicos, os centros serão identificados "
          "por códigos."),
        P("O período de referência dos dados é o ano civil de 2026, que inclui "
          "a estação chuvosa, de Novembro a Abril, e a estação seca, de Maio a "
          "Outubro, uma vez que a prescrição de antibióticos varia com a "
          "estação {faiela2025}, e que já reflecte a edição do FNM apresentada "
          "em 2025 {mboane2025}. O estudo decorre de Outubro de 2026 a Setembro "
          "de 2027, e a consulta dos arquivos realiza-se entre Fevereiro e Maio "
          "de 2027, depois da aprovação ética e das autorizações "
          "institucionais."),
    ]),
    ("População, unidade de análise e fontes documentais", [
        P("A população de estudo é constituída pelas consultas externas "
          "curativas de adultos e de crianças realizadas em 2026 nos centros "
          "elegíveis que resultaram em pelo menos um medicamento prescrito. A "
          "unidade de análise principal é a consulta, operacionalizada como a "
          "receita emitida a um doente, numa data, por um prescritor; para os "
          "indicadores de prescrição pela DCI e de conformidade com a LNME e "
          "para a classificação ATC e AWaRe, a unidade é o medicamento "
          "prescrito; para o objectivo específico 4, é a consulta com "
          "antibiótico e diagnóstico registado."),
        P("Como na metodologia da OMS, cada consulta é tratada como uma "
          "observação independente, mesmo que o doente tenha tido várias "
          "consultas no ano {oms1993}. Como não se registam nomes, as segundas "
          "vias do mesmo doente, na mesma data e no mesmo centro, serão "
          "identificadas pela coincidência da data, da idade, do sexo e dos "
          "medicamentos, mantendo-se apenas a primeira."),
        P("A fonte primária são as receitas arquivadas na farmácia de cada "
          "centro. O livro de registo de consultas externas é a fonte "
          "complementar para o diagnóstico, a idade, o sexo e a categoria do "
          "prescritor em falta na receita, por correspondência da data, da "
          "idade e do sexo. O local de arquivo e o período de conservação das "
          "receitas de 2026 serão verificados em cada centro [confirmar junto "
          "das direcções dos centros de saúde o arquivo das receitas de "
          "2026]."),
    ]),
    ("Amostra e cálculo do tamanho da amostra", [
        H3("Tamanho da amostra para a estimativa dos indicadores"),
        P("O tamanho da amostra foi calculado para estimar a percentagem de "
          "consultas com antibiótico, o indicador de maior variância esperada "
          "e de maior interesse para o combate à RAM. Na falta de uma "
          "estimativa local, usa-se a mediana da Região Africana da OMS, de "
          "46,8% {oforiasenso2016}, na fórmula para uma proporção "
          "{serdar2021}:"),
        FORMULA("n<sub>0</sub> = Z<sup>2</sup> × p × (1 - p) / d<sup>2</sup>"),
        P("em que n<sub>0</sub> é o número mínimo de consultas utilizáveis; Z "
          "é igual a 1,96, para um nível de confiança de 95%; p é a proporção "
          "esperada, igual a 0,468; e d é a margem de erro absoluta de 5 "
          "pontos percentuais, igual a 0,05. Substituindo:"),
        FORMULA("n<sub>0</sub> = 1,96<sup>2</sup> × 0,468 × 0,532 / "
                "0,05<sup>2</sup> = 382,6, arredondado para 383"),
        P("O número de consultas curativas de 2026 nos centros elegíveis (N) "
          "ainda não é conhecido, mas será da ordem das dezenas de milhares "
          "[confirmar junto do SDSMAS o volume de consultas externas de 2026]. "
          "A [[tabela:cenarios_n]] mostra que a correcção para população "
          "finita, n<sub>c</sub> = n<sub>0</sub> / [1 + (n<sub>0</sub> - 1) / "
          "N], reduziria a amostra em menos de 4% mesmo com 10.000 consultas; "
          "por prudência, não será aplicada."),
        TABELA("cenarios_n",
               "Tamanho da amostra corrigido para população finita segundo "
               "diferentes cenários do número de consultas elegíveis",
               ["Consultas elegíveis em 2026 (N)", "n corrigido",
                "Redução face a n<sub>0</sub> = 383"],
               [["10.000", "369", "3,7%"],
                ["25.000", "378", "1,3%"],
                ["50.000", "381", "0,5%"],
                ["100.000", "382", "0,3%"]],
               larguras=[5.5, 4.5, 6.0],
               fonte="Elaboração própria (2026).",
               nota="Valores arredondados por excesso."),
        P("Quando todos os centros elegíveis são incluídos, funcionam como "
          "estratos e não como conglomerados, e a perda de precisão resulta "
          "sobretudo da ponderação desigual e do agrupamento das consultas por "
          "prescritor; quando os centros são amostrados, somam-se as "
          "semelhanças entre consultas do mesmo centro. Esta perda é expressa "
          "pelo efeito de desenho (DEFF), que depende do número de consultas "
          "por centro (m) e do coeficiente de correlação intraclasse (CCI): "
          "DEFF = 1 + (m - 1) × CCI. Adopta-se um DEFF de 2, que corresponde, "
          "com 96 consultas por centro, a um CCI de cerca de 0,01. "
          "Acrescenta-se uma margem de 15% para receitas ilegíveis, "
          "incompletas ou inelegíveis, coerente com a falta de documentação "
          "observada em estudos semelhantes {manirakiza2025}:"),
        FORMULA("n<sub>f</sub> = n<sub>0</sub> × DEFF / (1 - 0,15) = 383 × 2 "
                "/ 0,85 = 901,2, arredondado para 902"),
        P("A amostra é repartida em partes iguais pelos centros e pelos 12 "
          "meses, para representar a variação sazonal e permitir estimativas "
          "por centro; o número por centro é o menor múltiplo de 12 que, "
          "multiplicado pelo número de centros, atinge 902 "
          "([[tabela:cenarios_centros]]). No cenário de planeamento, de 10 "
          "centros elegíveis, sortear-se-ão 8 receitas por centro e por mês, "
          "96 por centro e 960 no total, acima do mínimo de 600 consultas "
          "recomendado pela OMS {oms1993}. Se existirem mais de 12 centros "
          "elegíveis, seleccionar-se-ão 12 por amostragem sistemática com "
          "probabilidade proporcional ao volume de consultas de 2026."),
        TABELA("cenarios_centros",
               "Repartição da amostra segundo o número de centros de saúde "
               "elegíveis",
               ["Centros (k)", "Mínimo por centro (902/k)",
                "Receitas por centro e por mês", "Receitas por centro",
                "Total de receitas", "Precisão por centro (IC 95%, p = 0,5)"],
               [["6", "151", "13", "156", "936", "±7,8 pontos"],
                ["8", "113", "10", "120", "960", "±8,9 pontos"],
                ["10", "91", "8", "96", "960", "±10,0 pontos"],
                ["12", "76", "7", "84", "1.008", "±10,7 pontos"]],
               larguras=[2.0, 2.8, 2.8, 2.6, 2.4, 3.4],
               fonte="Elaboração própria (2026).",
               nota="Precisão calculada sobre as receitas sorteadas, antes das "
                    "perdas. Com mais de 12 centros elegíveis, seleccionam-se "
                    "12 com probabilidade proporcional ao volume de "
                    "consultas."),
        H3("Poder para as componentes analíticas"),
        P("Para comparações entre dois grupos de consultas, como crianças com "
          "menos de 5 anos e doentes mais velhos, ou estação chuvosa e seca, "
          "calculou-se o número por grupo necessário para detectar uma "
          "diferença de 15 pontos percentuais na percentagem de consultas com "
          "antibiótico, de 45% para 60%, com significância de 5% e poder de 80% "
          "{serdar2021}:"),
        FORMULA("n = [Z<sub>1-α/2</sub> × √(2 × p<sub>m</sub> × (1 - "
                "p<sub>m</sub>)) + Z<sub>1-β</sub> × √(p<sub>1</sub> × (1 - "
                "p<sub>1</sub>) + p<sub>2</sub> × (1 - p<sub>2</sub>))]"
                "<sup>2</sup> / (p<sub>1</sub> - p<sub>2</sub>)<sup>2</sup>"),
        FORMULA("n = [1,96 × √(2 × 0,525 × 0,475) + 0,84 × √(0,45 × 0,55 + "
                "0,60 × 0,40)]<sup>2</sup> / 0,15<sup>2</sup> = 172,6, "
                "arredondado para 173 por grupo"),
        P("em que p<sub>1</sub> e p<sub>2</sub> são as proporções esperadas "
          "nos dois grupos e p<sub>m</sub> a sua média. Com o DEFF de 2, são "
          "necessárias 346 consultas por grupo em repartição igual, 692 no "
          "total, abaixo das cerca de 816 consultas utilizáveis previstas (85% "
          "de 960). Para uma diferença de 15 pontos percentuais, o poder é de "
          "cerca de 86% com grupos de igual dimensão e de cerca de 80% quando "
          "o grupo menor representa 30% da amostra; diferenças "
          "menores serão apresentadas com os IC e interpretadas com cautela."),
        P("Para a regressão logística, esperam-se cerca de 382 consultas com "
          "antibiótico (46,8% de 816) e 204 com injectável (25%) "
          "{oforiasenso2016}. Com pelo menos 10 eventos por parâmetro "
          "{peduzzi1996}, os modelos comportam até 38 e 20 parâmetros, "
          "respectivamente. Os modelos previstos têm 18: 3 para o grupo "
          "etário, 1 para o sexo, 3 para a categoria do prescritor, 6 para o "
          "grupo diagnóstico, 1 para o antimalárico, 3 para o número de "
          "medicamentos não antibióticos e 1 para a estação. Como o modelo dos "
          "injectáveis fica junto ao limite, os grupos diagnósticos serão "
          "agregados se as consultas com injectável ficarem abaixo de 200."),
        H3("Procedimento de amostragem"),
        P("Na primeira etapa, incluem-se todos os centros elegíveis até ao "
          "limite de 12, ou seleccionam-se 12 como descrito. Na segunda, em "
          "cada centro e mês, as receitas elegíveis arquivadas são ordenadas "
          "por data e contadas (N<sub>m</sub>); calcula-se o intervalo "
          "k<sub>m</sub> = N<sub>m</sub> / n<sub>m</sub>, em que n<sub>m</sub> "
          "é o número a seleccionar (8 no cenário de referência), sorteia-se um "
          "número inicial r entre 1 e k<sub>m</sub> e seleccionam-se as "
          "receitas de ordem r, r + k<sub>m</sub>, r + 2k<sub>m</sub> e "
          "seguintes. Uma receita que se revele inelegível ou ilegível é "
          "substituída pela elegível seguinte, com registo do motivo; num mês "
          "com menos receitas do que as previstas, incluem-se todas e "
          "documenta-se a falta (Apêndice B)."),
        P("Como a repartição igual não é proporcional ao volume de cada "
          "centro, as estimativas para a cidade usarão pesos amostrais iguais "
          "ao inverso da fracção de amostragem de cada centro e mês, "
          "N<sub>m</sub> / n<sub>m</sub>, e as estimativas não ponderadas "
          "serão apresentadas para comparação."),
    ]),
    ("Critérios de inclusão e de exclusão", [
        H3("Critérios de inclusão"),
        LISTA([
            "Receitas de consultas externas curativas de adultos e de "
            "crianças emitidas entre 1 de Janeiro e 31 de Dezembro de 2026 nos "
            "centros de saúde elegíveis;",
            "Receitas com pelo menos um medicamento prescrito;",
            "Receitas com data identificável, pelo menos quanto ao mês e ao "
            "ano.",
        ]),
        H3("Critérios de exclusão"),
        LISTA([
            "Receitas de programas com registo e esquemas próprios, como o "
            "tratamento anti-retroviral, a tuberculose, a consulta pré-natal e "
            "o planeamento familiar;",
            "Receitas de consultas de especialidade, de urgência de "
            "maternidade ou de internamento, quando existam no centro;",
            "Receitas em que pelo menos um medicamento não possa ser "
            "identificado por ilegibilidade, depois da leitura independente "
            "pelos dois extractores;",
            "Segundas vias e receitas duplicadas do mesmo doente, na mesma "
            "data e no mesmo centro;",
            "Receitas de doentes referidos de outra unidade sanitária que "
            "apenas transcrevam a prescrição dessa unidade.",
        ]),
    ]),
    ("Variáveis e definições operacionais", [
        P("O [[quadro:indicadores]] apresenta o cálculo dos cinco indicadores "
          "e dos indicadores complementares, com os valores de referência, "
          "segundo as definições operacionais da revisão da literatura "
          "{oms1993,whocc2026}. O indicador "
          "complementar de conformidade com o nível de prescrição compara a "
          "categoria do prescritor com o nível atribuído a cada medicamento "
          "na LNME {misau2017} e só será calculado se a categoria estiver "
          "registada em pelo menos 60% das receitas."),
        QUADRO("indicadores",
               "Indicadores de prescrição, forma de cálculo e valores de "
               "referência",
               ["Indicador", "Numerador / denominador",
                "Valor de referência", "Objectivo"],
               [["Número médio de medicamentos por consulta",
                 "Total de medicamentos distintos prescritos / número de "
                 "consultas", "1,6 a 1,8 {nyabuti2020,atif2016}", "2"],
                ["Percentagem de consultas com antibiótico",
                 "Consultas com pelo menos um antibiótico / número de "
                 "consultas × 100", "20,0% a 26,8% {nyabuti2020,atif2016}",
                 "2, 5"],
                ["Percentagem de consultas com injectável",
                 "Consultas com pelo menos um injectável / número de "
                 "consultas × 100", "13,4% a 24,1% {nyabuti2020,atif2016}",
                 "2, 5"],
                ["Percentagem de medicamentos prescritos pela DCI",
                 "Medicamentos prescritos pela DCI / total de medicamentos "
                 "× 100", "100% {nyabuti2020,lei12de2017}", "2"],
                ["Percentagem de medicamentos da LNME",
                 "Medicamentos constantes da LNME / total de medicamentos × "
                 "100", "100% {nyabuti2020,lei12de2017}", "2"],
                ["Percentagem de antibióticos do grupo Acesso "
                 "(complementar)",
                 "Antibióticos do grupo Acesso / total de antibióticos "
                 "prescritos × 100",
                 "Pelo menos 60% {gres2024}; pelo menos 70% "
                 "{omsunga2024}", "3"],
                ["Percentagem de consultas com antibiótico sem indicação "
                 "(complementar)",
                 "Consultas com antibiótico classificadas «em regra não "
                 "indicado» / consultas com antibiótico e diagnóstico "
                 "registado × 100", "Sem valor de referência; quanto menor, "
                 "melhor", "4"],
                ["Percentagem de medicamentos fora do nível de prescrição "
                 "(complementar)",
                 "Medicamentos de nível superior ao da categoria do "
                 "prescritor / medicamentos com categoria conhecida × 100",
                 "0% {misau2017}", "2"],
                ["Percentagem de receitas com diagnóstico registado "
                 "(complementar)",
                 "Receitas com diagnóstico na receita ou no livro / número "
                 "de consultas × 100", "100% desejável", "1"]],
               larguras=[4.0, 5.6, 4.4, 2.0],
               fonte="Elaboração própria (2026), a partir das fontes "
                     "citadas."),
        P("O [[quadro:variaveis]] apresenta as variáveis, a sua definição "
          "operacional e o objectivo específico a que respondem. No objectivo "
          "específico 5, as variáveis dependentes são a consulta com "
          "antibiótico e a consulta com injectável."),
        QUADRO("variaveis", "Variáveis do estudo e definições operacionais",
               ["Variável", "Tipo", "Definição operacional e categorias",
                "Objectivo"],
               [["Centro de saúde", "Independente, nominal",
                 "Código atribuído pela equipa (A, B, C...); nome não "
                 "divulgado", "1, 2, 5"],
                ["Mês e estação do ano", "Independente, nominal",
                 "Mês da consulta; estação chuvosa (Novembro a Abril) ou seca "
                 "(Maio a Outubro)", "1, 5"],
                ["Idade", "Independente, quantitativa e ordinal",
                 "Anos completos (meses se inferior a 1 ano); grupos: menos "
                 "de 5, 5 a 14, 15 a 49 e 50 ou mais anos", "1, 5"],
                ["Sexo", "Independente, nominal",
                 "Masculino; feminino; não registado", "1, 5"],
                ["Categoria do prescritor", "Independente, nominal",
                 "Médico; técnico de medicina; agente de medicina ou "
                 "enfermeiro; não identificável", "1, 2, 5"],
                ["Grupo diagnóstico", "Independente, nominal",
                 "Diagnóstico registado codificado pela Classificação "
                 "Internacional de Doenças, 10.ª revisão, e agregado em: "
                 "infecção respiratória alta; infecção respiratória baixa; "
                 "diarreia; malária; outras infecções; doença não infecciosa; "
                 "sintoma sem diagnóstico ou não registado", "1, 4, 5"],
                ["Prescrição de antimalárico", "Independente, dicotómica",
                 "Sim, se a receita inclui um antimalárico; não", "5"],
                ["Número de medicamentos por consulta",
                 "Quantitativa discreta",
                 "Contagem de medicamentos distintos (associação em dose fixa "
                 "conta como um)", "2"],
                ["Número de medicamentos não antibióticos",
                 "Independente, ordinal",
                 "0; 1; 2; 3 ou mais medicamentos que não sejam antibióticos",
                 "5"],
                ["Consulta com antibiótico", "Dependente, dicotómica",
                 "Sim, se inclui pelo menos um antibacteriano do grupo J01 "
                 "da ATC, metronidazol ou tinidazol oral; não", "2, 5"],
                ["Consulta com injectável", "Dependente, dicotómica",
                 "Sim, se inclui pelo menos um medicamento por via "
                 "intramuscular, intravenosa ou subcutânea, excluindo vacinas "
                 "e contraceptivos; não", "2, 5"],
                ["Prescrição pela DCI", "Dicotómica (por medicamento)",
                 "Sim, se designado pela DCI ou designação genérica aceite; "
                 "não, se por marca comercial", "2"],
                ["Medicamento da LNME", "Dicotómica (por medicamento)",
                 "Sim, se a substância e a forma constam da LNME em vigor; "
                 "não", "2"],
                ["Conformidade com o nível de prescrição",
                 "Dicotómica (por medicamento)",
                 "Sim, se o nível do medicamento na LNME é compatível com a "
                 "categoria do prescritor; não", "2"],
                ["Grupo terapêutico ATC", "Nominal (por medicamento)",
                 "Grupo anatómico principal (1.º nível) e substância (5.º "
                 "nível)", "3"],
                ["Grupo AWaRe", "Nominal (por antibiótico)",
                 "Acesso; Vigilância; Reserva; não classificado, segundo a "
                 "classificação da OMS de 2025", "3"],
                ["Adequação da antibioterapia ao diagnóstico",
                 "Dependente, nominal",
                 "Indicada; em regra não indicada; indeterminada (critérios "
                 "do quadro de adequação)", "4"],
                ["Diagnóstico registado", "Dicotómica",
                 "Sim, se existe diagnóstico legível na receita ou no livro de "
                 "registo; não", "1, 4"]],
               larguras=[3.4, 3.0, 7.6, 2.0],
               fonte="Elaboração própria (2026)."),
    ]),
    ("Instrumentos de recolha de dados e respectivas fontes", [
        P("Serão usados três instrumentos em papel, sem campos para "
          "identificadores pessoais. A ficha de extracção por consulta "
          "(Apêndice A), construída a partir das definições do manual da OMS "
          "{oms1993} e das variáveis dos estudos africanos recentes "
          "{wendie2021,manirakiza2025}, regista a identificação codificada da "
          "consulta, os dados do doente e do prescritor, o diagnóstico e a sua "
          "fonte, e cada medicamento tal como foi escrito, com a forma "
          "farmacêutica, a via e a legibilidade. A lista de verificação prévia "
          "e o registo de amostragem (Apêndice B) documentam, por centro e por "
          "mês, as receitas arquivadas, o intervalo de amostragem, o número "
          "inicial sorteado e as substituições. O dicionário de classificação "
          "e a grelha de adequação (Apêndice C) são preenchidos no escritório, "
          "de forma independente, por dois avaliadores."),
        P("As fontes de referência para a classificação são a LNME em vigor "
          "{misau2017}, completada pelo FNM mais recente {mboane2025} "
          "[confirmar junto da ANARME a edição da lista e do formulário em "
          "vigor durante 2026]; o índice e as directrizes da classificação ATC "
          "{whocc2026}; a classificação AWaRe de 2025 {omsaware2025}; a "
          "Classificação Internacional de Doenças, 10.ª revisão (CID-10) "
          "{omscid2019}; e o manual AWaRe para a avaliação da adequação "
          "{omsaware2022}."),
        P("A validade de conteúdo da ficha será apreciada por três peritos, um "
          "farmacêutico docente da FCS, um clínico dos cuidados primários e um "
          "docente de epidemiologia, que classificarão a relevância e a "
          "clareza de cada campo numa escala de quatro pontos; os campos com "
          "índice de validade de conteúdo inferior a 0,80 serão revistos. O "
          "pré-teste será feito em Fevereiro de 2027 em 96 receitas de "
          "Dezembro de 2025 de dois centros, cerca de 10% da amostra, fora do "
          "período de referência e, por isso, da amostra final, para testar a "
          "legibilidade das fontes, a correspondência com o livro de registo, "
          "o tempo de preenchimento e a clareza das instruções."),
    ]),
    ("Procedimentos de recolha de dados e controlo de qualidade", [
        P("Depois da aprovação do Comité Institucional de Bioética para a "
          "Saúde da Universidade Lúrio (CIBS-UniLúrio) e das autorizações da "
          "DPS, do SDSMAS e das direcções dos centros, a equipa apresentará o "
          "estudo a cada direcção e ao responsável da farmácia e obterá o "
          "volume mensal de consultas de 2026. Em Fevereiro de 2027, em cada "
          "centro, será feita a verificação prévia de 30 receitas de 2026 "
          "escolhidas ao acaso (Apêndice B), com as seguintes regras de "
          "decisão, fixadas antes da recolha:"),
        LISTA([
            "Se o centro não conservar receitas de pelo menos 9 meses de "
            "2026, usa-se o livro de registo como fonte primária, desde que "
            "registe os medicamentos; caso contrário, o centro é substituído, "
            "se tiver havido selecção, ou documentado como perda;",
            "Se uma variável estiver preenchida em menos de 60% das receitas "
            "verificadas no conjunto dos centros, sai da análise principal; "
            "se tal suceder com o diagnóstico, o objectivo específico 4 passa "
            "a análise exploratória restrita às receitas com diagnóstico, e a "
            "alteração é relatada;",
            "Se mais de 15% das receitas de um centro forem ilegíveis, o "
            "número de receitas sorteadas nesse centro aumenta na mesma "
            "proporção.",
        ]),
        P("A recolha será feita pelo estudante e por um extractor assistente, "
          "finalista do curso de Farmácia, formados num dia com o manual de "
          "instruções e calibrados em 20 receitas de 2025 até atingirem um "
          "kappa de Cohen de pelo menos 0,80 nas variáveis-chave. A extracção "
          "decorre em espaço indicado pela direcção, sem retirar, fotocopiar "
          "ou fotografar documentos, e sem transcrever nomes, números de "
          "processo, endereços ou contactos de doentes, nem nomes de "
          "prescritores."),
        P("O controlo de qualidade assenta em quatro procedimentos. Primeiro, "
          "10% das receitas amostradas (96 no cenário de referência), "
          "sorteadas entre todos os centros, serão extraídas de forma "
          "independente pelo segundo extractor; a concordância será medida "
          "pelo kappa de Cohen para a presença de antibiótico, de injectável, "
          "de prescrição pela DCI e de medicamento da LNME, e pela "
          "percentagem de concordância para o número de medicamentos, e um "
          "kappa inferior a 0,60 numa variável implica nova formação e nova "
          "extracção do lote do centro em causa {mchugh2012}. Segundo, o "
          "estudante revê diariamente a completude e a coerência das fichas. "
          "Terceiro, o orientador supervisiona semanalmente uma amostra de "
          "fichas. Quarto, os dados serão introduzidos em dupla digitação "
          "independente no programa EpiData, de acesso livre, com regras de "
          "validação e comparação automática das duas entradas, e as "
          "discrepâncias serão resolvidas pela consulta da ficha em papel."),
    ]),
    ("Classificação dos medicamentos e avaliação da adequação da "
     "antibioterapia", [
        P("A classificação dos medicamentos será feita por dicionário: todas "
          "as designações distintas encontradas nas receitas serão listadas "
          "e cada uma será classificada, de forma independente, por dois "
          "avaliadores com formação em farmácia, quanto à prescrição pela DCI, "
          "à presença na LNME, ao nível de prescrição, ao código ATC, à "
          "condição de antibiótico e ao grupo AWaRe {misau2017,whocc2026,"
          "omsaware2025}, com concordância medida pelo kappa de Cohen e "
          "desacordos resolvidos por consenso ou, na falta deste, pelo "
          "orientador, como terceiro avaliador. O dicionário final é aplicado "
          "por código a todas as receitas, para que a mesma designação receba "
          "sempre a mesma classificação."),
        P("A adequação da antibioterapia é o componente que mais depende de "
          "julgamento. Cada consulta com antibiótico e diagnóstico registado "
          "será classificada pelos dois avaliadores, de forma independente, "
          "segundo os critérios do [[quadro:criterios_adequacao]], "
          "construídos a partir do manual AWaRe da OMS e das recomendações de "
          "primeira escolha que o acompanham {omsaware2022,moja2024}. Para "
          "reduzir o viés, os avaliadores verão o diagnóstico, o grupo etário, "
          "o sexo e os antibióticos prescritos, mas não o centro nem a "
          "categoria do prescritor. A meta de concordância é um kappa de pelo menos 0,80, "
          "com a mesma regra de resolução dos desacordos {mchugh2012}."),
        QUADRO("criterios_adequacao",
               "Critérios para a classificação da antibioterapia segundo o "
               "diagnóstico registado",
               ["Grupo diagnóstico registado", "Classificação",
                "Fundamentação"],
               [["Pneumonia; infecção urinária; disenteria ou diarreia com "
                 "sangue; infecção bacteriana de pele e tecidos moles; "
                 "otite média aguda; infecção sexualmente transmissível de "
                 "abordagem sindrómica", "Indicada",
                 "Infecções com indicação de antibiótico empírico no manual "
                 "AWaRe"],
                ["Constipação, gripe ou infecção respiratória alta não "
                 "especificada; bronquite aguda; diarreia aquosa aguda sem "
                 "sangue", "Em regra não indicada",
                 "Etiologia predominantemente viral ou autolimitada; o manual "
                 "AWaRe recomenda não prescrever antibiótico"],
                ["Malária registada como único diagnóstico, sem diagnóstico "
                 "de infecção bacteriana", "Em regra não indicada",
                 "O antibiótico não trata a malária e não tem indicação sem "
                 "outro diagnóstico"],
                ["Doença não infecciosa isolada (por exemplo, hipertensão, "
                 "dor osteomuscular, gastrite)", "Em regra não indicada",
                 "Ausência de infecção documentada"],
                ["Faringite ou amigdalite; sinusite; febre ou outro sintoma "
                 "sem diagnóstico; diagnóstico ilegível", "Indeterminada",
                 "Indicação dependente de critérios clínicos que não constam "
                 "dos registos"]],
               larguras=[6.4, 3.0, 6.6],
               fonte="Elaboração própria (2026), a partir do manual AWaRe da "
                     "OMS {omsaware2022}.",
               nota="Os antibióticos prescritos como profilaxia registada "
                    "(por exemplo, cotrimoxazol em doentes com HIV) são "
                    "classificados à parte e excluídos do denominador."),
    ]),
    ("Processamento e análise dos dados", [
        P("Os dados serão analisados no Statistical Package for the Social "
          "Sciences (SPSS), versão 26 ou superior, ou no programa R, de acesso "
          "livre, com um nível de significância de 5% e IC a 95%. As variáveis "
          "qualitativas serão descritas por frequências absolutas e relativas "
          "e as quantitativas por média e desvio-padrão ou, se assimétricas, "
          "por mediana e intervalo interquartil. Para o objectivo específico "
          "1, as características das consultas serão descritas no conjunto e "
          "por centro, incluindo a percentagem de receitas com diagnóstico e "
          "com categoria do prescritor registados, que informa a qualidade das "
          "fontes."),
        P("Para o objectivo específico 2, os cinco indicadores serão "
          "calculados segundo as fórmulas do [[quadro:indicadores]], para a "
          "cidade, com os pesos amostrais e IC a 95% que considerem a "
          "estratificação por centro e mês e o agrupamento das consultas, e "
          "por centro, com IC de Wilson para as proporções. Considera-se que "
          "um indicador se afasta da referência quando o seu IC a 95% fica "
          "inteiramente fora do intervalo de referência. A comparação entre "
          "centros usará o teste do qui-quadrado, ou o teste exacto de Fisher "
          "quando mais de 20% das frequências esperadas forem inferiores a 5, "
          "e o teste de Kruskal-Wallis para o número de medicamentos por "
          "consulta, uma contagem de distribuição assimétrica."),
        P("Para o objectivo específico 3, serão apresentadas as frequências "
          "dos medicamentos por grupo anatómico principal da ATC e das 20 "
          "substâncias mais prescritas, e as dos antibióticos por substância e "
          "por grupo AWaRe; a percentagem do grupo Acesso será estimada com IC "
          "a 95% e comparada com as metas de 60% e de 70% "
          "{gres2024,omsunga2024}. Para o objectivo específico 4, estimar-se-á "
          "a proporção de consultas com antibiótico «em regra não indicado», "
          "com IC a 95%, no conjunto e por grupo diagnóstico, e uma análise de "
          "sensibilidade dará os seus limites, considerando as consultas "
          "indeterminadas primeiro como indicadas e depois como não "
          "indicadas."),
        P("Para o objectivo específico 5, a associação entre cada variável "
          "independente e a prescrição de antibiótico, e depois de "
          "injectável, será avaliada pelo teste do qui-quadrado. As variáveis "
          "com p inferior a 0,20 na análise bivariada, a que se juntam a idade "
          "e o sexo por razões conceptuais, entrarão num modelo de regressão "
          "logística multinível com interceptos aleatórios por centro. Serão "
          "apresentados os ORa com IC a 95%, o coeficiente de partição da "
          "variância e a mediana do odds ratio (MOR), que traduz a "
          "heterogeneidade entre centros numa escala de fácil interpretação "
          "{austin2017}. Como a variância entre centros é estimada com "
          "imprecisão quando há menos de 15 centros, o modelo será repetido "
          "com o centro como efeito fixo, para confirmar a estabilidade dos "
          "ORa. A colinearidade será verificada pelo factor de inflação da "
          "variância, com o limite de 5. Como análise de sensibilidade, os "
          "modelos serão repetidos sem as consultas com profilaxia registada e "
          "sem as consultas sem diagnóstico."),
        P("Os dados em falta serão descritos por variável; quando uma "
          "covariável tiver mais de 10% de valores em falta, será criada a "
          "categoria «não registado», e nos restantes casos a análise usará as "
          "observações completas. Os resultados serão apresentados em tabelas "
          "e gráficos."),
    ]),
    ("Limitações do estudo e estratégias de mitigação", [
        P("O [[quadro:limitacoes]] identifica as principais limitações "
          "previstas, a sua consequência provável para os resultados e a "
          "estratégia adoptada para as reduzir. A mais importante decorre da "
          "natureza documental do estudo: os registos foram produzidos para "
          "fins assistenciais e não para investigação, pelo que a sua "
          "completude e legibilidade condicionam a validade das "
          "estimativas."),
        QUADRO("limitacoes",
               "Limitações previstas e estratégias de mitigação",
               ["Limitação", "Consequência", "Mitigação"],
               [["Receitas ilegíveis, incompletas ou não arquivadas",
                 "Perda de informação e possível viés de selecção, se as "
                 "receitas perdidas forem diferentes das conservadas",
                 "Verificação prévia com regras de decisão; margem de 15%; "
                 "substituição documentada; uso do livro de registo; "
                 "descrição das perdas por centro e mês"],
                ["A amostra inclui apenas consultas com pelo menos um "
                 "medicamento prescrito",
                 "Sobrestimação do número médio de medicamentos e das "
                 "percentagens face ao total das consultas",
                 "Declaração explícita da unidade de análise; comparação com "
                 "estudos que usaram receitas"],
                ["Diagnóstico registado pode não reflectir o quadro clínico",
                 "Erro na classificação da adequação da antibioterapia",
                 "Dois avaliadores independentes com kappa; categoria "
                 "indeterminada; análise de sensibilidade com limites"],
                ["Falta do resultado do TDR e de dados clínicos nos registos",
                 "Impossibilidade de avaliar a decisão clínica completa",
                 "Uso do antimalárico prescrito como indicador indirecto; "
                 "interpretação prudente"],
                ["Classificações dependentes de julgamento (DCI, LNME, "
                 "AWaRe, nível de prescrição)",
                 "Erro de classificação não diferencial",
                 "Dicionário único, dupla classificação independente, kappa "
                 "e terceiro avaliador"],
                ["Agrupamento das consultas superior ao previsto",
                 "Perda de precisão das estimativas da cidade",
                 "IC que consideram o desenho; modelos multinível; relato do "
                 "CCI observado"],
                ["Poder limitado para diferenças pequenas e categorias raras",
                 "Resultados falsamente negativos",
                 "Declaração do poder; agregação de categorias; apresentação "
                 "dos IC"],
                ["Estudo limitado aos centros de saúde públicos urbanos",
                 "Resultados não generalizáveis a hospitais, ao sector "
                 "privado ou às zonas rurais",
                 "Delimitação explícita; comparação apenas com contextos "
                 "semelhantes"]],
               larguras=[5.0, 5.0, 6.0],
               fonte="Elaboração própria (2026)."),
    ]),
    ("Considerações éticas", [
        P("A investigação observará os princípios da Declaração de Helsínquia "
          "da Associação Médica Mundial, na revisão de 2024 {wma2025}, e o "
          "regime da Lei n.º 3/2023 sobre a investigação em saúde humana "
          "{lei3de2023}. O protocolo será submetido ao CIBS-UniLúrio e, se este "
          "o determinar, ao Comité Nacional de Bioética para a Saúde (CNBS). A consulta dos arquivos só começará depois do parecer "
          "favorável e das autorizações escritas da DPS de Nampula, do SDSMAS "
          "da Cidade de Nampula e da direcção de cada centro de saúde "
          "(Apêndice E). Serão adoptadas as seguintes salvaguardas:"),
        LISTA([
            "Dispensa de consentimento informado: o estudo usa apenas "
            "registos de consultas já realizadas, sem contacto com doentes, "
            "com risco mínimo e sem recolha de identificadores; seria "
            "impraticável contactar os doentes de 2026; a dispensa será "
            "pedida formalmente ao CIBS-UniLúrio (Apêndice D).",
            "Confidencialidade dos doentes: não serão registados nomes, "
            "números de processo, endereços nem contactos; cada consulta "
            "recebe um código; as fichas ficam em caixa fechada à chave e a "
            "base de dados em ficheiro cifrado, com acesso restrito à equipa, "
            "sendo destruídas cinco anos após a defesa.",
            "Confidencialidade dos prescritores e das unidades: não serão "
            "registados nomes de prescritores, apenas a categoria; os centros "
            "serão identificados por códigos nos relatórios públicos; a "
            "devolução por centro será feita apenas à respectiva direcção, com "
            "fins formativos e não punitivos.",
            "Compromisso da equipa: o estudante, o extractor assistente e os "
            "avaliadores assinarão um termo de confidencialidade (Apêndice F).",
            "Riscos e benefícios: o único risco previsível é a quebra de "
            "confidencialidade, prevenida pelas medidas anteriores; não há "
            "benefício directo para os doentes de 2026, mas o estudo beneficia "
            "os futuros utentes ao orientar a melhoria da prescrição.",
            "Via de comunicação de problemas de segurança: se a extracção "
            "detectar uma prescrição com potencial de dano grave, como uma "
            "associação contra-indicada ou uma dose manifestamente tóxica, o "
            "estudante informa o orientador em 48 horas, e este comunica o "
            "facto, de forma confidencial, à direcção do centro e, quando "
            "aplicável, ao sistema de farmacovigilância da ANARME.",
            "Independência e conflitos de interesse: o estudo é financiado "
            "pelo próprio estudante, a equipa declara não ter conflitos de "
            "interesse, e os resultados serão partilhados com as instituições "
            "antes de qualquer publicação.",
        ]),
    ]),
]

# ----------------------------------------------------- 9 e 10 ---------------
RESULTADOS_ESPERADOS = [
    P("Os resultados esperados correspondem, pela mesma ordem, aos objectivos "
      "específicos. A direcção indicada apoia-se na literatura revista e será "
      "confirmada ou rejeitada pelos dados, sem valores fixados à partida."),
    LISTA([
        "Perfil das consultas amostradas por idade, sexo, categoria do "
        "prescritor, centro, mês e grupo diagnóstico, com a proporção de "
        "receitas com diagnóstico registado. Espera-se que a febre, as "
        "infecções respiratórias, a diarreia e a malária dominem os "
        "diagnósticos {fink2020,kilipamwambu2021}; o resultado mede também a "
        "qualidade dos registos de prescrição de cada centro.",
        "Estimativa dos cinco indicadores, com IC a 95%, no conjunto e por "
        "centro. Espera-se, como na Região Africana, mais medicamentos por "
        "consulta e mais consultas com antibiótico do que os valores de "
        "referência, com prescrição pela DCI e conformidade com a LNME "
        "elevadas mas abaixo de 100% {oforiasenso2016,teni2020}. O SDSMAS "
        "ganha uma linha de base por centro para a supervisão.",
        "Perfil terapêutico por grupo ATC e distribuição AWaRe dos "
        "antibióticos. Espera-se predomínio da amoxicilina e do cotrimoxazol "
        "e uma proporção do grupo Acesso superior a 60%, mas com antibióticos "
        "do grupo Vigilância, como a ceftriaxona, acima do desejável "
        "{faiela2025,xavier2024,sulis2020}. O resultado orienta a "
        "quantificação de medicamentos e a formação dos prescritores.",
        "Proporção de consultas com antibiótico em regra não indicado, com os "
        "limites da análise de sensibilidade. Espera-se que se concentre nas "
        "infecções respiratórias altas, na diarreia aquosa e na malária sem "
        "outro diagnóstico {gasson2018,hopkins2017}, o que identifica os "
        "diagnósticos prioritários para normas e auditorias.",
        "Factores associados à prescrição de antibióticos e de injectáveis, "
        "com ORa e MOR. Espera-se associação com a idade inferior a 5 anos, o "
        "diagnóstico respiratório ou diarreico, a ausência de antimalárico e "
        "o número de outros medicamentos {hailesilase2024,ahiabu2016,"
        "kilipamwambu2021}, e uma variação entre centros que justifique "
        "intervenções dirigidas.",
    ]),
]
DIVULGACAO = [
    P("O relatório final será defendido publicamente perante um júri da FCS "
      "da UniLúrio. Um relatório-síntese, com os indicadores da cidade e as "
      "recomendações, será entregue à DPS de Nampula, ao SDSMAS da Cidade de "
      "Nampula, à CMAM e à ANARME; cada direcção de centro receberá em "
      "separado, de forma confidencial, os resultados do seu centro, numa "
      "sessão de restituição com os prescritores e o pessoal da farmácia, de "
      "carácter formativo e não punitivo. Os principais achados serão "
      "submetidos a uma revista com revisão por pares, relatados segundo a "
      "declaração RECORD-PE {langan2018}, e apresentados nas jornadas "
      "científicas da UniLúrio e em encontros nacionais de saúde. A ficha de "
      "extracção, o dicionário de classificação e o protocolo de amostragem "
      "ficarão disponíveis no Departamento de Farmácia para auditorias "
      "futuras."),
]

# ----------------------------------------------------- 11. cronograma -------
CRONOGRAMA_TEXTO = [
    P("O [[quadro:cronograma]] distribui as actividades pelos 12 meses do "
      "estudo, de Outubro de 2026 a Setembro de 2027. A consulta dos arquivos "
      "só começa em Fevereiro de 2027, depois do parecer do CIBS-UniLúrio e "
      "das autorizações institucionais; se a aprovação se atrasar, as fases "
      "seguintes deslocam-se sem encurtar a recolha."),
]
CRONOGRAMA = {
    "inicio": (2026, 10),
    "n_meses": 12,
    "titulo": ("Cronograma de actividades, de Outubro de 2026 a Setembro de "
               "2027"),
    "actividades": [
        ("Revisão da literatura e redacção do protocolo", [1, 2]),
        ("Submissão ao CIBS-UniLúrio e pedidos de autorização", [2, 3, 4]),
        ("Validação da ficha por peritos e manual de instruções", [3, 4]),
        ("Verificação prévia das fontes, pré-teste, formação e calibração",
         [5]),
        ("Recolha de dados e dupla extracção de 10% das receitas", [6, 7, 8]),
        ("Dupla digitação e limpeza da base de dados", [7, 8, 9]),
        ("Classificação dos medicamentos e avaliação da adequação", [8, 9]),
        ("Processamento e análise estatística", [9, 10]),
        ("Redacção do relatório final", [10, 11]),
        ("Revisão pelo orientador e entrega", [11]),
        ("Defesa pública e devolução dos resultados", [12]),
    ],
}

# ----------------------------------------------------- 12. orcamento --------
ORCAMENTO_TEXTO = [
    P("A [[tabela:orcamento]] apresenta o orçamento estimado, em meticais. O "
      "estudo será financiado pelo estudante, que pedirá à FCS apoio para a "
      "impressão e o transporte se essa modalidade existir; os imprevistos, "
      "de 10%, cobrem também uma eventual taxa de apreciação ética. As "
      "rubricas maiores são a compensação do extractor assistente e o "
      "transporte e a alimentação da equipa, calculados para cerca de 40 "
      "dias de trabalho nos centros (contagem e sorteio das receitas, "
      "verificação prévia, pré-teste e extracção); a impressão das fichas "
      "cobre as 960 receitas da amostra, as 96 do pré-teste e as 96 da dupla "
      "extracção. O R e o EpiData são de acesso livre."),
]
ORCAMENTO = [
    ("Impressão das fichas de extracção (frente e verso, com reserva)",
     "página", 2600, 5),
    ("Impressão do protocolo, dos pedidos, do manual e dos registos de "
     "amostragem", "página", 800, 5),
    ("Material de escritório (esferográficas, lápis, pastas, clipes)",
     "conjunto", 2, 750),
    ("Caixa de arquivo com fechadura para as fichas", "unidade", 1, 2500),
    ("Disco externo para cópia de segurança cifrada", "unidade", 1, 3500),
    ("Transporte da equipa aos centros de saúde", "pessoa-dia", 80, 150),
    ("Alimentação da equipa no terreno", "pessoa-dia", 80, 200),
    ("Compensação do extractor assistente", "dia", 40, 500),
    ("Compensação dos dois avaliadores (classificação e adequação)",
     "avaliador", 2, 3000),
    ("Lanche da sessão de formação e calibração", "sessão", 1, 1500),
    ("Comunicações (crédito de telemóvel e dados móveis)", "mês", 12, 500),
    ("Impressão e encadernação do relatório final", "exemplar", 5, 800),
    ("Relatórios-síntese para as instituições e os centros", "exemplar", 15,
     150),
    ("Impressão do póster para as jornadas científicas", "unidade", 1, 2500),
]
ORCAMENTO_IMPREVISTOS = 0.10

# ----------------------------------------------------- apendices ------------
_MESES_2026 = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
               "Julho", "Agosto", "Setembro", "Outubro", "Novembro",
               "Dezembro"]
_TITULO_ENTRE_ASPAS = "«" + TITULO + "»"

APENDICES = [
    ("Ficha de extracção de dados por consulta", [
        NOTA("Instruções: preencher uma ficha por receita seleccionada, a "
             "partir da receita arquivada na farmácia e, para os campos em "
             "falta, do livro de registo de consultas externas (correspondência "
             "pela data, idade e sexo). Não transcrever nomes, números de "
             "processo, endereços ou contactos de doentes, nem nomes de "
             "prescritores. Transcrever cada medicamento tal como está escrito. "
             "Os campos marcados (E) são preenchidos no escritório com o "
             "dicionário de classificação (Apêndice C). Usar 99 para «não "
             "registado» e 88 para «ilegível». Códigos da via: 1 oral; 2 "
             "intramuscular; 3 intravenosa; 4 subcutânea; 5 tópica; 6 outra. "
             "Códigos AWaRe: A, Acesso; V, Vigilância; R, Reserva; X, não "
             "classificado."),
        H3("Secção I. Identificação codificada"),
        CAMPO("Código da ficha: __________    Código do centro: ______    "
              "Mês da consulta: ______ de 2026"),
        CAMPO("Número de ordem da receita no mês: ______    Receita de "
              "substituição: (   ) Não   (   ) Sim, motivo: ______________"),
        PERG("Estação do ano (deduzida do mês):",
             ["Chuvosa (Novembro a Abril)", "Seca (Maio a Outubro)"]),
        H3("Secção II. Doente"),
        PERG("Idade:", ["______ anos completos",
                        "______ meses, se inferior a 1 ano",
                        "Não registada (99)"]),
        PERG("Sexo:", ["Masculino", "Feminino", "Não registado (99)"]),
        H3("Secção III. Prescritor"),
        PERG("Categoria profissional do prescritor:",
             ["Médico", "Técnico de medicina", "Agente de medicina ou "
              "enfermeiro", "Não identificável (99)"]),
        PERG("Fonte da categoria:", ["Receita", "Livro de registo",
                                     "Nenhuma"]),
        H3("Secção IV. Diagnóstico"),
        PERG("Diagnóstico ou diagnósticos, tal como escritos:"),
        PERG("Fonte do diagnóstico:",
             ["Receita", "Livro de registo", "Não registado (99)",
              "Ilegível (88)"]),
        CAMPO("Código CID-10 (E): ________    Grupo diagnóstico (E, códigos 1 "
              "a 7 do Apêndice C): ____"),
        PERG("Antibiótico registado como profilaxia (por exemplo, "
             "cotrimoxazol em doente com HIV):", ["Sim", "Não"]),
        H3("Secção V. Medicamentos prescritos (transcrição no terreno)"),
        TABELA(None, "",
               ["N.º", "Designação e dose tal como escritas",
                "Forma farmacêutica", "Via (código 1 a 6)",
                "Legível (S/N)"],
               [[str(i), "", "", "", ""] for i in range(1, 9)],
               larguras=[1.0, 7.0, 3.0, 3.0, 2.0]),
        H3("Secção VI. Classificação dos medicamentos (E)"),
        TABELA(None, "",
               ["N.º", "DCI (S/N)", "LNME (S/N)", "Nível LNME (0 a 4)",
                "Código ATC", "Antibiótico (S/N)", "AWaRe (A, V, R, X)"],
               [[str(i), "", "", "", "", "", ""] for i in range(1, 9)],
               larguras=[1.0, 2.2, 2.2, 2.4, 3.0, 2.6, 2.6]),
        H3("Secção VII. Resumo da consulta (E)"),
        CAMPO("Número de medicamentos distintos: ____    Número de "
              "medicamentos não antibióticos: ____"),
        PERG("Consulta com antibiótico:", ["Sim", "Não"]),
        PERG("Consulta com injectável (excluindo vacinas e contraceptivos):",
             ["Sim", "Não"]),
        PERG("Consulta com antimalárico:", ["Sim", "Não"]),
        H3("Secção VIII. Controlo de qualidade"),
        CAMPO("Extractor (código): ______    Data da extracção: ___/___/2027"
              "    Dupla extracção: (   ) Não   (   ) Sim"),
        CAMPO("Revisão diária (rubrica): ______    1.ª digitação: (   )    "
              "2.ª digitação: (   )"),
    ]),
    ("Lista de verificação prévia das fontes e registo de amostragem", [
        NOTA("A Parte 1 aplica-se em Fevereiro de 2027, em cada centro, a 30 "
             "receitas de 2026 escolhidas ao acaso entre os meses arquivados. "
             "A Parte 2 preenche-se por centro, uma linha por mês, antes da "
             "selecção das receitas."),
        H3("Parte 1. Lista de verificação prévia"),
        CAMPO("Código do centro: ______    Data: ___/___/2027    Verificador "
              "(código): ______"),
        PERG("As receitas de 2026 estão arquivadas na farmácia do centro?",
             ["Sim, todos os meses", "Sim, com meses em falta", "Não"]),
        CAMPO("Meses em falta: ______________________    Local de arquivo: "
              "______________________"),
        PERG("O livro de registo de consultas externas de 2026 regista os "
             "medicamentos prescritos?", ["Sim", "Parcialmente", "Não"]),
        TABELA(None, "",
               ["Campo verificado nas 30 receitas",
                "Receitas com o campo preenchido e legível (n)", "%",
                "Decisão (mantém-se se 60% ou mais)"],
               [["Data (mês e ano)", "", "", ""],
                ["Idade", "", "", ""],
                ["Sexo", "", "", ""],
                ["Diagnóstico (na receita ou no livro)", "", "", ""],
                ["Categoria do prescritor", "", "", ""],
                ["Via de administração identificável", "", "", ""],
                ["Todos os medicamentos legíveis", "", "", ""]],
               larguras=[6.0, 4.0, 1.6, 4.4]),
        NOTA("Regras de decisão: com menos de 9 meses de receitas conservadas, "
             "usa-se o livro de registo como fonte primária, se registar os "
             "medicamentos, ou exclui-se o centro; uma variável com menos de "
             "60% de preenchimento no conjunto dos centros sai da análise "
             "principal; com mais de 15% de receitas ilegíveis num centro, o "
             "número de receitas sorteadas nesse centro aumenta na mesma "
             "proporção."),
        H3("Parte 2. Registo de amostragem por mês"),
        CAMPO("Código do centro: ______    Receitas a seleccionar por mês "
              "(n<sub>m</sub>): ______"),
        TABELA(None, "",
               ["Mês de 2026", "Receitas elegíveis arquivadas (N<sub>m</sub>)",
                "Intervalo k<sub>m</sub> = N<sub>m</sub> / n<sub>m</sub>",
                "Número inicial sorteado (r)", "Números de ordem "
                "seleccionados", "Substituições e motivo"],
               [[m, "", "", "", "", ""] for m in _MESES_2026],
               larguras=[2.3, 2.6, 2.6, 2.2, 3.4, 2.9]),
        CAMPO("Responsável pela amostragem: ______________________    Data: "
              "___/___/2027"),
    ]),
    ("Dicionário de classificação dos medicamentos e grelha de avaliação da "
     "adequação da antibioterapia", [
        NOTA("Cada designação distinta encontrada nas receitas é classificada, "
             "de forma independente, por dois avaliadores, com base na LNME em "
             "vigor, no índice ATC e na classificação AWaRe de 2025; os "
             "desacordos resolvem-se por consenso ou pelo orientador. Cada "
             "consulta com antibiótico e diagnóstico registado é classificada "
             "sem conhecimento do centro nem da categoria do prescritor, "
             "segundo os critérios de adequação definidos na metodologia."),
        H3("Parte 1. Dicionário de classificação"),
        TABELA(None, "",
               ["Código", "Designação encontrada", "DCI (S/N)", "LNME (S/N)",
                "Nível (0 a 4)", "Código ATC", "Antibiótico (S/N)",
                "AWaRe (A, V, R, X)", "Acordo (S/N)"],
               [["", "", "", "", "", "", "", "", ""] for _ in range(6)],
               larguras=[1.4, 3.4, 1.4, 1.5, 1.5, 1.9, 1.8, 1.8, 1.3]),
        H3("Parte 2. Códigos dos grupos diagnósticos"),
        TABELA(None, "",
               ["Código", "Grupo diagnóstico",
                "Exemplos de diagnósticos registados"],
               [["1", "Infecção respiratória alta",
                 "Constipação, gripe, faringite, amigdalite, sinusite, otite"],
                ["2", "Infecção respiratória baixa",
                 "Pneumonia, bronquite, bronquiolite"],
                ["3", "Diarreia",
                 "Diarreia aguda aquosa, disenteria, gastroenterite"],
                ["4", "Malária", "Malária confirmada por teste ou clínica"],
                ["5", "Outras infecções",
                 "Infecção urinária, de pele e tecidos moles, infecção "
                 "sexualmente transmissível, parasitoses intestinais"],
                ["6", "Doença não infecciosa",
                 "Hipertensão, dor osteomuscular, gastrite, anemia"],
                ["7", "Sintoma sem diagnóstico ou não registado",
                 "Febre, cefaleia, dor abdominal, receita sem diagnóstico"]],
               larguras=[1.6, 5.0, 9.4]),
        H3("Parte 3. Grelha de avaliação da adequação"),
        TABELA(None, "",
               ["Código da ficha", "Grupo etário", "Sexo",
                "Diagnóstico registado", "Antibióticos prescritos",
                "Classificação (I, N, D, P)", "Avaliador (1 ou 2)"],
               [["", "", "", "", "", "", ""] for _ in range(6)],
               larguras=[1.9, 1.7, 1.2, 3.8, 3.2, 2.4, 1.8]),
        NOTA("I: indicada; N: em regra não indicada; D: indeterminada; P: "
             "profilaxia registada, excluída do denominador."),
    ]),
    ("Pedido de dispensa do consentimento informado", [
        P("Ao Presidente do Comité Institucional de Bioética para a Saúde da "
          "Universidade Lúrio"),
        P("Assunto: pedido de dispensa do consentimento informado no "
          "protocolo " + _TITULO_ENTRE_ASPAS + "."),
        P("[Nome do(a) estudante], estudante da Licenciatura em Farmácia da "
          "Faculdade de Ciências de Saúde da Universidade Lúrio, sob "
          "orientação de [Nome e grau académico do(a) orientador(a)], vem "
          "solicitar a dispensa do consentimento informado individual no "
          "estudo acima identificado, com os seguintes fundamentos:"),
        LISTA([
            "o estudo é retrospectivo e usa apenas receitas e livros de "
            "registo de consultas externas realizadas em 2026, sem contacto "
            "com doentes ou prescritores e sem intervenção nos cuidados;",
            "não serão recolhidos nomes, números de processo, endereços, "
            "contactos ou outros identificadores directos, nem nomes de "
            "prescritores; cada consulta recebe um código e os centros são "
            "identificados por códigos nos relatórios públicos;",
            "o risco é mínimo e limita-se a uma eventual quebra de "
            "confidencialidade, prevenida pelas medidas do protocolo e pelo "
            "termo de confidencialidade assinado pela equipa;",
            "o consentimento seria impraticável, porque os doentes atendidos "
            "em 2026 não são contactáveis a partir dos registos consultados, "
            "e tentar contactá-los exigiria recolher os identificadores que o "
            "estudo evita;",
            "os resultados serão devolvidos de forma agregada às instituições "
            "de saúde, em benefício dos futuros utentes.",
        ]),
        P("A consulta dos arquivos só começará depois do parecer favorável "
          "deste Comité e das autorizações da Direcção Provincial de Saúde de "
          "Nampula, do Serviço Distrital de Saúde, Mulher e Acção Social da "
          "Cidade de Nampula e da direcção de cada centro de saúde."),
        CAMPO("Nampula, ____ de ______________ de 20___"),
        CAMPO("O(A) estudante: ______________________________"),
        CAMPO("O(A) orientador(a): ______________________________"),
        CAMPO("Contacto do(a) estudante: [preencher]"),
    ]),
    ("Pedido de autorização institucional", [
        NOTA("Modelo único, dirigido separadamente à Direcção Provincial de "
             "Saúde de Nampula, ao Serviço Distrital de Saúde, Mulher e Acção "
             "Social da Cidade de Nampula e à direcção de cada centro de "
             "saúde, acompanhado do protocolo e do parecer do comité de "
             "bioética."),
        P("Ao(À) Exmo.(a) Senhor(a) Director(a) de "
          "______________________________"),
        P("Assunto: pedido de autorização para consulta de receitas e de "
          "livros de registo de consultas externas de 2026."),
        P("[Nome do(a) estudante], estudante da Licenciatura em Farmácia da "
          "Faculdade de Ciências de Saúde da Universidade Lúrio, vem "
          "solicitar autorização para realizar o estudo " +
          _TITULO_ENTRE_ASPAS + ", orientado por [Nome e grau académico "
          "do(a) orientador(a)]. O estudo mede o padrão de prescrição segundo "
          "os indicadores da Organização Mundial da Saúde, para apoiar a "
          "melhoria do uso de medicamentos nos cuidados de saúde primários."),
        P("O trabalho decorrerá entre Fevereiro e Maio de 2027, depois do "
          "parecer favorável do Comité Institucional de Bioética para a Saúde "
          "da Universidade Lúrio, e consiste na consulta, na farmácia de cada "
          "centro, das receitas arquivadas e dos livros de registo das "
          "consultas externas curativas de 2026, de que serão seleccionadas "
          "cerca de 96 receitas por centro. Nenhum documento será retirado, "
          "fotocopiado ou fotografado, não serão registados nomes de doentes "
          "nem de prescritores, e o calendário será combinado com o "
          "responsável da farmácia para não perturbar o serviço. Solicita-se "
          "ainda o número de consultas externas curativas registadas em cada "
          "mês de 2026, necessário ao plano de amostragem."),
        P("Os resultados serão entregues à instituição num relatório-síntese "
          "e, a cada centro, numa sessão própria e confidencial."),
        CAMPO("Nampula, ____ de ______________ de 20___"),
        CAMPO("O(A) estudante: ______________________________"),
        CAMPO("O(A) orientador(a): ______________________________"),
        CAMPO("Despacho da instituição: (   ) Autorizado   (   ) Não "
              "autorizado    Assinatura e carimbo: ______________________"),
    ]),
    ("Termo de confidencialidade da equipa de investigação", [
        P("Eu, ______________________________, na qualidade de (   ) "
          "estudante investigador(a)   (   ) extractor(a) assistente   (   ) "
          "avaliador(a), no estudo " + _TITULO_ENTRE_ASPAS + ", "
          "comprometo-me a:"),
        LISTA([
            "não copiar, fotografar nem retirar dos centros de saúde qualquer "
            "receita ou livro de registo;",
            "não transcrever nomes, números de processo, endereços ou "
            "contactos de doentes, nem nomes de prescritores;",
            "não divulgar a terceiros informação sobre doentes, prescritores "
            "ou centros de saúde, durante e depois do estudo;",
            "guardar as fichas preenchidas em caixa fechada à chave e usar os "
            "dados apenas para os fins do estudo;",
            "comunicar ao orientador qualquer quebra de confidencialidade e "
            "qualquer prescrição com potencial de dano grave observada "
            "durante a extracção.",
        ]),
        CAMPO("Nome: ______________________________    Assinatura: "
              "______________________"),
        CAMPO("Nampula, ___/___/2027"),
    ]),
]
