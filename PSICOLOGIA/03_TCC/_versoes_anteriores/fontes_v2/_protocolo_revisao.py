"""Seccoes 3 a 6 do protocolo: objectivos, hipoteses, justificativa e revisao da literatura."""
from docx.shared import Cm, Pt

from _protocolo_texto import ESTADO_DA_ARTE

OBJECTIVOS_ESPECIFICOS = [
    "Caracterizar o perfil sociodemográfico e escolar dos adolescentes dos 10 aos 19 anos da "
    "Escola Secundária de Muatala.",
    "Determinar o nível e o perfil do comportamento agressivo dos adolescentes, nas dimensões de "
    "agressão física, agressão verbal, ira e hostilidade, e nas formas reactiva e proactiva.",
    "Identificar os factores psicossociais do contexto familiar presentes nestes adolescentes, "
    "designadamente o funcionamento familiar, a supervisão parental, o castigo físico em casa e a "
    "exposição à violência entre os progenitores.",
    "Descrever os factores psicossociais do contexto escolar, do grupo de pares e da comunidade, "
    "incluindo a vitimização por bullying, a ligação à escola, a associação a pares desviantes, o "
    "consumo de substâncias psicoactivas e a exposição à violência comunitária.",
    "Analisar a associação entre os factores psicossociais estudados e o comportamento agressivo, "
    "identificando os factores que a ele se mantêm independentemente associados.",
]

HIPOTESES = [
    ("Hipótese nula (H0): não existe associação estatisticamente significativa entre os factores "
     "psicossociais estudados, dos níveis individual, familiar, escolar e do grupo de pares e "
     "comunitário, e o nível de comportamento agressivo dos adolescentes dos 10 aos 19 anos da "
     "Escola Secundária de Muatala."),
    ("Hipótese alternativa (H1): existe associação estatisticamente significativa entre os "
     "factores psicossociais estudados e o nível de comportamento agressivo destes adolescentes, "
     "apresentando os que foram expostos a castigo físico em casa, a violência entre os "
     "progenitores, a vitimização por bullying, a pares desviantes ou ao consumo de substâncias "
     "psicoactivas pontuações de agressividade mais elevadas."),
]


def escrever_objectivos(e):
    e.h1("3. OBJECTIVOS")
    e.h2("3.1. Objectivo geral")
    e.p("Analisar os factores psicossociais relacionados ao comportamento agressivo em "
        "adolescentes dos 10 aos 19 anos da Escola Secundária de Muatala, cidade de Nampula, no "
        "segundo semestre de 2026.")
    e.h2("3.2. Objectivos específicos")
    for objectivo in OBJECTIVOS_ESPECIFICOS:
        e.marca(objectivo)

    e.h1("4. HIPÓTESES DE INVESTIGAÇÃO")
    e.p("Sendo o desenho analítico, formulam-se hipóteses direccionadas, que serão testadas na "
        "análise inferencial descrita na metodologia.")
    for hipotese in HIPOTESES:
        e.p(hipotese)
    e.p("Subordinadas a estas, testam-se ainda as hipóteses operacionais de que a pontuação total "
        "de agressividade é superior nos rapazes, aumenta com o número de experiências adversas "
        "acumuladas e diminui à medida que aumentam o funcionamento familiar e a ligação à escola "
        "[[gershoff2016,blum2019,tian2019]].")


