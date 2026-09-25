# -*- coding: utf-8 -*-
"""
Tema 14. Erros de prescricao em criancas internadas na enfermaria de Pediatria
do Hospital Central de Nampula (Farmacovigilancia e Seguranca do Medicamento).
Estudo documental retrospectivo das folhas de prescricao em papel de 2026, com
recolha nos arquivos em 2027.

Compor e validar:   python -X utf8 _motor/motor.py _conteudo/tema_14.py
Verificar fontes:   python -X utf8 _motor/refs.py verificar _conteudo/tema_14.py
"""
from blocos import (CAMPO, FORMULA, H3, LISTA, NOTA, P, PERG, QUADRO,
                    TABELA)

NUMERO = 14
SLUG = "Erros_Prescricao_Pediatria_HCN_Nampula"
TITULO = ("Erros de prescrição nas folhas de prescrição em papel das crianças "
          "internadas na enfermaria de Pediatria do Hospital Central de "
          "Nampula, de Janeiro a Dezembro de 2026")
DESENHO = ("Transversal retrospectivo, descritivo e analítico, documental "
           "(folhas de prescrição em papel, folhas de administração e "
           "processos clínicos)")

AUTOR = "[Nome do(a) estudante]"
ORIENTADOR = "[Nome e grau académico do(a) orientador(a)]"

# ---------------------------------------------------------------- resumo --
RESUMO = (
    "O erro de prescrição é a falha mais frequente do circuito do medicamento "
    "no hospital e as crianças internadas são o grupo mais exposto, porque "
    "quase todas as doses têm de ser calculadas a partir do peso e ajustadas "
    "à idade. Nas enfermarias que mantêm a prescrição manuscrita em papel, o "
    "risco cresce quando o peso não é registado, quando a letra não é legível "
    "e quando falta uma tabela de doses de consulta rápida junto da cama. As "
    "revisões mais recentes situam a proporção de prescrições pediátricas com "
    "erro entre um quinto e dois terços, com valores mais altos nos países de "
    "rendimento baixo e médio, e o único trabalho publicado no hospital em "
    "estudo encontrou erros em mais de um terço das prescrições de "
    "antibióticos em crianças, sobretudo na duração e na dose. Falta uma "
    "medição que abranja todos os medicamentos e todos os tipos de erro. O "
    "estudo determina a frequência e a natureza dos erros de prescrição nas "
    "folhas de prescrição em papel das crianças internadas na enfermaria de "
    "Pediatria do Hospital Central de Nampula entre 1 de Janeiro e 31 de "
    "Dezembro de 2026. Trata-se de um estudo transversal, retrospectivo, "
    "descritivo e analítico, de natureza documental, com consulta dos "
    "arquivos em 2027. Serão seleccionados 453 internamentos por amostragem "
    "sistemática ao longo do ano, com margem de 15% para processos não "
    "localizados, e analisadas todas as linhas de medicamento de cada folha. "
    "Uma ficha de extracção sem identificadores, validada por um painel de "
    "peritos e testada em 30 processos, registará o peso, a dose, a "
    "frequência, a via, a duração e a legibilidade. Dois avaliadores "
    "independentes classificarão cada erro e a sua gravidade potencial, com "
    "medição da concordância. A análise estimará proporções com intervalos de "
    "confiança e identificará os factores associados por regressão logística. "
    "Espera-se produzir a primeira medição moçambicana deste problema e uma "
    "tabela de doses pediátricas para a enfermaria.")
PALAVRAS_CHAVE = ["criança hospitalizada", "erros de medicação", "Moçambique",
                  "prescrição de medicamentos", "segurança do doente"]
ABSTRACT = (
    "Prescribing errors are the most frequent failure in the hospital "
    "medication process and hospitalised children are the most exposed group, "
    "because almost every dose has to be calculated from body weight and "
    "adjusted for age. In wards that still use handwritten paper prescription "
    "charts, the risk grows when weight is not recorded, when handwriting is "
    "not legible and when no quick reference dose table is available at the "
    "bedside. Recent reviews place the proportion of paediatric prescriptions "
    "with an error between one fifth and two thirds, with higher values in "
    "low and middle income countries, and the only published work from the "
    "study hospital found errors in more than one third of antibiotic "
    "prescriptions in children, mainly in duration and dose. A measurement "
    "covering all medicines and all error types is lacking. The study "
    "determines the frequency and nature of prescribing errors in the paper "
    "prescription charts of children admitted to the paediatric ward of the "
    "Central Hospital of Nampula between 1 January and 31 December 2026. It "
    "is a cross-sectional, retrospective, descriptive and analytical "
    "documentary study, with archive consultation in 2027. A total of 453 "
    "admissions will be selected by systematic sampling across the year, with "
    "a 15% allowance for records that cannot be located, and every medication "
    "order line on each chart will be analysed. A data extraction form "
    "without identifiers, validated by an expert panel and tested on 30 "
    "records, will register weight, dose, frequency, route, duration and "
    "legibility. Two independent reviewers will classify each error and its "
    "potential severity, with measurement of agreement. The analysis will "
    "estimate proportions with confidence intervals and identify associated "
    "factors by logistic regression. The study is expected to produce the "
    "first Mozambican measurement of this problem and a paediatric dose table "
    "for the ward.")
KEYWORDS = ["child, hospitalized", "medication errors", "Mozambique",
            "patient safety", "prescriptions"]

ABREVIATURAS = [
    ("ATC", "classificação Anatómica Terapêutica Química"),
    ("CIBS-UniLúrio", "Comité Institucional de Bioética para a Saúde da "
                      "Universidade Lúrio"),
    ("CNBS", "Comité Nacional de Bioética para a Saúde"),
    ("DCI", "denominação comum internacional"),
    ("FCS", "Faculdade de Ciências de Saúde"),
    ("HCN", "Hospital Central de Nampula"),
    ("HIV", "vírus da imunodeficiência humana"),
    ("IC95%", "intervalo de confiança a 95%"),
    ("IIQ", "intervalo interquartil"),
    ("IVC", "índice de validade de conteúdo"),
    ("LNME", "Lista Nacional de Medicamentos Essenciais"),
    ("MISAU", "Ministério da Saúde"),
    ("NCC MERP", "National Coordinating Council for Medication Error "
                 "Reporting and Prevention (Conselho Nacional de Coordenação "
                 "para a Notificação e Prevenção de Erros de Medicação)"),
    ("OMS", "Organização Mundial da Saúde"),
    ("OR", "odds ratio"),
    ("ORa", "odds ratio ajustado"),
    ("RECORD", "REporting of studies Conducted using Observational "
               "Routinely-collected health Data"),
    ("SPSS", "Statistical Package for the Social Sciences"),
    ("STROBE", "Strengthening the Reporting of Observational Studies in "
               "Epidemiology"),
    ("UniLúrio", "Universidade Lúrio"),
    ("VIF", "factor de inflação da variância"),
]

