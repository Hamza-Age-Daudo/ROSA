# -*- coding: utf-8 -*-
"""
Tema 05: Adesao ao tratamento da tuberculose e factores associados a' sua
interrupcao em adultos seguidos nos centros de saude da cidade de Nampula
(Farmacia Clinica e Cuidados Farmaceuticos). Metodos mistos sequencial
explicativo: coorte retrospectiva documental (registos de 2025, seguimento
ate' 2026, consulta em 2027) e entrevistas em profundidade (2027).

Compor e validar:   python _motor/motor.py _conteudo/tema_05.py
Verificar fontes:   python _motor/refs.py verificar _conteudo/tema_05.py
"""
from blocos import (CAMPO, FORMULA, H3, LISTA, NOTA, P, PERG, QUADRO,
                    TABELA)

NUMERO = 5
SLUG = "Adesao_Interrupcao_Tratamento_Tuberculose_Nampula"
TITULO = ("Adesão ao tratamento da tuberculose e factores associados à sua "
          "interrupção em adultos seguidos nos centros de saúde da cidade de "
          "Nampula, 2025-2027")
DESENHO = ("Métodos mistos sequencial explicativo: coorte retrospectiva "
           "documental (livros de registo e fichas de tratamento) seguida de "
           "entrevistas individuais em profundidade")

AUTOR = "[Nome do(a) estudante]"
ORIENTADOR = "[Nome e grau académico do(a) orientador(a)]"

# ---------------------------------------------------------------- resumo --
RESUMO = (
    "A tuberculose continua a ser a doença infecciosa que mais mata no mundo "
    "e Moçambique está entre os países com maior carga da doença. A cura com "
    "o regime de seis meses depende da toma regular dos medicamentos, e a "
    "interrupção do tratamento prolonga a transmissão, favorece a "
    "resistência aos fármacos e aumenta a mortalidade. Os relatórios "
    "nacionais indicam proporções baixas de perda de seguimento, enquanto "
    "estudos distritais do norte do país descrevem valores muito superiores, "
    "e desconhecem-se a frequência e as causas da interrupção nos centros de "
    "saúde da cidade de Nampula. O estudo tem como objectivo avaliar a "
    "adesão ao tratamento da tuberculose e os factores associados à sua "
    "interrupção em adultos seguidos nesses centros. Adopta-se um desenho de "
    "métodos mistos, sequencial explicativo. Na componente quantitativa, uma "
    "coorte retrospectiva incluirá os adultos com tuberculose sensível "
    "registados entre Janeiro e Dezembro de 2025, com seguimento documentado "
    "até Dezembro de 2026, numa amostra estratificada de pelo menos 556 "
    "registos, ou no censo quando os registos elegíveis não excederem 700. "
    "Os dados serão extraídos dos livros de registo e das fichas de "
    "tratamento para uma ficha sem identificadores. A adesão será medida "
    "pela proporção de dias com dose documentada e a interrupção por "
    "períodos de catorze ou mais dias sem medicação, com análise por "
    "proporções e intervalos de confiança, curvas de Kaplan-Meier e "
    "regressão de Cox. Na componente qualitativa, serão realizadas entre 20 "
    "e 24 entrevistas semi-estruturadas, em português ou em Emakhuwa, a "
    "adultos em tratamento em 2027, seleccionados intencionalmente até à "
    "saturação e analisadas por análise temática. Os resultados das duas "
    "componentes serão integrados numa matriz conjunta. Espera-se "
    "identificar a fase do tratamento, os grupos de doentes e as razões que "
    "concentram as interrupções, orientando o aconselhamento farmacêutico, a "
    "farmacovigilância, o apoio social e a busca activa dos faltosos.")
PALAVRAS_CHAVE = ["adesão ao tratamento", "métodos mistos", "Moçambique",
                  "perda de seguimento", "tuberculose"]
ABSTRACT = (
    "Tuberculosis remains the infectious disease that kills the most people "
    "worldwide, and Mozambique is among the countries with the highest "
    "burden. Cure with the six-month regimen depends on regular intake of "
    "the medicines, and treatment interruption prolongs transmission, "
    "favours drug resistance and increases mortality. National reports "
    "show low proportions of loss to follow-up, whereas district studies in "
    "the north of the country describe much higher values, and the "
    "frequency and causes of treatment interruption in the health centres "
    "of Nampula City are unknown. This study aims to assess adherence to "
    "tuberculosis treatment and the factors associated with its "
    "interruption among adults followed in those centres. A sequential "
    "explanatory mixed-methods design is adopted. In the quantitative "
    "component, a retrospective cohort will include adults with "
    "drug-susceptible tuberculosis registered between January and December "
    "2025, with follow-up documented until December 2026, in a stratified "
    "sample of at least 556 records, or a census when eligible records do "
    "not exceed 700. Data will be extracted from the tuberculosis registers "
    "and treatment cards into a form without identifiers. Adherence will be "
    "measured as the proportion of days with a documented dose and "
    "interruption as periods of fourteen or more days without medication, "
    "with analysis by proportions and confidence intervals, Kaplan-Meier "
    "curves and Cox regression. In the qualitative component, 20 to 24 "
    "semi-structured interviews will be conducted, in Portuguese or "
    "Emakhuwa, with adults on treatment in 2027, purposively selected until "
    "saturation and examined through thematic analysis. The results of both "
    "components will be integrated in a joint display. The study is "
    "expected to identify the treatment phase, patient groups and reasons "
    "that concentrate interruptions, guiding pharmaceutical counselling, "
    "pharmacovigilance, social support and the active tracing of patients "
    "who miss their visits.")
KEYWORDS = ["lost to follow-up", "medication adherence", "mixed methods",
            "Mozambique", "tuberculosis"]

ABREVIATURAS = [
    ("CIBS-UniLúrio", "Comité Institucional de Bioética para a Saúde da "
                      "Universidade Lúrio"),
    ("CNBS", "Comité Nacional de Bioética para a Saúde"),
    ("COREQ", "Consolidated Criteria for Reporting Qualitative Research"),
    ("DOT", "tratamento directamente observado (do inglês directly "
            "observed treatment)"),
    ("GRAMMS", "Good Reporting of a Mixed Methods Study"),
    ("HIV", "vírus da imunodeficiência humana"),
    ("IC95%", "intervalo de confiança a 95%"),
    ("IMC", "índice de massa corporal"),
    ("INE", "Instituto Nacional de Estatística"),
    ("IVC", "índice de validade de conteúdo"),
    ("MISAU", "Ministério da Saúde"),
    ("OMS", "Organização Mundial da Saúde"),
    ("PNCT", "Programa Nacional de Controlo da Tuberculose"),
    ("RECORD", "Reporting of Studies Conducted Using Observational "
               "Routinely-Collected Health Data"),
    ("SDSMAS", "Serviço Distrital de Saúde, Mulher e Acção Social"),
    ("SPSS", "Statistical Package for the Social Sciences"),
    ("STROBE", "Strengthening the Reporting of Observational Studies in "
               "Epidemiology"),
    ("TARV", "tratamento anti-retroviral"),
]

# ------------------------------------------------------------ referencias --
FONTES = {
    # --- documentos oficiais
    "who_gtb2025": "World Health Organization. Global tuberculosis report 2025 [Internet]. Geneva: World Health Organization; 2025 [citado 2026 Set 19]. Disponível em: https://www.who.int/teams/global-programme-on-tuberculosis-and-lung-health/tb-reports/global-tuberculosis-report-2025",
    "who_mod4_2025": "World Health Organization. WHO consolidated guidelines on tuberculosis: module 4: treatment and care [Internet]. Geneva: World Health Organization; 2025 [citado 2026 Set 19]. Disponível em: https://www.who.int/publications/i/item/9789240107243",
    "who_surv2024": "World Health Organization. Consolidated guidance on tuberculosis data generation and use: module 1: tuberculosis surveillance [Internet]. Geneva: World Health Organization; 2024 [citado 2026 Set 19]. Disponível em: https://www.who.int/publications/i/item/9789240075290",
    "who_adesao2003": "World Health Organization. Adherence to long-term therapies: evidence for action [Internet]. Geneva: World Health Organization; 2003 [citado 2026 Set 19]. Disponível em: https://www.paho.org/sites/default/files/WHO-Adherence-Long-Term-Therapies-Eng-2003.pdf",
    "misau_pnct2020": "Ministério da Saúde (Moçambique), Direcção Nacional de Saúde Pública, Programa Nacional de Controlo da Tuberculose. Relatório anual do programa 2020 [Internet]. Maputo: Ministério da Saúde; 2021 [citado 2026 Set 19]. Disponível em: https://docs.bvsalud.org/biblioref/2021/11/1344394/relatorio-anual-do-pnct-2020_final_v23062021.pdf",
    "misau_protocolos2019": "Ministério da Saúde (Moçambique), Programa Nacional de Controlo da Tuberculose. Protocolos nacionais: avaliação e manejo de pacientes com tuberculose. Versão 2 [Internet]. Maputo: Ministério da Saúde; 2019 [citado 2026 Set 19]. Disponível em: https://comitetarvmisau.co.mz/docs/orientacoes_nacionais/Gui%C3%A3o_Normas_cl%C3%ADnicas_PNCT_Dez19.pdf",
    "ine2021": "Instituto Nacional de Estatística (Moçambique). IV Recenseamento Geral da População e Habitação 2017: resultados definitivos, província de Nampula [Internet]. Nampula: Instituto Nacional de Estatística; 2021 [citado 2026 Set 19]. Disponível em: http://www.sina.gov.mz/wp-content/uploads/2024/05/NAMPULA-RESUTADOS-DEFINITIVOS-DO-CENSO-2017.pdf",
    # --- Moçambique
    "osorio2022": "Osório D, Munyangaju I, Nacarapa E, Nhangave AV, Ramos-Rincon JM. Predictors of unfavourable tuberculosis treatment outcome in Bilene District, Gaza Province, Mozambique: A retrospective analysis, 2016 - 2019. S Afr Med J. 2022;112(3):234-239. PMID: 35380527.",
    "give2024": "Give C, Morris C, Murray J, José B, Machava R, Wayal S. Sociocultural understanding of Tuberculosis and implications for care-seeking among adults in the province of Zambezia, Mozambique: Qualitative research. PLoS One. 2024;19(1):e0289928. doi:10.1371/journal.pone.0289928. PMID: 38236935.",
    "cuboia2024": "Cuboia N, Reis-Pardal J, Pfumo-Cuboia I, Manhiça I, Mutaquiha C, Nitrogénio L, et al. Spatial distribution and determinants of tuberculosis incidence in Mozambique: A nationwide Bayesian disease mapping study. Spat Spatiotemporal Epidemiol. 2024;48:100632. doi:10.1016/j.sste.2023.100632. PMID: 38355255.",
    "garciabasteiro2016": "García-Basteiro AL, Respeito D, Augusto OJ, López-Varela E, Sacoor C, Sequera VG, et al. Poor tuberculosis treatment outcomes in Southern Mozambique (2011-2012). BMC Infect Dis. 2016;16:214. doi:10.1186/s12879-016-1534-y. PMID: 27198545.",
    "wikmanjorgensen2015": "Wikman-Jorgensen PE, Morales-Cartagena A, Llenas-García J, Pérez-Porcuna TM, Hobbins M, Ehmer J, et al. Implementation challenges of a TB programme in rural northern mozambique: evaluation of 2012-2013 outcomes. Pathog Glob Health. 2015;109(5):221-7. doi:10.1179/2047773215Y.0000000027. PMID: 26239760.",
    "xavier2026": "Xavier SP, Rafael GAP, Gotine ARME, Agostinho MA, Cumaquela G, Rocha ZAJ, et al. A Novel Clinical Nomogram for Predicting Unfavorable Tuberculosis Treatment Outcomes: A Logistic Regression Risk Model. J Epidemiol Glob Health. 2026;16(1). doi:10.1007/s44197-026-00532-z. PMID: 41849009.",
    "mbatemutemba2026": "Mbate-Mutemba C, Nunes E, Munyangaju I, Ramos-Rincón JM, José B, Martins MDR. Factors associated with unsuccessful tuberculosis treatment outcome in children in four provinces of Mozambique: a retrospective cohort study, 2018-2021. BMC Infect Dis. 2026;26(1). doi:10.1186/s12879-026-13290-x. PMID: 41975300.",
    "nacarapa2020": "Nacarapa E, Muchiri E, Moon TD, Charalambous S, Verdu ME, Ramos JM, et al. Effect of Xpert MTB/RIF testing introduction and favorable outcome predictors for tuberculosis treatment among HIV infected adults in rural southern Mozambique. A retrospective cohort study. PLoS One. 2020;15(3):e0229995. doi:10.1371/journal.pone.0229995. PMID: 32150595.",
    "deschacht2019": "De Schacht C, Mutaquiha C, Faria F, Castro G, Manaca N, Manhiça I, et al. Barriers to access and adherence to tuberculosis services, as perceived by patients: A qualitative study in Mozambique. PLoS One. 2019;14(7):e0219470. doi:10.1371/journal.pone.0219470. PMID: 31291352.",
    "mitano2017": "Mitano F, Sicsú AN, Lima MC, Peruhype RC, Protti ST, Palha PF. Discourses on short-coursetherapy for tuberculosis control [Discursos sobre a terapia de curta duração para o controle da tuberculose]. Rev Bras Enferm. 2017;70(1):126-132. doi:10.1590/0034-7167-2016-0463. PMID: 28226051.",
    "lopezvarela2017": "Lopez-Varela E, Sequera VG, García-Basteiro AL, Augusto OJ, Munguambe K, Sacarlal J, et al. Adherence to Childhood Tuberculosis Treatment in Mozambique. J Trop Pediatr. 2017;63(2):87-97. doi:10.1093/tropej/fmw048. PMID: 27521147.",
    # --- adesao, medicao e determinantes
    "valencia2017": "Valencia S, León M, Losada I, Sequera VG, Fernández Quevedo M, García-Basteiro AL. How do we measure adherence to anti-tuberculosis treatment?. Expert Rev Anti Infect Ther. 2017;15(2):157-165. doi:10.1080/14787210.2017.1264270. PMID: 27910715.",
    "imperial2018": "Imperial MZ, Nahid P, Phillips PPJ, Davies GR, Fielding K, Hanna D, et al. A patient-level pooled analysis of treatment-shortening regimens for drug-susceptible pulmonary tuberculosis. Nat Med. 2018;24(11):1708-1715. doi:10.1038/s41591-018-0224-2. PMID: 30397355.",
    "ferreira2025": "Ferreira IBB, Menezes RC, Araújo-Pereira M, Rolla VC, Kritski AL, Cordeiro-Santos M, et al. Effects of missed anti-tuberculosis therapy doses on treatment outcome: a multi-center cohort study. Lancet Reg Health Am. 2025;48:101162. doi:10.1016/j.lana.2025.101162. PMID: 40657430.",
    "walker2024": "Walker EF, Flook M, Rodger AJ, Fielding KL, Stagg HR. Quantifying non-adherence to anti-tuberculosis treatment due to early discontinuation: a systematic literature review of timings to loss to follow-up. BMJ Open Respir Res. 2024;11(1). doi:10.1136/bmjresp-2023-001894. PMID: 38359965.",
    "teferi2021": "Teferi MY, El-Khatib Z, Boltena MT, Andualem AT, Asamoah BO, Biru M, et al. Tuberculosis Treatment Outcome and Predictors in Africa: A Systematic Review and Meta-Analysis. Int J Environ Res Public Health. 2021;18(20). doi:10.3390/ijerph182010678. PMID: 34682420.",
    "zegeye2019": "Zegeye A, Dessie G, Wagnew F, Gebrie A, Islam SMS, Tesfaye B, et al. Prevalence and determinants of anti-tuberculosis treatment non-adherence in Ethiopia: A systematic review and meta-analysis. PLoS One. 2019;14(1):e0210422. doi:10.1371/journal.pone.0210422. PMID: 30629684.",
    "watumo2022": "Watumo D, Mengesha MM, Gobena T, Gebremichael MA, Jerene D. Predictors of loss to follow-up among adult tuberculosis patients in Southern Ethiopia: a retrospective follow-up study. BMC Public Health. 2022;22(1):976. doi:10.1186/s12889-022-13390-8. PMID: 35568853.",
    "kibuule2020": "Kibuule D, Aiases P, Ruswa N, Rennie TW, Verbeeck RK, Godman B, et al. Predictors of loss to follow-up of tuberculosis cases under the DOTS programme in Namibia. ERJ Open Res. 2020;6(1). doi:10.1183/23120541.00030-2019. PMID: 32201689.",
    "appiah2023": "Appiah MA, Arthur JA, Gborgblorvor D, Asampong E, Kye-Duodu G, Kamau EM, et al. Barriers to tuberculosis treatment adherence in high-burden tuberculosis settings in Ashanti region, Ghana: a qualitative study from patient's perspective. BMC Public Health. 2023;23(1):1317. doi:10.1186/s12889-023-16259-6. PMID: 37430295.",
    "gebreweld2018": "Gebreweld FH, Kifle MM, Gebremicheal FE, Simel LL, Gezae MM, Ghebreyesus SS, et al. Factors influencing adherence to tuberculosis treatment in Asmara, Eritrea: a qualitative study. J Health Popul Nutr. 2018;37(1):1. doi:10.1186/s41043-017-0132-y. PMID: 29304840.",
    "timire2021": "Timire C, Ngwenya M, Chirenda J, Metcalfe JZ, Kranzer K, Pedrazzoli D, et al. Catastrophic costs among tuberculosis-affected households in Zimbabwe: A national health facility-based survey. Trop Med Int Health. 2021;26(10):1248-1255. doi:10.1111/tmi.13647. PMID: 34192392.",
    "wagnew2024": "Wagnew F, Gray D, Tsheten T, Kelly M, Clements ACA, Alene KA. Effectiveness of nutritional support to improve treatment adherence in patients with tuberculosis: a systematic review. Nutr Rev. 2024;82(9):1216-1225. doi:10.1093/nutrit/nuad120. PMID: 37759339.",
    "dixon2025": "Dixon EG, Biraua E, Brencsēns E, Pašuks V, Riekstina V, Šperberga A, et al. Adverse drug reactions, particularly liver disorders, drive interruptions in anti-tuberculosis treatment: A retrospective cohort study. Br J Clin Pharmacol. 2025;91(12):3461-3470. doi:10.1002/bcp.70197. PMID: 40785321.",
    "ruizgrosso2020": "Ruiz-Grosso P, Cachay R, de la Flor A, Schwalb A, Ugarte-Gil C. Association between tuberculosis and depression on negative outcomes of tuberculosis treatment: A systematic review and meta-analysis. PLoS One. 2020;15(1):e0227472. doi:10.1371/journal.pone.0227472. PMID: 31923280.",
    "lawal2025": "Lawal A, Hussein A, Tiberi S, Kunst H. Barriers to and enablers of adherence to the treatment of active drug-sensitive tuberculosis in people living with HIV: a mixed method systematic review. BMC Public Health. 2025;26(1):39. doi:10.1186/s12889-025-25631-7. PMID: 41316088.",
    # --- intervencoes e cuidados farmaceuticos
    "alipanah2018": "Alipanah N, Jarlsberg L, Miller C, Linh NN, Falzon D, Jaramillo E, et al. Adherence interventions and outcomes of tuberculosis treatment: A systematic review and meta-analysis of trials and observational studies. PLoS Med. 2018;15(7):e1002595. doi:10.1371/journal.pmed.1002595. PMID: 29969463.",
    "muller2018": "Müller AM, Osório CS, Silva DR, Sbruzzi G, de Tarso P, Dalcin R. Interventions to improve adherence to tuberculosis treatment: systematic review and meta-analysis. Int J Tuberc Lung Dis. 2018;22(7):731-740. doi:10.5588/ijtld.17.0596. PMID: 29914598.",
    "mohamed2025": "Mohamed MS, Zary M, Kafie C, Chilala CI, Bahukudumbi S, Foster N, et al. The impact of digital adherence technologies on treatment outcomes, adherence, and patient-reported outcomes in tuberculosis: a systematic review and meta-analysis. BMC Infect Dis. 2025;25(1):1314. doi:10.1186/s12879-025-11503-3. PMID: 41087928.",
    "iskandar2023": "Iskandar D, Suryanegara FDA, van Boven JFM, Postma MJ. Clinical pharmacy services for tuberculosis management: a systematic review. Front Pharmacol. 2023;14:1186905. doi:10.3389/fphar.2023.1186905. PMID: 37484021.",
    # --- metodos
    "murry2023": "Murry LT, Fadare OO, Al-Khatib A, Witry MJ. Integration in mixed-methods studies: existing practices, considerations and recommendations for pharmacy research. Int J Pharm Pract. 2023;31(4):431-437. doi:10.1093/ijpp/riad033. PMID: 37348921.",
    "ocathain2008": "O'Cathain A, Murphy E, Nicholl J. The quality of mixed methods studies in health services research. J Health Serv Res Policy. 2008;13(2):92-8. doi:10.1258/jhsrp.2007.007074. PMID: 18416914.",
    "von2007": "von Elm E, Altman DG, Egger M, Pocock SJ, Gøtzsche PC, Vandenbroucke JP. Strengthening the Reporting of Observational Studies in Epidemiology (STROBE) statement: guidelines for reporting observational studies. BMJ. 2007;335(7624):806-8. doi:10.1136/bmj.39335.541782.AD. PMID: 17947786.",
    "benchimol2015": "Benchimol EI, Smeeth L, Guttmann A, Harron K, Moher D, Petersen I, et al. The REporting of studies Conducted using Observational Routinely-collected health Data (RECORD) statement. PLoS Med. 2015;12(10):e1001885. doi:10.1371/journal.pmed.1001885. PMID: 26440803.",
    "tong2007": "Tong A, Sainsbury P, Craig J. Consolidated criteria for reporting qualitative research (COREQ): a 32-item checklist for interviews and focus groups. Int J Qual Health Care. 2007;19(6):349-57. doi:10.1093/intqhc/mzm042. PMID: 17872937.",
    "hennink2022": "Hennink M, Kaiser BN. Sample sizes for saturation in qualitative research: A systematic review of empirical tests. Soc Sci Med. 2022;292:114523. doi:10.1016/j.socscimed.2021.114523. PMID: 34785096.",
    "guest2020": "Guest G, Namey E, Chen M. A simple method to assess and report thematic saturation in qualitative research. PLoS One. 2020;15(5):e0232076. doi:10.1371/journal.pone.0232076. PMID: 32369511.",
    "byrne2022": "Byrne D. A worked example of Braun and Clarke’s approach to reflexive thematic analysis. Qual Quant. 2022;56(3):1391-1412. doi:10.1007/s11135-021-01182-y",
    "oconnor2020": "O’Connor C, Joffe H. Intercoder Reliability in Qualitative Research: Debates and Practical Guidelines. International Journal of Qualitative Methods. 2020;19:1609406919899220. doi:10.1177/1609406919899220",
    "serdar2021": "Serdar CC, Cihan M, Yücel D, Serdar MA. Sample size, power and effect size revisited: simplified and practical approaches in pre-clinical, clinical and laboratory studies. Biochem Med (Zagreb). 2021;31(1):010502. doi:10.11613/BM.2021.010502. PMID: 33380887.",
    "peduzzi1996": "Peduzzi P, Concato J, Kemper E, Holford TR, Feinstein AR. A simulation study of the number of events per variable in logistic regression analysis. J Clin Epidemiol. 1996;49(12):1373-9. doi:10.1016/s0895-4356(96)00236-3. PMID: 8970487.",
    "wma2025": "World Medical Association. World Medical Association Declaration of Helsinki: Ethical Principles for Medical Research Involving Human Participants. JAMA. 2025;333(1):71-74. doi:10.1001/jama.2024.21972. PMID: 39425955.",
}
SEMINAIS = {
    "who_adesao2003": "Documento original da OMS que define a adesão a "
                      "terapêuticas prolongadas e propõe o modelo das cinco "
                      "dimensões usado como quadro analítico do estudo.",
    "wikmanjorgensen2015": "Única avaliação publicada dos resultados do "
                           "programa de tuberculose num distrito rural do "
                           "norte de Moçambique, citada como evidência "
                           "regional e não incluída no estado da arte.",
    "von2007": "Declaração STROBE, norma de relato de estudos "
               "observacionais e base da extensão RECORD, ainda em vigor.",
    "benchimol2015": "Declaração RECORD, norma de relato de estudos com "
                     "dados de rotina, ainda em vigor.",
    "tong2007": "Lista COREQ, norma de relato de estudos qualitativos com "
                "entrevistas, ainda em vigor.",
    "ocathain2008": "Artigo que propõe as recomendações GRAMMS para o relato "
                    "de estudos de métodos mistos, ainda em vigor.",
    "peduzzi1996": "Estudo de simulação que fundamenta a regra de pelo menos "
                   "dez eventos por variável nos modelos de regressão.",
}

