"""Referencias do protocolo e numerador Vancouver.

Todas as entradas foram confirmadas no Crossref (DOI) ou por consulta directa a
pagina oficial (URL com resposta 200) em Setembro de 2026. No texto usa-se a chave
entre parenteses rectos duplos, por exemplo [[krug2002]] ou [[han2019,aboagye2021a]],
e o numerador atribui o numero pela ordem de aparecimento.
"""
import re

FONTES = {
    "oms_adolescente": "Organização Mundial da Saúde. Adolescent health [Internet]. Genebra: "
        "Organização Mundial da Saúde; 2026 [consultado a 16 de Setembro de 2026]. "
        "Disponível em: https://www.who.int/health-topics/adolescent-health.",
    "krug2002": "Krug EG, Dahlberg LL, Mercy JA, Zwi AB, Lozano R, editores. World report on "
        "violence and health. Genebra: Organização Mundial da Saúde; 2002. "
        "Disponível em: https://www.who.int/publications/i/item/9241545615.",
    "oms_violencia_jovem": "Organização Mundial da Saúde. Youth violence [ficha informativa na "
        "Internet]. Genebra: Organização Mundial da Saúde; 2026 [consultado a 16 de Setembro de "
        "2026]. Disponível em: https://www.who.int/news-room/fact-sheets/detail/youth-violence.",
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
    "vacs2019": "Governo de Moçambique, Centers for Disease Control and Prevention, Together for "
        "Girls. Mozambique Violence Against Children and Youth Survey (VACS) 2019 [Internet]. "
        "Maputo: Governo de Moçambique; 2022 [consultado a 16 de Setembro de 2026]. Disponível em: "
        "https://www.togetherforgirls.org/en/resources/mozambique-vacs-report-2022.",
    "amene2024": "Amene EW, Annor FB, Gilbert LK, McOwen J, Augusto A, Manuel P, et al. Prevalence "
        "of adverse childhood experiences in sub-Saharan Africa: a multicountry analysis of the "
        "Violence Against Children and Youth Surveys (VACS). Child Abuse Negl. 2024;150:106353. "
        "doi:10.1016/j.chiabu.2023.106353.",
    "sema2025": "Semá Baltazar C, Ribeiro Banze A, Muleia R. Patterns of self-reported alcohol and "
        "drug use among children and youth: Mozambique violence against children survey (VACS) "
        "2019. BMC Public Health. 2025;25(1):1159. doi:10.1186/s12889-025-22360-9.",
    "king2026": "King A, Adam S, Bila C, Fernandes ME, Rodrigues T, dos Santos PF, et al. "
        "Prevalence of mental disorders and healthcare seeking among Mozambican adolescents in "
        "school. Transcult Psychiatry. 2026. doi:10.1177/13634615251409683.",
    "igreja2024": "Igreja V, Axelsen T, Brekelmans A. Exploring the mental health of young people "
        "in households and schools in Gorongosa District, Center of Mozambique. Sci Rep. "
        "2024;14(1):28057. doi:10.1038/s41598-024-79257-7.",
    "scott2018": "Scott JG, Tunbridge M, Stathis S. The aggressive child. J Paediatr Child Health. "
        "2018;54(10):1165-9. doi:10.1111/jpc.14182.",
    "oms_status2020": "Organização Mundial da Saúde. Global status report on preventing violence "
        "against children 2020. Genebra: Organização Mundial da Saúde; 2020. Disponível em: "
        "https://www.who.int/publications/i/item/9789240004191.",
    "inspire2016": "Organização Mundial da Saúde. INSPIRE: seven strategies for ending violence "
        "against children. Genebra: Organização Mundial da Saúde; 2016. Disponível em: "
        "https://www.who.int/publications/i/item/9789241565356.",
    "matsinhe2024": "Matsinhe SO, Suffla S, Hector TJ. Occurrence and circumstances of child "
        "sexual assault in Maputo, Mozambique. J Forensic Leg Med. 2024;108:102778. "
        "doi:10.1016/j.jflm.2024.102778.",
    "vigneri2026": "Vigneri M, Fadare O, Devries K, Cluver L, Meinck F. Past political violence "
        "and interpersonal violence against children and youth in Africa. Nat Commun. "
        "2026;17(1). doi:10.1038/s41467-026-71075-x.",
    "bandura1961": "Bandura A, Ross D, Ross SA. Transmission of aggression through imitation of "
        "aggressive models. J Abnorm Soc Psychol. 1961;63(3):575-82. doi:10.1037/h0045925.",
    "oms_saude_mental": "Organização Mundial da Saúde. Mental health of adolescents [ficha "
        "informativa na Internet]. Genebra: Organização Mundial da Saúde; 2026 [consultado a 16 de "
        "Setembro de 2026]. Disponível em: "
        "https://www.who.int/news-room/fact-sheets/detail/adolescent-mental-health.",
    "tordjman2022": "Tordjman S. Aggressive behavior: a language to be understood. Encephale. "
        "2022;48(Suppl 1):S4-13. doi:10.1016/j.encep.2022.08.007.",
    "xu2024": "Xu X, Wu Y, Xu Y, Zhang J, Zhou N. The role of parent-child attachment, hostile "
        "attribution bias in aggression: a meta-analytic review. Trauma Violence Abuse. "
        "2024;25(3):2334-47. doi:10.1177/15248380231210920.",
    "nguyen2020": "Nguyen AJ, Bradshaw C, Townsend L, Bass J. Prevalence and correlates of "
        "bullying victimization in four low-resource countries. J Interpers Violence. "
        "2020;35(19-20):3767-90. doi:10.1177/0886260517709799.",
    "tarafa2022": "Tarafa H, Alemayehu Y, Bete T, Tarafa A. Bullying victimization and its "
        "associated factors among adolescents in Illu Abba Bor Zone, Southwest Ethiopia: a "
        "cross-sectional study. BMC Psychol. 2022;10(1):260. doi:10.1186/s40359-022-00967-6.",
    "sweidan2024": "Sweidan AT, El-Beialy AR, El-Mangoury NH, Fawzy SA. Prevalence and factors "
        "influencing bullying among Egyptian schoolchildren. J Orthod. 2024;51(3):240-50. "
        "doi:10.1177/14653125241229455.",
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
    "palermo2019": "Palermo T, Pereira A, Neijhoft N, Bello G, Buluma R, Diem P, et al. Risk "
        "factors for childhood violence and polyvictimization: a cross-country analysis from three "
        "regions. Child Abuse Negl. 2019;88:348-61. doi:10.1016/j.chiabu.2018.10.012.",
    "blum2019": "Blum RW, Li M, Naranjo-Rivera G. Measuring adverse child experiences among young "
        "adolescents globally: relationships with depressive symptoms and violence perpetration. "
        "J Adolesc Health. 2019;65(1):86-93. doi:10.1016/j.jadohealth.2019.01.020.",
    "brown2024": "Brown C, Nkemjika S, Ratto J, Dube SR, Gilbert L, Chiang L, et al. Adverse "
        "childhood experiences and associations with mental health, substance use, and violence "
        "perpetration among young adults in sub-Saharan Africa. Child Abuse Negl. "
        "2024;150:106524. doi:10.1016/j.chiabu.2023.106524.",
    "zietz2020": "Zietz S, Kajula L, McNaughton Reyes HL, Moodley D, Maman S. Patterns of adverse "
        "childhood experiences and subsequent risk of interpersonal violence perpetration among "
        "men in Dar es Salaam, Tanzania. Child Abuse Negl. 2020;99:104256. "
        "doi:10.1016/j.chiabu.2019.104256.",
    "miedema2026": "Miedema SS, Matthews SA, Annor FB, Kress H, Massetti GM. Prevalence of "
        "violence perpetration by men aged 18-24 years in low- and middle-income countries who "
        "were exposed to violence during childhood, eight countries, 2018-2023. MMWR Morb Mortal "
        "Wkly Rep. 2026;75(3):41-6. doi:10.15585/mmwr.mm7503a2.",
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
    "tian2021": "Tian S, Zhang T, Chen X, Li Y, Xi B. Substance use and psychological distress "
        "among school-going adolescents in 41 low-income and middle-income countries. J Affect "
        "Disord. 2021;291:254-60. doi:10.1016/j.jad.2021.05.024.",
    "abio2020": "Abio A, Sezirahiga J, E Davis L, Wilson ML. Substance use and sociodemographic "
        "correlates among adolescents in a low-income sub-Saharan setting. J Inj Violence Res. "
        "2020;12(1):21-7. doi:10.5249/jivr.v12i1.1195.",
    "obeid2019": "Obeid S, Saade S, Haddad C, Sacre H, Khansa W, Al Hajj R, et al. Internet "
        "addiction among Lebanese adolescents: the role of self-esteem, anger, depression, "
        "anxiety, social anxiety and fear, impulsivity, and aggression, a cross-sectional study. "
        "J Nerv Ment Dis. 2019;207(10):838-46. doi:10.1097/NMD.0000000000001034.",
    "olejarnik2023": "Olejarnik SZ, Romano D. Is playing violent video games a risk factor for "
        "aggressive behaviour? Adding narcissism, self-esteem and PEGI ratings to the debate. "
        "Front Psychol. 2023;14:1155807. doi:10.3389/fpsyg.2023.1155807.",
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
        "[consultado a 16 de Setembro de 2026]. Disponível em: https://www.who.int/publications/m/"
        "item/adverse-childhood-experiences-international-questionnaire-(ace-iq).",
    "gshs": "Organização Mundial da Saúde. Global School-based Student Health Survey (GSHS) "
        "[Internet]. Genebra: Organização Mundial da Saúde; 2026 [consultado a 16 de Setembro de "
        "2026]. Disponível em: https://www.who.int/teams/noncommunicable-diseases/surveillance/"
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
