# -*- coding: utf-8 -*-
"""
Tema 16: Disponibilidade de medicamentos essenciais e rupturas de stock em
unidades sanitarias da cidade de Nampula (Farmacia Hospitalar e Gestao
Farmaceutica). Inquerito transversal a unidades sanitarias, com verificacao
fisica no dia da visita e revisao retrospectiva das fichas de stock de 2026.

Compor e validar:   python _motor/motor.py _conteudo/tema_16.py
Verificar fontes:   python _motor/refs.py verificar _conteudo/tema_16.py
"""
from blocos import (CAMPO, FORMULA, H3, LISTA, NOTA, P, PERG, QUADRO,
                    TABELA)

NUMERO = 16
SLUG = "Disponibilidade_Medicamentos_Essenciais_Rupturas_Stock_Nampula"
TITULO = ("Disponibilidade de medicamentos traçadores essenciais e duração "
          "das rupturas de stock nas unidades sanitárias públicas da cidade "
          "de Nampula, 2026 e 2027")
DESENHO = ("Transversal, descritivo e analítico, inquérito a unidades "
           "sanitárias com verificação física e revisão documental das "
           "fichas de stock")

AUTOR = "[Nome do(a) estudante]"
ORIENTADOR = "[Nome e grau académico do(a) orientador(a)]"

# ---------------------------------------------------------------- resumo --
RESUMO = (
    "A falta de medicamentos essenciais nas unidades sanitárias públicas "
    "interrompe tratamentos já iniciados, transfere o custo dos cuidados para "
    "o orçamento das famílias e afasta os doentes dos serviços. Os inquéritos "
    "realizados em África descrevem uma disponibilidade média no sector "
    "público próxima de metade da lista avaliada, muito abaixo da meta "
    "internacional de oitenta por cento, e o único estudo moçambicano "
    "publicado com esta metodologia limitou-se a unidades da capital do país, "
    "pelo que não existe medição equivalente para a cidade de Nampula. O "
    "estudo mede a disponibilidade de trinta medicamentos traçadores no dia "
    "da visita e a frequência e a duração das rupturas de stock nos doze "
    "meses anteriores, nas unidades sanitárias públicas da cidade. O desenho "
    "é transversal, descritivo e analítico, e combina a verificação física "
    "dos medicamentos na farmácia e no depósito de cada unidade com a "
    "revisão retrospectiva das fichas de stock referentes ao ano de 2026, "
    "com trabalho de campo em 2027. Todas as unidades sanitárias públicas da "
    "cidade são estudadas por censo, por serem poucas. A lista de traçadores "
    "é construída a partir da lista nacional de medicamentos essenciais e "
    "dos programas prioritários, segundo critérios explícitos, e reparte-se "
    "em partes iguais entre medicamentos fornecidos pelos programas "
    "verticais e medicamentos de aquisição geral. A unidade de análise é o "
    "par formado por um medicamento e uma unidade sanitária. A qualidade das "
    "fichas é verificada em trinta registos antes da recolha, com regra de "
    "decisão escrita, e um segundo observador repete dez por cento das "
    "contagens. A análise recorre a proporções com intervalos de confiança a "
    "95 por cento, a comparação de grupos e a modelos com efeito aleatório "
    "da unidade. Esperam-se uma linha de base da disponibilidade, a medida "
    "da duração das rupturas e a identificação do ponto do circuito "
    "logístico onde a falha começa.")
PALAVRAS_CHAVE = ["disponibilidade de medicamentos", "gestão de existências",
                  "medicamentos essenciais", "Moçambique",
                  "unidades sanitárias"]
ABSTRACT = (
    "Shortages of essential medicines in public health facilities interrupt "
    "ongoing treatments, shift the cost of care to household budgets and "
    "drive patients away from health services. Surveys carried out in Africa "
    "describe mean availability in the public sector close to half of the "
    "assessed basket, far below the international target of eighty per cent, "
    "and the only Mozambican study published with this methodology was "
    "restricted to facilities in the national capital, so no equivalent "
    "measurement exists for the city of Nampula. This study measures the "
    "availability of thirty tracer medicines on the day of the visit and the "
    "frequency and duration of stock-outs during the previous twelve months "
    "in the public health facilities of the city. The design is "
    "cross-sectional, descriptive and analytical, and combines physical "
    "verification of medicines in the dispensary and store of each facility "
    "with retrospective review of the stock cards covering the year 2026, "
    "with fieldwork in 2027. All public health facilities in the city are "
    "studied as a census, because they are few. The tracer list is built "
    "from the national list of essential medicines and from the priority "
    "programmes, following explicit criteria, and is divided equally between "
    "medicines supplied by vertical programmes and medicines procured "
    "through the general system. The unit of analysis is the medicine and "
    "facility pair. The quality of the stock cards is checked in thirty "
    "records before data collection, under a written decision rule, and a "
    "second observer repeats ten per cent of the counts. Analysis uses "
    "proportions with confidence intervals at 95 per cent, group comparisons "
    "and models with a random facility effect. Expected outputs are a "
    "baseline of availability, a measure of stock-out duration and the "
    "identification of the point in the supply circuit where failure "
    "begins.")
KEYWORDS = ["essential medicines", "health facilities", "medicine "
            "availability", "Mozambique", "stock-outs"]

ABREVIATURAS = [
    ("CCI", "coeficiente de correlação intraclasse"),
    ("CIBS-UniLúrio", "Comité Institucional de Bioética para a Saúde da "
                      "Universidade Lúrio"),
    ("CMAM", "Central de Medicamentos e Artigos Médicos"),
    ("CNBS", "Comité Nacional de Bioética para a Saúde"),
    ("DCI", "denominação comum internacional"),
    ("DEFF", "efeito de desenho (do inglês design effect)"),
    ("DPS", "Direcção Provincial de Saúde"),
    ("IC95%", "intervalo de confiança a 95%"),
    ("LNME", "Lista Nacional de Medicamentos Essenciais"),
    ("MISAU", "Ministério da Saúde"),
    ("OMS", "Organização Mundial da Saúde"),
    ("OR", "odds ratio (razão de possibilidades)"),
    ("SDSMAS", "Serviço Distrital de Saúde, Mulher e Acção Social"),
    ("SPSS", "Statistical Package for the Social Sciences"),
    ("STROBE", "Strengthening the Reporting of Observational Studies in "
               "Epidemiology"),
    ("UI", "unidade internacional"),
]

# ------------------------------------------------------------ referencias --
FONTES = {
    "omseml2025": "World Health Organization. The selection and use of essential medicines, 2025: WHO Model List of Essential Medicines, 24th list [Internet]. Geneva: World Health Organization; 2025 [citado 2026 Set 19]. Disponível em: https://www.who.int/publications/i/item/B09474",
    "onu2021": "United Nations Statistics Division. SDG indicator metadata: indicator 3.b.3, proportion of health facilities that have a core set of relevant essential medicines available and affordable on a sustainable basis [Internet]. New York: United Nations; 2021 [citado 2026 Set 19]. Disponível em: https://unstats.un.org/sdgs/metadata/files/Metadata-03-0B-03.pdf",
    "joosse2023": "Joosse IR, Wirtz VJ, van Mourik AT, Wagner BA, Mantel-Teeuwisse AK, Suleman F, et al. SDG indicator 3.b.3 - an analysis of its robustness and challenges for measuring access to medicines for children. BMC Health Serv Res. 2023;23(1):574. doi:10.1186/s12913-023-09554-w. PMID: 37270535.",
    "albagir2026": "Albagir HA. Availability and affordability of essential medicines in African low- and middle-income countries: a systematic review and meta-analysis (2014-2025). BMC Public Health. 2026;26(1). doi:10.1186/s12889-026-26686-w. PMID: 41749165.",
    "kuwawenaruwa2020": "Kuwawenaruwa A, Wyss K, Wiedenmayer K, Metta E, Tediosi F. The effects of medicines availability and stock-outs on household's utilization of healthcare services in Dodoma region, Tanzania. Health Policy Plan. 2020;35(3):323-333. doi:10.1093/heapol/czz173. PMID: 31942625.",
    "obakiro2026": "Obakiro SB, Kibuuka R, Nakazibwe B, Kanyike AM, Mawejje F, Namugaya M, et al. Essential medicines out of reach: a cross-sectional study of community-level access in Eastern Uganda. BMC Health Serv Res. 2026;26(1):64. doi:10.1186/s12913-026-14145-6. PMID: 41634657.",
    "yeboah2026": "Yeboah M, Bonney RA, Antwi LA, Anane PA, Amponsah OKO, Agyei-Baffour P. Availability and affordability of essential medicines for non-communicable disease management in primary healthcare: Evidence from three municipalities in Ghana. PLoS One. 2026;21(1):e0346140. doi:10.1371/journal.pone.0346140. PMID: 41926511.",
    "omshai2008": "World Health Organization; Health Action International. Measuring medicine prices, availability, affordability and price components, 2nd edition [Internet]. Geneva: World Health Organization; 2008 [citado 2026 Set 19]. Disponível em: https://www.who.int/publications/i/item/WHO-PSM-PAR-2008.3",
    "omshhfa2023": "World Health Organization. Harmonized health facility assessment (HHFA): comprehensive guide [Internet]. Geneva: World Health Organization; 2023 [citado 2026 Set 19]. Disponível em: https://www.who.int/data/data-collection-tools/harmonized-health-facility-assessment",
    "jessen2023": "Jessen N, Sharma A, Jones J, Auala T, Boladuadua S, Jingi A, et al. Access to Essential Medicines and Diagnostic Tests for Cardiovascular Diseases in Maputo City, Mozambique. Glob Heart. 2023;18(1):8. doi:10.5334/gh.1186. PMID: 36874443.",
    "sambo2022": "Sambo J, Bauhofer AFL, Boene SS, Djedje M, Júnior A, Pilale A, et al. Readiness of Mozambique Health Facilities to Address Undernutrition and Diarrhea in Children under Five: Indicators from 2018 and 2021 Survey Data. Healthcare (Basel). 2022;10(7):1200. doi:10.3390/healthcare10071200. PMID: 35885727.",
    "wahlfeld2019": "Wahlfeld CC, Muicha A, Harrison P, Kipp AM, Claquin G, Silva WP, et al. HIV Rapid Diagnostic Test Inventories in Zambézia Province, Mozambique: A Tale of 2 Test Kits. Int J Health Policy Manag. 2019;8(5):267-273. doi:10.15171/ijhpm.2019.07. PMID: 31204445.",
    "wiseman2025": "Wiseman R, Truter I. Drug utilisation research and medicine access in Mozambique: An overview. Explor Res Clin Soc Pharm. 2025;17:100548. doi:10.1016/j.rcsop.2024.100548. PMID: 39759955.",
    "cmam2026": "Central de Medicamentos e Artigos Médicos. Central de Medicamentos e Artigos Médicos: missão e objectivos estratégicos [Internet]. Maputo: Ministério da Saúde; 2026 [citado 2026 Set 19]. Disponível em: https://www.cmam.gov.mz/",
    "misau2017": "Ministério da Saúde. Lista Nacional de Medicamentos Essenciais [Internet]. Maputo: Ministério da Saúde; 2017 [citado 2026 Set 19]. Disponível em: https://www.afro.who.int/sites/default/files/2018-07/LISTA%20NACIONAL%20DE%20MEDICAMENTOS%20ESSENCIAIS%202017.pdf",
    "lei12de2017": "República de Moçambique. Lei n.º 12/2017, de 8 de Setembro: Lei do medicamento, vacinas e outros produtos biológicos para o uso humano. Boletim da República, I Série, n.º 141 [Internet]. Maputo: Imprensa Nacional de Moçambique; 2017 [citado 2026 Set 19]. Disponível em: https://anarme.gov.mz/download/lei-12-2017-de-8-de-setembro-lei-de-medicamento/",
    "ine2021": "Instituto Nacional de Estatística. IV Recenseamento Geral da População e Habitação 2017: resultados definitivos, província de Nampula [Internet]. Nampula: Instituto Nacional de Estatística; 2021 [citado 2026 Set 19]. Disponível em: http://www.sina.gov.mz/wp-content/uploads/2024/05/NAMPULA-RESUTADOS-DEFINITIVOS-DO-CENSO-2017.pdf",
    "das2021": "das Neves Martins Pires PH, Macaringue C, Abdirazak A, Mucufo JR, Mupueleque MA, Zakus D, et al. Covid-19 pandemic impact on maternal and child health services access in Nampula, Mozambique: a mixed methods research. BMC Health Serv Res. 2021;21(1):860. doi:10.1186/s12913-021-06878-3. PMID: 34425807.",
    "sengo2023": "Sengo DB, Salamo ZMA, Dos Santos IIDB, Mate LM, Chivinde SM, Moragues R, et al. Assessment of the distribution of human and material resources for eye health in the public sector in Nampula, Mozambique. Hum Resour Health. 2023;21(1):25. doi:10.1186/s12960-023-00812-w. PMID: 37004070.",
    "tefera2022": "Tefera BB, Tafere C, Yehualaw A, Mebratu E, Chanie Y, Ayele S, et al. Availability and stock-out duration of essential medicines in Shegaw Motta general hospital and Motta Health Centre, North West Ethiopia. PLoS One. 2022;17(9):e0274776. doi:10.1371/journal.pone.0274776. PMID: 36112721.",
    "kefale2019": "Kefale AT, Shebo HH. Availability of essential medicines and pharmaceutical inventory management practice at health centers of Adama town, Ethiopia. BMC Health Serv Res. 2019;19(1):254. doi:10.1186/s12913-019-4087-0. PMID: 31023314.",
    "hailu2020": "Hailu AD, Mohammed SA. Availability, price, and affordability of WHO priority maternal and child health medicine in public health facilities of Dessie, north-East Ethiopia. BMC Med Inform Decis Mak. 2020;20(1):221. doi:10.1186/s12911-020-01247-2. PMID: 32917201.",
    "mekonnen2024": "Mekonnen BA, Worku MC, Tefera BB. Evaluation of logistics management information system and availability of non-program tracer drugs in public health facilities in Bahir Dar City, North West Ethiopia. PLoS One. 2024;19(4):e0302319. doi:10.1371/journal.pone.0302319. PMID: 38635541.",
    "umer2023": "Umer A, Mohammed H, Yazie B, Angaw DA, Gonete TZ, Endehabtu BF, et al. Assessment of Availability of Tracer Drugs and Basic Diagnostics at Public Primary Health Care Facilities in Ethiopia During COVID-19 Pandemic. Ethiop J Health Sci. 2023;33(Spec Iss 2):61-70. doi:10.4314/ejhs.v33i2.7S. PMID: 38352669.",
    "gutesa2024": "Gutesa A, Jebena T, Kebede O. Inventory Management Performance for Tracer Medicines in Public Health Facilities of Southwest Shewa Zone Oromia Region, Ethiopia: A mixed study. SAGE Open Med. 2024;12:20503121241274041. doi:10.1177/20503121241274041. PMID: 39263640.",
    "demessie2020": "Demessie MB, Workneh BD, Mohammed SA, Hailu AD. Availability of Tracer Drugs and Implementation of Their Logistic Management Information System in Public Health Facilities of Dessie, North-East Ethiopia. Integr Pharm Res Pract. 2020;9:83-92. doi:10.2147/IPRP.S262266. PMID: 32850300.",
    "ayako2023": "Ayako JA, Karimi PN, Rutungwa E, Ngenzi JL, Nyongesa KW, Jillo RH, et al. Factors affecting the availability of tracer health commodities in public facilities at Tana River County, Kenya. J Pharm Policy Pract. 2023;16(1):145. doi:10.1186/s40545-023-00658-6. PMID: 37968772.",
    "mukundiyukuri2020": "Mukundiyukuri JP, Irakiza JJ, Nyirahabimana N, Ng'ang'a L, Park PH, Ngoga G, et al. Availability, Costs and Stock-Outs of Essential NCD Drugs in Three Rural Rwandan Districts. Ann Glob Health. 2020;86(1):123. doi:10.5334/aogh.2729. PMID: 33024709.",
    "mohan2024": "Mohan S, Mangal TD, Colbourn T, Chalkley M, Chimwaza C, Collins JH, et al. Factors associated with medical consumable availability in level 1 facilities in Malawi: a secondary analysis of a facility census. Lancet Glob Health. 2024;12(6):e1027-e1037. doi:10.1016/S2214-109X(24)00095-0. PMID: 38762283.",
    "melaku2024": "Melaku T, Mekonnen Z, Terefe Tucho G, Mecha M, Årdal C, Jahre M. Availability of essential, generic medicines before and during COVID-19 at selected public pharmaceutical supply agencies in Ethiopia: a comparative cross-sectional study. BMJ Open. 2024;14(3):e077545. doi:10.1136/bmjopen-2023-077545. PMID: 38443082.",
    "gonah2026": "Gonah L, Nomatshila SC, Mabunda SA, Chitha WW. Essential Medicines Availability, Pricing, and Stock-Outs for Hypertension and Diabetes in Private Retail Pharmacies in Zimbabwe. Int J Environ Res Public Health. 2026;23(2):215. doi:10.3390/ijerph23020215. PMID: 41752297.",
    "iwu2020": "Iwu CJ, Ngcobo N, McCaul M, Mangqalaza H, Magwaca A, Chikte U, et al. Vaccine stock management in primary health care facilities in OR Tambo District, Eastern Cape, South Africa. Vaccine. 2020;38(25):4111-4118. doi:10.1016/j.vaccine.2020.04.019. PMID: 32362525.",
    "alemu2021": "Alemu T, Jemal A, Gashe F, Suleman S, Sudhakar S, Fekadu G. Integrated pharmaceutical logistics system implementation in selected health facilities of Ethiopia: The case of four WOLLEGA ZONES. Res Social Adm Pharm. 2021;17(5):956-968. doi:10.1016/j.sapharm.2020.07.026. PMID: 32847732.",
    "dinkashe2022": "Dinkashe FT, Haile K, Adem FM. Availability and affordability of priority lifesaving maternal health medicines in Addis Ababa, Ethiopia. BMC Health Serv Res. 2022;22(1):525. doi:10.1186/s12913-022-07793-x. PMID: 35443654.",
    "serdar2021": "Serdar CC, Cihan M, Yücel D, Serdar MA. Sample size, power and effect size revisited: simplified and practical approaches in pre-clinical, clinical and laboratory studies. Biochem Med (Zagreb). 2021;31(1):010502. doi:10.11613/BM.2021.010502. PMID: 33380887.",
    "mchugh2012": "McHugh ML. Interrater reliability: the kappa statistic. Biochem Med (Zagreb). 2012;22(3):276-82. PMID: 23092060.",
    "von2007": "von Elm E, Altman DG, Egger M, Pocock SJ, Gøtzsche PC, Vandenbroucke JP. The Strengthening the Reporting of Observational Studies in Epidemiology (STROBE) statement: guidelines for reporting observational studies. PLoS Med. 2007;4(10):e296. doi:10.1371/journal.pmed.0040296. PMID: 17941714.",
    "world2025": "World Medical Association. World Medical Association Declaration of Helsinki: Ethical Principles for Medical Research Involving Human Participants. JAMA. 2025;333(1):71-74. doi:10.1001/jama.2024.21972. PMID: 39425955.",
    "lei3de2023": "República de Moçambique. Lei n.º 3/2023, de 8 de Junho: Lei de Investigação em Saúde Humana [Internet]. Maputo: Imprensa Nacional de Moçambique; 2023 [citado 2026 Set 19]. Disponível em: https://anarme.gov.mz/download/lei-3-2023-de-8-de-junho-lei-de-investigacao-em-saude-humana/",
}

