# -*- coding: utf-8 -*-
"""
Tema 02 (Farmácia Clínica e Cuidados Farmacêuticos).
Técnica de auto-administração e conservação domiciliária da insulina em
adultos com diabetes seguidos no Hospital Central de Nampula, 2027.

Compor e validar:   python -X utf8 _motor/motor.py _conteudo/tema_02.py
Verificar fontes:   python -X utf8 _motor/refs.py verificar _conteudo/tema_02.py
"""
from blocos import (CAMPO, FORMULA, H3, LISTA, NOTA, P, PERG, QUADRO,
                    TABELA)

NUMERO = 2
SLUG = "Tecnica_Conservacao_Insulina_HCN"
TITULO = ("Técnica de auto-administração e conservação domiciliária da "
          "insulina em adultos com diabetes seguidos no Hospital Central de "
          "Nampula, 2027")
DESENHO = ("Transversal analítico, observação directa com lista de "
           "verificação, exame dos locais de injecção e entrevista "
           "estruturada")

AUTOR = "[Nome do(a) estudante]"
ORIENTADOR = "[Nome e grau académico do(a) orientador(a)]"

# ---------------------------------------------------------------- resumo --
RESUMO = (
    "A insulina só produz o efeito esperado quando a dose é preparada e "
    "injectada correctamente e quando o medicamento é guardado em condições "
    "que preservem a sua potência. Em Moçambique, onde menos de um em cada "
    "cinco agregados familiares possui frigorífico, não existe informação "
    "sobre a forma como os doentes administram e conservam a insulina em "
    "casa. O estudo tem como objectivo avaliar a técnica de "
    "auto-administração e as práticas de conservação domiciliária da "
    "insulina, e os factores associados, em adultos com diabetes seguidos "
    "no Hospital Central de Nampula. Trata-se de um estudo transversal "
    "analítico, de abordagem quantitativa, a realizar entre Março e Maio de "
    "2027 em adultos que administram a si próprios insulina há pelo menos "
    "três meses. Será feito um censo se houver até trezentos doentes "
    "elegíveis; acima desse número, será seleccionada uma amostra aleatória "
    "simples de 215 a 428 doentes, dimensionada para uma margem de erro de "
    "cinco por cento, poder de oitenta por cento e dez por cento de não "
    "resposta. A técnica será avaliada por observação directa com uma lista "
    "de verificação adaptada das recomendações internacionais, a "
    "lipohipertrofia por inspecção e palpação padronizadas e a conservação "
    "por entrevista estruturada e inspecção do frasco em uso, com dupla "
    "observação de dez por cento dos doentes. A análise incluirá proporções "
    "com intervalos de confiança a noventa e cinco por cento, o teste do "
    "qui-quadrado e a regressão logística, com significância de cinco por "
    "cento. Espera-se identificar os erros mais frequentes na preparação da "
    "dose, na rotação dos locais, na reutilização de agulhas e na "
    "conservação, e a sua relação com a lipohipertrofia, fundamentando "
    "materiais de educação com pictogramas em português e emakhuwa e o "
    "envolvimento do farmacêutico no ensino da técnica.")
PALAVRAS_CHAVE = ["conservação de medicamentos", "diabetes mellitus",
                  "injecções subcutâneas", "insulina", "lipohipertrofia"]
ABSTRACT = (
    "Insulin only has the intended effect when the dose is prepared and "
    "injected correctly and when the medicine is kept in conditions that "
    "preserve its potency. In Mozambique, where fewer than one in five "
    "households owns a refrigerator, there is no information on how "
    "patients administer and store insulin at home. The study aims to "
    "assess the self-administration technique and home storage practices of "
    "insulin, and their associated factors, among adults with diabetes "
    "followed at Nampula Central Hospital. It is an analytical "
    "cross-sectional study with a quantitative approach, to be carried out "
    "between March and May 2027 among adults who have been injecting "
    "insulin themselves for at least three months. A census will be "
    "conducted if there are up to three hundred eligible patients; above "
    "that number, a simple random sample of 215 to 428 patients will be "
    "selected, sized for a five percent margin of error, eighty percent "
    "power and ten percent non-response. Technique will be assessed by "
    "direct observation with a checklist adapted from international "
    "recommendations, lipohypertrophy by standardised inspection and "
    "palpation, and storage by structured interview and inspection of the "
    "vial in use, with double observation of ten percent of patients. The "
    "analysis will include proportions with ninety-five percent confidence "
    "intervals, the chi-square test and logistic regression, with a five "
    "percent significance level. The study is expected to identify the most "
    "frequent errors in dose preparation, site rotation, needle reuse and "
    "storage, and their relationship with lipohypertrophy, supporting "
    "education materials with pictograms in Portuguese and Emakhuwa and the "
    "involvement of pharmacists in teaching the technique.")
KEYWORDS = ["diabetes mellitus", "drug storage", "insulin",
            "lipohypertrophy", "subcutaneous injections"]

ABREVIATURAS = [
    ("CIBS-UniLúrio", "Comité Institucional de Bioética para a Saúde da "
                      "Universidade Lúrio"),
    ("EADSG", "East Africa Diabetes Study Group"),
    ("FITTER", "Forum for Injection Technique and Therapy Expert "
               "Recommendations"),
    ("HCN", "Hospital Central de Nampula"),
    ("IC95%", "Intervalo de confiança a 95%"),
    ("IDS", "Inquérito Demográfico e de Saúde"),
    ("KR-20", "Coeficiente de Kuder-Richardson, fórmula 20"),
    ("NPH", "Neutral Protamine Hagedorn (insulina humana isofânica)"),
    ("NA", "Não aplicável"),
    ("OMS", "Organização Mundial da Saúde"),
    ("OR", "Odds ratio (razão de possibilidades)"),
    ("SDSMAS", "Serviço Distrital de Saúde, Mulher e Acção Social"),
    ("SPSS", "Statistical Package for the Social Sciences"),
    ("STROBE", "Strengthening the Reporting of Observational Studies in "
               "Epidemiology"),
    ("UI", "Unidades internacionais"),
]

# ------------------------------------------------------------ referencias --
FONTES = {
    # epidemiologia global, regional e nacional
    "genitsaridi2026": "Genitsaridi I, Salpea P, Salim A, Sajjadi SF, Tomic D, James S, et al. 11th edition of the IDF Diabetes Atlas: global, regional, and national diabetes prevalence estimates for 2024 and projections for 2050. Lancet Diabetes Endocrinol. 2026;14(2):149-156. doi:10.1016/S2213-8587(25)00299-2. PMID: 41412135.",
    "ncdrisc2024": "NCD Risk Factor Collaboration (NCD-RisC). Worldwide trends in diabetes prevalence and treatment from 1990 to 2022: a pooled analysis of 1108 population-representative studies with 141 million participants. Lancet. 2024;404(10467):2077-2093. doi:10.1016/S0140-6736(24)02317-1. PMID: 39549716.",
    "who2021": "World Health Organization. Keeping the 100-year-old promise: making insulin access universal [Internet]. Geneva: World Health Organization; 2021 [citado 2026 Set 19]. Disponível em: https://www.who.int/publications/i/item/9789240039100",
    "mannegoehler2016": "Manne-Goehler J, Atun R, Stokes A, Goehler A, Houinato D, Houehanou C, et al. Diabetes diagnosis and care in sub-Saharan Africa: pooled analysis of individual data from 12 countries. Lancet Diabetes Endocrinol. 2016;4(11):903-912. doi:10.1016/S2213-8587(16)30181-4. PMID: 27727123.",
    "madede2022": "Madede T, Damasceno A, Lunet N, Augusto O, Silva-Matos C, Beran D, et al. Changes in prevalence and the cascade of care for type 2 diabetes over ten years (2005-2015): results of two nationally representative surveys in Mozambique. BMC Public Health. 2022;22(1):2174. doi:10.1186/s12889-022-14595-7. PMID: 36434584.",
    "madede2024": "Madede T, Mavume Mangunyane E, Munguambe K, Govo V, Beran D, Levitt N, et al. Human resources challenges in the management of diabetes and hypertension in Mozambique. PLoS One. 2024;19(3):e0297676. doi:10.1371/journal.pone.0297676. PMID: 38551894.",
    "mazzalai2025": "Mazzalai E, Nollino L, Ramirez L, de Assis CM, Mataure T, Mainato A, et al. Barriers and facilitators to accessing Non-Communicable Disease services among children, adolescents and young people with Type 1 Diabetes in Mozambique: a quantitative content analysis using the COM-B framework. Arch Public Health. 2025;83(1):138. doi:10.1186/s13690-025-01635-y. PMID: 40437609.",
    "misau2020": "Moçambique. Ministério da Saúde. Plano estratégico multissectorial de prevenção e controlo de doenças não transmissíveis 2020-2029 [Internet]. Maputo: Ministério da Saúde; 2020 [citado 2026 Set 19]. Disponível em: https://extranet.who.int/ncdccs/Data/MOZ_B3_s21_Plano%20Estrat%C3%A9gico%20Multissetorial%20de%20Prevencao%20e%20Controlo%20das%20DNTs%202020-2029%20FINALISSIMA.pdf",
    "misau2023lnme": "Moçambique. Ministério da Saúde. Diploma Ministerial n.º 52/2023, de 19 de Abril: aprova a Lista Nacional de Medicamentos Essenciais. Boletim da República, I Série, n.º 75 [Internet]. Maputo: Imprensa Nacional de Moçambique; 2023 [citado 2026 Set 19]. Disponível em: https://cdn.who.int/media/docs/default-source/essential-medicines/national-essential-medicines-lists-(neml)/afro_neml/mozambique-updated-lista-nacional-de-medicamentos-essenciais-2023.pdf?sfvrsn=22c3626a_1",
    "ine2024": "Instituto Nacional de Estatística, ICF. Moçambique Inquérito Demográfico e de Saúde 2022-23: relatório definitivo [Internet]. Maputo e Rockville: INE e ICF; 2024 [citado 2026 Set 19]. Disponível em: https://dhsprogram.com/pubs/pdf/FR389/FR389.pdf",
    "ine2021": "Instituto Nacional de Estatística. IV Recenseamento Geral da População e Habitação 2017: resultados definitivos, província de Nampula [Internet]. Nampula: Instituto Nacional de Estatística; 2021 [citado 2026 Set 19]. Disponível em: http://www.sina.gov.mz/wp-content/uploads/2024/05/NAMPULA-RESUTADOS-DEFINITIVOS-DO-CENSO-2017.pdf",
    # recomendacoes sobre tecnica e conservacao
    "frid2016": "Frid AH, Kreugel G, Grassi G, Halimi S, Hicks D, Hirsch LJ, et al. New Insulin Delivery Recommendations. Mayo Clin Proc. 2016;91(9):1231-55. doi:10.1016/j.mayocp.2016.06.010. PMID: 27594187.",
    "klonoff2025": "Klonoff DC, Berard L, Franco DR, Gentile S, Gomez OV, Hussein Z, et al. Advance Insulin Injection Technique and Education With FITTER Forward Expert Recommendations. Mayo Clin Proc. 2025;100(4):682-699. doi:10.1016/j.mayocp.2025.01.004. PMID: 40180487.",
    "bahendeka2019": "Bahendeka S, Kaushik R, Swai AB, Otieno F, Bajaj S, Kalra S, et al. EADSG Guidelines: Insulin Storage and Optimisation of Injection Technique in Diabetes Management. Diabetes Ther. 2019;10(2):341-366. doi:10.1007/s13300-019-0574-x. PMID: 30815830.",
    "frid2016itq": "Frid AH, Hirsch LJ, Menchior AR, Morel DR, Strauss KW. Worldwide Injection Technique Questionnaire Study: Population Parameters and Injection Practices. Mayo Clin Proc. 2016;91(9):1212-23. doi:10.1016/j.mayocp.2016.06.011. PMID: 27594185.",
    "frid2016lh": "Frid AH, Hirsch LJ, Menchior AR, Morel DR, Strauss KW. Worldwide Injection Technique Questionnaire Study: Injecting Complications and the Role of the Professional. Mayo Clin Proc. 2016;91(9):1224-30. doi:10.1016/j.mayocp.2016.06.012. PMID: 27594186.",
    # lipohipertrofia e reutilizacao
    "wang2021": "Wang K, Zhang S, Liu C, Chen Y. A meta-analysis and meta-regression on the prevalence of lipohypertrophy in diabetic patients on insulin therapy. Therapie. 2021;76(6):617-628. doi:10.1016/j.therap.2021.04.002. PMID: 33958198.",
    "mader2024": "Mader JK, Fornengo R, Hassoun A, Heinemann L, Kulzer B, Monica M, et al. Relationship Between Lipohypertrophy, Glycemic Control, and Insulin Dosing: A Systematic Meta-Analysis. Diabetes Technol Ther. 2024;26(5):351-362. doi:10.1089/dia.2023.0491. PMID: 38215209.",
    "mader2026": "Mader JK, Fornengo R, Hassoun A, Heinemann L, Kulzer B, Monica M, et al. Risk factors for Lipohypertrophy in People With Insulin-Treated Diabetes: A Systematic Meta-Analysis. J Diabetes Sci Technol. 2026;20(4):1342-1352. doi:10.1177/19322968251325569. PMID: 40109173.",
    "famulla2016": "Famulla S, Hövelmann U, Fischer A, Coester HV, Hermanski L, Kaltheuner M, et al. Insulin Injection Into Lipohypertrophic Tissue: Blunted and More Variable Insulin Absorption and Action and Impaired Postprandial Glucose Control. Diabetes Care. 2016;39(9):1486-92. doi:10.2337/dc16-0610. PMID: 27411698.",
    "gentile2016": "Gentile S, Guarino G, Giancaterini A, Guida P, Strollo F. A suitable palpation technique allows to identify skin lipohypertrophic lesions in insulin-treated people with diabetes. Springerplus. 2016;5:563. doi:10.1186/s40064-016-1978-y. PMID: 27213130.",
    "guo2026": "Guo L, Klonoff DC, Al Sifri SN, Bee YM, Calliari LE, Chen L, et al. Consensus Recommendations on Lipohypertrophy: Insights From an International Panel of Experts. Diabetes Res Clin Pract. 2026;239:113401. doi:10.1016/j.diabres.2026.113401. PMID: 42398590.",
    "xu2025": "Xu H, Cheng Z, Li X, Mu C, Bao D, Xing Q. Comparison of ultrasound scanning and clinical examination for detecting insulin injection related Lipohypertrophy and construction of Lipohypertrophy classification table. Diabet Med. 2025;42(3):e15458. doi:10.1111/dme.15458. PMID: 39462246.",
    "bazezew2026": "Bazezew ZA, Zeleke TK, Negesse CT, Mekonnen GB. Lipodystrophy and associated factors among patients with diabetes receiving insulin therapy: a multicenter study in Ethiopia. Sci Rep. 2026;16(1). doi:10.1038/s41598-026-41108-y. PMID: 41833962.",
    "alemseged2024": "Alemseged T, Mohamed AA, Hailu AG, Hadgu FB, Mohammedamin MM. Prevalence and associated factors of lipodystrophy in type 1 diabetic children and adolescents at Ayder Comprehensive Specialized Hospital, Tigray, Ethiopia. BMC Pediatr. 2024;24(1):548. doi:10.1186/s12887-024-05018-0. PMID: 39182067.",
    "zabaleta2016": "Zabaleta-Del-Olmo E, Vlacho B, Jodar-Fernández L, Urpí-Fernández AM, Lumillo-Gutiérrez I, Agudo-Ugena J, et al. Safety of the reuse of needles for subcutaneous insulin injection: A systematic review and meta-analysis. Int J Nurs Stud. 2016;60:121-32. doi:10.1016/j.ijnurstu.2016.04.010. PMID: 27297374.",
    "berlanda2024": "Berlanda G, Telo GH, Gossenheimer AN, Auler A, da Silva ES, Rodrigues PG, et al. Impact of Syringe and Needle Reuse on the Clinical Outcomes of Patients With Type 2 Diabetes: A 12-Week Randomized Clinical Trial. Diabetes Care. 2024;47(12):2146-2154. doi:10.2337/dc24-0157. PMID: 39405489.",
    "abujbara2022": "Abujbara M, Khreisat EA, Khader Y, Ajlouni KM. Effect of Insulin Injection Techniques on Glycemic Control Among Patients with Diabetes. Int J Gen Med. 2022;15:8593-8602. doi:10.2147/IJGM.S393597. PMID: 36545247.",
    # estabilidade e conservacao
    "richter2023": "Richter B, Bongaerts B, Metzendorf MI. Thermal stability and storage of human insulin. Cochrane Database Syst Rev. 2023;11(11):CD015385. doi:10.1002/14651858.CD015385.pub2. PMID: 37930742.",
    "kaufmann2021": "Kaufmann B, Boulle P, Berthou F, Fournier M, Beran D, Ciglenecki I, et al. Heat-stability study of various insulin types in tropical temperature conditions: New insights towards improving diabetes care. PLoS One. 2021;16(2):e0245372. doi:10.1371/journal.pone.0245372. PMID: 33534816.",
    "ogle2016": "Ogle GD, Abdullah M, Mason D, Januszewski AS, Besançon S. Insulin storage in hot climates without refrigeration: temperature reduction efficacy of clay pots and other techniques. Diabet Med. 2016;33(11):1544-1553. doi:10.1111/dme.13194. PMID: 27472257.",
    "kimaro2025": "Kimaro E, John J, Damiano P, Konje ET, Mori AT, Kidenya BR, et al. Impact of insulin storage and syringe reuse on insulin sterility in diabetes mellitus patients in Mwanza Tanzania. Sci Rep. 2025;15(1):6232. doi:10.1038/s41598-025-91029-5. PMID: 39979407.",
    # estudos africanos de pratica
    "netere2020": "Netere AK, Ashete E, Gebreyohannes EA, Belachew SA. Evaluations of knowledge, skills and practices of insulin storage and injection handling techniques of diabetic patients in Ethiopian primary hospitals. BMC Public Health. 2020;20(1):1537. doi:10.1186/s12889-020-09622-4. PMID: 33046046.",
    "nasir2021": "Nasir BB, Buseir MS, Muhammed OS. Knowledge, attitude and practice towards insulin self-administration and associated factors among diabetic patients at Zewditu Memorial Hospital, Ethiopia. PLoS One. 2021;16(2):e0246741. doi:10.1371/journal.pone.0246741. PMID: 33556090.",
    "feleke2025": "Feleke WM, Olis CS, Endris AH, Hassen SL, Ali YS, Abate Beyene D. Knowledge, Practice, and Associated Factors of Insulin Self-Administration in Patients With Diabetes at Dessie City Governmental Hospital Follow Up Clinic, Amhara Region, North East Ethiopia: Cross-Sectional Study. Health Sci Rep. 2025;8(4):e70631. doi:10.1002/hsr2.70631. PMID: 40226177.",
    "negash2023": "Negash Z, Tadiwos A, Urgessa EM, Gebretekle GB, Abebe E, Fentie AM. Insulin injection practice and health related quality of life among individuals with diabetes at Tikur Anbessa Specialized Hospital, Ethiopia: a cross-sectional study. Health Qual Life Outcomes. 2023;21(1):38. doi:10.1186/s12955-023-02123-z. PMID: 37143082.",
    "hacene2020": "Hacene MNB, Saker M, Youcef A, Koudri S, Cheriet S, Merzouk H, et al. Insulin injection technique in the western region of Algeria, Tlemcen. Pan Afr Med J. 2020;36:327. doi:10.11604/pamj.2020.36.327.21278. PMID: 33193981.",
    "dagnew2026": "Dagnew SB, Zewdu WS, Wondm SA, Moges TA, Dagnew FN, Anberbr SS, et al. Impacts of insulin storage and injection techniques intervention on glycemic control among patients with diabetes in northwest Ethiopia: a quasi-experimental study. Ther Adv Endocrinol Metab. 2026;17:20420188261417096. doi:10.1177/20420188261417096. PMID: 41694291.",
    "basazn2016": "Basazn Mekuria A, Melaku Gebresillassie B, Asfaw Erku D, Taye Haile K, Melese Birru E. Knowledge and Self-Reported Practice of Insulin Injection Device Disposal among Diabetes Patients in Gondar Town, Ethiopia: A Cross-Sectional Study. J Diabetes Res. 2016;2016:1897517. doi:10.1155/2016/1897517. PMID: 27738637.",
    # educacao do doente
    "ichikawa2022": "Ichikawa M, Akiyama T, Tsujimoto Y, Anan K, Yamakawa T, Terauchi Y. Efficacy of education on injection technique for patients diagnosed with diabetes with lipohypertrophy: systematic review and meta-analysis. BMJ Open. 2022;12(3):e055529. doi:10.1136/bmjopen-2021-055529. PMID: 35256444.",
    "selvadurai2021": "Selvadurai S, Cheah KY, Ching MW, Kamaruddin H, Lee XY, Ngajidin RM, et al. Impact of pharmacist insulin injection re-education on glycemic control among type II diabetic patients in primary health clinics. Saudi Pharm J. 2021;29(7):670-676. doi:10.1016/j.jsps.2021.04.028. PMID: 34400860.",
    "kapoor2016": "Kapoor U, Ramasamy G, Selvaraj K, Sahoo JP, Kar SS. Does one-to-one demonstration with insulin pads by health-care providers improves the insulin administration techniques among diabetic patients of a Tertiary Care Teaching Hospital in South India?. Indian J Endocrinol Metab. 2016;20(6):767-771. doi:10.4103/2230-8210.192904. PMID: 27867877.",
    "talevski2020": "Talevski J, Wong Shee A, Rasmussen B, Kemp G, Beauchamp A. Teach-back: A systematic review of implementation and impacts. PLoS One. 2020;15(4):e0231350. doi:10.1371/journal.pone.0231350. PMID: 32287296.",
    "mbanda2021": "Mbanda N, Dada S, Bastable K, Ingalill GB, Ralf W S. A scoping review of the use of visual aids in health education materials for persons with low-literacy levels. Patient Educ Couns. 2021;104(5):998-1017. doi:10.1016/j.pec.2020.11.034. PMID: 33339657.",
    # metodologia e etica
    "wang2020": "Wang X, Ji X. Sample Size Estimation in Clinical Research: From Randomized Controlled Trials to Observational Studies. Chest. 2020;158(1S):S12-S20. doi:10.1016/j.chest.2020.03.010. PMID: 32658647.",
    "peduzzi1996": "Peduzzi P, Concato J, Kemper E, Holford TR, Feinstein AR. A simulation study of the number of events per variable in logistic regression analysis. J Clin Epidemiol. 1996;49(12):1373-9. doi:10.1016/s0895-4356(96)00236-3. PMID: 8970487.",
    "almanasreh2019": "Almanasreh E, Moles R, Chen TF. Evaluation of methods used for estimating content validity. Res Social Adm Pharm. 2019;15(2):214-221. doi:10.1016/j.sapharm.2018.03.066. PMID: 29606610.",
    "tsang2017": "Tsang S, Royse CF, Terkawi AS. Guidelines for developing, translating, and validating a questionnaire in perioperative and pain medicine. Saudi J Anaesth. 2017;11(Suppl 1):S80-S89. doi:10.4103/sja.SJA_203_17. PMID: 28616007.",
    "mchugh2012": "McHugh ML. Interrater reliability: the kappa statistic. Biochem Med (Zagreb). 2012;22(3):276-82. PMID: 23092060.",
    "vonelm2007": "von Elm E, Altman DG, Egger M, Pocock SJ, Gøtzsche PC, Vandenbroucke JP. The Strengthening the Reporting of Observational Studies in Epidemiology (STROBE) statement: guidelines for reporting observational studies. PLoS Med. 2007;4(10):e296. doi:10.1371/journal.pmed.0040296. PMID: 17941714.",
    "wma2025": "World Medical Association. World Medical Association Declaration of Helsinki: Ethical Principles for Medical Research Involving Human Participants. JAMA. 2025;333(1):71-74. doi:10.1001/jama.2024.21972. PMID: 39425955.",
    "lei3de2023": "República de Moçambique. Lei n.º 3/2023, de 8 de Junho: Lei de Investigação em Saúde Humana [Internet]. Maputo: Imprensa Nacional de Moçambique; 2023 [citado 2026 Set 19]. Disponível em: https://anarme.gov.mz/download/lei-3-2023-de-8-de-junho-lei-de-investigacao-em-saude-humana/",
}
SEMINAIS = {
    "peduzzi1996": "Estudo de simulação original que fundamenta a regra de "
                   "pelo menos 10 eventos por variável na regressão logística.",
    "mchugh2012": "Referência metodológica de base para a interpretação do "
                  "kappa de Cohen em estudos de saúde.",
    "vonelm2007": "Declaração original da norma de relato STROBE, ainda em "
                  "vigor para estudos observacionais.",
}

