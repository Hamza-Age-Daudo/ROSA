"""Apendices do protocolo: questionario, folha de informacao, consentimento e assentimento.

As perguntas do questionario sao guardadas sem numero; a numeracao e gerada por
intervalos_dos_blocos, para que acrescentar ou retirar um item nao obrigue a renumerar
o resto a mao nem a corrigir as instrucoes ("nas perguntas X a Y").
"""
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Cm, Pt

from _protocolo_texto import ESTUDANTE, ORIENTADOR_COM_GRAU, TITULO_CORRENTE

SOCIODEMOGRAFICO = [
    ("Código do questionário, código da turma e data de aplicação, preenchidos pelo aplicador:",
     "Questionário ______   Turma ______   Data ____ / ____ / 2026"),
    ("Idade em anos completos:", "______"),
    ("Sexo:", "( ) Masculino   ( ) Feminino"),
    ("Classe que frequenta:", "( ) 7.ª   ( ) 8.ª   ( ) 9.ª   ( ) 10.ª   ( ) 11.ª   ( ) 12.ª"),
    ("Turno:", "( ) Manhã   ( ) Tarde   ( ) Noite"),
    ("Já repetiu alguma classe?", "( ) Sim   ( ) Não"),
    ("Nos últimos 30 dias, em quantos dias faltou às aulas sem justificação?",
     "( ) Nenhum dia   ( ) 1 a 2 dias   ( ) 3 a 5 dias   ( ) 6 ou mais dias"),
    ("Com quem vive actualmente?",
     "( ) Com o pai e a mãe   ( ) Só com a mãe   ( ) Só com o pai   "
     "( ) Com avós ou outros familiares   ( ) Outra situação: ____________"),
    ("O pai está vivo?", "( ) Sim   ( ) Não   ( ) Não sabe"),
    ("A mãe está viva?", "( ) Sim   ( ) Não   ( ) Não sabe"),
    ("Quantas pessoas vivem na sua casa, contando consigo?", "______"),
    ("Nos últimos 30 dias, com que frequência a sua família ficou sem comida suficiente?",
     "( ) Nunca   ( ) Raramente   ( ) Às vezes   ( ) Muitas vezes   ( ) Sempre"),
]

APGAR = [
    "Estou satisfeito com a ajuda que recebo da minha família quando tenho um problema.",
    "Estou satisfeito com a forma como a minha família fala comigo sobre os assuntos e "
    "partilha os problemas.",
    "Estou satisfeito com a forma como a minha família aceita e apoia as coisas novas que eu "
    "quero fazer.",
    "Estou satisfeito com a forma como a minha família me mostra carinho e se importa com o que "
    "eu sinto.",
    "Estou satisfeito com o tempo que passo com a minha família.",
]

FREQUENCIA_PARENTAL = "( ) Nunca   ( ) Raramente   ( ) Às vezes   ( ) Quase sempre   ( ) Sempre"
FREQUENCIA_VIOLENCIA = "( ) Nunca   ( ) Uma ou duas vezes   ( ) Várias vezes   ( ) Muitas vezes"
CONCORDANCIA = "( ) Discordo totalmente   ( ) Discordo   ( ) Concordo   ( ) Concordo totalmente"
NUMERO_AMIGOS = "( ) Nenhum   ( ) Um   ( ) Dois   ( ) Três ou mais"
NUMERO_VEZES = "( ) Nenhuma vez   ( ) 1 vez   ( ) 2 a 3 vezes   ( ) 4 ou mais vezes"

SUPERVISAO = [
    ("Nos últimos 30 dias, com que frequência os seus pais ou encarregados verificaram se fez "
     "os trabalhos de casa?", FREQUENCIA_PARENTAL),
    ("Nos últimos 30 dias, com que frequência os seus pais ou encarregados sabiam realmente o "
     "que fazia no seu tempo livre?", FREQUENCIA_PARENTAL),
    ("Nos últimos 30 dias, com que frequência os seus pais ou encarregados compreendiam os seus "
     "problemas e preocupações?", FREQUENCIA_PARENTAL),
]

VIOLENCIA = [
    ("Nos últimos 12 meses, algum adulto da sua casa lhe bateu, deu palmadas ou o castigou "
     "fisicamente?", FREQUENCIA_VIOLENCIA),
    ("Nos últimos 12 meses, algum adulto da sua casa o insultou, o humilhou ou lhe disse que "
     "preferia que você nunca tivesse nascido?", FREQUENCIA_VIOLENCIA),
    ("Nos últimos 12 meses, viu ou ouviu adultos da sua casa a baterem uns nos outros?",
     FREQUENCIA_VIOLENCIA),
    ("Nos últimos 12 meses, viu alguém ser agredido na rua ou no bairro onde vive?",
     FREQUENCIA_VIOLENCIA),
    ("Nos últimos 12 meses, algum professor ou funcionário da escola lhe bateu ou o castigou "
     "fisicamente?", FREQUENCIA_VIOLENCIA),
]

