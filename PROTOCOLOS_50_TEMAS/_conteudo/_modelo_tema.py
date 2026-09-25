# -*- coding: utf-8 -*-
"""
MODELO DE MODULO DE TEMA. Copiar para tema_NN.py e substituir TODO o conteudo.
Os textos abaixo so' mostram a forma dos campos; nao contem dados reais e
nenhuma frase deve ser reaproveitada.

Compor e validar:   python ../_motor/motor.py tema_NN.py
Verificar fontes:   python ../_motor/refs.py verificar tema_NN.py
"""
from blocos import (CAMPO, ESCALA, FORMULA, H3, LISTA, NOTA, P, PERG,
                    QUADRO, QUEBRA, TABELA)

NUMERO = 0                       # 1 a 50, igual ao documento de temas
SLUG = "Palavras_Chave_Do_Tema"  # nome do ficheiro .docx (ASCII, sem espacos)
TITULO = ("Título definitivo do protocolo, com local e período, "
          "até cerca de 25 palavras")
DESENHO = "Transversal analítico, inquérito por entrevista"  # para o LEIA-ME

AUTOR = "[Nome do(a) estudante]"
ORIENTADOR = "[Nome e grau académico do(a) orientador(a)]"

# ---------------------------------------------------------------- resumo --
# Parágrafo único, 250 a 300 palavras, sem citações, sem siglas.
RESUMO = ("...")
PALAVRAS_CHAVE = ["termo a", "termo b", "termo c"]   # 3 a 5, ordem alfabética
ABSTRACT = ("...")                                    # tradução fiel
KEYWORDS = ["term a", "term b", "term c"]             # 3 a 5, ordem alfabética

# Só as siglas efectivamente usadas no texto; forma extensa na 1.ª ocorrência.
ABREVIATURAS = [
    ("OMS", "Organização Mundial da Saúde"),
]

# ------------------------------------------------------------ referencias --
# Chave -> referência Vancouver GERADA por refs.py (doi / pmid / web).
# Nunca escrever metadados à mão. Mínimo 30 citadas; >= 80% de 2016 a 2026.
FONTES = {
    "chave2021": "Apelido AB, ... Título. Rev Abrev. 2021;9(4):e489-551. "
                 "doi:10.xxxx/xxxxx. PMID: 00000000.",
}
# Referências anteriores a 2016: só fontes seminais, com o motivo.
SEMINAIS = {
    # "chave1993": "Manual original dos indicadores de uso de medicamentos da OMS",
}

# ----------------------------------------------------- 1. introducao --------
INTRODUCAO = [
    P("Parágrafo com dado citado {chave2021}."),
]

# ----------------------------------------------------- 2. problema ----------
PROBLEMA = [P("...")]
PERGUNTA = "Qual é ...?"
DELIMITACAO = [P("...")]

# ----------------------------------------------------- 3. objectivos --------
OBJECTIVO_GERAL = "Avaliar ..."
OBJECTIVOS_ESPECIFICOS = [          # 3 a 5, verbo no infinitivo
    "Caracterizar ...",
    "Determinar ...",
    "Analisar a associação entre ...",
]

# ----------------------------------------------------- 4. hipoteses ---------
HIPOTESES_INTRO = [P("As hipóteses referem-se ao objectivo específico 3.")]
HIPOTESES = [
    ("H0", "não existe associação estatisticamente significativa entre ..."),
    ("H1", "existe associação estatisticamente significativa entre ..."),
]
QUESTOES = []   # para componentes descritivas (opcional)

# ----------------------------------------------------- 5. justificativa -----
JUSTIFICATIVA_INTRO = [P("...")]
JUSTIFICATIVA = {
    "cientifica": [P("...")],
    "academica": [P("...")],
    "social": [P("...")],
    "politica": [P("...")],
}

# ----------------------------------------------------- 6. revisao -----------
REVISAO = [
    ("Título do subtema 6.1", [P("..."), P("...")]),
    ("Título do subtema 6.2", [P("..."), H3("Sub-subtema, se necessário"),
                               P("...")]),
]

