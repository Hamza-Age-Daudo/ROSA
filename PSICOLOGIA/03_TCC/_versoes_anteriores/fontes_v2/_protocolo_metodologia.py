"""Seccoes 7 a 12 do protocolo: metodologia, resultados esperados, divulgacao,
cronograma, orcamento e recursos humanos."""
from docx.shared import Cm, Pt

from _protocolo_amostra import (EXPOSICAO_TIPICA, POPULACAO_EXEMPLO, PREDITORES_LINEAR,
                                PREVALENCIA_AGRESSIVIDADE_ELEVADA, amostra_base,
                                amostra_efectiva, amostra_para, cenarios_amostra,
                                eventos_esperados,
                                f2_minimo_detectavel, n0_exacto, or_minimo_detectavel,
                                parametros_maximos_logistica)


def _decimal(valor, casas):
    """Numero com virgula decimal, como exige a casa."""
    return f"{valor:.{casas}f}".replace(".", ",")


def _milhares(valor):
    return f"{valor:,}".replace(",", ".")


VARIAVEIS = [
    ["Idade", "Independente", "Quantitativa discreta", "Anos completos; 10-14 e 15-19"],
    ["Sexo", "Independente", "Qualitativa nominal", "Masculino; feminino"],
    ["Classe frequentada", "Independente", "Qualitativa ordinal", "8.ª a 12.ª classe"],
    ["Repetência escolar", "Independente", "Qualitativa nominal", "Sim; não"],
    ["Absentismo escolar", "Independente", "Qualitativa nominal",
     "Faltou sem justificação em um ou mais dias nos últimos 30 dias: sim; não"],
    ["Com quem vive", "Independente", "Qualitativa nominal",
     "Ambos os progenitores; um progenitor; outros familiares; outra situação"],
    ["Funcionamento familiar", "Independente", "Qualitativa ordinal",
     "APGAR familiar: funcional, 7 a 10 pontos; disfunção moderada, 4 a 6; disfunção grave, 0 a 3"],
    ["Supervisão parental", "Independente", "Qualitativa ordinal",
     "Itens do GSHS: elevada; intermédia; baixa"],
    ["Castigo físico em casa", "Independente", "Qualitativa nominal",
     "Item do ACE-IQ nos últimos 12 meses: sim; não"],
    ["Violência entre progenitores", "Independente", "Qualitativa nominal",
     "Testemunhou agressão entre adultos do agregado: sim; não"],
    ["Vitimização por bullying", "Independente", "Qualitativa nominal",
     "Item do GSHS nos últimos 30 dias: sim; não"],
    ["Ligação à escola", "Independente", "Qualitativa ordinal", "Pontuação em tercis: baixa; "
     "média; elevada"],
    ["Pares desviantes", "Independente", "Qualitativa ordinal",
     "Número de amigos próximos com comportamentos desviantes: nenhum; um; dois ou mais"],
    ["Consumo de álcool", "Independente", "Qualitativa nominal",
     "Consumo em pelo menos um dia nos últimos 30 dias: sim; não"],
    ["Consumo de tabaco ou de outras drogas", "Independente", "Qualitativa nominal", "Sim; não"],
    ["Exposição a violência comunitária", "Independente", "Qualitativa nominal",
     "Presenciou agressão no bairro nos últimos 12 meses: sim; não"],
    ["Exposição a conteúdos violentos", "Independente", "Qualitativa ordinal",
     "Horas diárias de exposição: menos de uma; uma a três; mais de três"],
    ["Sintomas emocionais", "Independente", "Qualitativa ordinal",
     "Subescala emocional do SDQ: normal; limítrofe; anormal"],
    ["Envolvimento em violência interpessoal", "Dependente", "Qualitativa nominal",
     "Indicador do GSHS: luta física ou agressão física sofrida nos últimos 12 meses: sim; não"],
    ["Comportamento agressivo total", "Dependente", "Quantitativa contínua",
     "Pontuação total do BPAQ-SF, de 12 a 60 pontos"],
    ["Dimensões da agressividade", "Dependente", "Quantitativa contínua",
     "Pontuações de agressão física, agressão verbal, ira e hostilidade"],
    ["Agressividade elevada", "Dependente", "Qualitativa nominal",
     "Pontuação total igual ou superior ao percentil 75 da amostra: sim; não"],
    ["Agressão reactiva e proactiva", "Dependente", "Quantitativa contínua",
     "Pontuações das duas subescalas do RPQ"],
]

