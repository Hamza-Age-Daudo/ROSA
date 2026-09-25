"""Seccoes 3 a 6 do protocolo: objectivos, hipoteses, justificativa e revisao da literatura."""
from docx.shared import Cm, Pt

from _protocolo_texto import ESTADO_DA_ARTE

OBJECTIVOS_ESPECIFICOS = [
    "Caracterizar o perfil sociodemográfico e escolar dos adolescentes dos 10 aos 19 anos da "
    "Escola Secundária de Muatala.",
    "Determinar o nível e o perfil do comportamento agressivo dos adolescentes, nas dimensões de "
    "agressão física, agressão verbal, ira e hostilidade e nas formas reactiva e proactiva, e "
    "estimar a prevalência de envolvimento em violência interpessoal e de participação em lutas "
    "físicas nos últimos 12 meses e a proporção de adolescentes acima do ponto de corte de "
    "rastreio para problemas de comportamento.",
    "Avaliar os factores psicológicos individuais dos adolescentes, designadamente as "
    "dificuldades de regulação emocional, a hiperactividade e desatenção, os sintomas "
    "emocionais, os sintomas de stress pós-traumático, a auto-estima e o comportamento "
    "pró-social.",
    "Identificar os factores psicossociais do contexto familiar, escolar, do grupo de pares e da "
    "comunidade a que estes adolescentes estão expostos, incluindo o funcionamento familiar, o "
    "castigo físico, a violência testemunhada, a vitimização por bullying e a afiliação a pares "
    "desviantes, e descrever o consumo de substâncias psicoactivas.",
    "Analisar a associação entre os factores psicológicos e psicossociais estudados e o "
    "comportamento agressivo, identificando os que a ele se mantêm independentemente associados "
    "e examinando se a associação entre a exposição à violência e a agressão comportamental é "
    "compatível "
    "com um efeito indirecto, em sentido estatístico, através das dificuldades de regulação "
    "emocional.",
]

HIPOTESES = [
    ("Hipótese nula (H0): na população de adolescentes dos 10 aos 19 anos da Escola Secundária de "
     "Muatala, os factores psicológicos individuais e os factores psicossociais do contexto "
     "familiar, escolar, do grupo de pares e comunitário não estão associados ao nível de "
     "comportamento agressivo."),
    ("Hipótese alternativa (H1): nessa população, estes factores estão associados ao nível de "
     "comportamento agressivo. Espera-se que obtenham pontuações de agressividade mais elevadas "
     "os adolescentes com maiores dificuldades de regulação emocional, mais hiperactividade e "
     "desatenção, mais sintomas emocionais e de stress pós-traumático, menor auto-estima e menor "
     "comportamento pró-social, bem como os expostos a castigo físico, a violência entre os "
     "adultos do agregado, a vitimização por bullying ou a pares desviantes e os que consomem "
     "substâncias psicoactivas."),
]


def escrever_objectivos(e):
    e.h1("3. OBJECTIVOS")
    e.h2("3.1. Objectivo geral")
    e.p("Analisar os factores psicossociais, com destaque para os factores psicológicos "
        "individuais, relacionados com o comportamento agressivo em adolescentes dos 10 aos 19 "
        "anos da Escola Secundária de Muatala, cidade de Nampula, no segundo semestre de 2026.")
    e.h2("3.2. Objectivos específicos")
    for objectivo in OBJECTIVOS_ESPECIFICOS:
        e.marca(objectivo)

    e.h1("4. HIPÓTESES DE INVESTIGAÇÃO")
    e.p("Sendo o desenho analítico, formulam-se hipóteses direccionadas, que serão testadas na "
        "análise inferencial descrita na metodologia.")
    for hipotese in HIPOTESES:
        e.p(hipotese)
    e.p("Subordinadas a estas, testam-se três hipóteses operacionais; a primeira e a terceira "
        "constituem as análises confirmatórias do estudo e a segunda, de mediação, tem carácter "
        "exploratório. A primeira é a de que, controlando a outra forma de agressão, a agressão "
        "reactiva se associa mais fortemente do que a proactiva às dificuldades de regulação "
        "emocional, aos sintomas emocionais e aos sintomas de stress pós-traumático, e a agressão "
        "proactiva mais fortemente ao baixo comportamento pró-social [[raine2006,card2006]]. A "
        "segunda é a de que parte da associação entre a exposição à violência em casa, na escola "
        "e na comunidade e a componente comportamental da agressão, isto é, a agressão física e "
        "verbal, é compatível com um efeito indirecto através das dificuldades de regulação "
        "emocional [[roberton2012,heleniak2016]]. A terceira é a de que as agressões física e "
        "verbal são superiores nos rapazes [[buss1992,card2008]]. Examinam-se ainda, de forma "
        "exploratória, a associação da agressividade com o número de experiências adversas "
        "acumuladas [[blum2019]], o funcionamento familiar [[henneberger2016]] e a ligação à "
        "escola [[tian2019]].")