SEMINAIS = {
    "omshai2008": ("Manual original da Organização Mundial da Saúde e da "
                   "Health Action International que define a metodologia de "
                   "inquérito de disponibilidade e preços de medicamentos "
                   "usada neste estudo; não tem edição posterior."),
    "von2007": ("Declaração de relato de estudos observacionais em vigor, "
                "sem versão posterior."),
    "mchugh2012": ("Artigo de referência sobre a interpretação do kappa de "
                   "Cohen, usado para fixar o limiar de concordância entre "
                   "observadores."),
}

# ----------------------------------------------------- 1. introducao --------
INTRODUCAO = [
    P("Um medicamento essencial é aquele que satisfaz as necessidades de "
      "saúde prioritárias de uma população e que, por isso, deve estar "
      "permanentemente disponível, na forma farmacêutica adequada, em "
      "quantidade suficiente e a um preço que o doente e o sistema de saúde "
      "possam suportar. A lista modelo da Organização Mundial da Saúde "
      "(OMS), revista de dois em dois anos, fixa o padrão a partir do qual "
      "cada país constrói a sua própria lista nacional e organiza a "
      "aquisição, a distribuição e a prescrição {omseml2025}. A "
      "disponibilidade física é a primeira das condições de acesso: sem o "
      "medicamento na prateleira, a prescrição correcta, o aconselhamento e "
      "a adesão perdem qualquer efeito prático. É esta a razão por que a "
      "comunidade internacional escolheu, para medir o progresso da meta de "
      "acesso a medicamentos, um indicador de unidade sanitária, a proporção "
      "de unidades que dispõem de um conjunto essencial de medicamentos "
      "relevantes, disponíveis e comportáveis de forma sustentável "
      "{onu2021}."),
    P("Medir a disponibilidade exige uma definição operacional estável. A "
      "metodologia do manual da OMS e da Health Action International, "
      "publicada em 2008 e usada desde então em dezenas de países, resolveu "
      "o problema com uma regra simples: um conjunto fixo de medicamentos "
      "traçadores, com forma farmacêutica e dosagem especificadas, é "
      "procurado fisicamente em cada estabelecimento no dia da visita, e a "
      "disponibilidade é a percentagem de traçadores encontrados "
      "{omshai2008}. A mesma lógica foi incorporada nos inquéritos de "
      "prontidão de serviços promovidos pela OMS, que avaliam a existência "
      "de itens traçadores como parte da capacidade instalada das unidades "
      "sanitárias {omshhfa2023}. O trabalho metodológico posterior mostrou "
      "que os resultados são estáveis desde que o cabaz não seja demasiado "
      "pequeno: com menos de doze medicamentos, as pontuações médias sobem "
      "depressa e o intervalo de variação alarga-se, o que torna a "
      "comparação entre unidades pouco informativa {joosse2023}."),
    P("O retrato que estes inquéritos devolvem de África é mau e persistente. "
      "Uma revisão sistemática de 52 estudos realizados em 34 países "
      "africanos de rendimento baixo e médio, entre 2014 e 2025, estimou uma "
      "disponibilidade combinada de 48,1% (IC95% 42,5-53,7) no sector "
      "público e de 70,3% (IC95% 64,1-76,5) no sector privado, muito abaixo "
      "da meta de 80% habitualmente usada como referência; a disponibilidade "
      "foi de 59,1% nos medicamentos para doenças transmissíveis e de apenas "
      "37,4% nos medicamentos para doenças não transmissíveis {albagir2026}. "
      "A diferença entre os dois grupos não é casual: os medicamentos "
      "apoiados por programas verticais com financiamento externo têm "
      "circuitos de aquisição próprios, enquanto os medicamentos de "
      "aquisição geral dependem do orçamento ordinário e são os primeiros a "
      "faltar."),
    P("As consequências da falta não ficam na farmácia. No distrito de "
      "Dodoma, na Tanzânia, a utilização dos serviços de saúde pelos "
      "agregados familiares associou-se à disponibilidade contínua dos "
      "medicamentos essenciais nas unidades da sua área de influência (OR "
      "3,49; IC95% 1,02-12,04), ou seja, as famílias deixam de procurar a "
      "unidade que sabem estar vazia {kuwawenaruwa2020}. No leste do Uganda, "
      "72,5% dos agregados apontaram as rupturas frequentes como o principal "
      "obstáculo ao acesso {obakiro2026}. Quando o medicamento falta no "
      "sector público, o doente compra-o no sector privado, onde, em três "
      "municípios do Gana, os preços das terapêuticas crónicas eram duas a "
      "cinco vezes superiores aos do sector público {yeboah2026}, ou "
      "interrompe simplesmente o tratamento."),
    P("Em Moçambique, a aquisição, o armazenamento e a distribuição dos "
      "medicamentos do Serviço Nacional de Saúde estão centralizados na "
      "Central de Medicamentos e Artigos Médicos (CMAM), que os faz chegar "
      "às unidades sanitárias através de armazéns centrais, provinciais e "
      "distritais {cmam2026}. A selecção obedece à Lista Nacional de "
      "Medicamentos Essenciais (LNME) do Ministério da Saúde (MISAU) "
      "{misau2017} e o enquadramento legal do circuito do medicamento consta "
      "da Lei n.º 12/2017, de 8 de Setembro {lei12de2017}. A investigação "
      "publicada sobre o desempenho deste circuito é escassa e concentra-se "
      "no sul do país {wiseman2025}. Em seis hospitais públicos da cidade de "
      "Maputo, a disponibilidade média dos medicamentos essenciais do "
      "conjunto núcleo internacional foi de 52,6% e a dos medicamentos "
      "cardiovasculares de 20,7% {jessen2023}. Na análise de 1.644 unidades "
      "sanitárias públicas avaliadas pelo inquérito nacional de "
      "disponibilidade e prontidão de serviços de 2018, nenhuma unidade "
      "reunia todos os itens traçadores considerados {sambo2022}."),
    P("A província de Nampula é a mais populosa do país, com 5.758.920 "
      "habitantes recenseados em 2017 {ine2021}, e a sua capital concentra a "
      "procura de cuidados de uma vasta área rural envolvente. Os poucos "
      "estudos locais disponíveis descrevem um sistema com recursos "
      "desigualmente distribuídos e vulnerável a choques externos: a "
      "distribuição do pessoal e do equipamento de saúde ocular na província "
      "mostrou concentração na cidade e escassez nos distritos {sengo2023}, "
      "e a primeira vaga da pandemia de 2020 reduziu de forma mensurável o "
      "acesso aos serviços de saúde materna e infantil na cidade de Nampula "
      "{das2021}. Nenhum destes trabalhos mediu a disponibilidade de "
      "medicamentos nas prateleiras nem a duração das rupturas."),
    P("Existe, portanto, uma lacuna concreta: não há, para as unidades "
      "sanitárias públicas da cidade de Nampula, nenhuma medição da "
      "disponibilidade de medicamentos essenciais feita com uma metodologia "
      "comparável, nem qualquer estimativa de quanto tempo dura uma ruptura "
      "quando ela acontece. Esta segunda dimensão é a que falta na maior "
      "parte dos inquéritos, que se limitam ao dia da visita e deixam por "
      "responder se a unidade esteve sem o medicamento durante três dias ou "
      "durante três meses. O presente estudo propõe-se preencher essa "
      "lacuna, medindo a disponibilidade no dia da visita e reconstruindo, a "
      "partir das fichas de stock, a frequência e a duração das rupturas ao "
      "longo de um ano civil completo."),
]

# ----------------------------------------------------- 2. problema ----------
PROBLEMA = [
    P("Nas unidades sanitárias públicas da cidade de Nampula, a queixa de "
      "que «o medicamento acabou» é parte da experiência corrente de quem "
      "procura cuidados, mas não está quantificada. A farmácia da unidade "
      "recebe os medicamentos do circuito distrital, regista as entradas e "
      "as saídas em fichas de stock e envia periodicamente um balanço; "
      "quando o saldo chega a zero, o doente sai com uma receita que terá de "
      "aviar noutro lado, ou sem tratamento. Sem uma medição sistemática, "
      "nem a direcção da unidade nem o Serviço Distrital de Saúde, Mulher e "
      "Acção Social (SDSMAS) da Cidade de Nampula conseguem distinguir a "
      "falta pontual, resolvida com um empréstimo entre unidades, da falta "
      "prolongada, que denuncia um problema de quantificação, de "
      "financiamento ou de transporte."),
    P("A consequência imediata é clínica. A interrupção de um tratamento "
      "anti-hipertensor ou anti-diabético anula o controlo obtido em meses "
      "de seguimento, e a indisponibilidade de um antibiótico de primeira "
      "linha leva à substituição por alternativas de espectro mais largo, "
      "com custo mais alto e maior pressão de selecção de resistências. A "
      "consequência económica recai sobre o utente, que passa a comprar no "
      "sector privado aquilo que deveria receber gratuitamente. A "
      "consequência institucional é a perda de confiança: as famílias que "
      "encontram a farmácia vazia deixam de se deslocar à unidade, o que "
      "reduz também a cobertura de intervenções que nada têm a ver com "
      "medicamentos {kuwawenaruwa2020,obakiro2026}."),
    P("O que falta saber é elementar e, ainda assim, não está documentado. "
      "Não se sabe que percentagem de uma lista definida de medicamentos "
      "traçadores está fisicamente presente nas unidades sanitárias públicas "
      "da cidade num dia qualquer, nem se essa percentagem difere entre os "
      "medicamentos dos programas verticais e os de aquisição geral, como a "
      "evidência africana sugere {albagir2026}. Não se sabe quantas vezes "
      "cada medicamento esteve em ruptura ao longo de um ano, nem quantos "
      "dias durou cada episódio, informação que só as fichas de stock podem "
      "dar e cuja própria qualidade de preenchimento é, ela mesma, uma "
      "incógnita: noutros contextos, a ficha de stock estava ausente em "
      "mais de quatro quintos das unidades avaliadas {mekonnen2024} e menos "
      "de metade das unidades preenchia as fichas com regularidade "
      "{iwu2020}."),
    P("Sem estes números, qualquer plano de melhoria da gestão farmacêutica "
      "na cidade assenta em impressões. Com eles, é possível identificar os "
      "medicamentos e as unidades que concentram o problema, comparar a "
      "situação com a de outros contextos africanos que usaram a mesma "
      "metodologia e estabelecer uma linha de base que permita avaliar "
      "qualquer intervenção futura."),
]
PERGUNTA = ("Qual é a disponibilidade dos medicamentos traçadores essenciais "
            "no dia da visita e qual a frequência e a duração das rupturas de "
            "stock registadas nos doze meses anteriores nas unidades "
            "sanitárias públicas da cidade de Nampula?")
DELIMITACAO = [
    P("O estudo decorre na cidade de Nampula, província de Nampula, e "
      "abrange todas as unidades sanitárias públicas da cidade que "
      "dispensem medicamentos ao público e mantenham farmácia ou depósito "
      "próprio, sob gestão do SDSMAS da Cidade de Nampula. A população de "
      "estudo não são doentes nem profissionais, mas medicamentos "
      "observados em unidades sanitárias: a unidade de análise é o par "
      "formado por um medicamento traçador e uma unidade sanitária, num "
      "total de trinta medicamentos por unidade visitada."),
    P("O período de observação tem duas componentes. A disponibilidade no "
      "dia da visita é registada durante o trabalho de campo, entre Março e "
      "Junho de 2027, numa única visita por unidade. A frequência e a "
      "duração das rupturas são reconstruídas a partir das fichas de stock "
      "referentes ao período de 1 de Janeiro a 31 de Dezembro de 2026, um "
      "ano civil completo, que cobre a estação chuvosa e a estação seca."),
    P("Ficam fora do estudo o sector privado retalhista e as farmácias "
      "comunitárias, os preços e a comportabilidade dos medicamentos, a "
      "qualidade físico-química dos produtos encontrados, a avaliação "
      "detalhada das condições de armazenamento, que constitui objecto de "
      "estudo autónomo, e qualquer informação individual de doentes. Os "
      "consumíveis médicos, os reagentes de laboratório e as vacinas também "
      "não entram na lista de traçadores, por terem circuitos de aquisição e "
      "de conservação distintos dos medicamentos."),
]

# ----------------------------------------------------- 3. objectivos --------
OBJECTIVO_GERAL = ("Avaliar a disponibilidade de medicamentos traçadores "
                   "essenciais e a duração das rupturas de stock nas "
                   "unidades sanitárias públicas da cidade de Nampula")
OBJECTIVOS_ESPECIFICOS = [
    "Caracterizar as unidades sanitárias públicas da cidade de Nampula "
    "quanto à organização da farmácia e do depósito e ao estado dos "
    "instrumentos de registo de existências",
    "Determinar a disponibilidade dos medicamentos traçadores no dia da "
    "visita, no conjunto das unidades, por unidade sanitária e por grupo "
    "terapêutico",
    "Determinar a frequência e a duração das rupturas de stock dos "
    "medicamentos traçadores nos doze meses do ano de 2026, a partir das "
    "fichas de stock",
    "Comparar a disponibilidade e a duração das rupturas entre os "
    "medicamentos fornecidos pelos programas verticais e os medicamentos de "
    "aquisição geral",
    "Identificar, junto dos responsáveis pela farmácia, os factores "
    "organizacionais e logísticos associados às rupturas observadas",
]

# ----------------------------------------------------- 4. hipoteses ---------
HIPOTESES_INTRO = [
    P("As hipóteses referem-se ao objectivo específico 4, a única "
      "componente formalmente analítica do estudo. A comparação é feita "
      "entre os dois grupos de aquisição definidos na lista de traçadores, "
      "com o mesmo número de medicamentos em cada grupo, e tem em conta o "
      "agrupamento das observações dentro de cada unidade sanitária."),
]
HIPOTESES = [
    ("H0", "não existe diferença estatisticamente significativa na "
           "disponibilidade no dia da visita entre os medicamentos "
           "fornecidos pelos programas verticais e os medicamentos de "
           "aquisição geral nas unidades sanitárias públicas da cidade de "
           "Nampula"),
    ("H1", "existe diferença estatisticamente significativa na "
           "disponibilidade no dia da visita entre os medicamentos "
           "fornecidos pelos programas verticais e os medicamentos de "
           "aquisição geral nas unidades sanitárias públicas da cidade de "
           "Nampula"),
    ("H0", "não existe diferença estatisticamente significativa na duração "
           "acumulada das rupturas em 2026 entre os medicamentos fornecidos "
           "pelos programas verticais e os medicamentos de aquisição geral"),
    ("H1", "existe diferença estatisticamente significativa na duração "
           "acumulada das rupturas em 2026 entre os medicamentos fornecidos "
           "pelos programas verticais e os medicamentos de aquisição geral"),
]
QUESTOES = [
    "Que percentagem dos medicamentos traçadores está fisicamente presente "
    "em cada unidade sanitária no dia da visita e qual a variação entre "
    "unidades?",
    "Quantos episódios de ruptura e quantos dias sem existências "
    "acumulou cada medicamento traçador ao longo de 2026?",
    "Em que estado se encontram as fichas de stock e qual a concordância "
    "entre o saldo registado e a contagem física?",
    "Que factores organizacionais e logísticos são apontados pelos "
    "responsáveis pela farmácia para explicar as rupturas?",
]

