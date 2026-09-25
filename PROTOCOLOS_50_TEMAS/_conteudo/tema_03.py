# -*- coding: utf-8 -*-
"""
TEMA 03. Controlo da pressao arterial e adesao a' terapeutica
anti-hipertensora em adultos seguidos em consultas externas na cidade de
Nampula.

Compor e validar:   python -X utf8 _motor/motor.py _conteudo/tema_03.py
Verificar fontes:   python -X utf8 _motor/refs.py verificar _conteudo/tema_03.py

ESTADO: COMPLETO E REVISTO. motor.py -> PROBLEMAS: nenhum (9.934 palavras no
corpo, 38 referencias, 86,8% de 2016-2026); refs.py verificar -> erros: 0,
1 aviso (ncd2021: autor real Zhou, colaboracao NCD-RisC).

REVISAO ADVERSARIAL (auditoria de 38 afirmacoes contra as fontes). Correccoes:
    adisa2018   35,2% e' a fraccao das RAZOES apontadas, nao dos doentes.
    mills2024   13,8% e' dado de contexto do artigo, nao resultado da
                meta-analise; a maior reducao sistolica e' partilhada por
                farmaceuticos e agentes comunitarios (pares: farmaceuticos >
                enfermeiros e medicos).
    cavagna2021 retirado o denominador derivado (2.123); o 23,3% usado no
                calculo da amostra fica declarado como complemento de 76,7%.
    nakwafila2022 retirado o superlativo (OR 8,49 > OR 5,44).
    nogueirasilva2016 a fonte fala de redaccao e formato, nao de "termos de
                frequencia".
    Coerencia: coluna Objectivo do quadro de variaveis alinhada com os
                modelos (crencas 4 e 5; comorbilidades e tempo de diagnostico
                tambem no 5; n.o de anti-hipertensores 1 e 4); modelo do
                objectivo 5 explicitado com 12 parametros; ponto de corte da
                adesao escrito no quadro; aparelho declarado validado.
    Extensao: corpo de 10.255 para 9.934 palavras, por remocao de repeticoes
                (introducao/revisao/estado da arte, cronograma, metodologia).

NUMEROS CONFIRMADOS NAS FONTES (lidos com refs.py resumo ou WebFetch):
    jessen2018   prevalencia 38,9% (25-64 anos, 2014-2015; 33,1% em 2005);
                 conhecimento 14,5%; tratamento entre os que sabem 50,1%;
                 controlo entre os tratados 44,5%; PAS media 134,6 mmHg;
                 PAD media 82,5 mmHg.
    aminde2025   nao adesao 43,9% (IC95% 39,2-48,6), 95 estudos, 34.102
                 adultos, 27 paises; controlo da PA na Africa subsariana
                 ~10%; determinantes: numero de comprimidos, custo, efeitos
                 adversos, comorbilidades.
    apostolou2026 adesao agregada aos anti-hipertensores 51% (IC95% 44-58),
                 312 estudos, 108.014 participantes, 28 paises;
                 auto-monitorizacao da PA 28%; escolaridade, auto-eficacia
                 e apoio social como determinantes transversais.
    muchanga2026 98 estudos, 27 paises africanos; hipertensao em 18;
                 escala de Morisky de 8 itens em 50 estudos; so' 15,3%
                 relataram validacao ou adaptacao local; adesao de 0% a
                 96,8%.
    commodoremensa2023 50 estudos (44 em hipertensao); alfa de Cronbach
                 0,75; subescala de toma da medicacao com melhor desempenho.
    nakwafila2022 Namibia, 400 doentes, Hill-Bone; 87,7% com boa adesao;
                 medicacao suficiente ate' a' consulta seguinte (OR 5,44),
                 falta de apoio de familia/amigos (OR 0,11), comparecimento
                 nas consultas (OR 8,49).
    nogueirasilva2016 traducao e adaptacao cultural da escala de Hill-Bone
                 para portugues europeu; carece de validacao posterior.
    bay2019      Mocambique (Hospital Geral de Mavalane, Maputo), 1.911
                 hipertensos; sem protocolos clinicos; disponibilidade media
                 de medicamentos de 28%.
    attaei2017   4 classes disponiveis em 13% das comunidades de rendimento
                 baixo (94% nas de rendimento alto); 31% dos agregados sem
                 capacidade para pagar dois medicamentos; controlo com OR
                 ajustado 2,06 (IC95% 1,69-2,50).
    sarfo2018    Gana, 5 hospitais, 2.870 doentes; 42,3% controlados; mau
                 controlo com cuidados terciarios ORa 2,47, ma adesao (escala
                 de Hill-Bone) ORa 1,21 por 5 pontos, dificuldade em obter
                 medicamentos ORa 1,24, n.o de anti-hipertensores ORa 1,32.
    sibomana2019 Ruanda, 112 doentes e 30 clinicos; adesao elevada em 77%, so'
                 29% na meta; 43% dos clinicos escolheram diuretico da ansa.
    sorato2022   Etiopia, 406 doentes; controlo 17,5%; 66,5% em combinacao;
                 custo anual 11,39 USD; comportavel para 22,4%; ORa 3,49.
    cavagna2021  12 paises, 29 hospitais, 2.198 doentes; 96,6% medicados;
                 76,7% dos tratados nao controlados, 28,3% destes com
                 180/110 mmHg ou mais; medicina tradicional OR 1,72.
    niriayo2024  Etiopia, 282 doentes; 67,4% nao controlados; inercia
                 terapeutica em 72% destes.
    yousuf2025   Etiopia, 364 doentes; adesao 59,94%; distancia < 10 km ORa
                 4,60; apoio social 1,86; seguro 2,00; 3+ medicamentos 0,28.
    ryabinina2026 Gana, 292 doentes; adesao 67,8%; conhecimento dos
                 medicamentos ORa 4,40, posologia 5,27, disponibilidade 4,16.
    adisa2018    Nigeria, 605 doentes; adesao 8,9% (54 doentes); adesao ao
                 estilo de vida 6,0%; esquecimento como motivo mais frequente,
                 com 404 mencoes, 35,2% das razoes; sistolica media
                 149,6 mmHg no primeiro contacto.
    hing2019     Malawi, 75 entrevistas; adesao pior na hipertensao do que no
                 HIV, atribuida ao custo dos anti-hipertensores.
    alfian2022   Indonesia, 440 doentes; 41,8% nao aderentes; compreensao
                 OR 0,89; resposta emocional OR 0,93.
    gupta2016    questionarios sobrestimam a adesao e tem baixa
                 especificidade; registos de farmacia uteis mas limitados.
    ncd2021      2019: 626 M mulheres e 652 M homens (30-79 anos); 59%/49%
                 diagnosticados, 47%/38% tratados, 23%/18% controlados.
    mills2024    100 ensaios, 116 comparacoes, 90.474 participantes; 13,8%
                 controlados no mundo (dado de contexto, nao resultado);
                 farmaceuticos -7,3 mmHg sistolica (IC95% -9,1 a -5,6) e
                 -3,9 mmHg diastolica (-5,2 a -2,5); agentes comunitarios
                 -7,1 mmHg; farmaceuticos significativamente melhores do que
                 enfermeiros e medicos nas comparacoes emparelhadas.
    who2023hta   1 em cada 3 adultos; 650 milhoes -> 1,3 mil milhoes
                 (1990-2019); 4 em 5 sem tratamento adequado; 76 milhoes de
                 mortes evitaveis 2023-2050.
    who2021hta   limiar 140/90 (130-139 sistolica em alto risco); alvo
                 <140/90 e sistolica <130 em alto risco; 3 classes de
                 1.a linha; combinacao em comprimido unico; seguimento mensal
                 ate' a meta e depois de 3 a 6 meses (lido no NCBI Bookshelf).
    misaudnt2020 (texto integral do PDF lido e pesquisado na revisao)
                 prevalencia 33,1% -> 39% (STEPS 2005/2015); metas 2029: -10%
                 de hipertensao e "pelo menos 46,6% das pessoas com HTA e
                 Diabetes com conhecimento sobre a sua condicao clinica"
                 (base 16,6%); "13% das mortes sao causadas por Hipertensao...
                 e mais de metade das doencas cardiacas, acidentes vasculares
                 cerebrais e falencias cardiacas"; cardiopatia isquemica e
                 ictus como 1.a e 2.a causas de morte; indicador de resposta
                 do sector "% de diabeticos e hipertensos tratados com sucesso
                 (controlados)"; integracao dos medicamentos na lista de
                 medicamentos essenciais; kit do doente cronico (niveis
                 primario e secundario) com esfigmomanometro de bracadeira
                 media e grande, balanca, estetoscopio, fita metrica e
                 estadiometro; conhecimento do diagnostico 15,2% urbano e
                 7,9% rural nos homens, 33,2% e 8,9% nas mulheres; "Cada 1$
                 investido no controlo da Hipertensao e Diabetes gera um
                 retorno de 3.29$".
    jessensal2018 3.116 participantes; 25,9% adicionam sal a' comida
                 preparada; 16,9% desconhecem o malefico do sal.
    madede2024   24 entrevistas; formacao centrada nas doencas infecciosas;
                 falta de equipamento, consumiveis e medicamentos.

DEFEITO DO MOTOR CONTORNADO: o validador extrai 'IC95' de 'IC95%' e assinala-o
como sigla nao listada; a lista contem a forma correcta 'IC95%'.
"""
from blocos import (CAMPO, ESCALA, FORMULA, H3, LISTA, NOTA, P, PERG,
                    QUADRO, TABELA)

NUMERO = 3
SLUG = "Controlo_PA_Adesao_Anti_Hipertensora_Nampula"
TITULO = ("Controlo da pressão arterial e adesão à terapêutica "
          "anti-hipertensora em adultos seguidos em consultas externas na "
          "cidade de Nampula, de Abril a Junho de 2027")
DESENHO = ("Transversal analítico, multicêntrico, com medição da pressão "
           "arterial, revisão da prescrição e questionário de adesão")

AUTOR = "[Nome do(a) estudante]"
ORIENTADOR = "[Nome e grau académico do(a) orientador(a)]"

# ---------------------------------------------------------------- resumo --
RESUMO = (
    "A hipertensão arterial é a doença crónica não transmissível mais "
    "frequente em Moçambique e a sua prevalência continua a aumentar, mas o "
    "resultado do tratamento nas consultas externas é pouco conhecido: não "
    "existe estimativa da proporção de doentes que atinge a meta tensional na "
    "cidade de Nampula, nem do nível de adesão ao tratamento ou dos factores "
    "que o condicionam. O estudo tem como objectivo avaliar o controlo da "
    "pressão arterial e a adesão à terapêutica anti-hipertensora em adultos "
    "seguidos em consultas externas na cidade de Nampula, entre Abril e Junho "
    "de 2027. Trata-se de um estudo transversal analítico, multicêntrico e de "
    "abordagem quantitativa, a realizar em 483 adultos com hipertensão "
    "diagnosticada e terapêutica prescrita há pelo menos três meses, "
    "seleccionados por amostragem aleatória sistemática à chegada à consulta "
    "em três unidades sanitárias da cidade. A pressão arterial será medida "
    "com aparelho oscilométrico de braço, após cinco minutos de repouso, em "
    "três leituras, considerando-se controlada quando a média da segunda e da "
    "terceira leituras for inferior a 140 milímetros de mercúrio de pressão "
    "sistólica e inferior a 90 milímetros de mercúrio de pressão diastólica. "
    "A adesão será medida por uma escala validada para a hipertensão, "
    "adaptada e traduzida para emakhuwa, e complementada pela revisão da "
    "prescrição e das datas de levantamento; um questionário aplicado por "
    "entrevista recolherá os dados sociodemográficos, o custo suportado com "
    "os medicamentos, a sua disponibilidade na unidade sanitária, os efeitos "
    "adversos percebidos e as crenças sobre a doença. A análise incluirá "
    "estatística descritiva, testes de associação e regressão logística "
    "multivariável, com nível de significância de cinco por cento. Espera-se "
    "estimar a proporção de doentes controlados, hierarquizar as barreiras à "
    "adesão e distinguir o que pode ser resolvido por aconselhamento "
    "farmacêutico do que exige decisões sobre o abastecimento e a prescrição."
)
PALAVRAS_CHAVE = ["adesão à medicação", "hipertensão", "Moçambique",
                  "pressão arterial"]
ABSTRACT = (
    "Arterial hypertension is the most frequent chronic non-communicable "
    "disease in Mozambique and its prevalence keeps rising, yet the outcome "
    "of treatment in outpatient clinics is poorly known: there is no estimate "
    "of the proportion of patients reaching the blood pressure target in the "
    "city of Nampula, nor of the level of treatment adherence or of the "
    "factors that shape it. This study aims to assess blood pressure control "
    "and adherence to antihypertensive therapy among adults followed in "
    "outpatient clinics in the city of Nampula between April and June 2027. "
    "It is an analytical, multicentre cross-sectional study with a "
    "quantitative approach, to be carried out among 483 adults with diagnosed "
    "hypertension and treatment prescribed for at least three months, "
    "selected by systematic random sampling on arrival at the clinic in three "
    "health facilities of the city. Blood pressure will be measured with an "
    "upper-arm oscillometric device, after five minutes of rest, in three "
    "readings, and will be considered controlled when the mean of the second "
    "and third readings is below 140 millimetres of mercury systolic and "
    "below 90 millimetres of mercury diastolic. Adherence will be measured "
    "with a scale validated for hypertension, adapted and translated into "
    "Emakhuwa, and complemented by review of the prescription and of the "
    "dispensing dates; an interviewer-administered questionnaire will collect "
    "sociodemographic data, the cost borne by the patient, medicine "
    "availability at the facility, perceived adverse effects and beliefs "
    "about the illness. The analysis will include descriptive statistics, "
    "association tests and multivariable logistic regression, with a "
    "significance level of five per cent. The study is expected to estimate "
    "the proportion of controlled patients, to rank the barriers to adherence "
    "and to separate what can be solved by pharmaceutical counselling from "
    "what requires decisions on medicine supply and prescribing."
)
KEYWORDS = ["blood pressure", "hypertension", "medication adherence",
            "Mozambique"]

ABREVIATURAS = [
    ("CIBS-UniLúrio", "Comité Institucional de Bioética para a Saúde da "
                      "Universidade Lúrio"),
    ("DNT", "doenças não transmissíveis"),
    ("HCN", "Hospital Central de Nampula"),
    ("HEARTS", "pacote técnico da Organização Mundial da Saúde para a gestão "
               "das doenças cardiovasculares nos cuidados de saúde primários"),
    ("IC95%", "intervalo de confiança a 95%"),
    ("IVC", "índice de validade de conteúdo"),
    ("MISAU", "Ministério da Saúde"),
    ("OMS", "Organização Mundial da Saúde"),
    ("OR", "odds ratio (razão de possibilidades)"),
    ("ORa", "odds ratio ajustado"),
    ("RP", "razão de prevalências"),
    ("SDSMAS", "Serviço Distrital de Saúde, Mulher e Acção Social"),
    ("SPSS", "Statistical Package for the Social Sciences"),
    ("STEPS", "abordagem passo a passo da Organização Mundial da Saúde para a "
              "vigilância dos factores de risco das doenças crónicas"),
    ("STROBE", "Strengthening the Reporting of Observational Studies in "
               "Epidemiology"),
]