CRONOGRAMA = [
    ["Revisão da literatura e elaboração do protocolo", "X", "X", "", "", "", "", ""],
    ["Submissão e aprovação pelo comité de bioética", "", "X", "X", "", "", "", ""],
    ["Autorizações da direcção distrital e da escola", "", "", "X", "", "", "", ""],
    ["Adaptação transcultural do instrumento e painel de peritos", "", "X", "X", "", "", "", ""],
    ["Pré-teste e estudo-piloto", "", "", "X", "", "", "", ""],
    ["Recolha de dados na escola", "", "", "X", "X", "", "", ""],
    ["Introdução, limpeza e validação da base de dados", "", "", "", "X", "X", "", ""],
    ["Análise estatística", "", "", "", "", "X", "X", ""],
    ["Redacção do relatório final", "", "", "", "", "", "X", ""],
    ["Entrega, defesa e devolução dos resultados à escola", "", "", "", "", "", "", "X"],
]

CRONOGRAMA_COLUNAS = ["Actividade", "Jul-Ago 2026", "Set 2026", "Out 2026", "Nov 2026",
                      "Dez 2026", "Jan-Fev 2027", "Mar 2027"]

ORCAMENTO = [
    ["Impressão de questionários e de termos de consentimento", "1.200 exemplares", "15", "18.000"],
    ["Material de escritório e de codificação", "1 conjunto", "4.000", "4.000"],
    ["Transporte da equipa para a escola", "25 deslocações", "400", "10.000"],
    ["Comunicação, telefone e Internet", "5 meses", "1.500", "7.500"],
    ["Alimentação da equipa no terreno", "20 dias", "400", "8.000"],
    ["Honorários de assistentes de recolha de dados", "3 pessoas", "9.000", "27.000"],
    ["Formação e pré-teste", "1 sessão", "5.000", "5.000"],
    ["Sessão de devolução dos resultados à escola", "1 sessão", "6.000", "6.000"],
    ["Impressão e encadernação do relatório final", "8 exemplares", "1.200", "9.600"],
    ["Imprevistos, 10 por cento", "", "", "9.510"],
    ["Total geral", "", "", "104.610"],
]

RECURSOS_HUMANOS = [
    ["(nome do estudante)", "Estudante finalista de Psicologia", "Investigador principal"],
    ["(nome do orientador)", "Docente da Faculdade de Ciências de Saúde", "Orientação científica"],
    ["Assistentes de recolha", "Estudantes de Psicologia ou de Ciências de Saúde",
     "Aplicação dos questionários e controlo de qualidade"],
    ["Psicólogo de referência", "Profissional da unidade sanitária ou do serviço distrital",
     "Acolhimento e encaminhamento dos casos identificados"],
    ["Direcção da escola", "Direcção da Escola Secundária de Muatala",
     "Autorização, articulação logística e devolução dos resultados"],
]


