# -*- coding: utf-8 -*-
"""
Tema 11 (Farmacovigilância e Segurança do Medicamento).
Conhecimentos, atitudes e práticas de farmacovigilância e barreiras à
notificação de reacções adversas entre profissionais de saúde das unidades
sanitárias da cidade de Nampula, 2027.

Compor e validar:   python -X utf8 _motor/motor.py _conteudo/tema_11.py
Verificar fontes:   python -X utf8 _motor/refs.py verificar _conteudo/tema_11.py
"""
from blocos import (CAMPO, ESCALA, FORMULA, H3, LISTA, NOTA, P, PERG, QUADRO,
                    TABELA)

NUMERO = 11
SLUG = "CAP_Farmacovigilancia_Profissionais_Nampula"
TITULO = ("Conhecimentos, atitudes e práticas de farmacovigilância e barreiras "
          "à notificação de reacções adversas entre profissionais de saúde das "
          "unidades sanitárias da cidade de Nampula, 2027")
DESENHO = ("Transversal analítico, inquérito de conhecimentos, atitudes e "
           "práticas por questionário auto-administrado")

AUTOR = "[Nome do(a) estudante]"
ORIENTADOR = "[Nome e grau académico do(a) orientador(a)]"

# ---------------------------------------------------------------- resumo --
RESUMO = (
    "A segurança dos medicamentos depois de entrarem no mercado depende da "
    "notificação das suspeitas de reacções adversas pelos profissionais que "
    "prescrevem, dispensam e administram. A subnotificação é o principal "
    "obstáculo aos sistemas de notificação espontânea e é especialmente "
    "acentuada em África. Moçambique dispõe de um sistema nacional de "
    "farmacovigilância regulamentado, com ficha de notificação própria e com "
    "a obrigação profissional de notificar, mas desconhece-se o grau de "
    "preparação dos profissionais das unidades sanitárias para o cumprir. O "
    "estudo tem como objectivo avaliar os conhecimentos, as atitudes e as "
    "práticas de farmacovigilância e as barreiras percebidas à notificação "
    "entre médicos, enfermeiros e técnicos de farmácia das unidades "
    "sanitárias públicas da cidade de Nampula. Trata-se de um estudo "
    "transversal analítico, de abordagem quantitativa, a realizar entre "
    "Março e Maio de 2027. Será feito um recenseamento se o número de "
    "profissionais elegíveis não exceder 385; acima desse efectivo será "
    "seleccionada uma amostra estratificada por categoria profissional, "
    "dimensionada para uma margem de erro de cinco por cento, confiança de "
    "noventa e cinco por cento e dez por cento de não resposta, situando-se "
    "entre 219 e 325 participantes consoante o efectivo confirmado. O "
    "instrumento é um questionário auto-administrado adaptado de "
    "instrumentos publicados, submetido a validação de conteúdo por painel "
    "de peritos, a pré-teste e a avaliação da consistência interna. Os "
    "níveis de conhecimento, atitude e prática são classificados por pontos "
    "de corte de oitenta e de sessenta por cento. A análise recorre a "
    "proporções com intervalos de confiança, ao teste do qui-quadrado e à "
    "regressão logística. Esperam-se lacunas de conhecimento sobre a ficha e "
    "o circuito de notificação, atitudes favoráveis acompanhadas de prática "
    "reduzida e barreiras dominadas pela falta de tempo, pelo "
    "desconhecimento da ficha e pelo receio de consequências, resultados que "
    "orientarão a formação em serviço e a simplificação do circuito de "
    "notificação.")
PALAVRAS_CHAVE = ["efeitos adversos de medicamentos", "farmacovigilância",
                  "inquéritos de conhecimentos e práticas",
                  "pessoal de saúde", "segurança do doente"]
ABSTRACT = (
    "The safety of medicines after they reach the market depends on the "
    "reporting of suspected adverse reactions by the professionals who "
    "prescribe, dispense and administer them. Under-reporting is the main "
    "obstacle to spontaneous reporting systems and is particularly marked in "
    "Africa. Mozambique has a regulated national pharmacovigilance system, "
    "with its own reporting form and a professional duty to report, yet it "
    "is not known how prepared health facility staff are to comply with it. "
    "The study aims to assess pharmacovigilance knowledge, attitudes and "
    "practices, and the perceived barriers to reporting, among physicians, "
    "nurses and pharmacy technicians in the public health facilities of "
    "Nampula city. This is an analytical cross-sectional study with a "
    "quantitative approach, to be carried out between March and May 2027. A "
    "census will be conducted if the number of eligible professionals does "
    "not exceed 385; above that figure a sample stratified by professional "
    "category will be selected, sized for a five percent margin of error, "
    "ninety-five percent confidence and ten percent non-response, ranging "
    "from 219 to 325 participants according to the confirmed workforce. The "
    "instrument is a self-administered questionnaire adapted from published "
    "instruments, submitted to content validation by an expert panel, "
    "pre-testing and assessment of internal consistency. Knowledge, attitude "
    "and practice levels are classified using eighty and sixty percent "
    "cut-off points. The analysis uses proportions with confidence "
    "intervals, the chi-square test and logistic regression. The study "
    "expects to find knowledge gaps regarding the reporting form and the "
    "reporting circuit, favourable attitudes alongside limited practice, and "
    "barriers dominated by lack of time, unfamiliarity with the form and "
    "fear of consequences, findings that will guide in-service training and "
    "the simplification of the reporting circuit.")
KEYWORDS = ["drug-related side effects and adverse reactions",
            "health knowledge, attitudes, practice", "health personnel",
            "patient safety", "pharmacovigilance"]

ABREVIATURAS = [
    ("ANARME", "Autoridade Nacional Reguladora de Medicamentos"),
    ("ChecKAP", "Checklist for Reporting a Knowledge, Attitude and Practice "
                "Study"),
    ("CIBS-UniLúrio", "Comité Institucional de Bioética para a Saúde da "
                      "Universidade Lúrio"),
    ("CNBS", "Comité Nacional de Bioética para a Saúde"),
    ("DPS", "Direcção Provincial de Saúde"),
    ("FCS", "Faculdade de Ciências de Saúde"),
    ("IC95%", "intervalo de confiança a 95%"),
    ("IVC", "índice de validade de conteúdo"),
    ("KR-20", "fórmula 20 de Kuder-Richardson"),
    ("MISAU", "Ministério da Saúde"),
    ("OMS", "Organização Mundial da Saúde"),
    ("OR", "odds ratio (razão de possibilidades)"),
    ("ORa", "odds ratio ajustado"),
    ("SDSMAS", "Serviço Distrital de Saúde, Mulher e Acção Social"),
    ("SNFV", "Sistema Nacional de Farmacovigilância"),
    ("SPSS", "Statistical Package for the Social Sciences"),
    ("STROBE", "Strengthening the Reporting of Observational Studies in "
               "Epidemiology"),
]

# ------------------------------------------------------------ referencias --
FONTES = {
    "hazell2006": "Hazell L, Shakir SA. Under-reporting of adverse drug reactions : a systematic review. Drug Saf. 2006;29(5):385-96. doi:10.2165/00002018-200629050-00003. PMID: 16689555.",
    "zarei2024": "Zarei F, Dehghani A, Ratansiri A, Ghaffari M, Raina SK, Halimi A, et al. ChecKAP: A Checklist for Reporting a Knowledge, Attitude, and Practice (KAP) Study. Asian Pac J Cancer Prev. 2024;25(7):2573-2577. doi:10.31557/APJCP.2024.25.7.2573. PMID: 39068593.",
    "gidey2020": "Gidey K, Seifu M, Hailu BY, Asgedom SW, Niriayo YL. Healthcare professionals knowledge, attitude and practice of adverse drug reactions reporting in Ethiopia: a cross-sectional study. BMJ Open. 2020;10(2):e034553. doi:10.1136/bmjopen-2019-034553. PMID: 32102821.",
    "seid2018": "Seid MA, Kasahun AE, Mante BM, Gebremariam SN. Healthcare professionals' knowledge, attitude and practice towards adverse drug reaction (ADR) reporting at the health center level in Ethiopia. Int J Clin Pharm. 2018;40(4):895-902. doi:10.1007/s11096-018-0682-0. PMID: 30094559.",
    "rotimi2024": "Rotimi K, Fagbemi B, Omole G, Biambo AA, Ibinaiye T, Iwegbu A, et al. Awareness, knowledge, attitude, and practice of adverse drug reaction reporting among health workers in primary health centres participating in seasonal malaria chemoprevention campaign in Nigeria in 2022: a cross-sectional survey. BMC Health Serv Res. 2024;24(1):952. doi:10.1186/s12913-024-11343-y. PMID: 39164692.",
    "adisa2019": "Adisa R, Omitogun TI. Awareness, knowledge, attitude and practice of adverse drug reaction reporting among health workers and patients in selected primary healthcare centres in Ibadan, southwestern Nigeria. BMC Health Serv Res. 2019;19(1):926. doi:10.1186/s12913-019-4775-9. PMID: 31796034.",
    "powell2023": "Powell JF, Henneh IT, Ekor M. Knowledge, attitude and practice of physicians and nurses at the cape coast teaching hospital in the Central Region of Ghana on spontaneous adverse drug reaction reporting. PLoS One. 2023;18(7):e0288100. doi:10.1371/journal.pone.0288100. PMID: 37418384.",
    "haines2020": "Haines HM, Meyer JC, Summers RS, Godman BB. Knowledge, attitudes and practices of health care professionals towards adverse drug reaction reporting in public sector primary health care facilities in a South African district. Eur J Clin Pharmacol. 2020;76(7):991-1001. doi:10.1007/s00228-020-02862-8. PMID: 32296857.",
    "chiumia2024": "Chiumia F, Dzabala N, Ndalama A, Sambakunsi C, Raguenaud ME, Merle C, et al. Impact of in-service training on the knowledge, attitude, and practice of pharmacovigilance in Malawi: a cross-sectional mixed methods study. Malawi Med J. 2024;36(3):163-169. doi:10.4314/mmj.v36i3.2. PMID: 40018398.",
    "adenuga2020": "Adenuga BA, Kibuule D, Rennie TW. Optimizing spontaneous adverse drug reaction reporting in public healthcare setting in Namibia. Basic Clin Pharmacol Toxicol. 2020;126(3):247-253. doi:10.1111/bcpt.13325. PMID: 31520574.",
    "hamid2025": "Hamid M, Osman M. Knowledge, attitude, and practice of pharmacovigilance among healthcare professionals at a tertiary level hospital, Sudan: a cross sectional study. BMC Health Serv Res. 2025;26(1):89. doi:10.1186/s12913-025-13364-7. PMID: 41351049.",
    "mssusa2025": "Mssusa AK, Kagashe G, Maregesi S, Holst L. Pharmacovigilance and herbal medicines safety: a cross-sectional study of healthcare professionals' knowledge, attitudes and practices in selected regions of Tanzania, 2021. BMC Complement Med Ther. 2025;26(1):37. doi:10.1186/s12906-025-05226-w. PMID: 41462198.",
    "fiagbey2026": "Fiagbey EDK, Nyame L, Bao Z, Kipanga ZG, Lamptey INL, Nyame DK, et al. Knowledge, awareness, and practices of adverse drug reaction reporting among healthcare professionals in the Ashanti region of Ghana. Indian J Pharmacol. 2026;58(5):530-536. doi:10.4103/ijp.ijp_1239_25. PMID: 42683983.",
    "ampadu2018": "Ampadu HH, Hoekman J, Arhinful D, Amoama-Dapaah M, Leufkens HGM, Dodoo ANO. Organizational capacities of national pharmacovigilance centres in Africa: assessment of resource elements associated with successful and unsuccessful pharmacovigilance experiences. Global Health. 2018;14(1):109. doi:10.1186/s12992-018-0431-0. PMID: 30445979.",
    "mussa2021": "Mussá M, Gaspar I, Namburete L, Sitoie TV, Couto A, Paulino JM, et al. Protocol for active safety monitoring of a cohort of patients using a dolutegravir-based antiretroviral regimen in Mozambique. BMJ Open. 2021;11(9):e050671. doi:10.1136/bmjopen-2021-050671. PMID: 34493520.",
    "haerdtlein2023": "Haerdtlein A, Debold E, Rottenkolber M, Boehmer AM, Pudritz YM, Shahid F, et al. Which Adverse Events and Which Drugs Are Implicated in Drug-Related Hospital Admissions? A Systematic Review and Meta-Analysis. J Clin Med. 2023;12(4). doi:10.3390/jcm12041320. PMID: 36835854.",
    "sendekie2023": "Sendekie AK, Kasahun AE, Limenh LW, Dagnaw AD, Belachew EA. Clinical and economic impact of adverse drug reactions in hospitalised patients: prospective matched nested case-control study in Ethiopia. BMJ Open. 2023;13(6):e073777. doi:10.1136/bmjopen-2023-073777. PMID: 37280017.",
    "hailu2020": "Hailu AD, Mohammed SA. Adverse Drug Reaction Reporting in Ethiopia: Systematic Review. Biomed Res Int. 2020;2020:8569314. doi:10.1155/2020/8569314. PMID: 32851089.",
    "terblanche2017": "Terblanche A, Meyer JC, Godman B, Summers RS. Knowledge, attitudes and perspective on adverse drug reaction reporting in a public sector hospital in South Africa: baseline analysis. Hosp Pract (1995). 2017;45(5):238-245. doi:10.1080/21548331.2017.1381013. PMID: 28914115.",
    "ncube2025": "Ncube N, Lubbe MS, Steyn H, Motaze NV. Awareness and Attitudes Regarding Adverse Drug Events and Reporting in South Africa. Ther Innov Regul Sci. 2025;59(4):882-891. doi:10.1007/s43441-025-00795-x. PMID: 40360900.",
    "adedeji2021": "Adedeji WA, Adegoke AB, Fehintola FA. Adverse drug reactions reporting practice and associated factors among community health extension workers in public health facilities, Southwest, Nigeria. Pan Afr Med J. 2021;40:165. doi:10.11604/pamj.2021.40.165.28574. PMID: 34970407.",
    "issak2025": "Issak MA, Mohamed ZFA, Mohammed KAA. Knowledge, attitudes, practices towards medication errors and adverse drug reactions reporting among healthcare professionals in Dongola, Sudan: a cross-sectional study. Sci Rep. 2025;15(1):43336. doi:10.1038/s41598-025-27221-4. PMID: 41276574.",
    "barry2020": "Barry A, Olsson S, Minzi O, Bienvenu E, Makonnen E, Kamuhabwa A, et al. Comparative Assessment of the National Pharmacovigilance Systems in East Africa: Ethiopia, Kenya, Rwanda and Tanzania. Drug Saf. 2020;43(4):339-350. doi:10.1007/s40264-019-00898-z. PMID: 31919794.",
    "tiemersma2021": "Tiemersma EW, Ali I, Alemu A, Avong YK, Duga A, Elagbaje C, et al. Baseline assessment of pharmacovigilance activities in four sub-Saharan African countries: a perspective on tuberculosis. BMC Health Serv Res. 2021;21(1):1062. doi:10.1186/s12913-021-07043-6. PMID: 34625085.",
    "van2024": "van Puijenbroek E, Barry A, Khaemba C, Ntirenganya L, Gebreyesus TD, Fimbo A, et al. Short-Term Training, a Useful Approach for Sustainable Pharmacovigilance Knowledge Development in Tanzania, Kenya, Ethiopia and Rwanda. Drug Saf. 2024;47(12):1193-1202. doi:10.1007/s40264-024-01469-7. PMID: 39162987.",
    "anbeo2023": "Anbeo ZG, Abacıoğlu N. A Systematic Review of Healthcare Professionals' Knowledge, Attitudes, and Practices Regarding Adverse Drug Reaction Reporting in Ethiopia. Turk J Pharm Sci. 2023;20(3):198-209. doi:10.4274/tjps.galenos.2022.28034. PMID: 37417202.",
    "zivanovic2022": "Živanović D, Mijatović Jovin V, Javorac J, Kvrgić S, Rašković A, Stojkov S, et al. Measuring pharmacovigilance knowledge and attitudes among healthcare sciences students: development and validation of a universal questionnaire. Eur Rev Med Pharmacol Sci. 2022;26(4):1196-1214. doi:10.26355/eurrev_202202_28112. PMID: 35253176.",
    "muringazuva2017": "Muringazuva C, Chirundu D, Mungati M, Shambira G, Gombe N, Bangure D, et al. Evaluation of the adverse drug reaction surveillance system Kadoma City, Zimbabwe 2015. Pan Afr Med J. 2017;27:55. doi:10.11604/pamj.2017.27.55.11090. PMID: 28819477.",
    "sengo2023": "Sengo DB, Salamo ZMA, Dos Santos IIDB, Mate LM, Chivinde SM, Moragues R, et al. Assessment of the distribution of human and material resources for eye health in the public sector in Nampula, Mozambique. Hum Resour Health. 2023;21(1):27. doi:10.1186/s12960-023-00812-w. PMID: 37004070.",
    "nduka2024": "Nduka SO, Ibe CO, Nwaodu MA, Robert CC. Identifying strategies to improve adverse drug reporting through key informant interviews among community pharmacists in a developing country. Sci Rep. 2024;14(1):16821. doi:10.1038/s41598-024-67263-8. PMID: 39039143.",
    "elemuwa2024": "Elemuwa UG, Bitrus F, Oreagba IA, Osakwe AI, Abiodun AS, Onu K, et al. Trends in Adverse Event Reporting Before and After the Introduction of the Med Safety App in Nigeria. Pharmaceut Med. 2024;38(3):251-259. doi:10.1007/s40290-024-00524-z. PMID: 38705932.",
    "ndagije2019": "Ndagije HB, Manirakiza L, Kajungu D, Galiwango E, Kusemererwa D, Olsson S, et al. The effect of community dialogues and sensitization on patient reporting of adverse events in rural Uganda: Uncontrolled before-after study. PLoS One. 2019;14(5):e0203721. doi:10.1371/journal.pone.0203721. PMID: 31071096.",
    "juttla2024": "Juttla PK, Ndiritu M, Milliano F, Odongo AO, Mwancha-Kwasa M. Knowledge, attitudes and practices towards COVID-19 among healthcare workers: A cross-sectional survey from Kiambu County, Kenya. PLoS One. 2024;19(3):e0297335. doi:10.1371/journal.pone.0297335. PMID: 38470888.",
    "almanasreh2019": "Almanasreh E, Moles R, Chen TF. Evaluation of methods used for estimating content validity. Res Social Adm Pharm. 2019;15(2):214-221. doi:10.1016/j.sapharm.2018.03.066. PMID: 29606610.",
    "world2025": "World Medical Association. World Medical Association Declaration of Helsinki: Ethical Principles for Medical Research Involving Human Participants. JAMA. 2025;333(1):71-74. doi:10.1001/jama.2024.21972. PMID: 39425955.",
    "von2008": "von Elm E, Altman DG, Egger M, Pocock SJ, Gøtzsche PC, Vandenbroucke JP. The Strengthening the Reporting of Observational Studies in Epidemiology (STROBE) statement: guidelines for reporting observational studies. J Clin Epidemiol. 2008;61(4):344-9. doi:10.1016/j.jclinepi.2007.11.008. PMID: 18313558.",
    "anarme2024": "Autoridade Nacional Reguladora de Medicamentos. Manual de Boas Práticas de Farmacovigilância. Versão 00 [Internet]. Maputo: ANARME, IP; 2024 [citado 2026 Set 19]. Disponível em: https://docs.bvsalud.org/biblioref/2025/03/1588906/manual-de-boas-praticas-de-farmacovigilancia.pdf",
    "umc2026": "Uppsala Monitoring Centre. Members of the WHO Programme for International Drug Monitoring [Internet]. Uppsala: Uppsala Monitoring Centre; 2026 [citado 2026 Set 19]. Disponível em: https://who-umc.org/about-the-who-programme-for-international-drug-monitoring/programme-members/",
    "oms2026": "World Health Organization. Pharmacovigilance [Internet]. Genebra: Organização Mundial da Saúde; 2026 [citado 2026 Set 19]. Disponível em: https://www.who.int/teams/regulation-prequalification/regulation-and-safety/pharmacovigilance",
}

