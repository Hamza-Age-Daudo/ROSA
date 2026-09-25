"""Seccoes 7 a 12 do protocolo: metodologia, resultados esperados, divulgacao,
cronograma, orcamento e recursos humanos."""
from docx.shared import Cm, Pt

from _protocolo_texto import ESTUDANTE, ORIENTADOR_COM_GRAU
from _protocolo_amostra import (DEFF_SENSIBILIDADE, EXPOSICAO_TIPICA, POPULACAO_EXEMPLO,
                                POPULACOES, PREDITORES_LINEAR, PREVALENCIA_LUTAS, amostra_base,
                                amostra_efectiva, amostra_para, cenarios_amostra,
                                efeito_minimo_mediacao, eventos_esperados,
                                f2_minimo_detectavel, n0_exacto, or_minimo_detectavel,
                                parametros_maximos_logistica, poder_mediacao)


def _decimal(valor, casas):
    """Numero com virgula decimal, como exige a casa."""
    return f"{valor:.{casas}f}".replace(".", ",")


def _milhares(valor):
    return f"{valor:,}".replace(",", ".")


VARIAVEIS = [
    ["Idade", "Independente", "Quantitativa discreta", "Anos completos; grupos de 10 a 14 e de "
     "15 a 19 anos"],
    ["Sexo", "Independente", "Qualitativa nominal", "Masculino; feminino"],
    ["Classe frequentada", "Independente", "Qualitativa ordinal",
     "Da 7.ª ou 8.ª à 12.ª; nos modelos, variável ordinal com um só parâmetro"],
    ["Turno", "Descritiva", "Qualitativa nominal", "Manhã; tarde; noite"],
    ["Repetência escolar", "Independente", "Qualitativa nominal", "Sim; não"],
    ["Absentismo escolar", "Independente", "Qualitativa nominal",
     "Faltou sem justificação em um ou mais dias nos últimos 30 dias: sim; não"],
    ["Com quem vive", "Independente", "Qualitativa nominal",
     "Ambos os progenitores; um progenitor; outros familiares; outra situação"],
    ["Orfandade", "Independente", "Qualitativa nominal", "Órfão de pai, de mãe ou de ambos: sim; "
     "não"],
    ["Tamanho do agregado", "Descritiva", "Quantitativa discreta", "Número de pessoas que vivem "
     "na casa"],
    ["Insegurança alimentar", "Independente", "Qualitativa ordinal",
     "Falta de comida nos últimos 30 dias, de nunca a sempre; às vezes ou mais: sim; não"],
    ["Funcionamento familiar", "Independente", "Quantitativa discreta",
     "APGAR familiar, de 0 a 10 nos modelos; na descrição, funcional (7 a 10), disfunção "
     "moderada (4 a 6) e grave (0 a 3)"],
    ["Supervisão parental", "Independente", "Quantitativa discreta",
     "Soma dos dois itens do GSHS sobre a verificação dos trabalhos e o conhecimento do tempo "
     "livre, cotados de 0 (nunca) a 4 (sempre), de 0 a 8"],
    ["Ligação parental", "Independente", "Quantitativa discreta",
     "Item do GSHS sobre a compreensão dos problemas pelos pais, de 0 a 4"],
    ["Castigo físico em casa", "Independente", "Qualitativa nominal",
     "Item adaptado do ACE-IQ, com referência aos últimos 12 meses: sim; não"],
    ["Violência psicológica em casa", "Independente", "Qualitativa nominal",
     "Item adaptado do ACE-IQ, últimos 12 meses: sim; não"],
    ["Violência entre adultos do agregado", "Independente", "Qualitativa nominal",
     "Viu ou ouviu adultos da casa a agredirem-se, últimos 12 meses: sim; não"],
    ["Castigo físico na escola", "Independente", "Qualitativa nominal",
     "Professor ou funcionário bateu-lhe ou castigou-o, últimos 12 meses: sim; não"],
    ["Exposição a violência comunitária", "Independente", "Qualitativa nominal",
     "Viu alguém ser agredido no bairro nos últimos 12 meses: sim; não"],
    ["Índice de exposição à violência", "Preditora na mediação",
     "Quantitativa discreta", "Soma dos cinco itens da Secção III, cotados de 0 (nunca) a 3 "
     "(muitas vezes), de 0 a 15"],
    ["Número de experiências adversas", "Independente (modelo próprio)", "Quantitativa discreta",
     "Contagem de 0 a 8: castigo físico em casa, violência psicológica, violência entre adultos "
     "do agregado, violência comunitária, castigo físico na escola, orfandade, não viver com "
     "nenhum progenitor e insegurança alimentar; contagem adaptada, que não equivale à "
     "pontuação do ACE-IQ"],
    ["Vitimização por bullying", "Independente", "Qualitativa nominal",
     "Item do GSHS nos últimos 30 dias: sim; não"],
    ["Ligação à escola", "Independente", "Quantitativa discreta",
     "Soma de três itens, cotados de 1 a 4, de 3 a 12; tercis apenas na descrição"],
    ["Pares desviantes", "Independente", "Quantitativa discreta",
     "Soma de três itens sobre amigos próximos, cotados de 0 (nenhum) a 3 (três ou mais), de 0 "
     "a 9"],
    ["Consumo de álcool", "Independente", "Qualitativa nominal",
     "Consumo em pelo menos um dia nos últimos 30 dias: sim; não"],
    ["Consumo de tabaco ou de outras drogas", "Independente", "Qualitativa nominal", "Sim; não"],
    ["Exposição a conteúdos violentos", "Independente", "Qualitativa ordinal",
     "Horas diárias de exposição: menos de uma; uma a três; mais de três"],
    ["Dificuldades de regulação emocional", "Independente e mediadora",
     "Quantitativa discreta", "Pontuação total da DERS-SF sem os itens de consciência "
     "emocional, de 15 a 75; a medida exclui, por isso, a componente de consciência"],
    ["Sintomas emocionais", "Independente", "Quantitativa discreta",
     "Subescala emocional do SDQ, de 0 a 10"],
    ["Hiperactividade e desatenção", "Independente", "Quantitativa discreta",
     "Subescala de hiperactividade e desatenção do SDQ, de 0 a 10"],
    ["Problemas de relacionamento com os pares", "Descritiva", "Quantitativa discreta",
     "Subescala de problemas com os pares do SDQ, de 0 a 10; não entra nos modelos, por "
     "sobreposição com a vitimização por bullying"],
    ["Comportamento pró-social", "Independente", "Quantitativa discreta",
     "Subescala pró-social do SDQ, de 0 a 10; mede comportamentos pró-sociais e não equivale "
     "aos traços de insensibilidade emocional"],
    ["Auto-estima", "Independente", "Quantitativa discreta",
     "Escala de Auto-Estima de Rosenberg, de 10 a 40"],
    ["Exposição a acontecimento potencialmente traumático", "Independente",
     "Qualitativa nominal", "Pergunta de filtro da Secção VIII: sim; não"],
    ["Sintomas de stress pós-traumático", "Independente", "Quantitativa discreta",
     "CRIES-8, de 0 a 40, com 0 para quem não relata acontecimento; 17 ou mais: risco provável"],
    ["Agressividade total", "Dependente (principal)", "Quantitativa discreta",
     "Pontuação total do BPAQ-SF, de 12 a 60"],
    ["Dimensões da agressividade", "Dependente", "Quantitativa discreta",
     "Agressão física, agressão verbal, ira e hostilidade, de 3 a 15 cada"],
    ["Agressão comportamental", "Dependente (mediação)", "Quantitativa discreta",
     "Soma das dimensões de agressão física e verbal do BPAQ-SF, de 6 a 30"],
    ["Agressão reactiva e proactiva", "Dependente", "Quantitativa discreta",
     "Pontuações das duas subescalas do RPQ"],
    ["Participação em lutas físicas", "Dependente (modelo logístico)", "Qualitativa nominal",
     "Pelo menos uma luta física nos últimos 12 meses: sim; não"],
    ["Problemas de comportamento", "Dependente", "Qualitativa ordinal",
     "Subescala do SDQ, alunos dos 11 aos 17 anos: normal; limítrofe; anormal, segundo as normas "
     "britânicas de rastreio"],
    ["Envolvimento em violência interpessoal", "Descritiva", "Qualitativa nominal",
     "Indicador do GSHS, luta física ou agressão física sofrida nos últimos 12 meses, para "
     "comparação com a África subsariana"],
]