def _desenho_local_e_populacao(e):
    e.h2("7.1. Tipo e desenho do estudo")
    e.p("Trata-se de um estudo de corte transversal, analítico, de abordagem quantitativa. O "
        "desenho transversal é adequado porque permite estimar, num único momento, o nível de "
        "comportamento agressivo e a frequência dos factores psicossociais, e testar as "
        "associações previstas nas hipóteses, sem exigir o seguimento dos participantes "
        "[[charan2013]]. Reconhece-se, como limitação inerente ao desenho, a impossibilidade de "
        "estabelecer a ordem temporal entre exposição e desfecho, pelo que os resultados serão "
        "interpretados como associações e não como relações de causa e efeito. O estudo será "
        "desenhado e reportado segundo a lista de verificação Strengthening the Reporting of "
        "Observational Studies in Epidemiology (STROBE), aplicável a estudos observacionais "
        "[[strobe2007]].")

    e.h2("7.2. Local e período do estudo")
    e.p("O estudo será realizado na Escola Secundária de Muatala, situada no bairro de Muatala, "
        "cidade de Nampula, província de Nampula, no norte de Moçambique. Trata-se de um "
        "estabelecimento público de ensino secundário, inserido num bairro periurbano de elevada "
        "densidade populacional, com predomínio da língua Emakhuwa e rendimento familiar "
        "maioritariamente proveniente do comércio informal e da agricultura. A recolha de dados "
        "decorrerá no segundo semestre do ano lectivo de 2026, entre Outubro e Novembro, depois "
        "da aprovação ética, nas semanas lectivas anteriores às provas finais e em datas a "
        "acordar com a direcção da escola, de modo a não perturbar a avaliação dos alunos.")

    e.h2("7.3. População do estudo")
    e.p("A população-alvo é constituída por todos os adolescentes dos 10 aos 19 anos de idade "
        "regularmente matriculados e em frequência efectiva na Escola Secundária de Muatala no "
        "segundo semestre de 2026, em ambos os turnos e em todas as classes leccionadas. O número "
        "exacto de alunos elegíveis, desagregado por classe, turma e turno, será obtido junto da "
        "direcção da escola no momento da aprovação do estudo e constituirá o enquadramento "
        "amostral.")



def _amostragem_e_criterios(e, h, doc):
    e.h2("7.4. Amostragem e cálculo do tamanho da amostra")
    e.p("A amostra será seleccionada por amostragem probabilística estratificada por classe, com "
        "selecção aleatória simples de turmas dentro de cada classe e inclusão de todos os alunos "
        "elegíveis das turmas sorteadas. A afectação às classes será proporcional ao número de "
        "alunos matriculados. A opção por amostragem probabilística, em substituição da amostragem "
        "por conveniência, é decisiva para a representatividade, para a validade externa dos "
        "resultados e para a legitimidade dos testes de associação previstos.")
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
    e.p(f"valor arredondado para {n0} participantes. Por se tratar de amostragem por "
        f"conglomerados, aplica-se um efeito de desenho (deff) de 1,5, que eleva o valor para "
        f"{n_deff} participantes. Este resultado é depois corrigido para a população finita da "
        f"escola, com N alunos elegíveis, e acrescido de 10 por cento para compensar recusas e "
        f"questionários incompletos:")
    h.formula(doc, [("n", None), ("c", "sub"), (f" = {n_deff} / [1 + ({n_deff} - 1) / N]", None),
                    ("        n", None), ("f", "sub"), (" = n", None), ("c", "sub"),
                    (" / 0,90", None)])
    h.tabela(doc, "Tabela 1: Tamanho da amostra segundo o número de alunos elegíveis na escola.",
             ["Alunos elegíveis (N)", "Amostra corrigida para população finita",
              "Amostra final, com 10% para não resposta"],
             cenarios_amostra(),
             "Fonte: o autor, 2026. Cálculo com Z=1,96; p=0,537; d=0,05; efeito de desenho de 1,5.",
             larguras=[Cm(4.0), Cm(6.0), Cm(6.0)])
    _corrigida, final_exemplo = amostra_para(POPULACAO_EXEMPLO)
    e.p("O cenário definitivo será fixado assim que a direcção da escola confirmar o número de "
        f"alunos elegíveis. A título indicativo, para uma população de "
        f"{_milhares(POPULACAO_EXEMPLO)} alunos, o estudo necessitará de {final_exemplo} "
        f"participantes.")
    _poder_para_o_objectivo_analitico(e)