# ----------------------------------------------------- 1. introducao --------
INTRODUCAO = [
    P("A diabetes mellitus afecta uma fracção crescente da população adulta "
      "mundial. Segundo a 11.ª edição do Atlas da Federação Internacional de "
      "Diabetes, 589 milhões de adultos dos 20 aos 79 anos viviam com a "
      "doença em 2024, o equivalente a 11,11% desse grupo etário, e "
      "prevê-se que o número atinja 853 milhões em 2050 {genitsaridi2026}. "
      "A análise conjunta de 1.108 estudos de base populacional mostrou que "
      "o peso da diabetes não tratada recai cada vez mais sobre os países de "
      "baixo e médio rendimento, onde a cobertura do tratamento não "
      "acompanhou o aumento da prevalência; essa cobertura era, em 2022, a "
      "mais baixa do mundo na África subsariana e no Sul da Ásia, e inferior "
      "a 10% nalguns países africanos {ncdrisc2024}. A insulina, descoberta "
      "há mais de um século, continua a ser indispensável para as pessoas "
      "com diabetes tipo 1 e para uma parte das pessoas com diabetes tipo 2: "
      "a Organização Mundial da Saúde (OMS) estima que cerca de 63 milhões "
      "de pessoas com diabetes tipo 2 precisem de insulina e que apenas "
      "metade delas a receba {who2021}."),
    P("O acesso ao medicamento não garante, porém, o benefício terapêutico. "
      "A insulina é uma proteína sensível ao calor e à congelação, "
      "administrada pelo próprio doente, uma ou várias vezes por dia, por "
      "via subcutânea, e o seu efeito depende de uma sequência de passos "
      "executados sem supervisão: homogeneizar as suspensões, aspirar a "
      "dose certa, escolher e alternar o local, inserir a agulha na "
      "profundidade correcta e eliminar o material com segurança "
      "{frid2016,klonoff2025}. Um dos maiores inquéritos alguma vez "
      "realizados em diabetes, com 13.289 doentes de 423 centros de 42 "
      "países, mostrou que a hemoglobina "
      "glicada era, em média, 0,5% mais elevada nos doentes com "
      "lipohipertrofia e também mais alta quando a rotação dos locais era "
      "incorrecta e as agulhas eram reutilizadas, situações em que as "
      "hipoglicemias inesperadas e a variabilidade glicémica eram mais "
      "frequentes {frid2016itq}. A mesma investigação revelou que menos de "
      "40% dos doentes tinham recebido instruções sobre a técnica nos seis "
      "meses anteriores e que 10% nunca tinham sido ensinados, apesar de "
      "injectarem, em média, há quase nove anos {frid2016lh}."),
    P("Na África subsariana, estes problemas acumulam-se com outros. Numa "
      "análise de inquéritos nacionais de 12 países, a mediana da "
      "prevalência de diabetes foi de 5% e a mediana da proporção de pessoas "
      "com diabetes que usava insulina foi de apenas 11% "
      "{mannegoehler2016}. A OMS reconhece que a exigência de conservação a "
      "frio é um obstáculo importante nos climas quentes e onde o acesso à "
      "refrigeração ou a electricidade fiável é limitado, e que o custo das "
      "seringas levou à reutilização de agulhas em quase todos os países "
      "inquiridos {who2021}. Os estudos etíopes, que reúnem a maior parte da "
      "evidência africana, descrevem conhecimentos e práticas apenas "
      "moderados sobre a conservação e a injecção da insulina "
      "{netere2020,nasir2021} e prevalências de lipodistrofia superiores a "
      "40% {dagnew2026,bazezew2026}; na Tanzânia, quase metade dos doentes "
      "guardava a insulina em potes de barro e parte dos frascos assim "
      "conservados estava contaminada {kimaro2025}."),
    P("Em Moçambique, a prevalência de diabetes nos adultos dos 25 aos 64 "
      "anos passou de 2,9% em 2005 para 7,4% em 2014/2015, e apenas 10% das "
      "pessoas com diabetes conheciam a sua condição {madede2022}. O Plano "
      "Estratégico Multissectorial de Prevenção e Controlo de Doenças Não "
      "Transmissíveis 2020-2029 fixa como meta que pelo menos 46,6% das "
      "pessoas com hipertensão e diabetes conheçam a sua condição clínica e "
      "prevê o reforço dos recursos de educação e apoio aos doentes "
      "{misau2020}. A Lista Nacional de Medicamentos Essenciais inclui a "
      "insulina humana solúvel, a insulina humana isofânica, a mistura "
      "bifásica 30/70 e a insulina glargina, todas em frasco multidose de "
      "10 mL, as insulinas simples com 100 unidades internacionais (UI) por "
      "mililitro e a mistura na proporção de 30/70 {misau2023lnme}, o "
      "que faz da seringa o dispositivo de administração mais provável no "
      "sector público. Os profissionais moçambicanos descrevem, por outro "
      "lado, uma formação orientada sobretudo para as doenças infecciosas e "
      "a falta de equipamento, consumíveis e medicamentos para as doenças "
      "não transmissíveis {madede2024}, e os jovens com diabetes tipo 1 "
      "referem interacções insuficientes com os profissionais e necessidade "
      "de maior literacia em saúde {mazzalai2025}."),
    P("As condições domésticas em que a insulina é guardada acrescentam "
      "risco. Segundo o Inquérito Demográfico e de Saúde (IDS) 2022-23, "
      "apenas 18,8% dos agregados familiares moçambicanos possuem "
      "frigorífico ou congelador (43,0% nas áreas urbanas e 6,5% nas "
      "rurais) e 35,9% dispõem de energia eléctrica {ine2024}. A província "
      "de Nampula, a mais populosa do país, com 5.758.920 habitantes em "
      "2017, dos quais 798.462 no distrito de Nampula {ine2021}, tem 31,7% "
      "da sua população no quintil de riqueza mais baixo, e apenas 26,1% "
      "das mulheres e 55,8% dos homens dos 15 aos 49 anos são alfabetizados, "
      "contra 46,6% e 68,5% no conjunto do país {ine2024}. Nestas "
      "condições, a conservação em potes de barro, em recipientes com água "
      "ou em locais expostos ao calor, a reutilização prolongada das "
      "seringas e a dificuldade em ler instruções escritas são problemas "
      "plausíveis que nunca foram medidos na província."),
    P("O Hospital Central de Nampula (HCN), unidade de referência do norte "
      "do país, acompanha em consulta externa adultos com diabetes em "
      "insulinoterapia provenientes da cidade e de outros distritos. Não foi "
      "encontrado nenhum estudo moçambicano que tenha observado a técnica de "
      "auto-administração, examinado os locais de injecção ou descrito a "
      "conservação da insulina no domicílio; a evidência mais próxima vem "
      "da Etiópia, da Tanzânia e da Argélia {netere2020,kimaro2025,"
      "hacene2020}. O presente estudo propõe-se avaliar a técnica de "
      "auto-administração e as práticas de conservação domiciliária da "
      "insulina em adultos com diabetes seguidos no HCN, em 2027, e "
      "identificar os factores associados aos erros, de modo a orientar a "
      "elaboração de materiais de educação ao doente adaptados à realidade "
      "local."),
]