# ------------------------------------------------------------ referencias --
FONTES = {
    # -- magnitude global do dano medicamentoso
    "oms2017": "World Health Organization. Medication Without Harm: WHO global patient safety challenge [Internet]. Geneva: World Health Organization; 2017 [citado 2026 Set 19]. Disponível em: https://www.who.int/publications/i/item/WHO-HIS-SDS-2017.6",
    "omsbrief2024": "World Health Organization. Medication without harm: policy brief [Internet]. Geneva: World Health Organization; 2024 [citado 2026 Set 19]. Disponível em: https://www.who.int/publications/i/item/9789240062764",
    "hodkinson2020": "Hodkinson A, Tyler N, Ashcroft DM, Keers RN, Khan K, Phipps D, et al. Preventable medication harm across health care settings: a systematic review and meta-analysis. BMC Med. 2020;18(1):313. doi:10.1186/s12916-020-01774-9. PMID: 33153451.",
    # -- epidemiologia do erro em pediatria
    "gates2019": "Gates PJ, Baysari MT, Gazarian M, Raban MZ, Meyerson S, Westbrook JI. Prevalence of Medication Errors Among Paediatric Inpatients: Systematic Review and Meta-Analysis. Drug Saf. 2019;42(11):1329-1342. doi:10.1007/s40264-019-00850-1. PMID: 31290127.",
    "chen2026": "Chen X, Meng Y, Wei X, Li A, He J, Yue L. Global Prevalence and Associated Factors of Medication Errors in Hospitalized Pediatric Patients: Systematic Review and Meta-Analysis. JMIR Pediatr Parent. 2026;9:e100070. doi:10.2196/100070. PMID: 42684394.",
    "hannibal2025": "Hannibal GD, Vithanage N, Madhushika MT, Sinhabahu TK, Kankananarachchi I, Liyanage P. A systematic review of prescription errors in paediatric care. BMC Health Serv Res. 2025;25(1):967. doi:10.1186/s12913-025-13109-6. PMID: 40696335.",
    "khoo2017": "Khoo TB, Tan JW, Ng HP, Choo CM, Bt Abdul Shukor INC, Teh SH. Paediatric in-patient prescribing errors in Malaysia: a cross-sectional multicentre study. Int J Clin Pharm. 2017;39(3):551-559. doi:10.1007/s11096-017-0463-1. PMID: 28417303.",
    "satir2023": "Satir AN, Pfiffner M, Meier CR, Caduff Good A. Prescribing Patterns in Pediatric General Wards and Their Association with Prescribing Errors: A Retrospective Observational Study. Drugs Real World Outcomes. 2023;10(4):619-629. doi:10.1007/s40801-023-00392-0. PMID: 37831373.",
    "badgeryparker2024": "Badgery-Parker T, Li L, Fitzpatrick E, Mumford V, Raban MZ, Westbrook JI. Child Age and Risk of Medication Error: A Multisite Children's Hospital Study. J Pediatr. 2024;272:114087. doi:10.1016/j.jpeds.2024.114087. PMID: 38705229.",
    # -- definicoes e classificacao
    "dean2000": "Dean B, Barber N, Schachter M. What is a prescribing error?. Qual Health Care. 2000;9(4):232-7. doi:10.1136/qhc.9.4.232. PMID: 11101708.",
    "ghaleb2005": "Ghaleb MA, Barber N, Dean Franklin B, Wong IC. What constitutes a prescribing error in paediatrics?. Qual Saf Health Care. 2005;14(5):352-7. doi:10.1136/qshc.2005.013797. PMID: 16195569.",
    "nccmerp2022": "National Coordinating Council for Medication Error Reporting and Prevention. NCC MERP index for categorizing medication errors [Internet]. Rockville: National Coordinating Council for Medication Error Reporting and Prevention; 2022 [citado 2026 Set 19]. Disponível em: https://www.nccmerp.org/sites/default/files/index-bw-2022.pdf",
    # -- dose pelo peso, registo do peso e referencias de dose
    "lubsch2023": "Lubsch L, Kimler K, Passerrello N, Parman M, Dunn A, Meyers R. Patient Weight Should Be Included on All Medication Prescriptions. J Pediatr Pharmacol Ther. 2023;28(4):380-381. doi:10.5863/1551-6776-28.4.380. PMID: 37795278.",
    "wells2020": "Wells M, Goldstein L. Drug dosing errors in simulated paediatric emergencies - Comprehensive dosing guides outperform length-based tapes with precalculated drug doses. Afr J Emerg Med. 2020;10(2):74-80. doi:10.1016/j.afjem.2020.01.005. PMID: 32612912.",
    "omspocket2013": "World Health Organization. Pocket book of hospital care for children: guidelines for the management of common childhood illnesses. 2nd ed [Internet]. Geneva: World Health Organization; 2013 [citado 2026 Set 19]. Disponível em: https://www.who.int/publications/i/item/9789241548373",
    "omsemlc2025": "World Health Organization. The selection and use of essential medicines, 2025: WHO Model List of Essential Medicines for Children, 10th list [Internet]. Geneva: World Health Organization; 2025 [citado 2026 Set 19]. Disponível em: https://www.who.int/publications/i/item/B09475",
    # -- legibilidade e integralidade da prescricao manuscrita
    "weldemariam2020": "Weldemariam DG, Amaha ND, Abdu N, Tesfamariam EH. Assessment of completeness and legibility of handwritten prescriptions in six community chain pharmacies of Asmara, Eritrea: a cross-sectional study. BMC Health Serv Res. 2020;20(1):570. doi:10.1186/s12913-020-05418-9. PMID: 32571385.",
    "abdullahi2023": "Khalid Abdullahi A, Senire Fatima I, Abdurrahaman U, Isa Sa'adatu S, Bukhari Hafsat A, Abdullahi Abdulrasheed H, et al. Assessment of Legibility of Handwritten Prescriptions and Adherence to W.H.O. Prescription Writing Guidelines in Ahmadu Bello University Teaching Hospital Zaria - Kaduna State, Nigeria. Innov Pharm. 2023;14(1). doi:10.24926/iip.v14i1.5164. PMID: 38035314.",
    "alworafi2018": "Mohammed Al-Worafi Y, Patel RP, Zaidi STR, Mohammed Alseragi W, Saeed Almutairi M, Saleh Alkhoshaiban A, et al. Completeness and Legibility of Handwritten Prescriptions in Sana'a, Yemen. Med Princ Pract. 2018;27(3):290-292. doi:10.1159/000487307. PMID: 29402821.",
    "raza2016": "Raza UA, Latif S, Naseer A, Saad M, Zeeshan MF, Qazi U. Introducing a structured prescription form improves the quality of handwritten prescriptions in limited resource setting of developing countries. J Eval Clin Pract. 2016;22(5):714-20. doi:10.1111/jep.12522. PMID: 26991112.",
    "migowa2018": "Migowa AN, Macharia WM, Samia P, Tole J, Keter AK. Effect of a voice recognition system on pediatric outpatient medication errors at a tertiary healthcare facility in Kenya. Ther Adv Drug Saf. 2018;9(9):499-508. doi:10.1177/2042098618781520. PMID: 30181858.",
    # -- evidencia africana e de paises de rendimento baixo e medio
    "fekadu2019": "Fekadu G, Abdisa E, Fanta K. Medication prescribing errors among hospitalized pediatric patients at Nekemte Referral Hospital, western Ethiopia: cross-sectional study. BMC Res Notes. 2019;12(1):421. doi:10.1186/s13104-019-4455-1. PMID: 31311587.",
    "moges2026": "Moges TA, Dagnew FN, Tarekegn GY, Wondm SA, Zewdu WS, Anberbr SS, et al. Clinical Factors Associated With Patterns of Medication Errors Among Pediatric Hospitalized Patients in Northwest Ethiopia: A Multicenter Prospective Observational Study. Biomed Res Int. 2026;2026(1):e8893135. doi:10.1155/bmri/8893135. PMID: 42175692.",
    "gokhul2016": "Gokhul A, Jeena PM, Gray A. Iatrogenic medication errors in a paediatric intensive care unit in Durban, South Africa. S Afr Med J. 2016;106(12):1222-1229. doi:10.7196/SAMJ.2016.v106.i12.10940. PMID: 27917768.",
    "baolenwo2025": "Baolenwo AB, Efua SV, Vida A. Prevalence and types of medication errors among children under five (5) years in 3 primary health care facilities in the Western region of Ghana: a retrospective quantitative study. BMC Prim Care. 2025;26(1):369. doi:10.1186/s12875-025-03072-w. PMID: 41249965.",
    "baraki2018": "Baraki Z, Abay M, Tsegay L, Gerensea H, Kebede A, Teklay H. Medication administration error and contributing factors among pediatric inpatient in public hospitals of Tigray, northern Ethiopia. BMC Pediatr. 2018;18(1):321. doi:10.1186/s12887-018-1294-5. PMID: 30305080.",
    "birarra2017": "Birarra MK, Heye TB, Shibeshi W. Assessment of drug-related problems in pediatric ward of Zewditu Memorial Referral Hospital, Addis Ababa, Ethiopia. Int J Clin Pharm. 2017;39(5):1039-1046. doi:10.1007/s11096-017-0504-9. PMID: 28689305.",
    "kassaw2026": "Kassaw AT, Tarekegn GY, Zerihun TE, Bekalu AF, Wondm SA, Moges TA, et al. The magnitude of drug-related problems, typology, and predictors among patients admitted to the pediatric intensive care unit: impact of pharmacist-led interventions in Northwest Ethiopia. Ther Adv Drug Saf. 2026;17:20420986261422800. doi:10.1177/20420986261422800. PMID: 41725626.",
    "tuti2022": "Tuti T, Aluvaala J, Malla L, Irimu G, Mbevi G, Wainaina J, et al. Evaluation of an audit and feedback intervention to reduce gentamicin prescription errors in newborn treatment (ReGENT) in neonatal inpatient care in Kenya: a controlled interrupted time series study protocol. Implement Sci. 2022;17(1):32. doi:10.1186/s13012-022-01203-w. PMID: 35578243.",
    # -- Mocambique e Nampula
    "xavier2022": "Xavier SP, Victor A, Cumaquela G, Vasco MD, Rodrigues OAS. Inappropriate use of antibiotics and its predictors in pediatric patients admitted at the Central Hospital of Nampula, Mozambique. Antimicrob Resist Infect Control. 2022;11(1):79. doi:10.1186/s13756-022-01115-w. PMID: 35655272.",
    "xavier2024": "Xavier SP, da Silva AMC, Victor A. Antibiotic prescribing patterns in pediatric patients using the WHO access, watch, reserve (AWaRe) classification at a quaternary hospital in Nampula, Mozambique. Sci Rep. 2024;14(1):22719. doi:10.1038/s41598-024-72349-4. PMID: 39349590.",
    "ferrao2025": "Salência-Ferrão J, Chissaque A, Manhique-Coutinho L, Kenga AN, Cassocera M, de Deus N. Inappropriate use of antibiotics in the management of diarrhoea in children under five years admitted with acute diarrhoea in four provinces of Mozambique 2014-2019. BMC Infect Dis. 2025;25(1):209. doi:10.1186/s12879-025-10597-z. PMID: 39939844.",
    "sambo2022": "Sambo J, Cassocera M, Chissaque A, Bauhofer AFL, Roucher C, Chilaúle J, et al. Characterizing Undernourished Children Under-Five Years Old with Diarrhoea in Mozambique: A Hospital Based Cross-Sectional Study, 2015-2019. Nutrients. 2022;14(6). doi:10.3390/nu14061164. PMID: 35334821.",
    "ferreira2020": "Ferreira FS, Pereira FDLM, Martins MDRO. Intestinal parasitic infections in children under five in the Central Hospital of Nampula, Northern Mozambique. J Infect Dev Ctries. 2020;14(5):532-539. doi:10.3855/jidc.11620. PMID: 32525841.",
    "pires2021": "das Neves Martins Pires PH, Macaringue C, Abdirazak A, Mucufo JR, Mupueleque MA, Zakus D, et al. Covid-19 pandemic impact on maternal and child health services access in Nampula, Mozambique: a mixed methods research. BMC Health Serv Res. 2021;21(1):860. doi:10.1186/s12913-021-06878-3. PMID: 34425807.",
    "ine2021": "Instituto Nacional de Estatística. IV Recenseamento Geral da População e Habitação 2017: resultados definitivos, província de Nampula [Internet]. Nampula: Instituto Nacional de Estatística; 2021 [citado 2026 Set 19]. Disponível em: http://www.sina.gov.mz/wp-content/uploads/2024/05/NAMPULA-RESUTADOS-DEFINITIVOS-DO-CENSO-2017.pdf",
    "misau2023": "Ministério da Saúde. Diploma Ministerial n.º 52/2023, de 19 de Abril: aprova a Lista Nacional de Medicamentos Essenciais. Boletim da República, I Série, n.º 75 [Internet]. Maputo: Imprensa Nacional de Moçambique; 2023 [citado 2026 Set 19]. Disponível em: https://cdn.who.int/media/docs/default-source/essential-medicines/national-essential-medicines-lists-(neml)/afro_neml/mozambique-updated-lista-nacional-de-medicamentos-essenciais-2023.pdf",
    "fnm2007": "Ministério da Saúde. Formulário Nacional de Medicamentos. 5.ª ed [Internet]. Maputo: Ministério da Saúde; 2007 [citado 2026 Set 19]. Disponível em: https://anarme.gov.mz/wp-content/uploads/2024/03/FORMULARIO-MEDICAMENTOS-2007.pdf",
    "lei3de2023": "República de Moçambique. Lei n.º 3/2023, de 8 de Junho: Lei de Investigação em Saúde Humana [Internet]. Maputo: Imprensa Nacional de Moçambique; 2023 [citado 2026 Set 19]. Disponível em: https://anarme.gov.mz/download/lei-3-2023-de-8-de-junho-lei-de-investigacao-em-saude-humana/",
    # -- metodo, estatistica, relato e etica
    "mchugh2012": "McHugh ML. Interrater reliability: the kappa statistic. Biochem Med (Zagreb). 2012;22(3):276-82. PMID: 23092060.",
    "vansmeden2019": "van Smeden M, Moons KG, de Groot JA, Collins GS, Altman DG, Eijkemans MJ, et al. Sample size for binary logistic prediction models: Beyond events per variable criteria. Stat Methods Med Res. 2019;28(8):2455-2474. doi:10.1177/0962280218784726. PMID: 29966490.",
    "vonelm2007": "von Elm E, Altman DG, Egger M, Pocock SJ, Gøtzsche PC, Vandenbroucke JP. Strengthening the Reporting of Observational Studies in Epidemiology (STROBE) statement: guidelines for reporting observational studies. BMJ. 2007;335(7624):806-8. doi:10.1136/bmj.39335.541782.AD. PMID: 17947786.",
    "benchimol2015": "Benchimol EI, Smeeth L, Guttmann A, Harron K, Moher D, Petersen I, et al. The REporting of studies Conducted using Observational Routinely-collected health Data (RECORD) statement. PLoS Med. 2015;12(10):e1001885. doi:10.1371/journal.pmed.1001885. PMID: 26440803.",
    "wma2025": "World Medical Association. World Medical Association Declaration of Helsinki: Ethical Principles for Medical Research Involving Human Participants. JAMA. 2025;333(1):71-74. doi:10.1001/jama.2024.21972. PMID: 39425955.",
}