def _poder_para_o_objectivo_analitico(e):
    """Verifica se a amostra descritiva chega para os modelos de regressao."""
    respondentes, efectiva = amostra_efectiva(POPULACAO_EXEMPLO)
    f2 = f2_minimo_detectavel(efectiva)
    razao = or_minimo_detectavel(efectiva)
    eventos = eventos_esperados(respondentes)
    e.p("O cálculo anterior dimensiona a estimativa descritiva. Para o objectivo analítico, "
        "verificou-se se a mesma amostra tem poder suficiente para os modelos de regressão, com "
        "um nível de significância de 5 por cento e um poder de 80 por cento [[faul2009]]. No "
        f"cenário de {_milhares(POPULACAO_EXEMPLO)} alunos esperam-se {respondentes} "
        "questionários válidos, que, divididos pelo efeito de desenho, equivalem a cerca de "
        f"{round(efectiva)} participantes seleccionados por amostragem aleatória simples. Com "
        f"este tamanho efectivo, a regressão linear múltipla, com até {PREDITORES_LINEAR} "
        "variáveis independentes, detecta o efeito isolado de uma variável a partir de um "
        f"tamanho de efeito de Cohen de {_decimal(f2, 3)}, o que corresponde a cerca de "
        f"{_decimal(100 * f2 / (1 + f2), 1)} por cento de variância explicada, um efeito "
        f"pequeno. Na regressão logística, uma exposição presente em "
        f"{round(100 * EXPOSICAO_TIPICA)} por cento dos adolescentes só é detectada com o mesmo "
        f"poder a partir de um odds ratio de {_decimal(razao, 2)}, valor da ordem do observado "
        "para a vitimização por bullying na África subsariana, mas acima do descrito para o "
        "consumo de álcool e para o absentismo [[aboagye2021a]]. Por esta razão, a regressão "
        "linear sobre a pontuação contínua constitui a análise principal e a regressão logística "
        "a análise complementar.")
    e.p("No modelo logístico, a agressividade elevada abrange, por definição, cerca de "
        f"{round(100 * PREVALENCIA_AGRESSIVIDADE_ELEVADA)} por cento dos participantes, o que "
        f"corresponde a {eventos} eventos esperados. Seguindo a regra de pelo menos dez eventos "
        f"por parâmetro estimado, o modelo não incluirá mais de "
        f"{parametros_maximos_logistica(respondentes)} parâmetros, contando cada categoria das "
        "variáveis qualitativas [[peduzzi1996]].")



def _criterios_de_elegibilidade(e):
    e.h2("7.5. Critérios de inclusão e de exclusão")
    e.h3("7.5.1. Critérios de inclusão")
    for criterio in (
            "Idade compreendida entre os 10 e os 19 anos completos à data da recolha;",
            "Matrícula e frequência efectiva na Escola Secundária de Muatala no segundo semestre "
            "de 2026;",
            "Assentimento do adolescente e, nos menores de 18 anos, consentimento livre e "
            "esclarecido do pai, da mãe ou do responsável legal;",
            "Estar presente na sala no dia da aplicação do questionário."):
        e.marca(criterio)
    e.h3("7.5.2. Critérios de exclusão")
    for criterio in (
            "Dificuldade de compreensão das perguntas que impeça o preenchimento autónomo, mesmo "
            "com apoio do aplicador;",
            "Recusa em participar, manifestada pelo adolescente ou pelo responsável legal;",
            "Questionário devolvido com mais de 10 por cento dos itens por responder ou com "
            "padrão de resposta manifestamente inconsistente;",
            "Estudante em situação de crise emocional aguda no momento da recolha, caso em que "
            "será encaminhado e não inquirido."):
        e.marca(criterio)



def _variaveis_e_instrumento(e, h, doc):
    e.h2("7.6. Variáveis do estudo e definições operacionais")
    e.p("A variável dependente é o comportamento agressivo, tratado como variável contínua, "
        "através da pontuação total e das pontuações por dimensão, e como variável dicotómica, "
        "distinguindo os adolescentes com agressividade elevada, definidos pela pontuação igual ou "
        "superior ao percentil 75 da amostra. Este critério é relativo e serve apenas a análise "
        "complementar, porque as escalas não dispõem de ponto de corte validado para adolescentes "
        "moçambicanos. Regista-se ainda o envolvimento em violência interpessoal, indicador "
        "comportamental que permite comparar a escola com os dados da África subsariana. As "
        "variáveis independentes são os factores psicossociais dos quatro níveis do modelo "
        "ecológico. O quadro seguinte apresenta a definição operacional de cada variável.")
    h.tabela(doc, "Quadro 2: Definição operacional das variáveis do estudo.",
             ["Variável", "Tipo", "Natureza e escala", "Categorias ou medição"],
             VARIAVEIS, "Fonte: o autor, 2026.",
             larguras=[Cm(4.2), Cm(2.4), Cm(3.0), Cm(6.4)])