# ----------------------------------------------------- 2. problema ----------
PROBLEMA = [
    P("O problema que motiva este estudo é a possibilidade de uma parte "
      "importante dos doentes que recebem insulina no HCN não obter dela o "
      "efeito pretendido por erros na forma como a preparam, injectam e "
      "guardam. A insulina fornecida pelo Serviço Nacional de Saúde é "
      "dispensada em frascos multidose para administração com seringa "
      "{misau2023lnme}, o que obriga o doente a homogeneizar as suspensões, "
      "a medir a dose numa escala graduada e a decidir onde e como injectar, "
      "tarefas exigentes para pessoas com pouca escolaridade ou dificuldades "
      "de visão. Em hospitais etíopes com perfil semelhante, apenas 49,0% "
      "dos doentes injectavam com o ângulo adequado e 71,8% repetiam com "
      "frequência o mesmo local {nasir2021}, e só 60,75% praticavam a "
      "rotação dos locais durante a demonstração observada {netere2020}."),
    P("As consequências destes erros são clínicas e económicas. A rotação "
      "incorrecta dos locais e a reutilização de agulhas são os factores de "
      "risco modificáveis mais fortes da lipohipertrofia {mader2026}, e a "
      "insulina injectada em tecido lipohipertrófico é absorvida de forma "
      "reduzida e muito mais variável, com glicemias pós-prandiais pelo "
      "menos 26% mais elevadas {famulla2016}. Nos doentes com "
      "lipohipertrofia, a hipoglicemia inexplicada é cerca de sete vezes "
      "mais provável e o consumo diário de insulina é maior {mader2024}. A "
      "conservação inadequada acrescenta outro risco, porque a imersão dos "
      "frascos em água favorece a contaminação e a perda de potência e pode "
      "originar abcessos no local de injecção {bahendeka2019}. Quando o "
      "controlo glicémico falha, a dose tende a ser aumentada: os doentes "
      "com lipohipertrofia consomem, em média, mais 7,68 UI de insulina por "
      "dia {mader2024}, num sistema de saúde em que metade dos países de "
      "baixo e médio rendimento inquiridos não fornece seringas em "
      "quantidade suficiente {who2021}."),
    P("No HCN não se conhece a proporção de doentes com técnica adequada, "
      "os erros mais frequentes, a prevalência de lipohipertrofia, nem onde "
      "e como a insulina é guardada em casas que, na sua maioria, não terão "
      "frigorífico {ine2024}. Também não se sabe que características dos "
      "doentes e da formação que receberam se associam aos erros. Sem esta "
      "informação, o aconselhamento prestado na consulta e na farmácia "
      "repete mensagens genéricas, pensadas para contextos com refrigeração "
      "e elevada literacia, e não aborda os erros que de facto ocorrem, "
      "quando os estudos de intervenção atribuem a melhoria da técnica e do "
      "controlo glicémico a uma educação dirigida e repetida "
      "{dagnew2026,selvadurai2021}."),
]
PERGUNTA = ("Qual é a proporção de adultos com diabetes seguidos no Hospital "
            "Central de Nampula que administram e conservam a insulina de "
            "forma adequada, qual é a prevalência de lipohipertrofia nos "
            "locais de injecção e que factores se associam à técnica "
            "inadequada e à lipohipertrofia?")
DELIMITACAO = [
    P("O estudo decorre na consulta externa do HCN que acompanha adultos "
      "com diabetes em insulinoterapia [confirmar junto da Direcção Clínica "
      "do HCN a designação, os dias e o horário desta consulta], na cidade "
      "de Nampula, com recolha de dados entre Março e Maio de 2027. A "
      "população é constituída pelos doentes com 18 ou mais anos, com "
      "diabetes tipo 1 ou tipo 2, em insulinoterapia há pelo menos três "
      "meses e que administram a insulina a si próprios. O objecto de estudo "
      "compreende a técnica de auto-administração observada (preparação da "
      "dose, escolha e rotação dos locais, inserção da agulha, reutilização "
      "e eliminação do material), a lipohipertrofia detectada por exame "
      "clínico e as práticas de conservação e transporte da insulina no "
      "domicílio."),
    P("Ficam fora do âmbito as crianças e os adolescentes, os doentes cuja "
      "insulina é administrada por familiares ou por profissionais, os "
      "doentes internados, a medição da temperatura nos domicílios, a "
      "determinação laboratorial da potência ou da esterilidade da insulina "
      "e a avaliação da eficácia de uma intervenção educativa, que dependerá "
      "dos resultados deste estudo."),
]

# ----------------------------------------------------- 3. objectivos --------
OBJECTIVO_GERAL = (
    "Avaliar a técnica de auto-administração e as práticas de conservação "
    "domiciliária da insulina, e os factores associados, em adultos com "
    "diabetes seguidos na consulta externa do Hospital Central de Nampula, "
    "entre Março e Maio de 2027, de modo a fundamentar materiais de "
    "educação ao doente.")
OBJECTIVOS_ESPECIFICOS = [
    "Caracterizar o perfil sociodemográfico, clínico e terapêutico dos "
    "adultos com diabetes em insulinoterapia, incluindo o tipo de diabetes, "
    "a duração e o esquema da insulinoterapia, o dispositivo utilizado e a "
    "formação recebida sobre a técnica.",
    "Determinar a proporção de doentes com técnica de auto-administração "
    "adequada, por observação directa com lista de verificação, e descrever "
    "a frequência de cada erro na preparação da dose, na escolha e rotação "
    "dos locais, na inserção da agulha, na reutilização e na eliminação do "
    "material.",
    "Estimar a prevalência de lipohipertrofia nos locais de injecção, por "
    "inspecção e palpação padronizadas.",
    "Descrever as condições e as práticas de conservação e transporte da "
    "insulina no domicílio, incluindo a disponibilidade de frigorífico e os "
    "métodos alternativos de arrefecimento, e determinar a proporção de "
    "doentes com conservação adequada.",
    "Analisar a associação entre as características sociodemográficas, "
    "clínicas e de formação dos doentes e a técnica inadequada, e entre a "
    "rotação incorrecta dos locais e a reutilização de agulhas e a presença "
    "de lipohipertrofia.",
]

# ----------------------------------------------------- 4. hipoteses ---------
HIPOTESES_INTRO = [
    P("As hipóteses referem-se ao objectivo específico 5 e serão testadas "
      "com o teste do qui-quadrado e a regressão logística, ao nível de "
      "significância de 5%. Os objectivos 1 a 4 são descritivos e "
      "orientam-se pelas questões de investigação apresentadas a seguir."),
]
HIPOTESES = [
    ("H0 (a)", "não existe associação estatisticamente significativa entre "
               "a escolaridade, a duração da insulinoterapia, a formação "
               "com demonstração prática ou a reeducação nos últimos seis "
               "meses e a técnica inadequada de auto-administração."),
    ("H1 (a)", "existe associação estatisticamente significativa entre pelo "
               "menos uma destas características e a técnica inadequada de "
               "auto-administração."),
    ("H0 (b)", "não existe associação estatisticamente significativa entre "
               "a rotação incorrecta dos locais de injecção ou a "
               "reutilização da mesma agulha mais de cinco vezes e a "
               "presença de lipohipertrofia."),
    ("H1 (b)", "existe associação estatisticamente significativa entre a "
               "rotação incorrecta dos locais ou a reutilização da mesma "
               "agulha mais de cinco vezes e a presença de lipohipertrofia."),
]
QUESTOES = [
    "Qual é o perfil sociodemográfico, clínico e terapêutico dos adultos "
    "que administram a si próprios insulina e que formação receberam sobre "
    "a técnica?",
    "Que proporção destes doentes executa a técnica de auto-administração "
    "de forma adequada e quais são os erros mais frequentes?",
    "Qual é a prevalência de lipohipertrofia nos locais de injecção e em "
    "que regiões do corpo se localiza?",
    "Onde e como é guardada e transportada a insulina e que proporção de "
    "doentes cumpre os critérios de conservação adequada?",
]

# ----------------------------------------------------- 5. justificativa -----
JUSTIFICATIVA_INTRO = [
    P("A escolha do tema resulta de três constatações: a diabetes cresce em "
      "Moçambique mais depressa do que a capacidade dos serviços para a "
      "diagnosticar e tratar {madede2022}, a insulina é um medicamento "
      "essencial, caro e difícil de conservar {who2021,misau2023lnme}, e o "
      "erro na sua utilização é frequente, silencioso e corrigível através "
      "da educação {ichikawa2022,dagnew2026}. O farmacêutico, que dispensa "
      "a insulina e as seringas em cada renovação da prescrição, está em "
      "posição privilegiada para detectar e corrigir esses erros, desde que "
      "saiba quais são."),
]
JUSTIFICATIVA = {
    "cientifica": [
        P("Não se conhece nenhum estudo publicado em Moçambique sobre a "
          "técnica de injecção ou a conservação domiciliária da insulina, e "
          "a evidência africana provém sobretudo da Etiópia e baseia-se, na "
          "maior parte dos casos, no auto-relato {nasir2021,negash2023}. O "
          "estudo produz evidência primária por observação directa, com uma "
          "lista de verificação baseada nas recomendações internacionais e "
          "regionais {klonoff2025,bahendeka2019}, exame padronizado dos "
          "locais de injecção {gentile2016,guo2026} e medição da "
          "concordância entre observadores, o que permite comparar os "
          "resultados com estudos de outros países e examinar a "
          "aplicabilidade das recomendações de conservação sem frigorífico, "
          "cuja base de evidência clínica ainda é limitada {richter2023}."),
    ],
    "academica": [
        P("Para a Faculdade de Ciências de Saúde da Universidade Lúrio, o "
          "trabalho aproxima a formação do licenciado em Farmácia da prática "
          "clínica, exercitando competências de observação estruturada, "
          "validação de instrumentos, análise estatística e comunicação com "
          "o doente. Os instrumentos validados e traduzidos para emakhuwa "
          "poderão ser reutilizados em trabalhos futuros, por exemplo num "
          "ensaio de intervenção educativa ou num estudo de medição da "
          "temperatura nos domicílios, e o relato segue a norma "
          "Strengthening the Reporting of Observational Studies in "
          "Epidemiology (STROBE) {vonelm2007}, o que facilita a publicação "
          "dos resultados."),
    ],
    "social": [
        P("Os doentes com diabetes em Nampula vivem, na sua maioria, em "
          "agregados sem frigorífico e com baixa literacia {ine2024}. Uma "
          "técnica incorrecta traduz-se em hipoglicemias, descompensações, "
          "internamentos e despesas para as famílias, enquanto a sua "
          "correcção custa pouco: a lipohipertrofia pode ser detectada por "
          "palpação e prevenida com rotação correcta e agulhas novas "
          "{guo2026}, e a educação com demonstração melhorou a técnica e o "
          "controlo glicémico num hospital etíope com poucos recursos "
          "{dagnew2026}. Os materiais de educação que resultarem deste "
          "estudo, com pictogramas e texto em português e emakhuwa, "
          "destinam-se a pessoas com pouca escolaridade, para as quais as "
          "ajudas visuais desenvolvidas com os próprios destinatários se "
          "mostraram eficazes {mbanda2021}."),
    ],
    "politica": [
        P("O estudo responde ao Plano Estratégico Multissectorial de "
          "Prevenção e Controlo de Doenças Não Transmissíveis 2020-2029, que "
          "prevê o reforço dos recursos de educação e apoio aos doentes e "
          "dos mecanismos de disponibilidade dos medicamentos essenciais "
          "destas doenças {misau2020}. Os resultados podem fundamentar a "
          "inclusão de orientações sobre a técnica de injecção e a "
          "conservação sem frigorífico nas normas nacionais, a revisão da "
          "quantidade de seringas dispensadas por doente, cuja escassez "
          "favorece a reutilização {who2021}, e a atribuição formal ao "
          "farmacêutico hospitalar do ensino e da reavaliação periódica da "
          "técnica, à semelhança do que se fez noutros países com benefício "
          "demonstrado {selvadurai2021}."),
    ],
}

