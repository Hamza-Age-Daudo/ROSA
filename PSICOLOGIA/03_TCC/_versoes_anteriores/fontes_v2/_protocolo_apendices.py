"""Apendices do protocolo: questionario, folha de informacao, consentimento e assentimento.

As perguntas do questionario sao guardadas sem numero; a numeracao e gerada por
intervalos_dos_blocos, para que acrescentar ou retirar um item nao obrigue a renumerar
o resto a mao nem a corrigir as instrucoes ("nas perguntas X a Y").
"""
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Cm, Pt

from _protocolo_texto import TITULO_CORRENTE

SOCIODEMOGRAFICO = [
    ("Código do questionário, código da turma e data de aplicação, preenchidos pelo aplicador:",
     "Questionário ______   Turma ______   Data ____ / ____ / 2026"),
    ("Idade em anos completos:", "______"),
    ("Sexo:", "( ) Masculino   ( ) Feminino"),
    ("Classe que frequenta:", "( ) 8.ª   ( ) 9.ª   ( ) 10.ª   ( ) 11.ª   ( ) 12.ª"),
    ("Turno:", "( ) Manhã   ( ) Tarde   ( ) Noite"),
    ("Já repetiu alguma classe?", "( ) Sim   ( ) Não"),
    ("Nos últimos 30 dias, faltou às aulas sem justificação?",
     "( ) Nenhum dia   ( ) 1 a 2 dias   ( ) 3 a 5 dias   ( ) 6 ou mais dias"),
    ("Com quem vive actualmente?",
     "( ) Com o pai e a mãe   ( ) Só com a mãe   ( ) Só com o pai   "
     "( ) Com avós ou outros familiares   ( ) Outra situação: ____________"),
    ("O pai está vivo?", "( ) Sim   ( ) Não   ( ) Não sabe"),
    ("A mãe está viva?", "( ) Sim   ( ) Não   ( ) Não sabe"),
    ("Quantas pessoas vivem na sua casa, incluindo o próprio?", "______"),
    ("Nos últimos 30 dias, alguma vez a sua família ficou sem comida suficiente?",
     "( ) Nunca   ( ) Raramente   ( ) Às vezes   ( ) Muitas vezes   ( ) Sempre"),
]

APGAR = [
    "Estou satisfeito com a ajuda que recebo da minha família quando tenho um problema.",
    "Estou satisfeito com a forma como a minha família fala comigo sobre os assuntos e "
    "partilha os problemas.",
    "Estou satisfeito com a forma como a minha família aceita e apoia os meus desejos de "
    "seguir novos caminhos.",
    "Estou satisfeito com a forma como a minha família demonstra afecto e reage aos meus "
    "sentimentos.",
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
    ("Nos últimos 30 dias, com que frequência os seus pais ou encarregados souberam o que "
     "fazia no seu tempo livre?", FREQUENCIA_PARENTAL),
    ("Nos últimos 30 dias, com que frequência os seus pais ou encarregados compreenderam os "
     "seus problemas e preocupações?", FREQUENCIA_PARENTAL),
]

