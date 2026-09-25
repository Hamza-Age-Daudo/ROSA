# -*- coding: utf-8 -*-
"""
Tema 09: Adequacao da profilaxia antibiotica em cesarianas no Hospital Central
de Nampula (Farmacoepidemiologia e Uso Racional de Medicamentos). Estudo
documental retrospectivo, cesarianas de 2026, recolha em 2027.

Compor e validar:   python _motor/motor.py _conteudo/tema_09.py
Verificar fontes:   python _motor/refs.py verificar _conteudo/tema_09.py
"""
from blocos import (CAMPO, FORMULA, H3, LISTA, NOTA, P, PERG, QUADRO,
                    TABELA)

NUMERO = 9
SLUG = "Profilaxia_Antibiotica_Cesarianas_HCN_Nampula"
TITULO = ("Adequação da profilaxia antibiótica nas cesarianas realizadas no "
          "Hospital Central de Nampula, de Janeiro a Dezembro de 2026")
DESENHO = ("Transversal retrospectivo, descritivo e analítico, documental "
           "(processos clínicos, fichas de anestesia e registos do bloco "
           "operatório)")

AUTOR = "[Nome do(a) estudante]"
ORIENTADOR = "[Nome e grau académico do(a) orientador(a)]"

# ---------------------------------------------------------------- resumo --
RESUMO = (
    "A cesariana é o principal factor de risco de infecção materna no "
    "pós-parto, e a profilaxia antibiótica administrada antes da incisão, em "
    "dose única, reduz de forma consistente a infecção da ferida operatória e "
    "a endometrite. Em muitos hospitais da África subsariana, porém, o "
    "antibiótico é dado depois da laqueação do cordão ou apenas no "
    "pós-operatório e mantém-se durante vários dias, o que aumenta o consumo "
    "de antibióticos e a resistência aos antimicrobianos. Não se "
    "encontrou avaliação publicada desta prática em Moçambique. O "
    "estudo tem como objectivo avaliar a adequação da profilaxia antibiótica "
    "nas cesarianas realizadas no Hospital Central de Nampula entre 1 de "
    "Janeiro e 31 de Dezembro de 2026, face às recomendações da Organização "
    "Mundial da Saúde e, quando exista, ao protocolo institucional em "
    "vigor. Trata-se de "
    "um estudo transversal, retrospectivo, descritivo e analítico, baseado "
    "nos processos clínicos, nas fichas de anestesia e nos registos do bloco "
    "operatório, com recolha em 2027. Serão seleccionadas 456 cesarianas por "
    "amostragem sistemática estratificada em cesarianas electivas e de "
    "urgência, com igual número por estrato e margem de 15% para "
    "processos não localizados ou incompletos. Uma ficha de extracção sem "
    "identificadores, validada por um painel de peritos e testada em 30 "
    "processos de 2025, registará o antibiótico, a dose, o momento da "
    "administração em relação à incisão e a duração; a adequação será "
    "classificada por dois avaliadores independentes, com dupla extracção de "
    "10% dos processos. A análise estimará proporções ponderadas com "
    "intervalos de confiança a 95%, comparará os dois grupos pelo teste do "
    "qui-quadrado e identificará os factores "
    "associados ao prolongamento da profilaxia por regressão logística. "
    "Espera-se quantificar os desvios em cada critério e o excesso de "
    "exposição a antibióticos, oferecendo ao hospital uma linha de base para "
    "a revisão do protocolo e para um programa de gestão de antimicrobianos.")
PALAVRAS_CHAVE = ["antibioticoprofilaxia", "cesariana",
                  "gestão de antimicrobianos", "Moçambique",
                  "uso racional de medicamentos"]
ABSTRACT = (
    "Caesarean section is the main risk factor for maternal postpartum "
    "infection, and antibiotic prophylaxis given as a single dose before "
    "incision consistently reduces wound infection and endometritis. In many "
    "hospitals in sub-Saharan Africa, however, the antibiotic is given after "
    "cord clamping or only after surgery and is continued for several days, "
    "which increases antibiotic consumption and favours antimicrobial "
    "resistance. No published assessment of this practice was found for "
    "Mozambique. The study aims to assess the appropriateness of antibiotic "
    "prophylaxis in caesarean sections performed at the Central Hospital of "
    "Nampula between 1 January and 31 December 2026, against the "
    "recommendations of the World Health Organization and, where one exists, "
    "the institutional protocol in force. It is a cross-sectional, "
    "retrospective, descriptive "
    "and analytical study based on clinical records, anaesthesia charts and "
    "operating theatre registers, with data collection in 2027. A total of "
    "456 caesarean sections will be selected by systematic sampling "
    "stratified into elective and emergency procedures, with equal numbers "
    "per stratum and a 15% allowance for records that cannot be located or "
    "are incomplete. A data extraction form without identifiers, validated "
    "by an expert panel and tested on 30 records from 2025, will record the "
    "antibiotic, dose, timing of administration relative to incision and "
    "duration; appropriateness will be classified by two independent "
    "reviewers, with double extraction of 10% of the records. The analysis "
    "will estimate weighted proportions with 95% confidence intervals, "
    "compare elective and emergency caesarean sections with the chi-square "
    "test and identify factors associated with prolonged prophylaxis by "
    "logistic regression. The study is expected to quantify deviations in "
    "each criterion and the excess exposure to antibiotics, giving the "
    "hospital a baseline for revising its protocol and for an antimicrobial "
    "stewardship programme.")
KEYWORDS = ["antibiotic prophylaxis", "antimicrobial stewardship",
            "caesarean section", "drug utilization", "Mozambique"]

ABREVIATURAS = [
    ("ATC", "classificação Anatómica Terapêutica Química"),
    ("AWaRe", "Access, Watch, Reserve (grupos Acesso, Vigilância e Reserva "
              "da classificação de antibióticos da OMS)"),
    ("CHTF", "Comité Hospitalar de Terapêutica e Farmácia"),
    ("CIBS-UniLúrio", "Comité Institucional de Bioética para a Saúde da "
                      "Universidade Lúrio"),
    ("CNBS", "Comité Nacional de Bioética para a Saúde"),
    ("DDD", "dose diária definida"),
    ("EV", "via endovenosa"),
    ("FCS", "Faculdade de Ciências de Saúde"),
    ("HCN", "Hospital Central de Nampula"),
    ("HIV", "vírus da imunodeficiência humana"),
    ("IC95%", "intervalo de confiança a 95%"),
    ("IIQ", "intervalo interquartil"),
    ("ILC", "infecção do local cirúrgico"),
    ("LNME", "Lista Nacional de Medicamentos Essenciais"),
    ("MISAU", "Ministério da Saúde"),
    ("OMS", "Organização Mundial da Saúde"),
    ("OR", "odds ratio"),
    ("ORa", "odds ratio ajustado"),
    ("RAM", "resistência aos antimicrobianos"),
    ("RECORD-PE", "REporting of studies Conducted using Observational "
                  "Routinely collected health Data for "
                  "PharmacoEpidemiology"),
    ("RR", "risco relativo"),
    ("SPSS", "Statistical Package for the Social Sciences"),
    ("STROBE", "Strengthening the Reporting of Observational Studies in "
               "Epidemiology"),
    ("UniLúrio", "Universidade Lúrio"),
    ("VIF", "factor de inflação da variância"),
]

