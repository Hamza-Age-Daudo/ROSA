"""Referencias do protocolo e numerador Vancouver.

Todas as entradas foram confirmadas no Crossref (DOI) ou por consulta directa a
pagina oficial (URL com resposta 200) em Setembro de 2026. Na versao 3 (23/09/2026)
as 57 referencias anteriores foram reauditadas: corrigiram-se autores, anos e formatos
e retiraram-se as que nao sustentavam o texto. No texto usa-se a chave
entre parenteses rectos duplos, por exemplo [[krug2002]] ou [[han2019,aboagye2021a]],
e o numerador atribui o numero pela ordem de aparecimento.
"""
import re

FONTES = {
    "oms_adolescente": "Organização Mundial da Saúde. Adolescent health [Internet]. Genebra: "
        "Organização Mundial da Saúde; 2026 [citado 2026 Set 23]. "
        "Disponível em: https://www.who.int/health-topics/adolescent-health.",
    "krug2002": "Krug EG, Dahlberg LL, Mercy JA, Zwi AB, Lozano R, editores. World report on "
        "violence and health. Genebra: Organização Mundial da Saúde; 2002. "
        "Disponível em: https://www.who.int/publications/i/item/9241545615.",
    "oms_violencia_jovem": "Organização Mundial da Saúde. Youth violence [Internet]. Genebra: "
        "Organização Mundial da Saúde; 2026 [citado 2026 Set 23]. "
        "Disponível em: https://www.who.int/news-room/fact-sheets/detail/youth-violence.",
    "buss1992": "Buss AH, Perry M. The aggression questionnaire. J Pers Soc Psychol. "
        "1992;63(3):452-9. doi:10.1037/0022-3514.63.3.452.",
    "raine2006": "Raine A, Dodge K, Loeber R, Gatzke-Kopp L, Lynam D, Reynolds C, et al. The "
        "reactive-proactive aggression questionnaire: differential correlates of reactive and "
        "proactive aggression in adolescent boys. Aggress Behav. 2006;32(2):159-71. "
        "doi:10.1002/ab.20115.",
    "han2019": "Han L, You D, Gao X, Duan S, Hu G, Wang H, et al. Unintentional injuries and "
        "violence among adolescents aged 12-15 years in 68 low-income and middle-income countries: "
        "a secondary analysis of data from the Global School-Based Student Health Survey. Lancet "
        "Child Adolesc Health. 2019;3(9):616-26. doi:10.1016/S2352-4642(19)30195-6.",
    "aboagye2021a": "Aboagye RG, Seidu AA, Adu C, Cadri A, Mireku DO, Ahinkorah BO. Interpersonal "
        "violence among in-school adolescents in sub-Saharan Africa: assessing the prevalence and "
        "predictors from the Global School-based health survey. SSM Popul Health. 2021;16:100929. "
        "doi:10.1016/j.ssmph.2021.100929.",
    "aboagye2021b": "Aboagye RG, Seidu AA, Hagan JE Jr, Frimpong JB, Budu E, Adu C, et al. A "
        "multi-country analysis of the prevalence and factors associated with bullying "
        "victimisation among in-school adolescents in sub-Saharan Africa: evidence from the global "
        "school-based health survey. BMC Psychiatry. 2021;21(1):325. "
        "doi:10.1186/s12888-021-03337-5.",
    "vacs2019": "Instituto Nacional de Saúde, Ministério da Saúde, Ministério do Género, Criança e "
        "Acção Social, Instituto Nacional de Estatística, Centers for Disease Control and "
        "Prevention. Mozambique Violence Against Children and Youth Survey (VACS 2019): final "
        "report. Maputo: Instituto Nacional de Saúde; 2022. Disponível em: "
        "https://cdn.togetherforgirls.org/assets/files/Mozambique-VACS-report.pdf.",
    "amene2024": "Amene EW, Annor FB, Gilbert LK, McOwen J, Augusto A, Manuel P, et al. Prevalence "
        "of adverse childhood experiences in sub-Saharan Africa: a multicountry analysis of the "
        "Violence Against Children and Youth Surveys (VACS). Child Abuse Negl. 2024;150:106353. "
        "doi:10.1016/j.chiabu.2023.106353.",
    "sema2025": "Semá Baltazar C, Ribeiro Banze A, Muleia R. Patterns of self-reported alcohol and "
        "drug use among children and youth: Mozambique violence against children survey (VACS) "
        "2019. BMC Public Health. 2025;25(1):1159. doi:10.1186/s12889-025-22360-9.",
    "king2026": "King A, Adam S, Bila C, Fernandes ME, Rodrigues T, dos Santos PF, et al. "
        "Prevalence of mental disorders and healthcare seeking among Mozambican adolescents in "
        "school. Transcult Psychiatry. 2026 Jun 12:13634615251409683. "
        "doi:10.1177/13634615251409683. Epub ahead of print.",
    "igreja2024": "Igreja V, Axelsen T, Brekelmans A. Exploring the mental health of young people "
        "in households and schools in Gorongosa District, Center of Mozambique. Sci Rep. "
        "2024;14(1):28057. doi:10.1038/s41598-024-79257-7.",
    "scott2018": "Scott JG, Tunbridge M, Stathis S. The aggressive child. J Paediatr Child Health. "
        "2018;54(10):1165-9. doi:10.1111/jpc.14182.",
    "inspire2016": "Organização Mundial da Saúde. INSPIRE: seven strategies for ending violence "
        "against children. Genebra: Organização Mundial da Saúde; 2016. Disponível em: "
        "https://www.who.int/publications/i/item/9789241565356.",
    "matsinhe2024": "Matsinhe SO, Suffla S, Hector TJ. Occurrence and circumstances of child "
        "sexual assault in Maputo, Mozambique. J Forensic Leg Med. 2024;108:102778. "
        "doi:10.1016/j.jflm.2024.102778.",
    "vigneri2026": "Vigneri M, Fadare O, Devries K, Iversen V, Brück T. Past political violence "
        "and interpersonal violence against children and youth in Africa. Nat Commun. "
        "2026;17(1):3044. doi:10.1038/s41467-026-71075-x.",
    "bandura1961": "Bandura A, Ross D, Ross SA. Transmission of aggression through imitation of "
        "aggressive models. J Abnorm Soc Psychol. 1961;63(3):575-82. doi:10.1037/h0045925.",
    "oms_saude_mental": "Organização Mundial da Saúde. Mental health of adolescents [Internet]. "
        "Genebra: Organização Mundial da Saúde; 2025 [citado 2026 Set 23]. Disponível em: "
        "https://www.who.int/news-room/fact-sheets/detail/adolescent-mental-health.",
    "xu2024": "Xu X, Wu Y, Xu Y, Ding M, Zhou S, Long S. The role of parent-child attachment, "
        "hostile attribution bias in aggression: a meta-analytic review. Trauma Violence Abuse. "
        "2024;25(3):2334-47. doi:10.1177/15248380231210920.",
    "tarafa2022": "Tarafa H, Alemayehu Y, Bete T, Tarecha D. Bullying victimization and its "
        "associated factors among adolescents in Illu Abba Bor Zone, Southwest Ethiopia: a "
        "cross-sectional study. BMC Psychol. 2022;10(1):260. doi:10.1186/s40359-022-00967-6.",
    "ameli2017": "Ameli V, Meinck F, Munthali A, Ushie B, Langhaug L. Associations between "
        "adolescent experiences of violence in Malawi and gender-based attitudes, internalizing, "
        "and externalizing behaviors. Child Abuse Negl. 2017;67:305-14. "
        "doi:10.1016/j.chiabu.2017.02.027.",
    "gershoff2016": "Gershoff ET, Grogan-Kaylor A. Spanking and child outcomes: old controversies "
        "and new meta-analyses. J Fam Psychol. 2016;30(4):453-69. doi:10.1037/fam0000191.",
    "elgar2018": "Elgar FJ, Donnelly PD, Michaelson V, Gariépy G, Riehm KE, Walsh SD, et al. "
        "Corporal punishment bans and physical fighting in adolescents: an ecological study of 88 "
        "countries. BMJ Open. 2018;8(9):e021616. doi:10.1136/bmjopen-2018-021616.",
    "henneberger2016": "Henneberger AK, Varga SM, Moudy A, Tolan PH. Family functioning and high "
        "risk adolescents' aggressive behavior: examining effects by ethnicity. J Youth Adolesc. "
        "2016;45(1):145-55. doi:10.1007/s10964-014-0222-8.",
    "tian2019": "Tian Y, Yu C, Lin S, Lu J, Liu Y, Zhang W. Parental psychological control and "
        "adolescent aggressive behavior: deviant peer affiliation as a mediator and school "
        "connectedness as a moderator. Front Psychol. 2019;10:358. doi:10.3389/fpsyg.2019.00358.",
    "annor2024": "Annor FB, Amene EW, Zhu L, Stamatakis C, Picchetti V, Matthews S, et al. "
        "Parental absence as an adverse childhood experience among young adults in sub-Saharan "
        "Africa. Child Abuse Negl. 2024;150:106556. doi:10.1016/j.chiabu.2023.106556.",
    "blum2019": "Blum RW, Li M, Naranjo-Rivera G. Measuring adverse child experiences among young "
        "adolescents globally: relationships with depressive symptoms and violence perpetration. "
        "J Adolesc Health. 2019;65(1):86-93. doi:10.1016/j.jadohealth.2019.01.020.",
    "brown2024": "Brown C, Nkemjika S, Ratto J, Dube SR, Gilbert L, Chiang L, et al. Adverse "
        "childhood experiences and associations with mental health, substance use, and violence "
        "perpetration among young adults in sub-Saharan Africa. Child Abuse Negl. "
        "2024;150:106524. doi:10.1016/j.chiabu.2023.106524.",
    "zietz2020": "Zietz S, Kajula L, McNaughton Reyes HL, Moracco B, Shanahan M, Martin S, et "
        "al. Patterns of adverse childhood experiences and subsequent risk of interpersonal "
        "violence perpetration among men in Dar es Salaam, Tanzania. Child Abuse Negl. "
        "2020;99:104256. doi:10.1016/j.chiabu.2019.104256.",
    "miedema2026": "Miedema SS, Matthews SA, Annor FB, Villaveces A, Mndzebele P, Adler MR, et "
        "al. Prevalence of violence perpetration by men aged 18-24 years in low- and "
        "middle-income countries who were exposed to violence during childhood, eight countries, "
        "2018-2023. MMWR Morb Mortal Wkly Rep. 2026;75(3):41-6. doi:10.15585/mmwr.mm7503a2.",
    "zhu2016": "Zhu J, Yu C, Zhang W, Bao Z, Jiang Y, Chen Y, et al. Peer victimization, deviant "
        "peer affiliation and impulsivity: predicting adolescent problem behaviors. Child Abuse "
        "Negl. 2016;58:39-50. doi:10.1016/j.chiabu.2016.06.008.",
    "li2024": "Li Y, Scott Huebner E, Tian L. Deviant peer affiliation, self-control, and "
        "aggression during early adolescence: within-person effects and between-person "
        "differences. Eur Child Adolesc Psychiatry. 2024;33(7):2343-52. "
        "doi:10.1007/s00787-023-02336-z.",
    "ugwu2024": "Ugwu LE, Ramadie KJ, Ajele WK, Idemudia ES. Childhood adversity and peer "
        "influence in adolescent bullying perpetration. Sci Rep. 2024;14(1):30959. "
        "doi:10.1038/s41598-024-81978-8.",
    "ma2018": "Ma C, Bovet P, Yang L, Zhao M, Liang Y, Xi B. Alcohol use among young adolescents "
        "in low-income and middle-income countries: a population-based study. Lancet Child Adolesc "
        "Health. 2018;2(6):415-29. doi:10.1016/S2352-4642(18)30112-3.",
    "tian2021": "Tian S, Zhang T, Chen X, Pan CW. Substance use and psychological distress "
        "among school-going adolescents in 41 low-income and middle-income countries. J Affect "
        "Disord. 2021;291:254-60. doi:10.1016/j.jad.2021.05.024.",
    "sukhodolsky2016": "Sukhodolsky DG, Smith SD, McCauley SA, Ibrahim K, Piasecka JB. Behavioral "
        "interventions for anger, irritability, and aggression in children and adolescents. J "
        "Child Adolesc Psychopharmacol. 2016;26(1):58-64. doi:10.1089/cap.2015.0120.",
    "pechorro2016": "Pechorro P, Barroso R, Poiares C, Oliveira JP, Torrealday O. Validation of "
        "the Buss-Perry Aggression Questionnaire-Short Form among Portuguese juvenile delinquents. "
        "Int J Law Psychiatry. 2016;44:75-80. doi:10.1016/j.ijlp.2015.08.033.",
    "pechorro2015": "Pechorro P, Ray JV, Raine A, Maroco J, Gonçalves RA. The reactive-proactive "
        "aggression questionnaire: validation among a Portuguese sample of incarcerated juvenile "
        "delinquents. J Interpers Violence. 2017;32(13):1995-2017. "
        "doi:10.1177/0886260515590784.",
    "tuvblad2016": "Tuvblad C, Dhamija D, Berntsen L, Raine A, Liu J. Cross-cultural validation of "
        "the Reactive-Proactive Aggression Questionnaire (RPQ) using four large samples from the "
        "US, Hong Kong, and China. J Psychopathol Behav Assess. 2016;38(1):48-55. "
        "doi:10.1007/s10862-015-9501-2.",
    "goodman1997": "Goodman R. The Strengths and Difficulties Questionnaire: a research note. J "
        "Child Psychol Psychiatry. 1997;38(5):581-6. doi:10.1111/j.1469-7610.1997.tb01545.x.",
    "smilkstein1978": "Smilkstein G. The family APGAR: a proposal for a family function test and "
        "its use by physicians. J Fam Pract. 1978;6(6):1231-9. PMID:660126.",
    "aceiq": "Organização Mundial da Saúde. Adverse Childhood Experiences International "
        "Questionnaire (ACE-IQ) [Internet]. Genebra: Organização Mundial da Saúde; 2026 "
        "[citado 2026 Set 23]. Disponível em: https://www.who.int/publications/m/"
        "item/adverse-childhood-experiences-international-questionnaire-(ace-iq).",
    "gshs": "Organização Mundial da Saúde. Global School-based Student Health Survey (GSHS) "
        "[Internet]. Genebra: Organização Mundial da Saúde; 2026 [citado 2026 Set 23]. "
        "Disponível em: https://www.who.int/teams/noncommunicable-diseases/surveillance/"
        "systems-tools/global-school-based-student-health-survey.",
    "strobe2007": "von Elm E, Altman DG, Egger M, Pocock SJ, Gøtzsche PC, Vandenbroucke JP. The "
        "Strengthening the Reporting of Observational Studies in Epidemiology (STROBE) statement: "
        "guidelines for reporting observational studies. Lancet. 2007;370(9596):1453-7. "
        "doi:10.1016/S0140-6736(07)61602-X.",
    "charan2013": "Charan J, Biswas T. How to calculate sample size for different study designs in "
        "medical research? Indian J Psychol Med. 2013;35(2):121-6. doi:10.4103/0253-7176.116232.",
    "faul2009": "Faul F, Erdfelder E, Buchner A, Lang AG. Statistical power analyses using G*Power "
        "3.1: tests for correlation and regression analyses. Behav Res Methods. "
        "2009;41(4):1149-60. doi:10.3758/BRM.41.4.1149.",
    "peduzzi1996": "Peduzzi P, Concato J, Kemper E, Holford TR, Feinstein AR. A simulation study "
        "of the number of events per variable in logistic regression analysis. J Clin Epidemiol. "
        "1996;49(12):1373-9. doi:10.1016/S0895-4356(96)00236-3.",
    "helsinquia2024": "World Medical Association. World Medical Association Declaration of "
        "Helsinki: ethical principles for medical research involving human participants. JAMA. "
        "2025;333(1):71-4. doi:10.1001/jama.2024.21972.",
    # Acrescentadas na versao 3 (23/09/2026), confirmadas no Crossref e no PubMed.
    "butovskaya2019": "Butovskaya M, Burkova V, Karelin D, Filatova V. The association between "
        "2D:4D ratio and aggression in children and adolescents: cross-cultural and gender "
        "differences. Early Hum Dev. 2019;137:104823. doi:10.1016/j.earlhumdev.2019.07.006.",
    "firth1993": "Firth D. Bias reduction of maximum likelihood estimates. Biometrika. "
        "1993;80(1):27-38. doi:10.1093/biomet/80.1.27.",
    "card2006": "Card NA, Little TD. Proactive and reactive aggression in childhood and "
        "adolescence: a meta-analysis of differential relations with psychosocial adjustment. "
        "Int J Behav Dev. 2006;30(5):466-80. doi:10.1177/0165025406071904.",
    "pechorro2018": "Pechorro P, Ayala-Nunes L, Kahn R, Nunes C. The Reactive-Proactive "
        "Aggression Questionnaire: measurement invariance and reliability among a school sample "
        "of Portuguese youths. Child Psychiatry Hum Dev. 2018;49(4):523-33. "
        "doi:10.1007/s10578-017-0772-6.",
    "gratz2004": "Gratz KL, Roemer L. Multidimensional assessment of emotion regulation and "
        "dysregulation: development, factor structure, and initial validation of the "
        "Difficulties in Emotion Regulation Scale. J Psychopathol Behav Assess. 2004;26(1):41-54. "
        "doi:10.1023/B:JOBA.0000007455.08539.94.",
    "oms_cid11": "Organização Mundial da Saúde. International Classification of Diseases, 11th "
        "Revision (ICD-11) for mortality and morbidity statistics [Internet]. Genebra: "
        "Organização Mundial da Saúde; 2025 [citado 2026 Set 23]. Disponível em: "
        "https://icd.who.int/browse/2025-01/mms/en.",
    "anderson2002": "Anderson CA, Bushman BJ. Human aggression. Annu Rev Psychol. 2002;53:27-51. "
        "doi:10.1146/annurev.psych.53.100901.135231.",
    "allen2018": "Allen JJ, Anderson CA, Bushman BJ. The General Aggression Model. Curr Opin "
        "Psychol. 2018;19:75-80. doi:10.1016/j.copsyc.2017.03.034.",
    "berkowitz1989": "Berkowitz L. Frustration-aggression hypothesis: examination and "
        "reformulation. Psychol Bull. 1989;106(1):59-73. doi:10.1037/0033-2909.106.1.59.",
    "crick1994": "Crick NR, Dodge KA. A review and reformulation of social "
        "information-processing mechanisms in children's social adjustment. Psychol Bull. "
        "1994;115(1):74-101. doi:10.1037/0033-2909.115.1.74.",
    "dodge2015": "Dodge KA, Malone PS, Lansford JE, Sorbring E, Skinner AT, Tapanya S, et al. "
        "Hostile attributional bias and aggressive behavior in global context. Proc Natl Acad Sci "
        "U S A. 2015;112(30):9310-5. doi:10.1073/pnas.1418572112.",
    "dodge1987": "Dodge KA, Coie JD. Social-information-processing factors in reactive and "
        "proactive aggression in children's peer groups. J Pers Soc Psychol. "
        "1987;53(6):1146-58. doi:10.1037/0022-3514.53.6.1146.",
    "moffitt1993": "Moffitt TE. Adolescence-limited and life-course-persistent antisocial "
        "behavior: a developmental taxonomy. Psychol Rev. 1993;100(4):674-701. "
        "doi:10.1037/0033-295X.100.4.674.",
    "engel1977": "Engel GL. The need for a new medical model: a challenge for biomedicine. "
        "Science. 1977;196(4286):129-36. doi:10.1126/science.847460.",
    "sroufe1984": "Sroufe LA, Rutter M. The domain of developmental psychopathology. Child Dev. "
        "1984;55(1):17-29. doi:10.2307/1129832.",
    "apa2022": "American Psychiatric Association. Diagnostic and statistical manual of mental "
        "disorders. 5.ª ed., texto rev. Washington: American Psychiatric Association Publishing; "
        "2022. doi:10.1176/appi.books.9780890425787.",
    "fairchild2019": "Fairchild G, Hawes DJ, Frick PJ, Copeland WE, Odgers CL, Franke B, et al. "
        "Conduct disorder. Nat Rev Dis Primers. 2019;5(1):43. doi:10.1038/s41572-019-0095-y.",
    "frick2014": "Frick PJ, Ray JV, Thornton LC, Kahn RE. Can callous-unemotional traits enhance "
        "the understanding, diagnosis, and treatment of serious conduct problems in children and "
        "adolescents? A comprehensive review. Psychol Bull. 2014;140(1):1-57. "
        "doi:10.1037/a0033076.",
    "leibenluft2013": "Leibenluft E, Stoddard J. The developmental psychopathology of "
        "irritability. Dev Psychopathol. 2013;25(4 Pt 2):1473-87. "
        "doi:10.1017/S0954579413000722.",
    "polanczyk2015": "Polanczyk GV, Salum GA, Sugaya LS, Caye A, Rohde LA. Annual research "
        "review: a meta-analysis of the worldwide prevalence of mental disorders in children and "
        "adolescents. J Child Psychol Psychiatry. 2015;56(3):345-65. doi:10.1111/jcpp.12381.",
    "saylor2016": "Saylor KE, Amann BH. Impulsive aggression as a comorbidity of "
        "attention-deficit/hyperactivity disorder in children and adolescents. J Child Adolesc "
        "Psychopharmacol. 2016;26(1):19-25. doi:10.1089/cap.2015.0126.",
    "blair2016": "Blair RJR. The neurobiology of impulsive aggression. J Child Adolesc "
        "Psychopharmacol. 2016;26(1):4-9. doi:10.1089/cap.2015.0088.",
    "roberton2012": "Roberton T, Daffern M, Bucks RS. Emotion regulation and aggression. Aggress "
        "Violent Behav. 2012;17(1):72-82. doi:10.1016/j.avb.2011.09.006.",
    "mclaughlin2011": "McLaughlin KA, Hatzenbuehler ML, Mennin DS, Nolen-Hoeksema S. Emotion "
        "dysregulation and adolescent psychopathology: a prospective study. Behav Res Ther. "
        "2011;49(9):544-54. doi:10.1016/j.brat.2011.06.003.",
    "heleniak2016": "Heleniak C, Jenness JL, Vander Stoep A, McCauley E, McLaughlin KA. Childhood "
        "maltreatment exposure and disruptions in emotion regulation: a transdiagnostic pathway to "
        "adolescent internalizing and externalizing psychopathology. Cognit Ther Res. "
        "2016;40(3):394-415. doi:10.1007/s10608-015-9735-z.",
    "kim2010": "Kim J, Cicchetti D. Longitudinal pathways linking child maltreatment, emotion "
        "regulation, peer relations, and psychopathology. J Child Psychol Psychiatry. "
        "2010;51(6):706-16. doi:10.1111/j.1469-7610.2009.02202.x.",
    "decastro2002": "Orobio de Castro B, Veerman JW, Koops W, Bosch JD, Monshouwer HJ. Hostile "
        "attribution of intent and aggressive behavior: a meta-analysis. Child Dev. "
        "2002;73(3):916-34. doi:10.1111/1467-8624.00447.",
    "verhoef2019": "Verhoef REJ, Alsem SC, Verhulp EE, De Castro BO. Hostile intent attribution "
        "and aggressive behavior in children revisited: a meta-analysis. Child Dev. "
        "2019;90(5):e525-47. doi:10.1111/cdev.13255.",
    "vachon2014": "Vachon DD, Lynam DR, Johnson JA. The (non)relation between empathy and "
        "aggression: surprising results from a meta-analysis. Psychol Bull. 2014;140(3):751-73. "
        "doi:10.1037/a0035236.",
    "donnellan2005": "Donnellan MB, Trzesniewski KH, Robins RW, Moffitt TE, Caspi A. Low "
        "self-esteem is related to aggression, antisocial behavior, and delinquency. Psychol Sci. "
        "2005;16(4):328-35. doi:10.1111/j.0956-7976.2005.01535.x.",
    "card2008": "Card NA, Stucky BD, Sawalani GM, Little TD. Direct and indirect aggression "
        "during childhood and adolescence: a meta-analytic review of gender differences, "
        "intercorrelations, and relations to maladjustment. Child Dev. 2008;79(5):1185-229. "
        "doi:10.1111/j.1467-8624.2008.01184.x.",
    "ford2010": "Ford JD, Elhai JD, Connor DF, Frueh BC. Poly-victimization and risk of "
        "posttraumatic, depressive, and substance use disorders and involvement in delinquency in "
        "a national sample of adolescents. J Adolesc Health. 2010;46(6):545-52. "
        "doi:10.1016/j.jadohealth.2009.11.212.",
    "fowler2009": "Fowler PJ, Tompsett CJ, Braciszewski JM, Jacques-Tiura AJ, Baltes BB. "
        "Community violence: a meta-analysis on the effect of exposure and mental health "
        "outcomes of children and adolescents. Dev Psychopathol. 2009;21(1):227-59. "
        "doi:10.1017/S0954579409000145.",
    "prescott2018": "Prescott AT, Sargent JD, Hull JG. Metaanalysis of the relationship between "
        "violent video game play and physical aggression over time. Proc Natl Acad Sci U S A. "
        "2018;115(40):9882-8. doi:10.1073/pnas.1611617114.",
    "hecker2014": "Hecker T, Hermenau K, Isele D, Elbert T. Corporal punishment and children's "
        "externalizing problems: a cross-sectional study of Tanzanian primary school aged "
        "children. Child Abuse Negl. 2014;38(5):884-92. doi:10.1016/j.chiabu.2013.11.007.",
    "amu2020": "Amu H, Seidu AA, Agbemavi W, Afriyie BO, Ahinkorah BO, Ameyaw EK, et al. "
        "Psychosocial distress among in-school adolescents in Mozambique: a cross-sectional study "
        "using the Global School-Based Health Survey data. Child Adolesc Psychiatry Ment Health. "
        "2020;14:38. doi:10.1186/s13034-020-00344-4.",
    "cortina2012": "Cortina MA, Sodha A, Fazel M, Ramchandani PG. Prevalence of child mental "
        "health problems in sub-Saharan Africa: a systematic review. Arch Pediatr Adolesc Med. "
        "2012;166(3):276-81. doi:10.1001/archpediatrics.2011.592.",
    "jornspresentati2021": "Jörns-Presentati A, Napp AK, Dessauvagie AS, Stein DJ, Jonker D, "
        "Breet E, et al. The prevalence of mental health problems in sub-Saharan adolescents: a "
        "systematic review. PLoS One. 2021;16(5):e0251689. doi:10.1371/journal.pone.0251689.",
    "dossantos2016": "dos Santos PF, Wainberg ML, Caldas-de-Almeida JM, Saraceno B, Mari JJ. "
        "Overview of the mental health system in Mozambique: addressing the treatment gap with a "
        "task-shifting strategy in primary care. Int J Ment Health Syst. 2016;10:1. "
        "doi:10.1186/s13033-015-0032-8.",
    "oms_mhgap": "Organização Mundial da Saúde. mhGAP intervention guide for mental, "
        "neurological and substance use disorders in non-specialized health settings: mental "
        "health Gap Action Programme (mhGAP), version 2.0. Genebra: Organização Mundial da Saúde; "
        "2016. Disponível em: https://www.who.int/publications/i/item/9789241549790.",
    "bryant2001": "Bryant FB, Smith BD. Refining the architecture of aggression: a measurement "
        "model for the Buss-Perry Aggression Questionnaire. J Res Pers. 2001;35(2):138-67. "
        "doi:10.1006/jrpe.2000.2302.",
    "goodman1998": "Goodman R, Meltzer H, Bailey V. The Strengths and Difficulties "
        "Questionnaire: a pilot study on the validity of the self-report version. Eur Child "
        "Adolesc Psychiatry. 1998;7(3):125-30. doi:10.1007/s007870050057.",
    "goodman2001": "Goodman R. Psychometric properties of the Strengths and Difficulties "
        "Questionnaire. J Am Acad Child Adolesc Psychiatry. 2001;40(11):1337-45. "
        "doi:10.1097/00004583-200111000-00015.",
    "hoosen2018": "Hoosen N, Davids EL, de Vries PJ, Shung-King M. The Strengths and "
        "Difficulties Questionnaire (SDQ) in Africa: a scoping review of its application and "
        "validation. Child Adolesc Psychiatry Ment Health. 2018;12:6. "
        "doi:10.1186/s13034-017-0212-1.",
    "kaufman2016": "Kaufman EA, Xia M, Fosco G, Yaptangco M, Skidmore CR, Crowell SE. The "
        "Difficulties in Emotion Regulation Scale Short Form (DERS-SF): validation and "
        "replication in adolescent and adult samples. J Psychopathol Behav Assess. "
        "2016;38(3):443-55. doi:10.1007/s10862-015-9529-3.",
    "moreira2022": "Moreira H, Gouveia MJ, Canavarro MC. A bifactor analysis of the Difficulties "
        "in Emotion Regulation Scale, Short Form (DERS-SF) in a sample of adolescents and adults. "
        "Curr Psychol. 2022;41(2):757-82. doi:10.1007/s12144-019-00602-5.",
    "schmitt2005": "Schmitt DP, Allik J. Simultaneous administration of the Rosenberg "
        "Self-Esteem Scale in 53 nations: exploring the universal and culture-specific features "
        "of global self-esteem. J Pers Soc Psychol. 2005;89(4):623-42. "
        "doi:10.1037/0022-3514.89.4.623.",
    "perrin2005": "Perrin S, Meiser-Stedman R, Smith P. The Children's Revised Impact of Event "
        "Scale (CRIES): validity as a screening instrument for PTSD. Behav Cogn Psychother. "
        "2005;33(4):487-98. doi:10.1017/S1352465805002419.",
    "sukhodolsky2004": "Sukhodolsky DG, Kassinove H, Gorman BS. Cognitive-behavioral therapy for "
        "anger in children and adolescents: a meta-analysis. Aggress Violent Behav. "
        "2004;9(3):247-69. doi:10.1016/j.avb.2003.08.005.",
    "murray2015": "Murray LK, Skavenski S, Kane JC, Mayeya J, Dorsey S, Cohen JA, et al. "
        "Effectiveness of trauma-focused cognitive behavioral therapy among trauma-affected "
        "children in Lusaka, Zambia: a randomized clinical trial. JAMA Pediatr. "
        "2015;169(8):761-9. doi:10.1001/jamapediatrics.2015.0580.",
    "nkuba2018": "Nkuba M, Hermenau K, Goessmann K, Hecker T. Reducing violence by teachers using "
        "the preventative intervention Interaction Competencies with Children for Teachers "
        "(ICC-T): a cluster randomized controlled trial at public secondary schools in Tanzania. "
        "PLoS One. 2018;13(8):e0201362. doi:10.1371/journal.pone.0201362.",
    "hayes2022": "Hayes AF. Introduction to mediation, moderation, and conditional process "
        "analysis: a regression-based approach. 3.ª ed. New York: Guilford Press; 2022. "
        "Disponível em: https://www.guilford.com/books/Introduction-to-Mediation-Moderation-and-"
        "Conditional-Process-Analysis/Andrew-Hayes/9781462549030.",
    "fritz2007": "Fritz MS, MacKinnon DP. Required sample size to detect the mediated effect. "
        "Psychol Sci. 2007;18(3):233-9. doi:10.1111/j.1467-9280.2007.01882.x.",
    "beaton2000": "Beaton DE, Bombardier C, Guillemin F, Ferraz MB. Guidelines for the process of "
        "cross-cultural adaptation of self-report measures. Spine (Phila Pa 1976). "
        "2000;25(24):3186-91. "
        "doi:10.1097/00007632-200012150-00014.",
    "polit2006": "Polit DF, Beck CT. The content validity index: are you sure you know what's "
        "being reported? Critique and recommendations. Res Nurs Health. 2006;29(5):489-97. "
        "doi:10.1002/nur.20147.",
    "taber2018": "Taber KS. The use of Cronbach's alpha when developing and reporting research "
        "instruments in science education. Res Sci Educ. 2018;48(6):1273-96. "
        "doi:10.1007/s11165-016-9602-2.",
    "podsakoff2003": "Podsakoff PM, MacKenzie SB, Lee JY, Podsakoff NP. Common method biases in "
        "behavioral research: a critical review of the literature and recommended remedies. J "
        "Appl Psychol. 2003;88(5):879-903. doi:10.1037/0021-9010.88.5.879.",
    "steinberg2008": "Steinberg L. A social neuroscience perspective on adolescent risk-taking. "
        "Dev Rev. 2008;28(1):78-106. doi:10.1016/j.dr.2007.08.002.",
    "solmi2022": "Solmi M, Radua J, Olivola M, Croce E, Soardo L, Salazar de Pablo G, et al. Age "
        "at onset of mental disorders worldwide: large-scale meta-analysis of 192 "
        "epidemiological studies. Mol Psychiatry. 2022;27(1):281-95. "
        "doi:10.1038/s41380-021-01161-7.",
}