def escrever_justificativa(e):
    e.h1("5. JUSTIFICATIVA")
    e.p("A escolha deste tema justifica-se pela necessidade de compreender, com dados locais e "
        "instrumentos validados, um fenómeno que a escola vive quotidianamente mas que nunca foi "
        "medido. A pertinência do estudo articula-se em quatro dimensões complementares.")
    e.h2("5.1. Relevância científica")
    e.p("A investigação sobre agressividade em adolescentes moçambicanos é escassa e, quando "
        "existe, recorre a indicadores comportamentais isolados, como o envolvimento em lutas, e "
        "não a escalas psicométricas com propriedades conhecidas. Ao aplicar a forma reduzida do "
        "Questionário de Agressividade de Buss e Perry e o Questionário de Agressão Reactiva e "
        "Proactiva, ambos com versão portuguesa validada, o estudo produz medidas comparáveis com "
        "a literatura internacional e contribui com dados sobre o comportamento psicométrico "
        "destes instrumentos num contexto africano de língua portuguesa [[pechorro2016,"
        "pechorro2015]].")
    e.h2("5.2. Relevância académica")
    e.p("O trabalho responde a uma lacuna de conhecimento identificada na revisão da literatura e "
        "constitui uma base metodológica replicável noutras escolas da província de Nampula. Para "
        "o curso de Psicologia, oferece ainda um exercício completo de investigação quantitativa, "
        "da adaptação transcultural de instrumentos à modelação multivariável, e material didáctico "
        "para a formação em psicologia escolar e comunitária.")
    e.h2("5.3. Relevância social")
    e.p("O comportamento agressivo afecta directamente o percurso escolar e o bem-estar dos "
        "adolescentes, dos seus colegas e das famílias. Identificar os factores que o acompanham "
        "permite desenhar respostas que actuem sobre as causas e não apenas sobre as "
        "manifestações, beneficiando de imediato a comunidade escolar de Muatala. Num contexto em "
        "que apenas uma minoria dos adolescentes com sofrimento mental procura ajuda, a escola "
        "surge como porta de entrada privilegiada para a detecção e o encaminhamento [[king2026]].")
    e.h2("5.4. Relevância política")
    e.p("Os resultados fornecem evidência local para as políticas de protecção da criança e do "
        "adolescente conduzidas pelo Ministério da Educação e Desenvolvimento Humano "
        "(MINEDH) e pelo Ministério da Saúde (MISAU), e permitem alinhar a acção da escola "
        "com as estratégias INSPIRE "
        "recomendadas pela OMS, em particular as que dizem respeito à educação parental, aos "
        "ambientes escolares seguros e às competências socioemocionais [[inspire2016,"
        "oms_status2020]].")


def _conceitos_e_modelos_teoricos(e):
    e.h2("6.1. A adolescência como período crítico do desenvolvimento")
    e.p("A OMS define a adolescência como o período compreendido entre os 10 e os 19 anos, "
        "subdividido em adolescência inicial, dos 10 aos 14 anos, e adolescência tardia, dos 15 "
        "aos 19 anos [[oms_adolescente]]. É uma fase de reorganização biológica, cognitiva e "
        "social, marcada pela maturação assíncrona entre os sistemas cerebrais de recompensa, que "
        "amadurecem cedo, e os sistemas de controlo executivo, que amadurecem mais tarde. Esta "
        "assincronia ajuda a explicar a maior propensão para a tomada de risco e para as respostas "
        "impulsivas nesta idade. Metade das perturbações mentais que persistem na vida adulta "
        "manifesta-se antes dos 14 anos e três quartos antes dos 25, o que faz da adolescência a "
        "janela mais rentável para a prevenção [[oms_saude_mental]].")

    e.h2("6.2. Comportamento agressivo: conceito, dimensões e distinção de violência")
    e.p("Entende-se por comportamento agressivo qualquer conduta dirigida a outro indivíduo com a "
        "intenção de lhe causar dano, físico ou psicológico. A violência é uma forma extrema de "
        "agressão, definida pela OMS como o uso intencional da força física ou do poder que resulta "
        "ou tem elevada probabilidade de resultar em lesão, morte, dano psicológico ou privação "
        "[[krug2002]]. Nem toda a agressão é violência, mas toda a violência é agressão.")
    e.p("O modelo de Buss e Perry decompõe a agressividade em quatro dimensões: a agressão física "
        "e a agressão verbal, que constituem a componente instrumental ou motora; a ira, que "
        "corresponde à activação emocional e fisiológica; e a hostilidade, que representa a "
        "componente cognitiva, feita de ressentimento e de desconfiança [[buss1992]]. A esta "
        "estrutura sobrepõe-se a distinção funcional entre a agressão reactiva, impulsiva e "
        "defensiva, desencadeada por uma provocação percebida e acompanhada de activação "
        "emocional intensa, e a agressão proactiva, instrumental, planeada e dirigida à obtenção "
        "de um ganho, mais associada a traços de insensibilidade emocional [[raine2006]]. A "
        "distinção tem consequências práticas, porque as duas formas respondem a intervenções "
        "diferentes: a reactiva beneficia sobretudo do treino de regulação emocional e a proactiva "
        "de estratégias que alterem as contingências de reforço [[sukhodolsky2016,tordjman2022]].")

    e.h2("6.3. Modelos teóricos explicativos")
    e.p("A teoria da aprendizagem social sustenta que a agressão é, em larga medida, aprendida por "
        "observação. Os trabalhos clássicos de Bandura demonstraram que as crianças reproduzem "
        "condutas agressivas observadas em modelos adultos, sobretudo quando esses modelos não são "
        "punidos ou são recompensados pelo seu comportamento [[bandura1961]]. Daqui decorre a "
        "expectativa, largamente confirmada, de que o castigo físico e a violência testemunhada em "
        "casa aumentem a agressividade da criança, em vez de a reduzirem [[gershoff2016]].")
    e.p("O modelo ecológico adoptado pela OMS organiza os determinantes da violência em quatro "
        "níveis interdependentes: o individual, que reúne características biológicas e da história "
        "pessoal; o relacional, que abrange a família e o grupo de pares; o comunitário, que "
        "corresponde aos contextos de vida como a escola e o bairro; e o social, que integra as "
        "normas culturais e as políticas públicas [[krug2002]]. Este modelo estrutura o esquema "
        "conceptual do presente estudo e justifica a inclusão simultânea de variáveis dos vários "
        "níveis na análise multivariável.")
    e.p("O modelo do processamento da informação social completa esta leitura no plano cognitivo. "
        "Os adolescentes com elevada agressividade reactiva tendem a interpretar como hostis as "
        "intenções alheias em situações ambíguas, um enviesamento de atribuição hostil que se "
        "associa de forma consistente à agressividade e que é mais frequente em jovens com "
        "vinculação insegura [[xu2024]].")