# ------------------------------------------------------------ referencias --
# Todas geradas por _motor/refs.py (pmid, doi ou web); nada escrito à mão.
FONTES = {
    "jessen2018": "Jessen N, Damasceno A, Silva-Matos C, Tuzine E, Madede T, Mahoque R, et al. Hypertension in Mozambique: trends between 2005 and 2015. J Hypertens. 2018;36(4):779-784. doi:10.1097/HJH.0000000000001618. PMID: 29210894.",
    "aminde2025": "Aminde LN, Agbor VN, Fongwen NT, Ngwasiri CA, Nkoke C, Nji MA, et al. High Burden and Trend in Nonadherence to Blood Pressure-Lowering Medications: Meta-Analysis of Data From Over 34 000 Adults With Hypertension in Sub-Saharan Africa. J Am Heart Assoc. 2025;14(9):e037555. doi:10.1161/JAHA.124.037555. PMID: 40314353.",
    "apostolou2026": "Apostolou A, Simfukwe R, Saint A, Mushani B, Chekhchar H, Aovare P, et al. Adherence to medications, lifestyle advice, and self-monitoring for type 2 diabetes and hypertension in sub-Saharan Africa: A systematic review, meta-analysis, and interactive network analysis. PLoS Med. 2026;23(8):e1005189. doi:10.1371/journal.pmed.1005189. PMID: 42546023.",
    "muchanga2026": "Muchanga IJ, Midão L, Mazuze A, Melo D, Alcântara L, Figueiredo T, et al. Mapping medication adherence tools in Africa: a scoping review. BMJ Open. 2026;16(9):e112898. doi:10.1136/bmjopen-2025-112898. PMID: 42749368.",
    "commodoremensa2023": "Commodore-Mensah Y, Delva S, Ogungbe O, Smulcer LA, Rives S, Dennison Himmelfarb CR, et al. A Systematic Review of the Hill-Bone Compliance to Blood Pressure Therapy Scale. Patient Prefer Adherence. 2023;17:2401-2420. doi:10.2147/PPA.S412198. PMID: 37790863.",
    "nakwafila2022": "Nakwafila O, Mashamba-Thompson T, Godi A, Sartorius B. A Cross-Sectional Study on Hypertension Medication Adherence in a High-Burden Region in Namibia: Exploring Hypertension Interventions and Validation of the Namibia Hill-Bone Compliance Scale. Int J Environ Res Public Health. 2022;19(7). doi:10.3390/ijerph19074416. PMID: 35410095.",
    "nogueirasilva2016": "Nogueira-Silva L, Sá-Sousa A, Lima MJ, Monteiro A, Dennison-Himmelfarb C, Fonseca JA. Translation and cultural adaptation of the Hill-Bone Compliance to High Blood Pressure Therapy Scale to Portuguese. Rev Port Cardiol. 2016;35(2):93-7. doi:10.1016/j.repc.2015.07.013. PMID: 26852304.",
    "kim2000": "Kim MT, Hill MN, Bone LR, Levine DM. Development and testing of the Hill-Bone Compliance to High Blood Pressure Therapy Scale. Prog Cardiovasc Nurs. 2000;15(3):90-6. doi:10.1111/j.1751-7117.2000.tb00211.x. PMID: 10951950.",
    "bay2019": "Bay N, Juga E, Macuacua C, João J, Costa M, Stewart S, et al. Assessment of care provision for hypertension at the emergency Department of an Urban Hospital in Mozambique. BMC Health Serv Res. 2019;19(1):975. doi:10.1186/s12913-019-4820-8. PMID: 31852481.",
    "attaei2017": "Attaei MW, Khatib R, McKee M, Lear S, Dagenais G, Igumbor EU, et al. Availability and affordability of blood pressure-lowering medicines and the effect on blood pressure control in high-income, middle-income, and low-income countries: an analysis of the PURE study data. Lancet Public Health. 2017;2(9):e411-e419. doi:10.1016/S2468-2667(17)30141-X. PMID: 29253412.",
    "adisa2018": "Adisa R, Ilesanmi OA, Fakeye TO. Treatment adherence and blood pressure outcome among hypertensive out-patients in two tertiary hospitals in Sokoto, Northwestern Nigeria. BMC Cardiovasc Disord. 2018;18(1):194. doi:10.1186/s12872-018-0934-x. PMID: 30340528.",
    "sibomana2019": "Sibomana JP, McNamara RL, Walker TD. Patient, clinician and logistic barriers to blood pressure control among adult hypertensives in rural district hospitals in Rwanda: a cross-sectional study. BMC Cardiovasc Disord. 2019;19(1):231. doi:10.1186/s12872-019-1203-3. PMID: 31638907.",
    "cavagna2021": "Cavagna P, Takombe JL, Damorou JM, Kouam Kouam C, Diop IB, Ikama SM, et al. Blood pressure-lowering medicines implemented in 12 African countries: the cross-sectional multination EIGHT study. BMJ Open. 2021;11(12):e049632. doi:10.1136/bmjopen-2021-049632. PMID: 34857562.",
    "sorato2022": "Sorato MM, Davari M, Kebriaeezadeh A, Sarrafzadegan N, Shibru T. Antihypertensive prescribing pattern, prescriber adherence to ISH 2020 guidelines, and implication of outpatient drug price on blood pressure control at selected hospitals in Southern Ethiopia. Eur J Clin Pharmacol. 2022;78(9):1487-1502. doi:10.1007/s00228-022-03352-9. PMID: 35708747.",
    "hing2019": "Hing M, Hoffman RM, Seleman J, Chibwana F, Kahn D, Moucheraud C. 'Blood pressure can kill you tomorrow, but HIV gives you time': illness perceptions and treatment experiences among Malawian individuals living with HIV and hypertension. Health Policy Plan. 2019;34(Supplement_2):ii36-ii44. doi:10.1093/heapol/czz112. PMID: 31723966.",
    "gupta2016": "Gupta P, Patel P, Horne R, Buchanan H, Williams B, Tomaszewski M. How to Screen for Non-Adherence to Antihypertensive Therapy. Curr Hypertens Rep. 2016;18(12):89. doi:10.1007/s11906-016-0697-7. PMID: 27889904.",
    "ncd2021": "NCD Risk Factor Collaboration (NCD-RisC). Worldwide trends in hypertension prevalence and progress in treatment and control from 1990 to 2019: a pooled analysis of 1201 population-representative studies with 104 million participants. Lancet. 2021;398(10304):957-980. doi:10.1016/S0140-6736(21)01330-1. PMID: 34450083.",
    "unger2020": "Unger T, Borghi C, Charchar F, Khan NA, Poulter NR, Prabhakaran D, et al. 2020 International Society of Hypertension Global Hypertension Practice Guidelines. Hypertension. 2020;75(6):1334-1357. doi:10.1161/HYPERTENSIONAHA.120.15026. PMID: 32370572.",
    "mills2024": "Mills KT, O'Connell SS, Pan M, Obst KM, He H, He J. Role of Health Care Professionals in the Success of Blood Pressure Control Interventions in Patients With Hypertension: A Meta-Analysis. Circ Cardiovasc Qual Outcomes. 2024;17(8):e010396. doi:10.1161/CIRCOUTCOMES.123.010396. PMID: 39027934.",
    "who2023hta": "World Health Organization. Global report on hypertension: the race against a silent killer [Internet]. Geneva: World Health Organization; 2023 [citado 2026 Set 19]. Disponível em: https://www.who.int/publications/i/item/9789240081062",
    "who2021hta": "World Health Organization. Guideline for the pharmacological treatment of hypertension in adults [Internet]. Geneva: World Health Organization; 2021 [citado 2026 Set 19]. Disponível em: https://www.who.int/publications/i/item/9789240033986",
    "whohearts2020": "World Health Organization. HEARTS technical package for cardiovascular disease management in primary health care: risk-based CVD management [Internet]. Geneva: World Health Organization; 2020 [citado 2026 Set 19]. Disponível em: https://www.who.int/publications/i/item/9789240001367",
    "misaudnt2020": "Ministério da Saúde (Moçambique). Plano Estratégico Multissectorial de Prevenção e Controlo das Doenças Não Transmissíveis 2020-2029 [Internet]. Maputo: MISAU; 2020 [citado 2026 Set 19]. Disponível em: https://extranet.who.int/ncdccs/Data/MOZ_B3_s21_Plano%20Estrat%C3%A9gico%20Multissetorial%20de%20Prevencao%20e%20Controlo%20das%20DNTs%202020-2029%20FINALISSIMA.pdf",
    "sarfo2018": "Sarfo FS, Mobula LM, Burnham G, Ansong D, Plange-Rhule J, Sarfo-Kantanka O, et al. Factors associated with uncontrolled blood pressure among Ghanaians: Evidence from a multicenter hospital-based study. PLoS One. 2018;13(3):e0193494. doi:10.1371/journal.pone.0193494. PMID: 29554106.",
    "yousuf2025": "Yousuf J, Roba KT, Ahmed N, Belsty T, Wondimneh F, Daba L, et al. Antihypertensive medication adherence and associated factors among adult hypertensive patients at public hospitals in eastern Ethiopia: A Cross-sectional study. PLoS One. 2025;20(5):e0322655. doi:10.1371/journal.pone.0322655. PMID: 40435367.",
    "ryabinina2026": "Ryabinina O, Addo FO, Thomford NE, Zumesew F, Debrah AA, Nsiah P, et al. Antihypertensive medication adherence and associated risk factors among adults with hypertension: a cross-sectional study in a teaching hospital, Ghana. BMC Cardiovasc Disord. 2026;26(1):156. doi:10.1186/s12872-025-05410-3. PMID: 41699474.",
    "alfian2022": "Alfian SD, Annisa N, Perwitasari DA, Coelho A, Abdulah R. The role of illness perceptions on medication nonadherence among patients with hypertension: A multicenter study in indonesia. Front Pharmacol. 2022;13:985293. doi:10.3389/fphar.2022.985293. PMID: 36225558.",
    "broadbent2006": "Broadbent E, Petrie KJ, Main J, Weinman J. The brief illness perception questionnaire. J Psychosom Res. 2006;60(6):631-7. doi:10.1016/j.jpsychores.2005.10.020. PMID: 16731240.",
    "broadbent2015": "Broadbent E, Wilkes C, Koschwanez H, Weinman J, Norton S, Petrie KJ. A systematic review and meta-analysis of the Brief Illness Perception Questionnaire. Psychol Health. 2015;30(11):1361-85. doi:10.1080/08870446.2015.1070851. PMID: 26181764.",
    "schutte2022": "Schutte AE, Kollias A, Stergiou GS. Blood pressure and its variability: classic and novel measurement techniques. Nat Rev Cardiol. 2022;19(10):643-654. doi:10.1038/s41569-022-00690-0. PMID: 35440738.",
    "vonelm2007": "von Elm E, Altman DG, Egger M, Pocock SJ, Gøtzsche PC, Vandenbroucke JP. The Strengthening the Reporting of Observational Studies in Epidemiology (STROBE) statement: guidelines for reporting observational studies. Lancet. 2007;370(9596):1453-7. doi:10.1016/S0140-6736(07)61602-X. PMID: 18064739.",
    "helsinki2025": "World Medical Association. World Medical Association Declaration of Helsinki: Ethical Principles for Medical Research Involving Human Participants. JAMA. 2025;333(1):71-74. doi:10.1001/jama.2024.21972. PMID: 39425955.",
    "peduzzi1996": "Peduzzi P, Concato J, Kemper E, Holford TR, Feinstein AR. A simulation study of the number of events per variable in logistic regression analysis. J Clin Epidemiol. 1996;49(12):1373-9. doi:10.1016/s0895-4356(96)00236-3. PMID: 8970487.",
    "tamhane2016": "Tamhane AR, Westfall AO, Burkholder GA, Cutter GR. Prevalence odds ratio versus prevalence ratio: choice comes with consequences. Stat Med. 2016;35(30):5730-5735. doi:10.1002/sim.7059. PMID: 27460748.",
    "madede2024": "Madede T, Mavume Mangunyane E, Munguambe K, Govo V, Beran D, Levitt N, et al. Human resources challenges in the management of diabetes and hypertension in Mozambique. PLoS One. 2024;19(3):e0297676. doi:10.1371/journal.pone.0297676. PMID: 38551894.",
    "almanasreh2019": "Almanasreh E, Moles R, Chen TF. Evaluation of methods used for estimating content validity. Res Social Adm Pharm. 2019;15(2):214-221. doi:10.1016/j.sapharm.2018.03.066. PMID: 29606610.",
    "jessensal2018": "Jessen N, Santos A, Damasceno A, Silva-Matos C, Severo M, Padrão P, et al. Knowledge and behaviors regarding salt intake in Mozambique. Eur J Clin Nutr. 2018;72(12):1690-1699. doi:10.1038/s41430-018-0125-y. PMID: 29588530.",
    "niriayo2024": "Niriayo YL, Girmay S, Tesfay N, Gidey K, Asgedom SW. Therapeutic inertia and contributing factors among ambulatory patients with hypertension. BMC Cardiovasc Disord. 2024;24(1):523. doi:10.1186/s12872-024-04109-1. PMID: 39333861.",
}
SEMINAIS = {
    "kim2000": "Artigo original da escala de Hill-Bone de adesão à "
               "terapêutica anti-hipertensora (instrumento usado no estudo).",
    "broadbent2006": "Artigo original do questionário breve de percepção da "
                     "doença (instrumento usado no estudo).",
    "broadbent2015": "Revisão sistemática que reúne as propriedades "
                     "psicométricas do questionário breve de percepção da "
                     "doença em 188 estudos e 26 línguas.",
    "vonelm2007": "Declaração STROBE, norma de relato em vigor para estudos "
                  "observacionais.",
    "peduzzi1996": "Estudo de simulação que estabeleceu a regra de pelo menos "
                   "10 eventos por variável na regressão logística.",
}

# ----------------------------------------------------- 1. introducao --------
INTRODUCAO = [
    P("A hipertensão arterial é responsável por 13% das mortes e está na "
      "origem de mais de metade das doenças cardíacas, dos acidentes "
      "vasculares cerebrais e das insuficiências cardíacas {misaudnt2020}. A "
      "Organização Mundial da Saúde (OMS) estima que afecte um em cada três "
      "adultos e que o "
      "número de pessoas que vivem com a doença tenha duplicado entre 1990 e "
      "2019, de 650 milhões para 1,3 mil milhões, residindo mais de três "
      "quartos delas em países de rendimento baixo e médio {who2023hta}. A "
      "análise conjunta de 1.201 estudos populacionais detalha o percurso do "
      "doente: em 2019, entre os adultos dos 30 aos 79 anos "
      "com hipertensão, 59% das mulheres "
      "e 49% dos homens tinham diagnóstico conhecido, 47% e 38% estavam "
      "medicados e apenas 23% e 18% tinham a pressão arterial controlada "
      "{ncd2021}."),
    P("O controlo é, assim, o elo mais frágil da cadeia de cuidados. Cerca de "
      "quatro em cada cinco pessoas com hipertensão não recebem tratamento "
      "adequado e quase metade desconhece a sua condição, embora o "
      "alargamento da cobertura do tratamento pudesse evitar 76 milhões de "
      "mortes, 120 milhões de acidentes vasculares cerebrais e 79 milhões de "
      "enfartes do miocárdio entre 2023 e 2050 {who2023hta}. No conjunto do "
      "mundo, apenas 13,8% dos doentes hipertensos têm a pressão arterial "
      "controlada {mills2024}. A "
      "distância entre o que a terapêutica pode alcançar e o que alcança na "
      "prática depende sobretudo de dois elos que se cruzam na farmácia: a "
      "continuidade do acesso ao medicamento e a toma regular pelo doente."),
    P("Na África subsariana, essa distância é maior. As taxas de controlo da "
      "pressão arterial rondam os 10% e a não adesão "
      "aos anti-hipertensores foi estimada em 43,9%, com um intervalo de "
      "confiança a 95% (IC95%) de 39,2% a 48,6%, numa meta-análise de 95 "
      "estudos com 34.102 adultos de 27 países {aminde2025}. Uma revisão de 312 estudos, "
      "com 108.014 participantes de 28 países, situou a adesão agregada à "
      "medicação anti-hipertensora em 51% (IC95% 44-58) {apostolou2026}. Em "
      "consultas externas de 29 hospitais de 12 países africanos, 76,7% dos "
      "doentes medicados mantinham a pressão arterial acima da meta e "
      "28,3% destes apresentavam valores iguais ou superiores a 180/110 mmHg "
      "{cavagna2021}."),
    P("A oferta de medicamentos explica parte deste padrão. Em 626 "
      "comunidades de 20 países, apenas 13% das que pertenciam a países de "
      "rendimento baixo dispunham das quatro classes de anti-hipertensores, e "
      "viver numa comunidade com todas elas disponíveis associou-se a maior "
      "probabilidade de controlo, com *odds ratio* (OR) ajustado de 2,06 "
      "(IC95% 1,69-2,50) {attaei2017}. O custo e a ruptura de stock deixam, "
      "por isso, de ser um pormenor logístico e passam a ser determinantes "
      "clínicos."),
    P("Em Moçambique, o inquérito nacional de factores de risco de doenças não "
      "transmissíveis (DNT), conduzido segundo a abordagem passo a passo da "
      "OMS (STEPS), mostrou que a prevalência da hipertensão nos adultos dos "
      "25 aos 64 anos subiu de 33,1% em 2005 para 38,9% em 2014-2015, "
      "enquanto o conhecimento do diagnóstico se manteve em 14,5% e o "
      "tratamento entre os que conheciam o diagnóstico em 50,1%; entre os "
      "tratados, 44,5% tinham a pressão arterial controlada e a pressão "
      "diastólica média subiu de 78,2 para 82,5 mmHg {jessen2018}. O Plano "
      "Estratégico Multissectorial de Prevenção e Controlo das DNT 2020-2029 "
      "assume que a cardiopatia isquémica e o acidente vascular cerebral são "
      "a primeira e a segunda causas de morte no país, tendo a hipertensão "
      "como principal factor de risco, e fixa como metas até 2029 a redução "
      "de 10% na prevalência da doença e o aumento para 46,6% da proporção de "
      "pessoas com hipertensão ou diabetes que conhecem a sua condição "
      "clínica, a partir de 16,6% {misaudnt2020}."),
    P("As condições em que o tratamento é prestado no país limitam o que se "
      "pode esperar do doente. Num levantamento de 30 dias no serviço de "
      "urgência de um hospital geral de Maputo, que incluiu 1.911 doentes "
      "hipertensos, não existiam protocolos clínicos nem algoritmos de "
      "estratificação do risco e a disponibilidade média dos medicamentos era "
      "de 28% {bay2019}. A formação orientada para as doenças "
      "infecciosas e a falta de equipamento, consumíveis e medicamentos foram "
      "também apontadas por gestores e profissionais moçambicanos "
      "{madede2024}. Atribuir o mau controlo apenas ao comportamento do "
      "doente é, neste contexto, uma leitura incompleta."),
    P("Na cidade de Nampula, no norte do país, as consultas externas de "
      "doentes crónicos do Hospital Central de Nampula (HCN) e das unidades "
      "sanitárias urbanas acompanham adultos hipertensos que levantam os "
      "medicamentos nas respectivas farmácias, mas não se encontrou nenhum "
      "estudo publicado que tenha medido a proporção destes doentes que atinge "
      "a meta tensional, o seu nível de adesão ou os factores que os "
      "condicionam. A lacuna é tanto mais relevante quanto as intervenções "
      "conduzidas por farmacêuticos figuram entre as que produzem maior "
      "redução da pressão sistólica, de 7,3 mmHg (IC95% 5,6-9,1), "
      "significativamente acima da obtida por enfermeiros e por médicos "
      "{mills2024}. O presente "
      "protocolo propõe um estudo transversal analítico, a realizar entre "
      "Abril e Junho de 2027, que junta a medição padronizada da pressão "
      "arterial, a revisão da prescrição e um questionário de adesão, para "
      "estimar a proporção de doentes controlados e identificar os factores "
      "associados ao mau controlo e à baixa adesão."),
]