SEMINAIS = {
    "dean2000": ("Definição de erro de prescrição obtida por consenso de "
                 "peritos, adoptada de forma generalizada nos estudos de "
                 "prevalência e usada como definição operacional deste "
                 "estudo; não foi substituída por nenhuma definição "
                 "posterior."),
    "ghaleb2005": ("Adaptação pediátrica, pela mesma técnica de consenso, da "
                   "definição anterior, com a lista de cenários que contam e "
                   "não contam como erro em crianças; é a referência "
                   "metodológica dos estudos de erros de prescrição em "
                   "pediatria."),
    "omspocket2013": ("Manual de bolso da Organização Mundial da Saúde para "
                      "os cuidados hospitalares à criança no primeiro nível "
                      "de referência, com as tabelas de dose por peso "
                      "utilizadas nas enfermarias de pediatria dos países de "
                      "rendimento baixo; continua a ser a edição em vigor."),
    "fnm2007": ("Formulário Nacional de Medicamentos de Moçambique, "
                "disponível publicamente no sítio da autoridade reguladora e "
                "fonte primária das doses de referência no país; a edição em "
                "uso no hospital será confirmada antes da recolha."),
    "mchugh2012": ("Artigo metodológico de referência sobre a interpretação "
                   "do kappa de Cohen em investigação em saúde, usado para "
                   "fixar o limiar de concordância entre avaliadores."),
    "vonelm2007": ("Declaração original do STROBE, norma de relato dos "
                   "estudos observacionais que a extensão RECORD "
                   "complementa."),
    "benchimol2015": ("Declaração RECORD, norma de relato dos estudos que "
                      "usam dados recolhidos por rotina, aplicável à "
                      "auditoria de registos clínicos deste protocolo."),
}

# ----------------------------------------------------- 1. introducao --------
INTRODUCAO = [
    P("O dano causado por medicamentos é hoje reconhecido como o maior "
      "problema evitável de segurança do doente. A Organização Mundial da "
      "Saúde (OMS) lançou em 2017 o terceiro desafio global de segurança do "
      "doente, dedicado ao medicamento, com a meta de reduzir em 50%, em "
      "cinco anos, o dano grave e evitável relacionado com medicamentos "
      "{oms2017}, e o documento de orientação política que actualizou o "
      "desafio estima que os medicamentos e as opções terapêuticas expliquem "
      "quase metade de todo o dano evitável nos cuidados de saúde "
      "{omsbrief2024}. A meta-análise mais ampla sobre o tema, com estudos de "
      "todos os níveis de cuidados, concluiu que cerca de um em cada trinta "
      "doentes sofre dano medicamentoso evitável, que mais de um quarto desse "
      "dano é clinicamente grave ou põe a vida em risco e que a fase da "
      "prescrição é responsável pela maior proporção de dano evitável, 58%, "
      "seguida da monitorização {hodkinson2020}. A prescrição é, por isso, o "
      "ponto do circuito do medicamento onde a correcção rende mais."),
    P("As crianças internadas são o grupo mais exposto. Uma revisão "
      "sistemática de 71 estudos em serviços pediátricos mostrou que os erros "
      "de medicação são frequentes, que as unidades de cuidados intensivos e "
      "os serviços de urgência apresentam as taxas mais altas e que as "
      "enfermarias que usam folhas de prescrição em papel registam mais erros "
      "do que as que usam prescrição electrónica {gates2019}. A meta-análise "
      "mais recente, com 61 estudos de 29 países, estimou uma taxa agregada "
      "de erros de prescrição de 28%, que sobe para 44% nos países de "
      "rendimento médio-baixo e para 30% quando se consideram apenas as "
      "prescrições de antibióticos, e calculou que 54% das crianças "
      "internadas sofrem pelo menos um erro de medicação {chen2026}. Uma "
      "revisão dedicada especificamente à prescrição pediátrica encontrou "
      "prevalências entre 22% e 70%, identificou o erro de dose como o tipo "
      "mais frequente nas enfermarias e nas urgências e apontou os "
      "antibióticos como a classe mais envolvida {hannibal2025}."),
    P("A razão desta vulnerabilidade é conhecida. Ao contrário do adulto, "
      "para quem existem doses fixas, quase todos os medicamentos da criança "
      "são prescritos em miligramas por quilograma e por dia, o que obriga a "
      "dispor do peso actualizado, a fazer um cálculo e a converter o "
      "resultado na apresentação disponível. Cada um destes passos pode "
      "falhar, e o erro de um factor de dez é possível sem que nada no papel "
      "o assinale. A associação profissional de farmácia pediátrica recomenda "
      "por isso que o peso, em quilogramas, conste obrigatoriamente de todas "
      "as prescrições, em regime de internamento e em ambulatório, porque sem "
      "ele o farmacêutico não consegue verificar a dose {lubsch2023}. Um "
      "estudo de simulação realizado em África mostrou a dimensão do "
      "problema: sem um guia de doses, menos de 20% das prescrições de "
      "emergência pediátricas estavam correctas, proporção que subiu para 47% "
      "quando os profissionais dispunham de um guia completo de doses "
      "{wells2020}."),
    P("Os estudos africanos confirmam que o erro de dose domina. Em "
      "enfermarias pediátricas de um hospital de referência da Etiópia "
      "ocidental, o erro de dose representou 48,6% dos erros de prescrição "
      "detectados e a escolha incorrecta do medicamento 19,0%, com a doença "
      "grave, a via endovenosa e o número de medicamentos a preverem o erro "
      "{fekadu2019}. Num estudo multicêntrico prospectivo no noroeste da "
      "Etiópia, 53,6% das crianças internadas sofreram pelo menos um erro de "
      "medicação, a prescrição foi a fase mais afectada (40,2% dos erros) e "
      "os tipos predominantes foram a dose (30,3%), a frequência (15,0%) e a "
      "omissão (14,2%) {moges2026}. Numa unidade de cuidados intensivos "
      "pediátricos da África do Sul, 94,9% das crianças estiveram expostas a "
      "pelo menos um erro, 89,2% dos erros ocorreram na prescrição e 10,0% "
      "envolveram um desvio de dez vezes ou mais no cálculo da dose "
      "{gokhul2016}. Em unidades de cuidados primários do Gana, a "
      "prevalência de erros em crianças com menos de cinco anos foi de 59,3%, "
      "com 47,3% de erros de dose e 17,8% de frequência {baolenwo2025}."),
    P("Moçambique não tem, até hoje, uma medição publicada deste problema. A "
      "província de Nampula é a mais populosa do país, com 5.758.920 "
      "habitantes no recenseamento de 2017 {ine2021}, e o Hospital Central de "
      "Nampula (HCN), classificado como hospital de nível quaternário "
      "{xavier2024}, recebe as crianças que as unidades de menor nível não "
      "conseguem tratar. Os dois únicos estudos publicados sobre "
      "medicamentos na pediatria do HCN limitaram-se aos antibióticos: 97,5% "
      "das crianças internadas receberam antibióticos, 96,2% por via "
      "injectável, com uma média de 1,51 antibióticos por prescrição "
      "{xavier2024}, e 36,5% das prescrições continham erros, sobretudo de "
      "duração (74,0% dos erros) e de dose (24,4%) {xavier2022}. O padrão "
      "repete-se noutras províncias: num estudo em quatro províncias "
      "moçambicanas, 93,2% das crianças com menos de cinco anos internadas "
      "por diarreia aguda receberam antibióticos e 49,1% receberam mais do "
      "que um {ferrao2025}."),
    P("O contexto local agrava o risco. Entre as crianças moçambicanas "
      "internadas por diarreia, 28,8% estavam com peso insuficiente para a "
      "idade e 15,2% apresentavam emagrecimento {ferrao2025}, e a "
      "desnutrição altera a farmacocinética e torna o peso um dado ainda mais "
      "determinante da dose {sambo2022}. As crianças internadas no HCN "
      "apresentam, além disso, uma carga elevada de doença infecciosa, com "
      "uma prevalência de parasitas intestinais patogénicos de 31,6% nos "
      "menores de cinco anos {ferreira2020}, o que se traduz em esquemas "
      "terapêuticos com vários medicamentos em simultâneo. A prescrição "
      "continua a ser manuscrita em folhas de papel, sem verificação "
      "automática de doses e sem um farmacêutico permanente na enfermaria, e "
      "o sistema de informação em saúde da província foi descrito como "
      "carecendo de melhoria {pires2021}."),
    P("Não se conhece, portanto, quantas prescrições pediátricas do HCN "
      "contêm erros, que tipos de erro predominam, com que frequência o peso "
      "não é registado e quantas folhas são ilegíveis. Sem esta medição, a "
      "enfermaria não pode escolher onde intervir nem avaliar o efeito de "
      "qualquer medida. O presente estudo determina a frequência e a natureza "
      "dos erros de prescrição nas folhas de prescrição em papel das crianças "
      "internadas na enfermaria de Pediatria do HCN entre 1 de Janeiro e 31 "
      "de Dezembro de 2026, classifica a sua gravidade potencial, identifica "
      "os factores associados e deixa ao serviço uma tabela de doses "
      "pediátricas de consulta rápida construída a partir das referências "
      "nacionais e internacionais em vigor."),
]

