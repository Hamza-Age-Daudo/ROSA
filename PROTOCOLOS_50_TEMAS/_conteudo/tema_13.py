# -*- coding: utf-8 -*-
"""
Tema 13: Ganho de peso, obesidade abdominal e alteracoes da pressao arterial
em adultos com esquemas contendo dolutegravir no Hospital Central de Nampula
(Farmacovigilancia e Seguranca do Medicamento). Transversal analitico com
componente longitudinal retrospectiva (peso e pressao arterial iniciais
extraidos do processo clinico; medicao actual em 2027).

Compor e validar:   python _motor/motor.py _conteudo/tema_13.py
Verificar fontes:   python _motor/refs.py verificar _conteudo/tema_13.py
"""
from blocos import (CAMPO, FORMULA, H3, LISTA, NOTA, P, PERG, QUADRO, TABELA)

NUMERO = 13
SLUG = "Peso_Pressao_Arterial_Dolutegravir_Nampula"
TITULO = ("Ganho de peso, obesidade abdominal e alterações da pressão "
          "arterial em adultos em tratamento com dolutegravir no Hospital "
          "Central de Nampula, 2027")
DESENHO = ("Transversal analítico de base hospitalar, com componente "
           "longitudinal retrospectiva: medição do peso, altura, perímetro "
           "abdominal e pressão arterial comparada com os valores registados "
           "no processo clínico no início do esquema")

AUTOR = "[Nome do(a) estudante]"
ORIENTADOR = "[Nome e grau académico do(a) orientador(a)]"

# ---------------------------------------------------------------- resumo --
RESUMO = (
    "O dolutegravir integra o esquema de primeira linha recomendado para o "
    "tratamento da infecção pelo vírus da imunodeficiência humana e "
    "substituiu o efavirenz na quase totalidade dos adultos seguidos nas "
    "unidades sanitárias moçambicanas. Ensaios clínicos e coortes africanas "
    "descrevem com este fármaco um ganho de peso superior ao observado com "
    "os esquemas anteriores, acompanhado de aumento do perímetro abdominal e "
    "da pressão arterial em algumas populações, mas a magnitude do efeito "
    "varia muito entre países e desconhece-se o que sucede no norte de "
    "Moçambique, onde a insegurança alimentar é frequente e a medição da "
    "pressão arterial é pouco praticada. O estudo tem como objectivo avaliar "
    "a variação do peso corporal e da pressão arterial e a frequência de "
    "excesso de peso, obesidade, obesidade abdominal e tensão arterial "
    "elevada em adultos tratados com esquemas contendo dolutegravir no maior "
    "hospital da cidade de Nampula. Adopta-se um desenho transversal "
    "analítico com componente retrospectiva: o peso e a pressão arterial do "
    "início do esquema serão extraídos do processo clínico e comparados com "
    "a medição feita no momento do estudo. Participarão 241 adultos com pelo "
    "menos doze meses de exposição ao esquema, escolhidos por amostragem "
    "sistemática na consulta de seguimento, entre Março e Julho de 2027. O "
    "peso, a altura, o perímetro abdominal e a pressão arterial serão "
    "medidos por dois avaliadores formados, com aparelhos validados e "
    "aferidos, segundo um procedimento padronizado. A análise recorre a "
    "testes para amostras emparelhadas, proporções com intervalos de "
    "confiança e modelos de regressão linear e logística. Espera-se "
    "quantificar o ganho de peso médio anual, a proporção de participantes "
    "com aumento igual ou superior a dez por cento do peso inicial e a "
    "frequência de tensão arterial elevada, identificando os grupos que "
    "merecem vigilância metabólica reforçada e apoio nutricional dentro da "
    "própria consulta de tratamento.")
PALAVRAS_CHAVE = ["dolutegravir", "hipertensão", "Moçambique",
                  "obesidade abdominal", "peso corporal"]
ABSTRACT = (
    "Dolutegravir is part of the recommended first-line regimen for the "
    "treatment of human immunodeficiency virus infection and has replaced "
    "efavirenz for almost all adults followed in Mozambican health "
    "facilities. Clinical trials and African cohorts describe greater weight "
    "gain with this drug than with previous regimens, accompanied by "
    "increases in waist circumference and blood pressure in some "
    "populations, but the size of the effect varies widely between countries "
    "and nothing is known about northern Mozambique, where food insecurity "
    "is common and blood pressure is seldom measured. This study aims to "
    "assess the change in body weight and blood pressure and the frequency "
    "of overweight, obesity, abdominal obesity and raised blood pressure in "
    "adults treated with dolutegravir-containing regimens at the largest "
    "hospital in the city of Nampula. An analytical cross-sectional design "
    "with a retrospective component is adopted: weight and blood pressure at "
    "the start of the regimen will be extracted from the clinical record and "
    "compared with measurements taken at the time of the study. A total of "
    "241 adults with at least twelve months of exposure to the regimen will "
    "take part, chosen by systematic sampling at the follow-up consultation, "
    "between March and July 2027. Weight, height, waist circumference and "
    "blood pressure will be measured by two trained assessors, with "
    "validated and calibrated devices, following a standardised procedure. "
    "Analysis will use paired-sample tests, proportions with confidence "
    "intervals and linear and logistic regression models. The study is "
    "expected to quantify mean annual weight gain, the proportion of "
    "participants with an increase of ten per cent or more over the initial "
    "weight and the frequency of raised blood pressure, identifying the "
    "groups that deserve closer metabolic surveillance and nutritional "
    "support within the treatment consultation itself.")
KEYWORDS = ["abdominal obesity", "body weight", "dolutegravir",
            "hypertension", "Mozambique"]

ABREVIATURAS = [
    ("ADVANCE", "designação do ensaio clínico sul-africano que comparou três "
                "esquemas de primeira linha"),
    ("IMC", "índice de massa corporal"),
    ("MISAU", "Ministério da Saúde"),
    ("NAMSAL", "designação do ensaio clínico camaronês que comparou o "
               "dolutegravir com o efavirenz em dose reduzida"),
    ("OMS", "Organização Mundial da Saúde"),
    ("SIDA", "síndrome da imunodeficiência adquirida"),
    ("SPSS", "Statistical Package for the Social Sciences"),
    ("STROBE", "normas para o relato de estudos observacionais em "
               "epidemiologia (Strengthening the Reporting of Observational "
               "Studies in Epidemiology)"),
    ("TARV", "tratamento anti-retroviral"),
    ("TLD", "combinação em dose fixa de tenofovir disoproxil fumarato, "
            "lamivudina e dolutegravir"),
    ("VIH", "vírus da imunodeficiência humana"),
]