# ----------------------------------------------------- 2. problema ----------
PROBLEMA = [
    P("O problema que motiva o estudo é a ausência de informação local sobre o "
      "resultado do tratamento anti-hipertensor nas consultas externas da "
      "cidade de Nampula. A única estimativa nacional disponível, de "
      "2014-2015, indica que 44,5% dos adultos tratados tinham a pressão "
      "arterial controlada {jessen2018}, mas provém de um inquérito "
      "populacional e não das unidades sanitárias, onde os valores observados "
      "noutros países africanos se situam entre 17,5% e 42,3% "
      "{sarfo2018,sibomana2019,sorato2022}. Nas unidades sanitárias de "
      "Nampula não existe registo "
      "agregado da proporção de doentes que atinge a meta tensional, e a "
      "adesão é avaliada de forma informal, pela pergunta sobre comprimidos "
      "esquecidos, sem instrumento estruturado nem cruzamento com o registo de "
      "levantamentos."),
    P("As consequências do mau controlo são clínicas e económicas. A "
      "hipertensão não controlada é o principal factor de risco das duas "
      "primeiras causas de morte no país, a cardiopatia isquémica e o acidente "
      "vascular cerebral {misaudnt2020}, e cada agravamento obriga a consultas "
      "adicionais, a esquemas com mais medicamentos e, quando surge a "
      "complicação, a internamento. A responsabilidade não é só do doente: "
      "num hospital etíope, 72% dos doentes descontrolados não viram a "
      "terapêutica iniciada nem intensificada apesar de a meta não "
      "estar atingida {niriayo2024}. Sem saber quantos doentes estão "
      "descontrolados "
      "e porquê, a unidade sanitária não distingue o problema de adesão do "
      "problema de prescrição nem do problema de abastecimento."),
    P("O que falta saber é, portanto, de três ordens. Primeiro, que proporção "
      "dos adultos seguidos nestas consultas atinge a meta tensional, medida "
      "com um procedimento padronizado e não com o aparelho e a técnica "
      "disponíveis em cada dia. Segundo, qual é o nível de adesão medido com "
      "um instrumento validado, sabendo que os questionários tendem a "
      "sobrestimar a adesão e têm baixa especificidade diagnóstica "
      "{gupta2016} e que, em África, apenas 15,3% dos estudos que os usaram "
      "descreveram validação ou adaptação local do instrumento "
      "{muchanga2026}. Terceiro, que factores, entre o número de medicamentos "
      "prescritos, o custo suportado, a disponibilidade na farmácia, o "
      "esquecimento e as crenças sobre a doença, pesam mais nesta população, "
      "de modo a que o aconselhamento farmacêutico deixe de ser genérico e "
      "passe a ser dirigido."),
]
PERGUNTA = ("Qual é a proporção de adultos hipertensos seguidos em consultas "
            "externas na cidade de Nampula que atinge a meta tensional e de "
            "que forma a adesão à terapêutica, o número de medicamentos "
            "prescritos, o custo suportado e as crenças sobre a doença se "
            "associam ao mau controlo da pressão arterial?")
DELIMITACAO = [
    P("O estudo decorre nas consultas externas de doentes crónicos de três "
      "unidades sanitárias da cidade de Nampula, o HCN e duas unidades "
      "sanitárias urbanas com maior volume de consultas de hipertensão "
      "[confirmar junto do Serviço Distrital de Saúde, Mulher e Acção Social "
      "(SDSMAS) da Cidade de Nampula quais são as duas unidades com maior "
      "volume e qual a designação oficial de cada consulta], e abrange os "
      "adultos com 18 ou mais anos com diagnóstico de hipertensão arterial "
      "registado no processo ou no cartão do doente crónico e com terapêutica "
      "anti-hipertensora prescrita há pelo menos três meses, que comparecem à "
      "consulta entre 1 de Abril e 30 de Junho de 2027. O objecto de estudo é "
      "o controlo da pressão arterial no dia da consulta, medido com "
      "esfigmomanómetro segundo um procedimento padronizado, e a adesão à "
      "terapêutica, medida por escala validada e complementada pela revisão da "
      "prescrição e das datas de levantamento."),
    P("Ficam fora do âmbito os menores de 18 anos, as grávidas e as puérperas "
      "até seis semanas, os "
      "doentes com hipertensão diagnosticada há menos de três meses ou ainda "
      "sem prescrição, os doentes internados e os que recebem a medicação "
      "através de terceiros. O estudo não avalia a qualidade da "
      "prescrição face a uma norma clínica, não mede a pressão arterial fora "
      "do consultório, não confirma a toma por doseamento dos fármacos no "
      "sangue ou na urina e não testa qualquer intervenção; o programa de "
      "aconselhamento farmacêutico proposto no final é um produto derivado dos "
      "resultados e não uma componente experimental."),
]

# ----------------------------------------------------- 3. objectivos --------
OBJECTIVO_GERAL = ("Avaliar o controlo da pressão arterial e a adesão à "
                   "terapêutica anti-hipertensora em adultos seguidos em "
                   "consultas externas na cidade de Nampula, de Abril a "
                   "Junho de 2027.")
OBJECTIVOS_ESPECIFICOS = [
    "Caracterizar o perfil sociodemográfico, clínico e terapêutico dos "
    "adultos com hipertensão arterial seguidos nas consultas externas "
    "seleccionadas, incluindo o número e as classes de anti-hipertensores "
    "prescritos e o custo mensal suportado com os medicamentos.",
    "Determinar a proporção de adultos com a pressão arterial controlada, "
    "definida por pressão sistólica inferior a 140 mmHg e pressão diastólica "
    "inferior a 90 mmHg.",
    "Determinar o nível de adesão à terapêutica anti-hipertensora e descrever "
    "os motivos de não adesão referidos pelos participantes.",
    "Analisar a associação entre o mau controlo da pressão arterial e a "
    "adesão, o número de anti-hipertensores prescritos, o custo suportado e "
    "as crenças sobre a doença, com ajustamento para factores "
    "sociodemográficos e clínicos.",
    "Identificar os factores associados à baixa adesão à terapêutica "
    "anti-hipertensora.",
]

# ----------------------------------------------------- 4. hipoteses ---------
HIPOTESES_INTRO = [
    P("As hipóteses referem-se aos objectivos específicos 4 e 5 e serão "
      "testadas com um nível de significância de 5%. Formulam-se cinco pares "
      "de hipóteses, pela ordem seguinte: adesão, número de "
      "anti-hipertensores, custo suportado e crenças sobre a doença, para o "
      "controlo da pressão arterial, e indisponibilidade dos medicamentos na "
      "unidade sanitária, para a baixa adesão."),
]
HIPOTESES = [
    ("H0", "não existe associação estatisticamente significativa entre a "
           "adesão à terapêutica anti-hipertensora e o controlo da pressão "
           "arterial."),
    ("H1", "o controlo da pressão arterial é mais frequente nos adultos com "
           "boa adesão à terapêutica anti-hipertensora."),
    ("H0", "não existe associação estatisticamente significativa entre o "
           "número de anti-hipertensores prescritos e o controlo da pressão "
           "arterial."),
    ("H1", "o mau controlo da pressão arterial é mais frequente nos adultos "
           "com três ou mais anti-hipertensores prescritos."),
    ("H0", "não existe associação estatisticamente significativa entre o "
           "custo mensal suportado com os anti-hipertensores e o controlo da "
           "pressão arterial."),
    ("H1", "o mau controlo da pressão arterial é mais frequente nos adultos "
           "que pagam do próprio bolso pelo menos um dos anti-hipertensores "
           "prescritos."),
    ("H0", "não existe associação estatisticamente significativa entre as "
           "crenças sobre a doença e o controlo da pressão arterial."),
    ("H1", "percepções mais ameaçadoras da doença e menor percepção de "
           "controlo pelo tratamento associam-se a maior probabilidade de mau "
           "controlo da pressão arterial."),
    ("H0", "não existe associação estatisticamente significativa entre a "
           "indisponibilidade dos medicamentos na unidade sanitária e a baixa "
           "adesão à terapêutica anti-hipertensora."),
    ("H1", "a baixa adesão é mais frequente nos adultos que, nos três meses "
           "anteriores, não receberam na unidade sanitária pelo menos um dos "
           "anti-hipertensores prescritos."),
]
QUESTOES = [
    "Qual é o perfil sociodemográfico, clínico e terapêutico dos adultos "
    "hipertensos seguidos nestas consultas externas, quantos "
    "anti-hipertensores lhes são prescritos e que custo mensal suportam?",
    "Que proporção destes adultos tem a pressão arterial controlada no dia da "
    "consulta?",
    "Qual é o nível de adesão à terapêutica anti-hipertensora e que motivos de "
    "não adesão são referidos com mais frequência?",
]

# ----------------------------------------------------- 5. justificativa -----
JUSTIFICATIVA_INTRO = [
    P("A escolha do tema assenta em três constatações que se reforçam. A "
      "hipertensão é a doença crónica não transmissível mais frequente em "
      "Moçambique e continua a aumentar {jessen2018,misaudnt2020}; o controlo "
      "nas unidades sanitárias africanas é baixo e a não adesão atinge dois em "
      "cada cinco doentes tratados {aminde2025}; e a farmácia, que vê o doente "
      "em todos os levantamentos, é um dos serviços onde a intervenção sobre a "
      "adesão produz maior efeito na pressão arterial {mills2024}. Medir "
      "simultaneamente o resultado clínico, a adesão e as barreiras permite "
      "converter esta oportunidade em prática."),
]
JUSTIFICATIVA = {
    "cientifica": [
        P("Do ponto de vista científico, o estudo produz a primeira estimativa "
          "da proporção de adultos hipertensos com a pressão arterial "
          "controlada nas consultas externas da cidade de Nampula e "
          "relaciona-a, na mesma pessoa, com uma medida estruturada de adesão, "
          "com a prescrição revista e com o registo de levantamentos. Esta "
          "combinação é rara na região: a revisão de 98 estudos africanos "
          "sobre instrumentos de adesão mostrou que a maioria recorre a "
          "questionários genéricos aplicados por entrevistador, que poucos "
          "acrescentam métodos objectivos e que só 15,3% descrevem validação "
          "ou adaptação cultural do instrumento {muchanga2026}."),
        P("A adaptação para o contexto moçambicano e para o emakhuwa da escala "
          "de Hill-Bone, partindo da versão portuguesa já publicada "
          "{nogueirasilva2016}, com avaliação da validade de conteúdo e da "
          "consistência interna, acrescenta evidência psicométrica útil a "
          "outros serviços do país. A escala tem propriedades documentadas em "
          "50 estudos, com alfa de Cronbach de 0,75, e a sua subescala de toma "
          "da medicação é a que apresenta melhor desempenho "
          "{commodoremensa2023}, tendo já sido usada em populações africanas "
          "{sarfo2018,nakwafila2022}."),
    ],
    "academica": [
        P("No plano académico, o trabalho insere o estudante de Farmácia da "
          "Universidade Lúrio no campo das doenças crónicas não "
          "transmissíveis e exige competências de "
          "desenho de estudos, medição padronizada da pressão arterial, "
          "revisão de prescrição, adaptação de instrumentos e análise "
          "multivariável. Os resultados criam a linha de base para trabalhos "
          "posteriores, nomeadamente para um ensaio de aconselhamento "
          "farmacêutico dirigido, cujo efeito esperado está quantificado na "
          "literatura {mills2024}, e aproximam o ensino farmacêutico das "
          "consultas de doentes crónicos das unidades sanitárias da cidade."),
    ],
    "social": [
        P("A relevância social decorre do que está em jogo para o doente e "
          "para a família. Cada acidente vascular cerebral evitado poupa anos "
          "de incapacidade a uma pessoa muitas vezes em idade produtiva e "
          "custos elevados ao agregado familiar, e mais de metade destes "
          "acidentes tem origem na hipertensão {misaudnt2020}. Ao quantificar "
          "o peso do custo dos "
          "medicamentos e da ruptura de stock, o estudo dá visibilidade a uma "
          "barreira que os doentes sentem mas que raramente é registada: em "
          "hospitais do sul da Etiópia, o esquema anti-hipertensor era "
          "comportável para apenas 22,4% dos doentes, e essa "
          "comportabilidade associou-se ao controlo da pressão arterial, com "
          "OR ajustado de 3,49 {sorato2022}."),
    ],
    "politica": [
        P("No plano político, os resultados respondem directamente a metas "
          "nacionais. O Plano Estratégico Multissectorial de Prevenção e "
          "Controlo das DNT 2020-2029 elege como indicador de resposta do "
          "sector a proporção de doentes hipertensos e diabéticos tratados com "
          "sucesso, integra os anti-hipertensores na lista de medicamentos "
          "essenciais e estima que cada dólar investido no controlo da "
          "hipertensão e da diabetes gere um retorno de 3,29 dólares "
          "{misaudnt2020}. O pacote técnico da OMS para a gestão das doenças "
          "cardiovasculares nos cuidados de saúde primários (HEARTS) organiza "
          "esse controlo em protocolos padronizados, acesso garantido aos "
          "medicamentos e cuidados partilhados em equipa {whohearts2020}. Ao "
          "fornecer à direcção de cada unidade sanitária, ao SDSMAS da Cidade "
          "de Nampula e à Direcção Provincial de Saúde de Nampula uma medida "
          "local do indicador e a hierarquia das barreiras, o estudo dá "
          "conteúdo operacional a essas orientações."),
    ],
}