def escrever_justificativa(e):
    e.h1("5. JUSTIFICATIVA")
    e.p("A escolha deste tema nasceu da observação, em 2025, de numerosos episódios de "
        "agressividade entre os alunos da Escola Secundária de Muatala e de uma pergunta de "
        "natureza clínica sobre o que sustenta estes comportamentos. A resposta disciplinar "
        "descreve o acto; a psicologia clínica procura compreender as emoções, as cognições e as "
        "experiências que o sustentam, porque é sobre elas que a intervenção pode actuar. A "
        "pertinência do estudo articula-se em quatro dimensões complementares.")
    e.h2("5.1. Relevância científica")
    e.p("A investigação sobre agressividade em adolescentes moçambicanos é escassa e, quando "
        "existe, recorre a indicadores comportamentais isolados, como o envolvimento em lutas, sem "
        "escalas psicométricas com propriedades conhecidas nem avaliação dos mecanismos "
        "psicológicos. Ao combinar a forma reduzida do Questionário de Agressividade de Buss e "
        "Perry e o Questionário de Agressão Reactiva e Proactiva, ambos com versão portuguesa "
        "validada, com medidas de regulação emocional, de sintomas psicológicos e de auto-estima, "
        "o estudo testa num contexto africano de língua portuguesa modelos explicativos "
        "construídos sobretudo noutros continentes e produz dados sobre o comportamento "
        "psicométrico destes instrumentos [[pechorro2016,pechorro2015,kaufman2016]].")
    e.h2("5.2. Relevância académica")
    e.p("Para o curso de Psicologia, e em particular para a formação em psicologia clínica, o "
        "trabalho oferece um exercício completo de avaliação psicológica em contexto comunitário, "
        "da selecção e adaptação transcultural de instrumentos à análise dos mecanismos que "
        "ligam a experiência de violência ao comportamento. Responde ainda a uma lacuna de "
        "conhecimento identificada na revisão da literatura e constitui uma base metodológica "
        "replicável noutras escolas da província de Nampula e em serviços de saúde que atendem "
        "adolescentes.")
    e.h2("5.3. Relevância social")
    e.p("O comportamento agressivo afecta directamente o percurso escolar e o bem-estar dos "
        "adolescentes, dos seus colegas e das famílias, e é muitas vezes a face visível de um "
        "sofrimento psicológico que não chega aos serviços de saúde. Identificar os factores "
        "psicológicos que o acompanham permite passar de uma resposta apenas punitiva para uma "
        "resposta que inclua a detecção, o encaminhamento e o tratamento. Num contexto em que, em "
        "duas escolas de Maputo, só 2,7 por cento dos adolescentes com perturbação mental tinham "
        "procurado cuidados [[king2026]] e em que, em 2014, o sistema de saúde contava apenas 109 psicólogos e 10 "
        "psiquiatras [[dossantos2016]], a informação produzida ajuda a orientar recursos escassos "
        "para os alvos de maior benefício.")
    e.h2("5.4. Relevância política")
    e.p("Os resultados fornecem evidência local para as políticas de saúde mental e de protecção "
        "da criança e do adolescente conduzidas pelo Ministério da Saúde (MISAU) e pelo "
        "Ministério da Educação e Cultura (MEC), nomeadamente para a "
        "integração dos cuidados de saúde mental nos serviços destinados a adolescentes, "
        "prevista no guia de intervenção da OMS para as perturbações mentais nos cuidados não "
        "especializados [[oms_mhgap]]. Permitem ainda alinhar a acção da escola com o pacote de "
        "sete estratégias da OMS para pôr fim à violência contra as crianças (INSPIRE), em "
        "particular as que dizem respeito ao apoio aos pais, aos ambientes escolares seguros e "
        "às competências socioemocionais [[inspire2016]].")


def _conceitos_e_modelos_teoricos(e):
    e.h2("6.1. A adolescência como período crítico do desenvolvimento")
    e.p("A OMS define a adolescência como o período compreendido entre os 10 e os 19 anos, que se "
        "costuma subdividir em dois grupos, dos 10 aos 14 e dos 15 aos 19 anos "
        "[[oms_adolescente]]. É uma fase de reorganização biológica, cognitiva e social, em que o "
        "sistema socioemocional do cérebro, ligado à procura de recompensa, se transforma por "
        "volta da puberdade, enquanto o sistema de controlo cognitivo, responsável pela "
        "auto-regulação, amadurece de forma mais lenta até ao início da idade adulta. Estes "
        "calendários desencontrados tornam o meio da adolescência um período de maior "
        "vulnerabilidade a comportamentos impulsivos e de risco, sobretudo na presença dos pares "
        "[[steinberg2008]].")
    e.p("É também o período em que surge grande parte da psicopatologia. Uma meta-análise de 192 "
        "estudos epidemiológicos, com mais de 700 mil participantes, estimou que 34,6 por cento "
        "das perturbações mentais têm início antes dos 14 anos, 48,4 por cento antes dos 18 e "
        "62,5 por cento antes dos 25, com um pico de início aos 14,5 anos [[solmi2022]]. Na "
        "perspectiva da psicopatologia do desenvolvimento, o comportamento agressivo que surge "
        "nesta idade deve ser lido à luz da história de vida do adolescente e das tarefas de "
        "desenvolvimento que enfrenta, e não apenas como transgressão [[sroufe1984]]. É, por "
        "isso, a janela em que a detecção e a intervenção psicológica têm maior potencial de "
        "prevenir trajectórias persistentes.")

    e.h2("6.2. Comportamento agressivo: conceito, dimensões e funções")
    e.p("Entende-se por comportamento agressivo qualquer conduta dirigida a outro indivíduo com a "
        "intenção imediata de lhe causar dano, físico ou psicológico, e por violência a forma de "
        "agressão que tem por objectivo um dano extremo [[anderson2002]]. A OMS adopta uma "
        "definição mais ampla de violência, como o uso intencional da força física ou do poder, "
        "real ou em ameaça, contra si próprio, contra outra pessoa ou contra um grupo ou "
        "comunidade, que resulte ou tenha elevada probabilidade de resultar em lesão, morte, dano "
        "psicológico, deficiência de desenvolvimento ou privação [[krug2002]]. Neste protocolo, "
        "como no inquérito global de saúde escolar, a violência interpessoal designa o "
        "envolvimento em lutas físicas ou a agressão física sofrida nos últimos 12 meses, e não "
        "apenas as formas extremas de agressão.")
    e.p("O modelo de Buss e Perry decompõe a agressividade em quatro dimensões: a agressão física "
        "e a agressão verbal, que constituem a componente motora ou comportamental; a ira, que "
        "corresponde à activação emocional e fisiológica; e a hostilidade, que representa a "
        "componente cognitiva, feita de ressentimento e de desconfiança [[buss1992]]. A esta "
        "estrutura sobrepõe-se a distinção funcional proposta por Dodge e Coie entre a agressão "
        "reactiva, impulsiva e defensiva, desencadeada por uma provocação percebida e acompanhada "
        "de raiva intensa, e a agressão proactiva, instrumental, planeada e dirigida à obtenção de "
        "um ganho [[dodge1987]]. Os dois tipos têm correlatos diferentes: a agressão reactiva "
        "associa-se sobretudo à impulsividade, à hostilidade e à ansiedade social, e a proactiva à "
        "personalidade psicopática, ao afecto embotado, à delinquência e à violência grave "
        "[[raine2006]]. A distinção tem consequências clínicas: a agressão reactiva, movida pela "
        "raiva, é o alvo privilegiado das intervenções cognitivo-comportamentais de regulação da "
        "raiva e de resolução de problemas sociais [[sukhodolsky2016]], enquanto na agressão "
        "proactiva ganham peso os traços de insensibilidade emocional, com implicações próprias "
        "para o tratamento [[frick2014]].")


