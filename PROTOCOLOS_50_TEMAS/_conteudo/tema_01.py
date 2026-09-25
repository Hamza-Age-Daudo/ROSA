# -*- coding: utf-8 -*-
"""
TEMA 01. Adesão à terapêutica anti-retroviral e factores associados em
adultos seguidos no Hospital Central de Nampula.

Compor e validar:   python -X utf8 _motor/motor.py _conteudo/tema_01.py
Verificar fontes:   python -X utf8 _motor/refs.py verificar _conteudo/tema_01.py
"""
from blocos import (CAMPO, ESCALA, FORMULA, H3, LISTA, NOTA, P, PERG,
                    QUADRO, TABELA)

NUMERO = 1
SLUG = "Adesao_TARV_Factores_Associados_Adultos_HCN"
TITULO = ("Adesão à terapêutica anti-retroviral e factores associados em "
          "adultos seguidos no Hospital Central de Nampula, de Abril a Junho "
          "de 2027")
DESENHO = ("Transversal analítico, de base hospitalar, com entrevista "
           "estruturada, contagem de comprimidos no levantamento e consulta "
           "do processo clínico")

AUTOR = "[Nome do(a) estudante]"
ORIENTADOR = "[Nome e grau académico do(a) orientador(a)]"

# ---------------------------------------------------------------- resumo --
RESUMO = (
    "A terapêutica anti-retroviral transformou a infecção pelo vírus da "
    "imunodeficiência humana numa doença crónica controlável, mas o seu "
    "benefício depende de uma adesão elevada e mantida ao longo da vida. Na "
    "província de Nampula, a supressão da carga viral entre os adultos que "
    "vivem com o vírus está entre as mais baixas do país e não existem "
    "estimativas da adesão obtidas por métodos objectivos no Hospital Central "
    "de Nampula, nem dos factores que a condicionam. O estudo tem como "
    "objectivo avaliar a adesão à terapêutica anti-retroviral e os factores "
    "associados em adultos seguidos no Hospital Central de Nampula, entre "
    "Abril e Junho de 2027. Trata-se de um estudo transversal analítico, de "
    "base hospitalar e abordagem quantitativa, a realizar em 535 adultos com "
    "pelo menos seis meses de tratamento, seleccionados por amostragem "
    "aleatória sistemática no acto do levantamento da medicação na farmácia. "
    "A adesão será medida pela contagem de comprimidos, com ponto de corte de "
    "95%, e complementada pelo auto-relato de três itens e pelo registo de "
    "levantamentos. Um questionário estruturado, aplicado por entrevista em "
    "português ou em emakhuwa, recolherá dados sociodemográficos, o tempo, a "
    "distância e o custo da deslocação, os efeitos adversos percebidos, o "
    "estigma relacionado com o vírus, o apoio familiar percebido e o consumo "
    "de álcool, com escalas previamente validadas; a carga viral mais recente "
    "será extraída do processo clínico. A análise incluirá estatística "
    "descritiva, a concordância entre métodos pelo coeficiente kappa, o teste "
    "do qui-quadrado e a regressão logística multivariável, com nível de "
    "significância de cinco por cento. Espera-se estimar a proporção de "
    "doentes com boa adesão, identificar os factores modificáveis que a "
    "comprometem e verificar a sua relação com a supressão viral, "
    "fundamentando um programa de sessões de aconselhamento farmacêutico "
    "dirigido aos doentes de maior risco."
)
PALAVRAS_CHAVE = ["adesão à medicação", "estigma social",
                  "infecções por HIV", "Moçambique",
                  "terapêutica anti-retroviral"]
ABSTRACT = (
    "Antiretroviral therapy has turned infection with the human "
    "immunodeficiency virus into a manageable chronic disease, but its "
    "benefit depends on high adherence sustained throughout life. In Nampula "
    "province, viral load suppression among adults living with the virus is "
    "among the lowest in the country, and there are no estimates of "
    "adherence obtained with objective methods at Nampula Central Hospital, "
    "nor of the factors that shape it. This study aims to assess adherence to "
    "antiretroviral therapy and its associated factors among adults followed "
    "at Nampula Central Hospital between April and June 2027. It is an "
    "analytical, hospital-based cross-sectional study with a quantitative "
    "approach, to be carried out among 535 adults with at least six months of "
    "treatment, selected by systematic random sampling at the time of "
    "medication pick-up at the pharmacy. Adherence will be measured by pill "
    "count, with a cut-off of 95%, and complemented by a three-item "
    "self-report and by pharmacy refill records. A structured questionnaire, "
    "administered by interview in Portuguese or Emakhuwa, will collect "
    "sociodemographic data, travel time, distance and cost, perceived adverse "
    "effects, stigma related to the virus, perceived family support and "
    "alcohol use, using previously validated scales; the most recent viral "
    "load will be extracted from the clinical record. The analysis will "
    "include descriptive statistics, agreement between methods using the "
    "kappa coefficient, the chi-square test and multivariable logistic "
    "regression, with a significance level of five per cent. The study is "
    "expected to estimate the proportion of patients with good adherence, to "
    "identify the modifiable factors that compromise it and to verify its "
    "relationship with viral suppression, providing the basis for a "
    "programme of pharmaceutical counselling sessions targeted at the "
    "patients at highest risk."
)
KEYWORDS = ["antiretroviral therapy", "HIV infections",
            "medication adherence", "Mozambique", "social stigma"]

ABREVIATURAS = [
    ("AUDIT-C", "Alcohol Use Disorders Identification Test, versão de "
                "consumo (teste de identificação de perturbações do uso de "
                "álcool, três itens)"),
    ("CD4", "grupo de diferenciação 4, marcador dos linfócitos T "
            "auxiliares"),
    ("CIBS-UniLúrio", "Comité Institucional de Bioética para a Saúde da "
                      "Universidade Lúrio"),
    ("FILA", "Ficha Individual de Levantamento de Anti-retrovirais"),
    ("GAAC", "Grupos de Apoio à Adesão Comunitária"),
    ("HCN", "Hospital Central de Nampula"),
    ("HIV", "vírus da imunodeficiência humana"),
    ("HRa", "hazard ratio ajustado (razão de riscos instantâneos ajustada)"),
    ("IC95%", "intervalo de confiança a 95%"),
    ("INSIDA", "Inquérito Nacional sobre o Impacto do HIV e SIDA"),
    ("IVC", "índice de validade de conteúdo"),
    ("MDS", "Modelos Diferenciados de Serviços"),
    ("MISAU", "Ministério da Saúde"),
    ("MSPSS", "Multidimensional Scale of Perceived Social Support (escala "
              "multidimensional de apoio social percebido)"),
    ("OMS", "Organização Mundial da Saúde"),
    ("ONUSIDA", "Programa Conjunto das Nações Unidas sobre o HIV/SIDA"),
    ("OR", "odds ratio (razão de possibilidades)"),
    ("ORa", "odds ratio ajustado"),
    ("RP", "razão de prevalências"),
    ("SDSMAS", "Serviço Distrital de Saúde, Mulher e Acção Social"),
    ("SIDA", "síndrome da imunodeficiência adquirida"),
    ("SPSS", "Statistical Package for the Social Sciences"),
    ("STROBE", "Strengthening the Reporting of Observational Studies in "
               "Epidemiology"),
    ("TARV", "terapêutica anti-retroviral"),
    ("TLD", "combinação de dose fixa de fumarato de tenofovir disoproxil, "
            "lamivudina e dolutegravir"),
]