ESCOLA_PARES = [
    ("Nos últimos 30 dias, em quantos dias foi vítima de bullying, ou seja, gozado, ameaçado, "
     "excluído ou agredido repetidamente por colegas?",
     "( ) Nenhum dia   ( ) 1 a 2 dias   ( ) 3 a 5 dias   ( ) 6 ou mais dias"),
    ("Nos últimos 12 meses, quantas vezes se envolveu em lutas físicas?", NUMERO_VEZES),
    ("Nos últimos 12 meses, quantas vezes foi agredido fisicamente por alguém?", NUMERO_VEZES),
    ("Sinto que faço parte desta escola.", CONCORDANCIA),
    ("Os professores desta escola preocupam-se comigo.", CONCORDANCIA),
    ("Na maior parte dos dias, gosto de vir à escola.", CONCORDANCIA),
    ("Quantos dos seus amigos próximos já se envolveram em lutas ou confusões?",
     NUMERO_AMIGOS),
    ("Quantos dos seus amigos próximos bebem álcool ou consomem drogas?", NUMERO_AMIGOS),
    ("Quantos dos seus amigos próximos faltam frequentemente às aulas?", NUMERO_AMIGOS),
]

SUBSTANCIAS = [
    ("Nos últimos 30 dias, em quantos dias bebeu pelo menos uma bebida alcoólica (cerveja, "
     "vinho, aguardente ou bebidas tradicionais feitas em casa)?",
     "( ) Nenhum dia   ( ) 1 a 2 dias   ( ) 3 a 9 dias   ( ) 10 ou mais dias"),
    ("Nos últimos 30 dias, em quantos dias fumou cigarros ou usou tabaco?",
     "( ) Nenhum dia   ( ) 1 a 2 dias   ( ) 3 a 9 dias   ( ) 10 ou mais dias"),
    ("Alguma vez consumiu suruma, canábis ou outra droga?",
     "( ) Nunca   ( ) Sim, no passado   ( ) Sim, nos últimos 30 dias"),
    ("Quanto tempo por dia passa a ver filmes ou vídeos, ou a jogar jogos, com conteúdo "
     "violento, como lutas, tiros ou pessoas a serem feridas?",
     "( ) Não vejo nem jogo   ( ) Menos de uma hora   ( ) Uma a três horas   "
     "( ) Mais de três horas"),
]

# Itens em traducao de trabalho, para apreciacao do juri; na aplicacao usam-se, sem
# alteracoes, as versoes portuguesas validadas ou oficiais de cada instrumento.
EMO, COMP, HIPER, PARES, PRO = ("Sintomas emocionais", "Problemas de comportamento",
                                "Hiperactividade e desatenção", "Problemas com os pares",
                                "Pró-social")
SDQ_ITENS = [
    ("Tento ser simpático com as outras pessoas. Preocupo-me com o que sentem.", PRO, False),
    ("Sou irrequieto, não consigo ficar quieto muito tempo.", HIPER, False),
    ("Tenho muitas dores de cabeça, dores de barriga ou vómitos.", EMO, False),
    ("Normalmente partilho as minhas coisas com os outros (comida, jogos, canetas).", PRO, False),
    ("Fico muito zangado e perco a calma com facilidade.", COMP, False),
    ("Estou quase sempre sozinho, normalmente fico ou brinco sozinho.", PARES, False),
    ("Normalmente faço o que me mandam.", COMP, True),
    ("Preocupo-me muito.", EMO, False),
    ("Ajudo quando alguém está magoado, triste ou doente.", PRO, False),
    ("Estou sempre a mexer-me, não consigo estar parado.", HIPER, False),
    ("Tenho pelo menos um bom amigo ou uma boa amiga.", PARES, True),
    ("Ando muitas vezes à luta e consigo obrigar os outros a fazer o que eu quero.", COMP, False),
    ("Ando muitas vezes triste, desanimado ou com vontade de chorar.", EMO, False),
    ("Os jovens da minha idade geralmente gostam de mim.", PARES, True),
    ("Distraio-me com facilidade, tenho dificuldade em concentrar-me.", HIPER, False),
    ("Fico nervoso em situações novas e perco facilmente a confiança.", EMO, False),
    ("Sou simpático com os mais novos.", PRO, False),
    ("Acusam-me muitas vezes de mentir ou de fazer batota.", COMP, False),
    ("Os outros jovens metem-se comigo, gozam-me ou ameaçam-me.", PARES, False),
    ("Ofereço-me muitas vezes para ajudar os outros (pais, professores, colegas).", PRO, False),
    ("Penso antes de fazer as coisas.", HIPER, True),
    ("Tiro coisas que não são minhas, em casa, na escola ou noutros sítios.", COMP, False),
    ("Dou-me melhor com adultos do que com jovens da minha idade.", PARES, False),
    ("Tenho muitos medos e assusto-me com facilidade.", EMO, False),
    ("Acabo as tarefas que começo, tenho boa atenção.", HIPER, True),
]