# ----------------------------------------------------- 7. estado da arte ----
ESTADO_ARTE = [
    P("O [[quadro:estado_arte]] sintetiza ..."),
    QUADRO("estado_arte", "Síntese de estudos sobre ... (estado da arte)",
           ["Autor (ano)", "Local", "Desenho (n)", "Principais resultados"],
           [["Apelido et al. (2021) {chave2021}", "País", "Transversal (586)",
             "Achado com números reais da fonte."]],
           larguras=[3.2, 2.3, 2.8, 7.7],
           fonte="Elaboração própria (2026), a partir das fontes citadas."),
    P("Leitura crítica do quadro: padrão recorrente e lacuna que o estudo "
      "preenche."),
]
ESQUEMA_TEXTO = [P("A [[figura:esquema]] representa ...")]
ESQUEMA_TITULO = "Esquema conceptual do problema de investigação"
ESQUEMA = {
    "contexto": "Local, população e período",
    "blocos": [
        ("Factores sociodemográficos", ["idade", "sexo", "escolaridade"]),
        ("Factores clínicos", ["..."]),
    ],
    "desfecho": ("Variável dependente", ["categoria 1", "categoria 2"]),
    "moderadores": ("Variáveis de confundimento", ["..."]),   # ou None
}

# ----------------------------------------------------- 8. metodologia -------
METODOLOGIA = [
    ("Tipo e desenho do estudo", [P("...")]),
    ("Local e período do estudo", [P("...")]),
    ("População e unidade de análise", [P("...")]),
    ("Amostra e cálculo do tamanho da amostra", [
        P("..."),
        FORMULA("n<sub>0</sub> = Z<sup>2</sup> × p × (1 - p) / d<sup>2</sup>"),
        P("..."),
    ]),
    ("Critérios de inclusão e de exclusão", [
        H3("Critérios de inclusão"), LISTA(["..."]),
        H3("Critérios de exclusão"), LISTA(["..."]),
    ]),
    ("Variáveis e definições operacionais", [
        P("O [[quadro:variaveis]] apresenta ..."),
        QUADRO("variaveis", "Variáveis do estudo e definições operacionais",
               ["Variável", "Tipo", "Definição operacional e categorias",
                "Objectivo"],
               [["Idade", "Independente, quantitativa", "Anos completos", "1"]],
               larguras=[3.2, 2.8, 8.0, 2.0]),
    ]),
    ("Instrumentos de recolha de dados e respectivas fontes", [P("...")]),
    ("Procedimentos de recolha de dados e controlo de qualidade", [P("...")]),
    ("Processamento e análise dos dados", [P("...")]),
    ("Limitações do estudo e estratégias de mitigação", [
        P("O [[quadro:limitacoes]] ..."),
        QUADRO("limitacoes", "Limitações previstas e estratégias de mitigação",
               ["Limitação", "Consequência", "Mitigação"], [["...", "...", "..."]],
               larguras=[5, 5, 6]),
    ]),
    ("Considerações éticas", [P("..."), LISTA(["..."])]),
]

# ----------------------------------------------------- 9 e 10 ---------------
RESULTADOS_ESPERADOS = [P("..."), LISTA(["Um resultado por objectivo ..."])]
DIVULGACAO = [P("...")]

# ----------------------------------------------------- 11. cronograma -------
CRONOGRAMA_TEXTO = [P("O [[quadro:cronograma]] distribui ...")]
CRONOGRAMA = {
    "inicio": (2026, 10),       # (ano, mês) da primeira coluna
    "n_meses": 12,
    "actividades": [            # (actividade, [meses 1..n_meses])
        ("Revisão da literatura e redacção do protocolo", [1, 2]),
    ],
}

# ----------------------------------------------------- 12. orcamento --------
ORCAMENTO_TEXTO = [P("A [[tabela:orcamento]] apresenta ...")]
ORCAMENTO = [                   # (rubrica, unidade, quantidade, custo unitário MT)
    ("Impressão de questionários", "página", 1500, 5),
]
ORCAMENTO_IMPREVISTOS = 0.10    # fracção do subtotal (0 para não incluir)

# ----------------------------------------------------- apendices ------------
APENDICES = [
    ("Questionário ...", [
        NOTA("Instruções ao entrevistador ..."),
        H3("Secção I. Dados sociodemográficos"),
        PERG("Sexo:", ["Masculino", "Feminino"]),
        PERG("Idade em anos completos:"),
        ESCALA(["Afirmação 1", "Afirmação 2"],
               ["1", "2", "3", "4", "5"]),
        CAMPO("Código do questionário: __________"),
    ]),
    ("Folha de informação ao participante", [P("...")]),
    ("Termo de consentimento livre e esclarecido", [P("..."), CAMPO("...")]),
    ("Pedido de autorização institucional", [P("...")]),
]