# ------------------------------------------------------------ referencias --
FONTES = {
    # -- magnitude global e africana
    "betran2021": "Betran AP, Ye J, Moller AB, Souza JP, Zhang J. Trends and projections of caesarean section rates: global and regional estimates. BMJ Glob Health. 2021;6(6). doi:10.1136/bmjgh-2021-005671. PMID: 34130991.",
    "islam2025": "Islam N, Thalib L, Mahmood S, Varol SA, Adel I, Aqel A, et al. Regional variations in incidence of surgical site infection and associated risk factors in women undergoing cesarean section: A systematic review and Meta-Analysis. Intensive Crit Care Nurs. 2025;89:103951. doi:10.1016/j.iccn.2025.103951. PMID: 39881456.",
    "gloss2020": "WHO Global Maternal Sepsis Study (GLOSS) Research Group. Frequency and management of maternal infection in health facilities in 52 countries (GLOSS): a 1-week inception cohort study. Lancet Glob Health. 2020;8(5):e661-e671. doi:10.1016/S2214-109X(20)30109-1. PMID: 32353314.",
    "bishop2019": "Bishop D, Dyer RA, Maswime S, Rodseth RN, van Dyk D, Kluyts HL, et al. Maternal and neonatal outcomes after caesarean delivery in the African Surgical Outcomes Study: a 7-day prospective observational cohort study. Lancet Glob Health. 2019;7(4):e513-e522. doi:10.1016/S2214-109X(19)30036-1. PMID: 30879511.",
    # -- eficacia e recomendacoes
    "oms2021": "World Health Organization. WHO recommendation on prophylactic antibiotics for women undergoing caesarean section [Internet]. Geneva: World Health Organization; 2021 [citado 2026 Set 19]. Disponível em: https://www.who.int/publications/i/item/9789240028012",
    "oms2018": "World Health Organization. Global guidelines for the prevention of surgical site infection. 2nd ed [Internet]. Geneva: World Health Organization; 2018 [citado 2026 Set 19]. Disponível em: https://www.who.int/publications/i/item/9789241550475",
    "omsaware2022": "World Health Organization. The WHO AWaRe (Access, Watch, Reserve) antibiotic book [Internet]. Geneva: World Health Organization; 2022 [citado 2026 Set 19]. Disponível em: https://www.who.int/publications/i/item/9789240062382",
    "omsaware2025": "World Health Organization. The selection and use of essential medicines, 2025: WHO AWaRe (Access, Watch, Reserve) classification of antibiotics for evaluation and monitoring of use [Internet]. Geneva: World Health Organization; 2025 [citado 2026 Set 19]. Disponível em: https://www.who.int/publications/i/item/B09489",
    "smaill2014": "Smaill FM, Grivell RM. Antibiotic prophylaxis versus no prophylaxis for preventing infection after cesarean section. Cochrane Database Syst Rev. 2014;2014(10):CD007482. doi:10.1002/14651858.CD007482.pub3. PMID: 25350672.",
    "bollig2018": "Bollig C, Nothacker M, Lehane C, Motschall E, Lang B, Meerpohl JJ, et al. Prophylactic antibiotics before cord clamping in cesarean delivery: a systematic review. Acta Obstet Gynecol Scand. 2018;97(5):521-535. doi:10.1111/aogs.13276. PMID: 29215155.",
    "pintolopes2017": "Pinto-Lopes R, Sousa-Pinto B, Azevedo LF. Single dose versus multiple dose of antibiotic prophylaxis in caesarean section: a systematic review and meta-analysis. BJOG. 2017;124(4):595-605. doi:10.1111/1471-0528.14373. PMID: 27885778.",
    "igwemadu2022": "Igwemadu GT, Eleje GU, Eno EE, Akunaeziri UA, Afolabi FA, Alao AI, et al. Single-dose versus multiple-dose antibiotics prophylaxis for preventing caesarean section postpartum infections: A randomized controlled trial. Womens Health (Lond). 2022;18:17455057221101071. doi:10.1177/17455057221101071. PMID: 35670414.",
    "dejonge2020": "de Jonge SW, Boldingh QJJ, Solomkin JS, Dellinger EP, Egger M, Salanti G, et al. Effect of postoperative continuation of antibiotic prophylaxis on the incidence of surgical site infection: a systematic review and meta-analysis. Lancet Infect Dis. 2020;20(10):1182-1192. doi:10.1016/S1473-3099(20)30084-0. PMID: 32470329.",
    "branchelliman2019": "Branch-Elliman W, O'Brien W, Strymish J, Itani K, Wyatt C, Gupta K. Association of Duration and Type of Surgical Prophylaxis With Antimicrobial-Associated Adverse Events. JAMA Surg. 2019;154(7):590-598. doi:10.1001/jamasurg.2019.0569. PMID: 31017647.",
    "acog2018": "Committee on Practice Bulletins-Obstetrics. ACOG Practice Bulletin No. 199: Use of Prophylactic Antibiotics in Labor and Delivery. Obstet Gynecol. 2018;132(3):e103-e119. doi:10.1097/AOG.0000000000002833. PMID: 30134425.",
    "tita2016": "Tita AT, Szychowski JM, Boggess K, Saade G, Longo S, Clark E, et al. Adjunctive Azithromycin Prophylaxis for Cesarean Delivery. N Engl J Med. 2016;375(13):1231-41. doi:10.1056/NEJMoa1602044. PMID: 27682034.",
    "sanchezramos2026": "Sanchez-Ramos L, Preis R, Romero R. Prophylactic antibiotics to prevent postcesarean infection: which antimicrobial, when, how, and why?. Am J Obstet Gynecol. 2026;233(6S):S483-S503. doi:10.1016/j.ajog.2025.09.044. PMID: 41485837.",
    "wade2026": "Wade T, Looby A, Burgert J, Roberts N, Heneghan CJ, Onakpoya IJ. Surgical antibiotic prophylaxis in women undergoing caesarean delivery: a systematic review of clinical practice guidelines. J Hosp Infect. 2026;169:74-84. doi:10.1016/j.jhin.2025.11.014. PMID: 41297672.",
    "cooper2020": "Cooper L, Sneddon J, Afriyie DK, Sefah IA, Kurdi A, Godman B, et al. Supporting global antimicrobial stewardship: antibiotic prophylaxis for the prevention of surgical site infection in low- and middle-income countries (LMICs): a scoping review and meta-analysis. JAC Antimicrob Resist. 2020;2(3):dlaa070. doi:10.1093/jacamr/dlaa070. PMID: 34223026.",
    # -- pratica em Africa e noutros paises de rendimento baixo e medio
    "denardo2016": "De Nardo P, Gentilotti E, Nguhuni B, Vairo F, Chaula Z, Nicastri E, et al. Post-caesarean section surgical site infections at a Tanzanian tertiary hospital: a prospective observational study. J Hosp Infect. 2016;93(4):355-9. doi:10.1016/j.jhin.2016.02.021. PMID: 27125664.",
    "aulakh2018": "Aulakh A, Idoko P, Anderson ST, Graham W. Caesarean section wound infections and antibiotic use: a retrospective case-series in a tertiary referral hospital in The Gambia. Trop Doct. 2018;48(3):192-199. doi:10.1177/0049475517739539. PMID: 29108473.",
    "abubakar2018": "Abubakar U, Syed Sulaiman SA, Adesiyun AG. Utilization of surgical antibiotic prophylaxis for obstetrics and gynaecology surgeries in Northern Nigeria. Int J Clin Pharm. 2018;40(5):1037-1043. doi:10.1007/s11096-018-0702-0. PMID: 30054786.",
    "sway2020": "Sway A, Wanyoro A, Nthumba P, Aiken A, Ching P, Maruta A, et al. Prospective Cohort Study on Timing of Antimicrobial Prophylaxis for Post-Cesarean Surgical Site Infections. Surg Infect (Larchmt). 2020;21(6):552-557. doi:10.1089/sur.2018.226. PMID: 31951506.",
    "gentilotti2020": "Gentilotti E, De Nardo P, Nguhuni B, Piscini A, Damian C, Vairo F, et al. Implementing a combined infection prevention and control with antimicrobial stewardship joint program to prevent caesarean section surgical site infections and antimicrobial resistance: a Tanzanian tertiary hospital experience. Antimicrob Resist Infect Control. 2020;9(1):69. doi:10.1186/s13756-020-00740-7. PMID: 32430026.",
    "velin2021": "Velin L, Umutesi G, Riviello R, Muwanguzi M, Bebell LM, Yankurije M, et al. Surgical Site Infections and Antimicrobial Resistance After Cesarean Section Delivery in Rural Rwanda. Ann Glob Health. 2021;87(1):77. doi:10.5334/aogh.3413. PMID: 34430227.",
    "kakolwa2021": "Kakolwa MA, Woodd SL, Aiken AM, Manzi F, Gon G, Graham WJ, et al. Overuse of antibiotics in maternity and neonatal wards, a descriptive report from public hospitals in Dar es Salaam, Tanzania. Antimicrob Resist Infect Control. 2021;10(1):142. doi:10.1186/s13756-021-01014-6. PMID: 34627366.",
    "carshonmarsh2022": "Carshon-Marsh R, Squire JS, Kamara KN, Sargsyan A, Delamou A, Camara BS, et al. Incidence of Surgical Site Infection and Use of Antibiotics among Patients Who Underwent Caesarean Section and Herniorrhaphy at a Regional Referral Hospital, Sierra Leone. Int J Environ Res Public Health. 2022;19(7). doi:10.3390/ijerph19074048. PMID: 35409731.",
    "mbuyamba2023": "Mbuyamba HT, Muamba CM, Binene SK, Uwonda SA. Evaluation of the practice of surgical antibiotic prophylaxis in a Zonal Referral Hospital in Mbujimayi, Democratic Republic of the Congo (DRC). BMC Surg. 2023;23(1):28. doi:10.1186/s12893-023-01926-7. PMID: 36739370.",
    "habteweld2023": "Habteweld HA, Yimam M, Tsige AW, Wondmkun YT, Endalifer BL, Ayenew KD. Surgical site infection and antimicrobial prophylaxis prescribing profile, and its determinants among hospitalized patients in Northeast Ethiopia: a hospital based cross-sectional study. Sci Rep. 2023;13(1):14689. doi:10.1038/s41598-023-41834-7. PMID: 37674035.",
    "cleancut2024": "Clean Cut Investigators Group. An observational cohort study on the effects of extended postoperative antibiotic prophylaxis on surgical-site infections in low- and middle-income countries. Br J Surg. 2024;111(1). doi:10.1093/bjs/znad438. PMID: 38198157.",
    "kachipedzu2024": "Kachipedzu AT, Kulapani DK, Meja SJ, Musaya J. Surgical site infection and antimicrobial use following caesarean section at QECH in Blantyre, Malawi: a prospective cohort study. Antimicrob Resist Infect Control. 2024;13(1):131. doi:10.1186/s13756-024-01483-5. PMID: 39473007.",
    "schrama2025": "Schrama TJ, Vliegenthart-Jongbloed KJ, Gemuwang M, Nuwass EQ. Surgical prophylaxis in Haydom Lutheran Hospital, Tanzania - learning from a point prevalence survey. Infect Prev Pract. 2025;7(1):100429. doi:10.1016/j.infpip.2024.100429. PMID: 39925485.",
    "sefah2025": "Sefah IA, Chetty S, Yamoah P, Bangalee V. The impact of antimicrobial stewardship interventions on surgical antibiotic prophylaxis guidelines compliance in a teaching hospital in Ghana. PLoS One. 2025;20(8):e0329541. doi:10.1371/journal.pone.0329541. PMID: 40758736.",
    "njoroge2025": "Njoroge A, Westercamp M, Kihungi L, Ndinda M, Wesangula E, Mwangi C, et al. Implementing a surveillance and prevention program for post-caesarean surgical site infections in Kenya. Antimicrob Resist Infect Control. 2025;14(1):136. doi:10.1186/s13756-025-01633-3. PMID: 41219800.",
    "siachalinga2023": "Siachalinga L, Godman B, Mwita JC, Sefah IA, Ogunleye OO, Massele A, et al. Current Antibiotic Use Among Hospitals in the sub-Saharan Africa Region; Findings and Implications. Infect Drug Resist. 2023;16:2179-2190. doi:10.2147/IDR.S398223. PMID: 37077250.",
    "guido2025": "Guido G, Frallonardo L, Asaduzzaman M, Farkas FB, De Vita E, Seni A, et al. Third-generation Cephalosporin resistance in Sub-Saharan Africa: a systematic review and meta-analysis. Commun Med (Lond). 2025;6(1):10. doi:10.1038/s43856-025-01243-5. PMID: 41258441.",
    # -- intervencoes de gestao de antimicrobianos
    "sefah2024": "Sefah IA, Chetty S, Yamoah P, Bangalee V. The impact of antimicrobial stewardship interventions on appropriate use of surgical antimicrobial prophylaxis in low- and middle-income countries: a systematic review. Syst Rev. 2024;13(1):306. doi:10.1186/s13643-024-02731-w. PMID: 39702434.",
    "nofal2024": "Nofal MR, Tesfaye A, Gebeyehu N, Masersha MN, Hayredin I, Belayneh K, et al. A Prospective Quality Improvement Program to Reduce Prolonged Postoperative Antibiotic Prophylaxis in Ethiopia. Surg Infect (Larchmt). 2024;25(9):652-658. doi:10.1089/sur.2024.059. PMID: 38990697.",
    # -- Mocambique e Nampula
    "ine2024ids": "Instituto Nacional de Estatística; ICF. Moçambique: Inquérito Demográfico e de Saúde 2022-23, relatório definitivo [Internet]. Maputo; Rockville: INE e ICF; 2024 [citado 2026 Set 19]. Disponível em: https://dhsprogram.com/publications/publication-FR389-DHS-Final-Reports.cfm",
    "ine2021": "Instituto Nacional de Estatística. IV Recenseamento Geral da População e Habitação 2017: resultados definitivos, província de Nampula [Internet]. Nampula: Instituto Nacional de Estatística; 2021 [citado 2026 Set 19]. Disponível em: http://www.sina.gov.mz/wp-content/uploads/2024/05/NAMPULA-RESUTADOS-DEFINITIVOS-DO-CENSO-2017.pdf",
    "elshazly2026": "El-Shazly MYM, Buonamassa R, Cornelli A, El-Shazly AY, Iatta R, Gomonda EDS, et al. Surgical Site Infections in Mozambique: A Literature Review of Incidence, Antimicrobial Resistance, Risk Factors, and Surveillance Practices. Ann Glob Health. 2026;92(1):24. doi:10.5334/aogh.5143. PMID: 41800066.",
    "misau2019": "Ministério da Saúde; Ministério da Agricultura e Segurança Alimentar. Plano Nacional de Acção Contra a Resistência Antimicrobiana 2019-2023 [Internet]. Maputo: Ministério da Saúde; 2019 [citado 2026 Set 19]. Disponível em: https://www.afro.who.int/pt/publications/plano-nacional-de-accao-contra-resistencia-antimicrobiana-2019-2023",
    "misau2023": "Ministério da Saúde. Diploma Ministerial n.º 52/2023, de 19 de Abril: aprova a Lista Nacional de Medicamentos Essenciais. Boletim da República, I Série, n.º 75 [Internet]. Maputo: Imprensa Nacional de Moçambique; 2023 [citado 2026 Set 19]. Disponível em: https://cdn.who.int/media/docs/default-source/essential-medicines/national-essential-medicines-lists-(neml)/afro_neml/mozambique-updated-lista-nacional-de-medicamentos-essenciais-2023.pdf",
    "xavier2022": "Xavier SP, Victor A, Cumaquela G, Vasco MD, Rodrigues OAS. Inappropriate use of antibiotics and its predictors in pediatric patients admitted at the Central Hospital of Nampula, Mozambique. Antimicrob Resist Infect Control. 2022;11(1):79. doi:10.1186/s13756-022-01115-w. PMID: 35655272.",
    "xavier2024": "Xavier SP, da Silva AMC, Victor A. Antibiotic prescribing patterns in pediatric patients using the WHO access, watch, reserve (AWaRe) classification at a quaternary hospital in Nampula, Mozambique. Sci Rep. 2024;14(1):22719. doi:10.1038/s41598-024-72349-4. PMID: 39349590.",
    "kenga2026": "Kenga DB, Sacarlal J, Sidat M, Chicamba V, Kenga AN, Manjate Y, et al. Knowledge, attitudes, and practices of antimicrobial resistance and stewardship among pediatric health professionals in Maputo, Mozambique. Antimicrob Resist Infect Control. 2026;15(1). doi:10.1186/s13756-026-01729-4. PMID: 41845534.",
    "lei3de2023": "República de Moçambique. Lei n.º 3/2023, de 8 de Junho: Lei de Investigação em Saúde Humana [Internet]. Maputo: Imprensa Nacional de Moçambique; 2023 [citado 2026 Set 19]. Disponível em: https://anarme.gov.mz/download/lei-3-2023-de-8-de-junho-lei-de-investigacao-em-saude-humana/",
    # -- metodo, estatistica, relato e etica
    "omspps2019": "World Health Organization. WHO methodology for point prevalence survey on antibiotic use in hospitals, version 1.1 (WHO/EMP/IAU/2018.01) [Internet]. Geneva: World Health Organization; 2019 [citado 2026 Set 19]. Disponível em: https://www.who.int/publications/i/item/WHO-EMP-IAU-2018.01",
    "whocc2026": "WHO Collaborating Centre for Drug Statistics Methodology. ATC/DDD Index 2026 [Internet]. Oslo: Norwegian Institute of Public Health; 2026 [citado 2026 Set 19]. Disponível em: https://atcddd.fhi.no/atc_ddd_index/",
    "peduzzi1996": "Peduzzi P, Concato J, Kemper E, Holford TR, Feinstein AR. A simulation study of the number of events per variable in logistic regression analysis. J Clin Epidemiol. 1996;49(12):1373-9. doi:10.1016/s0895-4356(96)00236-3. PMID: 8970487.",
    "mchugh2012": "McHugh ML. Interrater reliability: the kappa statistic. Biochem Med (Zagreb). 2012;22(3):276-82. PMID: 23092060.",
    "vonelm2007": "von Elm E, Altman DG, Egger M, Pocock SJ, Gøtzsche PC, Vandenbroucke JP. Strengthening the Reporting of Observational Studies in Epidemiology (STROBE) statement: guidelines for reporting observational studies. BMJ. 2007;335(7624):806-8. doi:10.1136/bmj.39335.541782.AD. PMID: 17947786.",
    "langan2018": "Langan SM, Schmidt SA, Wing K, Ehrenstein V, Nicholls SG, Filion KB, et al. The reporting of studies conducted using observational routinely collected health data statement for pharmacoepidemiology (RECORD-PE). BMJ. 2018;363:k3532. doi:10.1136/bmj.k3532. PMID: 30429167.",
    "wma2025": "World Medical Association. World Medical Association Declaration of Helsinki: Ethical Principles for Medical Research Involving Human Participants. JAMA. 2025;333(1):71-74. doi:10.1001/jama.2024.21972. PMID: 39425955.",
}

SEMINAIS = {
    "smaill2014": ("Revisão sistemática Cochrane de referência (95 ensaios) que "
                   "estabelece a eficácia da profilaxia antibiótica na "
                   "cesariana; é a base da recomendação da OMS e não foi "
                   "substituída por revisão mais recente."),
    "vonelm2007": ("Declaração STROBE original, norma de relato dos estudos "
                   "observacionais que a extensão RECORD-PE complementa."),
    "peduzzi1996": ("Estudo de simulação que fundamenta a regra de pelo menos "
                    "10 eventos por variável na regressão logística, usada no "
                    "planeamento do modelo multivariável."),
    "mchugh2012": ("Artigo metodológico de referência sobre a interpretação "
                   "do kappa de Cohen em estudos de saúde, usado para fixar o "
                   "limiar de concordância entre avaliadores."),
}

# ----------------------------------------------------- 1. introducao --------
INTRODUCAO = [
    P("A cesariana tornou-se a intervenção cirúrgica mais frequente em muitos "
      "hospitais. Em 154 países que concentram 94,5% dos nascimentos, 21,1% "
      "das mulheres deram à luz por cesariana, com médias que vão de 5% na "
      "África subsariana a 42,8% na América Latina e Caraíbas, e as "
      "projecções apontam para 28,5% em 2030 {betran2021}. A cirurgia salva "
      "vidas quando é indicada, mas é também o factor de risco mais "
      "importante de infecção no puerpério imediato, com um risco cinco a "
      "vinte vezes maior do que o do parto vaginal; as infecções maternas à "
      "volta do parto causam, além disso, cerca de um milhão de mortes "
      "neonatais por ano {oms2021}. Numa meta-análise de 49 coortes, com "
      "271.954 mulheres, a incidência de infecção do local cirúrgico (ILC) "
      "após cesariana foi de 7,0%, subiu para 8,0% nos países de rendimento "
      "baixo e médio e foi significativamente mais alta em África "
      "{islam2025}. No estudo multicêntrico da Organização Mundial da Saúde "
      "(OMS) sobre sepse materna, 70,4 mulheres hospitalizadas por cada 1.000 "
      "nados-vivos tinham uma infecção materna, e as mortes relacionadas com "
      "infecção representaram mais de metade das mortes intra-hospitalares "
      "{gloss2020}."),
    P("A profilaxia antibiótica é a medida isolada mais eficaz para prevenir "
      "estas infecções. Na revisão Cochrane de 95 ensaios, com mais de 15.000 "
      "mulheres, a profilaxia reduziu a infecção da ferida, com um risco "
      "relativo (RR) de 0,40, a endometrite (RR 0,38) e as complicações "
      "infecciosas graves (RR 0,31), isto é, entre 60% e 70% {smaill2014}. A "
      "administração antes da incisão da pele é mais eficaz do que a "
      "administração depois da laqueação do cordão, sem prejuízo para o "
      "recém-nascido {bollig2018}. Por isso, a OMS recomenda uma dose única "
      "de uma cefalosporina de primeira geração ou de uma penicilina, "
      "administrada 30 a 60 minutos antes da incisão, em todas as "
      "cesarianas, electivas ou de urgência {oms2021}, e desaconselha a "
      "continuação da profilaxia depois do fim da cirurgia "
      "{oms2018,omsaware2022}."),
    P("A prática na África subsariana afasta-se com frequência destas "
      "recomendações. No African Surgical Outcomes Study, a mortalidade "
      "materna depois da cesariana foi 50 vezes superior à dos países de "
      "rendimento alto {bishop2019}. Num hospital de referência da Gâmbia, só "
      "7,4% das mulheres receberam a profilaxia antes da cirurgia e todas "
      "receberam várias doses no pós-operatório {aulakh2018}; em três "
      "hospitais do norte da Nigéria, a profilaxia foi prolongada em todas "
      "as intervenções obstétricas e ginecológicas, com uma duração média de "
      "8,7 dias {abubakar2018}; em hospitais públicos de Dar es Salaam, entre "
      "90% e 100% das mulheres receberam antibióticos depois da cesariana "
      "{kakolwa2021}. A nível mundial, o inquérito de prevalência de 2015 "
      "encontrou profilaxia cirúrgica prolongada por mais de um dia em 40,6% "
      "a 86,3% das prescrições profilácticas, consoante a região "
      "{omsaware2022}. Este excesso "
      "ocorre num contexto em que a prevalência agregada de agentes "
      "patogénicos resistentes às cefalosporinas de terceira geração na "
      "África subsariana atingiu 45,3% {guido2025}."),
    P("Em Moçambique, segundo o Inquérito Demográfico e de Saúde de 2022-23, "
      "5,2% dos nascidos vivos nos dois anos anteriores nasceram por "
      "cesariana, com 11,3% na área urbana e 2,8% na rural, e a razão de "
      "mortalidade materna foi estimada em 233 mortes por 100.000 nascidos "
      "vivos {ine2024ids}. A evidência sobre a ILC no país é escassa e "
      "fragmentada: uma revisão recente não encontrou estimativas nacionais "
      "da sua incidência, descreveu a vigilância nacional como praticamente "
      "ausente e registou prevalências de *Staphylococcus aureus* resistente "
      "à meticilina entre 15% e 42% nos hospitais estudados {elshazly2026}. "
      "O Plano Nacional de Acção Contra a Resistência Antimicrobiana "
      "reconhece que o uso excessivo e inadequado de antimicrobianos é o "
      "maior condutor da resistência e prevê a criação de equipas de gestão "
      "de antimicrobianos nos hospitais centrais e a realização de "
      "auditorias do uso de medicamentos pelos Comités Hospitalares de "
      "Terapêutica e Farmácia (CHTF) {misau2019}."),
    P("A província de Nampula é a mais populosa do país, com 5.758.920 "
      "habitantes no censo de 2017, 20,6% da população nacional {ine2021}, e "
      "a percentagem de partos por cesariana na província, 2,9%, está entre "
      "as mais baixas de Moçambique {ine2024ids}. O Hospital Central de "
      "Nampula (HCN) é um hospital de nível quaternário {xavier2024} e, como "
      "tal, a referência para os casos que as unidades de menor nível não "
      "conseguem resolver. Os "
      "estudos publicados sobre antibióticos no HCN referem-se à pediatria: "
      "97,5% das crianças internadas recebiam antibióticos e 36,5% das "
      "prescrições tinham erros, sobretudo de duração (74,1% dos erros "
      "detectados) e de dose (24,4%) {xavier2022}. Não se encontrou nenhum "
      "estudo sobre a "
      "profilaxia antibiótica na cesariana no HCN nem noutro hospital "
      "moçambicano."),
    P("Esta ausência de dados impede o hospital de saber se a profilaxia é "
      "dada a todas as mulheres, com o antibiótico e a dose adequados, no "
      "momento certo e sem prolongamentos desnecessários, e impede também o "
      "CHTF de fixar metas e de medir o efeito de qualquer intervenção. O "
      "presente estudo pretende avaliar a adequação da profilaxia "
      "antibiótica nas cesarianas realizadas no HCN de 1 de Janeiro a 31 de "
      "Dezembro de 2026, face às recomendações da OMS e, quando exista, ao "
      "protocolo institucional em vigor, e identificar os factores "
      "associados ao seu "
      "prolongamento, produzindo a primeira linha de base moçambicana para a "
      "gestão de antimicrobianos em obstetrícia."),
]