DERS_SF_ITENS = [
    ("Presto atenção ao que sinto.", "Consciência emocional", True),
    ("Não faço ideia de como me estou a sentir.", "Clareza emocional", False),
    ("Tenho dificuldade em perceber os meus sentimentos.", "Clareza emocional", False),
    ("Quando me sinto mal (triste, zangado ou nervoso), reconheço as minhas emoções.",
     "Consciência emocional", True),
    ("Sinto-me confuso sobre o que sinto.", "Clareza emocional", False),
    ("Quando me sinto mal, fico envergonhado por me sentir assim.", "Não aceitação", False),
    ("Quando me sinto mal, tenho dificuldade em fazer os meus trabalhos.", "Objectivos", False),
    ("Quando me sinto mal, fico descontrolado.", "Impulsos", False),
    ("Quando me sinto mal, acho que vou acabar por ficar muito deprimido.", "Estratégias", False),
    ("Quando me sinto mal, tenho dificuldade em concentrar-me noutras coisas.", "Objectivos",
     False),
    ("Quando me sinto mal, sinto-me culpado por me sentir assim.", "Não aceitação", False),
    ("Quando me sinto mal, tenho dificuldade em concentrar-me.", "Objectivos", False),
    ("Quando me sinto mal, tenho dificuldade em controlar o meu comportamento.", "Impulsos",
     False),
    ("Quando me sinto mal, acho que a única coisa que posso fazer é ficar sempre a pensar no "
     "mesmo assunto.", "Estratégias", False),
    ("Quando me sinto mal, tenho vergonha de mim próprio por me sentir assim.", "Não aceitação",
     False),
    ("Quando me sinto mal, começo a sentir-me muito mal comigo próprio.", "Estratégias", False),
    ("Quando me sinto mal, sinto que perco o controlo.", "Impulsos", False),
    ("Importo-me com o que estou a sentir.", "Consciência emocional", True),
]

ROSENBERG_ITENS = [
    ("De um modo geral, estou satisfeito comigo próprio.", False),
    ("Por vezes penso que não presto para nada.", True),
    ("Sinto que tenho algumas boas qualidades.", False),
    ("Sou capaz de fazer as coisas tão bem como a maioria das pessoas.", False),
    ("Sinto que não tenho muito de que me orgulhar.", True),
    ("Por vezes sinto-me inútil.", True),
    ("Sinto que sou uma pessoa de valor, pelo menos tanto como os outros.", False),
    ("Gostava de ter mais respeito por mim próprio.", True),
    ("No geral, sinto que sou um fracasso.", True),
    ("Tenho uma atitude positiva em relação a mim próprio.", False),
]

CRIES_FILTRO = [
    ("Alguma vez viveu ou presenciou um acontecimento muito assustador ou violento, como uma "
     "agressão grave, um acidente, um ataque armado ou a morte violenta de alguém próximo?",
     "( ) Não (passe à Secção IX)   ( ) Sim. Se sim, qual foi o mais perturbador: "
     "( ) agressão grave   ( ) acidente   ( ) ataque armado   ( ) morte violenta de alguém "
     "próximo   ( ) outro"),
]

CRIES_ITENS = [
    ("Pensa nesse acontecimento mesmo quando não quer?", "Intrusão"),
    ("Tenta apagá-lo da memória?", "Evitamento"),
    ("De repente, sente emoções muito fortes (medo, raiva ou tristeza) por causa dele?", "Intrusão"),
    ("Evita lugares ou situações que o fazem lembrar dele?", "Evitamento"),
    ("Tenta não falar sobre ele?", "Evitamento"),
    ("Aparecem-lhe na cabeça imagens desse acontecimento?", "Intrusão"),
    ("Há outras coisas que o fazem voltar a pensar nele?", "Intrusão"),
    ("Tenta não pensar nele?", "Evitamento"),
]