def _perspectiva_clinica(e):
    e.h2("6.3. Perspectiva clínica: a agressividade na psicopatologia do adolescente")
    e.p("Nos sistemas de classificação em uso, a agressividade atravessa várias categorias "
        "diagnósticas. No Manual de Diagnóstico e Estatística das Perturbações Mentais, na "
        "quinta edição revista, integra os critérios da perturbação do comportamento, definida por "
        "um padrão persistente de violação dos direitos dos outros e das normas sociais, que "
        "inclui agressão a pessoas e a animais, e da perturbação explosiva intermitente, "
        "caracterizada por explosões agressivas recorrentes, desproporcionadas em relação à "
        "provocação. Relaciona-se ainda com a perturbação de oposição e desafio, marcada por "
        "humor zangado e irritável, comportamento argumentativo e desafiante e vingança, mas sem "
        "a agressão física a pessoas ou a animais própria da perturbação do comportamento "
        "[[apa2022]]. Na Classificação Internacional de Doenças, 11.ª revisão, a perturbação de "
        "oposição e desafio pode ser especificada com irritabilidade e raiva crónicas, e esta e a "
        "perturbação do comportamento dissocial admitem o qualificador com emoções pró-sociais "
        "limitadas [[oms_cid11]]. A perturbação do comportamento "
        "afecta cerca de 3 por cento das crianças em idade escolar, é duas vezes mais frequente "
        "no sexo masculino, coexiste com frequência com a perturbação de hiperactividade e défice "
        "de atenção e associa-se a alterações nos circuitos cerebrais do processamento e da "
        "regulação das emoções [[fairchild2019]]. Numa meta-análise mundial, as perturbações "
        "disruptivas atingiram 5,7 por cento das crianças e adolescentes, valor próximo do das "
        "perturbações de ansiedade, de 6,5 por cento [[polanczyk2015]].")
    e.p("Três conceitos clínicos ajudam a compreender a heterogeneidade destes quadros. O "
        "primeiro é a idade de início: a taxonomia de Moffitt distingue um comportamento "
        "anti-social persistente ao longo da vida, que começa na infância e se associa a défices "
        "neuropsicológicos e a ambientes adversos, de um comportamento limitado à adolescência, "
        "mais frequente e ligado à procura de autonomia e à influência dos pares [[moffitt1993]]. "
        "O segundo são os traços de insensibilidade emocional, ou seja, a falta de culpa, de "
        "empatia e de expressão afectiva, que definem um subgrupo com agressão mais grave, mais "
        "instrumental e mais persistente, reconhecido no especificador de emoções pró-sociais "
        "limitadas da perturbação do comportamento [[frick2014]]. O terceiro é a irritabilidade "
        "crónica, dimensão transdiagnóstica que se situa na fronteira entre o comportamento "
        "disruptivo e a psicopatologia afectiva e que prediz, na idade adulta, depressão, "
        "ansiedade e comportamento suicidário [[leibenluft2013]]; no Manual de Diagnóstico e "
        "Estatística das Perturbações Mentais, tem expressão própria na perturbação de "
        "desregulação disruptiva do humor, caracterizada por explosões de raiva graves e "
        "recorrentes sobre um humor persistentemente irritável, com início antes dos 10 anos "
        "[[apa2022]].")
    e.p("A agressividade surge também como comorbilidade. Mais de metade dos pré-adolescentes com "
        "perturbação de hiperactividade e défice de atenção de apresentação combinada apresenta "
        "agressividade clinicamente significativa, predominantemente impulsiva, o que agrava o "
        "prognóstico [[saylor2016]]. Do ponto de vista neurobiológico, a agressão impulsiva "
        "associada à raiva resulta da activação do sistema de resposta à ameaça, centrado na "
        "amígdala e no hipotálamo, quando as regiões pré-frontais que seleccionam a resposta não "
        "conseguem modulá-lo [[blair2016]]. Estes dados justificam que o presente estudo avalie, "
        "ao lado da agressividade, a desatenção e a hiperactividade, os sintomas emocionais, os "
        "sintomas de stress pós-traumático e o comportamento pró-social.")