# ----------------------------------------------------- 2. problema ----------
PROBLEMA = [
    P("Como hospital de referência, o HCN realiza cesarianas electivas e de "
      "urgência, incluindo em mulheres referidas em trabalho de parto ou com "
      "ruptura de membranas, situações que aumentam o risco de infecção "
      "{oms2021} e em que a tentação de prolongar os antibióticos é maior. Nos hospitais de países de "
      "rendimento baixo e médio, a profilaxia pós-operatória é comum porque "
      "se crê que protege contra a infecção {cleancut2024}, e a administração "
      "exclusivamente pós-operatória continua a ser a norma em grande parte "
      "da África subsariana {sway2020}. No próprio HCN, o padrão encontrado "
      "na pediatria, em que a duração representou quase três quartos dos "
      "erros de prescrição detectados {xavier2022}, sugere que o "
      "prolongamento de esquemas "
      "antibióticos não é raro na instituição, embora não se saiba se o "
      "mesmo acontece na maternidade."),
    P("As consequências de uma profilaxia inadequada somam-se em duas "
      "direcções. Quando o antibiótico é dado tarde, depois da laqueação do "
      "cordão ou só no pós-operatório, perde-se parte do efeito protector: "
      "num estudo queniano, a ILC foi de 4,0% no hospital que dava a "
      "profilaxia antes da incisão e de 9,3% no que só a dava depois da "
      "cirurgia {sway2020}. Quando a profilaxia é prolongada, não se ganha "
      "protecção adicional {dejonge2020}: numa coorte de 8.714 doentes de "
      "quatro países, a manutenção dos antibióticos por 24 horas ou mais não "
      "reduziu a ILC e aumentou o internamento em 1,4 dias {cleancut2024}, e "
      "cada dia a mais de profilaxia associa-se a mais lesão renal aguda e a "
      "mais infecção por *Clostridioides difficile* {branchelliman2019}. A "
      "exposição desnecessária selecciona bactérias resistentes na "
      "microbiota da própria doente {omsaware2022}, num contexto regional em "
      "que, num hospital rural do Ruanda, nenhum dos bacilos Gram-negativos "
      "isolados das feridas de cesariana era sensível à ampicilina e a grande "
      "maioria resistia à ceftriaxona {velin2021}."),
    P("Falta saber, para o HCN, que antibiótico é usado, em que dose, em que "
      "momento em relação à incisão e durante quanto tempo, e que "
      "características da mulher, da cirurgia e da organização do serviço "
      "se associam ao prolongamento. Não se encontrou publicada uma norma "
      "nacional específica de profilaxia antibiótica cirúrgica ou "
      "obstétrica; a Lista Nacional de Medicamentos Essenciais (LNME) inclui "
      "a cefazolina injectável {misau2023}, mas desconhece-se a sua "
      "disponibilidade e o seu uso efectivo na maternidade, e a existência e "
      "o conteúdo do protocolo institucional de profilaxia terão de ser "
      "confirmados [confirmar junto da Direcção Clínica do HCN]. Sem uma "
      "linha de base medida com critérios explícitos, o CHTF não pode "
      "cumprir a tarefa de auditoria que o plano nacional lhe atribui "
      "{misau2019}, nem saber onde intervir primeiro."),
]
PERGUNTA = ("Em que medida a profilaxia antibiótica administrada nas "
            "cesarianas realizadas no Hospital Central de Nampula entre 1 de "
            "Janeiro e 31 de Dezembro de 2026 é adequada quanto à escolha do "
            "antibiótico, à dose, ao momento da administração em relação à "
            "incisão e à duração, e que factores se associam ao seu "
            "prolongamento?")
DELIMITACAO = [
    P("O estudo decorre no Departamento de Ginecologia e Obstetrícia do HCN, "
      "cidade de Nampula, e abrange as cesarianas realizadas no bloco "
      "operatório da maternidade entre 1 de Janeiro e 31 de Dezembro de "
      "2026, com consulta dos arquivos entre Março e Maio de 2027. A "
      "população é constituída pelas mulheres submetidas a cesariana nesse "
      "período e a unidade de análise é o episódio de cesariana. O objecto é "
      "o uso de antibióticos com finalidade profiláctica, avaliado pela "
      "escolha do antibiótico, pela dose, pelo momento da administração em "
      "relação à incisão da pele e pela duração, e a exposição total medida "
      "em doses diárias definidas (DDD)."),
    P("Ficam fora do estudo a incidência de ILC depois da alta, que exigiria "
      "seguimento prospectivo, a microbiologia das infecções, a "
      "antibioterapia dirigida a infecções diagnosticadas antes da cirurgia, "
      "os partos vaginais, as outras cirurgias obstétricas e ginecológicas e "
      "as cesarianas realizadas noutras unidades sanitárias. Os "
      "conhecimentos e as atitudes dos prescritores também não são medidos, "
      "embora os resultados possam orientar um estudo posterior com essa "
      "finalidade."),
]

# ----------------------------------------------------- 3. objectivos --------
OBJECTIVO_GERAL = (
    "Avaliar a adequação da profilaxia antibiótica nas cesarianas realizadas "
    "no Hospital Central de Nampula entre 1 de Janeiro e 31 de Dezembro de "
    "2026, face às recomendações da Organização Mundial da Saúde e, quando "
    "exista, ao protocolo institucional em vigor.")
OBJECTIVOS_ESPECIFICOS = [
    "Caracterizar as mulheres submetidas a cesariana segundo as variáveis "
    "sociodemográficas, obstétricas e cirúrgicas;",
    "Descrever os esquemas de profilaxia antibiótica administrados "
    "(antibiótico, dose, via, momento em relação à incisão e duração) e "
    "quantificar a exposição a antibióticos em doses diárias definidas por "
    "cesariana;",
    "Determinar a proporção de cesarianas com profilaxia adequada quanto à "
    "escolha do antibiótico, à dose, ao momento da administração e à "
    "duração, e a proporção globalmente adequada;",
    "Comparar a proporção de administrações no momento adequado entre as "
    "cesarianas electivas e as cesarianas de urgência;",
    "Analisar os factores clínicos, cirúrgicos e organizacionais associados "
    "ao prolongamento da profilaxia por 24 horas ou mais depois da "
    "cirurgia.",
]

# ----------------------------------------------------- 4. hipoteses ---------
HIPOTESES_INTRO = [
    P("As hipóteses referem-se às componentes analíticas do estudo, isto é, "
      "aos objectivos específicos 4 e 5, e serão testadas com um nível de "
      "significância de 5%. Os objectivos 1 a 3 são descritivos e "
      "orientam-se pelas questões de investigação apresentadas a seguir."),
]
HIPOTESES = [
    ("H0 (objectivo específico 4)",
     "não existe diferença estatisticamente significativa na proporção de "
     "profilaxias administradas nos 60 minutos anteriores à incisão entre as "
     "cesarianas electivas e as cesarianas de urgência."),
    ("H1 (objectivo específico 4)",
     "existe diferença estatisticamente significativa na proporção de "
     "profilaxias administradas nos 60 minutos anteriores à incisão entre as "
     "cesarianas electivas e as cesarianas de urgência."),
    ("H0 (objectivo específico 5)",
     "o tipo de cesariana, a ruptura de membranas antes da cirurgia, a "
     "categoria profissional do cirurgião, o turno da cirurgia, a infecção "
     "pelo vírus da imunodeficiência humana (HIV) e a hemorragia "
     "intra-operatória não se associam de forma estatisticamente "
     "significativa ao prolongamento da profilaxia por 24 horas ou mais."),
    ("H1 (objectivo específico 5)",
     "pelo menos um destes factores associa-se de forma estatisticamente "
     "significativa ao prolongamento da profilaxia por 24 horas ou mais."),
]
QUESTOES = [
    "Quais são as características sociodemográficas, obstétricas e "
    "cirúrgicas das mulheres submetidas a cesariana no HCN em 2026?",
    "Que antibióticos, doses, vias, momentos de administração e durações "
    "compõem a profilaxia registada, e qual é a exposição média em DDD por "
    "cesariana?",
    "Que proporção das cesarianas recebe profilaxia adequada em cada "
    "critério e em todos os critérios em simultâneo?",
]

# ----------------------------------------------------- 5. justificativa -----
JUSTIFICATIVA_INTRO = [
    P("A profilaxia antibiótica na cesariana é, simultaneamente, uma das "
      "intervenções mais eficazes da obstetrícia e uma das utilizações de "
      "antibióticos mais frequentes numa maternidade. Por ser barata, "
      "simples e dirigida a um momento preciso, é também uma das práticas "
      "mais fáceis de corrigir quando se conhece o desvio: uma dose única, "
      "dada à hora certa, protege a mulher e poupa antibióticos. O estudo "
      "justifica-se por quatro razões complementares."),
]
JUSTIFICATIVA = {
    "cientifica": [
        P("O estudo produz os primeiros dados moçambicanos sobre a adequação "
          "da profilaxia antibiótica na cesariana, num país onde a evidência "
          "sobre a ILC é descrita como escassa e fragmentada {elshazly2026}. "
          "Uma revisão de 51 estudos de países de rendimento baixo e médio "
          "concluiu que os dados de vigilância são pobres e que faltam "
          "orientações locais de profilaxia {cooper2020}. Ao contrário de "
          "muitos estudos africanos, que registam apenas se houve profilaxia "
          "antes da incisão, este aplica quatro critérios explícitos, mede a "
          "exposição em DDD, compara cesarianas electivas e de urgência e "
          "quantifica a concordância entre avaliadores, o que torna os "
          "resultados comparáveis com os de outros hospitais da região."),
    ],
    "academica": [
        P("Para a Licenciatura em Farmácia da Faculdade de Ciências de Saúde "
          "(FCS) da Universidade Lúrio (UniLúrio), o estudo treina o "
          "estudante em investigação de utilização de medicamentos, na "
          "leitura crítica de processos clínicos, na classificação "
          "Anatómica Terapêutica Química (ATC) e no cálculo de DDD, "
          "competências centrais do farmacêutico hospitalar. Dá continuidade "
          "à linha de trabalho sobre o uso de antibióticos no HCN iniciada "
          "na pediatria {xavier2022,xavier2024} e deixa uma ficha de "
          "extracção validada que pode ser reutilizada noutros serviços "
          "cirúrgicos ou numa segunda medição, depois de uma intervenção."),
    ],
    "social": [
        P("As mulheres de Nampula têm menos acesso à cesariana do que as da "
          "maioria das províncias {ine2024ids}; quando a cirurgia é feita, "
          "deve ser segura. A infecção pós-cesariana causa morbilidade grave e "
          "incapacidade duradoura, e as infecções maternas à volta do parto "
          "associam-se a cerca de um milhão de mortes neonatais por ano "
          "{oms2021}; num hospital do Malawi, 60% das mulheres com ILC foram "
          "reinternadas {kachipedzu2024}. No país, 53,4% das mulheres que "
          "tiveram um nado-vivo por cesariana numa unidade sanitária "
          "ficaram internadas três ou mais dias {ine2024ids}, e o "
          "prolongamento da profilaxia associa-se a internamentos mais "
          "longos {cleancut2024}, com custos para as famílias e para o "
          "hospital. Uma profilaxia correcta protege a mulher sem a expor a "
          "antibióticos de que não precisa."),
    ],
    "politica": [
        P("O Plano Nacional de Acção Contra a Resistência Antimicrobiana "
          "prevê equipas de gestão de antimicrobianos nos hospitais "
          "centrais, o reforço dos CHTF em todos os hospitais e a "
          "apresentação de auditorias sobre o uso de medicamentos "
          "{misau2019}. A LNME de 2023 passou a indicar o grupo da "
          "classificação AWaRe (Acesso, Vigilância e Reserva) de cada "
          "antibiótico {misau2023,omsaware2025}. O estudo oferece ao HCN "
          "uma auditoria de base que responde a estas orientações, "
          "fundamenta a revisão do protocolo institucional à luz da "
          "recomendação da OMS {oms2021} e permite medir o efeito de "
          "intervenções de gestão de antimicrobianos, que em países de "
          "rendimento baixo e médio melhoraram a adesão às orientações de "
          "profilaxia cirúrgica {sefah2024}."),
    ],
}