# ----------------------------------------------------- 6. revisao -----------
REVISAO = [
    ("Hipertensão arterial, diagnóstico e metas de controlo", [
        P("A hipertensão arterial define-se pela presença de pressão sistólica "
          "igual ou superior a 140 mmHg, de pressão diastólica igual ou "
          "superior a 90 mmHg, ou pela toma de medicação anti-hipertensora; é "
          "esta a definição usada nas análises internacionais de tendências "
          "{ncd2021} e a que o Plano Estratégico Multissectorial de Prevenção "
          "e Controlo das DNT adopta para a vigilância em Moçambique "
          "{misaudnt2020}. A medição no consultório, com braçadeira no braço, "
          "continua a ser o método de referência para a classificação e para "
          "a definição das metas terapêuticas, mas a pressão arterial é "
          "altamente variável, razão pela qual todas as normas recomendam usar "
          "a média de várias leituras e não uma leitura isolada "
          "{schutte2022}."),
        P("A norma da OMS para o tratamento farmacológico da hipertensão no "
          "adulto recomenda iniciar medicação a partir de 140 mmHg de pressão "
          "sistólica ou 90 mmHg de pressão diastólica na população geral, e já "
          "entre 130 e 139 mmHg de pressão sistólica nos doentes com doença "
          "cardiovascular estabelecida, diabetes, doença renal crónica ou "
          "risco cardiovascular elevado. O alvo é uma pressão arterial "
          "inferior a 140/90 mmHg na população geral e uma pressão sistólica "
          "inferior a 130 mmHg nesses doentes de maior risco. Como primeira "
          "linha aceita qualquer das três classes, diuréticos tiazídicos ou "
          "análogos, inibidores da enzima de conversão da angiotensina ou "
          "antagonistas dos receptores da angiotensina, e bloqueadores dos "
          "canais de cálcio di-hidropiridínicos de acção longa, preferindo a "
          "combinação de dois fármacos, de preferência num único comprimido, "
          "como tratamento inicial. O seguimento deve ser mensal até se "
          "atingir a meta e, depois, de três em três ou de seis em seis meses "
          "{who2021hta}."),
        P("O presente estudo adopta como definição operacional de pressão "
          "arterial controlada a média de leituras padronizadas inferior a "
          "140 mmHg de sistólica e inferior a 90 mmHg de diastólica, o mesmo "
          "critério usado nos estudos africanos de base hospitalar com que os "
          "resultados serão comparados {cavagna2021,sarfo2018}."),
    ]),
    ("Magnitude e consequências do mau controlo da pressão arterial", [
        P("O mau controlo é um problema global antes de ser local: as "
          "melhorias observadas desde 1990 concentraram-se nos países de "
          "rendimento alto, praticamente sem alteração na África subsariana "
          "{ncd2021}. Nas unidades sanitárias africanas os valores são "
          "consistentemente "
          "baixos, embora variem com o nível de cuidados. Em 29 hospitais de "
          "12 países, 76,7% dos doentes medicados estavam acima da meta e "
          "28,3% destes apresentavam pressão arterial igual ou superior a "
          "180/110 mmHg, sendo a monoterapia o esquema mais frequente entre "
          "eles {cavagna2021}. Em cinco hospitais do Gana, com 2.870 doentes, "
          "42,3% estavam controlados {sarfo2018}; em hospitais do sul da "
          "Etiópia, a proporção foi de 17,5% {sorato2022}; e em quatro "
          "hospitais distritais rurais do Ruanda, apenas 26 de 89 doentes com "
          "dados de pressão arterial, ou seja 29%, atingiam a meta "
          "{sibomana2019}."),
        P("Em Moçambique, a informação disponível é sobretudo populacional: "
          "entre 2005 e 2014-2015 o controlo entre os tratados passou de 39,9% "
          "para 44,5%, sem significado estatístico, enquanto a prevalência "
          "subiu e o conhecimento do diagnóstico ficou estagnado "
          "{jessen2018}. O acesso ao diagnóstico é "
          "desigual: entre os homens, 15,2% na área urbana e 7,9% na área "
          "rural conheciam o seu estado, e entre as mulheres a diferença foi "
          "de 33,2% para 8,9% {misaudnt2020}."),
        P("Parte do mau controlo não depende do doente. Num estudo "
          "prospectivo com 282 doentes hipertensos ambulatórios, 67,4% tinham "
          "a pressão arterial descontrolada e 72% destes não viram a "
          "terapêutica iniciada nem intensificada, situação designada por "
          "inércia terapêutica {niriayo2024}. No Ruanda, 43% dos clínicos "
          "escolheram um diurético da ansa como medicamento para um doente "
          "hipertenso recém-diagnosticado sem comorbilidades, contrariando a "
          "norma em vigor, e metade reconheceu a falta de cumprimento das "
          "normas como barreira {sibomana2019}. Qualquer leitura da adesão "
          "tem, por isso, de ser acompanhada da descrição da prescrição."),
    ]),
    ("Adesão à terapêutica anti-hipertensora: magnitude e determinantes", [
        P("A adesão traduz o grau em que a toma dos medicamentos corresponde "
          "ao esquema acordado com o profissional de saúde e é reconhecida "
          "como um preditor forte do controlo da pressão arterial "
          "{aminde2025}. Distingue-se da persistência, que é a continuidade do "
          "tratamento ao longo do tempo, e da adesão às medidas não "
          "farmacológicas, como a redução do sal, que na escala usada neste "
          "estudo constitui um domínio próprio {sarfo2018}."),
        P("As estimativas variam muito. Uma meta-análise de 312 estudos, com "
          "108.014 participantes de 28 países africanos, situou a adesão "
          "agregada aos anti-hipertensores em 51% (IC95% 44-58), com adesão de "
          "apenas 28% à auto-monitorização da pressão arterial e adesão global "
          "aos vários pilares do auto-cuidado de 35% {apostolou2026}. Outra "
          "meta-análise, de 95 estudos e 34.102 adultos tratados, encontrou "
          "não adesão em 43,9% (IC95% 39,2-48,6), sem alteração ao longo do "
          "tempo e com diferenças segundo o método de medida e a idade, sendo "
          "a não adesão mais frequente abaixo dos 57 anos, com 47,9%, do que "
          "acima dessa idade, com 39,4% {aminde2025}. Nos estudos primários, "
          "os valores vão de 8,9% de adesão em dois hospitais terciários do "
          "norte da Nigéria {adisa2018} a 87,7% numa região da Namíbia "
          "{nakwafila2022}, passando por 59,94% no leste da Etiópia "
          "{yousuf2025} e 67,8% num hospital universitário do Gana "
          "{ryabinina2026}; a revisão dos instrumentos usados em África "
          "documenta valores entre 0% e 96,8% {muchanga2026}."),
        P("Os determinantes repetem-se de estudo para estudo. A meta-análise "
          "africana identificou os factores socioeconómicos e os relacionados "
          "com o doente como os mais frequentes, apontando o elevado número de "
          "comprimidos, o custo da medicação, os efeitos secundários e as "
          "comorbilidades como preditores de má adesão, e a participação "
          "activa do doente, a percepção correcta da doença e o conhecimento "
          "sobre o tratamento como preditores de boa adesão {aminde2025}. A "
          "escolaridade, a auto-eficácia e o apoio social surgiram como "
          "determinantes transversais na análise em rede de 312 estudos "
          "{apostolou2026}. No leste da Etiópia, residir a menos de 10 km da "
          "unidade sanitária associou-se a melhor adesão, com *odds ratio* "
          "ajustado (ORa) de 4,60 (IC95% 1,97-10,73), tal como ter apoio "
          "social (ORa 1,86; IC95% 1,13-3,08) e possuir seguro de "
          "saúde (ORa 2,00; IC95% 1,11-3,59), "
          "enquanto tomar três ou mais medicamentos se associou a pior adesão "
          "(ORa 0,28; IC95% 0,12-0,64) {yousuf2025}."),
    ]),
    ("Custo, disponibilidade dos medicamentos e barreiras de acesso", [
        P("A adesão só é possível quando o medicamento existe e é pago. O "
          "estudo Prospective Urban Rural Epidemiology, em 626 comunidades de "
          "20 países, mostrou que apenas 13% das comunidades de países de "
          "rendimento baixo dispunham das quatro classes de anti-hipertensores "
          "e que 31% dos agregados familiares desses países não conseguiam "
          "pagar dois medicamentos; a disponibilidade das quatro classes "
          "associou-se a maior uso de medicação, a mais terapêutica combinada "
          "e a maior probabilidade de controlo (OR ajustado 2,06; IC95% "
          "1,69-2,50) {attaei2017}. Em hospitais do sul da Etiópia, o custo "
          "anual médio dos anti-hipertensores foi de 11,39 dólares dos Estados "
          "Unidos, o esquema era comportável para apenas 22,4% dos doentes e a "
          "comportabilidade associou-se ao controlo (ORa 3,49; IC95% "
          "1,42-9,83) {sorato2022}."),
        P("Em Moçambique, a fragilidade do abastecimento está documentada. No "
          "serviço de urgência de um hospital geral de Maputo, a "
          "disponibilidade média dos medicamentos necessários ao manejo da "
          "hipertensão era de 28% e não existiam protocolos clínicos nem "
          "algoritmos de estratificação do risco {bay2019}. Gestores e "
          "profissionais de unidades urbanas e rurais apontaram a escassez de "
          "equipamento de diagnóstico, de consumíveis e de medicamentos, e o "
          "financiamento insuficiente, como barreiras ao cuidado das DNT, "
          "agravadas por uma formação centrada nas doenças infecciosas "
          "{madede2024}. O contraste com os programas verticais é sentido "
          "pelos próprios doentes: em Lilongwe, adultos com infecção pelo "
          "vírus da imunodeficiência humana e hipertensão referiram adesão "
          "claramente pior à medicação anti-hipertensora, atribuindo a "
          "diferença ao custo destes medicamentos por oposição à gratuitidade "
          "da terapêutica anti-retroviral {hing2019}."),
        P("Os estudos clínicos africanos confirmam o peso destas barreiras no "
          "resultado. No Gana, o mau controlo associou-se de forma "
          "independente às dificuldades referidas em obter os "
          "anti-hipertensores (ORa 1,24; IC95% 1,02-1,49) e ao número de "
          "anti-hipertensores prescritos (ORa 1,32; IC95% 1,21-1,44) "
          "{sarfo2018}. Na Namíbia, receber medicação suficiente até à "
          "consulta seguinte associou-se à boa adesão (OR 5,44; IC95% "
          "1,76-16,85), tal como o comparecimento nas consultas de seguimento "
          "(OR 8,49; IC95% 3,82-18,85) "
          "{nakwafila2022}, e num hospital universitário do Gana a "
          "disponibilidade da medicação manteve-se como preditor da adesão "
          "(ORa 4,16) {ryabinina2026}."),
    ]),
    ("Crenças sobre a doença, esquecimento e determinantes psicossociais", [
        P("As crenças do doente sobre a sua doença organizam-se em dimensões "
          "estáveis, como as consequências percebidas, a duração esperada, o "
          "controlo pessoal, o controlo pelo tratamento, os sintomas "
          "atribuídos, a preocupação, a compreensão e a resposta emocional, "
          "captadas pelo questionário breve de percepção da doença "
          "{broadbent2006}. A revisão de 188 estudos, em 26 línguas e 36 "
          "países, documentou a validade concorrente e preditiva do "
          "instrumento e a sua sensibilidade à mudança após intervenções "
          "{broadbent2015}. Num estudo multicêntrico com 440 doentes "
          "hipertensos, em que 41,8% referiram não adesão, a melhor "
          "compreensão da doença (OR 0,89; IC95% 0,82-0,97) e uma resposta "
          "emocional menos marcada (OR 0,93; IC95% 0,88-0,99) associaram-se a "
          "menor probabilidade de não adesão {alfian2022}."),
        P("Em África, as crenças assumem formas próprias. Em Lilongwe, os "
          "doentes consideravam a hipertensão uma doença tão ou mais "
          "preocupante do que a infecção pelo vírus da imunodeficiência "
          "humana, pela gravidade das suas consequências e pela dificuldade em "
          "as antecipar, mas aderiam menos ao tratamento {hing2019}. O recurso "
          "à medicina tradicional foi o único factor independentemente "
          "associado à pressão arterial não controlada nas consultas de 12 "
          "países africanos (OR 1,72; IC95% 1,19-2,49) {cavagna2021}. O "
          "esquecimento continua a ser o motivo de não adesão mais referido, "
          "correspondendo a 35,2% das razões apontadas por 605 doentes de dois "
          "hospitais terciários nigerianos {adisa2018}."),
        P("O comportamento alimentar completa o quadro, porque a escala usada "
          "neste estudo inclui um domínio de consumo de sal. No inquérito "
          "nacional moçambicano, com 3.116 participantes dos 15 aos 64 anos, "
          "25,9% referiram adicionar sal ou tempero salgado à comida já "
          "preparada com frequência ou sempre, 16,9% desconheciam que o "
          "consumo elevado de sal pode prejudicar a saúde e 74,9% não "
          "limitavam o consumo de alimentos processados; o conhecimento do "
          "diagnóstico de hipertensão associou-se, em geral, a melhor "
          "conhecimento e a comportamentos mais favoráveis {jessensal2018}."),
    ]),
    ("Enquadramento normativo moçambicano e papel da farmácia", [
        P("O Plano Estratégico Multissectorial de Prevenção e Controlo das DNT "
          "2020-2029, do Ministério da Saúde (MISAU), integra a prevenção e o "
          "controlo da hipertensão e da diabetes nos cuidados de saúde "
          "primários, inclui os respectivos "
          "medicamentos na lista nacional de medicamentos essenciais e define, "
          "como indicador de resposta do sector da saúde, a proporção de "
          "doentes hipertensos e diabéticos tratados com sucesso, ou seja "
          "controlados. O kit básico da "
          "consulta do doente crónico, definido para os níveis primário e "
          "secundário, inclui um esfigmomanómetro com braçadeira média e "
          "grande, balança, estetoscópio, fita métrica e estadiómetro "
          "{misaudnt2020}."),
        P("A nível internacional, o pacote técnico HEARTS organiza o controlo "
          "da hipertensão nos cuidados primários em protocolos de tratamento "
          "padronizados, acesso garantido aos medicamentos e à tecnologia, "
          "cuidados baseados na equipa e sistemas de informação orientados "
          "para o doente {whohearts2020}, e a norma da OMS de 2021 fornece o "
          "conteúdo clínico desses protocolos {who2021hta}. Em Moçambique, "
          "porém, faltam protocolos escritos ao nível da unidade sanitária "
          "{bay2019} e formação específica dos profissionais {madede2024}, o "
          "que abre espaço à variabilidade de práticas."),
        P("Neste espaço, a farmácia tem uma posição distinta: é o serviço em "
          "que o doente passa em cada levantamento, mesmo quando não há "
          "consulta clínica, e onde é possível verificar a prescrição, "
          "confirmar as datas dos levantamentos e conversar sobre as "
          "dificuldades de toma. A meta-análise de 116 comparações mostrou que "
          "as intervenções conduzidas por farmacêuticos e por agentes "
          "comunitários de saúde produziram as maiores reduções da pressão "
          "sistólica, de 7,3 mmHg (IC95% 5,6-9,1) no caso dos farmacêuticos, e "
          "da pressão diastólica, de 3,9 mmHg (IC95% 2,5-5,2), sendo as "
          "primeiras significativamente mais eficazes do que as conduzidas por "
          "enfermeiros ou por médicos {mills2024}. Conhecer o perfil local dos "
          "doentes descontrolados é a condição para desenhar essa intervenção "
          "com eficiência."),
    ]),
    ("Medição da pressão arterial e da adesão: métodos e instrumentos", [
        P("Não existe método perfeito para medir a adesão. Os relatos "
          "subjectivos, incluindo a percepção do clínico, são inexactos; os "
          "questionários preenchidos pelo doente tendem a sobrestimar a adesão "
          "e têm baixa especificidade diagnóstica; os registos de dispensa da "
          "farmácia são úteis mas dependem da qualidade do registo; os "
          "dispositivos electrónicos são exactos mas caros e seguem "
          "habitualmente um só medicamento; e nenhum destes métodos indirectos "
          "confirma a ingestão, que só o doseamento dos fármacos em fluidos "
          "biológicos por cromatografia líquida acoplada a espectrometria de "
          "massa consegue demonstrar {gupta2016}. Em contextos de recursos "
          "limitados, a recomendação prática é combinar um instrumento "
          "estruturado com uma medida indirecta objectiva, o que este estudo "
          "faz ao juntar a escala de adesão ao registo de levantamentos e à "
          "revisão da prescrição."),
        P("A escala de Hill-Bone de adesão à terapêutica anti-hipertensora foi "
          "desenvolvida para populações com baixa escolaridade e tem 14 itens "
          "distribuídos por três domínios, a toma da medicação, o "
          "comparecimento nas consultas e a redução do consumo de sal "
          "{kim2000,sarfo2018}. A revisão sistemática de 50 estudos, 44 deles "
          "em hipertensão, documentou propriedades psicométricas sólidas, com "
          "alfa de Cronbach de 0,75, sensibilidade para captar o efeito de "
          "intervenções e melhor desempenho da subescala de toma da medicação "
          "{commodoremensa2023}. Pontuações mais elevadas indicam pior adesão: "
          "no Gana, cada cinco pontos adicionais na escala associaram-se a "
          "maior probabilidade de pressão arterial não controlada (ORa 1,21; "
          "IC95% 1,09-1,35) {sarfo2018}. Existe uma versão em português "
          "europeu, obtida por tradução e retroversão formais, que precisou de "
          "alterações de redacção e de formato para ser compreendida por "
          "doentes idosos e com baixa literacia e que carece de validação em "
          "estudos posteriores {nogueirasilva2016}."),
        P("A escolha desta escala em vez da escala de Morisky de oito itens, "
          "usada em 50 dos 98 estudos africanos revistos {muchanga2026}, "
          "assenta em dois motivos: a escala de Hill-Bone foi construída para "
          "a hipertensão e inclui os domínios de consulta e de sal, "
          "relevantes no contexto local, e dispõe de versão portuguesa "
          "publicada. Uma vez que a validação local dos instrumentos é rara "
          "nos estudos africanos {muchanga2026}, o protocolo prevê painel de "
          "peritos com cálculo do índice de validade de conteúdo (IVC) "
          "{almanasreh2019}, tradução e retroversão para emakhuwa, pré-teste e "
          "consistência interna."),
        P("Quanto à pressão arterial, o kit "
          "nacional da consulta do doente crónico prevê esfigmomanómetro com "
          "braçadeira média e grande {misaudnt2020}, mas a exactidão depende "
          "do estado do aparelho e do cumprimento do procedimento, pelo que o "
          "estudo usa aparelho próprio, verificado, e um procedimento único "
          "nas três unidades sanitárias."),
    ]),
]