SEMINAIS = {
    "hazell2006": "Revisão sistemática de referência sobre a magnitude da "
                  "subnotificação de reacções adversas, ainda hoje a fonte "
                  "citada para a mediana de 94% de subnotificação; não foi "
                  "substituída por nenhuma revisão posterior equivalente.",
    "von2008": "Norma de relato de estudos observacionais (STROBE), documento "
               "original que continua em vigor e que o presente protocolo "
               "segue na componente transversal.",
}

# ----------------------------------------------------- 1. introducao --------
INTRODUCAO = [
    P("A farmacovigilância é definida pela Organização Mundial da Saúde "
      "(OMS) como a ciência e o conjunto de actividades relativas à "
      "detecção, avaliação, compreensão e prevenção de efeitos adversos ou "
      "de qualquer outro problema relacionado com medicamentos ou vacinas "
      "{oms2026}. O ensaio clínico que precede a autorização de introdução "
      "no mercado estuda um número limitado de doentes, durante um período "
      "curto e em condições seleccionadas, pelo que as reacções raras, as "
      "que surgem tardiamente e as que ocorrem em grupos excluídos dos "
      "ensaios só se tornam visíveis quando o medicamento passa a ser "
      "utilizado em larga escala. A vigilância depois da comercialização "
      "deixou por isso de ser acessória e passou a ser a única forma "
      "realista de conhecer o perfil de segurança de um medicamento na "
      "população que efectivamente o usa {anarme2024}."),
    P("O peso das reacções adversas em saúde pública está bem documentado. "
      "Uma revisão sistemática com meta-análise de estudos publicados entre "
      "2012 e 2021 estimou que 8,3% das admissões a serviços de urgência e a "
      "enfermarias se devem a reacções adversas, com intervalo de confiança a "
      "95% (IC95%) de 6,4 a 10,7%, e que cerca de metade delas, 44,7% (IC95% "
      "28,1 a 62,4%), seriam pelo menos possivelmente evitáveis "
      "{haerdtlein2023}. Em África, um estudo prospectivo de casos e "
      "controlos emparelhados conduzido num hospital universitário etíope "
      "mostrou que os doentes internados com reacções adversas tiveram "
      "internamentos mais longos, 19,8 contra 15,2 dias, mais passagens por "
      "cuidados intensivos, 11,2% contra 6,8%, e mortalidade hospitalar mais "
      "elevada, 4,4% contra 1,9%, além de custos directos superiores "
      "{sendekie2023}. O dano é, portanto, clínico e económico, e uma parte "
      "substancial dele é prevenível se for detectado a tempo."),
    P("A detecção depende quase inteiramente da notificação espontânea, o "
      "método mais simples e económico, aplicável a todos os medicamentos e "
      "a toda a população durante todo o ciclo de vida do produto "
      "{anarme2024}. O seu ponto fraco é conhecido e mensurável: a revisão "
      "sistemática de referência sobre o tema, que reuniu 37 estudos de 12 "
      "países, encontrou uma mediana de subnotificação de 94%, com "
      "amplitude interquartil de 82 a 98%, e mostrou que mesmo as reacções "
      "graves continuam por notificar em cerca de 85% dos casos "
      "{hazell2006}. Um sistema nacional pode estar formalmente instalado e "
      "produzir pouca informação útil se os profissionais que observam as "
      "reacções não as comunicarem."),
    P("Na África subsariana o problema soma-se à fragilidade das estruturas. "
      "Um inquérito a dirigentes de centros nacionais de farmacovigilância "
      "de 18 países africanos concluiu que todos enfrentam os mesmos três "
      "problemas de fundo, independentemente da maturidade dos seus "
      "sistemas: dependência excessiva de parceiros de desenvolvimento, "
      "desinteresse dos governos depois de obtida a adesão ao Programa da "
      "OMS de Monitorização Internacional de Medicamentos, e dificuldade em "
      "envolver de forma sustentada os programas verticais de saúde "
      "pública {ampadu2018}. A avaliação comparativa dos sistemas da Etiópia, "
      "do Quénia, do Ruanda e da Tanzânia mostrou que os progressos "
      "regulamentares não se traduziram automaticamente em notificação "
      "regular a partir das unidades sanitárias {barry2020}, e a avaliação "
      "de base das actividades de farmacovigilância em quatro países "
      "subsarianos, na perspectiva da tuberculose, identificou falta de "
      "formação, de fichas e de retorno de informação como limitações "
      "transversais {tiemersma2021}."),
    P("Moçambique é membro do Programa da OMS de Monitorização Internacional "
      "de Medicamentos desde 2005 {umc2026}. O Sistema Nacional de "
      "Farmacovigilância (SNFV) é regido pela Lei n.º 12/2017, de 8 de "
      "Setembro, e pelo Diploma Ministerial n.º 3/2023, de 4 de Janeiro, e "
      "o Manual de Boas Práticas de Farmacovigilância, aprovado pela "
      "Autoridade Nacional Reguladora de Medicamentos (ANARME) em 2024, "
      "estabelece que todos os profissionais de saúde do sistema nacional de "
      "saúde devem notificar de imediato todas as suspeitas de reacções "
      "adversas de que tenham conhecimento, mesmo quando houver dúvida "
      "quanto à associação entre o acontecimento e o medicamento "
      "{anarme2024}. O mesmo manual fixa os critérios mínimos de uma "
      "notificação válida, um doente identificável, um notificador "
      "identificável, uma suspeita de reacção adversa e pelo menos um "
      "medicamento suspeito, e garante que o notificador não é penalizado "
      "por notificar."),
    P("A experiência moçambicana de vigilância de segurança tem-se apoiado "
      "sobretudo em dispositivos verticais e temporários. A transição "
      "nacional para o regime anti-retroviral com dolutegravir levou à "
      "criação de um sistema de vigilância activa em dez unidades sanitárias "
      "sentinela, com uma coorte prevista de 3.000 doentes {mussa2021}, "
      "solução adequada para um sinal de segurança concreto mas que não "
      "substitui a notificação espontânea de rotina em toda a rede. Na "
      "cidade de Nampula, capital da província mais populosa do país, a "
      "concentração de profissionais e de serviços diferenciados é "
      "documentada {sengo2023} e faz dela o local onde a notificação "
      "espontânea teria maior probabilidade de existir; não há, contudo, "
      "qualquer estudo publicado sobre o que os profissionais aí colocados "
      "sabem, pensam e fazem em matéria de farmacovigilância."),
    P("A pesquisa bibliográfica realizada para este protocolo não "
      "identificou nenhum inquérito de conhecimentos, atitudes e práticas de "
      "farmacovigilância conduzido junto de profissionais de saúde em "
      "Moçambique, enquanto estudos equivalentes existem na Etiópia "
      "{gidey2020}, na Nigéria {rotimi2024}, no Gana {fiagbey2026}, na "
      "África do Sul {haines2020}, na Namíbia {adenuga2020}, no Malawi "
      "{chiumia2024} e na Tanzânia {mssusa2025}. Sem essa informação, "
      "qualquer intervenção de formação ou de reorganização do circuito de "
      "notificação na cidade de Nampula seria desenhada às cegas. O presente "
      "estudo propõe-se produzir essa linha de base, medindo conhecimentos, "
      "atitudes e práticas, hierarquizando as barreiras percebidas e "
      "identificando os factores associados à notificação efectiva."),
]

# ----------------------------------------------------- 2. problema ----------
PROBLEMA = [
    P("As unidades sanitárias da cidade de Nampula dispensam diariamente "
      "medicamentos anti-retrovirais, antituberculosos, antimaláricos, "
      "antibióticos, anti-hipertensores e antidiabéticos orais a um número "
      "elevado de utentes, num contexto de rotação frequente de esquemas "
      "terapêuticos definidos a nível central. A obrigação de notificar as "
      "suspeitas de reacções adversas está escrita e é inequívoca "
      "{anarme2024}, mas a sua execução depende de cada profissional "
      "reconhecer a reacção, saber que a ficha existe, saber onde a obter, "
      "saber preenchê-la e saber a quem a entregar. Qualquer falha nesta "
      "cadeia transforma uma reacção observada em informação perdida."),
    P("A consequência não é apenas administrativa. Quando as notificações "
      "não chegam ao Centro Nacional de Farmacovigilância, o país deixa de "
      "poder detectar sinais próprios e passa a depender de alertas gerados "
      "noutras populações, com perfis genéticos, nutricionais e de "
      "co-morbilidade diferentes. Ao nível da unidade sanitária, a "
      "subnotificação retira à equipa a possibilidade de reconhecer padrões "
      "locais, por exemplo a concentração de reacções cutâneas associadas a "
      "um lote ou a um esquema, e de agir sobre eles. Os estudos africanos "
      "mostram que o padrão é persistente: atitudes favoráveis à notificação "
      "convivem com proporções de notificação efectiva de 16,0% na África do "
      "Sul {haines2020}, 18,9% no Sudão {hamid2025}, 22,9% na Tanzânia "
      "{mssusa2025} e 12,6% entre agentes de saúde comunitários da Nigéria "
      "{adedeji2021}."),
    P("O que falta saber, no caso concreto da cidade de Nampula, é a "
      "dimensão de cada elo desta cadeia. Não se conhece a proporção de "
      "médicos, enfermeiros e técnicos de farmácia que define correctamente "
      "reacção adversa, que já viu a ficha de notificação em uso no país, "
      "que sabe a quem a entregar e que efectivamente notificou pelo menos "
      "uma suspeita no último ano. Também não se conhece o peso relativo das "
      "barreiras invocadas noutros contextos, designadamente a falta de "
      "tempo, o desconhecimento do procedimento, a indisponibilidade da "
      "ficha, a incerteza quanto ao diagnóstico de causalidade e o receio de "
      "consequências profissionais {terblanche2017}. Sem hierarquizar estas "
      "barreiras é impossível decidir se a prioridade é formar, imprimir "
      "fichas, criar um ponto focal ou simplificar o circuito."),
    P("O estudo delimita-se a este problema mensurável e accionável: "
      "descrever conhecimentos, atitudes e práticas, hierarquizar barreiras "
      "e identificar os factores associados à notificação efectiva, num "
      "conjunto de profissionais que trabalha num território urbano "
      "delimitado e sob a mesma direcção distrital de saúde."),
]
PERGUNTA = ("Quais são os conhecimentos, as atitudes e as práticas sobre "
            "farmacovigilância, e quais as barreiras percebidas à notificação "
            "de suspeitas de reacções adversas, dos médicos, enfermeiros e "
            "técnicos de farmácia das unidades sanitárias públicas da cidade "
            "de Nampula em 2027?")