# ----------------------------------------------------- 1. introducao --------
INTRODUCAO = [
    P("A tuberculose continua a ser a principal causa de morte por um único "
      "agente infeccioso. Em 2024, estima-se que 10,7 milhões de pessoas "
      "tenham adoecido com tuberculose e que a doença tenha causado 1,23 "
      "milhões de mortes, 150.000 das quais em pessoas que vivem com o vírus "
      "da imunodeficiência humana (HIV). Entre 2015 e 2024, a taxa de "
      "incidência global desceu apenas 12%, longe da redução de 50% prevista "
      "para 2025 na Estratégia pelo Fim da Tuberculose da Organização Mundial "
      "da Saúde (OMS), e cerca de metade das pessoas tratadas e dos seus "
      "agregados suportou custos catastróficos, superiores a 20% do "
      "rendimento anual do agregado {who_gtb2025}. Entre os factores de risco "
      "quantificados, a subnutrição continua a ser aquele a que se atribui o "
      "maior número de casos novos, 0,97 milhões em 2024, seguida de perto "
      "pela diabetes, com 0,93 milhões, enquanto à infecção pelo HIV se "
      "atribuem 0,57 milhões {who_gtb2025}."),
    P("A tuberculose sensível aos fármacos cura-se com um regime padronizado "
      "de seis meses. Em Moçambique, os adultos recebem uma fase intensiva de "
      "dois meses com isoniazida, rifampicina, pirazinamida e etambutol em "
      "dose fixa combinada, seguida de uma fase de manutenção de quatro meses "
      "com isoniazida e rifampicina, ambas de toma diária "
      "{misau_protocolos2019}. A eficácia deste regime depende da "
      "regularidade da toma. Numa análise conjunta de dados individuais de "
      "3.405 participantes de ensaios clínicos, a adesão igual ou inferior a "
      "90% foi um factor de risco significativo de resultado desfavorável "
      "{imperial2018}, e numa coorte brasileira os doentes que falharam mais "
      "de 10% das doses tiveram resultados desfavoráveis em 81,2% dos casos, "
      "contra 21,6% entre os que tomaram todas as doses {ferreira2025}. No "
      "extremo da não adesão está a perda de seguimento, que a OMS define "
      "como a interrupção do tratamento durante dois meses consecutivos ou "
      "mais {who_surv2024}."),
    P("Na África subsariana, os resultados do tratamento continuam aquém das "
      "metas. Uma meta-análise de 26 estudos africanos estimou uma taxa de "
      "sucesso terapêutico de 79%, abaixo do limiar de 85% fixado pela OMS, e "
      "atribuiu 47% dos resultados sem sucesso ao abandono do tratamento e "
      "48% ao óbito {teferi2021}. Na Etiópia, a prevalência agregada de não "
      "adesão foi de 21,29%, associada ao esquecimento, ao receio dos efeitos "
      "adversos, ao tempo de espera nos serviços e à distância percebida até "
      "à unidade sanitária {zegeye2019}. Estudos qualitativos no Gana e na "
      "Eritreia acrescentam a insegurança alimentar, o custo do transporte, a "
      "perda de rendimento, o estigma e a sensação de cura ou a melhoria "
      "clínica depois da fase intensiva como razões apontadas pelos próprios "
      "doentes para deixar a medicação {appiah2023,gebreweld2018}."),
    P("Moçambique integra a lista dos 30 países com elevada carga de "
      "tuberculose {osorio2022}, com uma incidência estimada de 368 casos por "
      "100.000 habitantes em 2020 {give2024}. Entre 2016 e 2020 foram "
      "diagnosticadas 512.877 pessoas com tuberculose no país, com uma "
      "distribuição desigual entre os 154 distritos e uma incidência "
      "positivamente associada à prevalência do HIV {cuboia2024}. Segundo o "
      "relatório anual do Programa Nacional de Controlo da Tuberculose (PNCT) "
      "do Ministério da Saúde (MISAU), foram notificados 97.093 casos em "
      "2020, uma taxa de notificação de 323 casos por 100.000 habitantes, "
      "aquém da incidência estimada; a taxa de "
      "sucesso do tratamento da tuberculose sensível atingiu 92%, com 3% de "
      "óbitos, 1,7% de perda de seguimento e 0,2% de falência, e 27% dos "
      "doentes tinham co-infecção pelo HIV {misau_pnct2020}."),
    P("Os estudos distritais descrevem um quadro menos favorável do que os "
      "agregados nacionais. Em Manhiça, no sul do país, 15,1% dos 1.957 "
      "doentes que iniciaram tratamento em 2011-2012 morreram durante o "
      "tratamento e 10% abandonaram-no {garciabasteiro2016}. No distrito de "
      "Ancuabe, no norte rural, 44,9% dos casos novos registados em "
      "2012-2013 foram perdidos para o seguimento {wikmanjorgensen2015}, e em "
      "Nacarôa, na província de Nampula, 26,8% dos 205 doentes tratados "
      "entre 2021 e 2023 tiveram um resultado desfavorável, sendo a ausência "
      "de tratamento directamente observado um dos preditores {xavier2026}. "
      "A cidade de Nampula, capital da província, era em 2017 o distrito "
      "mais populoso da província, com 798.462 habitantes recenseados, 13,9% "
      "do total provincial {ine2021}."),
    P("Apesar desta carga, não foi localizado nenhum estudo publicado que "
      "medisse a adesão ou a interrupção do tratamento nos centros de saúde "
      "da cidade de Nampula, nem que ouvisse os doentes sobre as razões para "
      "deixar a medicação. A evidência qualitativa moçambicana disponível "
      "provém de doentes das províncias de Sofala e Manica {deschacht2019}, "
      "de membros da comunidade e de profissionais na Zambézia {give2024} e "
      "de profissionais de saúde envolvidos no tratamento observado "
      "{mitano2017}. O presente estudo pretende colmatar esta lacuna, "
      "avaliando a adesão ao tratamento da tuberculose e os factores "
      "associados à sua interrupção em adultos seguidos nos centros de saúde "
      "da cidade de Nampula, através de um desenho de métodos mistos que "
      "quantifica as interrupções a partir dos registos clínicos e procura "
      "compreender as suas causas nas palavras de quem está em tratamento."),
]