CRONOGRAMA = [
    ["Revisão da literatura e elaboração do protocolo", "X", "X", "", "", "", "", ""],
    ["Painel de peritos e versão do instrumento para pré-teste", "", "X", "", "", "", "", ""],
    ["Submissão e aprovação pelo comité de bioética", "", "X", "X", "", "", "", ""],
    ["Autorizações do serviço distrital de educação e da escola", "", "", "X", "", "", "", ""],
    ["Pré-teste cognitivo e versão final do instrumento", "", "", "X", "", "", "", ""],
    ["Recolha de dados na escola", "", "", "X", "X", "", "", ""],
    ["Introdução, limpeza e validação da base de dados", "", "", "", "X", "X", "", ""],
    ["Análise estatística", "", "", "", "", "X", "X", ""],
    ["Redacção do relatório final", "", "", "", "", "", "X", ""],
    ["Entrega, defesa e devolução dos resultados à escola", "", "", "", "", "", "", "X"],
]

CRONOGRAMA_COLUNAS = ["Actividade", "Jul-Ago 2026", "Set 2026", "Out 2026", "Nov 2026",
                      "Dez 2026", "Jan-Fev 2027", "Mar 2027"]

ORCAMENTO = [
    ["Impressão de questionários e de termos de consentimento", "1.200 exemplares", "20", "24.000"],
    ["Material de escritório e de codificação", "1 conjunto", "4.000", "4.000"],
    ["Transporte da equipa para a escola", "25 deslocações", "400", "10.000"],
    ["Comunicação, telefone e Internet", "5 meses", "1.500", "7.500"],
    ["Alimentação da equipa no terreno", "20 dias", "400", "8.000"],
    ["Honorários de assistentes de recolha e de digitação", "3 pessoas", "9.000", "27.000"],
    ["Formação da equipa, incluindo primeiros socorros psicológicos, e pré-teste", "1 sessão",
     "5.000", "5.000"],
    ["Sessão de devolução dos resultados à escola", "1 sessão", "6.000", "6.000"],
    ["Impressão e encadernação do relatório final", "8 exemplares", "1.200", "9.600"],
    ["Imprevistos, 10 por cento", "", "", "10.110"],
    ["Total geral", "", "", "111.210"],
]

RECURSOS_HUMANOS = [
    [ESTUDANTE, "Estudante finalista de Psicologia", "Investigadora principal"],
    [ORIENTADOR_COM_GRAU, "Docente da Faculdade de Ciências de Saúde", "Orientação científica"],
    ["Assistentes de recolha", "Estudantes de Psicologia ou de Ciências de Saúde",
     "Aplicação dos questionários, controlo de qualidade e digitação em dupla entrada"],
    ["Psicólogo clínico de referência", "Psicólogo da unidade sanitária de referência ou docente "
     "de psicologia da FCS, presente ou contactável em todas as sessões",
     "Acolhimento dos adolescentes que peçam ajuda e encaminhamento"],
    ["Direcção da escola", "Direcção da Escola Secundária de Muatala",
     "Autorização, articulação logística e devolução dos resultados"],
]


def _desenho_local_e_populacao(e):
    e.h2("7.1. Tipo e desenho do estudo")
    e.p("Trata-se de um estudo de corte transversal, analítico, de abordagem quantitativa. O "
        "desenho transversal é adequado porque permite estimar, num único momento, o nível de "
        "comportamento agressivo, o funcionamento psicológico e a frequência dos factores "
        "psicossociais, e testar as associações previstas nas hipóteses, sem exigir o seguimento "
        "dos participantes [[charan2013]]. Reconhece-se, como limitação inerente ao desenho, a "
        "impossibilidade de estabelecer a ordem temporal entre exposição e desfecho, pelo que os "
        "resultados serão interpretados como associações e não como relações de causa e efeito. "
        "Os resultados serão relatados segundo a lista de verificação Strengthening the "
        "Reporting of Observational Studies in Epidemiology (STROBE), aplicável a estudos "
        "observacionais [[strobe2007]].")

    e.h2("7.2. Local e período do estudo")
    e.p("O estudo será realizado na Escola Secundária de Muatala, situada no bairro de Muatala, "
        "cidade de Nampula, província de Nampula, no norte de Moçambique. Trata-se de um "
        "estabelecimento público de ensino secundário, inserido num bairro periurbano de elevada "
        "densidade populacional, com predomínio da língua Emakhuwa e rendimento familiar "
        "maioritariamente proveniente do comércio informal e da agricultura. A recolha de dados "
        "decorrerá no segundo semestre de 2026, entre Outubro e Novembro, isto é, no terceiro "
        "trimestre do ano lectivo, depois "
        "da aprovação ética, nas semanas lectivas anteriores às avaliações finais e em datas a "
        "acordar com a direcção da escola, começando pelas turmas das classes com exame. Se o "
        "parecer ético chegar depois de meados de Outubro, a recolha passará para o primeiro "
        "trimestre do ano lectivo de 2027, e o período indicado no título será ajustado em "
        "articulação com a coordenação do curso.")

    e.h2("7.3. População do estudo")
    e.p("A população-alvo é constituída por todos os adolescentes dos 10 aos 19 anos de idade "
        "regularmente matriculados e em frequência efectiva na Escola Secundária de Muatala no "
        "segundo semestre de 2026, em todos os turnos e em todas as classes leccionadas. O número "
        "exacto de alunos elegíveis, desagregado por classe, turma e turno, será obtido junto da "
        "direcção da escola no momento da aprovação do estudo e constituirá a base de "
        "amostragem.")


