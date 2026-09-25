"""Gera a Figura 1 do protocolo: esquema conceptual do comportamento agressivo no
adolescente. Os factores psicossociais do contexto (distais) relacionam-se com o
comportamento agressivo sobretudo atraves de factores psicologicos individuais
(proximais), como propoe o Modelo Geral da Agressao; o modelo ecologico da OMS
organiza os contextos."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

matplotlib.rcParams["font.family"] = "serif"
matplotlib.rcParams["font.serif"] = ["Times New Roman", "DejaVu Serif"]

DESTINO = Path(__file__).resolve().parent / "figuras" / "esquema_conceptual.png"

CONTEXTOS = [
    ("Contexto familiar", "#e4e4e4",
     "Funcionamento familiar\nSupervisão parental\nCastigo físico e violência\npsicológica em casa\n"
     "Violência entre adultos\ndo agregado"),
    ("Escola e grupo de pares", "#e4e4e4",
     "Vitimização por bullying\nCastigo físico na escola\nLigação à escola\n"
     "Pares desviantes\nRepetência e absentismo"),
    ("Comunidade e cultura", "#e4e4e4",
     "Violência presenciada\nno bairro\nInsegurança alimentar\n"
     "Acesso a álcool e drogas\nConteúdos violentos"),
]

PSICOLOGICOS_ESQUERDA = ("Dificuldades de regulação emocional\n"
                         "Hiperactividade e desatenção\n"
                         "Sintomas emocionais (ansiedade, tristeza)\n"
                         "Sintomas de stress pós-traumático")
PSICOLOGICOS_DIREITA = ("Auto-estima\n"
                        "Comportamento pró-social\n"
                        "Problemas de relacionamento com os pares\n"
                        "Consumo de substâncias psicoactivas")

DESFECHO = ("Agressão física, agressão verbal, ira e hostilidade (BPAQ-SF)\n"
            "Agressão reactiva e agressão proactiva (RPQ)\n"
            "Lutas físicas e problemas de comportamento (SDQ, rastreio)")

COR_LINHA = "#2e2e2e"
ALVOS_NO_BLOCO_PSICOLOGICO = (2.4, 5.0, 7.6)


def _caixa(eixo, x, y, largura, altura, cor, espessura=1.1):
    eixo.add_patch(FancyBboxPatch((x, y), largura, altura, boxstyle="round,pad=0.05",
                                  facecolor=cor, edgecolor=COR_LINHA, linewidth=espessura,
                                  zorder=2))


def _seta(eixo, origem, destino, tracejada=False, curva=0.0):
    eixo.add_patch(FancyArrowPatch(origem, destino, arrowstyle="-|>", mutation_scale=15,
                                   linewidth=1.2, color=COR_LINHA,
                                   linestyle=(0, (4, 3)) if tracejada else "solid",
                                   connectionstyle=f"arc3,rad={curva}", zorder=1))


def _contextos(eixo):
    eixo.text(5.0, 9.72, "Factores psicossociais do contexto (distais)", ha="center",
              va="center", fontsize=10.5, fontweight="bold", color="#111111")
    largura, intervalo = 3.05, 0.2
    for indice, (rotulo, cor, detalhe) in enumerate(CONTEXTOS):
        x = 0.2 + indice * (largura + intervalo)
        _caixa(eixo, x, 6.95, largura, 2.45, cor)
        eixo.text(x + largura / 2, 9.08, rotulo, ha="center", va="center", fontsize=10,
                  fontweight="bold", color="#111111", zorder=3)
        eixo.text(x + largura / 2, 7.95, detalhe, ha="center", va="center", fontsize=8.8,
                  color="#111111", zorder=3, linespacing=1.35)
        _seta(eixo, (x + largura / 2, 6.93), (ALVOS_NO_BLOCO_PSICOLOGICO[indice], 5.93))


def _psicologicos(eixo):
    _caixa(eixo, 0.2, 3.55, 9.55, 2.3, "#f4f4f4", espessura=1.4)
    eixo.text(5.0, 5.52, "Factores psicológicos individuais (proximais)", ha="center",
              va="center", fontsize=10.5, fontweight="bold", color="#111111", zorder=3)
    eixo.text(0.5, 4.42, PSICOLOGICOS_ESQUERDA, ha="left", va="center", fontsize=8.9,
              color="#111111", zorder=3, linespacing=1.4)
    eixo.text(5.35, 4.42, PSICOLOGICOS_DIREITA, ha="left", va="center", fontsize=8.9,
              color="#111111", zorder=3, linespacing=1.4)
    _seta(eixo, (5.0, 3.53), (5.0, 2.72))


def _desfecho(eixo):
    _caixa(eixo, 1.2, 1.05, 7.55, 1.6, "#ffffff", espessura=1.8)
    eixo.text(5.0, 2.33, "Comportamento agressivo", ha="center", va="center", fontsize=10.5,
              fontweight="bold", color="#111111", zorder=3)
    eixo.text(5.0, 1.58, DESFECHO, ha="center", va="center", fontsize=8.9, color="#111111",
              zorder=3, linespacing=1.4)
    # associacao directa dos contextos com o desfecho, nao explicada pelos factores psicologicos
    _seta(eixo, (0.17, 7.6), (1.15, 1.85), tracejada=True, curva=0.22)
    _seta(eixo, (9.78, 7.6), (8.8, 1.85), tracejada=True, curva=-0.22)


def desenhar():
    fig, eixo = plt.subplots(figsize=(8.6, 8.2), dpi=220)
    eixo.set_xlim(-0.35, 10.3)
    eixo.set_ylim(-0.25, 10.0)
    eixo.axis("off")
    _contextos(eixo)
    _psicologicos(eixo)
    _desfecho(eixo)
    eixo.text(-0.3, 0.55, "Setas contínuas: relação através dos factores psicológicos; setas "
              "tracejadas: associação directa. Variáveis de controlo: idade, sexo e classe.",
              ha="left", va="center", fontsize=8.4, color="#222222")
    eixo.text(-0.3, 0.05, "Desenho transversal: estimam-se associações e mediação estatística, "
              "não relações de causa e efeito.", ha="left", va="center", fontsize=8.4,
              color="#222222")
    DESTINO.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(DESTINO, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("figura gravada:", DESTINO)


if __name__ == "__main__":
    desenhar()