# ------------------------------------------------------------ referencias --
# Todas geradas por _motor/refs.py (pmid, doi ou web); nada escrito à mão.
FONTES = {
    # ---- documentos oficiais
    "unaids2026": "Joint United Nations Programme on HIV/AIDS. Global HIV and AIDS statistics: fact sheet [Internet]. Geneva: UNAIDS; 2026 [citado 2026 Set 19]. Disponível em: https://www.unaids.org/en/resources/fact-sheet",
    "who2021": "World Health Organization. Consolidated guidelines on HIV prevention, testing, treatment, service delivery and monitoring: recommendations for a public health approach [Internet]. Geneva: World Health Organization; 2021 [citado 2026 Set 19]. Disponível em: https://www.who.int/publications/i/item/9789240031593",
    "who2023": "World Health Organization. The role of HIV viral suppression in improving individual health and reducing transmission: policy brief [Internet]. Geneva: World Health Organization; 2023 [citado 2026 Set 19]. Disponível em: https://www.who.int/publications/i/item/9789240055179",
    "unaids2021": "Joint United Nations Programme on HIV/AIDS. Global AIDS Strategy 2021-2026. End inequalities. End AIDS [Internet]. Geneva: UNAIDS; 2021 [citado 2026 Set 19]. Disponível em: https://www.unaids.org/en/resources/documents/2021/2021-2026-global-AIDS-strategy",
    "insida2022": "Instituto Nacional de Saúde (Moçambique), ICAP at Columbia University. Mozambique Population-based HIV Impact Assessment, INSIDA 2021: summary sheet [Internet]. New York: ICAP at Columbia University; 2022 [citado 2026 Set 19]. Disponível em: https://phia.icap.columbia.edu/wp-content/uploads/2022/12/53059_14_INSIDA_Summary-sheet-Web.pdf",
    "misau2023": "Ministério da Saúde (Moçambique), Direcção Nacional de Saúde Pública. Guião de cuidados do HIV do adulto, adolescente, grávida, lactante e criança: guião de bolso [Internet]. Maputo: MISAU; 2023 [citado 2026 Set 19]. Disponível em: https://comitetarvmisau.co.mz/docs/guiao_tarv/Tratamento%20antiretroviral%20e%20infecc%CC%A7o%CC%83es%20oportunistas%20do%20adulto%2C%20adolescente%20e%20crianc%CC%A7a_27.03.2023.pdf",
    "misaumds2023": "Ministério da Saúde (Moçambique), Direcção Nacional de Saúde Pública. Orientação para a implementação do novo pacote de Modelos Diferenciados de Serviços para o HIV/SIDA (Circular DNSP/023) [Internet]. Maputo: MISAU; 2023 [citado 2026 Set 19]. Disponível em: https://comitetarvmisau.co.mz/docs/orientacoes_nacionais/2023/Circular%20MDS_19-02-2023.pdf",
    "misau2015": "Ministério da Saúde (Moçambique), Direcção Nacional de Assistência Médica. Directriz nacional de apoio psicossocial e prevenção positiva [Internet]. Maputo: MISAU; 2015 [citado 2026 Set 19]. Disponível em: https://docs.bvsalud.org/biblioref/2020/10/1123151/directriz-nacional-de-apoio-psicossocial-e-prevencao-positiva-3.pdf",
    # ---- magnitude e determinantes
    "heestermans2016": "Heestermans T, Browne JL, Aitken SC, Vervoort SC, Klipstein-Grobusch K. Determinants of adherence to antiretroviral therapy among HIV-positive adults in sub-Saharan Africa: a systematic review. BMJ Glob Health. 2016;1(4):e000125. doi:10.1136/bmjgh-2016-000125. PMID: 28588979.",
    "aytenew2024": "Aytenew TM, Demis S, Birhane BM, Asferie WN, Simegn A, Nibret G, et al. Non-Adherence to Anti-Retroviral Therapy Among Adult People Living with HIV in Ethiopia: Systematic Review and Meta-Analysis. AIDS Behav. 2024;28(2):609-624. doi:10.1007/s10461-023-04252-4. PMID: 38157133.",
    "gobezie2024": "Gobezie MY, Tesfaye NA, Solomon T, Demessie MB, Fentie Wendie T, Tadesse G, et al. Exploring optimal HAART adherence rates in Ethiopian adults: a systematic review and meta-analysis. Front Public Health. 2024;12:1390901. doi:10.3389/fpubh.2024.1390901. PMID: 39469205.",
    "velloza2020": "Velloza J, Kemp CG, Aunon FM, Ramaiya MK, Creegan E, Simoni JM. Alcohol Use and Antiretroviral Therapy Non-Adherence Among Adults Living with HIV/AIDS in Sub-Saharan Africa: A Systematic Review and Meta-Analysis. AIDS Behav. 2020;24(6):1727-1742. doi:10.1007/s10461-019-02716-0. PMID: 31673913.",
    "mosha2024": "Mosha IH, Nyondo GG, Munishi CG, Njiro BJ, Bwire GM. Prevalence and factors associated with viral non-suppression in people living with HIV receiving antiretroviral therapy in sub-Saharan Africa: A systematic review and meta-analysis. Rev Med Virol. 2024;34(3):e2540. doi:10.1002/rmv.2540. PMID: 38708846.",
    "fite2021": "Fite RO. Association between adherence to Antiretroviral Therapy and place of residence among adult HIV infected patients in Ethiopia: A systematic review and meta-analysis. PLoS One. 2021;16(9):e0256948. doi:10.1371/journal.pone.0256948. PMID: 34473774.",
    "sweeney2016": "Sweeney SM, Vanable PA. The Association of HIV-Related Stigma to HIV Medication Adherence: A Systematic Review and Synthesis of the Literature. AIDS Behav. 2016;20(1):29-50. doi:10.1007/s10461-015-1164-1. PMID: 26303196.",
    "campbell2020": "Campbell L, Masquillier C, Thunnissen E, Ariyo E, Tabana H, Sematlane N, et al. Social and Structural Determinants of Household Support for ART Adherence in Low- and Middle-Income Countries: A Systematic Review . Int J Environ Res Public Health. 2020;17(11). doi:10.3390/ijerph17113808. PMID: 32471153.",
    "kanters2020": "Kanters S, Vitoria M, Zoratti M, Doherty M, Penazzato M, Rangaraj A, et al. Comparative efficacy, tolerability and safety of dolutegravir and efavirenz 400mg among antiretroviral therapies for first-line HIV treatment: A systematic literature review and network meta-analysis. EClinicalMedicine. 2020;28:100573. doi:10.1016/j.eclinm.2020.100573. PMID: 33294805.",
    "byrd2019": "Byrd KK, Hou JG, Hazen R, Kirkham H, Suzuki S, Clay PG, et al. Antiretroviral Adherence Level Necessary for HIV Viral Suppression Using Real-World Data. J Acquir Immune Defic Syndr. 2019;82(3):245-251. doi:10.1097/QAI.0000000000002142. PMID: 31343455.",
    "domapielle2024": "Domapielle MK, Abugbila SZ, Kala M. Bypassing primary antiretroviral therapy centres in Sub-Saharan Africa: An integrative review of the theoretical and empirical literature. J Virus Erad. 2024;10(4):100580. doi:10.1016/j.jve.2024.100580. PMID: 39845102.",
    # ---- Moçambique
    "mandlate2023": "Mandlate FM, Greene MC, Pereira LF, Gouveia ML, Mari JJ, Cournos F, et al. Association between mental disorders and adherence to antiretroviral treatment in health facilities in two Mozambican provinces in 2018: a cross-sectional study. BMC Psychiatry. 2023;23(1):274. doi:10.1186/s12888-023-04782-0. PMID: 37081470.",
    "viisainen2024": "Viisainen K, Baumgart Dos Santos M, Sunderbrink U, Couto A. Gender and stigma in antiretroviral treatment adherence in Mozambique: A qualitative study. PLOS Glob Public Health. 2024;4(7):e0003166. doi:10.1371/journal.pgph.0003166. PMID: 39008454.",
    "filimao2019": "Filimão DBC, Moon TD, Senise JF, Diaz RS, Sidat M, Castelo A. Individual factors associated with time to non-adherence to ART pick-up within HIV care and treatment services in three health facilities of Zambézia Province, Mozambique. PLoS One. 2019;14(3):e0213804. doi:10.1371/journal.pone.0213804. PMID: 30908522.",
    "deschacht2023": "De Schacht C, Amorim G, Van Rompaey S, Melo M, Verissimo C, Naftal A, et al. Favorable Impact of Community Adherence Support Groups on Retention in Care and Viral Suppression Rates Among Persons with HIV Receiving Antiretroviral Therapy in Mozambique. AIDS Res Hum Retroviruses. 2023;39(10):525-532. doi:10.1089/AID.2022.0149. PMID: 36802932.",
    "sauralazaro2024": "Saura-Lázaro A, Augusto O, Fernández-Luis S, López-Varela E, Fuente-Soro L, Bila D, et al. HIV care retention in three multi-month ART dispensing: a retrospective cohort study in Mozambique. AIDS. 2024;38(9):1402-1411. doi:10.1097/QAD.0000000000003913. PMID: 38652496.",
    "carrasco2017": "Carrasco MA, Arias R, Figueroa ME. The multidimensional nature of HIV stigma: evidence from Mozambique. Afr J AIDS Res. 2017;16(1):11-18. doi:10.2989/16085906.2016.1264983. PMID: 28367746.",
    "ciccacci2025": "Ciccacci F, Doro Altan AM, Majid N, Orlando S, Uamusse E, Rafael M, et al. HIV Dolutegravir resistance and multiclass failure in Mozambique: findings from a real-world cohort. BMC Infect Dis. 2025;25(1):1210. doi:10.1186/s12879-025-11639-2. PMID: 41023944.",
    "mccabe2025": "McCabe KC, Augusto A, Koole O, McCracken SD, Tiberi O, Boothe M, et al. Non-disclosure of Known HIV Status among People Living with HIV in the Mozambique Population-Based HIV Impact Assessment (INSIDA 2021). AIDS Behav. 2025;29(7):2054-2065. doi:10.1007/s10461-025-04699-7. PMID: 40205309.",
    # ---- estudos empiricos africanos
    "kioko2017": "Kioko MT, Pertet AM. Factors contributing to antiretroviral drug adherence among adults living with HIV or AIDS in a Kenyan rural community. Afr J Prim Health Care Fam Med. 2017;9(1):e1-e7. doi:10.4102/phcfm.v9i1.1343. PMID: 28828875.",
    "aychiluhm2021": "Aychiluhm SB, Tadesse AW, Urmale Mare K, Melaku MS, Ibrahim IM, Ahmed O, et al. Level of non-adherence and its associated factors among adults on first-line antiretroviral therapy in Amhara Regional State, Ethiopia. PLoS One. 2021;16(8):e0255912. doi:10.1371/journal.pone.0255912. PMID: 34370762.",
    "anyaike2019": "Anyaike C, Atoyebi OA, Musa OI, Bolarinwa OA, Durowade KA, Ogundiran A, et al. Adherence to combined Antiretroviral therapy (cART) among people living with HIV/AIDS in a Tertiary Hospital in Ilorin, Nigeria. Pan Afr Med J. 2019;32:10. doi:10.11604/pamj.2019.32.10.7508. PMID: 31080546.",
    "isika2022": "Isika AI, Shehu A, Dahiru T, Obi IF, Oku AO, Balogun MS, et al. Factors influencing adherence to antiretroviral therapy among HIV-infected adults in Cross River State, Nigeria: a cross-sectional study. Pan Afr Med J. 2022;43:187. doi:10.11604/pamj.2022.43.187.37172. PMID: 36915414.",
    "ogbonnaya2024": "Ogbonnaya LU, Onah CK, Azuogu BN, Akpa CO, Okeke KC, Nwachukwu VN, et al. Adverse drug reactions, adherence, and virologic outcomes in adult patients on dolutegravir-based antiretroviral therapy at a tertiary hospital, southeast Nigeria. Ghana Med J. 2024;58(1):101-108. doi:10.4314/gmj.v58i1.14. PMID: 38957273.",
    "nutor2023": "Nutor JJ, Gyamerah AO, Alhassan RK, Duah HO, Thompson RGA, Wilson N, et al. Influence of depression and interpersonal support on adherence to antiretroviral therapy among people living with HIV. AIDS Res Ther. 2023;20(1):42. doi:10.1186/s12981-023-00538-8. PMID: 37386514.",
    "alemu2022": "Alemu A, Meskele M, Darebo TD, Beyene Handiso T, Abebe A, Paulos K. Perceived HIV Stigma and Associated Factors Among Adult ART Patients in Wolaita Zone, Southern Ethiopia. HIV AIDS (Auckl). 2022;14:487-501. doi:10.2147/HIV.S372738. PMID: 36389002.",
    "mudhune2018": "Mudhune V, Gvetadze R, Girde S, Ndivo R, Angira F, Zeh C, et al. Correlation of Adherence by Pill Count, Self-report, MEMS and Plasma Drug Levels to Treatment Response Among Women Receiving ARV Therapy for PMTCT in Kenya. AIDS Behav. 2018;22(3):918-928. doi:10.1007/s10461-017-1724-7. PMID: 28197845.",
    "kizito2026": "Kizito S, Ssewamala FM, Nabayinda J, Nabunya P, Bahar OS, Namatovu P, et al. Comparing Self-Reports, Pill Counts, and Electronic Devices in Assessing Antiretroviral Therapy Adherence and its Association With Viral Suppression in Adolescents Living With HIV. J Acquir Immune Defic Syndr. 2026;101(9):1049-1056. doi:10.1097/QAI.0000000000003899. PMID: 42091096.",
    # ---- medicao e instrumentos
    "anghel2019": "Anghel LA, Farcas AM, Oprean RN. An overview of the common methods used to measure treatment adherence. Med Pharm Rep. 2019;92(2):117-122. doi:10.15386/mpr-1201. PMID: 31086837.",
    "paterson2000": "Paterson DL, Swindells S, Mohr J, Brester M, Vergis EN, Squier C, et al. Adherence to protease inhibitor therapy and outcomes in patients with HIV infection. Ann Intern Med. 2000;133(1):21-30. doi:10.7326/0003-4819-133-1-200007040-00004. PMID: 10877736.",
    "wilson2016": "Wilson IB, Lee Y, Michaud J, Fowler FJ Jr, Rogers WH. Validation of a New Three-Item Self-Report Measure for Medication Adherence. AIDS Behav. 2016;20(11):2700-2708. doi:10.1007/s10461-016-1406-x. PMID: 27098408.",
    "kalichman2024": "Kalichman SC, Banas E, Shkembi B, Kalichman M, Mathews C. The three-item patient-reported instrument for retrospective adherence in resource constrained settings: reliability, validity and potential utility. J Behav Med. 2024;47(1):135-143. doi:10.1007/s10865-023-00438-2. PMID: 37524887.",
    "reinius2017": "Reinius M, Wettergren L, Wiklander M, Svedhem V, Ekström AM, Eriksson LE. Development of a 12-item short version of the HIV stigma scale. Health Qual Life Outcomes. 2017;15(1):115. doi:10.1186/s12955-017-0691-z. PMID: 28558805.",
    "luz2020": "Luz PM, Torres TS, Almeida-Brasil CC, Marins LMS, Bezerra DRB, Veloso VG, et al. Translation and validation of the Short HIV Stigma scale in Brazilian Portuguese. Health Qual Life Outcomes. 2020;18(1):322. doi:10.1186/s12955-020-01571-1. PMID: 33008400.",
    "wanjala2022": "Wanjala SW, Nyongesa MK, Mwangi P, Mutua AM, Luchters S, Newton CRJC, et al. Measurement characteristics and correlates of HIV-related stigma among adults living with HIV: a cross-sectional study from coastal Kenya. BMJ Open. 2022;12(2):e050709. doi:10.1136/bmjopen-2021-050709. PMID: 35193904.",
    "zimet1988": "Zimet GD, Dahlem NW, Zimet SG, Farley GK. The Multidimensional Scale of Perceived Social Support. Journal of Personality Assessment. 1988;52(1):30-41. doi:10.1207/s15327752jpa5201_2",
    "dambi2018": "Dambi JM, Corten L, Chiwaridzo M, Jack H, Mlambo T, Jelsma J. A systematic review of the psychometric properties of the cross-cultural translations and adaptations of the Multidimensional Perceived Social Support Scale (MSPSS). Health Qual Life Outcomes. 2018;16(1):80. doi:10.1186/s12955-018-0912-0. PMID: 29716589.",
    "inoue2021": "Inoue S, Chitambi C, Vinikoor MJ, Kanguya T, Murray LK, Sharma A, et al. Testing the validity of the AUDIT-C and AUDIT-3 to detect unhealthy alcohol use among high-risk populations in Zambia: A secondary analysis from two randomized trials. Drug Alcohol Depend. 2021;229(Pt A):109156. doi:10.1016/j.drugalcdep.2021.109156. PMID: 34773884.",
    "almanasreh2019": "Almanasreh E, Moles R, Chen TF. Evaluation of methods used for estimating content validity. Res Social Adm Pharm. 2019;15(2):214-221. doi:10.1016/j.sapharm.2018.03.066. PMID: 29606610.",
    # ---- intervencoes
    "ahmed2022": "Ahmed A, Abdulelah Dujaili J, Rehman IU, Chuah LH, Hashmi FK, Awaisu A, et al. Effect of pharmacist care on clinical outcomes among people living with HIV/AIDS: A systematic review and meta-analysis. Res Social Adm Pharm. 2022;18(6):2962-2980. doi:10.1016/j.sapharm.2021.07.020. PMID: 34353754.",
    "chatha2020": "Chatha ZF, Rashid U, Olsen S, Din FU, Khan A, Nawaz K, et al. Pharmacist-led counselling intervention to improve antiretroviral drug adherence in Pakistan: a randomized controlled trial. BMC Infect Dis. 2020;20(1):874. doi:10.1186/s12879-020-05571-w. PMID: 33228562.",
    "nyoni2020": "Nyoni T, Sallah YH, Okumu M, Byansi W, Lipsey K, Small E. The effectiveness of treatment supporter interventions in antiretroviral treatment adherence in sub-Saharan Africa: a systematic review and meta-Analysis. AIDS Care. 2020;32(Suppl 2):214-227. doi:10.1080/09540121.2020.1742870. PMID: 32196385.",
    # ---- metodologia e etica
    "peduzzi1996": "Peduzzi P, Concato J, Kemper E, Holford TR, Feinstein AR. A simulation study of the number of events per variable in logistic regression analysis. J Clin Epidemiol. 1996;49(12):1373-9. doi:10.1016/s0895-4356(96)00236-3. PMID: 8970487.",
    "tamhane2016": "Tamhane AR, Westfall AO, Burkholder GA, Cutter GR. Prevalence odds ratio versus prevalence ratio: choice comes with consequences. Stat Med. 2016;35(30):5730-5735. doi:10.1002/sim.7059. PMID: 27460748.",
    "vonelm2007": "von Elm E, Altman DG, Egger M, Pocock SJ, Gøtzsche PC, Vandenbroucke JP. The Strengthening the Reporting of Observational Studies in Epidemiology (STROBE) statement: guidelines for reporting observational studies. Lancet. 2007;370(9596):1453-7. doi:10.1016/S0140-6736(07)61602-X. PMID: 18064739.",
    "helsinki2025": "World Medical Association. World Medical Association Declaration of Helsinki: Ethical Principles for Medical Research Involving Human Participants. JAMA. 2025;333(1):71-74. doi:10.1001/jama.2024.21972. PMID: 39425955.",
}
SEMINAIS = {
    "paterson2000": "Estudo original que fundamenta o limiar de adesão de "
                    "95% usado na classificação por contagem de comprimidos.",
    "zimet1988": "Artigo original da escala multidimensional de apoio "
                 "social percebido (instrumento usado no estudo).",
    "peduzzi1996": "Estudo de simulação que estabeleceu a regra de pelo menos "
                   "10 eventos por variável na regressão logística.",
    "vonelm2007": "Declaração STROBE, norma de relato em vigor para estudos "
                  "observacionais.",
    "misau2015": "Directriz nacional em vigor que regula o apoio "
                 "psicossocial e o aconselhamento de adesão em Moçambique.",
}

# ----------------------------------------------------- 1. introducao --------
INTRODUCAO = [
    P("A infecção pelo vírus da imunodeficiência humana (HIV) continua a ser "
      "um dos maiores problemas de saúde pública do mundo. Em 2025 viviam com "
      "o HIV 41,0 milhões de pessoas, das quais 32,1 milhões tinham acesso à "
      "terapêutica anti-retroviral (TARV); registaram-se 1,2 milhões de novas "
      "infecções e 570.000 mortes relacionadas com a síndrome da "
      "imunodeficiência adquirida (SIDA), e, entre todas as pessoas que vivem "
      "com o vírus, 88% conheciam o seu estado, 78% estavam em tratamento e "
      "74% tinham a carga viral suprimida {unaids2026}. A Estratégia Global "
      "do Programa Conjunto das Nações Unidas sobre o HIV/SIDA (ONUSIDA) para "
      "2021-2026 fixou as metas de 95% de diagnóstico, 95% de tratamento e "
      "95% de supressão viral, reconhecendo que o último destes patamares "
      "depende sobretudo da continuidade e da regularidade do tratamento "
      "{unaids2021}."),
    P("A TARV transformou a infecção pelo HIV numa doença crónica "
      "controlável, mas o seu efeito depende da toma diária e continuada "
      "dos medicamentos. A Organização "
      "Mundial da Saúde (OMS) recomenda, como primeira linha para adultos, o "
      "regime de tenofovir, lamivudina e dolutegravir e a monitorização "
      "periódica da carga viral {who2021}. Quando a carga viral deixa de ser "
      "detectável, o risco de transmissão sexual é nulo, e quando se mantém "
      "suprimida, embora detectável, o risco é quase nulo {who2023}. A "
      "adesão insuficiente anula estes ganhos: permite a replicação viral, "
      "selecciona estirpes resistentes, conduz à falência terapêutica e "
      "mantém a transmissão na comunidade {who2021,mosha2024}."),
    P("A África subsariana concentra a maior parte do peso da epidemia e "
      "também a maior parte da evidência sobre adesão. Uma revisão "
      "sistemática de 146 estudos, que incluiu 161.922 doentes da região, "
      "encontrou uma adesão média de 72,9% e apontou como principais "
      "determinantes da não adesão o consumo de álcool, o sexo masculino, o "
      "uso de medicina tradicional, a insatisfação com os serviços, a "
      "depressão, o estigma e a discriminação e o fraco apoio social "
      "{heestermans2016}. Na mesma região, a proporção de pessoas em TARV sem "
      "supressão viral foi estimada em 20,0% {mosha2024}. As estimativas de "
      "adesão variam muito com o método de medida: na Etiópia, a adesão "
      "óptima agregada foi de 79%, mas desceu para 64% quando se usaram "
      "métodos estruturados de avaliação e subiu para 82% com o auto-relato "
      "{gobezie2024}."),
    P("Em Moçambique, o inquérito nacional de impacto do HIV de 2021 (INSIDA "
      "2021) estimou uma prevalência de 12,5% nos adultos com 15 ou mais "
      "anos, o que corresponde a cerca de 2.097.000 adultos a viver com o "
      "vírus, com 15,0% nas mulheres e 9,5% nos homens. Entre os adultos que "
      "conheciam o seu diagnóstico, 96,4% estavam em TARV, e entre os que "
      "estavam em TARV, 89,4% tinham a carga viral suprimida {insida2022}. O "
      "Ministério da Saúde (MISAU) adoptou como primeira linha a combinação "
      "de dose fixa de fumarato de tenofovir disoproxil, lamivudina e "
      "dolutegravir (TLD) e determina que a adesão seja avaliada em todas as "
      "consultas {misau2023}. Os estudos nacionais mostram, porém, que a "
      "adesão continua a ser um desafio: num inquérito em unidades sanitárias "
      "de Maputo e de Nampula, 74,68% dos doentes referiram algum grau de "
      "não adesão nos últimos 30 dias {mandlate2023}, e numa coorte da Zambézia 81% "
      "dos doentes tiveram pelo menos um atraso de 15 ou mais dias no "
      "levantamento dos medicamentos {filimao2019}. Já foram documentados no "
      "país casos de resistência ao dolutegravir em doentes com falência "
      "virológica, o que torna a adesão ainda mais decisiva para preservar a "
      "eficácia do regime actual {ciccacci2025}."),
    P("A província de Nampula apresenta uma situação particular. Com uma "
      "prevalência de 10,0% nos adultos, abaixo da média nacional, tem uma "
      "das mais baixas proporções de supressão viral entre os adultos que "
      "vivem com o HIV, de 47,9%, apenas acima de Cabo Delgado (42,5%) e "
      "muito aquém de Gaza (80,3%) e da média nacional (64,1%) {insida2022}. "
      "O Hospital Central de Nampula (HCN), hospital de referência da "
      "província e da região norte, acompanha adultos em TARV que residem na "
      "cidade e noutros distritos e pode receber doentes que preferem um "
      "hospital de nível superior, quer pela procura de cuidados "
      "especializados quer para proteger a confidencialidade do "
      "diagnóstico, fenómeno descrito na África subsariana como contorno "
      "dos centros de tratamento primários {domapielle2024}. A distância, o custo da "
      "deslocação e o estigma podem, por isso, pesar de forma especial nesta "
      "população, a par dos factores clínicos e familiares descritos na "
      "literatura moçambicana {viisainen2024,carrasco2017}."),
    P("A farmácia é o ponto de contacto mais frequente entre o doente em "
      "TARV e o serviço de saúde, uma vez que o levantamento dos medicamentos "
      "ocorre mesmo nos meses em que não há consulta clínica. O guião "
      "nacional manda avaliar a adesão em todas as consultas de seguimento "
      "e, no doente com carga viral elevada, rever a Ficha Individual de "
      "Levantamento de Anti-retrovirais (FILA) à procura de atrasos e "
      "perguntar quantos comprimidos foram esquecidos na última semana e no "
      "último mês {misau2023}. A intervenção do farmacêutico junto das "
      "pessoas que vivem "
      "com o HIV associou-se, numa meta-análise de 25 estudos, a maior "
      "probabilidade de adesão, com *odds ratio* (OR) de 2,70, e de "
      "supressão viral, com OR de 4,13 {ahmed2022}. Falta, contudo, informação local que permita orientar "
      "esse aconselhamento para os doentes e para os factores de maior "
      "risco."),
    P("Não se encontrou nenhum estudo publicado que tenha medido a adesão à "
      "TARV por contagem de comprimidos no HCN, nem que tenha relacionado a "
      "adesão, nesta população, com a distância à unidade sanitária, o "
      "estigma, os efeitos adversos e o apoio familiar medidos com "
      "instrumentos validados. O presente protocolo propõe um estudo "
      "transversal analítico, a realizar entre Abril e Junho de 2027, para "
      "estimar a proporção de adultos com boa adesão à TARV no HCN, "
      "identificar os factores associados e verificar a relação entre a "
      "adesão e a supressão viral, de modo a fundamentar sessões de "
      "aconselhamento farmacêutico dirigidas."),
]