# ----------------------------------------------------- 6. revisao -----------
REVISAO = [
    ("Diabetes mellitus, insulinoterapia e definições operacionais", [
        P("Em termos epidemiológicos, considera-se que uma pessoa tem "
          "diabetes quando apresenta glicemia plasmática em jejum igual ou "
          "superior a 7,0 mmol/L, hemoglobina glicada igual ou superior a "
          "6,5% ou toma medicação para a diabetes {ncdrisc2024}. A insulina "
          "é indispensável na diabetes tipo 1 e necessária numa parte das "
          "pessoas com diabetes tipo 2, das quais apenas cerca de metade a "
          "recebe {who2021}. A insulinoterapia não se limita, contudo, à "
          "prescrição: o doente passa a executar sozinho, uma ou mais vezes "
          "por dia, uma tarefa técnica que noutros medicamentos injectáveis "
          "cabe a profissionais de saúde, e o êxito do tratamento depende "
          "tanto da dose prescrita como da forma como essa dose chega ao "
          "tecido subcutâneo."),
        P("No sector público moçambicano estão disponíveis a insulina humana "
          "solúvel, de acção curta, a insulina humana isofânica, conhecida "
          "como Neutral Protamine Hagedorn (NPH), de acção intermédia, a "
          "mistura bifásica de insulina solúvel e isofânica na proporção "
          "30/70 e a insulina glargina, análogo de acção prolongada, todas "
          "em frasco de 10 mL e com nível de prescrição 3 na "
          "lista nacional {misau2023lnme}. A insulina NPH e as misturas "
          "bifásicas são suspensões turvas que têm de ser homogeneizadas "
          "antes de cada aspiração; a falta de homogeneização associou-se a "
          "maior consumo diário de insulina no inquérito internacional "
          "{frid2016itq} e, na Argélia, os doentes desconheciam a técnica "
          "correcta de ressuspensão {hacene2020}. Num hospital de referência "
          "etíope, 62,1% dos doentes usavam apenas insulina de acção "
          "intermédia e 91,2% injectavam duas vezes por dia {negash2023}, "
          "padrão que se espera encontrar também em Nampula, dada a "
          "composição da lista nacional."),
        P("Neste estudo, a técnica de auto-administração define-se como o "
          "conjunto de passos executados pelo próprio doente desde a "
          "verificação do frasco até à eliminação da seringa, observados com "
          "a lista de verificação do Apêndice A, e considera-se adequada "
          "quando o doente cumpre pelo menos 80% dos itens aplicáveis e não "
          "comete nenhum erro crítico. A conservação domiciliária adequada "
          "exige o cumprimento simultâneo de cinco critérios derivados das "
          "recomendações da OMS e do East Africa Diabetes Study Group "
          "(EADSG): insulina nunca congelada, frascos sem contacto com água, "
          "protegidos do sol e de fontes de calor, frasco em uso descartado "
          "até 28 dias após a abertura e reservas para mais de dois meses "
          "mantidas em frigorífico {who2021,bahendeka2019}. A lipohipertrofia "
          "define-se como o espessamento localizado do tecido subcutâneo, de "
          "consistência elástica ou firme, num local de injecção, detectado "
          "por inspecção e palpação estruturada {gentile2016,guo2026}."),
    ]),
    ("Técnica de injecção recomendada: preparação, locais, rotação, "
     "inserção e eliminação", [
        P("As recomendações do Forum for Injection Technique and Therapy "
          "Expert Recommendations (FITTER), redigidas em 2015 por 183 "
          "peritos de 54 países com base num inquérito internacional às "
          "práticas, organizam a técnica em torno da anatomia, da "
          "fisiologia, da patologia, da psicologia e da tecnologia "
          "{frid2016}. Entre as mais importantes contam-se o uso das agulhas "
          "mais curtas (4 mm para caneta e 6 mm para seringa) como primeira "
          "escolha em todos os doentes, a prevenção da injecção "
          "intramuscular, sobretudo com insulinas de acção prolongada, pelo "
          "risco de hipoglicemia grave, a proibição de injectar em zonas de "
          "lipohipertrofia, a rotação correcta dos locais e a eliminação "
          "segura do material cortante {frid2016}. A actualização FITTER "
          "Forward, preparada em 2023 e 2024 por 16 especialistas de 13 "
          "países, descreve os procedimentos para caneta e seringa desde a "
          "conservação da insulina até à eliminação da agulha e propõe "
          "programas estruturados de formação dos doentes {klonoff2025}."),
        P("Como estas recomendações não contemplam as limitações dos países "
          "de baixo e médio rendimento, o EADSG reuniu em Kigali, em Março "
          "de 2018, profissionais e doentes para as adaptar à África "
          "Oriental {bahendeka2019}. As orientações resultantes recomendam "
          "agulhas de 6 mm quando se usa seringa, a prega cutânea nos "
          "doentes emagrecidos sempre que a agulha seja mais longa do que a "
          "de 4 mm, e evitar a inclinação excessiva da agulha, que deposita "
          "a insulina logo abaixo da epiderme, com absorção deficiente e "
          "cicatrizes. Quanto à reutilização, desaconselham-na, mas, "
          "reconhecendo que é prática comum, recomendam não alarmar os "
          "doentes, descartar a agulha quando a injecção se torna mais "
          "dolorosa e nunca a usar mais de cinco vezes {bahendeka2019}. Este "
          "limite de cinco utilizações é adoptado neste estudo como critério "
          "de reutilização excessiva."),
        P("A sequência de passos com seringa, que a actualização FITTER "
          "Forward descreve da conservação à eliminação {klonoff2025}, "
          "inclui a verificação do tipo, do prazo e do aspecto da insulina, "
          "a homogeneização das suspensões turvas {frid2016itq}, a "
          "aspiração da dose prescrita, a escolha de um local sem "
          "lipohipertrofia e a sua rotação {frid2016}, o ângulo e a prega "
          "adequados ao comprimento da agulha e à espessura do tecido "
          "{bahendeka2019} e a colocação do material usado num recipiente "
          "seguro {frid2016}. Na prática, estes passos falham com "
          "frequência. No inquérito internacional, as agulhas de 4 mm e de 8 "
          "mm eram usadas, cada uma, por cerca de 30% dos doentes e a "
          "eliminação do material cortante era claramente insuficiente, "
          "acabando muitas agulhas no lixo comum {frid2016itq}. Em Gondar, "
          "na Etiópia, 80,7% dos doentes tinham práticas de eliminação "
          "inadequadas e 31% deitavam as seringas na rua quando viajavam "
          "{basazn2016}, e em Tlemcen, na Argélia, mais de metade dos "
          "doentes reutilizava a agulha da caneta dez ou mais vezes "
          "{hacene2020}."),
    ]),
    ("Lipohipertrofia e reutilização de agulhas: magnitude, consequências "
     "e factores de risco", [
        P("A lipohipertrofia é a complicação local mais frequente da "
          "insulinoterapia. No inquérito internacional foi referida por "
          "29,0% dos doentes e encontrada ao exame em 30,8% {frid2016lh}. "
          "Uma meta-análise de 45 estudos, com 26.865 participantes, estimou "
          "uma prevalência de 41,8% (intervalo de confiança a 95% (IC95%) "
          "35,9-47,6%) e de 34,8% (IC95% 16,9-52,8%) nos estudos africanos, "
          "e identificou a duração da insulinoterapia como único factor "
          "associado na meta-regressão {wang2021}. O consenso internacional "
          "de 2026 situa a prevalência entre 29% e 76% e estima que a "
          "lipohipertrofia pode exigir doses de insulina até 25% mais "
          "elevadas {guo2026}. Na Etiópia, a lipodistrofia atingiu 53,1% dos "
          "doentes de três hospitais do noroeste {bazezew2026} e 49,2% das "
          "crianças e adolescentes com diabetes tipo 1 de um hospital de "
          "Tigray {alemseged2024}, e na Jordânia 57,0% dos doentes com "
          "diabetes tipo 1 e 55,5% dos doentes com diabetes tipo 2 "
          "apresentavam lipohipertrofia {abujbara2022}."),
        P("As consequências clínicas estão bem documentadas. Num estudo "
          "cruzado com 13 doentes com diabetes tipo 1, a insulina injectada "
          "em tecido lipohipertrófico teve absorção menor e muito mais "
          "variável (coeficiente de variação de 52% contra 11% no tecido "
          "normal) e as glicemias pós-prandiais foram pelo menos 26% mais "
          "elevadas {famulla2016}. Uma meta-análise de 37 estudos mostrou "
          "que os doentes com lipohipertrofia têm maior probabilidade de "
          "hipoglicemia inexplicada (odds ratio (OR) de prevalência 6,98) e de "
          "variabilidade glicémica (5,24), hemoglobina glicada 0,55% mais "
          "elevada e mais 7,68 UI de insulina por dia {mader2024}. Em "
          "crianças etíopes, o mau controlo glicémico foi mais frequente com "
          "lipodistrofia (75%) do que sem ela (47,1%) {alemseged2024}."),
        P("Os factores de risco são sobretudo comportamentais e "
          "modificáveis. Uma meta-análise de 51 estudos identificou a "
          "rotação incorrecta como o factor mais forte (OR de prevalência "
          "8,85; IC95% 5,10-15,33), seguida da reutilização de agulhas "
          "(3,20; IC95% 1,99-5,13), da insulinoterapia há mais de cinco "
          "anos (2,62) e de mais de duas injecções por dia (2,27), sem "
          "associação com o sexo, a idade ou o tipo de dispositivo "
          "{mader2026}. Nos estudos etíopes, a ausência de rotação (OR "
          "ajustado de 1,8 em adultos e de 9,0 em crianças) e a "
          "reutilização de agulhas repetiram-se como factores associados "
          "{bazezew2026,alemseged2024}, e no inquérito internacional a "
          "inspecção regular dos locais pelo profissional associou-se a "
          "menos lipohipertrofia e a melhor rotação {frid2016lh}."),
        P("A reutilização merece uma análise cuidadosa. Uma revisão "
          "sistemática de 25 estudos, todos com elevado risco de viés, não "
          "encontrou associação entre reutilização e infecção no local de "
          "injecção, mas encontrou-a com a lipohipertrofia (diferença de "
          "risco de 0,16; IC95% 0,05-0,28), concluindo que não havia "
          "evidência clara a favor ou contra a prática {zabaleta2016}. Num "
          "ensaio aleatorizado brasileiro com 71 doentes com diabetes tipo "
          "2, a reutilização da seringa até cinco vezes aumentou "
          "modestamente a lipohipertrofia e os nódulos, sem agravar a dor, "
          "o controlo glicémico ou a contaminação microbiológica em 12 "
          "semanas {berlanda2024}. Como a escassez de seringas leva à "
          "reutilização em quase todos os países de baixo e médio "
          "rendimento {who2021}, é mais informativo quantificar o número de "
          "utilizações do que registar apenas se o doente reutiliza."),
    ]),
    ("Estabilidade térmica e conservação da insulina sem frigorífico", [
        P("Segundo as farmacopeias, os frascos por abrir devem ser guardados "
          "no frigorífico, entre 2 e 8 °C, sendo em geral permitida a "
          "conservação à temperatura ambiente (25-30 °C) durante as quatro "
          "semanas de utilização do frasco aberto {kaufmann2021}. As "
          "recomendações variam, contudo, entre 10 e 45 dias de utilização e "
          "entre 25 e 37 °C de temperatura máxima {richter2023}. A OMS "
          "reconhece que, em muitos países com poucos recursos, quem não "
          "tem refrigeração em casa pode ter de se deslocar diariamente à "
          "unidade sanitária para receber as injecções, e inclui a "
          "estabilidade da insulina à temperatura ambiente entre as "
          "prioridades de investigação {who2021}."),
        P("A evidência disponível é, em parte, tranquilizadora. Uma revisão "
          "Cochrane de 17 estudos, maioritariamente laboratoriais, concluiu, "
          "com base nos dados dos fabricantes, que os frascos e cartuchos "
          "por abrir de insulina humana de acção curta e intermédia podem "
          "ser guardados até 25 °C durante um máximo de seis meses e até 37 "
          "°C durante um máximo de dois meses sem perda clinicamente "
          "relevante de potência, e que temperaturas oscilantes entre 25 e "
          "37 °C durante até três meses não reduziram a actividade da "
          "insulina solúvel, intermédia ou bifásica {richter2023}. No campo "
          "de refugiados de Dagahaley, no norte do Quénia, as temperaturas "
          "oscilaram entre 25 e 37 °C, e a insulina submetida a essas "
          "condições em laboratório manteve a estabilidade e a actividade "
          "biológica durante as quatro semanas de utilização "
          "{kaufmann2021}. A mesma revisão sublinha, porém, que faltam "
          "estudos clínicos e dados sobre a esterilidade {richter2023}."),
        P("Na ausência de frigorífico, muitos doentes recorrem a dispositivos "
          "de arrefecimento por evaporação. Treze dispositivos usados no "
          "Sudão, na Etiópia, na Tanzânia, no Mali e noutros países, entre "
          "os quais dez potes de barro, reduziram a temperatura interior "
          "entre 2,7 e 8,3 °C em relação ao ambiente, com melhor desempenho "
          "em ar seco {ogle2016}. O modo de uso é, no entanto, decisivo: em "
          "Mwanza, na Tanzânia, 49% dos doentes guardavam a insulina em "
          "potes de barro, com práticas que incluíam imergir os frascos em "
          "água ou numa mistura de água e areia, e 16% dos frascos assim conservados estavam "
          "contaminados, contra nenhum dos guardados no frigorífico "
          "{kimaro2025}. Por isso, o EADSG recomenda que a insulina em uso "
          "nunca seja imersa em água e que seja transportada sem "
          "agitação, sem exposição a temperaturas superiores a 32 °C e sem "
          "congelação {bahendeka2019}."),
        P("A conservação inadequada tem tradução clínica. Num hospital "
          "etíope, a conservação inadequada associou-se a mau controlo "
          "glicémico (OR ajustado de 2,675), associação que deixou de ser "
          "significativa depois de uma intervenção educativa sobre "
          "conservação e injecção {dagnew2026}. Em Moçambique, onde só 6,5% "
          "dos agregados rurais e 43,0% dos urbanos possuem frigorífico ou "
          "congelador {ine2024}, conhecer os métodos efectivamente usados é "
          "condição prévia para dar conselhos realistas."),
    ]),
    ("Enquadramento normativo moçambicano e papel do farmacêutico na "
     "educação do doente", [
        P("O Plano Estratégico Multissectorial de Prevenção e Controlo de "
          "Doenças Não Transmissíveis 2020-2029, o segundo do país, "
          "estabelece como metas até 2029 conter o aumento da diabetes e "
          "garantir que pelo menos 46,6% das pessoas com hipertensão e "
          "diabetes conheçam a sua condição, e inclui entre os seus "
          "objectivos o reforço da disponibilidade dos medicamentos "
          "essenciais das doenças não transmissíveis e o envolvimento da "
          "comunidade na criação de recursos de educação e apoio aos "
          "doentes e na prevenção de complicações {misau2020}. A Lista "
          "Nacional de Medicamentos Essenciais, aprovada pelo Diploma "
          "Ministerial n.º 52/2023, determina que o Serviço Nacional de "
          "Saúde adquira apenas os medicamentos nela constantes, salvo os "
          "de especialidade, e inclui "
          "quatro insulinas, todas em frasco multidose {misau2023lnme}."),
        P("A capacidade dos serviços para ensinar a técnica é limitada. Os "
          "gestores e profissionais moçambicanos entrevistados sobre a "
          "diabetes e a hipertensão descreveram uma formação orientada para "
          "as doenças infecciosas, a necessidade de formação em serviço, a "
          "falta de equipamento, consumíveis e medicamentos e um "
          "financiamento insuficiente {madede2024}. Nos jovens com diabetes "
          "tipo 1, as barreiras predominaram (67,3% dos temas "
          "identificados), com destaque para as interacções inadequadas com "
          "o pessoal de saúde, as longas esperas e o estigma, e os autores "
          "recomendaram melhorar a formação dos profissionais e a literacia "
          "em saúde dos doentes {mazzalai2025}."),
        P("O farmacêutico está bem colocado para preencher esta lacuna, "
          "porque contacta o doente em cada dispensa. Num ensaio "
          "aleatorizado na Malásia com 160 doentes, a reeducação mensal "
          "sobre a técnica feita por farmacêuticos durante quatro meses "
          "melhorou a técnica e reduziu a hemoglobina glicada mais 0,63% do "
          "que o aconselhamento habitual {selvadurai2021}. Na Índia, a "
          "demonstração individual com almofadas de injecção melhorou passos "
          "como a lavagem das mãos, a verificação do prazo, o rolar do "
          "frasco entre as mãos e a eliminação das bolhas de ar "
          "{kapoor2016}, e na Etiópia uma intervenção educativa elevou a "
          "proporção de doentes com técnica adequada de 48,68% para 72,46% "
          "{dagnew2026}. Uma meta-análise de três ensaios com 637 doentes "
          "com lipohipertrofia sugere que a educação sobre a técnica reduz "
          "ligeiramente a dose diária de insulina, sendo incerto o efeito "
          "na hemoglobina glicada {ichikawa2022}, o que reforça a "
          "necessidade de intervenções bem desenhadas a partir de um "
          "diagnóstico local."),
        P("Numa população com baixa literacia, a forma dos materiais conta "
          "tanto como o conteúdo. Uma revisão de 47 estudos mostrou que as "
          "ajudas visuais desenvolvidas com a participação de pessoas com "
          "baixa literacia melhoraram a literacia em saúde, a compreensão e "
          "a adesão, sendo os pictogramas e os vídeos os mais eficazes "
          "{mbanda2021}. O método de ensino de retorno, em que o doente "
          "explica ou demonstra o que aprendeu, foi eficaz em 19 de 20 "
          "estudos {talevski2020}. Ambos orientarão a proposta de material "
          "educativo que resultar deste estudo."),
    ]),
    ("Métodos de avaliação da técnica e da lipohipertrofia e "
     "propriedades de medida", [
        P("A maior parte dos estudos africanos mediu a técnica por "
          "entrevista, com pontuações construídas pelos autores "
          "{nasir2021,negash2023}; em Dessie, por exemplo, 63,9% dos doentes "
          "foram classificados com boa prática, associada à idade mais jovem "
          "e à insulinoterapia há mais de nove anos {feleke2025}. O auto-relato é barato, mas sobrestima a "
          "prática correcta, porque o doente tende a descrever o que sabe "
          "que deve fazer. Na Etiópia, 70% dos doentes referiram a rotação "
          "dos locais, mas só 60,75% a executaram durante a demonstração "
          "observada com uma lista de verificação de cinco pontos "
          "{netere2020}, e na Índia uma lista de verificação dos passos de "
          "administração permitiu documentar a mudança da técnica antes e "
          "depois da demonstração {kapoor2016}. A observação directa de "
          "toda a sequência, com uma lista de verificação baseada nas "
          "recomendações, é por isso o método preferido, embora sujeito ao "
          "efeito de ser observado, que tende a melhorar o desempenho."),
        P("Quando não existe instrumento validado para o contexto, a lista "
          "de verificação tem de ser adaptada e submetida a validação. A "
          "validade de conteúdo avalia-se por um painel de peritos que "
          "classifica cada item quanto à relevância, calculando-se o índice "
          "de validade de conteúdo por item e para o conjunto da escala "
          "{almanasreh2019}. A tradução e a retroversão, o pré-teste em "
          "doentes semelhantes aos da amostra e a estimativa da fiabilidade "
          "completam o processo {tsang2017}; para itens dicotómicos, a "
          "consistência interna estima-se pelo coeficiente de "
          "Kuder-Richardson (KR-20). Como a classificação de cada passo "
          "depende do julgamento do observador, a concordância entre dois "
          "observadores independentes mede-se pelo kappa de Cohen, cuja "
          "interpretação original, que admitia valores a partir de 0,41, é "
          "considerada demasiado tolerante para estudos de saúde "
          "{mchugh2012}."),
        P("A ecografia é o método de referência para a lipohipertrofia, mas "
          "é demasiado cara para rastreio. Com um procedimento de palpação "
          "estruturado e formação específica, profissionais sem experiência "
          "atingiram 97% de concordância com a ecografia na identificação "
          "das lesões {gentile2016}. Em 395 doentes, a ecografia detectou "
          "lipohipertrofia em 89,6%, a inspecção com palpação estruturada em "
          "78,0% e a palpação comum em 66,6% {xu2025}. O consenso de 2026 "
          "recomenda protocolos padronizados de inspecção e palpação "
          "sistemática, reservando a ecografia para as lesões subclínicas "
          "{guo2026}. A palpação estruturada, feita por observadores "
          "treinados, é assim o método exequível no HCN, com a subestimação "
          "que dela decorre."),
    ]),
]