def _instrumento_e_validacao(e):
    e.h2("7.7. Instrumento de recolha de dados")
    e.p("A recolha far-se-á por questionário estruturado de auto-preenchimento, anónimo, aplicado "
        "em sala de aula sob supervisão da equipa de investigação. O instrumento não é construído "
        "de raiz: resulta da reunião de módulos de escalas previamente validadas, o que preserva a "
        "comparabilidade dos resultados e dispensa a validação integral de um questionário novo. O "
        "questionário organiza-se em sete secções, apresentadas no Apêndice A.")
    for seccao in (
            "Secção I, dados sociodemográficos e escolares, construída para este estudo a partir "
            "das variáveis do quadro 2;",
            "Secção II, contexto familiar, com o APGAR familiar de cinco itens para o "
            "funcionamento familiar [[smilkstein1978]] e itens de supervisão e ligação parental do "
            "inquérito global de saúde escolar [[gshs]];",
            "Secção III, exposição à violência, com itens do questionário internacional de "
            "experiências adversas na infância da OMS, relativos ao castigo físico em casa e na "
            "escola, à violência testemunhada em casa e à violência presenciada na comunidade "
            "[[aceiq]];",
            "Secção IV, contexto escolar e grupo de pares, com itens de vitimização por bullying, "
            "de envolvimento em lutas físicas e de agressão física sofrida, que formam o indicador "
            "de violência interpessoal, e itens de ligação à escola e de afiliação a pares "
            "desviantes [[gshs]];",
            "Secção V, consumo de substâncias psicoactivas, com itens de álcool, tabaco e outras "
            "drogas do inquérito global de saúde escolar [[gshs]];",
            "Secção VI, sintomas emocionais, com a subescala de cinco itens do Questionário de "
            "Capacidades e de Dificuldades [[goodman1997]];",
            "Secção VII, comportamento agressivo, com a forma reduzida de doze itens do "
            "Questionário de Agressividade de Buss e Perry, na versão portuguesa validada, e com o "
            "Questionário de Agressão Reactiva e Proactiva, de vinte e três itens, igualmente com "
            "versão portuguesa validada [[pechorro2016,pechorro2015]]."):
        e.marca(seccao)

    e.h2("7.8. Adaptação transcultural e validação do instrumento")
    e.p("O conjunto será submetido a adaptação transcultural em quatro etapas. Primeiro, a "
        "adequação linguística para português simplificado, acessível a adolescentes com "
        "escolaridade secundária inicial e falantes de Emakhuwa como primeira língua, com "
        "retroversão de controlo. Segundo, a apreciação por um painel de cinco peritos em "
        "psicologia, saúde mental e educação, com cálculo do índice de validade de conteúdo, "
        "considerando-se aceitáveis valores iguais ou superiores a 0,80. Terceiro, um pré-teste "
        "cognitivo com dez a quinze adolescentes de uma escola não incluída no estudo, para "
        "verificar a compreensão dos itens e cronometrar o tempo de preenchimento. Quarto, um "
        "estudo-piloto com cerca de trinta participantes, para estimar a consistência interna pelo "
        "coeficiente alfa de Cronbach, considerando-se aceitáveis valores iguais ou superiores a "
        "0,70 [[tuvblad2016]]. A aplicação das escalas protegidas por direitos de autor será "
        "precedida de pedido formal de autorização aos respectivos autores.")