# ----------------------------------------------------- 2. problema ----------
PROBLEMA = [
    P("Nos centros de saúde da cidade de Nampula, o adulto com tuberculose "
      "sensível inicia o tratamento no sector de tuberculose e, segundo os "
      "protocolos nacionais, deve ser visto diariamente para a toma "
      "observada durante os dois primeiros meses e avaliado clinicamente às "
      "duas semanas e, depois, pelo menos uma vez por mês "
      "{misau_protocolos2019}. Na fase de manutenção, a toma deixa de ser "
      "observada todos os dias e a adesão passa a ser avaliada pela revisão "
      "do cartão do doente e pela pergunta sobre as tomas não presenciadas "
      "{misau_protocolos2019}. A literatura situa as interrupções tanto nos "
      "dois primeiros meses, em que a perda de seguimento é mais frequente do "
      "que o esperado em muitos países {walker2024}, como na passagem para a "
      "fase de manutenção, quando o doente se sente melhor {appiah2023}."),
    P("O problema concreto é que a magnitude destas interrupções na cidade é "
      "desconhecida. O indicador de rotina do programa só contabiliza a "
      "perda de seguimento, isto é, a interrupção de dois meses ou mais, e o "
      "valor nacional de 1,7% registado em 2020 {misau_pnct2020} contrasta "
      "com as proporções de perda de seguimento e de resultados desfavoráveis "
      "descritas em estudos distritais do norte do país "
      "{wikmanjorgensen2015,xavier2026}. As interrupções mais curtas, que o "
      "próprio algoritmo nacional classifica em menos de duas semanas e em "
      "duas a oito semanas, e que obrigam a prolongar o tratamento ou a "
      "repetir exames {misau_protocolos2019}, não aparecem nos relatórios e "
      "ficam anotadas apenas nas fichas de tratamento. Sem a sua "
      "quantificação, não se sabe quantos doentes estão em risco nem em que "
      "fase do tratamento as interrupções se concentram."),
    P("As consequências são clínicas, epidemiológicas e sociais. A falha de "
      "doses, mesmo em proporções modestas, associa-se a resultados "
      "desfavoráveis {imperial2018,ferreira2025}, e a adesão incompleta "
      "aumenta o risco de conversão bacteriológica tardia, de transmissão "
      "continuada na comunidade, de falência, de recaída e de resistência aos "
      "fármacos {alipanah2018}. Os sintomas depressivos, comuns na "
      "tuberculose, associam-se fortemente à perda de seguimento, com uma "
      "razão de probabilidades de 8,70 numa meta-análise {ruizgrosso2020}. "
      "Para as famílias, a doença traduz-se em custos que, no Zimbabué, foram "
      "catastróficos para 80% dos agregados afectados {timire2021}."),
    P("Falta saber, no contexto urbano de Nampula, quem interrompe o "
      "tratamento, quando e porquê. Os factores descritos noutros países, "
      "como a melhoria precoce dos sintomas, os efeitos adversos, a falta de "
      "alimentos ou os custos de transporte {appiah2023,gebreweld2018,"
      "dixon2025}, dependem do contexto económico e cultural e da "
      "organização dos serviços, e não foram estudados nos centros de saúde "
      "da cidade. Esta lacuna impede a equipa de saúde, incluindo os "
      "farmacêuticos, de orientar o aconselhamento, a farmacovigilância, o "
      "apoio nutricional e a busca activa para os doentes e para os momentos "
      "de maior risco."),
]
PERGUNTA = ("Qual é a adesão ao tratamento da tuberculose sensível entre os "
            "adultos seguidos nos centros de saúde da cidade de Nampula, com "
            "que frequência, em que fase e em que doentes ocorre a "
            "interrupção do tratamento, e que razões apontam os doentes para "
            "essa interrupção?")
DELIMITACAO = [
    P("O estudo decorre nos centros de saúde públicos da cidade de Nampula "
      "que iniciam e seguem o tratamento ambulatório da tuberculose "
      "sensível, sob a gestão do Serviço Distrital de Saúde, Mulher e Acção "
      "Social (SDSMAS) da Cidade de Nampula. A componente quantitativa "
      "abrange os adultos, com 18 ou mais anos, registados para tratamento "
      "de primeira linha entre 1 de Janeiro e 31 de Dezembro de 2025, cujo "
      "seguimento ficou documentado até 31 de Dezembro de 2026; os livros e "
      "as fichas serão consultados entre Março e Abril de 2027. A componente "
      "qualitativa abrange adultos em tratamento nos mesmos centros, "
      "entrevistados entre Maio e Junho de 2027. O objecto do estudo é a "
      "adesão ao tratamento, a interrupção e a perda de seguimento, os "
      "factores associados e as razões atribuídas pelos doentes."),
    P("Ficam fora do estudo a tuberculose resistente à rifampicina, cujo "
      "regime, registos e modelo de seguimento são distintos; as crianças e "
      "os adolescentes com menos de 18 anos, cujos determinantes de adesão "
      "envolvem os cuidadores e merecem estudo próprio; o tratamento "
      "preventivo da tuberculose; os doentes seguidos apenas em hospitais ou "
      "em clínicas privadas; a perspectiva dos profissionais de saúde; a "
      "medição da adesão por marcadores biológicos; e a quantificação "
      "monetária dos custos suportados pelos agregados."),
]

# ----------------------------------------------------- 3. objectivos --------
OBJECTIVO_GERAL = ("Avaliar a adesão ao tratamento da tuberculose e os "
                   "factores associados à sua interrupção em adultos "
                   "seguidos nos centros de saúde da cidade de Nampula, "
                   "entre 2025 e 2027.")
OBJECTIVOS_ESPECIFICOS = [
    "Caracterizar o perfil sociodemográfico, clínico e de seguimento dos "
    "adultos que iniciaram o tratamento da tuberculose sensível em 2025;",
    "Determinar a proporção de dias com dose documentada, a frequência, a "
    "duração e a fase de ocorrência das interrupções do tratamento, "
    "incluindo a perda de seguimento;",
    "Analisar a associação entre os factores sociodemográficos, clínicos e "
    "de serviço e a interrupção do tratamento;",
    "Explorar as razões da interrupção e os facilitadores da adesão, na "
    "perspectiva dos adultos em tratamento em 2027.",
]

# ----------------------------------------------------- 4. hipoteses ---------
HIPOTESES_INTRO = [
    P("As hipóteses referem-se ao objectivo específico 3, que analisa os "
      "factores associados à interrupção, e à comparação das taxas de "
      "interrupção entre as fases do tratamento, prevista no objectivo "
      "específico 2.")]
HIPOTESES = [
    ("H0 (factores)", "não existe associação estatisticamente significativa "
     "entre os factores sociodemográficos (sexo, idade, residência), clínicos "
     "(categoria do doente, forma e base do diagnóstico, estado serológico "
     "para o HIV, índice de massa corporal inicial, efeitos adversos "
     "registados) e de serviço (modalidade de supervisão, contacto "
     "telefónico e apoio nutricional registados) e o tempo até à primeira "
     "interrupção do tratamento;"),
    ("H1 (factores)", "pelo menos um destes factores está associado de forma "
     "estatisticamente significativa ao tempo até à primeira interrupção do "
     "tratamento;"),
    ("H0 (fases)", "a taxa de início de interrupções por 1.000 pessoas-dia "
     "de tratamento é igual na fase intensiva e na fase de manutenção;"),
    ("H1 (fases)", "a taxa de início de interrupções por 1.000 pessoas-dia "
     "de tratamento difere entre a fase intensiva e a fase de manutenção."),
]
QUESTOES = [
    "Que proporção de adultos atinge uma adesão adequada, isto é, dose "
    "documentada em 90% ou mais dos dias de tratamento, e que proporção tem "
    "pelo menos uma interrupção de 14 ou mais dias?",
    "Como descrevem os adultos em tratamento as razões que os levaram, ou "
    "quase levaram, a interromper a medicação?",
    "Que condições familiares, económicas e dos serviços de saúde ajudam os "
    "doentes a completar o tratamento?",
]

# ----------------------------------------------------- 5. justificativa -----
JUSTIFICATIVA_INTRO = [
    P("A escolha do tema responde a um problema de saúde pública com peso "
      "elevado na província, a uma lacuna de evidência local e a uma área em "
      "que a intervenção farmacêutica tem espaço para melhorar os "
      "resultados do tratamento. A sua pertinência organiza-se em quatro "
      "dimensões.")]
JUSTIFICATIVA = {
    "cientifica": [
        P("O estudo produz a primeira estimativa, para os centros de saúde da "
          "cidade de Nampula, da adesão ao tratamento e das interrupções de "
          "curta e de longa duração, e não apenas da perda de seguimento que "
          "os relatórios de rotina registam {misau_pnct2020}. Ao medir o "
          "momento em que as interrupções começam, contribui para uma questão "
          "em aberto na literatura, que mostra perdas de seguimento "
          "concentradas nos primeiros meses em muitos países {walker2024}. "
          "Como não existe um padrão de referência para medir a adesão à "
          "terapêutica antituberculosa nem uma definição consensual dos seus "
          "níveis {valencia2017}, a descrição explícita de um método de "
          "medição a partir dos registos de rotina tem utilidade para estudos "
          "posteriores em contextos de recursos limitados."),
        P("A componente qualitativa acrescenta a explicação que os estudos "
          "moçambicanos baseados em registos não oferecem, porque identificam "
          "preditores de resultados desfavoráveis sem ouvir os doentes "
          "{osorio2022,xavier2026}."),
    ],
    "academica": [
        P("Para o curso de Farmácia da Universidade Lúrio, o estudo aplica "
          "métodos de farmacoepidemiologia e de investigação qualitativa a "
          "um problema de cuidados farmacêuticos. A integração intencional "
          "de dados quantitativos e qualitativos permite respostas que "
          "nenhuma das componentes daria isoladamente {murry2023}. Numa revisão "
          "sistemática de serviços de farmácia clínica na tuberculose, a "
          "adesão à medicação foi o foco de 50% das intervenções, o "
          "aconselhamento e a informação sobre medicamentos estiveram "
          "presentes em 80% e a monitorização de reacções adversas em 50% "
          "{iskandar2023}, o que situa o tema no núcleo das competências do "
          "farmacêutico. O trabalho prolonga ainda a produção científica "
          "sobre tuberculose com participação de autores da Universidade "
          "Lúrio {mitano2017,xavier2026}."),
    ],
    "social": [
        P("A interrupção do tratamento prolonga a transmissão no agregado, "
          "aumenta o risco de morte e agrava a pobreza. Cerca de metade das "
          "pessoas tratadas por tuberculose no mundo e dos seus agregados "
          "enfrentam custos catastróficos {who_gtb2025} e, no Zimbabué, esses "
          "custos atingiram 80% dos agregados, sendo os suplementos "
          "nutricionais o principal componente do custo depois do "
          "diagnóstico {timire2021}. Ao identificar as razões económicas, "
          "alimentares e sociais das interrupções, o estudo fornece base para "
          "orientar o apoio nutricional, que melhorou a adesão em cinco dos "
          "oito estudos incluídos numa revisão sistemática {wagnew2024}, e "
          "para devolver aos doentes e às famílias informação útil sobre a "
          "duração e a importância do tratamento."),
    ],
    "politica": [
        P("A OMS emite uma recomendação forte a favor da educação para a "
          "saúde e do aconselhamento sobre a doença e a adesão para todos os "
          "doentes em tratamento, admite pacotes de intervenções de adesão que incluem "
          "apoio material, apoio psicológico, rastreadores ou monitores "
          "digitais e formação do pessoal, e prefere o apoio ao tratamento na "
          "comunidade ou no domicílio ao apoio centrado na unidade sanitária "
          "ou ao tratamento não supervisionado {who_mod4_2025}. O PNCT prevê "
          "intervenções comunitárias que incluem a educação para a saúde, o "
          "apoio emocional aos doentes e a busca activa dos faltosos e dos "
          "abandonos {misau_pnct2020}."),
        P("Os resultados permitirão ao SDSMAS e à Direcção Provincial de "
          "Saúde de Nampula decidir em que doentes e em que fase do "
          "tratamento concentrar estes recursos, que são escassos, e "
          "contribuem para a aproximação às metas da Estratégia pelo Fim da "
          "Tuberculose, das quais o mundo permanece distante {who_gtb2025}."),
    ],
}