# ----------------------------------------------------- 5. justificativa -----
JUSTIFICATIVA_INTRO = [
    P("O estudo justifica-se por produzir, com um desenho simples e "
      "barato, informação que hoje não existe e que é imediatamente "
      "utilizável por quem gere o circuito do medicamento na cidade."),
]
JUSTIFICATIVA = {
    "cientifica": [
        P("A literatura africana sobre disponibilidade de medicamentos é "
          "abundante mas desequilibrada: a esmagadora maioria dos estudos "
          "mede apenas a disponibilidade no dia da visita e um número muito "
          "menor reconstrói a duração das rupturas, indicador que exige o "
          "trabalho mais moroso de leitura das fichas de stock "
          "{tefera2022,kefale2019,hailu2020}. Ao medir as duas dimensões na "
          "mesma amostra de unidades, o estudo permite verificar se a "
          "fotografia do dia da visita é um bom substituto da situação ao "
          "longo do ano, questão metodológica ainda em aberto e com "
          "consequências directas para o desenho de inquéritos futuros."),
        P("Acresce a quase ausência de evidência moçambicana. A revisão "
          "disponível sobre investigação em utilização de medicamentos e "
          "acesso em Moçambique descreve um campo pouco desenvolvido e "
          "geograficamente concentrado {wiseman2025}, e o único inquérito "
          "publicado com metodologia comparável foi feito em Maputo "
          "{jessen2023}. Um estudo conduzido no norte do país, com uma lista "
          "de traçadores construída segundo critérios explícitos e "
          "comparável com a de outros inquéritos, alarga a base empírica "
          "disponível para a região."),
    ],
    "academica": [
        P("Para a Faculdade de Ciências de Saúde da Universidade Lúrio, o "
          "trabalho exercita competências centrais do perfil do licenciado "
          "em Farmácia que raramente são avaliadas em trabalho de campo: "
          "leitura crítica de uma lista nacional de medicamentos essenciais, "
          "construção de uma lista de traçadores, contagem física, "
          "reconciliação entre existências e registos e interpretação de "
          "indicadores de gestão de existências. São competências exigidas a "
          "qualquer farmacêutico que venha a assumir a farmácia de uma "
          "unidade sanitária ou um depósito distrital."),
        P("O protocolo deixa ainda instalado um instrumento reutilizável. A "
          "lista de traçadores, a ficha de verificação e a grelha de leitura "
          "das fichas de stock podem ser aplicadas noutros distritos da "
          "província ou repetidas na mesma cidade ao fim de dois anos, o que "
          "transforma um trabalho de fim de curso numa linha de base e abre "
          "caminho a estudos de série temporal."),
    ],
    "social": [
        P("Quem suporta o custo de uma ruptura é o utente. Nas unidades "
          "públicas moçambicanas, a maior parte dos medicamentos essenciais "
          "é dispensada sem encargo directo; quando falta, o doente compra "
          "no sector privado a preços que, em contextos africanos "
          "comparáveis, chegam a ser várias vezes superiores {yeboah2026} ou "
          "interrompe o tratamento. Nas doenças crónicas, essa interrupção "
          "traduz-se em descompensações evitáveis; nas doenças agudas da "
          "infância, num atraso que pode ser fatal."),
        P("A perda de confiança agrava o problema. A associação entre "
          "disponibilidade contínua de medicamentos e utilização dos "
          "serviços {kuwawenaruwa2020} mostra que a farmácia vazia afasta as "
          "famílias de toda a oferta da unidade, incluindo a vacinação e o "
          "seguimento da gravidez. Identificar os medicamentos e as unidades "
          "com pior desempenho permite dirigir a correcção para onde ela tem "
          "maior efeito social."),
    ],
    "politica": [
        P("O indicador que o estudo produz é directamente comparável com o "
          "indicador internacional de acesso a medicamentos, que mede a "
          "proporção de unidades sanitárias com um conjunto essencial de "
          "medicamentos disponível de forma sustentável {onu2021}. Um valor "
          "local para a cidade de Nampula dá ao SDSMAS e à Direcção "
          "Provincial de Saúde (DPS) de Nampula um número próprio para "
          "confrontar com a meta de 80% e para incluir nos instrumentos de "
          "planificação."),
        P("A separação entre medicamentos de programas verticais e "
          "medicamentos de aquisição geral tem, por si, uma leitura de "
          "política. Se a diferença observada em África {albagir2026} se "
          "confirmar na cidade, fica demonstrado que o problema não é de "
          "capacidade técnica das unidades, que gerem bem o que recebe "
          "financiamento dedicado, mas de financiamento e quantificação do "
          "cabaz geral, o que desloca a recomendação do nível da unidade "
          "para o nível distrital e provincial."),
    ],
}

# ----------------------------------------------------- 6. revisao -----------
REVISAO = [
    ("Medicamentos essenciais: conceito, selecção e a lista nacional "
     "moçambicana", [
         P("O conceito de medicamento essencial nasceu da constatação de que "
           "nenhum sistema de saúde consegue disponibilizar todos os "
           "produtos registados no seu mercado e de que a selecção "
           "criteriosa de um número limitado de medicamentos, escolhidos "
           "pela relevância para a carga de doença, pela eficácia e "
           "segurança demonstradas e pelo custo comparado, melhora o acesso "
           "e a qualidade da terapêutica. A lista modelo da OMS, na sua "
           "vigésima quarta edição, organiza esses medicamentos por grupo "
           "terapêutico e distingue os que são indispensáveis em qualquer "
           "nível de cuidados daqueles que exigem meios de diagnóstico ou "
           "vigilância especializados {omseml2025}. A lista não é uma "
           "prescrição rígida: cada país adapta-a ao seu perfil "
           "epidemiológico, à organização da sua rede e à capacidade "
           "financeira do seu sistema."),
         P("Em Moçambique, essa adaptação está materializada na LNME do "
           "MISAU, que define, para cada nível de atendimento, os "
           "medicamentos que devem existir, com a respectiva forma "
           "farmacêutica e dosagem, e que serve simultaneamente de "
           "referência à prescrição e de base à quantificação das "
           "necessidades {misau2017}. A lista é o documento a partir do qual "
           "se decide o que deve estar na prateleira de um centro de saúde, "
           "e é por isso o ponto de partida obrigatório para construir "
           "qualquer lista de medicamentos traçadores destinada a medir "
           "disponibilidade. Ao lado dela funcionam os programas nacionais "
           "de combate à malária, à tuberculose e à infecção pelo vírus da "
           "imunodeficiência humana, de saúde materna e infantil e de "
           "planeamento familiar, cujos medicamentos seguem circuitos de "
           "quantificação e financiamento parcialmente autónomos."),
         P("O enquadramento jurídico do medicamento, desde o registo até à "
           "dispensa, consta da Lei n.º 12/2017, de 8 de Setembro, que fixa "
           "as competências da autoridade reguladora e as obrigações dos "
           "estabelecimentos que manipulam medicamentos {lei12de2017}. É "
           "neste quadro que se inscreve a obrigação prática de manter "
           "registos de entrada e saída dos produtos, sem os quais não é "
           "possível reconstruir o histórico de existências de uma unidade "
           "sanitária nem responsabilizar quem a gere."),
     ]),
    ("Disponibilidade e ruptura de stock: definições operacionais e "
     "indicadores", [
         P("A disponibilidade de um medicamento numa unidade sanitária pode "
           "ser medida de duas maneiras, que respondem a perguntas "
           "diferentes. A disponibilidade no ponto, ou no dia da visita, é a "
           "proporção de medicamentos de uma lista definida que se encontram "
           "fisicamente presentes no momento em que o observador visita a "
           "unidade; é a medida do manual da OMS e da Health Action "
           "International e a que permite comparações entre países, porque "
           "não depende da existência nem da qualidade de registos "
           "{omshai2008}. A disponibilidade no período é a proporção do "
           "tempo de um intervalo definido, habitualmente seis ou doze "
           "meses, em que o medicamento esteve efectivamente disponível; "
           "obriga a ler registos e é, por isso, mais exigente, mas evita "
           "que uma entrega feita na véspera da visita disfarce meses de "
           "ausência."),
         P("A distância entre as duas medidas pode ser grande ou pequena, "
           "consoante o contexto. Em Dessie, no nordeste da Etiópia, um "
           "inquérito a 45 medicamentos prioritários de saúde materna e "
           "infantil obteve 34,02% de disponibilidade no período e 33,5% no "
           "ponto, valores quase coincidentes, mas com uma média de 3,9 "
           "episódios de ruptura por medicamento e 128,9 dias de ausência "
           "{hailu2020}. Noutros estudos a diferença é maior, o que mostra "
           "que a fotografia do dia da visita não substitui, sem "
           "verificação, a história do ano."),
         P("A ruptura de stock é o acontecimento que liga as duas medidas. "
           "Define-se operacionalmente como o período contínuo em que o "
           "saldo do medicamento na unidade é zero, e caracteriza-se por "
           "duas grandezas independentes: a frequência, ou número de "
           "episódios no intervalo considerado, e a duração, em dias, de "
           "cada episódio e do conjunto. A distinção é decisiva para o "
           "diagnóstico do problema: rupturas frequentes mas curtas "
           "apontam para erros de quantificação e para pontos de encomenda "
           "mal fixados, ao passo que rupturas raras mas longas apontam "
           "para falhas de financiamento, de aquisição central ou de "
           "transporte. Num estudo etíope que mediu explicitamente as duas "
           "grandezas, a duração média das rupturas em seis meses foi de "
           "38,8 dias num hospital, com episódios entre 10 e 157 dias, e de "
           "11,2 dias num centro de saúde {tefera2022}."),
         P("O indicador internacional de acesso a medicamentos adoptou a "
           "lógica da unidade sanitária, definindo-se como a proporção de "
           "unidades que dispõem de um conjunto essencial de medicamentos "
           "relevantes, disponíveis e comportáveis de forma sustentável "
           "{onu2021}. A mesma abordagem por itens traçadores está "
           "incorporada nos inquéritos de avaliação harmonizada de unidades "
           "sanitárias promovidos pela OMS, que verificam a existência de "
           "medicamentos e de meios de diagnóstico como parte da capacidade "
           "instalada {omshhfa2023}. O trabalho de validação deste tipo de "
           "indicador mostrou que a pontuação média de uma unidade é estável "
           "enquanto o cabaz mantiver pelo menos doze medicamentos, e que "
           "abaixo desse número as pontuações sobem e a sua dispersão "
           "aumenta {joosse2023}, o que fornece um critério objectivo para "
           "decidir a dimensão mínima de uma lista de traçadores."),
     ]),
    ("Magnitude do problema em África e em Moçambique", [
         P("A síntese quantitativa mais recente da evidência africana reuniu "
           "52 estudos de 34 países de rendimento baixo e médio publicados "
           "entre 2014 e 2025 e estimou uma disponibilidade combinada de "
           "48,1% (IC95% 42,5-53,7) no sector público, contra 70,3% (IC95% "
           "64,1-76,5) no sector privado, com heterogeneidade elevada entre "
           "estudos; a disponibilidade foi de 59,1% nos medicamentos para "
           "doenças transmissíveis e de 37,4% nos medicamentos para doenças "
           "não transmissíveis {albagir2026}. Nenhum destes valores se "
           "aproxima da meta de 80% que serve de referência aos planos "
           "nacionais de acesso a medicamentos."),
         P("Os inquéritos nacionais confirmam o retrato e acrescentam a "
           "dispersão entre unidades. Na Etiópia, a disponibilidade média de "
           "medicamentos traçadores nas unidades primárias foi de 77,6%, mas "
           "apenas 2,8% das unidades tinham a lista completa {umer2023}. Em "
           "Adama, a disponibilidade no dia da visita foi de 76,3% e a "
           "duração média das rupturas nos doze meses anteriores foi de 40,6 "
           "dias, com um extremo de 144 dias para os sais de reidratação "
           "oral e um mínimo de 1,4 dias para o paracetamol {kefale2019}. Em "
           "Bahir Dar, 78,68% dos traçadores de aquisição geral estavam "
           "disponíveis no dia da visita e a pomada oftálmica de "
           "tetraciclina acumulou uma ruptura média de 69,64 dias "
           "{mekonnen2024}. Em três distritos rurais do Ruanda, a "
           "disponibilidade foi de 71% nos centros de saúde e 78% nos "
           "hospitais distritais, com 77% dos centros a registarem pelo "
           "menos uma ruptura de amlodipina e de metformina e medianas de "
           "duração entre 9 e 72 dias {mukundiyukuri2020}."),
         P("A evidência moçambicana é escassa e localizada. O inquérito "
           "conduzido em Maputo com uma versão adaptada da metodologia da "
           "OMS e da Health Action International encontrou, nos seis "
           "hospitais públicos da cidade, uma disponibilidade média de 52,6% "
           "nos medicamentos essenciais do conjunto núcleo e de 20,7% nos "
           "medicamentos cardiovasculares, com valores mais altos no sector "
           "privado {jessen2023}. A análise das 1.644 unidades sanitárias "
           "públicas avaliadas pelo inquérito nacional de disponibilidade e "
           "prontidão de serviços de 2018 mostrou que nenhuma unidade reunia "
           "todos os itens traçadores exigidos para os serviços de nutrição "
           "e de tratamento da diarreia na criança {sambo2022}. A vigilância "
           "de existências de testes rápidos em 75 unidades da província da "
           "Zambézia, entre 2015 e 2017, encontrou existências adequadas em "
           "mais de 89% do tempo, mas com risco desigual entre os dois "
           "testes usados no algoritmo (OR 1,82; IC95% 1,40-2,38 para o "
           "teste inicial) {wahlfeld2019}. Falta, para o norte do país, "
           "qualquer medição equivalente centrada em medicamentos."),
     ]),
    ("Determinantes das rupturas: cadeia de abastecimento, informação "
     "logística e recursos da unidade", [
         P("As rupturas raramente têm uma causa única. A análise secundária "
           "de um censo de unidades do nível primário no Malawi, com 130 "
           "consumíveis, mostrou que a disponibilidade dependia de "
           "características estruturais mensuráveis: as unidades com "
           "farmacêutico ou técnico de farmácia tinham maior probabilidade "
           "de ter o produto do que aquelas em que o depósito era gerido por "
           "um auxiliar (OR 1,85; IC95% 1,40-2,44), e as unidades de nível "
           "superior superavam os centros de saúde simples (OR 1,64; IC95% "
           "1,37-1,97) {mohan2024}. No Quénia, um censo de 62 unidades de "
           "um condado obteve uma disponibilidade média de 68,73% e "
           "identificou a formação do pessoal em gestão de produtos e a "
           "presença de técnico de farmácia como factores associados "
           "{ayako2023}."),
         P("A qualidade do sistema de informação logística é o segundo "
           "determinante recorrente. Em Bahir Dar, a ficha de registo de "
           "existências estava presente em apenas duas de doze unidades "
           "avaliadas {mekonnen2024}; no Sudoeste de Oromia, a exactidão do "
           "inventário foi de 76% nos hospitais e 72,5% nos centros de "
           "saúde, com uma taxa média de ruptura de 24,99% e apenas um "
           "quarto das unidades a cumprir os critérios de armazenamento "
           "{gutesa2024}; em Dessie, 77,8% dos medicamentos traçadores "
           "tinham ficha de prateleira, das quais 86% estavam actualizadas, "
           "e a discrepância entre a contagem física e o saldo registado "
           "variou entre 0% e 100% {demessie2020}. A implementação de um "
           "sistema logístico integrado em unidades etíopes melhorou "
           "indicadores de registo e de reposição, mas manteve lacunas de "
           "formação e de supervisão {alemu2021}, e a revisão africana "
           "estimou que as intervenções de digitalização da cadeia de "
           "abastecimento melhoraram a disponibilidade em cerca de um terço "
           "{albagir2026}."),
         P("O terceiro grupo de determinantes é externo à unidade. Choques "
           "de oferta propagam-se rapidamente até à prateleira: em agências "
           "públicas de abastecimento etíopes, a disponibilidade média de um "
           "cabaz de medicamentos genéricos para doenças crónicas caiu de "
           "67,4% antes da pandemia de 2020 para 43,3% (IC95% 37,1-49,5) "
           "durante a pandemia, e os dias sem existências por mês subiram de "
           "11,7 (IC95% 9,9-13,5) para 15,7 (IC95% 13,2-18,2) {melaku2024}. "
           "Na cidade de Nampula, a mesma pandemia reduziu o acesso aos "
           "serviços de saúde materna e infantil {das2021}, o que torna "
           "plausível um efeito paralelo sobre o abastecimento. A "
           "regularidade das entregas, a quantidade efectivamente recebida "
           "face à requisitada e a distância ao depósito de origem completam "
           "o quadro de factores que qualquer estudo local deve registar."),
     ]),
    ("Consequências clínicas, económicas e de confiança", [
         P("A primeira consequência de uma ruptura é a interrupção do "
           "tratamento. Nas doenças crónicas, essa interrupção desfaz o "
           "controlo tensional ou glicémico conseguido ao longo de meses e "
           "aumenta o risco de complicações agudas; a evidência africana "
           "mostra precisamente que são os medicamentos das doenças não "
           "transmissíveis os menos disponíveis, com 37,4% contra 59,1% nos "
           "medicamentos das doenças transmissíveis {albagir2026}. Nas "
           "doenças agudas, a ausência do medicamento de primeira linha "
           "obriga à substituição por alternativas menos adequadas, com "
           "efeitos sobre a eficácia, o custo e a pressão de selecção de "
           "resistências."),
         P("A segunda consequência é económica e recai sobre o utente. "
           "Quando o sector público não tem o produto, o doente recorre ao "
           "sector privado, onde a disponibilidade é maior mas o preço "
           "também: em três municípios do Gana, os medicamentos para "
           "doenças crónicas custavam no privado duas a cinco vezes mais do "
           "que no sector público, e a probabilidade de encontrar preços "
           "incomportáveis era significativamente maior nas unidades "
           "privadas {yeboah2026}. Em farmácias privadas do Zimbabué, a "
           "maior parte dos traçadores para hipertensão e diabetes estava "
           "disponível em 80% ou mais dos estabelecimentos e as rupturas "
           "duravam em média menos de três dias por mês, o que confirma a "
           "assimetria entre sectores e o papel do privado como recurso de "
           "substituição {gonah2026}. Em Addis Abeba, a avaliação de "
           "medicamentos prioritários de saúde materna mostrou que a baixa "
           "disponibilidade no sector público se associava a encargos "
           "elevados para as famílias {dinkashe2022}."),
         P("A terceira consequência é a erosão da confiança na unidade "
           "sanitária. No leste do Uganda, apenas 8,6% dos agregados "
           "familiares reuniam todas as condições de acesso ao medicamento "
           "de que precisavam, e 72,5% apontaram as rupturas frequentes como "
           "obstáculo principal {obakiro2026}. Na Tanzânia, a utilização dos "
           "serviços de saúde pelos agregados esteve associada à "
           "disponibilidade contínua dos medicamentos essenciais nas "
           "unidades da sua área (OR 3,49; IC95% 1,02-12,04) "
           "{kuwawenaruwa2020}. O efeito não se limita ao medicamento em "
           "falta: a família que desiste de se deslocar deixa também de "
           "aceder à vacinação, ao seguimento da gravidez e ao rastreio."),
     ]),
    ("O circuito do medicamento em Moçambique e os registos na unidade "
     "sanitária", [
         P("A CMAM é a instituição do MISAU responsável pela planificação, "
           "aquisição, armazenagem, conservação e distribuição dos "
           "medicamentos e produtos de saúde do Serviço Nacional de Saúde, "
           "com um armazém central e uma rede de distribuição que desce ao "
           "nível provincial e distrital {cmam2026}. A unidade sanitária "
           "situa-se no fim desta cadeia: recebe periodicamente os produtos "
           "do nível distrital ou provincial, guarda-os no seu depósito, "
           "transfere quantidades de trabalho para a farmácia de dispensa e "
           "presta contas do consumo através de um balanço periódico que "
           "serve de base à reposição."),
         P("Os instrumentos que sustentam este circuito ao nível da unidade "
           "são a ficha de stock de cada produto, onde se registam as "
           "entradas, as saídas e o saldo, e o mapa periódico de balanço e "
           "requisição, que resume o movimento e fundamenta o pedido "
           "seguinte. É a ficha de stock que permite reconstruir, a "
           "posteriori, o dia em que o saldo chegou a zero e o dia em que "
           "foi reposto, e por isso é a fonte indispensável para medir a "
           "duração das rupturas. A sua utilidade depende inteiramente da "
           "disciplina de preenchimento: em unidades primárias da África do "
           "Sul, menos de metade das unidades visitadas preenchia as fichas "
           "com regularidade, apesar de estarem disponíveis em todas, e 77% "
           "das unidades registaram pelo menos uma ruptura de vacinas "
           "{iwu2020}."),
         P("A investigação moçambicana sobre este circuito é limitada. A "
           "revisão do campo da utilização de medicamentos e do acesso em "
           "Moçambique descreve um número reduzido de estudos, concentrados "
           "em Maputo e em temas de prescrição, e assinala a falta de "
           "trabalho sobre a gestão de existências ao nível da unidade "
           "{wiseman2025}. O estudo de vigilância de existências na "
           "Zambézia demonstrou, porém, que os dados de rotina das "
           "farmácias das unidades sanitárias moçambicanas podem ser "
           "explorados com proveito quando há um período suficientemente "
           "longo de registos {wahlfeld2019}, o que apoia a opção "
           "metodológica deste protocolo."),
     ]),
    ("Métodos de medição e suas propriedades", [
         P("A medição da disponibilidade no dia da visita depende de três "
           "decisões que determinam a comparabilidade dos resultados: a "
           "composição da lista de traçadores, a definição do que conta como "
           "presente e o local onde se procura. O manual da OMS e da Health "
           "Action International fixa a regra de procurar o produto com a "
           "forma farmacêutica e a dosagem especificadas e de o considerar "
           "disponível apenas quando está fisicamente presente no "
           "estabelecimento no momento da visita {omshai2008}. Para uma "
           "unidade sanitária com farmácia e depósito, a regra tem de ser "
           "explicitada, porque o produto pode estar no depósito e não na "
           "prateleira de dispensa, situação que não configura ruptura mas "
           "que só é detectada se o observador verificar os dois locais."),
         P("A medição da duração das rupturas depende da qualidade das "
           "fichas de stock, que não pode ser assumida. Os estudos que a "
           "avaliaram encontraram valores muito variáveis: fichas presentes "
           "em 77,8% dos produtos e actualizadas em 86% dos casos, com "
           "discrepâncias entre contagem e registo entre 0% e 100% "
           "{demessie2020}; exactidão de inventário de 72,5% a 76% "
           "{gutesa2024}; fichas ausentes na maioria das unidades "
           "{mekonnen2024}. Daqui decorre uma exigência metodológica "
           "incontornável: a verificação prévia da fonte, num pequeno número "
           "de registos, antes de comprometer o estudo com um objectivo que "
           "os documentos não sustentam, e a adopção de uma regra de decisão "
           "escrita sobre o que fazer se a qualidade ficar abaixo do "
           "limiar."),
         P("A reprodutibilidade da observação é a terceira propriedade a "
           "assegurar. A contagem física e a leitura de uma ficha manuscrita "
           "envolvem julgamento, e a solução corrente é a repetição "
           "independente de uma fracção das observações por um segundo "
           "observador, com medida formal da concordância. Para variáveis "
           "categóricas, o kappa de Cohen corrige a concordância observada "
           "pela concordância esperada por acaso e valores a partir de 0,80 "
           "são interpretados como concordância forte {mchugh2012}. O relato "
           "final de estudos observacionais deve seguir a declaração STROBE, "
           "que fixa os itens a descrever no desenho, na fonte de dados, na "
           "definição das variáveis e no tratamento dos dados em falta "
           "{von2007}; num inquérito cuja unidade de observação não é uma "
           "pessoa mas um par formado por um medicamento e uma unidade "
           "sanitária, a lista tem de ser adaptada, substituindo os itens "
           "relativos a participantes pelos itens relativos a "
           "estabelecimentos e a produtos."),
     ]),
]

