# -*- coding: utf-8 -*-
"""
Desenho do esquema conceptual do problema (figura a preto e branco).

ESQUEMA = {
    "blocos": [("Factores sociodemográficos", ["idade", "sexo", ...]), ...],
    "desfecho": ("Adesão ao TARV", ["boa (>= 95%)", "insuficiente"]),
    "moderadores": ("Variáveis de confundimento", ["...", ...]),   # opcional
    "contexto": "Texto curto no topo (opcional), p. ex. o local e o período",
}
Os blocos da esquerda ligam-se ao desfecho por setas cheias; os moderadores,
quando existem, ligam-se ao desfecho por seta tracejada.
"""
import textwrap

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch  # noqa: E402

plt.rcParams["font.family"] = "Times New Roman"

LARG = 6.3          # polegadas (16 cm)
FS_TIT = 9.5
FS_ITEM = 8.6
LINHA = 0.165       # altura de uma linha de item, em polegadas
PAD = 0.09


def _linhas(titulo, itens, largura_chars):
    tit = textwrap.wrap(titulo, largura_chars) or [""]
    corpo = []
    for it in itens:
        partes = textwrap.wrap(it, largura_chars - 2) or [""]
        corpo.append("• " + partes[0])
        corpo.extend("  " + x for x in partes[1:])
    return tit, corpo


def _altura(tit, corpo):
    return PAD * 2 + len(tit) * (LINHA + 0.01) + 0.05 + len(corpo) * LINHA


def _caixa(ax, x, y, w, h, tit, corpo, destaque=False):
    caixa = FancyBboxPatch((x, y), w, h,
                           boxstyle="round,pad=0,rounding_size=0.06",
                           linewidth=1.6 if destaque else 0.9,
                           edgecolor="black",
                           facecolor="#E6E6E6" if destaque else "white")
    ax.add_patch(caixa)
    ty = y + h - PAD
    for t in tit:
        ax.text(x + w / 2, ty, t, ha="center", va="top", fontsize=FS_TIT,
                fontweight="bold")
        ty -= LINHA + 0.01
    ty -= 0.05
    for c in corpo:
        ax.text(x + 0.07, ty, c, ha="left", va="top", fontsize=FS_ITEM)
        ty -= LINHA


def desenhar(esquema, caminho_png):
    blocos = esquema["blocos"]
    d_tit, d_itens = esquema["desfecho"]
    mod = esquema.get("moderadores")
    contexto = esquema.get("contexto")

    xe, we = 0.05, 3.55            # coluna da esquerda
    xd, wd = 4.35, 1.9             # desfecho
    esq = [_linhas(t, i, 58) for t, i in blocos]
    alturas = [_altura(t, c) for t, c in esq]
    gap = 0.14
    h_esq = sum(alturas) + gap * (len(alturas) - 1)

    dt, dc = _linhas(d_tit, d_itens, 30)
    h_d = _altura(dt, dc)

    h_mod, mt, mc = 0, [], []
    if mod:
        mt, mc = _linhas(mod[0], mod[1], 30)
        h_mod = _altura(mt, mc)

    h_ctx = 0.32 if contexto else 0
    h_dir = h_d + (0.45 + h_mod if mod else 0)
    altura = max(h_esq, h_dir) + 0.2 + h_ctx

    fig = plt.figure(figsize=(LARG, altura), dpi=300)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, LARG)
    ax.set_ylim(0, altura)
    ax.axis("off")

    topo = altura - 0.1 - h_ctx
    if contexto:
        ax.text(LARG / 2, altura - 0.08, contexto, ha="center", va="top",
                fontsize=FS_TIT, style="italic")

    y = topo - (max(h_esq, h_dir) - h_esq) / 2
    centros = []
    for (tit, corpo), h in zip(esq, alturas):
        y -= h
        _caixa(ax, xe, y, we, h, tit, corpo)
        centros.append(y + h / 2)
        y -= gap

    y_d = topo - (max(h_esq, h_dir) - h_dir) / 2 - h_d
    _caixa(ax, xd, y_d, wd, h_d, dt, dc, destaque=True)
    cy_d = y_d + h_d / 2
    for cy in centros:
        destino_y = min(max(cy, y_d + 0.12), y_d + h_d - 0.12)
        ax.add_patch(FancyArrowPatch((xe + we + 0.02, cy),
                                     (xd - 0.02, destino_y),
                                     arrowstyle="-|>", mutation_scale=11,
                                     linewidth=0.9, color="black"))
    if mod:
        y_m = y_d - 0.45 - h_mod
        _caixa(ax, xd, y_m, wd, h_mod, mt, mc)
        ax.add_patch(FancyArrowPatch((xd + wd / 2, y_m + h_mod + 0.02),
                                     (xd + wd / 2, y_d - 0.02),
                                     arrowstyle="-|>", mutation_scale=11,
                                     linewidth=0.9, color="black",
                                     linestyle=(0, (4, 3))))
    _ = cy_d
    fig.savefig(caminho_png, dpi=300, facecolor="white")
    plt.close(fig)
    return caminho_png