# ----------------------------------------------------- 2. problema ----------
PROBLEMA = [
    P("O problema que motiva o estudo é a baixa proporção de adultos com "
      "carga viral suprimida na província de Nampula, de 47,9%, muito "
      "abaixo da média nacional de 64,1% {insida2022}. Esta diferença resulta "
      "de lacunas em várias etapas da cascata de cuidados, do diagnóstico à "
      "retenção, mas a adesão diária aos medicamentos é o determinante mais "
      "próximo da supressão viral naqueles que já estão em tratamento e é, "
      "ao mesmo tempo, um dos mais modificáveis {heestermans2016,mosha2024}. "
      "Os instrumentos que as normas nacionais prevêem para avaliar a adesão, "
      "a pergunta sobre doses esquecidas e a revisão das datas de "
      "levantamento na FILA {misau2023}, dependem do relato do doente ou "
      "medem apenas a ida à farmácia. No HCN não há registo sistemático de "
      "uma medida objectiva da toma, como a contagem de comprimidos, nem uma "
      "estimativa da proporção de doentes com adesão insuficiente."),
    P("As consequências da adesão insuficiente são clínicas, sociais e "
      "económicas. A carga viral persistentemente igual ou superior a 1.000 "
      "cópias/mL obriga, segundo as normas nacionais, a três meses de "
      "reforço da adesão e, se não houver resposta, à avaliação pelo comité "
      "terapêutico para mudança de regime {misau2023}, o que implica mais "
      "consultas, mais testes e medicamentos de segunda linha mais caros. Em "
      "Moçambique já foi descrita resistência ao dolutegravir em 13 de 28 "
      "doentes com falência virológica testados após reforço da adesão "
      "{ciccacci2025}. A dimensão social do problema também é visível: no "
      "INSIDA 2021, entre os participantes com anti-retrovirais detectados no "
      "sangue, 14,1% não declararam o seu diagnóstico, e os que tinham carga "
      "viral não suprimida tinham uma probabilidade seis vezes maior de o "
      "ocultar, com *odds ratio* ajustado (ORa) de 6,27 {mccabe2025}, o que sugere uma ligação entre "
      "estigma, ocultação e insucesso terapêutico."),
    P("O que falta saber é quantos adultos seguidos no HCN tomam de facto a "
      "medicação prescrita e que factores explicam a diferença entre os que "
      "aderem e os que não aderem. O auto-relato, que é a forma mais usada na "
      "rotina, tende a sobrestimar a adesão: num estudo queniano, a adesão "
      "foi de 86% por auto-relato e de 58,6% por contagem de comprimidos "
      "{kioko2017}. Sem uma medida objectiva e sem a quantificação local do "
      "peso da distância, do estigma, dos efeitos adversos e do apoio "
      "familiar, a farmácia não consegue identificar os doentes de maior "
      "risco nem ajustar o conteúdo do aconselhamento às barreiras que "
      "efectivamente pesam nesta população."),
]
PERGUNTA = ("Qual é a proporção de adultos em terapêutica anti-retroviral com "
            "boa adesão, medida pela contagem de comprimidos no acto do "
            "levantamento da medicação no Hospital Central de Nampula, e de "
            "que forma a distância à unidade sanitária, o estigma, os efeitos "
            "adversos e o apoio familiar se associam a essa adesão?")
DELIMITACAO = [
    P("O estudo decorre na farmácia que dispensa anti-retrovirais a adultos "
      "no HCN, na cidade de Nampula, e abrange os adultos com 18 ou mais anos "
      "em TARV há pelo menos seis meses que se apresentam pessoalmente para "
      "levantar a medicação entre Abril e Junho de 2027. A carga viral "
      "considerada é a mais recente registada no processo clínico nos 12 "
      "meses anteriores à entrevista. O objecto de estudo é a adesão à toma "
      "dos medicamentos anti-retrovirais, medida pela contagem de "
      "comprimidos e complementada pelo auto-relato e pelo registo de "
      "levantamentos, e a sua associação com a distância à unidade "
      "sanitária, o estigma, os efeitos adversos percebidos e o apoio "
      "familiar."),
    P("Ficam fora do âmbito as crianças e os adolescentes com menos de 18 "
      "anos, as mulheres grávidas e lactantes, que seguem um calendário "
      "próprio de consultas e de levantamentos, os doentes que recebem a "
      "medicação através de representantes, de Grupos de Apoio à Adesão "
      "Comunitária (GAAC) ou da dispensa comunitária, e os doentes nos "
      "primeiros seis meses de tratamento. O estudo não avalia a retenção "
      "nos cuidados nem o efeito de uma intervenção; a proposta de sessões de "
      "aconselhamento farmacêutico é um produto derivado dos resultados e "
      "não uma componente experimental."),
]

# ----------------------------------------------------- 3. objectivos --------
OBJECTIVO_GERAL = ("Avaliar a adesão à terapêutica anti-retroviral e os "
                   "factores associados em adultos seguidos no Hospital "
                   "Central de Nampula, de Abril a Junho de 2027.")
OBJECTIVOS_ESPECIFICOS = [
    "Caracterizar o perfil sociodemográfico, clínico, terapêutico e de acesso "
    "à unidade sanitária (distância, tempo e custo da deslocação) dos adultos "
    "em terapêutica anti-retroviral que levantam a medicação no Hospital "
    "Central de Nampula.",
    "Determinar a proporção de adultos com boa adesão (95% ou mais) pela "
    "contagem de comprimidos no acto do levantamento e a sua concordância "
    "com o auto-relato e com o registo de levantamentos.",
    "Descrever a frequência de efeitos adversos percebidos, o nível de "
    "estigma relacionado com o HIV e o apoio familiar percebido pelos "
    "participantes.",
    "Analisar a associação entre a boa adesão e a distância à unidade "
    "sanitária, o estigma, os efeitos adversos percebidos e o apoio "
    "familiar, com ajustamento para factores sociodemográficos e clínicos.",
    "Analisar a relação entre a adesão medida pela contagem de comprimidos e "
    "a supressão viral registada no processo clínico.",
]

# ----------------------------------------------------- 4. hipoteses ---------
HIPOTESES_INTRO = [
    P("As hipóteses referem-se aos objectivos específicos 4 e 5 e serão "
      "testadas com um nível de significância de 5%. Formulam-se cinco pares "
      "de hipóteses, pela ordem seguinte: tempo de deslocação, estigma, "
      "efeitos adversos, apoio familiar e supressão viral."),
]
HIPOTESES = [
    ("H0", "não existe associação estatisticamente significativa entre o "
           "tempo de deslocação até ao HCN e a boa adesão à TARV."),
    ("H1", "a boa adesão à TARV é menos frequente nos adultos cuja "
           "deslocação até ao HCN demora mais de 60 minutos."),
    ("H0", "não existe associação estatisticamente significativa entre a "
           "pontuação de estigma relacionado com o HIV e a boa adesão."),
    ("H1", "pontuações mais elevadas de estigma associam-se a menor "
           "probabilidade de boa adesão."),
    ("H0", "não existe associação estatisticamente significativa entre a "
           "presença de efeitos adversos percebidos nos últimos 30 dias e a "
           "boa adesão."),
    ("H1", "a boa adesão é menos frequente nos adultos que referem efeitos "
           "adversos nos últimos 30 dias."),
    ("H0", "não existe associação estatisticamente significativa entre a "
           "pontuação de apoio familiar percebido e a boa adesão."),
    ("H1", "pontuações mais elevadas de apoio familiar associam-se a maior "
           "probabilidade de boa adesão."),
    ("H0", "a proporção de carga viral suprimida (menos de 1.000 cópias/mL) "
           "não difere entre os adultos com boa adesão e os adultos com "
           "adesão subóptima."),
    ("H1", "a proporção de carga viral suprimida é maior nos adultos com boa "
           "adesão do que nos adultos com adesão subóptima."),
]
QUESTOES = [
    "Qual é o perfil sociodemográfico, clínico, terapêutico e de acesso à "
    "unidade sanitária dos adultos em TARV que levantam a medicação no HCN?",
    "Que proporção destes adultos tem boa adesão pela contagem de comprimidos "
    "e em que medida essa classificação concorda com o auto-relato e com o "
    "registo de levantamentos?",
    "Com que frequência são referidos efeitos adversos e quais são os níveis "
    "de estigma relacionado com o HIV e de apoio familiar percebido?",
]

# ----------------------------------------------------- 5. justificativa -----
JUSTIFICATIVA_INTRO = [
    P("A escolha do tema justifica-se pela coincidência de três factos: "
      "Nampula tem uma das mais baixas proporções de supressão viral do país "
      "{insida2022}, a adesão é o determinante modificável mais próximo "
      "dessa supressão {heestermans2016}, e a farmácia do HCN contacta todos "
      "os meses ou todos os trimestres com os doentes em TARV sem dispor de "
      "uma medida objectiva da adesão. Um estudo que meça a adesão com rigor "
      "e identifique os factores associados responde a uma necessidade do "
      "serviço e produz conhecimento aplicável noutras unidades da região."),
]
JUSTIFICATIVA = {
    "cientifica": [
        P("Do ponto de vista científico, o estudo produz a primeira estimativa "
          "da adesão à TARV por contagem de comprimidos no HCN na era do "
          "dolutegravir e compara-a com o auto-relato e com o registo de "
          "levantamentos na mesma pessoa. Esta comparação é relevante porque "
          "a diferença entre métodos pode ultrapassar 25 pontos percentuais "
          "{kioko2017} e porque as meta-análises africanas mostram "
          "estimativas muito diferentes consoante a medida usada "
          "{gobezie2024}. O estudo verifica ainda se o limiar clássico de "
          "95% {paterson2000} discrimina a supressão viral num regime com "
          "inibidor da integrase, para o qual dados de vida real sugerem "
          "que níveis de adesão mais baixos podem bastar {byrd2019}."),
        P("A adaptação para português e emakhuwa da escala curta de estigma "
          "e da escala multidimensional de apoio social percebido, com "
          "avaliação da validade de conteúdo e da fiabilidade, acrescenta "
          "evidência psicométrica numa população moçambicana, lacuna "
          "assinalada na revisão das traduções desta última escala, muitas "
          "das quais não foram rigorosamente traduzidas nem pré-testadas "
          "{dambi2018}."),
    ],
    "academica": [
        P("No plano académico, o estudo integra o estudante de Farmácia da "
          "Universidade Lúrio na investigação em farmácia clínica, num "
          "hospital de ensino, com aplicação de competências de desenho de "
          "estudos, medição da adesão, adaptação de instrumentos e análise "
          "multivariável. Os resultados servem de base a trabalhos futuros "
          "da faculdade, nomeadamente a um ensaio de aconselhamento "
          "farmacêutico semelhante ao que, no Paquistão, aumentou a adesão e "
          "a contagem de linfócitos T auxiliares (CD4) em oito semanas "
          "{chatha2020}, e "
          "reforçam a ligação entre o ensino farmacêutico e os serviços de "
          "TARV."),
    ],
    "social": [
        P("A relevância social decorre das consequências da adesão para o "
          "doente, para a família e para a comunidade. A supressão viral "
          "protege a saúde do próprio e, quando a carga viral deixa de ser "
          "detectável, elimina o risco de transmissão sexual {who2023}. "
          "Conhecer o peso do estigma e do apoio familiar permite envolver "
          "a família de forma mais eficaz: as intervenções com apoiantes do "
          "tratamento, incluindo familiares, aumentaram a adesão em 7,6% na "
          "África subsariana {nyoni2020}. Ao identificar os doentes de maior "
          "risco, o estudo ajuda a evitar falências terapêuticas, "
          "internamentos e a passagem a regimes de segunda linha, com ganhos "
          "para os doentes e para o sistema de saúde."),
    ],
    "politica": [
        P("No plano político, o estudo responde às orientações do MISAU, que "
          "determinam a avaliação da adesão em todas as consultas e a "
          "elaboração de planos de melhoria da adesão {misau2023}, que "
          "colocam o aconselhamento de adesão no centro do apoio "
          "psicossocial {misau2015} e que expandiram os Modelos "
          "Diferenciados de Serviços (MDS) com dispensa trimestral e "
          "semestral {misaumds2023}. Os resultados fornecem à direcção do HCN "
          "e à Direcção Provincial de Saúde de Nampula dados para orientar "
          "recursos de apoio à adesão numa província que está longe da meta "
          "de 95% de supressão viral {unaids2021,insida2022}, e sustentam o "
          "reconhecimento do farmacêutico como agente de adesão, cujo "
          "benefício está documentado {ahmed2022}."),
    ],
}