# ----------------------------------------------------- 6. revisao -----------
REVISAO = [
    ("Cesariana, infecção pós-cesariana e definições operacionais", [
        P("A cesariana é um procedimento cirúrgico que envolve uma incisão "
          "no abdómen e no útero para o nascimento de um ou mais bebés "
          "{ine2024ids}. Por abrir o tracto genital em condições "
          "controladas, a ferida é classificada como limpa-contaminada "
          "{omsaware2022}. A ILC define-se como a infecção que ocorre até 30 "
          "dias depois da cirurgia e atinge a pele e o tecido subcutâneo da "
          "incisão (superficial), os tecidos profundos, como a fáscia e o "
          "músculo (profunda), ou qualquer órgão ou espaço manipulado "
          "durante a operação {omsaware2022}. Na cesariana, as infecções "
          "peri-operatórias incluem a infecção da ferida, a endometrite e a "
          "infecção urinária {oms2021}."),
        P("A profilaxia antibiótica consiste na administração de um "
          "antibiótico eficaz antes da exposição à contaminação cirúrgica, "
          "para prevenir complicações infecciosas {omsaware2022}, e "
          "distingue-se da antibioterapia, que trata uma infecção já "
          "presente. Neste estudo, considera-se profiláctica toda a dose "
          "administrada entre a decisão cirúrgica e as 24 horas seguintes ao "
          "fim da cirurgia, e todas as doses posteriores, incluindo as "
          "prescritas por via oral na alta, quando não exista um diagnóstico "
          "de infecção registado no processo antes dessa dose. A cesariana é "
          "electiva quando foi programada e realizada fora do trabalho de "
          "parto e de urgência quando foi decidida durante o trabalho de "
          "parto ou por uma complicação materna ou fetal aguda. O momento de "
          "referência é a hora da incisão da pele registada na ficha de "
          "anestesia ou no relatório operatório, e o fim da cirurgia é a "
          "hora do encerramento da pele."),
        P("A frequência da infecção pós-cesariana varia muito com o "
          "contexto. Estima-se que ocorra em 5% a 20% das mulheres depois da "
          "cesariana {sanchezramos2026}; a OMS cita taxas de infecção de 3% "
          "a 11% nos países de rendimento alto e de 3% a 24% nos de "
          "rendimento baixo e médio {omsaware2022}. A meta-análise mais "
          "recente estimou uma incidência global de 7,0%, de 8,0% nos países "
          "de rendimento baixo e médio e significativamente mais alta em "
          "África, e associou a infecção a factores maternos, à técnica "
          "cirúrgica e à qualidade dos cuidados {islam2025}."),
    ]),
    ("Eficácia e fundamentos da profilaxia antibiótica na cesariana", [
        P("A eficácia da profilaxia está bem estabelecida. Na revisão "
          "Cochrane, a redução foi observada também nas cesarianas "
          "electivas, com RR de 0,62 para a infecção da ferida e de 0,38 "
          "para a endometrite, e foi semelhante com a maioria dos "
          "antibióticos e das associações estudadas {smaill2014}. A revisão "
          "concluiu que a profilaxia deve ser administrada por rotina a "
          "todas as mulheres submetidas a cesariana, electiva ou não "
          "{smaill2014}, e a OMS reafirmou esta posição em 2021, ao "
          "recomendar a profilaxia para as cesarianas electivas e de "
          "urgência {oms2021}."),
        P("O momento da administração foi durante décadas debatido, pelo "
          "receio de expor o recém-nascido ao antibiótico. Numa revisão de "
          "18 ensaios, a administração antes da incisão reduziu a morbilidade "
          "infecciosa (RR 0,72), a endometrite (RR 0,57) e a infecção da "
          "ferida (RR 0,62) em comparação com a administração depois da "
          "laqueação do cordão, sem diferenças nos desfechos neonatais "
          "{bollig2018}. Nos países de rendimento baixo e médio, a "
          "meta-análise dos ensaios em cesariana encontrou um RR de 0,77 a "
          "favor da administração antes da incisão, com um intervalo de "
          "confiança que incluía a unidade {cooper2020}, o que reforça a "
          "necessidade de dados locais."),
        P("Quanto à escolha, a OMS recomenda uma cefalosporina de primeira "
          "geração ou uma penicilina, em dose única, de preferência a outras "
          "classes; desaconselha as cefalosporinas de terceira geração, que "
          "a evidência sugere serem menos eficazes do que as penicilinas "
          "nesta indicação, e desaconselha a amoxicilina com ácido "
          "clavulânico antes da laqueação do cordão nas cesarianas "
          "pré-termo, pelo risco de enterocolite necrosante no "
          "recém-nascido {oms2021}. A cefazolina é o agente padrão pela "
          "actividade, pela "
          "farmacocinética e pela segurança; nas alergias graves aos "
          "betalactâmicos usa-se a clindamicina com gentamicina, associação "
          "que se acompanha de mais ILC {sanchezramos2026}. Nos Estados "
          "Unidos, a adição de azitromicina 500 mg às cesarianas não "
          "electivas reduziu a infecção de 12,0% para 6,1% {tita2016} e foi "
          "incorporada nas orientações do colégio de obstetras "
          "{acog2018}, mas não faz parte da recomendação da OMS."),
    ]),
    ("Critérios de adequação: escolha, dose, momento e duração", [
        P("A adequação da profilaxia é um conceito com várias dimensões. Os "
          "estudos africanos mais completos avaliam a indicação, a escolha "
          "do antibiótico, a dose, o momento da primeira administração e a "
          "duração, e só consideram adequada a profilaxia que cumpre todos "
          "os critérios {mbuyamba2023}; outros confiam a classificação a um "
          "farmacêutico clínico, a partir de uma norma de referência "
          "{abubakar2018}. Como as orientações diferem entre si e a sua "
          "qualidade metodológica é variável, a norma de referência deve "
          "ser explícita: numa revisão de 11 directrizes publicadas entre "
          "2015 e 2025, só 45% recomendavam de forma explícita a cefazolina "
          "antes da incisão {wade2026}."),
        P("A dose de referência da cefazolina no adulto é de 2 g por via "
          "endovenosa (EV), com doses mais altas, por exemplo 3 g, nas "
          "mulheres com mais de 120 kg {omsaware2022}; a obesidade duplica "
          "o risco de ILC e altera a farmacocinética do antibiótico "
          "{sanchezramos2026}. Em cirurgias longas, justifica-se uma segunda "
          "dose de cefazolina quatro horas depois da primeira, ou perante "
          "uma perda sanguínea major {omsaware2022}. A OMS admite que outros "
          "factores, como o índice de massa corporal elevado, o trabalho de "
          "parto prolongado ou a hemorragia maciça, possam justificar uma "
          "dose maior ou uma segunda dose, por decisão clínica {oms2021}."),
        P("Para o momento, a directriz geral da OMS recomenda a "
          "administração nos 120 minutos que antecedem a incisão, porque a "
          "administração mais precoce aumentou o risco de ILC, com um "
          "*odds ratio* (OR) de 5,26 {oms2018}; a recomendação específica "
          "para a cesariana "
          "fixa uma janela de 30 a 60 minutos antes da incisão {oms2021}, e "
          "a revisão mais recente refere uma dose única nos 60 minutos "
          "anteriores {sanchezramos2026}. Este estudo adopta como critério "
          "principal a administração nos 60 minutos anteriores à incisão e "
          "usa as janelas de 30 a 60 e de 120 minutos em análises de "
          "sensibilidade."),
        P("Para a duração, a profilaxia não deve continuar depois da "
          "cirurgia, mesmo na presença de dreno, porque uma dose cobre todo "
          "o período de contaminação {omsaware2022}. A meta-análise de 52 "
          "ensaios, com 19.273 participantes, não mostrou benefício da "
          "continuação quando se cumpriam as boas práticas (RR 1,04) "
          "{dejonge2020}; na cesariana, dose única e doses múltiplas não "
          "diferiram na morbilidade infecciosa (RR 0,95) {pintolopes2017}, "
          "e um ensaio nigeriano com ceftriaxona e metronidazol obteve "
          "resultados equivalentes com a dose única {igwemadu2022}. A "
          "metodologia da OMS para inquéritos de prevalência classifica a "
          "duração em dose única, várias doses num dia e várias doses em "
          "mais de um dia {omspps2019}; o estudo adopta estas três "
          "categorias, mas conta o tempo a partir do fim da cirurgia e em "
          "janelas de 24 horas, por ser essa a referência das recomendações "
          "sobre a duração da profilaxia {oms2018,omsaware2022}."),
    ]),
    ("Uso excessivo de antibióticos na profilaxia cirúrgica e as suas "
     "consequências", [
        P("A profilaxia cirúrgica é uma das principais razões de uso de "
          "antibióticos nos hospitais: no inquérito mundial de 2015, "
          "representou 17,8% de todas as prescrições {omsaware2022}. Nos "
          "hospitais da África subsariana, a prevalência de uso de "
          "antibióticos variou entre 37,7% na África do Sul e 80,1% na "
          "Nigéria, a adesão às orientações chegou a ser de apenas 4% e a "
          "profilaxia prolongada para além de 24 horas foi frequente "
          "{siachalinga2023}. Num hospital rural da Tanzânia, nenhum doente "
          "recebeu a profilaxia em dose única, 67% receberam-na por mais de "
          "24 horas e 33% dos antibióticos usados não eram recomendados pela "
          "OMS {schrama2025}; no nordeste da Etiópia, a ceftriaxona foi o "
          "antibiótico profiláctico mais usado (70,5%) e 78% dos doentes "
          "receberam uma profilaxia inadequada {habteweld2023}."),
        P("O prolongamento tem custos clínicos. Na coorte multinacional "
          "Clean Cut, 92,9% dos doentes receberam antibióticos depois da "
          "cirurgia e 27,7% durante 24 horas ou mais, sem redução da ILC "
          "(RR 1,09) e com mais 1,4 dias de internamento {cleancut2024}. "
          "Numa coorte de 79.058 intervenções, cada dia adicional de "
          "profilaxia aumentou a probabilidade de lesão renal aguda e de "
          "infecção por *Clostridioides difficile*, que chegou a um OR "
          "ajustado (ORa) de 3,65 com 72 horas ou mais {branchelliman2019}. "
          "Limitar a profilaxia a uma dose reduz também a selecção de "
          "bactérias resistentes na microbiota da doente {omsaware2022}."),
        P("A resistência aos antimicrobianos (RAM) fecha o círculo, porque "
          "compromete a própria profilaxia. Na África subsariana, a "
          "prevalência de resistência às cefalosporinas de terceira geração "
          "subiu de 22,8% antes de 2009 para 42,0% entre 2020 e 2024, e as "
          "enfermarias cirúrgicas estão entre os locais de maior risco "
          "{guido2025}. No Ruanda rural, 68,4% dos isolados das ILC "
          "pós-cesariana eram Gram-negativos, nenhum era sensível à "
          "ampicilina e 92,1% eram resistentes ou intermédios à ceftriaxona "
          "{velin2021}."),
        P("A literatura aponta determinantes do prolongamento que orientam "
          "as variáveis do quinto objectivo. A crença de que os antibióticos "
          "pós-operatórios protegem {cleancut2024} e a falta de orientações "
          "locais, somadas a convicções fortemente enraizadas {cooper2020}, "
          "surgem como factores individuais e culturais; a documentação "
          "também pesa, pois 90% das prescrições profilácticas de um hospital "
          "tanzaniano não tinham justificação registada e 83% não tinham "
          "data de suspensão ou revisão {schrama2025}. Em Moçambique, só 34% "
          "dos profissionais de pediatria do Hospital Central de Maputo "
          "conheciam o conceito de programa de gestão de antimicrobianos "
          "{kenga2026}. As características clínicas, como a ruptura de "
          "membranas, o trabalho de parto prolongado e a hemorragia, "
          "aumentam o risco percebido e podem motivar doses adicionais "
          "{oms2021}."),
    ]),
    ("Enquadramento normativo e programático em Moçambique", [
        P("O Plano Nacional de Acção Contra a Resistência Antimicrobiana "
          "2019-2023, elaborado pelo Ministério da Saúde (MISAU) e pelo "
          "Ministério da Agricultura e Segurança Alimentar, tem como visão "
          "assegurar o uso racional dos antimicrobianos e define como "
          "objectivo estratégico a optimização do uso de antibióticos na "
          "saúde humana e animal. O plano reconhece que em Moçambique a "
          "maioria dos antibióticos é usada de forma empírica e que o uso "
          "apropriado depende de protocolos de tratamento actualizados; entre "
          "as acções previstas contam-se o estabelecimento de equipas de "
          "gestão de antimicrobianos em todos os hospitais centrais, o "
          "reforço dos CHTF, a apresentação de auditorias sobre o uso de "
          "medicamentos e um programa de vigilância das infecções "
          "hospitalares {misau2019}."),
        P("A LNME aprovada pelo Diploma Ministerial n.º 52/2023 inclui a "
          "cefazolina injectável de 1 g, a ampicilina injectável, a "
          "gentamicina, a clindamicina injectável e o metronidazol, todos no "
          "grupo Acesso, e a ceftriaxona no grupo Vigilância {misau2023}, em "
          "linha com a classificação AWaRe da OMS {omsaware2025}. A "
          "presença da cefazolina na lista nacional significa que a escolha "
          "recomendada pela OMS é, em princípio, possível no sistema "
          "público; o estudo registará a disponibilidade do medicamento na "
          "farmácia do HCN em 2026 para interpretar os desvios na escolha."),
        P("Não se encontrou, nos repositórios públicos do MISAU e da OMS, "
          "uma norma nacional de profilaxia antibiótica cirúrgica ou "
          "específica da cesariana. Os estudos sobre antibióticos no HCN "
          "recorreram, por isso, a referências internacionais {xavier2022}. "
          "Na mesma linha, este estudo usa como norma de referência a "
          "recomendação da OMS para a cesariana {oms2021}, completada pelo "
          "livro de antibióticos AWaRe {omsaware2022} para a dose e para a "
          "repetição intra-operatória; se o HCN tiver um protocolo escrito em "
          "vigor em 2026, a adequação será avaliada também face a esse "
          "protocolo, e as duas classificações serão apresentadas lado a "
          "lado."),
    ]),
    ("Métodos de avaliação do uso de antibióticos profilácticos", [
        P("O uso de antibióticos nos hospitais pode ser medido por "
          "inquéritos de prevalência num dia, por auditorias retrospectivas "
          "de processos ou por coortes prospectivas. O inquérito de "
          "prevalência da OMS regista a indicação, o antibiótico, a dose e a "
          "duração da profilaxia cirúrgica num corte transversal "
          "{omspps2019}, mas não capta o curso completo da profilaxia de "
          "cada doente. A auditoria retrospectiva permite reconstituir todo "
          "o episódio, da decisão cirúrgica à alta, e depende da qualidade "
          "da documentação: num hospital da Gâmbia foram recuperados 682 dos "
          "777 processos procurados, 88% {aulakh2018}."),
        P("A exposição a antibióticos pode ser expressa em DDD, a dose média "
          "de manutenção diária para a indicação principal no adulto, "
          "atribuída a cada substância no índice ATC/DDD {whocc2026}. No "
          "norte da Nigéria, a profilaxia das cirurgias obstétricas e "
          "ginecológicas consumiu 16,75 DDD por procedimento, e o metronidazol "
          "redundante representou um terço desse total {abubakar2018}. A "
          "classificação AWaRe permite, por sua vez, descrever a qualidade "
          "do consumo, separando os antibióticos de primeira escolha dos que "
          "exigem vigilância {omsaware2025}."),
        P("Como a classificação da adequação envolve julgamento, sobretudo "
          "na distinção entre profilaxia e tratamento, a fiabilidade deve "
          "ser medida pela concordância entre avaliadores independentes. O "
          "kappa de Cohen corrige a concordância esperada pelo acaso, e a "
          "interpretação original de Cohen é considerada demasiado "
          "permissiva para a investigação em saúde, por admitir valores tão "
          "baixos como 0,41 {mchugh2012}. O relato dos estudos com dados de "
          "rotina segue a declaração STROBE {vonelm2007} e a sua extensão "
          "para farmacoepidemiologia, RECORD-PE {langan2018}."),
        P("A auditoria de base é o primeiro passo das intervenções de "
          "gestão de antimicrobianos. Uma revisão sistemática de 20 estudos "
          "em países de rendimento baixo e médio mostrou que 80% das "
          "intervenções melhoraram a adesão às orientações de profilaxia "
          "cirúrgica, sem alteração da ILC nem da mortalidade {sefah2024}. "
          "No Gana, a formação e a devolução dos resultados de base "
          "melhoraram a escolha e a duração, mas não o momento da "
          "administração {sefah2025}; na Etiópia, um programa de melhoria da "
          "qualidade reduziu a proporção de doentes com 24 horas ou mais de "
          "profilaxia de 50,9% para 40,9% {nofal2024}; e na Tanzânia, um "
          "programa conjunto de controlo de infecção e gestão de "
          "antimicrobianos elevou a profilaxia de 2% para 98% das "
          "cesarianas {gentilotti2020}."),
    ]),
]