def _modelos_teoricos(e):
    e.h2("6.4. Modelos teóricos explicativos")
    e.p("A teoria da aprendizagem social sustenta que a agressão é, em larga medida, aprendida por "
        "observação. Os trabalhos clássicos de Bandura demonstraram que as crianças reproduzem "
        "condutas agressivas observadas em modelos adultos [[bandura1961]]. Daqui decorre a "
        "expectativa, largamente confirmada, de que o castigo físico [[gershoff2016]] e a violência "
        "sofrida ou testemunhada na infância [[brown2024]] se associem a maior agressividade, em "
        "vez de a reduzirem.")
    e.p("A reformulação da hipótese frustração-agressão, proposta por Berkowitz, explica a "
        "agressão de tipo reactivo: acontecimentos aversivos, como a frustração, a dor ou a "
        "provocação, geram afecto negativo, que activa de forma automática pensamentos, "
        "recordações e tendências de acção associados à raiva e à agressão [[berkowitz1989]]. "
        "O modelo do processamento da informação social descreve os passos cognitivos que "
        "medeiam a resposta a uma situação social, da codificação e interpretação das pistas à "
        "escolha e avaliação da resposta, e mostra que os adolescentes agressivos tendem a "
        "interpretar como hostis as intenções alheias em situações ambíguas [[crick1994]]. Num "
        "estudo com 1.299 crianças de 12 grupos culturais de nove países, incluindo o Quénia, "
        "a atribuição de intenção hostil predisse a agressão reactiva em todos os grupos e "
        "explicou parte das diferenças entre culturas nos problemas de agressividade "
        "[[dodge2015]].")
    e.p("O Modelo Geral da Agressão integra estas teorias num quadro único. Os factores da "
        "pessoa, como os traços, as atitudes e as experiências passadas, e os da situação, como a "
        "provocação, a frustração ou a presença de pistas agressivas, influenciam o estado "
        "interno do indivíduo, composto por cognições, afecto e activação fisiológica; este, por "
        "sua vez, condiciona os processos de avaliação e de decisão que conduzem, ou não, ao acto "
        "agressivo [[anderson2002]]. Cada episódio funciona como uma aprendizagem que reforça as "
        "estruturas de conhecimento agressivas, e os factores ambientais persistentes, como a "
        "violência na família e no bairro, moldam a personalidade através dessas estruturas "
        "[[allen2018]]. Este modelo fundamenta o esquema conceptual do presente estudo, em que "
        "os contextos de vida funcionam como factores distais e as características psicológicas "
        "do adolescente como factores proximais do comportamento agressivo.")
    e.p("O modelo biopsicossocial, proposto por Engel como alternativa ao modelo biomédico, "
        "lembra que o sofrimento e o comportamento resultam da interacção de factores "
        "biológicos, psicológicos e sociais [[engel1977]], e o modelo ecológico adoptado pela "
        "OMS organiza os determinantes sociais da violência nos níveis individual, relacional, "
        "comunitário e social [[krug2002]]. Os dois modelos justificam a inclusão simultânea, na "
        "análise, de variáveis psicológicas e de variáveis dos vários contextos de vida.")