# ----------------------------------------------------- 6. revisao -----------
REVISAO = [
    ("Terapêutica anti-retroviral e conceito de adesão", [
        P("A OMS define a adesão como o grau em que o comportamento da "
          "pessoa, na toma dos medicamentos, no cumprimento de uma dieta ou "
          "na mudança de estilos de vida, corresponde às recomendações "
          "acordadas com o profissional de saúde {anghel2019}. A definição "
          "sublinha o acordo entre o doente e o profissional e distingue a "
          "adesão da simples obediência a uma prescrição. No caso da TARV, "
          "importa separar a adesão à toma, que diz respeito à regularidade "
          "diária das doses, da retenção nos cuidados, que diz respeito à "
          "permanência no programa e ao comparecimento nas consultas e nos "
          "levantamentos. O presente estudo centra-se na primeira, usando a "
          "segunda como informação complementar."),
        P("O limiar de 95% das doses tomadas, usado desde o início da era da "
          "terapêutica combinada, tem origem num estudo com monitorização "
          "electrónica em que a falência virológica ocorreu em 22% dos "
          "doentes com adesão de 95% ou mais, em 61% dos doentes com adesão "
          "entre 80% e 94,9% e em 80% dos doentes com adesão inferior a 80% "
          "{paterson2000}. Os regimes actuais são mais potentes e mais "
          "tolerantes a falhas ocasionais: em dados de vida real, a adesão "
          "necessária para obter supressão em 90% das determinações de carga "
          "viral foi de 82% no conjunto e de 75% nos regimes com inibidor da "
          "integrase {byrd2019}. Por essa razão, o estudo mantém os 95% como "
          "definição principal de boa adesão, para comparabilidade com a "
          "literatura, e analisa os limiares de 90% e de 80% como análises de "
          "sensibilidade."),
        P("Em Moçambique, a primeira linha para adultos é a combinação TLD; "
          "a alternativa com abacavir, lamivudina e dolutegravir destina-se "
          "aos doentes com depuração da creatinina igual ou inferior a 60 "
          "mL/min, e a combinação de tenofovir e lamivudina com atazanavir "
          "potenciado aos doentes com intolerância ao dolutegravir "
          "{misau2023}. Numa meta-análise em rede que informou as "
          "recomendações da OMS, o dolutegravir, comparado com o efavirenz, "
          "aumentou a probabilidade de supressão viral às 96 semanas (OR 1,94), "
          "protegeu contra a resistência (OR 0,13) e reduziu as interrupções "
          "de tratamento (OR 0,58) {kanters2020}. A supressão viral é "
          "definida pelo MISAU como carga viral inferior a 1.000 cópias/mL "
          "{misau2023}; a OMS distingue a carga viral não detectável, a "
          "suprimida (detectável mas igual ou inferior a 1.000 cópias/mL) e "
          "a não suprimida {who2023}."),
    ]),
    ("Magnitude e consequências da adesão insuficiente", [
        P("A adesão à TARV na África subsariana está longe de ser "
          "uniforme. A revisão de Heestermans e colaboradores, com 146 "
          "estudos, encontrou uma adesão média de 72,9% {heestermans2016}. Na "
          "Etiópia, duas meta-análises recentes estimaram uma não adesão "
          "agregada de 20,68% {aytenew2024} e uma adesão óptima de 79% "
          "{gobezie2024}, com grande heterogeneidade entre estudos. Nos "
          "estudos primários, os valores vão de 34% no Gana {nutor2023} a "
          "97,1% num hospital terciário da Nigéria {ogbonnaya2024}, amplitude "
          "que reflecte tanto diferenças reais entre populações como "
          "diferenças nos métodos e nos limiares usados."),
        P("Em Moçambique, a evidência sobre a adesão é ainda escassa e "
          "provém sobretudo de auto-relato, de registos de levantamento e de "
          "estudos qualitativos. Num inquérito em Maputo e em Nampula, com o "
          "auto-relato de três itens, 74,68% dos participantes referiram algum "
          "grau de não adesão em pelo menos uma das perguntas relativas aos "
          "últimos 30 dias {mandlate2023}. Na Zambézia, 81% dos doentes que "
          "iniciaram a TARV tiveram atrasos de 15 ou mais dias no "
          "levantamento, e os que residiam em zona urbana tiveram menor risco "
          "de atraso {filimao2019}. Os grupos comunitários de adesão "
          "melhoraram a retenção aos seis meses (93% contra 77%) e a supressão "
          "viral (ORa 1,14) {deschacht2023}."),
        P("As consequências da adesão insuficiente acumulam-se ao longo da "
          "cascata. Na região, dois em cada dez adultos em TARV não têm a "
          "carga viral suprimida, e a adesão subóptima, a falta de apoio "
          "familiar e social, o estigma, a depressão e o consumo de álcool "
          "estão entre os factores associados a essa falta de supressão "
          "{mosha2024}. A replicação persistente selecciona resistências: num "
          "estudo em centros moçambicanos, 13 de 28 doentes em falência "
          "virológica com regimes baseados em dolutegravir tinham "
          "resistência a este fármaco, e todos os que foram testados para "
          "outras classes tinham também co-resistência {ciccacci2025}. A "
          "falta de supressão mantém, além disso, a possibilidade de "
          "transmissão do vírus {who2023}."),
    ]),
    ("Determinantes relacionados com o acesso e com o tratamento", [
        P("A distância e o custo da deslocação são barreiras estruturais "
          "recorrentes. Na região de Amhara, na Etiópia, os doentes que "
          "percorriam mais de 10 km até à clínica tiveram maior "
          "probabilidade de não adesão (ORa 2,42) {aychiluhm2021}, e a "
          "meta-análise etíope identificou a falta de acesso à unidade "
          "sanitária como preditor independente (ORa 3,86) {aytenew2024}. A "
          "residência urbana associou-se a melhor adesão numa meta-análise "
          "de sete estudos (OR 2,07) {fite2021}. Num hospital terciário da "
          "Nigéria, a falta de dinheiro para o transporte até ao hospital "
          "(75%) encabeçou a lista de factores que afectavam a adesão "
          "{anyaike2019}. Em "
          "sentido contrário, alguns doentes percorrem voluntariamente "
          "distâncias maiores para serem seguidos num hospital de nível "
          "superior, quer pela procura de cuidados especializados quer para "
          "ocultar o diagnóstico {domapielle2024}, o que torna a relação "
          "entre distância e adesão menos linear num hospital central."),
        P("Os MDS procuram reduzir o peso das deslocações. Em Moçambique, a "
          "circular de 2023 prevê que, aos 12 meses de TARV, os doentes "
          "elegíveis sejam avaliados para a dispensa trimestral com consulta "
          "semestral, para os GAAC, para a dispensa comunitária e para a "
          "dispensa semestral {misaumds2023}. No sul do país, a dispensa "
          "trimestral reduziu para metade o risco de abandono nos adultos já "
          "estabelecidos em tratamento, com razão de riscos instantâneos "
          "ajustada (HRa) de 0,50 {sauralazaro2024}. O "
          "modelo de dispensa é, por isso, uma variável a considerar na "
          "relação entre distância e adesão."),
        P("Os efeitos adversos, reais ou percebidos, constituem o segundo "
          "grupo de factores. O guião nacional descreve efeitos geralmente não "
          "graves comuns a vários anti-retrovirais, como náuseas, vómitos, "
          "diarreia, cefaleias e tonturas, e refere a insónia como efeito "
          "mais frequente com o dolutegravir do que com o efavirenz "
          "{misau2023}. Num hospital terciário nigeriano, 17,1% dos doentes em "
          "regime com dolutegravir referiram reacções adversas, sobretudo "
          "cefaleias (9,7%), prurido (3,1%) e erupção cutânea (2,7%), com "
          "aumento médio de peso de 0,9 kg {ogbonnaya2024}. No Quénia, o peso "
          "dos efeitos secundários foi um dos preditores da adesão "
          "{kioko2017}. As queixas de toxicidade figuram também entre as "
          "barreiras que o guião nacional manda investigar quando a carga "
          "viral está elevada {misau2023}."),
    ]),
    ("Determinantes psicossociais: estigma, apoio familiar e álcool", [
        P("O estigma relacionado com o HIV actua sobre a adesão por várias "
          "vias. Uma revisão de 38 estudos confirmou a associação entre "
          "estigma e dificuldades de adesão e propôs como mecanismos a maior "
          "vulnerabilidade a problemas de saúde mental, a redução da "
          "auto-eficácia e o receio de revelação inadvertida do diagnóstico "
          "{sweeney2016}. Na Etiópia, tomar os comprimidos com desconforto na "
          "presença de outras pessoas associou-se fortemente à não adesão "
          "(ORa 5,21) {aytenew2024}, e 57,8% dos adultos em TARV de Wolaita "
          "referiram estigma percebido elevado {alemu2022}. Em Moçambique, "
          "estudos qualitativos mostram que o estigma é sobretudo moral, "
          "ligado à ideia de responsabilidade pessoal {carrasco2017}, e que "
          "interage com as normas de género: as mulheres interrompem o "
          "tratamento por receio da reacção do parceiro, enquanto os homens "
          "revelam estigma internalizado e adiam o tratamento por estigma "
          "antecipado e pela norma de força masculina {viisainen2024}."),
        P("O apoio familiar é, em sentido inverso, um facilitador. Uma revisão "
          "de 33 estudos em 15 países de rendimento baixo e médio mostrou que "
          "o apoio dado no agregado familiar depende das normas de género, da "
          "escolaridade, das crenças religiosas e culturais e da situação "
          "económica, e que o estigma gera segredo em torno da toma dos "
          "medicamentos {campbell2020}. No Gana, o apoio interpessoal elevado "
          "associou-se a maior adesão (ORa 3,45) {nutor2023}, e em Moçambique "
          "o apoio do parceiro, da mãe ou de outros familiares facilitou a "
          "adesão de homens e de mulheres {viisainen2024}. As intervenções "
          "com apoiantes do tratamento aumentaram a adesão medida por "
          "contagem de comprimidos {nyoni2020}."),
        P("O consumo de álcool e a saúde mental completam o quadro de "
          "factores psicossociais. Na África subsariana, os consumidores de "
          "álcool tiveram o dobro da probabilidade de não adesão (34% contra "
          "18%; OR 2,25) {velloza2020}, e na Nigéria o consumo de álcool "
          "associou-se a menor adesão auto-referida (OR 0,382) {isika2022}. Em Moçambique, a presença de "
          "qualquer perturbação mental associou-se a falhar pelo menos uma "
          "dose nos últimos 30 dias (OR 1,45) {mandlate2023}. Estes factores "
          "entram no estudo como variáveis de ajustamento, porque podem "
          "confundir a relação entre estigma, apoio familiar e adesão."),
    ]),
    ("Enquadramento normativo moçambicano", [
        P("O guião de cuidados do HIV de 2023 do MISAU estabelece que, em "
          "todas as consultas de seguimento, se avaliem a toxicidade dos "
          "anti-retrovirais e a adesão ao tratamento {misau2023}. A carga "
          "viral de rotina é pedida seis meses após o início ou a mudança de "
          "regime e, depois, anualmente; perante uma carga viral igual ou "
          "superior a 1.000 cópias/mL, o doente recebe apoio psicossocial e "
          "reforço da adesão durante três meses consecutivos, repete a carga "
          "viral e, se esta se mantiver elevada, é submetido ao comité "
          "terapêutico {misau2023}. Na avaliação da adesão, o guião manda "
          "rever a FILA e a ficha mestra à procura de atrasos, perguntar "
          "quantos comprimidos foram esquecidos na última semana e no último "
          "mês e investigar barreiras como o consumo de álcool, a falta de "
          "revelação do diagnóstico, as queixas de toxicidade, a depressão, "
          "a pobreza, a falta de apoio familiar, a falta de dinheiro para o "
          "transporte e as crenças alternativas sobre a doença {misau2023}. "
          "As reacções adversas devem ser notificadas ao sector de "
          "farmacovigilância através da ficha nacional de notificação "
          "{misau2023}."),
        P("A directriz nacional de apoio psicossocial e prevenção positiva "
          "define o pacote de actividades de apoio ao doente, que inclui o "
          "aconselhamento de adesão após o início da TARV, o aconselhamento "
          "para a revelação do diagnóstico, os grupos de apoio, os GAAC e a "
          "busca activa consentida dos faltosos {misau2015}. A circular de "
          "2023 sobre os MDS alinha no mesmo dia a consulta clínica, a "
          "consulta de apoio psicossocial e o levantamento dos medicamentos "
          "e define os critérios de passagem para os modelos de levantamento "
          "trimestral e semestral {misaumds2023}. O enquadramento nacional "
          "reconhece, assim, a adesão como responsabilidade partilhada entre "
          "a consulta clínica, o apoio psicossocial e a farmácia, mas não "
          "prevê uma medida objectiva de adesão no acto do levantamento, "
          "espaço que o presente estudo explora."),
    ]),
    ("Métodos de medição da adesão e instrumentos", [
        P("Não existe um método de referência perfeito para medir a adesão. "
          "Os métodos indirectos mais usados são a contagem de comprimidos, "
          "que é simples mas não prova a ingestão; o registo de levantamentos "
          "na farmácia, que mede a posse do medicamento e usa habitualmente o "
          "limiar de 80%; e o auto-relato, barato e simples, mas com tendência "
          "a sobrestimar a adesão, pelo que se recomenda combinar pelo menos "
          "dois métodos {anghel2019}. A discordância entre métodos está bem "
          "documentada: no Quénia, 86% por auto-relato e 58,6% por contagem de "
          "comprimidos {kioko2017}; no Uganda, coeficientes de concordância "
          "entre 0,410 e 0,545 e fraca capacidade de todos os métodos para "
          "prever a supressão viral {kizito2026}. Apesar disso, a adesão de "
          "95% ou mais, por qualquer dos métodos, associou-se a melhor "
          "resposta ao tratamento em mulheres quenianas {mudhune2018}."),
        P("O auto-relato de três itens desenvolvido por Wilson e "
          "colaboradores pergunta, para os últimos 30 dias, em quantos dias "
          "falhou pelo menos uma dose, como avalia a forma como tomou os "
          "medicamentos e com que frequência os tomou como devia; teve alfa "
          "de Cronbach de 0,83 e correlacionou-se com a monitorização "
          "electrónica (r=0,47) {wilson2016}. Na Cidade do Cabo, o mesmo "
          "instrumento mostrou consistência interna, estabilidade temporal e "
          "validade face à contagem de comprimidos e à carga viral "
          "{kalichman2024}, e foi já usado em Moçambique, em unidades "
          "sanitárias de Maputo e de Nampula {mandlate2023}."),
        P("A escala curta de estigma relacionado com o HIV tem 12 itens, três "
          "por cada uma das subescalas de estigma personalizado, "
          "preocupações com a revelação, preocupações com as atitudes "
          "públicas e auto-imagem negativa, respondidos numa escala de quatro "
          "pontos; derivada da escala original de 40 itens, reproduziu a "
          "estrutura de quatro factores, com alfas superiores a 0,70 em "
          "todas as subescalas {reinius2017}. A "
          "versão em português do Brasil obteve alfa de 0,83 {luz2020} e, no "
          "Quénia, a escala mostrou alfa de 0,80, coeficiente de correlação "
          "intraclasse de 0,92 no teste-reteste e bom ajustamento na análise "
          "factorial confirmatória {wanjala2022}."),
        P("A escala multidimensional de apoio social percebido (MSPSS) tem 12 "
          "itens distribuídos por três fontes de apoio, a família, os amigos "
          "e uma pessoa significativa, respondidos numa escala de sete "
          "pontos, de «discordo muito fortemente» a «concordo muito "
          "fortemente», com boa consistência interna e validade factorial na "
          "amostra original {zimet1988}. A escala foi traduzida para 22 "
          "línguas e a maioria das versões atingiu um alfa de Cronbach de "
          "pelo menos 0,70, mas 16 dessas 22 traduções não seguiram um "
          "processo rigoroso de tradução e retroversão, de reconciliação ou "
          "de pré-teste {dambi2018}. Para o consumo de "
          "álcool, a versão de três "
          "itens do teste de identificação de perturbações do uso de álcool "
          "(AUDIT-C) teve, na Zâmbia, com o ponto de corte de 3 e tomando o "
          "teste completo como referência, sensibilidade superior a 80% e "
          "especificidade superior a 76% nos homens e sensibilidade superior "
          "a 84% e especificidade superior a 88% nas mulheres "
          "{inoue2021}."),
    ]),
    ("Intervenções farmacêuticas e aconselhamento para a adesão", [
        P("A participação do farmacêutico no cuidado às pessoas que vivem com "
          "o HIV tem efeito documentado. Uma meta-análise de 25 estudos, com "
          "3.206 doentes, mostrou que a intervenção farmacêutica, isolada ou "
          "integrada numa equipa, aumentou a adesão (OR 2,70), a supressão "
          "viral (OR 4,13) e a contagem de linfócitos CD4, embora a "
          "qualidade da evidência variasse entre moderada e muito baixa "
          "{ahmed2022}. Num ensaio aleatorizado no Paquistão, o "
          "aconselhamento conduzido por farmacêuticos aumentou a "
          "probabilidade de os doentes referirem não falhar a medicação "
          "durante períodos longos e de a falharem com menos frequência "
          "{chatha2020}."),
        P("A evidência africana aponta para intervenções que combinam "
          "aconselhamento, envolvimento da família e apoio comunitário. As "
          "intervenções com apoiantes do tratamento aumentaram a adesão em "
          "7,6% e a supressão viral em 5% face aos cuidados habituais, com "
          "efeito mais claro nos contextos comunitários {nyoni2020}, e os "
          "GAAC melhoraram a retenção e a supressão viral em Moçambique "
          "{deschacht2023}. Um programa de aconselhamento farmacêutico no "
          "HCN será mais eficaz se for dirigido aos factores que, nesta "
          "população, se associam de facto à adesão, o que justifica a "
          "abordagem analítica do presente estudo."),
    ]),
]