def _procedimentos_e_analise(e):
    e.h2("7.9. Procedimentos de recolha de dados")
    e.p("Após a aprovação ética e as autorizações institucionais, a equipa apresentará o estudo à "
        "direcção da escola e aos directores de turma. Os termos de consentimento serão enviados "
        "aos encarregados de educação com pelo menos sete dias de antecedência, através dos "
        "directores de turma, e recolhidos antes da aplicação. No dia marcado, o questionário será "
        "aplicado em sala de aula, num período de cerca de trinta minutos, em ambiente que "
        "assegure a privacidade das respostas, com os alunos sentados de forma distanciada e sem a "
        "presença do professor da turma, de modo a reduzir o efeito de desejabilidade social. Cada "
        "questionário será identificado apenas por um código numérico. Os alunos ausentes no dia "
        "da aplicação serão contactados numa segunda visita à mesma turma, e a terceira ausência "
        "será registada como não resposta. No final, todos os participantes receberão uma folha "
        "com informação sobre onde procurar apoio psicológico.")

    e.h2("7.10. Gestão e análise dos dados")
    e.p("Os questionários serão codificados e introduzidos em dupla entrada numa base de dados, "
        "com verificação de consistência e de valores fora de intervalo antes do encerramento da "
        "base. A análise será conduzida no programa Statistical Package for the Social Sciences "
        "(SPSS), ou em alternativa de acesso livre equivalente, como o R ou o Jamovi.")
    e.p("A análise descritiva incluirá frequências absolutas e relativas, para as variáveis "
        "qualitativas, e medidas de tendência central e de dispersão, para as quantitativas, "
        "verificando-se a normalidade das distribuições pelo teste de Kolmogorov-Smirnov e pela "
        "inspecção gráfica. A consistência interna de cada escala será reportada pelo coeficiente "
        "alfa de Cronbach.")
    e.p("Na análise inferencial, a comparação das pontuações médias de agressividade entre grupos "
        "recorrerá ao teste t de Student e à análise de variância, ou aos testes de Mann-Whitney e "
        "de Kruskal-Wallis quando os pressupostos não se verificarem. A relação entre variáveis "
        "quantitativas será examinada pelos coeficientes de correlação de Pearson ou de Spearman. "
        "A associação entre os factores psicossociais e a classificação de agressividade elevada "
        "será avaliada pelo teste do qui-quadrado de Pearson, ou pelo teste exacto de Fisher "
        "quando aplicável.")
    e.p("Seguir-se-á a modelação multivariável. A regressão linear múltipla, tendo como variável "
        "dependente a pontuação total de agressividade, constitui a análise principal, e a "
        "regressão logística binária, tendo como variável dependente a agressividade elevada, a "
        "análise complementar. A selecção das variáveis segue o esquema conceptual da Figura 1: "
        "entram a idade e o sexo, mantidos por decisão a priori, e os factores com p inferior a "
        "0,20 na análise bivariada, respeitando no modelo logístico o limite de parâmetros "
        "fixado no cálculo da amostra. Serão reportados os coeficientes beta com "
        "intervalos de confiança a 95 por cento (IC95%), no modelo linear, e os odds ratio "
        "brutos (OR) e ajustados (aOR), com IC95%, no modelo logístico. A multicolinearidade será "
        "avaliada pelo factor de inflação da variância, adoptando-se o limiar de 5, e a qualidade "
        "de ajustamento do modelo logístico pelo teste de Hosmer e Lemeshow. O nível de "
        "significância adoptado é de 5 por cento (p<0,05). Os resultados serão apresentados em "
        "tabelas e gráficos, com decimais assinalados por vírgula.")
    e.p("Todas as estimativas terão em conta o desenho amostral, com a classe como estrato e a "
        "turma como unidade primária de amostragem, através do módulo de amostras complexas do "
        "SPSS ou, em alternativa, de erros-padrão robustos agrupados por turma, o que exige o "
        "registo do código da turma em cada questionário. O efeito de desenho observado será "
        "reportado e comparado com o valor de 1,5 assumido no cálculo da amostra. Quanto aos "
        "dados omissos, a pontuação de uma subescala com um único item por responder será "
        "calculada pela média dos restantes itens do próprio participante; com mais itens "
        "omissos, a subescala será tratada como omissa.")