BPAQ_ITENS = [
    ("Se for suficientemente provocado, posso bater noutra pessoa.", "Agressão física"),
    ("Houve pessoas que me provocaram tanto que chegámos a vias de facto.", "Agressão física"),
    ("Já ameacei pessoas que conheço.", "Agressão física"),
    ("Dou muitas vezes por mim a discordar das pessoas.", "Agressão verbal"),
    ("Não consigo evitar discutir quando as pessoas discordam de mim.", "Agressão verbal"),
    ("Os meus amigos dizem que discuto muito.", "Agressão verbal"),
    ("Irrito-me depressa, mas também me passa depressa.", "Ira"),
    ("Às vezes perco a cabeça sem uma boa razão.", "Ira"),
    ("Tenho dificuldade em controlar a minha raiva.", "Ira"),
    ("Às vezes sinto que a vida tem sido injusta comigo.", "Hostilidade"),
    ("Os outros parecem ter sempre mais sorte do que eu.", "Hostilidade"),
    ("Às vezes pergunto-me porque me sinto tão amargurado com certas coisas.", "Hostilidade"),
]

RPQ_ITENS = [
    ("Fiquei zangado quando alguém me contrariou.", "Reactiva"),
    ("Reagi com raiva quando fui provocado por outros.", "Reactiva"),
    ("Bati em alguém quando fui gozado ou ameaçado.", "Reactiva"),
    ("Usei a força para obter dinheiro ou coisas de outras pessoas.", "Proactiva"),
    ("Ameacei ou intimidei alguém para conseguir o que queria.", "Proactiva"),
    ("Fiz parte de um grupo que andou à luta para se sentir importante.", "Proactiva"),
]

BLOCOS = (
    ("sociodemografico", SOCIODEMOGRAFICO),
    ("apgar", APGAR),
    ("supervisao", SUPERVISAO),
    ("violencia", VIOLENCIA),
    ("escola_pares", ESCOLA_PARES),
    ("substancias", SUBSTANCIAS),
    ("sdq", SDQ_ITENS),
    ("ders", DERS_SF_ITENS),
    ("rosenberg", ROSENBERG_ITENS),
    ("cries_filtro", CRIES_FILTRO),
    ("cries", CRIES_ITENS),
    ("bpaq", BPAQ_ITENS),
    ("rpq", RPQ_ITENS),
)


def intervalos_dos_blocos():
    """Primeiro e ultimo numero de pergunta de cada bloco, pela ordem do questionario."""
    intervalos, proximo = {}, 1
    for nome, itens in BLOCOS:
        intervalos[nome] = (proximo, proximo + len(itens) - 1)
        proximo += len(itens)
    return intervalos


def _numerados(nome):
    """Pares (numero, item) de um bloco, com a numeracao continua do questionario."""
    primeiro, _ultimo = intervalos_dos_blocos()[nome]
    itens = dict(BLOCOS)[nome]
    return list(enumerate(itens, start=primeiro))


def _intervalo(nome):
    primeiro, ultimo = intervalos_dos_blocos()[nome]
    return f"{primeiro} a {ultimo}"


def _itens(h, doc, nome, tamanho=Pt(11)):
    """Pergunta numerada numa linha e opcoes de resposta na linha seguinte, recuadas."""
    for numero, (pergunta, opcoes) in _numerados(nome):
        par = h.paragrafo(doc, f"{numero}. {pergunta}", WD_ALIGN_PARAGRAPH.LEFT,
                          tamanho=tamanho, espaco=1.15, depois=Pt(1))
        par.paragraph_format.keep_with_next = True
        h.paragrafo(doc, opcoes, WD_ALIGN_PARAGRAPH.LEFT, tamanho=tamanho, espaco=1.15,
                    depois=Pt(7), recuo=Cm(0.6))


def _nota(h, doc, texto):
    h.paragrafo(doc, texto, WD_ALIGN_PARAGRAPH.LEFT, italico=True, tamanho=Pt(10), espaco=1.0,
                depois=Pt(6))


def _tabela_de_escala(h, doc, nome, opcoes):
    h.tabela(doc, None, ["N.º e afirmação"] + opcoes,
             [[f"{numero}. {texto}"] + ["( )"] * len(opcoes) for numero, texto in _numerados(nome)],
             None, Pt(10), larguras=[Cm(11.0)] + [Cm(1.6)] * len(opcoes))


def _folha_de_rosto_dos_apendices(e, h, doc):
    h.quebra_pagina(doc)
    h.titulo(doc, "APÊNDICES", 1)
    e.p("Os apêndices reúnem o instrumento de recolha de dados e os documentos de informação, "
        "consentimento e assentimento a submeter ao comité de bioética.")