# ----------------------------------------------------- 7. estado da arte ----
ESTADO_ARTE = [
    P("O [[quadro:estado_arte]] reúne estudos empíricos dos últimos dez anos "
      "sobre o controlo da pressão arterial e a adesão à terapêutica "
      "anti-hipertensora em adultos, com prioridade para Moçambique e para a "
      "África subsariana, indicando o local, o desenho, a dimensão da amostra "
      "e os resultados numéricos principais."),
    QUADRO("estado_arte",
           "Síntese de estudos sobre o controlo da pressão arterial e a "
           "adesão à terapêutica anti-hipertensora (estado da arte)",
           ["Autor (ano)", "Local", "Desenho (n)", "Principais resultados"],
           [
               ["Jessen et al. (2018) {jessen2018}", "Moçambique (nacional)",
                "Transversal de base populacional (2.965)",
                "Prevalência de 38,9% nos 25-64 anos em 2014-2015 contra "
                "33,1% em 2005; conhecimento do diagnóstico de 14,5%; "
                "tratamento entre os que sabiam de 50,1%; controlo entre os "
                "tratados de 44,5%."],
               ["Bay et al. (2019) {bay2019}",
                "Moçambique (hospital geral, Maputo)",
                "Observacional prospectivo de 30 dias (1.911)",
                "Percurso do doente não padronizado; ausência de protocolos "
                "clínicos e de algoritmos de estratificação do risco; "
                "disponibilidade média dos medicamentos de 28%."],
               ["Madede et al. (2024) {madede2024}",
                "Moçambique (unidades urbanas e rurais, Maputo)",
                "Qualitativo (24 entrevistas)",
                "Formação orientada para as doenças infecciosas; falta de "
                "equipamento de diagnóstico, consumíveis e medicamentos; "
                "financiamento insuficiente para as doenças não "
                "transmissíveis."],
               ["Cavagna et al. (2021) {cavagna2021}",
                "12 países africanos (29 hospitais)",
                "Transversal multinacional (2.198)",
                "96,6% sob medicação; 76,7% dos tratados não controlados e "
                "28,3% destes com 180/110 mmHg ou mais; uso de medicina "
                "tradicional associado ao mau controlo (OR 1,72; IC95% "
                "1,19-2,49)."],
               ["Sarfo et al. (2018) {sarfo2018}", "Gana (5 hospitais)",
                "Transversal multicêntrico (2.870)",
                "42,3% controlados; mau controlo associado a cuidados "
                "terciários (ORa 2,47), a pior adesão na escala de Hill-Bone "
                "(ORa 1,21 por 5 pontos), a dificuldades em obter os "
                "medicamentos (ORa 1,24) e ao número de anti-hipertensores "
                "(ORa 1,32)."],
               ["Sibomana et al. (2019) {sibomana2019}",
                "Ruanda (4 hospitais distritais rurais)",
                "Transversal (112 doentes, 30 clínicos)",
                "Adesão elevada em 77%, mas apenas 29% com a meta tensional "
                "atingida; 43% dos clínicos escolheram um diurético da ansa "
                "em primeira linha; nenhum factor do doente associado ao mau "
                "controlo."],
               ["Sorato et al. (2022) {sorato2022}",
                "Etiópia (hospitais do sul)", "Transversal (406)",
                "Controlo de 17,5%; 66,5% em terapêutica combinada; custo "
                "anual médio de 11,39 dólares dos Estados Unidos; esquema "
                "comportável para 22,4%; comportabilidade associada ao "
                "controlo (ORa 3,49; IC95% 1,42-9,83)."],
               ["Niriayo et al. (2024) {niriayo2024}", "Etiópia (Tigray)",
                "Observacional prospectivo (282)",
                "67,4% com pressão arterial não controlada; inércia "
                "terapêutica em 72% destes, com indicação de aumento de dose "
                "em 73% e de associação de novo fármaco em 27%."],
               ["Yousuf et al. (2025) {yousuf2025}",
                "Etiópia (leste, hospitais públicos)", "Transversal (364)",
                "Adesão de 59,94% (IC95% 54,65-65,06); melhor adesão com "
                "distância inferior a 10 km (ORa 4,60), apoio social (ORa "
                "1,86) e seguro de saúde (ORa 2,00); pior adesão com três ou "
                "mais medicamentos (ORa 0,28)."],
               ["Adisa et al. (2018) {adisa2018}",
                "Nigéria (Sokoto, 2 hospitais terciários)",
                "Transversal com revisão de processos (605)",
                "Adesão à medicação de 8,9% e às medidas de estilo de vida de "
                "6,0%; esquecimento como motivo mais frequente de não adesão "
                "(35,2% das razões apontadas); pressão sistólica média de "
                "149,6 mmHg no primeiro contacto."],
               ["Nakwafila et al. (2022) {nakwafila2022}",
                "Namíbia (região de Khomas)", "Transversal (400)",
                "87,7% com boa adesão pela escala de Hill-Bone; medicação "
                "suficiente até à consulta seguinte (OR 5,44), comparecimento "
                "nas consultas (OR 8,49) e apoio de familiares e amigos "
                "associados à adesão."],
               ["Ryabinina et al. (2026) {ryabinina2026}",
                "Gana (hospital universitário, Cape Coast)",
                "Transversal (292)",
                "Adesão de 67,8%; conhecimento dos medicamentos (ORa 4,40), "
                "do esquema posológico (ORa 5,27), disponibilidade da "
                "medicação (ORa 4,16) e monitorização regular da pressão "
                "arterial (ORa 1,85) como preditores."],
               ["Hing et al. (2019) {hing2019}", "Malawi (Lilongwe)",
                "Qualitativo (75 entrevistas)",
                "Adesão auto-relatada muito pior para a hipertensão do que "
                "para a infecção pelo vírus da imunodeficiência humana, "
                "atribuída ao custo dos anti-hipertensores face à "
                "gratuitidade da terapêutica anti-retroviral."],
               ["Alfian et al. (2022) {alfian2022}",
                "Indonésia (3 cidades)",
                "Transversal multicêntrico (440)",
                "41,8% com não adesão; melhor compreensão da doença (OR 0,89) "
                "e resposta emocional menos marcada (OR 0,93) associadas a "
                "menor não adesão."],
           ],
           larguras=[3.3, 2.5, 2.8, 7.4],
           fonte="Elaboração própria (2026), a partir das fontes citadas."),
    P("A leitura do quadro revela três padrões. O primeiro é a dissociação "
      "entre adesão declarada e resultado clínico: no Ruanda, 77% dos doentes "
      "foram classificados como aderentes e apenas 29% tinham a meta atingida "
      "{sibomana2019}. A dissociação aponta para causas que não estão no "
      "doente, como a inércia terapêutica {niriayo2024}, e para a "
      "sobrestimação própria dos instrumentos de auto-relato {gupta2016}. O "
      "segundo padrão é a amplitude das estimativas de adesão, de 8,9% "
      "{adisa2018} a 87,7% {nakwafila2022}, que acompanha o instrumento usado "
      "e a ausência quase generalizada de adaptação local {muchanga2026}, o "
      "que reforça a necessidade de descrever com rigor o instrumento e o "
      "ponto de corte."),
    P("O terceiro padrão é a convergência dos determinantes ligados ao "
      "medicamento e ao serviço. O número de anti-hipertensores prescritos, as "
      "dificuldades em obtê-los e o seu custo surgem associados ao mau "
      "controlo ou à má adesão no Gana {sarfo2018,ryabinina2026}, na Etiópia "
      "{sorato2022,yousuf2025}, na Namíbia {nakwafila2022} e no Malawi "
      "{hing2019}. A evidência moçambicana, porém, é populacional "
      "{jessen2018} ou centrada na organização dos serviços "
      "{bay2019,madede2024}: nenhum dos estudos identificados mediu, em "
      "consultas externas do país, a proporção de doentes com a pressão "
      "arterial controlada em conjunto com uma medida estruturada de adesão, "
      "a prescrição revista e o custo suportado, e nenhum foi realizado em "
      "Nampula. É esta a lacuna que o presente estudo preenche."),
]
ESQUEMA_TEXTO = [
    P("A [[figura:esquema]] representa o modelo conceptual do estudo, "
      "construído a partir dos determinantes descritos na revisão da "
      "literatura {aminde2025,sarfo2018}. Quatro grupos de factores, "
      "relacionados com o medicamento e o serviço, com o acesso à unidade "
      "sanitária, com o doente e com as suas características "
      "sociodemográficas e clínicas, influenciam a adesão à terapêutica "
      "anti-hipertensora e, através dela e de forma directa, o controlo da "
      "pressão arterial, que é o desfecho principal. A adesão é analisada "
      "simultaneamente como variável independente no modelo do controlo "
      "(objectivo específico 4) e como desfecho próprio (objectivo específico "
      "5). A idade, o sexo, o tempo de diagnóstico, a presença de diabetes ou "
      "de outras comorbilidades entram "
      "como variáveis de ajustamento."),
]
ESQUEMA_TITULO = ("Esquema conceptual dos factores associados ao controlo da "
                  "pressão arterial e à adesão à terapêutica "
                  "anti-hipertensora")
ESQUEMA = {
    "contexto": ("Adultos hipertensos seguidos em consultas externas de três "
                 "unidades sanitárias da cidade de Nampula, Abril a Junho de "
                 "2027"),
    "blocos": [
        ("Medicamento e serviço",
         ["número de anti-hipertensores prescritos",
          "custo mensal suportado pelo doente",
          "falta do medicamento na unidade sanitária"]),
        ("Acesso à unidade sanitária",
         ["tempo de deslocação até à consulta",
          "custo do transporte de ida e volta"]),
        ("Factores do doente",
         ["crenças sobre a doença",
          "esquecimento e efeitos adversos percebidos",
          "uso de medicina tradicional"]),
        ("Factores sociodemográficos e clínicos",
         ["idade, sexo, escolaridade e rendimento",
          "tempo de diagnóstico e comorbilidades"]),
    ],
    "desfecho": ("Controlo da pressão arterial",
                 ["controlada: sistólica abaixo de 140 mmHg e diastólica "
                  "abaixo de 90 mmHg",
                  "não controlada",
                  "variável intermédia analisada: adesão à terapêutica "
                  "anti-hipertensora"]),
    "moderadores": ("Variáveis de ajustamento",
                    ["idade e sexo",
                     "tempo desde o diagnóstico",
                     "diabetes e outras comorbilidades",
                     "unidade sanitária (estratificação)"]),
}