def _etica_e_limitacoes(e):
    e.h2("7.11. Considerações éticas")
    e.p("A investigação observará os princípios consagrados na Declaração de Helsínquia da "
        "Associação Médica Mundial, na sua revisão de 2024 [[helsinquia2024]]. Por envolver "
        "menores de idade e abordar temas sensíveis, adoptam-se as salvaguardas seguintes.")
    for salvaguarda in (
            "Aprovação institucional: o protocolo será submetido ao Comité Institucional de "
            "Bioética para a Saúde (CIBS) da Universidade Lúrio (UniLúrio) e, quando aplicável, "
            "ao Comité Nacional de Bioética para a Saúde (CNBS), iniciando-se a recolha apenas após parecer favorável e "
            "atribuição do respectivo número de referência.",
            "Autorizações locais: serão obtidas as autorizações dos Serviços Distritais de "
            "Educação, Juventude e Tecnologia e da direcção da Escola Secundária de Muatala antes "
            "de qualquer contacto com os alunos.",
            "Consentimento e assentimento: nos participantes com menos de 18 anos, exige-se o "
            "termo de consentimento livre e esclarecido (TCLE) assinado pelo pai, pela mãe ou pelo "
            "responsável legal, acompanhado do assentimento do próprio adolescente; nos participantes com 18 ou mais "
            "anos, basta o consentimento próprio. A recusa do adolescente prevalece sempre sobre a "
            "autorização do responsável.",
            "Confidencialidade e protecção de dados: os questionários são anónimos e identificados "
            "apenas por código; as folhas de consentimento serão guardadas em separado das "
            "respostas, em armário fechado, e os ficheiros electrónicos protegidos por palavra-passe, "
            "com acesso restrito à equipa de investigação.",
            "Gestão do risco emocional: o questionário aborda experiências de violência e pode "
            "suscitar desconforto; o participante pode não responder a qualquer pergunta e "
            "interromper a participação a qualquer momento, sem prejuízo. Estará presente, em cada "
            "sessão, um membro da equipa com formação em primeiros socorros psicológicos.",
            "Via de referenciação: como o questionário é anónimo, as respostas não permitem "
            "identificar quem relata violência; por isso, todos os participantes recebem uma "
            "folha com os contactos de apoio psicológico e de protecção da criança. Os "
            "adolescentes que peçam ajuda, que manifestem sofrimento durante a sessão ou que "
            "revelem espontaneamente situações de violência em curso serão encaminhados, com o "
            "seu conhecimento, para o serviço de psicologia da unidade sanitária de referência e, "
            "quando a lei o exija, para os mecanismos de protecção da criança, procedimento que "
            "consta expressamente da folha de informação.",
            "Ausência de incentivos: não haverá qualquer pagamento ou benefício material pela "
            "participação, evitando-se influência indevida sobre a decisão do adolescente.",
            "Devolução dos resultados: os resultados agregados serão apresentados à escola e à "
            "comunidade educativa, sem qualquer identificação individual."):
        e.marca(salvaguarda)

    e.h2("7.12. Limitações previstas")
    e.p("Antecipam-se quatro limitações. A primeira decorre do desenho transversal, que não "
        "permite estabelecer a direcção temporal das associações. A segunda é o recurso ao "
        "auto-relato para medir comportamentos socialmente censurados, o que pode subestimar a "
        "agressividade por desejabilidade social; procura-se atenuá-la com o anonimato, a "
        "aplicação sem a presença do professor e a inclusão de itens invertidos. A terceira é a "
        "restrição da amostra aos adolescentes escolarizados, que exclui os que abandonaram a "
        "escola e nos quais a prevalência do problema tende a ser superior, limitando a "
        "generalização dos resultados. A quarta é a possibilidade de erro de medida associado à "
        "adaptação transcultural dos instrumentos, atenuada pelo painel de peritos, pelo pré-teste "
        "cognitivo e pela verificação da consistência interna no estudo-piloto.")


def escrever_metodologia(e, h, doc):
    """Seccao 7 completa, montada a partir dos blocos acima pela ordem do protocolo."""
    e.h1("7. METODOLOGIA")
    _desenho_local_e_populacao(e)
    _amostragem_e_criterios(e, h, doc)
    _criterios_de_elegibilidade(e)
    _variaveis_e_instrumento(e, h, doc)
    _instrumento_e_validacao(e)
    _procedimentos_e_analise(e)
    _etica_e_limitacoes(e)