def _apendice_a_questionario(e, h, doc):
    h.quebra_pagina(doc)
    h.titulo(doc, "APÊNDICE A. QUESTIONÁRIO SOBRE FACTORES PSICOSSOCIAIS E COMPORTAMENTO "
             "AGRESSIVO", 1)
    e.p("Instrumento composto por módulos do APGAR familiar [[smilkstein1978]], do questionário "
        "internacional de experiências adversas na infância [[aceiq]] e do inquérito global de "
        "saúde escolar [[gshs]], pelas escalas psicológicas do Questionário de Capacidades e de "
        "Dificuldades [[goodman1997]], da DERS-SF [[kaufman2016,moreira2022]], da Escala de "
        "Auto-Estima de Rosenberg [[schmitt2005]] e da CRIES-8 [[perrin2005]], e pelas versões "
        "portuguesas do Questionário de Agressividade de Buss e Perry e do Questionário de "
        "Agressão Reactiva e Proactiva [[pechorro2016,pechorro2015]]. Os itens das escalas "
        "psicológicas são apresentados em tradução de trabalho, para apreciação do júri; na "
        "aplicação serão usadas as versões portuguesas validadas ou oficiais, sem alterações, e "
        "a versão submetida ao comité de bioética incluirá o texto integral dessas versões, "
        "incluindo os 23 itens do RPQ. As "
        "colunas das dimensões e as indicações sobre as fontes destinam-se ao júri; na versão "
        "entregue aos alunos mantêm-se apenas as instruções de resposta.", italico=True,
        tamanho=Pt(10), espaco=1.0)
    e.p("Este questionário é anónimo. Não escreva o seu nome em parte alguma. Não há respostas "
        "certas nem erradas: interessa apenas o que se passa consigo. Pode deixar sem resposta "
        "qualquer pergunta que o incomode. O preenchimento demora cerca de 45 minutos.")

    h.subtitulo(doc, "Secção I. Dados sociodemográficos e escolares")
    _itens(h, doc, "sociodemografico")

    h.subtitulo(doc, "Secção II. Funcionamento familiar, supervisão e ligação parental")
    _nota(h, doc, f"Nas perguntas {_intervalo('apgar')}, assinale: 0 = quase nunca; "
          "1 = algumas vezes; 2 = quase sempre. Adaptado do APGAR familiar.")
    _tabela_de_escala(h, doc, "apgar", ["0", "1", "2"])
    _nota(h, doc, f"Perguntas {_intervalo('supervisao')} adaptadas do inquérito global de saúde "
          "escolar.")
    _itens(h, doc, "supervisao")

    h.subtitulo(doc, "Secção III. Exposição à violência")
    _nota(h, doc, "Itens adaptados do questionário internacional de experiências adversas na "
          "infância da Organização Mundial da Saúde.")
    _itens(h, doc, "violencia")

    h.subtitulo(doc, "Secção IV. Escola e grupo de pares")
    _nota(h, doc, "As duas perguntas sobre lutas físicas e agressão física sofrida formam o "
          "indicador de violência interpessoal do inquérito global de saúde escolar, usado no "
          "cálculo do tamanho da amostra.")
    _itens(h, doc, "escola_pares")


def _tabela_com_dimensao(h, doc, nome, opcoes, coluna, dimensao_de, largura_opcao=None):
    """Tabela de escala com o numero, a afirmacao, as opcoes e a dimensao que o item mede.

    A coluna da dimensao destina-se ao juri e sai da versao entregue aos alunos."""
    if largura_opcao is None:
        largura_opcao = 0.8 if len(opcoes) > 3 else 0.9
    largura_texto = 15.4 - 0.9 - 2.7 - largura_opcao * len(opcoes)
    h.tabela(doc, None, ["N.º", "Afirmação"] + opcoes + [coluna],
             [[str(numero), item[0]] + ["( )"] * len(opcoes) + [dimensao_de(item)]
              for numero, item in _numerados(nome)], None, Pt(9.5),
             larguras=[Cm(0.9), Cm(largura_texto)] + [Cm(largura_opcao)] * len(opcoes)
             + [Cm(2.7)])


def _com_inversao(subescala, invertido):
    return f"{subescala} (invertido)" if invertido else subescala