def _desenho_amostral(e):
    e.h2("7.4. Amostragem e cálculo do tamanho da amostra")
    e.p("A amostra será seleccionada por amostragem probabilística estratificada por "
        "conglomerados, com a classe como estrato e a turma como conglomerado: dentro de cada "
        "classe sortear-se-ão turmas inteiras, e serão convidados todos os alunos elegíveis das "
        "turmas sorteadas. O número de turmas por classe será proporcional ao número de alunos "
        "matriculados e nunca inferior a duas, pelo que o número de turmas a sortear será o maior "
        "entre o necessário para atingir a amostra da Tabela 1 e duas turmas por classe, e a "
        "amostra efectivamente convidada pode exceder os valores da tabela; se alguma classe não "
        "tiver turmas suficientes, as "
        "classes serão agrupadas em dois ciclos, da 7.ª ou 8.ª à 9.ª e da 10.ª à 12.ª. Cada aluno "
        "receberá um peso amostral igual ao inverso da probabilidade de a sua turma ser sorteada, "
        "ajustado à não resposta dentro da turma. A amostragem probabilística assegura a "
        "representatividade, a validade externa dos resultados e a legitimidade dos testes de "
        "associação previstos.")


def _amostragem_e_criterios(e, h, doc):
    _desenho_amostral(e)
    e.p("O tamanho mínimo da amostra foi calculado pela fórmula da proporção única para populações "
        "grandes [[charan2013]]:")
    h.formula(doc, [("n", None), ("0", "sub"), (" = Z", None), ("2", "sup"),
                    (" × p × (1 - p) / d", None), ("2", "sup")])
    n0, n_deff = amostra_base()
    e.p("em que Z corresponde a 1,96, para um nível de confiança de 95 por cento; p é a "
        "prevalência esperada de envolvimento em violência interpessoal, isto é, ter participado "
        "numa luta física ou ter sido agredido fisicamente nos últimos 12 meses, fixada em 53,7 "
        "por cento, valor obtido com este mesmo indicador do inquérito global de saúde escolar na "
        "análise agrupada de oito países da África subsariana para adolescentes dos 10 aos 19 "
        "anos [[aboagye2021a]]; e d é a precisão absoluta admitida, de 5 pontos percentuais. O "
        "indicador é medido directamente por duas perguntas do questionário (Apêndice A), e a "
        "proximidade de p a 50 por cento torna o cálculo conservador, porque é nesse valor que a "
        "amostra necessária atinge o máximo. Substituindo os valores:")
    h.formula(doc, [("n", None), ("0", "sub"), (" = 1,96", None), ("2", "sup"),
                    (" × 0,537 × (1 - 0,537) / 0,05", None), ("2", "sup"),
                    (f" = {_decimal(n0_exacto(), 2)}", None)])
    e.p(f"valor arredondado para {n0} participantes. Como as turmas são sorteadas inteiras, os "
        "alunos da mesma turma tendem a ser mais parecidos entre si do que alunos escolhidos ao "
        "acaso, o que se corrige com o efeito de desenho (deff), igual a 1 + (m - 1) × c, em que "
        "m é o número médio de alunos por turma e c o coeficiente de correlação intraclasse. Com "
        "turmas de cerca de 50 alunos, um efeito de desenho de 1,5 corresponde a uma correlação "
        f"intraclasse de 0,01 e eleva o valor para {n_deff} participantes. Este resultado é "
        "depois corrigido para a população finita da escola, com N alunos elegíveis, e acrescido "
        "de 10 por cento para compensar recusas e questionários incompletos:")
    h.formula(doc, [("n", None), ("c", "sub"), (f" = {n_deff} / [1 + ({n_deff} - 1) / N]", None),
                    ("        n", None), ("f", "sub"), (" = n", None), ("c", "sub"),
                    (" / 0,90", None)])
    _tabela_1_e_cenario(e, h, doc)
    _poder_para_o_objectivo_analitico(e)


def _tabela_1_e_cenario(e, h, doc):
    sensibilidade = _decimal(DEFF_SENSIBILIDADE, 1)
    h.tabela(doc, "Tabela 1: Tamanho da amostra segundo o número de alunos elegíveis na escola.",
             ["Alunos elegíveis (N)", "Amostra corrigida para população finita",
              "Amostra final, com 10% para não resposta",
              f"Amostra final com efeito de desenho de {sensibilidade}"],
             cenarios_amostra(),
             "Fonte: a autora, 2026. Cálculo com Z=1,96; p=0,537; d=0,05; efeito de desenho de 1,5 "
             f"e, na última coluna, de {sensibilidade}.",
             larguras=[Cm(3.4), Cm(4.2), Cm(4.2), Cm(4.2)])
    _corrigida, final_exemplo = amostra_para(POPULACAO_EXEMPLO)
    _corrigida, final_sensibilidade = amostra_para(POPULACAO_EXEMPLO, DEFF_SENSIBILIDADE)
    e.p("O cenário definitivo será fixado assim que a direcção da escola confirmar o número de "
        "alunos elegíveis e o tamanho médio das turmas. A título indicativo, para uma população "
        f"de {_milhares(POPULACAO_EXEMPLO)} alunos, o estudo necessitará de {final_exemplo} "
        "participantes. Como a correlação intraclasse da agressividade dentro das turmas pode ser "
        f"superior a 0,01, a última coluna da Tabela 1 apresenta, como análise de sensibilidade, "
        f"a amostra necessária com um efeito de desenho de {sensibilidade}, que no mesmo cenário "
        f"é de {final_sensibilidade} alunos; se o número de alunos elegíveis o permitir, será "
        "este o tamanho adoptado.")


def _poder_para_o_objectivo_analitico(e):
    """Verifica se a amostra descritiva chega para os modelos de regressao e a mediacao."""
    respondentes, efectiva = amostra_efectiva(POPULACAO_EXEMPLO)
    f2 = f2_minimo_detectavel(efectiva)
    e.p("O cálculo anterior dimensiona a estimativa descritiva. Para o objectivo analítico, "
        "verificou-se se a mesma amostra tem poder suficiente para os modelos de regressão, com "
        "um nível de significância de 5 por cento e um poder de 80 por cento [[faul2009]]. No "
        f"cenário de {_milhares(POPULACAO_EXEMPLO)} alunos esperam-se {respondentes} "
        "questionários válidos, que, divididos pelo efeito de desenho, equivalem a cerca de "
        f"{round(efectiva)} participantes seleccionados por amostragem aleatória simples. Com "
        f"este tamanho efectivo, a regressão linear múltipla, com até {PREDITORES_LINEAR} "
        "parâmetros, detecta o efeito isolado de uma variável a partir de um tamanho de efeito "
        f"de Cohen, medido pelo f ao quadrado, de {_decimal(f2, 3)}, o que corresponde a cerca de "
        f"{_decimal(100 * f2 / (1 + f2), 1)} por cento de variância explicada, um efeito "
        "pequeno. Numa comparação bivariada, uma exposição presente em "
        f"{round(100 * EXPOSICAO_TIPICA)} por cento dos adolescentes só é detectada com o mesmo "
        f"poder a partir de um odds ratio de {_decimal(or_minimo_detectavel(efectiva), 2)}, e o "
        "limiar será mais elevado no modelo ajustado. Por esta razão, a regressão linear sobre a "
        "pontuação contínua constitui a análise principal e a regressão logística a análise "
        "complementar.")
    _poder_no_pior_cenario_e_logistica(e, respondentes)
    _poder_da_mediacao(e, efectiva, amostra_efectiva(min(POPULACOES))[1])


