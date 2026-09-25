"""Calculo do tamanho da amostra e do poder para o objectivo analitico.

O tamanho da amostra dimensiona a estimativa descritiva (proporcao unica). O poder
verifica se essa amostra chega para os modelos de regressao e para a analise de mediacao
exploratoria, depois de descontar a nao resposta e o efeito de desenho da amostragem
por turmas.
"""
import math

from scipy import optimize, stats

Z = 1.96
PREVALENCIA = 0.537
PRECISAO = 0.05
DEFF = 1.5
DEFF_SENSIBILIDADE = 2.0
NAO_RESPOSTA = 0.10
POPULACOES = (800, 1200, 1600, 2000, 2500)
POPULACAO_EXEMPLO = 1600

ALFA = 0.05
PODER = 0.80
PREDITORES_LINEAR = 35
EXPOSICAO_TIPICA = 0.30
PREVALENCIA_LUTAS = 0.364  # desfecho do modelo logistico: lutas fisicas (Han et al., 2019)
EVENTOS_POR_PARAMETRO = 10


def amostra_base(deff=DEFF):
    """Tamanho minimo para populacao infinita, antes e depois do efeito de desenho."""
    n0 = (Z ** 2) * PREVALENCIA * (1 - PREVALENCIA) / (PRECISAO ** 2)
    return math.ceil(n0), math.ceil(math.ceil(n0) * deff)


def n0_exacto():
    """Valor da formula antes do arredondamento, para mostrar a substituicao no texto."""
    return (Z ** 2) * PREVALENCIA * (1 - PREVALENCIA) / (PRECISAO ** 2)


def amostra_para(populacao, deff=DEFF):
    """Amostra corrigida para populacao finita e amostra final, para um dado N."""
    _n0, n_deff = amostra_base(deff)
    corrigido = math.ceil(n_deff / (1 + (n_deff - 1) / populacao))
    return corrigido, math.ceil(corrigido / (1 - NAO_RESPOSTA))


def cenarios_amostra():
    """Tabela de cenarios: correccao para populacao finita, acrescimo por nao resposta e,
    como analise de sensibilidade, a amostra final com um efeito de desenho de 2,0."""
    linhas = []
    for populacao in POPULACOES:
        corrigido, final = amostra_para(populacao)
        _corrigido, final_sensibilidade = amostra_para(populacao, DEFF_SENSIBILIDADE)
        linhas.append([f"{populacao:,}".replace(",", "."), str(corrigido), str(final),
                       str(final_sensibilidade)])
    return linhas


def amostra_efectiva(populacao):
    """Questionarios validos esperados e o seu equivalente em amostragem aleatoria simples.

    Os validos sao a amostra corrigida, porque o acrescimo de 10% existe para compensar a
    nao resposta; o tamanho efectivo divide-os pelo efeito de desenho.
    """
    respondentes, _final = amostra_para(populacao)
    return respondentes, respondentes / DEFF


def _poder_f(f2, n, preditores, alfa):
    """Poder do teste F para um coeficiente isolado num modelo com k preditores."""
    gl_erro = n - preditores - 1
    critico = stats.f.ppf(1 - alfa, 1, gl_erro)
    return 1 - stats.ncf.cdf(critico, 1, gl_erro, f2 * n)


def f2_minimo_detectavel(n, preditores=PREDITORES_LINEAR, alfa=ALFA, poder=PODER):
    """Menor tamanho de efeito de Cohen (f2) detectavel na regressao linear multipla."""
    return optimize.brentq(lambda f2: _poder_f(f2, n, preditores, alfa) - poder, 1e-5, 2.0)


def _proporcoes_para_or(odds_ratio, exposicao, desfecho):
    """Proporcoes do desfecho em expostos e nao expostos que mantem a prevalencia global."""
    def expostos(p0):
        return odds_ratio * p0 / (1 - p0 + odds_ratio * p0)

    p0 = optimize.brentq(lambda p: exposicao * expostos(p) + (1 - exposicao) * p - desfecho,
                         1e-9, desfecho)
    return expostos(p0), p0


def _poder_duas_proporcoes(odds_ratio, n, exposicao, desfecho, alfa):
    p1, p0 = _proporcoes_para_or(odds_ratio, exposicao, desfecho)
    h = 2 * math.asin(math.sqrt(p1)) - 2 * math.asin(math.sqrt(p0))
    n1, n2 = n * exposicao, n * (1 - exposicao)
    return stats.norm.cdf(abs(h) * math.sqrt(n1 * n2 / (n1 + n2)) - stats.norm.ppf(1 - alfa / 2))


def or_minimo_detectavel(n, exposicao=EXPOSICAO_TIPICA,
                         desfecho=PREVALENCIA_LUTAS, alfa=ALFA, poder=PODER):
    """Menor odds ratio detectavel para uma exposicao binaria com a prevalencia dada."""
    return optimize.brentq(
        lambda o: _poder_duas_proporcoes(o, n, exposicao, desfecho, alfa) - poder, 1.001, 50.0)


def parametros_maximos_logistica(respondentes, desfecho=PREVALENCIA_LUTAS,
                                 eventos_por_parametro=EVENTOS_POR_PARAMETRO):
    """Numero maximo de parametros no modelo logistico pela regra dos eventos por variavel."""
    return math.floor(eventos_esperados(respondentes, desfecho) / eventos_por_parametro)


def eventos_esperados(respondentes, desfecho=PREVALENCIA_LUTAS):
    """Adolescentes envolvidos em lutas fisicas esperados; o mesmo valor que o texto mostra."""
    return round(respondentes * desfecho)


def poder_mediacao(a, b, n, alfa=ALFA):
    """Poder do teste de significancia conjunta do efeito indirecto (X -> M -> Y).

    Coeficientes padronizados, sem efeito directo. O caminho a e testado na regressao de M
    em X; o caminho b na regressao de Y em M ajustada a X, cujo f2 parcial e
    b2(1 - a2)/(1 - b2). O efeito indirecto e declarado quando ambos sao significativos; os
    dois testes sao aproximadamente independentes, pelo que o poder e o produto.
    """
    f2_a = a ** 2 / (1 - a ** 2)
    f2_b = b ** 2 * (1 - a ** 2) / (1 - b ** 2)
    return _poder_f(f2_a, n, 1, alfa) * _poder_f(f2_b, n, 2, alfa)


def efeito_minimo_mediacao(n, poder=PODER, alfa=ALFA):
    """Menor valor comum de a e b detectavel com o poder pedido."""
    return optimize.brentq(lambda efeito: poder_mediacao(efeito, efeito, n, alfa) - poder,
                           0.01, 0.9)