def _apendice_a_funcionamento_psicologico(e, h, doc):
    h.subtitulo(doc, "Secção VI. Como me sinto e como me comporto")
    _nota(h, doc, f"Nas perguntas {_intervalo('sdq')}, pense nos últimos seis meses e assinale: "
          "0 = não é verdade; 1 = é um pouco verdade; 2 = é muito verdade. Questionário de "
          "Capacidades e de Dificuldades, versão de auto-avaliação dos 11 aos 17 anos; na "
          "aplicação será usada, sem alterações, a versão portuguesa oficial.")
    _tabela_com_dimensao(h, doc, "sdq", ["0", "1", "2"], "Subescala",
                         lambda item: _com_inversao(item[1], item[2]))

    h.subtitulo(doc, "Secção VII. Emoções e auto-estima")
    _nota(h, doc, f"Nas perguntas {_intervalo('ders')}, indique com que frequência cada frase se "
          "aplica a si: 1 = quase nunca; 2 = às vezes; 3 = cerca de metade das vezes; 4 = a "
          "maior parte das vezes; 5 = quase sempre. Forma reduzida da Escala de Dificuldades de "
          "Regulação Emocional; na aplicação será usada a versão portuguesa validada.")
    _tabela_com_dimensao(h, doc, "ders", ["1", "2", "3", "4", "5"], "Dimensão",
                         lambda item: _com_inversao(item[1], item[2]))
    _nota(h, doc, f"Nas perguntas {_intervalo('rosenberg')}, assinale: 1 = discordo "
          "totalmente; 2 = discordo; 3 = concordo; 4 = concordo totalmente. Escala de Auto-Estima "
          "de Rosenberg, versão portuguesa.")
    _tabela_com_dimensao(h, doc, "rosenberg", ["1", "2", "3", "4"], "Cotação",
                         lambda item: "Invertida" if item[1] else "Directa")

    h.subtitulo(doc, "Secção VIII. Acontecimentos perturbadores")
    _itens(h, doc, "cries_filtro")
    _nota(h, doc, f"Só para quem respondeu Sim. Nas perguntas {_intervalo('cries')}, pense nesse "
          "acontecimento e indique com que frequência tal lhe aconteceu nos últimos sete dias. "
          "Escala Revista de Impacto de Acontecimentos para Crianças, versão de oito itens; na "
          "cotação, nunca vale 0, raramente 1, às vezes 3 e muitas vezes 5.")
    _tabela_com_dimensao(h, doc, "cries", ["Nunca", "Raramente", "Às vezes", "Muitas vezes"],
                         "Dimensão", lambda item: item[1], largura_opcao=1.55)


def _apendice_a_desfechos(e, h, doc):
    h.subtitulo(doc, "Secção V. Consumo de substâncias e exposição a conteúdos violentos")
    _itens(h, doc, "substancias")

    _apendice_a_funcionamento_psicologico(e, h, doc)

    h.subtitulo(doc, "Secção IX. Comportamento agressivo")
    _nota(h, doc, f"Nas perguntas {_intervalo('bpaq')}, indique até que ponto cada afirmação o "
          "descreve: 1 = muito diferente de mim; 2 = diferente de mim; 3 = nem uma coisa nem "
          "outra; 4 = parecido comigo; 5 = muito parecido comigo. Itens correspondentes à forma "
          "reduzida do Questionário de Agressividade de Buss e Perry; na aplicação será usada a "
          "versão portuguesa validada, mediante autorização dos autores.")
    _tabela_com_dimensao(h, doc, "bpaq", ["1", "2", "3", "4", "5"], "Dimensão",
                         lambda item: item[1])
    _nota(h, doc, f"Nas perguntas {_intervalo('rpq')}, indique com que frequência fez cada "
          "uma destas coisas: 0 = nunca; 1 = às vezes; 2 = muitas vezes. Itens exemplificativos do "
          "Questionário de Agressão Reactiva e Proactiva; na aplicação serão usados os vinte e "
          "três itens da versão portuguesa validada, mediante autorização dos autores.")
    _tabela_com_dimensao(h, doc, "rpq", ["0", "1", "2"], "Forma", lambda item: item[1])
    e.p("Obrigado pela sua colaboração. Se alguma pergunta o deixou preocupado ou triste, "
        "procure a pessoa responsável pela sessão no fim: ela indicará onde pode obter apoio.")



