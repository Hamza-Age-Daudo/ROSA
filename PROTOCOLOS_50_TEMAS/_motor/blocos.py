# -*- coding: utf-8 -*-
"""
Blocos de conteudo usados nos modulos de tema (_conteudo/tema_NN.py).

Marcacao aceite dentro de qualquer texto:
  {chave}  ou  {chave1,chave2}      citacao Vancouver (numero atribuido pelo motor)
  [[quadro:chave]] [[tabela:chave]] [[figura:esquema]]   remissao numerada
  *italico*                          nomes cientificos, termos latinos
  <sub>0</sub>  <sup>2</sup>         indices e expoentes reais do Word
O negrito (**...**) so e' permitido dentro de celulas de tabelas.
"""


def P(texto):
    """Paragrafo justificado do corpo do texto."""
    return {"tipo": "p", "texto": texto}


def LISTA(itens, numerada=False):
    """Lista com marcas (ou numerada 1., 2., ...). Cada item e' uma frase."""
    return {"tipo": "lista", "itens": list(itens), "numerada": numerada}


def H3(texto):
    """Subtitulo de terceiro nivel (numerado automaticamente, sem negrito)."""
    return {"tipo": "h3", "texto": texto}


def FORMULA(texto):
    """Formula centrada, em italico. Usar <sub> e <sup> para indices."""
    return {"tipo": "formula", "texto": texto}


def NOTA(texto):
    """Texto em corpo 10, espaco simples (notas, observacoes de formulario)."""
    return {"tipo": "nota", "texto": texto}


def TABELA(chave, titulo, cabecalho, linhas, larguras=None,
           fonte="Elaboração própria (2026).", nota=None):
    """Tabela (informacao principal numerica). Titulo acima, fonte abaixo.
    chave=None cria uma tabela sem numero nem legenda (so em apendices)."""
    return {"tipo": "tabela", "rotulo": "Tabela", "chave": chave,
            "titulo": titulo, "cabecalho": list(cabecalho),
            "linhas": [list(l) for l in linhas], "larguras": larguras,
            "fonte": fonte, "nota": nota}


def QUADRO(chave, titulo, cabecalho, linhas, larguras=None,
           fonte="Elaboração própria (2026).", nota=None):
    """Quadro (informacao principal textual ou comparativa)."""
    return {"tipo": "tabela", "rotulo": "Quadro", "chave": chave,
            "titulo": titulo, "cabecalho": list(cabecalho),
            "linhas": [list(l) for l in linhas], "larguras": larguras,
            "fonte": fonte, "nota": nota}


def CAMPO(texto):
    """Linha de formulario alinhada a' esquerda, espaco simples."""
    return {"tipo": "campo", "texto": texto}


def PERG(texto, opcoes=None, instrucao=None):
    """Pergunta de questionario. opcoes: lista de respostas '( ) ...'.
    Sem opcoes, deixa uma linha para resposta aberta."""
    return {"tipo": "pergunta", "texto": texto,
            "opcoes": list(opcoes) if opcoes else [], "instrucao": instrucao}


def ESCALA(afirmacoes, niveis, cabecalho_item="Afirmação"):
    """Grelha de escala de Likert (sem numero de quadro). afirmacoes: lista de
    textos; niveis: lista de rotulos curtos das colunas (ex.: '1', '2', ...)."""
    return {"tipo": "escala", "afirmacoes": list(afirmacoes),
            "niveis": list(niveis), "cabecalho_item": cabecalho_item}


def QUEBRA():
    """Quebra de pagina."""
    return {"tipo": "quebra"}