# ------------------------------------------------------------ referencias --
FONTES = {
    # --- documentos oficiais e normas
    "who_hiv2021": "World Health Organization. Consolidated guidelines on HIV prevention, testing, treatment, service delivery and monitoring: recommendations for a public health approach [Internet]. Geneva: World Health Organization; 2021 [citado 2026 Set 19]. Disponível em: https://www.who.int/publications/i/item/9789240031593",
    "who_hta2021": "World Health Organization. Guideline for the pharmacological treatment of hypertension in adults [Internet]. Geneva: World Health Organization; 2021 [citado 2026 Set 19]. Disponível em: https://www.who.int/publications/i/item/9789240033986",
    "who_obes": "World Health Organization. Obesity and overweight: fact sheet [Internet]. Geneva: World Health Organization; 2024 [citado 2026 Set 19]. Disponível em: https://www.who.int/news-room/fact-sheets/detail/obesity-and-overweight",
    "who_steps": "World Health Organization. WHO STEPS surveillance manual. Part 3, Section 5: collecting Step 2 data: physical measurements [Internet]. Geneva: World Health Organization; 2017 [citado 2026 Set 19]. Disponível em: https://cdn.who.int/media/docs/default-source/ncds/ncd-surveillance/steps/part3-section5.pdf",
    "who_perimetro2011": "World Health Organization. Waist circumference and waist-hip ratio: report of a WHO expert consultation [Internet]. Geneva: World Health Organization; 2011 [citado 2026 Set 19]. Disponível em: https://www.who.int/publications/i/item/9789241501491",
    "misau_mds2023": "Ministério da Saúde (Moçambique), Direcção Nacional de Saúde Pública, Programa Nacional de Controlo do HIV e SIDA. Guião orientador sobre os modelos diferenciados de serviços para o HIV e SIDA em Moçambique [Internet]. Maputo: Ministério da Saúde; 2023 [citado 2026 Set 19]. Disponível em: https://www.differentiatedservicedelivery.org/wp-content/uploads/Mozambique-MOH-DSD-Manual-WEB.pdf",
    "insida2021": "Instituto Nacional de Saúde (Moçambique), Ministério da Saúde, Conselho Nacional de Combate ao HIV e SIDA, Instituto Nacional de Estatística. Mozambique population-based HIV impact assessment INSIDA 2021: summary sheet [Internet]. Maputo: Instituto Nacional de Saúde; 2022 [citado 2026 Set 19]. Disponível em: https://phia.icap.columbia.edu/wp-content/uploads/2022/12/53059_14_INSIDA_Summary-sheet-Web.pdf",
    "ine2021": "Instituto Nacional de Estatística (Moçambique). IV Recenseamento Geral da População e Habitação 2017: resultados definitivos, província de Nampula [Internet]. Nampula: Instituto Nacional de Estatística; 2021 [citado 2026 Set 19]. Disponível em: http://www.sina.gov.mz/wp-content/uploads/2024/05/NAMPULA-RESUTADOS-DEFINITIVOS-DO-CENSO-2017.pdf",
    # --- ensaios clinicos e sintese de evidencia
    "kouanfack2019": "Kouanfack C, Mpoudi-Etame M, Omgba Bassega P, Eymard-Duvernay S, Leroy S, Boyer S, et al. Dolutegravir-Based or Low-Dose Efavirenz-Based Regimen for the Treatment of HIV-1. N Engl J Med. 2019;381(9):816-826. doi:10.1056/NEJMoa1904340. PMID: 31339676.",
    "calmy2020": "Calmy A, Tovar Sanchez T, Kouanfack C, Mpoudi-Etame M, Leroy S, Perrineau S, et al. Dolutegravir-based and low-dose efavirenz-based regimen for the initial treatment of HIV-1 infection (NAMSAL): week 96 results from a two-group, multicentre, randomised, open label, phase 3 non-inferiority trial in Cameroon. Lancet HIV. 2020;7(10):e677-e687. doi:10.1016/S2352-3018(20)30238-1. PMID: 33010241.",
    "sokhela2024": "Sokhela S, Venter WDF, Bosch B, Woods J, McCann K, Akpomiemie G, et al. Final 192-Week Efficacy and Safety Results of the ADVANCE Trial, Comparing 3 First-line Antiretroviral Regimens. Open Forum Infect Dis. 2024;11(3):ofae007. doi:10.1093/ofid/ofae007. PMID: 38529213.",
    "mannegoehler2024": "Manne-Goehler J, Fabian J, Sokhela S, Akpomiemie G, Rahim N, Lalla-Edward ST, et al. Blood pressure increases are associated with weight gain and not antiretroviral regimen or kidney function: a secondary analysis from the ADVANCE trial in South Africa. J Int AIDS Soc. 2024;27(7):e26268. doi:10.1002/jia2.26268. PMID: 38978403.",
    "mccann2021": "McCann K, Shah S, Hindley L, Hill A, Qavi A, Simmons B, et al. Implications of weight gain with newer anti-retrovirals: 10-year predictions of cardiovascular disease and diabetes. AIDS. 2021;35(10):1657-1665. doi:10.1097/QAD.0000000000002930. PMID: 33927086.",
    "kanters2022": "Kanters S, Renaud F, Rangaraj A, Zhang K, Limbrick-Oldfield E, Hughes M, et al. Evidence synthesis evaluating body weight gain among people treating HIV with antiretroviral therapy - a systematic literature review and network meta-analysis. EClinicalMedicine. 2022;48:101412. doi:10.1016/j.eclinm.2022.101412. PMID: 35706487.",
    # --- coortes e estudos africanos
    "esber2022": "Esber AL, Chang D, Iroezindu M, Bahemana E, Kibuuka H, Owuoth J, et al. Weight gain during the dolutegravir transition in the African Cohort Study. J Int AIDS Soc. 2022;25(4):e25899. doi:10.1002/jia2.25899. PMID: 35419973.",
    "romo2023": "Romo ML, Esber AL, Owuoth J, Maswai J, Sing'oei V, Iroezindu M, et al. Impact of weight gain with dolutegravir on antiretroviral adherence and viral suppression in four African countries. HIV Med. 2023;24(10):1066-1074. doi:10.1111/hiv.13501. PMID: 37232057.",
    "shamu2024": "Shamu T, Egger M, Mudzviti T, Chimbetete C, Manasa J, Anderegg N. Body weight and blood pressure changes on dolutegravir-, efavirenz- or atazanavir-based antiretroviral therapy in Zimbabwe: a longitudinal study. J Int AIDS Soc. 2024;27(2):e26216. doi:10.1002/jia2.26216. PMID: 38332525.",
    "kouamou2024": "Kouamou V, Washaya T, Mapangisana T, Ndhlovu CE, Manasa J. Virological, weight, and drug resistance outcomes among patients initiating a dolutegravir-based first-line antiretroviral therapy regimen in Zimbabwe. AIDS. 2024;38(5):689-696. doi:10.1097/QAD.0000000000003830. PMID: 38227596.",
    "bourgi2022": "Bourgi K, Ofner S, Musick B, Griffith B, Diero L, Wools-Kaloustian K, et al. Weight Gain Among Treatment-Naïve Persons With HIV Receiving Dolutegravir in Kenya. J Acquir Immune Defic Syndr. 2022;91(5):490-496. doi:10.1097/QAI.0000000000003087. PMID: 36126175.",
    "hickey2023": "Hickey MD, Wafula E, Ogachi SM, Ojwando H, Orori G, Adede RO, et al. Weight Change Following Switch to Dolutegravir for HIV Treatment in Rural Kenya During Country Roll-Out. J Acquir Immune Defic Syndr. 2023;93(2):154-161. doi:10.1097/QAI.0000000000003173. PMID: 36787723.",
    "migisha2024": "Migisha R, Chen G, Muyindike WR, Aung TN, Nanfuka V, Komukama N, et al. Regional variation in weight change after the transition to dolutegravir in Uganda and South Africa. AIDS. 2024;38(9):1314-1322. doi:10.1097/QAD.0000000000003888. PMID: 38507584.",
    "tien2026": "Tien D, Chandiwana N, Shazi G, Chen G, Mabweazara S, Moosa MS, et al. Brief Report: Dolutegravir-Based Therapy, Diet, Physical Activity, and Weight Gain: A 48-week Prospective Cohort in South Africa. J Acquir Immune Defic Syndr. 2026;101(4):405-408. doi:10.1097/QAI.0000000000003812. PMID: 41329528.",
    "mukuna2024": "Mukuna DM, Decroo T, Nyapokoto CM. Effect of dolutegravir-based versus efavirenz-based antiretroviral therapy on excessive weight gain in adult treatment-naïve HIV patients at Matsanjeni health center, Eswatini: a retrospective cohort study. AIDS Res Ther. 2024;21(1):4. doi:10.1186/s12981-023-00591-3. PMID: 38185696.",
    "hachey2023": "Hachey D, van Woerden I, Shiluama R, Singu BS. Weight gain in Namibians with HIV switching from efavirenz to dolutegravir. Int J STD AIDS. 2023;34(12):854-859. doi:10.1177/09564624231179767. PMID: 37309139.",
    "jemal2025": "Jemal M, Abebaw D, Workineh YT, Liyew WA, Malik T, Adugna A. Hypertension among people living with HIV receiving dolutegravir-based antiretroviral therapy in ethiopia: a cross-sectional study. Sci Rep. 2025;15(1):23267. doi:10.1038/s41598-025-06145-z. PMID: 40603478.",
    "jemalms2024": "Jemal M, Ashenef B, Sinamaw D, Adugna A, Getinet M, Baylie T, et al. Metabolic Syndrome Among People Living With HIV on Dolutegravir and Efavirenz-Based Antiretroviral Therapy in Ethiopia: A Comparative Cross-Sectional Study. J Int Assoc Provid AIDS Care. 2024;23:23259582241303305. doi:10.1177/23259582241303305. PMID: 39665219.",
    "mirai2024": "Mirai TE, Kilonzo KG, Sadiq AM, Muhina IAI, Kyala NJ, Marandu AA, et al. Metabolic Syndrome and Associated Factors Among People Living With HIV on Dolutegravir-Based Antiretroviral Therapy in Northern Tanzania. J Int Assoc Provid AIDS Care. 2024;23:23259582241306492. doi:10.1177/23259582241306492. PMID: 39714472.",
    "todowede2019": "Todowede OO, Mianda SZ, Sartorius B. Prevalence of metabolic syndrome among HIV-positive and HIV-negative populations in sub-Saharan Africa-a systematic review and meta-analysis. Syst Rev. 2019;8(1):4. doi:10.1186/s13643-018-0927-y. PMID: 30606249.",
    # --- mecanismos e revisoes
    "bailin2020": "Bailin SS, Gabriel CL, Wanjalla CN, Koethe JR. Obesity and Weight Gain in Persons with HIV. Curr HIV/AIDS Rep. 2020;17(2):138-150. doi:10.1007/s11904-020-00483-5. PMID: 32072466.",
    "gorwood2020": "Gorwood J, Bourgeois C, Pourcher V, Pourcher G, Charlotte F, Mantecon M, et al. The Integrase Inhibitors Dolutegravir and Raltegravir Exert Proadipogenic and Profibrotic Effects and Induce Insulin Resistance in Human/Simian Adipose Tissue and Human Adipocytes. Clin Infect Dis. 2020;71(10):e549-e560. doi:10.1093/cid/ciaa259. PMID: 32166319.",
    "jemalrev2024": "Jemal M. A review of dolutegravir-associated weight gain and secondary metabolic comorbidities. SAGE Open Med. 2024;12:20503121241260613. doi:10.1177/20503121241260613. PMID: 38881592.",
    # --- medicao, normas de hipertensao e de relato
    "ross2020": "Ross R, Neeland IJ, Yamashita S, Shai I, Seidell J, Magni P, et al. Waist circumference as a vital sign in clinical practice: a Consensus Statement from the IAS and ICCR Working Group on Visceral Obesity. Nat Rev Endocrinol. 2020;16(3):177-189. doi:10.1038/s41574-019-0310-7. PMID: 32020062.",
    "mancia2023": "Mancia G, Kreutz R, Brunström M, Burnier M, Grassi G, Januszewicz A, et al. 2023 ESH Guidelines for the management of arterial hypertension The Task Force for the management of arterial hypertension of the European Society of Hypertension: Endorsed by the International Society of Hypertension (ISH) and the European Renal Association (ERA). J Hypertens. 2023;41(12):1874-2071. doi:10.1097/HJH.0000000000003480. PMID: 37345492.",
    "doku2026": "Doku A, Kruger R, Asamoah KT, Akumiah FK, Auala T, Beheiry H, et al. 2026 ISH guidelines for the management of hypertension in Africa: the International Society of Hypertension (ISH) African Regional Advisory Group and the Pan African Society of Cardiology (PASCAR). J Hypertens. 2026;44(10):1732-1760. doi:10.1097/HJH.0000000000004411. PMID: 42554264.",
    "stergiou2018": "Stergiou GS, Alpert B, Mieke S, Asmar R, Atkins N, Eckert S, et al. A universal standard for the validation of blood pressure measuring devices: Association for the Advancement of Medical Instrumentation/European Society of Hypertension/International Organization for Standardization (AAMI/ESH/ISO) Collaboration Statement. J Hypertens. 2018;36(3):472-478. doi:10.1097/HJH.0000000000001634. PMID: 29384983.",
    "von2008": "von Elm E, Altman DG, Egger M, Pocock SJ, Gøtzsche PC, Vandenbroucke JP. The Strengthening the Reporting of Observational Studies in Epidemiology (STROBE) statement: guidelines for reporting observational studies. J Clin Epidemiol. 2008;61(4):344-9. doi:10.1016/j.jclinepi.2007.11.008. PMID: 18313558.",
    "world2025": "World Medical Association. World Medical Association Declaration of Helsinki: Ethical Principles for Medical Research Involving Human Participants. JAMA. 2025;333(1):71-74. doi:10.1001/jama.2024.21972. PMID: 39425955.",
    # --- Mocambique e Nampula
    "jessen2018": "Jessen N, Damasceno A, Silva-Matos C, Tuzine E, Madede T, Mahoque R, et al. Hypertension in Mozambique: trends between 2005 and 2015. J Hypertens. 2018;36(4):779-784. doi:10.1097/HJH.0000000000001618. PMID: 29210894.",
    "matsuzaki2020": "Matsuzaki M, Sherr K, Augusto O, Kawakatsu Y, Ásbjörnsdóttir K, Chale F, et al. The prevalence of hypertension and its distribution by sociodemographic factors in Central Mozambique: a cross sectional study. BMC Public Health. 2020;20(1):1843. doi:10.1186/s12889-020-09947-0. PMID: 33261617.",
    "fontes2019": "Fontes F, Damasceno A, Jessen N, Prista A, Silva-Matos C, Padrão P, et al. Prevalence of overweight and obesity in Mozambique in 2005 and 2015. Public Health Nutr. 2019;22(17):3118-3126. doi:10.1017/S1368980019002325. PMID: 31453793.",
    "silva2023": "Silva I, Damasceno A, Fontes F, Araújo N, Prista A, Jessen N, et al. Prevalence of Cardiovascular Risk Factors among Young Adults (18-25 Years) in Mozambique. J Cardiovasc Dev Dis. 2023;10(7). doi:10.3390/jcdd10070298. PMID: 37504554.",
    "ismael2025": "Ismael N, Hussein C, Magul C, Inguane H, Couto A, Nhangave A, et al. HIV Drug Resistance Profile in Clients Experiencing Treatment Failure After the Transition to a Dolutegravir-Based First-Line Antiretroviral Treatment Regimen in Mozambique. Pathogens. 2025;14(1). doi:10.3390/pathogens14010048. PMID: 39861009.",
    "meque2024": "Meque I, Herrera N, Nhangave A, Mandlate D, Guilaze R, Tambo A, et al. The rollout of paediatric dolutegravir and virological outcomes among children living with HIV in Mozambique. South Afr J HIV Med. 2024;25(1):1578. doi:10.4102/sajhivmed.v25i1.1578. PMID: 39113779.",
    "cobre2020": "Cobre AF, Pedro CAA, Fachi MM, Vilhena RO, Marson BM, Nicobue V, et al. Five-year survival analysis and predictors of death in HIV-positive serology patients attending the Military Hospital of Nampula, Mozambique. AIDS Care. 2020;32(11):1379-1387. doi:10.1080/09540121.2020.1761938. PMID: 32397744.",
    "teasdale2021": "Teasdale CA, Brittain K, Zerbe A, Mellins CA, Falcao J, Couto A, et al. Characteristics of adolescents aged 15-19 years living with vertically and horizontally acquired HIV in Nampula, Mozambique. PLoS One. 2021;16(4):e0250218. doi:10.1371/journal.pone.0250218. PMID: 33901229.",
}