def _apendice_b_informacao(e, h, doc):
    h.quebra_pagina(doc)
    h.titulo(doc, "APÊNDICE B. FOLHA DE INFORMAÇÃO AO PARTICIPANTE E AO ENCARREGADO DE EDUCAÇÃO", 1)
    for rotulo, texto in (
            ("Título do estudo:", TITULO_CORRENTE + "."),
            ("Investigadora principal:", f"{ESTUDANTE}, estudante finalista do Curso de "
             "Psicologia da Faculdade de Ciências de Saúde da Universidade Lúrio, sob orientação "
             f"do {ORIENTADOR_COM_GRAU}."),
            ("Objectivo:", "Compreender como os adolescentes se sentem, como lidam com as emoções "
             "e que factores da família, da escola, do grupo de amigos e do bairro se relacionam "
             "com o comportamento agressivo, para ajudar a escola e os serviços de saúde a "
             "planear acções de apoio psicológico e de prevenção."),
            ("Selecção dos participantes:", "A turma foi sorteada entre as turmas da escola. "
             "Todos os alunos da turma com idade entre os 10 e os 19 anos são convidados a "
             "participar."),
            ("Procedimentos:", "Se o aluno aceitar participar, preencherá um questionário na sala "
             "de aula, durante cerca de 45 minutos, que poderão ser divididos em duas sessões em "
             "dias seguidos, sem escrever o nome. Ninguém saberá "
             "quais "
             "foram as suas respostas."),
            ("Participação voluntária:", "A participação é livre. O aluno pode recusar ou "
             "interromper o preenchimento em qualquer momento, sem qualquer prejuízo nas notas ou "
             "no tratamento que recebe na escola. A recusa do aluno é respeitada mesmo que o "
             "encarregado de educação tenha autorizado."),
            ("Riscos e desconfortos:", "Algumas perguntas falam de castigos, brigas, emoções "
             "difíceis e acontecimentos assustadores e podem causar desconforto. O aluno pode não responder a qualquer "
             "pergunta. Estará presente uma pessoa preparada para conversar com quem se sentir "
             "incomodado."),
            ("Benefícios:", "Não há qualquer pagamento. Os resultados ajudarão a escola a "
             "organizar acções de apoio. Como o questionário não tem nome, ninguém saberá quem deu "
             "cada resposta; por isso, todos os alunos recebem uma folha com os contactos de "
             "apoio e um talão, separado das respostas, com o qual cada aluno pode pedir para ser "
             "contactado por um psicólogo; quem pedir ajuda ou se sentir mal durante a sessão será "
             "encaminhado, com o seu conhecimento, para o serviço de psicologia da unidade "
             "sanitária de referência."),
            ("Confidencialidade:", "O questionário não tem nome e é identificado apenas por um "
             "código. "
             "As folhas de autorização serão guardadas separadamente das respostas. Os dados serão "
             "usados apenas para este estudo."),
            ("Partilha de resultados:", "Os resultados serão apresentados de forma agregada à "
             "escola, à Universidade Lúrio e às autoridades de educação e de saúde, sem "
             "identificar qualquer aluno."),
            ("Contactos:", f"Investigadora: {ESTUDANTE}, telefone +258 ____________, correio electrónico "
             "________________. Comité Institucional de Bioética para a Saúde da Universidade "
             "Lúrio: telefone +258 845770070.")):
        h.paragrafo_misto(doc, [(rotulo + " ", True, False), (texto, False, False)],
                          espaco=1.15, depois=Pt(6))



def _apendice_c_consentimento(e, h, doc):
    h.quebra_pagina(doc)
    h.titulo(doc, "APÊNDICE C. TERMO DE CONSENTIMENTO LIVRE E ESCLARECIDO", 1)
    h.paragrafo(doc, "A preencher pelo pai, pela mãe ou pelo responsável legal do aluno com menos "
                "de 18 anos de idade.", WD_ALIGN_PARAGRAPH.LEFT, italico=True, tamanho=Pt(11),
                espaco=1.0, depois=Pt(10))
    e.p("Eu, ________________________________________________________, na qualidade de "
        "( ) pai   ( ) mãe   ( ) responsável legal (indicar: ____________________) do aluno ou "
        f"aluna ______________________________________, "
        f"declaro que autorizo a sua participação no estudo intitulado «{TITULO_CORRENTE}».")
    for texto in (
            "Declaro que me foi explicado, em linguagem que compreendi, o objectivo do estudo, o "
            "que será pedido ao meu educando, a duração do preenchimento, a ausência de riscos "
            "físicos e a possibilidade de algumas perguntas, sobre castigos, violência entre "
            "adultos da casa, acontecimentos assustadores e emoções difíceis, causarem desconforto "
            "emocional, estando presente na sessão uma pessoa preparada para apoiar o meu "
            "educando.",
            "Fui informado(a) de que a participação é voluntária, de que o meu educando pode recusar "
            "ou desistir em qualquer momento, sem qualquer prejuízo nas notas ou no tratamento "
            "que recebe na escola, e de que a recusa dele será respeitada mesmo depois desta "
            "autorização.",
            "Compreendi que não haverá qualquer compensação material ou financeira e que as "
            "respostas serão usadas apenas para os fins deste estudo, de forma confidencial, não "
            "aparecendo o nome do meu educando em parte alguma.",
            "Fui informado(a) de que, se o meu educando pedir ajuda ou se sentir mal durante a "
            "sessão, será encaminhado para o serviço de psicologia da unidade sanitária de "
            "referência, e de que receberá uma folha com os contactos de apoio disponíveis.",
            "Em caso de dúvida, posso contactar a investigadora ou o Comité Institucional de "
            "Bioética para a Saúde da Universidade Lúrio, através do telefone +258 845770070."):
        e.p(texto)
    h.paragrafo(doc, "Data: ____ / ____ / 2026", WD_ALIGN_PARAGRAPH.LEFT, depois=Pt(14))
    for linha in ("Assinatura ou impressão digital do encarregado de educação: "
                  "____________________________",
                  "Nome e assinatura da testemunha, para quem não sabe ler nem escrever: "
                  "____________________",
                  "Nome e assinatura da investigadora: ____________________________"):
        h.paragrafo(doc, linha, WD_ALIGN_PARAGRAPH.LEFT, depois=Pt(14))