def _poder_no_pior_cenario_e_logistica(e, respondentes):
    pior_respondentes, pior_efectiva = amostra_efectiva(min(POPULACOES))
    e.p(f"No cenário mais desfavorável da Tabela 1, de {_milhares(min(POPULACOES))} alunos, "
        f"esperam-se {pior_respondentes} questionários válidos e um tamanho efectivo de "
        f"{round(pior_efectiva)}, com um f ao quadrado mínimo detectável de "
        f"{_decimal(f2_minimo_detectavel(pior_efectiva), 3)} e um odds ratio mínimo de "
        f"{_decimal(or_minimo_detectavel(pior_efectiva), 2)}. O desfecho do modelo logístico é a "
        "participação em lutas físicas nos últimos 12 meses, com uma prevalência esperada de "
        f"{_decimal(100 * PREVALENCIA_LUTAS, 1)} por cento [[han2019]], o que corresponde a "
        f"{eventos_esperados(respondentes)} eventos no cenário de referência e a "
        f"{eventos_esperados(pior_respondentes)} no mais desfavorável. Seguindo a regra de pelo "
        "menos dez eventos por parâmetro estimado, o modelo terá no máximo "
        f"{parametros_maximos_logistica(respondentes)} parâmetros no primeiro caso e "
        f"{parametros_maximos_logistica(pior_respondentes)} no segundo, contando cada categoria "
        "das variáveis qualitativas [[peduzzi1996]]; a classe entrará como variável ordinal, com "
        "um só parâmetro, e, se for necessário incluir mais parâmetros do que este limite "
        "permite, usar-se-á a regressão logística penalizada de Firth [[firth1993]]. Como se "
        "prevêem cerca de 12 turmas, os testes terão poucos graus de liberdade do desenho e serão "
        "mais conservadores do que este cálculo indica.")


def _poder_da_mediacao(e, efectiva, pior_efectiva):
    minimo = efeito_minimo_mediacao(efectiva)
    e.p("Para a análise de mediação exploratória, o poder foi estimado pelo teste de "
        "significância conjunta dos dois caminhos do efeito indirecto, um dos testes do efeito "
        "mediado para os quais Fritz e MacKinnon tabelaram o tamanho da amostra necessário "
        f"[[fritz2007]]. Com o tamanho efectivo de {round(efectiva)} do cenário de referência, "
        "o poder é de "
        f"{round(100 * poder_mediacao(0.26, 0.26, efectiva))} por cento quando os dois caminhos "
        "têm coeficientes padronizados de 0,26, valor intermédio entre um efeito pequeno e um "
        "médio, e o menor efeito comum detectável com poder de 80 por cento é de "
        f"{_decimal(minimo, 2)}. Efeitos indirectos compostos por dois caminhos pequenos, de "
        "0,14, só seriam detectados com poder de "
        f"{round(100 * poder_mediacao(0.14, 0.14, efectiva))} por cento, e com "
        f"{round(100 * poder_mediacao(0.14, 0.14, pior_efectiva))} por cento no cenário mais "
        "desfavorável, limitação que será tida em conta na interpretação.")


def _criterios_de_elegibilidade(e):
    e.h2("7.5. Critérios de inclusão e de exclusão")
    e.h3("7.5.1. Critérios de inclusão")
    for criterio in (
            "Idade compreendida entre os 10 e os 19 anos completos à data da recolha;",
            "Matrícula e frequência efectiva na Escola Secundária de Muatala no segundo semestre "
            "de 2026;",
            "Assentimento do adolescente e, nos menores de 18 anos, consentimento livre e "
            "esclarecido do pai, da mãe ou do responsável legal;",
            "Presença na aplicação do questionário, na visita marcada ou na visita de recuperação; se "
            "a aplicação for dividida em duas partes (7.8), presença em ambas."):
        e.marca(criterio)
    e.h3("7.5.2. Critérios de exclusão")
    for criterio in (
            "Recusa em participar, manifestada pelo adolescente ou pelo responsável legal;",
            "Estudante em situação de crise emocional aguda no momento da recolha, caso em que "
            "será acolhido e encaminhado e não inquirido."):
        e.marca(criterio)
    e.p("Os alunos com dificuldade de leitura não são excluídos: responderão com aplicação "
        "assistida individual, num espaço separado da sala, em que um membro da equipa lê os "
        "itens em voz baixa, sem sugerir respostas, e o aluno assinala as respostas numa folha que "
        "o aplicador não vê; a opção fica registada no questionário, para análise de "
        "sensibilidade.")


def _variaveis_e_instrumento(e, h, doc):
    e.h2("7.6. Variáveis do estudo e definições operacionais")
    e.p("A variável dependente principal é a agressividade total, medida pela pontuação do "
        "BPAQ-SF, analisada também por dimensão e, na análise de mediação, pela sua componente "
        "comportamental, isto é, a soma das dimensões de agressão física e verbal. As formas "
        "reactiva e proactiva são medidas pelo RPQ. Para o modelo logístico complementar usa-se a "
        "participação em lutas físicas nos últimos 12 meses, indicador comportamental com "
        "prevalência conhecida noutros países. O indicador de envolvimento em violência "
        "interpessoal, que junta lutas e agressão sofrida, é usado apenas para descrever a escola "
        "e compará-la com os dados da África subsariana. As variáveis independentes organizam-se "
        "em dois grupos, segundo o esquema conceptual: os factores psicológicos individuais, "
        "entre os quais as dificuldades de regulação emocional, que funcionam também como "
        "variável mediadora, e os factores psicossociais do contexto familiar, escolar, do grupo "
        "de pares e comunitário. O quadro seguinte apresenta a definição operacional de cada "
        "variável.")
    h.tabela(doc, "Quadro 2: Definição operacional das variáveis do estudo.",
             ["Variável", "Tipo", "Natureza e escala", "Categorias ou medição"],
             VARIAVEIS, "Fonte: a autora, 2026.",
             larguras=[Cm(4.0), Cm(2.8), Cm(2.8), Cm(6.4)])