SEMINAIS = {
    "who_perimetro2011": "Relatório da consulta de peritos da Organização "
                         "Mundial da Saúde que fixa os pontos de corte do "
                         "perímetro abdominal usados neste protocolo; "
                         "continua a ser a norma de referência em vigor.",
    "von2008": "Documento original das normas de relato de estudos "
               "observacionais (STROBE), exigido pelas revistas e pela "
               "Comissão Científica; não foi substituído por versão "
               "posterior.",
}

# ----------------------------------------------------- 1. introducao --------
INTRODUCAO = [
    P("O tratamento anti-retroviral (TARV) transformou a infecção pelo vírus "
      "da imunodeficiência humana (VIH) numa doença crónica e deslocou a "
      "atenção clínica dos episódios oportunistas para a segurança a longo "
      "prazo dos medicamentos. Desde 2018, a Organização Mundial da Saúde "
      "(OMS) recomenda o dolutegravir, um inibidor da integrase, como "
      "fármaco preferencial de primeira e de segunda linha em todas as "
      "populações, combinado em dose fixa com tenofovir disoproxil fumarato "
      "e lamivudina (TLD) {who_hiv2021,jemalrev2024}. A escolha assentou na "
      "barreira genética elevada, na rapidez da supressão viral e na melhor "
      "tolerabilidade neuropsiquiátrica face ao efavirenz. Moçambique "
      "acompanhou a recomendação e transitou os adultos em TARV para o "
      "esquema com dolutegravir, processo cuja execução em campo já foi "
      "documentada na província de Gaza, onde 717 adultos transitados para o "
      "TLD foram avaliados entre Agosto de 2021 e Fevereiro de 2022 "
      "{ismael2025}, e cuja extensão pediátrica decorreu a partir de 2022 "
      "{meque2024}."),
    P("Ao mesmo tempo que confirmavam a eficácia virológica, os ensaios "
      "conduzidos em África levantaram um sinal de segurança metabólica. No "
      "ensaio NAMSAL, realizado nos Camarões com 613 adultos sem tratamento "
      "prévio, o ganho mediano de peso às 48 semanas foi de 5,0 kg no grupo "
      "do dolutegravir contra 3,0 kg no grupo do efavirenz em dose reduzida, "
      "com incidência de obesidade de 12,3% e 5,4% {kouanfack2019}; às 96 "
      "semanas, a incidência de obesidade era de 22% e 16% {calmy2020}. No "
      "ensaio ADVANCE, conduzido na África do Sul, o ganho médio de peso às "
      "192 semanas foi de 8,9 kg com tenofovir alafenamida associado ao "
      "dolutegravir, de 5,9 kg com tenofovir disoproxil fumarato associado "
      "ao dolutegravir e de 3,2 kg com o esquema contendo efavirenz, sendo "
      "maior nas mulheres {sokhela2024}. Uma meta-análise em rede "
      "encomendada pela OMS, que reuniu 73 estudos, estimou uma diferença "
      "média de 1,99 kg às 96 semanas entre os esquemas com dolutegravir e "
      "os esquemas com efavirenz {kanters2022}."),
    P("O ganho de peso não é um desfecho estético. A análise secundária do "
      "ensaio ADVANCE mostrou que, ao longo de 96 semanas, a proporção de "
      "participantes que desenvolveu tensão arterial elevada durante o "
      "tratamento foi de 18,2%, 15,4% e 13,3% nos três grupos, e que a "
      "variação do índice de massa corporal (IMC), e não o esquema em si, "
      "explicava o aumento da pressão sistólica {mannegoehler2024}. Numa "
      "coorte do Zimbabwe com 9.487 adultos, o ganho mediano de peso aos 24 "
      "meses após o início ou a mudança para dolutegravir foi de 4,54 kg nas "
      "mulheres e de 3,71 kg nos homens, e a prevalência de tensão arterial "
      "elevada subiu de cerca de 5% no início para mais de 20% aos 24 meses, "
      "sem alteração equivalente nos doentes que mantiveram efavirenz ou "
      "atazanavir {shamu2024}. A projecção do risco a dez anos a partir dos "
      "dados do ADVANCE aponta para excesso de casos de diabetes e, em menor "
      "grau, de doença cardiovascular atribuíveis ao peso ganho "
      "{mccann2021}."),
    P("A magnitude do efeito, porém, não é uniforme em África. Num estudo "
      "prospectivo que seguiu 428 adultos no Uganda e 367 na África do Sul "
      "durante 48 semanas após a transição para o TLD, a variação média do "
      "peso foi de 0,6 kg no Uganda e de 2,9 kg na África do Sul, a do "
      "perímetro abdominal foi de 0,8 cm e 2,3 cm, e o ganho de peso "
      "clinicamente significativo, definido como aumento de 10% ou mais, "
      "ocorreu em 9,8% e 18,0% dos participantes {migisha2024}. Em meio "
      "rural no Quénia, onde a insegurança alimentar é frequente, o peso aos "
      "12 meses após a mudança foi apenas 0,7 kg superior ao previsto nas "
      "mulheres e praticamente igual ao previsto nos homens, e o ganho "
      "esperado era maior nos participantes com segurança alimentar "
      "{hickey2023}. Estes contrastes mostram que o efeito depende do estado "
      "nutricional e do contexto alimentar da população, o que impede "
      "transpor directamente para o norte de Moçambique os valores "
      "observados na África austral."),
    P("Moçambique reúne as duas condições que tornam a questão relevante. "
      "Por um lado, a carga da infecção é elevada: o inquérito nacional de "
      "impacto realizado entre Abril de 2021 e Fevereiro de 2022 estimou uma "
      "prevalência de 12,5% nos adultos com 15 ou mais anos, correspondente "
      "a cerca de 2.097.000 pessoas, com 15,0% nas mulheres e 9,5% nos "
      "homens, e 10,0% na província de Nampula {insida2021}. Por outro lado, "
      "os factores de risco cardiovascular são comuns e mal detectados: a "
      "prevalência de hipertensão arterial nos adultos de 25 a 64 anos "
      "passou de 33,1% em 2005 para 38,9% em 2014-2015, com apenas 14,5% dos "
      "hipertensos conscientes da sua condição {jessen2018}. Num inquérito "
      "domiciliário nas províncias de Manica e Sofala, entre os participantes "
      "com tensão arterial elevada apenas 34,9% tinham tido alguma medição "
      "anterior e 12,2% tinham diagnóstico prévio {matsuzaki2020}. No mesmo "
      "período, a prevalência de excesso de peso e obesidade subiu de 18,3% "
      "para 30,5% nas mulheres e de 11,7% para 18,2% nos homens, e a "
      "obesidade abdominal nas mulheres mais do que duplicou, de 9,4% para "
      "20,4% {fontes2019}."),
    P("Nampula é a província mais populosa do país {ine2021} e apresenta um "
      "desempenho programático desfavorável: a supressão da carga viral "
      "entre os adultos que vivem com VIH foi de 47,9%, contra 64,1% no "
      "conjunto do país {insida2021}. A investigação local disponível "
      "concentra-se na sobrevivência e nos preditores de morte em coortes "
      "hospitalares {cobre2020} e nas características dos adolescentes em "
      "seguimento {teasdale2021}, sem qualquer avaliação dos efeitos "
      "metabólicos do esquema actualmente em uso. Acresce que os modelos "
      "diferenciados de serviços adoptados pelo Ministério da Saúde (MISAU) "
      "afastam o utente estável da unidade sanitária, com dispensa trimestral "
      "ou semestral de medicamentos e levantamento comunitário "
      "{misau_mds2023}, reduzindo as oportunidades de pesar o doente e de "
      "lhe medir a pressão arterial."),
    P("Existe, assim, uma lacuna concreta: sabe-se que o dolutegravir faz "
      "ganhar peso e que o peso ganho faz subir a pressão arterial, mas "
      "desconhece-se a dimensão deste fenómeno na população adulta seguida "
      "no norte de Moçambique, onde coexistem desnutrição prévia, "
      "insegurança alimentar e transição nutricional urbana. O presente "
      "estudo propõe-se medir o peso, a altura, o perímetro abdominal e a "
      "pressão arterial de adultos em tratamento com esquemas contendo "
      "dolutegravir no Hospital Central de Nampula e compará-los com os "
      "valores registados no processo clínico no início do esquema, "
      "quantificando a variação e a frequência das alterações "
      "antropométricas e tensionais que dela resultam."),
]