# ----------------------------------------------------- 7. estado da arte ----
ESTADO_ARTE = [
    P("O [[quadro:estado_arte]] sintetiza estudos empíricos publicados nos "
      "últimos dez anos sobre a adesão à TARV e os seus determinantes em "
      "adultos, com prioridade para Moçambique e para a África subsariana, "
      "indicando o local, o desenho, a dimensão da amostra e os principais "
      "resultados numéricos."),
    QUADRO("estado_arte",
           "Síntese de estudos sobre a adesão à terapêutica anti-retroviral "
           "e factores associados (estado da arte)",
           ["Autor (ano)", "Local", "Desenho (n)", "Principais resultados"],
           [
               ["Mandlate et al. (2023) {mandlate2023}",
                "Moçambique (Maputo e Nampula)", "Transversal (395)",
                "Auto-relato de três itens: 74,68% com algum grau de não "
                "adesão nos últimos 30 dias; qualquer perturbação mental "
                "associada a falhar doses (OR 1,45; IC95% 1,01-2,10)."],
               ["Filimão et al. (2019) {filimao2019}",
                "Moçambique (Zambézia)", "Coorte retrospectiva (1.413)",
                "81% com atraso de 15 ou mais dias no levantamento; "
                "residência urbana protectora (HRa 0,754); não pertencer a "
                "GAAC aumentou o risco de atraso (HRa 1,431)."],
               ["De Schacht et al. (2023) {deschacht2023}",
                "Moçambique (Zambézia)",
                "Coorte retrospectiva emparelhada (26.858)",
                "Retenção aos seis meses de 93% nos membros de GAAC e de 77% "
                "nos restantes; supressão viral superior nos membros de GAAC "
                "(ORa 1,14)."],
               ["Viisainen et al. (2024) {viisainen2024}", "Moçambique",
                "Qualitativo (139 entrevistas)",
                "Estigma antecipado frequente; mulheres interrompem por medo "
                "da reacção do parceiro; homens com estigma internalizado; "
                "apoio do parceiro ou da família facilita a adesão."],
               ["Aychiluhm et al. (2021) {aychiluhm2021}",
                "Etiópia (Amhara)", "Transversal (326)",
                "Não adesão de 17,4%; distância superior a 10 km (ORa 2,42), "
                "ausência de escolaridade (ORa 5,57) e consumo de "
                "substâncias (ORa 3,57) associados à não adesão."],
               ["Kioko e Pertet (2017) {kioko2017}", "Quénia (Machakos)",
                "Transversal comunitário (301)",
                "Adesão de 86% por auto-relato e de 58,6% por contagem de "
                "comprimidos (limiar de 95%); peso dos efeitos secundários e "
                "estado civil como preditores."],
               ["Anyaike et al. (2019) {anyaike2019}",
                "Nigéria (Ilorin, hospital terciário)", "Transversal (550)",
                "Adesão de 92,6% por auto-relato; falta de dinheiro para o "
                "transporte (75%) e efeitos secundários entre os motivos de "
                "falha."],
               ["Isika et al. (2022) {isika2022}", "Nigéria (Cross River)",
                "Transversal (999)",
                "Adesão auto-referida (95% ou mais das doses em sete dias) "
                "de 60,1%; consumo de álcool associado a menor adesão "
                "(OR 0,382)."],
               ["Ogbonnaya et al. (2024) {ogbonnaya2024}",
                "Nigéria (hospital terciário)",
                "Revisão de processos (515, dolutegravir)",
                "Adesão auto-referida de 97,1%; reacções adversas em 17,1% "
                "(cefaleia 9,7%); supressão viral de 94,4%; aumento médio de "
                "peso de 0,9 kg."],
               ["Nutor et al. (2023) {nutor2023}", "Gana (Volta)",
                "Transversal (181)",
                "Adesão de 34%; apoio interpessoal elevado associado a boa "
                "adesão (ORa 3,45); depressão sem associação no modelo "
                "ajustado."],
               ["Alemu et al. (2022) {alemu2022}", "Etiópia (Wolaita)",
                "Transversal (638)",
                "Escala curta de 12 itens: 57,8% com estigma percebido "
                "elevado; fraco apoio social (ORa 2,05) e não revelação "
                "(ORa 1,657) associados ao estigma."],
               ["Mudhune et al. (2018) {mudhune2018}", "Quénia",
                "Coorte (463 com contagem)",
                "Adesão de 95% ou mais por contagem, auto-relato, "
                "monitorização electrónica ou doseamento associada a "
                "resposta favorável ao tratamento."],
               ["Kalichman et al. (2024) {kalichman2024}",
                "África do Sul (Cidade do Cabo)", "Validação (1.022)",
                "Auto-relato de três itens fiável e válido face à contagem "
                "de comprimidos e à carga viral; área sob a curva de 0,646 "
                "para o limiar de 75%."],
               ["Kizito et al. (2026) {kizito2026}", "Uganda (Masaka)",
                "Transversal (702 adolescentes)",
                "Concordância entre métodos de 0,410 a 0,545; só o "
                "auto-relato se associou à supressão viral (OR 2,16)."],
           ],
           larguras=[3.3, 2.5, 2.8, 7.4],
           fonte="Elaboração própria (2026), a partir das fontes citadas."),
    P("A leitura do quadro mostra três padrões. Primeiro, as estimativas de "
      "adesão variam entre 34% e 97,1%, e a variação acompanha de perto o "
      "método: os valores mais altos provêm do auto-relato e da revisão de "
      "processos, e os mais baixos de medidas estruturadas ou da contagem de "
      "comprimidos, com diferenças que chegam a 27 pontos percentuais na "
      "mesma amostra {kioko2017}. Segundo, a distância e o custo da "
      "deslocação, o consumo de álcool, o estigma e o apoio familiar surgem "
      "de forma consistente como determinantes, mas cada estudo mede-os com "
      "instrumentos próprios, o que dificulta a comparação e a síntese. "
      "Terceiro, os estudos que usaram o limiar de 95% encontraram "
      "associação com a resposta virológica {mudhune2018}, enquanto os "
      "estudos mais recentes, em populações tratadas com regimes mais "
      "potentes, mostram capacidade limitada de todos os métodos para prever "
      "a supressão {kizito2026,kalichman2024}."),
    P("A evidência moçambicana assenta no auto-relato {mandlate2023}, nos "
      "registos de levantamento {filimao2019,deschacht2023} e em estudos "
      "qualitativos {viisainen2024}. Nenhum dos estudos identificados mediu a "
      "adesão por contagem de comprimidos em Nampula nem avaliou em conjunto, "
      "com escalas validadas, a distância, o estigma, os efeitos adversos e o "
      "apoio familiar em doentes tratados com dolutegravir. O presente "
      "estudo preenche esta lacuna, combina três métodos de medida na mesma "
      "pessoa e relaciona-os com a supressão viral registada no processo "
      "clínico."),
]
ESQUEMA_TEXTO = [
    P("A [[figura:esquema]] representa o modelo conceptual do estudo, "
      "construído a partir dos determinantes descritos na revisão da "
      "literatura {heestermans2016,misau2023}. Quatro grupos de factores "
      "(acesso à unidade sanitária, factores relacionados com o tratamento, "
      "factores psicossociais e factores sociodemográficos) influenciam a "
      "adesão à TARV medida pela contagem de comprimidos, que é o desfecho "
      "principal. A adesão, por sua vez, condiciona a supressão viral, "
      "analisada como consequência no objectivo específico 5. O consumo de "
      "álcool, a revelação do diagnóstico, o tempo em TARV e o modelo de "
      "dispensa são tratados como variáveis de confundimento na análise "
      "multivariável."),
]
ESQUEMA_TITULO = ("Esquema conceptual dos factores associados à adesão à "
                  "terapêutica anti-retroviral no Hospital Central de Nampula")
ESQUEMA = {
    "contexto": ("Adultos em TARV que levantam a medicação no HCN, Abril a "
                 "Junho de 2027"),
    "blocos": [
        ("Acesso à unidade sanitária",
         ["tempo de deslocação (mais de 60 minutos)",
          "distância e distrito de residência",
          "custo do transporte de ida e volta"]),
        ("Factores relacionados com o tratamento",
         ["efeitos adversos percebidos nos últimos 30 dias",
          "regime terapêutico e número de comprimidos por dia"]),
        ("Factores psicossociais",
         ["estigma relacionado com o HIV (escala de 12 itens)",
          "apoio familiar percebido (MSPSS)"]),
        ("Factores sociodemográficos",
         ["idade, sexo e estado civil",
          "escolaridade, ocupação e rendimento"]),
    ],
    "desfecho": ("Adesão à TARV por contagem de comprimidos",
                 ["boa adesão (95% ou mais)",
                  "adesão subóptima (menos de 95%)",
                  "consequência analisada: supressão viral (menos de 1.000 "
                  "cópias/mL)"]),
    "moderadores": ("Variáveis de confundimento",
                    ["consumo de álcool (AUDIT-C)",
                     "revelação do diagnóstico",
                     "tempo em TARV",
                     "modelo de dispensa"]),
}