# ----------------------------------------------------- 7. estado da arte ----
ESTADO_ARTE = [
    P("O [[quadro:estado_arte]] sintetiza 15 estudos empíricos publicados "
      "nos últimos dez anos sobre a profilaxia antibiótica na cesariana e "
      "noutras cirurgias em países de rendimento baixo e médio, com "
      "prioridade para a África subsariana, e inclui o único estudo "
      "publicado sobre a adequação do uso de antibióticos no HCN."),
    QUADRO("estado_arte",
           "Síntese de estudos sobre a profilaxia antibiótica na cesariana e "
           "noutras cirurgias em países de rendimento baixo e médio (estado "
           "da arte)",
           ["Autor (ano)", "Local", "Desenho (n)", "Principais resultados"],
           [
               ["De Nardo et al. (2016) {denardo2016}", "Tanzânia, Dodoma",
                "Coorte prospectiva, todas as cesarianas de três meses",
                "ILC em 224 mulheres (48%); só 10 (2,1%) receberam a "
                "profilaxia antes da incisão."],
               ["Aulakh et al. (2018) {aulakh2018}", "Gâmbia",
                "Série retrospectiva (682 processos)",
                "Infecção da ferida em 13,2%; profilaxia pré-operatória em "
                "7,4%; todas as mulheres receberam várias doses no "
                "pós-operatório."],
               ["Abubakar et al. (2018) {abubakar2018}",
                "Nigéria, três hospitais terciários",
                "Prospectivo (248 cirurgias obstétricas e ginecológicas)",
                "Momento óptimo em 16,5%; profilaxia prolongada em todas "
                "(média de 8,7 dias); cobertura anaeróbia redundante em "
                "71,4%; 17,9 DDD por cesariana ou miomectomia."],
               ["Sway et al. (2020) {sway2020}", "Quénia, dois hospitais",
                "Coorte prospectiva (609)",
                "ILC de 4,0% com profilaxia antes da incisão e de 9,3% com "
                "profilaxia só pós-operatória."],
               ["Gentilotti et al. (2020) {gentilotti2020}",
                "Tanzânia, Dodoma",
                "Antes e depois de intervenção (464 e 573)",
                "Profilaxia de 2% para 98% das cesarianas; ILC de 48% para "
                "17%."],
               ["Velin et al. (2021) {velin2021}", "Ruanda rural",
                "Coorte prospectiva (930 incluídas; 795 seguidas)",
                "ILC em 5,7%; 68,4% dos isolados Gram-negativos, nenhum "
                "sensível à ampicilina; 92,1% resistentes ou intermédios à "
                "ceftriaxona."],
               ["Kakolwa et al. (2021) {kakolwa2021}",
                "Tanzânia, três hospitais públicos",
                "Inquéritos de prevalência",
                "Entre 90% e 100% das mulheres receberam antibióticos depois "
                "da cesariana, sobretudo como profilaxia."],
               ["Carshon-Marsh et al. (2022) {carshonmarsh2022}",
                "Serra Leoa, hospital regional",
                "Coorte retrospectiva (599 cesarianas)",
                "Profilaxia pré-operatória em 85%; antibióticos "
                "pós-operatórios em 85%; ILC de 7,5% nas cesarianas."],
               ["Xavier et al. (2022) {xavier2022}", "Moçambique, HCN",
                "Transversal retrospectivo (315 crianças, 464 antibióticos, "
                "pediatria)",
                "Uso de antibióticos em 97,5%; erros em 36,5% das "
                "prescrições, sobretudo de duração (74,1% dos erros) e de "
                "dose (24,4%)."],
               ["Mbuyamba et al. (2023) {mbuyamba2023}",
                "República Democrática do Congo",
                "Prospectivo (324 doentes cirúrgicos e obstétricos)",
                "Conformidade de 87,35% na indicação, 0,31% na escolha, "
                "3,65% no momento e nula na duração; conformidade global "
                "nula."],
               ["Clean Cut Investigators Group (2024) {cleancut2024}",
                "Etiópia, Madagáscar, Índia e Bolívia",
                "Coorte (8.714)",
                "Profilaxia pós-operatória em 92,9% e por 24 horas ou mais "
                "em 27,7%; sem redução da ILC (RR 1,09); mais 1,4 dias de "
                "internamento."],
               ["Kachipedzu et al. (2024) {kachipedzu2024}",
                "Malawi, Blantyre",
                "Coorte prospectiva (208 cesarianas)",
                "ILC de 9,61%; 66,35% receberam ceftriaxona pré-operatória e "
                "antibióticos pós-operatórios."],
               ["Schrama et al. (2025) {schrama2025}",
                "Tanzânia, hospital rural",
                "Inquérito de prevalência (199 internados)",
                "Nenhuma profilaxia em dose única; 67% por mais de 24 horas; "
                "90% sem justificação registada."],
               ["Sefah et al. (2025) {sefah2025}", "Gana, hospital de ensino",
                "Quase-experimental (150 e 150 processos)",
                "Melhoria da escolha (p=0,001) e da duração (p<0,001) após a "
                "intervenção; sem alteração do momento (p=0,636)."],
               ["Njoroge et al. (2025) {njoroge2025}", "Quénia, dois hospitais",
                "Programa de vigilância (1.039 cesarianas)",
                "Profilaxia pré-operatória em 100% num hospital e em 66% no "
                "outro; ILC em 7% das mulheres contactadas até 30 dias."],
           ],
           larguras=[3.3, 2.6, 3.3, 6.8],
           fonte="Elaboração própria (2026), a partir das fontes citadas."),
    P("A leitura do quadro mostra um padrão recorrente. Onde se mediu o "
      "momento, a administração antes da incisão variou entre 2,1% na "
      "Tanzânia e 85% na Serra Leoa, mas mesmo onde era frequente "
      "coexistiu com antibióticos pós-operatórios na grande maioria das "
      "mulheres; o prolongamento foi quase universal, com esquemas de "
      "vários dias, associações redundantes e cefalosporinas de terceira "
      "geração. Os estudos divergem na magnitude, em parte porque usam "
      "definições e normas de referência diferentes: alguns consideram "
      "suficiente qualquer dose antes da incisão, outros exigem o "
      "cumprimento simultâneo de todos os critérios, e poucos distinguem "
      "cesarianas electivas e de urgência ou medem a concordância entre "
      "avaliadores. As intervenções do Gana e da Tanzânia mostram que a "
      "prática muda quando se mede e se devolve a informação, embora o "
      "momento da administração pareça mais difícil de corrigir do que a "
      "escolha e a duração."),
    P("A lacuna é clara para Moçambique: o único estudo sobre a adequação "
      "de antibióticos no HCN foi feito na pediatria, e nenhum avaliou a "
      "profilaxia na cesariana. O presente estudo preenche essa lacuna com "
      "critérios explícitos, alinhados com a recomendação da OMS, com "
      "comparação entre tipos de cesariana, medição da exposição em DDD e "
      "controlo da fiabilidade da classificação."),
]
ESQUEMA_TEXTO = [
    P("A [[figura:esquema]] representa as relações que o estudo examina. "
      "As características da mulher, as características obstétricas e "
      "cirúrgicas e os factores organizacionais do serviço influenciam a "
      "decisão de administrar a profilaxia, a escolha e a dose do "
      "antibiótico, o momento da primeira administração e a manutenção de "
      "doses depois da cirurgia. O desfecho é a adequação da profilaxia em "
      "cada um dos quatro critérios e globalmente. O mês da cirurgia e a "
      "existência de um diagnóstico de infecção registado no processo são "
      "tratados como variáveis de confundimento, porque podem alterar a "
      "disponibilidade de medicamentos e a fronteira entre profilaxia e "
      "tratamento."),
]
ESQUEMA_TITULO = ("Esquema conceptual dos factores associados à adequação "
                  "da profilaxia antibiótica na cesariana")
ESQUEMA = {
    "contexto": ("Cesarianas realizadas no Hospital Central de Nampula, "
                 "1 de Janeiro a 31 de Dezembro de 2026"),
    "blocos": [
        ("Características da mulher",
         ["idade e paridade", "infecção por HIV",
          "peso ou obesidade registada",
          "alergia aos betalactâmicos documentada"]),
        ("Características obstétricas e cirúrgicas",
         ["tipo de cesariana (electiva ou de urgência)",
          "trabalho de parto e ruptura de membranas",
          "duração da cirurgia",
          "hemorragia intra-operatória"]),
        ("Factores organizacionais",
         ["categoria profissional do cirurgião",
          "turno e dia da semana",
          "protocolo institucional",
          "disponibilidade de cefazolina"]),
    ],
    "desfecho": ("Adequação da profilaxia antibiótica",
                 ["escolha do antibiótico", "dose", "momento da "
                  "administração", "duração (prolongamento)",
                  "adequação global"]),
    "moderadores": ("Variáveis de confundimento",
                    ["mês da cirurgia",
                     "diagnóstico de infecção registado"]),
}