# ----------------------------------------------------- 2. problema ----------
PROBLEMA = [
    P("Na consulta de TARV do Hospital Central de Nampula acompanha-se "
      "actualmente uma população adulta quase inteiramente tratada com "
      "esquemas contendo dolutegravir, na sequência da transição nacional "
      "{ismael2025}. O peso é registado de forma rotineira nas fichas de "
      "seguimento, mas serve sobretudo para detectar emagrecimento, sinal "
      "clássico de falência terapêutica ou de tuberculose. O aumento de "
      "peso, pelo contrário, tende a ser interpretado como recuperação do "
      "estado nutricional e não desencadeia qualquer acção, mesmo quando "
      "ultrapassa os limiares que definem excesso de peso e obesidade "
      "{who_obes}. A pressão arterial não é medida de forma sistemática em "
      "cada visita e, quando é medida, raramente conduz a seguimento, como "
      "sucede no conjunto do país {matsuzaki2020}."),
    P("A consequência é dupla. Em primeiro lugar, doentes que ganham peso "
      "rapidamente e desenvolvem obesidade abdominal permanecem sem "
      "identificação, apesar de a literatura africana mostrar que uma parte "
      "substancial dos utentes transitados ultrapassa os 10% de aumento face "
      "ao peso inicial {migisha2024,tien2026} e de o perímetro abdominal ser "
      "a componente mais frequente da síndrome metabólica nesta população "
      "{mirai2024}. Em segundo lugar, a hipertensão arterial instala-se sem "
      "diagnóstico, num serviço que vê o doente várias vezes por ano e que "
      "teria, por isso, a melhor oportunidade de rastreio de todo o sistema "
      "de saúde {shamu2024,jemal2025}. A soma dos dois problemas transfere "
      "para o futuro um custo evitável de doença cardiovascular e de "
      "diabetes {mccann2021}."),
    P("A esta falha clínica junta-se uma falha de informação. Não existe, "
      "até onde foi possível apurar, qualquer estudo moçambicano publicado "
      "que quantifique o ganho de peso associado ao dolutegravir ou a "
      "variação da pressão arterial que o acompanha, nem na região norte nem "
      "no resto do país. A evidência regional disponível é heterogénea e "
      "gerada em contextos com perfis nutricionais diferentes "
      "{hickey2023,migisha2024}, o que impede o programa nacional de decidir "
      "se precisa de vigilância metabólica reforçada e, em caso afirmativo, "
      "para que grupos. Sem um valor local, o serviço não sabe quantos "
      "doentes deveria referenciar, nem com que periodicidade deveria "
      "pesá-los e medir-lhes a pressão arterial."),
    P("Este estudo responde a essa falha medindo directamente os "
      "participantes e recuperando do processo clínico os valores do início "
      "do esquema, o que permite estimar a variação sem esperar por um "
      "seguimento prospectivo de vários anos. O desenho assume, por isso, "
      "uma dependência da qualidade do registo clínico, tratada de forma "
      "explícita na metodologia."),
]
PERGUNTA = ("Qual é a variação do peso corporal e da pressão arterial, e qual "
            "a frequência de excesso de peso, obesidade, obesidade abdominal "
            "e tensão arterial elevada, em adultos em tratamento com esquemas "
            "contendo dolutegravir no Hospital Central de Nampula?")
DELIMITACAO = [
    P("O estudo decorre no Hospital Central de Nampula, cidade de Nampula, "
      "província de Nampula, na consulta e na farmácia de atendimento a "
      "pessoas que vivem com VIH. A população de estudo são os adultos com "
      "18 ou mais anos, de ambos os sexos, em TARV com um esquema contendo "
      "dolutegravir há pelo menos 12 meses, com processo clínico disponível "
      "na unidade. A recolha decorre de Março a Julho de 2027, após "
      "aprovação ética, e os dados retrospectivos referem-se à data de "
      "início do esquema com dolutegravir de cada participante, qualquer que "
      "seja o ano em que ocorreu."),
    P("O objecto é a alteração antropométrica e tensional associada ao "
      "tempo de exposição ao dolutegravir: peso, IMC, perímetro abdominal e "
      "pressão arterial. Ficam fora do estudo as crianças e os adolescentes "
      "com menos de 18 anos, as mulheres grávidas e as que estejam no "
      "primeiro ano após o parto, os doentes internados e os que iniciaram o "
      "esquema há menos de 12 meses. Ficam igualmente fora do âmbito a "
      "avaliação laboratorial do perfil lipídico e da glicemia, a "
      "classificação de síndrome metabólica, a medição da composição "
      "corporal por métodos de imagem, a avaliação da adesão ao tratamento e "
      "a determinação da carga viral para além do que já conste do processo "
      "clínico. O estudo não atribui causalidade ao dolutegravir, porque não "
      "dispõe de um grupo concorrente tratado com outro esquema; descreve a "
      "magnitude da alteração numa população inteiramente exposta."),
]

# ----------------------------------------------------- 3. objectivos --------
OBJECTIVO_GERAL = ("Avaliar a variação do peso corporal e da pressão arterial "
                   "e a frequência de alterações antropométricas e tensionais "
                   "em adultos em tratamento com esquemas contendo "
                   "dolutegravir no Hospital Central de Nampula, em 2027.")
OBJECTIVOS_ESPECIFICOS = [
    "Caracterizar os participantes quanto às variáveis sociodemográficas, "
    "clínicas, de tratamento e de estilo de vida.",
    "Determinar a variação do peso corporal e do índice de massa corporal "
    "entre o início do esquema contendo dolutegravir e a avaliação actual, "
    "incluindo a variação anualizada e a proporção de participantes com "
    "ganho igual ou superior a 10% do peso inicial.",
    "Estimar a prevalência de excesso de peso, de obesidade, de obesidade "
    "abdominal e de tensão arterial elevada na avaliação actual e descrever "
    "a variação da pressão arterial nos participantes com registo inicial "
    "utilizável.",
    "Identificar os factores sociodemográficos, clínicos, de tratamento e de "
    "estilo de vida associados ao ganho de peso durante a exposição ao "
    "dolutegravir.",
    "Analisar a associação entre a variação do peso corporal e a pressão "
    "arterial medida na avaliação actual.",
]

# ----------------------------------------------------- 4. hipoteses ---------
HIPOTESES_INTRO = [
    P("As hipóteses referem-se aos objectivos específicos 4 e 5, que "
      "constituem as componentes analíticas do estudo. Os objectivos "
      "específicos 1 a 3 são descritivos e conduzem às questões de "
      "investigação abaixo. O nível de significância adoptado é de 5%."),
]
HIPOTESES = [
    ("H0", "não existe associação estatisticamente significativa entre o "
           "tempo de exposição ao esquema contendo dolutegravir e o ganho de "
           "peso igual ou superior a 10% do peso inicial"),
    ("H1", "existe associação estatisticamente significativa entre o tempo de "
           "exposição ao esquema contendo dolutegravir e o ganho de peso "
           "igual ou superior a 10% do peso inicial"),
    ("H0", "não existe diferença estatisticamente significativa na proporção "
           "de participantes com ganho de peso igual ou superior a 10% entre "
           "mulheres e homens"),
    ("H1", "existe diferença estatisticamente significativa na proporção de "
           "participantes com ganho de peso igual ou superior a 10% entre "
           "mulheres e homens"),
    ("H0", "não existe associação estatisticamente significativa entre a "
           "variação do peso corporal e a pressão arterial sistólica medida "
           "na avaliação actual"),
    ("H1", "existe associação estatisticamente significativa entre a variação "
           "do peso corporal e a pressão arterial sistólica medida na "
           "avaliação actual"),
]
QUESTOES = [
    "Quais são as características sociodemográficas, clínicas, de tratamento "
    "e de estilo de vida dos adultos em tratamento com esquemas contendo "
    "dolutegravir no Hospital Central de Nampula?",
    "Qual é a variação média do peso corporal e do índice de massa corporal "
    "entre o início do esquema e a avaliação actual, e qual a variação "
    "anualizada?",
    "Qual é a prevalência de excesso de peso, de obesidade, de obesidade "
    "abdominal e de tensão arterial elevada nesta população?",
]