# ----------------------------------------------------- 7. estado da arte ----
ESTADO_ARTE = [
    P("O [[quadro:estado_arte]] reúne quinze estudos empíricos publicados "
      "nos últimos dez anos que mediram a disponibilidade de medicamentos "
      "essenciais em unidades sanitárias, a duração das rupturas ou a "
      "qualidade dos registos de existências, com atenção especial aos "
      "estudos moçambicanos e da África subsariana."),
    QUADRO("estado_arte",
           "Síntese de estudos sobre disponibilidade de medicamentos "
           "essenciais e rupturas de stock em unidades sanitárias (estado da "
           "arte)",
           ["Autor (ano)", "Local", "Desenho (dimensão)",
            "Principais resultados"],
           [
               ["Albagir (2026) {albagir2026}", "34 países africanos",
                "Revisão sistemática e meta-análise (52 estudos)",
                "Disponibilidade combinada de 48,1% (IC95% 42,5-53,7) no "
                "sector público e 70,3% no privado; 59,1% nas doenças "
                "transmissíveis e 37,4% nas não transmissíveis."],
               ["Jessen et al. (2023) {jessen2023}", "Maputo, Moçambique",
                "Transversal, metodologia adaptada (6 hospitais públicos, 6 "
                "privados, 30 farmácias)",
                "Disponibilidade média de 52,6% dos medicamentos essenciais "
                "do conjunto núcleo e de 20,7% dos cardiovasculares nos "
                "hospitais públicos."],
               ["Sambo et al. (2022) {sambo2022}", "Moçambique",
                "Análise de inquérito nacional (1.644 unidades públicas)",
                "Nenhuma unidade reunia todos os itens traçadores; prontidão "
                "mediana de 57,1% na nutrição e 72,2% na diarreia."],
               ["Wahlfeld et al. (2019) {wahlfeld2019}",
                "Zambézia, Moçambique",
                "Vigilância de existências (75 unidades, 2015-2017)",
                "Existências adequadas em mais de 89% do tempo; risco maior "
                "para o teste inicial do algoritmo (OR 1,82; IC95% "
                "1,40-2,38)."],
               ["Tefera et al. (2022) {tefera2022}", "Amhara, Etiópia",
                "Descritivo (15 medicamentos, 1 hospital e 1 centro)",
                "Disponibilidade de 80% e 93,3%; duração média das rupturas "
                "em seis meses de 38,8 dias (10-157) e de 11,2 dias."],
               ["Kefale e Shebo (2019) {kefale2019}", "Adama, Etiópia",
                "Transversal (centros de saúde urbanos)",
                "Disponibilidade de 76,3% no dia da visita; 40,6 dias de "
                "ruptura em doze meses; 144 dias nos sais de reidratação "
                "oral."],
               ["Hailu e Mohammed (2020) {hailu2020}", "Dessie, Etiópia",
                "Transversal (45 medicamentos prioritários)",
                "Disponibilidade de 34,02% no período e 33,5% no ponto; "
                "média de 3,9 rupturas e 128,9 dias por medicamento."],
               ["Mekonnen et al. (2024) {mekonnen2024}",
                "Bahir Dar, Etiópia", "Transversal (12 unidades públicas)",
                "78,68% dos traçadores disponíveis no dia da visita; ficha "
                "de existências em apenas 2 unidades (16,7%); 69,64 dias de "
                "ruptura na pomada de tetraciclina."],
               ["Umer et al. (2023) {umer2023}", "Etiópia",
                "Inquérito nacional a unidades primárias",
                "Disponibilidade média dos traçadores de 77,6%; apenas 2,8% "
                "das unidades tinham a lista completa."],
               ["Gutesa et al. (2024) {gutesa2024}", "Oromia, Etiópia",
                "Estudo misto (hospitais e centros de saúde)",
                "Exactidão do inventário de 76% nos hospitais e 72,5% nos "
                "centros; taxa média de ruptura de 24,99%."],
               ["Demessie et al. (2020) {demessie2020}", "Dessie, Etiópia",
                "Transversal (12 traçadores, todas as unidades públicas)",
                "Ficha de prateleira em 77,8% dos produtos, 86% "
                "actualizadas; discrepância entre contagem e registo de 0% a "
                "100%."],
               ["Ayako et al. (2023) {ayako2023}", "Tana River, Quénia",
                "Censo de 62 unidades (60 participantes)",
                "Disponibilidade média de 68,73%; formação do pessoal e "
                "presença de técnico de farmácia associadas à "
                "disponibilidade."],
               ["Mukundiyukuri et al. (2020) {mukundiyukuri2020}",
                "Três distritos rurais, Ruanda",
                "Transversal com revisão de registos",
                "71% nos centros de saúde e 78% nos hospitais; 77% dos "
                "centros com ruptura de amlodipina e metformina; medianas de "
                "9 a 72 dias."],
               ["Kuwawenaruwa et al. (2020) {kuwawenaruwa2020}",
                "Dodoma, Tanzânia",
                "Inquérito a unidades e a 1.237 agregados",
                "18 traçadores disponíveis de forma contínua em cerca de 70% "
                "do tempo; utilização associada à disponibilidade contínua "
                "(OR 3,49; IC95% 1,02-12,04)."],
               ["Mohan et al. (2024) {mohan2024}", "Malawi",
                "Análise secundária de censo de unidades (130 consumíveis)",
                "Gestão por técnico de farmácia (OR 1,85; IC95% 1,40-2,44) e "
                "nível superior da unidade (OR 1,64; IC95% 1,37-1,97) "
                "associados a maior disponibilidade."],
           ],
           larguras=[3.6, 2.6, 3.4, 6.4],
           fonte="Elaboração própria (2026), a partir das fontes citadas."),
    P("A leitura do quadro revela três padrões constantes. O primeiro é a "
      "distância entre o valor observado e a meta de 80%: com excepção dos "
      "estudos que se limitam a listas curtas ou a unidades de referência, a "
      "disponibilidade no sector público situa-se entre pouco mais de um "
      "terço e cerca de três quartos da lista avaliada, e a proporção de "
      "unidades com a lista completa é quase sempre residual. O segundo é a "
      "desigualdade entre grupos de medicamentos: os produtos de programas "
      "verticais e das doenças transmissíveis saem sistematicamente melhor "
      "do que os de aquisição geral e das doenças crónicas. O terceiro é a "
      "fragilidade dos registos, com fichas ausentes, desactualizadas ou "
      "discordantes da contagem física em proporções que, em alguns "
      "estudos, inviabilizariam qualquer medição de duração de rupturas sem "
      "verificação prévia."),
    P("Sobressaem também duas divergências. A duração das rupturas varia "
      "muito mais entre estudos do que a disponibilidade no dia da visita, o "
      "que sugere que a segunda esconde realidades logísticas muito "
      "diferentes; e o nível da unidade produz resultados contraditórios, "
      "com hospitais a saírem melhor num contexto e pior noutro. A lacuna "
      "que este estudo preenche é geográfica e metodológica: não existe "
      "nenhuma medição para o norte de Moçambique, e os dois estudos "
      "moçambicanos disponíveis ou se limitam à capital, com medição apenas "
      "no dia da visita {jessen2023}, ou tratam de produtos de diagnóstico e "
      "não de medicamentos {wahlfeld2019}. Ao medir as duas dimensões na "
      "mesma amostra de unidades, com uma lista de traçadores construída "
      "segundo critérios explícitos e equilibrada entre grupos de aquisição, "
      "o estudo permite quantificar o problema e localizar a sua origem."),
]
ESQUEMA_TEXTO = [
    P("A [[figura:esquema]] organiza o raciocínio do estudo. Blocos de "
      "factores situados a três níveis, o da cadeia de abastecimento, o da "
      "unidade sanitária e o do próprio medicamento, actuam sobre o "
      "desfecho, que reúne a disponibilidade no dia da visita e as "
      "características das rupturas documentadas nas fichas de stock. O "
      "esquema não postula relações causais demonstráveis com este desenho "
      "transversal, mas fixa as variáveis que serão recolhidas e o sentido "
      "em que serão interpretadas."),
]
ESQUEMA_TITULO = ("Esquema conceptual da disponibilidade de medicamentos e "
                  "das rupturas de stock na unidade sanitária")
ESQUEMA = {
    "contexto": ("Unidades sanitárias públicas da cidade de Nampula, "
                 "medicamentos traçadores, ano de 2026 e visitas de 2027"),
    "blocos": [
        ("Cadeia de abastecimento", [
            "periodicidade das entregas recebidas",
            "quantidade recebida face à requisitada",
            "nível de origem do reabastecimento",
            "tempo entre a requisição e a entrega",
        ]),
        ("Unidade sanitária", [
            "tipo e dimensão da unidade",
            "qualificação de quem gere a farmácia",
            "formação em gestão de existências",
            "separação entre depósito e sala de dispensa",
        ]),
        ("Sistema de registo", [
            "existência da ficha de stock por produto",
            "regularidade e legibilidade dos registos",
            "concordância entre saldo registado e contagem física",
            "envio atempado do balanço periódico",
        ]),
        ("Medicamento", [
            "grupo de aquisição (programa vertical ou geral)",
            "grupo terapêutico",
            "forma farmacêutica",
            "sazonalidade da procura",
        ]),
    ],
    "desfecho": ("Disponibilidade e rupturas de stock", [
        "disponibilidade no dia da visita",
        "número de episódios de ruptura em 2026",
        "duração acumulada das rupturas em dias",
        "disponibilidade no período de doze meses",
    ]),
    "moderadores": ("Contexto e confundimento", [
        "estação do ano e época de maior procura",
        "epidemias e emergências",
        "financiamento externo dos programas verticais",
    ]),
}