# ----------------------------------------------------- 2. problema ----------
PROBLEMA = [
    P("Na enfermaria de Pediatria do HCN, a prescrição é escrita à mão numa "
      "folha de papel que acompanha o processo da criança e que serve de base "
      "à preparação e à administração pela enfermagem. Nessa folha têm de "
      "coexistir, para cada medicamento, a denominação, a dose por "
      "administração, a frequência, a via e a duração, e no cabeçalho o peso "
      "que justifica o cálculo. A ausência de qualquer destes elementos "
      "obriga quem administra a interpretar, a adivinhar ou a interromper o "
      "tratamento, e as três alternativas são prejudiciais. O problema é "
      "conhecido em contextos semelhantes: num hospital universitário da "
      "Nigéria, a via de administração estava completa em 80,8% das "
      "prescrições e a duração em 82,4%, os prescritores raramente indicavam "
      "o peso e a idade da criança e o total de erros de medicação chegou a "
      "38,0% {abdullahi2023}; em farmácias do Iémen, apenas 19 de 2.178 "
      "prescrições, ou seja 0,9%, foram consideradas de boa qualidade "
      "{alworafi2018}."),
    P("As consequências são mensuráveis e, em pediatria, desproporcionadas. "
      "Um erro de dose de dez vezes num antibiótico injectável ou num "
      "anticonvulsivante pode ser fatal numa criança de poucos quilogramas, e "
      "este tipo de desvio foi observado em 10,0% dos erros de uma unidade de "
      "cuidados intensivos pediátricos africana {gokhul2016}. Num estudo "
      "multicêntrico da Malásia, 1,7% dos erros de prescrição em crianças "
      "internadas foram considerados de consequência clínica grave e 0,1% "
      "potencialmente fatais {khoo2017}. A via endovenosa, dominante na "
      "pediatria do HCN, é ela própria um factor de risco: na meta-análise "
      "global, a administração endovenosa multiplicou por 6,86 a "
      "probabilidade de erro, o internamento com mais de cinco dias por 1,94 "
      "e a prescrição de três ou mais medicamentos por 2,12 {chen2026}. "
      "Acresce o custo indirecto do erro, que se traduz em internamentos mais "
      "longos e em consumo evitável de medicamentos num serviço com recursos "
      "limitados."),
    P("Falta saber, para esta enfermaria, qual a proporção de linhas de "
      "medicamento com erro, quais os tipos de erro que dominam, que "
      "proporção das folhas não tem o peso registado, que proporção não é "
      "legível e que características da criança, do medicamento e da "
      "organização do serviço se associam ao erro. Falta também um "
      "instrumento simples que reduza o risco no acto da prescrição. O "
      "estudo anterior feito no HCN mediu apenas os antibióticos e usou "
      "critérios restritos à duração e à dose {xavier2022}, deixando por "
      "caracterizar a frequência, a via, a omissão do peso e a legibilidade, "
      "que são precisamente as dimensões em que uma folha manuscrita falha. "
      "A definição do que conta como erro e a referência de dose a aplicar "
      "têm de ser fixadas antes da recolha, sob pena de os resultados não "
      "serem comparáveis nem defensáveis; a existência e a edição em vigor do "
      "formulário e das normas pediátricas usadas na enfermaria terão de ser "
      "confirmadas [confirmar junto da Direcção Clínica e da farmácia do "
      "HCN]."),
]
PERGUNTA = ("Qual é a frequência e a natureza dos erros de prescrição "
            "registados nas folhas de prescrição em papel das crianças "
            "internadas na enfermaria de Pediatria do Hospital Central de "
            "Nampula entre 1 de Janeiro e 31 de Dezembro de 2026, e que "
            "factores se associam à sua ocorrência?")
DELIMITACAO = [
    P("O estudo decorre na enfermaria de Pediatria do HCN, na cidade de "
      "Nampula, e abrange os internamentos de crianças com idade inferior a "
      "15 anos ocorridos entre 1 de Janeiro e 31 de Dezembro de 2026, com "
      "consulta dos arquivos entre Março e Maio de 2027. A unidade de análise "
      "principal é a linha de medicamento prescrita, isto é, cada medicamento "
      "inscrito na folha de prescrição com a sua dose, frequência, via e "
      "duração; o internamento é a unidade de análise secundária, usada para "
      "a omissão do peso, para a legibilidade e para a componente analítica. "
      "O objecto é o conteúdo escrito da prescrição, avaliado face a uma "
      "referência de dose fixada à partida, e não a decisão terapêutica na "
      "sua globalidade."),
    P("Ficam fora do estudo os erros de dispensa, de preparação e de "
      "administração, que exigiriam observação directa, os erros de "
      "monitorização e de transcrição para a folha de enfermagem, as "
      "reacções adversas a medicamentos e o dano efectivamente sofrido pela "
      "criança, que um desenho retrospectivo não permite atribuir com "
      "segurança. Ficam igualmente de fora os internamentos em cuidados "
      "intensivos pediátricos e neonatais, se existirem como unidades "
      "autónomas, as consultas externas e as urgências, e as opiniões dos "
      "prescritores sobre as causas dos erros, que poderão ser objecto de um "
      "estudo qualitativo posterior."),
]

# ----------------------------------------------------- 3. objectivos --------
OBJECTIVO_GERAL = (
    "Determinar a frequência e a natureza dos erros de prescrição registados "
    "nas folhas de prescrição em papel das crianças internadas na enfermaria "
    "de Pediatria do Hospital Central de Nampula entre 1 de Janeiro e 31 de "
    "Dezembro de 2026.")
OBJECTIVOS_ESPECIFICOS = [
    "Caracterizar as crianças internadas e os medicamentos prescritos segundo "
    "as variáveis sociodemográficas, clínicas e terapêuticas;",
    "Determinar a proporção de linhas de medicamento com pelo menos um erro "
    "de prescrição e a proporção de internamentos com pelo menos um erro, e "
    "descrever a distribuição dos erros por tipo, com destaque para a dose "
    "calculada pelo peso, a frequência, a via e a duração;",
    "Determinar a proporção de folhas de prescrição sem registo do peso da "
    "criança e avaliar a legibilidade das folhas numa escala de quatro graus;",
    "Classificar os erros detectados quanto à gravidade potencial e "
    "identificar os grupos terapêuticos e os medicamentos mais envolvidos;",
    "Analisar os factores da criança, do internamento e da organização do "
    "serviço associados à ocorrência de pelo menos um erro de prescrição "
    "durante o internamento.",
]