def _mecanismos_psicologicos(e):
    e.h2("6.5. Mecanismos psicológicos individuais")
    e.p("A regulação emocional, isto é, a capacidade de reconhecer, compreender e aceitar as "
        "emoções, de controlar o comportamento quando se está perturbado, de forma ajustada aos "
        "objectivos, e de recorrer de forma flexível a estratégias adequadas para modular a "
        "intensidade e a duração das respostas emocionais [[gratz2004]], é um mecanismo "
        "central. As dificuldades de regulação aumentam a probabilidade de "
        "agressão porque intensificam e prolongam a raiva, reduzem o controlo dos impulsos e "
        "diminuem a capacidade de escolher respostas alternativas [[roberton2012]]. Num estudo "
        "prospectivo com 1.065 adolescentes, a desregulação emocional predisse o aumento do "
        "comportamento agressivo sete meses depois, mesmo controlando o nível inicial, ao passo "
        "que a agressividade não predisse o aumento da desregulação [[mclaughlin2011]]. A "
        "regulação emocional é também o elo que liga a adversidade à psicopatologia: em "
        "crianças e adolescentes, os maus-tratos associaram-se a maior reactividade emocional, "
        "a ruminação e a respostas impulsivas perante o sofrimento, e estas dificuldades "
        "intermediaram a associação entre os maus-tratos e os sintomas externalizantes "
        "[[heleniak2016,kim2010]]. Esta evidência fundamenta a hipótese de mediação do presente "
        "estudo.")
    e.p("A cognição social é o segundo mecanismo. A associação entre a atribuição de intenção "
        "hostil e a agressão foi confirmada em três meta-análises. A de Verhoef e colaboradores, "
        "com 111 estudos e mais de 29 mil participantes, encontrou-a mais forte quando a "
        "situação envolve maior activação emocional [[decastro2002,verhoef2019]], e a de Xu e "
        "colaboradores, com 118 estudos, encontrou uma correlação de 0,30 entre este enviesamento e a agressão, mais "
        "forte na agressão reactiva, e mostrou que ele intermedeia a relação entre a segurança da "
        "vinculação aos pais e o comportamento agressivo [[xu2024]], embora a meta-análise de "
        "Verhoef e colaboradores não tenha encontrado essa diferença entre as formas de agressão "
        "[[verhoef2019]].")
    e.p("A exposição à violência e o trauma constituem o terceiro mecanismo. Numa meta-análise "
        "de 114 estudos, a exposição à violência comunitária teve os efeitos mais fortes sobre o "
        "stress pós-traumático e os problemas externalizantes, e os adolescentes mostraram uma "
        "relação mais forte do que as crianças entre essa exposição e os comportamentos "
        "externalizantes [[fowler2009]]. Os adolescentes expostos a múltiplas formas de "
        "vitimização têm maior risco de perturbação psiquiátrica e de envolvimento em "
        "delinquência com pares delinquentes [[ford2010]]. No stress pós-traumático, os sintomas "
        "de activação e de reactividade, isto é, a irritabilidade, as explosões de raiva e a "
        "hipervigilância, são os que mais directamente se ligam à agressão reactiva [[apa2022]], "
        "o que faz dos sintomas pós-traumáticos uma variável clínica a avaliar em contextos de "
        "elevada violência como o moçambicano.")
    e.p("A auto-estima, a empatia e o comportamento pró-social completam o quadro. Em três "
        "estudos com adolescentes e estudantes universitários, a baixa auto-estima associou-se "
        "à agressão, de forma transversal e longitudinal e independentemente do narcisismo "
        "[[donnellan2005]]. A relação entre a empatia e a agressão é, pelo contrário, mais fraca "
        "do que se supunha, com uma correlação negativa de apenas 0,11 em adultos [[vachon2014]], o "
        "que sugere "
        "que o défice relevante não é a empatia em geral, mas o conjunto de traços de "
        "insensibilidade emocional que caracteriza um subgrupo de jovens com agressão "
        "instrumental [[frick2014]]. Por fim, o sexo masculino associa-se a mais agressão "
        "directa, física e verbal, mas não a mais agressão indirecta, e a agressão directa "
        "relaciona-se com problemas externalizantes, más relações com os pares e baixo "
        "comportamento pró-social [[card2008]].")


def _magnitude_do_problema(e):
    e.h2("6.6. Magnitude do comportamento agressivo e do sofrimento psicológico")
    e.p("A prevalência de agressão é elevada e transversal aos continentes. Nos 68 países de "
        "baixo e médio rendimento analisados a partir dos inquéritos globais de saúde escolar, "
        "36,4 por cento dos adolescentes dos 12 aos 15 anos envolveram-se em lutas físicas e 35,6 "
        "por cento sofreram agressão física nos 12 meses anteriores; as lutas foram muito mais "
        "frequentes nos rapazes, 45,5 por cento contra 26,9 por cento nas raparigas, enquanto a "
        "vitimização por bullying, de 34,4 por cento, não diferiu entre os sexos [[han2019]]. Na "
        "África subsariana, a análise agrupada de oito países estimou a prevalência de violência "
        "interpessoal em 53,7 por cento e identificou como preditores a vitimização por "
        "bullying, o absentismo escolar e o consumo de álcool e de tabaco, enquanto o apoio dos "
        "pares e a ligação parental funcionaram como factores protectores [[aboagye2021a]].")
    e.p("O sofrimento psicológico acompanha estes números. Uma revisão de 2012, com 10 estudos de "
        "seis países, estimou que cerca de uma em cada sete crianças subsarianas apresentava "
        "psicopatologia [[cortina2012]], e uma revisão "
        "sistemática de estudos em 16 países documentou prevalências relevantes de depressão, "
        "ansiedade, dificuldades emocionais e de comportamento, stress pós-traumático e "
        "comportamento suicidário nos adolescentes [[jornspresentati2021]]. Em Moçambique, a "
        "análise do inquérito global de saúde escolar de 2015, com 1.918 adolescentes "
        "escolarizados, encontrou sofrimento psicossocial em 21,2 por cento, mais frequente nos "
        "que se tinham envolvido em lutas físicas, com um odds ratio ajustado (aOR) de 1,38, nos "
        "que tinham sido agredidos fisicamente (aOR de 1,80) e nas vítimas de bullying (aOR de "
        "1,45), e menos frequente nos que "
        "tinham amigos próximos (aOR de 0,50) [[amu2020]]. A agressão e o sofrimento psicológico "
        "aparecem, assim, ligados nos próprios adolescentes escolarizados moçambicanos.")