DELIMITACAO = [
    P("O estudo decorre nas unidades sanitárias públicas da cidade de "
      "Nampula, província de Nampula, sob a jurisdição do Serviço Distrital "
      "de Saúde, Mulher e Acção Social (SDSMAS) da Cidade de Nampula e da "
      "Direcção Provincial de Saúde (DPS) de Nampula, incluindo o hospital "
      "de referência da cidade e os centros de saúde urbanos [confirmar a "
      "lista e o número de unidades sanitárias junto do SDSMAS da Cidade de "
      "Nampula]. A população é constituída pelos profissionais de saúde que "
      "prescrevem, dispensam ou administram medicamentos, agrupados em três "
      "categorias: médicos e técnicos de medicina, enfermeiros de todos os "
      "níveis, e técnicos e agentes de farmácia. A recolha decorre entre "
      "Março e Maio de 2027, depois da aprovação ética e das autorizações "
      "institucionais."),
    P("O objecto é o conhecimento declarado sobre o conceito de reacção "
      "adversa e sobre o circuito nacional de notificação, a atitude "
      "perante a notificação, a prática auto-relatada de notificação nos "
      "doze meses anteriores e as barreiras percebidas. Ficam fora do "
      "estudo o sector privado, as farmácias comunitárias e os depósitos de "
      "medicamentos, os estudantes em formação prática, a determinação da "
      "incidência real de reacções adversas nos doentes, a avaliação de "
      "causalidade dos casos e a análise da qualidade de preenchimento das "
      "fichas efectivamente submetidas, que exigiriam desenhos distintos."),
]

# ----------------------------------------------------- 3. objectivos --------
OBJECTIVO_GERAL = ("Avaliar os conhecimentos, as atitudes e as práticas sobre "
                   "farmacovigilância e as barreiras percebidas à notificação "
                   "de suspeitas de reacções adversas entre os profissionais "
                   "de saúde das unidades sanitárias públicas da cidade de "
                   "Nampula, em 2027")
OBJECTIVOS_ESPECIFICOS = [
    "Caracterizar os participantes quanto ao perfil sociodemográfico, à "
    "categoria e ao tempo de exercício profissional, ao nível da unidade "
    "sanitária e à exposição prévia a formação em farmacovigilância",
    "Determinar a proporção de profissionais com nível bom, moderado e fraco "
    "de conhecimentos sobre o conceito de reacção adversa, a ficha de "
    "notificação e o circuito nacional de notificação",
    "Determinar a proporção de profissionais com atitude favorável perante a "
    "notificação e a proporção que notificou pelo menos uma suspeita de "
    "reacção adversa através da ficha oficial nos doze meses anteriores",
    "Identificar e hierarquizar as barreiras percebidas à notificação de "
    "suspeitas de reacções adversas",
    "Analisar a associação entre a notificação efectiva e o nível de "
    "conhecimentos, a atitude, a formação prévia em farmacovigilância, a "
    "categoria profissional e o tempo de exercício",
]

# ----------------------------------------------------- 4. hipoteses ---------
HIPOTESES_INTRO = [
    P("As hipóteses referem-se ao objectivo específico 5. A variável "
      "dependente é a notificação efectiva, definida como ter notificado "
      "pelo menos uma suspeita de reacção adversa através da ficha oficial "
      "nos doze meses anteriores ao inquérito. Os objectivos específicos 1 a "
      "4 são descritivos e estão traduzidos em questões de investigação."),
]
HIPOTESES = [
    ("H0", "não existe associação estatisticamente significativa entre o "
           "nível de conhecimentos sobre farmacovigilância e a notificação "
           "efectiva de suspeitas de reacções adversas"),
    ("H1", "os profissionais com nível bom ou moderado de conhecimentos "
           "apresentam maior probabilidade de notificação efectiva do que os "
           "profissionais com nível fraco"),
    ("H0", "não existe associação estatisticamente significativa entre ter "
           "recebido formação prévia em farmacovigilância e a notificação "
           "efectiva de suspeitas de reacções adversas"),
    ("H1", "os profissionais com formação prévia em farmacovigilância "
           "apresentam maior probabilidade de notificação efectiva do que os "
           "profissionais sem essa formação"),
]
QUESTOES = [
    "Qual é a distribuição dos participantes por categoria profissional, "
    "tempo de exercício, nível da unidade sanitária e formação prévia em "
    "farmacovigilância?",
    "Que proporção de profissionais atinge nível bom, moderado e fraco de "
    "conhecimentos sobre farmacovigilância?",
    "Que proporção de profissionais apresenta atitude favorável e que "
    "proporção notificou pelo menos uma suspeita no último ano?",
    "Quais são as barreiras à notificação mais frequentemente assinaladas e "
    "qual a sua ordem de importância?",
]

# ----------------------------------------------------- 5. justificativa -----
JUSTIFICATIVA_INTRO = [
    P("O estudo justifica-se por preencher uma lacuna de informação sobre um "
      "sistema que o país já instituiu por via legal e cujo funcionamento "
      "depende de um comportamento profissional que nunca foi medido em "
      "Moçambique."),
]
JUSTIFICATIVA = {
    "cientifica": [
        P("A literatura sobre conhecimentos, atitudes e práticas de "
          "farmacovigilância em África concentra-se na Etiópia, na Nigéria e "
          "no Gana, com contributos mais recentes da Tanzânia, do Sudão e do "
          "Malawi {anbeo2023,mssusa2025,issak2025,chiumia2024}. Não existe "
          "publicação equivalente para Moçambique, o que impede a "
          "comparação entre países lusófonos e deixa por testar se os "
          "padrões descritos noutros sistemas de saúde se reproduzem num "
          "sistema com legislação recente e uma autoridade reguladora "
          "criada há poucos anos {anarme2024}."),
        P("O estudo acrescenta ainda um elemento metodológico útil: mede a "
          "prática de notificação com uma definição operacional explícita e "
          "verificável, ancorada nos critérios mínimos de notificação "
          "fixados a nível nacional, em vez da pergunta genérica «já "
          "notificou alguma vez» que dificulta a comparação entre estudos e "
          "que tende a sobrestimar a prática {hazell2006}."),
    ],
    "academica": [
        P("As instituições de ensino da área da saúde têm, no quadro "
          "normativo moçambicano, a responsabilidade explícita de "
          "incorporar módulos de farmacovigilância nos currículos, de "
          "assegurar formação em serviço e desenvolvimento profissional "
          "contínuo, e de realizar estudos de segurança {anarme2024}. Um "
          "trabalho de fim de curso da Licenciatura em Farmácia da "
          "Faculdade de Ciências de Saúde (FCS) da Universidade Lúrio sobre "
          "esta matéria cumpre directamente essa atribuição institucional."),
        P("O protocolo exercita ainda competências centrais da formação "
          "farmacêutica, da construção e validação de um instrumento de "
          "medida à análise multivariável, e produz um instrumento em "
          "português que fica disponível para replicação noutras cidades e "
          "províncias, condição para que os resultados de Nampula possam "
          "vir a ser comparados com outros contextos moçambicanos."),
    ],
    "social": [
        P("Os utentes das unidades sanitárias da cidade de Nampula são os "
          "primeiros beneficiários de um sistema de notificação que "
          "funcione. Cerca de 8,3% das admissões hospitalares devem-se a "
          "reacções adversas e perto de metade delas é evitável "
          "{haerdtlein2023}; em contexto africano, o internamento de um "
          "doente com reacção adversa prolonga-se em média em mais de "
          "quatro dias e associa-se a maior mortalidade hospitalar "
          "{sendekie2023}. Cada reacção detectada e comunicada a tempo é "
          "uma oportunidade de evitar um dano semelhante noutro doente."),
        P("O estudo tem também um efeito directo de sensibilização. A "
          "experiência do Uganda mostra que iniciativas deliberadas de "
          "sensibilização aumentam a notificação {ndagije2019}, e a simples "
          "passagem de um questionário que descreve a ficha e o circuito "
          "deixa nos serviços uma informação que antes não circulava. O "
          "relatório devolvido a cada unidade sanitária, em forma agregada, "
          "permitirá às equipas reconhecer as suas próprias lacunas sem "
          "exposição individual."),
    ],
    "politica": [
        P("Os resultados destinam-se a decisões concretas do SDSMAS da "
          "Cidade de Nampula, da DPS de Nampula e da ANARME. Se a barreira "
          "dominante for o desconhecimento do procedimento, a resposta é "
          "formação em serviço, cuja eficácia está demonstrada: no Malawi, "
          "a pontuação média de conhecimento subiu de 56% (IC95% 53 a 58%) "
          "para 66% (IC95% 64 a 69%) depois da formação, com aumento da "
          "detecção e da notificação {chiumia2024}. Se a barreira dominante "
          "for a indisponibilidade da ficha ou a complexidade do circuito, "
          "a resposta é logística e organizativa."),
        P("A experiência nigeriana com a introdução de uma via electrónica "
          "de notificação ilustra o alcance desta segunda via: o número de "
          "notificações recebidas passou de 2.051 no período de referência "
          "para 18.995 no período seguinte, com redução da notificação em "
          "papel de 98,4% para 15,7% e aumento da notificação directa pelos "
          "consumidores de 2,7% para 17,6% {elemuwa2024}. Conhecer, em "
          "Nampula, qual das barreiras pesa mais permite escolher entre "
          "estas opções com fundamento local em vez de por imitação."),
    ],
}