# ----------------------------------------------------- 8. metodologia -------
METODOLOGIA = [
    ("Tipo e desenho do estudo", [
        P("Trata-se de um estudo observacional, transversal, de abordagem "
          "quantitativa, com uma componente descritiva, correspondente aos "
          "objectivos específicos 1, 2, 3 e 5, e uma componente analítica, "
          "correspondente ao objectivo específico 4. A observação faz-se ao "
          "nível do estabelecimento e não do doente: em cada unidade "
          "sanitária, o investigador verifica fisicamente a presença de uma "
          "lista fixa de medicamentos e lê os registos de existências "
          "referentes ao ano anterior. Não há contacto com utentes, não se "
          "consultam processos clínicos nem receitas, e a recolha decorre "
          "sem interferência no funcionamento do serviço."),
        P("O desenho combina, na mesma visita, duas fontes com propriedades "
          "diferentes. A verificação física dá uma medida directa e "
          "independente de registos, comparável com a de inquéritos "
          "conduzidos noutros países com a metodologia da OMS e da Health "
          "Action International {omshai2008}. A leitura retrospectiva das "
          "fichas de stock dá a dimensão temporal que a verificação física "
          "não capta, mas depende da qualidade dos documentos, o que obriga "
          "a uma verificação prévia da fonte e a uma regra de decisão "
          "escrita antes da recolha definitiva. O protocolo e o relatório "
          "final seguem a declaração STROBE, adaptada a um inquérito cuja "
          "unidade de observação é um par formado por um medicamento e uma "
          "unidade sanitária: os itens relativos a participantes são "
          "substituídos por itens relativos a estabelecimentos e a "
          "produtos, e a descrição do enviesamento passa a tratar da "
          "selecção das unidades, da composição da lista de traçadores e da "
          "qualidade dos registos {von2007}."),
    ]),
    ("Local e período do estudo", [
        P("O estudo decorre na cidade de Nampula, capital da província de "
          "Nampula, no norte de Moçambique, província que reunia 5.758.920 "
          "habitantes no recenseamento de 2017 {ine2021}. São abrangidas "
          "todas as unidades sanitárias públicas da cidade que dispensem "
          "medicamentos ao público e mantenham farmácia ou depósito "
          "próprio, sob gestão do SDSMAS da Cidade de Nampula. A lista "
          "nominal e o número exacto de unidades elegíveis serão obtidos no "
          "início do trabalho de campo [confirmar a lista das unidades "
          "sanitárias públicas junto do SDSMAS da Cidade de Nampula]. O "
          "contexto urbano justifica-se por concentrar a maior procura da "
          "província e por permitir visitar todas as unidades com custos de "
          "deslocação comportáveis, condição para um censo."),
        P("O período tem duas componentes. A disponibilidade no dia da "
          "visita é registada durante o trabalho de campo, entre Março e "
          "Junho de 2027, numa visita única e não anunciada com "
          "antecedência superior a 48 horas, para evitar reposições "
          "preparatórias. A frequência e a duração das rupturas são "
          "reconstruídas a partir das fichas de stock referentes a 1 de "
          "Janeiro a 31 de Dezembro de 2026, ano civil completo que cobre a "
          "estação chuvosa, de Novembro a Março, e a estação seca, de Abril "
          "a Outubro. A verificação prévia da qualidade das fichas decorre "
          "em Fevereiro de 2027, antes da recolha definitiva."),
    ]),
    ("População, unidade de análise e fontes de dados", [
        P("A população de estudo é constituída pelos medicamentos "
          "traçadores observados nas unidades sanitárias públicas elegíveis "
          "da cidade de Nampula. A unidade de análise é o par formado por "
          "um medicamento traçador e uma unidade sanitária, isto é, cada "
          "combinação de um dos trinta medicamentos da lista com uma das "
          "unidades visitadas. Num cenário de catorze unidades, a base de "
          "observação tem 420 pares. Todos os indicadores de disponibilidade "
          "são calculados sobre este par, e não sobre a unidade nem sobre o "
          "medicamento isoladamente; as leituras por unidade e por "
          "medicamento são obtidas por agregação da mesma base."),
        P("Um par é classificado como não aplicável quando o medicamento não "
          "está previsto para o nível de atendimento daquela unidade na "
          "LNME, situação em que sai do numerador e do denominador dessa "
          "unidade e é contabilizado à parte. O denominador efectivo de cada "
          "unidade é sempre declarado no relatório, e prevê-se que as "
          "exclusões por não aplicabilidade não ultrapassem 10% dos pares, "
          "margem incorporada no cálculo da dimensão da amostra."),
        P("Três fontes alimentam a recolha. A primeira é a observação "
          "directa das prateleiras da farmácia de dispensa e das estantes "
          "do depósito da unidade, com contagem das unidades existentes e "
          "leitura do prazo de validade. A segunda é a ficha de stock de "
          "cada medicamento traçador referente a 2026, de onde se extraem "
          "as datas em que o saldo chegou a zero e as datas de reposição; na "
          "sua falta, recorre-se ao mapa periódico de balanço e requisição "
          "arquivado na unidade [confirmar a designação exacta dos "
          "instrumentos de registo em uso junto da farmácia provincial]. A "
          "terceira é um questionário curto ao responsável pela farmácia, "
          "que documenta a organização do serviço, a periodicidade das "
          "entregas e as causas de ruptura percebidas, e que constitui a "
          "única componente do estudo com participação humana."),
    ]),
    ("Construção da lista de medicamentos traçadores", [
        P("A lista de traçadores é o instrumento que determina o resultado "
          "do estudo e por isso é construída com critérios explícitos, "
          "aplicados por esta ordem. Primeiro, o medicamento tem de constar "
          "da LNME do MISAU e estar previsto para o nível de atendimento das "
          "unidades a visitar {misau2017}. Segundo, tem de ser terapêutica "
          "de primeira linha de uma das causas mais frequentes de procura de "
          "cuidados na província, o que inclui a malária, as infecções "
          "respiratórias e diarreicas, a infecção pelo vírus da "
          "imunodeficiência humana, a tuberculose, a anemia, a saúde materna "
          "e o planeamento familiar, e as doenças crónicas não "
          "transmissíveis. Terceiro, tem de ter denominação comum "
          "internacional (DCI), forma farmacêutica e dosagem inequívocas, "
          "verificáveis por observação directa da embalagem, com as "
          "dosagens expressas em miligramas, microgramas ou unidades "
          "internacionais (UI). Quarto, a lista reparte-se em partes iguais "
          "entre medicamentos fornecidos pelos programas verticais e "
          "medicamentos de aquisição geral, condição necessária à comparação "
          "prevista no objectivo específico 4. Quinto, incluem-se "
          "medicamentos de uso corrente nos inquéritos internacionais "
          "conduzidos com esta metodologia, para permitir a comparação dos "
          "resultados com os de Maputo e de outros países "
          "{jessen2023,albagir2026}."),
        P("O número de trinta medicamentos resulta de três considerações. A "
          "análise de robustez do indicador internacional de acesso mostrou "
          "que as pontuações médias das unidades se mantêm estáveis, com "
          "variação inferior a 5%, enquanto o cabaz tiver pelo menos doze "
          "medicamentos, e que abaixo desse limiar sobem e dispersam-se "
          "{joosse2023}; trinta medicamentos ficam confortavelmente acima do "
          "mínimo. A repartição equilibrada exige um número par e "
          "suficientemente grande para que cada grupo mantenha poder "
          "estatístico depois de aplicado o efeito de desenho. A "
          "exequibilidade impõe o limite superior: a verificação física e a "
          "leitura das fichas de trinta produtos ocupam entre duas e três "
          "horas por unidade, duração compatível com uma visita única que "
          "não perturbe o serviço. A lista definitiva é submetida, antes do "
          "trabalho de campo, à apreciação de três peritos, um farmacêutico "
          "hospitalar, um responsável de depósito distrital e um docente de "
          "farmácia, que confirmam a pertinência de cada item e a "
          "classificação no grupo de aquisição; os itens que não reúnam "
          "acordo de pelo menos dois peritos são substituídos."),
        P("O [[quadro:tracadores]] apresenta a lista proposta. A "
          "classificação de cada medicamento no grupo de aquisição segue o "
          "circuito pelo qual a unidade o recebe e é confirmada junto do "
          "depósito distrital antes do início da recolha [confirmar a "
          "afectação de cada medicamento ao circuito de programa ou ao "
          "circuito geral junto do depósito distrital]."),
        QUADRO("tracadores",
               "Lista dos trinta medicamentos traçadores, por grupo de "
               "aquisição e grupo terapêutico",
               ["N.º", "Medicamento (denominação comum internacional)",
                "Forma farmacêutica e dosagem", "Grupo terapêutico",
                "Grupo de aquisição"],
               [
                   ["1", "Arteméter + lumefantrina",
                    "Comprimido 20 mg + 120 mg", "Antimalárico",
                    "Programa vertical"],
                   ["2", "Artesunato", "Pó para solução injectável 60 mg",
                    "Antimalárico", "Programa vertical"],
                   ["3", "Sulfadoxina + pirimetamina",
                    "Comprimido 500 mg + 25 mg", "Antimalárico",
                    "Programa vertical"],
                   ["4", "Tenofovir + lamivudina + dolutegravir",
                    "Comprimido 300 mg + 300 mg + 50 mg", "Anti-retroviral",
                    "Programa vertical"],
                   ["5", "Dolutegravir", "Comprimido dispersível 10 mg",
                    "Anti-retroviral", "Programa vertical"],
                   ["6", "Sulfametoxazol + trimetoprim",
                    "Comprimido 400 mg + 80 mg",
                    "Profilaxia de infecções oportunistas",
                    "Programa vertical"],
                   ["7", "Isoniazida", "Comprimido 100 mg",
                    "Antituberculoso", "Programa vertical"],
                   ["8", "Rifampicina + isoniazida + pirazinamida + "
                    "etambutol",
                    "Comprimido 150 mg + 75 mg + 400 mg + 275 mg",
                    "Antituberculoso", "Programa vertical"],
                   ["9", "Sulfato ferroso + ácido fólico",
                    "Comprimido 60 mg + 0,4 mg", "Saúde materna",
                    "Programa vertical"],
                   ["10", "Oxitocina", "Solução injectável 10 UI/mL",
                    "Saúde materna", "Programa vertical"],
                   ["11", "Misoprostol", "Comprimido 200 microgramas",
                    "Saúde materna", "Programa vertical"],
                   ["12", "Medroxiprogesterona",
                    "Suspensão injectável 150 mg/mL",
                    "Planeamento familiar", "Programa vertical"],
                   ["13", "Retinol (vitamina A)", "Cápsula 200.000 UI",
                    "Saúde infantil", "Programa vertical"],
                   ["14", "Sais de reidratação oral",
                    "Saqueta de baixa osmolaridade", "Saúde infantil",
                    "Programa vertical"],
                   ["15", "Sulfato de zinco",
                    "Comprimido dispersível 20 mg", "Saúde infantil",
                    "Programa vertical"],
                   ["16", "Paracetamol", "Comprimido 500 mg",
                    "Analgésico e antipirético", "Aquisição geral"],
                   ["17", "Ibuprofeno", "Comprimido 400 mg",
                    "Anti-inflamatório", "Aquisição geral"],
                   ["18", "Amoxicilina", "Cápsula 500 mg", "Antibacteriano",
                    "Aquisição geral"],
                   ["19", "Amoxicilina", "Comprimido dispersível 250 mg",
                    "Antibacteriano", "Aquisição geral"],
                   ["20", "Metronidazol", "Comprimido 250 mg",
                    "Antibacteriano e antiprotozoário", "Aquisição geral"],
                   ["21", "Ciprofloxacina", "Comprimido 500 mg",
                    "Antibacteriano", "Aquisição geral"],
                   ["22", "Benzilpenicilina benzatínica",
                    "Pó para solução injectável 2.400.000 UI",
                    "Antibacteriano", "Aquisição geral"],
                   ["23", "Ceftriaxona", "Pó para solução injectável 1 g",
                    "Antibacteriano", "Aquisição geral"],
                   ["24", "Hidroclorotiazida", "Comprimido 25 mg",
                    "Anti-hipertensor", "Aquisição geral"],
                   ["25", "Amlodipina", "Comprimido 5 mg",
                    "Anti-hipertensor", "Aquisição geral"],
                   ["26", "Captopril", "Comprimido 25 mg",
                    "Anti-hipertensor", "Aquisição geral"],
                   ["27", "Metformina", "Comprimido 500 mg",
                    "Antidiabético oral", "Aquisição geral"],
                   ["28", "Glibenclamida", "Comprimido 5 mg",
                    "Antidiabético oral", "Aquisição geral"],
                   ["29", "Salbutamol",
                    "Inalador pressurizado 100 microgramas por dose",
                    "Broncodilatador", "Aquisição geral"],
                   ["30", "Omeprazol", "Cápsula 20 mg",
                    "Antissecretor gástrico", "Aquisição geral"],
               ],
               larguras=[0.9, 4.4, 4.3, 3.2, 3.2],
               fonte="Elaboração própria (2026), a partir da Lista Nacional "
                     "de Medicamentos Essenciais e dos programas nacionais "
                     "prioritários.",
               nota="A afectação de cada medicamento ao circuito de programa "
                    "ou ao circuito geral é confirmada junto do depósito "
                    "distrital antes da recolha e corrigida no relatório se "
                    "divergir."),
    ]),
    ("Amostra e cálculo do tamanho da amostra", [
        P("As unidades sanitárias não são amostradas: todas as unidades "
          "elegíveis da cidade entram no estudo, por censo. A opção "
          "justifica-se por o universo ser pequeno, por a deslocação dentro "
          "da cidade ter custo reduzido e por qualquer amostragem de um "
          "conjunto desta dimensão produzir estimativas com precisão "
          "insuficiente e impedir a leitura por unidade, que é justamente a "
          "informação útil ao SDSMAS. O censo elimina ainda o enviesamento "
          "de selecção das unidades, que é o principal risco deste tipo de "
          "inquérito."),
        P("O que tem de ser dimensionado é o número de pares medicamento-"
          "unidade, base de cálculo da disponibilidade. Parte-se da fórmula "
          "da estimativa de uma proporção em população considerada grande "
          "{serdar2021}:"),
        FORMULA("n<sub>0</sub> = Z<sup>2</sup> × p × (1 - p) / d<sup>2</sup>"),
        P("em que Z é 1,96, valor da distribuição normal padrão para um "
          "nível de confiança de 95%, p é a disponibilidade esperada e d é a "
          "precisão absoluta pretendida. Adopta-se p de 0,5, que maximiza a "
          "variância e dá a dimensão mais exigente; o valor é também "
          "próximo dos 48,1% estimados para o sector público africano "
          "{albagir2026} e dos 52,6% observados nos hospitais públicos de "
          "Maputo {jessen2023}, pelo que não se perde eficiência. A precisão "
          "é fixada em 7,5 pontos percentuais, suficiente para distinguir "
          "uma unidade próxima da meta de 80% de uma unidade próxima da "
          "média africana. A substituição dá n<sub>0</sub> igual a 3,8416 "
          "multiplicado por 0,25 e dividido por 0,005625, ou seja, 170,7 "
          "pares."),
        P("Os pares observados na mesma unidade não são independentes: uma "
          "unidade bem abastecida tende a ter todos os produtos e uma "
          "unidade mal abastecida tende a não ter nenhum. Aplica-se por isso "
          "um efeito de desenho (DEFF) de 2, que, com trinta medicamentos "
          "por unidade, corresponde a um coeficiente de correlação "
          "intraclasse (CCI) de 0,034 pela relação DEFF igual a 1 mais o "
          "produto de (m - 1) por CCI, valor conservador para agrupamentos "
          "desta dimensão:"),
        FORMULA("n = n<sub>0</sub> × DEFF"),
        P("O produto de 170,7 por 2 dá 341,4, arredondado para 342 pares "
          "válidos. Com trinta medicamentos por unidade e uma margem de 10% "
          "para pares classificados como não aplicáveis, cada unidade "
          "contribui com 27 pares válidos, pelo que são necessárias 342 "
          "divididas por 27, ou seja, 12,7, arredondado para treze unidades "
          "sanitárias. O [[quadro:cenarios]] mostra a precisão obtida em "
          "cinco cenários de número de unidades elegíveis."),
        QUADRO("cenarios",
               "Pares medicamento-unidade e precisão da estimativa da "
               "disponibilidade global, segundo o número de unidades "
               "sanitárias elegíveis",
               ["Unidades elegíveis", "Pares observados (30 por unidade)",
                "Pares válidos após 10% de não aplicáveis",
                "Precisão absoluta (pontos percentuais)", "Decisão"],
               [
                   ["8", "240", "216", "9,4",
                    "Abaixo do previsto: declarar a perda de precisão e "
                    "alargar a lista a 36 medicamentos"],
                   ["10", "300", "270", "8,4",
                    "Abaixo do previsto: alargar a lista a 36 medicamentos"],
                   ["12", "360", "324", "7,7",
                    "Próximo do previsto: alargar a lista a 36 medicamentos"],
                   ["14", "420", "378", "7,1",
                    "Cenário de referência: lista de 30 medicamentos"],
                   ["18", "540", "486", "6,3",
                    "Acima do previsto: lista de 30 medicamentos"],
               ],
               larguras=[2.2, 3.0, 3.0, 2.8, 5.0],
               nota="Precisão calculada como 1,96 multiplicado pela raiz "
                    "quadrada de 0,25 multiplicado pelo efeito de desenho de "
                    "2 e dividido pelo número de pares válidos, para uma "
                    "disponibilidade esperada de 50%."),
        P("Se o número de unidades elegíveis ficar abaixo de treze, a lista "
          "de traçadores é alargada para trinta e seis medicamentos, "
          "mantendo a repartição em partes iguais entre os dois grupos de "
          "aquisição, o que repõe o número de pares válidos acima de 342 a "
          "partir de doze unidades. A decisão é tomada e registada antes do "
          "início da recolha, nunca depois de conhecidos os resultados."),
        P("O poder foi verificado para a componente analítica e não apenas "
          "para a estimativa descritiva. No cenário de referência, cada "
          "grupo de aquisição contribui com quinze medicamentos em catorze "
          "unidades, ou seja, 210 pares, reduzidos a 189 pares válidos e a "
          "94 observações efectivas depois do efeito de desenho. Para "
          "detectar, com significância de 5% e poder de 80%, a diferença "
          "entre 59,1% e 37,4% observada na meta-análise africana entre "
          "medicamentos de doenças transmissíveis e de doenças não "
          "transmissíveis {albagir2026}, seriam necessárias 82 observações "
          "efectivas por grupo, número inferior ao disponível. A menor "
          "diferença detectável nestas condições é de cerca de 20 pontos "
          "percentuais, pelo que o estudo não tem poder para diferenças "
          "moderadas, limitação declarada nos resultados. Para a comparação "
          "da duração das rupturas, de distribuição assimétrica e com "
          "excesso de zeros, o poder é menor e a análise é apresentada como "
          "exploratória."),
    ]),
    ("Critérios de inclusão e de exclusão", [
        H3("Critérios de inclusão das unidades sanitárias"),
        LISTA([
            "Unidade sanitária pública situada na cidade de Nampula e gerida "
            "pelo SDSMAS da Cidade de Nampula;",
            "Com dispensa de medicamentos ao público em funcionamento "
            "durante todo o ano de 2026 e no momento da visita;",
            "Com farmácia ou depósito de medicamentos próprio, distinto do "
            "depósito distrital;",
            "Com autorização escrita da direcção da unidade para a "
            "verificação física e a consulta dos registos de existências.",
        ]),
        H3("Critérios de exclusão das unidades sanitárias"),
        LISTA([
            "Unidade aberta depois de 1 de Janeiro de 2026 ou encerrada "
            "durante mais de três meses no período de estudo;",
            "Unidade que dispense exclusivamente medicamentos de um único "
            "programa, sem cabaz geral;",
            "Depósito distrital, armazém provincial e farmácias privadas, "
            "que não são unidades de dispensa ao público no sentido deste "
            "estudo.",
        ]),
        H3("Critérios de inclusão dos medicamentos e dos registos"),
        LISTA([
            "Medicamento constante da lista de traçadores aprovada antes do "
            "trabalho de campo;",
            "Ficha de stock ou registo equivalente referente ao ano de 2026 "
            "arquivado e acessível na unidade, com datas legíveis.",
        ]),
        H3("Critérios de exclusão dos medicamentos e dos registos"),
        LISTA([
            "Par medicamento-unidade em que o medicamento não está previsto "
            "para o nível de atendimento da unidade, classificado como não "
            "aplicável;",
            "Ficha cujo período de registo cubra menos de seis meses do ano "
            "de 2026, ou cujas datas não permitam determinar o início e o "
            "fim dos episódios de saldo zero, classificada como registo "
            "inutilizável para o objectivo específico 3 mas mantida para o "
            "objectivo específico 2.",
        ]),
    ]),
    ("Variáveis e definições operacionais", [
        P("O [[quadro:variaveis]] apresenta as variáveis do estudo, o seu "
          "tipo, a definição operacional e as categorias, e o objectivo "
          "específico a que cada uma serve. Três definições merecem "
          "explicitação prévia. Um medicamento é considerado disponível "
          "quando pelo menos uma unidade do produto, na forma farmacêutica e "
          "na dosagem especificadas na lista, dentro do prazo de validade, "
          "está fisicamente presente na farmácia de dispensa ou no depósito "
          "da unidade no momento da visita; a presença exclusiva no depósito "
          "conta como disponível, mas é registada à parte, por constituir "
          "uma ruptura funcional na sala de dispensa. Uma ruptura de stock é "
          "um período contínuo de um ou mais dias em que o saldo registado "
          "na ficha do medicamento é igual a zero. A duração de um episódio "
          "é o número de dias decorridos entre a data do registo do saldo "
          "zero e a data do registo da entrada seguinte que reponha saldo "
          "positivo, contando o primeiro dia e não contando o dia da "
          "reposição."),
        P("A partir destas definições calculam-se os indicadores. A "
          "disponibilidade de uma unidade sanitária é a razão entre o número "
          "de traçadores presentes e o número de traçadores aplicáveis nessa "
          "unidade:"),
        FORMULA("D<sub>j</sub> = (m<sub>j</sub> / M<sub>j</sub>) × 100"),
        P("em que m<sub>j</sub> é o número de traçadores encontrados na "
          "unidade j e M<sub>j</sub> o número de traçadores aplicáveis nessa "
          "unidade. A disponibilidade global do conjunto das unidades é "
          "calculada sobre todos os pares válidos e não como média simples "
          "das percentagens das unidades, para que unidades com "
          "denominadores diferentes não recebam o mesmo peso. A "
          "disponibilidade no período de um par medicamento-unidade é "
          "calculada a partir dos dias de ruptura:"),
        FORMULA("DP<sub>ij</sub> = [(365 - R<sub>ij</sub>) / 365] × 100"),
        P("em que R<sub>ij</sub> é a soma dos dias com saldo zero do "
          "medicamento i na unidade j durante o ano de 2026."),
        QUADRO("variaveis", "Variáveis do estudo e definições operacionais",
               ["Variável", "Tipo",
                "Definição operacional e categorias", "Objectivo"],
               [
                   ["Tipo de unidade sanitária", "Independente, qualitativa "
                    "nominal", "Classificação oficial da unidade na rede "
                    "sanitária da cidade [confirmar a tipologia em uso junto "
                    "do SDSMAS]", "1"],
                   ["Separação entre depósito e sala de dispensa",
                    "Independente, qualitativa nominal",
                    "Sim; não", "1"],
                   ["Qualificação do responsável pela farmácia",
                    "Independente, qualitativa nominal",
                    "Farmacêutico; técnico de farmácia; agente de medicina "
                    "preventiva; outro profissional", "1, 5"],
                   ["Formação em gestão de existências nos últimos 24 meses",
                    "Independente, qualitativa nominal", "Sim; não", "1, 5"],
                   ["Existência da ficha de stock do medicamento",
                    "Independente, qualitativa nominal",
                    "Existente e localizada; existente mas não localizada no "
                    "momento da visita; inexistente", "1, 3"],
                   ["Actualização da ficha de stock",
                    "Independente, qualitativa ordinal",
                    "Último registo datado nos 30 dias anteriores; entre 31 "
                    "e 90 dias; há mais de 90 dias; sem data legível",
                    "1, 3"],
                   ["Concordância entre saldo registado e contagem física",
                    "Dependente intermédia, quantitativa contínua",
                    "Diferença percentual absoluta entre a contagem física e "
                    "o saldo da ficha; concordante se igual ou inferior a "
                    "5%", "1"],
                   ["Medicamento traçador", "Independente, qualitativa "
                    "nominal", "Cada um dos 30 medicamentos da lista "
                    "aprovada", "2, 3, 4"],
                   ["Grupo de aquisição", "Independente, qualitativa "
                    "nominal", "Programa vertical; aquisição geral", "4"],
                   ["Grupo terapêutico", "Independente, qualitativa nominal",
                    "Antimalárico; anti-retroviral; antituberculoso; "
                    "antibacteriano; saúde materna e planeamento familiar; "
                    "saúde infantil; doença crónica não transmissível; "
                    "outro", "2"],
                   ["Forma farmacêutica", "Independente, qualitativa "
                    "nominal", "Comprimido ou cápsula; forma oral "
                    "pediátrica; pó ou solução injectável; inalador; "
                    "saqueta", "2"],
                   ["Disponibilidade no dia da visita",
                    "Dependente, qualitativa dicotómica",
                    "Disponível: pelo menos uma unidade do produto, na forma "
                    "e dosagem especificadas, dentro do prazo de validade, "
                    "presente na farmácia ou no depósito; indisponível: "
                    "ausente ou apenas com unidades expiradas", "2, 4"],
                   ["Local onde o produto foi encontrado",
                    "Independente, qualitativa nominal",
                    "Farmácia de dispensa; apenas depósito; ambos", "2"],
                   ["Presença de unidades expiradas",
                    "Independente, qualitativa nominal", "Sim; não", "2"],
                   ["Número de episódios de ruptura em 2026",
                    "Dependente, quantitativa discreta",
                    "Número de períodos contínuos com saldo zero registado "
                    "na ficha entre 1 de Janeiro e 31 de Dezembro de 2026",
                    "3, 4"],
                   ["Duração acumulada das rupturas em 2026",
                    "Dependente, quantitativa contínua",
                    "Soma, em dias, dos períodos com saldo zero no ano",
                    "3, 4"],
                   ["Duração do episódio de ruptura mais longo",
                    "Dependente, quantitativa contínua",
                    "Maior número de dias consecutivos com saldo zero no "
                    "ano", "3"],
                   ["Disponibilidade no período",
                    "Dependente, quantitativa contínua",
                    "Percentagem de dias do ano com saldo positivo, "
                    "calculada pela fórmula apresentada", "3"],
                   ["Periodicidade das entregas recebidas",
                    "Independente, qualitativa ordinal",
                    "Mensal; bimestral; trimestral; irregular", "5"],
                   ["Razão entre a quantidade recebida e a requisitada na "
                    "última entrega", "Independente, quantitativa contínua",
                    "Quociente percentual declarado e confirmado no "
                    "documento de entrega", "5"],
                   ["Tempo entre a requisição e a entrega",
                    "Independente, quantitativa discreta",
                    "Número de dias na última requisição documentada", "5"],
                   ["Causas de ruptura apontadas pelo responsável",
                    "Independente, qualitativa nominal",
                    "Falta no nível de abastecimento; atraso no transporte; "
                    "erro de quantificação; falta de fundos; aumento "
                    "inesperado da procura; outra", "5"],
               ],
               larguras=[3.6, 2.8, 7.2, 1.4]),
    ]),
    ("Instrumentos de recolha de dados e respectivas fontes", [
        P("São usados dois instrumentos, ambos apresentados nos apêndices. O "
          "primeiro é a ficha de verificação da disponibilidade e das "
          "rupturas, adaptada da estrutura do formulário de recolha do "
          "manual da OMS e da Health Action International {omshai2008} e dos "
          "módulos de itens traçadores dos inquéritos harmonizados de "
          "unidades sanitárias {omshhfa2023}. A ficha tem uma linha por "
          "medicamento traçador e colunas para a presença física, a "
          "localização, a quantidade contada, o prazo de validade mais "
          "próximo, o saldo registado na ficha de stock, a data do último "
          "registo, o número de episódios de saldo zero em 2026 e a soma dos "
          "dias sem existências. A adaptação consistiu em retirar as colunas "
          "de preço, que não fazem parte dos objectivos, e acrescentar as "
          "colunas de leitura retrospectiva da ficha de stock, que o "
          "formulário original não contempla."),
        P("O segundo instrumento é um questionário estruturado de resposta "
          "curta dirigido ao responsável pela farmácia da unidade, com "
          "secções sobre a organização do serviço, a qualificação e a "
          "formação do pessoal, a periodicidade e a completude das entregas, "
          "os instrumentos de registo em uso e as causas de ruptura "
          "percebidas. Os itens de causas de ruptura seguem as categorias "
          "identificadas nos estudos que documentaram determinantes de "
          "disponibilidade em unidades africanas {ayako2023,gutesa2024,"
          "mohan2024}. O questionário é submetido a validação de conteúdo "
          "pelos mesmos três peritos que apreciam a lista de traçadores, "
          "exigindo-se um índice de validade de conteúdo de pelo menos 0,80 "
          "por item; os itens abaixo desse limiar são reformulados ou "
          "retirados. Não se aplicam escalas psicométricas, pelo que não há "
          "lugar a medidas de consistência interna."),
        P("Ambos os instrumentos são pré-testados em duas unidades "
          "sanitárias públicas de um distrito vizinho, fora da cidade de "
          "Nampula e portanto fora da amostra final, em Fevereiro de 2027. O "
          "pré-teste avalia o tempo necessário por unidade, a clareza das "
          "instruções, a adequação das categorias e a exequibilidade da "
          "leitura retrospectiva das fichas, e conduz à versão definitiva "
          "antes do início da recolha."),
    ]),
    ("Procedimentos de recolha de dados e controlo de qualidade", [
        P("A recolha começa depois da aprovação pelo CIBS-UniLúrio e da "
          "obtenção das autorizações institucionais. Em cada unidade, o "
          "investigador apresenta-se à direcção, entrega a credencial e o "
          "pedido de autorização, e combina a visita com o responsável pela "
          "farmácia de modo a não coincidir com o período de maior afluência "
          "de utentes. A visita decorre numa única deslocação e segue sempre "
          "a mesma sequência: verificação física na sala de dispensa, "
          "verificação física no depósito, leitura das fichas de stock de "
          "2026 e, por fim, aplicação do questionário ao responsável."),
        P("A verificação física consiste em procurar, produto a produto, "
          "cada medicamento da lista, confirmar a DCI, a forma farmacêutica "
          "e a dosagem no rótulo, contar as unidades existentes e registar "
          "o prazo de validade mais próximo. Produtos com prazo de validade "
          "ultrapassado são registados mas não contam como disponíveis. "
          "Quando o medicamento não é encontrado, o investigador pergunta "
          "expressamente ao responsável se existe noutro local da unidade "
          "antes de o classificar como indisponível, procedimento que evita "
          "falsos negativos por desconhecimento da arrumação."),
        P("A qualidade da fonte documental é verificada antes da recolha "
          "definitiva. Em Fevereiro de 2027, durante o pré-teste, são "
          "examinadas trinta fichas de stock de medicamentos não incluídos "
          "na lista de traçadores, nas duas unidades sanitárias do distrito "
          "vizinho usadas no pré-teste, e avaliados três atributos: "
          "existência da ficha, continuidade dos registos ao longo dos doze "
          "meses e legibilidade das datas de movimento. A regra de decisão é "
          "escrita e aplicada antes de se conhecerem os resultados do "
          "estudo: se menos de 60% das fichas permitirem identificar com "
          "segurança o início e o fim dos períodos de saldo zero, o "
          "objectivo específico 3 passa a ser medido apenas para os últimos "
          "seis meses de 2026; se menos de 40% o permitirem, a duração das "
          "rupturas é substituída pela frequência de meses com ruptura "
          "declarada nos mapas periódicos de balanço, e a limitação é "
          "assumida no título da secção de resultados. A necessidade desta "
          "precaução está documentada: a ficha de existências estava "
          "ausente na maioria das unidades num estudo etíope {mekonnen2024} "
          "e menos de metade das unidades sul-africanas avaliadas preenchia "
          "as fichas com regularidade {iwu2020}."),
        P("A reprodutibilidade das observações é assegurada por dupla "
          "verificação independente de 10% dos pares medicamento-unidade, "
          "seleccionados por sorteio aleatório simples e distribuídos por "
          "todas as unidades visitadas. Um auxiliar de recolha, estudante "
          "finalista de Farmácia formado em duas sessões antes do trabalho "
          "de campo, repete a contagem física e a leitura da ficha sem "
          "acesso ao registo do primeiro observador. A concordância na "
          "classificação binária de disponibilidade é medida pelo kappa de "
          "Cohen, exigindo-se um valor igual ou superior a 0,80, interpretado "
          "como concordância forte {mchugh2012}; a concordância no número de "
          "dias de ruptura é medida pelo coeficiente de correlação "
          "intraclasse, com o mesmo limiar. Se o valor ficar abaixo do "
          "limiar, as definições operacionais são revistas, os dois "
          "observadores são reinstruídos e as unidades já visitadas são "
          "reavaliadas nos itens discordantes. As discordâncias pontuais são "
          "resolvidas por terceira leitura conjunta, com registo da decisão."),
        P("Os dados são registados em papel durante a visita e introduzidos "
          "no mesmo dia numa folha de cálculo com regras de validação de "
          "intervalo e listas fechadas, que impedem valores impossíveis "
          "como duração de ruptura superior a 365 dias ou datas fora do "
          "período. As fichas em papel são guardadas em pasta fechada, sob "
          "responsabilidade do investigador, e a base electrónica é "
          "protegida por palavra-passe e copiada semanalmente para um "
          "suporte separado."),
    ]),
    ("Processamento e análise dos dados", [
        P("A análise é feita em IBM SPSS Statistics, versão 26 ou superior, "
          "ou em alternativa de acesso livre equivalente. Antes da análise, "
          "a base é depurada com verificação de duplicados por unidade e "
          "medicamento, conferência de 10% dos registos contra a ficha em "
          "papel e tratamento explícito dos valores em falta, que são "
          "descritos por variável e nunca imputados nas variáveis de "
          "desfecho."),
        P("A caracterização das unidades e dos instrumentos de registo, "
          "correspondente ao objectivo específico 1, é apresentada em "
          "frequências absolutas e relativas para as variáveis qualitativas "
          "e em mediana com amplitude interquartil para as quantitativas "
          "assimétricas. A disponibilidade no dia da visita, objectivo "
          "específico 2, é apresentada como percentagem global sobre os "
          "pares válidos, com IC95% calculado pelo método de Wilson, e "
          "desagregada por unidade sanitária, por grupo terapêutico e por "
          "forma farmacêutica; a percentagem de unidades com a lista "
          "completa e a percentagem de unidades acima do limiar de 80% são "
          "apresentadas separadamente, por serem os indicadores comparáveis "
          "com a literatura {albagir2026,umer2023}."),
        P("A frequência e a duração das rupturas, objectivo específico 3, "
          "são descritas por mediana, amplitude interquartil e valores "
          "extremos, por medicamento e por unidade, dado que a distribuição "
          "dos dias de ruptura é assimétrica e tem excesso de zeros. A "
          "disponibilidade no período é apresentada em paralelo com a "
          "disponibilidade no dia da visita, e a concordância entre as duas "
          "medidas é examinada pelo coeficiente de correlação de Spearman e "
          "por representação gráfica, o que permite responder à questão "
          "metodológica de saber se a fotografia do dia da visita substitui "
          "a história do ano."),
        P("A comparação entre grupos de aquisição, objectivo específico 4, "
          "usa o teste do qui-quadrado de Pearson para a disponibilidade no "
          "dia da visita e o teste de Mann-Whitney para a duração acumulada "
          "das rupturas, seguidos de um modelo de regressão logística "
          "multinível com intercepto aleatório da unidade sanitária, que "
          "respeita o agrupamento das observações e estima o efeito do grupo "
          "de aquisição ajustado para o grupo terapêutico e a forma "
          "farmacêutica. O coeficiente de correlação intraclasse do modelo "
          "vazio é apresentado, por quantificar a parte da variação "
          "atribuível à unidade e por permitir verificar a plausibilidade do "
          "efeito de desenho assumido. Os resultados são expressos em odds "
          "ratio (OR) com IC95%."),
        P("Os factores organizacionais e logísticos, objectivo específico 5, "
          "são analisados de forma descritiva e cruzados com a "
          "disponibilidade de cada unidade, mas sem modelação multivariável "
          "ao nível da unidade: com um número de unidades da ordem da dezena "
          "não há graus de liberdade para estimar coeficientes fiáveis, e "
          "qualquer tentativa nesse sentido produziria estimativas "
          "instáveis. A leitura é feita por ordenação das unidades segundo a "
          "disponibilidade e inspecção das características associadas aos "
          "extremos, com apresentação das causas de ruptura declaradas em "
          "frequências. O nível de significância é de 5% em todos os testes "
          "e os pressupostos de cada procedimento são verificados e "
          "relatados."),
    ]),
    ("Limitações do estudo e estratégias de mitigação", [
        P("O [[quadro:limitacoes]] reúne as limitações previstas, a "
          "consequência de cada uma para a interpretação e a estratégia "
          "adoptada para a reduzir."),
        QUADRO("limitacoes",
               "Limitações previstas e estratégias de mitigação",
               ["Limitação", "Consequência", "Mitigação"],
               [
                   ["Medição num único dia por unidade",
                    "A disponibilidade observada pode não representar o "
                    "ano; uma entrega recente inflaciona o resultado",
                    "Leitura retrospectiva das fichas de stock de 2026, que "
                    "fornece a disponibilidade no período e a duração das "
                    "rupturas; apresentação conjunta das duas medidas"],
                   ["Dependência da qualidade das fichas de stock",
                    "Fichas ausentes, incompletas ou ilegíveis podem "
                    "impedir a medição da duração das rupturas",
                    "Verificação prévia de 30 fichas com regra de decisão "
                    "escrita; redução do período para seis meses ou "
                    "substituição do indicador quando o limiar não for "
                    "atingido"],
                   ["Número pequeno de unidades sanitárias",
                    "Precisão limitada das estimativas globais e "
                    "impossibilidade de modelar determinantes ao nível da "
                    "unidade",
                    "Censo de todas as unidades elegíveis; efeito de "
                    "desenho incorporado no cálculo; alargamento da lista de "
                    "traçadores se as unidades forem menos de treze; análise "
                    "de nível de unidade apenas descritiva"],
                   ["Lista de traçadores não esgota a lista nacional",
                    "Os resultados aplicam-se aos medicamentos "
                    "seleccionados e não a todo o cabaz da unidade",
                    "Critérios de selecção explícitos e apreciação por três "
                    "peritos; apresentação da lista completa no relatório; "
                    "interpretação limitada ao cabaz avaliado"],
                   ["Reactividade dos profissionais à visita",
                    "Possibilidade de reposição preparatória ou de "
                    "apresentação selectiva dos registos",
                    "Aviso com antecedência não superior a 48 horas; "
                    "verificação simultânea de farmácia e depósito; "
                    "confronto entre contagem física e saldo registado"],
                   ["Ausência de informação sobre consumo e procura",
                    "Não é possível distinguir ruptura por subquantificação "
                    "de ruptura por falha de fornecimento",
                    "Registo da periodicidade das entregas, da razão entre "
                    "quantidade recebida e requisitada e das causas "
                    "declaradas pelo responsável; interpretação prudente"],
                   ["Desenho transversal",
                    "As associações observadas não permitem inferência "
                    "causal sobre os determinantes das rupturas",
                    "Apresentação das associações como exploratórias; "
                    "recomendação de estudo de seguimento com repetição das "
                    "visitas"],
               ],
               larguras=[4.4, 5.6, 6.0]),
    ]),
    ("Considerações éticas", [
        P("O estudo não recolhe qualquer dado de doentes. Não são "
          "consultados processos clínicos, receitas nominais nem livros de "
          "registo de atendimento, e nenhum utente é abordado, observado ou "
          "inquirido. A única participação humana é a do responsável pela "
          "farmácia de cada unidade, que responde a um questionário sobre a "
          "organização do serviço e o circuito de abastecimento, e cuja "
          "participação é voluntária, precedida de folha de informação e de "
          "termo de consentimento livre e esclarecido, e revogável em "
          "qualquer momento sem consequências."),
        P("O protocolo é submetido ao Comité Institucional de Bioética para "
          "a Saúde da Universidade Lúrio (CIBS-UniLúrio) e, se este o "
          "determinar, ao Comité Nacional de Bioética para a Saúde (CNBS). "
          "A recolha só começa depois do parecer favorável e das "
          "autorizações escritas da DPS de Nampula, do SDSMAS da Cidade de "
          "Nampula e da direcção de cada unidade sanitária visitada "
          "[preencher os contactos telefónicos das instituições no pedido "
          "de autorização]. O estudo obedece aos princípios da Declaração "
          "de Helsínquia na revisão de 2024 {world2025} e ao regime da Lei "
          "n.º 3/2023, de 8 de Junho, sobre investigação em saúde humana "
          "{lei3de2023}."),
        P("A confidencialidade das unidades sanitárias é tratada com o mesmo "
          "cuidado que a confidencialidade das pessoas. Cada unidade recebe "
          "um código na base de dados e os relatórios públicos, a "
          "dissertação e qualquer artigo apresentam os resultados por código "
          "e nunca pelo nome da unidade, de modo a que o estudo não sirva "
          "para expor ou responsabilizar individualmente um serviço ou um "
          "profissional. Os nomes dos responsáveis pela farmácia não são "
          "registados; o questionário identifica apenas a categoria "
          "profissional."),
        P("A devolução dos resultados é formativa e não punitiva. Cada "
          "unidade recebe, no fim do estudo, uma folha de duas páginas com "
          "os seus próprios resultados e a comparação anónima com a "
          "distribuição das restantes unidades, acompanhada de sugestões "
          "práticas de melhoria do registo de existências. O relatório "
          "global é entregue ao SDSMAS da Cidade de Nampula e à DPS de "
          "Nampula. Está expressamente previsto que os dados não serão "
          "usados em processos disciplinares nem em avaliações individuais "
          "de desempenho, compromisso incluído por escrito no pedido de "
          "autorização institucional."),
        P("Os benefícios do estudo são indirectos para os profissionais "
          "envolvidos e directos para a população servida, na medida em que "
          "a informação produzida permite corrigir falhas de abastecimento. "
          "Os riscos são mínimos e limitam-se ao desconforto de responder a "
          "um questionário e ao tempo despendido a acompanhar a verificação, "
          "estimado em menos de trinta minutos por responsável. Se, durante "
          "a visita, forem detectados medicamentos fora do prazo de validade "
          "misturados com o stock utilizável, o facto é comunicado de "
          "imediato ao responsável pela farmácia e registado, por se tratar "
          "de um risco directo para os utentes que exige correcção "
          "imediata. Os dados são conservados durante cinco anos e "
          "destruídos depois desse prazo."),
    ]),
]