# ----------------------------------------------------- 8. metodologia -------
METODOLOGIA = [
    ("Tipo e desenho do estudo", [
        P("Trata-se de um estudo observacional, transversal, descritivo e "
          "analítico, multicêntrico e de abordagem quantitativa. Cada "
          "participante é avaliado num único momento, o da sua consulta "
          "externa, através de três fontes complementares: a medição "
          "padronizada da pressão arterial pelo investigador, a revisão da "
          "prescrição e do cartão do doente crónico, e uma entrevista "
          "estruturada que recolhe a adesão, as crenças sobre a doença, o "
          "custo suportado e as barreiras de acesso. O desenho permite estimar "
          "a proporção de doentes controlados e analisar associações, mas não "
          "estabelece causalidade. "
          "O relato seguirá a declaração Strengthening the Reporting of "
          "Observational Studies in Epidemiology (STROBE) {vonelm2007}."),
    ]),
    ("Local e período do estudo", [
        P("O estudo decorre em três unidades sanitárias da cidade de Nampula "
          "com consulta externa de doentes crónicos: o HCN, hospital de "
          "referência da região norte e unidade de ensino, e duas unidades "
          "sanitárias urbanas com maior volume de consultas de hipertensão "
          "[confirmar junto do SDSMAS da Cidade de Nampula a identificação "
          "das duas unidades urbanas com maior volume de consultas de "
          "hipertensão e a designação oficial de cada consulta]. Em cada "
          "unidade, o doente hipertenso é atendido na consulta, sai com "
          "prescrição e levanta os medicamentos na farmácia da própria "
          "unidade, ficando o registo da dispensa no cartão do doente crónico "
          "ou no livro de registo da farmácia [confirmar junto de cada "
          "farmácia qual o suporte de registo da dispensa em uso]."),
        P("A recolha de dados decorre de 1 de Abril a 30 de Junho de 2027, nos "
          "dias úteis em que há consulta de doentes crónicos, durante o "
          "horário de funcionamento. O estudo, no seu conjunto, decorre de "
          "Outubro de 2026 a Setembro de 2027, e a recolha só começa depois do "
          "parecer favorável do comité de bioética e das autorizações "
          "institucionais. O pré-teste do instrumento decorre em Março de "
          "2027, também depois da aprovação ética."),
    ]),
    ("População e unidade de análise", [
        P("A população-alvo é constituída pelos adultos com hipertensão "
          "arterial seguidos em consulta externa na cidade de Nampula. A "
          "população acessível são os adultos com 18 ou mais anos, com "
          "diagnóstico de hipertensão registado e terapêutica "
          "anti-hipertensora prescrita há pelo menos três meses, que "
          "comparecem às consultas das três unidades seleccionadas durante o "
          "período de recolha. O número de consultas mensais de hipertensão em "
          "cada unidade será obtido junto da respectiva direcção antes do "
          "início da recolha [confirmar junto da direcção de cada unidade "
          "sanitária o número de consultas mensais de doentes hipertensos "
          "adultos]."),
        P("A unidade de análise é o doente. Cada doente é incluído uma única "
          "vez: se regressar à consulta durante o período de recolha, não é "
          "novamente seleccionado, o que se verifica por uma lista de "
          "controlo, guardada à parte, com o número do processo dos já "
          "entrevistados em cada unidade. Os três meses de tratamento exigidos "
          "garantem que houve tempo para pelo menos um ciclo completo de "
          "levantamento e para a titulação inicial da terapêutica, de acordo "
          "com o seguimento mensal recomendado até se atingir a meta "
          "{who2021hta}."),
    ]),
    ("Amostra e cálculo do tamanho da amostra", [
        P("O tamanho mínimo da amostra foi calculado para o objectivo "
          "descritivo principal, a proporção de adultos com a pressão arterial "
          "controlada, pela fórmula para estimar uma proporção numa população "
          "grande:"),
        FORMULA("n<sub>0</sub> = Z<sup>2</sup> × p × (1 - p) / d<sup>2</sup>"),
        P("Em que Z = 1,96 corresponde a um nível de confiança de 95%; p é a "
          "proporção esperada de doentes controlados, fixada em 0,25 a partir "
          "dos valores observados em consultas externas africanas, de 17,5% "
          "em hospitais do sul da Etiópia {sorato2022}, de 23,3% entre os "
          "doentes tratados de 12 países africanos, por complemento dos 76,7% "
          "não controlados {cavagna2021}, e de 29% em "
          "hospitais distritais do Ruanda {sibomana2019}; e d = 0,05 é a "
          "margem de erro absoluta admitida. Substituindo:"),
        FORMULA("n<sub>0</sub> = 1,96<sup>2</sup> × 0,25 × 0,75 / "
                "0,05<sup>2</sup> = 288,12, arredondado para 289"),
        P("Como os participantes de cada unidade partilham o prescritor, o "
          "abastecimento e a organização da consulta, a informação "
          "independente contida na amostra é menor, pelo que se aplica um "
          "efeito de desenho de 1,5, conservador para três "
          "conglomerados com cerca de 161 participantes cada: 289 × 1,5 = "
          "433,5, ou seja 434 participantes com dados completos. "
          "Acrescenta-se uma margem de 10% para recusas e questionários "
          "incompletos:"),
        FORMULA("n<sub>f</sub> = 434 / (1 - 0,10) = 434 / 0,9 = 482,2, "
                "arredondado para 483"),
        P("A amostra final é de 483 adultos, repartidos pelas três unidades de "
          "forma proporcional ao número de consultas mensais de hipertensão; "
          "enquanto esse número não for confirmado, assume-se a repartição "
          "igual de 161 participantes por unidade. A [[tabela:cenarios_n]] "
          "mostra o efeito da correcção para população finita, n<sub>c</sub> = "
          "n<sub>0</sub> / [1 + (n<sub>0</sub> - 1) / N], em vários cenários "
          "do total de doentes seguidos: reduziria a amostra de base para "
          "valores entre 224 e 279, mas não será aplicada, porque o cálculo "
          "de poder consome essa margem."),
        TABELA("cenarios_n",
               "Amostra de base com correcção para população finita, segundo "
               "o número de doentes hipertensos seguidos nas três unidades "
               "sanitárias",
               ["Doentes hipertensos seguidos (N)",
                "Amostra corrigida (n<sub>c</sub>)", "Decisão"],
               [["1.000", "224", "Manter 289"],
                ["2.000", "253", "Manter 289"],
                ["3.000", "264", "Manter 289"],
                ["5.000", "273", "Manter 289"],
                ["8.000", "279", "Manter 289"]],
               larguras=[5.2, 4.6, 6.2],
               fonte="Elaboração própria (2026). Z = 1,96; p = 0,25; "
                     "d = 0,05."),
        P("Para o objectivo específico 4, verificou-se o poder para comparar a "
          "proporção de controlados entre doentes com boa e com baixa adesão, "
          "pela fórmula para duas proporções em grupos de igual dimensão:"),
        FORMULA("n<sub>g</sub> = [Z<sub>1-α/2</sub> × √(2 × p<sub>m</sub> × "
                "(1 - p<sub>m</sub>)) + Z<sub>1-β</sub> × "
                "√(p<sub>1</sub>(1 - p<sub>1</sub>) + p<sub>2</sub>(1 - "
                "p<sub>2</sub>))]<sup>2</sup> / (p<sub>1</sub> - "
                "p<sub>2</sub>)<sup>2</sup>"),
        P("Admitiu-se α = 0,05 (Z<sub>1-α/2</sub> = 1,96), poder de 80% "
          "(Z<sub>1-β</sub> = 0,84), controlo de 20% no grupo com baixa "
          "adesão (p<sub>1</sub>) e de 35% no grupo com boa adesão "
          "(p<sub>2</sub>), o que dá p<sub>m</sub> = 0,275. A diferença de 15 "
          "pontos percentuais corresponde a um OR de 2,15, magnitude "
          "compatível com a associação entre adesão e controlo descrita no "
          "Gana {sarfo2018} e com a repartição aproximadamente equilibrada "
          "entre aderentes e não aderentes que a meta-análise africana faz "
          "prever {aminde2025}. Substituindo:"),
        FORMULA("n<sub>g</sub> = [1,96 × √(0,39875) + 0,84 × "
                "√(0,38750)]<sup>2</sup> / 0,15<sup>2</sup> = "
                "(1,2377 + 0,5229)<sup>2</sup> / 0,0225 = 137,8"),
        P("São necessários 138 participantes em cada grupo, ou seja 276 no "
          "total, que com o mesmo efeito de desenho de 1,5 passam a 414, "
          "abaixo dos 434 previstos com dados completos. Para a regressão "
          "logística exigem-se pelo menos 10 eventos por parâmetro "
          "{peduzzi1996}: com 434 participantes e uma proporção esperada de "
          "25% de doentes controlados, a categoria menos frequente do desfecho "
          "reúne cerca de 109 observações, o que suporta um modelo de até 10 "
          "parâmetros; o modelo principal tem nove. Se a proporção de "
          "controlados for inferior a 21%, o modelo será reduzido pela ordem "
          "definida na análise. Para o objectivo específico 5, com "
          "não adesão esperada próxima de 44% {aminde2025}, haverá cerca de "
          "191 eventos, suficientes para os 12 parâmetros do modelo "
          "respectivo."),
        H3("Técnica de amostragem"),
        P("Em cada unidade sanitária, a selecção é aleatória sistemática a "
          "partir da sequência diária de chegada dos doentes à consulta de "
          "doentes crónicos. O intervalo de amostragem é k = L / n, em que L é "
          "o número de consultas de hipertensão esperado na unidade entre "
          "Abril e Junho, estimado a partir do registo do trimestre anterior, "
          "e n é a quota atribuída à unidade; por exemplo, com 1.610 consultas "
          "no trimestre e uma quota de 161, k = 10. Em cada dia, o primeiro "
          "doente é sorteado entre os k primeiros a chegar e os seguintes são "
          "seleccionados de k em k. Os doentes seleccionados que não cumpram "
          "os critérios de elegibilidade ou recusem participar são "
          "substituídos pelo doente elegível seguinte, e as recusas e os "
          "motivos declarados são registados para calcular a taxa de "
          "participação."),
    ]),
    ("Critérios de inclusão e de exclusão", [
        H3("Critérios de inclusão"),
        LISTA([
            "Idade igual ou superior a 18 anos na data da entrevista.",
            "Diagnóstico de hipertensão arterial registado no processo "
            "clínico ou no cartão do doente crónico.",
            "Terapêutica anti-hipertensora prescrita há pelo menos três "
            "meses, confirmada na prescrição ou no cartão do doente crónico.",
            "Comparecimento pessoal à consulta externa de doentes crónicos de "
            "uma das três unidades sanitárias durante o período de recolha.",
            "Consentimento informado escrito, ou por impressão digital com "
            "testemunha no caso de quem não sabe ler.",
        ]),
        H3("Critérios de exclusão"),
        LISTA([
            "Gravidez ou puerpério até seis semanas, por terem metas "
            "tensionais e esquemas terapêuticos próprios.",
            "Doente internado ou encaminhado para internamento no próprio "
            "dia, antes da medição.",
            "Impossibilidade de medir a pressão arterial em qualquer dos "
            "braços, por amputação, fístula arteriovenosa, linfedema, ferida "
            "ou outra condição que o desaconselhe.",
            "Estado clínico ou mental que impeça a entrevista, segundo a "
            "avaliação do profissional de serviço.",
            "Participação no pré-teste do instrumento.",
        ]),
        P("O doente que tenha mudado de esquema terapêutico no último mês não "
          "é excluído, mas a data da última alteração é registada e usada "
          "numa análise de sensibilidade, porque a pressão arterial pode ainda "
          "não reflectir o efeito do novo esquema."),
    ]),
    ("Variáveis e definições operacionais", [
        P("A variável dependente principal é o controlo da pressão arterial, "
          "definido pela média da segunda e da terceira leituras obtidas "
          "segundo o procedimento padronizado descrito adiante: considera-se "
          "controlada a pressão arterial quando a média da sistólica é "
          "inferior a 140 mmHg e a média da diastólica é inferior a 90 mmHg, "
          "critério que corresponde ao alvo da norma da OMS para a população "
          "geral {who2021hta}, ao usado pelos estudos africanos de base "
          "hospitalar com que os resultados serão comparados "
          "{cavagna2021,sarfo2018} e às directrizes globais da Sociedade "
          "Internacional de Hipertensão de 2020 aplicadas no estudo etíope "
          "{unger2020,sorato2022}. Nos participantes com diabetes, doença "
          "renal crónica ou doença cardiovascular estabelecida, realiza-se uma "
          "análise de sensibilidade com o alvo de pressão sistólica inferior a "
          "130 mmHg {who2021hta}. O [[quadro:variaveis]] apresenta todas as "
          "variáveis, o seu tipo, a definição operacional e o objectivo "
          "específico a que cada uma responde."),
        QUADRO("variaveis", "Variáveis do estudo e definições operacionais",
               ["Variável", "Tipo", "Definição operacional e categorias",
                "Objectivo"],
               [
                   ["Idade", "Independente, quantitativa",
                    "Anos completos; categorias 18-39, 40-49, 50-59, 60 ou "
                    "mais", "1, 4, 5"],
                   ["Sexo", "Independente, nominal", "Masculino; feminino",
                    "1, 4, 5"],
                   ["Escolaridade", "Independente, ordinal",
                    "Nenhuma; primária; secundária; superior", "1, 5"],
                   ["Ocupação e rendimento", "Independente, nominal",
                    "Com rendimento regular; sem rendimento regular", "1"],
                   ["Residência", "Independente, nominal",
                    "Cidade de Nampula; outro distrito", "1"],
                   ["Tempo de deslocação até à consulta",
                    "Independente, quantitativa",
                    "Minutos, só ida; 30 ou menos; mais de 30", "1, 5"],
                   ["Custo do transporte", "Independente, quantitativa",
                    "Meticais gastos na ida e volta; zero se a pé", "1"],
                   ["Unidade sanitária", "Independente, nominal",
                    "Uma das três unidades; usada na estratificação dos "
                    "resultados e no agrupamento dos erros-padrão",
                    "1, 4, 5"],
                   ["Tempo desde o diagnóstico",
                    "Independente, quantitativa",
                    "Meses desde o registo do diagnóstico; menos de 12; "
                    "12-59; 60 ou mais", "1, 4, 5"],
                   ["Comorbilidades", "Independente, nominal",
                    "Diabetes; doença renal crónica; doença cardiovascular "
                    "estabelecida; outras; nenhuma", "1, 4, 5"],
                   ["Número de anti-hipertensores prescritos",
                    "Independente, quantitativa",
                    "Contagem na prescrição em vigor; 1; 2; 3 ou mais "
                    "(exposição principal)", "1, 4"],
                   ["Classes de anti-hipertensores",
                    "Descritiva, nominal",
                    "Diurético tiazídico ou análogo; inibidor da enzima de "
                    "conversão da angiotensina ou antagonista dos receptores "
                    "da angiotensina; bloqueador dos canais de cálcio; beta "
                    "bloqueador; outra {who2021hta}", "1"],
                   ["Combinação em comprimido único",
                    "Descritiva, nominal", "Sim; não", "1"],
                   ["Número total de comprimidos por dia",
                    "Independente, quantitativa",
                    "Contagem de todos os comprimidos diários prescritos",
                    "1, 5"],
                   ["Custo mensal suportado com os anti-hipertensores",
                    "Independente, quantitativa",
                    "Meticais pagos pelo doente no último mês; zero quando "
                    "recebe tudo gratuitamente; analisada de forma contínua e "
                    "dicotomizada em zero contra qualquer valor positivo "
                    "(exposição principal)", "1, 4, 5"],
                   ["Falta do medicamento na unidade sanitária",
                    "Independente, nominal",
                    "Nos três meses anteriores não recebeu pelo menos um dos "
                    "anti-hipertensores prescritos: sim; não", "1, 4, 5"],
                   ["Adesão à terapêutica anti-hipertensora",
                    "Dependente no objectivo 5, independente no 4, "
                    "quantitativa",
                    "Pontuação total (14-56) da escala de Hill-Bone adaptada; "
                    "valores mais elevados indicam pior adesão {sarfo2018}; "
                    "análise contínua e, em alternativa, dicotomizada em boa "
                    "adesão (nenhum comportamento de não adesão na subescala "
                    "de toma) contra baixa adesão",
                    "3, 4, 5"],
                   ["Subescala de toma da medicação",
                    "Dependente, quantitativa",
                    "Pontuação da subescala de toma da escala de Hill-Bone "
                    "{commodoremensa2023}", "3, 5"],
                   ["Motivos de não adesão", "Descritiva, nominal",
                    "Esquecimento; custo; falta do medicamento na unidade "
                    "sanitária; efeitos adversos; sentir-se bem; uso de "
                    "medicina tradicional; outro", "3"],
                   ["Atraso no levantamento", "Descritiva, nominal",
                    "Atraso de 7 ou mais dias em algum levantamento dos três "
                    "meses anteriores, segundo o registo: sim; não; sem "
                    "registo", "3"],
                   ["Crenças sobre a doença",
                    "Independente, quantitativa",
                    "Questionário breve de percepção da doença adaptado; "
                    "pontuação global de ameaça percebida e itens de controlo "
                    "pelo tratamento e de compreensão analisados à parte "
                    "{broadbent2006}", "4, 5"],
                   ["Efeitos adversos percebidos", "Independente, nominal",
                    "Pelo menos um de 10 sintomas atribuídos aos "
                    "anti-hipertensores nos últimos 30 dias: sim; não; número "
                    "de sintomas", "3, 5"],
                   ["Uso de medicina tradicional", "Independente, nominal",
                    "Uso de remédios tradicionais para a tensão nos últimos "
                    "30 dias: sim; não {cavagna2021}", "1, 5"],
                   ["Pressão arterial sistólica e diastólica",
                    "Dependente, quantitativa",
                    "Média da segunda e da terceira leituras, em mmHg", "2, 4"],
                   ["Controlo da pressão arterial", "Dependente, nominal",
                    "Controlada: sistólica inferior a 140 mmHg e diastólica "
                    "inferior a 90 mmHg; não controlada: qualquer valor igual "
                    "ou superior {who2021hta}", "2, 4"],
               ],
               larguras=[3.4, 2.8, 7.8, 2.0]),
    ]),
    ("Instrumentos de recolha de dados e respectivas fontes", [
        P("A recolha assenta em três instrumentos reunidos num caderno único "
          "(Apêndice A): a ficha de medição da pressão arterial, a ficha de "
          "revisão da prescrição e o questionário aplicado por entrevista. O "
          "questionário tem sete secções, da identificação e dos dados "
          "sociodemográficos e de acesso aos dados clínicos e terapêuticos, ao "
          "custo e disponibilidade dos medicamentos, à adesão pela escala de "
          "Hill-Bone adaptada, aos motivos de não adesão e efeitos adversos "
          "percebidos e às crenças sobre a doença. A ficha de revisão da "
          "prescrição regista as classes prescritas segundo a classificação "
          "usada na norma da OMS {who2021hta}, o número de anti-hipertensores, "
          "o número total de comprimidos por dia, a existência de combinação "
          "em comprimido único e as datas dos levantamentos dos três meses "
          "anteriores."),
        P("A adesão é medida pela escala de Hill-Bone, escolhida por ter sido "
          "construída para a hipertensão e para populações com baixa "
          "escolaridade, por incluir os domínios de toma da medicação, "
          "comparecimento nas consultas e consumo de sal {kim2000,sarfo2018}, "
          "por ter propriedades psicométricas documentadas em 50 estudos "
          "{commodoremensa2023} e por existir uma versão em português europeu "
          "obtida por tradução e retroversão formais {nogueirasilva2016}. "
          "Como não há ponto de corte consensual, a análise principal usa a "
          "pontuação contínua, à semelhança do estudo ganês {sarfo2018}, e a "
          "classificação em boa adesão, definida pela ausência de qualquer "
          "comportamento de não adesão na subescala de toma da medicação, é "
          "usada como definição secundária declarada, com análise de "
          "sensibilidade pela mediana da amostra. As crenças sobre a doença "
          "são medidas pelo questionário breve de percepção da doença "
          "{broadbent2006,broadbent2015}. As versões apresentadas no Apêndice "
          "A são versões de trabalho em português europeu, a harmonizar com as "
          "versões publicadas antes da tradução."),
        H3("Adaptação, tradução e validação"),
        P("A adaptação decorre em quatro etapas. Na primeira, um painel de "
          "cinco peritos, composto por um farmacêutico hospitalar, um clínico "
          "da consulta de doentes crónicos, um enfermeiro da mesma consulta, "
          "um docente de saúde pública e um docente de farmácia clínica, "
          "classifica a relevância e a clareza de cada item numa escala de "
          "quatro pontos, calculando-se o IVC de cada item e do conjunto "
          "{almanasreh2019}; os itens com IVC inferior a 0,80 são revistos. Na "
          "segunda, dois tradutores independentes, falantes nativos de "
          "emakhuwa, traduzem o caderno e um terceiro faz a retroversão para "
          "português, resolvendo-se as discrepâncias em reunião com o "
          "investigador, com atenção especial à redacção e ao formato das "
          "perguntas, que exigiram alterações na adaptação portuguesa da "
          "escala {nogueirasilva2016}. Na terceira, o pré-teste é aplicado a 48 "
          "adultos, cerca de 10% da amostra, em Março de 2027, numa das "
          "unidades sanitárias, ficando estes participantes excluídos da "
          "amostra final; avalia-se a compreensão, o tempo de aplicação e a "
          "exequibilidade da revisão da prescrição. Na quarta, calcula-se a "
          "consistência interna pelo alfa de Cronbach, exigindo-se 0,70 ou "
          "mais, valor próximo do descrito para a escala noutras populações "
          "{commodoremensa2023}; a fiabilidade é recalculada na amostra "
          "final."),
    ]),
    ("Procedimentos de recolha de dados e controlo de qualidade", [
        P("A recolha é feita pelo investigador e por um inquiridor assistente "
          "fluente em português e emakhuwa, sem funções clínicas nas unidades "
          "sanitárias, formado durante dois dias sobre o protocolo, a ética, a "
          "aplicação das escalas e a técnica de medição da pressão arterial. "
          "Depois da selecção sistemática, o doente é convidado para um espaço "
          "reservado, recebe a informação sobre o estudo e assina o "
          "consentimento. A medição da pressão arterial precede a entrevista "
          "e obedece a um procedimento único nas três unidades: aparelho "
          "oscilométrico automático de braço, validado para uso clínico e com "
          "braçadeira ajustada ao "
          "perímetro braquial; doente sentado, com as costas apoiadas, os pés "
          "no chão e o braço apoiado ao nível do coração, sem falar; cinco "
          "minutos de repouso; três leituras separadas por um minuto; e média "
          "da segunda e da terceira, uma vez que a variabilidade da pressão "
          "obriga a usar a média de várias leituras e não uma leitura isolada "
          "{schutte2022}. Na primeira leitura mede-se nos dois braços e "
          "utiliza-se depois o braço com o valor mais elevado. Evita-se a "
          "medição nos 30 minutos seguintes ao consumo de café, tabaco ou a "
          "esforço físico, e pede-se ao doente que esvazie a bexiga antes."),
        P("A revisão da prescrição é feita a seguir à entrevista, a partir da "
          "prescrição em vigor e do cartão do doente crónico, com uma ficha "
          "própria sem nome, ligada ao questionário apenas pelo código do "
          "participante. O controlo de qualidade inclui a verificação do "
          "aparelho de pressão arterial antes do início da recolha e no fim de "
          "cada mês, com registo do número de série e da data; a repetição "
          "independente das três leituras pelo inquiridor em 10% dos "
          "participantes, com cálculo do coeficiente de correlação "
          "intraclasse entre observadores; a revisão diária de todos os "
          "cadernos quanto à completude e à coerência; a verificação, por uma "
          "segunda pessoa, de 10% das fichas de revisão da prescrição; a dupla "
          "digitação independente com comparação dos ficheiros e correcção "
          "pelo original; e a supervisão semanal pelo orientador. A entrevista "
          "e a medição demoram cerca de 25 minutos e decorrem enquanto o "
          "doente aguarda, sem atrasar o atendimento."),
    ]),
    ("Processamento e análise dos dados", [
        P("Os dados serão digitados duas vezes em folhas de cálculo com "
          "validação de campos e analisados no programa Statistical Package "
          "for the Social Sciences (SPSS), versão 26 ou superior, ou, em "
          "alternativa, no R, com nível de significância de 5% (p<0,05) e "
          "IC95%. A análise descritiva usa frequências absolutas e relativas "
          "para as variáveis categóricas e média com desvio-padrão ou mediana "
          "com intervalo interquartil para as quantitativas, conforme a "
          "normalidade avaliada pelo teste de Shapiro-Wilk. As pontuações das "
          "escalas são calculadas apenas quando pelo menos 80% dos itens "
          "estão respondidos."),
        P("Para o objectivo específico 1, apresenta-se a caracterização "
          "completa da amostra, incluindo a distribuição do número de "
          "anti-hipertensores, das classes prescritas e do custo mensal "
          "suportado. Para o objectivo 2, estima-se a proporção de doentes "
          "controlados com IC95% pelo método de Wilson, no conjunto e por "
          "unidade sanitária, comparando-se as unidades pelo teste do "
          "qui-quadrado. Para o objectivo 3, descreve-se a distribuição da "
          "pontuação da escala de adesão e da sua subescala de toma, com o "
          "respectivo alfa de Cronbach, a frequência de cada motivo de não "
          "adesão e a proporção de participantes com atraso no levantamento."),
        P("Para o objectivo 4, a associação de cada factor com o mau controlo "
          "é testada pelo qui-quadrado de Pearson, ou pelo teste exacto de "
          "Fisher quando mais de 20% das frequências esperadas forem "
          "inferiores a 5, e pelo teste t de Student ou de Mann-Whitney para "
          "as variáveis quantitativas. Segue-se a regressão logística "
          "multivariável, com a pressão arterial não controlada como variável "
          "dependente, incluindo as quatro exposições principais, a pontuação "
          "de adesão, o número de anti-hipertensores prescritos, o custo "
          "mensal suportado e a pontuação de ameaça percebida, e as variáveis "
          "de ajustamento definidas *a priori*, a idade, o sexo, o tempo desde "
          "o diagnóstico, a presença de diabetes e a falta do medicamento na "
          "unidade sanitária, num total de nove parâmetros. A unidade "
          "sanitária não entra como variável do modelo principal, sendo o seu "
          "efeito tratado pelo agrupamento dos erros-padrão e testado numa "
          "análise de sensibilidade com duas variáveis indicadoras. Se a "
          "categoria menos frequente do desfecho reunir menos de 90 "
          "observações, retiram-se por esta ordem a falta do medicamento e o "
          "tempo desde o diagnóstico. Apresentam-se os ORa com "
          "IC95%, avalia-se a colinearidade pelo factor de inflação da "
          "variância, aceitável abaixo de 5, e o ajustamento pelo teste de "
          "Hosmer-Lemeshow. Como o mau controlo deverá ser frequente, o OR "
          "sobrestima a razão de prevalências, pelo que se estima também a "
          "razão de prevalências (RP) ajustada por regressão de Poisson com "
          "variância robusta {tamhane2016}, com os erros-padrão agrupados por "
          "unidade sanitária, para reflectir o efeito de conglomerado."),
        P("Para o objectivo 5, a baixa adesão é analisada como desfecho, "
          "primeiro na forma contínua, por regressão linear da pontuação da "
          "escala, e depois na forma dicotomizada, por regressão logística "
          "ajustada para a idade, o sexo, a escolaridade, o tempo desde o "
          "diagnóstico e a presença de diabetes, tendo como exposições o número "
          "de comprimidos por dia, o custo suportado, a falta do medicamento "
          "na unidade sanitária, o tempo de deslocação, os efeitos adversos "
          "percebidos, o uso de medicina tradicional e as crenças sobre a "
          "doença, num total de 12 parâmetros, comportáveis pelos cerca de 191 "
          "casos de não adesão previstos. As análises de "
          "sensibilidade incluem o alvo de pressão sistólica inferior a 130 "
          "mmHg nos doentes de maior risco {who2021hta}, a exclusão dos "
          "participantes com alteração do esquema no último mês e a "
          "comparação das características dos participantes e dos recusantes. "
          "Os dados em falta são descritos e não são imputados na análise "
          "principal."),
    ]),
    ("Limitações do estudo e estratégias de mitigação", [
        P("O [[quadro:limitacoes]] resume as limitações previstas, a "
          "consequência de cada uma para a interpretação dos resultados e as "
          "estratégias adoptadas para as reduzir."),
        QUADRO("limitacoes", "Limitações previstas e estratégias de mitigação",
               ["Limitação", "Consequência", "Mitigação"],
               [
                   ["Desenho transversal",
                    "Não permite inferir causalidade nem separar a má adesão "
                    "do mau controlo no tempo",
                    "Interpretar como associações; usar períodos de "
                    "referência anteriores à medição nas perguntas sobre "
                    "adesão, custo e falta de medicamento"],
                   ["Classificação do controlo a partir de uma única visita",
                    "Sobrestimação do mau controlo por efeito de bata branca "
                    "e pela variabilidade da pressão arterial",
                    "Procedimento padronizado com repouso, três leituras e "
                    "média da segunda e da terceira; declarar a limitação e "
                    "não usar o resultado para diagnóstico individual"],
                   ["Adesão medida por auto-relato",
                    "Sobrestimação da adesão e baixa especificidade",
                    "Escala validada e adaptada localmente, inquiridor sem "
                    "funções clínicas, espaço reservado e cruzamento com as "
                    "datas de levantamento registadas"],
                   ["Registo incompleto das datas de levantamento",
                    "Perda da medida indirecta objectiva de adesão",
                    "Verificação prévia em cerca de 30 cartões por unidade; "
                    "se menos de 60% estiverem preenchidos, a variável passa "
                    "a descritiva e não entra nos modelos"],
                   ["Custo e falta de medicamento referidos pelo doente",
                    "Erro de memória e enviesamento das estimativas",
                    "Período de referência curto, de um a três meses; "
                    "confirmação do que foi dispensado no registo da farmácia "
                    "sempre que exista"],
                   ["Apenas três unidades sanitárias urbanas",
                    "Generalização limitada às zonas rurais do distrito e da "
                    "província",
                    "Descrever bem cada unidade e a população atendida; "
                    "apresentar resultados por unidade; extrapolar com "
                    "prudência"],
                   ["Efeito de conglomerado entre unidades sanitárias",
                    "Subestimação dos erros-padrão",
                    "Efeito de desenho de 1,5 no cálculo da amostra, unidade "
                    "incluída nos modelos e erros-padrão agrupados por "
                    "unidade"],
                   ["Tradução para emakhuwa e adaptação das escalas",
                    "Erros de compreensão e perda de validade",
                    "Tradução e retroversão, painel de peritos com IVC, "
                    "pré-teste e cálculo do alfa de Cronbach"],
                   ["Inércia terapêutica e qualidade da prescrição não "
                    "avaliadas face a uma norma",
                    "Atribuição indevida do mau controlo ao doente",
                    "Registar o número e as classes prescritas e o tempo "
                    "desde o diagnóstico; discutir os resultados à luz da "
                    "evidência sobre inércia terapêutica {niriayo2024}"],
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
          "Direcção Provincial de Saúde de Nampula, do SDSMAS da Cidade de "
          "Nampula e da direcção de cada uma das três unidades sanitárias "
          "(Apêndice D). Aplicam-se as salvaguardas seguintes:"),
        LISTA([
            "Consentimento informado livre e esclarecido, escrito, após "
            "leitura da folha de informação em português ou emakhuwa "
            "(Apêndices B e C); quem não sabe ler assina por impressão "
            "digital, na presença de uma testemunha imparcial escolhida pelo "
            "participante. O consentimento inclui a autorização para consultar "
            "a prescrição e o cartão do doente crónico.",
            "Voluntariedade: a recusa ou a desistência não altera o "
            "atendimento nem a dispensa dos medicamentos, o que é explicado "
            "ao participante antes de qualquer pergunta.",
            "Confidencialidade: entrevista em espaço reservado; cadernos "
            "identificados apenas por código; lista de ligação entre o código "
            "e o número do processo guardada em armário fechado, separada dos "
            "cadernos, e destruída após a análise; base de dados sem "
            "identificadores, protegida por palavra-passe; resultados "
            "divulgados apenas de forma agregada; cadernos guardados durante "
            "cinco anos.",
            "Riscos e benefícios: o risco é mínimo, limitado ao tempo da "
            "entrevista, ao desconforto passageiro da braçadeira e à "
            "possibilidade de o participante se inquietar ao conhecer um "
            "valor elevado de pressão arterial; o participante pode recusar "
            "qualquer pergunta. Não há pagamento, e o benefício directo é o "
            "conhecimento do seu valor de pressão arterial e o encaminhamento "
            "descrito a seguir.",
            "Via de referenciação: o valor medido é sempre comunicado ao "
            "participante e registado no cartão do doente crónico. O "
            "participante com pressão arterial igual ou superior a 180/110 "
            "mmHg, ou com queixas como cefaleia intensa, dor torácica, "
            "alterações da visão ou défice neurológico, é acompanhado no "
            "mesmo dia ao clínico de serviço, antes de prosseguir a "
            "entrevista; o participante com pressão arterial não controlada "
            "sem sinais de alarme é informado e encaminhado para a consulta "
            "da sua unidade sanitária. As suspeitas de reacções adversas aos "
            "anti-hipertensores são notificadas pela ficha nacional de "
            "farmacovigilância do MISAU.",
            "Conflito de interesses: o investigador declara não ter conflitos "
            "de interesses; o estudo não tem financiamento de empresas "
            "farmacêuticas e as marcas comerciais não são registadas.",
        ]),
    ]),
]

# ----------------------------------------------------- 9 e 10 ---------------
RESULTADOS_ESPERADOS = [
    P("Os resultados esperados seguem a ordem dos objectivos específicos, com "
      "a direcção indicada pela literatura revista e a utilidade prática de "
      "cada um."),
    LISTA([
        "Objectivo 1: uma caracterização dos adultos hipertensos seguidos "
        "nestas consultas, com a distribuição do número e das classes de "
        "anti-hipertensores e do custo mensal suportado. Espera-se "
        "predomínio feminino e idade média acima dos 50 anos, como noutras "
        "consultas africanas {sarfo2018,ryabinina2026}, e uma parte "
        "substancial dos doentes em monoterapia {cavagna2021}. O perfil serve "
        "para dimensionar a "
        "necessidade de terapêutica combinada e para estimar o peso "
        "financeiro que recai sobre o doente.",
        "Objectivo 2: uma estimativa, com IC95% e por unidade sanitária, da "
        "proporção de doentes com a pressão arterial controlada. Espera-se um "
        "valor abaixo dos 44,5% estimados para os adultos tratados no "
        "inquérito nacional {jessen2018} e próximo do observado em consultas "
        "hospitalares africanas {sarfo2018,sorato2022}. É o primeiro "
        "indicador local do resultado do tratamento e responde ao indicador "
        "de resposta do sector previsto no plano nacional {misaudnt2020}.",
        "Objectivo 3: a distribuição da pontuação de adesão, a consistência "
        "interna da escala adaptada e a hierarquia dos motivos de não adesão. "
        "Espera-se que o esquecimento, o custo e a falta do medicamento na "
        "unidade sanitária encabecem a lista, como noutros países africanos "
        "{adisa2018,ryabinina2026}. Estes dados definem os temas do "
        "aconselhamento farmacêutico.",
        "Objectivo 4: a identificação dos factores independentemente "
        "associados ao mau controlo. Espera-se pior controlo nos doentes com "
        "pior adesão, com mais anti-hipertensores prescritos, que suportam "
        "custo próprio e que percebem a doença como menos controlável pelo "
        "tratamento {sarfo2018,sorato2022,alfian2022}. O resultado permite "
        "construir um perfil de risco simples para seleccionar os doentes que "
        "devem receber acompanhamento reforçado.",
        "Objectivo 5: os factores associados à baixa adesão, entre o número "
        "de comprimidos por dia, o custo, a falta do medicamento, a distância "
        "e as crenças sobre a doença. Espera-se associação com o número de "
        "medicamentos e com a indisponibilidade na unidade sanitária "
        "{yousuf2025,nakwafila2022}. O resultado distingue o que pode ser "
        "resolvido por aconselhamento do que exige decisão de gestão, como a "
        "previsão de stock ou a simplificação do esquema.",
    ]),
    P("O produto final é uma proposta de intervenção farmacêutica dirigida, a "
      "apresentar à direcção de cada unidade sanitária: sessões breves no acto "
      "do levantamento para os doentes com o perfil de risco identificado e um "
      "aviso ao prescritor quando o doente se mantiver acima da meta apesar "
      "de boa adesão, situação em que a inércia terapêutica "
      "pesa mais {niriayo2024,mills2024}."),
]
DIVULGACAO = [
    P("Os resultados serão apresentados na defesa pública do trabalho de "
      "conclusão de curso na Faculdade de Ciências de Saúde da Universidade "
      "Lúrio. Um relatório técnico, com os resultados agregados por unidade "
      "sanitária e a proposta de intervenção farmacêutica, será entregue à "
      "direcção de cada uma das três unidades, ao SDSMAS da Cidade de Nampula "
      "e à Direcção Provincial de Saúde de Nampula, e discutido numa reunião "
      "com as equipas da consulta de doentes crónicos e da farmácia. O "
      "manuscrito será submetido a uma revista científica com revisão por "
      "pares, de preferência de acesso aberto, e os resultados serão "
      "apresentados nas jornadas científicas da universidade e em encontros "
      "nacionais. Para devolver os resultados aos doentes, será preparado um "
      "cartaz em linguagem simples, em português e emakhuwa, para a sala de "
      "espera de cada consulta, sem qualquer dado individual."),
]

# ----------------------------------------------------- 11. cronograma -------
CRONOGRAMA_TEXTO = [
    P("O [[quadro:cronograma]] distribui as actividades pelos 12 meses do "
      "estudo, de Outubro de 2026 a Setembro de 2027. A submissão ao comité "
      "de bioética e os pedidos de autorização ocupam Dezembro e Janeiro; o "
      "painel de peritos, a tradução e a retroversão decorrem em Janeiro e "
      "Fevereiro; a formação do inquiridor e o pré-teste realizam-se em Março, "
      "depois da aprovação ética; a recolha de dados decorre de Abril a Junho "
      "de 2027; a análise e a redacção ocupam Julho e Agosto; "
      "a entrega e a defesa estão previstas para Setembro de 2027."),
]
CRONOGRAMA = {
    "inicio": (2026, 10),
    "n_meses": 12,
    "actividades": [
        ("Revisão da literatura e redacção do protocolo", [1, 2]),
        ("Submissão ao CIBS-UniLúrio e pedidos de autorização", [3, 4]),
        ("Painel de peritos, tradução e retroversão dos instrumentos",
         [4, 5]),
        ("Aquisição e verificação dos esfigmomanómetros", [5, 6]),
        ("Formação do inquiridor e pré-teste", [6]),
        ("Recolha de dados nas três unidades sanitárias", [7, 8, 9]),
        ("Dupla digitação, limpeza e processamento", [8, 9, 10]),
        ("Análise estatística", [10, 11]),
        ("Redacção do relatório final", [10, 11]),
        ("Revisão pelo orientador e entrega", [12]),
        ("Defesa pública e devolução às instituições", [12]),
    ],
}

# ----------------------------------------------------- 12. orcamento --------
ORCAMENTO_TEXTO = [
    P("A [[tabela:orcamento]] apresenta o orçamento estimado, em meticais. O "
      "estudo será financiado com recursos próprios do estudante, "
      "complementados por apoio a solicitar à Universidade Lúrio e a "
      "parceiros do programa de doenças não transmissíveis da província. A "
      "rubrica maior é o subsídio do inquiridor assistente, necessário para "
      "entrevistar em emakhuwa e para a repetição independente das medições "
      "durante os 70 dias de pré-teste e recolha nas três unidades "
      "sanitárias. Seguem-se as fotocópias do caderno de recolha, com 10 "
      "páginas por participante para 531 pessoas, ou seja os 483 da amostra e "
      "os 48 do pré-teste, e a aquisição de dois esfigmomanómetros "
      "oscilométricos de braço com braçadeiras de dois tamanhos, indispensável "
      "para garantir o mesmo procedimento de medição nas três unidades e a "
      "repetição de controlo."),
]
ORCAMENTO = [
    ("Esfigmomanómetro oscilométrico automático de braço", "unidade", 2, 6000),
    ("Braçadeira adicional de tamanho grande", "unidade", 2, 1500),
    ("Pilhas e adaptadores de corrente", "conjunto", 1, 1500),
    ("Fotocópias do caderno de recolha (10 páginas por participante)",
     "página", 5310, 3),
    ("Tradução para emakhuwa e retroversão", "serviço", 3, 2500),
    ("Comunicação com o painel de peritos", "perito", 5, 500),
    ("Formação do inquiridor assistente", "dia", 2, 1500),
    ("Subsídio do inquiridor assistente", "dia", 70, 500),
    ("Transporte do investigador entre as três unidades sanitárias", "dia",
     70, 150),
    ("Comunicação telefónica e internet", "mês", 8, 500),
    ("Material de escritório (pranchetas, pastas, canetas, envelopes)",
     "conjunto", 1, 2500),
    ("Armário com fechadura para arquivo", "unidade", 1, 3500),
    ("Disco externo para cópia de segurança encriptada", "unidade", 1, 2000),
    ("Taxa de submissão ao comité de bioética", "taxa", 1, 5000),
    ("Impressão e encadernação do relatório final", "exemplar", 4, 800),
    ("Cartazes de devolução e apresentação em jornadas", "unidade", 3, 1000),
]
ORCAMENTO_IMPREVISTOS = 0.10

# ----------------------------------------------------- apendices ------------
APENDICES = [
    ("Caderno de recolha de dados", [
        NOTA("Instruções ao entrevistador: aplicar apenas depois da "
             "assinatura do consentimento, em espaço reservado, em português "
             "ou emakhuwa, conforme a preferência do participante. A Secção "
             "VIII, de medição da pressão arterial, é preenchida antes da "
             "entrevista; a Secção IX é preenchida no fim, a partir da "
             "prescrição em vigor e do cartão do doente crónico. Ler as "
             "perguntas tal como estão escritas, sem sugerir respostas. Não "
             "escrever o nome do participante em nenhuma folha."),
        H3("Secção I. Identificação"),
        CAMPO("Código do participante: __________     Unidade sanitária: "
              "( ) 1   ( ) 2   ( ) 3     Data: ___/___/2027"),
        CAMPO("Entrevistador: __________"),
        PERG("Língua da entrevista:", ["Português", "Emakhuwa"]),
        H3("Secção II. Dados sociodemográficos e acesso"),
        PERG("Idade em anos completos:"),
        PERG("Sexo:", ["Masculino", "Feminino"]),
        PERG("Escolaridade concluída:", ["Nenhuma", "Primária", "Secundária",
                                         "Superior"]),
        PERG("Ocupação principal:", ["Emprego formal",
                                     "Conta própria ou comércio",
                                     "Agricultura", "Reformado(a)",
                                     "Sem ocupação", "Outra"]),
        PERG("Tem rendimento regular todos os meses?", ["Sim", "Não"]),
        PERG("Distrito de residência:", ["Cidade de Nampula",
                                         "Outro distrito (qual?) __________"]),
        PERG("Bairro ou localidade de residência:"),
        PERG("Quanto tempo demora, só de ida, de casa até esta unidade "
             "sanitária (minutos)?"),
        PERG("Quanto gasta em transporte na ida e volta a esta unidade "
             "sanitária (meticais)?"),
        H3("Secção III. Dados clínicos e terapêuticos"),
        PERG("Há quanto tempo lhe disseram que tem tensão alta (meses ou "
             "anos)?"),
        PERG("Além da tensão alta, tem alguma destas doenças?",
             ["Diabetes", "Doença dos rins", "Já teve trombose ou ataque "
              "cardíaco", "Outra (qual?) __________", "Nenhuma"]),
        PERG("Já mudou de comprimidos para a tensão no último mês?",
             ["Sim", "Não", "Não sabe"]),
        PERG("Costuma medir a tensão fora da unidade sanitária?",
             ["Sim", "Não"]),
        PERG("Nos últimos 30 dias, usou remédios tradicionais ou de "
             "curandeiro para a tensão?", ["Sim", "Não"]),
        H3("Secção IV. Custo e disponibilidade dos medicamentos"),
        PERG("Onde levanta habitualmente os comprimidos para a tensão?",
             ["Farmácia desta unidade sanitária", "Farmácia privada",
              "Nos dois sítios", "Outro"]),
        PERG("No último mês, quanto pagou do seu bolso pelos comprimidos para "
             "a tensão (meticais)? Escrever zero se não pagou nada:"),
        PERG("Nos últimos três meses, houve alguma vez em que não lhe "
             "entregaram nesta unidade sanitária pelo menos um dos "
             "comprimidos receitados?", ["Sim", "Não", "Não sabe"]),
        PERG("Se sim, o que fez nessa ocasião?",
             ["Comprou numa farmácia privada", "Ficou sem esse comprimido",
              "Tomou menos do que devia", "Voltou noutro dia", "Outra"]),
        PERG("Nos últimos três meses, alguma vez faltou ou se atrasou a uma "
             "consulta por falta de dinheiro para o transporte?",
             ["Sim", "Não"]),
        H3("Secção V. Adesão à terapêutica anti-hipertensora"),
        NOTA("Adaptado da escala de Hill-Bone de adesão à terapêutica "
             "anti-hipertensora de Kim e colaboradores (2000) e da versão "
             "portuguesa de Nogueira-Silva e colaboradores (2016); versão de "
             "trabalho a harmonizar com as versões publicadas antes da "
             "tradução para emakhuwa. Opções: 1 = nunca; 2 = algumas vezes; "
             "3 = muitas vezes; 4 = sempre. Pontuação total de 14 a 56, em "
             "que valores mais elevados indicam pior adesão. Os itens 1 a 9 "
             "formam a subescala de toma da medicação, os itens 10 e 11 a "
             "subescala de comparecimento nas consultas e os itens 12 a 14 a "
             "subescala de consumo de sal."),
        ESCALA(["Esquece-se de tomar os comprimidos para a tensão.",
                "Deixa passar a hora de tomar os comprimidos para a tensão.",
                "Deixa de tomar os comprimidos quando se sente melhor.",
                "Deixa de tomar os comprimidos quando se sente mal.",
                "Deixa de tomar os comprimidos quando está fora de casa.",
                "Fica sem comprimidos para a tensão antes da data de "
                "levantar mais.",
                "Deixa de comprar os comprimidos para a tensão por falta de "
                "dinheiro.",
                "Toma os comprimidos apenas nos dias anteriores à consulta.",
                "Passa mais de três dias seguidos sem tomar os comprimidos.",
                "Falta às consultas marcadas para a tensão.",
                "Falta às consultas de seguimento quando se sente bem.",
                "Come alimentos salgados, como peixe seco ou salgado.",
                "Põe sal na comida já servida no prato.",
                "Come comida preparada fora de casa, de barraca ou "
                "restaurante."],
               ["1", "2", "3", "4"],
               cabecalho_item="Nos últimos 30 dias"),
        H3("Secção VI. Motivos de não adesão e efeitos adversos percebidos"),
        PERG("Qual é o principal motivo por que, às vezes, não toma os "
             "comprimidos para a tensão?",
             ["Esquecimento", "Falta de dinheiro para comprar",
              "Não havia o comprimido na unidade sanitária",
              "Efeitos dos comprimidos", "Sentia-se bem e achou que não "
              "precisava", "Estava a usar remédio tradicional",
              "Outro (qual?) __________", "Não se aplica, toma sempre"]),
        NOTA("Para cada sintoma, perguntar: «Nos últimos 30 dias, teve este "
             "problema e acha que foi causado pelos comprimidos para a "
             "tensão?»"),
        ESCALA(["Tosse seca persistente", "Tonturas ao levantar-se",
                "Inchaço dos pés ou dos tornozelos",
                "Urinar muitas vezes ou de noite", "Dor de cabeça",
                "Cansaço fora do normal", "Palpitações",
                "Cãibras nas pernas", "Diminuição do desejo sexual",
                "Comichão ou manchas na pele"],
               ["Sim", "Não"],
               cabecalho_item="Sintoma nos últimos 30 dias"),
        PERG("Nos últimos 30 dias, deixou de tomar alguma dose por causa "
             "destes problemas?", ["Sim", "Não"]),
        H3("Secção VII. Crenças sobre a doença"),
        NOTA("Adaptado do questionário breve de percepção da doença de "
             "Broadbent e colaboradores (2006); versão de trabalho a "
             "harmonizar com a versão publicada antes da tradução. Cada um "
             "dos oito primeiros itens é respondido numa escala numérica de "
             "0 a 10, mostrada ao participante num cartão com âncoras nos "
             "extremos. Neste estudo, a pontuação global de ameaça percebida "
             "é obtida somando os itens 1, 2, 5, 6 e 8 com os itens 3, 4 e 7 "
             "invertidos, variando de 0 a 80; os itens 3, 4 e 7 são também "
             "analisados isoladamente."),
        PERG("1. Quanto é que a tensão alta afecta a sua vida? "
             "(0 = não afecta nada; 10 = afecta muitíssimo): ______"),
        PERG("2. Quanto tempo pensa que a sua tensão alta vai durar? "
             "(0 = pouquíssimo tempo; 10 = para toda a vida): ______"),
        PERG("3. Quanto controlo sente que tem sobre a sua tensão alta? "
             "(0 = nenhum controlo; 10 = controlo total): ______"),
        PERG("4. Quanto pensa que o tratamento ajuda a sua tensão alta? "
             "(0 = não ajuda nada; 10 = ajuda muitíssimo): ______"),
        PERG("5. Quanto sente sintomas por causa da tensão alta? "
             "(0 = nenhum sintoma; 10 = muitíssimos sintomas): ______"),
        PERG("6. Quanto é que a tensão alta o preocupa? "
             "(0 = não preocupa nada; 10 = preocupa muitíssimo): ______"),
        PERG("7. Até que ponto sente que compreende a sua tensão alta? "
             "(0 = não compreende nada; 10 = compreende muito bem): ______"),
        PERG("8. Quanto é que a tensão alta o afecta emocionalmente, por "
             "exemplo deixando-o triste, assustado ou zangado? "
             "(0 = nada; 10 = muitíssimo): ______"),
        PERG("9. Na sua opinião, quais são as três principais causas da sua "
             "tensão alta? (resposta livre, registar pelas palavras do "
             "participante)"),
        H3("Secção VIII. Ficha de medição da pressão arterial"),
        NOTA("Doente sentado, costas apoiadas, pés no chão, braço apoiado ao "
             "nível do coração, sem falar. Cinco minutos de repouso antes da "
             "primeira leitura e um minuto entre leituras. Braçadeira "
             "ajustada ao perímetro braquial. Na primeira leitura medir nos "
             "dois braços e usar depois o braço com o valor mais elevado. Não "
             "medir nos 30 minutos seguintes a café, tabaco ou esforço "
             "físico."),
        CAMPO("Perímetro braquial (cm): ______     Braçadeira usada: "
              "( ) média   ( ) grande     Braço usado: ( ) direito   "
              "( ) esquerdo"),
        CAMPO("Leitura nos dois braços: direito ____/____ mmHg     esquerdo "
              "____/____ mmHg"),
        CAMPO("1.ª leitura: ____/____ mmHg     2.ª leitura: ____/____ mmHg     "
              "3.ª leitura: ____/____ mmHg"),
        CAMPO("Média da 2.ª e da 3.ª leituras: sistólica ______ mmHg     "
              "diastólica ______ mmHg"),
        CAMPO("Classificação: ( ) controlada (sistólica abaixo de 140 e "
              "diastólica abaixo de 90 mmHg)   ( ) não controlada"),
        CAMPO("Repetição de controlo pelo segundo observador (10% dos "
              "participantes): ____/____ mmHg     Rubrica: ______"),
        CAMPO("Encaminhamento feito no dia: ( ) clínico de serviço, por "
              "valores iguais ou superiores a 180/110 mmHg ou por queixas   "
              "( ) consulta de seguimento   ( ) nenhum"),
        H3("Secção IX. Ficha de revisão da prescrição"),
        CAMPO("Anti-hipertensores prescritos (nome, dose e número de tomas "
              "por dia):"),
        CAMPO("1. __________________________  2. __________________________"),
        CAMPO("3. __________________________  4. __________________________"),
        CAMPO("Número de anti-hipertensores: ______     Número total de "
              "comprimidos por dia: ______"),
        CAMPO("Classes prescritas: ( ) diurético tiazídico ou análogo   "
              "( ) inibidor da enzima de conversão da angiotensina ou "
              "antagonista dos receptores da angiotensina   ( ) bloqueador "
              "dos canais de cálcio   ( ) beta bloqueador   ( ) outra"),
        CAMPO("Combinação em comprimido único: ( ) Sim   ( ) Não"),
        CAMPO("Datas dos levantamentos dos últimos três meses: ___/___/____   "
              "___/___/____   ___/___/____"),
        CAMPO("Atraso de 7 ou mais dias em algum levantamento: ( ) Sim   "
              "( ) Não   ( ) Sem registo"),
        CAMPO("Data da última alteração do esquema terapêutico: ___/___/____   "
              "( ) Sem registo"),
    ]),
    ("Folha de informação ao participante", [
        P("Título do estudo: Controlo da pressão arterial e adesão à "
          "terapêutica anti-hipertensora em adultos seguidos em consultas "
          "externas na cidade de Nampula, de Abril a Junho de 2027. "
          "Investigador: [Nome do(a) estudante], estudante de Licenciatura em "
          "Farmácia da Faculdade de Ciências de Saúde da Universidade Lúrio, "
          "sob orientação de [Nome e grau académico do(a) orientador(a)]."),
        P("Convidamo-lo(a) a participar num estudo que pretende saber quantas "
          "pessoas com tensão alta seguidas nesta consulta têm a tensão "
          "controlada e que dificuldades encontram para tomar os comprimidos, "
          "como o número de comprimidos, o preço, a falta do medicamento na "
          "farmácia ou o esquecimento. Os resultados servirão para melhorar o "
          "apoio dado na consulta e na farmácia."),
        P("Se aceitar, mediremos a sua tensão arterial três vezes, com um "
          "aparelho de braço, depois de cinco minutos sentado(a) em repouso, e "
          "faremos uma entrevista de cerca de 25 minutos, num espaço "
          "reservado, enquanto aguarda a sua vez. Consultaremos ainda a sua "
          "receita e o seu cartão do doente crónico, apenas para registar os "
          "medicamentos receitados e as datas em que os levantou. Diremos "
          "sempre qual foi o valor da sua tensão e escrevê-lo-emos no seu "
          "cartão."),
        P("A participação é voluntária. Pode recusar ou desistir a qualquer "
          "momento, sem dar explicações, e continuará a receber o mesmo "
          "atendimento e os mesmos medicamentos. Pode não responder a qualquer "
          "pergunta. O seu nome não será escrito em nenhuma folha, que terá "
          "apenas um código, e as informações serão guardadas em lugar fechado "
          "e apresentadas apenas em conjunto, sem identificar ninguém. Não "
          "receberá pagamento. O risco é mínimo: a braçadeira aperta o braço "
          "durante alguns segundos e algumas perguntas podem causar "
          "desconforto. Se a sua tensão estiver muito alta ou se tiver "
          "queixas, acompanhamo-lo(a) no mesmo dia ao clínico de serviço; se "
          "estiver acima da meta sem queixas, será informado(a) e encaminhado "
          "para a sua consulta."),
        P("Para esclarecimentos, pode contactar o investigador pelo telefone "
          "[preencher] ou o Comité Institucional de Bioética para a Saúde da "
          "Universidade Lúrio pelo telefone [preencher]."),
    ]),
    ("Termo de consentimento livre e esclarecido", [
        P("Declaro que me foi lida e explicada a folha de informação sobre o "
          "estudo «Controlo da pressão arterial e adesão à terapêutica "
          "anti-hipertensora em adultos seguidos em consultas externas na "
          "cidade de Nampula, de Abril a Junho de 2027», numa língua que "
          "compreendo, que pude fazer perguntas e que as minhas dúvidas foram "
          "esclarecidas. Compreendo que a participação é voluntária, que posso "
          "desistir a qualquer momento sem prejuízo do meu atendimento e que "
          "as minhas informações são confidenciais. Autorizo a medição da "
          "minha tensão arterial e a consulta da minha receita e do meu cartão "
          "do doente crónico para os fins descritos."),
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
        NOTA("Este termo é feito em duas vias: uma fica com o participante e a "
             "outra é guardada pelo investigador, separada do caderno de "
             "recolha."),
    ]),
    ("Pedido de autorização institucional", [
        CAMPO("Ao Excelentíssimo Senhor Director da [designação da unidade "
              "sanitária]"),
        CAMPO("Nampula, ____ de ________________ de 2027"),
        CAMPO("Assunto: Pedido de autorização para realização de estudo"),
        P("Eu, [Nome do(a) estudante], estudante do curso de Licenciatura em "
          "Farmácia da Faculdade de Ciências de Saúde da Universidade Lúrio, "
          "venho solicitar a Vossa Excelência autorização para realizar, na "
          "consulta externa de doentes crónicos e na farmácia desta unidade "
          "sanitária, o estudo intitulado «Controlo da pressão arterial e "
          "adesão à terapêutica anti-hipertensora em adultos seguidos em "
          "consultas externas na cidade de Nampula, de Abril a Junho de "
          "2027», sob orientação de [Nome e grau académico do(a) "
          "orientador(a)]."),
        P("O estudo consiste em medir a pressão arterial e entrevistar 483 "
          "adultos hipertensos no conjunto de três unidades sanitárias da "
          "cidade, seleccionados por amostragem sistemática à chegada à "
          "consulta, e em rever a receita e o cartão do doente crónico para "
          "registar os medicamentos prescritos e as datas de levantamento. A "
          "recolha decorre entre 1 de Abril e 30 de Junho de 2027, em espaço "
          "reservado, sem interferir com o funcionamento da consulta nem da "
          "farmácia, e só começa depois do parecer favorável do Comité "
          "Institucional de Bioética para a Saúde da Universidade Lúrio. "
          "Solicito ainda a indicação do número de consultas mensais de "
          "doentes hipertensos adultos e do suporte de registo da dispensa em "
          "uso na farmácia, necessários ao plano de amostragem."),
        P("Comprometo-me a garantir a confidencialidade dos doentes, a não "
          "retirar documentos da unidade sanitária, a não registar nomes, a "
          "comunicar a cada participante o valor da sua pressão arterial e a "
          "encaminhar ao clínico de serviço quem apresentar valores muito "
          "elevados ou queixas, e a entregar à direcção um relatório com os "
          "resultados agregados e uma proposta de intervenção farmacêutica."),
        CAMPO("Pede deferimento."),
        CAMPO("O(A) estudante: ______________________________"),
        CAMPO("O(A) orientador(a): ______________________________"),
        NOTA("Pedidos semelhantes serão dirigidos à Direcção Provincial de "
             "Saúde de Nampula e ao Serviço Distrital de Saúde, Mulher e "
             "Acção Social da Cidade de Nampula."),
    ]),
]