def _seccoes_do_questionario(e):
    for seccao in (
            "Secção I, dados sociodemográficos e escolares, construída para este estudo a partir "
            "das variáveis do Quadro 2;",
            "Secção II, contexto familiar, com o APGAR familiar de cinco itens [[smilkstein1978]] "
            "e itens de supervisão e ligação parental do inquérito global de saúde escolar "
            "[[gshs]];",
            "Secção III, exposição à violência, com itens adaptados do ACE-IQ, relativos ao "
            "castigo físico e à violência psicológica em casa, ao castigo físico na escola, à "
            "violência testemunhada em casa e à violência presenciada na comunidade; como o "
            "ACE-IQ original é retrospectivo e destinado a maiores de 18 anos, os itens foram "
            "adaptados aos últimos 12 meses [[aceiq]];",
            "Secção IV, contexto escolar e grupo de pares, com itens de vitimização por bullying, "
            "de envolvimento em lutas físicas e de agressão física sofrida e itens de ligação à "
            "escola e de afiliação a pares desviantes [[gshs]];",
            "Secção V, consumo de substâncias psicoactivas e exposição a conteúdos violentos, com "
            "itens do inquérito global de saúde escolar [[gshs]];",
            "Secção VI, funcionamento psicológico geral, com os 25 itens da versão de "
            "auto-avaliação do SDQ, que fornece as subescalas de sintomas emocionais, problemas "
            "de comportamento, hiperactividade e desatenção, problemas com os pares e "
            "comportamento pró-social [[goodman1997,goodman1998]];",
            "Secção VII, regulação emocional e auto-estima, com os 18 itens da DERS-SF, na versão "
            "portuguesa [[kaufman2016,moreira2022]], e os 10 itens da Escala de Auto-Estima de "
            "Rosenberg [[schmitt2005]];",
            "Secção VIII, sintomas de stress pós-traumático, com uma pergunta de filtro, de "
            "resposta fechada, sobre acontecimentos potencialmente traumáticos, e os 8 itens da "
            "CRIES-8, que avaliam a intrusão e o evitamento [[perrin2005]];",
            "Secção IX, comportamento agressivo, com os 12 itens do BPAQ-SF [[bryant2001]], na "
            "versão portuguesa [[pechorro2016]], e os 23 itens do RPQ, na versão portuguesa "
            "[[pechorro2015,pechorro2018]]."):
        e.marca(seccao)


def _instrumento_de_recolha(e):
    e.h2("7.7. Instrumento de recolha de dados")
    e.p("A recolha far-se-á por questionário estruturado de auto-preenchimento, confidencial e "
        "sem identificação nominal, aplicado em sala de aula sob supervisão da equipa de "
        "investigação. O instrumento não é construído de raiz: resulta da reunião de escalas "
        "psicológicas e de módulos de inquéritos previamente validados, o que preserva a "
        "comparabilidade dos resultados. Organiza-se em nove secções, apresentadas no Apêndice A.")
    _seccoes_do_questionario(e)
    e.p("A escolha das escalas psicológicas obedeceu a três critérios: medirem os mecanismos que a "
        "literatura associa ao comportamento agressivo, serem curtas e terem versão em língua "
        "portuguesa ou uso documentado em adolescentes africanos. As validações disponíveis "
        "têm, contudo, limites que o estudo assume. A versão portuguesa do BPAQ-SF foi validada "
        "em rapazes, sobretudo de contexto forense [[pechorro2016]], e a do RPQ em rapazes "
        "detidos e, depois, numa amostra escolar mista de 782 jovens portugueses, com estrutura "
        "de dois factores invariante entre sexos depois da exclusão do item 21 "
        "[[pechorro2015,pechorro2018]]; nenhuma das escalas foi estudada em adolescentes "
        "moçambicanos. A CRIES-8 foi preferida à versão com itens de hiperactivação porque esses "
        "itens incluem a irritabilidade, que ficaria dos dois lados do modelo. A versão de auto-avaliação do SDQ "
        "destina-se aos 11 a 17 anos, pelo que as bandas de rastreio serão calculadas só para "
        "essa faixa, e as pontuações dos alunos de 10, 18 e 19 anos entrarão apenas como "
        "variáveis contínuas. Como nenhuma das escalas tem ponto de corte validado para "
        "adolescentes moçambicanos, as bandas e os pontos de corte são indicadores de rastreio e "
        "nunca diagnóstico clínico individual [[hoosen2018]].")


def _adaptacao_e_validacao(e):
    e.h2("7.8. Adaptação transcultural e validação do instrumento")
    e.p("As escalas psicológicas serão aplicadas nas versões portuguesas validadas ou oficiais, "
        "sem alteração dos itens, e a adaptação transcultural limitar-se-á às instruções, aos "
        "exemplos, à apresentação das opções de resposta e a um glossário oral padronizado, "
        "elaborado por dois profissionais de psicologia falantes de Emakhuwa, que o aplicador "
        "usará quando um aluno pedir esclarecimento, cobrindo obrigatoriamente expressões como "
        "«vias de facto», «amargurado», «perder a cabeça», «irrequieto» e «batota», segundo as "
        "orientações internacionais para "
        "instrumentos de auto-relato [[beaton2000]]. As secções construídas para o estudo "
        "(Secções I a V) e as instruções serão apreciadas por um painel de cinco peritos, com "
        "pelo menos dois psicólogos clínicos, um deles falante de Emakhuwa, um profissional de "
        "saúde mental infanto-juvenil e um professor, com cálculo do índice de validade de "
        "conteúdo por item, exigindo-se o valor de 1,00 por o painel ter cinco peritos, e da "
        "média desse índice na escala, considerando-se aceitável 0,90 ou mais [[polit2006]].")
    e.p("Segue-se um pré-teste cognitivo com 10 a 15 adolescentes de uma escola não incluída no "
        "estudo, para verificar a compreensão dos itens, sobretudo os que descrevem emoções, e "
        "cronometrar o preenchimento. Se, no pré-teste, o percentil 75 do tempo de preenchimento "
        "exceder 45 minutos, o questionário será aplicado em duas sessões, em dias consecutivos e "
        "ligadas pelo mesmo código, com as Secções I a V na primeira e as Secções VI a IX na "
        "segunda. A avaliação psicométrica far-se-á na amostra principal: a consistência interna "
        "de cada escala será estimada pelo alfa de Cronbach e pelo ómega de McDonald, com "
        "intervalos de confiança a 95 por cento (IC95%), "
        "tomando 0,70 como referência indicativa e interpretando o valor com cautela, porque um "
        "alfa elevado não demonstra por si só a fiabilidade nem a unidimensionalidade da escala "
        "[[taber2018]]; a estrutura factorial do BPAQ-SF, do RPQ, do SDQ e da DERS-SF será "
        "examinada por análise factorial confirmatória, e a invariância do BPAQ-SF e do RPQ será "
        "testada por sexo e por grupo etário, dos 10 aos 14 e dos 15 aos 19 anos, antes de se "
        "compararem médias, no caso do RPQ com e sem o item 21 [[pechorro2018]]. A aplicação das "
        "escalas protegidas por direitos de "
        "autor será precedida de pedido formal de autorização aos respectivos autores.")