def escrever_resultados_esperados(e):
    e.h1("8. RESULTADOS ESPERADOS")
    e.p("Em coerência com os objectivos específicos, esperam-se os seguintes resultados.")
    for resultado in (
            "Um perfil sociodemográfico e escolar caracterizado dos adolescentes da Escola "
            "Secundária de Muatala, por idade, sexo, classe, situação familiar e percurso escolar.",
            "A estimativa do nível de comportamento agressivo e do seu perfil por dimensão, a "
            "distinção entre agressão reactiva e proactiva e a prevalência de envolvimento em "
            "violência interpessoal, comparável com a observada na África subsariana "
            "[[aboagye2021a]].",
            "A descrição da frequência dos factores familiares em estudo, esperando-se encontrar "
            "proporções relevantes de castigo físico em casa e de exposição a violência entre "
            "adultos do agregado, em linha com os dados nacionais [[vacs2019]].",
            "A descrição dos factores escolares, do grupo de pares e comunitários, incluindo a "
            "prevalência de vitimização por bullying, de afiliação a pares desviantes e de consumo "
            "de substâncias psicoactivas.",
            "A identificação dos factores psicossociais que se mantêm independentemente associados "
            "ao comportamento agressivo após ajustamento mútuo, com estimativas quantificadas e "
            "intervalos de confiança, testando as hipóteses formuladas.",
            "Um conjunto de recomendações operacionais para a escola, para os serviços distritais "
            "de educação e de saúde e para as famílias, alinhadas com as estratégias INSPIRE, e um "
            "contributo metodológico sobre o desempenho psicométrico dos instrumentos usados em "
            "adolescentes moçambicanos [[inspire2016]]."):
        e.marca(resultado)


def escrever_divulgacao(e):
    e.h1("9. DIVULGAÇÃO DOS RESULTADOS")
    e.p("Os resultados serão divulgados por quatro vias. Em primeiro lugar, o trabalho será "
        "apresentado e defendido publicamente perante um júri da Faculdade de Ciências de Saúde "
        "(FCS) da Universidade Lúrio, como requisito para a obtenção do grau de licenciado em Psicologia. "
        "Em segundo lugar, realizar-se-á uma sessão de devolução na Escola Secundária de Muatala, "
        "dirigida à direcção, aos professores, aos alunos e aos encarregados de educação, com "
        "apresentação dos resultados agregados e discussão das recomendações. Em terceiro lugar, "
        "será entregue um relatório executivo aos Serviços Distritais de Educação, Juventude e "
        "Tecnologia e aos serviços de saúde da cidade de Nampula. Em quarto lugar, procurar-se-á a "
        "publicação dos principais achados em revista científica revista por pares, na área da "
        "psicologia ou da saúde pública, e a sua apresentação em jornadas científicas nacionais.")


def escrever_cronograma_orcamento(e, h, doc):
    e.h1("10. CRONOGRAMA DE ACTIVIDADES")
    e.p("O cronograma foi construído de modo a que nenhuma actividade com participantes, do "
        "pré-teste à recolha de dados, comece antes da aprovação ética, e a que a recolha "
        "decorra no segundo semestre do ano lectivo de 2026, antes das provas finais.")
    h.tabela(doc, "Quadro 3: Cronograma de actividades, de Julho de 2026 a Março de 2027.",
             CRONOGRAMA_COLUNAS, CRONOGRAMA, "Fonte: o autor, 2026.", tamanho=Pt(10),
             larguras=[Cm(4.6)] + [Cm(1.6)] * 7)

    e.h1("11. ORÇAMENTO")
    e.p("O orçamento estimado cobre a totalidade das despesas previstas, desde a impressão dos "
        "instrumentos até à devolução dos resultados à escola. Os valores estão expressos em "
        "meticais e serão suportados pelo investigador, salvo apoio institucional que venha a ser "
        "concedido.")
    h.tabela(doc, "Quadro 4: Orçamento estimado do estudo.",
             ["Rubrica", "Quantidade", "Custo unitário (MZN)", "Custo total (MZN)"],
             ORCAMENTO, "Fonte: o autor, 2026. MZN: metical moçambicano.",
             larguras=[Cm(7.0), Cm(3.0), Cm(3.0), Cm(3.0)])

    e.h1("12. RECURSOS HUMANOS")
    h.tabela(doc, "Quadro 5: Recursos humanos afectos ao estudo.",
             ["Interveniente", "Categoria", "Função"], RECURSOS_HUMANOS,
             "Fonte: o autor, 2026.", larguras=[Cm(4.4), Cm(5.6), Cm(6.0)])