# ----------------------------------------------------- 5. justificativa -----
JUSTIFICATIVA_INTRO = [
    P("O estudo justifica-se por responder a um sinal de segurança "
      "reconhecido internacionalmente com dados medidos localmente, usando "
      "recursos que já existem no serviço e produzindo informação "
      "directamente utilizável pelo programa de tratamento."),
]
JUSTIFICATIVA = {
    "cientifica": [
        P("A evidência africana sobre o ganho de peso com o dolutegravir é "
          "abundante mas geograficamente desequilibrada: concentra-se na "
          "África do Sul, no Zimbabwe, no Quénia, no Uganda, na Etiópia e na "
          "Tanzânia {sokhela2024,shamu2024,hickey2023,migisha2024,jemal2025,"
          "mirai2024}, e a variação entre esses países é grande o suficiente "
          "para que a extrapolação seja imprudente. O contraste entre os 2,9 "
          "kg médios da África do Sul e os 0,6 kg do Uganda no mesmo "
          "protocolo de seguimento {migisha2024} indica que o estado "
          "nutricional de partida e a segurança alimentar modulam o efeito "
          "{hickey2023}. Uma medição no norte de Moçambique, região com "
          "elevada prevalência de insegurança alimentar e com transição "
          "nutricional urbana em curso {fontes2019}, acrescenta um ponto de "
          "observação que falta ao mapa continental."),
        P("O estudo acrescenta ainda a medição simultânea do perímetro "
          "abdominal e da pressão arterial, dimensões menos documentadas do "
          "que o peso. O perímetro abdominal é reconhecido como sinal vital "
          "na prática clínica por informar sobre a gordura visceral para "
          "além do que o IMC capta {ross2020} e é a componente mais "
          "prevalente da síndrome metabólica entre doentes africanos "
          "tratados com dolutegravir {mirai2024}. A associação entre "
          "variação de peso e pressão arterial, demonstrada em ensaio "
          "{mannegoehler2024} e em coorte {shamu2024}, nunca foi examinada "
          "em Moçambique."),
    ],
    "academica": [
        P("O protocolo exercita competências centrais da formação em "
          "Farmácia: farmacovigilância activa, avaliação de reacções "
          "adversas de instalação lenta, antropometria padronizada, medição "
          "validada da pressão arterial e leitura crítica do processo "
          "clínico. O estudante aprende a distinguir um efeito adverso "
          "previsível de um achado clínico isolado e a construir uma medida "
          "de exposição a partir de registos de rotina, competência exigida "
          "em qualquer sistema de farmacovigilância de países com recursos "
          "limitados."),
        P("A Faculdade de Ciências de Saúde da Universidade Lúrio tem "
          "produção prévia associada a coortes de doentes com VIH em Nampula "
          "{cobre2020}, o que facilita a continuidade metodológica e a "
          "comparação de resultados. O conjunto de dados gerado pode servir "
          "de base a trabalhos posteriores que acrescentem perfil lipídico, "
          "glicemia ou seguimento prospectivo, transformando este protocolo "
          "no primeiro passo de uma linha de investigação local sobre "
          "segurança metabólica do TARV."),
    ],
    "social": [
        P("Para o participante, o estudo tem benefício imediato: cada pessoa "
          "avaliada fica a conhecer o seu peso, o seu índice de massa "
          "corporal, o seu perímetro abdominal e a sua pressão arterial, e "
          "quem apresentar valores alterados é encaminhado para a consulta "
          "apropriada no mesmo dia. Num país em que apenas 34,9% dos adultos "
          "com tensão arterial elevada alguma vez tinham tido uma medição "
          "prévia {matsuzaki2020}, a simples execução do protocolo funciona "
          "como rastreio oportunista numa população que contacta o serviço "
          "de saúde com regularidade."),
        P("A população-alvo é vulnerável por duas vias que se reforçam: vive "
          "com uma infecção estigmatizada e enfrenta agora um risco "
          "cardiovascular crescente que os serviços de VIH não foram "
          "desenhados para gerir. Identificar quem ganha peso depressa "
          "permite oferecer aconselhamento nutricional e actividade física "
          "antes de instalada a obesidade, intervenção de custo baixo e "
          "aceitação elevada, ainda que a evidência sul-africana mostre que "
          "o efeito do estilo de vida sobre o ganho de peso associado ao "
          "fármaco é limitado {tien2026}, o que reforça a necessidade de "
          "vigilância clínica e não apenas de conselhos."),
    ],
    "politica": [
        P("O MISAU precisa de dados nacionais para decidir se acrescenta ao "
          "pacote de seguimento do utente estável a medição periódica do "
          "peso, do perímetro abdominal e da pressão arterial, e com que "
          "periodicidade. A adopção dos modelos diferenciados de serviços, "
          "com dispensa trimestral e semestral e levantamento comunitário "
          "{misau_mds2023}, reduziu o número de contactos clínicos e torna "
          "esta decisão mais delicada: quanto menos visitas, mais importa "
          "que as existentes incluam as medições certas."),
        P("Os resultados alimentam também o sistema nacional de "
          "farmacovigilância, ao documentar uma reacção adversa de "
          "instalação lenta que os sistemas de notificação espontânea "
          "raramente captam, e apoiam a integração entre o programa de VIH e "
          "o programa de doenças não transmissíveis, recomendada pelas "
          "orientações africanas de hipertensão {doku2026} e pela "
          "orientação da OMS sobre tratamento farmacológico da hipertensão "
          "{who_hta2021}."),
    ],
}