# ----------------------------------------------------- 4. hipoteses ---------
HIPOTESES_INTRO = [
    P("As hipóteses referem-se à componente analítica do estudo, isto é, ao "
      "objectivo específico 5, e serão testadas com um nível de significância "
      "de 5%. Os objectivos específicos 1 a 4 são descritivos e orientam-se "
      "pelas questões de investigação enunciadas a seguir."),
]
HIPOTESES = [
    ("H0 (objectivo específico 5)",
     "a idade da criança, o número de medicamentos prescritos, a presença de "
     "pelo menos um medicamento por via endovenosa, a ausência de registo do "
     "peso, a categoria profissional do prescritor, o turno da admissão e a "
     "duração do internamento não se associam de forma estatisticamente "
     "significativa à ocorrência de pelo menos um erro de prescrição."),
    ("H1 (objectivo específico 5)",
     "pelo menos um destes factores associa-se de forma estatisticamente "
     "significativa à ocorrência de pelo menos um erro de prescrição."),
    ("H0 (comparação por grupo etário)",
     "não existe diferença estatisticamente significativa na proporção de "
     "internamentos com pelo menos um erro de prescrição entre as crianças "
     "com menos de 12 meses e as crianças com 12 meses ou mais."),
    ("H1 (comparação por grupo etário)",
     "existe diferença estatisticamente significativa na proporção de "
     "internamentos com pelo menos um erro de prescrição entre as crianças "
     "com menos de 12 meses e as crianças com 12 meses ou mais."),
]
QUESTOES = [
    "Quais são as características sociodemográficas e clínicas das crianças "
    "internadas na enfermaria de Pediatria do HCN em 2026 e que medicamentos "
    "lhes foram prescritos?",
    "Que proporção das linhas de medicamento e dos internamentos apresenta "
    "pelo menos um erro de prescrição, e como se distribuem os erros por "
    "tipo?",
    "Em que proporção das folhas de prescrição falta o registo do peso e que "
    "grau de legibilidade apresentam as folhas?",
    "Qual é a gravidade potencial dos erros detectados e que grupos "
    "terapêuticos estão mais envolvidos?",
]

# ----------------------------------------------------- 5. justificativa -----
JUSTIFICATIVA_INTRO = [
    P("O erro de prescrição é, entre os problemas de segurança do doente, "
      "aquele que melhor se deixa medir com os meios de um trabalho de "
      "licenciatura e aquele cuja correcção é mais barata: uma folha de "
      "prescrição bem desenhada, o peso registado e uma tabela de doses ao "
      "alcance do prescritor custam pouco e actuam no momento exacto em que o "
      "erro nasce. O estudo justifica-se por quatro razões complementares."),
]
JUSTIFICATIVA = {
    "cientifica": [
        P("O estudo produz os primeiros dados moçambicanos sobre erros de "
          "prescrição em crianças internadas medidos com uma definição "
          "operacional explícita e com uma referência de dose declarada. A "
          "literatura disponível sobre o país limita-se aos antibióticos e a "
          "dois tipos de erro {xavier2022}, e a evidência regional, embora "
          "abundante, usa definições heterogéneas que dificultam a "
          "comparação, problema reconhecido pelas revisões sistemáticas "
          "{gates2019,hannibal2025}. Ao adoptar a definição de erro de "
          "prescrição obtida por consenso de peritos {dean2000} na sua "
          "adaptação pediátrica {ghaleb2005}, ao declarar a referência de "
          "dose e ao medir a concordância entre avaliadores, o protocolo "
          "torna os seus resultados directamente comparáveis com os de outros "
          "hospitais africanos e deixa um método replicável noutros serviços "
          "do HCN."),
    ],
    "academica": [
        P("Para a Licenciatura em Farmácia da Faculdade de Ciências de Saúde "
          "(FCS) da Universidade Lúrio (UniLúrio), o estudo exercita "
          "competências centrais do farmacêutico hospitalar: a leitura "
          "crítica de uma prescrição, o cálculo da dose pediátrica a partir "
          "do peso, o uso do formulário nacional e das normas da OMS, a "
          "classificação de erros e a avaliação da sua gravidade potencial. "
          "Dá continuidade à linha de investigação sobre medicamentos na "
          "pediatria do HCN iniciada pelo Departamento de Farmácia da própria "
          "instituição {xavier2022,xavier2024} e deixa uma ficha de "
          "extracção validada e um manual de preenchimento que podem ser "
          "reutilizados numa segunda medição, depois de uma intervenção."),
    ],
    "social": [
        P("As crianças de Nampula chegam ao HCN frequentemente desnutridas e "
          "com várias doenças em simultâneo, condição em que a margem entre a "
          "dose eficaz e a dose tóxica é estreita {ferrao2025,sambo2022}. Um "
          "erro de dose num aminoglicosídeo, num anticonvulsivante ou num "
          "anti-malárico injectável tem consequências imediatas, e num "
          "serviço africano comparável um em cada dez erros envolveu um "
          "desvio de dez vezes ou mais {gokhul2016}. Reduzir estes erros "
          "protege directamente a criança, poupa medicamentos e encurta "
          "internamentos, num contexto em que o acesso aos serviços "
          "maternos e infantis da província já se mostrou frágil {pires2021}. "
          "A tabela de doses de consulta rápida que o estudo deixa na "
          "enfermaria beneficia todas as crianças internadas depois da sua "
          "introdução, e não apenas as que integraram a amostra."),
    ],
    "politica": [
        P("O desafio global da OMS pede aos países medições de base que "
          "permitam demonstrar a redução do dano medicamentoso grave e "
          "evitável {oms2017}, e o documento de orientação política que o "
          "acompanha organiza a acção em quatro domínios, entre os quais os "
          "profissionais de saúde e os sistemas e práticas de utilização do "
          "medicamento, e em três áreas prioritárias, onde se incluem as "
          "situações de alto risco e a polimedicação {omsbrief2024}. A Lista "
          "Nacional de Medicamentos Essenciais (LNME) em vigor {misau2023} e "
          "o Formulário Nacional de Medicamentos {fnm2007} fornecem a "
          "referência normativa nacional, e a lista de medicamentos "
          "essenciais para crianças da OMS {omsemlc2025} completa-a para as "
          "apresentações pediátricas. Um diagnóstico local permite ao "
          "hospital cumprir estas orientações com medidas concretas, como a "
          "revisão do impresso de prescrição, a obrigatoriedade do registo "
          "do peso e a formação dirigida dos prescritores mais recentes."),
    ],
}