# ----------------------------------------------------- 6. revisao -----------
REVISAO = [
    ("Tuberculose sensível: regime terapêutico e resultados do tratamento", [
        P("Os protocolos nacionais classificam como caso novo o doente nunca "
          "tratado para tuberculose ou tratado durante menos de um mês, e "
          "como caso previamente tratado o que recebeu pelo menos um mês de "
          "tratamento. Todos os esquemas de primeira linha usam fármacos em "
          "dose fixa combinada e têm uma fase intensiva e uma fase de "
          "manutenção: no adulto, dois meses diários de isoniazida, "
          "rifampicina, pirazinamida e etambutol, seguidos de quatro meses "
          "diários de isoniazida e rifampicina. Na maioria das formas "
          "extrapulmonares a duração é igualmente de seis meses, com "
          "excepção da tuberculose meníngea e osteoarticular, e o país deixou "
          "de usar o regime de retratamento com injectável, passando os "
          "doentes previamente tratados a fazer testes de sensibilidade "
          "{misau_protocolos2019}. A dose é calculada pelo peso, o que obriga "
          "a pesar o doente em cada consulta e a ajustar o número de "
          "comprimidos {misau_protocolos2019}."),
        P("O resultado de cada tratamento é atribuído segundo definições "
          "padronizadas. É curado o doente com tuberculose pulmonar "
          "bacteriologicamente confirmada que completa o tratamento com "
          "evidência de resposta bacteriológica; tem tratamento completo o "
          "que o termina sem cumprir os critérios de cura ou de falência; "
          "sucesso terapêutico é a soma destas duas categorias; e há ainda "
          "falência, óbito, perda de seguimento, quando o tratamento é "
          "interrompido durante dois meses consecutivos ou mais, e não "
          "avaliado, quando nenhum resultado é atribuído {who_surv2024}. "
          "Estas definições, registadas no livro da tuberculose, serão "
          "usadas sem alteração neste estudo."),
        P("A co-infecção pelo HIV exige a toma simultânea do tratamento "
          "anti-retroviral (TARV), com mais comprimidos e mais consultas. Em "
          "2020, a cobertura do TARV nos doentes com tuberculose e HIV "
          "manteve-se em 95% no país {misau_pnct2020}, mas numa revisão de "
          "estudos sobre doentes co-infectados a doença avançada, as "
          "comorbilidades, o consumo de álcool, o baixo nível socioeconómico "
          "e as interacções negativas com os serviços surgiram como barreiras "
          "à adesão ao tratamento da tuberculose {lawal2025}."),
    ]),
    ("Adesão ao tratamento e interrupção: conceitos e medição", [
        P("A OMS define a adesão como a medida em que o comportamento da "
          "pessoa, ao tomar a medicação, seguir uma dieta ou mudar o estilo "
          "de vida, corresponde às recomendações acordadas com um "
          "profissional de saúde, e distingue-a do cumprimento porque exige "
          "o acordo do doente {who_adesao2003}. No mesmo documento, a adesão "
          "é explicada por cinco dimensões que interagem: factores sociais e "
          "económicos, factores do sistema e da equipa de saúde, factores da "
          "doença, factores da terapêutica e factores do doente "
          "{who_adesao2003}. Na tuberculose, a má adesão é reconhecida como "
          "uma das principais causas de falência, recaída e resistência "
          "{who_adesao2003}."),
        P("Não existe um padrão de referência para medir a adesão à "
          "terapêutica antituberculosa nem uma definição amplamente aceite "
          "dos seus níveis, e os métodos disponíveis diferem em custo, "
          "fiabilidade e aceitabilidade, sobretudo em contextos de recursos "
          "limitados {valencia2017}. Os registos de rotina têm a vantagem de "
          "existir para todos os doentes e de permitir reconstruir o "
          "percurso do tratamento, e os protocolos nacionais mandam avaliar a "
          "adesão em cada consulta pela revisão do cartão do doente e pela "
          "pergunta sobre as tomas não presenciadas {misau_protocolos2019}. A "
          "fronteira de 90% de doses tomadas tem fundamento clínico: a "
          "adesão igual ou inferior a esse valor foi um factor de risco de "
          "resultado desfavorável numa análise de 3.405 participantes "
          "{imperial2018}, e a falha de mais de 10% das doses associou-se a "
          "resultados desfavoráveis em 81,2% dos doentes de uma coorte "
          "brasileira {ferreira2025}."),
        P("A interrupção tem padrões temporais próprios. Numa revisão "
          "sistemática de 40 estudos de 21 países, em 31 dos 36 que "
          "informavam o momento da perda de seguimento a proporção de doentes "
          "perdidos até aos dois meses foi igual ou superior à esperada, e os "
          "doentes perdidos falharam entre 37% e 77% dos meses-dose de tratamento "
          "previstos {walker2024}. Numa coorte da Letónia, os períodos de "
          "doses falhadas por reacções adversas foram menos frequentes mas "
          "mais longos do que os restantes, com mediana de 15 dias nas "
          "reacções hepatobiliares {dixon2025}."),
        P("Com base nestes elementos, o estudo adopta três definições "
          "operacionais. A adesão é a proporção de dias de tratamento com "
          "dose documentada, por toma observada ou por medicação dispensada "
          "que cobre esse dia, e é adequada quando atinge 90% ou mais. A "
          "interrupção é qualquer período de 14 ou mais dias consecutivos sem "
          "dose documentada, classificada em 14 a 59 dias ou em 60 ou mais "
          "dias. O algoritmo nacional distingue interrupções de menos de duas "
          "semanas, de duas a oito semanas e de dois meses ou mais, manda "
          "prolongar o tratamento no número de doses perdidas nas "
          "interrupções curtas e registar como tratamento pós-perda de "
          "seguimento o doente que regressa depois de dois meses "
          "{misau_protocolos2019}; a categoria de 14 a 59 dias adoptada aqui "
          "reúne a faixa de duas a oito semanas e os poucos dias que a "
          "separam dos dois meses, de modo a que o limiar superior coincida "
          "com a perda de seguimento definida pela OMS {who_surv2024}."),
    ]),
    ("Magnitude e consequências da interrupção do tratamento", [
        P("A taxa global de sucesso do tratamento da tuberculose sensível "
          "manteve-se em 88% na coorte inscrita em 2023 {who_gtb2025}, mas em "
          "África a meta-análise de "
          "26 estudos estimou 79%, com variação entre 53% na Nigéria e 92% na "
          "Etiópia {teferi2021}. Na Namíbia, 3,6% dos 104.203 casos "
          "registados entre 2006 e 2015 foram perdidos para o seguimento, o "
          "que representou um quarto dos maus resultados {kibuule2020}; no "
          "sul da Etiópia, a perda de seguimento ocorreu a uma taxa de 11,26 "
          "por 1.000 pessoas-mês de observação {watumo2022}. A não adesão, "
          "medida de formas diversas, atingiu 21,29% na meta-análise etíope "
          "{zegeye2019}."),
        P("Em Moçambique, os números variam muito com o local e a fonte. O "
          "relatório nacional de 2020 registou 1,7% de perda de seguimento "
          "{misau_pnct2020}, e em Bilene, na província de Gaza, o sucesso "
          "atingiu 95,1% em 3.012 doentes, embora 41,5% não tivessem teste "
          "bacteriológico no diagnóstico e os autores pedissem melhor "
          "qualidade dos dados {osorio2022}. Em Chókwè, apenas 73,2% dos "
          "9.655 doentes com 15 ou mais anos tiveram resultado favorável, "
          "com 82,8% de "
          "co-infecção pelo HIV {nacarapa2020}; em Manhiça, 10% abandonaram o "
          "tratamento {garciabasteiro2016}; e em Ancuabe a perda de "
          "seguimento atingiu 44,9% dos casos novos {wikmanjorgensen2015}. "
          "Nas crianças, a adesão incompleta chegou a 31,3% numa coorte de "
          "Manhiça {lopezvarela2017}, e num estudo de quatro províncias o "
          "resultado sem sucesso foi de 5,6%, com menor risco em Nampula do "
          "que na Cidade de Maputo {mbatemutemba2026}."),
        P("Esta dispersão sugere que o valor nacional pode depender da "
          "qualidade do registo e da forma como se contam os doentes que desaparecem, e "
          "reforça a necessidade de medir a interrupção directamente nas "
          "fichas. As consequências estão bem descritas: a adesão incompleta "
          "atrasa a conversão bacteriológica, mantém a transmissão e aumenta "
          "a falência, a recaída e a resistência {alipanah2018}; a má adesão "
          "prolonga a infecciosidade e aumenta a mortalidade "
          "{gebreweld2018}; e, para os agregados, soma-se a perda de "
          "rendimento aos custos do tratamento {timire2021}."),
    ]),
    ("Determinantes da adesão e da interrupção", [
        P("As cinco dimensões da adesão propostas pela OMS {who_adesao2003} "
          "organizam os determinantes descritos na literatura. Numa revisão "
          "de estudos em pessoas com tuberculose e HIV, as barreiras "
          "incluíram o sexo masculino, as comorbilidades, a doença avançada, "
          "o consumo de álcool e de tabaco, o baixo nível socioeconómico, o "
          "conhecimento limitado, o estigma e as falhas dos serviços, e os "
          "facilitadores incluíram o apoio social, o apoio nutricional, os "
          "lembretes por mensagem, o conhecimento da doença, o TARV "
          "concomitante e uma boa relação com os profissionais {lawal2025}."),
        P("Na dimensão social e económica, a distância e os custos pesam de "
          "forma consistente. No sul da Etiópia, os doentes que viviam a 10 "
          "km ou mais da unidade sanitária tiveram uma razão de riscos "
          "ajustada de perda de seguimento de 6,06, e a idade de 45 ou mais "
          "anos e a falta de apoio familiar também se associaram ao desfecho "
          "{watumo2022}. Na Namíbia, os preditores foram o sexo masculino, a "
          "idade entre 15 e 24 anos, o prestador do tratamento, a fase "
          "intensiva e a residência em regiões fronteiriças ou de trânsito "
          "{kibuule2020}. No Gana, os doentes que abandonaram o tratamento "
          "apontaram a insegurança alimentar, o custo do transporte, a "
          "insegurança de rendimento e a distância {appiah2023}, e, entre os "
          "factores de risco quantificados pela OMS, a subnutrição continua a "
          "ser aquele a que se atribui o maior número de casos novos no mundo, "
          "seguida de perto pela diabetes {who_gtb2025}."),
        P("Nas dimensões do doente e da terapêutica, a percepção de cura e os "
          "efeitos adversos destacam-se. Na Eritreia, «sentir-se curado» foi "
          "a razão mais citada para parar o tratamento, a par do "
          "desconhecimento da duração do tratamento, da perda de emprego, do "
          "estigma e dos efeitos adversos {gebreweld2018}. Na meta-análise "
          "etíope, o esquecimento, o receio dos efeitos adversos, a espera de "
          "uma hora ou mais e a distância percebida como longa associaram-se "
          "à não adesão {zegeye2019}, e na coorte da Letónia 31,0% dos "
          "doentes que falharam doses fizeram-no por reacções adversas "
          "{dixon2025}. Os sintomas depressivos associaram-se fortemente à "
          "perda de seguimento {ruizgrosso2020}."),
        P("Em Moçambique, os doentes de Sofala e Manica descreveram atrasos no "
          "diagnóstico, estigma, esperas longas, ausência de apoio nutricional "
          "e de apoio psicossocial e falta de conhecimento sobre a doença na "
          "comunidade {deschacht2019}. Na Zambézia, o conhecimento sobre os "
          "sintomas e as causas da tuberculose era baixo, crenças "
          "socioculturais levavam a procurar primeiro o médico tradicional e "
          "o estigma e o género influenciavam a procura de cuidados "
          "{give2024}. Os profissionais moçambicanos apontaram dificuldades "
          "na aplicação do tratamento observado e a necessidade de envolver a "
          "família, a comunidade e o Estado {mitano2017}. Nos estudos de "
          "registos, o sexo masculino, a tuberculose recorrente, a "
          "co-infecção pelo HIV, a microbiologia positiva e a ausência de "
          "tratamento observado associaram-se a resultados desfavoráveis "
          "{osorio2022,xavier2026}."),
    ]),
    ("Enquadramento normativo e organização do apoio ao tratamento em "
     "Moçambique", [
        P("O PNCT, integrado na Direcção Nacional de Saúde Pública do MISAU, "
          "orienta a prática clínica pelos protocolos nacionais de avaliação "
          "e manejo dos doentes com tuberculose, e o seu plano estratégico "
          "está alinhado com a estratégia global da OMS. Os protocolos "
          "determinam o tratamento directamente "
          "observado (DOT, do inglês *directly observed treatment*) diário "
          "durante a fase intensiva, a avaliação clínica às duas semanas e "
          "depois mensal, com pesagem e cálculo do índice de massa corporal "
          "(IMC) em cada visita, a pesquisa de sintomas de toxicidade e a "
          "notificação de todas as reacções adversas na ficha própria "
          "{misau_protocolos2019}."),
        P("Perante uma interrupção, os protocolos mandam fazer a busca activa "
          "do doente, investigar os motivos, avaliar o consumo de álcool, a "
          "depressão e os efeitos adversos, reforçar o aconselhamento, "
          "referir para apoio psicossocial e identificar um padrinho, "
          "confidente ou activista comunitário, decidindo a conduta "
          "terapêutica segundo a duração da interrupção "
          "{misau_protocolos2019}. As intervenções comunitárias do programa, "
          "financiadas por parceiros e executadas por organizações de base "
          "comunitária, incluem o rastreio, a educação para a saúde, o apoio "
          "emocional e a busca activa dos faltosos e dos abandonos "
          "{misau_pnct2020}."),
        P("A evidência internacional sustenta este modelo. Numa meta-análise "
          "de 129 estudos, o tratamento auto-administrado teve menor sucesso "
          "do que o DOT, o DOT na comunidade teve mais sucesso e menos perda "
          "de seguimento do que o DOT na unidade sanitária, e o DOT feito por "
          "familiares associou-se a menor adesão do que o feito por "
          "profissionais {alipanah2018}. Noutra meta-análise de ensaios, o "
          "DOT reduziu o abandono em 49%, os incentivos financeiros em 26% e "
          "a educação e o aconselhamento em 13% {muller2018}. As tecnologias "
          "digitais de adesão tiveram um efeito modesto e de certeza muito "
          "baixa sobre o sucesso terapêutico {mohamed2025}. A OMS recomenda "
          "educação e aconselhamento para todos e o apoio ao tratamento na "
          "comunidade ou no domicílio, feito por profissionais ou "
          "leigos formados {who_mod4_2025}."),
        P("O farmacêutico tem nesta organização um papel próprio: assegura a "
          "disponibilidade dos medicamentos, aconselha sobre a toma e os "
          "efeitos adversos e alimenta a farmacovigilância. Numa revisão "
          "sistemática, os serviços de farmácia clínica na tuberculose "
          "associaram-se a taxas de sucesso entre 72% e 93%, mas a evidência "
          "foi considerada inconsistente pela falta de ensaios aleatorizados "
          "{iskandar2023}, o que justifica estudos locais que identifiquem "
          "onde a intervenção farmacêutica pode ser mais útil."),
    ]),
    ("Abordagens metodológicas: registos de rotina, entrevistas e "
     "integração", [
        P("Os estudos com dados de rotina permitem analisar coortes grandes a "
          "baixo custo, mas dependem da completude e da exactidão dos "
          "registos, e o seu relato deve seguir a declaração Strengthening "
          "the Reporting of Observational Studies in Epidemiology (STROBE), "
          "que fixa os itens mínimos do relato de estudos observacionais "
          "{von2007}, e a sua extensão Reporting of "
          "Studies Conducted Using Observational Routinely-Collected Health "
          "Data (RECORD), que exige a descrição da fonte, da validação das "
          "variáveis e do tratamento dos dados em falta {benchimol2015}. Em "
          "Moçambique, a falta de teste bacteriológico em 41,5% dos doentes "
          "de uma coorte distrital ilustra as limitações dos registos "
          "{osorio2022}, pelo que a verificação prévia da fonte e a dupla "
          "extracção são obrigatórias."),
        P("A entrevista individual em profundidade é adequada para explorar "
          "experiências sensíveis, como a decisão de parar a medicação. Numa "
          "revisão sistemática de testes empíricos, a saturação foi atingida "
          "entre 9 e 17 entrevistas, sobretudo em populações homogéneas e com "
          "objectivos delimitados {hennink2022}, e existe um método simples "
          "para a avaliar e relatar, que combina uma base inicial de "
          "entrevistas, uma sequência de entrevistas adicionais e um limiar "
          "de informação nova {guest2020}. A análise temática reflexiva "
          "organiza-se em seis fases, da familiarização com os dados à "
          "redacção {byrne2022}, e a comparação da codificação entre "
          "investigadores pode apoiar a transparência quando usada como "
          "exercício reflexivo {oconnor2020}. O relato segue a lista "
          "Consolidated Criteria for Reporting Qualitative Research (COREQ), "
          "de 32 itens {tong2007}."),
        P("Nos métodos mistos, o valor acrescentado depende da integração, "
          "que pode fazer-se pela amostragem, pela transformação de dados, "
          "por matrizes conjuntas e por uma discussão integrada {murry2023}. "
          "A análise de estudos mistos em serviços de saúde mostrou falta de "
          "justificação do desenho, pouca transparência da componente "
          "qualitativa e integração rara {ocathain2008}; as recomendações "
          "Good Reporting of a Mixed Methods Study (GRAMMS), propostas nesse "
          "trabalho, orientarão o relato deste estudo."),
    ]),
]

# ----------------------------------------------------- 7. estado da arte ----
ESTADO_ARTE = [
    P("O [[quadro:estado_arte]] sintetiza estudos empíricos dos últimos dez "
      "anos sobre a adesão, a interrupção e os resultados do tratamento da "
      "tuberculose, com prioridade para os moçambicanos e africanos, "
      "completados por estudos de outros continentes que mediram as doses "
      "falhadas com rigor."),
    QUADRO("estado_arte",
           "Síntese de estudos sobre adesão, interrupção e resultados do "
           "tratamento da tuberculose (estado da arte)",
           ["Autor (ano)", "Local", "Desenho (n)", "Principais resultados"],
           [
               ["Xavier et al. (2026) {xavier2026}", "Nacarôa, Nampula",
                "Coorte retrospectiva (205)",
                "Resultado desfavorável em 26,8% (55/205); preditores: "
                "tratamento prévio, ausência de tratamento observado, "
                "diagnóstico clínico ou radiológico e baciloscopia positiva."],
               ["Osório et al. (2022) {osorio2022}", "Bilene, Gaza",
                "Coorte retrospectiva (3.012)",
                "Sucesso em 95,1%; resultado desfavorável associado ao sexo "
                "masculino (razão de probabilidades ajustada 1,48), à "
                "recorrência (1,63), ao HIV (2,17) e à microbiologia "
                "positiva (5,27)."],
               ["García-Basteiro et al. (2016) {garciabasteiro2016}",
                "Manhiça, Maputo", "Coorte retrospectiva (1.957)",
                "Óbito durante o tratamento em 15,1% e abandono em 10%; óbito "
                "associado ao HIV (razão de probabilidades 2,73) e ao sexo "
                "masculino (1,39)."],
               ["Nacarapa et al. (2020) {nacarapa2020}", "Chókwè, Gaza",
                "Coorte retrospectiva (9.655)",
                "Resultado favorável em 73,2%; co-infecção pelo HIV em 82,8%; "
                "piores resultados nos que nunca iniciaram o TARV ou o "
                "iniciaram pouco antes do diagnóstico."],
               ["Mbate-Mutemba et al. (2026) {mbatemutemba2026}",
                "Quatro províncias, incluindo Nampula",
                "Coorte retrospectiva de crianças (1.421)",
                "Resultado sem sucesso em 5,6%; menor risco em Nampula face à "
                "Cidade de Maputo (razão de probabilidades ajustada 0,16)."],
               ["Lopez-Varela et al. (2017) {lopezvarela2017}",
                "Manhiça, Maputo", "Coorte de crianças com menos de 3 anos "
                "(50)",
                "Perda de seguimento em 8,0% e adesão incompleta em 31,3%, "
                "associada à desnutrição e à mãe migrante."],
               ["De Schacht et al. (2019) {deschacht2019}", "Sofala e Manica",
                "Qualitativo, 11 grupos focais (51)",
                "Atrasos no diagnóstico, estigma, esperas longas, ausência de "
                "apoio nutricional e psicossocial, conhecimento insuficiente."],
               ["Watumo et al. (2022) {watumo2022}", "Sul da Etiópia",
                "Coorte retrospectiva (402)",
                "37 perdas de seguimento; distância de 10 km ou mais (razão "
                "de riscos ajustada 6,06), idade de 45 ou mais anos (7,71) e "
                "falta de apoio familiar (2,80)."],
               ["Kibuule et al. (2020) {kibuule2020}", "Namíbia",
                "Coorte nacional retrospectiva (104.203)",
                "Perda de seguimento em 3,6%, um quarto dos maus resultados; "
                "preditores: sexo masculino, 15-24 anos, fase intensiva, "
                "regiões fronteiriças."],
               ["Zegeye et al. (2019) {zegeye2019}", "Etiópia",
                "Meta-análise (13 estudos)",
                "Não adesão de 21,29%; esquecimento (razão de probabilidades "
                "3,22), receio de efeitos adversos (1,93), espera de uma hora "
                "ou mais (4,88), distância longa (5,35)."],
               ["Appiah et al. (2023) {appiah2023}", "Ashanti, Gana",
                "Qualitativo, entrevistas (20)",
                "Insegurança alimentar, custo do transporte, falta de apoio "
                "familiar, efeitos adversos e melhoria após a fase intensiva."],
               ["Gebreweld et al. (2018) {gebreweld2018}", "Asmara, Eritreia",
                "Qualitativo, 12 entrevistas e 3 grupos focais",
                "«Sentir-se curado» como principal razão para parar; perda de "
                "emprego, fome, estigma; a proximidade facilitou a adesão."],
               ["Ferreira et al. (2025) {ferreira2025}", "Brasil",
                "Coorte prospectiva (578)",
                "23% falharam mais de 10% das doses; resultado desfavorável "
                "em 81,2% destes, contra 21,6% com adesão completa."],
               ["Dixon et al. (2025) {dixon2025}", "Riga, Letónia",
                "Coorte retrospectiva (174)",
                "31,0% falharam doses por reacções adversas; 20,9% das doses "
                "falhadas deveram-se a reacções, sobretudo hepatobiliares."],
           ],
           larguras=[3.3, 2.4, 3.0, 7.3],
           fonte="Elaboração própria (2026), a partir das fontes citadas."),
    P("A leitura do quadro mostra um padrão recorrente. Os estudos "
      "moçambicanos são sobretudo coortes retrospectivas de registos, "
      "concentradas no sul do país, que usam o resultado final do "
      "tratamento como desfecho e identificam o sexo masculino, a "
      "co-infecção pelo HIV, o tratamento prévio e a ausência de tratamento "
      "observado como preditores. Nenhum mediu a proporção de doses tomadas "
      "nem as interrupções inferiores a dois meses em adultos, e o único "
      "estudo com adultos da província de Nampula decorreu num distrito "
      "rural. Os "
      "estudos qualitativos, dentro e fora do país, convergem num conjunto "
      "de razões para parar a medicação, em que se repetem a sensação de "
      "cura, os efeitos adversos, a fome e o custo do transporte."),
    P("As divergências são igualmente informativas: a perda de seguimento "
      "vai de 3,6% numa coorte nacional a 44,9% num distrito rural "
      "moçambicano, o que reflecte diferenças de contexto mas também de "
      "definição e de qualidade dos registos. Falta, sobretudo, um estudo "
      "que meça a adesão e a interrupção nos mesmos registos e que ouça, no "
      "mesmo contexto urbano, os doentes em tratamento. É esta a lacuna que "
      "o presente estudo preenche para a cidade de Nampula."),
]
ESQUEMA_TEXTO = [
    P("A [[figura:esquema]] representa o modelo conceptual do estudo, "
      "construído sobre as cinco dimensões da adesão {who_adesao2003} e os "
      "determinantes descritos na revisão. Os factores sociodemográficos e "
      "económicos, clínicos, da terapêutica e dos serviços actuam sobre a "
      "adesão e a interrupção do tratamento, que constituem o desfecho. Os "
      "factores registados nas fichas são analisados na componente "
      "quantitativa; os que não constam dos registos, como a fome, o custo "
      "do transporte, o estigma ou a percepção de cura, são explorados nas "
      "entrevistas. O centro de saúde e o período de início do tratamento "
      "são tratados como variáveis de confundimento."),
]
ESQUEMA_TITULO = ("Esquema conceptual dos factores associados à adesão e à "
                  "interrupção do tratamento da tuberculose")