# ----------------------------------------------------- 9 e 10 ---------------
RESULTADOS_ESPERADOS = [
    P("Os resultados esperados seguem a ordem dos objectivos específicos. "
      "Nenhum valor é antecipado como número, mas a direcção esperada é "
      "indicada quando a literatura a sustenta."),
    LISTA([
        "Do objectivo específico 1, espera-se uma descrição completa das "
        "unidades sanitárias públicas da cidade quanto à organização da "
        "farmácia e do depósito, à qualificação de quem gere as "
        "existências e ao estado dos instrumentos de registo, com "
        "identificação das unidades sem ficha de stock por produto ou com "
        "fichas desactualizadas. A utilidade é imediata: a falta de "
        "instrumentos de registo é corrigível com medidas de baixo custo e "
        "é condição de qualquer melhoria posterior da gestão.",
        "Do objectivo específico 2, espera-se uma estimativa da "
        "disponibilidade global no dia da visita com precisão de cerca de "
        "sete pontos percentuais, provavelmente abaixo da meta de 80% e "
        "próxima dos valores descritos para o sector público africano e "
        "para os hospitais públicos de Maputo, com variação assinalável "
        "entre unidades e entre grupos terapêuticos. A utilidade é "
        "produzir, pela primeira vez, um valor local comparável com o "
        "indicador internacional de acesso a medicamentos.",
        "Do objectivo específico 3, espera-se a distribuição do número de "
        "episódios de ruptura e da duração acumulada por medicamento e por "
        "unidade em 2026, com medianas que a literatura africana situa "
        "entre poucas semanas e vários meses por medicamento, e a "
        "identificação dos produtos com rupturas mais longas. A utilidade é "
        "distinguir o problema de quantificação, que produz rupturas "
        "frequentes e curtas, do problema de fornecimento, que produz "
        "rupturas raras e longas, e dirigir a correcção em conformidade.",
        "Do objectivo específico 4, espera-se uma disponibilidade superior "
        "nos medicamentos fornecidos pelos programas verticais e rupturas "
        "mais longas nos medicamentos de aquisição geral, diferença que a "
        "meta-análise africana estimou em cerca de vinte pontos "
        "percentuais. Confirmando-se, fica demonstrado que a capacidade "
        "técnica das unidades não é o factor limitante e que a "
        "recomendação se dirige ao financiamento e à quantificação do "
        "cabaz geral.",
        "Do objectivo específico 5, espera-se uma hierarquia das causas de "
        "ruptura declaradas pelos responsáveis pelas farmácias, com "
        "provável predomínio da falta no nível de abastecimento e do atraso "
        "no transporte, e a sua confrontação com os dados objectivos de "
        "periodicidade e completude das entregas. A utilidade é indicar em "
        "que ponto do circuito a falha começa, informação que a leitura "
        "isolada da prateleira não fornece.",
    ]),
    P("Do conjunto espera-se ainda um resultado de natureza metodológica: a "
      "comparação entre a disponibilidade no dia da visita e a "
      "disponibilidade no período permitirá dizer se a primeira, muito mais "
      "barata de obter, é um substituto aceitável da segunda no contexto das "
      "unidades sanitárias da cidade de Nampula, o que tem consequências "
      "directas para o desenho de futuras avaliações de rotina."),
]
DIVULGACAO = [
    P("Os resultados serão apresentados em defesa pública perante júri "
      "designado pela Faculdade de Ciências de Saúde da Universidade Lúrio, "
      "nos termos do regulamento do trabalho de culminação do curso, e a "
      "dissertação ficará depositada na biblioteca da instituição."),
    P("Será entregue um relatório técnico ao SDSMAS da Cidade de Nampula e "
      "à DPS de Nampula, com os resultados agregados, a lista dos "
      "medicamentos com pior desempenho e as recomendações operacionais "
      "decorrentes. Cada unidade sanitária participante receberá uma folha "
      "de duas páginas com os seus próprios resultados e a sua posição "
      "anónima na distribuição das restantes unidades, num formato "
      "formativo e não comparativo em público. Uma sessão de devolução "
      "conjunta será proposta ao SDSMAS, com a presença dos responsáveis "
      "pelas farmácias, para discutir as causas identificadas e as medidas "
      "possíveis ao nível de cada unidade."),
    P("Está prevista a submissão de um artigo a revista científica com "
      "revisão por pares, de preferência de acesso aberto e com "
      "circulação na região africana, redigido segundo a declaração STROBE "
      "adaptada a inquéritos de unidades sanitárias, e a apresentação de "
      "uma comunicação nas jornadas científicas da Universidade Lúrio e em "
      "encontro nacional de farmácia. Nenhuma unidade sanitária será "
      "identificada pelo nome em qualquer destes produtos."),
]