# ----------------------------------------------------- 8. metodologia -------
METODOLOGIA = [
    ("Tipo e desenho do estudo", [
        P("Trata-se de um estudo observacional, transversal, retrospectivo, "
          "descritivo e analítico, de natureza documental e abordagem "
          "quantitativa, que audita a utilização de antibióticos com "
          "finalidade profiláctica a partir dos registos clínicos de rotina. "
          "A componente descritiva responde aos objectivos específicos 1 a 3 "
          "e a componente analítica aos objectivos 4 e 5. O desenho "
          "retrospectivo foi escolhido por três razões: permite reconstituir "
          "todo o curso da profilaxia, da decisão cirúrgica à alta, o que um "
          "inquérito de prevalência num só dia não capta {omspps2019}; não "
          "altera o comportamento dos prescritores, como aconteceria numa "
          "observação prospectiva anunciada; e é exequível com os recursos de "
          "um trabalho de licenciatura. A contrapartida é a dependência da "
          "qualidade dos registos, tratada na verificação prévia e nas "
          "análises de sensibilidade. O relato seguirá a declaração STROBE "
          "{vonelm2007} e a extensão RECORD-PE {langan2018}."),
    ]),
    ("Local e período do estudo", [
        P("O estudo realiza-se no HCN, na cidade de Nampula, hospital de "
          "nível quaternário {xavier2024}, envolvendo o Departamento de "
          "Ginecologia e Obstetrícia, o bloco operatório da maternidade, as "
          "enfermarias de puerpério, o arquivo clínico e a farmácia "
          "hospitalar. O período de referência dos dados vai de 1 de Janeiro "
          "a 31 de Dezembro de 2026, o que abrange as variações sazonais de "
          "procura e de abastecimento de medicamentos ao longo de um ano "
          "completo. A consulta dos arquivos decorre entre Março e Maio de "
          "2027, depois da aprovação ética e das autorizações "
          "institucionais; a verificação prévia do instrumento, feita em "
          "processos de 2025, decorre em Fevereiro de 2027."),
    ]),
    ("População, unidade de análise e fontes documentais", [
        P("A população-alvo são as mulheres submetidas a cesariana no HCN e a "
          "população de estudo são as cesarianas realizadas no bloco "
          "operatório da maternidade entre 1 de Janeiro e 31 de Dezembro de "
          "2026 e inscritas no livro de registo do bloco. A unidade de "
          "análise é o episódio de cesariana, definido pela intervenção "
          "cirúrgica e pelo internamento que se lhe segue até à alta. Se a "
          "mesma mulher tiver mais de uma cesariana no período, só a primeira "
          "entra no estudo, e as reintervenções (por exemplo, laparotomias "
          "por complicação) não são consideradas novos episódios."),
        P("As fontes documentais são o livro de registo do bloco operatório, "
          "que constitui a base de amostragem e fornece a data, a hora, o "
          "tipo de cesariana e a categoria do cirurgião; a ficha de "
          "anestesia, que regista as horas da indução, da incisão, do "
          "nascimento e do fim da cirurgia e os medicamentos administrados "
          "no bloco; o relatório operatório, com a indicação, a duração e a "
          "perda sanguínea; a folha de prescrição e o diário clínico; a folha "
          "de administração de medicamentos da enfermagem, que é a fonte "
          "principal das doses efectivamente dadas depois da cirurgia; e a "
          "nota de alta, com os antibióticos prescritos para casa. As fichas "
          "de existências da farmácia informam a disponibilidade mensal de "
          "cefazolina em 2026."),
    ]),
    ("Amostra e cálculo do tamanho da amostra", [
        P("O número de cesarianas realizadas no HCN em 2026 (N) e a fracção "
          "de cesarianas electivas não estão publicados e serão obtidos do "
          "livro do bloco operatório no início da recolha [confirmar junto "
          "do Departamento de Ginecologia e Obstetrícia do HCN]. O tamanho da "
          "amostra é, por isso, calculado para satisfazer ao mesmo tempo a "
          "estimativa descritiva do objectivo 3 e a comparação do objectivo "
          "4, e a sua aplicação é apresentada em cenários de N."),
        H3("Componente descritiva (objectivo específico 3)"),
        P("Para estimar a proporção de cesarianas com profilaxia globalmente "
          "adequada usa-se a fórmula para uma proporção:"),
        FORMULA("n<sub>0</sub> = Z<sup>2</sup> × p × (1 - p) / "
                "d<sup>2</sup>"),
        P("em que Z = 1,96 corresponde a um nível de confiança de 95%, p é a "
          "proporção esperada e d é a precisão absoluta. Os estudos africanos "
          "descrevem proporções muito díspares, desde uma conformidade global "
          "nula na República Democrática do Congo {mbuyamba2023} até 85% de "
          "administração pré-operatória na Serra Leoa {carshonmarsh2022}, e "
          "não há dados moçambicanos; adopta-se por isso p = 0,50, o valor "
          "que maximiza o tamanho da amostra, e d = 0,05. A substituição dá:"),
        FORMULA("n<sub>0</sub> = 1,96<sup>2</sup> × 0,50 × 0,50 / "
                "0,05<sup>2</sup> = 0,9604 / 0,0025 = 384,2, ou seja, 385 "
                "cesarianas analisáveis"),
        H3("Componente analítica (objectivo específico 4)"),
        P("Para comparar a proporção de administrações no momento adequado "
          "entre as cesarianas electivas e de urgência usa-se a fórmula para "
          "duas proporções independentes, com nível de significância de 5% "
          "(Z<sub>α/2</sub> = 1,96) e poder de 80% (Z<sub>β</sub> = 0,8416):"),
        FORMULA("n por grupo = [Z<sub>α/2</sub> × √(2 × p<sub>m</sub> × "
                "(1 - p<sub>m</sub>)) + Z<sub>β</sub> × √(p<sub>1</sub> × "
                "(1 - p<sub>1</sub>) + p<sub>2</sub> × (1 - p<sub>2</sub>))]"
                "<sup>2</sup> / (p<sub>1</sub> - p<sub>2</sub>)<sup>2</sup>"),
        P("em que p<sub>m</sub> é a média das duas proporções. Na ausência "
          "de estudos que comparem os dois tipos de cesariana, fixa-se como "
          "diferença mínima com relevância prática 15 pontos percentuais, com "
          "p<sub>1</sub> = 0,40 nas cesarianas electivas e p<sub>2</sub> = "
          "0,25 nas de urgência (p<sub>m</sub> = 0,325), valores de "
          "planeamento situados dentro do intervalo observado nos estudos do "
          "[[quadro:estado_arte]]. A substituição dá:"),
        FORMULA("n = [1,96 × √(2 × 0,325 × 0,675) + 0,8416 × √(0,40 × 0,60 "
                "+ 0,25 × 0,75)]<sup>2</sup> / 0,15<sup>2</sup> = (1,2983 + "
                "0,5503)<sup>2</sup> / 0,0225 = 151,9, ou seja, 152 por grupo"),
        H3("Amostra final, estratificação e margem para perdas"),
        P("Para cumprir as duas exigências, a amostra é estratificada pelo "
          "tipo de cesariana, com o mesmo número de cesarianas analisáveis em "
          "cada estrato: 193 electivas e 193 de urgência, 386 no total, "
          "número que satisfaz a componente descritiva (385) e ultrapassa as "
          "152 por grupo exigidas pela componente analítica. Acrescenta-se "
          "uma margem de 15% para processos não localizados ou sem os "
          "registos mínimos, superior à perda de 12% observada numa auditoria "
          "retrospectiva semelhante na Gâmbia {aulakh2018}:"),
        FORMULA("n<sub>h</sub> = 193 / (1 - 0,15) = 227,1, ou seja, 228 por "
                "estrato e 456 cesarianas seleccionadas"),
        P("Como a fracção de cesarianas electivas deverá ser inferior a "
          "metade, a afectação igual sobre-representa as electivas. As "
          "estimativas globais serão por isso ponderadas pelo inverso da "
          "fracção de amostragem de cada estrato (N<sub>h</sub>/n<sub>h</sub>), "
          "o que introduz um efeito de desenho por ponderação que, com "
          "estratos de igual dimensão, é dado por:"),
        FORMULA("deff<sub>p</sub> = n × Σ (W<sub>h</sub><sup>2</sup> / "
                "n<sub>h</sub>) = 2 × (W<sub>e</sub><sup>2</sup> + "
                "W<sub>u</sub><sup>2</sup>)"),
        P("em que W<sub>e</sub> e W<sub>u</sub> são as fracções de "
          "cesarianas electivas e de urgência em N. Com 20% a 50% de "
          "electivas, o efeito de desenho varia entre 1,36 e 1,00 e a "
          "precisão efectiva da estimativa global fica entre ±5,8 e ±5,0 "
          "pontos percentuais, o que se considera aceitável e será declarado "
          "no relatório; a correcção para população finita, aplicada na "
          "análise quando N for conhecido, melhora esta precisão. A "
          "[[tabela:cenarios]] mostra a aplicação do plano. Em cada estrato, "
          "a selecção é sistemática, com intervalo k = N<sub>h</sub>/n<sub>h"
          "</sub> (fraccionário quando necessário) e início aleatório entre 1 "
          "e k, sobre a lista ordenada pela data e hora da cirurgia, o que "
          "distribui a amostra pelos 12 meses. Quando um estrato tiver 228 "
          "cesarianas ou menos no ano, todas serão incluídas (censo do "
          "estrato) e a diferença passa para o outro estrato, para manter as "
          "456 cesarianas; se N total for igual ou inferior a 456, far-se-á o "
          "censo de todas as cesarianas."),
        TABELA("cenarios",
               "Cenários de aplicação do plano de amostragem segundo o número "
               "anual de cesarianas (N) e a fracção de cesarianas electivas",
               ["N anual", "Electivas", "N electivas / urgência",
                "Seleccionadas electivas / urgência",
                "Intervalo k electivas / urgência", "Efeito de desenho"],
               [["800", "25%", "200 / 600", "200 (censo) / 256",
                 "censo / 2,34", "1,14"],
                ["1.000", "25%", "250 / 750", "228 / 228", "1,10 / 3,29",
                 "1,25"],
                ["2.000", "20%", "400 / 1.600", "228 / 228", "1,75 / 7,02",
                 "1,36"],
                ["2.000", "25%", "500 / 1.500", "228 / 228", "2,19 / 6,58",
                 "1,25"],
                ["2.000", "40%", "800 / 1.200", "228 / 228", "3,51 / 5,26",
                 "1,04"],
                ["3.000", "25%", "750 / 2.250", "228 / 228", "3,29 / 9,87",
                 "1,25"]],
               larguras=[2.0, 2.0, 3.2, 3.6, 3.2, 2.0],
               fonte="Elaboração própria (2026).",
               nota=("Os valores de N e a fracção de electivas são cenários "
                     "de planeamento; os valores reais serão obtidos do livro "
                     "do bloco operatório. O efeito de desenho do primeiro "
                     "cenário foi calculado com 170 electivas e 218 "
                     "cesarianas de urgência analisáveis.")),
        H3("Poder para o objectivo específico 5"),
        P("O prolongamento da profilaxia por 24 horas ou mais deverá ser "
          "frequente, a julgar pelos estudos africanos "
          "{abubakar2018,schrama2025}. Nesse caso, o número de eventos que "
          "limita o modelo multivariável é o da categoria menos frequente, "
          "as cesarianas sem prolongamento. A regra de pelo menos 10 eventos "
          "por parâmetro {peduzzi1996} permite o modelo previsto, com sete "
          "parâmetros, se pelo menos 70 das 386 cesarianas analisáveis (18%) "
          "pertencerem à categoria menos frequente. Com 40 a 69 eventos, o "
          "modelo será reduzido às variáveis de maior plausibilidade (tipo de "
          "cesariana, categoria do cirurgião e turno, com quatro parâmetros); "
          "com menos de 40, a análise ficará pela comparação bivariada, e a "
          "limitação de poder será declarada."),
        H3("Dupla extracção e verificação prévia"),
        P("A dupla extracção abrange 46 processos, 10% dos 456 "
          "seleccionados, escolhidos aleatoriamente. A verificação prévia do "
          "instrumento usa 30 processos de cesarianas de Novembro e Dezembro "
          "de 2025, fora do período de estudo, para não consumir nem "
          "contaminar a amostra."),
    ]),
    ("Critérios de inclusão e de exclusão", [
        H3("Critérios de inclusão"),
        LISTA([
            "Cesariana realizada no bloco operatório da maternidade do HCN "
            "entre 1 de Janeiro e 31 de Dezembro de 2026 e inscrita no livro "
            "de registo do bloco;",
            "Processo clínico localizado no arquivo, com a ficha de anestesia "
            "ou o relatório operatório e com a folha de prescrição ou de "
            "administração de medicamentos.",
        ]),
        H3("Critérios de exclusão"),
        LISTA([
            "Antibioterapia terapêutica em curso no momento da cirurgia, por "
            "infecção diagnosticada antes dela (por exemplo, corioamnionite, "
            "pielonefrite, pneumonia ou sepse);",
            "Antibiótico sistémico iniciado nas 24 horas anteriores à decisão "
            "cirúrgica por outra indicação (por exemplo, ruptura prematura de "
            "membranas pré-termo ou profilaxia intraparto do estreptococo do "
            "grupo B), porque impede avaliar a escolha e o momento da "
            "profilaxia;",
            "Cesariana associada a outra cirurgia abdominal programada (por "
            "exemplo, miomectomia ou histerectomia planeada), com excepção da "
            "laqueação tubária;",
            "Transferência para outro hospital nas primeiras 24 horas depois "
            "da cirurgia, que impede observar a duração;",
            "Segundo episódio de cesariana da mesma mulher no período.",
        ]),
        P("As cesarianas excluídas serão contadas e descritas pelo motivo de "
          "exclusão no fluxograma de selecção, como recomenda a declaração "
          "RECORD-PE {langan2018}."),
    ]),
    ("Variáveis e definições operacionais", [
        P("O [[quadro:variaveis]] apresenta as variáveis, o seu tipo, a "
          "definição operacional com as categorias e o objectivo específico "
          "a que respondem, e o [[quadro:criterios]] define os critérios de "
          "adequação aplicados a cada cesariana. A adequação é avaliada nos "
          "quatro critérios enunciados nos objectivos, a escolha do "
          "antibiótico, a dose, o momento e a duração, precedidos da "
          "verificação de que houve administração de profilaxia: a omissão "
          "é registada à parte, impede a avaliação dos quatro critérios e "
          "torna a cesariana inadequada na classificação global. A variável "
          "dependente do "
          "objectivo 4 é a administração no momento adequado e a do objectivo "
          "5 é o prolongamento da profilaxia por 24 horas ou mais depois do "
          "fim da cirurgia."),
        QUADRO("variaveis", "Variáveis do estudo e definições operacionais",
               ["Variável", "Tipo", "Definição operacional e categorias",
                "Objectivo"],
               [
                   ["Idade", "Independente, quantitativa",
                    "Anos completos; categorias: menos de 20, 20 a 34, 35 ou "
                    "mais", "1"],
                   ["Paridade", "Independente, qualitativa",
                    "Primípara; multípara", "1"],
                   ["Proveniência e referência", "Independente, qualitativa",
                    "Cidade de Nampula, outro distrito, outra província; "
                    "referida de outra unidade sanitária (sim, não)", "1"],
                   ["Idade gestacional", "Independente, quantitativa",
                    "Semanas completas; pré-termo (menos de 37) ou termo",
                    "1"],
                   ["Infecção por HIV", "Independente, qualitativa",
                    "Positiva; negativa; desconhecida (excluída do modelo "
                    "multivariável)", "1, 5"],
                   ["Peso registado", "Independente, quantitativa",
                    "Quilogramas; peso superior a 120 kg (sim, não, sem "
                    "registo)", "1, 3"],
                   ["Alergia aos betalactâmicos", "Independente, qualitativa",
                    "Documentada no processo (sim, não)", "1, 3"],
                   ["Tipo de cesariana", "Independente, qualitativa",
                    "Electiva (programada, fora do trabalho de parto); de "
                    "urgência (decidida em trabalho de parto ou por "
                    "complicação aguda)", "1, 4, 5"],
                   ["Indicação principal", "Independente, qualitativa",
                    "Cesariana anterior, sofrimento fetal, distócia, "
                    "apresentação anómala, doença hipertensiva, hemorragia "
                    "anteparto, outra", "1"],
                   ["Ruptura de membranas antes da cirurgia",
                    "Independente, qualitativa",
                    "Sim; não; horas desde a ruptura quando registadas",
                    "1, 5"],
                   ["Duração da cirurgia", "Independente, quantitativa",
                    "Minutos entre a incisão e o encerramento da pele", "1, 3"],
                   ["Categoria do cirurgião", "Independente, qualitativa",
                    "Médico especialista em Ginecologia e Obstetrícia; médico "
                    "de clínica geral ou interno; técnico de cirurgia", "1, 5"],
                   ["Turno da cirurgia", "Independente, qualitativa",
                    "Horário normal (dias úteis, 07h30 a 15h29); fora do "
                    "horário normal (restantes horas, fins de semana e "
                    "feriados)", "1, 5"],
                   ["Hemorragia intra-operatória", "Independente, qualitativa",
                    "Hemorragia major registada pelo cirurgião ou pelo "
                    "anestesista, ou transfusão no bloco (sim, não)",
                    "1, 3, 5"],
                   ["Infecção registada até à alta", "Descritiva, qualitativa",
                    "ILC superficial, profunda ou de órgão ou espaço; "
                    "endometrite; outra; nenhuma", "1"],
                   ["Antibiótico profiláctico", "Descritiva, qualitativa",
                    "Denominação comum internacional, código ATC e grupo "
                    "AWaRe (Acesso, Vigilância, Reserva); número de "
                    "antibióticos", "2"],
                   ["Dose e via", "Descritiva, quantitativa",
                    "Gramas ou mg/kg por administração; EV, intramuscular ou "
                    "oral", "2, 3"],
                   ["Momento da primeira dose", "Descritiva, quantitativa",
                    "Minutos antes ou depois da incisão; categorias: mais de "
                    "120 min antes, 61 a 120, 31 a 60, 0 a 30, depois da "
                    "incisão e antes do nascimento, depois do nascimento, "
                    "só no pós-operatório", "2, 3, 4"],
                   ["Duração da profilaxia", "Descritiva, qualitativa",
                    "Dose única; várias doses em 24 horas; várias doses por "
                    "mais de 24 horas; horas entre a primeira e a última "
                    "dose, incluindo a prescrição na alta", "2, 3, 5"],
                   ["Exposição a antibióticos", "Descritiva, quantitativa",
                    "DDD por cesariana: soma, por substância, da quantidade "
                    "administrada dividida pela DDD do índice ATC/DDD", "2"],
                   ["Administração de profilaxia", "Dependente, qualitativa",
                    "Pelo menos uma dose antes do fim da cirurgia (sim, "
                    "não); a omissão impede avaliar os quatro critérios",
                    "3"],
                   ["Adequação por critério", "Dependente, qualitativa",
                    "Escolha, dose, momento e duração: adequada, inadequada "
                    "ou não avaliável, segundo o quadro de critérios", "3"],
                   ["Adequação global", "Dependente, qualitativa",
                    "Adequada se houve administração e se os quatro "
                    "critérios forem adequados", "3"],
                   ["Momento adequado", "Dependente, qualitativa",
                    "Primeira dose nos 60 minutos anteriores à incisão (sim, "
                    "não)", "4"],
                   ["Prolongamento da profilaxia", "Dependente, qualitativa",
                    "Doses profilácticas por 24 horas ou mais depois do fim "
                    "da cirurgia (sim, não)", "5"],
                   ["Disponibilidade de cefazolina", "Contexto, qualitativa",
                    "Existência na farmácia do HCN no mês da cirurgia (sim, "
                    "não, sem informação)", "2, 3"],
               ],
               larguras=[3.3, 2.6, 8.3, 1.8]),
        QUADRO("criterios",
               "Critérios de adequação da profilaxia antibiótica adoptados "
               "pelo estudo",
               ["Critério", "Profilaxia adequada", "Profilaxia inadequada",
                "Fonte"],
               [
                   ["Administração",
                    "Pelo menos uma dose de antibiótico antes do fim da "
                    "cirurgia, em cesariana electiva ou de urgência",
                    "Nenhum antibiótico até ao fim da cirurgia (omissão)",
                    "{smaill2014,oms2021}"],
                   ["Escolha",
                    "Cefalosporina de primeira geração (cefazolina) ou "
                    "penicilina (ampicilina) em monoterapia; em alergia grave "
                    "documentada aos betalactâmicos, clindamicina com "
                    "gentamicina",
                    "Cefalosporina de terceira geração, associação com "
                    "metronidazol ou outro antibiótico, ou outra classe; a "
                    "cefuroxima é registada à parte como alternativa "
                    "aceitável", "{oms2021,sanchezramos2026}"],
                   ["Dose",
                    "Cefazolina 2 g EV, ou 3 g se o peso registado for "
                    "superior a 120 kg; gentamicina 5 mg/kg; ampicilina e "
                    "clindamicina na dose do protocolo do HCN ou, na sua "
                    "falta, na dose fixada pelo painel de peritos antes da "
                    "recolha",
                    "Dose inferior ou superior à de referência, ou via "
                    "diferente da EV", "{omsaware2022}"],
                   ["Momento",
                    "Primeira dose nos 60 minutos anteriores à incisão; "
                    "análises de sensibilidade com as janelas de 30 a 60 "
                    "minutos e de até 120 minutos",
                    "Mais de 60 minutos antes da incisão, depois da incisão "
                    "(antes ou depois da laqueação do cordão) ou só no "
                    "pós-operatório", "{oms2021,oms2018,sanchezramos2026}"],
                   ["Duração",
                    "Dose única; segunda dose intra-operatória aceite se a "
                    "cirurgia se prolongar mais de quatro horas depois da "
                    "primeira dose ou se houver hemorragia major registada",
                    "Qualquer dose depois do fim da cirurgia sem diagnóstico "
                    "de infecção registado (várias doses em 24 horas ou por "
                    "mais de 24 horas)", "{omsaware2022,omspps2019}"],
                   ["Adequação global",
                    "Todos os critérios anteriores adequados",
                    "Pelo menos um critério inadequado", "{mbuyamba2023}"],
               ],
               larguras=[2.3, 5.3, 5.3, 3.1],
               fonte="Elaboração própria (2026), a partir das fontes citadas.",
               nota=("Um critério é não avaliável quando falta a informação "
                     "necessária; a cesariana só entra na adequação global "
                     "se todos os critérios forem avaliáveis, com excepção "
                     "da omissão de profilaxia, que é sempre classificada "
                     "como globalmente inadequada. Se o HCN tiver "
                     "um protocolo escrito em vigor em 2026, cada critério "
                     "será também classificado face a esse protocolo.")),
    ]),
    ("Instrumento de recolha de dados e respectivas fontes", [
        P("Os dados serão registados numa ficha de extracção em papel "
          "(Apêndice A), sem nomes, números de processo nem outros "
          "identificadores, com seis secções: identificação do registo por "
          "código, características da mulher, características da cesariana, "
          "antibióticos administrados do internamento à alta, evolução até à "
          "alta e classificação da adequação. As variáveis do uso de "
          "antibióticos foram adaptadas da metodologia da OMS para inquéritos "
          "de prevalência em hospitais {omspps2019}, e os critérios de "
          "adequação decorrem da recomendação da OMS para a cesariana "
          "{oms2021} e do livro de antibióticos AWaRe {omsaware2022}. A "
          "ficha não contém escalas psicométricas; a sua fiabilidade é, por "
          "isso, avaliada pela concordância entre extractores e entre "
          "avaliadores, e não por coeficientes de consistência interna."),
        P("A validade de conteúdo será apreciada por um painel de cinco "
          "peritos (um obstetra, um anestesista, um farmacêutico hospitalar, "
          "um membro da comissão de controlo de infecção e um docente de "
          "farmacologia), que classificará a relevância e a clareza de cada "
          "item e de cada critério numa escala de quatro pontos. Será "
          "calculado o índice de validade de conteúdo de cada item e da "
          "ficha, exigindo-se pelo menos 0,80; os itens abaixo deste valor "
          "serão reformulados e reavaliados. O painel fixará também, antes da "
          "recolha, as doses de referência da ampicilina e da clindamicina, "
          "se o HCN não tiver protocolo escrito, e a lista dos diagnósticos "
          "que definem antibioterapia terapêutica."),
        P("A verificação prévia em 30 processos de 2025 medirá a "
          "percentagem de preenchimento de cada variável e o tempo de "
          "extracção. A regra de decisão é escrita antes da verificação: uma "
          "variável preenchida em menos de 60% dos processos sai dos "
          "objectivos e passa a ser apenas descrita. Se a hora de "
          "administração do antibiótico ou a hora da incisão estiverem "
          "registadas em menos de 60% dos processos, o critério do momento "
          "passa a ser avaliado apenas pela sequência dos acontecimentos "
          "(antes ou depois da incisão, antes ou depois da laqueação do "
          "cordão), e o objectivo 4 é reformulado nesses termos, com "
          "comunicação prévia ao Comité Institucional de Bioética para a "
          "Saúde da Universidade Lúrio (CIBS-UniLúrio)."),
    ]),
    ("Procedimentos de recolha de dados e controlo de qualidade", [
        P("Depois da aprovação ética e da autorização da Direcção-Geral do "
          "HCN, o investigador e um segundo extractor, estudante finalista de "
          "Farmácia, receberão um dia de formação com o manual de "
          "preenchimento e farão a calibração conjunta em dez processos de "
          "2025. A base de amostragem será construída a partir do livro do "
          "bloco operatório, copiando para uma lista numerada apenas a data, "
          "a hora, o tipo de cesariana e o número de processo; esta lista, "
          "que liga o código ao processo, ficará com o orientador, guardada à "
          "parte das fichas. As cesarianas serão seleccionadas por estrato, "
          "segundo o plano descrito, e os processos pedidos ao arquivo."),
        P("A extracção decorre numa sala do arquivo clínico, sem fotografia "
          "nem cópia de documentos. As doses administradas depois da cirurgia "
          "são retiradas da folha de administração da enfermagem; quando a "
          "prescrição e a administração divergirem, regista-se a "
          "administração e anota-se a divergência. Um processo não "
          "localizado depois de três pedidos em dias diferentes é "
          "classificado como perda e não é substituído, porque a margem de "
          "15% cobre as perdas; as características disponíveis no livro do "
          "bloco (tipo de cesariana, mês e turno) serão comparadas entre "
          "processos localizados e não localizados para avaliar o viés de "
          "selecção."),
        P("O controlo de qualidade tem quatro componentes. Primeira, a dupla "
          "extracção independente de 46 processos, com cálculo do kappa de "
          "Cohen para o antibiótico, a categoria do momento e a categoria da "
          "duração, e revisão das divergências contra a fonte. Segunda, a "
          "classificação da adequação de todas as cesarianas por dois "
          "avaliadores independentes, o investigador e um farmacêutico "
          "hospitalar, com base no [[quadro:criterios]]; o estudo exige um "
          "kappa de pelo menos 0,80 em cada critério, valor mais exigente do "
          "que a interpretação original de Cohen {mchugh2012}; se nas "
          "primeiras 50 classificações o kappa ficar abaixo desse valor, as "
          "regras serão clarificadas e os avaliadores retreinados antes de "
          "continuar. As divergências serão resolvidas por consenso e, na "
          "falta dele, por um terceiro avaliador, obstetra. Terceira, a "
          "digitação dupla das fichas no programa EpiData, com comparação "
          "automática dos dois ficheiros e correcção contra o papel. "
          "Quarta, a verificação semanal pelo orientador de uma amostra das "
          "fichas preenchidas."),
    ]),
    ("Processamento e análise dos dados", [
        P("Os dados serão analisados no Statistical Package for the Social "
          "Sciences (SPSS) Statistics, versão 26 ou "
          "superior, ou no R, com nível de significância de 5% (p<0,05) e "
          "intervalos de confiança a 95% (IC95%). O [[quadro:analise]] "
          "resume o plano por objectivo. As variáveis quantitativas serão "
          "descritas pela média e desvio-padrão ou, se a distribuição não "
          "for normal pelo teste de Shapiro-Wilk, pela mediana e intervalo "
          "interquartil (IIQ); as qualitativas, por frequências e "
          "proporções. As estimativas para o conjunto das cesarianas serão "
          "ponderadas pelo inverso da fracção de amostragem de cada estrato, "
          "com correcção para população finita, e as estimativas por estrato "
          "serão apresentadas sem ponderação."),
        P("No objectivo 2, cada antibiótico será codificado pela classificação "
          "ATC e pelo grupo AWaRe {omsaware2025}, e a exposição por cesariana "
          "será calculada somando, por substância, a quantidade total "
          "administrada dividida pela respectiva DDD do índice ATC/DDD em "
          "vigor {whocc2026}, com apresentação da mediana e do IIQ. No "
          "objectivo 3, as proporções de adequação por critério serão "
          "estimadas com IC95% pelo método de Wilson, excluindo do "
          "denominador as cesarianas em que o critério não é avaliável, que "
          "serão contadas à parte. Três análises de sensibilidade testarão a "
          "robustez dos resultados: as janelas de 30 a 60 minutos e de até "
          "120 minutos para o momento; os cenários extremos em que todas as "
          "cesarianas não avaliáveis são adequadas ou inadequadas; e, se "
          "existir, a classificação face ao protocolo do HCN."),
        P("No objectivo 4, a proporção de administrações no momento adequado "
          "será comparada entre os estratos pelo teste do qui-quadrado de "
          "Pearson, ou pelo teste exacto de Fisher quando alguma frequência "
          "esperada for inferior a 5, com a diferença de proporções e o OR "
          "acompanhados dos IC95%. No objectivo 5, a associação de cada "
          "factor com o prolongamento será primeiro avaliada pelo "
          "qui-quadrado e pelo OR bruto; depois, os seis factores "
          "pré-especificados entrarão em simultâneo num modelo de regressão "
          "logística, sem selecção automática, com estimativa do ORa e IC95%, "
          "respeitando a regra de eventos por parâmetro {peduzzi1996}. O "
          "tipo de cesariana, variável de estratificação, entra no modelo "
          "como covariável; a colinearidade será verificada pelo factor de "
          "inflação da variância (VIF), aceitando-se valores inferiores a 5, "
          "e o ajustamento pelo teste de Hosmer-Lemeshow. Quando uma variável "
          "do modelo tiver mais de 10% de valores em falta, a análise de "
          "casos completos será comparada com uma análise por imputação "
          "múltipla."),
        QUADRO("analise", "Plano de análise por objectivo específico",
               ["Objectivo", "Indicadores", "Método"],
               [["1. Caracterizar as mulheres e as cesarianas",
                 "Frequências, médias ou medianas das variáveis "
                 "sociodemográficas, obstétricas e cirúrgicas",
                 "Estatística descritiva ponderada; IC95%"],
                ["2. Descrever os esquemas e a exposição",
                 "Distribuição por substância, grupo AWaRe, dose, via, "
                 "momento e duração; DDD por cesariana",
                 "Proporções ponderadas com IC95%; mediana e IIQ das DDD"],
                ["3. Determinar a adequação",
                 "Proporção adequada em cada critério e global",
                 "Proporções ponderadas com IC95% (Wilson); análises de "
                 "sensibilidade"],
                ["4. Comparar o momento por tipo de cesariana",
                 "Proporção no momento adequado nas electivas e nas de "
                 "urgência",
                 "Qui-quadrado de Pearson ou teste exacto de Fisher; "
                 "diferença de proporções e OR com IC95%"],
                ["5. Analisar o prolongamento",
                 "Proporção com 24 horas ou mais de profilaxia segundo os "
                 "factores",
                 "OR bruto; regressão logística multivariável (ORa e IC95%); "
                 "VIF; Hosmer-Lemeshow"]],
               larguras=[4.2, 6.0, 5.8]),
    ]),
    ("Limitações do estudo e estratégias de mitigação", [
        P("O [[quadro:limitacoes]] identifica as principais limitações "
          "previsíveis, a sua consequência para os resultados e a estratégia "
          "adoptada para as reduzir."),
        QUADRO("limitacoes", "Limitações previstas e estratégias de mitigação",
               ["Limitação", "Consequência", "Mitigação"],
               [["Horas de administração ou de incisão em falta ou ilegíveis",
                 "Subestimação ou impossibilidade de avaliar o momento",
                 "Verificação prévia com regra de decisão escrita; categoria "
                 "não avaliável; cenários extremos na análise"],
                ["Doses administradas e não registadas, ou registadas e não "
                 "dadas",
                 "Erro na duração e na exposição em DDD",
                 "Folha de administração como fonte principal; registo das "
                 "divergências entre prescrição e administração"],
                ["Fronteira entre profilaxia e tratamento",
                 "Classificação errada da duração",
                 "Regra escrita e lista de diagnósticos fixada pelo painel; "
                 "dois avaliadores, kappa e terceiro avaliador"],
                ["Processos não localizados",
                 "Viés de selecção se as perdas se concentrarem num tipo de "
                 "cesariana ou num período",
                 "Margem de 15%; comparação das características no livro do "
                 "bloco entre localizados e não localizados"],
                ["Um único hospital de referência",
                 "Validade externa limitada",
                 "Descrição detalhada do contexto; comparação com os estudos "
                 "africanos"],
                ["Ausência de seguimento depois da alta",
                 "O estudo não mede o efeito clínico da profilaxia",
                 "ILC até à alta apenas descrita; limitação declarada"],
                ["Prolongamento quase universal",
                 "Poucos eventos e poder limitado no objectivo 5",
                 "Regra de eventos por parâmetro; modelo reduzido "
                 "pré-especificado; limitação declarada"],
                ["Rupturas de stock ou mudança de protocolo durante 2026",
                 "Desvios não atribuíveis à decisão clínica",
                 "Registo mensal da disponibilidade de cefazolina e da versão "
                 "do protocolo; análise por mês"]],
               larguras=[5.0, 5.0, 6.0]),
    ]),
    ("Considerações éticas", [
        P("O estudo respeita a Declaração de Helsínquia na revisão de 2024 "
          "{wma2025} e a Lei n.º 3/2023, que regula a investigação em saúde "
          "humana em Moçambique {lei3de2023}. O protocolo será submetido ao "
          "CIBS-UniLúrio e, se este o determinar, ao Comité Nacional de "
          "Bioética para a Saúde (CNBS); a recolha só começará depois da "
          "aprovação e da autorização escrita da Direcção-Geral do HCN "
          "(Apêndice C), com conhecimento da Direcção Clínica, do "
          "Departamento de Ginecologia e Obstetrícia, do arquivo clínico e "
          "da farmácia."),
        P("Será pedida a dispensa do consentimento informado (Apêndice B), "
          "porque o estudo é retrospectivo e de risco mínimo, usa apenas "
          "registos já existentes, não tem qualquer contacto com as mulheres "
          "e seria impraticável obter o consentimento de mulheres que tiveram "
          "alta há vários meses e cujos contactos não são fiáveis; os dados "
          "serão registados sem identificadores e o conhecimento produzido "
          "serve directamente a qualidade dos cuidados prestados às futuras "
          "utentes. O risco principal é a quebra de confidencialidade, e as "
          "medidas para o prevenir são as seguintes:"),
        LISTA([
            "fichas identificadas apenas por código; lista de ligação entre "
            "código e processo guardada pelo orientador, separada das fichas "
            "e destruída depois da verificação da qualidade dos dados;",
            "proibição de fotografar ou copiar documentos e assinatura de um "
            "termo de confidencialidade pelos extractores (Apêndice D);",
            "base de dados num computador protegido por palavra-passe, com "
            "cópia num disco cifrado, conservada durante cinco anos e depois "
            "destruída;",
            "registo apenas da categoria profissional do cirurgião e do "
            "prescritor, nunca do nome, e apresentação dos resultados de "
            "forma agregada e não punitiva, sem identificar profissionais, "
            "turnos individuais ou mulheres.",
        ]),
        P("O estudo não traz benefício directo às mulheres cujos processos "
          "são consultados, mas o benefício indirecto é relevante: os "
          "resultados orientarão a revisão do protocolo e a gestão de "
          "antimicrobianos na maternidade. Como via de referenciação, se "
          "durante a extracção for detectada uma situação que ainda exija "
          "acção clínica, por exemplo um resultado laboratorial relevante sem "
          "registo de actuação numa mulher ainda em seguimento, o orientador "
          "informará de forma confidencial o Director Clínico do HCN no prazo "
          "de 48 horas, sem que essa comunicação entre nos dados do estudo. "
          "Os autores declaram não ter conflitos de interesse."),
    ]),
]

