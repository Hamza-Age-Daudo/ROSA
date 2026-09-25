"""Gera a Figura 1 do protocolo: esquema conceptual dos factores psicossociais
associados ao comportamento agressivo no adolescente, organizado pelos quatro
niveis do modelo ecologico da Organizacao Mundial da Saude."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

matplotlib.rcParams["font.family"] = "serif"
matplotlib.rcParams["font.serif"] = ["Times New Roman", "DejaVu Serif"]

DESTINO = Path(__file__).resolve().parent / "figuras" / "esquema_conceptual.png"

NIVEIS = [
    ("Nível sociocultural e comunitário", "#f1f1f1",
     "Exposição à violência na comunidade, pobreza do agregado, normas de género,\n"
     "disponibilidade de álcool e drogas, exposição a conteúdos violentos nos média"),
    ("Nível escolar e grupo de pares", "#e6e6e6",
     "Vitimização por bullying, castigo físico na escola, ligação à escola,\n"
     "associação a pares desviantes, insucesso e absentismo escolar"),
    ("Nível familiar", "#dadada",
     "Funcionamento familiar, supervisão e ligação parental, castigo físico em casa,\n"
     "violência entre os progenitores, ausência parental e orfandade"),
    ("Nível individual", "#cdcdcd",
     "Idade, sexo, classe, impulsividade, auto-estima, sintomas emocionais,\n"
     "consumo de álcool, tabaco e outras substâncias psicoactivas"),
]

CAIXA_X, CAIXA_LARGURA = 0.35, 6.85
ALTURA, PRIMEIRO_TOPO, INTERVALO = 1.72, 9.45, 2.05


def desenhar():
    fig, eixo = plt.subplots(figsize=(10.4, 7.0), dpi=220)
    eixo.set_xlim(0, 12)
    eixo.set_ylim(0, 10)
    eixo.axis("off")

    destino = (8.45, 5.15)
    for indice, (rotulo, cor, detalhe) in enumerate(NIVEIS):
        topo = PRIMEIRO_TOPO - indice * INTERVALO
        base = topo - ALTURA
        eixo.add_patch(FancyBboxPatch((CAIXA_X, base), CAIXA_LARGURA, ALTURA,
                                      boxstyle="round,pad=0.06", facecolor=cor,
                                      edgecolor="#3c3c3c", linewidth=1.1, zorder=2))
        eixo.text(CAIXA_X + 0.28, topo - 0.42, rotulo, ha="left", va="center",
                  fontsize=10.2, fontweight="bold", color="#111111", zorder=3)
        eixo.text(CAIXA_X + 0.28, base + 0.60, detalhe, ha="left", va="center",
                  fontsize=8.4, color="#111111", zorder=3, linespacing=1.55)
        eixo.add_patch(FancyArrowPatch((CAIXA_X + CAIXA_LARGURA + 0.05, topo - ALTURA / 2),
                                       destino, arrowstyle="-|>", mutation_scale=17,
                                       linewidth=1.3, color="#3c3c3c",
                                       connectionstyle="arc3,rad=0.0", zorder=1))

    eixo.add_patch(FancyBboxPatch((8.55, 3.55), 3.15, 3.15, boxstyle="round,pad=0.12",
                                  facecolor="#ffffff", edgecolor="#111111",
                                  linewidth=1.8, zorder=4))
    eixo.text(10.13, 6.22, "Comportamento agressivo", ha="center", va="center",
              fontsize=10.4, fontweight="bold", color="#111111", zorder=5)
    eixo.text(10.13, 5.10,
              "Agressão física, agressão verbal,\nira e hostilidade (BPAQ-SF)\n\n"
              "Agressão reactiva e\nagressão proactiva (RPQ)",
              ha="center", va="center", fontsize=8.6, color="#111111",
              zorder=5, linespacing=1.6)

    eixo.text(0.35, 1.05,
              "Variáveis de controlo: idade, sexo e classe frequentada.",
              ha="left", va="center", fontsize=8.4, color="#222222")
    eixo.text(0.35, 0.50,
              "Desenho transversal analítico: a exposição e o desfecho são medidos no mesmo momento, "
              "pelo que se\nestimam associações e não relações de causa e efeito.",
              ha="left", va="center", fontsize=8.4, color="#333333", linespacing=1.6)

    DESTINO.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(DESTINO, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("figura gravada:", DESTINO)


if __name__ == "__main__":
    desenhar()