def _factores_familiares(e):
    e.h2("6.7. Factores psicossociais do contexto familiar")
    e.p("A família é o primeiro contexto de aprendizagem da regulação emocional e do "
        "relacionamento. Uma meta-análise de 75 estudos, abrangendo mais de 160 mil crianças, "
        "concluiu que o castigo físico se associa a maior agressividade, a mais problemas de "
        "comportamento e a pior saúde mental, sem qualquer benefício documentado em termos de "
        "obediência a longo prazo [[gershoff2016]]. O mesmo padrão foi observado em contexto "
        "africano: em 409 alunos do ensino primário da Tanzânia, quase todos já castigados "
        "fisicamente em casa e na escola, o castigo físico pelos pais associou-se a mais "
        "problemas externalizantes [[hecker2014]]. Ao nível populacional, os países com "
        "proibição total do castigo físico apresentam 69 por cento da taxa de lutas frequentes "
        "nos rapazes e 42 por cento nas raparigas, quando comparados com os países sem qualquer "
        "proibição [[elgar2018]].")
    e.p("Para além da punição, pesam a qualidade do funcionamento familiar e o estilo de "
        "parentalidade. Em 1.232 alunos norte-americanos com agressividade elevada, a baixa coesão "
        "familiar associou-se a mais agressão física [[henneberger2016]], e o controlo "
        "psicológico parental, isto é, o recurso à indução de culpa e à retirada de afecto para "
        "controlar os pensamentos e as emoções do adolescente, associa-se à agressividade por "
        "via da afiliação a pares desviantes [[tian2019]]. Em cinco países subsarianos, "
        "incluindo Moçambique, a ausência prolongada de um dos pais biológicos foi relatada por "
        "30,5 por cento das mulheres e 25,1 por cento dos homens dos 18 aos 24 anos e "
        "associou-se a pior saúde mental e a maior consumo de substâncias [[annor2024]].")
    e.p("A acumulação de experiências adversas é particularmente relevante. Em adolescentes dos 10 "
        "aos 14 anos de 14 países, o número de experiências adversas associou-se aos "
        "sintomas depressivos e à perpetração de violência [[blum2019]]. Na África subsariana, a "
        "análise dos inquéritos nacionais mostrou uma relação gradual entre as experiências "
        "adversas acumuladas e o sofrimento mental, o consumo de substâncias e a perpetração de "
        "violência nos jovens adultos [[brown2024]], e, em homens adultos de Dar es Salaam, "
        "padrões específicos de adversidade na infância antecederam a perpetração de violência "
        "interpessoal [[zietz2020]]. Em oito países de baixo e médio rendimento, a violência "
        "sofrida ou testemunhada na infância associou-se a maior probabilidade de perpetração de "
        "violência nos homens dos 18 aos 24 anos; em Moçambique, 21,0 por cento destes jovens "
        "relataram ter perpetrado violência física ou sexual [[miedema2026]].")


def _factores_escolares_e_comunitarios(e):
    e.h2("6.8. Factores psicossociais do contexto escolar e do grupo de pares")
    e.p("A escola pode ser factor de protecção ou de risco. A ligação à escola, entendida como o "
        "sentimento de pertença e a percepção de apoio por parte dos professores, atenua o efeito "
        "dos factores familiares adversos sobre a agressividade [[tian2019]]. Em sentido "
        "contrário, a vitimização por bullying associa-se a solidão, a ansiedade e a consumo de "
        "canábis [[aboagye2021b]], e, em Moçambique, as vítimas de bullying apresentam mais "
        "sofrimento psicossocial [[amu2020]]. Numa amostra comunitária de 819 adolescentes etíopes, a vitimização "
        "associou-se ao sexo masculino, ao abuso físico e emocional, ao consumo de substâncias e "
        "ao sofrimento psicológico [[tarafa2022]]. No Malawi, em 561 alunos do ensino primário, "
        "42,4 por cento das raparigas e 36,4 por cento dos rapazes relataram abuso físico na "
        "escola, que nos rapazes se associou à perpetração de bullying [[ameli2017]].")
    e.p("O grupo de pares assume, na adolescência, um papel normativo que rivaliza com o da "
        "família. Num estudo longitudinal com 4.078 alunos no início da adolescência, a "
        "afiliação a pares desviantes e a agressividade reforçaram-se mutuamente ao longo de dois "
        "anos, e o baixo autocontrolo associou-se a ambas [[li2024]]. A vitimização pelos pares "
        "associa-se a mais comportamentos problemáticos através da afiliação a pares desviantes, "
        "com efeito mais forte nos adolescentes mais impulsivos [[zhu2016]]. Na África do Sul, "
        "em 769 alunos do ensino secundário, a adversidade na infância predisse a perpetração de "
        "bullying, com mediação pela influência dos pares e moderação por traços de "
        "personalidade [[ugwu2024]].")

    e.h2("6.9. Consumo de substâncias e factores comunitários")
    e.p("O consumo de álcool e de outras substâncias é simultaneamente factor de risco e "
        "consequência. Nos adolescentes dos 12 aos 15 anos de 57 países de baixo e médio "
        "rendimento, com dados de 2006 a 2013, 25,0 por cento tinham bebido álcool nos 30 dias "
        "anteriores [[ma2018]], e, em "
        "41 países, o consumo de substâncias associou-se ao sofrimento psicológico e foi mais "
        "frequente nos adolescentes envolvidos em lutas, agredidos fisicamente ou vítimas de "
        "bullying [[tian2021]]. Em Moçambique, 29,7 por cento dos jovens dos 13 aos 24 anos "
        "declararam consumir álcool [[sema2025]].")
    e.p("A exposição à violência na comunidade normaliza a agressão como forma de resolver "
        "conflitos. Em Moçambique, 45,9 por cento das raparigas e 66,7 por cento dos rapazes dos "
        "18 aos 24 anos testemunharam violência na comunidade antes dos 18 anos [[vacs2019]], e a "
        "exposição passada à violência política associa-se a mais violência interpessoal contra "
        "crianças e jovens em vários países africanos, incluindo Moçambique [[vigneri2026]], "
        "aspecto pertinente num país que viveu uma guerra civil e, mais recentemente, conflito "
        "armado no norte. Mais de sete "
        "em cada dez jovens subsarianos relatam pelo menos uma experiência adversa [[amene2024]]. "
        "Quanto aos conteúdos violentos nos jogos electrónicos, uma meta-análise de 24 estudos "
        "prospectivos com mais de 17 mil participantes encontrou um efeito pequeno sobre a "
        "agressão física posterior, com coeficientes entre 0,08 e 0,11 [[prescott2018]]; neste "
        "estudo, a exposição a estes conteúdos será registada por um único item de auto-relato.")