# ----------------------------------------------------- 9 e 10 ---------------
RESULTADOS_ESPERADOS = [
    P("Os resultados esperados seguem a ordem dos objectivos específicos. "
      "Não se antecipam valores numéricos; indica-se a direcção provável, "
      "apoiada na literatura, e a utilidade de cada resultado para o HCN."),
    LISTA([
        "Objectivo 1: uma descrição das mulheres submetidas a cesariana e das "
        "intervenções, incluindo o peso das cesarianas de urgência e dos "
        "factores de risco infeccioso (trabalho de parto, ruptura de "
        "membranas, infecção por HIV); esta informação dimensiona as "
        "necessidades de profilaxia e o consumo esperado de cefazolina.",
        "Objectivo 2: o retrato dos esquemas usados, em que se espera "
        "encontrar, a par dos antibióticos do grupo Acesso, o uso de "
        "ceftriaxona e de associações com metronidazol, como noutros "
        "hospitais da região {abubakar2018,habteweld2023,kachipedzu2024}, e "
        "uma exposição em DDD por cesariana muito superior à de uma dose "
        "única; a medida servirá ao CHTF para quantificar o consumo evitável "
        "e planear as necessidades de aquisição.",
        "Objectivo 3: as proporções de adequação por critério, prevendo-se, "
        "pela literatura africana {denardo2016,aulakh2018,mbuyamba2023}, que "
        "a duração e o momento sejam os critérios menos cumpridos e que a "
        "adequação global seja baixa; o resultado indica ao hospital em que "
        "critério intervir primeiro.",
        "Objectivo 4: a comparação entre cesarianas electivas e de urgência, "
        "esperando-se maior adequação do momento nas electivas, em que há "
        "tempo para planear a administração; uma diferença confirmada "
        "orientará a organização da profilaxia nas urgências, definindo "
        "quem administra o antibiótico e em que ponto do circuito da mulher "
        "até ao bloco.",
        "Objectivo 5: a identificação dos factores associados ao "
        "prolongamento, esperando-se que as cesarianas de urgência, a "
        "ruptura de membranas e a infecção por HIV se associem a mais "
        "prolongamento, e que a categoria do cirurgião e o turno mostrem "
        "diferenças de prática; estes resultados orientam formação "
        "dirigida e medidas organizacionais como o registo obrigatório da "
        "data de suspensão na folha de prescrição, cuja ausência foi "
        "documentada num hospital tanzaniano {schrama2025}, ou a discussão "
        "multidisciplinar da indicação e da duração do antibiótico durante "
        "a visita clínica, que na Etiópia reduziu a profilaxia prolongada "
        "{nofal2024}.",
    ]),
    P("No conjunto, o estudo fornecerá ao HCN uma linha de base medida com "
      "critérios explícitos, que permitirá rever o protocolo institucional à "
      "luz da recomendação da OMS {oms2021} e repetir a auditoria depois de "
      "uma intervenção, para medir o seu efeito."),
]
DIVULGACAO = [
    P("Os resultados serão apresentados na defesa pública da monografia na "
      "FCS da UniLúrio e entregues, num relatório técnico com "
      "recomendações, à Direcção-Geral e à Direcção Clínica do HCN, ao "
      "Departamento de Ginecologia e Obstetrícia, ao CHTF e à comissão de "
      "controlo de infecção. Será proposta uma sessão de apresentação na "
      "reunião clínica do hospital, com discussão das medidas prioritárias, "
      "e será enviado um resumo à Direcção Provincial de Saúde de Nampula."),
    P("O estudo será submetido como artigo original a uma revista com "
      "revisão por pares, de preferência de acesso aberto, e apresentado em "
      "jornadas científicas da UniLúrio ou em congressos nacionais de "
      "saúde. Em todas as formas de divulgação os resultados serão "
      "agregados, sem identificação de mulheres, de profissionais ou de "
      "turnos concretos, e com uma leitura orientada para a melhoria e não "
      "para a responsabilização individual."),
]