PADRAO = re.compile(r"\[\[([a-z0-9_,]+)\]\]")


class Numerador:
    """Atribui numeros Vancouver pela ordem de aparecimento e formata a citacao."""

    def __init__(self, fontes=None):
        self.fontes = dict(FONTES if fontes is None else fontes)
        self.ordem = []

    def _numero(self, chave):
        if chave not in self.fontes:
            raise KeyError(f"referencia desconhecida: {chave}")
        if chave not in self.ordem:
            self.ordem.append(chave)
        return self.ordem.index(chave) + 1

    @staticmethod
    def _comprimir(numeros):
        numeros = sorted(set(numeros))
        blocos, inicio, anterior = [], numeros[0], numeros[0]
        for numero in numeros[1:]:
            if numero == anterior + 1:
                anterior = numero
                continue
            blocos.append((inicio, anterior))
            inicio = anterior = numero
        blocos.append((inicio, anterior))
        partes = []
        for principio, fim in blocos:
            if fim - principio >= 2:
                partes.append(f"{principio}-{fim}")
            elif fim - principio == 1:
                partes.extend([str(principio), str(fim)])
            else:
                partes.append(str(principio))
        return ",".join(partes)

    def resolver(self, texto):
        def substituir(correspondencia):
            chaves = correspondencia.group(1).split(",")
            return "(" + self._comprimir({self._numero(c) for c in chaves}) + ")"
        return PADRAO.sub(substituir, texto)

    def lista_final(self):
        return [(indice + 1, self.fontes[chave]) for indice, chave in enumerate(self.ordem)]

    def nao_citadas(self):
        return sorted(set(self.fontes) - set(self.ordem))