# ----------------------------------------------------- 6. revisao -----------
REVISAO = [
    ("Reacção adversa a medicamentos: conceito, classificação e magnitude", [
        P("A definição adoptada no quadro normativo moçambicano descreve a "
          "reacção adversa como uma resposta nociva e não desejada que "
          "ocorre em doses normalmente usadas na prática clínica, e "
          "qualifica como grave a reacção que conduz à morte, põe a vida em "
          "perigo, requer hospitalização, conduz a incapacidade persistente "
          "ou significativa, resulta em anomalia congénita ou é considerada "
          "clinicamente importante {anarme2024}. Esta é a definição "
          "operacional usada neste estudo, tanto na formulação dos itens de "
          "conhecimento como na classificação das respostas, por ser a que "
          "os profissionais estão obrigados a aplicar no seu exercício."),
        P("A distinção entre reacção adversa e acontecimento adverso é "
          "determinante para a notificação. O acontecimento adverso é "
          "qualquer ocorrência clínica desfavorável durante o tratamento, "
          "sem que a relação causal esteja estabelecida; a reacção adversa "
          "pressupõe a suspeita dessa relação. O manual nacional resolve a "
          "ambiguidade a favor da notificação, ao instruir os profissionais "
          "a notificar mesmo quando houver dúvida quanto à associação "
          "precisa entre o acontecimento e o medicamento {anarme2024}. Este "
          "ponto é frequentemente mal compreendido: em estudos africanos, "
          "uma parte considerável dos profissionais declara não notificar "
          "por não ter a certeza de que a reacção foi causada pelo "
          "medicamento {terblanche2017,rotimi2024}."),
        P("Quanto à magnitude, a meta-análise mais recente de estudos "
          "observacionais estimou em 8,3% (IC95% 6,4 a 10,7%) a proporção "
          "de admissões a urgências e enfermarias atribuíveis a reacções "
          "adversas e em 13,9% (IC95% 8,1 a 22,8%) a proporção atribuível a "
          "acontecimentos adversos medicamentosos em sentido lato; as "
          "classes mais implicadas foram os fármacos do sistema nervoso, "
          "seguidos dos cardiovasculares e dos antitrombóticos "
          "{haerdtlein2023}. Em África, o estudo etíope de casos e "
          "controlos emparelhados quantificou o custo clínico e económico "
          "do fenómeno ao nível do internamento {sendekie2023}, e um estudo "
          "de campo no Gana mostrou que os antibióticos, com 36,5%, e os "
          "anti-hipertensores, com 17,8%, dominam as reacções "
          "efectivamente relatadas pelos profissionais, com manifestações "
          "sobretudo gastrintestinais, 34,4%, e do sistema nervoso central, "
          "32,4% {fiagbey2026}."),
    ]),
    ("Farmacovigilância e notificação espontânea: métodos, forças e limites", [
        P("A farmacovigilância combina métodos passivos e activos. A "
          "notificação espontânea, ou vigilância passiva, consiste no "
          "relato simplificado de uma ocorrência associada a um tratamento "
          "suspeito, feito pelo próprio doente ou por outro notificador. As "
          "suas vantagens reconhecidas são a cobertura de toda a população "
          "e de todos os medicamentos durante todo o ciclo de vida do "
          "produto, o baixo custo, o horizonte temporal longo, a não "
          "interferência com a prescrição e a capacidade de gerar sinais "
          "precoces e de detectar reacções raras {anarme2024}. A vigilância "
          "activa, pelo contrário, procura determinar de forma completa o "
          "número de acontecimentos através de um processo contínuo "
          "pré-organizado, como o seguimento de coortes sentinela, e reduz "
          "a subnotificação à custa de recursos muito superiores."),
        P("A fraqueza estrutural da notificação espontânea é a "
          "subnotificação. A revisão sistemática que reuniu 43 estimativas "
          "numéricas provenientes de 37 estudos e 12 países encontrou uma "
          "mediana de subnotificação de 94%, com amplitude interquartil de "
          "82 a 98%, sem diferença significativa entre cuidados primários e "
          "hospitalares; mesmo para combinações de medicamento e reacção "
          "graves e específicas a mediana permaneceu em 85% {hazell2006}. "
          "Daqui decorre que o número de notificações recebidas por um "
          "centro nacional mede sobretudo o comportamento dos notificadores "
          "e só indirectamente a segurança dos medicamentos."),
        P("Em Moçambique, a resposta a um sinal de segurança concreto, o "
          "levantado pelos resultados do estudo Tsepamo sobre o "
          "dolutegravir, foi a criação de um sistema de vigilância activa "
          "em dez unidades sanitárias sentinela, com seguimento mensal nos "
          "primeiros três meses e trimestral até completar um ano, e uma "
          "coorte prevista de 3.000 doentes {mussa2021}. Esta escolha "
          "ilustra a complementaridade dos métodos: a vigilância activa "
          "responde a uma pergunta delimitada sobre um produto, ao passo "
          "que a notificação espontânea é o único mecanismo capaz de cobrir "
          "os restantes milhares de medicamentos em uso na rede sanitária. "
          "A capacidade de notificação espontânea depende inteiramente dos "
          "profissionais das unidades sanitárias, que este estudo avalia."),
    ]),
    ("O Sistema Nacional de Farmacovigilância e o circuito da notificação em "
     "Moçambique", [
        P("O SNFV é regido pela Lei n.º 12/2017, de 8 de Setembro, relativa "
          "a medicamentos, vacinas e outros produtos biológicos para uso "
          "humano, e pelo Diploma Ministerial n.º 3/2023, de 4 de Janeiro, "
          "que cria o próprio sistema {anarme2024}. Integra a autoridade "
          "reguladora, através do Centro Nacional de Farmacovigilância, a "
          "Comissão Nacional de Farmacovigilância, os fabricantes, as "
          "unidades de farmacovigilância e os responsáveis regionais, "
          "provinciais, distritais e das unidades sanitárias, os programas "
          "de saúde pública, os profissionais de saúde, as instituições de "
          "ensino da área da saúde, os titulares de autorização de "
          "introdução no mercado, as farmácias e postos de venda, os "
          "centros de investigação e os próprios doentes."),
        P("As obrigações dos profissionais de saúde estão enunciadas de "
          "forma directa: notificar de imediato todas as suspeitas de "
          "reacções adversas de que tenham conhecimento, informar os "
          "doentes da necessidade de comunicar acontecimentos adversos "
          "graves ou não descritos no folheto informativo, conservar a "
          "documentação clínica das suspeitas para permitir o seguimento, e "
          "cooperar com o sistema fornecendo a informação adicional que lhes "
          "seja pedida {anarme2024}. Aos responsáveis provinciais e "
          "distritais compete receber, classificar, processar e validar as "
          "notificações da sua área, informar o Centro Nacional das "
          "suspeitas graves no prazo máximo de quinze dias, introduzir os "
          "dados das fichas na base de dados no mesmo prazo, distribuir as "
          "fichas pelos profissionais e promover a notificação. O circuito "
          "está, portanto, definido; o que se desconhece é o grau em que os "
          "profissionais o conhecem e o utilizam."),
        P("A ficha de notificação exige quatro elementos mínimos para ser "
          "válida: um doente identificável, com iniciais, idade, sexo, peso "
          "e estado de gravidez; um notificador identificável, com nome, "
          "categoria profissional e contactos; a descrição da suspeita de "
          "reacção adversa, com data de início, gravidade, acção tomada e "
          "desfecho; e pelo menos um medicamento suspeito, com denominação "
          "genérica e comercial, dose, via, frequência, datas de início e "
          "fim, indicação, lote e validade {anarme2024}. O mesmo documento "
          "acrescenta duas garantias que interessam directamente a este "
          "protocolo: todas as notificações são tratadas com "
          "confidencialidade para proteger o notificador e o doente, e o "
          "notificador não é penalizado por notificar suspeitas de reacções "
          "adversas nem erros de medicação. Estas garantias são "
          "reproduzidas no questionário e na folha de informação ao "
          "participante, por serem a resposta institucional ao receio de "
          "consequências profissionais."),
        P("Moçambique aderiu ao Programa da OMS de Monitorização "
          "Internacional de Medicamentos em 2005 {umc2026}, o que significa "
          "que as notificações validadas alimentam a base de dados "
          "internacional gerida pelo centro colaborador da OMS. A utilidade "
          "dessa participação depende, porém, do fluxo de notificações "
          "gerado no país, e esse fluxo começa na unidade sanitária."),
    ]),
    ("Determinantes e barreiras da notificação pelos profissionais de saúde",
     [
        P("A literatura africana converge num padrão de três andares: "
          "consciência elevada da importância da notificação, conhecimento "
          "operacional insuficiente e prática baixa. Num hospital terciário "
          "da Etiópia, 58,3% dos profissionais tinham conhecimento fraco, "
          "59,9% tinham atitude positiva e apenas 32,1% tinham prática "
          "adequada {gidey2020}. Ao nível dos centros de saúde do mesmo "
          "país, 47% tinham conhecimento inadequado, 86,3% tinham atitude "
          "positiva e mais de metade não notificou as reacções que "
          "encontrou {seid2018}. Em unidades de cuidados primários da "
          "África do Sul, a atitude era adequada mas a frequência de "
          "notificação foi de 16,0%, com 60,5% dos inquiridos a declarar "
          "não saber como, onde ou quando notificar e 51,5% a referir que o "
          "seu nível de conhecimento clínico dificultava a decisão sobre se "
          "tinha ocorrido uma reacção adversa {haines2020}. Em centros de "
          "cuidados primários de Ibadan, na Nigéria, 72,5% dos "
          "profissionais tinham ouvido falar de farmacovigilância mas "
          "apenas 5,2% descreveram correctamente o conceito e somente 15,0% "
          "revelaram conhecimento adequado sobre reacções adversas "
          "{adisa2019}."),
        P("As barreiras específicas foram quantificadas com detalhe num "
          "hospital público sul-africano: não saber como notificar, 53,8%; "
          "falta de tempo, 37,1%; incerteza quanto ao resultado da "
          "notificação, 32,6%; carga de trabalho adicional, 22,0%; e falta "
          "de confiança para discutir reacções adversas com colegas, 22,0%. "
          "No mesmo estudo, apenas 18,9% sabiam que existia um sistema de "
          "farmacovigilância no hospital, 15,2% tinham a ficha disponível e "
          "18,9% sabiam a quem a entregar {terblanche2017}. Na Nigéria, "
          "entre os trabalhadores de unidades envolvidas na quimioprevenção "
          "sazonal da malária, 23% acreditavam que as reacções não eram "
          "notificadas por não serem graves nem ameaçadoras da vida e 11,6% "
          "referiram receio de responsabilização {rotimi2024}. No Gana, a "
          "indisponibilidade de fichas, com 30,3%, e a falta de formação, "
          "com 23,3%, foram as barreiras dominantes {fiagbey2026}. A "
          "avaliação do sistema de vigilância de reacções adversas de uma "
          "cidade do Zimbabué acrescenta uma barreira de outra natureza, a "
          "descrença na utilidade do sistema: 79% dos profissionais não o "
          "consideravam necessário e foi preenchida uma única ficha para as "
          "vinte reacções ocorridas no distrito {muringazuva2017}."),
        P("Os determinantes da prática são consistentes entre estudos. Na "
          "Etiópia, o conhecimento fraco, com odds ratio ajustado (ORa) de "
          "2,63 (IC95% 1,26 a 5,45), e a ausência de formação em "
          "notificação, com ORa de 7,31 (IC95% 3,42 a 15,62), "
          "associaram-se negativamente à prática de notificação "
          "{gidey2020}. Entre agentes de saúde comunitários nigerianos, a "
          "formação foi o único determinante da notificação, com ORa de "
          "3,63 (IC95% 1,13 a 11,63), num grupo em que 61,6% tinham "
          "encontrado doentes com reacções adversas mas apenas 12,6% as "
          "tinham notificado {adedeji2021}. Na Namíbia, a categoria de "
          "enfermagem associou-se a menor probabilidade de notificar, com "
          "ORa de 0,17 (IC95% 0,07 a 0,40) {adenuga2020}, e na Tanzânia a "
          "formação em farmacovigilância e a disponibilidade das fichas "
          "associaram-se de forma significativa à prática, com p inferior a "
          "0,001 {mssusa2025}. Estes achados sustentam a escolha das "
          "variáveis independentes deste protocolo."),
        P("A componente qualitativa dos estudos acrescenta um elemento que "
          "os inquéritos fechados tendem a perder: a ausência de retorno de "
          "informação. No Malawi, os profissionais formados preferiram o "
          "sistema em papel mas apontaram a falta de retorno, a "
          "indisponibilidade de fichas e o atraso na transmissão dos dados "
          "ao centro nacional como factores que desencorajam a notificação "
          "{chiumia2024}; entre farmacêuticos comunitários nigerianos, as "
          "estratégias sugeridas passaram pela simplificação do processo e "
          "pelo reconhecimento do notificador {nduka2024}. A desmotivação "
          "por ausência de retorno é, assim, uma barreira distinta do "
          "desconhecimento e merece item próprio no questionário."),
    ]),
    ("Intervenções para aumentar a notificação e o papel do farmacêutico", [
        P("A formação em serviço é a intervenção mais estudada e a que "
          "apresenta resultados mais imediatos. No Malawi, a pontuação "
          "média de conhecimento subiu de 56% (IC95% 53 a 58%) para 66% "
          "(IC95% 64 a 69%) após formação, com aumento de 2,8 vezes no "
          "número de participantes capazes de detectar uma reacção adversa "
          "e de 1,8 vezes na proporção que notificou as reacções detectadas "
          "{chiumia2024}. Em quatro países da África oriental, cursos "
          "curtos de farmacovigilância mostraram-se úteis para o "
          "desenvolvimento sustentado de conhecimento {van2024}. O estudo "
          "nigeriano de maior dimensão adverte, no entanto, que a formação "
          "isolada pode não bastar e propõe acompanhamento continuado dos "
          "profissionais como complemento {rotimi2024}."),
        P("A segunda via de intervenção actua sobre o circuito. A "
          "introdução de uma aplicação de notificação electrónica na "
          "Nigéria fez subir as notificações recebidas de 2.051 no período "
          "de referência para 18.995 no período seguinte, reduziu a "
          "notificação em papel de 98,4% para 15,7%, aumentou a notificação "
          "directa pelos consumidores de 2,7% para 17,6% e manteve "
          "qualidade elevada, com 97,3% das notificações submetidas pela "
          "aplicação a obterem pontuação de completude superior a 70% "
          "{elemuwa2024}. A sensibilização dirigida à comunidade também "
          "produziu aumento da notificação pelos doentes em meio rural no "
          "Uganda {ndagije2019}, e em contexto sul-africano verificou-se "
          "que as ferramentas de notificação dirigidas ao público "
          "permanecem pouco conhecidas, com apenas 17,3% dos adultos "
          "inquiridos a conhecerem a aplicação disponível {ncube2025}."),
        P("Ao farmacêutico cabe um papel específico neste conjunto. Nos "
          "estudos em que a categoria profissional foi analisada, os "
          "farmacêuticos obtiveram as pontuações mais altas em práticas "
          "preferenciais de notificação {haines2020} e a formação de base "
          "em farmacologia coloca-os em posição de apoiar a avaliação "
          "preliminar da causalidade e o preenchimento correcto da ficha. "
          "As revisões dos estudos etíopes concluem de forma convergente "
          "que a fraqueza do sistema é sobretudo de conhecimento "
          "operacional e não de vontade {anbeo2023,hailu2020}, o que coloca "
          "a formação e a organização do circuito, e não a coerção, no "
          "centro das respostas possíveis."),
    ]),
    ("Medida de conhecimentos, atitudes e práticas: instrumentos, validação "
     "e pontos de corte", [
        P("O modelo de conhecimentos, atitudes e práticas assume que o "
          "comportamento depende do saber e da disposição favorável, sem os "
          "reduzir um ao outro. A sua aplicação em farmacovigilância está "
          "consolidada, com inquéritos comparáveis em vários países "
          "africanos {gidey2020,haines2020,adenuga2020,fiagbey2026}, mas a "
          "comparabilidade é limitada pela heterogeneidade dos instrumentos "
          "e dos pontos de corte, problema que a lista de verificação para "
          "o relato de estudos de conhecimentos, atitudes e práticas "
          "(ChecKAP) procura corrigir ao normalizar a descrição do "
          "instrumento, da pontuação e dos pontos de corte {zarei2024}."),
        P("Existem instrumentos publicados com propriedades psicométricas "
          "descritas. O questionário universal de conhecimentos e atitudes "
          "em farmacovigilância foi desenvolvido e validado para "
          "profissionais e estudantes das ciências da saúde "
          "{zivanovic2022}, e os inquéritos africanos de maior dimensão "
          "usaram instrumentos pré-testados, como o questionário de 45 "
          "itens aplicado na Nigéria {rotimi2024} ou o instrumento com alfa "
          "de Cronbach de 0,72 usado no Gana {powell2023}. Nenhum destes "
          "instrumentos está adaptado ao circuito moçambicano, o que obriga "
          "a uma adaptação com validação de conteúdo antes da aplicação."),
        P("A validação de conteúdo por painel de peritos, com cálculo do "
          "índice de validade de conteúdo (IVC) de cada item e do conjunto, "
          "é o procedimento aceite para essa adaptação, exigindo-se "
          "habitualmente 0,80 ou mais por item {almanasreh2019}. A "
          "consistência interna mede-se com a fórmula 20 de "
          "Kuder-Richardson (KR-20) nos itens dicotómicos de conhecimento e "
          "com o alfa de Cronbach na escala ordinal de atitude, sendo 0,70 "
          "o limiar convencional de aceitação."),
        P("A classificação dos resultados em níveis segue os pontos de "
          "corte de Bloom, usados em inquéritos deste tipo em África, que "
          "classificam como bom o desempenho igual ou superior a 80% da "
          "pontuação máxima, como moderado o desempenho entre 60 e 79% e "
          "como fraco o desempenho inferior a 60% {juttla2024}. A adopção "
          "destes pontos de corte permite comparar directamente os "
          "resultados com os de estudos que os utilizaram e evita a "
          "definição arbitrária de limiares depois de conhecidos os dados. "
          "Os mesmos valores são aplicados às três dimensões e reproduzidos "
          "sem alteração no quadro de variáveis."),
    ]),
]