# ----------------------------------------------------- 6. revisao -----------
REVISAO = [
    ("Infecção pelo vírus da imunodeficiência humana e tratamento "
     "anti-retroviral em Moçambique", [
         P("Moçambique é um dos países com maior carga de infecção pelo VIH "
           "do mundo. O inquérito nacional de impacto conduzido entre Abril "
           "de 2021 e Fevereiro de 2022 estimou uma prevalência de 12,5% "
           "entre os adultos com 15 ou mais anos, o equivalente a cerca de "
           "2.097.000 pessoas, com uma diferença marcada entre sexos, de "
           "15,0% nas mulheres e 9,5% nos homens. A prevalência provincial "
           "variou entre 7,9% em Manica e 20,9% em Gaza, situando-se "
           "Nampula em 10,0%. A supressão da carga viral entre todos os "
           "adultos que vivem com o vírus foi de 64,1% no conjunto do país, "
           "mas apenas de 47,9% em Nampula, um dos valores mais baixos do "
           "território nacional {insida2021}."),
         P("Estes números traduzem-se, na prática clínica de Nampula, numa "
           "população numerosa em tratamento e com seguimento de qualidade "
           "desigual. A análise retrospectiva de 332 processos de doentes "
           "em primeira linha no Hospital Militar de Nampula mostrou uma "
           "sobrevida média de 54,8 meses nas mulheres e de 49,7 meses nos "
           "homens, com mortalidade associada ao diagnóstico apenas "
           "presuntivo e à ausência de contagem de linfócitos registada, o "
           "que indica que a lacuna de informação no processo clínico tem "
           "ela própria valor prognóstico {cobre2020}. Estudos em "
           "adolescentes seguidos em Nampula descrevem igualmente "
           "dificuldades de retenção e de documentação {teasdale2021}."),
         P("A organização dos cuidados mudou substancialmente com a adopção "
           "dos modelos diferenciados de serviços. O guião nacional em "
           "vigor define critérios de elegibilidade para a dispensa "
           "trimestral e semestral de anti-retrovirais e para o "
           "levantamento comunitário, destinados a utentes considerados "
           "estáveis, com mais de seis meses de tratamento e carga viral "
           "inferior a 1.000 cópias por mililitro {misau_mds2023}. O ganho "
           "em comodidade e em descongestionamento das unidades sanitárias "
           "tem como contrapartida a redução do número de contactos "
           "clínicos anuais, e com eles das ocasiões de pesar o utente, de "
           "lhe medir o perímetro abdominal e de lhe avaliar a pressão "
           "arterial. Qualquer estratégia de vigilância metabólica no "
           "contexto moçambicano tem de ser desenhada dentro destas "
           "restrições."),
     ]),
    ("Dolutegravir: lugar no esquema de primeira linha e perfil de "
     "segurança", [
         P("O dolutegravir é um inibidor da transferência de cadeia da "
           "integrase que bloqueia a integração do material genético viral "
           "no genoma da célula hospedeira. A OMS recomenda-o como fármaco "
           "preferencial de primeira e de segunda linha em todas as "
           "populações, associado a tenofovir disoproxil fumarato e "
           "lamivudina numa combinação em dose fixa de toma única diária "
           "{who_hiv2021,jemalrev2024}. Os argumentos que sustentaram a "
           "recomendação foram a barreira genética elevada à resistência, a "
           "rapidez da supressão virológica e a melhor tolerabilidade face "
           "ao efavirenz, além do custo reduzido da formulação genérica."),
         P("Os dois grandes ensaios africanos confirmaram a eficácia. No "
           "NAMSAL, com 613 adultos camaroneses sem tratamento prévio, a "
           "proporção com carga viral inferior a 50 cópias por mililitro às "
           "96 semanas foi de 74% no grupo do dolutegravir e de 72% no "
           "grupo do efavirenz em dose reduzida, sem qualquer mutação de "
           "resistência ao dolutegravir, contra 17 mutações ao efavirenz "
           "{calmy2020}. No ADVANCE, conduzido na África do Sul com 1.053 "
           "participantes, a supressão manteve-se elevada às 192 semanas "
           "nos três grupos, também sem mutações significativas na "
           "integrase {sokhela2024}. Em Moçambique, um estudo transversal "
           "realizado em Gaza entre Agosto de 2021 e Fevereiro de 2022, com "
           "717 adultos transitados para o esquema com dolutegravir, "
           "encontrou falência virológica em 30,2% e resistência intermédia "
           "a alta ao dolutegravir em 19,6% dos 183 doentes genotipados, "
           "valores que sublinham a importância de verificar a carga viral "
           "antes da transição {ismael2025}."),
         P("A tolerabilidade favorável não significa ausência de efeitos "
           "adversos. O sinal de segurança que se impôs à escala global foi "
           "metabólico: ganho de peso superior ao dos esquemas anteriores, "
           "com aparecimento de excesso de peso e de obesidade em doentes "
           "que antes tinham peso normal, e consequências potenciais sobre "
           "a glicemia, o perfil lipídico e a pressão arterial "
           "{jemalrev2024,bailin2020}. É um efeito adverso de instalação "
           "lenta, que só se torna visível ao fim de meses ou anos e que os "
           "sistemas de notificação espontânea dificilmente captam, o que "
           "obriga a estratégias activas de farmacovigilância assentes em "
           "medição."),
     ]),
    ("Ganho de peso associado aos inibidores da integrase: magnitude, "
     "mecanismos e determinantes", [
         P("A magnitude do efeito foi estabelecida por ensaios "
           "randomizados. No NAMSAL, o ganho mediano de peso às 48 semanas "
           "foi de 5,0 kg no grupo do dolutegravir contra 3,0 kg no grupo "
           "do efavirenz em dose reduzida, com incidência de obesidade de "
           "12,3% e 5,4% {kouanfack2019}, subindo para 22% e 16% às 96 "
           "semanas {calmy2020}. No ADVANCE, o ganho médio às 192 semanas "
           "foi de 8,9 kg com tenofovir alafenamida associado ao "
           "dolutegravir, 5,9 kg com tenofovir disoproxil fumarato "
           "associado ao dolutegravir e 3,2 kg com o esquema contendo "
           "efavirenz, com trajectória mais acentuada nas mulheres, nos "
           "doentes que recebiam tenofovir alafenamida e nos que tinham "
           "contagem de linfócitos mais baixa no início; o ritmo de ganho "
           "abrandou depois da semana 96 {sokhela2024}. A meta-análise em "
           "rede encomendada pela OMS, que reuniu 113 publicações "
           "referentes a 73 estudos, estimou uma diferença média de 1,99 kg "
           "às 96 semanas entre esquemas com dolutegravir e esquemas com "
           "efavirenz, e identificou como preditores consistentes a "
           "contagem baixa de linfócitos e a carga viral elevada no início "
           "{kanters2022}."),
         P("Os dados de coorte, mais próximos da prática de rotina, "
           "reproduzem o sinal com amplitudes menores. Na coorte africana "
           "que segue adultos no Quénia, no Uganda, na Tanzânia e na "
           "Nigéria, os 1.474 participantes transitados para o esquema com "
           "dolutegravir tiveram 1,77 vezes o risco de atingir um índice de "
           "massa corporal igual ou superior a 25 kg/m<sup>2</sup>, e a "
           "variação média de peso passou de 0,35 kg por ano antes da "
           "transição para 1,46 kg por ano no ano seguinte {esber2022}. Na "
           "mesma coorte, 29,1% dos 1.508 participantes ganharam 5% ou mais "
           "do peso corporal após a mudança, com maior frequência nas "
           "mulheres do que nos homens, de 32,2% contra 25,2%, e nos que "
           "vinham de efavirenz {romo2023}. No Zimbabwe, entre 172 doentes "
           "que iniciaram o esquema, o ganho médio foi de 5,25 kg após uma "
           "mediana de 27 semanas, sendo menor nos que tinham contagem de "
           "linfócitos mais alta no início {kouamou2024}."),
         P("A heterogeneidade geográfica é o dado mais relevante para "
           "Moçambique. Um estudo prospectivo comparou 428 adultos do "
           "Uganda com 367 da África do Sul durante 48 semanas após a "
           "transição, com o mesmo protocolo: a variação média do peso foi "
           "de 0,6 kg e 2,9 kg, a do perímetro abdominal de 0,8 cm e 2,3 "
           "cm, e o ganho igual ou superior a 10% ocorreu em 9,8% e 18,0% "
           "dos participantes {migisha2024}. Em meio rural no Quénia, o "
           "peso aos 12 meses foi apenas 0,7 kg superior ao previsto nas "
           "mulheres e sobreponível ao previsto nos homens, com ganho "
           "estimado de 1,1 kg nos participantes com segurança alimentar e "
           "praticamente nulo nos que viviam insegurança alimentar moderada "
           "{hickey2023}. Na Namíbia, o peso aumentou 1,7 kg aos 12 meses "
           "após a mudança, com significância apenas nas mulheres "
           "{hachey2023}. No Quénia, entre 17.044 doentes sem tratamento "
           "prévio, as mulheres que iniciaram dolutegravir tiveram o maior "
           "ganho, com média de 6,1 kg aos 18 meses {bourgi2022}. No "
           "Eswatini, o aumento mediano do índice de massa corporal aos 24 "
           "meses foi de 1,09 kg/m<sup>2</sup> com dolutegravir contra 0,20 "
           "kg/m<sup>2</sup> com efavirenz, com razão de possibilidades "
           "ajustada de 2,61 para ganho excessivo {mukuna2024}."),
         P("Os mecanismos permanecem em discussão. Estudos em tecido "
           "adiposo humano e de primata mostraram que o dolutegravir e o "
           "raltegravir exercem efeitos pró-adipogénicos e pró-fibróticos e "
           "induzem resistência à insulina {gorwood2020}. Outras hipóteses "
           "apontam para interferência com a regulação central do apetite, "
           "nomeadamente através do receptor de melanocortina do tipo 4, e "
           "para penetração no tecido adiposo com efeito directo sobre a "
           "adipogénese, a fibrose e a sensibilidade à insulina "
           "{jemalrev2024}. Simultaneamente, parte do aumento observado "
           "corresponde a recuperação do peso perdido antes do tratamento, "
           "efeito de retorno à saúde tanto maior quanto mais avançada "
           "estiver a doença no início {bailin2020}. A contribuição do "
           "estilo de vida parece modesta: numa coorte sul-africana de 367 "
           "adultos seguidos durante 48 semanas, nem o consumo de fruta e "
           "de legumes, nem a frequência de refeições rápidas ou de bebidas "
           "açucaradas, nem a actividade física se associaram de forma "
           "consistente ao ganho de peso clinicamente significativo, que "
           "ocorreu em 18,0% dos participantes {tien2026}."),
     ]),
    ("Do peso à pressão arterial e às consequências cardiometabólicas", [
         P("A análise secundária do ensaio ADVANCE examinou explicitamente "
           "a pressão arterial. Ao longo de 96 semanas, a variação média da "
           "pressão sistólica foi de 1,7 mmHg no grupo com tenofovir "
           "alafenamida e dolutegravir, de -0,5 mmHg no grupo com tenofovir "
           "disoproxil fumarato e dolutegravir e de -2,1 mmHg no grupo com "
           "efavirenz, e a proporção que desenvolveu tensão arterial "
           "elevada durante o tratamento foi de 18,2%, 15,4% e 13,3%, "
           "respectivamente. O achado decisivo foi que a variação do índice "
           "de massa corporal, e não o esquema nem a função renal, "
           "explicava o aumento da pressão sistólica: o ajuste para o "
           "índice de massa corporal anulava a relação entre o esquema e a "
           "pressão arterial {mannegoehler2024}."),
         P("A confirmação em condições de rotina veio do Zimbabwe, onde "
           "foram analisados 99.969 registos de peso e 35.449 de pressão "
           "arterial de 9.487 adultos. Aos 24 meses após o início ou a "
           "mudança para dolutegravir, o ganho mediano de peso foi de 4,54 "
           "kg nas mulheres e de 3,71 kg nos homens, cerca do dobro do "
           "observado com atazanavir potenciado e mais de quatro vezes o "
           "observado com efavirenz. A prevalência de tensão arterial "
           "elevada subiu de cerca de 5% no momento da mudança para mais de "
           "20% aos 24 meses nos doentes com dolutegravir, sem alteração "
           "equivalente nos restantes esquemas, e o aumento foi tanto maior "
           "quanto maior tinha sido o ganho de peso {shamu2024}. Na "
           "Etiópia, um estudo transversal com 415 adultos em esquema com "
           "dolutegravir há pelo menos seis meses encontrou hipertensão "
           "arterial em 15,2% (IC95% 11,9-19), associada ao sexo, à duração "
           "da terapêutica, à história familiar, ao índice de massa "
           "corporal e à glicemia em jejum {jemal2025}."),
         P("O impacto estende-se ao conjunto do perfil metabólico. Na "
           "Tanzânia, entre 312 adultos em esquema com dolutegravir, a "
           "prevalência de síndrome metabólica foi de 42,3%, sendo o "
           "perímetro abdominal aumentado a componente mais frequente, "
           "presente em 73% {mirai2024}. Num estudo comparativo etíope com "
           "172 doentes, a síndrome metabólica afectou 25,6% dos tratados "
           "com dolutegravir e 11,6% dos tratados com efavirenz "
           "{jemalms2024}. Uma revisão sistemática com meta-análise estimou "
           "uma prevalência combinada de síndrome metabólica de 21,5% "
           "(IC95% 15,09-26,86) nas pessoas que vivem com VIH na África "
           "subsariana, contra 12,0% nas não infectadas {todowede2019}. A "
           "projecção a dez anos feita a partir dos dados do ADVANCE, em "
           "participantes com mais de 30 anos, apontou para risco acrescido "
           "de diabetes tipo 2 e, em menor grau, de doença cardiovascular, "
           "atribuível sobretudo ao peso ganho, com a ressalva de que as "
           "equações de risco usadas não foram validadas em população "
           "africana com VIH {mccann2021}."),
     ]),
    ("Hipertensão arterial, excesso de peso e obesidade em Moçambique", [
         P("A transição epidemiológica moçambicana está documentada por "
           "inquéritos nacionais sucessivos. A prevalência de hipertensão "
           "arterial nos adultos de 25 a 64 anos aumentou de 33,1% em 2005 "
           "para 38,9% em 2014-2015, enquanto a proporção de hipertensos "
           "conscientes do seu estado permaneceu praticamente inalterada, "
           "de 14,8% para 14,5%, e a pressão diastólica média subiu de 78,2 "
           "para 82,5 mmHg. Mesmo entre os 15 e os 24 anos, a prevalência "
           "de hipertensão em 2014-2015 foi de 13,1% (IC95% 9,8-16,4) "
           "{jessen2018}. Um inquérito domiciliário representativo das "
           "províncias de Manica e Sofala, com 4.101 respondentes, "
           "encontrou pressão arterial elevada em 15,7% das mulheres e "
           "16,1% dos homens, mas apenas 34,9% dos participantes com "
           "pressão elevada tinham tido uma medição anterior e 12,2% tinham "
           "diagnóstico prévio {matsuzaki2020}."),
         P("O excesso de peso acompanha a mesma trajectória. Entre 2005 e "
           "2014-2015, a prevalência de excesso de peso e obesidade passou "
           "de 18,3% para 30,5% nas mulheres e de 11,7% para 18,2% nos "
           "homens; a obesidade abdominal nas mulheres subiu de 9,4% para "
           "20,4%, sem variação significativa nos homens. Os valores são "
           "mais do dobro nas áreas urbanas, e já uma em cada cinco "
           "mulheres urbanas dos 18 aos 24 anos tem excesso de peso ou "
           "obesidade {fontes2019}. Num estudo com 776 adultos jovens dos "
           "18 aos 25 anos, representativo do país, a prevalência de "
           "excesso de peso ou obesidade foi mais alta nas mulheres "
           "urbanas, com 21,6% (IC95% 14,7-30,6), e a de hipertensão foi "
           "mais alta nos homens urbanos, com 25,2% (IC95% 15,9-37,6) "
           "{silva2023}."),
         P("A combinação destes dois quadros com a epidemia de VIH cria uma "
           "população em que o ganho de peso induzido por fármaco se soma a "
           "uma tendência populacional de aumento do peso e a um sistema de "
           "saúde que quase não rastreia a pressão arterial. As orientações "
           "africanas de hipertensão publicadas em 2026 insistem "
           "precisamente na integração do rastreio e do tratamento da "
           "hipertensão nos serviços que já têm contacto regular com a "
           "população, entre os quais os serviços de VIH {doku2026}, e a "
           "orientação da OMS sobre tratamento farmacológico define os "
           "limiares de intervenção a aplicar nesses contextos "
           "{who_hta2021}."),
     ]),
    ("Medição do peso, da estatura, do perímetro abdominal e da pressão "
     "arterial: definições operacionais", [
         P("O índice de massa corporal (IMC) é obtido dividindo o peso em "
           "quilogramas pelo quadrado da estatura em metros. A OMS "
           "classifica como excesso de peso um valor igual ou superior a 25 "
           "kg/m<sup>2</sup> e como obesidade um valor igual ou superior a "
           "30 kg/m<sup>2</sup>; em 2022, 2,5 mil milhões de adultos, ou "
           "43% da população adulta mundial, tinham excesso de peso e mais "
           "de 890 milhões, ou 16%, viviam com obesidade, mais do dobro da "
           "proporção registada em 1990 {who_obes}. Neste protocolo "
           "adoptam-se as categorias de baixo peso abaixo de 18,5 "
           "kg/m<sup>2</sup>, peso normal de 18,5 a 24,9 kg/m<sup>2</sup>, "
           "excesso de peso de 25,0 a 29,9 kg/m<sup>2</sup> e obesidade a "
           "partir de 30,0 kg/m<sup>2</sup>."),
         P("O perímetro abdominal informa sobre a gordura visceral de forma "
           "independente e aditiva em relação ao índice de massa corporal, "
           "razão pela qual a declaração de consenso do grupo de trabalho "
           "internacional sobre obesidade visceral propõe que seja tratado "
           "como sinal vital na prática clínica {ross2020}. A consulta de "
           "peritos da OMS fixou os pontos de corte que este protocolo "
           "adopta: risco aumentado de complicações metabólicas a partir de "
           "94 cm nos homens e de 80 cm nas mulheres, e risco "
           "substancialmente aumentado a partir de 102 cm nos homens e de "
           "88 cm nas mulheres {who_perimetro2011}. Define-se obesidade "
           "abdominal, para efeitos deste estudo, como perímetro igual ou "
           "superior a 94 cm nos homens e igual ou superior a 80 cm nas "
           "mulheres."),
         P("A técnica de medição está padronizada no manual de vigilância "
           "de factores de risco da OMS. O perímetro abdominal mede-se no "
           "ponto médio entre a margem inferior da última costela palpável "
           "e o bordo superior da crista ilíaca, no fim de uma expiração "
           "normal, com os braços relaxados e os pés juntos, com fita de "
           "tensão constante colocada directamente sobre a pele ou sobre "
           "roupa leve, horizontal à frente e atrás, lida ao 0,1 cm mais "
           "próximo e sem comprimir a pele. A estatura mede-se com "
           "estadiómetro, sem calçado nem adornos na cabeça, com os "
           "calcanhares encostados, os joelhos direitos e o olhar na "
           "horizontal, lida ao milímetro. O peso mede-se com balança "
           "colocada em superfície firme e plana, sem calçado, meias, "
           "cintos pesados nem objectos nos bolsos {who_steps}."),
         P("A pressão arterial exige cuidados equivalentes. O manual da OMS "
           "determina 15 minutos de repouso sentado com as pernas "
           "descruzadas, bexiga vazia, sem café antes ou durante a medição "
           "e sem falar, com o cotovelo apoiado, braçadeira de tamanho "
           "adequado ao perímetro do braço colocada 1 a 2 cm acima da prega "
           "do cotovelo e ao nível do coração, e três medições separadas "
           "por três minutos de repouso, calculando-se a média da segunda e "
           "da terceira {who_steps}. As orientações europeias em vigor "
           "definem hipertensão arterial no consultório como pressão "
           "sistólica igual ou superior a 140 mmHg ou pressão diastólica "
           "igual ou superior a 90 mmHg {mancia2023}, critério retomado "
           "pelas orientações africanas {doku2026}. Os aparelhos usados "
           "devem ter passado uma validação clínica segundo o protocolo "
           "universal acordado entre a associação para o avanço da "
           "instrumentação médica, a sociedade europeia de hipertensão e a "
           "organização internacional de normalização {stergiou2018}."),
     ]),
    ("Enquadramento normativo, farmacovigilância e normas de relato", [
         P("A base normativa do tratamento é a orientação consolidada da "
           "OMS, que estabelece o esquema com dolutegravir como "
           "preferencial e define o seguimento clínico e laboratorial "
           "mínimo {who_hiv2021}. Em Moçambique, a organização do "
           "seguimento é regida pelo guião nacional dos modelos "
           "diferenciados de serviços, que define os critérios de utente "
           "estável e a periodicidade da dispensa {misau_mds2023}. A "
           "vigilância de efeitos adversos de instalação lenta, como o "
           "ganho de peso, não está coberta por nenhum instrumento de "
           "notificação espontânea eficaz, o que faz dos estudos de medição "
           "directa a principal fonte de informação disponível ao nível do "
           "país."),
         P("A qualidade do registo clínico é uma condição crítica de "
           "qualquer estudo que dependa de valores iniciais documentados. "
           "Na avaliação nacional da introdução do dolutegravir pediátrico "
           "em Moçambique, 196 de 1.353 crianças, ou 14,5%, não tinham peso "
           "registado, e os autores identificaram a documentação "
           "insuficiente nos registos clínicos como um dos principais "
           "obstáculos encontrados {meque2024}. Este dado sustenta a opção, "
           "tomada neste protocolo, de verificar previamente uma amostra de "
           "processos e de fixar por escrito uma regra de decisão antes de "
           "iniciar a recolha."),
         P("O relato dos resultados seguirá a lista de verificação para "
           "estudos observacionais transversais {von2008}, e a conduta "
           "ética obedecerá à Declaração de Helsínquia na sua revisão de "
           "2024 {world2025}, que reforça a protecção dos participantes em "
           "situação de vulnerabilidade e as exigências de "
           "confidencialidade na investigação que envolve dados de saúde "
           "sensíveis."),
     ]),
]