def _magnitude_do_problema(e):
    e.h2("6.4. Magnitude do comportamento agressivo no adolescente")
    e.p("A prevalência é elevada e transversal aos continentes. Nos 68 países de baixo e médio "
        "rendimento analisados a partir dos inquéritos globais de saúde escolar, 36,4 por cento "
        "dos adolescentes dos 12 aos 15 anos envolveram-se em lutas físicas e 35,6 por cento "
        "sofreram agressão física nos doze meses anteriores, com valores muito superiores nos "
        "rapazes, 45,5 por cento contra 26,9 por cento nas raparigas, no caso das lutas "
        "[[han2019]]. Na África subsariana, a análise agrupada de oito países estimou a prevalência "
        "de violência interpessoal em 53,7 por cento e identificou como preditores a vitimização "
        "por bullying, o absentismo escolar e o consumo de álcool e de tabaco, enquanto o apoio dos "
        "pares e a ligação parental funcionaram como factores protectores [[aboagye2021a]].")
    e.p("Os estudos africanos de base escolar confirmam o padrão. Na Etiópia e no Egipto, a "
        "vitimização por bullying associou-se ao sexo masculino, ao consumo de substâncias e à "
        "disfunção familiar [[tarafa2022,sweidan2024]]. No Malawi, 42,4 por cento das raparigas e "
        "36,4 por cento dos rapazes relataram castigo físico na escola, e essa exposição associou-se "
        "a problemas de externalização [[ameli2017]]. Em quatro países de baixos recursos, a "
        "vitimização por bullying mostrou-se associada a pior funcionamento emocional e escolar "
        "[[nguyen2020]]. Na Nigéria, a adversidade vivida na infância predisse a perpetração de "
        "bullying, com mediação pela influência dos pares [[ugwu2024]].")