# ----------------------------------------------------- 7. estado da arte ----
ESTADO_ARTE = [
    P("O [[quadro:estado_arte]] reúne quinze estudos empíricos publicados "
      "entre 2017 e 2026 sobre conhecimentos, atitudes e práticas de "
      "notificação de reacções adversas entre profissionais de saúde, "
      "privilegiando a evidência africana por ser a que mais se aproxima do "
      "contexto moçambicano em termos de organização dos serviços e de "
      "disponibilidade de recursos."),
    QUADRO("estado_arte",
           "Síntese de estudos sobre conhecimentos, atitudes e práticas de "
           "notificação de reacções adversas entre profissionais de saúde "
           "(estado da arte)",
           ["Autor (ano)", "Local", "Desenho (n)", "Principais resultados"],
           [["Terblanche et al. (2017) {terblanche2017}", "África do Sul, "
             "hospital público", "Transversal (132)",
             "96,2% consideram a notificação necessária, mas só 18,9% sabiam "
             "que existia sistema no hospital, 15,2% tinham a ficha e 18,9% "
             "sabiam a quem entregá-la; barreiras: não saber notificar "
             "53,8%, falta de tempo 37,1%, incerteza sobre o resultado "
             "32,6%."],
            ["Muringazuva et al. (2017) {muringazuva2017}", "Zimbabué, "
             "cidade de Kadoma", "Avaliação de sistema, transversal (6 "
             "unidades sanitárias)",
             "43% conheciam pelo menos dois objectivos do sistema e 83% "
             "declararam disponibilidade para participar, mas 79% não "
             "consideravam o sistema necessário; foi preenchida uma única "
             "ficha para 20 reacções ocorridas no distrito."],
            ["Seid et al. (2018) {seid2018}", "Etiópia, centros de saúde de "
             "Gondar", "Transversal (102)",
             "47% com conhecimento inadequado e 86,3% com atitude positiva; "
             "51% não notificaram a reacção que encontraram; ausência de "
             "formação associada a conhecimento inadequado (p=0,037)."],
            ["Adisa e Omitogun (2019) {adisa2019}", "Nigéria, dez centros de "
             "cuidados primários de Ibadan", "Transversal (80 profissionais "
             "e 360 utentes)",
             "72,5% tinham ouvido falar de farmacovigilância mas só 5,2% "
             "definiram correctamente o conceito; 15,0% com conhecimento "
             "adequado, 46,2% com atitude positiva e 37,5% tinham visto a "
             "ficha de notificação."],
            ["Gidey et al. (2020) {gidey2020}", "Etiópia, hospital terciário "
             "do Tigray", "Transversal (307; resposta 84,8%)",
             "58,3% com conhecimento fraco, 59,9% com atitude positiva e "
             "32,1% com prática adequada; conhecimento fraco e ausência de "
             "formação associados a pior prática."],
            ["Haines et al. (2020) {haines2020}", "África do Sul, distrito "
             "de Tshwane, cuidados primários", "Transversal (200; resposta "
             "91,7%)",
             "Notificação efectiva de 16,0%; 60,5% não sabiam como, onde ou "
             "quando notificar; 97,5% afirmam que deveriam notificar e mais "
             "de 70% defendem notificação obrigatória."],
            ["Adenuga et al. (2020) {adenuga2020}", "Namíbia, sector "
             "público", "Transversal (197)",
             "63,4% conheciam o sistema nacional de notificação e 37,3% "
             "já tinham notificado; pertencer à enfermagem associou-se a "
             "menor notificação, com odds ratio ajustado de 0,17."],
            ["Hailu e Mohammed (2020) {hailu2020}", "Etiópia, revisão "
             "sistemática", "13 estudos",
             "Conhecimento médio de 41,50% e atitude média de 57,18%; "
             "46,93% encontraram reacções adversas e 41,8% notificaram nos "
             "últimos doze meses; 34,15% não sabem como notificar."],
            ["Adedeji et al. (2021) {adedeji2021}", "Nigéria, agentes de "
             "saúde comunitários do sudoeste", "Transversal (333)",
             "61,6% tinham encontrado doentes com reacções adversas mas só "
             "12,6% as notificaram na ficha; 57,4% com conhecimento "
             "inadequado; a formação foi o único determinante da "
             "notificação."],
            ["Powell et al. (2023) {powell2023}", "Gana, hospital "
             "universitário de Cape Coast", "Transversal (107 médicos e "
             "enfermeiros)",
             "82,3% reconhecem a notificação como responsabilidade própria, "
             "mas o conhecimento foi inadequado em 66,7% dos itens; "
             "prevalência de notificação de 7,5%; 80,4% atribuem a "
             "subnotificação à falta de formação."],
            ["Rotimi et al. (2024) {rotimi2024}", "Nigéria, nove estados, "
             "campanha de quimioprevenção da malária", "Transversal (2.144)",
             "95,0% com boa consciencialização e 72,2% com boa atitude, mas "
             "só 37,7% com bom conhecimento; 23% justificam a não "
             "notificação por as reacções não serem graves e 11,6% referem "
             "receio de responsabilização."],
            ["Chiumia et al. (2024) {chiumia2024}", "Malawi, âmbito "
             "nacional", "Transversal de métodos mistos, antes e depois de "
             "formação",
             "Conhecimento médio subiu de 56% para 66% (p<0,001), com "
             "aumento de 2,8 vezes na detecção e de 1,8 vezes na "
             "notificação; apontadas a falta de retorno, a "
             "indisponibilidade de fichas e o atraso na transmissão."],
            ["Hamid e Osman (2025) {hamid2025}", "Sudão, hospital "
             "universitário de Atbara", "Transversal (122)",
             "Conhecimento moderado, com média de 5,1 em 12; 23,8% "
             "conheciam o programa nacional; 66,4% observaram uma reacção "
             "adversa mas só 18,9% a notificaram."],
            ["Issak et al. (2025) {issak2025}", "Sudão, Dongola",
             "Transversal (216; resposta 79,4%)",
             "Conhecimento fraco sobre notificação de reacções adversas "
             "(35,2%), atitude positiva (81,9%) e prática baixa (29,6%); "
             "barreira principal a falta de conhecimento (28,9%)."],
            ["Mssusa et al. (2025) {mssusa2025}", "Tanzânia, cinco regiões",
             "Transversal multicêntrico (380)",
             "65,8% com pontuação baixa em conhecimento de "
             "farmacovigilância e 86,8% com atitude favorável, mas apenas "
             "22,9% notificaram à autoridade reguladora; formação e "
             "disponibilidade de fichas associadas à prática (p<0,001)."],
            ["Fiagbey et al. (2026) {fiagbey2026}", "Gana, região de "
             "Ashanti", "Transversal (326)",
             "93,6% conheciam a farmacovigilância e 85,6% reconheciam a "
             "obrigação de notificar, mas só 49,4% conheciam o centro "
             "nacional e 50% tinham submetido fichas completas; barreiras: "
             "indisponibilidade de fichas 30,3% e falta de formação "
             "23,3%."]],
           larguras=[3.3, 2.6, 2.7, 7.4],
           fonte="Elaboração própria (2026), a partir das fontes citadas."),
    P("A leitura do quadro revela um padrão que se repete em contextos "
      "muito diferentes quanto ao rendimento nacional e à maturidade "
      "regulamentar: a atitude favorável é quase universal, situando-se "
      "entre 46,2% e 86,8%, ao passo que a notificação efectiva raramente "
      "ultrapassa um terço dos profissionais e desce a 7,5% num hospital "
      "universitário ganês {powell2023} e a 12,6% entre agentes "
      "comunitários nigerianos {adedeji2021}. O elo em falta não é a "
      "vontade mas o conhecimento operacional, isto é, saber que a ficha "
      "existe, onde a obter, como preenchê-la e a quem entregá-la; as "
      "revisões sistemáticas etíopes chegam à mesma conclusão e "
      "acrescentam que os farmacêuticos tendem a apresentar melhores "
      "resultados nas três dimensões do que as restantes categorias "
      "{hailu2020,anbeo2023}."),
    P("Existem, contudo, divergências que justificam a medição local. A "
      "proporção com bom conhecimento varia entre 15,0% {adisa2019} e 37,7% "
      "{rotimi2024}, e a prática entre 7,5% {powell2023} e 41,8% "
      "{hailu2020}, amplitude que não se explica apenas pela composição "
      "profissional das amostras e que reflecte também a heterogeneidade "
      "dos instrumentos e dos pontos de corte, problema que a "
      "normalização do relato procura atenuar {zarei2024}. A hierarquia "
      "das barreiras também não é estável: predomina o desconhecimento do "
      "procedimento na África do Sul {terblanche2017}, a indisponibilidade "
      "de fichas no Gana {fiagbey2026} e a percepção de inutilidade no "
      "Zimbabué {muringazuva2017}. Nenhum destes estudos foi conduzido em "
      "Moçambique, país que só em 2023 aprovou o regulamento que cria o "
      "seu sistema nacional e em 2024 o manual de boas práticas "
      "{anarme2024}. A lacuna que este estudo preenche é, portanto, dupla: "
      "produzir a primeira medida moçambicana destas três dimensões e "
      "identificar qual das barreiras conhecidas predomina num contexto "
      "cujo enquadramento normativo é recente."),
]
ESQUEMA_TEXTO = [
    P("A [[figura:esquema]] representa o modelo que orienta a análise. "
      "Quatro blocos de variáveis independentes, individuais, de formação e "
      "informação, organizacionais e atitudinais, convergem para o "
      "desfecho, a notificação efectiva de suspeitas de reacções adversas "
      "nos doze meses anteriores. O nível da unidade sanitária e o sector "
      "de trabalho entram como variáveis de confundimento, por "
      "determinarem simultaneamente a exposição a reacções adversas e o "
      "acesso a fichas e a formação. O modelo assume que o conhecimento "
      "opera sobretudo como condição necessária e a atitude como condição "
      "facilitadora, sendo os factores organizacionais os que traduzem, ou "
      "bloqueiam, a intenção em comportamento."),
]
ESQUEMA_TITULO = ("Esquema conceptual dos determinantes da notificação de "
                  "suspeitas de reacções adversas")
ESQUEMA = {
    "contexto": ("Unidades sanitárias públicas da cidade de Nampula, "
                 "profissionais de saúde, 2027"),
    "blocos": [
        ("Factores individuais", ["idade", "sexo", "categoria profissional",
                                  "tempo de exercício"]),
        ("Formação e informação", ["formação prévia em farmacovigilância",
                                   "conhecimento do conceito de reacção "
                                   "adversa",
                                   "conhecimento da ficha e do circuito"]),
        ("Factores organizacionais", ["disponibilidade da ficha",
                                      "ponto focal na unidade sanitária",
                                      "retorno de informação",
                                      "carga de trabalho"]),
        ("Atitudes e percepções", ["utilidade percebida da notificação",
                                   "receio de consequências profissionais",
                                   "dúvida sobre a causalidade"]),
    ],
    "desfecho": ("Notificação efectiva de suspeitas de reacções adversas nos "
                 "doze meses anteriores", ["notificou", "não notificou"]),
    "moderadores": ("Variáveis de confundimento",
                    ["nível da unidade sanitária", "sector de trabalho",
                     "participação em programas verticais de saúde"]),
}