# ----------------------------------------------------- 8. metodologia -------
METODOLOGIA = [
    ("Tipo e desenho do estudo", [
        P("Trata-se de um estudo observacional, transversal, descritivo e "
          "analítico, de base hospitalar e abordagem quantitativa. A adesão é "
          "medida num único momento, o do levantamento da medicação, por três "
          "métodos aplicados à mesma pessoa: a contagem de comprimidos, que é "
          "a medida principal, o auto-relato de três itens e o registo de "
          "levantamentos na FILA. Os factores de exposição são recolhidos por "
          "entrevista estruturada e a carga viral é extraída do processo "
          "clínico. O desenho transversal é adequado para estimar a "
          "proporção de doentes com boa adesão e para analisar associações, "
          "mas não permite estabelecer relações de causalidade. O relato "
          "seguirá a declaração Strengthening the Reporting of "
          "Observational Studies in Epidemiology (STROBE) {vonelm2007}."),
    ]),
    ("Local e período do estudo", [
        P("O estudo decorre no HCN, na cidade de Nampula, hospital central e "
          "de ensino, na farmácia que dispensa anti-retrovirais a adultos "
          "[confirmar junto da direcção do HCN a designação e a localização "
          "actuais da farmácia de dispensa de anti-retrovirais a adultos]. "
          "Nesta farmácia, cada levantamento é registado na FILA, que contém "
          "a data do levantamento, o medicamento, a dosagem, a quantidade "
          "aviada e a data do próximo levantamento, e no sistema electrónico "
          "de dispensa em uso [confirmar o sistema em uso junto da "
          "farmácia]. O processo clínico e a ficha mestra de cada doente "
          "ficam no serviço de TARV do mesmo hospital."),
        P("A recolha de dados decorre de 1 de Abril a 30 de Junho de 2027, "
          "nos dias úteis, durante o horário de funcionamento da farmácia. "
          "A carga viral considerada é a mais recente registada nos 12 meses "
          "anteriores à data da entrevista, o que abrange resultados de Abril "
          "de 2026 a Junho de 2027. O estudo, no seu conjunto, decorre de "
          "Outubro de 2026 a Setembro de 2027, e a recolha só começa depois "
          "da aprovação do comité de bioética e das autorizações "
          "institucionais."),
    ]),
    ("População e unidade de análise", [
        P("A população-alvo é constituída pelos adultos que vivem com o HIV "
          "em TARV seguidos no HCN. A população acessível são os adultos com "
          "18 ou mais anos, em TARV há pelo menos seis meses, que se "
          "apresentam pessoalmente na farmácia para levantar anti-retrovirais "
          "durante o período de recolha. O número de adultos em TARV "
          "seguidos no HCN e o número de levantamentos mensais de adultos na "
          "farmácia serão obtidos junto da direcção do hospital antes do "
          "início da recolha [confirmar junto da direcção do HCN e do serviço "
          "de TARV]."),
        P("A unidade de análise é o doente. Cada doente é incluído uma única "
          "vez: se voltar à farmácia durante o período de recolha, não é "
          "novamente seleccionado, o que se verifica através de uma lista de "
          "controlo, guardada à parte, com o número de identificação do "
          "processo dos já entrevistados. A contagem de comprimidos refere-se "
          "ao intervalo entre o levantamento anterior registado na FILA e o "
          "levantamento do dia da entrevista."),
    ]),
    ("Amostra e cálculo do tamanho da amostra", [
        P("O tamanho mínimo da amostra para o objectivo descritivo principal, "
          "a proporção de adultos com boa adesão por contagem de comprimidos, "
          "foi calculado pela fórmula para estimar uma proporção:"),
        FORMULA("n<sub>0</sub> = Z<sup>2</sup> × p × (1 - p) / d<sup>2</sup>"),
        P("Em que Z = 1,96 corresponde a um nível de confiança de 95%; p é a "
          "proporção esperada de boa adesão, fixada em 0,5 porque não existe "
          "estimativa por contagem de comprimidos no HCN e as estimativas "
          "publicadas na região variam entre 34% e 97,1% "
          "{nutor2023,ogbonnaya2024}, sendo este o valor que maximiza a "
          "amostra; e d = 0,05 é a margem de erro absoluta. Substituindo:"),
        FORMULA("n<sub>0</sub> = 1,96<sup>2</sup> × 0,5 × 0,5 / "
                "0,05<sup>2</sup> = 384,16, arredondado para 385"),
        P("Como o número de adultos em TARV no HCN ainda não está confirmado, "
          "a [[tabela:cenarios_n]] apresenta o efeito da correcção para "
          "população finita, n<sub>c</sub> = n<sub>0</sub> / [1 + "
          "(n<sub>0</sub> - 1) / N], em vários cenários de N. A correcção "
          "reduziria a amostra para valores entre 307 e 378, mas não será "
          "aplicada, porque o cálculo de poder para os objectivos analíticos, "
          "apresentado a seguir, exige 337 contagens válidas e a regressão "
          "logística beneficia de mais eventos; mantém-se por isso "
          "n<sub>0</sub> = 385 contagens válidas como alvo."),
        TABELA("cenarios_n",
               "Tamanho da amostra com correcção para população finita, "
               "segundo o número de adultos em TARV no HCN",
               ["Adultos em TARV no HCN (N)",
                "Amostra corrigida (n<sub>c</sub>)", "Decisão"],
               [["1.500", "307", "Manter 385 (poder analítico)"],
                ["3.000", "342", "Manter 385 (poder analítico)"],
                ["5.000", "358", "Manter 385 (poder analítico)"],
                ["10.000", "371", "Manter 385 (poder analítico)"],
                ["20.000", "378", "Manter 385 (poder analítico)"]],
               larguras=[5.2, 4.6, 6.2],
               fonte="Elaboração própria (2026). Z = 1,96; p = 0,5; "
                     "d = 0,05."),
        P("Para o objectivo específico 4, verificou-se o poder para comparar "
          "a proporção de boa adesão entre os adultos cuja deslocação demora "
          "mais de 60 minutos (grupo 1) e os restantes (grupo 2), com a "
          "fórmula para duas proporções com grupos de dimensão diferente, "
          "em que r é a razão entre a dimensão do grupo 2 e a do grupo 1:"),
        FORMULA("n<sub>1</sub> = [Z<sub>1-α/2</sub> × √((1 + 1/r) × "
                "p<sub>m</sub> × (1 - p<sub>m</sub>)) + Z<sub>1-β</sub> × "
                "√(p<sub>1</sub>(1 - p<sub>1</sub>) + p<sub>2</sub>(1 - "
                "p<sub>2</sub>) / r)]<sup>2</sup> / (p<sub>1</sub> - "
                "p<sub>2</sub>)<sup>2</sup>"),
        P("Admitiu-se α = 0,05 (Z<sub>1-α/2</sub> = 1,96), poder de 80% "
          "(Z<sub>1-β</sub> = 0,84), boa adesão de 55% no grupo 1 "
          "(p<sub>1</sub>) e de 70% no grupo 2 (p<sub>2</sub>) e 40% dos "
          "doentes no grupo 1 (r = 1,5), o que dá p<sub>m</sub> = (0,55 + "
          "1,5 × 0,70) / 2,5 = 0,64. A diferença de 15 pontos percentuais "
          "corresponde a um OR de 1,91, inferior ao observado na Etiópia para "
          "distâncias superiores a 10 km (ORa 2,42) {aychiluhm2021}, o que "
          "torna o cálculo conservador. Substituindo:"),
        FORMULA("n<sub>1</sub> = [1,96 × √(1,667 × 0,64 × 0,36) + 0,84 × "
                "√(0,2475 + 0,21 / 1,5)]<sup>2</sup> / 0,15<sup>2</sup> = "
                "(1,2146 + 0,5229)<sup>2</sup> / 0,0225 = 134,2"),
        P("São necessários 135 adultos no grupo 1 e 202 no grupo 2, ou seja, "
          "337 contagens válidas, valor inferior às 385 previstas. Com 385 "
          "contagens, o poder é de 85% se 40% dos doentes estiverem no grupo "
          "1 e de 80% se estiverem 30%. Para a regressão logística exigem-se "
          "pelo menos 10 eventos por parâmetro {peduzzi1996}: se a adesão "
          "subóptima ocorrer em 25% a 50% das 385 contagens, haverá 96 a 192 "
          "eventos, o suficiente para 9 a 19 parâmetros. O modelo principal "
          "tem 10 parâmetros e, se houver menos de 100 eventos, será reduzido "
          "pela ordem definida na secção de análise."),
        P("A amostra final acrescenta duas margens. A primeira, de 20%, "
          "cobre os participantes sem contagem válida, por não apresentarem "
          "os frascos, por mudança de regime no intervalo ou por registos "
          "incoerentes na FILA; este valor será reestimado no pré-teste. A "
          "segunda, de 10%, cobre as desistências e os questionários "
          "incompletos:"),
        FORMULA("n<sub>f</sub> = n<sub>0</sub> / [(1 - 0,20) × (1 - 0,10)] = "
                "385 / 0,72 = 534,7, arredondado para 535"),
        P("A amostra final é de 535 adultos. Se o pré-teste mostrar que mais "
          "de 20% dos doentes não apresentam os frascos, o recrutamento "
          "prossegue até se obterem 385 contagens válidas, dentro do período "
          "de recolha, e qualquer perda de poder será declarada no "
          "relatório."),
        H3("Técnica de amostragem"),
        P("A selecção é aleatória sistemática, a partir da sequência diária de "
          "chegada dos adultos à farmácia para levantar anti-retrovirais. O "
          "intervalo de amostragem é k = L / 535, em que L é o número de "
          "levantamentos de adultos esperado entre Abril e Junho, estimado a "
          "partir do registo de dispensas do trimestre anterior; por exemplo, "
          "com 5.350 levantamentos no trimestre, k = 10. Em cada dia, o "
          "primeiro doente é sorteado entre os k primeiros a chegar e os "
          "seguintes são seleccionados de k em k. Os doentes seleccionados "
          "que não cumpram os critérios de elegibilidade ou recusem "
          "participar são substituídos pelo doente elegível seguinte, e as "
          "recusas e os seus motivos declarados são registados para calcular "
          "a taxa de participação. Como o estudo decorre num único local e "
          "sem conglomerados, o efeito de desenho é igual a 1."),
    ]),
    ("Critérios de inclusão e de exclusão", [
        H3("Critérios de inclusão"),
        LISTA([
            "Idade igual ou superior a 18 anos na data da entrevista.",
            "Diagnóstico de infecção pelo HIV e TARV iniciada há pelo menos "
            "seis meses, segundo a FILA ou o processo clínico.",
            "Levantamento pessoal de anti-retrovirais na farmácia do HCN "
            "durante o período de recolha.",
            "Pelo menos um levantamento anterior registado na FILA, com data "
            "e quantidade aviada legíveis.",
            "Consentimento informado escrito, ou por impressão digital com "
            "testemunha no caso de quem não sabe ler.",
        ]),
        H3("Critérios de exclusão"),
        LISTA([
            "Gravidez ou amamentação declarada, por seguirem um calendário "
            "próprio de consultas e levantamentos.",
            "Levantamento feito por representante, por GAAC ou por dispensa "
            "comunitária.",
            "Estado clínico ou mental que impeça a entrevista, segundo a "
            "avaliação do profissional de serviço.",
            "Participação no pré-teste do instrumento.",
        ]),
        P("A mudança de regime no intervalo entre levantamentos não exclui o "
          "participante, que responde ao questionário, mas torna a contagem "
          "não válida para a medida principal."),
    ]),
    ("Variáveis e definições operacionais", [
        P("O [[quadro:variaveis]] apresenta as variáveis do estudo, o seu "
          "tipo, a definição operacional com as categorias ou pontuações e o "
          "objectivo específico a que cada uma responde. A variável "
          "dependente principal é a adesão por contagem de comprimidos, "
          "calculada pela fórmula seguinte:"),
        FORMULA("A (%) = (N<sub>d</sub> - N<sub>r</sub>) / (D × t) × 100"),
        P("Em que N<sub>d</sub> é o número de comprimidos aviados no "
          "levantamento anterior (FILA), N<sub>r</sub> o número de "
          "comprimidos restantes contados no dia da entrevista, D o número de "
          "comprimidos prescritos por dia e t o número de dias decorridos "
          "desde o levantamento anterior. Valores superiores a 100% são "
          "truncados em 100% e sinalizados. A adesão é classificada como boa "
          "quando é igual ou superior a 95% e como subóptima quando é "
          "inferior a 95% {paterson2000}; os limiares de 90% e 80% são "
          "usados em análises de sensibilidade {byrd2019}."),
        QUADRO("variaveis", "Variáveis do estudo e definições operacionais",
               ["Variável", "Tipo", "Definição operacional e categorias",
                "Objectivo"],
               [
                   ["Idade", "Independente, quantitativa",
                    "Anos completos; categorias 18-29, 30-39, 40-49, 50 ou "
                    "mais", "1, 4"],
                   ["Sexo", "Independente, nominal", "Masculino; feminino",
                    "1, 4"],
                   ["Estado civil", "Independente, nominal",
                    "Solteiro; casado ou em união de facto; separado ou "
                    "divorciado; viúvo", "1"],
                   ["Escolaridade", "Independente, ordinal",
                    "Nenhuma; primária; secundária; superior", "1"],
                   ["Ocupação e rendimento", "Independente, nominal",
                    "Com rendimento regular; sem rendimento regular", "1"],
                   ["Residência", "Independente, nominal",
                    "Cidade de Nampula; outro distrito", "1"],
                   ["Tempo de deslocação (distância à unidade sanitária)",
                    "Independente, quantitativa",
                    "Minutos da casa ao HCN, só ida; 60 ou menos; mais de 60 "
                    "(exposição principal)", "1, 4"],
                   ["Custo do transporte", "Independente, quantitativa",
                    "Meticais gastos na ida e volta; zero se a pé", "1"],
                   ["Contorno de unidade mais próxima",
                    "Independente, nominal",
                    "Existe unidade com TARV mais próxima de casa: sim; não; "
                    "motivo da escolha do HCN", "1"],
                   ["Tempo em TARV", "Independente, quantitativa",
                    "Meses desde o início (FILA ou processo)", "1, 4"],
                   ["Regime e comprimidos por dia", "Independente, nominal",
                    "TLD; outro de primeira linha; segunda linha; número de "
                    "comprimidos por dia", "1, 5"],
                   ["Modelo de dispensa", "Independente, nominal",
                    "Mensal; trimestral; semestral", "1, 4"],
                   ["Revelação do diagnóstico", "Independente, nominal",
                    "Revelou a pelo menos um familiar ou parceiro: sim; não",
                    "1, 4"],
                   ["Uso de medicina tradicional", "Independente, nominal",
                    "Nos últimos 30 dias: sim; não", "1"],
                   ["Consumo de álcool", "Independente, quantitativa",
                    "AUDIT-C, 0-12; rastreio positivo com 3 ou mais "
                    "{inoue2021}", "1, 4"],
                   ["Adesão por contagem de comprimidos",
                    "Dependente, quantitativa",
                    "Percentagem pela fórmula do texto; boa: 95% ou mais; "
                    "subóptima: menos de 95%", "2, 4, 5"],
                   ["Apresentação dos frascos", "Descritiva, nominal",
                    "Contagem válida: sim; não, com motivo", "2"],
                   ["Adesão por auto-relato", "Quantitativa",
                    "Três itens, média 0-100; boa: 90 ou mais {kizito2026}",
                    "2, 5"],
                   ["Adesão pelo registo de levantamentos", "Nominal",
                    "Atraso de 15 ou mais dias em algum levantamento dos "
                    "seis meses anteriores: sim; não {filimao2019}", "2"],
                   ["Efeitos adversos percebidos", "Independente, nominal",
                    "Pelo menos um de 12 sintomas atribuídos aos "
                    "anti-retrovirais nos últimos 30 dias: sim; não; número "
                    "de sintomas", "3, 4"],
                   ["Falha de doses por efeitos adversos",
                    "Descritiva, nominal", "Sim; não", "3"],
                   ["Estigma relacionado com o HIV",
                    "Independente, quantitativa",
                    "Escala de 12 itens, 12-48; quatro subescalas de 3-12; "
                    "análise contínua e em tercis", "3, 4"],
                   ["Apoio familiar percebido", "Independente, quantitativa",
                    "Subescala família da MSPSS, média 1-7; MSPSS total, "
                    "média 1-7", "3, 4"],
                   ["Supressão viral", "Dependente, nominal",
                    "Carga viral mais recente nos 12 meses anteriores: "
                    "suprimida, menos de 1.000 cópias/mL; não suprimida, "
                    "1.000 ou mais; sem resultado", "5"],
               ],
               larguras=[3.4, 2.8, 7.8, 2.0]),
    ]),
    ("Instrumentos de recolha de dados e respectivas fontes", [
        P("O instrumento principal é um questionário estruturado aplicado "
          "por entrevista (Apêndice A), com onze secções: identificação; "
          "dados sociodemográficos; acesso à unidade sanitária; dados "
          "clínicos e terapêuticos; auto-relato de adesão; efeitos adversos "
          "percebidos; estigma; apoio social; consumo de álcool; ficha de "
          "contagem de comprimidos; e ficha de extracção do processo "
          "clínico. As perguntas sobre acesso e sobre barreiras seguem as "
          "barreiras que o guião nacional manda investigar, e a lista de 12 "
          "sintomas baseia-se na tabela de efeitos adversos dos "
          "anti-retrovirais do mesmo guião {misau2023}."),
        P("As escalas usadas são adaptadas de instrumentos validados, sem "
          "alteração do conteúdo dos itens: o auto-relato de três itens de "
          "Wilson e colaboradores, pontuado de 0 a 100 {wilson2016}; a escala "
          "curta de estigma relacionado com o HIV, de 12 itens e quatro "
          "pontos {reinius2017}, partindo da versão em português do Brasil "
          "{luz2020}; a MSPSS, de 12 itens e sete pontos {zimet1988}; e o "
          "AUDIT-C, de três itens {inoue2021}. As versões apresentadas no "
          "Apêndice A são versões de trabalho em português europeu, que serão "
          "harmonizadas com as versões publicadas antes da tradução."),
        H3("Adaptação, tradução e validação"),
        P("A adaptação decorre em quatro etapas. Na primeira, um painel de "
          "cinco peritos (um farmacêutico hospitalar, um clínico do serviço "
          "de TARV, um conselheiro de apoio psicossocial, um docente de "
          "saúde pública e um docente de farmácia clínica) classifica a "
          "relevância e a clareza de cada item numa escala de quatro pontos, "
          "calculando-se o índice de validade de conteúdo (IVC) de cada item "
          "e do conjunto {almanasreh2019}; os itens com IVC inferior a 0,80 "
          "são revistos. Na segunda, dois tradutores independentes, falantes "
          "nativos de emakhuwa, traduzem o questionário e um terceiro faz a "
          "retroversão para português, sendo as discrepâncias resolvidas em "
          "reunião com o investigador. Na terceira, o pré-teste é aplicado a "
          "54 adultos, cerca de 10% da amostra, em Março de 2027, no HCN, que "
          "ficam excluídos da amostra final; avalia-se a compreensão, o tempo "
          "de aplicação, a proporção de doentes que apresenta os frascos e a "
          "exequibilidade da contagem. Na quarta, calcula-se a consistência "
          "interna das escalas pelo alfa de Cronbach, exigindo-se 0,70 ou "
          "mais, valor alcançado por estas escalas noutras populações "
          "{reinius2017,wanjala2022,dambi2018}; a fiabilidade é recalculada "
          "na amostra final."),
    ]),
    ("Procedimentos de recolha de dados e controlo de qualidade", [
        P("A recolha é feita pelo investigador e por um inquiridor assistente "
          "fluente em português e emakhuwa, sem funções clínicas no serviço, "
          "formado durante dois dias sobre o protocolo, a ética, a aplicação "
          "das escalas e a técnica de contagem. Em cada dia, depois da "
          "selecção sistemática, o doente é convidado para um espaço "
          "reservado, fora da sala de espera, onde recebe a informação sobre "
          "o estudo e assina o consentimento. Segue-se, antes da dispensa do "
          "novo levantamento, a contagem de comprimidos: o participante "
          "apresenta todos os frascos de anti-retrovirais que tem consigo, os "
          "comprimidos são contados duas vezes num tabuleiro de contagem, "
          "com luvas, e o número é registado na ficha, com a data e a "
          "quantidade do levantamento anterior copiadas da FILA. O "
          "participante que não trouxe os frascos responde ao questionário e "
          "o motivo é registado. A entrevista dura cerca de 30 minutos e "
          "decorre enquanto o doente aguarda a dispensa, sem atrasar o "
          "atendimento."),
        P("A extracção da carga viral e da data de início da TARV é feita a "
          "partir do processo clínico e da ficha mestra, no serviço de TARV, "
          "com uma ficha própria sem nome, ligada ao questionário apenas pelo "
          "código do participante. O controlo de qualidade inclui a revisão "
          "diária de todos os questionários quanto à completude e à "
          "coerência; a recontagem independente dos comprimidos pelo "
          "inquiridor em 10% dos participantes, com cálculo do coeficiente de "
          "correlação intraclasse entre as duas contagens; a verificação de "
          "10% das extracções do processo clínico por uma segunda pessoa; a "
          "dupla digitação independente de todos os questionários, com "
          "comparação dos ficheiros e correcção das discrepâncias pelo "
          "original; e a supervisão semanal pelo orientador."),
    ]),
    ("Processamento e análise dos dados", [
        P("Os dados serão digitados duas vezes em folhas de cálculo com "
          "validação de campos e analisados no programa Statistical "
          "Package for the Social Sciences (SPSS), versão 26 ou superior, "
          "ou, em alternativa, no R, com nível de significância de "
          "5% (p<0,05) e intervalos de confiança a 95% (IC95%). A análise "
          "descritiva usa frequências absolutas e relativas para as variáveis "
          "categóricas e média com desvio-padrão ou mediana com intervalo "
          "interquartil para as quantitativas, conforme a normalidade "
          "avaliada pelo teste de Shapiro-Wilk. As pontuações das escalas "
          "são calculadas apenas quando pelo menos 80% dos itens estão "
          "respondidos."),
        P("Para o objectivo específico 1, apresenta-se a caracterização "
          "completa da amostra. Para o objectivo 2, estima-se a proporção de "
          "boa adesão por contagem de comprimidos com IC95% pelo método de "
          "Wilson; a concordância entre a classificação por contagem e as "
          "classificações por auto-relato e pelo registo de levantamentos é "
          "avaliada pelo kappa de Cohen, a diferença entre as proporções "
          "pelo teste de McNemar e a correlação entre a percentagem de "
          "adesão e a pontuação de auto-relato pelo coeficiente de Spearman. "
          "Como o ponto de corte da contagem (95%) e o do auto-relato (90 "
          "pontos, seguindo {kizito2026}) não coincidem, o kappa é "
          "recalculado com o auto-relato dicotomizado também em 95 pontos, "
          "para mostrar quanto da discordância se deve à diferença de "
          "limiares e quanto se deve ao método. "
          "Para o objectivo 3, descrevem-se as frequências de cada efeito "
          "adverso e as pontuações de estigma e de apoio familiar, com a "
          "respectiva consistência interna."),
        P("Para o objectivo 4, a associação de cada factor com a boa adesão "
          "é testada pelo qui-quadrado de Pearson, ou pelo teste exacto de "
          "Fisher quando mais de 20% das frequências esperadas forem "
          "inferiores a 5, e pelo teste t de Student ou de Mann-Whitney para "
          "as variáveis quantitativas. Segue-se a regressão logística "
          "multivariável, com a boa adesão como variável dependente, que "
          "inclui as quatro exposições principais (tempo de deslocação, "
          "estigma, efeitos adversos e apoio familiar) e, como variáveis de "
          "ajustamento definidas *a priori*, a idade, o sexo, o tempo em TARV, "
          "o modelo de dispensa, o rastreio positivo de álcool e a revelação "
          "do diagnóstico. Para que o modelo não gaste mais graus de "
          "liberdade do que a amostra suporta, a idade e o tempo em TARV "
          "entram como variáveis contínuas e o modelo de dispensa como "
          "mensal contra vários meses, ficando as categorias do quadro de "
          "variáveis reservadas à descrição; o modelo tem assim 10 "
          "parâmetros. Se houver menos de 100 "
          "eventos, retiram-se por esta ordem a revelação do diagnóstico e o "
          "modelo de dispensa. Apresentam-se os ORa com IC95%, avalia-se a "
          "colinearidade pelo factor de inflação da variância (aceitável "
          "abaixo de 5) e o ajustamento pelo teste de Hosmer-Lemeshow. Como "
          "a boa adesão deverá ser frequente, o OR sobrestima a razão de "
          "prevalências; por isso estima-se também a razão de prevalências "
          "(RP) ajustada por regressão de Poisson com variância robusta "
          "{tamhane2016}."),
        P("Para o objectivo 5, compara-se a proporção de carga viral "
          "suprimida entre os adultos com boa adesão e com adesão subóptima "
          "pelo qui-quadrado e por regressão logística ajustada para o tempo "
          "em TARV e o regime, e calculam-se a sensibilidade, a "
          "especificidade e os valores preditivos da contagem de comprimidos "
          "e do auto-relato para a supressão viral, bem como a área sob a "
          "curva característica de operação. As análises de sensibilidade "
          "incluem os limiares de adesão de 90% e de 80%, a restrição às "
          "cargas virais colhidas nos seis meses anteriores à entrevista e a "
          "comparação das características dos participantes com e sem "
          "contagem válida, para avaliar o viés de selecção. Os dados em "
          "falta são descritos e não são imputados na análise principal."),
    ]),
    ("Limitações do estudo e estratégias de mitigação", [
        P("O [[quadro:limitacoes]] resume as limitações previstas, a sua "
          "consequência para a interpretação dos resultados e as estratégias "
          "adoptadas para as reduzir."),
        QUADRO("limitacoes", "Limitações previstas e estratégias de mitigação",
               ["Limitação", "Consequência", "Mitigação"],
               [
                   ["Desenho transversal",
                    "Não permite inferir causalidade entre os factores e a "
                    "adesão",
                    "Interpretar como associações; usar períodos de "
                    "referência anteriores à medição (efeitos adversos e "
                    "auto-relato nos 30 dias anteriores)"],
                   ["Contagem limitada aos frascos que o doente traz "
                    "consigo, sujeita a descarte de comprimidos ou a "
                    "reservas guardadas em casa",
                    "Sobrestimação ou subestimação da adesão",
                    "Contagem não anunciada, por selecção no momento da "
                    "chegada à farmácia; contar todos os frascos "
                    "apresentados; truncar valores acima de 100%; comparar "
                    "com auto-relato, registo de levantamentos e carga "
                    "viral"],
                   ["Doentes que não apresentam os frascos",
                    "Viés de selecção na medida principal",
                    "Registar motivos, comparar características com e sem "
                    "contagem, margem de 20% na amostra"],
                   ["Desejabilidade social no auto-relato e nas escalas de "
                    "estigma",
                    "Sobrestimação da adesão e subestimação do estigma",
                    "Inquiridor sem funções clínicas, espaço reservado, "
                    "perguntas neutras e garantia de que as respostas não "
                    "afectam o atendimento"],
                   ["Diferença temporal entre a carga viral e a contagem",
                    "Associação atenuada entre adesão e supressão viral",
                    "Registar o intervalo; análise restrita às cargas virais "
                    "dos seis meses anteriores"],
                   ["Estudo num único hospital central",
                    "Generalização limitada aos cuidados primários",
                    "Descrever bem a população e o modelo de dispensa; "
                    "extrapolar com prudência"],
                   ["Tradução para emakhuwa e adaptação das escalas",
                    "Erros de compreensão e perda de validade",
                    "Tradução e retroversão, painel de peritos, pré-teste e "
                    "cálculo do alfa de Cronbach"],
                   ["Confundidores não medidos (depressão, insegurança "
                    "alimentar)",
                    "Confundimento residual",
                    "Ajustamento para os confundidores medidos; discussão "
                    "à luz da literatura"],
               ],
               larguras=[5, 5, 6]),
    ]),
    ("Considerações éticas", [
        P("O estudo respeita os princípios da Declaração de Helsínquia da "
          "Associação Médica Mundial, na revisão de 2024 {helsinki2025}. O "
          "protocolo será submetido ao Comité Institucional de Bioética para "
          "a Saúde da Universidade Lúrio (CIBS-UniLúrio) e, se este o "
          "determinar, ao Comité Nacional de Bioética para a Saúde, e a "
          "recolha só começa após o parecer favorável e as autorizações da "
          "Direcção Provincial de Saúde de Nampula, do Serviço Distrital de "
          "Saúde, Mulher e Acção Social (SDSMAS) da Cidade de Nampula e da "
          "direcção do HCN (Apêndice D). Aplicam-se as salvaguardas "
          "seguintes:"),
        LISTA([
            "Consentimento informado livre e esclarecido, escrito, após "
            "leitura da folha de informação em português ou emakhuwa "
            "(Apêndices B e C); quem não sabe ler assina por impressão "
            "digital, na presença de uma testemunha imparcial escolhida pelo "
            "participante. O consentimento inclui a autorização para "
            "consultar a FILA e o processo clínico.",
            "Voluntariedade: a recusa ou a desistência não altera o "
            "atendimento, e a contagem de comprimidos não tem qualquer "
            "consequência sobre a dispensa, o que é explicado ao "
            "participante.",
            "Confidencialidade: entrevista em espaço reservado; questionários "
            "identificados apenas por código; lista de ligação entre código e "
            "número do processo guardada em armário fechado, separada dos "
            "questionários, e destruída após a análise; base de dados sem "
            "identificadores, protegida por palavra-passe; resultados "
            "divulgados apenas de forma agregada; questionários guardados "
            "durante cinco anos. Não é registado em nenhuma folha do "
            "estudo o nome, o contacto telefónico ou a morada do "
            "participante. O investigador e o inquiridor assinam, antes do "
            "início da recolha, um termo de confidencialidade que os obriga "
            "a não revelar a participação nem o estado serológico de "
            "ninguém, dentro ou fora do hospital.",
            "Riscos e benefícios: o risco é mínimo, limitado ao tempo da "
            "entrevista e ao possível desconforto com perguntas sobre estigma "
            "e álcool; o participante pode recusar qualquer pergunta. Não há "
            "pagamento nem benefício directo, além da orientação descrita no "
            "ponto seguinte.",
            "Via de referenciação: com o acordo do participante, quem tiver "
            "adesão por contagem inferior a 95%, efeitos adversos que o "
            "levem a falhar doses, rastreio positivo de álcool ou sofrimento "
            "associado ao estigma é encaminhado no mesmo dia para o sector "
            "de apoio psicossocial ou para o clínico do serviço de TARV do "
            "HCN. É encaminhado pela mesma via, e com a mesma reserva, o "
            "participante cuja carga viral mais recente registada no "
            "processo seja igual ou superior a 1.000 cópias/mL, por ser um "
            "achado que as normas nacionais mandam seguir com reforço da "
            "adesão {misau2023}. As suspeitas de reacções adversas são "
            "notificadas pela ficha nacional de farmacovigilância "
            "{misau2023}.",
            "Conflito de interesses: o investigador declara não ter conflitos "
            "de interesses; o estudo não tem financiamento de empresas "
            "farmacêuticas.",
        ]),
    ]),
]