# ----------------------------------------------------- 11. cronograma -------
CRONOGRAMA_TEXTO = [
    P("O [[quadro:cronograma]] distribui as actividades por 12 meses, de "
      "Outubro de 2026 a Setembro de 2027. A submissão ao CIBS-UniLúrio e "
      "os pedidos de autorização ocupam Dezembro de 2026 e Janeiro de 2027; "
      "a verificação prévia em processos de 2025 só se faz em Fevereiro de "
      "2027, depois da aprovação, e a recolha nos processos de 2026 decorre "
      "de Março a Maio de 2027, seguida da análise, da redacção e da defesa "
      "em Setembro de 2027."),
]
CRONOGRAMA = {
    "inicio": (2026, 10),
    "n_meses": 12,
    "actividades": [
        ("Revisão da literatura e redacção do protocolo", [1, 2]),
        ("Submissão ao CIBS-UniLúrio e pedidos de autorização ao HCN",
         [3, 4]),
        ("Validação da ficha pelo painel de peritos e formação dos "
         "extractores", [4, 5]),
        ("Verificação prévia em 30 processos de 2025 e ajuste da ficha", [5]),
        ("Construção da base de amostragem e selecção das cesarianas",
         [5, 6]),
        ("Recolha de dados nos processos de 2026, com dupla extracção de 10%",
         [6, 7, 8]),
        ("Classificação independente da adequação e cálculo do kappa",
         [7, 8]),
        ("Digitação dupla, limpeza e análise dos dados", [8, 9]),
        ("Redacção da monografia", [9, 10]),
        ("Revisão pelo orientador, correcções e entrega", [11]),
        ("Defesa pública e devolução dos resultados ao HCN", [12]),
    ],
}

# ----------------------------------------------------- 12. orcamento --------
ORCAMENTO_TEXTO = [
    P("A [[tabela:orcamento]] apresenta as rubricas do estudo em meticais, "
      "com 10% de imprevistos. O estudo será financiado pelo estudante, com "
      "pedido de apoio à FCS da UniLúrio para a impressão e para a "
      "divulgação. As rubricas maiores são o subsídio de alimentação e as "
      "deslocações ao HCN durante a verificação prévia e a recolha, "
      "calculados para cerca de 50 dias de trabalho de cada um dos dois "
      "extractores, e a impressão das 532 fichas de extracção (456 da "
      "amostra, 46 de dupla extracção e 30 da verificação prévia), com "
      "quatro páginas cada. O valor da taxa de submissão ao CIBS-UniLúrio é "
      "uma estimativa [confirmar o valor em vigor junto do CIBS-UniLúrio]. "
      "Não há custos de licenças, porque a digitação usa o EpiData e a "
      "análise pode fazer-se no R, ambos gratuitos."),
]
ORCAMENTO = [
    ("Impressão das fichas de extracção (532 fichas de 4 páginas)",
     "página", 2128, 5),
    ("Impressão do manual de preenchimento e dos critérios de adequação",
     "página", 120, 5),
    ("Impressão e encadernação do protocolo e dos pedidos de autorização",
     "exemplar", 5, 400),
    ("Material de escritório (pastas, canetas, lápis, blocos, agrafador)",
     "conjunto", 1, 1500),
    ("Caixa de arquivo com fechadura para guarda das fichas", "unidade", 1,
     2500),
    ("Disco externo cifrado para cópia de segurança dos dados", "unidade", 1,
     2500),
    ("Deslocações ao HCN dos dois extractores", "viagem de ida e volta", 100,
     100),
    ("Subsídio de alimentação durante a verificação prévia e a recolha",
     "dia por pessoa", 100, 200),
    ("Subsídio ao segundo extractor e avaliador independente", "mês", 3,
     3000),
    ("Reunião do painel de peritos para validação da ficha", "sessão", 1,
     2000),
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
        NOTA("Instruções: preencher a partir do livro do bloco operatório, da "
             "ficha de anestesia, do relatório operatório, da folha de "
             "prescrição, da folha de administração de medicamentos da "
             "enfermagem e da nota de alta. Não registar nomes, números de "
             "processo nem outros identificadores; usar apenas o código "
             "atribuído na lista de selecção. Registar as horas no formato de "
             "24 horas (hh:mm). Quando a informação não existir, escrever "
             "«sem registo» (código 99). Não fotografar nem copiar "
             "documentos."),
        H3("Secção I. Identificação do registo"),
        CAMPO("Código da cesariana: __________   Estrato: (   ) Electiva   "
              "(   ) Urgência   Mês da cirurgia: ______"),
        CAMPO("Extractor: (   ) 1   (   ) 2   Dupla extracção: (   ) Sim   "
              "(   ) Não   Data da extracção: ___/___/2027"),
        PERG("Registos disponíveis no processo (assinalar todos):",
             ["Ficha de anestesia", "Relatório operatório",
              "Folha de prescrição", "Folha de administração de "
              "medicamentos", "Nota de alta"]),
        PERG("Critérios de exclusão presentes (se algum for assinalado, "
             "parar e registar o motivo):",
             ["Nenhum", "Antibioterapia terapêutica por infecção prévia à "
              "cirurgia", "Antibiótico iniciado nas 24 horas anteriores por "
              "outra indicação", "Outra cirurgia abdominal programada",
              "Transferência nas primeiras 24 horas",
              "Segundo episódio da mesma mulher"]),
        H3("Secção II. Características da mulher"),
        PERG("Idade (anos completos):"),
        PERG("Número de partos, incluindo o actual:"),
        PERG("Proveniência:", ["Cidade de Nampula", "Outro distrito da "
                               "província", "Outra província", "Sem registo"]),
        PERG("Referida de outra unidade sanitária:",
             ["Sim", "Não", "Sem registo"]),
        PERG("Idade gestacional (semanas completas):"),
        PERG("Estado serológico para o HIV:",
             ["Positivo", "Negativo", "Desconhecido ou sem registo"]),
        PERG("Peso registado (kg):"),
        PERG("Alergia aos betalactâmicos documentada:",
             ["Não", "Sim (descrever a reacção): ______________",
              "Sem registo"]),
        H3("Secção III. Características da cesariana"),
        PERG("Tipo de cesariana:",
             ["Electiva (programada, fora do trabalho de parto)",
              "De urgência"]),
        PERG("Indicação principal:",
             ["Cesariana anterior", "Sofrimento fetal",
              "Distócia ou trabalho de parto estacionário",
              "Apresentação anómala", "Doença hipertensiva da gravidez",
              "Hemorragia anteparto", "Outra: ______________"]),
        PERG("Trabalho de parto antes da cirurgia:",
             ["Sim", "Não", "Sem registo"]),
        PERG("Ruptura de membranas antes da cirurgia:",
             ["Sim, há ____ horas", "Não", "Sem registo"]),
        CAMPO("Data da cirurgia: ___/___/2026   Hora de entrada no bloco: "
              "___:___   Hora da incisão da pele: ___:___"),
        CAMPO("Hora do nascimento: ___:___   Hora do encerramento da pele: "
              "___:___   Duração (min): ______"),
        PERG("Turno da cirurgia (a partir da data e da hora da incisão):",
             ["Horário normal (dias úteis, 07h30 a 15h29)",
              "Fora do horário normal (restantes horas, fins de semana e "
              "feriados)"]),
        PERG("Técnica anestésica:",
             ["Raquianestesia", "Anestesia geral", "Outra", "Sem registo"]),
        PERG("Categoria profissional do cirurgião principal:",
             ["Médico especialista em Ginecologia e Obstetrícia",
              "Médico de clínica geral ou interno", "Técnico de cirurgia",
              "Sem registo"]),
        PERG("Perda sanguínea e hemorragia:",
             ["Perda estimada: ______ mL", "Hemorragia major registada ou "
              "transfusão no bloco", "Sem registo"]),
        PERG("Procedimento associado:",
             ["Nenhum", "Laqueação tubária", "Outro: ______________"]),
        H3("Secção IV. Antibióticos administrados, do internamento à alta"),
        NOTA("Registar cada administração numa linha. Via: endovenosa, "
             "intramuscular ou oral. Momento em relação à incisão: A = mais "
             "de 120 min antes; B = 61 a 120 min antes; C = 31 a 60 min "
             "antes; D = 0 a 30 min antes; E = depois da incisão e antes do "
             "nascimento; F = depois do nascimento, ainda no bloco; G = "
             "depois do fim da cirurgia; 99 = sem registo de hora. Fonte: 1 "
             "= ficha de anestesia; 2 = folha de administração; 3 = folha de "
             "prescrição; 4 = nota de alta."),
        TABELA(None, "Registo das administrações de antibióticos",
               ["N.º", "Antibiótico (denominação comum)", "Dose", "Via",
                "Data", "Hora", "Momento", "Fonte"],
               [[str(i), "", "", "", "", "", "", ""] for i in range(1, 11)],
               larguras=[1.0, 4.4, 1.8, 1.8, 1.9, 1.5, 1.8, 1.8]),
        PERG("Antibiótico prescrito na alta:",
             ["Não", "Sim: substância ________ dose ________ dias ____"]),
        PERG("Diagnóstico de infecção registado depois da cirurgia e antes de "
             "alguma dose:",
             ["Não", "Sim: diagnóstico ____________ data ___/___ hora "
              "___:___"]),
        PERG("Cefazolina disponível na farmácia do HCN no mês da cirurgia "
             "(ficha de existências):", ["Sim", "Não", "Sem informação"]),
        H3("Secção V. Evolução até à alta"),
        PERG("Infecção registada até à alta:",
             ["Nenhuma", "Infecção superficial da ferida",
              "Infecção profunda ou de órgão ou espaço", "Endometrite",
              "Outra: ______________"]),
        CAMPO("Data da alta: ___/___/2026   Dias de internamento depois da "
              "cirurgia: ______"),
        H3("Secção VI. Classificação da adequação (cada avaliador preenche "
           "de forma independente)"),
        TABELA(None, "Classificação da adequação",
               ["Critério", "Adequado", "Inadequado", "Não avaliável",
                "Observação"],
               [["Administração", "(   )", "(   )", "(   )", ""],
                ["Escolha", "(   )", "(   )", "(   )", ""],
                ["Dose", "(   )", "(   )", "(   )", ""],
                ["Momento (0 a 60 min)", "(   )", "(   )", "(   )", ""],
                ["Momento (30 a 60 min)", "(   )", "(   )", "(   )", ""],
                ["Momento (até 120 min)", "(   )", "(   )", "(   )", ""],
                ["Duração", "(   )", "(   )", "(   )", ""],
                ["Adequação global", "(   )", "(   )", "(   )", ""],
                ["Adequação face ao protocolo do HCN", "(   )", "(   )",
                 "(   )", ""]],
               larguras=[5.0, 2.0, 2.2, 2.4, 4.4]),
        CAMPO("Duração da profilaxia: (   ) dose única   (   ) várias doses "
              "em 24 horas   (   ) várias doses por mais de 24 horas"),
        CAMPO("Horas entre a primeira e a última dose profiláctica: ______   "
              "Avaliador: (   ) 1   (   ) 2   (   ) 3"),
        CAMPO("Assinatura do avaliador: ______________________________"),
    ]),
    ("Pedido de dispensa do consentimento informado", [
        P("Ao Comité Institucional de Bioética para a Saúde da Universidade "
          "Lúrio (CIBS-UniLúrio), Nampula."),
        P("Assunto: pedido de dispensa do consentimento informado no estudo "
          "«Adequação da profilaxia antibiótica nas cesarianas realizadas no "
          "Hospital Central de Nampula, de Janeiro a Dezembro de 2026»."),
        P("O(A) estudante abaixo assinado(a), do curso de Licenciatura em "
          "Farmácia da Faculdade de Ciências de Saúde, vem pedir a dispensa "
          "do consentimento informado das mulheres cujos processos clínicos "
          "serão consultados, com os seguintes fundamentos: o estudo é "
          "retrospectivo e documental, usa apenas registos clínicos e "
          "administrativos já existentes e não envolve qualquer contacto, "
          "intervenção ou colheita de material; as mulheres tiveram alta há "
          "vários meses e os seus contactos não são fiáveis, o que tornaria "
          "impraticável obter o consentimento e introduziria um viés de "
          "selecção; o risco é mínimo e limita-se à quebra de "
          "confidencialidade, prevenida pelo registo por código, pela "
          "separação da lista de ligação, pela proibição de cópias e "
          "fotografias e pela apresentação agregada dos resultados; e o "
          "conhecimento produzido destina-se a melhorar a profilaxia "
          "antibiótica oferecida às futuras utentes do hospital."),
        P("Compromete-se a cumprir o protocolo aprovado, a comunicar ao "
          "Comité qualquer alteração e a entregar-lhe o relatório final."),
        CAMPO("Nampula, ____ de ______________ de 2026"),
        CAMPO("O(A) estudante: ______________________________   Contacto: "
              "[preencher]"),
        CAMPO("O(A) orientador(a): ______________________________"),
    ]),
    ("Pedido de autorização institucional", [
        P("Ao Senhor Director-Geral do Hospital Central de Nampula."),
        P("Assunto: pedido de autorização para a realização de um estudo "
          "documental no Departamento de Ginecologia e Obstetrícia."),
        P("O(A) estudante abaixo assinado(a), do curso de Licenciatura em "
          "Farmácia da Faculdade de Ciências de Saúde da Universidade Lúrio, "
          "vem pedir autorização para realizar o estudo «Adequação da "
          "profilaxia antibiótica nas cesarianas realizadas no Hospital "
          "Central de Nampula, de Janeiro a Dezembro de 2026», sob "
          "orientação de [Nome e grau académico do(a) orientador(a)]. O "
          "estudo consiste na consulta do livro de registo do bloco "
          "operatório da maternidade, de uma amostra de 456 processos "
          "clínicos de cesarianas realizadas em 2026 e de 30 processos de "
          "2025 para teste do instrumento, incluindo as fichas de anestesia, "
          "os relatórios operatórios, as folhas de prescrição e de "
          "administração de medicamentos e as notas de alta, bem como das "
          "fichas de existências de cefazolina da farmácia hospitalar."),
        P("A recolha decorrerá entre Fevereiro e Maio de 2027, no arquivo "
          "clínico, em horário a combinar com os serviços, sem retirar "
          "documentos do hospital nem os fotografar. Os dados serão "
          "registados sem identificação das utentes nem dos profissionais, e "
          "os resultados serão devolvidos ao hospital num relatório técnico "
          "e numa sessão de apresentação. A recolha só começará depois da "
          "aprovação do CIBS-UniLúrio, cuja cópia será entregue."),
        CAMPO("Nampula, ____ de ______________ de 2026"),
        CAMPO("O(A) estudante: ______________________________   Contacto: "
              "[preencher]"),
        CAMPO("Parecer e despacho da Direcção-Geral: "
              "______________________________"),
    ]),
    ("Termo de confidencialidade dos extractores de dados", [
        P("Eu, abaixo assinado(a), participante na recolha de dados do "
          "estudo «Adequação da profilaxia antibiótica nas cesarianas "
          "realizadas no Hospital Central de Nampula, de Janeiro a Dezembro "
          "de 2026», comprometo-me a: não divulgar, por qualquer meio, "
          "informação que permita identificar as utentes ou os profissionais "
          "referidos nos processos consultados; não fotografar, copiar nem "
          "retirar documentos do arquivo; registar os dados apenas nas "
          "fichas codificadas do estudo e entregá-las ao investigador no fim "
          "de cada dia de trabalho; e comunicar ao orientador qualquer "
          "situação que possa exigir acção clínica, sem a registar nos dados "
          "do estudo."),
        CAMPO("Nome: ______________________________   Função no estudo: "
              "______________"),
        CAMPO("Assinatura: ______________________________   Data: "
              "___/___/2027"),
    ]),
]