# ----------------------------------------------------- 8. metodologia -------
METODOLOGIA = [
    ("Tipo e desenho do estudo", [
        P("Trata-se de um estudo observacional, descritivo e analítico, de "
          "corte transversal e abordagem quantitativa, conduzido sob a forma "
          "de inquérito de conhecimentos, atitudes e práticas com "
          "questionário auto-administrado. O desenho transversal é "
          "adequado porque o objectivo é estimar proporções num momento "
          "definido e examinar associações entre características dos "
          "profissionais e a notificação já ocorrida, sem qualquer "
          "intervenção sobre os participantes nem seguimento no tempo."),
        P("O relato seguirá a lista de verificação para estudos de "
          "conhecimentos, atitudes e práticas, que normaliza a descrição do "
          "instrumento, da pontuação, dos pontos de corte e da "
          "interpretação dos resultados {zarei2024}, complementada pela "
          "norma Strengthening the Reporting of Observational Studies in "
          "Epidemiology (STROBE) na parte comum aos estudos observacionais "
          "transversais {von2008}. A natureza transversal implica que as "
          "associações identificadas não permitem inferência causal, "
          "limitação assumida na interpretação e na redacção das "
          "conclusões."),
    ]),
    ("Local e período do estudo", [
        P("O estudo decorre nas unidades sanitárias públicas da cidade de "
          "Nampula, província de Nampula, no norte de Moçambique. A cidade "
          "concentra o hospital de referência provincial e a rede de "
          "centros de saúde urbanos, e é o ponto do território provincial "
          "onde a densidade de profissionais e de serviços diferenciados é "
          "maior, padrão documentado para outras áreas clínicas na mesma "
          "província {sengo2023}. Esta concentração torna a cidade o local "
          "onde a notificação espontânea teria, em princípio, as melhores "
          "condições para ocorrer, e por isso o local mais informativo para "
          "uma primeira medição nacional."),
        P("A lista definitiva das unidades sanitárias, o seu nível de "
          "atendimento e o número de profissionais afectos a cada uma serão "
          "obtidos junto do SDSMAS da Cidade de Nampula na fase de "
          "preparação [confirmar a lista das unidades sanitárias e os "
          "efectivos por categoria junto do SDSMAS da Cidade de Nampula]. O "
          "protocolo é elaborado em 2026; a recolha de dados decorre entre "
          "Março e Maio de 2027, depois da aprovação pelo comité de "
          "bioética e da emissão das autorizações institucionais, e a "
          "análise e redacção entre Junho e Setembro de 2027."),
    ]),
    ("População de estudo e unidade de análise", [
        P("A população de estudo é constituída pelos profissionais de saúde "
          "em exercício nas unidades sanitárias públicas da cidade de "
          "Nampula que prescrevem, dispensam ou administram medicamentos, "
          "agrupados em três estratos: médicos e técnicos de medicina; "
          "enfermeiros de todos os níveis, incluindo enfermagem de saúde "
          "materno-infantil; e técnicos e agentes de farmácia. Estas são as "
          "categorias que o quadro normativo nacional identifica como "
          "responsáveis pela notificação de suspeitas de reacções adversas "
          "{anarme2024} e são também as categorias comparadas na literatura "
          "africana {gidey2020,haines2020,adenuga2020}."),
        P("A unidade de análise é o profissional de saúde. Cada profissional "
          "responde uma única vez, independentemente do número de serviços "
          "em que trabalhe dentro da mesma unidade sanitária. Os "
          "profissionais que acumulam funções em mais do que uma unidade "
          "sanitária pública da cidade são inquiridos na unidade onde "
          "cumprem o maior número de horas semanais, informação registada "
          "no questionário e usada para eliminar duplicações durante a "
          "verificação dos dados."),
    ]),
    ("Amostra e cálculo do tamanho da amostra", [
        P("O efectivo total de profissionais elegíveis na cidade de Nampula "
          "não é conhecido à data de elaboração do protocolo. Adopta-se, "
          "por isso, uma regra de decisão escrita: se o efectivo confirmado "
          "junto do SDSMAS da Cidade de Nampula for igual ou inferior ao "
          "tamanho mínimo calculado para população infinita, realiza-se um "
          "recenseamento, convidando todos os profissionais elegíveis; se "
          "for superior, selecciona-se uma amostra probabilística "
          "estratificada por categoria profissional, com afectação "
          "proporcional ao peso de cada estrato."),
        P("O tamanho mínimo para estimar uma proporção em população infinita "
          "obtém-se pela fórmula seguinte."),
        FORMULA("n<sub>0</sub> = Z<sup>2</sup> × p × (1 - p) / "
                "d<sup>2</sup>"),
        P("Em que n<sub>0</sub> é o tamanho mínimo, Z é o valor da "
          "distribuição normal padrão correspondente ao nível de confiança "
          "de 95%, isto é 1,96; p é a proporção esperada do desfecho "
          "principal; e d é a margem de erro absoluta admitida, fixada em "
          "5%. Adopta-se p igual a 0,50 porque as estimativas publicadas "
          "para a proporção de profissionais com bom conhecimento variam "
          "entre 15,0% {adisa2019} e 37,7% {rotimi2024} e as de notificação "
          "efectiva entre 7,5% {powell2023} e 41,8% {hailu2020}, sem que "
          "exista qualquer estimativa moçambicana que permita escolher "
          "entre elas; o valor de 0,50 maximiza a variância e garante um "
          "tamanho suficiente qualquer que seja a proporção observada. A "
          "substituição dá n<sub>0</sub> igual a 1,96<sup>2</sup> "
          "× 0,50 × 0,50 / 0,05<sup>2</sup>, ou seja 384,16, que "
          "se arredonda por excesso para 385 profissionais."),
        P("Se o efectivo confirmado for igual ou inferior a 385, o estudo "
          "passa a recenseamento e não há amostragem. Se for superior, "
          "aplica-se a correcção para população finita, n = n<sub>0</sub> / "
          "[1 + (n<sub>0</sub> - 1) / N], seguida de um acréscimo para 10% "
          "de não resposta, percentagem escolhida por ser superior à perda "
          "observada em inquéritos comparáveis, que registaram taxas de "
          "resposta de 84,8% {gidey2020}, 91,7% {haines2020} e 79,4% "
          "{issak2025}. A [[tabela:cenarios]] apresenta os tamanhos "
          "resultantes para efectivos plausíveis."),
        TABELA("cenarios",
               "Tamanho da amostra por cenário de efectivo total de "
               "profissionais elegíveis",
               ["Efectivo total (N)", "Amostra corrigida",
                "Amostra a convidar (com 10% de não resposta)",
                "Fracção de amostragem"],
               [["400", "197", "219", "54,8%"],
                ["500", "218", "243", "48,6%"],
                ["600", "235", "262", "43,7%"],
                ["800", "261", "290", "36,3%"],
                ["1.000", "279", "310", "31,0%"],
                ["1.200", "292", "325", "27,1%"]],
               larguras=[3.4, 3.2, 5.4, 3.4],
               fonte="Elaboração própria (2026).",
               nota="Cálculo a partir de n<sub>0</sub> igual a 385, com "
                    "correcção para população finita e acréscimo para 10% "
                    "de não resposta. Se o efectivo confirmado for igual ou "
                    "inferior a 385, realiza-se recenseamento."),
        P("Dentro de cada estrato, os participantes são seleccionados por "
          "amostragem aleatória simples a partir da lista nominal de "
          "profissionais fornecida pelo SDSMAS da Cidade de Nampula, usando "
          "números aleatórios gerados por computador. A lista serve apenas "
          "para a selecção e para o controlo de duplicações e é destruída "
          "após a recolha; não é transportada para a base de dados de "
          "análise. Como a amostragem é aleatória simples dentro de "
          "estratos e não por conglomerados, não se aplica efeito de "
          "desenho."),
        P("O tamanho necessário para o objectivo analítico foi calculado à "
          "parte, pela fórmula de comparação de duas proporções "
          "independentes, com nível de significância de 5% bilateral e "
          "poder de 80%. Admitindo uma notificação efectiva de 45% entre os "
          "profissionais com nível bom ou moderado de conhecimento e de 28% "
          "entre os de nível fraco, diferença compatível com as razões de "
          "possibilidades publicadas {gidey2020,adedeji2021}, obtêm-se 125 "
          "profissionais por grupo, isto é 250 no total, ou 278 com "
          "acréscimo de 10% para não resposta. Os tamanhos da "
          "[[tabela:cenarios]] satisfazem este requisito a partir de um "
          "efectivo de 600 profissionais; para efectivos menores, o poder "
          "para detectar diferenças desta ordem fica abaixo de 80% e essa "
          "limitação será declarada nos resultados."),
        P("Para a regressão logística aplica-se a regra de pelo menos dez "
          "acontecimentos por variável independente. Com uma proporção "
          "esperada de notificação efectiva entre 20% e 30% e uma amostra "
          "de 262 a 325 participantes, esperam-se entre 52 e 98 "
          "acontecimentos, o que permite um modelo final com cinco a oito "
          "variáveis independentes. O modelo será limitado a esse número, "
          "com selecção prévia das candidatas na análise bivariável."),
    ]),
    ("Critérios de inclusão e de exclusão", [
        H3("Critérios de inclusão"),
        LISTA([
            "Ser médico, técnico de medicina, enfermeiro de qualquer nível, "
            "técnico de farmácia ou agente de farmácia;",
            "Exercer funções numa unidade sanitária pública da cidade de "
            "Nampula durante o período de recolha;",
            "Ter pelo menos seis meses completos de exercício na unidade "
            "sanitária, tempo mínimo para ter tido oportunidade de observar "
            "e de notificar uma reacção adversa;",
            "Aceitar participar e assinar o termo de consentimento livre e "
            "esclarecido.",
        ]),
        H3("Critérios de exclusão"),
        LISTA([
            "Profissionais em férias, em licença ou em formação fora da "
            "unidade sanitária durante todo o período de recolha, após duas "
            "tentativas de contacto;",
            "Estudantes em estágio, internos e voluntários sem vínculo "
            "laboral com a unidade sanitária;",
            "Profissionais afectos exclusivamente a funções "
            "administrativas, laboratoriais ou de apoio, sem contacto "
            "directo com a prescrição, a dispensa ou a administração de "
            "medicamentos;",
            "Profissionais que participaram no painel de peritos ou no "
            "pré-teste do instrumento;",
            "Questionários devolvidos com menos de 80% dos itens "
            "respondidos em qualquer uma das três dimensões.",
        ]),
    ]),
    ("Variáveis e definições operacionais", [
        P("O [[quadro:variaveis]] apresenta as variáveis do estudo, o seu "
          "tipo, a definição operacional com as respectivas categorias e o "
          "objectivo específico a que cada uma responde. Os pontos de corte "
          "indicados são os mesmos que constam da secção de análise e do "
          "questionário, sem qualquer variação."),
        QUADRO("variaveis",
               "Variáveis do estudo, definições operacionais e objectivos",
               ["Variável", "Tipo", "Definição operacional e categorias",
                "Objectivo"],
               [["Idade", "Independente, quantitativa discreta",
                 "Anos completos à data do inquérito; categorizada em 30 ou "
                 "menos, 31 a 40 e mais de 40 anos", "1"],
                ["Sexo", "Independente, qualitativa nominal",
                 "Masculino; feminino", "1"],
                ["Categoria profissional", "Independente, qualitativa "
                 "nominal",
                 "Médico ou técnico de medicina; enfermeiro; técnico ou "
                 "agente de farmácia", "1, 5"],
                ["Tempo de exercício profissional",
                 "Independente, quantitativa discreta",
                 "Anos completos desde o início do exercício da profissão; "
                 "categorizado em menos de 5, 5 a 9 e 10 ou mais anos",
                 "1, 5"],
                ["Nível da unidade sanitária",
                 "Independente e de confundimento, qualitativa nominal",
                 "Hospital de referência; centro de saúde urbano", "1"],
                ["Sector de trabalho",
                 "Independente e de confundimento, qualitativa nominal",
                 "Consulta externa; internamento; urgência; farmácia; "
                 "programas verticais de tuberculose, infecção por vírus da "
                 "imunodeficiência humana ou saúde materno-infantil", "1"],
                ["Formação prévia em farmacovigilância",
                 "Independente, qualitativa nominal",
                 "Participação em pelo menos uma acção formal de formação "
                 "(curso, seminário, sessão de actualização) sobre "
                 "farmacovigilância ou notificação de reacções adversas "
                 "desde o início do exercício: sim; não", "1, 5"],
                ["Pontuação de conhecimento",
                 "Independente, quantitativa discreta",
                 "Soma de 20 itens de resposta fechada sobre conceito de "
                 "reacção adversa, gravidade, critérios mínimos de "
                 "notificação, ficha e circuito nacional; um ponto por "
                 "resposta correcta, zero por resposta incorrecta ou por "
                 "«não sei»; amplitude de 0 a 20", "2, 5"],
                ["Nível de conhecimento",
                 "Independente, qualitativa ordinal",
                 "Pontos de corte de Bloom sobre a pontuação de "
                 "conhecimento: bom, 16 ou mais (80% ou mais); moderado, 12 "
                 "a 15 (60 a 79%); fraco, menos de 12 (menos de 60%)",
                 "2, 5"],
                ["Pontuação de atitude",
                 "Independente, quantitativa discreta",
                 "Soma de 10 afirmações numa escala ordinal de cinco "
                 "pontos, de discordo totalmente a concordo totalmente, com "
                 "inversão dos itens formulados pela negativa; amplitude de "
                 "10 a 50", "3, 5"],
                ["Nível de atitude", "Independente, qualitativa ordinal",
                 "Favorável, 40 ou mais (80% ou mais); neutra, 30 a 39 (60 "
                 "a 79%); desfavorável, menos de 30 (menos de 60%)",
                 "3, 5"],
                ["Pontuação de prática",
                 "Dependente secundária, quantitativa discreta",
                 "Soma de 10 itens sobre comportamentos de "
                 "farmacovigilância no último ano; um ponto por "
                 "comportamento realizado; amplitude de 0 a 10", "3"],
                ["Nível de prática", "Dependente secundária, qualitativa "
                 "ordinal",
                 "Boa, 8 ou mais (80% ou mais); moderada, 6 a 7 (60 a 79%); "
                 "fraca, 5 ou menos (menos de 60%)", "3"],
                ["Notificação efectiva",
                 "Dependente principal, qualitativa dicotómica",
                 "Ter preenchido e entregue pelo menos uma ficha oficial de "
                 "notificação de suspeita de reacção adversa nos doze meses "
                 "anteriores ao inquérito: sim; não", "3, 5"],
                ["Barreiras percebidas à notificação",
                 "Independente, qualitativa nominal de resposta múltipla",
                 "Doze barreiras pré-definidas, cada uma classificada numa "
                 "escala ordinal de cinco pontos quanto à importância "
                 "atribuída, com espaço para barreiras não listadas", "4"],
                ["Disponibilidade da ficha no local de trabalho",
                 "Independente, qualitativa nominal",
                 "Existência de fichas de notificação acessíveis no serviço "
                 "onde trabalha: sim; não; não sabe", "4, 5"],
                ["Existência de ponto focal de farmacovigilância",
                 "Independente, qualitativa nominal",
                 "Conhecimento de um responsável identificado pela "
                 "farmacovigilância na unidade sanitária: sim; não; não "
                 "sabe", "4"],
                ["Retorno de informação sobre notificações",
                 "Independente, qualitativa nominal",
                 "Ter alguma vez recebido informação de retorno sobre uma "
                 "notificação submetida, pela unidade sanitária ou pelo "
                 "nível superior: sim; não; nunca notificou", "4"]],
               larguras=[3.4, 2.9, 7.6, 1.8]),
    ]),
    ("Instrumento de recolha de dados, adaptação e validação", [
        P("O instrumento é um questionário estruturado, auto-administrado, "
          "em português, organizado em cinco secções: caracterização "
          "sociodemográfica e profissional, com oito perguntas; "
          "conhecimentos, com vinte itens de resposta fechada; atitudes, "
          "com dez afirmações numa escala ordinal de cinco pontos; "
          "práticas, com dez itens; e barreiras percebidas, com doze itens "
          "classificados quanto à importância e uma pergunta aberta de "
          "sugestões. O questionário completo consta do primeiro apêndice."),
        P("Os itens são adaptados de instrumentos publicados e não "
          "reproduzem nenhuma escala proprietária. A base conceptual e a "
          "formulação das dimensões de conhecimento e de atitude seguem o "
          "questionário universal de farmacovigilância desenvolvido e "
          "validado para profissionais e estudantes das ciências da saúde "
          "{zivanovic2022}; os itens de prática e de barreiras são "
          "adaptados dos inquéritos aplicados na África do Sul "
          "{terblanche2017,haines2020}, na Etiópia {gidey2020} e na Nigéria "
          "{rotimi2024}, em todos os casos com reformulação para "
          "corresponder à ficha e ao circuito moçambicanos. Os itens de "
          "conhecimento relativos à definição de reacção adversa, à "
          "definição de reacção adversa grave, aos critérios mínimos de uma "
          "notificação válida, aos prazos e às responsabilidades são "
          "construídos directamente a partir do manual nacional de boas "
          "práticas {anarme2024}, que constitui a referência de correcção "
          "das respostas."),
        P("A validade de conteúdo é estabelecida por um painel de seis "
          "peritos: dois farmacêuticos com experiência hospitalar, o "
          "responsável provincial de farmacovigilância, um médico "
          "clínico, um enfermeiro com funções de supervisão e um docente "
          "com experiência em metodologia de investigação. Cada perito "
          "classifica a relevância de cada item numa escala de quatro "
          "pontos, calculando-se o IVC de cada item e do conjunto "
          "{almanasreh2019}. Os itens com índice inferior a 0,80 são "
          "reformulados ou eliminados e o índice médio da escala deve "
          "atingir pelo menos 0,90 antes da aplicação."),
        P("Segue-se um pré-teste em cerca de 10% do tamanho previsto, isto "
          "é 28 profissionais de uma unidade sanitária pública fora da "
          "cidade de Nampula e portanto fora da amostra final [confirmar a "
          "unidade sanitária do distrito vizinho junto da DPS de Nampula]. "
          "O pré-teste verifica a compreensão das perguntas, o tempo de "
          "preenchimento, previsto em 15 a 20 minutos, e a taxa de itens "
          "não respondidos. A consistência interna é estimada nos dados do "
          "pré-teste e recalculada na amostra final: pela fórmula KR-20 nos "
          "vinte itens dicotómicos de conhecimento e pelo alfa de Cronbach "
          "na escala de atitude, exigindo-se 0,70 em ambos. A estabilidade "
          "temporal é avaliada por reaplicação a vinte participantes do "
          "pré-teste catorze dias depois, com coeficiente kappa de Cohen "
          "por item e coeficiente de correlação intraclasse para as "
          "pontuações, aceitando-se valores iguais ou superiores a 0,70."),
        P("O questionário é aplicado em português, língua de formação e de "
          "trabalho de todas as categorias abrangidas, pelo que não se "
          "justifica tradução para emakhuwa; a folha de informação ao "
          "participante é, ainda assim, explicada oralmente sempre que o "
          "participante o solicite. A fonte de dados é exclusivamente a "
          "resposta do profissional; não são consultados processos "
          "clínicos, registos de pessoal nem arquivos de fichas de "
          "notificação, o que preserva o anonimato e dispensa qualquer "
          "ligação entre respostas e identidade."),
    ]),
    ("Procedimentos de recolha de dados e controlo de qualidade", [
        P("A recolha é conduzida pelo investigador e por dois auxiliares de "
          "investigação com formação superior em saúde, previamente "
          "treinados durante dois dias sobre os objectivos do estudo, o "
          "conteúdo do questionário, o procedimento de consentimento e as "
          "regras de confidencialidade. O treino inclui um exercício de "
          "aplicação simulada e a padronização das respostas às dúvidas "
          "mais prováveis, para evitar que explicações diferentes "
          "introduzam variação nas respostas."),
        P("Em cada unidade sanitária, a direcção é informada por escrito e é "
          "acordado um calendário que não interfira com o atendimento. O "
          "questionário é entregue em mão, acompanhado da folha de "
          "informação e do termo de consentimento, e é preenchido sem a "
          "presença do investigador, para reduzir o efeito de desejabilidade "
          "social. O participante coloca o questionário preenchido num "
          "envelope não identificado e deposita-o numa urna selada colocada "
          "num local reservado do serviço; o termo de consentimento "
          "assinado é depositado em urna separada, de modo que nunca seja "
          "possível associar uma assinatura a um questionário. As urnas são "
          "recolhidas pelo investigador ao fim de cinco dias úteis, com uma "
          "segunda passagem para os profissionais ausentes na primeira."),
        P("Cada questionário recebe um código sequencial atribuído no "
          "momento da entrega, sem qualquer elemento identificador do "
          "participante. No fim de cada dia, o investigador verifica a "
          "completude dos questionários recolhidos e regista o número de "
          "convites, de recusas e de devoluções, para cálculo da taxa de "
          "resposta exigida pela norma de relato {zarei2024}. Os "
          "questionários com menos de 80% dos itens respondidos numa "
          "dimensão são excluídos do cálculo da pontuação dessa dimensão, "
          "regra fixada antes do início da recolha."),
        P("Os dados são introduzidos numa base construída de raiz, com "
          "regras de validação por campo, limites de amplitude e listas "
          "fechadas, de modo a impedir valores impossíveis. Dez por cento "
          "dos questionários, seleccionados aleatoriamente, são "
          "reintroduzidos por um segundo operador e comparados "
          "automaticamente; discrepâncias acima de 1% obrigam à "
          "reintrodução completa do lote correspondente. A chave de "
          "correcção dos itens de conhecimento é fixada por escrito antes "
          "do início da recolha, a partir do manual nacional {anarme2024}, "
          "e não é alterada depois de conhecidos os dados."),
    ]),
    ("Processamento e análise dos dados", [
        P("A análise é feita no Statistical Package for the Social Sciences "
          "(SPSS), versão 26 ou superior, ou, em alternativa, no R, de "
          "acesso livre. As variáveis qualitativas são descritas por "
          "frequências absolutas e relativas e as quantitativas por média e "
          "desvio-padrão quando a distribuição for simétrica, ou por "
          "mediana e amplitude interquartil quando não o for, avaliando-se "
          "a normalidade pelo teste de Shapiro-Wilk e pela inspecção "
          "gráfica."),
        P("O primeiro objectivo específico é respondido pela descrição do "
          "perfil dos participantes. O segundo e o terceiro produzem "
          "proporções de profissionais em cada nível de conhecimento, de "
          "atitude e de prática, e a proporção de notificação efectiva, "
          "todas com intervalo de confiança a 95% calculado pelo método de "
          "Wilson, preferido ao método assintótico para proporções "
          "afastadas de 0,50. O quarto objectivo é respondido pela "
          "ordenação das barreiras segundo a frequência com que são "
          "assinaladas e segundo a pontuação média de importância "
          "atribuída, apresentando-se as duas ordenações lado a lado para "
          "evidenciar eventuais divergências."),
        P("Para o quinto objectivo, a associação entre cada variável "
          "independente e a notificação efectiva é examinada pelo teste do "
          "qui-quadrado de Pearson, ou pelo teste exacto de Fisher quando "
          "mais de 20% das células apresentarem frequência esperada "
          "inferior a cinco. A comparação de pontuações entre categorias "
          "profissionais recorre ao teste de Kruskal-Wallis, com comparações "
          "múltiplas corrigidas pelo método de Bonferroni, e a relação "
          "entre as pontuações de conhecimento, atitude e prática ao "
          "coeficiente de correlação de Spearman."),
        P("As variáveis com valor de p inferior a 0,20 na análise "
          "bivariável, acrescidas das que a literatura identifica como "
          "determinantes mesmo na ausência de significância local, "
          "designadamente a formação prévia e a categoria profissional "
          "{gidey2020,adedeji2021,adenuga2020}, entram num modelo de "
          "regressão logística binária pelo método de entrada forçada, "
          "limitado a oito variáveis independentes para respeitar a regra "
          "de dez acontecimentos por variável. Apresentam-se a razão de "
          "possibilidades bruta, o odds ratio (OR), e a razão de "
          "possibilidades ajustada (ORa), ambas com intervalo de confiança "
          "a 95%. A colinearidade é verificada pela tolerância e pelo "
          "factor de inflação da variância, excluindo-se variáveis com "
          "factor superior a 5, e o ajustamento do modelo pelo teste de "
          "Hosmer-Lemeshow. O nível de significância é de 5% em todos os "
          "testes."),
        P("Não está prevista imputação de valores em falta. Os casos com "
          "dados em falta numa variável do modelo são excluídos dessa "
          "análise e o número de casos usado em cada modelo é declarado; se "
          "a proporção de valores em falta exceder 10% numa variável "
          "central, essa variável é descrita mas retirada do modelo "
          "multivariável, regra estabelecida antes da análise."),
    ]),
    ("Limitações do estudo e estratégias de mitigação", [
        P("O [[quadro:limitacoes]] reúne as limitações previstas, as suas "
          "consequências para a interpretação e as medidas adoptadas para "
          "as atenuar."),
        QUADRO("limitacoes",
               "Limitações previstas e estratégias de mitigação",
               ["Limitação", "Consequência", "Mitigação"],
               [["Desenho transversal",
                 "Impossibilidade de estabelecer relação causal entre "
                 "conhecimento, atitude e notificação",
                 "Formulação das conclusões em termos de associação; "
                 "discussão explícita da temporalidade na interpretação"],
                ["Prática de notificação auto-relatada",
                 "Possível sobrestimação da notificação efectiva por "
                 "desejabilidade social",
                 "Preenchimento sem presença do investigador, anonimato "
                 "completo, urna selada e pergunta de confirmação sobre o "
                 "conteúdo da ficha preenchida"],
                ["Memória do período de doze meses",
                 "Classificação incorrecta de quem notificou há mais tempo "
                 "ou de quem esqueceu a notificação",
                 "Ancoragem temporal explícita no enunciado e pergunta "
                 "complementar sobre a data aproximada da última "
                 "notificação"],
                ["Efectivo total desconhecido na fase de protocolo",
                 "Incerteza sobre o tamanho final da amostra e sobre o "
                 "poder estatístico",
                 "Regra de decisão escrita entre recenseamento e "
                 "amostragem, com tabela de cenários e declaração do poder "
                 "obtido"],
                ["Exclusão do sector privado e das farmácias comunitárias",
                 "Resultados não generalizáveis a todos os profissionais "
                 "que dispensam medicamentos na cidade",
                 "Delimitação declarada no título e nos objectivos; "
                 "recomendação de estudo complementar nesse sector"],
                ["Não resposta diferencial",
                 "Participação preferencial dos profissionais mais "
                 "sensibilizados, com sobrestimação do conhecimento",
                 "Acréscimo de 10% no tamanho, duas passagens de recolha, "
                 "registo e comparação da distribuição dos não respondentes "
                 "por categoria e unidade sanitária"],
                ["Ausência de instrumento validado para Moçambique",
                 "Risco de itens desajustados ao circuito nacional",
                 "Adaptação a partir de instrumentos publicados, validação "
                 "de conteúdo por painel de peritos, pré-teste e medida da "
                 "consistência interna"]],
               larguras=[4.2, 5.6, 6.0]),
    ]),
    ("Considerações éticas", [
        P("O protocolo será submetido ao Comité Institucional de Bioética "
          "para a Saúde da Universidade Lúrio (CIBS-UniLúrio) e a recolha "
          "só se inicia após parecer favorável. Por se tratar de um estudo "
          "circunscrito a uma cidade, sem recolha de amostras biológicas e "
          "sem envolvimento de doentes, não se prevê submissão ao Comité "
          "Nacional de Bioética para a Saúde (CNBS), sem prejuízo de o "
          "fazer se o CIBS-UniLúrio o determinar. Serão pedidas "
          "autorizações à DPS de Nampula, ao SDSMAS da Cidade de Nampula e "
          "à direcção de cada unidade sanitária [preencher os contactos "
          "telefónicos e endereços institucionais]. A investigação "
          "conduz-se segundo os princípios da Declaração de Helsínquia na "
          "revisão de 2024 {world2025}."),
        P("A participação é voluntária e precedida de consentimento livre e "
          "esclarecido, formalizado em documento próprio que o participante "
          "assina em duplicado e deposita em urna separada da dos "
          "questionários. A recusa ou a desistência a qualquer momento não "
          "acarreta qualquer consequência e não é comunicada à chefia. O "
          "questionário não regista nome, número de funcionário, serviço "
          "específico nem qualquer outro elemento que permita "
          "identificação individual, e os resultados são apresentados "
          "exclusivamente de forma agregada, nunca por unidade sanitária "
          "identificada quando o número de participantes de uma categoria "
          "for inferior a cinco."),
        P("O risco principal deste estudo é o receio de que respostas que "
          "revelem desconhecimento ou ausência de notificação venham a ter "
          "consequências profissionais. Esse risco é tratado de forma "
          "explícita em três níveis. Primeiro, a folha de informação "
          "declara que o estudo não avalia o desempenho individual, que "
          "nenhum resultado individual será comunicado a chefias ou a "
          "órgãos de supervisão e que os dados não podem ser reconduzidos a "
          "uma pessoa. Segundo, o procedimento de recolha separa "
          "fisicamente consentimentos e questionários e usa urna selada. "
          "Terceiro, o próprio quadro normativo nacional estabelece que o "
          "notificador não é penalizado por notificar suspeitas de reacções "
          "adversas nem erros de medicação, e que as informações recolhidas "
          "nas notificações não podem ser usadas para juízos de valor sobre "
          "a intervenção dos profissionais de saúde {anarme2024}; esta "
          "garantia é transcrita na folha de informação."),
        P("Não há benefício directo para o participante. O benefício "
          "indirecto é a identificação de lacunas que fundamentem formação "
          "e melhorias organizativas, com ganho para os utentes. Se, "
          "durante a aplicação, um participante relatar uma suspeita de "
          "reacção adversa por notificar, a equipa disponibiliza uma cópia "
          "da ficha oficial e indica o circuito de entrega, sem registar o "
          "caso no estudo; se solicitar formação, é encaminhado para o "
          "ponto focal provincial de farmacovigilância. Os dados são "
          "guardados em ficheiro protegido por palavra-passe, acessível "
          "apenas ao investigador e ao orientador, e eliminados cinco anos "
          "após a defesa. Os questionários em papel são conservados em "
          "armário fechado durante o mesmo período e depois destruídos."),
        LISTA([
            "Aprovação prévia pelo CIBS-UniLúrio e autorizações "
            "institucionais antes de qualquer contacto com profissionais;",
            "Consentimento livre e esclarecido, escrito, com direito de "
            "desistência sem justificação;",
            "Anonimato completo do questionário e separação física entre "
            "consentimentos e respostas;",
            "Garantia escrita de ausência de consequências profissionais e "
            "de não comunicação de respostas individuais a chefias;",
            "Devolução dos resultados em forma agregada e não punitiva às "
            "instituições envolvidas;",
            "Encaminhamento para o ponto focal de farmacovigilância sempre "
            "que o participante manifeste necessidade de apoio ou "
            "formação.",
        ]),
    ]),
]