# ----------------------------------------------------- 7. estado da arte ----
ESTADO_ARTE = [
    P("O [[quadro:estado_arte]] sintetiza 14 estudos empíricos publicados "
      "entre 2016 e 2026 sobre a técnica de injecção, a lipohipertrofia e a "
      "conservação da insulina, com destaque para os africanos e para o "
      "único estudo moçambicano encontrado sobre pessoas com diabetes "
      "insulinotratada."),
    QUADRO("estado_arte",
           "Síntese de estudos sobre a técnica de injecção, a "
           "lipohipertrofia e a conservação da insulina (estado da arte)",
           ["Autor (ano)", "Local", "Desenho (n)", "Principais resultados"],
           [
               ["Frid et al. (2016) {frid2016lh}", "42 países",
                "Transversal, inquérito (13.289)",
                "Lipohipertrofia referida por 29,0% e encontrada ao exame "
                "em 30,8%; com lipohipertrofia, mais 10,1 UI por dia e "
                "hemoglobina glicada 0,55% mais alta; menos de 40% "
                "receberam instrução nos seis meses anteriores."],
               ["Kapoor et al. (2016) {kapoor2016}", "Índia",
                "Quase-experimental (91)",
                "A demonstração individual com almofadas de injecção "
                "melhorou passos como a lavagem das mãos, a verificação do "
                "prazo e a eliminação das bolhas (p<0,05)."],
               ["Netere et al. (2020) {netere2020}", "Etiópia",
                "Transversal, entrevista e demonstração (166)",
                "Conhecimento moderadamente adequado (64,3%) e prática "
                "razoável (55,4%); 70% referiram a rotação e 60,75% "
                "praticaram-na na demonstração."],
               ["Hacene et al. (2020) {hacene2020}", "Argélia",
                "Transversal, questionário internacional (100)",
                "Caneta em 98%, com agulhas de 6 e 8 mm; ressuspensão da "
                "insulina turva desconhecida; mais de metade reutilizava a "
                "agulha dez ou mais vezes."],
               ["Nasir et al. (2021) {nasir2021}", "Etiópia",
                "Transversal (245)",
                "Conhecimento global de 63,4%; 72,2% auto-administravam; "
                "49,0% injectavam com o ângulo adequado e 71,8% repetiam o "
                "mesmo local."],
               ["Selvadurai et al. (2021) {selvadurai2021}", "Malásia",
                "Ensaio aleatorizado (160)",
                "A reeducação mensal pelo farmacêutico durante quatro meses "
                "reduziu a hemoglobina glicada mais 0,63% do que o "
                "controlo e melhorou a técnica."],
               ["Abujbara et al. (2022) {abujbara2022}", "Jordânia",
                "Transversal (851)",
                "Rotação em 66,8% (tipo 1) e 69,4% (tipo 2); agulha usada "
                "mais de três vezes por 36,6% e 50,5%; lipohipertrofia em "
                "57,0% e 55,5%, associada a pior controlo."],
               ["Negash et al. (2023) {negash2023}", "Etiópia",
                "Transversal (319)",
                "Prática razoável em 73,4% (mediana de 38 em 56 pontos); "
                "62,1% só com insulina intermédia; idade, escolaridade e "
                "duração da doença associadas à prática."],
               ["Alemseged et al. (2024) {alemseged2024}", "Etiópia",
                "Transversal (122 crianças e adolescentes)",
                "Lipodistrofia em 49,2%; rotação inadequada (OR ajustado "
                "9,0) e insulinoterapia prolongada (3,6) associadas; mau "
                "controlo em 75% contra 47,1%."],
               ["Berlanda et al. (2024) {berlanda2024}", "Brasil",
                "Ensaio aleatorizado (71)",
                "Reutilizar a seringa até cinco vezes aumentou modestamente "
                "a lipohipertrofia e os nódulos, sem pior controlo, dor ou "
                "contaminação em 12 semanas."],
               ["Kimaro et al. (2025) {kimaro2025}", "Tanzânia",
                "Transversal laboratorial (51 doentes, 81 frascos)",
                "49% guardavam a insulina em potes de barro; 6,2% dos "
                "frascos contaminados, 16% nos potes de barro contra 0% no "
                "frigorífico."],
               ["Mazzalai et al. (2025) {mazzalai2025}", "Moçambique",
                "Qualitativo (26 doentes, 18 cuidadores, 16 profissionais)",
                "Barreiras em 67,3% dos temas: falta de apoio psicológico, "
                "interacções inadequadas, longas esperas e estigma; sem "
                "dados sobre a técnica."],
               ["Dagnew et al. (2026) {dagnew2026}", "Etiópia",
                "Quase-experimental (330)",
                "Técnica adequada passou de 48,68% para 72,46%; "
                "lipohipertrofia em 40,9%; conservação inadequada associada "
                "a mau controlo (OR ajustado 2,675)."],
               ["Bazezew et al. (2026) {bazezew2026}", "Etiópia",
                "Transversal, três hospitais (407)",
                "Lipodistrofia em 53,1%, sobretudo abdominal "
                "(36,5%); ausência de rotação (OR ajustado 1,8) e "
                "reutilização de agulhas associadas."],
           ],
           larguras=[3.3, 2.1, 3.0, 7.6],
           fonte="Elaboração própria (2026), a partir das fontes citadas."),
    P("A leitura do quadro mostra um padrão consistente. Em todos os "
      "contextos, uma parte substancial dos doentes comete erros de técnica, "
      "a lipohipertrofia ou a lipodistrofia atinge entre 40% e 57% dos "
      "doentes nos estudos africanos e jordano {dagnew2026,bazezew2026,"
      "abujbara2022}, e a rotação incorrecta e a reutilização de agulhas "
      "surgem repetidamente associadas às lesões {alemseged2024,"
      "bazezew2026}. Os estudos de intervenção, com demonstração "
      "individual, reeducação pelo farmacêutico ou sessões educativas com "
      "material para levar para casa, melhoraram a técnica em semanas ou "
      "meses {kapoor2016,selvadurai2021,dagnew2026}, o que confirma que o "
      "problema é corrigível."),
    P("As divergências são sobretudo metodológicas. A maioria dos estudos "
      "africanos mediu a prática por auto-relato e classificou-a com "
      "pontuações e pontos de corte próprios, o que explica proporções tão "
      "diferentes como 55,4% e 73,4% de prática razoável em dois estudos "
      "etíopes {netere2020,negash2023}, e poucos observaram a técnica ou "
      "examinaram os locais de injecção. A conservação foi quase sempre "
      "tratada como um conjunto de perguntas secundárias, e só o estudo "
      "tanzaniano relacionou a forma de conservação com a contaminação dos "
      "frascos {kimaro2025}. Em Moçambique, a única investigação encontrada "
      "sobre pessoas com diabetes insulinotratada é qualitativa e trata das "
      "barreiras de acesso de jovens com diabetes tipo 1 {mazzalai2025}. "
      "Falta, portanto, um estudo que observe directamente a técnica, "
      "examine os locais de injecção com um método padronizado e descreva "
      "a conservação em casas sem frigorífico numa população adulta "
      "moçambicana, lacuna que o presente protocolo pretende preencher."),
]
ESQUEMA_TEXTO = [
    P("A [[figura:esquema]] representa as relações que o estudo examina. "
      "As características sociodemográficas, clínicas e terapêuticas, a "
      "formação recebida e as condições do domicílio são tratadas como "
      "variáveis independentes que influenciam três desfechos: a técnica de "
      "auto-administração, a presença de lipohipertrofia e a conservação da "
      "insulina. As práticas de rotação e de reutilização das agulhas, "
      "componentes da técnica, são também as exposições principais da "
      "análise da lipohipertrofia. A duração da insulinoterapia e o número "
      "de injecções diárias, factores de risco conhecidos da lesão "
      "{mader2026,wang2021}, e o modo de observação (injecção real ou "
      "demonstração simulada) são tratados como variáveis de confundimento "
      "ou de controlo nos modelos multivariáveis."),
]
ESQUEMA_TITULO = ("Esquema conceptual dos factores associados à técnica de "
                  "auto-administração, à lipohipertrofia e à conservação da "
                  "insulina")
ESQUEMA = {
    "contexto": ("Adultos com diabetes em insulinoterapia, consulta externa "
                 "do Hospital Central de Nampula, Março a Maio de 2027"),
    "blocos": [
        ("Factores sociodemográficos",
         ["idade e sexo", "escolaridade e capacidade de leitura",
          "residência e tempo de transporte até ao hospital"]),
        ("Factores clínicos e terapêuticos",
         ["tipo de diabetes", "tipo de insulina e dispositivo",
          "comprimento da agulha", "dificuldade visual"]),
        ("Formação recebida",
         ["instrução inicial com demonstração prática",
          "reeducação nos últimos seis meses",
          "inspecção dos locais pelo profissional"]),
        ("Práticas de injecção e condições do domicílio",
         ["rotação dos locais e número de utilizações da agulha",
          "energia eléctrica e frigorífico",
          "métodos alternativos de arrefecimento"]),
    ],
    "desfecho": ("Técnica e conservação da insulina",
                 ["técnica adequada ou inadequada",
                  "lipohipertrofia presente ou ausente",
                  "conservação adequada ou inadequada"]),
    "moderadores": ("Variáveis de confundimento e de controlo",
                    ["duração da insulinoterapia",
                     "número de injecções diárias",
                     "modo de observação (real ou simulada)"]),
}