ESQUEMA = {
    "contexto": ("Adultos em tratamento da tuberculose sensível, centros de "
                 "saúde da cidade de Nampula, 2025-2027"),
    "blocos": [
        ("Factores sociodemográficos e económicos",
         ["sexo e idade", "residência e distância ao centro",
          "custo do transporte e perda de rendimento",
          "insegurança alimentar"]),
        ("Factores clínicos e da doença",
         ["categoria do doente (novo ou previamente tratado)",
          "forma e base do diagnóstico", "co-infecção pelo HIV e TARV",
          "estado nutricional (IMC)"]),
        ("Factores da terapêutica",
         ["efeitos adversos", "melhoria precoce dos sintomas",
          "fase do tratamento"]),
        ("Factores dos serviços e do apoio",
         ["modalidade de supervisão (DOT)",
          "aconselhamento e relação com a equipa",
          "disponibilidade de medicamentos",
          "apoio familiar e estigma"]),
    ],
    "desfecho": ("Adesão e interrupção do tratamento",
                 ["adesão adequada (90% ou mais dos dias)",
                  "interrupção de 14 ou mais dias",
                  "perda de seguimento (60 ou mais dias)"]),
    "moderadores": ("Variáveis de confundimento",
                    ["centro de saúde", "trimestre de início do tratamento"]),
}