def _apendice_d_assentimento(e, h, doc):
    h.quebra_pagina(doc)
    h.titulo(doc, "APÊNDICE D. TERMO DE ASSENTIMENTO DO ADOLESCENTE", 1)
    h.paragrafo(doc, "A preencher pelo próprio aluno, em qualquer idade, e válido como "
                "consentimento nos alunos com 18 ou mais anos.", WD_ALIGN_PARAGRAPH.LEFT,
                italico=True, tamanho=Pt(11), espaco=1.0, depois=Pt(10))
    e.p("Eu, ________________________________________________________, aceito participar num "
        "estudo sobre o que os jovens da minha escola pensam, sentem e fazem em situações de "
        "conflito, e sobre aquilo que se passa na família, na escola e no bairro.")
    for texto in (
            "Foi-me explicado que vou preencher um questionário sem o meu nome, com cerca de 45 "
            "minutos.",
            "Sei que não sou obrigado(a) a responder a nenhuma pergunta e que posso parar quando "
            "quiser, sem que isso tenha qualquer consequência para mim, para as minhas notas ou "
            "para a minha relação com os professores.",
            "Sei que algumas perguntas falam de castigos, brigas, violência e emoções difíceis e que, "
            "se me sentir incomodado(a), posso falar com a pessoa responsável pela sessão.",
            "Recebi e compreendi a folha de informação (Apêndice B) e sei que, em caso de "
            "dúvida, posso contactar a investigadora ou o Comité Institucional de Bioética para "
            "a Saúde da Universidade Lúrio, através do telefone +258 845770070.",
            "Sei que as minhas respostas não serão mostradas aos meus pais, aos meus professores "
            "nem aos meus colegas."):
        e.p(texto)
    h.paragrafo(doc, "Data: ____ / ____ / 2026", WD_ALIGN_PARAGRAPH.LEFT, depois=Pt(14))
    for linha in ("Assinatura do aluno: ____________________________",
                  "Nome e assinatura da investigadora: ____________________________"):
        h.paragrafo(doc, linha, WD_ALIGN_PARAGRAPH.LEFT, depois=Pt(14))



def _apendice_e_pedido_escola(e, h, doc):
    h.quebra_pagina(doc)
    h.titulo(doc, "APÊNDICE E. PEDIDO DE AUTORIZAÇÃO À DIRECÇÃO DA ESCOLA", 1)
    h.paragrafo(doc, "Exmo. Senhor Director da Escola Secundária de Muatala",
                WD_ALIGN_PARAGRAPH.LEFT, depois=Pt(12))
    e.p(f"Eu, {ESTUDANTE}, estudante finalista do Curso de Psicologia da Faculdade de "
        "Ciências de Saúde da Universidade Lúrio, venho por este meio solicitar a Vossa "
        "Excelência autorização para realizar, nesta escola, a recolha de dados do estudo "
        f"intitulado «{TITULO_CORRENTE}», sob orientação do {ORIENTADOR_COM_GRAU}.")
    e.p("A recolha consistirá na aplicação de um questionário anónimo, de cerca de quarenta e "
        "cinco minutos, "
        "a alunos de turmas seleccionadas por sorteio, em data a combinar com a direcção e fora da "
        "época de exames. O estudo foi aprovado pelo Comité Institucional de Bioética para a Saúde "
        "da Universidade Lúrio, com a referência ____________, e será precedido da autorização "
        "escrita dos encarregados de educação. A escola receberá, no final, um relatório com os "
        "resultados agregados e uma sessão de devolução dirigida à comunidade educativa.")
    h.paragrafo(doc, "Pede deferimento.", WD_ALIGN_PARAGRAPH.LEFT, depois=Pt(14))
    h.paragrafo(doc, "Nampula, ____ de ______________ de 2026", WD_ALIGN_PARAGRAPH.LEFT,
                depois=Pt(14))
    h.paragrafo(doc, "A requerente: ____________________________", WD_ALIGN_PARAGRAPH.LEFT,
                depois=Pt(14))


def escrever_apendices(e, h, doc):
    """Apendices A a E, cada um a comecar em pagina propria."""
    _folha_de_rosto_dos_apendices(e, h, doc)
    _apendice_a_questionario(e, h, doc)
    _apendice_a_desfechos(e, h, doc)
    _apendice_b_informacao(e, h, doc)
    _apendice_c_consentimento(e, h, doc)
    _apendice_d_assentimento(e, h, doc)
    _apendice_e_pedido_escola(e, h, doc)