# ----------------------------------------------------- 9 e 10 ---------------
RESULTADOS_ESPERADOS = [
    P("Os resultados esperados são apresentados pela ordem dos objectivos "
      "específicos. Não se antecipam valores numéricos; indica-se a direcção "
      "esperada, com base na literatura revista, e a utilidade prática de "
      "cada resultado."),
    LISTA([
        "Objectivo 1: uma caracterização dos adultos em TARV que levantam a "
        "medicação no HCN, incluindo a proporção que reside fora da cidade, "
        "que demora mais de 60 minutos a chegar ao hospital ou que contorna "
        "uma unidade mais próxima. Espera-se que a maioria esteja em regime "
        "TLD e em dispensa de vários meses {misau2023,misaumds2023}. Este "
        "perfil serve para planear a dispensa de vários meses e a eventual "
        "transferência de doentes estáveis para unidades mais próximas.",
        "Objectivo 2: uma estimativa, com IC95%, da proporção de adultos com "
        "boa adesão por contagem de comprimidos. Espera-se que seja inferior "
        "à estimada por auto-relato e que a concordância entre métodos seja "
        "apenas moderada, como noutros estudos africanos "
        "{kioko2017,gobezie2024,kizito2026}. O resultado mostra se a "
        "contagem de comprimidos deve ser incorporada na rotina da farmácia.",
        "Objectivo 3: a frequência dos efeitos adversos percebidos e os "
        "níveis de estigma e de apoio familiar. Espera-se que os efeitos "
        "adversos sejam sobretudo ligeiros, como cefaleias e insónia "
        "{ogbonnaya2024,misau2023}, e que o estigma seja frequente, sobretudo "
        "nas subescalas de revelação e de atitudes públicas {alemu2022}. Estes "
        "dados definem os temas do aconselhamento farmacêutico.",
        "Objectivo 4: a identificação dos factores independentemente "
        "associados à boa adesão. Espera-se menor adesão nos doentes com "
        "deslocações mais longas, com mais estigma e com efeitos adversos, e "
        "maior adesão nos que têm mais apoio familiar "
        "{aychiluhm2021,sweeney2016,kioko2017,nutor2023}. O resultado permite "
        "construir um perfil de risco simples para seleccionar os doentes "
        "que devem receber aconselhamento reforçado.",
        "Objectivo 5: a medida da relação entre a adesão por contagem e a "
        "supressão viral. Espera-se maior supressão nos doentes com boa "
        "adesão, com capacidade discriminativa apenas moderada da contagem "
        "isolada {mudhune2018,kizito2026}. O resultado indica se a contagem "
        "na farmácia pode servir de rastreio para antecipar o reforço da "
        "adesão antes da carga viral anual.",
    ]),
    P("O produto final do estudo é uma proposta de programa de sessões de "
      "aconselhamento farmacêutico, a apresentar à direcção do HCN, "
      "integrada no apoio psicossocial previsto nas normas nacionais "
      "{misau2015}: sessões individuais no acto do levantamento, dirigidas "
      "aos doentes com o perfil de risco identificado, com conteúdos "
      "ajustados aos factores que se revelarem associados à adesão, como a "
      "gestão dos efeitos adversos, o planeamento das tomas e das "
      "deslocações, a revelação do diagnóstico e o envolvimento de um "
      "familiar apoiante {nyoni2020,ahmed2022}."),
]
DIVULGACAO = [
    P("Os resultados serão apresentados na defesa pública do trabalho de "
      "conclusão de curso na Faculdade de Ciências de Saúde da Universidade "
      "Lúrio. Um relatório técnico, com os resultados agregados e a proposta "
      "de sessões de aconselhamento farmacêutico, será entregue à direcção "
      "do HCN, à farmácia e ao serviço de TARV, à Direcção Provincial de "
      "Saúde de Nampula e ao SDSMAS da Cidade de Nampula, e discutido numa "
      "reunião com a equipa da farmácia e do apoio psicossocial. O "
      "manuscrito será submetido a uma revista científica com revisão por "
      "pares, de preferência de acesso aberto, e os resultados serão "
      "apresentados em jornadas científicas da universidade e em encontros "
      "científicos nacionais. Para devolver os resultados aos doentes, será "
      "preparado um cartaz em linguagem simples, em português e emakhuwa, "
      "para a sala de espera da farmácia, sem qualquer dado individual."),
]

# ----------------------------------------------------- 11. cronograma -------
CRONOGRAMA_TEXTO = [
    P("O [[quadro:cronograma]] distribui as actividades pelos 12 meses do "
      "estudo, de Outubro de 2026 a Setembro de 2027. A submissão ao comité "
      "de bioética e os pedidos de autorização ocupam Dezembro e Janeiro; a "
      "formação do inquiridor e o pré-teste decorrem em Março, depois da "
      "aprovação ética; a recolha de dados decorre de Abril a Junho de 2027; "
      "a análise e a redacção ocupam Julho e Agosto; a entrega e a defesa "
      "estão previstas para Setembro de 2027."),
]
CRONOGRAMA = {
    "inicio": (2026, 10),
    "n_meses": 12,
    "actividades": [
        ("Revisão da literatura e redacção do protocolo", [1, 2]),
        ("Submissão ao CIBS-UniLúrio e pedidos de autorização", [3, 4]),
        ("Painel de peritos, tradução e retroversão dos instrumentos",
         [4, 5]),
        ("Formação do inquiridor e pré-teste", [6]),
        ("Recolha de dados (entrevista, contagem e extracção)", [7, 8, 9]),
        ("Dupla digitação, limpeza e processamento", [8, 9, 10]),
        ("Análise estatística", [10, 11]),
        ("Redacção do relatório final", [10, 11]),
        ("Revisão pelo orientador e entrega", [12]),
        ("Defesa pública e devolução às instituições", [12]),
    ],
}

# ----------------------------------------------------- 12. orcamento --------
ORCAMENTO_TEXTO = [
    P("A [[tabela:orcamento]] apresenta o orçamento estimado, em meticais. "
      "O estudo será financiado com recursos próprios do estudante, "
      "complementados por apoio a solicitar à Universidade Lúrio e a "
      "parceiros do programa de HIV da província. A rubrica maior é o "
      "subsídio do inquiridor assistente, necessário para entrevistar em "
      "emakhuwa e para a recontagem de controlo durante os 70 dias de "
      "trabalho de campo (65 dias úteis de recolha, de Abril a Junho de 2027, "
      "e 5 dias de pré-teste em Março); seguem-se as fotocópias dos "
      "questionários, "
      "fichas e termos para 590 participantes (535 da amostra e 54 do "
      "pré-teste, arredondados), e a tradução e retroversão dos "
      "instrumentos."),
]
ORCAMENTO = [
    ("Fotocópias de questionários, fichas e termos (10 páginas por "
     "participante)", "página", 5900, 3),
    ("Tradução para emakhuwa e retroversão", "serviço", 3, 2500),
    ("Comunicação com o painel de peritos", "perito", 5, 500),
    ("Formação do inquiridor assistente", "dia", 2, 1500),
    ("Subsídio do inquiridor assistente", "dia", 70, 500),
    ("Transporte do investigador", "dia", 70, 100),
    ("Comunicação telefónica e internet", "mês", 8, 500),
    ("Material de escritório (pranchetas, pastas, canetas, envelopes)",
     "conjunto", 1, 2500),
    ("Tabuleiros e espátulas para contagem de comprimidos", "conjunto", 2,
     600),
    ("Luvas descartáveis (caixa de 100)", "caixa", 6, 400),
    ("Armário com fechadura para arquivo", "unidade", 1, 3500),
    ("Disco externo para cópia de segurança encriptada", "unidade", 1,
     2000),
    ("Taxa de submissão ao comité de bioética", "taxa", 1, 5000),
    ("Impressão e encadernação do relatório final", "exemplar", 4, 800),
    ("Cartazes de devolução e apresentação em jornadas", "unidade", 3, 1000),
]
ORCAMENTO_IMPREVISTOS = 0.10