def _avaliacao_e_intervencao(e):
    e.h2("6.10. Avaliação psicológica do comportamento agressivo")
    e.p("A avaliação clínica da agressividade combina medidas dimensionais de auto-relato, que "
        "permitem rastrear grupos alargados, com a entrevista clínica, necessária para o "
        "diagnóstico individual. O Questionário de Agressividade de Buss e Perry (Buss-Perry "
        "Aggression Questionnaire, BPAQ) é o instrumento de auto-relato mais utilizado "
        "[[buss1992]]; a sua forma reduzida de 12 itens (BPAQ-SF), com três itens por dimensão, "
        "foi proposta por Bryant e Smith [[bryant2001]] e validada em rapazes portugueses, "
        "sobretudo de contexto forense [[pechorro2016]]. O Questionário de Agressão Reactiva e "
        "Proactiva (Reactive-Proactive Aggression Questionnaire, RPQ), de 23 itens, separa as duas "
        "formas funcionais de agressão; foi validado em rapazes portugueses detidos e numa amostra "
        "escolar mista de 782 jovens portugueses, e a sua estrutura foi replicada nos Estados "
        "Unidos e na China [[raine2006,pechorro2015,pechorro2018,tuvblad2016]]. O questionário de "
        "Buss e Perry foi usado em poucas amostras africanas, como crianças e adolescentes Datoga "
        "e Meru da Tanzânia [[butovskaya2019]], nenhuma de língua portuguesa, e não se "
        "encontraram estudos do RPQ em adolescentes africanos; nenhuma das duas escalas foi "
        "estudada em Moçambique.")
    e.p("Para o funcionamento psicológico, o Questionário de Capacidades e de Dificuldades "
        "(Strengths and Difficulties Questionnaire, SDQ) avalia, em 25 itens, os sintomas "
        "emocionais, os problemas de comportamento, a hiperactividade e desatenção, os problemas "
        "com os pares e o comportamento pró-social [[goodman1997]]. A versão de auto-avaliação "
        "discriminou adolescentes da comunidade e de consulta de saúde mental [[goodman1998]], e, "
        "numa amostra nacional britânica, a estrutura de cinco factores confirmou-se, com alfa "
        "médio de 0,73 no conjunto dos três informantes, e as pontuações acima do percentil 90 "
        "associaram-se a perturbação psiquiátrica diagnosticada, embora com menor força na versão "
        "de auto-avaliação do que nas versões para pais e professores [[goodman2001]]. Foi usado em 54 estudos de 12 países "
        "africanos, embora nem sempre com versões autorizadas nas línguas locais "
        "[[hoosen2018]]. A forma reduzida da Escala de Dificuldades de Regulação Emocional "
        "(Difficulties in Emotion Regulation Scale, Short Form, DERS-SF) mantém, com metade dos "
        "itens, as propriedades da escala original em adolescentes e adultos [[kaufman2016]], e "
        "a sua validação em 612 adolescentes portugueses recomendou o cálculo da pontuação total "
        "sem os itens de consciência emocional [[moreira2022]]. A Escala de Auto-Estima de "
        "Rosenberg foi aplicada em 53 nações com estrutura factorial largamente invariante, mas os "
        "itens formulados pela negativa foram interpretados de forma diferente entre nações, "
        "sobretudo nas menos desenvolvidas, cuidado a ter no pré-teste [[schmitt2005]]. A Escala Revista de Impacto "
        "de Acontecimentos para Crianças, na versão de oito itens (Children's Revised Impact of "
        "Event Scale, CRIES-8), rastreia o stress pós-traumático, com ponto de corte de 17 "
        "[[perrin2005]].")
    e.p("Os factores do contexto recorrem a instrumentos igualmente consolidados: a escala de "
        "funcionamento familiar de Smilkstein (APGAR), com cinco itens, avalia a percepção do "
        "funcionamento familiar nas dimensões de adaptação, participação, crescimento, afecto e "
        "resolução [[smilkstein1978]]; o questionário internacional de experiências adversas na "
        "infância da OMS (Adverse Childhood Experiences International Questionnaire, ACE-IQ) "
        "fornece itens sobre castigo físico e violência testemunhada, formulados para maiores de "
        "18 anos e de forma retrospectiva, que neste estudo foram adaptados aos últimos 12 meses "
        "[[aceiq]]; e o inquérito global de saúde escolar disponibiliza módulos sobre bullying, "
        "lutas físicas, supervisão parental e consumo de substâncias, comparáveis com os dados "
        "de outros países africanos [[gshs]].")

    e.h2("6.11. Implicações clínicas: detecção, encaminhamento e intervenção")
    e.p("As crianças agressivas têm maior probabilidade de, na idade adulta, apresentar doença "
        "física e mental, desemprego, pobreza e problemas com a justiça [[scott2018]], e a "
        "violência juvenil associa-se a abandono escolar [[oms_violencia_jovem]]. As intervenções com melhor evidência são "
        "psicossociais: o treino parental e a terapia cognitivo-comportamental, centrada na "
        "regulação da raiva e na resolução de problemas sociais, têm apoio extenso em ensaios "
        "aleatorizados [[sukhodolsky2016]], e a eficácia da terapia cognitivo-comportamental "
        "para a raiva em crianças e adolescentes foi confirmada em meta-análise "
        "[[sukhodolsky2004]]. Em contexto africano, a terapia cognitivo-comportamental focada no "
        "trauma, aplicada por conselheiros leigos supervisionados a crianças e adolescentes de "
        "Lusaka, reduziu os sintomas traumáticos em 81,9 por cento, contra 21,1 por cento no "
        "tratamento habitual [[murray2015]], e, na Tanzânia, um programa de formação de "
        "professores em competências de interacção reduziu a violência emocional e física "
        "exercida pelos professores [[nkuba2018]].")
    e.p("Em Moçambique, os recursos especializados são escassos: entre 2010 e 2014, o número de "
        "psicólogos no sistema de saúde passou de 56 para 109 e o de psiquiatras de 9 para 10, "
        "numa estratégia assente na delegação de tarefas nos cuidados de saúde primários "
        "[[dossantos2016]]. O guia de intervenção da OMS para os cuidados não especializados "
        "inclui um módulo dedicado às perturbações mentais e comportamentais da criança e do "
        "adolescente [[oms_mhgap]], e o pacote INSPIRE reúne sete estratégias de prevenção, entre "
        "as quais o apoio aos pais e cuidadores e o desenvolvimento de competências para a vida "
        "[[inspire2016]]. Conhecer quais os factores psicológicos que mais pesam na agressividade "
        "dos adolescentes de Muatala permitirá escolher, entre estas respostas, as que actuam "
        "sobre os mecanismos presentes na escola.")