def _factores_familiares(e):
    e.h2("6.5. Factores psicossociais do contexto familiar")
    e.p("A família é o primeiro contexto de aprendizagem da regulação emocional e do "
        "relacionamento. A meta-análise de 75 estudos, abrangendo mais de 160 mil crianças, "
        "concluiu que o castigo físico se associa a maior agressividade, a mais problemas de "
        "comportamento e a pior saúde mental, sem qualquer benefício documentado em termos de "
        "obediência a longo prazo [[gershoff2016]]. Ao nível populacional, o estudo ecológico de 88 "
        "países mostrou que os países com proibição total do castigo corporal, na escola e em casa, "
        "apresentam 69 por cento da taxa de lutas frequentes nos rapazes e 42 por cento nas "
        "raparigas, quando comparados com os países sem qualquer proibição [[elgar2018]].")
    e.p("Para além da punição, pesam a qualidade do funcionamento familiar e o estilo de "
        "parentalidade. Famílias com baixa coesão e comunicação deficitária associam-se a maior "
        "agressividade nos adolescentes [[henneberger2016]], e o controlo psicológico parental, "
        "que substitui a supervisão pela manipulação afectiva, aumenta a agressividade por via da "
        "associação a pares desviantes [[tian2019]]. A ausência parental, por migração laboral, "
        "separação ou morte, é reconhecida como experiência adversa autónoma na África subsariana "
        "e associa-se a pior saúde mental e a maior risco de violência [[annor2024]].")
    e.p("A acumulação de experiências adversas é particularmente relevante. Em adolescentes dos 10 "
        "aos 14 anos de catorze países, o número de experiências adversas relacionou-se de forma "
        "gradual com os sintomas depressivos e com a perpetração de violência [[blum2019]]. Na "
        "África subsariana, a análise dos inquéritos nacionais mostrou que as experiências adversas "
        "se associam a sofrimento mental, a consumo de substâncias e à perpetração de violência na "
        "idade adulta jovem [[brown2024]], e em Dar es Salaam identificaram-se padrões específicos "
        "de adversidade que antecipam a perpetração de violência interpessoal [[zietz2020]]. Em "
        "oito países de baixo e médio rendimento, os homens dos 18 aos 24 anos expostos a violência "
        "durante a infância apresentaram maior prevalência de perpetração de violência "
        "[[miedema2026]]. A polivitimização, isto é, a exposição simultânea a várias formas de "
        "violência, agrava de forma consistente este risco [[palermo2019]].")



def _factores_escolares_e_individuais(e):
    e.h2("6.6. Factores psicossociais do contexto escolar e do grupo de pares")
    e.p("A escola pode ser factor de protecção ou de risco. A ligação à escola, entendida como o "
        "sentimento de pertença e a percepção de apoio por parte dos professores, atenua o efeito "
        "dos factores familiares adversos sobre a agressividade [[tian2019]]. Em sentido contrário, "
        "a vitimização por bullying é um dos preditores mais robustos do comportamento agressivo, "
        "estabelecendo-se com frequência um ciclo em que a vítima se torna também agressora "
        "[[aboagye2021a,aboagye2021b]].")
    e.p("O grupo de pares assume, na adolescência, um papel normativo que rivaliza com o da "
        "família. A associação a pares desviantes prediz de forma prospectiva o aumento da "
        "agressividade, sobretudo nos adolescentes com menor autocontrolo [[li2024]], e medeia a "
        "relação entre a vitimização sofrida e os comportamentos problemáticos subsequentes, com a "
        "impulsividade a funcionar como moderador [[zhu2016]]. Este conjunto de resultados sustenta "
        "a inclusão, no presente estudo, de indicadores de vitimização, de ligação à escola e de "
        "afiliação a pares desviantes.")

    e.h2("6.7. Factores individuais e consumo de substâncias psicoactivas")
    e.p("O sexo masculino e a idade mais avançada dentro do intervalo adolescente associam-se "
        "sistematicamente a pontuações mais elevadas de agressão física [[han2019]]. A baixa "
        "auto-estima, os sintomas depressivos e ansiosos e a impulsividade aparecem associados à "
        "ira e à hostilidade, tendo sido documentada, em adolescentes libaneses, a associação entre "
        "estas variáveis, a agressividade e o uso problemático da Internet [[obeid2019]].")
    e.p("O consumo de álcool e de outras substâncias merece destaque pela sua dupla condição de "
        "factor de risco e de consequência. Em 41 países de baixo e médio rendimento, o consumo de "
        "substâncias associou-se a sofrimento psicológico nos adolescentes escolarizados "
        "[[tian2021]], e a análise dos inquéritos globais mostrou prevalências elevadas de consumo "
        "de álcool nesta faixa etária [[ma2018]]. Em contexto subsariano de baixo rendimento, o "
        "consumo associou-se a factores sociodemográficos identificáveis e a comportamentos de "
        "risco concomitantes [[abio2020]]. Em Moçambique, quase um terço dos jovens dos 13 aos 24 "
        "anos declarou consumir álcool [[sema2025]].")
    e.p("A exposição a conteúdos violentos nos média e nos jogos electrónicos é um factor "
        "frequentemente invocado, mas de efeito controverso e de magnitude modesta, "
        "condicionado por variáveis de personalidade como o narcisismo e a auto-estima "
        "[[olejarnik2023]]. Neste estudo será medida como variável de exposição, sem pressuposto "
        "de causalidade.")