# ----------------------------------------------------- 8. metodologia -------
METODOLOGIA = [
    ("Tipo e desenho do estudo", [
        P("Trata-se de um estudo observacional, transversal, descritivo e "
          "analítico, de base hospitalar e abordagem quantitativa. Numa única "
          "sessão, cada participante é submetido a três procedimentos "
          "complementares: a observação directa da técnica de "
          "auto-administração com lista de verificação, o exame clínico dos "
          "locais de injecção e uma entrevista estruturada sobre a formação "
          "recebida e a conservação da insulina, completada pela inspecção "
          "do frasco em uso e pela consulta do processo clínico. O desenho "
          "transversal permite estimar proporções e explorar associações num "
          "único momento, o que é adequado a um trabalho de licenciatura com "
          "três meses de recolha, mas não permite estabelecer a sequência "
          "temporal entre exposições e desfechos. O relato seguirá a "
          "declaração STROBE para estudos transversais {vonelm2007}."),
    ]),
    ("Local e período do estudo", [
        P("O estudo realiza-se no HCN, na cidade de Nampula, capital da "
          "província mais populosa do país {ine2021}. O hospital é a unidade "
          "de referência do norte de Moçambique e acompanha, em consulta "
          "externa, adultos com diabetes residentes na cidade e noutros "
          "distritos, a quem a insulina e as seringas são dispensadas pela "
          "farmácia hospitalar. Num clima tropical quente, e numa província "
          "em que a maioria dos agregados não tem frigorífico {ine2024}, a "
          "conservação da insulina entre as consultas é um problema real e "
          "não teórico. A organização da consulta, os dias de atendimento e "
          "o circuito de dispensa da insulina serão confirmados com a "
          "Direcção Clínica e com a farmácia do hospital durante a fase de "
          "autorizações."),
        P("O protocolo decorre de Outubro de 2026 a Setembro de 2027. A "
          "recolha de dados realiza-se de 1 de Março a 31 de Maio de 2027, "
          "depois do parecer favorável do comité de bioética, previsto para "
          "Janeiro de 2027, e do pré-teste, em Fevereiro de 2027. Doze "
          "semanas de recolha abrangem pelo menos duas consultas de cada "
          "doente com renovação mensal ou bimestral da insulina, o que "
          "permite contactar quase todos os elegíveis."),
    ]),
    ("População e unidade de análise", [
        P("A população-alvo são os adultos com diabetes em insulinoterapia "
          "seguidos na consulta externa do HCN, e a população acessível são "
          "os que estão registados como utilizadores de insulina e comparecem "
          "à consulta ou à farmácia durante o período de recolha. A unidade "
          "de análise é o doente. Cada doente é incluído uma única vez: o "
          "código atribuído na primeira participação é anotado numa lista de "
          "controlo, e as visitas seguintes do mesmo doente não dão origem a "
          "nova entrevista. No exame dos locais de injecção registam-se todas "
          "as lesões, mas a variável de análise é a presença de "
          "lipohipertrofia em pelo menos um local; na conservação, a unidade "
          "é o domicílio do doente, descrito pelo próprio."),
    ]),
    ("Amostra e cálculo do tamanho da amostra", [
        P("O número de adultos em insulinoterapia seguidos no HCN (N) não é "
          "conhecido e será obtido antes da recolha, a partir dos registos "
          "da consulta e da farmácia [confirmar junto da consulta e da "
          "farmácia do HCN a existência e o formato do registo nominal de "
          "doentes em insulinoterapia]. Adopta-se a seguinte regra: se N for "
          "igual ou inferior a 300, faz-se um censo de todos os elegíveis que "
          "compareçam durante o período de recolha; se N for superior a 300, "
          "selecciona-se uma amostra aleatória simples a partir da lista "
          "nominal, com números aleatórios gerados por computador, e cada "
          "doente sorteado é convidado na primeira consulta que ocorra no "
          "período. O estudo decorre num único hospital, sem amostragem por "
          "conglomerados, pelo que o efeito de desenho é igual a 1."),
        P("O tamanho mínimo para o objectivo descritivo principal, a "
          "proporção de doentes com técnica adequada, calcula-se pela "
          "fórmula da proporção única {wang2020}:"),
        FORMULA("n<sub>0</sub> = Z<sup>2</sup> × p × (1 - p) / d<sup>2</sup>"
                " = 1,96<sup>2</sup> × 0,5 × 0,5 / 0,05<sup>2</sup> = 384,16"),
        P("Em que Z = 1,96 corresponde a um nível de confiança de 95%, d = "
          "0,05 é a margem de erro admitida e p = 0,5 é a proporção esperada. "
          "O valor de 0,5 justifica-se por dois motivos: é próximo das "
          "proporções observadas em hospitais etíopes, onde 48,68% dos "
          "doentes tinham técnica adequada antes de uma intervenção "
          "{dagnew2026} e 49,0% injectavam com o ângulo correcto "
          "{nasir2021}, e maximiza o tamanho da amostra quando não há dados "
          "locais. Arredonda-se n<sub>0</sub> para 385. Quando N for "
          "conhecido, aplica-se a correcção para população finita e "
          "acrescentam-se 10% para compensar recusas e registos incompletos. "
          "Todos os tamanhos são arredondados para o inteiro imediatamente "
          "superior:"),
        FORMULA("n = n<sub>0</sub> / [1 + (n<sub>0</sub> - 1) / N];      "
                "n<sub>final</sub> = n / 0,90"),
        P("O objectivo 5 exige também poder estatístico. Para a comparação "
          "da prevalência de lipohipertrofia entre doentes com rotação "
          "incorrecta e com rotação correcta, admite-se que cerca de 40% dos "
          "doentes não praticam a rotação, a partir dos 60,75% que a "
          "praticaram na Etiópia {netere2020}, o que dá uma razão k = 1,5 "
          "entre não expostos e expostos. Admite-se uma prevalência de 30% "
          "nos doentes com rotação correcta, próxima dos 34,8% estimados "
          "para África {wang2021}, e de 50% nos doentes com rotação "
          "incorrecta, diferença que corresponde a um OR de 2,33, muito "
          "inferior ao OR de prevalência de 8,85 da meta-análise "
          "{mader2026} e, por isso, conservadora. Com α = 0,05 bilateral "
          "(Z<sub>α/2</sub> = 1,96), poder de 80% (Z<sub>β</sub> = 0,84) e "
          "a fórmula de duas proporções com grupos desiguais {wang2020}:"),
        FORMULA("n<sub>1</sub> = [Z<sub>α/2</sub> × √(p<sub>m</sub> × (1 - p<sub>m</sub>) × (1 + "
                "1/k)) + Z<sub>β</sub> × √(p<sub>1</sub>(1 - p<sub>1</sub>)"
                " + p<sub>2</sub>(1 - p<sub>2</sub>)/k)]<sup>2</sup> / "
                "(p<sub>1</sub> - p<sub>2</sub>)<sup>2</sup>"),
        P("Com p<sub>1</sub> = 0,50, p<sub>2</sub> = 0,30, k = 1,5 e p<sub>m</sub> = "
          "(p<sub>1</sub> + k × p<sub>2</sub>) / (1 + k) = 0,38, obtém-se "
          "n<sub>1</sub> = 76,8, isto é, 77 doentes com rotação incorrecta "
          "e n<sub>2</sub> = k × n<sub>1</sub> = 115,5, isto é, 116 com "
          "rotação correcta, 193 no total, ou 215 com a margem de 10% de não "
          "resposta. Com 193 doentes e uma prevalência de lipohipertrofia "
          "próxima de 35% esperam-se cerca de 68 casos, o que permite até "
          "seis variáveis no modelo multivariável com pelo menos 10 eventos "
          "por variável {peduzzi1996}; para a técnica inadequada, esperada "
          "em cerca de metade dos doentes, o número de eventos é maior. A "
          "amostra final corresponde ao maior dos dois valores, o descritivo "
          "corrigido ou 215, como mostra a [[tabela:cenarios]]."),
        TABELA("cenarios",
               "Tamanho da amostra segundo o número de doentes elegíveis",
               ["N (elegíveis)", "n corrigido para N",
                "n com 10% de não resposta", "Amostra final e método"],
               [["200", "132", "147", "Censo dos elegíveis (poder "
                 "limitado para o objectivo 5)"],
                ["300", "169", "188", "Censo dos elegíveis"],
                ["400", "197", "219", "219, amostra aleatória simples"],
                ["500", "218", "243", "243, amostra aleatória simples"],
                ["800", "261", "290", "290, amostra aleatória simples"],
                ["1.000", "279", "310", "310, amostra aleatória simples"],
                ["1.500", "307", "342", "342, amostra aleatória simples"]],
               larguras=[2.6, 3.2, 3.6, 6.6],
               nota="Com N muito grande, o máximo é 428 (385 / 0,90). Entre "
                    "301 e 386 elegíveis prevalece o mínimo de 215 "
                    "exigido pelo objectivo 5."),
        P("Se N for inferior a 215, o censo mantém-se e a limitação do poder "
          "para o objectivo 5 será declarada, com apresentação dos "
          "intervalos de confiança das estimativas. O pré-teste incluirá 20 "
          "doentes, cerca de 10% do mínimo de 215, recrutados fora do HCN e "
          "excluídos da amostra final, e a dupla observação abrangerá 10% "
          "dos participantes, seleccionados por sorteio dos dias de "
          "recolha."),
    ]),
    ("Critérios de inclusão e de exclusão", [
        H3("Critérios de inclusão"),
        LISTA([
            "Idade igual ou superior a 18 anos.",
            "Diagnóstico de diabetes tipo 1 ou tipo 2 registado no processo "
            "clínico.",
            "Insulinoterapia há pelo menos três meses, com seguimento na "
            "consulta externa do HCN.",
            "Administração da insulina pelo próprio doente, em todas ou na "
            "maioria das doses.",
            "Consentimento informado, escrito ou por impressão digital com "
            "testemunha.",
        ]),
        H3("Critérios de exclusão"),
        LISTA([
            "Insulina habitualmente administrada por familiar ou por "
            "profissional de saúde.",
            "Diabetes gestacional.",
            "Doença aguda, hipoglicemia ou hiperglicemia sintomáticas no dia "
            "da consulta (o doente é convidado para a consulta seguinte).",
            "Incapacidade cognitiva ou física que impeça o consentimento ou "
            "a demonstração da técnica.",
            "Participação no pré-teste.",
        ]),
    ]),
    ("Variáveis e definições operacionais", [
        P("O [[quadro:variaveis]] apresenta as variáveis, o tipo, a "
          "definição operacional com as categorias e o objectivo a que cada "
          "uma responde. Os pontos de corte da pontuação da técnica "
          "(adequada com 80% ou mais dos itens aplicáveis correctos e nenhum "
          "erro crítico) e os critérios de conservação adequada são os "
          "definidos na revisão da literatura e aplicam-se sem alteração na "
          "análise."),
        QUADRO("variaveis", "Variáveis do estudo e definições operacionais",
               ["Variável", "Tipo", "Definição operacional e categorias",
                "Objectivo"],
               [
                ["Idade", "Independente, quantitativa",
                 "Anos completos; grupos 18-39, 40-59 e 60 ou mais", "1, 5"],
                ["Sexo", "Independente, nominal", "Masculino; feminino",
                 "1, 5"],
                ["Escolaridade", "Independente, ordinal",
                 "Nenhuma; primária; secundária; superior", "1, 5"],
                ["Capacidade de leitura", "Independente, nominal",
                 "Lê em voz alta uma frase simples em português ou emakhuwa: "
                 "sim; não", "1, 5"],
                ["Residência e tempo de transporte", "Independente, nominal "
                 "e quantitativa",
                 "Cidade de Nampula; outro distrito; minutos de viagem entre "
                 "a farmácia e a casa", "1, 4"],
                ["Tipo de diabetes", "Independente, nominal",
                 "Tipo 1; tipo 2 (processo clínico)", "1, 5"],
                ["Duração da insulinoterapia", "Independente, quantitativa",
                 "Anos desde o início da insulina; menos de 5; 5 ou mais",
                 "1, 5"],
                ["Esquema de insulina", "Independente, nominal",
                 "Solúvel; NPH; bifásica 30/70; glargina; número de "
                 "injecções por dia (1; 2; 3 ou mais)", "1, 5"],
                ["Dispositivo e agulha", "Independente, nominal",
                 "Seringa com agulha fixa; caneta; comprimento da agulha em "
                 "mm", "1, 2"],
                ["Dificuldade visual", "Independente, nominal",
                 "Refere dificuldade em ler a escala da seringa: sim; não",
                 "1, 5"],
                ["Formação recebida", "Independente, nominal",
                 "Instrução inicial (sim; não; quem ensinou); com "
                 "demonstração prática (sim; não); reeducação nos últimos "
                 "seis meses (sim; não); inspecção dos locais pelo "
                 "profissional nos últimos seis meses (sim; não)", "1, 5"],
                ["Glicemia e hipoglicemia", "Descritiva, quantitativa",
                 "Última glicemia em jejum registada no processo (mg/dL); "
                 "hemoglobina glicada, se existir; episódios de hipoglicemia "
                 "referidos nas últimas quatro semanas", "1"],
                ["Pontuação da técnica", "Dependente, quantitativa",
                 "Itens correctos / itens aplicáveis × 100; boa, 80% ou mais; "
                 "moderada, 60-79%; fraca, menos de 60%. Calculada com todos "
                 "os itens e, para sensibilidade, só com os observados", "2"],
                ["Técnica adequada", "Dependente, nominal",
                 "Adequada: pontuação de 80% ou mais e nenhum erro crítico; "
                 "inadequada: restantes casos", "2, 5"],
                ["Erros específicos", "Dependente, nominal",
                 "Cada item da lista de verificação: correcto; incorrecto; "
                 "não aplicável", "2"],
                ["Rotação dos locais", "Independente, nominal",
                 "Diagrama corporal dos locais usados nos últimos sete dias. "
                 "Correcta: alterna regiões e afasta cada injecção pelo menos "
                 "1 cm da anterior dentro da mesma região; incorrecta",
                 "2, 5"],
                ["Reutilização da agulha", "Independente, ordinal",
                 "Número de injecções com a mesma seringa ou agulha, "
                 "declarado e confrontado com a inspecção da seringa: 1; 2-5; "
                 "mais de 5 (reutilização excessiva)", "2, 5"],
                ["Eliminação do material", "Descritiva, nominal",
                 "Recipiente rígido fechado; lixo doméstico; latrina; "
                 "queima; outro", "2"],
                ["Lipohipertrofia", "Dependente, nominal",
                 "Presente em pelo menos um local; ausente; locais afectados "
                 "e maior diâmetro em cm", "3, 5"],
                ["Condições do domicílio", "Independente, nominal",
                 "Energia eléctrica: sim; não; frigorífico funcional: sim; "
                 "não", "4"],
                ["Local de conservação", "Descritiva, nominal",
                 "Frasco em uso e reservas: frigorífico; pote de barro; "
                 "recipiente com água; lugar fresco da casa; outro", "4"],
                ["Práticas de risco na conservação", "Descritiva, nominal",
                 "Imersão ou contacto com água; exposição ao sol ou a fonte "
                 "de calor; congelação; frasco em uso há mais de 28 dias; "
                 "reserva superior a dois meses fora do frigorífico", "4"],
                ["Aspecto e validade do frasco", "Descritiva, nominal",
                 "Normal; alterado (grumos, cristais ou turvação da insulina "
                 "solúvel); prazo expirado; data de abertura anotada", "4"],
                ["Conservação adequada", "Dependente, nominal",
                 "Adequada: cumpre os cinco critérios de conservação; "
                 "inadequada: falha pelo menos um", "4"],
                ["Modo de observação", "Controlo, nominal",
                 "Injecção real; demonstração simulada", "2, 5"],
               ],
               larguras=[3.4, 2.8, 8.0, 1.8]),
    ]),
    ("Instrumentos de recolha de dados e respectivas fontes", [
        P("Os dados serão registados num formulário único (Apêndice A), com "
          "seis secções: dados sociodemográficos; dados clínicos e "
          "terapêuticos, parte dos quais extraída do processo clínico; "
          "formação recebida; lista de verificação da técnica; exame dos "
          "locais de injecção; e conservação, transporte e inspecção do "
          "frasco. A lista de verificação tem 17 passos para a seringa, dos "
          "quais 15 directamente observados, "
          "e foi adaptada das recomendações FITTER e FITTER Forward "
          "{frid2016,klonoff2025}, das orientações do EADSG para a África "
          "Oriental {bahendeka2019} e das listas usadas na Etiópia e na Índia "
          "{netere2020,kapoor2016}; as perguntas sobre locais, rotação, "
          "reutilização e eliminação inspiram-se no questionário "
          "internacional de técnica de injecção {frid2016itq}. Como nenhum "
          "destes instrumentos foi validado em Moçambique, os itens são "
          "adaptados e não reproduzidos, e o conjunto será validado antes da "
          "recolha."),
        P("Consideram-se erros críticos, que tornam a técnica inadequada "
          "qualquer que seja a pontuação, cinco falhas com consequência "
          "clínica directa: aspirar uma dose diferente da prescrita, não "
          "homogeneizar a insulina turva, injectar numa zona com "
          "lipohipertrofia, não fazer rotação dos locais e usar a mesma "
          "agulha mais de cinco vezes {frid2016,bahendeka2019,mader2026}. "
          "Três destes itens não se estabelecem pela observação de uma única "
          "injecção e têm procedimento próprio: o local escolhido é anotado "
          "com precisão e só é classificado como lipohipertrófico depois do "
          "exame dos locais, feito a seguir; a rotação é apurada pedindo ao "
          "doente que assinale num diagrama corporal os locais usados nos "
          "últimos sete dias e comparando-os com o local escolhido na "
          "observação; e o número de utilizações da mesma agulha, declarado "
          "pelo doente, é corroborado pela inspecção da seringa trazida "
          "(ponta romba ou dobrada, ausência do protector). A pontuação da "
          "técnica é por isso calculada de duas maneiras, com todos os itens "
          "aplicáveis e apenas com os itens directamente observados, sendo a "
          "segunda apresentada como análise de sensibilidade. O "
          "exame dos locais segue o procedimento de palpação estruturada "
          "descrito por Gentile e colaboradores {gentile2016} e as "
          "recomendações do consenso de 2026 {guo2026}: inspecção com luz "
          "tangencial das regiões usadas (abdómen, coxas, braços e nádegas), "
          "palpação com as polpas dos dedos em movimentos circulares e com "
          "prega cutânea, comparação com zonas não injectadas e medição do "
          "maior diâmetro de cada lesão com régua flexível."),
        P("A validade de conteúdo será avaliada por um painel de cinco "
          "peritos (dois farmacêuticos, um médico que acompanhe doentes com "
          "diabetes, um enfermeiro e um docente de metodologia), que "
          "classificam a relevância de cada item numa escala de 1 a 4; "
          "calcula-se o índice de validade de conteúdo por item e para a "
          "escala {almanasreh2019}, exigindo-se pelo menos 0,80 em ambos e "
          "revendo-se os itens abaixo desse valor. A tradução para emakhuwa "
          "será feita por dois tradutores independentes, com retroversão "
          "para português por um terceiro que desconhece a versão original e "
          "reconciliação das discrepâncias {tsang2017}. O pré-teste, em 20 "
          "doentes de uma unidade sanitária da cidade de Nampula com consulta "
          "de doenças crónicas, a indicar pelo Serviço Distrital de Saúde, "
          "Mulher e Acção Social (SDSMAS) da Cidade de Nampula [confirmar "
          "junto do SDSMAS a unidade e o número de doentes em "
          "insulinoterapia], avaliará a compreensão, a duração e a "
          "exequibilidade. A consistência interna da lista de verificação "
          "estima-se pelo KR-20, com um mínimo de 0,70, e a concordância "
          "entre observadores pelo kappa de Cohen, com um mínimo de 0,60 "
          "por item e para a classificação final, valor mais exigente do que "
          "a interpretação original de Cohen {mchugh2012}."),
    ]),
    ("Procedimentos de recolha de dados e controlo de qualidade", [
        P("Participam na recolha o estudante investigador e um observador "
          "assistente, licenciado em Farmácia ou em Enfermagem. Ambos "
          "recebem três dias de formação, com o conteúdo das recomendações, "
          "o preenchimento do formulário, a palpação estruturada em "
          "voluntários sob supervisão clínica e a observação de "
          "demonstrações gravadas para calibração, e só iniciam a recolha "
          "depois de atingirem o kappa mínimo em dez observações conjuntas. "
          "Os doentes sorteados, ou todos os elegíveis no caso do censo, são "
          "convidados na consulta anterior ou por telefone a trazer o frasco "
          "de insulina em uso, a seringa que estão a usar e o saco ou "
          "recipiente em que transportam a insulina."),
        P("No dia da consulta, numa sala reservada, a sessão dura cerca de 40 "
          "minutos e segue uma ordem fixa: consentimento; entrevista sobre "
          "os dados sociodemográficos, clínicos e de formação; observação "
          "da técnica; exame dos locais; entrevista sobre a conservação e "
          "inspecção do frasco; e extracção dos dados do processo. Quando a "
          "dose habitual coincide com a hora da consulta, o que é frequente "
          "nos doentes que vêm em jejum para a glicemia, observa-se a "
          "injecção real com o material do próprio doente; nos restantes "
          "casos, o doente demonstra toda a sequência com a sua seringa numa "
          "almofada de treino, usando o seu frasco para a verificação e a "
          "homogeneização e um frasco de soro fisiológico para a aspiração, "
          "e indica no próprio corpo onde injectaria nesse dia. O modo de "
          "observação é registado. O observador pede ao doente que faça «como "
          "faz em casa», não interrompe nem corrige durante a observação e "
          "só intervém para evitar dano imediato, registando o erro."),
        P("No fim da sessão, cada participante recebe ensino individual "
          "sobre os erros observados, com demonstração e confirmação pelo "
          "método de ensino de retorno {talevski2020}, e os que vieram em "
          "jejum recebem um lanche. O controlo de qualidade inclui a dupla "
          "observação independente em 10% dos participantes, a revisão "
          "diária dos formulários pelo investigador antes de o doente sair, "
          "a dupla digitação de todos os formulários por pessoas diferentes, "
          "a correcção das discrepâncias com o formulário em papel e reuniões "
          "semanais com o orientador para rever os problemas encontrados."),
    ]),
    ("Processamento e análise dos dados", [
        P("Os dados serão digitados duas vezes no EpiData e analisados no "
          "Statistical Package for the Social Sciences (SPSS), versão 26 "
          "ou superior, ou no R. As variáveis categóricas descrevem-se por "
          "frequências e proporções com intervalo de confiança a 95% "
          "calculado pelo método de Wilson, e as quantitativas por média e "
          "desvio-padrão ou mediana e intervalo interquartil, conforme a "
          "distribuição avaliada pelo teste de Shapiro-Wilk. O objectivo 1 "
          "resume-se em tabelas de frequências. Para o objectivo 2 "
          "calculam-se a pontuação da técnica, a proporção de técnica "
          "adequada e a frequência de cada erro, com IC95%; para o objectivo "
          "3, a prevalência de lipohipertrofia, o número de lesões e a sua "
          "distribuição por região; para o objectivo 4, a frequência de cada "
          "local e prática de conservação e a proporção de conservação "
          "adequada, estratificadas pela posse de frigorífico e pela "
          "residência."),
        P("Para o objectivo 5, a associação bivariável avalia-se pelo teste "
          "do qui-quadrado de Pearson, ou pelo teste exacto de Fisher quando "
          "alguma frequência esperada for inferior a 5, com OR bruto e "
          "IC95%. Seguem-se dois modelos de regressão logística "
          "multivariável. No primeiro, a variável dependente é a técnica "
          "inadequada e as independentes são as da hipótese (a), ajustadas "
          "para a idade e o modo de observação; no segundo, a variável "
          "dependente é a lipohipertrofia e as exposições são a rotação "
          "incorrecta e a reutilização excessiva, ajustadas para a duração "
          "da insulinoterapia, o número de injecções diárias e o tipo de "
          "diabetes. Cada modelo terá no máximo seis variáveis "
          "{peduzzi1996}; apresentam-se OR ajustados com IC95%, a "
          "qualidade do ajustamento pelo teste de Hosmer-Lemeshow e a "
          "colinearidade pela inspecção das correlações entre as variáveis "
          "independentes. Considera-se significativo p<0,05."),
        P("Em duas análises de sensibilidade, os resultados dos objectivos 2 "
          "e 5 repetem-se apenas com as observações de injecção real e, "
          "depois, com a pontuação calculada só a partir dos 15 itens "
          "directamente observados, isto é, sem o item da rotação e o do "
          "local sem lesão. Os dados em "
          "falta são descritos por variável e a análise usa os casos "
          "completos; uma variável com mais de 10% de valores em falta é "
          "analisada apenas descritivamente. Os valores do kappa por item e "
          "do KR-20 são apresentados junto dos resultados."),
    ]),
    ("Limitações do estudo e estratégias de mitigação", [
        P("O [[quadro:limitacoes]] identifica as principais limitações "
          "previstas, a sua consequência provável nos resultados e as "
          "estratégias de mitigação adoptadas."),
        QUADRO("limitacoes", "Limitações previstas e estratégias de "
                             "mitigação",
               ["Limitação", "Consequência", "Mitigação"],
               [
                ["Efeito de ser observado", "Sobrestimação da técnica "
                 "adequada", "Pedido neutro para fazer «como em casa»; "
                 "observação sem interrupções; ensino só no fim"],
                ["Demonstração simulada em parte dos doentes",
                 "Diferenças face à injecção real", "Registo do modo de "
                 "observação, ajustamento no modelo e análise de "
                 "sensibilidade"],
                ["Conservação e reutilização referidas pelo doente",
                 "Viés de memória e de desejabilidade social",
                 "Perguntas neutras e concretas; inspecção do frasco, da "
                 "data de abertura e do recipiente de transporte"],
                ["Sem medição da temperatura nos domicílios",
                 "Impossibilidade de quantificar a exposição térmica",
                 "Critérios de conservação baseados nas recomendações; "
                 "proposta de estudo futuro com registadores"],
                ["Lipohipertrofia só por palpação, sem ecografia",
                 "Subestimação das lesões subclínicas", "Palpação "
                 "estruturada, formação com calibração e dupla observação "
                 "com kappa"],
                ["Número de elegíveis desconhecido", "Incerteza sobre o "
                 "tamanho final e o poder", "Regra de censo ou amostra e "
                 "tabela de cenários; declaração do poder obtido"],
                ["Hospital único de referência",
                 "Generalização limitada aos cuidados primários",
                 "Descrição detalhada da amostra e da residência; "
                 "recomendação de estudos em outras unidades"],
                ["Desenho transversal", "Sem inferência causal",
                 "Linguagem de associação; ajustamento para confundidores "
                 "conhecidos"],
                ["Baixa literacia e diversidade linguística",
                 "Erros de compreensão nas entrevistas", "Versão em "
                 "emakhuwa com retroversão; entrevistadores treinados; "
                 "pré-teste"],
                ["Exclusão de quem não injecta a si próprio",
                 "Os erros de cuidadores ficam por conhecer",
                 "Registo do número de excluídos por este motivo; "
                 "recomendação de estudo com cuidadores"],
                ["Dependência de o doente trazer o frasco e a seringa",
                 "A inspecção do material e a confirmação da reutilização "
                 "podem faltar em parte dos participantes",
                 "Convite na consulta anterior e lembrete telefónico; "
                 "registo de quem não traz o material e comparação do perfil "
                 "destes doentes com o dos restantes"],
                ["Recusa do exame dos locais por parte de alguns "
                 "participantes", "Perda selectiva de dados no objectivo 3",
                 "Consentimento modular com registo da recusa; comparação "
                 "das características de quem recusa e de quem aceita"],
               ],
               larguras=[4.8, 4.6, 6.6]),
    ]),
    ("Considerações éticas", [
        P("O estudo respeita a Declaração de Helsínquia, na revisão de 2024 "
          "{wma2025}, e a Lei n.º 3/2023, de 8 de Junho, que regula a "
          "investigação em saúde humana em Moçambique {lei3de2023}. O "
          "protocolo será submetido ao Comité Institucional de Bioética para "
          "a Saúde da Universidade Lúrio (CIBS-UniLúrio), e a recolha só "
          "começará depois do parecer favorável e das autorizações da "
          "Direcção Provincial de Saúde de Nampula, da Direcção-Geral do HCN "
          "(Apêndice D) e do SDSMAS da Cidade de Nampula, para o pré-teste."),
        P("A participação é voluntária e depende de consentimento informado "
          "escrito, obtido depois da leitura da folha de informação "
          "(Apêndice B) em português ou em emakhuwa. Quem não sabe ler "
          "consente por impressão digital, na presença de uma testemunha "
          "escolhida pelo participante e alheia à equipa (Apêndice C). A "
          "recusa ou a desistência não altera os cuidados prestados. Os "
          "formulários identificam-se apenas por código; a lista que liga "
          "nomes e códigos, necessária para evitar inclusões repetidas, fica "
          "guardada à parte, em armário fechado, e é destruída no fim da "
          "recolha. A base de dados não contém nomes e os resultados são "
          "apresentados de forma agregada."),
        P("Os riscos são mínimos e resumem-se ao tempo dispendido, ao "
          "desconforto da palpação e à exposição de zonas do corpo, "
          "minimizados pela sala reservada e pela possibilidade de o exame "
          "ser feito por pessoa do mesmo sexo ou na presença de "
          "acompanhante. O consentimento é modular: o participante pode "
          "recusar apenas o exame dos locais de injecção e manter-se no "
          "estudo, ficando essa recusa registada no formulário. O estudo "
          "nunca pede ao doente que atrase ou altere "
          "a sua dose, e quem vem em jejum recebe um lanche no fim. O "
          "benefício directo é o ensino individual da técnica. Por dever de "
          "cuidado, o observador interrompe a observação quando um erro pode "
          "causar dano imediato, como uma dose errada ou o uso de insulina "
          "alterada. Os doentes com lipohipertrofia, frascos alterados ou "
          "fora de prazo, doses diferentes da prescrição ou sinais de "
          "hipoglicemia ou de infecção no local de injecção são "
          "encaminhados, com o seu acordo e no mesmo dia, para o clínico da "
          "consulta e, quando for caso disso, para a farmácia, para "
          "substituição do frasco segundo as normas do hospital. A "
          "devolução dos resultados às equipas é agregada e não punitiva."),
    ]),
]