# ----------------------------------------------------- apendices ------------
APENDICES = [
    ("Questionário de recolha de dados", [
        NOTA("Instruções ao entrevistador: aplicar apenas depois da "
             "assinatura do consentimento, em espaço reservado, em português "
             "ou emakhuwa, conforme a preferência do participante. Ler as "
             "perguntas tal como estão escritas, sem sugerir respostas. A "
             "ficha de contagem (Secção X) é preenchida antes da dispensa do "
             "novo levantamento. Não escrever o nome do participante em "
             "nenhuma folha."),
        H3("Secção I. Identificação"),
        CAMPO("Código do participante: __________     Data: ___/___/2027     "
              "Entrevistador: __________"),
        PERG("Língua da entrevista:", ["Português", "Emakhuwa"]),
        H3("Secção II. Dados sociodemográficos"),
        PERG("Idade em anos completos:"),
        PERG("Sexo:", ["Masculino", "Feminino"]),
        PERG("Estado civil:", ["Solteiro(a)", "Casado(a) ou em união de facto",
                               "Separado(a) ou divorciado(a)", "Viúvo(a)"]),
        PERG("Escolaridade concluída:", ["Nenhuma", "Primária", "Secundária",
                                         "Superior"]),
        PERG("Ocupação principal:", ["Emprego formal", "Conta própria ou "
                                     "comércio", "Agricultura", "Estudante",
                                     "Sem ocupação", "Outra"]),
        PERG("Tem rendimento regular todos os meses?", ["Sim", "Não"]),
        PERG("Número de pessoas que vivem no seu agregado familiar:"),
        H3("Secção III. Acesso à unidade sanitária"),
        PERG("Distrito de residência:", ["Cidade de Nampula", "Outro distrito "
                                         "(qual?) __________"]),
        PERG("Bairro ou localidade de residência:"),
        PERG("Quanto tempo demora, só de ida, de casa até ao HCN (minutos)?"),
        PERG("Meio de transporte habitual:", ["A pé", "Bicicleta",
                                              "Mota-táxi", "Chapa ou autocarro",
                                              "Viatura própria", "Outro"]),
        PERG("Quanto gasta em transporte na ida e volta ao HCN (meticais)?"),
        PERG("Existe uma unidade sanitária com TARV mais perto da sua casa do "
             "que o HCN?", ["Sim", "Não", "Não sabe"]),
        PERG("Se sim, por que razão prefere levantar no HCN?",
             ["Melhor atendimento", "Confidencialidade", "Transferido pelo "
              "clínico", "Perto do trabalho", "Outra"]),
        PERG("Nos últimos seis meses, alguma vez faltou ou se atrasou num "
             "levantamento por falta de dinheiro para o transporte?",
             ["Sim", "Não"]),
        H3("Secção IV. Dados clínicos e terapêuticos (confirmar na FILA)"),
        PERG("Data de início da TARV (mês e ano): ___/______"),
        PERG("Regime actual:", ["TLD", "Outro de primeira linha (qual?) "
                                "________", "Segunda linha (qual?) ________"]),
        PERG("Número de comprimidos de anti-retrovirais por dia:"),
        PERG("Mudou de regime desde o último levantamento?", ["Sim", "Não"]),
        PERG("Modelo de dispensa actual:", ["Mensal", "Trimestral",
                                            "Semestral"]),
        PERG("Alguém da sua família ou o seu parceiro sabe que vive com o "
             "HIV?", ["Sim", "Não", "Prefere não responder"]),
        PERG("Nos últimos 30 dias, usou medicamentos tradicionais ou "
             "remédios de curandeiro?", ["Sim", "Não"]),
        H3("Secção V. Auto-relato de adesão (três itens)"),
        NOTA("Adaptado de Wilson e colaboradores (2016). Pontuação: item 1 "
             "convertido em (30 - dias) / 30 × 100; itens 2 e 3 pontuados 0, "
             "20, 40, 60, 80 e 100 pela ordem das opções; pontuação final "
             "igual à média dos três itens (0-100)."),
        PERG("Nos últimos 30 dias, em quantos dias falhou pelo menos uma dose "
             "dos seus medicamentos para o HIV? ______ dias (0 a 30)"),
        PERG("Nos últimos 30 dias, como avalia a forma como tomou os seus "
             "medicamentos para o HIV, tal como devia?",
             ["Muito má", "Má", "Razoável", "Boa", "Muito boa", "Excelente"]),
        PERG("Nos últimos 30 dias, com que frequência tomou os seus "
             "medicamentos para o HIV da forma como devia?",
             ["Nunca", "Raramente", "Às vezes", "Normalmente",
              "Quase sempre", "Sempre"]),
        H3("Secção VI. Efeitos adversos percebidos"),
        NOTA("Lista baseada na tabela de efeitos adversos dos "
             "anti-retrovirais do guião nacional de 2023. Para cada sintoma, "
             "perguntar: «Nos últimos 30 dias, teve este problema e acha que "
             "foi causado pelos medicamentos para o HIV?»"),
        ESCALA(["Náuseas ou enjoos", "Vómitos", "Dor de barriga", "Diarreia",
                "Dor de cabeça", "Tonturas", "Dificuldade em dormir",
                "Sonhos muito vivos ou pesadelos",
                "Mudanças de humor (tristeza, irritação)",
                "Formigueiro, dor ou dormência nos pés ou nas mãos",
                "Comichão ou manchas na pele",
                "Aumento de peso não desejado"],
               ["Sim", "Não"], cabecalho_item="Sintoma nos últimos 30 dias"),
        PERG("Outro problema que atribui aos medicamentos (qual?):"),
        PERG("Nos últimos 30 dias, deixou de tomar alguma dose por causa "
             "destes problemas?", ["Sim", "Não"]),
        H3("Secção VII. Estigma relacionado com o HIV (escala curta de 12 "
           "itens)"),
        NOTA("Adaptado de Reinius e colaboradores (2017) e da versão em "
             "português do Brasil de Luz e colaboradores (2020); versão de "
             "trabalho a harmonizar antes da tradução. Opções: 1 = discordo "
             "totalmente; 2 = discordo; 3 = concordo; 4 = concordo "
             "totalmente. Pontuação total de 12 a 48; itens 1-3 estigma "
             "personalizado, 4-6 preocupações com a revelação, 7-9 "
             "atitudes públicas, 10-12 auto-imagem negativa."),
        ESCALA(["Pessoas de quem gosto deixaram de me contactar depois de "
                "saberem que tenho HIV.",
                "Perdi amigos por lhes dizer que tenho HIV.",
                "Algumas pessoas evitam tocar-me depois de saberem que tenho "
                "HIV.",
                "Dizer a alguém que tenho HIV é arriscado.",
                "Esforço-me muito para manter em segredo que tenho HIV.",
                "Tenho muito cuidado com as pessoas a quem digo que tenho "
                "HIV.",
                "A maioria das pessoas pensa que quem tem HIV é sujo.",
                "As pessoas com HIV são tratadas como marginais.",
                "A maioria das pessoas sente-se desconfortável perto de "
                "alguém com HIV.",
                "Sinto-me culpado(a) por ter HIV.",
                "As atitudes das pessoas em relação ao HIV fazem-me sentir "
                "pior comigo mesmo(a).",
                "Sinto que não sou tão boa pessoa como os outros por ter "
                "HIV."],
               ["1", "2", "3", "4"]),
        H3("Secção VIII. Apoio social percebido (MSPSS)"),
        NOTA("Adaptado de Zimet e colaboradores (1988); versão de trabalho a "
             "harmonizar antes da tradução. Opções: 1 = discordo muito "
             "fortemente; 2 = discordo fortemente; 3 = discordo ligeiramente; "
             "4 = neutro; 5 = concordo ligeiramente; 6 = concordo "
             "fortemente; 7 = concordo muito fortemente. Subescala família: "
             "itens 3, 4, 8 e 11; amigos: 6, 7, 9 e 12; pessoa "
             "significativa: 1, 2, 5 e 10. Pontuações expressas como média "
             "de 1 a 7."),
        ESCALA(["Há uma pessoa especial que está por perto quando preciso.",
                "Há uma pessoa especial com quem posso partilhar as minhas "
                "alegrias e tristezas.",
                "A minha família tenta realmente ajudar-me.",
                "Recebo da minha família a ajuda e o apoio emocional de que "
                "preciso.",
                "Tenho uma pessoa especial que é uma verdadeira fonte de "
                "conforto para mim.",
                "Os meus amigos tentam realmente ajudar-me.",
                "Posso contar com os meus amigos quando as coisas correm mal.",
                "Posso falar dos meus problemas com a minha família.",
                "Tenho amigos com quem posso partilhar as minhas alegrias e "
                "tristezas.",
                "Há uma pessoa especial na minha vida que se preocupa com os "
                "meus sentimentos.",
                "A minha família está disposta a ajudar-me a tomar decisões.",
                "Posso falar dos meus problemas com os meus amigos."],
               ["1", "2", "3", "4", "5", "6", "7"]),
        H3("Secção IX. Consumo de álcool (AUDIT-C)"),
        NOTA("Usar o cartão ilustrado de bebidas padrão (garrafa pequena de "
             "cerveja, copo de vinho, dose de bebida destilada ou medida "
             "equivalente de bebida tradicional). Pontuação de 0 a 12, pela "
             "ordem das opções (0 a 4); rastreio positivo com 3 ou mais."),
        PERG("Com que frequência consome bebidas que contêm álcool?",
             ["Nunca", "Uma vez por mês ou menos", "Duas a quatro vezes por "
              "mês", "Duas a três vezes por semana", "Quatro ou mais vezes "
              "por semana"]),
        PERG("Quando bebe, quantas bebidas padrão consome num dia típico?",
             ["1 ou 2", "3 ou 4", "5 ou 6", "7 a 9", "10 ou mais"]),
        PERG("Com que frequência consome seis ou mais bebidas numa única "
             "ocasião?", ["Nunca", "Menos de uma vez por mês", "Mensalmente",
                          "Semanalmente", "Diariamente ou quase "
                          "diariamente"]),
        H3("Secção X. Ficha de contagem de comprimidos"),
        NOTA("Contar duas vezes todos os comprimidos de anti-retrovirais "
             "apresentados, num tabuleiro, com luvas. Se as duas contagens "
             "diferirem, contar uma terceira vez. Copiar da FILA a data e a "
             "quantidade do levantamento anterior."),
        PERG("O participante apresentou os frascos?",
             ["Sim", "Não (motivo): __________"]),
        CAMPO("Data do levantamento anterior (FILA): ___/___/______     "
              "Data de hoje: ___/___/2027"),
        CAMPO("Dias decorridos (t): ______     Comprimidos prescritos por dia "
              "(D): ______"),
        CAMPO("Comprimidos aviados no levantamento anterior (Nd): ______"),
        CAMPO("Comprimidos restantes: 1.ª contagem ______ 2.ª contagem ______ "
              "valor final (Nr) ______"),
        CAMPO("Adesão (%) = (Nd - Nr) / (D × t) × 100 = ______ %     "
              "Classificação: (   ) 95% ou mais   (   ) menos de 95%"),
        CAMPO("Atraso de 15 ou mais dias em algum levantamento dos últimos "
              "seis meses (FILA): (   ) Sim   (   ) Não"),
        CAMPO("Recontagem de controlo (10% dos participantes): ______ "
              "Rubrica do inquiridor: ______"),
        H3("Secção XI. Ficha de extracção do processo clínico"),
        CAMPO("Resultado da carga viral mais recente nos 12 meses anteriores: "
              "__________ cópias/mL     (   ) Sem resultado"),
        CAMPO("Data da colheita: ___/___/______     Intervalo até à entrevista "
              "(dias): ______"),
        CAMPO("Data de início da TARV confirmada no processo: ___/______     "
              "Regime registado: __________"),
        CAMPO("Encaminhamento feito no dia da entrevista: (   ) Apoio "
              "psicossocial   (   ) Clínico   (   ) Notificação de reacção "
              "adversa   (   ) Nenhum"),
    ]),
    ("Folha de informação ao participante", [
        P("Título do estudo: Adesão à terapêutica anti-retroviral e factores "
          "associados em adultos seguidos no Hospital Central de Nampula, de "
          "Abril a Junho de 2027. Investigador: [Nome do(a) estudante], "
          "estudante de Licenciatura em Farmácia da Faculdade de Ciências de "
          "Saúde da Universidade Lúrio, sob orientação de [Nome e grau "
          "académico do(a) orientador(a)]."),
        P("Convidamo-lo(a) a participar num estudo que pretende saber como os "
          "adultos que levantam medicamentos para o HIV no HCN conseguem "
          "tomá-los e que dificuldades encontram, como a distância, os "
          "efeitos dos medicamentos, a reacção das outras pessoas e o apoio "
          "da família. Os resultados servirão para melhorar o aconselhamento "
          "dado na farmácia."),
        P("Se aceitar, faremos uma entrevista de cerca de 30 minutos, num "
          "espaço reservado, enquanto aguarda a sua vez. Pediremos para "
          "contar os comprimidos que trouxe do levantamento anterior e "
          "consultaremos a sua ficha de levantamentos e o seu processo "
          "clínico, apenas para registar a data de início do tratamento, o "
          "regime e o resultado da última carga viral. A contagem não serve "
          "para o avaliar nem tem qualquer consequência sobre a entrega dos "
          "seus medicamentos."),
        P("A participação é voluntária. Pode recusar ou desistir a qualquer "
          "momento, sem dar explicações, e continuará a receber o mesmo "
          "atendimento. Pode não responder a qualquer pergunta. O seu nome "
          "não será escrito no questionário, que terá apenas um código, e as "
          "informações serão guardadas em lugar fechado e apresentadas apenas "
          "em conjunto, sem identificar ninguém. Não receberá pagamento. O "
          "risco é mínimo: algumas perguntas sobre o HIV e o álcool podem "
          "causar desconforto. Se durante a entrevista identificarmos "
          "dificuldades na toma dos medicamentos ou efeitos que o(a) "
          "preocupem, e se concordar, será encaminhado(a) no mesmo dia para o "
          "apoio psicossocial ou para o clínico do serviço."),
        P("Para esclarecimentos, pode contactar o investigador pelo telefone "
          "[preencher] ou o Comité Institucional de Bioética para a Saúde da "
          "Universidade Lúrio pelo telefone [preencher]."),
    ]),
    ("Termo de consentimento livre e esclarecido", [
        P("Declaro que me foi lida e explicada a folha de informação sobre o "
          "estudo «Adesão à terapêutica anti-retroviral e factores "
          "associados em adultos seguidos no Hospital Central de Nampula, de "
          "Abril a Junho de 2027», numa língua que compreendo, que pude fazer "
          "perguntas e que as minhas dúvidas foram esclarecidas. Compreendo "
          "que a participação é voluntária, que posso desistir a qualquer "
          "momento sem prejuízo do meu atendimento e que as minhas "
          "informações são confidenciais. Autorizo a contagem dos meus "
          "comprimidos e a consulta da minha ficha de levantamentos e do meu "
          "processo clínico para os fins descritos."),
        CAMPO("Código do participante: __________"),
        CAMPO("Assinatura do participante: ______________________________   "
              "Data: ___/___/2027"),
        CAMPO("Impressão digital (se não souber assinar):"),
        CAMPO("[   espaço para a impressão digital   ]"),
        CAMPO("Nome da testemunha imparcial: ______________________________"),
        CAMPO("Assinatura da testemunha: ______________________________   "
              "Data: ___/___/2027"),
        CAMPO("Nome de quem obteve o consentimento: "
              "______________________________"),
        CAMPO("Assinatura: ______________________________   "
              "Data: ___/___/2027"),
        NOTA("Este termo é feito em duas vias: uma fica com o participante e "
             "a outra é guardada pelo investigador, separada do "
             "questionário."),
    ]),
    ("Pedido de autorização institucional", [
        CAMPO("Ao Excelentíssimo Senhor Director-Geral do Hospital Central de "
              "Nampula"),
        CAMPO("Nampula, ____ de ________________ de 2027"),
        CAMPO("Assunto: Pedido de autorização para realização de estudo"),
        P("Eu, [Nome do(a) estudante], estudante do curso de Licenciatura em "
          "Farmácia da Faculdade de Ciências de Saúde da Universidade Lúrio, "
          "venho solicitar a Vossa Excelência autorização para realizar, na "
          "farmácia de dispensa de anti-retrovirais a adultos e no serviço de "
          "TARV deste hospital, o estudo intitulado «Adesão à terapêutica "
          "anti-retroviral e factores associados em adultos seguidos no "
          "Hospital Central de Nampula, de Abril a Junho de 2027», sob "
          "orientação de [Nome e grau académico do(a) orientador(a)]."),
        P("O estudo consiste em entrevistar 535 adultos em TARV, "
          "seleccionados por amostragem sistemática no acto do levantamento, "
          "contar os comprimidos que trazem do levantamento anterior e "
          "consultar a FILA e o processo clínico para registar a data de "
          "início da TARV, o regime e a última carga viral. A recolha decorre "
          "entre 1 de Abril e 30 de Junho de 2027, em espaço reservado, sem "
          "interferir com o funcionamento da farmácia, e só começa depois do "
          "parecer favorável do Comité Institucional de Bioética para a Saúde "
          "da Universidade Lúrio. Solicito ainda a indicação do número de "
          "adultos em TARV seguidos no hospital e do número de levantamentos "
          "mensais na farmácia, necessários ao plano de amostragem."),
        P("Comprometo-me a garantir a confidencialidade dos doentes, a não "
          "retirar documentos do hospital, a não registar nomes e a entregar "
          "à direcção um relatório com os resultados agregados e uma "
          "proposta de sessões de aconselhamento farmacêutico."),
        CAMPO("Pede deferimento."),
        CAMPO("O(A) estudante: ______________________________"),
        CAMPO("O(A) orientador(a): ______________________________"),
        NOTA("Pedidos semelhantes serão dirigidos à Direcção Provincial de "
             "Saúde de Nampula e ao SDSMAS da Cidade de Nampula."),
    ]),
]