def _factores_comunitarios_e_prevencao(e):
    e.h2("6.8. Factores comunitários e socioculturais")
    e.p("A exposição à violência na comunidade normaliza a agressão como forma legítima de "
        "resolução de conflitos. Em Moçambique, 45,9 por cento das raparigas e 66,7 por cento dos "
        "rapazes dos 18 aos 24 anos testemunharam violência na comunidade antes dos 18 anos, e "
        "cerca de um terço dos adolescentes dos 13 aos 17 anos presenciou episódios semelhantes nos "
        "doze meses anteriores ao inquérito [[vacs2019]]. A investigação a nível continental "
        "mostrou ainda que a memória histórica da violência política se associa a maiores níveis de "
        "violência interpessoal contra crianças e jovens nas zonas afectadas [[vigneri2026]], um "
        "aspecto com particular pertinência no contexto moçambicano [[igreja2024]]. A pobreza do "
        "agregado, as normas de género que toleram a agressividade masculina e a disponibilidade "
        "de álcool completam o quadro dos determinantes distais [[krug2002,amene2024]].")

    e.h2("6.9. Consequências e estratégias de prevenção")
    e.p("A agressividade persistente na adolescência associa-se a insucesso e abandono escolar, a "
        "perturbações do comportamento, a consumo de substâncias, a envolvimento com a justiça e a "
        "pior saúde mental na idade adulta [[scott2018,tordjman2022]]. As intervenções com "
        "evidência de eficácia são de natureza psicossocial e não farmacológica: o treino de "
        "competências de resolução de problemas, a reestruturação cognitiva e o treino parental "
        "reduzem de forma consistente a ira, a irritabilidade e a agressão em crianças e "
        "adolescentes [[sukhodolsky2016]]. No plano das políticas, o pacote INSPIRE da OMS reúne "
        "sete estratégias, entre as quais a aplicação da lei, as normas e valores, os ambientes "
        "seguros, o apoio aos pais e cuidadores e o desenvolvimento de competências para a vida "
        "[[inspire2016]], cuja implementação é monitorizada no relatório global sobre a prevenção "
        "da violência contra as crianças [[oms_status2020]].")