# ----------------------------------------------------- 6. revisao -----------
REVISAO = [
    ("Erro de medicação e erro de prescrição: conceitos e definição "
     "operacional", [
        P("Erro de medicação é todo o acontecimento evitável que pode causar "
          "ou levar a uma utilização inadequada do medicamento ou a dano no "
          "doente, enquanto o medicamento está sob o controlo do "
          "profissional de saúde, do doente ou do consumidor, e abrange a "
          "prescrição, a comunicação da ordem, a rotulagem, a preparação, a "
          "dispensa, a administração, a educação e a monitorização "
          "{nccmerp2022,omsbrief2024}. O erro distingue-se da reacção "
          "adversa, que decorre da acção farmacológica do medicamento "
          "correctamente utilizado, e do dano, que é a consequência "
          "eventual e não a falha em si; a maioria dos erros não chega a "
          "causar dano, mas a proporção que causa é elevada o suficiente "
          "para justificar a vigilância {hodkinson2020}."),
        P("Para o subconjunto que interessa a este estudo existe uma "
          "definição obtida por consenso de peritos: ocorre um erro de "
          "prescrição clinicamente significativo quando, em resultado de uma "
          "decisão de prescrição ou do processo de escrita da prescrição, "
          "resulta uma redução não intencional e significativa da "
          "probabilidade de o tratamento ser eficaz ou atempado, ou um "
          "aumento do risco de dano, por comparação com a prática "
          "geralmente aceite {dean2000}. O painel que a construiu aceitou "
          "como erros a falha na comunicação de informação essencial, os "
          "erros de transcrição e o uso de medicamentos, formulações ou "
          "doses inadequados ao doente concreto, e excluiu os desvios em "
          "relação a políticas ou orientações institucionais e a omissão de "
          "informação não essencial {dean2000}."),
        P("A transposição desta definição para a pediatria foi feita pela "
          "mesma técnica de consenso, com um painel de profissionais de "
          "serviços pediátricos hospitalares que classificou 40 cenários: "
          "27 foram aceites como erros de prescrição, 10 foram excluídos e "
          "três ficaram dependentes da situação clínica concreta "
          "{ghaleb2005}. O uso de medicamentos não licenciados ou fora das "
          "indicações aprovadas não foi considerado erro, decisão relevante "
          "num serviço onde a prescrição fora da indicação aprovada é "
          "inevitável. O presente estudo adopta esta definição e a lista de "
          "cenários correspondente, complementadas pelos critérios "
          "operacionais fixados no protocolo para a dose, a frequência, a "
          "via e a duração."),
        P("A gravidade do erro é uma dimensão distinta da sua frequência. O "
          "índice do National Coordinating Council for Medication Error "
          "Reporting and Prevention (NCC MERP) classifica cada erro em "
          "categorias que vão da circunstância com capacidade para causar "
          "erro, sem erro ocorrido, ao erro que contribuiu para a morte do "
          "doente, distinguindo se o erro chegou ou não ao doente e o grau "
          "de dano causado {nccmerp2022}. Este índice é o mais usado nos "
          "estudos de prescrição pediátrica e permite separar os erros "
          "triviais dos que exigem acção imediata {satir2023}."),
    ]),
    ("Magnitude e consequências dos erros de prescrição em pediatria", [
        P("A revisão sistemática que melhor controla a heterogeneidade dos "
          "métodos identificou 71 estudos de erros de medicação em crianças "
          "internadas e concluiu que as estimativas variam sobretudo com o "
          "tipo de enfermaria e com o suporte da prescrição, sendo mais "
          "altas nos cuidados intensivos e nas urgências e mais baixas nos "
          "serviços com prescrição electrónica do que nos que usam folhas em "
          "papel {gates2019}. A meta-análise mais recente, com 61 estudos de "
          "29 países, estimou a taxa agregada de erros de prescrição em 28%, "
          "a de erros de administração em 32% e a proporção de crianças "
          "internadas com pelo menos um erro em 54%; a taxa de erros de "
          "prescrição subiu para 44% nos países de rendimento médio-baixo e "
          "para 34% nos cuidados intensivos {chen2026}."),
        P("A distribuição por tipo de erro é notavelmente estável. A revisão "
          "dedicada à prescrição pediátrica encontrou o erro de dose como "
          "tipo mais frequente em cinco de nove estudos, tanto em "
          "internamento como na urgência, e as abreviaturas inadequadas como "
          "tipo dominante em ambulatório; os antibióticos foram a classe "
          "mais implicada {hannibal2025}. O estudo multicêntrico da Malásia, "
          "com 17 hospitais e 17.889 medicamentos prescritos, obteve uma "
          "taxa global de erro de prescrição de 9,2%, valor mais baixo mas "
          "obtido com uma definição estrita, e atribuiu a maioria dos erros "
          "a factores humanos, sobretudo a falta de supervisão e de "
          "conhecimento {khoo2017}."),
        P("Quanto às consequências, 1,7% dos erros do estudo malaio foram "
          "julgados de consequência clínica grave e 0,1% potencialmente "
          "fatais {khoo2017}; na meta-análise sobre dano evitável, mais de "
          "um quarto do dano medicamentoso evitável foi grave ou pôs a vida "
          "em risco {hodkinson2020}. Os factores associados ao erro "
          "convergem entre estudos: a via endovenosa (odds ratio, OR, de "
          "6,86), o internamento superior a cinco dias (OR de 1,94) e a "
          "prescrição de três ou mais medicamentos (OR de 2,12) "
          "{chen2026}. A relação com a idade é menos consensual: num estudo "
          "de dois hospitais pediátricos terciários, os erros de prescrição "
          "aumentaram de forma não linear com a idade, com pouca associação "
          "dos zero aos três anos e subida até aos dez anos {badgeryparker2024}, "
          "enquanto a evidência africana aponta os lactentes como grupo mais "
          "afectado {baraki2018,kassaw2026}. Esta divergência justifica que "
          "a idade seja tratada como variável de interesse e não como mera "
          "variável de ajustamento."),
    ]),
    ("A dose calculada pelo peso e as outras dimensões da prescrição "
     "pediátrica", [
        P("A dose pediátrica resulta de uma cadeia de operações que a "
          "prescrição do adulto não exige: obter o peso actual, multiplicar "
          "pela dose por quilograma recomendada, dividir pelo número de "
          "administrações diárias, confrontar o resultado com a dose máxima "
          "do adulto e convertê-lo no volume ou na fracção de comprimido "
          "disponível. A recomendação de que o peso em quilogramas conste "
          "obrigatoriamente de todas as prescrições existe precisamente "
          "porque sem ele nenhuma verificação posterior é possível: o "
          "farmacêutico fica reduzido a perguntar ao acompanhante ou a "
          "presumir que o cálculo foi feito com um peso correcto "
          "{lubsch2023}. Em crianças desnutridas, situação comum nos "
          "internamentos moçambicanos {ferrao2025,sambo2022}, o peso real "
          "afasta-se muito do peso esperado para a idade, e prescrever pela "
          "idade em vez do peso conduz a sobredosagem sistemática."),
        P("A referência de dose tem de ser explícita e acessível. Em "
          "Moçambique, o Formulário Nacional de Medicamentos é a fonte "
          "primária das doses e apresenta os medicamentos por capítulo "
          "terapêutico, com o nível de prescrição autorizado para cada um "
          "{fnm2007}; a LNME define os medicamentos e as apresentações "
          "disponíveis no sector público {misau2023}; e o manual de bolso da "
          "OMS para os cuidados hospitalares à criança reúne as doses por "
          "peso dos medicamentos usados nas doenças que causam a maior parte "
          "da mortalidade infantil, incluindo a pneumonia, a diarreia, a "
          "malária, a meningite e a desnutrição aguda grave {omspocket2013}. "
          "A lista de medicamentos essenciais para crianças da OMS "
          "complementa estas fontes na escolha das apresentações adequadas à "
          "idade {omsemlc2025}. A divergência entre fontes é possível, e por "
          "isso o protocolo fixa uma hierarquia de consulta antes de "
          "iniciar a recolha."),
        P("A disponibilidade de um guia de doses muda o resultado de forma "
          "mensurável. Num estudo de simulação de emergências pediátricas "
          "realizado em África, a proporção de doses correctamente "
          "prescritas ficou abaixo de 20% no grupo sem guia de doses e no "
          "grupo que usou uma fita de estimativa de peso com doses "
          "pré-calculadas, e subiu para 47% com um guia completo de doses e "
          "para 31% com uma aplicação móvel; os autores concluíram que são "
          "necessárias, em simultâneo, uma estimativa correcta do peso e uma "
          "fonte de doses completa {wells2020}. Este resultado fundamenta "
          "directamente o produto prático previsto neste protocolo."),
        P("A frequência, a via e a duração completam o conjunto. A "
          "frequência errada resulta de confusão entre a dose diária total e "
          "a dose por administração, e foi o segundo tipo de erro mais "
          "frequente em estudos etíopes e ganeses, com 15,0% e 17,8% dos "
          "erros {moges2026,baolenwo2025}. A via é crítica num serviço onde "
          "96,2% dos antibióticos são injectáveis {xavier2024}, porque a "
          "manutenção desnecessária da via endovenosa acrescenta risco "
          "infeccioso e multiplica a oportunidade de erro {chen2026}. A "
          "duração, quando não é escrita, deixa o fim do tratamento à "
          "decisão de quem estiver de turno, e foi o tipo de erro dominante "
          "no único estudo feito na pediatria do HCN, com 74,0% dos erros "
          "detectados {xavier2022}."),
    ]),
    ("Legibilidade e integralidade da prescrição manuscrita", [
        P("A prescrição manuscrita continua a ser a norma na maior parte dos "
          "hospitais africanos, e a sua qualidade é mensurável. Num estudo "
          "de 385 prescrições recolhidas em seis farmácias de Asmara, a "
          "integralidade média foi de 78,6%, com a dose presente em 83,7%, a "
          "frequência em 87,7% e a quantidade ou duração em 95,1%; a "
          "legibilidade foi classificada numa escala de quatro graus, com "
          "54,3% das prescrições no grau quatro, claramente legível, e 30,6% "
          "no grau três {weldemariam2020}. O mesmo estudo mostrou que a "
          "legibilidade diminui à medida que aumenta o número de "
          "medicamentos prescritos e o uso de nomes comerciais, dois "
          "factores que estão presentes nas enfermarias pediátricas "
          "{weldemariam2020}."),
        P("Os valores pioram em serviços hospitalares de maior volume. No "
          "hospital universitário Ahmadu Bello, na Nigéria, a prescrição por "
          "denominação comum internacional (DCI) foi de 68,4%, os detalhes "
          "do medicamento estavam completos em 85,2%, a via em 80,8% e a "
          "duração em 82,4%, a assinatura do prescritor em 84,9%, e o peso, "
          "a idade e o serviço de origem eram frequentemente omitidos; o "
          "total de erros de medicação atingiu 38,0% {abdullahi2023}. Num "
          "levantamento de 2.178 prescrições no Iémen, apenas 0,9% foram "
          "consideradas de boa qualidade e os erros de escrita relativos ao "
          "doente e aos medicamentos foram os mais comuns {alworafi2018}. "
          "Numa urgência pediátrica do Quénia, 74,3% de 1.196 prescrições "
          "manuscritas continham erros identificáveis {migowa2018}."),
        P("A boa notícia é que o suporte da prescrição é modificável sem "
          "tecnologia dispendiosa. A introdução de um impresso de prescrição "
          "estruturado num hospital de um país de recursos limitados elevou "
          "a proporção de prescrições sem problemas de legibilidade de 76,2% "
          "para 94,1%, a presença da duração do tratamento de 90,4% para "
          "99,5% e a presença da assinatura de 92,7% para 99,0% "
          "{raza2016}. A substituição da escrita manual por um sistema de "
          "reconhecimento de voz numa urgência pediátrica queniana reduziu a "
          "proporção de prescrições com erro de 74,3% para 65,7%, com o "
          "maior efeito nas doses incorrectas {migowa2018}. Um estudo que "
          "meça a legibilidade e a integralidade permite escolher entre "
          "estas opções com base em dados locais."),
    ]),
    ("Determinantes do erro e intervenções testadas em África", [
        P("Os factores associados ao erro repetem-se nos estudos africanos. "
          "Em enfermarias pediátricas da Etiópia ocidental, a doença grave "
          "(odds ratio ajustado, ORa, de 5,31), a via endovenosa (ORa de "
          "3,98), a prescrição de quatro a seis medicamentos (ORa de 3,10) e "
          "a de mais de seis medicamentos (ORa de 7,23) previram de forma "
          "independente o erro de prescrição {fekadu2019}. No noroeste do "
          "mesmo país, a polimedicação com cinco ou mais medicamentos (ORa "
          "de 2,01), o sexo masculino (ORa de 1,71) e o internamento "
          "prolongado (ORa de 1,67) associaram-se aos erros de medicação "
          "{moges2026}. Numa unidade de cuidados intensivos pediátricos "
          "etíope, 63,7% das 394 crianças tiveram pelo menos um problema "
          "relacionado com medicamentos, 97,7% considerados evitáveis, com a "
          "selecção do medicamento e a selecção da dose como causas "
          "principais, em 46,0% e 43,8% dos casos {kassaw2026}."),
        P("A organização do serviço pesa tanto como as características da "
          "criança. Na Tigray, onde se observaram 1.251 administrações, a "
          "ausência de uma sala de preparação e a ausência de um guia de "
          "administração associaram-se ao erro, tal como a idade inferior a "
          "um mês e o número de medicamentos por doente; a taxa global de "
          "erro de administração foi de 62,7%, com a dose errada a "
          "representar 53,7% dos casos {baraki2018}. Numa enfermaria "
          "pediátrica de Adis Abeba, a revisão de 1.055 ordens de "
          "medicamento em 285 crianças identificou 106 problemas em 90 "
          "doentes, uma taxa de 31,6%, com a dose demasiado baixa em 34,9% e "
          "demasiado alta em 7,5%, e o número de medicamentos prescritos "
          "(ORa de 2,3) e o número de doenças (ORa de 4,8) como factores de "
          "risco {birarra2017}."),
        P("As intervenções testadas na região são de dois tipos. As "
          "intervenções sobre o suporte da prescrição, como o impresso "
          "estruturado {raza2016} ou o sistema de reconhecimento de voz "
          "{migowa2018}, actuam no acto de escrever. As intervenções de "
          "auditoria e devolução actuam sobre o comportamento do prescritor: "
          "na rede de hospitais públicos do Quénia, um programa desenhado "
          "para reduzir os erros de prescrição da gentamicina em "
          "recém-nascidos combinou relatórios individualizados de erros, "
          "seminários conduzidos por farmacêuticos e discussão em grupos "
          "profissionais, com avaliação por séries temporais interrompidas "
          "{tuti2022}. Ambas as famílias de intervenção pressupõem uma "
          "medição de base credível, que é o que este estudo se propõe "
          "produzir."),
    ]),
    ("Enquadramento normativo e do sistema de saúde em Moçambique", [
        P("A investigação em saúde humana em Moçambique é regulada pela Lei "
          "n.º 3/2023, que fixa os princípios da protecção dos "
          "participantes, o dever de aprovação por um comité de bioética e "
          "as condições de tratamento dos dados de saúde {lei3de2023}. No "
          "plano do medicamento, a LNME aprovada em 2023 define os "
          "medicamentos e as apresentações disponíveis no sector público e "
          "passou a indicar o grupo da classificação de antibióticos da OMS "
          "para cada substância {misau2023}, e o Formulário Nacional de "
          "Medicamentos fornece as doses e as condições de utilização, com "
          "indicação do nível de prescrição autorizado para cada "
          "especialidade farmacêutica {fnm2007}. A edição do formulário em "
          "uso na enfermaria e a existência de normas pediátricas internas "
          "serão confirmadas antes da recolha, e a referência de dose "
          "aplicada será declarada no relatório final."),
        P("A evidência sobre a prática no HCN vem de dois estudos do "
          "Departamento de Farmácia da própria FCS. O primeiro, "
          "retrospectivo, analisou os antibióticos prescritos a crianças "
          "internadas e encontrou uma prevalência de uso de antibióticos de "
          "97,5%, com 464 antibióticos prescritos, e erros em 36,5% das "
          "prescrições, sobretudo de duração, com 74,0% dos erros, e de "
          "dose, com 24,4%; a prescrição de três ou mais antibióticos (OR de "
          "2,83) e o internamento curto (OR de 1,88) foram os preditores do "
          "uso inadequado {xavier2022}. O segundo descreveu o padrão de "
          "prescrição pela classificação da OMS e registou 74,8% de "
          "antibióticos do grupo Acesso, 23,7% do grupo Vigilância, uma "
          "média de 1,51 antibióticos por prescrição e 96,2% de "
          "administrações por via injectável, com todos os antibióticos "
          "prescritos por denominação genérica e constantes da lista de "
          "medicamentos essenciais {xavier2024}."),
        P("O quadro completa-se com as características das crianças "
          "internadas. Entre as crianças com menos de cinco anos internadas "
          "por diarreia aguda em quatro províncias moçambicanas, 93,2% "
          "receberam antibióticos, 49,1% receberam mais do que um, e os mais "
          "prescritos foram a ampicilina, a gentamicina e o cotrimoxazol "
          "{ferrao2025}; 28,8% estavam com peso insuficiente para a idade e "
          "15,2% apresentavam emagrecimento {ferrao2025}, e a caracterização "
          "das crianças desnutridas com diarreia no país mostra que a "
          "desnutrição se concentra nos lactentes {sambo2022}. No próprio "
          "HCN, a prevalência de parasitas intestinais patogénicos em "
          "crianças com menos de cinco anos internadas foi de 31,6% "
          "{ferreira2020}. Trata-se, portanto, de uma população em que a "
          "polimedicação por via injectável é a regra e em que o peso é "
          "simultaneamente instável e determinante da dose."),
    ]),
    ("Métodos de medição dos erros de prescrição e das suas propriedades", [
        P("Os erros de medicação podem ser medidos por notificação "
          "voluntária, por observação directa ou por revisão de registos. A "
          "notificação voluntária subestima a frequência, porque depende da "
          "disponibilidade e da confiança de quem notifica; a observação "
          "directa é o método de eleição para os erros de administração, mas "
          "altera o comportamento observado e é inviável para um ano inteiro "
          "de internamentos; a revisão de registos é o método adequado aos "
          "erros de prescrição, porque a prescrição deixa um traço escrito "
          "completo e permanente {gates2019}. A revisão sistemática que "
          "comparou estes métodos concluiu que o método de detecção afectou "
          "sobretudo as taxas de erro de administração, e não as de "
          "prescrição, o que reforça a validade da auditoria documental para "
          "o objecto deste estudo {gates2019}."),
        P("A revisão de registos tem limitações próprias que o desenho tem "
          "de antecipar. Depende da qualidade do registo, pelo que a "
          "verificação prévia da fonte num pequeno conjunto de processos, "
          "com uma regra de decisão escrita sobre o que fazer com as "
          "variáveis mal preenchidas, é uma exigência metodológica e não uma "
          "formalidade. Exige também a duplicação de uma fracção da "
          "extracção, para estimar o erro de transcrição do próprio "
          "investigador. A declaração RECORD, extensão da declaração STROBE "
          "para os estudos que usam dados recolhidos por rotina, obriga a "
          "descrever a origem dos dados, os critérios de selecção aplicados "
          "aos registos, as variáveis não disponíveis e o fluxo de registos "
          "excluídos {benchimol2015,vonelm2007}."),
        P("Como a classificação de um erro depende de julgamento, a "
          "fiabilidade tem de ser medida. O coeficiente kappa de Cohen "
          "corrige a concordância observada pela concordância esperada por "
          "acaso; a interpretação original é considerada demasiado "
          "permissiva para a investigação em saúde, por admitir como "
          "aceitáveis valores tão baixos como 0,41, pelo que se recomendam "
          "limiares mais exigentes quando a decisão tem consequências "
          "clínicas {mchugh2012}. O mesmo raciocínio aplica-se à "
          "legibilidade, que é uma avaliação subjectiva reconhecida como tal "
          "pelos próprios autores que a medem {raza2016} e que exige, por "
          "isso, dois avaliadores independentes e uma escala definida antes "
          "da recolha {weldemariam2020}."),
        P("Por último, o dimensionamento da componente analítica obedece a "
          "regras próprias. A regra tradicional de dez acontecimentos por "
          "variável na regressão logística foi mostrada como uma "
          "simplificação que pode ser insuficiente ou excessiva conforme a "
          "prevalência do desfecho e o número de candidatos a preditor, "
          "recomendando-se que o número de parâmetros seja fixado à partida "
          "e que o modelo não recorra a selecção automática de variáveis "
          "{vansmeden2019}. O protocolo segue esta orientação, fixa os "
          "preditores antes da análise e declara o limite de parâmetros "
          "compatível com o número de acontecimentos observados."),
    ]),
]