# ----------------------------------------------------- 8. metodologia -------
METODOLOGIA = [
    ("Tipo e desenho do estudo", [
        P("Trata-se de um estudo de métodos mistos com desenho sequencial "
          "explicativo, em que uma componente quantitativa precede e orienta "
          "uma componente qualitativa e os resultados das duas são "
          "integrados na interpretação {murry2023}. A componente quantitativa "
          "é uma coorte retrospectiva, documental, descritiva e analítica, "
          "que reconstrói o percurso de tratamento de cada adulto a partir do "
          "livro de registo da tuberculose e da ficha de tratamento. A "
          "componente qualitativa é descritiva e interpretativa e usa "
          "entrevistas individuais em profundidade, semi-estruturadas, com "
          "adultos em tratamento."),
        P("O desenho responde à natureza da pergunta. Os registos permitem "
          "quantificar a adesão e as interrupções num número grande de "
          "doentes, com datas e sem viés de memória, mas não contêm as razões "
          "das interrupções, que só os doentes podem relatar. A ligação entre "
          "as componentes faz-se em três pontos: os resultados preliminares "
          "da coorte, em particular a fase e os grupos com mais interrupções, "
          "orientam a selecção intencional dos entrevistados e o "
          "aprofundamento do guião; as duas componentes partilham o quadro das "
          "cinco dimensões da adesão {who_adesao2003}; e os resultados são "
          "reunidos numa matriz conjunta. Os entrevistados não serão as "
          "pessoas da coorte de 2025, que já terão terminado o tratamento, mas "
          "adultos em tratamento nos mesmos centros em 2027, opção cujas "
          "consequências são discutidas nas limitações."),
    ]),
    ("Local e período do estudo", [
        P("O estudo será realizado na cidade de Nampula, capital da província "
          "de Nampula, no norte de Moçambique. Segundo o Instituto Nacional de "
          "Estatística (INE), o distrito da cidade tinha 798.462 habitantes "
          "recenseados em 2017 e era o mais populoso da província {ine2021}. "
          "Os cuidados primários são prestados por centros de saúde públicos "
          "coordenados pelo SDSMAS da Cidade de Nampula, e os que dispõem de "
          "sector de tuberculose iniciam e seguem o tratamento ambulatório. "
          "Serão incluídos todos os centros de saúde da cidade com sector de "
          "tuberculose activo em 2025, cujo número será confirmado antes da "
          "recolha [confirmar junto do SDSMAS da Cidade de Nampula]. Em cada "
          "centro, o doente é inscrito no livro de registo da tuberculose e "
          "acompanhado por uma ficha de tratamento; é também portador de um "
          "cartão de identificação, que a equipa revê nas consultas para "
          "avaliar a adesão {misau_protocolos2019}."),
        P("O estudo decorre de Outubro de 2026 a Setembro de 2027. A coorte "
          "quantitativa inclui os adultos registados entre 1 de Janeiro e 31 "
          "de Dezembro de 2025, com o seguimento documentado até 31 de "
          "Dezembro de 2026. A escolha da coorte de 2025, e não da de 2026, "
          "garante que todos os doentes, incluindo os que iniciaram o "
          "tratamento em Dezembro e os que o prolongaram por doses perdidas, "
          "tenham resultado final registado quando os arquivos forem "
          "consultados, em Março e Abril de 2027, depois da aprovação ética. "
          "As entrevistas decorrerão em Maio e Junho de 2027."),
    ]),
    ("População e unidade de análise", [
        P("Na componente quantitativa, a população-alvo são os adultos "
          "tratados por tuberculose sensível nos centros de saúde da cidade "
          "de Nampula, e a população de estudo são os adultos com 18 ou mais "
          "anos registados para tratamento de primeira linha nesses centros em "
          "2025. A unidade de análise é o episódio de tratamento, isto é, o "
          "período entre o início do tratamento e o resultado final. Quando a "
          "mesma pessoa tiver mais de um registo no período, por reinício "
          "após perda de seguimento ou por transferência entre centros "
          "incluídos, os registos serão ligados no momento da extracção, pela "
          "comparação do nome, da idade, do sexo e do endereço no livro, sem "
          "que estes dados passem para a ficha. Entra na análise apenas o "
          "primeiro episódio, e o reinício é registado como variável; o "
          "episódio transferido entre centros incluídos é analisado no centro "
          "de origem, reunindo as duas fichas."),
        P("Na componente qualitativa, a população são os adultos em "
          "tratamento da tuberculose sensível nos centros incluídos durante o "
          "período das entrevistas, e a unidade de análise é o participante, "
          "cujo relato é tratado como um caso."),
    ]),
    ("Amostra e cálculo do tamanho da amostra", [
        H3("Componente quantitativa"),
        P("A amostragem será aleatória estratificada por centro de saúde, "
          "com afectação proporcional ao número de adultos registados em 2025 "
          "em cada centro. Dentro de cada centro, os registos serão "
          "seleccionados por amostragem sistemática no livro, com intervalo "
          "igual ao número de registos elegíveis do centro dividido pelo "
          "número a seleccionar e início aleatório. O tamanho mínimo foi "
          "calculado para dois fins, a precisão da proporção de adultos com "
          "interrupção (objectivo específico 2) e o poder da análise de "
          "associação (objectivo específico 3), prevalecendo o maior "
          "{serdar2021}. Para a precisão, usa-se a fórmula da proporção "
          "única:"),
        FORMULA("n<sub>0</sub> = Z<sup>2</sup> × p × (1 - p) / d<sup>2</sup>"),
        P("Em que Z = 1,96 corresponde ao nível de confiança de 95%; p é a "
          "proporção esperada de adultos com pelo menos uma interrupção de 14 "
          "ou mais dias, fixada em 0,5 porque nenhum estudo mediu esta "
          "proporção em Nampula e este valor maximiza a amostra; e d = 0,05 é "
          "a margem de erro absoluta. A substituição dá:"),
        FORMULA("n<sub>0</sub> = 1,96<sup>2</sup> × 0,5 × 0,5 / "
                "0,05<sup>2</sup> = 384,16, arredondado para 385"),
        P("Os doentes do mesmo centro partilham a organização do serviço, a "
          "modalidade de supervisão e, muitas vezes, as condições do bairro, "
          "o que cria correlação entre as observações. Por prudência, "
          "aplica-se um efeito de desenho de 1,5, obtendo n<sub>1</sub> = 385 "
          "× 1,5 = 577,5, arredondado para 578. Prevendo que 10% dos registos "
          "seleccionados não tenham ficha localizável ou legível, o tamanho "
          "para uma população muito grande é 578 / 0,90 = 642,2, isto é, 643 "
          "registos. Como o número de adultos elegíveis (N) é finito, "
          "aplica-se a correcção para população finita, seguida da mesma "
          "margem de 10%:"),
        FORMULA("n<sub>c</sub> = n<sub>1</sub> / [1 + (n<sub>1</sub> - 1) / "
                "N]"),
        P("Para o poder, a comparação de duas proporções com nível de "
          "significância de 5% e poder de 80% exige, por grupo:"),
        FORMULA("n = [Z<sub>1-α/2</sub> × √(2 × p<sub>m</sub> × "
                "q<sub>m</sub>) + Z<sub>1-β</sub> × √(p<sub>1</sub> × "
                "q<sub>1</sub> + p<sub>2</sub> × q<sub>2</sub>)]<sup>2</sup> "
                "/ (p<sub>1</sub> - p<sub>2</sub>)<sup>2</sup>"),
        P("Assume-se uma diferença de 10 pontos percentuais entre dois grupos "
          "de dimensão semelhante, como homens e mulheres (p<sub>1</sub> = "
          "0,25 e p<sub>2</sub> = 0,15), considerada relevante para o "
          "programa, com uma proporção média p<sub>m</sub> = 0,20, próxima da "
          "não adesão agregada de 21,29% estimada na Etiópia {zegeye2019}; "
          "q = 1 - p, Z<sub>1-α/2</sub> = 1,96 e Z<sub>1-β</sub> = 0,84. A "
          "substituição dá:"),
        FORMULA("n = (1,109 + 0,471)<sup>2</sup> / 0,10<sup>2</sup> = 249,7, "
                "arredondado para 250 por grupo"),
        P("São necessários 500 registos analisáveis, ou 556 registos "
          "seleccionados com a margem de 10% (500 / 0,90 = 555,6). Com 500 "
          "registos e uma proporção de interrupção próxima de 20%, esperam-se "
          "cerca de 100 eventos, o que permite até dez parâmetros no modelo "
          "multivariável, segundo a regra de pelo menos dez eventos por "
          "variável {peduzzi1996}. Nas comparações entre grupos desiguais, "
          "como doentes com e sem co-infecção pelo HIV, que representaram 27% "
          "dos doentes no país em 2020 {misau_pnct2020}, o poder será "
          "inferior a 80%, o que será declarado."),
        P("A regra de decisão é a seguinte: se N for igual ou inferior a 700, "
          "serão incluídos todos os registos elegíveis (censo); se for "
          "superior, recolhe-se o maior de dois valores, o de precisão "
          "corrigido para N ou o de poder (556). A [[tabela:cenarios]] "
          "apresenta os cenários, a confirmar com o número real de registos "
          "de 2025 [confirmar junto do SDSMAS da Cidade de Nampula]."),
        TABELA("cenarios",
               "Tamanho da amostra da componente quantitativa segundo o "
               "número de adultos elegíveis registados em 2025",
               ["N (registos elegíveis)",
                "n para a precisão (correcção finita e 10% de perdas)",
                "n mínimo para o poder", "n a recolher"],
               [["600", "328", "556", "Censo (600)"],
                ["700", "353", "556", "Censo (700)"],
                ["1.000", "408", "556", "556"],
                ["2.000", "499", "556", "556"],
                ["3.000", "539", "556", "556"],
                ["5.000", "576", "556", "576"],
                ["10.000", "608", "556", "608"],
                ["Muito grande", "643", "556", "643"]],
               larguras=[3.6, 5.2, 3.4, 3.8],
               fonte="Elaboração própria (2026). Efeito de desenho de 1,5 "
                     "aplicado antes da correcção para população finita."),
        H3("Componente qualitativa"),
        P("Os participantes serão seleccionados por amostragem intencional de "
          "variação máxima, em dois grupos: o grupo A, de adultos com pelo "
          "menos uma interrupção de 14 ou mais dias no tratamento actual ou "
          "que o reiniciaram depois de uma perda de seguimento; e o grupo B, "
          "de adultos sem interrupção e com pelo menos dois meses de "
          "tratamento, que já passaram pela transição para a fase de "
          "manutenção. Dentro de cada grupo procurar-se-á diversidade de "
          "sexo, idade, estado serológico para o HIV, fase do tratamento, "
          "distância ao centro e centro de saúde, e serão sobre-representados "
          "os perfis que a componente quantitativa identificar como de maior "
          "risco."),
        P("Prevêem-se 10 a 12 entrevistas por grupo, num total de 20 a 24, "
          "com um mínimo de seis por grupo. O número apoia-se na revisão que "
          "encontrou saturação entre 9 e 17 entrevistas {hennink2022}, "
          "aumentado porque a população inclui dois grupos com experiências "
          "distintas. A saturação será avaliada em cada grupo pelo método de "
          "Guest e colaboradores {guest2020}, com os parâmetros seguintes, "
          "fixados neste protocolo: base de seis entrevistas, sequências de "
          "três entrevistas e limiar de informação nova de 5%. A recolha "
          "termina num grupo quando uma sequência de três entrevistas "
          "acrescentar 5% ou menos de códigos novos em relação aos códigos "
          "da base."),
    ]),
    ("Critérios de inclusão e de exclusão", [
        H3("Componente quantitativa: critérios de inclusão"),
        LISTA(["Idade igual ou superior a 18 anos à data do registo;",
               "Tuberculose sensível, ou sem resistência à rifampicina "
               "conhecida no início, em qualquer forma e categoria;",
               "Registo no livro da tuberculose de um centro incluído entre 1 "
               "de Janeiro e 31 de Dezembro de 2025, com início do regime de "
               "primeira linha nesse centro;",
               "Ficha de tratamento localizada no arquivo do centro."]),
        H3("Componente quantitativa: critérios de exclusão"),
        LISTA(["Resistência à rifampicina diagnosticada antes do início ou "
               "início directo de regime de segunda linha;",
               "Transferência de outra unidade sanitária com o tratamento já "
               "iniciado, cujas primeiras semanas não estão documentadas no "
               "centro;",
               "Ficha não encontrada após duas buscas em dias diferentes, "
               "contabilizada como perda."]),
        H3("Componente qualitativa: critérios de inclusão"),
        LISTA(["Idade igual ou superior a 18 anos;",
               "Tratamento da tuberculose sensível em curso num centro "
               "incluído, há pelo menos quatro semanas;",
               "Capacidade de comunicar em português ou em Emakhuwa;",
               "Consentimento livre e esclarecido, incluindo para a gravação "
               "áudio."]),
        H3("Componente qualitativa: critérios de exclusão"),
        LISTA(["Estado clínico grave ou sofrimento que desaconselhe a "
               "entrevista no momento, segundo o clínico do sector;",
               "Défice cognitivo ou de comunicação que impeça a entrevista;",
               "Participação no pré-teste do guião."]),
    ]),
    ("Variáveis e definições operacionais", [
        P("O [[quadro:variaveis]] apresenta as variáveis, o seu tipo, a "
          "definição operacional com as categorias e o objectivo específico "
          "a que respondem. As variáveis independentes seguem o esquema "
          "conceptual e limitam-se às que os registos de rotina contêm; as "
          "dimensões que os registos não captam entram como domínios da "
          "componente qualitativa."),
        QUADRO("variaveis", "Variáveis do estudo e definições operacionais",
               ["Variável", "Tipo", "Definição operacional e categorias",
                "Objectivo"],
               [
                   ["Sexo", "Independente, nominal",
                    "Masculino; feminino, segundo o livro", "1, 3"],
                   ["Idade", "Independente, quantitativa",
                    "Anos completos no registo; grupos 18-24, 25-34, 35-44, "
                    "45-54 e 55 ou mais", "1, 3"],
                   ["Residência", "Independente, nominal",
                    "Bairro dentro ou fora da área de referência do centro; "
                    "não registado", "1, 3"],
                   ["Contacto telefónico registado", "Independente, "
                    "dicotómica", "Sim; não (telemóvel do doente ou do "
                    "confidente anotado)", "1, 3"],
                   ["Categoria do doente", "Independente, nominal",
                    "Caso novo; recaída; tratamento pós-perda de seguimento; "
                    "outro previamente tratado", "1, 3"],
                   ["Forma e base do diagnóstico", "Independente, nominal",
                    "Pulmonar bacteriologicamente confirmada; pulmonar "
                    "clinicamente diagnosticada; extrapulmonar", "1, 3"],
                   ["Estado serológico para o HIV", "Independente, nominal",
                    "Negativo; positivo em TARV; positivo sem registo de "
                    "TARV; desconhecido", "1, 3"],
                   ["IMC inicial", "Independente, quantitativa",
                    "Peso em quilogramas dividido pelo quadrado da altura em "
                    "metros; baixo peso se inferior a 18,5; não registado",
                    "1, 3"],
                   ["Modalidade de supervisão", "Independente, nominal",
                    "Em cada fase: DOT na unidade sanitária; DOT na "
                    "comunidade por activista ou confidente; DOT por "
                    "familiar; auto-administrado; não registado", "1, 3"],
                   ["Efeitos adversos registados", "Independente, "
                    "dicotómica", "Sim, se anotados na ficha ou notificados "
                    "(hepáticos, neurológicos, gastrointestinais, cutâneos, "
                    "outros); não", "1, 3"],
                   ["Apoio nutricional registado", "Independente, "
                    "dicotómica", "Sim; não", "1, 3"],
                   ["Centro e trimestre de início", "Confundimento, nominal",
                    "Código do centro; trimestre de 2025", "3"],
                   ["Adesão documentada", "Dependente, quantitativa e "
                    "dicotómica", "Dias com dose documentada (toma observada "
                    "ou medicação dispensada que cobre o dia) sobre os dias "
                    "de tratamento previstos até ao resultado, vezes 100; "
                    "adequada se 90% ou mais, inadequada se inferior a 90%",
                    "2"],
                   ["Interrupção do tratamento", "Dependente, dicotómica",
                    "Pelo menos um período de 14 ou mais dias consecutivos "
                    "sem dose documentada; sim; não", "2, 3"],
                   ["Duração do maior período sem dose documentada",
                    "Dependente, ordinal",
                    "Menos de 14 dias (doses isoladas, não classificado como "
                    "interrupção); 14-59 dias; 60 ou mais dias", "2"],
                   ["Fase da primeira interrupção", "Dependente, nominal",
                    "Intensiva (primeiros 60 dias); manutenção", "2"],
                   ["Tempo até à primeira interrupção", "Dependente, "
                    "quantitativa", "Dias desde o início até ao primeiro dia "
                    "sem dose do período de interrupção; censura no fim do "
                    "tratamento, óbito, transferência ou mudança de regime",
                    "2, 3"],
                   ["Perda de seguimento", "Dependente, dicotómica",
                    "Interrupção de dois meses consecutivos ou mais, segundo "
                    "a OMS; sim; não", "2, 3"],
                   ["Resultado do tratamento", "Descritiva, nominal",
                    "Curado; tratamento completo; falência; óbito; perda de "
                    "seguimento; não avaliado, incluindo transferido para "
                    "fora", "1, 2"],
                   ["Razões da interrupção e facilitadores", "Qualitativa, "
                    "temas", "Percepções sobre a doença e a cura; efeitos "
                    "adversos; alimentação e custos; transporte e distância; "
                    "apoio familiar e estigma; relação com os serviços e "
                    "disponibilidade de medicamentos", "4"],
                   ["Características dos entrevistados", "Descritiva",
                    "Idade, sexo, escolaridade, ocupação, tempo e custo de "
                    "deslocação, fase do tratamento, grupo A ou B", "4"],
               ],
               larguras=[3.4, 2.8, 8.0, 1.8]),
    ]),
    ("Instrumentos de recolha de dados e respectivas fontes", [
        P("A componente quantitativa usa uma ficha de extracção (Apêndice A), "
          "construída a partir dos campos do livro de registo e da ficha de "
          "tratamento, das definições da OMS {who_surv2024} e do algoritmo "
          "nacional de manejo das interrupções {misau_protocolos2019}. A "
          "ficha tem sete secções: identificação codificada do registo, dados "
          "sociodemográficos, dados clínicos, tratamento e supervisão, "
          "calendário de doses e interrupções, resultado do tratamento e "
          "controlo de qualidade. Não contém nome, endereço completo, número "
          "de telefone nem número do processo. Será programada numa aplicação "
          "de recolha electrónica de acesso livre, o KoboToolbox, em "
          "telemóvel, com validação de intervalos e de datas e funcionamento "
          "sem rede, havendo versão em papel como reserva."),
        P("A componente qualitativa usa um guião de entrevista "
          "semi-estruturada (Apêndice B), com uma parte breve de "
          "caracterização do participante e onze perguntas abertas com "
          "sugestões de aprofundamento. As perguntas foram construídas a "
          "partir das cinco dimensões da adesão {who_adesao2003} e das "
          "barreiras descritas em estudos moçambicanos e africanos "
          "{deschacht2019,appiah2023,gebreweld2018}, e não reproduzem itens "
          "de escalas validadas. Completam o instrumento um caderno de notas "
          "de campo, um diário reflexivo do investigador e dois gravadores "
          "digitais."),
        P("A validade de conteúdo dos dois instrumentos será avaliada por um "
          "painel de cinco peritos (dois profissionais do sector de "
          "tuberculose, um farmacêutico, um epidemiologista e um investigador "
          "com experiência qualitativa), que classificarão a relevância e a "
          "clareza de cada item numa escala de 1 a 4. Calcula-se o índice de "
          "validade de conteúdo (IVC) de cada item, exigindo 0,80 ou mais, e "
          "os itens abaixo deste valor serão revistos. O guião, a folha de "
          "informação e o termo de consentimento serão traduzidos para "
          "Emakhuwa por um tradutor e retrovertidos para português por outro, "
          "independente, com reconciliação das diferenças. O guião será "
          "pré-testado em duas entrevistas com doentes que não integrarão a "
          "amostra, cerca de 10% do número previsto, para ajustar a "
          "linguagem, a ordem das perguntas e a duração."),
        P("As fontes de dados são secundárias na componente quantitativa (o "
          "livro de registo da tuberculose e a ficha de tratamento de cada "
          "centro) e primárias na componente qualitativa (os relatos dos "
          "participantes)."),
    ]),
    ("Procedimentos de recolha de dados e controlo de qualidade", [
        H3("Componente quantitativa"),
        P("Depois das aprovações, o investigador e um assistente de "
          "investigação, finalista de Farmácia, receberão um dia de formação "
          "sobre as definições, a ficha e a confidencialidade. Antes da "
          "recolha, faz-se a verificação prévia da fonte em 30 registos de "
          "2025, dez em cada um de três centros de dimensão diferente, "
          "medindo a proporção de preenchimento de cada variável. Aplicam-se "
          "regras de decisão escritas: uma variável preenchida em menos de "
          "60% dos registos sai do modelo multivariável e mantém-se apenas na "
          "descrição; se a ficha permitir reconstruir as tomas diárias em 60% "
          "ou mais dos registos, a adesão é calculada pelas tomas; se não, "
          "calcula-se pelos dias cobertos pela medicação dispensada; e, se "
          "nenhuma das duas formas for possível em 60% dos registos, os "
          "objectivos específicos 2 e 3 passam a usar apenas a perda de "
          "seguimento e as datas das consultas, alteração que será comunicada "
          "ao Comité Institucional de Bioética para a Saúde da Universidade "
          "Lúrio (CIBS-UniLúrio) como emenda."),
        P("A recolha segue a lista de amostragem de cada centro. Para cada "
          "registo seleccionado, o extractor localiza a ficha, atribui um "
          "código (centro e número sequencial) e preenche a ficha "
          "electrónica; a lista que liga o código ao número do livro fica "
          "apenas com o investigador, guardada em separado, e é destruída "
          "após o controlo de qualidade. A extracção de 10% dos registos "
          "(cerca de 56), escolhidos aleatoriamente, será repetida de forma "
          "independente pelo membro da equipa que não os extraiu. A "
          "concordância será medida pelo kappa de Cohen nas variáveis "
          "categóricas, com meta de 0,80 ou mais, e pela diferença absoluta "
          "na adesão, aceitável até 5 pontos percentuais; uma variável com "
          "kappa inferior a 0,60 será reextraída em todos os registos, e as "
          "discordâncias serão resolvidas por consulta da fonte. O "
          "investigador revê semanalmente a completude e a coerência das "
          "datas."),
        H3("Componente qualitativa"),
        P("Os candidatos serão identificados pelo profissional responsável "
          "pelo sector de tuberculose, a partir das fichas dos doentes em "
          "tratamento e segundo os critérios de cada grupo, e abordados por "
          "este no dia da consulta ou do levantamento da medicação, para "
          "evitar deslocações adicionais. Quem aceitar ouvir a proposta será "
          "apresentado ao investigador, que lerá a folha de informação "
          "(Apêndice C) em português ou em Emakhuwa e obterá o consentimento "
          "(Apêndice D). As entrevistas decorrerão numa sala reservada do "
          "centro, depois da consulta, com duração prevista de 40 a 60 "
          "minutos, e serão conduzidas pelo investigador com um assistente "
          "fluente em Emakhuwa, que não pertence à equipa do centro, e "
          "gravadas em áudio."),
        P("No fim de cada entrevista, o entrevistador resume ao participante "
          "as ideias principais e pede-lhe que as confirme ou corrija. As "
          "notas de campo e o diário reflexivo são escritos no mesmo dia. As "
          "gravações serão transcritas na íntegra nas 72 horas seguintes; os "
          "trechos em Emakhuwa serão traduzidos para português pelo "
          "assistente e 20% das traduções serão verificadas por um segundo "
          "tradutor. As transcrições serão anonimizadas, substituindo nomes "
          "de pessoas, de bairros e de centros por códigos, e a matriz de "
          "saturação é actualizada depois de cada entrevista. Cada "
          "participante receberá 300 meticais para o transporte e um lanche, "
          "valor que compensa a deslocação e o tempo sem constituir incentivo "
          "indevido."),
    ]),
    ("Processamento e análise dos dados", [
        H3("Componente quantitativa"),
        P("Os dados serão exportados da aplicação para o programa Statistical "
          "Package for the Social Sciences (SPSS), versão 26 ou superior, e "
          "para o R, de acesso livre, onde serão limpos e verificados quanto a "
          "valores fora de intervalo e a datas incoerentes. A análise "
          "descritiva (objectivo específico 1) usa frequências absolutas e "
          "relativas, médias e desvios-padrão ou medianas e intervalos "
          "interquartis, conforme a distribuição. Para o objectivo específico "
          "2, estimam-se a mediana da adesão documentada e as proporções de "
          "adultos com adesão adequada, com pelo menos uma interrupção de 14 "
          "ou mais dias e com perda de seguimento, com intervalo de confiança "
          "a 95% (IC95%) pelo método de Wilson, bem como a distribuição das "
          "interrupções por duração e por fase e a curva de Kaplan-Meier do "
          "tempo até à primeira interrupção. A hipótese sobre as fases é "
          "testada pela comparação das taxas de início de interrupções por "
          "1.000 pessoas-dia na fase intensiva e na de manutenção, por "
          "regressão de Poisson, com a razão de taxas e o IC95%."),
        P("Para o objectivo específico 3, a análise bivariada usa o teste do "
          "qui-quadrado ou o teste exacto de Fisher e o teste de log-rank. O "
          "modelo principal é a regressão de riscos proporcionais de Cox para "
          "o tempo até à primeira interrupção de 14 ou mais dias, com censura "
          "no fim do tratamento, no óbito, na transferência para fora ou na "
          "mudança para regime de segunda linha. Entram no modelo as "
          "variáveis com p inferior a 0,20 na análise bivariada e, por "
          "decisão prévia, o sexo, a idade e o estado serológico para o HIV, "
          "sem ultrapassar dez parâmetros. A correlação entre doentes do "
          "mesmo centro é tratada por variância robusta agrupada por centro, "
          "no pacote survival do R; a proporcionalidade dos riscos será "
          "verificada pelos resíduos de Schoenfeld e a colinearidade pelo "
          "factor de inflação da variância, que deve ser inferior a 5. Os "
          "resultados serão apresentados como razões de riscos instantâneos "
          "brutas e ajustadas com IC95%, com nível de significância de 5% "
          "(p<0,05)."),
        P("Em análise de sensibilidade, o modelo é repetido com a perda de "
          "seguimento como desfecho. Os dados em falta serão descritos por "
          "variável, e a análise principal usará os casos completos. O relato "
          "seguirá a declaração STROBE {von2007} e a sua extensão RECORD "
          "{benchimol2015}."),
        H3("Componente qualitativa"),
        P("As transcrições serão analisadas por análise temática reflexiva, "
          "nas seis fases de familiarização, codificação, construção de temas "
          "candidatos, revisão, definição e denominação dos temas e redacção "
          "{byrne2022}, combinando um quadro inicial de códigos derivado das "
          "cinco dimensões da adesão {who_adesao2003} com códigos indutivos "
          "que emergem dos dados. A codificação será feita no programa de "
          "acesso livre Taguette. O investigador e o orientador codificarão "
          "de forma independente as quatro primeiras transcrições, cerca de "
          "20% do total previsto, e compararão as codificações; a percentagem "
          "de concordância será relatada como exercício de transparência, e "
          "as divergências serão discutidas para refinar o livro de códigos "
          "{oconnor2020}."),
        P("A credibilidade será reforçada pela comparação entre os grupos A e "
          "B e com os dados quantitativos, pela confirmação dos resumos com "
          "os participantes, pelo registo das decisões analíticas e pelo "
          "diário reflexivo. Os resultados serão apresentados por temas, com "
          "citações identificadas por código, sexo, idade e fase do "
          "tratamento, e o relato seguirá a lista COREQ {tong2007}."),
        H3("Integração das duas componentes"),
        P("A integração faz-se numa matriz conjunta que coloca, para cada "
          "resultado quantitativo relevante, como a fase com maior taxa de "
          "interrupções ou um factor associado, os temas qualitativos "
          "correspondentes e a meta-inferência, classificada como "
          "confirmação, expansão ou discordância {murry2023}. As "
          "discordâncias serão discutidas e não eliminadas, e o relato do "
          "conjunto seguirá as recomendações GRAMMS {ocathain2008}."),
    ]),
    ("Limitações do estudo e estratégias de mitigação", [
        P("O [[quadro:limitacoes]] apresenta as limitações previstas, as suas "
          "consequências e as estratégias adoptadas para as reduzir. As mais "
          "relevantes decorrem do uso de registos de rotina, que não foram "
          "concebidos para investigação, e da opção de entrevistar doentes "
          "diferentes dos da coorte."),
        QUADRO("limitacoes", "Limitações previstas e estratégias de mitigação",
               ["Limitação", "Consequência", "Mitigação"],
               [
                   ["Registos incompletos, ilegíveis ou com datas em falta",
                    "Viés de informação e perda de variáveis ou de registos",
                    "Verificação prévia de 30 registos com regras escritas, "
                    "dupla extracção de 10%, margem de 10% na amostra e "
                    "descrição dos dados em falta"],
                   ["Fichas que registam dispensas e não tomas na fase de "
                    "manutenção",
                    "Adesão sobrestimada, porque a medicação levantada não é "
                    "necessariamente tomada",
                    "Designação da medida como adesão documentada, leitura "
                    "como limite superior e confronto com as entrevistas"],
                   ["Ausência nos registos de rendimento, alimentação, "
                    "álcool ou depressão",
                    "Confundimento residual no modelo multivariável",
                    "Exploração destes factores nas entrevistas e declaração "
                    "explícita na discussão"],
                   ["Entrevistados diferentes da coorte de 2025",
                    "Integração feita ao nível dos padrões e não das pessoas",
                    "Selecção orientada pelos resultados quantitativos, nos "
                    "mesmos centros, e discussão explícita da opção"],
                   ["Doentes que abandonaram definitivamente não são "
                    "encontrados no centro",
                    "Sub-representação de quem não regressou",
                    "Inclusão de doentes que retomaram o tratamento após "
                    "interrupção e reconhecimento do limite"],
                   ["Desejabilidade social nas entrevistas feitas no centro",
                    "Subnotificação de interrupções e de críticas aos "
                    "serviços",
                    "Entrevistador externo à equipa do centro, sala "
                    "reservada, confidencialidade e ausência de efeito no "
                    "atendimento"],
                   ["Tradução entre Emakhuwa e português",
                    "Perda ou alteração de sentido",
                    "Tradução e retroversão do guião, assistente fluente e "
                    "verificação de 20% das traduções"],
                   ["Poucos eventos ou grupos de dimensão desigual",
                    "Poder inferior a 80% em algumas comparações",
                    "Limite de dez parâmetros, análise de sensibilidade e "
                    "declaração do poder alcançado"],
                   ["Estudo restrito a centros de saúde urbanos",
                    "Generalização limitada a hospitais e a distritos rurais",
                    "Descrição detalhada do contexto para apoiar a "
                    "transferibilidade"],
               ],
               larguras=[5.0, 4.6, 6.4]),
    ]),
    ("Considerações éticas", [
        P("O estudo respeitará os princípios da Declaração de Helsínquia da "
          "Associação Médica Mundial, na revisão de 2024 {wma2025}. O "
          "protocolo será submetido ao CIBS-UniLúrio e, se este o determinar, "
          "ao Comité Nacional de Bioética para a Saúde (CNBS), e a recolha só "
          "começará depois do parecer favorável e das autorizações da "
          "Direcção Provincial de Saúde de Nampula, do SDSMAS da Cidade de "
          "Nampula e da direcção de cada centro de saúde (Apêndice F). Serão "
          "adoptadas as salvaguardas seguintes:"),
        LISTA([
            "Dispensa de consentimento na componente documental: será pedida "
            "ao comité (Apêndice E), porque o estudo é retrospectivo, de "
            "risco mínimo e sem contacto com os doentes, e porque contactar "
            "os adultos de 2025, muitos já sem seguimento, transferidos ou "
            "falecidos, seria impraticável; a ficha não contém "
            "identificadores e a lista de correspondência será destruída "
            "após o controlo de qualidade.",
            "Consentimento na componente qualitativa: a participação é "
            "voluntária e precedida da leitura da folha de informação em "
            "português ou em Emakhuwa; quem não souber ler nem escrever dará "
            "o consentimento por impressão digital, na presença de uma "
            "testemunha imparcial; a gravação áudio exige consentimento "
            "específico, e o participante pode recusar perguntas ou desistir "
            "a qualquer momento, sem efeito no seu tratamento.",
            "Confidencialidade reforçada: o diagnóstico de tuberculose e o "
            "estado serológico para o HIV são informação estigmatizante, pelo "
            "que se usam códigos em vez de nomes; o convite é feito em "
            "privado e a entrevista decorre numa sala reservada que não "
            "identifique o participante como doente de tuberculose; o estado "
            "serológico só é registado se o próprio o quiser informar e nunca "
            "é revelado a familiares, acompanhantes ou empregadores; os "
            "ficheiros áudio ficam em computador protegido por palavra-passe "
            "e são apagados após a validação das transcrições; as "
            "transcrições anonimizadas e as bases de dados são guardadas "
            "durante cinco anos, com acesso restrito à equipa, e os "
            "resultados são publicados de forma agregada, sem citações que "
            "permitam reconhecer a pessoa.",
            "Riscos e benefícios: o risco principal é o desconforto ao falar "
            "da doença, do estigma ou de uma interrupção; o entrevistador, "
            "formado para o efeito, pode suspender a entrevista e não emitirá "
            "juízos. Não há benefício directo além do reembolso do transporte "
            "e do lanche; o benefício esperado é colectivo, pela melhoria do "
            "apoio aos doentes.",
            "Via de referenciação: quando o participante relatar uma "
            "interrupção em curso, sinais de reacção adversa, falta de "
            "alimentos ou sofrimento psicológico, será encaminhado, com o seu "
            "acordo, para o clínico do sector de tuberculose, para o apoio "
            "psicossocial do centro ou para os serviços de acção social, sem "
            "que a informação seja usada para qualquer sanção.",
            "Devolução não punitiva: os resultados de cada centro serão "
            "entregues apenas à respectiva direcção e ao SDSMAS, para "
            "melhoria dos serviços, e os relatórios públicos não "
            "identificarão centros nem profissionais.",
            "Independência: nenhum membro da equipa de recolha pertence às "
            "equipas dos centros estudados, e a equipa declara não ter "
            "conflitos de interesse.",
        ]),
    ]),
]