def _instrumentos_de_avaliacao(e):
    e.h2("6.10. Instrumentos de avaliação")
    e.p("O Questionário de Agressividade de Buss e Perry (Buss-Perry Aggression Questionnaire, "
        "BPAQ) é o instrumento de auto-relato mais utilizado na avaliação da agressividade, na "
        "sua versão original de 29 itens e na forma reduzida de 12 itens (BPAQ-SF), que preserva "
        "a estrutura de quatro factores e apresenta propriedades psicométricas adequadas na "
        "população juvenil portuguesa [[buss1992,pechorro2016]]. O Questionário de Agressão "
        "Reactiva e Proactiva (Reactive-Proactive Aggression Questionnaire, RPQ), com 23 itens, "
        "permite separar as duas formas funcionais de agressão, tem validação portuguesa e "
        "validação transcultural em amostras de vários continentes "
        "[[raine2006,pechorro2015,tuvblad2016]].")
    e.p("Para os factores psicossociais recorre-se a instrumentos igualmente consolidados: a "
        "escala de funcionamento familiar de Smilkstein (APGAR), com cinco itens, avalia "
        "a percepção do funcionamento familiar nas dimensões de adaptação, participação, "
        "crescimento, afecto e resolução [[smilkstein1978]]; o questionário internacional de "
        "experiências adversas na infância da OMS (Adverse Childhood Experiences International "
        "Questionnaire, ACE-IQ) fornece itens padronizados sobre castigo físico, violência "
        "testemunhada e negligência [[aceiq]]; o inquérito global de saúde escolar disponibiliza "
        "módulos validados sobre bullying, lutas físicas, supervisão parental e consumo de "
        "substâncias, o que permite a comparação directa com os dados de outros países africanos "
        "[[gshs]]; e a subescala de sintomas emocionais do Questionário de Capacidades e de "
        "Dificuldades (Strengths and Difficulties Questionnaire, SDQ) avalia a componente "
        "internalizante do sofrimento psicológico [[goodman1997]].")



def _estado_da_arte_e_esquema(e, h, doc, caminho_figura):
    e.h2("6.11. Estado da arte")
    e.p("O quadro seguinte sintetiza os principais estudos que fundamentam este protocolo, "
        "organizados pela ordem em que foram discutidos nas secções anteriores. Nos estudos "
        "analíticos, a força de cada associação é expressa pelo odds ratio ajustado (aOR), isto "
        "é, depois de controladas as restantes variáveis do modelo.")
    h.tabela(doc, "Quadro 1: Síntese dos estudos que fundamentam o protocolo.",
             ["Autor (ano)", "Local", "Método (amostra)", "Principais resultados"],
             [[e.resolver(celula) for celula in linha] for linha in ESTADO_DA_ARTE],
             "Fonte: o autor, 2026.",
             larguras=[Cm(3.0), Cm(2.8), Cm(3.6), Cm(6.6)])
    e.p("A leitura conjunta destes trabalhos revela três lacunas que o presente estudo procura "
        "colmatar. Em primeiro lugar, quase toda a evidência africana assenta em indicadores "
        "comportamentais isolados, como o envolvimento em lutas, e não em escalas psicométricas de "
        "agressividade. Em segundo lugar, os estudos moçambicanos disponíveis são de âmbito "
        "nacional ou circunscrevem-se ao sul do país, faltando dados da região norte e, em "
        "particular, do meio escolar periurbano. Em terceiro lugar, raramente se testam em "
        "simultâneo factores dos quatro níveis do modelo ecológico, o que impede saber quais se "
        "mantêm associados depois do ajustamento mútuo.")

    e.h2("6.12. Esquema conceptual do problema")
    e.p("A figura seguinte representa as relações que o estudo se propõe examinar. Os factores "
        "psicossociais estão organizados pelos quatro níveis do modelo ecológico e são testados "
        "quanto à sua associação com o comportamento agressivo, medido nas dimensões do "
        "questionário de Buss e Perry e nas formas reactiva e proactiva [[krug2002,buss1992,"
        "raine2006]].")
    h.figura(doc, caminho_figura,
             "Figura 1: Esquema conceptual dos factores psicossociais associados ao comportamento "
             "agressivo no adolescente, segundo os níveis do modelo ecológico.", largura=Cm(15.5))
    h.paragrafo(doc, "Fonte: o autor, 2026, com base no modelo ecológico da Organização Mundial da "
                "Saúde.", tamanho=Pt(10), espaco=1.0)


def escrever_revisao(e, h, doc, caminho_figura):
    """Seccao 6 completa, montada a partir dos blocos tematicos acima."""
    e.h1("6. REVISÃO DA LITERATURA")
    _conceitos_e_modelos_teoricos(e)
    _magnitude_do_problema(e)
    _factores_familiares(e)
    _factores_escolares_e_individuais(e)
    _factores_comunitarios_e_prevencao(e)
    _instrumentos_de_avaliacao(e)
    _estado_da_arte_e_esquema(e, h, doc, caminho_figura)