# ----------------------------------------------------- 7. estado da arte ----
ESTADO_ARTE = [
    P("O [[quadro:estado_arte]] reúne os estudos empíricos dos últimos dez "
      "anos que mediram o peso, o perímetro abdominal ou a pressão arterial "
      "em pessoas tratadas com esquemas contendo dolutegravir, com "
      "prioridade para os conduzidos em África, e inclui os inquéritos "
      "nacionais moçambicanos que fornecem os valores de comparação "
      "populacional."),
    QUADRO("estado_arte",
           "Síntese de estudos sobre ganho de peso e pressão arterial com "
           "esquemas contendo dolutegravir e sobre factores de risco "
           "cardiometabólico em Moçambique (estado da arte)",
           ["Autor (ano)", "Local", "Desenho (n)", "Principais resultados"],
           [
               ["Kouanfack et al. (2019) {kouanfack2019}", "Camarões",
                "Ensaio randomizado (613)",
                "Ganho mediano às 48 semanas de 5,0 kg com dolutegravir e "
                "3,0 kg com efavirenz em dose reduzida; obesidade em 12,3% "
                "e 5,4%."],
               ["Calmy et al. (2020) {calmy2020}", "Camarões",
                "Ensaio randomizado, 96 semanas (613)",
                "Supressão viral de 74% e 72%; ganho mediano de 5,0 kg e "
                "3,0 kg; incidência de obesidade de 22% e 16% (p=0,043)."],
               ["Sokhela et al. (2024) {sokhela2024}", "África do Sul",
                "Ensaio randomizado, 192 semanas (1.053)",
                "Ganho médio de 8,9 kg, 5,9 kg e 3,2 kg nos três grupos; "
                "maior nas mulheres; abrandamento após a semana 96."],
               ["Manne-Goehler et al. (2024) {mannegoehler2024}",
                "África do Sul", "Análise secundária de ensaio (1.053)",
                "Tensão arterial elevada de novo em 18,2%, 15,4% e 13,3% às "
                "96 semanas; a variação do índice de massa corporal "
                "explicou o aumento da pressão sistólica."],
               ["Kanters et al. (2022) {kanters2022}", "Multinacional",
                "Revisão sistemática e meta-análise em rede (73 estudos)",
                "Diferença média de 1,99 kg (IC95% 0,85-3,09) às 96 semanas "
                "entre dolutegravir e efavirenz."],
               ["Esber et al. (2022) {esber2022}",
                "Quénia, Uganda, Tanzânia, Nigéria",
                "Coorte prospectiva (1.474 transitados)",
                "Risco 1,77 vezes maior de índice de massa corporal igual "
                "ou superior a 25 kg/m2; ganho de 0,35 kg por ano antes e "
                "1,46 kg por ano depois da transição."],
               ["Romo et al. (2023) {romo2023}",
                "Quénia, Uganda, Tanzânia, Nigéria",
                "Coorte prospectiva (1.508)",
                "Ganho igual ou superior a 5% em 29,1%; 32,2% nas mulheres "
                "e 25,2% nos homens; sem efeito sobre a adesão ou a carga "
                "viral."],
               ["Shamu et al. (2024) {shamu2024}", "Zimbabwe",
                "Coorte longitudinal (9.487)",
                "Aos 24 meses, ganho mediano de 4,54 kg nas mulheres e 3,71 "
                "kg nos homens; tensão arterial elevada de cerca de 5% para "
                "mais de 20%."],
               ["Migisha et al. (2024) {migisha2024}",
                "Uganda e África do Sul", "Coorte prospectiva (795)",
                "Variação média de peso de 0,6 kg e 2,9 kg; perímetro "
                "abdominal mais 0,8 cm e mais 2,3 cm; ganho igual ou "
                "superior a 10% em 9,8% e 18,0%."],
               ["Hickey et al. (2023) {hickey2023}", "Quénia rural",
                "Coorte retrospectiva (4.445) e prospectiva (135)",
                "Peso aos 12 meses 0,7 kg acima do previsto nas mulheres e "
                "sem alteração nos homens; ganho maior nos participantes "
                "com segurança alimentar."],
               ["Bourgi et al. (2022) {bourgi2022}", "Quénia",
                "Coorte retrospectiva (17.044)",
                "Maior ganho nas mulheres com dolutegravir, com média de "
                "6,1 kg aos 18 meses; risco acrescido com baixo peso "
                "inicial e tuberculose em tratamento."],
               ["Mukuna et al. (2024) {mukuna2024}", "Eswatini",
                "Coorte retrospectiva (316)",
                "Aumento mediano do índice de massa corporal aos 24 meses "
                "de 1,09 contra 0,20 kg/m2; razão de possibilidades "
                "ajustada de 2,61 para ganho excessivo."],
               ["Tien et al. (2026) {tien2026}", "África do Sul",
                "Coorte prospectiva, 48 semanas (367)",
                "Ganho igual ou superior a 10% em 18,0%; dieta e actividade "
                "física sem associação consistente com o ganho."],
               ["Jemal et al. (2025) {jemal2025}", "Etiópia",
                "Transversal analítico (415)",
                "Hipertensão arterial em 15,2% (IC95% 11,9-19), associada "
                "ao sexo, à duração da terapêutica e ao índice de massa "
                "corporal."],
               ["Mirai et al. (2024) {mirai2024}", "Tanzânia",
                "Transversal analítico (312)",
                "Síndrome metabólica em 42,3%; o perímetro abdominal "
                "aumentado foi a componente mais frequente, em 73%."],
               ["Jessen et al. (2018) e Fontes et al. (2019) "
                "{jessen2018,fontes2019}", "Moçambique",
                "Inquéritos nacionais (2.965 e 2.595)",
                "Hipertensão de 33,1% para 38,9% entre 2005 e 2014-2015; "
                "excesso de peso e obesidade de 18,3% para 30,5% nas "
                "mulheres; obesidade abdominal de 9,4% para 20,4%."],
           ],
           larguras=[3.4, 2.1, 3.0, 7.5],
           fonte="Elaboração própria (2026), a partir das fontes citadas."),
    P("A leitura do quadro revela três padrões. O primeiro é a consistência "
      "da direcção do efeito: em todos os desenhos, dos ensaios "
      "randomizados às coortes de rotina, o esquema contendo dolutegravir "
      "associa-se a maior ganho de peso do que os esquemas com efavirenz, e "
      "o ganho é sistematicamente superior nas mulheres. O segundo é a "
      "amplitude muito variável da magnitude, que vai de 0,6 kg em 48 "
      "semanas no Uganda {migisha2024} a 8,9 kg em 192 semanas na África do "
      "Sul {sokhela2024}, diferença que não se explica apenas pelo tempo de "
      "seguimento e que aponta para o peso inicial, a segurança alimentar e "
      "o grau de urbanização como moduladores {hickey2023}. O terceiro é a "
      "escassez de medições do perímetro abdominal e da pressão arterial: "
      "apenas três dos estudos reunidos as documentam de forma sistemática "
      "{mannegoehler2024,shamu2024,migisha2024}, embora sejam essas as "
      "variáveis que traduzem o risco cardiovascular."),
    P("A lacuna que este estudo preenche é geográfica e metodológica. Não "
      "consta do quadro nenhum estudo moçambicano sobre ganho de peso ou "
      "pressão arterial com dolutegravir, e os dois inquéritos nacionais "
      "incluídos descrevem a população geral e não os doentes em "
      "tratamento. Moçambique combina um perfil nutricional de partida "
      "provavelmente mais próximo do Uganda e do Quénia rural com uma "
      "transição nutricional urbana acelerada {fontes2019}, pelo que "
      "nenhuma das estimativas regionais existentes pode ser adoptada sem "
      "verificação. Este protocolo aplica num hospital de referência do "
      "norte do país o mesmo conjunto de medições usado nos estudos "
      "citados, permitindo comparação directa, e acrescenta o perímetro "
      "abdominal e a pressão arterial à leitura habitual do peso."),
]
ESQUEMA_TEXTO = [
    P("A [[figura:esquema]] representa a relação em estudo. Os blocos da "
      "esquerda reúnem as variáveis independentes, agrupadas em "
      "características sociodemográficas, características clínicas e de "
      "tratamento e factores de estilo de vida, que se supõe influenciarem "
      "a magnitude da alteração antropométrica e tensional. O bloco de "
      "desfecho reúne as medidas que o estudo produz. As variáveis de "
      "confundimento, ligadas ao desfecho por traço interrompido, "
      "correspondem a condições que alteram o peso ou a pressão arterial "
      "por mecanismos independentes do fármaco e que serão controladas por "
      "critérios de exclusão ou por ajuste estatístico."),
]
ESQUEMA_TITULO = ("Esquema conceptual da relação entre a exposição ao "
                  "dolutegravir e as alterações antropométricas e tensionais")