# ----------------------------------------------------- 9 e 10 ---------------
RESULTADOS_ESPERADOS = [
    P("Os resultados esperados correspondem, pela mesma ordem, aos "
      "objectivos específicos. A direcção indicada apoia-se na literatura "
      "citada e não antecipa valores."),
    LISTA([
        "Objectivo 1: espera-se uma população sobretudo com diabetes tipo 2, "
        "tratada com insulina NPH ou bifásica em frasco e seringa, e uma "
        "minoria reeducada nos últimos seis meses, como no inquérito "
        "internacional {frid2016lh}. Esta caracterização indica a quem se "
        "devem dirigir primeiro os materiais educativos.",
        "Objectivo 2: espera-se que a proporção de técnica adequada se situe "
        "próxima ou abaixo de metade, como na Etiópia {dagnew2026}, com "
        "erros frequentes na homogeneização, na rotação e na reutilização. "
        "A frequência de cada erro define os conteúdos prioritários do "
        "material educativo e da reeducação na farmácia.",
        "Objectivo 3: espera-se uma prevalência de lipohipertrofia entre os "
        "valores estimados para África e os observados em hospitais "
        "etíopes {wang2021,dagnew2026}. O resultado fundamenta a inclusão "
        "da inspecção periódica dos locais na consulta {guo2026}.",
        "Objectivo 4: espera-se que a maioria dos doentes não tenha "
        "frigorífico {ine2024} e use potes de barro, recipientes com água ou "
        "outros locais da casa, e que a imersão dos frascos seja comum "
        "{kimaro2025}. Os resultados permitem formular conselhos de "
        "conservação sem frigorífico coerentes com as recomendações "
        "regionais {bahendeka2019}.",
        "Objectivo 5: espera-se associação entre a rotação incorrecta, a "
        "reutilização excessiva e a lipohipertrofia {mader2026}, e entre a "
        "formação com demonstração e a técnica adequada. Estas associações "
        "indicam os comportamentos que a intervenção educativa deve "
        "mudar e sustentam o pedido de mais seringas por doente.",
    ]),
]
DIVULGACAO = [
    P("Os resultados serão apresentados em defesa pública na Faculdade de "
      "Ciências de Saúde da Universidade Lúrio e num relatório à "
      "Direcção-Geral do HCN, à Direcção Provincial de Saúde de Nampula e ao "
      "Departamento de Doenças Não Transmissíveis do Ministério da Saúde. "
      "Será preparado um artigo para uma revista com revisão por pares, de "
      "preferência de acesso aberto, e um resumo para as jornadas "
      "científicas da Universidade Lúrio e para as jornadas nacionais de "
      "saúde."),
    P("A devolução à comunidade assistencial faz-se numa sessão com as "
      "equipas da consulta e da farmácia do HCN, na qual se apresenta a "
      "proposta de material educativo: um folheto e um cartaz com "
      "pictogramas sobre a preparação da dose, a rotação dos locais, o "
      "número máximo de utilizações da agulha e a conservação sem "
      "frigorífico, em português e em emakhuwa, desenhados a partir dos "
      "erros mais frequentes e destinados a validação com doentes num "
      "estudo posterior {mbanda2021}."),
]

# ----------------------------------------------------- 11. cronograma -------
CRONOGRAMA_TEXTO = [
    P("O [[quadro:cronograma]] distribui as actividades pelos 12 meses do "
      "protocolo, de Outubro de 2026 a Setembro de 2027. A recolha, de "
      "Março a Maio de 2027, só começa depois do parecer favorável do "
      "CIBS-UniLúrio e das autorizações institucionais, e o pré-teste "
      "decorre em Fevereiro de 2027, já com o parecer ético."),
]
CRONOGRAMA = {
    "inicio": (2026, 10),
    "n_meses": 12,
    "actividades": [
        ("Revisão da literatura e redacção do protocolo", [1, 2]),
        ("Submissão ao CIBS-UniLúrio e pedidos de autorização", [2, 3, 4]),
        ("Validação de conteúdo, tradução e formação dos observadores",
         [3, 4]),
        ("Pré-teste e ajuste dos instrumentos", [5]),
        ("Recolha de dados no HCN", [6, 7, 8]),
        ("Dupla digitação, limpeza e análise dos dados", [7, 8, 9]),
        ("Redacção do relatório e proposta de material educativo", [9, 10]),
        ("Revisão pelo orientador e entrega", [10, 11]),
        ("Defesa pública e devolução dos resultados", [12]),
    ],
}

# ----------------------------------------------------- 12. orcamento --------
ORCAMENTO_TEXTO = [
    P("A [[tabela:orcamento]] apresenta o orçamento, calculado para o "
      "cenário mais exigente da [[tabela:cenarios]], de 342 participantes e "
      "20 doentes do pré-teste; se o número "
      "de elegíveis exigir uma amostra maior, a diferença de impressão é "
      "coberta pela margem de imprevistos. O estudo será financiado pelo "
      "estudante, com pedido de apoio à Universidade Lúrio. As rubricas "
      "maiores são o subsídio do observador assistente, indispensável à "
      "dupla observação e ao fluxo de doentes nos dias de consulta, a "
      "impressão dos formulários e dos termos de consentimento e o lanche "
      "dos participantes que vêm em jejum, medida de segurança e não "
      "incentivo. A eventual taxa de apreciação ética, cujo valor não se "
      "fixa neste protocolo, será coberta pelos imprevistos."),
]
ORCAMENTO = [
    ("Impressão dos formulários de recolha (8 páginas por doente)",
     "página", 2896, 5),
    ("Impressão das folhas de informação e dos termos de consentimento "
     "(4 páginas por doente, termo em duplicado)", "página", 1448, 5),
    ("Impressão e encadernação do protocolo e do relatório final",
     "exemplar", 6, 1500),
    ("Almofadas de treino para injecção subcutânea", "unidade", 2, 2500),
    ("Seringas de insulina de 1 mL (100 UI/mL) para demonstração",
     "unidade", 400, 15),
    ("Soro fisiológico a 0,9% em frasco, para demonstração", "frasco", 30,
     60),
    ("Contentores para material cortante", "unidade", 10, 250),
    ("Luvas de exame (caixa de 100)", "caixa", 5, 450),
    ("Réguas flexíveis e marcadores dermográficos", "conjunto", 2, 300),
    ("Lanche para participantes em jejum", "unidade", 362, 40),
    ("Subsídio do observador assistente", "dia", 40, 500),
    ("Formação dos observadores (materiais e lanche)", "dia", 3, 1000),
    ("Tradução e retroversão para emakhuwa", "tradutor", 3, 2000),
    ("Transporte do investigador (recolha e pré-teste)", "dia", 70, 100),
    ("Comunicações para convite dos doentes", "mês", 6, 500),
    ("Material de escritório (canetas, pastas, pranchetas)", "conjunto", 1,
     2000),
    ("Desenho gráfico dos pictogramas do material educativo", "serviço", 1,
     5000),
    ("Impressão a cores do protótipo do folheto e do cartaz", "exemplar",
     100, 60),
]
ORCAMENTO_IMPREVISTOS = 0.10

# ----------------------------------------------------- apendices ------------
_OPC_LOCAL = ["Frigorífico, na prateleira",
              "Frigorífico, no congelador ou encostado a ele",
              "Pote de barro, sem água a tocar no frasco",
              "Recipiente com água ou areia molhada",
              "Lugar fresco da casa, sem água", "Outro: __________"]