# ----------------------------------------------------- 9 e 10 ---------------
RESULTADOS_ESPERADOS = [
    P("Os resultados esperados correspondem, pela mesma ordem, aos cinco "
      "objectivos específicos. Não se antecipam valores próprios para "
      "Moçambique, por não existirem estimativas locais; indica-se apenas a "
      "direcção sugerida pela literatura citada, que os dados confirmarão ou "
      "contrariarão."),
    LISTA([
        "Um retrato do pessoal inquirido por idade, sexo, categoria "
        "profissional, tempo de exercício, nível da unidade sanitária, "
        "sector de trabalho e formação prévia em farmacovigilância, que "
        "servirá de linha de base para a planificação da formação em "
        "serviço e permitirá identificar as categorias e os sectores menos "
        "cobertos por acções anteriores;",
        "A proporção de profissionais em cada nível de conhecimento, com "
        "intervalos de confiança a 95%. Espera-se que a maioria não atinja o "
        "nível bom, à semelhança do observado na Etiópia, onde 58,3% tinham "
        "conhecimento fraco {gidey2020}, e na Tanzânia, onde 65,8% obtiveram "
        "pontuação baixa {mssusa2025}, e que as lacunas se concentrem nos "
        "itens sobre a ficha, os prazos e o destinatário da notificação, "
        "informação que indica directamente o conteúdo prioritário da "
        "formação;",
        "A proporção com atitude favorável e a proporção com notificação "
        "efectiva nos doze meses anteriores. Espera-se o padrão descrito na "
        "literatura africana, de atitude maioritariamente favorável "
        "acompanhada de notificação efectiva inferior a um terço "
        "{haines2020,hamid2025,mssusa2025}, resultado que, a confirmar-se, "
        "desloca o problema da motivação para a capacidade e para a "
        "organização do circuito;",
        "A hierarquia das barreiras percebidas, apresentada por frequência e "
        "por importância atribuída. Espera-se o predomínio do "
        "desconhecimento do procedimento, da indisponibilidade da ficha e da "
        "falta de tempo {terblanche2017,fiagbey2026}, com peso não "
        "desprezável do receio de consequências {rotimi2024}; a ordenação "
        "obtida permitirá decidir entre formação, reposição de fichas, "
        "criação de ponto focal ou simplificação do circuito;",
        "Os factores associados à notificação efectiva, expressos em razões "
        "de possibilidades ajustadas com intervalos de confiança a 95%. "
        "Espera-se associação positiva com a formação prévia e com o nível "
        "de conhecimento {gidey2020,adedeji2021}, e diferenças entre "
        "categorias profissionais {adenuga2020}, permitindo dirigir a "
        "intervenção aos grupos com menor probabilidade de notificar em vez "
        "de a distribuir uniformemente.",
    ]),
    P("O produto final inclui ainda um instrumento em português, validado "
      "quanto ao conteúdo e com consistência interna medida, disponível "
      "para replicação noutras cidades e províncias, e um conjunto de "
      "recomendações operacionais dirigidas ao SDSMAS da Cidade de Nampula, "
      "à DPS de Nampula e à ANARME."),
]
DIVULGACAO = [
    P("Os resultados são apresentados em defesa pública perante o júri "
      "designado pela FCS da Universidade Lúrio, nos termos do regulamento "
      "de culminação de estudos, e depositados na biblioteca da "
      "instituição."),
    P("Será entregue um relatório escrito, em português e com linguagem "
      "acessível, à direcção de cada unidade sanitária participante, ao "
      "SDSMAS da Cidade de Nampula, à DPS de Nampula e à ANARME, com os "
      "resultados sempre em forma agregada e com uma secção de "
      "recomendações operacionais. A devolução às equipas das unidades "
      "sanitárias é feita em sessões curtas de apresentação, de tom "
      "formativo e não punitivo, nas quais se distribui também uma cópia da "
      "ficha oficial de notificação e uma nota com o circuito de entrega."),
    P("Está prevista a submissão de um artigo original a uma revista "
      "científica com revisão por pares, preferencialmente de acesso "
      "aberto e com interesse pela saúde em África, seguindo a lista de "
      "verificação para estudos de conhecimentos, atitudes e práticas "
      "{zarei2024}. Os resultados serão ainda apresentados em jornadas "
      "científicas da Universidade Lúrio e em encontros do Ministério da "
      "Saúde (MISAU) sobre segurança do doente, quando ocorram. Os dados "
      "anonimizados poderão ser disponibilizados mediante pedido fundamentado "
      "e parecer do CIBS-UniLúrio."),
]

# ----------------------------------------------------- 11. cronograma -------
CRONOGRAMA_TEXTO = [
    P("O [[quadro:cronograma]] distribui as actividades por doze meses, de "
      "Outubro de 2026 a Setembro de 2027. A recolha de dados ocupa os "
      "meses de Março a Maio de 2027 e só se inicia depois de obtido o "
      "parecer favorável do comité de bioética e as autorizações "
      "institucionais, previstos para Fevereiro de 2027."),
]
CRONOGRAMA = {
    "inicio": (2026, 10),
    "n_meses": 12,
    "actividades": [
        ("Revisão da literatura e redacção do protocolo", [1, 2, 3]),
        ("Submissão ao comité de bioética e pedidos de autorização "
         "institucional", [3, 4, 5]),
        ("Adaptação do instrumento e validação de conteúdo pelo painel de "
         "peritos", [4, 5]),
        ("Pré-teste do questionário e análise da fiabilidade", [5]),
        ("Formação dos auxiliares de investigação", [5, 6]),
        ("Recolha de dados nas unidades sanitárias", [6, 7, 8]),
        ("Introdução, dupla entrada e limpeza da base de dados", [8, 9]),
        ("Análise estatística", [9, 10]),
        ("Redacção do relatório final", [10, 11]),
        ("Revisão pelo orientador e entrega", [11, 12]),
        ("Defesa pública e devolução dos resultados às instituições", [12]),
    ],
}

# ----------------------------------------------------- 12. orcamento --------
ORCAMENTO_TEXTO = [
    P("A [[tabela:orcamento]] apresenta as rubricas previstas, em meticais, "
      "calculadas para o cenário mais exigente da [[tabela:cenarios]], isto "
      "é 325 questionários a distribuir."),
]
ORCAMENTO = [
    ("Impressão e fotocópia dos questionários", "página", 2100, 5),
    ("Impressão das folhas de informação e dos termos de consentimento",
     "página", 700, 5),
    ("Material de escritório, envelopes, urnas seladas e pastas",
     "conjunto", 1, 6000),
    ("Ajudas de custo dos auxiliares de investigação", "dia", 30, 750),
    ("Formação dos auxiliares de investigação", "dia", 2, 2500),
    ("Transporte urbano durante a recolha", "deslocação", 60, 350),
    ("Deslocação ao distrito vizinho para o pré-teste", "deslocação", 4, 1500),
    ("Comunicações e dados móveis", "mês", 6, 900),
    ("Sessão de trabalho do painel de peritos", "perito", 6, 1000),
    ("Impressão e encadernação de relatórios e do trabalho final",
     "exemplar", 8, 900),
    ("Taxa de submissão ao comité de bioética", "submissão", 1, 5000),
]
ORCAMENTO_IMPREVISTOS = 0.10