def _procedimentos(e):
    e.h2("7.9. Procedimentos de recolha de dados")
    e.p("Após a aprovação ética e as autorizações institucionais, a equipa apresentará o estudo à "
        "direcção da escola e aos directores de turma. Os termos de consentimento serão enviados "
        "aos encarregados de educação com pelo menos sete dias de antecedência, através dos "
        "directores de turma, e recolhidos antes da aplicação. No dia marcado, o questionário será "
        "aplicado em sala de aula, num período de cerca de 45 minutos, equivalente a um tempo "
        "lectivo, em ambiente que assegure a privacidade das respostas, com os alunos sentados de "
        "forma distanciada e sem a presença do professor da turma, de modo a reduzir o efeito de "
        "desejabilidade social. Nas classes iniciais, o aplicador lerá as instruções e os "
        "exemplos em voz alta. Cada questionário será identificado apenas por um código "
        "numérico. Os alunos ausentes serão convidados numa segunda visita à turma, e a ausência "
        "nas duas visitas será registada como não resposta. As medidas de apoio aos "
        "participantes estão descritas em 7.11.")


def _gestao_e_descricao(e):
    e.h2("7.10. Gestão e análise dos dados")
    e.p("Os questionários serão codificados e introduzidos em dupla entrada numa base de dados, "
        "com verificação de consistência e de valores fora de intervalo antes do encerramento da "
        "base. A análise será conduzida no programa Statistical Package for the Social Sciences "
        "(SPSS) ou, em alternativa, num programa de acesso livre equivalente, como o R ou o "
        "jamovi. Um questionário será considerado inválido se tiver mais de 10 por cento dos itens "
        "sem resposta, sem contar os que foram saltados por instrução de filtro.")
    e.p("As escalas serão cotadas segundo os respectivos manuais, com inversão prévia da cotação "
        "dos itens assinalados como invertidos em cada manual; a pontuação total da DERS-SF será calculada sem os "
        "itens de consciência emocional, como recomendado na validação portuguesa "
        "[[moreira2022]]. Aos participantes que respondam não ter vivido um acontecimento "
        "potencialmente traumático será atribuída a pontuação 0 na CRIES-8, que não será tratada "
        "como omissa, e a exposição a esse acontecimento entrará nos modelos como variável "
        "própria. A análise descritiva incluirá frequências absolutas e relativas e medidas de "
        "tendência central e de dispersão; estimar-se-ão a prevalência de envolvimento em "
        "violência interpessoal e de participação em lutas físicas e a proporção de adolescentes "
        "nas "
        "bandas de rastreio do SDQ, entre os 11 e os 17 anos, e com 17 ou mais pontos na "
        "CRIES-8, no total da amostra, com IC95%. Nas "
        "comparações bivariadas usar-se-ão regressões simples e o teste do qui-quadrado com a "
        "correcção de Rao e Scott, ambos ajustados ao desenho amostral, e a normalidade será "
        "avaliada nos resíduos dos modelos, por gráficos quantil-quantil.")


def _modelos_multivariaveis(e):
    e.p("A regressão linear múltipla, tendo como variável dependente a agressividade total, "
        "constitui a análise principal. As variáveis entram em blocos pré-especificados, pela "
        "ordem do esquema conceptual da Figura 1: primeiro a idade, o sexo e a classe; depois os "
        "factores do contexto familiar, escolar e comunitário; por fim, os factores psicológicos "
        "individuais. Cada bloco entra completo, independentemente dos resultados bivariados, e o "
        "aumento do coeficiente de determinação indicará quanto da variância é explicado pelos "
        "factores psicológicos para além dos do contexto. O modelo principal inclui as variáveis "
        "de exposição individuais; o número de experiências adversas é testado num modelo "
        "próprio, que o substitui aos seus componentes, e o índice de exposição à violência é "
        "usado apenas na análise de mediação, evitando a colinearidade entre as somas e os "
        "itens que as compõem. Os coeficientes dos factores de "
        "contexto serão lidos no segundo bloco como associação total, ajustada às variáveis "
        "sociodemográficas, e no modelo final como associação directa. Serão apresentados os "
        "coeficientes beta com IC95%, e a multicolinearidade será avaliada pelo factor de "
        "inflação da variância, adoptando-se o limiar de 5.")
    e.p("Para testar os correlatos específicos de cada forma de agressão, as duas pontuações "
        "do RPQ serão padronizadas, e o modelo da agressão reactiva incluirá a agressão proactiva "
        "como covariável, e vice-versa, porque as duas formas estão fortemente correlacionadas e "
        "as diferenças entre os seus correlatos só se tornam visíveis quando se controla a outra "
        "forma [[raine2006,card2006]]. A diferença entre os coeficientes parciais de cada factor "
        "psicológico nas duas formas será testada por um teste de Wald, com a covariância dos "
        "estimadores obtida por bootstrap ajustado ao desenho; se a agressão proactiva tiver "
        "distribuição muito assimétrica, a regressão binomial negativa será usada como análise de "
        "sensibilidade. A regressão logística binária, sobre a participação em lutas físicas, é a "
        "análise complementar, com as variáveis pré-especificadas seguintes: idade, sexo, classe, "
        "castigo físico em casa, violência entre adultos do agregado, vitimização por bullying, "
        "pares desviantes, consumo de álcool, dificuldades de regulação emocional, sintomas de "
        "stress pós-traumático, sintomas emocionais e hiperactividade e desatenção. Apresentará "
        "os odds ratio brutos (OR) e os aOR, com IC95%, e a qualidade de ajustamento pelo teste F "
        "ajustado de Archer e Lemeshow para amostras complexas.")


def _mediacao_e_desenho(e):
    e.p("A hipótese de mediação será examinada de forma exploratória, com o índice de exposição à "
        "violência como variável independente, as dificuldades de regulação emocional como "
        "mediadora e a agressão comportamental como variável dependente, ajustando para a idade, "
        "o sexo e a classe; a escolha da componente comportamental evita que a raiva esteja dos "
        "dois lados do modelo. O efeito indirecto será avaliado pelo teste de significância "
        "conjunta dos dois caminhos, com erros-padrão ajustados ao desenho, e o intervalo de "
        "confiança do produto será obtido pelo método de Monte Carlo [[fritz2007,hayes2022]]. "
        "Em análise de sensibilidade, a mediação será repetida com a DERS-SF sem os itens de "
        "impulsos e com a subescala proactiva do RPQ, que não contém itens de raiva. Por o "
        "desenho ser transversal, o resultado será "
        "lido como efeito indirecto em sentido estatístico, compatível com o mecanismo proposto, e "
        "não como prova da sequência causal.")
    e.p("Todas as estimativas terão em conta o desenho amostral, com a classe como estrato, a "
        "turma como unidade primária de amostragem e os pesos amostrais, através do módulo de "
        "amostras complexas do SPSS ou de pacotes equivalentes. Os testes usarão os graus de "
        "liberdade do desenho, iguais ao número de turmas menos o número de estratos, e, com menos "
        "de 20 turmas, erros-padrão com correcção para poucos conglomerados; os resultados "
        "inferenciais serão, nesse caso, interpretados com cautela. O efeito de desenho observado "
        "será apresentado e comparado com o valor assumido no cálculo da amostra. A pontuação de "
        "uma subescala com um único item por responder será calculada pela média dos restantes "
        "itens do próprio participante, e os valores omissos que restarem nos modelos serão "
        "tratados por imputação múltipla por equações encadeadas, com 20 conjuntos imputados. "
        "A primeira e a terceira hipóteses operacionais constituem as análises confirmatórias, "
        "com um nível de significância de 5 por cento (p<0,05) e correcção de Holm para as "
        "comparações múltiplas dentro de cada uma; a hipótese de mediação e as restantes "
        "associações são exploratórias. Os "
        "resultados serão apresentados em tabelas e gráficos, com decimais assinalados por "
        "vírgula.")