# ----------------------------------------------------- 9 e 10 ---------------
RESULTADOS_ESPERADOS = [
    P("Os resultados esperados correspondem, pela mesma ordem, aos "
      "objectivos específicos. Não se antecipam valores, mas a literatura "
      "citada permite indicar a direcção provável de alguns achados e a "
      "utilidade de cada um."),
    LISTA([
        "Perfil dos adultos tratados em 2025 (objectivo específico 1): "
        "espera-se uma coorte com mais homens do que mulheres, como na "
        "distribuição mundial da doença {who_gtb2025}, e com uma fracção "
        "relevante de co-infecção pelo HIV, próxima dos 27% registados no "
        "país {misau_pnct2020}; a descrição da modalidade de supervisão "
        "efectivamente registada informará o SDSMAS sobre a cobertura real "
        "do DOT.",
        "Adesão e interrupções (objectivo específico 2): espera-se uma "
        "proporção de adultos com interrupção de 14 ou mais dias superior à "
        "perda de seguimento de 1,7% dos relatórios nacionais "
        "{misau_pnct2020}, e uma concentração das interrupções nos dois "
        "primeiros meses ou na passagem para a fase de manutenção "
        "{walker2024,appiah2023}; o resultado indicará o momento em que o "
        "aconselhamento farmacêutico e a busca activa devem ser reforçados.",
        "Factores associados (objectivo específico 3): espera-se associação "
        "da interrupção com o sexo masculino, o tratamento prévio, a "
        "co-infecção pelo HIV e a ausência de tratamento observado, como nos "
        "estudos moçambicanos {osorio2022,xavier2026}; o resultado permitirá "
        "definir critérios simples de risco para seguimento reforçado desde "
        "a primeira consulta.",
        "Razões e facilitadores (objectivo específico 4): espera-se que a "
        "sensação de cura, os efeitos adversos, a fome, o custo do "
        "transporte, o estigma e a espera nos serviços surjam como razões, e "
        "o apoio familiar e a boa relação com a equipa como facilitadores "
        "{gebreweld2018,appiah2023,deschacht2019}, a par de razões próprias "
        "do contexto de Nampula; o resultado orientará o conteúdo do "
        "aconselhamento e do apoio social.",
    ], numerada=True),
    P("Da integração resultará uma matriz que junta, para cada padrão de "
      "interrupção, as razões que o explicam e uma proposta de resposta, "
      "como o aconselhamento na transição de fase, a farmacovigilância "
      "activa, a prioridade no apoio nutricional ou o contacto telefónico "
      "precoce dos faltosos, a apresentar às direcções dos centros, ao "
      "SDSMAS e ao PNCT."),
]
DIVULGACAO = [
    P("Os resultados serão divulgados de forma a chegar à comunidade "
      "académica, aos serviços e aos doentes. O trabalho será defendido "
      "publicamente perante um júri da Faculdade de Ciências de Saúde da "
      "Universidade Lúrio. Será entregue um relatório técnico à Direcção "
      "Provincial de Saúde de Nampula, ao SDSMAS da Cidade de Nampula e à "
      "direcção de cada centro, com os resultados agregados e, para cada "
      "centro, os seus próprios indicadores, numa perspectiva de melhoria e "
      "não de avaliação individual, e será organizada uma sessão de "
      "devolução com as equipas dos sectores de tuberculose e de farmácia e "
      "com os activistas comunitários."),
    P("Será preparado um artigo para uma revista com revisão por pares e "
      "acesso aberto, seguindo as normas STROBE e RECORD, COREQ e GRAMMS, e os "
      "resultados serão apresentados nas jornadas científicas da "
      "Universidade Lúrio e noutros encontros nacionais de saúde. Para os "
      "doentes e as famílias, será elaborado um folheto em português e em "
      "Emakhuwa, com as mensagens principais sobre a duração do tratamento, "
      "os efeitos adversos e os apoios disponíveis, a distribuir nos centros "
      "participantes."),
]

# ----------------------------------------------------- 11. cronograma -------
CRONOGRAMA_TEXTO = [
    P("O [[quadro:cronograma]] distribui as actividades pelos doze meses do "
      "estudo, de Outubro de 2026 a Setembro de 2027. A submissão ao comité "
      "e os pedidos de autorização ocupam os meses de Novembro de 2026 a "
      "Janeiro de 2027, e nenhuma actividade com acesso aos dados ou aos "
      "participantes começa antes de Fevereiro de 2027, depois da aprovação "
      "ética. A extracção dos registos precede as entrevistas, como exige o "
      "desenho sequencial, e a análise quantitativa preliminar orienta a "
      "selecção dos entrevistados."),
]
CRONOGRAMA = {
    "inicio": (2026, 10),
    "n_meses": 12,
    "titulo": "Cronograma de actividades (Outubro de 2026 a Setembro de 2027)",
    "actividades": [
        ("Revisão da literatura e redacção do protocolo", [1, 2]),
        ("Submissão ao CIBS-UniLúrio e pedidos de autorização institucional",
         [2, 3, 4]),
        ("Painel de peritos, tradução para Emakhuwa e programação da ficha "
         "electrónica", [3, 4]),
        ("Formação da equipa, verificação prévia de 30 registos e pré-teste "
         "do guião", [5]),
        ("Extracção dos dados dos livros de registo e das fichas de "
         "tratamento", [6, 7]),
        ("Análise quantitativa preliminar e selecção intencional dos "
         "entrevistados", [7, 8]),
        ("Entrevistas em profundidade, transcrição e tradução", [8, 9]),
        ("Análise quantitativa final, análise temática e integração",
         [9, 10]),
        ("Redacção do relatório final", [10, 11]),
        ("Revisão pelo orientador, correcções e entrega", [11]),
        ("Defesa pública e devolução dos resultados às instituições", [12]),
    ],
}

# ----------------------------------------------------- 12. orcamento --------
ORCAMENTO_TEXTO = [
    P("A [[tabela:orcamento]] apresenta o orçamento estimado, em meticais. O "
      "estudo será financiado pelo estudante, e será pedido apoio à "
      "Faculdade de Ciências de Saúde da Universidade Lúrio e a parceiros do "
      "programa de tuberculose para as rubricas de recolha de dados. As "
      "rubricas maiores são a transcrição e a tradução das entrevistas, "
      "correspondentes a cerca de 20 horas de áudio, e o subsídio do "
      "assistente de investigação, necessário para a extracção e a dupla "
      "extracção de pelo menos 556 registos em vários centros. O transporte "
      "cobre as deslocações da equipa durante a extracção e as entrevistas, "
      "o reembolso aos participantes compensa a deslocação e o tempo, e a "
      "recolha electrónica em telemóvel dispensa a impressão das fichas de "
      "extracção."),
]
ORCAMENTO = [
    ("Transporte local da equipa (extracção e entrevistas)", "dia-pessoa",
     90, 150),
    ("Subsídio do assistente de investigação (extracção e dupla "
     "extracção)", "dia", 30, 700),
    ("Subsídio do assistente intérprete de Emakhuwa (entrevistas)",
     "entrevista", 26, 600),
    ("Transcrição e tradução das entrevistas", "hora de áudio", 20, 1200),
    ("Tradução e retroversão do guião e dos termos para Emakhuwa",
     "documento", 3, 1500),
    ("Reembolso de transporte e lanche aos participantes", "participante",
     26, 300),
    ("Gravador de voz digital", "unidade", 2, 3500),
    ("Pacote de dados móveis e comunicações", "mês", 8, 500),
    ("Impressão e cópias (folhas de informação, termos, guiões, reserva)",
     "página", 1200, 5),
    ("Material de escritório", "conjunto", 1, 3000),
    ("Formação da equipa e reunião do painel de peritos", "sessão", 2, 1500),
    ("Encadernação do relatório final", "exemplar", 4, 1500),
    ("Folhetos em português e Emakhuwa e cartaz para as jornadas",
     "conjunto", 1, 4500),
]
ORCAMENTO_IMPREVISTOS = 0.10

# ----------------------------------------------------- apendices ------------
_SUPERVISAO = ["DOT na unidade sanitária",
               "DOT na comunidade por activista ou confidente",
               "DOT por familiar", "Auto-administrado", "Não registado"]