# ----------------------------------------------------- apendices ------------
APENDICES = [
    ("Questionário sobre conhecimentos, atitudes e práticas de "
     "farmacovigilância", [
        NOTA("Instruções ao participante: este questionário é anónimo e "
             "destina-se exclusivamente a fins de investigação. Não escreva "
             "o seu nome nem o número de funcionário. Não existem respostas "
             "certas ou erradas na secção de atitudes e de barreiras. As "
             "suas respostas não serão comunicadas a chefias nem a órgãos "
             "de supervisão e não têm qualquer consequência profissional. "
             "Depois de preencher, coloque o questionário no envelope "
             "fornecido e deposite-o na urna selada. Tempo previsto de "
             "preenchimento: 15 a 20 minutos."),
        CAMPO("Código do questionário: __________     Data: ___/___/2027"),
        H3("Secção I. Caracterização sociodemográfica e profissional"),
        PERG("Idade em anos completos:"),
        PERG("Sexo:", ["Masculino", "Feminino"]),
        PERG("Categoria profissional:",
             ["Médico ou técnico de medicina", "Enfermeiro de qualquer nível",
              "Técnico ou agente de farmácia"]),
        PERG("Nível de formação concluído:",
             ["Básico", "Médio", "Superior (licenciatura ou mais)"]),
        PERG("Tempo de exercício da profissão, em anos completos:"),
        PERG("Nível da unidade sanitária onde trabalha:",
             ["Hospital de referência", "Centro de saúde urbano"]),
        PERG("Sector principal de trabalho:",
             ["Consulta externa", "Internamento", "Urgência", "Farmácia",
              "Programa de tuberculose, de infecção por vírus da "
              "imunodeficiência humana ou de saúde materno-infantil",
              "Outro"]),
        PERG("Participou alguma vez numa acção formal de formação sobre "
             "farmacovigilância ou sobre notificação de reacções adversas?",
             ["Sim. Ano da última acção: ________", "Não"]),
        H3("Secção II. Conhecimentos sobre farmacovigilância"),
        NOTA("Assinale, para cada afirmação, se a considera verdadeira, "
             "falsa ou se não sabe. Cada resposta correcta vale um ponto; "
             "as respostas incorrectas e a opção «não sei» valem zero "
             "pontos. Pontuação máxima: 20 pontos."),
        ESCALA(["1. A farmacovigilância ocupa-se da detecção, avaliação, "
                "compreensão e prevenção de efeitos adversos de "
                "medicamentos e vacinas.",
                "2. Reacção adversa é uma resposta nociva e não desejada "
                "que ocorre em doses normalmente usadas na prática clínica.",
                "3. Só devem ser notificadas as reacções adversas cuja "
                "relação com o medicamento esteja comprovada.",
                "4. A morte, o perigo de vida, a hospitalização, a "
                "incapacidade persistente e a anomalia congénita definem "
                "uma reacção adversa grave.",
                "5. As vacinas estão excluídas do sistema nacional de "
                "farmacovigilância.",
                "6. Os medicamentos à base de plantas podem ser objecto de "
                "notificação de suspeita de reacção adversa.",
                "7. Os erros de medicação podem ser comunicados através do "
                "sistema de farmacovigilância.",
                "8. Uma notificação válida exige a identificação de um "
                "doente, ainda que apenas pelas iniciais.",
                "9. Uma notificação válida exige a identificação do "
                "notificador.",
                "10. Uma notificação válida exige a identificação de pelo "
                "menos um medicamento suspeito.",
                "11. Uma notificação só é aceite se incluir resultados "
                "laboratoriais que confirmem a reacção.",
                "12. O profissional de saúde deve notificar de imediato "
                "todas as suspeitas de reacções adversas de que tenha "
                "conhecimento.",
                "13. As notificações são recebidas e avaliadas pelo Centro "
                "Nacional de Farmacovigilância da autoridade reguladora "
                "nacional.",
                "14. As suspeitas de reacções adversas graves devem chegar "
                "ao Centro Nacional no prazo máximo de quinze dias após a "
                "recepção.",
                "15. O sistema nacional de farmacovigilância foi criado por "
                "regulamento próprio, com base na lei do medicamento.",
                "16. As notificações são tratadas de forma confidencial "
                "quanto à identidade do doente e do notificador.",
                "17. O notificador pode ser penalizado se a suspeita "
                "notificada não se vier a confirmar.",
                "18. Apenas os médicos estão autorizados a preencher a "
                "ficha de notificação.",
                "19. Moçambique integra o programa internacional de "
                "monitorização de medicamentos da Organização Mundial da "
                "Saúde.",
                "20. A notificação espontânea permite detectar reacções "
                "raras que não foram identificadas nos ensaios clínicos."],
               ["Verdadeira", "Falsa", "Não sei"]),
        H3("Secção III. Atitudes perante a notificação"),
        NOTA("Indique o seu grau de concordância com cada afirmação, "
             "usando a escala: 1, discordo totalmente; 2, discordo; 3, não "
             "concordo nem discordo; 4, concordo; 5, concordo totalmente. "
             "As afirmações 3, 4, 7 e 8 são pontuadas de forma invertida. "
             "Pontuação máxima: 50 pontos."),
        ESCALA(["1. Notificar suspeitas de reacções adversas faz parte das "
                "minhas responsabilidades profissionais.",
                "2. A notificação contribui para a segurança dos doentes "
                "que atendo.",
                "3. Notificar uma única reacção não faz diferença para o "
                "sistema.",
                "4. Só vale a pena notificar reacções graves ou ainda não "
                "descritas.",
                "5. Sinto-me à vontade para notificar mesmo quando tenho "
                "dúvidas sobre a causa da reacção.",
                "6. A farmacovigilância deveria ser ensinada a todos os "
                "profissionais de saúde.",
                "7. Notificar expõe o profissional a críticas ou a sanções.",
                "8. O tempo gasto a preencher a ficha é tempo retirado ao "
                "doente.",
                "9. Gostaria de receber informação de retorno sobre as "
                "notificações que submeto.",
                "10. A notificação deveria ser obrigatória e verificada nas "
                "unidades sanitárias."],
               ["1", "2", "3", "4", "5"]),
        H3("Secção IV. Práticas e contexto do serviço"),
        NOTA("Responda pensando exclusivamente nos últimos doze meses. Cada "
             "resposta afirmativa nos itens 1 a 10 vale um ponto; pontuação "
             "máxima: 10 pontos. Considera-se notificação efectiva a "
             "resposta afirmativa simultânea aos itens 5 e 6."),
        ESCALA(["1. Perguntei ao doente sobre reacções anteriores a "
                "medicamentos antes de prescrever, dispensar ou "
                "administrar.",
                "2. Registei no processo clínico ou no livro de registo uma "
                "suspeita de reacção adversa observada.",
                "3. Informei o doente sobre as reacções adversas mais "
                "frequentes do medicamento entregue.",
                "4. Consultei o folheto informativo ou outra fonte para "
                "confirmar se a reacção observada estava descrita.",
                "5. Preenchi pelo menos uma ficha oficial de notificação de "
                "suspeita de reacção adversa.",
                "6. Entreguei a ficha preenchida ao responsável da unidade "
                "sanitária ou ao nível superior.",
                "7. Comuniquei uma suspeita de reacção adversa ao médico ou "
                "ao farmacêutico responsável.",
                "8. Aconselhei um doente a comunicar reacções adversas ao "
                "serviço de saúde.",
                "9. Participei numa discussão de equipa sobre segurança de "
                "medicamentos.",
                "10. Procurei informação sobre farmacovigilância ou sobre o "
                "circuito de notificação."],
               ["Sim", "Não"]),
        PERG("Se respondeu «sim» ao item 5, indique a data aproximada da "
             "última ficha preenchida:", ["Mês: ______ Ano: ______"]),
        PERG("Existem fichas de notificação acessíveis no serviço onde "
             "trabalha?", ["Sim", "Não", "Não sei"]),
        PERG("Existe na sua unidade sanitária um responsável identificado "
             "pela farmacovigilância?", ["Sim", "Não", "Não sei"]),
        PERG("Alguma vez recebeu informação de retorno sobre uma "
             "notificação submetida?",
             ["Sim", "Não", "Nunca notifiquei"]),
        H3("Secção V. Barreiras percebidas à notificação"),
        NOTA("Classifique a importância de cada barreira para explicar a "
             "não notificação no seu serviço, usando a escala: 1, nada "
             "importante; 2, pouco importante; 3, moderadamente importante; "
             "4, importante; 5, muito importante."),
        ESCALA(["1. Não sei como preencher a ficha de notificação.",
                "2. Não sei a quem entregar a ficha depois de preenchida.",
                "3. Não há fichas disponíveis no meu serviço.",
                "4. Falta de tempo durante o atendimento.",
                "5. Volume de trabalho já elevado.",
                "6. Dúvida sobre se a reacção foi causada pelo medicamento.",
                "7. A reacção já é conhecida e está descrita no folheto.",
                "8. A reacção observada não era grave.",
                "9. Receio de consequências profissionais ou disciplinares.",
                "10. Receio de expor um colega que prescreveu ou "
                "administrou o medicamento.",
                "11. Nunca recebi informação de retorno sobre notificações "
                "anteriores.",
                "12. Considero que a notificação não altera nada na "
                "prática."],
               ["1", "2", "3", "4", "5"]),
        CAMPO("Outras barreiras não listadas: "
              "_______________________________________________"),
        CAMPO("Sugestões para facilitar a notificação no seu serviço: "
              "____________________________"),
        NOTA("Obrigado pela sua participação. Coloque o questionário no "
             "envelope e deposite-o na urna selada."),
    ]),
    ("Folha de informação ao participante", [
        P("Título do estudo: conhecimentos, atitudes e práticas de "
          "farmacovigilância e barreiras à notificação de reacções adversas "
          "entre profissionais de saúde das unidades sanitárias da cidade de "
          "Nampula, 2027."),
        P("Investigador: [Nome do(a) estudante], estudante finalista da "
          "Licenciatura em Farmácia da Faculdade de Ciências de Saúde da "
          "Universidade Lúrio. Orientador: [Nome e grau académico do(a) "
          "orientador(a)]. Contacto: [preencher o telefone e o correio "
          "electrónico do investigador]."),
        P("Convidamo-lo a participar num estudo que procura conhecer o que "
          "os profissionais de saúde da cidade de Nampula sabem, pensam e "
          "fazem em relação à notificação de suspeitas de reacções adversas "
          "a medicamentos, e que dificuldades encontram para notificar. O "
          "estudo é um trabalho académico de fim de curso e não é uma "
          "avaliação de desempenho, uma inspecção ou uma auditoria."),
        P("Se aceitar participar, será convidado a preencher sozinho um "
          "questionário anónimo com cerca de 60 perguntas, que demora 15 a "
          "20 minutos. Não escreverá o seu nome nem qualquer dado que "
          "permita identificá-lo. Depois de preencher, colocará o "
          "questionário num envelope e depositá-lo-á numa urna selada. O "
          "termo de consentimento que assinar será depositado noutra urna, "
          "separada, para que nunca seja possível ligar a sua assinatura às "
          "suas respostas."),
        P("A participação é inteiramente voluntária. Pode recusar ou "
          "desistir em qualquer momento, sem dar explicações e sem qualquer "
          "consequência para si. A sua decisão não será comunicada à sua "
          "chefia. Nenhuma resposta individual será mostrada a chefias, a "
          "supervisores ou a qualquer órgão do sector da saúde: os "
          "resultados serão apresentados apenas em forma agregada, para o "
          "conjunto dos participantes."),
        P("O quadro normativo nacional de farmacovigilância estabelece que o "
          "notificador não é penalizado por notificar suspeitas de reacções "
          "adversas ou erros de medicação, e que a informação recolhida nas "
          "notificações não pode ser usada para fazer juízos de valor sobre "
          "a intervenção dos profissionais de saúde. Este estudo respeita "
          "integralmente esse princípio."),
        P("O estudo não traz benefício directo para si nem apresenta riscos "
          "físicos. O desconforto possível limita-se ao tempo gasto e à "
          "eventual dificuldade em responder a perguntas de conhecimento; "
          "recorde-se que a pontuação individual não é comunicada a "
          "ninguém. O benefício indirecto é contribuir para que a formação "
          "e a organização do circuito de notificação na cidade de Nampula "
          "passem a assentar em informação real."),
        P("Os dados serão guardados em ficheiro protegido por palavra-passe, "
          "acessível apenas ao investigador e ao orientador, e destruídos "
          "cinco anos após a defesa. O estudo foi aprovado pelo Comité "
          "Institucional de Bioética para a Saúde da Universidade Lúrio "
          "[preencher o número e a data do parecer]. Para dúvidas sobre os "
          "seus direitos como participante pode contactar o comité "
          "[preencher o contacto do comité de bioética]."),
    ]),
    ("Termo de consentimento livre e esclarecido", [
        P("Declaro que li, ou que me foi lida e explicada, a folha de "
          "informação ao participante relativa ao estudo sobre "
          "conhecimentos, atitudes e práticas de farmacovigilância entre "
          "profissionais de saúde das unidades sanitárias da cidade de "
          "Nampula."),
        P("Compreendi o objectivo do estudo, o que me é pedido, o tempo "
          "necessário e o facto de o questionário ser anónimo. Foi-me dada "
          "oportunidade de colocar perguntas e todas foram respondidas de "
          "forma satisfatória."),
        P("Compreendo que a minha participação é voluntária, que posso "
          "recusar ou desistir a qualquer momento sem justificação e sem "
          "qualquer prejuízo, e que as minhas respostas individuais não "
          "serão comunicadas a chefias, a supervisores ou a qualquer órgão "
          "do sector da saúde, não tendo qualquer consequência "
          "profissional."),
        P("Aceito participar neste estudo nas condições descritas."),
        CAMPO("Nome do participante: _________________________________"),
        CAMPO("Assinatura: ______________________  Data: ___/___/2027"),
        CAMPO("Nome do investigador: ________________________________"),
        CAMPO("Assinatura: ______________________  Data: ___/___/2027"),
        NOTA("Este termo é assinado em duplicado, ficando um exemplar com o "
             "participante e outro com o investigador. Por o estudo "
             "abranger exclusivamente profissionais de saúde com formação "
             "escolar completa, não se prevê a modalidade de impressão "
             "digital com testemunha; se ainda assim for necessária, o "
             "termo é lido em voz alta e assinado por uma testemunha "
             "independente da equipa de investigação."),
    ]),
    ("Pedido de autorização institucional", [
        P("Exmo. Senhor Director [do Serviço Distrital de Saúde, Mulher e "
          "Acção Social da Cidade de Nampula / da Direcção Provincial de "
          "Saúde de Nampula / da unidade sanitária]."),
        P("Assunto: pedido de autorização para a realização de um estudo "
          "sobre conhecimentos, atitudes e práticas de farmacovigilância "
          "entre profissionais de saúde."),
        P("[Nome do(a) estudante], estudante finalista da Licenciatura em "
          "Farmácia da Faculdade de Ciências de Saúde da Universidade "
          "Lúrio, vem por este meio solicitar autorização para realizar, "
          "nas unidades sanitárias sob a sua direcção, a recolha de dados "
          "do estudo acima identificado, entre Março e Maio de 2027."),
        P("O estudo consiste na aplicação de um questionário anónimo e "
          "auto-administrado a médicos, técnicos de medicina, enfermeiros, "
          "técnicos e agentes de farmácia, com duração de preenchimento de "
          "15 a 20 minutos, em horário acordado com a direcção de cada "
          "unidade sanitária de modo a não perturbar o atendimento. Não "
          "serão consultados processos clínicos nem registos de pessoal, e "
          "nenhum participante será identificado."),
        P("Solicita-se ainda, para efeitos de dimensionamento e de "
          "selecção aleatória da amostra, a disponibilização do número de "
          "profissionais por categoria e por unidade sanitária, informação "
          "que será usada exclusivamente para esse fim e destruída após a "
          "recolha."),
        P("O protocolo foi submetido ao Comité Institucional de Bioética "
          "para a Saúde da Universidade Lúrio e a recolha só se iniciará "
          "após parecer favorável, cuja cópia será anexada. Compromete-se o "
          "investigador a entregar a essa direcção um relatório com os "
          "resultados agregados e as recomendações operacionais."),
        CAMPO("Nampula, ____ de ______________ de 2027"),
        CAMPO("O(A) estudante: ______________________________"),
        CAMPO("O(A) orientador(a): ___________________________"),
        CAMPO("Deferimento: ______________________  Data: ___/___/2027"),
    ]),
]