def _procedimentos_e_analise(e):
    _procedimentos(e)
    _gestao_e_descricao(e)
    _modelos_multivariaveis(e)
    _mediacao_e_desenho(e)


def _salvaguardas_eticas():
    return (
        "Aprovação institucional: o protocolo será submetido ao Comité Institucional de "
        "Bioética para a Saúde (CIBS) da Universidade Lúrio (UniLúrio) e, quando aplicável, ao "
        "Comité Nacional de Bioética para a Saúde (CNBS), iniciando-se a recolha apenas após "
        "parecer favorável e atribuição do respectivo número de referência.",
        "Autorizações locais: serão obtidas as autorizações do serviço distrital de educação da "
        "cidade de Nampula, da direcção da Escola Secundária de Muatala e da escola do "
        "pré-teste antes de qualquer contacto com os alunos.",
        "Consentimento e assentimento: nos participantes com menos de 18 anos, exige-se o termo "
        "de consentimento livre e esclarecido (TCLE) assinado pelo pai, pela mãe ou pelo "
        "responsável legal, acompanhado do assentimento do próprio adolescente; nos "
        "participantes com 18 ou mais anos, basta o consentimento próprio. A recusa do "
        "adolescente prevalece sempre sobre a autorização do responsável.",
        "Confidencialidade e protecção de dados: os questionários não têm identificação nominal "
        "e são identificados apenas por código; as folhas de consentimento serão guardadas em "
        "separado das respostas, em armário fechado, e os ficheiros electrónicos protegidos por "
        "palavra-passe, com acesso restrito à equipa. Não serão apresentados resultados de "
        "subgrupos com menos de 10 alunos.",
        "Gestão do risco emocional: o questionário aborda experiências de violência, "
        "acontecimentos traumáticos e emoções difíceis e pode suscitar desconforto; o "
        "participante pode não responder a qualquer pergunta e interromper a participação a "
        "qualquer momento, sem prejuízo. A secção sobre acontecimentos traumáticos tem uma "
        "pergunta de filtro de resposta fechada, que permite saltá-la sem descrever o "
        "acontecimento, e o questionário termina com uma mensagem de encerramento. Estará "
        "presente, em cada sessão, um membro da equipa com formação em primeiros socorros "
        "psicológicos, e o psicólogo clínico de referência estará presente ou contactável.",
        "Natureza de rastreio: as escalas psicológicas servem para caracterizar o grupo e não "
        "para diagnosticar; nenhum aluno será rotulado nem receberá um diagnóstico a partir das "
        "suas respostas, e os resultados individuais não serão comunicados à escola nem à "
        "família.",
        "Via de referenciação: como o questionário não identifica o aluno, as respostas não "
        "permitem saber quem relata violência ou sofrimento. Por isso, no fim da sessão, todos "
        "os alunos recebem uma folha com os contactos de apoio, incluindo a Linha Fala Criança, "
        "pelo número 116, e os Serviços Amigos dos Adolescentes e Jovens (SAAJ) mais próximos, e um talão "
        "destacável, sem ligação ao código do questionário, que quem desejar preenche com o "
        "nome e a turma e deposita numa urna separada, para ser contactado pelo psicólogo de "
        "referência nos cinco dias seguintes. Os adolescentes que peçam ajuda ou que manifestem "
        "sofrimento durante a sessão serão encaminhados, com o seu conhecimento, para o serviço "
        "de psicologia da unidade sanitária de referência ou para o SAAJ, que terá aceitado "
        "previamente, por escrito, receber estes encaminhamentos. A revelação espontânea de "
        "violência em curso seguirá os procedimentos previstos na Lei n.º 7/2008, de 9 de Julho, "
        "de Promoção e Protecção dos Direitos da Criança.",
        "Ausência de incentivos: não haverá qualquer pagamento ou benefício material pela "
        "participação, evitando-se influência indevida sobre a decisão do adolescente.",
        "Devolução dos resultados: os resultados agregados serão apresentados à escola e à "
        "comunidade educativa, sem qualquer identificação individual, acompanhados de uma "
        "sessão de psicoeducação sobre a gestão da raiva e sobre os sinais de sofrimento "
        "psicológico que justificam procurar ajuda.",
    )


def _etica_e_limitacoes(e):
    e.h2("7.11. Considerações éticas")
    e.p("A investigação observará os princípios consagrados na Declaração de Helsínquia da "
        "Associação Médica Mundial, na sua revisão de 2024 [[helsinquia2024]]. Por envolver "
        "menores de idade e abordar temas sensíveis, adoptam-se as salvaguardas seguintes.")
    for salvaguarda in _salvaguardas_eticas():
        e.marca(salvaguarda)

    e.h2("7.12. Limitações previstas")
    e.p("A primeira limitação decorre do desenho transversal, que não permite estabelecer a "
        "direcção temporal das associações; em particular, a análise de mediação é compatível "
        "com o mecanismo proposto mas não o demonstra, porque a agressividade também pode agravar "
        "as dificuldades emocionais e a exposição à violência. A segunda é o recurso exclusivo "
        "ao auto-relato para medir comportamentos socialmente censurados e estados emocionais, "
        "o que pode subestimar a agressividade por desejabilidade social e inflacionar as "
        "correlações por variância de método comum [[podsakoff2003]]; procura-se atenuá-la com a "
        "confidencialidade, a aplicação sem a presença do professor, a inclusão de itens "
        "invertidos e a separação das escalas no questionário.")
    e.p("A terceira limitação é o carácter de rastreio das medidas psicológicas: sem entrevista "
        "clínica não é possível estabelecer diagnósticos, os pontos de corte usados são "
        "britânicos, a versão de auto-avaliação do SDQ não cobre os alunos de 10, 18 e 19 anos e "
        "os itens do ACE-IQ foram adaptados aos últimos 12 meses. Alguns construtos da revisão "
        "da literatura só são medidos de forma indirecta ou não são medidos: a subescala "
        "pró-social do SDQ não equivale aos traços de insensibilidade emocional, que exigiriam o "
        "Inventário de Traços Calosos e Não Emocionais; a CRIES-8 avalia a intrusão e o "
        "evitamento, mas não a hiperactivação; a irritabilidade crónica não tem medida própria; e "
        "o enviesamento de atribuição hostil, apresentado na revisão como mecanismo central, não "
        "é medido, porque exigiria vinhetas de provocação ambígua [[decastro2002]]. "
        "A quarta é a restrição aos adolescentes escolarizados, que exclui os que abandonaram a "
        "escola e nos quais a prevalência do problema tende a ser superior. A quinta é a "
        "validação das escalas de agressividade em rapazes portugueses, sobretudo de contexto "
        "forense, e a ausência de validação em Moçambique, atenuadas pelo pré-teste cognitivo, "
        "pela análise factorial confirmatória e pelos testes de invariância na amostra. Uma "
        "segunda fase, com entrevista clínica semi-estruturada a uma subamostra de adolescentes "
        "que se auto-referenciem, poderá aprofundar a compreensão individual dos casos e fica "
        "recomendada para investigação futura.")