VIOLENCIA = [
    ("Nos últimos 12 meses, algum adulto da sua casa lhe bateu, deu palmadas ou o castigou "
     "fisicamente?", FREQUENCIA_VIOLENCIA),
    ("Nos últimos 12 meses, algum adulto da sua casa o insultou, humilhou ou disse que "
     "gostaria que não tivesse nascido?", FREQUENCIA_VIOLENCIA),
    ("Nos últimos 12 meses, viu ou ouviu adultos da sua casa a baterem-se uns aos outros?",
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
    ("Nos últimos 30 dias, em quantos dias bebeu pelo menos uma bebida alcoólica?",
     "( ) Nenhum dia   ( ) 1 a 2 dias   ( ) 3 a 9 dias   ( ) 10 ou mais dias"),
    ("Nos últimos 30 dias, em quantos dias fumou cigarros ou usou tabaco?",
     "( ) Nenhum dia   ( ) 1 a 2 dias   ( ) 3 a 9 dias   ( ) 10 ou mais dias"),
    ("Alguma vez consumiu suruma, canábis ou outra droga?",
     "( ) Nunca   ( ) Sim, no passado   ( ) Sim, nos últimos 30 dias"),
    ("Quanto tempo por dia passa a ver filmes, vídeos ou jogos com conteúdo violento?",
     "( ) Menos de uma hora   ( ) Uma a três horas   ( ) Mais de três horas"),
]

SDQ_EMOCIONAL = [
    "Queixo-me muitas vezes de dores de cabeça, de dores de barriga ou de má disposição.",
    "Preocupo-me muito com as coisas.",
    "Sinto-me muitas vezes triste, desanimado ou com vontade de chorar.",
    "Fico nervoso em situações novas e perco facilmente a confiança.",
    "Tenho muitos medos e assusto-me com facilidade.",
]

BPAQ_ITENS = [
    ("Se for suficientemente provocado, posso bater noutra pessoa.", "Agressão física"),
    ("Já ameacei pessoas que conheço.", "Agressão física"),
    ("Já houve situações em que cheguei a agredir alguém fisicamente.", "Agressão física"),
    ("Os meus amigos dizem que discuto muito.", "Agressão verbal"),
    ("Não consigo evitar discutir quando as pessoas discordam de mim.", "Agressão verbal"),
    ("Quando as pessoas me irritam, digo-lhes o que penso delas.", "Agressão verbal"),
    ("Por vezes sinto-me como um barril de pólvora prestes a explodir.", "Ira"),
    ("Sou uma pessoa calma e tranquila. (item invertido)", "Ira"),
    ("Tenho dificuldade em controlar o meu temperamento.", "Ira"),
    ("Por vezes sinto que os outros se riem de mim nas minhas costas.", "Hostilidade"),
    ("Desconfio de pessoas desconhecidas que se mostram demasiado simpáticas.",
     "Hostilidade"),
    ("Às vezes pergunto-me porque me sinto tão amargurado com certas coisas.",
     "Hostilidade"),
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
    ("sdq", SDQ_EMOCIONAL),
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
        "internacional de experiências adversas na infância [[aceiq]], do inquérito global de "
        "saúde escolar [[gshs]], do Questionário de Capacidades e de Dificuldades "
        "[[goodman1997]] e das versões portuguesas do Questionário de Agressividade de Buss e "
        "Perry e do Questionário de Agressão Reactiva e Proactiva [[pechorro2016,pechorro2015]]. "
        "As notas em itálico e a coluna das dimensões destinam-se ao júri e não constam da versão "
        "entregue aos alunos.", italico=True, tamanho=Pt(10), espaco=1.0)
    e.p("Este questionário é anónimo. Não escreva o seu nome em parte alguma. Não há respostas "
        "certas nem erradas: interessa apenas o que se passa consigo. Pode deixar sem resposta "
        "qualquer pergunta que o incomode. O preenchimento demora cerca de trinta minutos.")

    h.subtitulo(doc, "Secção I. Dados sociodemográficos e escolares")
    _itens(h, doc, "sociodemografico")

    h.subtitulo(doc, "Secção II. Funcionamento familiar e supervisão parental")
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


def _apendice_a_desfechos(e, h, doc):
    h.subtitulo(doc, "Secção V. Consumo de substâncias e exposição a conteúdos violentos")
    _itens(h, doc, "substancias")

    h.subtitulo(doc, "Secção VI. Sintomas emocionais")
    _nota(h, doc, f"Nas perguntas {_intervalo('sdq')}, assinale: 0 = não é verdade; 1 = é um "
          "pouco verdade; 2 = é muito verdade. Subescala de sintomas emocionais do Questionário "
          "de Capacidades e de Dificuldades.")
    _tabela_de_escala(h, doc, "sdq", ["0", "1", "2"])

    h.subtitulo(doc, "Secção VII. Comportamento agressivo")
    _nota(h, doc, f"Nas perguntas {_intervalo('bpaq')}, indique até que ponto cada afirmação o "
          "descreve: 1 = muito diferente de mim; 2 = diferente de mim; 3 = nem uma coisa nem "
          "outra; 4 = parecido comigo; 5 = muito parecido comigo. Itens correspondentes à forma "
          "reduzida do Questionário de Agressividade de Buss e Perry; na aplicação será usada a "
          "versão portuguesa validada, mediante autorização dos autores.")
    h.tabela(doc, None, ["N.º", "Afirmação", "1", "2", "3", "4", "5", "Dimensão"],
             [[str(numero), texto] + ["( )"] * 5 + [dimensao]
              for numero, (texto, dimensao) in _numerados("bpaq")], None, Pt(9.5),
             larguras=[Cm(0.9), Cm(7.0), Cm(0.8), Cm(0.8), Cm(0.8), Cm(0.8), Cm(0.8), Cm(2.6)])
    _nota(h, doc, f"Nas perguntas {_intervalo('rpq')}, indique com que frequência tal lhe "
          "aconteceu: 0 = nunca; 1 = às vezes; 2 = muitas vezes. Itens exemplificativos do "
          "Questionário de Agressão Reactiva e Proactiva; na aplicação serão usados os vinte e "
          "três itens da versão portuguesa validada, mediante autorização dos autores.")
    h.tabela(doc, None, ["N.º", "Afirmação", "0", "1", "2", "Forma"],
             [[str(numero), texto] + ["( )"] * 3 + [forma]
              for numero, (texto, forma) in _numerados("rpq")], None, Pt(9.5),
             larguras=[Cm(0.9), Cm(8.4), Cm(0.9), Cm(0.9), Cm(0.9), Cm(2.5)])
    e.p("Obrigado pela sua colaboração. Se alguma pergunta o deixou preocupado ou triste, "
        "procure o aplicador no fim da sessão: ele indicará onde pode obter apoio.")



def _apendice_b_informacao(e, h, doc):
    h.quebra_pagina(doc)
    h.titulo(doc, "APÊNDICE B. FOLHA DE INFORMAÇÃO AO PARTICIPANTE E AO ENCARREGADO DE EDUCAÇÃO", 1)
    for rotulo, texto in (
            ("Título do estudo:", TITULO_CORRENTE + "."),
            ("Investigador principal:", "(nome do estudante), estudante finalista do Curso de "
             "Psicologia da Faculdade de Ciências de Saúde da Universidade Lúrio."),
            ("Objectivo:", "Compreender que factores da família, da escola, do grupo de amigos e "
             "do bairro se relacionam com o comportamento agressivo dos adolescentes, para ajudar "
             "a escola a planear acções de prevenção."),
            ("Selecção dos participantes:", "A turma foi sorteada entre as turmas da escola. "
             "Todos os alunos da turma com idade entre os 10 e os 19 anos são convidados a "
             "participar."),
            ("Procedimentos:", "Se aceitar participar, o aluno preencherá um questionário na sala "
             "de aula, durante cerca de trinta minutos, sem escrever o nome. Ninguém saberá quais "
             "foram as suas respostas."),
            ("Participação voluntária:", "A participação é livre. O aluno pode recusar ou "
             "interromper o preenchimento em qualquer momento, sem qualquer prejuízo nas notas ou "
             "no tratamento que recebe na escola. A recusa do aluno é respeitada mesmo que o "
             "encarregado de educação tenha autorizado."),
            ("Riscos e desconfortos:", "Algumas perguntas falam de castigos, brigas e situações "
             "de violência e podem causar desconforto. O aluno pode não responder a qualquer "
             "pergunta. Estará presente uma pessoa preparada para conversar com quem se sentir "
             "incomodado."),
            ("Benefícios:", "Não há qualquer pagamento. Os resultados ajudarão a escola a "
             "organizar acções de apoio. Como o questionário é anónimo, ninguém saberá quem deu "
             "cada resposta; por isso, todos os alunos recebem uma folha com os contactos de "
             "apoio, e quem pedir ajuda ou se sentir mal durante a sessão será encaminhado, com o "
             "seu conhecimento, para o serviço de psicologia da unidade sanitária de referência."),
            ("Confidencialidade:", "O questionário é anónimo e identificado apenas por um código. "
             "As folhas de autorização serão guardadas separadamente das respostas. Os dados serão "
             "usados apenas para este estudo."),
            ("Partilha de resultados:", "Os resultados serão apresentados de forma agregada à "
             "escola, à Universidade Lúrio e às autoridades de educação e de saúde, sem "
             "identificar qualquer aluno."),
            ("Contactos:", "Investigador: (nome), telefone +258 ____________, correio electrónico "
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
        f"encarregado de educação do aluno ou aluna ________________________________________, "
        f"declaro que autorizo a sua participação no estudo intitulado «{TITULO_CORRENTE}».")
    for texto in (
            "Declaro que me foi explicado, em linguagem que compreendi, o objectivo do estudo, o "
            "que será pedido ao meu educando, a duração do preenchimento e a ausência de riscos "
            "físicos.",
            "Fui informado de que a participação é voluntária, de que o meu educando pode recusar "
            "ou desistir em qualquer momento, sem qualquer prejuízo nas notas ou no tratamento "
            "que recebe na escola, e de que a recusa dele será respeitada mesmo depois desta "
            "autorização.",
            "Compreendi que não haverá qualquer compensação material ou financeira e que as "
            "respostas serão usadas apenas para os fins deste estudo, de forma anónima, não "
            "aparecendo o nome do meu educando em parte alguma.",
            "Fui informado de que, se o meu educando pedir ajuda ou se sentir mal durante a "
            "sessão, será encaminhado para o serviço de psicologia da unidade sanitária de "
            "referência, e de que receberá uma folha com os contactos de apoio disponíveis.",
            "Em caso de dúvida, posso contactar o investigador ou o Comité Institucional de "
            "Bioética para a Saúde da Universidade Lúrio, através do telefone +258 845770070."):
        e.p(texto)
    h.paragrafo(doc, "Data: ____ / ____ / 2026", WD_ALIGN_PARAGRAPH.LEFT, depois=Pt(14))
    for linha in ("Assinatura ou impressão digital do encarregado de educação: "
                  "____________________________",
                  "Nome e assinatura da testemunha, para quem não sabe ler nem escrever: "
                  "____________________",
                  "Nome e assinatura do investigador: ____________________________"):
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
            "Foi-me explicado que vou preencher um questionário anónimo, com cerca de trinta "
            "minutos, e que não devo escrever o meu nome.",
            "Sei que não sou obrigado a responder a nenhuma pergunta e que posso parar quando "
            "quiser, sem que isso tenha qualquer consequência para mim, para as minhas notas ou "
            "para a minha relação com os professores.",
            "Sei que algumas perguntas falam de castigos, brigas e violência e que, se me sentir "
            "incomodado, posso falar com a pessoa responsável pela sessão.",
            "Sei que as minhas respostas não serão mostradas aos meus pais, aos meus professores "
            "nem aos meus colegas."):
        e.p(texto)
    h.paragrafo(doc, "Data: ____ / ____ / 2026", WD_ALIGN_PARAGRAPH.LEFT, depois=Pt(14))
    for linha in ("Assinatura do aluno: ____________________________",
                  "Nome e assinatura do investigador: ____________________________"):
        h.paragrafo(doc, linha, WD_ALIGN_PARAGRAPH.LEFT, depois=Pt(14))



def _apendice_e_pedido_escola(e, h, doc):
    h.quebra_pagina(doc)
    h.titulo(doc, "APÊNDICE E. PEDIDO DE AUTORIZAÇÃO À DIRECÇÃO DA ESCOLA", 1)
    h.paragrafo(doc, "Exmo. Senhor Director da Escola Secundária de Muatala",
                WD_ALIGN_PARAGRAPH.LEFT, depois=Pt(12))
    e.p("Eu, (nome do estudante), estudante finalista do Curso de Psicologia da Faculdade de "
        "Ciências de Saúde da Universidade Lúrio, venho por este meio solicitar a Vossa "
        "Excelência autorização para realizar, nesta escola, a recolha de dados do estudo "
        f"intitulado «{TITULO_CORRENTE}», sob orientação de (nome do orientador).")
    e.p("A recolha consistirá na aplicação de um questionário anónimo, de cerca de trinta minutos, "
        "a alunos de turmas seleccionadas por sorteio, em data a combinar com a direcção e fora da "
        "época de exames. O estudo foi aprovado pelo Comité Institucional de Bioética para a Saúde "
        "da Universidade Lúrio, com a referência ____________, e será precedido da autorização "
        "escrita dos encarregados de educação. A escola receberá, no final, um relatório com os "
        "resultados agregados e uma sessão de devolução dirigida à comunidade educativa.")
    h.paragrafo(doc, "Pede deferimento.", WD_ALIGN_PARAGRAPH.LEFT, depois=Pt(14))
    h.paragrafo(doc, "Nampula, ____ de ______________ de 2026", WD_ALIGN_PARAGRAPH.LEFT,
                depois=Pt(14))
    h.paragrafo(doc, "O requerente: ____________________________", WD_ALIGN_PARAGRAPH.LEFT,
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