APENDICES = [
    ("Ficha de extracção de dados dos livros de registo e das fichas de "
     "tratamento", [
        NOTA("Instruções ao extractor: preencher uma ficha por episódio "
             "seleccionado. Não copiar nome, endereço completo, telefone nem "
             "número do processo. Usar 99 para «não registado» e 88 para «não "
             "aplicável». Datas no formato dia/mês/ano. Em caso de dúvida, "
             "anotar em observações e consultar o investigador."),
        H3("Secção I. Identificação codificada"),
        CAMPO("Código do registo (centro e número sequencial): ____-______"),
        CAMPO("Código do centro: ______   Extractor: ______   Data da "
              "extracção: ___/___/______"),
        PERG("Trimestre do registo em 2025:",
             ["Janeiro a Março", "Abril a Junho", "Julho a Setembro",
              "Outubro a Dezembro"]),
        PERG("Outro registo da mesma pessoa em 2025:",
             ["Não", "Sim, reinício após perda de seguimento",
              "Sim, transferência entre centros incluídos",
              "Sim, outro motivo"]),
        H3("Secção II. Dados sociodemográficos"),
        PERG("Sexo:", ["Masculino", "Feminino", "Não registado"]),
        PERG("Idade em anos completos à data do registo:"),
        PERG("Bairro de residência em relação ao centro:",
             ["Dentro da área de referência", "Fora da área de referência",
              "Não registado"]),
        PERG("Contacto telefónico do doente ou do confidente anotado:",
             ["Sim", "Não"]),
        H3("Secção III. Dados clínicos"),
        PERG("Categoria do doente:",
             ["Caso novo", "Recaída", "Tratamento pós-perda de seguimento",
              "Outro previamente tratado", "Não registado"]),
        PERG("Forma e base do diagnóstico:",
             ["Pulmonar bacteriologicamente confirmada",
              "Pulmonar clinicamente diagnosticada", "Extrapulmonar",
              "Não registado"]),
        PERG("Método de confirmação bacteriológica:",
             ["Baciloscopia", "Teste molecular rápido", "Cultura",
              "Não aplicável"]),
        PERG("Estado serológico para o HIV:",
             ["Negativo", "Positivo, em TARV no início",
              "Positivo, iniciou TARV durante o tratamento",
              "Positivo, sem registo de TARV", "Desconhecido"]),
        CAMPO("Peso inicial (kg): ______   Altura (m): ______   IMC: ______"),
        H3("Secção IV. Tratamento e supervisão"),
        CAMPO("Data de início do tratamento: ___/___/______   Início da fase "
              "de manutenção: ___/___/______"),
        PERG("Regime registado:",
             ["Primeira linha de seis meses",
              "Primeira linha prolongada (nove ou doze meses)",
              "Outro regime de primeira linha (especificar)"]),
        PERG("Modalidade de supervisão na fase intensiva:", _SUPERVISAO),
        PERG("Modalidade de supervisão na fase de manutenção:", _SUPERVISAO),
        PERG("Efeitos adversos anotados ou notificados:",
             ["Não", "Hepáticos", "Neurológicos", "Gastrointestinais",
              "Cutâneos", "Outros"],
             instrucao="Pode assinalar mais de uma opção."),
        PERG("Apoio nutricional anotado:", ["Sim", "Não"]),
        PERG("Busca activa anotada:", ["Sim", "Não"]),
        H3("Secção V. Calendário de doses e interrupções"),
        PERG("Forma de registo das doses na ficha:",
             ["Tomas diárias assinaladas",
              "Datas de dispensa com número de dias de medicação",
              "Apenas datas de consulta", "Sem registo utilizável"]),
        CAMPO("Dias de tratamento previstos até ao resultado: ______   Dias "
              "com dose documentada: ______   Adesão (%): ______"),
        CAMPO("Dias com doses isoladas falhadas (períodos inferiores a 14 "
              "dias): ______"),
        TABELA(None, "Episódios de interrupção",
               ["Episódio", "Última dose antes da interrupção",
                "Data da retoma", "Duração (dias)", "Fase",
                "Motivo anotado"],
               [["1", "", "", "", "", ""], ["2", "", "", "", "", ""],
                ["3", "", "", "", "", ""]],
               larguras=[1.8, 3.2, 2.6, 2.2, 2.2, 4.0]),
        NOTA("Registar apenas períodos de 14 ou mais dias consecutivos sem "
             "dose documentada. A fase é intensiva nos primeiros 60 dias e de "
             "manutenção a partir daí."),
        H3("Secção VI. Resultado do tratamento"),
        PERG("Resultado registado:",
             ["Curado", "Tratamento completo", "Falência", "Óbito",
              "Perda de seguimento", "Transferido para fora", "Não avaliado",
              "Mudança para regime de segunda linha"]),
        CAMPO("Data do resultado: ___/___/______"),
        H3("Secção VII. Controlo de qualidade"),
        PERG("Registo seleccionado para dupla extracção:", ["Sim", "Não"]),
        CAMPO("Variáveis sem preenchimento na fonte: "
              "__________________________________"),
        CAMPO("Observações: ______________________________________________"),
        NOTA("Regras da verificação prévia (30 registos): a variável com "
             "menos de 60% de preenchimento sai do modelo multivariável; a "
             "forma de cálculo da adesão é escolhida segundo o registo "
             "disponível em 60% ou mais das fichas."),
    ]),
    ("Guião de entrevista semi-estruturada", [
        NOTA("Instruções ao entrevistador: confirmar o consentimento e a "
             "autorização de gravação antes de começar. Usar a língua "
             "escolhida pelo participante. As perguntas são pontos de "
             "partida: seguir o relato e usar as sugestões de aprofundamento "
             "só quando necessário. Não fazer juízos sobre as interrupções. "
             "Duração prevista: 40 a 60 minutos."),
        H3("Parte I. Caracterização do participante"),
        CAMPO("Código da entrevista: E____   Grupo: A (   )  B (   )   "
              "Centro: ______   Data: ___/___/______"),
        PERG("Idade em anos completos:"),
        PERG("Sexo:", ["Masculino", "Feminino"]),
        PERG("Estado civil:", ["Solteiro(a)", "Casado(a) ou em união",
                               "Separado(a) ou divorciado(a)", "Viúvo(a)"]),
        PERG("Escolaridade:", ["Nenhuma", "Primária", "Secundária",
                               "Técnica ou superior"]),
        PERG("Ocupação principal:",
             ["Sem ocupação", "Trabalho por conta própria ou informal",
              "Trabalho assalariado", "Estudante", "Doméstica", "Outra"]),
        PERG("Língua da entrevista:", ["Português", "Emakhuwa"]),
        PERG("Tempo de deslocação de casa ao centro (minutos) e meio de "
             "transporte:"),
        PERG("Custo de ida e volta ao centro (meticais):"),
        PERG("Fase do tratamento:", ["Intensiva", "Manutenção"]),
        PERG("Meses em tratamento (confirmados na ficha, com autorização do "
             "participante):"),
        PERG("Estado serológico para o HIV, se o participante quiser "
             "informar:", ["Negativo", "Positivo", "Prefere não dizer"]),
        H3("Parte II. Perguntas orientadoras"),
        LISTA([
            "Conte-me como soube que tinha tuberculose e como começou o "
            "tratamento. Aprofundar: primeiros sintomas; onde procurou ajuda "
            "primeiro; explicações recebidas no início.",
            "O que sabe sobre a tuberculose e sobre o tempo que o tratamento "
            "dura? Aprofundar: causa; se tem cura; porque dura seis meses; o "
            "que acontece se parar.",
            "Como é o seu dia-a-dia com os comprimidos? Aprofundar: hora da "
            "toma; quem observa; tomas ao fim-de-semana; como se lembra.",
            "Houve alturas em que deixou de tomar os comprimidos, ou em que "
            "teve vontade de deixar? Conte-me o que aconteceu. Aprofundar: "
            "sentir-se melhor ou curado; efeitos dos medicamentos; falta de "
            "comida; viagens ou trabalho; álcool; conselhos de familiares ou "
            "de médicos tradicionais.",
            "Que efeitos sentiu com os medicamentos e o que fez quando os "
            "sentiu? Aprofundar: se comunicou à equipa; se foi atendido; se "
            "alguém lhe explicou o que fazer.",
            "Como faz para vir ao centro de saúde? Quanto tempo e quanto "
            "dinheiro isso lhe custa? Aprofundar: transporte; dias de "
            "trabalho perdidos; como arranja o dinheiro.",
            "Como tem sido a alimentação em casa desde que começou o "
            "tratamento? Aprofundar: fome com os comprimidos; apoio "
            "alimentar recebido ou pedido.",
            "Quem o apoia no tratamento? Como reagiram a família, os vizinhos "
            "e as pessoas do trabalho? Aprofundar: confidente ou padrinho; "
            "estigma; esconder a doença.",
            "Como é atendido no centro de saúde? Aprofundar: tempo de "
            "espera; forma como é tratado; aconselhamento recebido; falta de "
            "medicamentos; contacto quando faltou.",
            "Para quem interrompeu: como voltou ao tratamento? Para quem não "
            "interrompeu: o que o ajudou a não parar? Aprofundar: quem o "
            "procurou ou incentivou; o que mudou.",
            "O que deveria mudar para que as pessoas com tuberculose não "
            "deixem o tratamento? Há mais alguma coisa que queira dizer?",
        ], numerada=True),
        H3("Parte III. Fecho"),
        NOTA("Resumir ao participante as ideias principais e pedir que as "
             "confirme ou corrija. Agradecer, entregar o reembolso do "
             "transporte e o lanche e, se surgir necessidade, aplicar a via "
             "de referenciação prevista no protocolo."),
        CAMPO("Duração da entrevista (minutos): ______   Notas de campo "
              "registadas: (   ) sim   (   ) não"),
    ]),
    ("Folha de informação ao participante", [
        P("Título do estudo: Adesão ao tratamento da tuberculose e factores "
          "associados à sua interrupção em adultos seguidos nos centros de "
          "saúde da cidade de Nampula, 2025-2027."),
        P("Investigador: [Nome do(a) estudante], estudante do curso de "
          "Farmácia da Faculdade de Ciências de Saúde da Universidade Lúrio, "
          "sob orientação de [Nome e grau académico do(a) orientador(a)]."),
        P("Estamos a fazer um estudo para perceber como as pessoas com "
          "tuberculose conseguem tomar os comprimidos durante todo o "
          "tratamento, o que as leva por vezes a parar e o que as ajuda a "
          "continuar. Os resultados vão servir para melhorar o apoio aos "
          "doentes nos centros de saúde da cidade."),
        P("Se aceitar participar, terá uma conversa connosco, numa sala "
          "reservada deste centro, em português ou em Emakhuwa, com a duração "
          "de 40 a 60 minutos. Com a sua autorização, a conversa será "
          "gravada, para não perdermos nada do que disser. Não há respostas "
          "certas nem erradas."),
        P("A participação é voluntária. Pode recusar, não responder a alguma "
          "pergunta ou parar a conversa a qualquer momento, e isso não muda "
          "em nada o seu tratamento nem o atendimento neste centro. O seu "
          "nome não será escrito nas transcrições nem nos relatórios; usaremos "
          "um código, e a gravação será apagada depois de transcrita. Com a "
          "sua autorização, confirmaremos na sua ficha de tratamento apenas a "
          "fase e a duração do tratamento."),
        P("Falar da doença pode trazer alguma tristeza ou desconforto; se "
          "isso acontecer, podemos fazer uma pausa ou parar. Se nos contar "
          "que está com dificuldades no tratamento, com efeitos dos "
          "medicamentos ou sem comida, e se concordar, ajudamo-lo a falar "
          "com o clínico do sector de tuberculose ou com o apoio psicossocial "
          "do centro. Receberá 300 meticais para o transporte e um lanche."),
        P("O estudo foi aprovado pelo Comité Institucional de Bioética para "
          "a Saúde da Universidade Lúrio e autorizado pelos serviços de saúde "
          "da cidade (referência do parecer: ______). Para qualquer dúvida, "
          "pode contactar o investigador pelo telefone [preencher] ou o "
          "comité pelo telefone [preencher]."),
    ]),
    ("Termo de consentimento livre e esclarecido", [
        P("Eu, abaixo identificado(a), declaro que me foi lida e explicada, "
          "numa língua que compreendo, a folha de informação sobre o estudo "
          "«Adesão ao tratamento da tuberculose e factores associados à sua "
          "interrupção em adultos seguidos nos centros de saúde da cidade de "
          "Nampula, 2025-2027». Compreendi o objectivo do estudo, o que a "
          "minha participação envolve, os riscos e os benefícios, e que posso "
          "desistir a qualquer momento sem prejuízo para o meu tratamento. "
          "Tive oportunidade de fazer perguntas e as respostas foram "
          "satisfatórias."),
        PERG("Aceito participar na entrevista:", ["Sim", "Não"]),
        PERG("Autorizo a gravação áudio da entrevista:", ["Sim", "Não"]),
        PERG("Autorizo a consulta da minha ficha de tratamento para "
             "confirmar a fase e a duração do tratamento:", ["Sim", "Não"]),
        PERG("Aceito ser encaminhado(a), se necessário, para apoio no centro "
             "de saúde:", ["Sim", "Não"]),
        CAMPO("Código do participante: E____"),
        CAMPO("Assinatura do participante: "
              "____________________________________"),
        CAMPO("Impressão digital (se não souber assinar):   [          ]"),
        CAMPO("Nome da testemunha imparcial: "
              "__________________________________"),
        CAMPO("Assinatura da testemunha: "
              "_____________________________________"),
        CAMPO("Nome e assinatura do investigador: "
              "_____________________________"),
        CAMPO("Local e data: Nampula, ___/___/2027"),
        NOTA("Este termo é feito em duas vias: uma fica com o participante e "
             "outra com o investigador. A testemunha é obrigatória quando o "
             "participante não sabe ler nem escrever e assina por impressão "
             "digital."),
    ]),
    ("Pedido de dispensa de consentimento informado para a componente "
     "documental", [
        CAMPO("À Presidente ou ao Presidente do Comité Institucional de "
              "Bioética para a Saúde da Universidade Lúrio"),
        CAMPO("Nampula, ___ de ______________ de 2026"),
        P("Assunto: pedido de dispensa de consentimento informado individual "
          "para a extracção de dados dos livros de registo e das fichas de "
          "tratamento da tuberculose."),
        P("No âmbito do protocolo «Adesão ao tratamento da tuberculose e "
          "factores associados à sua interrupção em adultos seguidos nos "
          "centros de saúde da cidade de Nampula, 2025-2027», venho solicitar "
          "a dispensa do consentimento informado individual para a "
          "componente documental, com os fundamentos seguintes:"),
        LISTA([
            "O estudo usa apenas dados já registados, relativos aos adultos "
            "que iniciaram o tratamento em 2025, sem qualquer intervenção nem "
            "contacto com os doentes;",
            "Obter o consentimento seria impraticável, porque muitos doentes "
            "terminaram o tratamento, foram transferidos, perderam o "
            "seguimento ou faleceram, e a exigência enviesaria a amostra "
            "contra os que interromperam o tratamento, que são o objecto do "
            "estudo;",
            "O risco é mínimo: a ficha de extracção não contém nome, endereço "
            "completo, telefone nem número de processo, e a lista que liga "
            "cada código ao número do livro fica apenas com o investigador e "
            "é destruída após o controlo de qualidade;",
            "Os dados serão usados apenas para os fins do estudo, guardados "
            "com acesso restrito e publicados de forma agregada, sem "
            "identificação de doentes, profissionais ou centros;",
            "A consulta dos arquivos será feita nos próprios centros, com "
            "autorização das respectivas direcções e do SDSMAS da Cidade de "
            "Nampula.",
        ]),
        P("Os participantes da componente qualitativa, pelo contrário, darão "
          "consentimento livre e esclarecido, conforme os Apêndices C e D."),
        CAMPO("O investigador: _____________________________________"),
        CAMPO("O orientador: ______________________________________"),
    ]),
    ("Pedido de autorização institucional", [
        CAMPO("À Directora ou ao Director do Serviço Distrital de Saúde, "
              "Mulher e Acção Social da Cidade de Nampula"),
        CAMPO("C/c: Direcção Provincial de Saúde de Nampula; direcções dos "
              "centros de saúde com sector de tuberculose"),
        CAMPO("Nampula, ___ de ______________ de 2026"),
        P("Assunto: pedido de autorização para a realização de um estudo "
          "sobre a adesão ao tratamento da tuberculose nos centros de saúde "
          "da cidade de Nampula."),
        P("[Nome do(a) estudante], estudante do curso de Farmácia da "
          "Faculdade de Ciências de Saúde da Universidade Lúrio, sob "
          "orientação de [Nome e grau académico do(a) orientador(a)], vem "
          "solicitar autorização para realizar o estudo «Adesão ao tratamento "
          "da tuberculose e factores associados à sua interrupção em adultos "
          "seguidos nos centros de saúde da cidade de Nampula, 2025-2027», "
          "cujo protocolo foi submetido ao Comité Institucional de Bioética "
          "para a Saúde da Universidade Lúrio."),
        P("O estudo compreende duas actividades: a consulta, em Março e Abril "
          "de 2027, dos livros de registo e das fichas de tratamento da "
          "tuberculose dos adultos registados em 2025, para extracção de "
          "dados sem identificadores; e a realização, em Maio e Junho de "
          "2027, de entrevistas a adultos em tratamento que aceitem "
          "participar, numa sala reservada do centro e sem interferir com as "
          "consultas. Solicita-se ainda a informação sobre o número de "
          "centros com sector de tuberculose e o número de adultos "
          "registados em 2025 em cada um, necessária ao cálculo da amostra."),
        P("O investigador compromete-se a iniciar a recolha apenas após o "
          "parecer favorável do comité, a respeitar a confidencialidade dos "
          "doentes e o funcionamento dos serviços, e a entregar ao SDSMAS e a "
          "cada centro um relatório com os resultados, numa perspectiva de "
          "melhoria dos serviços."),
        CAMPO("O investigador: _____________________________________"),
        CAMPO("O orientador: ______________________________________"),
        CAMPO("Despacho: _________________________________________"),
    ]),
]