# ----------------------------------------------------- 11. cronograma -------
CRONOGRAMA_TEXTO = [
    P("O [[quadro:cronograma]] distribui as actividades por doze meses, de "
      "Outubro de 2026 a Setembro de 2027. A recolha de dados só começa "
      "depois do parecer do comité de bioética e das autorizações "
      "institucionais, previstos para o primeiro trimestre de 2027, e "
      "decorre entre Março e Junho de 2027."),
]
CRONOGRAMA = {
    "inicio": (2026, 10),
    "n_meses": 12,
    "titulo": ("Cronograma de actividades, de Outubro de 2026 a Setembro de "
               "2027"),
    "actividades": [
        ("Revisão da literatura e redacção do protocolo", [1, 2, 3]),
        ("Submissão ao comité de bioética e pedidos de autorização",
         [3, 4, 5]),
        ("Construção e validação da lista de medicamentos traçadores",
         [4, 5]),
        ("Elaboração e validação de conteúdo dos instrumentos", [4, 5]),
        ("Verificação prévia da qualidade das fichas de stock e pré-teste",
         [5]),
        ("Formação do auxiliar de recolha", [5, 6]),
        ("Visitas às unidades sanitárias e recolha de dados", [6, 7, 8, 9]),
        ("Dupla verificação de 10% das observações", [7, 8, 9]),
        ("Processamento, depuração e análise dos dados", [9, 10]),
        ("Redacção do relatório final", [10, 11]),
        ("Revisão, entrega e devolução formativa às unidades", [11, 12]),
        ("Defesa pública", [12]),
    ],
}

# ----------------------------------------------------- 12. orcamento --------
ORCAMENTO_TEXTO = [
    P("A [[tabela:orcamento]] apresenta as rubricas previstas, em meticais. "
      "O estudo é financiado por recursos próprios do estudante, com "
      "pedido de apoio à Faculdade de Ciências de Saúde da Universidade "
      "Lúrio para as rubricas de deslocação e de submissão ao comité de "
      "bioética."),
    P("As rubricas maiores são as ajudas de custo durante o trabalho de "
      "campo e o transporte urbano, que decorrem da natureza do estudo: "
      "visitar todas as unidades sanitárias da cidade, com uma permanência "
      "de duas a três horas em cada uma e deslocações repetidas para a "
      "dupla verificação, obriga a um número elevado de viagens ao longo de "
      "quatro meses. O honorário do auxiliar de recolha cobre apenas os "
      "dias de dupla verificação e é indispensável à medida de concordância "
      "entre observadores. A impressão em papel mantém-se necessária porque "
      "a recolha decorre em salas de depósito sem energia garantida."),
]
ORCAMENTO = [
    ("Impressão das fichas de verificação e dos questionários", "página",
     900, 5),
    ("Reprodução do protocolo e dos relatórios intermédios", "página",
     600, 5),
    ("Material de escritório para o trabalho de campo", "conjunto", 1, 3500),
    ("Transporte urbano para as visitas às unidades sanitárias",
     "deslocação", 40, 350),
    ("Ajudas de custo do investigador durante o trabalho de campo", "dia",
     25, 750),
    ("Honorário do auxiliar de recolha para a dupla verificação", "dia",
     12, 900),
    ("Formação da equipa e pré-teste dos instrumentos", "sessão", 2, 3000),
    ("Comunicações e acesso à Internet", "mês", 8, 800),
    ("Programa de análise estatística e apoio informático", "verba", 1,
     6000),
    ("Impressão e encadernação da versão final", "exemplar", 5, 900),
    ("Taxa de submissão ao comité de bioética", "submissão", 1, 5000),
    ("Participação em jornadas científicas para divulgação", "inscrição",
     1, 7500),
]
ORCAMENTO_IMPREVISTOS = 0.10