def escrever_metodologia(e, h, doc):
    """Seccao 7 completa, montada a partir dos blocos acima pela ordem do protocolo."""
    e.h1("7. METODOLOGIA")
    _desenho_local_e_populacao(e)
    _amostragem_e_criterios(e, h, doc)
    _criterios_de_elegibilidade(e)
    _variaveis_e_instrumento(e, h, doc)
    _instrumento_de_recolha(e)
    _adaptacao_e_validacao(e)
    _procedimentos_e_analise(e)
    _etica_e_limitacoes(e)


def escrever_resultados_esperados(e):
    e.h1("8. RESULTADOS ESPERADOS")
    e.p("Em coerência com os objectivos específicos, esperam-se os seguintes resultados.")
    for resultado in (
            "Um perfil sociodemográfico e escolar caracterizado dos adolescentes da Escola "
            "Secundária de Muatala, por idade, sexo, classe, situação familiar e percurso escolar.",
            "A estimativa do nível de comportamento agressivo e do seu perfil por dimensão, a "
            "distinção entre agressão reactiva e proactiva, a prevalência de envolvimento em "
            "violência interpessoal, comparável com a observada na África subsariana "
            "[[aboagye2021a]], e a proporção de adolescentes acima do ponto de corte de rastreio "
            "do SDQ para problemas de comportamento, a interpretar como indicador de rastreio e não "
            "como diagnóstico.",
            "O perfil psicológico dos adolescentes, com a distribuição das dificuldades de "
            "regulação emocional, da hiperactividade e desatenção, dos sintomas emocionais, dos "
            "sintomas de stress pós-traumático, da auto-estima e do comportamento pró-social, e a "
            "proporção de alunos acima dos pontos de corte de rastreio, dado com utilidade directa "
            "para o planeamento de serviços de psicologia clínica.",
            "A descrição da frequência dos factores familiares, escolares, do grupo de pares e "
            "comunitários, esperando-se encontrar proporções relevantes de castigo físico, de "
            "exposição a violência entre adultos do agregado e de vitimização por bullying, em "
            "linha com os dados nacionais [[vacs2019]].",
            "A identificação dos factores psicológicos e psicossociais que se mantêm "
            "independentemente associados ao comportamento agressivo após ajustamento mútuo, com "
            "estimativas e intervalos de confiança, a diferenciação dos correlatos específicos da "
            "agressão reactiva e da proactiva e a estimativa, em sentido estatístico, do efeito "
            "indirecto da exposição à violência através das dificuldades de regulação emocional, "
            "testando as hipóteses formuladas.",
            "Um conjunto de recomendações clínicas e preventivas para a escola, para os serviços "
            "de saúde e de acção social e para as famílias, que indique os alvos psicológicos "
            "prioritários de avaliação, de encaminhamento e de intervenção, e um contributo "
            "metodológico sobre o desempenho psicométrico dos instrumentos usados em "
            "adolescentes moçambicanos."):
        e.marca(resultado)


def escrever_divulgacao(e):
    e.h1("9. DIVULGAÇÃO DOS RESULTADOS")
    e.p("O trabalho será apresentado e defendido publicamente perante um júri da Faculdade de "
        "Ciências de Saúde (FCS) da Universidade Lúrio, como requisito para a obtenção do grau de "
        "licenciada em Psicologia. Os resultados agregados serão depois apresentados numa sessão "
        "de devolução na Escola Secundária de Muatala, dirigida à direcção, aos professores, aos "
        "alunos e aos encarregados de educação, com discussão das recomendações. Será ainda "
        "entregue um relatório executivo ao serviço distrital de educação, aos serviços de saúde "
        "mental e aos SAAJ da cidade de Nampula, com as "
        "implicações clínicas dos resultados para a detecção e o encaminhamento, e procurar-se-á "
        "a publicação dos principais achados numa revista científica com revisão por pares, na "
        "área da psicologia clínica ou da saúde mental, e a sua apresentação em jornadas "
        "científicas nacionais.")


def escrever_cronograma_orcamento(e, h, doc):
    e.h1("10. CRONOGRAMA DE ACTIVIDADES")
    e.p("O cronograma foi construído de modo a que nenhuma actividade com participantes, do "
        "pré-teste à recolha de dados, comece antes da aprovação ética, e a que a recolha "
        "decorra no segundo semestre de 2026, antes das avaliações finais do ano lectivo. O plano "
        "de contingência para um parecer tardio está descrito em 7.2.")
    h.tabela(doc, "Quadro 3: Cronograma de actividades, de Julho de 2026 a Março de 2027.",
             CRONOGRAMA_COLUNAS, CRONOGRAMA, "Fonte: a autora, 2026.", tamanho=Pt(10),
             larguras=[Cm(4.6)] + [Cm(1.6)] * 7)

    e.h1("11. ORÇAMENTO")
    e.p("O orçamento estimado cobre a totalidade das despesas previstas, desde a impressão dos "
        "instrumentos até à devolução dos resultados à escola. Os valores estão expressos em "
        "meticais e serão suportados pela investigadora, salvo apoio institucional que venha a "
        "ser concedido.")
    h.tabela(doc, "Quadro 4: Orçamento estimado do estudo.",
             ["Rubrica", "Quantidade", "Custo unitário (MZN)", "Custo total (MZN)"],
             ORCAMENTO, "Fonte: a autora, 2026. MZN: metical moçambicano.",
             larguras=[Cm(7.0), Cm(3.0), Cm(3.0), Cm(3.0)])

    e.h1("12. RECURSOS HUMANOS")
    h.tabela(doc, "Quadro 5: Recursos humanos afectos ao estudo.",
             ["Interveniente", "Categoria", "Função"], RECURSOS_HUMANOS,
             "Fonte: a autora, 2026.", larguras=[Cm(4.4), Cm(5.6), Cm(6.0)])