ESQUEMA = {
    "contexto": ("Adultos em tratamento anti-retroviral com esquema contendo "
                 "dolutegravir, Hospital Central de Nampula, 2027"),
    "blocos": [
        ("Características sociodemográficas",
         ["sexo", "idade", "escolaridade", "ocupação", "área de residência"]),
        ("Características clínicas e de tratamento",
         ["tempo total de tratamento anti-retroviral",
          "tempo de exposição ao dolutegravir", "esquema anterior",
          "peso e índice de massa corporal iniciais",
          "carga viral mais recente", "tuberculose em tratamento"]),
        ("Estilo de vida e contexto alimentar",
         ["actividade física", "consumo de álcool e de tabaco",
          "número de refeições por dia", "insegurança alimentar percebida"]),
    ],
    "desfecho": ("Alterações antropométricas e tensionais",
                 ["variação do peso e do índice de massa corporal",
                  "ganho igual ou superior a 10% do peso inicial",
                  "excesso de peso e obesidade",
                  "obesidade abdominal",
                  "tensão arterial elevada"]),
    "moderadores": ("Variáveis de confundimento",
                    ["gravidez ou primeiro ano após o parto",
                     "medicação anti-hipertensora em curso",
                     "co-morbilidades e medicação concomitante",
                     "baixo peso no início do esquema"]),
}