APENDICES = [
    ("Formulário de recolha de dados: entrevista, lista de verificação da "
     "técnica e exame dos locais de injecção", [
        NOTA("Instrumento adaptado das recomendações FITTER e FITTER Forward, "
             "das orientações do EADSG, das listas de verificação usadas na "
             "Etiópia e na Índia e do questionário internacional de técnica "
             "de injecção (secção 8.7). Aplicar numa sala reservada, pela "
             "ordem das secções, em português ou na versão em emakhuwa "
             "resultante da tradução e retroversão. Não escrever o nome do "
             "participante neste formulário."),
        CAMPO("Código do participante: ________   Data: ___/___/2027   "
              "Observador: ________   Dupla observação: (   ) sim   (   ) não"),
        H3("Secção I. Dados sociodemográficos"),
        PERG("Idade em anos completos:"),
        PERG("Sexo:", ["Masculino", "Feminino"]),
        PERG("Nível de escolaridade mais alto frequentado:",
             ["Nenhum", "Primário", "Secundário", "Superior"]),
        PERG("Leitura do cartão «A insulina deve ser guardada num lugar "
             "fresco», em português ou em emakhuwa:",
             ["Lê a frase completa", "Lê parte da frase", "Não lê"]),
        PERG("Residência:", ["Cidade de Nampula",
                             "Outro distrito. Qual? __________"]),
        PERG("Tempo de viagem entre a farmácia do hospital e a casa, em "
             "minutos:"),
        H3("Secção II. Dados clínicos e terapêuticos"),
        NOTA("As perguntas 7 a 12 são preenchidas a partir do processo "
             "clínico e confirmadas com o participante."),
        PERG("Tipo de diabetes registado:", ["Tipo 1", "Tipo 2",
                                             "Não registado"]),
        PERG("Ano de início da insulina:"),
        PERG("Insulina prescrita e dose de cada uma (UI):",
             ["Solúvel ____ UI", "NPH ____ UI", "Bifásica 30/70 ____ UI",
              "Glargina ____ UI"],
             instrucao="Assinalar todas as que se aplicam."),
        PERG("Número de injecções por dia:", ["1", "2", "3 ou mais"]),
        PERG("Última glicemia em jejum registada (mg/dL) e data:"),
        PERG("Hemoglobina glicada dos últimos seis meses (%), se existir:"),
        PERG("Dispositivo utilizado:",
             ["Seringa de 1 mL com agulha fixa", "Seringa de 0,5 mL ou 0,3 "
              "mL", "Caneta"]),
        PERG("Comprimento da agulha em mm, lido na embalagem:"),
        PERG("Tem dificuldade em ver os números da seringa?",
             ["Sim", "Não"]),
        PERG("Nas últimas quatro semanas, quantas vezes teve tremores, "
             "suores ou fraqueza que passaram depois de comer ou beber algo "
             "doce?", ["Nenhuma", "1 ou 2", "3 ou mais"]),
        H3("Secção III. Formação recebida"),
        PERG("Quando começou a insulina, alguém lhe ensinou a injectar?",
             ["Sim", "Não"]),
        PERG("Quem ensinou?", ["Médico", "Enfermeiro", "Farmacêutico ou "
                               "técnico de farmácia", "Familiar ou outro "
                               "doente", "Outro"]),
        PERG("O ensino incluiu uma demonstração prática, com o doente a "
             "injectar diante do profissional?", ["Sim", "Não"]),
        PERG("Nos últimos seis meses, algum profissional voltou a rever "
             "consigo a forma de injectar?", ["Sim", "Não"]),
        PERG("Nos últimos seis meses, algum profissional observou ou palpou "
             "os locais onde injecta?", ["Sim", "Não"]),
        PERG("Recebeu algum folheto ou cartaz com imagens sobre a insulina?",
             ["Sim", "Não"]),
        H3("Secção IV. Lista de verificação da técnica (observação directa)"),
        NOTA("Modo de observação: (   ) injecção real   (   ) demonstração "
             "simulada em almofada de treino. Dizer ao participante: «Faça "
             "como faz em casa.» Não interromper nem corrigir, salvo risco de "
             "dano imediato. Marcar S (correcto), N (incorrecto) ou NA (não "
             "aplicável). Os itens assinalados como críticos tornam a técnica "
             "inadequada. Nos utilizadores de caneta, os itens 5, 6, 8 e 9 "
             "são substituídos por: colocar agulha nova, fazer o teste de "
             "segurança segundo o folheto, marcar a dose no selector e "
             "verificar a dose no visor. Os itens 11 e 16 ficam em branco "
             "durante a observação e só são classificados depois do diagrama "
             "corporal e do exame da secção V."),
        TABELA(None, "Lista de verificação",
               ["N.º", "Passo observado", "Critério de correcção", "S", "N",
                "NA"],
               [
                ["1", "Higiene das mãos", "Lava com água e sabão ou "
                 "desinfecta as mãos antes de tocar no frasco", "", "", ""],
                ["2", "Verificação do frasco", "Confirma o tipo de insulina "
                 "e o prazo de validade no rótulo", "", "", ""],
                ["3", "Aspecto da insulina", "Não usa frasco com grumos, "
                 "cristais ou insulina solúvel turva", "", "", ""],
                ["4", "Homogeneização (crítico)", "Rola o frasco entre as "
                 "palmas e inverte-o suavemente até ficar uniformemente "
                 "leitoso, sem agitar com força; NA se só usa insulina "
                 "transparente", "", "", ""],
                ["5", "Limpeza da tampa", "Passa algodão com álcool na "
                 "tampa de borracha antes de a perfurar", "", "", ""],
                ["6", "Introdução de ar", "Aspira ar em volume igual à dose "
                 "e injecta-o no frasco", "", "", ""],
                ["7", "Dose aspirada (crítico)", "A dose na escala é igual à "
                 "prescrita, conferida pelo observador", "", "", ""],
                ["8", "Bolhas de ar", "Elimina as bolhas antes de retirar a "
                 "agulha do frasco", "", "", ""],
                ["9", "Mistura de duas insulinas", "Aspira a insulina "
                 "transparente antes da turva; NA se não mistura", "", "",
                 ""],
                ["10", "Região de injecção", "Escolhe abdómen, coxa, braço "
                 "ou nádega", "", "", ""],
                ["11", "Local sem lesão (crítico)", "Não injecta em "
                 "lipohipertrofia, cicatriz ou inflamação (ver secção V)",
                 "", "", ""],
                ["12", "Prega cutânea", "Faz a prega quando a agulha tem "
                 "mais de 4 mm ou o doente é magro e mantém-na até retirar "
                 "a agulha", "", "", ""],
                ["13", "Ângulo de inserção", "Ângulo adequado à agulha e à "
                 "espessura do tecido, sem inclinação excessiva", "", "",
                 ""],
                ["14", "Injecção e permanência", "Empurra o êmbolo até ao fim "
                 "e mantém a agulha alguns segundos antes de a retirar", "",
                 "", ""],
                ["15", "Depois da injecção", "Não esfrega nem massaja o "
                 "local", "", "", ""],
                ["16", "Rotação dos locais (crítico)", "Alterna regiões e "
                 "afasta cada injecção pelo menos 1 cm (um dedo) da "
                 "anterior", "", "", ""],
                ["17", "Eliminação", "Coloca a seringa usada num recipiente "
                 "rígido com tampa", "", "", ""],
               ],
               larguras=[1.0, 3.8, 8.6, 0.9, 0.9, 0.9]),
        CAMPO("Local exacto usado nesta observação (região e ponto): "
              "______________________"),
        PERG("Diagrama corporal: assinalar com o participante todos os locais "
             "em que injectou nos últimos sete dias, por ordem, e contar "
             "quantas regiões diferentes foram usadas:",
             ["Uma região", "Duas regiões", "Três ou mais regiões"],
             instrucao="Usar a figura do corpo impressa no verso. O item 16 "
                       "é correcto quando o participante alterna regiões e "
                       "nenhum ponto assinalado coincide com o anterior a "
                       "menos de 1 cm."),
        PERG("Quantas injecções faz com a mesma seringa ou agulha antes de a "
             "deitar fora?", ["1 (usa sempre nova)", "2 a 5",
                              "Mais de 5 (crítico)"]),
        PERG("Inspecção da seringa ou agulha trazida pelo participante:",
             ["Agulha nova, com protector", "Ponta romba ou dobrada",
              "Sem protector", "Graduação ilegível ou apagada",
              "Não trouxe a seringa"],
             instrucao="Assinalar todas as que se aplicam; registar a "
                       "discrepância se o aspecto contrariar a resposta "
                       "anterior."),
        PERG("Onde deita as seringas usadas?",
             ["Recipiente rígido com tampa", "Lixo doméstico", "Latrina",
              "Queima", "Entrega na unidade sanitária", "Outro"]),
        CAMPO("Itens correctos ____ / itens aplicáveis ____ = ____%   "
              "Erros críticos: ____   Técnica: (   ) adequada   (   ) "
              "inadequada"),
        CAMPO("Só itens directamente observados (excluir 11 e 16): correctos "
              "____ / aplicáveis ____ = ____%"),
        H3("Secção V. Exame dos locais de injecção"),
        NOTA("Exame realizado: (   ) sim   (   ) recusado pelo participante. "
             "Examinador do mesmo sexo ou na presença de acompanhante. "
             "Inspecção com luz tangencial e palpação estruturada com as "
             "polpas dos dedos, em movimentos circulares e com prega "
             "cutânea, comparando com zonas não injectadas. Medir o maior "
             "diâmetro de cada lesão com régua flexível."),
        TABELA(None, "Exame dos locais",
               ["Região", "Usada para injectar (S/N)",
                "Lipohipertrofia (S/N)", "N.º de lesões",
                "Maior diâmetro (cm)"],
               [["Abdómen", "", "", "", ""],
                ["Coxa direita", "", "", "", ""],
                ["Coxa esquerda", "", "", "", ""],
                ["Braço direito", "", "", "", ""],
                ["Braço esquerdo", "", "", "", ""],
                ["Nádegas", "", "", "", ""]],
               larguras=[3.4, 3.4, 3.4, 2.6, 3.2]),
        CAMPO("Outras alterações (equimose, nódulo doloroso, sinais de "
              "infecção, lipoatrofia): ______________________________"),
        CAMPO("Lipohipertrofia em pelo menos um local: (   ) sim   (   ) não"),
        H3("Secção VI. Conservação, transporte e inspecção do frasco"),
        PERG("Tem energia eléctrica em casa?", ["Sim", "Não"]),
        PERG("Tem frigorífico (geleira) a funcionar em casa?", ["Sim", "Não"]),
        PERG("Onde guarda os frascos ainda fechados?", _OPC_LOCAL +
             ["Não tem frascos de reserva"]),
        PERG("Onde guarda o frasco que está a usar?", _OPC_LOCAL),
        PERG("O frasco fica alguma vez dentro de água ou em contacto com água "
             "ou areia molhada?", ["Sim", "Não"]),
        PERG("O frasco fica alguma vez ao sol, perto do fogão ou noutro "
             "lugar quente?", ["Sim", "Não"]),
        PERG("A insulina alguma vez ficou congelada?",
             ["Sim", "Não", "Não sabe"]),
        PERG("Quantos frascos recebe em cada dispensa e para quantos meses?"),
        PERG("Durante quantos dias usa um frasco depois de o abrir?",
             ["Até 28 dias", "Mais de 28 dias", "Não sabe"]),
        PERG("Como transporta a insulina da farmácia para casa?",
             ["Saco comum", "Recipiente com gelo ou garrafa fria",
              "No bolso ou na mão", "Outro"]),
        PERG("Inspecção do frasco trazido pelo participante:",
             ["Aspecto normal", "Grumos ou cristais", "Insulina solúvel "
              "turva", "Prazo expirado", "Data de abertura anotada",
              "Não trouxe o frasco"],
             instrucao="Assinalar todas as que se aplicam."),
        CAMPO("Critérios cumpridos: nunca congelada (   ); sem contacto com "
              "água (   ); protegida do sol e do calor (   ); frasco aberto "
              "usado até 28 dias (   ); reserva para mais de dois meses no "
              "frigorífico ou inexistente (   ).   Conservação: (   ) "
              "adequada   (   ) inadequada"),
        NOTA("Encaminhamento: (   ) não necessário   (   ) clínico da consulta "
             "(   ) farmácia. Motivo: ______________. Ensino individual com "
             "ensino de retorno realizado: (   ) sim."),
    ]),
    ("Folha de informação ao participante", [
        P("Título do estudo: «Técnica de auto-administração e conservação "
          "domiciliária da insulina em adultos com diabetes seguidos no "
          "Hospital Central de Nampula, 2027». Investigador: estudante do "
          "curso de licenciatura em Farmácia da Faculdade de Ciências de "
          "Saúde da Universidade Lúrio, sob orientação de um docente da "
          "Faculdade."),
        P("Estamos a convidá-lo(a) a participar num estudo sobre a forma como "
          "as pessoas com diabetes injectam e guardam a insulina em casa. O "
          "objectivo é conhecer as dificuldades mais frequentes para preparar "
          "materiais de ensino que ajudem os doentes a usar melhor a "
          "insulina. Antes de decidir, leia ou peça que lhe leiam esta folha "
          "e faça as perguntas que quiser."),
        P("Se aceitar, numa sala reservada do hospital, responderá a "
          "perguntas sobre si, sobre a sua diabetes e sobre a forma como "
          "guarda a insulina; mostrará como prepara e injecta a insulina, "
          "com a sua própria seringa, na injecção que já teria de fazer ou "
          "numa almofada de treino; e deixará que o examinador observe e "
          "apalpe os locais onde injecta. Consultaremos também o seu processo "
          "clínico. Tudo demora cerca de 40 minutos. Não lhe pediremos que "
          "atrase nem altere a sua dose."),
        P("Os riscos são pequenos: o tempo gasto e algum desconforto ou "
          "embaraço no exame, que é feito em privado, por pessoa do mesmo "
          "sexo ou com um acompanhante, se preferir. Pode recusar apenas o "
          "exame dos locais de injecção e continuar no resto do estudo. No "
          "fim, receberá "
          "ensino individual sobre a técnica. Se encontrarmos algum problema, "
          "como alterações nos locais de injecção ou um frasco estragado, "
          "com o seu acordo informaremos o seu médico ou a farmácia no mesmo "
          "dia. Se vier em jejum, receberá um lanche. Não há pagamento pela "
          "participação."),
        P("A participação é voluntária. Pode recusar ou desistir a qualquer "
          "momento, sem dar explicações e sem qualquer prejuízo no seu "
          "tratamento. O seu nome não aparece nos formulários nem na base "
          "de dados, que usam apenas um código, e os resultados são "
          "apresentados em conjunto, sem identificar ninguém. O estudo foi "
          "aprovado pelo Comité Institucional de Bioética para a Saúde da "
          "Universidade Lúrio."),
        P("Contactos: investigador, telefone [preencher]; Comité "
          "Institucional de Bioética para a Saúde da Universidade Lúrio, "
          "telefone [preencher]."),
    ]),
    ("Termo de consentimento livre e esclarecido", [
        P("Declaro que me foi lida, ou que li, a folha de informação sobre o "
          "estudo «Técnica de auto-administração e conservação domiciliária "
          "da insulina em adultos com diabetes seguidos no Hospital Central "
          "de Nampula, 2027», na língua que escolhi, que compreendi o "
          "objectivo, os procedimentos, os riscos e os benefícios, que pude "
          "fazer perguntas e que obtive respostas satisfatórias. Sei que a "
          "participação é voluntária, que posso desistir a qualquer momento "
          "sem prejuízo do meu tratamento e que os meus dados serão tratados "
          "de forma confidencial. Aceito participar, autorizo que me observem "
          "a preparar e a administrar a insulina, autorizo a inspecção e a "
          "palpação dos locais onde injecto, que posso recusar sem deixar de "
          "participar no resto do estudo, e autorizo a consulta do "
          "meu processo clínico para os fins do estudo."),
        CAMPO("Código do participante: ______________"),
        CAMPO("Assinatura do participante: ________________________   Data: "
              "___/___/2027"),
        CAMPO("Impressão digital do participante (se não souber assinar):"),
        CAMPO("[                                ]"),
        CAMPO("Testemunha (para participante que não sabe ler), nome: "
              "________________________"),
        CAMPO("Assinatura da testemunha: ________________________   Data: "
              "___/___/2027"),
        CAMPO("Declaro que expliquei o estudo ao participante e respondi às "
              "suas perguntas. Assinatura do investigador: "
              "____________________   Data: ___/___/2027"),
        NOTA("Este termo é feito em duplicado: um exemplar fica com o "
             "participante e o outro com o investigador, guardado "
             "separadamente dos formulários de recolha."),
    ]),
    ("Pedido de autorização institucional", [
        CAMPO("Exmo(a). Senhor(a) Director(a)-Geral do Hospital Central de "
              "Nampula"),
        CAMPO("Nampula, ___ de ____________ de 2026"),
        CAMPO("Assunto: pedido de autorização para a realização de estudo "
              "de investigação"),
        P("Eu, [Nome do(a) estudante], estudante do curso de licenciatura em "
          "Farmácia da Faculdade de Ciências de Saúde da Universidade Lúrio, "
          "venho solicitar a V. Ex.ª autorização para realizar, na consulta "
          "externa e na farmácia do Hospital Central de Nampula, entre 1 de "
          "Março e 31 de Maio de 2027, o estudo intitulado «Técnica de "
          "auto-administração e conservação domiciliária da insulina em "
          "adultos com diabetes seguidos no Hospital Central de Nampula, "
          "2027», sob orientação de [Nome e grau académico do(a) "
          "orientador(a)]."),
        P("O estudo consiste na entrevista, na observação da técnica de "
          "injecção e no exame dos locais de injecção de adultos com "
          "diabetes em insulinoterapia que aceitem participar, e na consulta "
          "dos respectivos processos clínicos, sem qualquer alteração do "
          "tratamento. Solicita-se ainda o acesso ao registo de doentes em "
          "insulinoterapia, para definir a população elegível, e a "
          "utilização de uma sala reservada nos dias de consulta. A recolha "
          "só começará depois do parecer favorável do Comité Institucional "
          "de Bioética para a Saúde da Universidade Lúrio, cuja cópia será "
          "entregue a esta Direcção."),
        P("Os dados serão tratados de forma confidencial e os resultados "
          "serão apresentados a esta Direcção num relatório e numa sessão "
          "com as equipas da consulta e da farmácia, juntamente com uma "
          "proposta de material educativo para os doentes. Junto se envia o "
          "protocolo de investigação."),
        CAMPO("Pede deferimento."),
        CAMPO("O(A) estudante: ______________________________"),
        CAMPO("O(A) orientador(a): ______________________________"),
    ]),
]