def _estado_da_arte_e_esquema(e, h, doc, caminho_figura):
    e.h2("6.12. Estado da arte")
    e.p("O quadro seguinte sintetiza os principais estudos que fundamentam este protocolo, "
        "começando pela evidência moçambicana e africana e seguindo para os estudos sobre os "
        "mecanismos psicológicos. Quando o estudo o apresenta, a força da associação é expressa "
        "pelo aOR, estimado depois de controladas as restantes variáveis do modelo.")
    h.tabela(doc, "Quadro 1: Síntese dos estudos que fundamentam o protocolo.",
             ["Autor (ano)", "Local", "Método (amostra)", "Principais resultados"],
             [[e.resolver(celula) for celula in linha] for linha in ESTADO_DA_ARTE],
             "Fonte: a autora, 2026.",
             larguras=[Cm(3.0), Cm(2.8), Cm(3.6), Cm(6.6)])
    e.p("A leitura conjunta destes trabalhos revela as lacunas que o presente estudo procura "
        "colmatar. A evidência africana assenta sobretudo em indicadores comportamentais "
        "isolados, como o envolvimento em lutas, e não em escalas psicométricas de agressividade, "
        "enquanto os estudos sobre os mecanismos psicológicos, como a regulação emocional, a "
        "atribuição hostil ou a auto-estima, provêm da América do Norte, da Europa e da Ásia e "
        "raramente foram testados em adolescentes africanos. Os estudos moçambicanos são de "
        "âmbito nacional ou das regiões sul e centro e medem a violência e a saúde mental em "
        "separado, sem "
        "as relacionar com a agressividade, e raramente se testam em simultâneo os factores "
        "psicológicos e os dos contextos de vida, o que impede saber quais se mantêm associados "
        "depois do ajustamento mútuo e por que via actuam.")

    e.h2("6.13. Esquema conceptual do problema")
    e.p("A figura seguinte representa as relações que o estudo se propõe examinar, inspiradas no "
        "Modelo Geral da Agressão e no modelo ecológico. Os factores psicossociais do contexto "
        "familiar, escolar e comunitário são tratados como factores distais, que se relacionam "
        "com o comportamento agressivo sobretudo através dos factores psicológicos individuais, "
        "tratados como factores proximais; as setas tracejadas representam a associação directa "
        "que não passa por esses factores [[anderson2002,allen2018,krug2002]].")
    h.figura(doc, caminho_figura,
             "Figura 1: Esquema conceptual do comportamento agressivo no adolescente, com os "
             "factores psicossociais do contexto, os factores psicológicos individuais e o "
             "desfecho.", largura=Cm(15.0))
    h.paragrafo(doc, "Fonte: a autora, 2026, com base no Modelo Geral da Agressão e no modelo "
                "ecológico da Organização Mundial da Saúde.", tamanho=Pt(10), espaco=1.0)


def escrever_revisao(e, h, doc, caminho_figura):
    """Seccao 6 completa, montada a partir dos blocos tematicos acima."""
    e.h1("6. REVISÃO DA LITERATURA")
    _conceitos_e_modelos_teoricos(e)
    _perspectiva_clinica(e)
    _modelos_teoricos(e)
    _mecanismos_psicologicos(e)
    _magnitude_do_problema(e)
    _factores_familiares(e)
    _factores_escolares_e_comunitarios(e)
    _avaliacao_e_intervencao(e)
    _estado_da_arte_e_esquema(e, h, doc, caminho_figura)