# ----------------------------------------------------- apendices ------------
APENDICES = [
    ("Ficha de verificação da disponibilidade de medicamentos traçadores e "
     "das rupturas de stock", [
         NOTA("Instruções ao investigador: preencher uma ficha por unidade "
              "sanitária, no momento da visita. Procurar cada medicamento "
              "primeiro na sala de dispensa e depois no depósito. Confirmar "
              "sempre a denominação comum internacional, a forma "
              "farmacêutica e a dosagem no rótulo antes de assinalar "
              "presente. Produtos com prazo de validade ultrapassado são "
              "registados na coluna própria e não contam como presentes. "
              "Assinalar não aplicável apenas quando o medicamento não "
              "estiver previsto para o nível de atendimento da unidade. Não "
              "registar nomes de profissionais nem de utentes."),
         H3("Secção I. Identificação da unidade e da visita"),
         CAMPO("Código da unidade sanitária (atribuído pelo investigador): "
               "US - _____"),
         CAMPO("Data da visita: ____ / ____ / 2027      Hora de início: "
               "____:____      Hora de fim: ____:____"),
         CAMPO("Nome do investigador: ______________________________"),
         CAMPO("Observador da dupla verificação (quando aplicável): "
               "______________________________"),
         H3("Secção II. Caracterização da farmácia e do depósito"),
         PERG("A unidade tem sala de dispensa e depósito separados?",
              ["Sim", "Não"]),
         PERG("Categoria profissional de quem gere as existências:",
              ["Farmacêutico", "Técnico de farmácia",
               "Agente de medicina preventiva", "Outro profissional"]),
         PERG("Quem gere as existências recebeu formação em gestão de "
              "existências nos últimos 24 meses?", ["Sim", "Não"]),
         PERG("Instrumentos de registo encontrados na unidade:",
              ["Ficha de stock por produto",
               "Mapa periódico de balanço e requisição",
               "Registo informatizado", "Nenhum"]),
         PERG("Periodicidade habitual das entregas recebidas:",
              ["Mensal", "Bimestral", "Trimestral", "Irregular"]),
         H3("Secção III. Verificação física no dia da visita"),
         NOTA("Local: D = sala de dispensa; A = depósito; DA = presente nos "
              "dois locais. Validade: indicar o prazo mais próximo "
              "encontrado, no formato mês e ano."),
         TABELA(None, None,
                ["N.º", "Medicamento, forma e dosagem", "Não aplicável",
                 "Presente", "Local", "Quantidade contada",
                 "Validade mais próxima"],
                [["1", "Arteméter + lumefantrina 20 mg + 120 mg, comprimido",
                  "( )", "( ) Sim ( ) Não", "____", "______", "___/____"],
                 ["2", "Artesunato 60 mg, injectável", "( )",
                  "( ) Sim ( ) Não", "____", "______", "___/____"],
                 ["3", "Sulfadoxina + pirimetamina 500 mg + 25 mg, "
                  "comprimido", "( )", "( ) Sim ( ) Não", "____", "______",
                  "___/____"],
                 ["4", "Tenofovir + lamivudina + dolutegravir, comprimido",
                  "( )", "( ) Sim ( ) Não", "____", "______", "___/____"],
                 ["5", "Dolutegravir 10 mg, comprimido dispersível", "( )",
                  "( ) Sim ( ) Não", "____", "______", "___/____"],
                 ["6", "Sulfametoxazol + trimetoprim 400 mg + 80 mg, "
                  "comprimido", "( )", "( ) Sim ( ) Não", "____", "______",
                  "___/____"],
                 ["7", "Isoniazida 100 mg, comprimido", "( )",
                  "( ) Sim ( ) Não", "____", "______", "___/____"],
                 ["8", "Rifampicina + isoniazida + pirazinamida + "
                  "etambutol, comprimido", "( )", "( ) Sim ( ) Não", "____",
                  "______", "___/____"],
                 ["9", "Sulfato ferroso + ácido fólico 60 mg + 0,4 mg, "
                  "comprimido", "( )", "( ) Sim ( ) Não", "____", "______",
                  "___/____"],
                 ["10", "Oxitocina 10 UI/mL, injectável", "( )",
                  "( ) Sim ( ) Não", "____", "______", "___/____"],
                 ["11", "Misoprostol 200 microgramas, comprimido", "( )",
                  "( ) Sim ( ) Não", "____", "______", "___/____"],
                 ["12", "Medroxiprogesterona 150 mg/mL, injectável", "( )",
                  "( ) Sim ( ) Não", "____", "______", "___/____"],
                 ["13", "Retinol 200.000 UI, cápsula", "( )",
                  "( ) Sim ( ) Não", "____", "______", "___/____"],
                 ["14", "Sais de reidratação oral, saqueta", "( )",
                  "( ) Sim ( ) Não", "____", "______", "___/____"],
                 ["15", "Sulfato de zinco 20 mg, comprimido dispersível",
                  "( )", "( ) Sim ( ) Não", "____", "______", "___/____"],
                 ["16", "Paracetamol 500 mg, comprimido", "( )",
                  "( ) Sim ( ) Não", "____", "______", "___/____"],
                 ["17", "Ibuprofeno 400 mg, comprimido", "( )",
                  "( ) Sim ( ) Não", "____", "______", "___/____"],
                 ["18", "Amoxicilina 500 mg, cápsula", "( )",
                  "( ) Sim ( ) Não", "____", "______", "___/____"],
                 ["19", "Amoxicilina 250 mg, comprimido dispersível", "( )",
                  "( ) Sim ( ) Não", "____", "______", "___/____"],
                 ["20", "Metronidazol 250 mg, comprimido", "( )",
                  "( ) Sim ( ) Não", "____", "______", "___/____"],
                 ["21", "Ciprofloxacina 500 mg, comprimido", "( )",
                  "( ) Sim ( ) Não", "____", "______", "___/____"],
                 ["22", "Benzilpenicilina benzatínica 2.400.000 UI, "
                  "injectável", "( )", "( ) Sim ( ) Não", "____", "______",
                  "___/____"],
                 ["23", "Ceftriaxona 1 g, injectável", "( )",
                  "( ) Sim ( ) Não", "____", "______", "___/____"],
                 ["24", "Hidroclorotiazida 25 mg, comprimido", "( )",
                  "( ) Sim ( ) Não", "____", "______", "___/____"],
                 ["25", "Amlodipina 5 mg, comprimido", "( )",
                  "( ) Sim ( ) Não", "____", "______", "___/____"],
                 ["26", "Captopril 25 mg, comprimido", "( )",
                  "( ) Sim ( ) Não", "____", "______", "___/____"],
                 ["27", "Metformina 500 mg, comprimido", "( )",
                  "( ) Sim ( ) Não", "____", "______", "___/____"],
                 ["28", "Glibenclamida 5 mg, comprimido", "( )",
                  "( ) Sim ( ) Não", "____", "______", "___/____"],
                 ["29", "Salbutamol 100 microgramas por dose, inalador",
                  "( )", "( ) Sim ( ) Não", "____", "______", "___/____"],
                 ["30", "Omeprazol 20 mg, cápsula", "( )",
                  "( ) Sim ( ) Não", "____", "______", "___/____"]],
                larguras=[0.8, 5.6, 1.6, 2.4, 1.4, 2.2, 2.0]),
         H3("Secção IV. Leitura da ficha de stock referente a 2026"),
         NOTA("Preencher uma linha por medicamento. Ficha: E = existente e "
              "localizada; N = existente mas não localizada; I = "
              "inexistente. Episódios: número de períodos contínuos com "
              "saldo zero entre 1 de Janeiro e 31 de Dezembro de 2026. Dias "
              "sem existências: soma dos dias desses períodos. Assinalar "
              "registo inutilizável quando as datas não permitirem "
              "determinar o início e o fim dos períodos."),
         TABELA(None, None,
                ["N.º", "Medicamento", "Ficha", "Data do último registo",
                 "Saldo registado", "Episódios em 2026",
                 "Dias sem existências", "Registo inutilizável"],
                [[str(i), nome, "____", "___/___/____", "______", "____",
                  "______", "( )"]
                 for i, nome in [
                     (1, "Arteméter + lumefantrina"), (2, "Artesunato"),
                     (3, "Sulfadoxina + pirimetamina"),
                     (4, "Tenofovir + lamivudina + dolutegravir"),
                     (5, "Dolutegravir dispersível"),
                     (6, "Sulfametoxazol + trimetoprim"), (7, "Isoniazida"),
                     (8, "Rifampicina + isoniazida + pirazinamida + "
                         "etambutol"),
                     (9, "Sulfato ferroso + ácido fólico"), (10, "Oxitocina"),
                     (11, "Misoprostol"), (12, "Medroxiprogesterona"),
                     (13, "Retinol"), (14, "Sais de reidratação oral"),
                     (15, "Sulfato de zinco"), (16, "Paracetamol"),
                     (17, "Ibuprofeno"), (18, "Amoxicilina 500 mg"),
                     (19, "Amoxicilina 250 mg dispersível"),
                     (20, "Metronidazol"), (21, "Ciprofloxacina"),
                     (22, "Benzilpenicilina benzatínica"),
                     (23, "Ceftriaxona"), (24, "Hidroclorotiazida"),
                     (25, "Amlodipina"), (26, "Captopril"), (27, "Metformina"),
                     (28, "Glibenclamida"), (29, "Salbutamol"),
                     (30, "Omeprazol")]],
                larguras=[0.8, 4.4, 1.2, 2.6, 1.8, 1.8, 2.0, 1.4]),
         H3("Secção V. Observações"),
         CAMPO("Medicamentos fora do prazo de validade encontrados "
               "misturados com o stock utilizável (comunicar de imediato ao "
               "responsável): ______________________________"),
         CAMPO("Outras observações: "
               "______________________________________________________"),
     ]),
    ("Questionário ao responsável pela farmácia da unidade sanitária", [
        NOTA("Instruções: aplicar depois da verificação física, ao "
             "profissional que gere as existências. Não registar o nome do "
             "respondente. Tempo estimado de resposta: quinze minutos."),
        CAMPO("Código da unidade sanitária: US - _____      Data: "
              "____ / ____ / 2027"),
        H3("Secção I. Organização do serviço"),
        PERG("Há quanto tempo desempenha funções na farmácia desta unidade?",
             ["Menos de 1 ano", "De 1 a 3 anos", "De 4 a 10 anos",
              "Mais de 10 anos"]),
        PERG("Quantas pessoas trabalham na farmácia ou no depósito desta "
             "unidade?"),
        PERG("A unidade tem um responsável formalmente designado pela "
             "gestão das existências?", ["Sim", "Não"]),
        H3("Secção II. Abastecimento"),
        PERG("De onde recebe habitualmente os medicamentos?",
             ["Depósito distrital", "Armazém provincial",
              "Directamente de um programa", "Outra origem"]),
        PERG("Com que periodicidade recebeu entregas em 2026?",
             ["Mensal", "Bimestral", "Trimestral", "Irregular"]),
        PERG("Na última entrega, que proporção da quantidade requisitada foi "
             "recebida?",
             ["Toda a quantidade", "Entre 75% e 99%", "Entre 50% e 74%",
              "Menos de 50%", "Não sabe"]),
        PERG("Quantos dias decorreram entre a última requisição e a "
             "respectiva entrega?"),
        PERG("A unidade recorreu a empréstimo de medicamentos de outra "
             "unidade sanitária em 2026?",
             ["Nunca", "Uma ou duas vezes", "Três a cinco vezes",
              "Mais de cinco vezes"]),
        H3("Secção III. Registo de existências"),
        PERG("Que instrumentos usa para registar entradas e saídas?",
             ["Ficha de stock por produto",
              "Mapa periódico de balanço e requisição",
              "Registo informatizado", "Nenhum"]),
        PERG("Com que frequência actualiza a ficha de stock?",
             ["A cada movimento", "Diariamente", "Semanalmente",
              "Mensalmente", "Raramente ou nunca"]),
        PERG("Com que frequência faz contagem física para conferir o saldo "
             "registado?",
             ["Mensalmente", "Trimestralmente", "Semestralmente",
              "Anualmente", "Nunca"]),
        PERG("Recebeu supervisão externa à gestão de existências nos "
             "últimos 12 meses?", ["Sim", "Não"]),
        H3("Secção IV. Causas de ruptura"),
        PERG("Na sua experiência em 2026, quais foram as principais causas "
             "de falta de medicamentos nesta unidade? Assinalar até três.",
             ["Falta do produto no nível que abastece a unidade",
              "Atraso no transporte ou na entrega",
              "Quantidade requisitada insuficiente face ao consumo",
              "Falta de fundos para aquisição",
              "Aumento inesperado da procura",
              "Perda por expiração ou danificação",
              "Outra causa"]),
        PERG("Que medida considera mais urgente para reduzir as rupturas "
             "nesta unidade?"),
        CAMPO("Observações do respondente: "
              "______________________________________________________"),
    ]),
    ("Folha de informação ao participante e termo de consentimento livre e "
     "esclarecido", [
         H3("Folha de informação"),
         P("É convidado a participar num estudo sobre a disponibilidade de "
           "medicamentos essenciais e as rupturas de stock nas unidades "
           "sanitárias públicas da cidade de Nampula, realizado por um "
           "estudante finalista do curso de Licenciatura em Farmácia da "
           "Faculdade de Ciências de Saúde da Universidade Lúrio, no âmbito "
           "do seu trabalho de culminação do curso."),
         P("O estudo procura saber que proporção de uma lista de trinta "
           "medicamentos essenciais está presente nas unidades sanitárias "
           "da cidade no dia da visita e quantos dias esses medicamentos "
           "estiveram em falta ao longo do ano de 2026, segundo as fichas de "
           "stock. A sua participação consiste em responder a um "
           "questionário de cerca de quinze minutos sobre a organização da "
           "farmácia, o abastecimento e as causas de falta de medicamentos, "
           "e em acompanhar, se assim o entender, a verificação dos "
           "produtos nas prateleiras e no depósito."),
         P("O estudo não recolhe qualquer informação sobre doentes. Não "
           "serão consultados processos clínicos nem receitas, e nenhum "
           "utente será abordado. O seu nome não é registado em parte "
           "alguma do estudo: o questionário identifica apenas a categoria "
           "profissional. A unidade sanitária recebe um código e os "
           "relatórios, a dissertação e eventuais artigos apresentam os "
           "resultados por código, nunca pelo nome da unidade."),
         P("A participação é voluntária. Pode recusar participar ou "
           "interromper a participação em qualquer momento, sem necessidade "
           "de justificação e sem qualquer consequência para si ou para a "
           "unidade. Os resultados não serão usados em processos "
           "disciplinares nem em avaliações individuais de desempenho."),
         P("Não há benefício material directo pela participação. O benefício "
           "esperado é indirecto: a informação recolhida permitirá "
           "identificar os pontos do circuito de abastecimento onde as "
           "faltas começam e apoiar medidas de correcção. No fim do estudo, "
           "a unidade receberá uma folha com os seus próprios resultados e a "
           "comparação anónima com as restantes unidades da cidade. Os "
           "riscos são mínimos e limitam-se ao tempo despendido."),
         P("Para esclarecimentos sobre o estudo pode contactar o "
           "investigador ou o orientador. Para questões relacionadas com os "
           "seus direitos enquanto participante pode contactar o Comité "
           "Institucional de Bioética para a Saúde da Universidade Lúrio."),
         CAMPO("Investigador: [Nome do(a) estudante] - telefone "
               "[preencher] - correio electrónico [preencher]"),
         CAMPO("Orientador: [Nome e grau académico do(a) orientador(a)] - "
               "telefone [preencher]"),
         CAMPO("Comité Institucional de Bioética para a Saúde da "
               "Universidade Lúrio - telefone [preencher]"),
         H3("Termo de consentimento livre e esclarecido"),
         P("Declaro que li, ou me foi lida, a folha de informação acima, "
           "que compreendi o objectivo e os procedimentos do estudo, que "
           "tive oportunidade de fazer perguntas e que obtive respostas "
           "satisfatórias. Compreendo que a participação é voluntária, que "
           "posso desistir em qualquer momento sem consequências e que o meu "
           "nome não será registado. Aceito participar."),
         CAMPO("Código da unidade sanitária: US - _____      Categoria "
               "profissional do respondente: ______________________"),
         CAMPO("Assinatura do participante: ______________________________ "
               "     Data: ____ / ____ / 2027"),
         CAMPO("Impressão digital (quando o participante não souber ou não "
               "puder assinar): ____________"),
         CAMPO("Nome e assinatura da testemunha: "
               "______________________________      Data: ____ / ____ / "
               "2027"),
         CAMPO("Assinatura do investigador: ______________________________ "
               "     Data: ____ / ____ / 2027"),
         NOTA("Este documento é feito em duplicado: um exemplar fica com o "
              "participante e outro com o investigador."),
     ]),
    ("Pedido de autorização institucional", [
        CAMPO("Exmo. Senhor Director do Serviço Distrital de Saúde, Mulher "
              "e Acção Social da Cidade de Nampula"),
        CAMPO("Com conhecimento da Direcção Provincial de Saúde de Nampula "
              "e da direcção de cada unidade sanitária visitada"),
        P("[Nome do(a) estudante], estudante finalista do curso de "
          "Licenciatura em Farmácia da Faculdade de Ciências de Saúde da "
          "Universidade Lúrio, vem solicitar autorização para realizar, nas "
          "unidades sanitárias públicas da cidade de Nampula, o estudo "
          "intitulado «Disponibilidade de medicamentos traçadores essenciais "
          "e duração das rupturas de stock nas unidades sanitárias públicas "
          "da cidade de Nampula, 2026 e 2027», sob orientação de [Nome e "
          "grau académico do(a) orientador(a)]."),
        P("O estudo consiste numa visita única a cada unidade sanitária, "
          "entre Março e Junho de 2027, durante a qual serão verificados "
          "fisicamente trinta medicamentos essenciais na sala de dispensa e "
          "no depósito, serão consultadas as fichas de stock desses "
          "medicamentos referentes ao ano de 2026 e será aplicado um "
          "questionário de quinze minutos ao responsável pela farmácia. A "
          "visita ocupa entre duas e três horas e é combinada previamente de "
          "modo a não coincidir com o período de maior afluência de "
          "utentes."),
        P("Declara-se expressamente que não serão recolhidos dados de "
          "doentes: não serão consultados processos clínicos, receitas "
          "nominais nem livros de registo de atendimento, e nenhum utente "
          "será abordado. Cada unidade sanitária receberá um código e os "
          "relatórios públicos, a dissertação e eventuais artigos "
          "apresentarão os resultados por código e nunca pelo nome da "
          "unidade. Os dados não serão usados em processos disciplinares "
          "nem em avaliações individuais de desempenho dos profissionais."),
        P("Comprometo-me a entregar um relatório técnico ao Serviço "
          "Distrital de Saúde, Mulher e Acção Social da Cidade de Nampula e "
          "à Direcção Provincial de Saúde de Nampula, e a devolver a cada "
          "unidade sanitária uma folha com os seus próprios resultados, em "
          "formato formativo. O protocolo foi submetido ao Comité "
          "Institucional de Bioética para a Saúde da Universidade Lúrio e a "
          "recolha só terá início após o parecer favorável e a presente "
          "autorização."),
        CAMPO("Pede deferimento."),
        CAMPO("Nampula, ____ de __________________ de 2027"),
        CAMPO("O(A) estudante: ______________________________"),
        CAMPO("O(A) orientador(a): ______________________________"),
        CAMPO("Parecer da entidade: ______________________________      "
              "Data: ____ / ____ / 2027"),
    ]),
]