# ----------------------------------------------------- 7. estado da arte ----
ESTADO_ARTE = [
    P("O [[quadro:estado_arte]] reúne 14 estudos empíricos publicados nos "
      "últimos dez anos sobre erros de prescrição e de medicação em crianças "
      "e sobre a qualidade da prescrição manuscrita, com prioridade para a "
      "África subsariana e para os países de rendimento baixo e médio, e "
      "inclui os dois estudos disponíveis sobre a pediatria do HCN."),
    QUADRO("estado_arte",
           "Síntese de estudos sobre erros de prescrição em crianças e sobre "
           "a qualidade da prescrição manuscrita (estado da arte)",
           ["Autor (ano)", "Local", "Desenho (n)", "Principais resultados"],
           [
               ["Gokhul et al. (2016) {gokhul2016}",
                "África do Sul, Durban",
                "Prospectivo, cuidados intensivos pediátricos (117 crianças)",
                "94,9% das crianças expostas a pelo menos um erro; 89,2% dos "
                "erros na prescrição; 10,0% com desvio de dez vezes ou mais "
                "na dose."],
               ["Raza et al. (2016) {raza2016}",
                "Paquistão, hospital universitário",
                "Antes e depois de um impresso estruturado (203 prescrições "
                "em cada fase)",
                "Prescrições sem problemas de legibilidade de 76,2% para "
                "94,1%; duração presente de 90,4% para 99,5%; assinatura de "
                "92,7% para 99,0%."],
               ["Khoo et al. (2017) {khoo2017}",
                "Malásia, 17 hospitais públicos",
                "Transversal multicêntrico (17.889 medicamentos prescritos)",
                "Taxa global de erro de prescrição de 9,2%; 1,7% de "
                "consequência grave e 0,1% potencialmente fatais; causas "
                "sobretudo humanas."],
               ["Birarra et al. (2017) {birarra2017}",
                "Etiópia, Adis Abeba",
                "Transversal, enfermaria pediátrica (285 crianças, 1.055 "
                "ordens)",
                "106 problemas relacionados com medicamentos em 90 crianças "
                "(31,6%); dose baixa em 34,9% e alta em 7,5%; número de "
                "medicamentos com ORa de 2,3."],
               ["Baraki et al. (2018) {baraki2018}",
                "Etiópia, Tigray, hospitais públicos",
                "Observação directa (1.251 administrações)",
                "Erro de administração em 62,7% (IC95% 59,6-65,0); dose "
                "errada em 53,7%; ausência de guia de administração entre os "
                "factores associados."],
               ["Migowa et al. (2018) {migowa2018}",
                "Quénia, hospital terciário",
                "Antes e depois de reconhecimento de voz (1.196 e 501 "
                "prescrições)",
                "Erros em 74,3% das prescrições manuscritas e em 65,7% das "
                "geradas por voz; maior efeito na correcção das doses."],
               ["Fekadu et al. (2019) {fekadu2019}",
                "Etiópia ocidental, Nekemte",
                "Transversal, enfermarias pediátricas (384 crianças)",
                "Erro de dose em 48,6% e escolha incorrecta do medicamento "
                "em 19,0% dos erros; via endovenosa com ORa de 3,98; mais de "
                "seis medicamentos com ORa de 7,23."],
               ["Weldemariam et al. (2020) {weldemariam2020}",
                "Eritreia, Asmara",
                "Transversal (385 prescrições, 710 medicamentos)",
                "Integralidade média de 78,6%; dose presente em 83,7% e "
                "frequência em 87,7%; 54,3% das prescrições claramente "
                "legíveis."],
               ["Wells e Goldstein (2020) {wells2020}",
                "África do Sul, simulação",
                "Experimental, emergências pediátricas simuladas",
                "Menos de 20% de doses correctas sem guia de doses; 47% com "
                "guia completo e 31% com aplicação móvel."],
               ["Xavier et al. (2022) {xavier2022}",
                "Moçambique, Hospital Central de Nampula",
                "Transversal retrospectivo, pediatria (464 antibióticos)",
                "Uso de antibióticos em 97,5%; erros em 36,5% das "
                "prescrições, sobretudo de duração (74,0%) e de dose "
                "(24,4%); três ou mais antibióticos com OR de 2,83."],
               ["Abdullahi et al. (2023) {abdullahi2023}",
                "Nigéria, hospital universitário de Zaria",
                "Transversal, prescrições de internamento e ambulatório",
                "Prescrição por denominação genérica em 68,4%; via completa "
                "em 80,8% e duração em 82,4%; erros de medicação em 38,0%; "
                "peso e idade frequentemente omitidos."],
               ["Satir et al. (2023) {satir2023}",
                "Suíça, hospital pediátrico universitário",
                "Retrospectivo, enfermarias pediátricas gerais",
                "Erros potencialmente lesivos mais frequentes dos 2 aos 11 "
                "anos do que abaixo dos 2 anos (p=0,029); gravidade "
                "classificada pelo índice NCC MERP."],
               ["Badgery-Parker et al. (2024) {badgeryparker2024}",
                "Austrália, dois hospitais pediátricos",
                "Análise secundária de auditorias e observação (5.137 "
                "administrações)",
                "Erros de prescrição a aumentar de forma não linear com a "
                "idade (p=0,01), com pouca associação dos 0 aos 3 anos e "
                "subida até aos 10 anos."],
               ["Moges et al. (2026) {moges2026}",
                "Etiópia, noroeste, quatro hospitais",
                "Prospectivo multicêntrico (358 crianças, 254 erros)",
                "53,6% com pelo menos um erro; 40,2% dos erros na "
                "prescrição; dose 30,3%, frequência 15,0% e omissão 14,2%; "
                "polimedicação com ORa de 2,01."],
           ],
           larguras=[3.3, 2.7, 3.4, 6.6],
           fonte="Elaboração própria (2026), a partir das fontes citadas."),
    P("A leitura do quadro revela três padrões constantes. O primeiro é o "
      "domínio do erro de dose, que aparece como tipo mais frequente em "
      "todos os estudos que discriminam tipos, com proporções entre 30,3% e "
      "53,7% dos erros; a dose é também a dimensão que mais depende do peso "
      "e do cálculo, e portanto a mais sensível ao suporte disponível. O "
      "segundo é o efeito do suporte da prescrição: sempre que se "
      "estruturou o impresso, se introduziu um guia de doses ou se "
      "substituiu a escrita manual, a qualidade melhorou de forma "
      "estatisticamente significativa, sem recurso a tecnologia "
      "dispendiosa. O terceiro é a consistência dos factores associados, "
      "com o número de medicamentos, a via endovenosa e o internamento "
      "prolongado a repetirem-se em contextos muito diferentes."),
    P("Os estudos divergem em dois pontos, e a divergência é informativa. "
      "As estimativas de frequência variam entre 9,2% de linhas de "
      "medicamento com erro e 94,9% de crianças com pelo menos um erro, "
      "porque a unidade de análise e a definição de erro não são as mesmas; "
      "qualquer estudo novo tem de declarar ambas antes de recolher dados. E "
      "a relação com a idade opõe os achados de serviços com prescrição "
      "electrónica, onde o erro aumenta com a idade, aos de serviços "
      "africanos, onde os lactentes surgem como grupo mais afectado. A "
      "lacuna que este estudo preenche é clara: em Moçambique, a única "
      "medição existente restringiu-se aos antibióticos e a dois tipos de "
      "erro, não mediu a omissão do peso nem a legibilidade, não classificou "
      "a gravidade potencial e não avaliou a concordância entre "
      "avaliadores."),
]
ESQUEMA_TEXTO = [
    P("A [[figura:esquema]] representa as relações que o estudo examina. As "
      "características da criança, as características do internamento e da "
      "terapêutica e os factores organizacionais do serviço influenciam a "
      "ocorrência de erros na folha de prescrição. O desfecho é o erro de "
      "prescrição, observado ao nível da linha de medicamento e ao nível do "
      "internamento, decomposto nos tipos de erro que o estudo mede e "
      "graduado pela sua gravidade potencial. O mês do internamento, que "
      "reflecte a disponibilidade de medicamentos e a rotação de pessoal, e "
      "a qualidade do registo, que condiciona a detectabilidade do erro, são "
      "tratados como variáveis de confundimento."),
]
ESQUEMA_TITULO = ("Esquema conceptual dos factores associados aos erros de "
                  "prescrição em crianças internadas")
ESQUEMA = {
    "contexto": ("Internamentos de crianças com menos de 15 anos na "
                 "enfermaria de Pediatria do Hospital Central de Nampula, "
                 "1 de Janeiro a 31 de Dezembro de 2026"),
    "blocos": [
        ("Características da criança",
         ["idade em meses", "sexo", "peso registado e estado nutricional",
          "diagnóstico principal e comorbilidades", "infecção por HIV"]),
        ("Características da terapêutica",
         ["número de medicamentos por internamento",
          "presença de medicamento por via endovenosa",
          "grupo terapêutico e margem terapêutica estreita",
          "duração do internamento"]),
        ("Factores organizacionais",
         ["categoria profissional do prescritor",
          "turno e dia da admissão",
          "impresso de prescrição utilizado",
          "existência de tabela de doses na enfermaria"]),
    ],
    "desfecho": ("Erro de prescrição",
                 ["dose calculada pelo peso", "frequência", "via",
                  "duração", "omissão de informação essencial",
                  "gravidade potencial"]),
    "moderadores": ("Variáveis de confundimento",
                    ["mês do internamento",
                     "qualidade e legibilidade do registo"]),
}

# === PARTE 2 A ACRESCENTAR ===
