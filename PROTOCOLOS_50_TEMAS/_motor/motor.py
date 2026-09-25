# -*- coding: utf-8 -*-
"""
Motor comum dos 50 protocolos: le um modulo de tema (_conteudo/tema_NN.py),
compoe o protocolo na estrutura de 13 seccoes da FCS/UniLurio, grava o .docx
na pasta da categoria e valida a conformidade.

Uso:
  python motor.py ../_conteudo/tema_06.py
Saida:
  ../NN_CATEGORIA/PROTOCOLO_TNN_SLUG.docx  e o relatorio de validacao.
Entregar apenas quando o relatorio indicar "PROBLEMAS: nenhum".
"""
import importlib.util
import os
import re
import sys
import unicodedata

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
sys.path.insert(0, AQUI)

import docx  # noqa: E402

import esquema as ESQ  # noqa: E402
import norma as N  # noqa: E402
from validacao import validar  # noqa: E402

AL = N.AL

CATEGORIAS = {
    1: ("01_Farmacia_Clinica", "Farmácia Clínica e Cuidados Farmacêuticos"),
    2: ("02_Farmacoepidemiologia_URM",
        "Farmacoepidemiologia e Uso Racional de Medicamentos"),
    3: ("03_Farmacovigilancia", "Farmacovigilância e Segurança do Medicamento"),
    4: ("04_Farmacia_Hospitalar_Gestao",
        "Farmácia Hospitalar e Gestão Farmacêutica"),
    5: ("05_Farmacia_Comunitaria_Saude_Publica",
        "Farmácia Comunitária e Saúde Pública"),
    6: ("06_Controlo_Qualidade",
        "Controlo de Qualidade e Análise de Medicamentos"),
    7: ("07_Farmacognosia_Plantas_Medicinais",
        "Farmacognosia e Plantas Medicinais"),
    8: ("08_Tecnologia_Farmaceutica", "Tecnologia Farmacêutica e Formulação"),
    9: ("09_Microbiologia_Resistencia",
        "Microbiologia Farmacêutica e Resistência Antimicrobiana"),
    10: ("10_Toxicologia_Cosmetica_Regulamentacao",
         "Toxicologia, Cosmética e Regulamentação Farmacêutica"),
}

MESES = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set",
         "Out", "Nov", "Dez"]

MARCA_CIT = re.compile(r"\{([a-z0-9_]+(?:\s*,\s*[a-z0-9_]+)*)\}")
MARCA_REM = re.compile(r"\[\[(quadro|tabela|figura):([a-z0-9_]+)\]\]")


# ==========================================================================
#  carregamento
# ==========================================================================

def carregar(caminho):
    spec = importlib.util.spec_from_file_location(
        "tema_" + os.path.basename(caminho).replace(".py", ""), caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def g(mod, nome, omissao=None):
    return getattr(mod, nome, omissao)


def pasta_e_ficheiro(mod):
    cat = (mod.NUMERO - 1) // 5 + 1
    pasta = os.path.join(RAIZ, CATEGORIAS[cat][0])
    os.makedirs(pasta, exist_ok=True)
    slug = re.sub(r"[^A-Za-z0-9_]", "_",
                  unicodedata.normalize("NFKD", mod.SLUG)
                  .encode("ascii", "ignore").decode())
    return pasta, os.path.join(pasta, f"PROTOCOLO_T{mod.NUMERO:02d}_{slug}.docx")


# ==========================================================================
#  bibliografia e remissoes
# ==========================================================================

class Bibliografia:
    def __init__(self, fontes):
        self.fontes = fontes
        self.ordem = []

    def numero(self, chave):
        if chave not in self.fontes:
            raise KeyError(f"Citacao de referencia inexistente em FONTES: "
                           f"{{{chave}}}")
        if chave not in self.ordem:
            self.ordem.append(chave)
        return self.ordem.index(chave) + 1

    @staticmethod
    def comprimir(nums):
        nums = sorted(set(nums))
        blocos, ini, ant = [], nums[0], nums[0]
        for n in nums[1:]:
            if n == ant + 1:
                ant = n
                continue
            blocos.append((ini, ant))
            ini = ant = n
        blocos.append((ini, ant))
        partes = []
        for a, b in blocos:
            if b - a >= 2:
                partes.append(f"{a}-{b}")
            elif b - a == 1:
                partes += [str(a), str(b)]
            else:
                partes.append(str(a))
        return ",".join(partes)

    def resolver(self, texto):
        def troca(m):
            chaves = [c.strip() for c in m.group(1).split(",") if c.strip()]
            return "(" + self.comprimir([self.numero(c) for c in chaves]) + ")"
        return MARCA_CIT.sub(troca, texto)

    def nao_citadas(self):
        return sorted(set(self.fontes) - set(self.ordem))


class Composicao:
    """Estado partilhado durante a composicao."""

    def __init__(self, mod):
        self.mod = mod
        self.bib = Bibliografia(mod.FONTES)
        self.numeros = {}           # (tipo, chave) -> numero
        self.referidos = set()      # (tipo, chave) remetidos no texto
        self.elementos = []         # (tipo, chave, numero, titulo)

    def txt(self, texto):
        texto = self.bib.resolver(texto)

        def rem(m):
            tipo, chave = m.group(1), m.group(2)
            if (tipo, chave) not in self.numeros:
                raise KeyError(f"Remissao para elemento inexistente: "
                               f"[[{tipo}:{chave}]]")
            self.referidos.add((tipo, chave))
            return f"{tipo.capitalize()} {self.numeros[(tipo, chave)]}"
        return MARCA_REM.sub(rem, texto)


# ==========================================================================
#  pre-numeracao de quadros, tabelas e figuras (pela ordem do documento)
# ==========================================================================

def sequencia_blocos(mod):
    """Todos os blocos do documento, pela ordem em que serao compostos."""
    seq = []
    for nome in ("INTRODUCAO", "PROBLEMA", "DELIMITACAO", "JUSTIFICATIVA_INTRO"):
        seq += g(mod, nome, []) or []
    for k in ("cientifica", "academica", "social", "politica"):
        seq += (g(mod, "JUSTIFICATIVA", {}) or {}).get(k, [])
    for _, blocos in g(mod, "REVISAO", []) or []:
        seq += blocos
    seq += g(mod, "ESTADO_ARTE", []) or []
    seq += g(mod, "ESQUEMA_TEXTO", []) or []
    seq.append({"tipo": "figura_esquema"})
    for _, blocos in g(mod, "METODOLOGIA", []) or []:
        seq += blocos
    for nome in ("RESULTADOS_ESPERADOS", "DIVULGACAO", "CRONOGRAMA_TEXTO"):
        seq += g(mod, nome, []) or []
    seq.append({"tipo": "cronograma"})
    seq += g(mod, "ORCAMENTO_TEXTO", []) or []
    seq.append({"tipo": "orcamento"})
    for _, blocos in g(mod, "APENDICES", []) or []:
        seq += blocos
    return seq


def numerar(comp):
    cont = {"quadro": 0, "tabela": 0, "figura": 0}
    for b in sequencia_blocos(comp.mod):
        t = b["tipo"]
        if t == "tabela" and b.get("chave"):
            tipo = b["rotulo"].lower()
            if (tipo, b["chave"]) in comp.numeros:
                raise KeyError(f"Chave de {tipo} repetida: {b['chave']}")
            cont[tipo] += 1
            comp.numeros[(tipo, b["chave"])] = cont[tipo]
        elif t == "figura_esquema":
            cont["figura"] += 1
            comp.numeros[("figura", "esquema")] = cont["figura"]
        elif t == "cronograma":
            cont["quadro"] += 1
            comp.numeros[("quadro", "cronograma")] = cont["quadro"]
        elif t == "orcamento":
            cont["tabela"] += 1
            comp.numeros[("tabela", "orcamento")] = cont["tabela"]


# ==========================================================================
#  composicao de blocos
# ==========================================================================

def compor_bloco(doc, comp, b, ctx):
    t = b["tipo"]
    if t == "p":
        N.paragrafo(doc, comp.txt(b["texto"]))
    elif t == "lista":
        N.lista(doc, [comp.txt(i) for i in b["itens"]], b.get("numerada"))
    elif t == "h3":
        if ctx.get("prefixo"):
            ctx["h3"] = ctx.get("h3", 0) + 1
            N.titulo(doc, f"{ctx['prefixo']}.{ctx['h3']}. "
                          f"{comp.txt(b['texto'])}", 3)
        else:
            N.subtitulo_formulario(doc, comp.txt(b["texto"]))
    elif t == "formula":
        N.formula(doc, comp.txt(b["texto"]))
    elif t == "nota":
        N.nota(doc, comp.txt(b["texto"]))
    elif t == "campo":
        N.campo_formulario(doc, comp.txt(b["texto"]))
    elif t == "quebra":
        N.quebra_de_pagina(doc)
    elif t == "tabela":
        compor_tabela(doc, comp, b)
    elif t == "pergunta":
        compor_pergunta(doc, comp, b, ctx)
    elif t == "escala":
        linhas = [[str(i + 1), comp.txt(a)] + ["(   )"] * len(b["niveis"])
                  for i, a in enumerate(b["afirmacoes"])]
        larg = [0.9, 8.5] + [1.1] * len(b["niveis"])
        N.tabela(doc, ["N.º", b.get("cabecalho_item", "Afirmação")] +
                 b["niveis"], linhas, larg)
        N.vazios(doc, 1)
    else:
        raise ValueError(f"Bloco desconhecido: {t}")


def compor_tabela(doc, comp, b):
    tipo = b["rotulo"].lower()
    if b.get("chave"):
        num = comp.numeros[(tipo, b["chave"])]
        N.legenda(doc, b["rotulo"], num, comp.txt(b["titulo"]))
        comp.elementos.append((tipo, b["chave"], num, b["titulo"]))
    cab = [comp.txt(c) for c in b["cabecalho"]]
    linhas = [[comp.txt(str(c)) for c in l] for l in b["linhas"]]
    N.tabela(doc, cab, linhas, b.get("larguras"))
    rodape = []
    if b.get("nota"):
        rodape.append(comp.txt(b["nota"]))
    if b.get("chave") and b.get("fonte"):
        rodape.append("Fonte: " + comp.txt(b["fonte"]))
    if rodape:
        N.fonte_elemento(doc, " ".join(rodape))
    else:
        N.vazios(doc, 1)


def compor_pergunta(doc, comp, b, ctx):
    ctx["q"] = ctx.get("q", 0) + 1
    p = N.campo_formulario(doc, f"{ctx['q']}. {comp.txt(b['texto'])}")
    p.paragraph_format.keep_with_next = True
    p.paragraph_format.space_before = N.Pt(4)
    if b.get("instrucao"):
        N.nota(doc, comp.txt(b["instrucao"]), AL.LEFT)
    ops = [comp.txt(o) for o in b.get("opcoes", [])]
    if not ops:
        N.campo_formulario(doc, "_" * 62)
        return
    curtas = sum(len(N.texto_simples(o)) + 8 for o in ops) <= 88
    if curtas:
        q = N.campo_formulario(doc, "     ".join(f"(   ) {o}" for o in ops))
        q.paragraph_format.left_indent = N.Cm(0.6)
    else:
        for o in ops:
            q = N.campo_formulario(doc, f"(   ) {o}")
            q.paragraph_format.left_indent = N.Cm(0.6)
            q.paragraph_format.space_after = N.Pt(1)


# ==========================================================================
#  seccoes
# ==========================================================================

def pretextuais(doc, comp):
    mod = comp.mod
    autor = g(mod, "AUTOR", "[Nome do(a) estudante]")
    orient = g(mod, "ORIENTADOR", "[Nome e grau académico do(a) orientador(a)]")
    topo = ["UNIVERSIDADE LÚRIO", "FACULDADE DE CIÊNCIAS DE SAÚDE",
            "CURSO DE LICENCIATURA EM FARMÁCIA"]
    # capa
    N.linhas_centradas(doc, topo, negrito=True)
    N.vazios(doc, 5)
    N.linhas_centradas(doc, ["Protocolo de Investigação"], espaco=10)
    N.linhas_centradas(doc, [mod.TITULO.upper()], negrito=True,
                       espacamento=1.5)
    N.vazios(doc, 5)
    N.linhas_centradas(doc, [autor])
    N.vazios(doc, 8)
    N.linhas_centradas(doc, ["Nampula", "2026"], negrito=True)
    # folha de rosto
    N.nova_pagina(N.linhas_centradas(doc, [autor])[0])
    N.vazios(doc, 5)
    N.linhas_centradas(doc, [mod.TITULO.upper()], negrito=True,
                       espacamento=1.5)
    N.vazios(doc, 3)
    N.paragrafo_direita(doc,
        "Protocolo de investigação apresentado à Faculdade de Ciências de "
        "Saúde da Universidade Lúrio, como parte dos requisitos para a "
        "elaboração do Trabalho de Conclusão de Curso conducente à obtenção "
        "do grau de licenciado em Farmácia.")
    N.vazios(doc, 1)
    N.paragrafo_direita(doc, f"Orientador(a): {orient}")
    N.vazios(doc, 6)
    N.linhas_centradas(doc, ["Nampula", "2026"], negrito=True)
    # declaracao do orientador
    N.titulo(doc, "Declaração do orientador", 1, nova_pagina=True)
    N.paragrafo(doc,
        f"Eu, {orient}, docente da Faculdade de Ciências de Saúde da "
        f"Universidade Lúrio, declaro que o protocolo de investigação "
        f"intitulado «{N.texto_simples(mod.TITULO)}», da autoria de {autor}, "
        f"estudante do curso de licenciatura em Farmácia, foi elaborado sob a "
        f"minha orientação e reúne as condições científicas e metodológicas "
        f"para ser submetido à apreciação da Comissão Científica e do comité "
        f"de bioética competente.")
    N.vazios(doc, 1)
    N.paragrafo(doc, "Nampula, ____ de ________________ de 2026", AL.LEFT)
    N.vazios(doc, 2)
    N.linhas_centradas(doc, ["O(A) Orientador(a)", "",
                             "_______________________________________",
                             f"({orient})"])
    # resumo e abstract
    N.titulo(doc, "Resumo", 1, nova_pagina=True)
    N.paragrafo(doc, mod.RESUMO)
    N.paragrafo(doc, "Palavras-chave: " + ", ".join(mod.PALAVRAS_CHAVE) + ".")
    N.titulo(doc, "Abstract", 1, nova_pagina=True)
    N.paragrafo(doc, mod.ABSTRACT)
    N.paragrafo(doc, "Keywords: " + ", ".join(mod.KEYWORDS) + ".")
    # abreviaturas
    N.titulo(doc, "Lista de abreviaturas e siglas", 1, nova_pagina=True)
    chave_ord = lambda s: unicodedata.normalize("NFKD", s[0]).lower()  # noqa
    for sig, significado in sorted(mod.ABREVIATURAS, key=chave_ord):
        N.sigla(doc, sig, significado)
    N.titulo_fora_do_indice(doc, "Índice")
    N.indice(doc)


def blocos(doc, comp, lista_blocos, prefixo=None):
    ctx = {"prefixo": prefixo}
    for b in lista_blocos or []:
        compor_bloco(doc, comp, b, ctx)


def seccoes(doc, comp, caminho_png):
    mod = comp.mod
    N.titulo(doc, "1. Introdução e contextualização", 1, nova_pagina=True)
    blocos(doc, comp, mod.INTRODUCAO)

    N.titulo(doc, "2. Identificação e formulação do problema e delimitação", 1)
    blocos(doc, comp, mod.PROBLEMA)
    N.titulo(doc, "2.1. Pergunta de investigação", 2)
    N.paragrafo(doc, comp.txt(mod.PERGUNTA), italico=True)
    N.titulo(doc, "2.2. Delimitação do estudo", 2)
    blocos(doc, comp, mod.DELIMITACAO)

    N.titulo(doc, "3. Objectivos", 1)
    N.titulo(doc, "3.1. Objectivo geral", 2)
    N.paragrafo(doc, comp.txt(mod.OBJECTIVO_GERAL))
    N.titulo(doc, "3.2. Objectivos específicos", 2)
    N.lista(doc, [comp.txt(o) for o in mod.OBJECTIVOS_ESPECIFICOS],
            numerada=True)

    hip, que = g(mod, "HIPOTESES", []), g(mod, "QUESTOES", [])
    if hip and que:
        N.titulo(doc, "4. Hipóteses e questões de investigação", 1)
    elif hip:
        N.titulo(doc, "4. Hipóteses de investigação", 1)
    else:
        N.titulo(doc, "4. Questões de investigação", 1)
    blocos(doc, comp, g(mod, "HIPOTESES_INTRO", []))
    for rot, texto in hip:
        N.lista(doc, [f"{rot}: {comp.txt(texto)}"])
    if que:
        if hip:
            N.paragrafo(doc, "Para as componentes descritivas, formulam-se "
                             "as seguintes questões de investigação:")
        N.lista(doc, [comp.txt(q) for q in que], numerada=True)

    N.titulo(doc, "5. Justificativa", 1)
    blocos(doc, comp, g(mod, "JUSTIFICATIVA_INTRO", []))
    for i, (k, nome) in enumerate((("cientifica", "Relevância científica"),
                                   ("academica", "Relevância académica"),
                                   ("social", "Relevância social"),
                                   ("politica", "Relevância política")), 1):
        N.titulo(doc, f"5.{i}. {nome}", 2)
        blocos(doc, comp, mod.JUSTIFICATIVA[k])

    N.titulo(doc, "6. Revisão da literatura", 1)
    for i, (tit, bl) in enumerate(mod.REVISAO, 1):
        N.titulo(doc, f"6.{i}. {comp.txt(tit)}", 2)
        blocos(doc, comp, bl, prefixo=f"6.{i}")

    N.titulo(doc, "7. Estado da arte e esquema conceptual", 1)
    N.titulo(doc, "7.1. Estado da arte", 2)
    blocos(doc, comp, mod.ESTADO_ARTE, prefixo="7.1")
    N.titulo(doc, "7.2. Esquema conceptual", 2)
    blocos(doc, comp, mod.ESQUEMA_TEXTO)
    num = comp.numeros[("figura", "esquema")]
    ESQ.desenhar(mod.ESQUEMA, caminho_png)
    N.legenda(doc, "Figura", num, comp.txt(g(
        mod, "ESQUEMA_TITULO", "Esquema conceptual do problema de investigação")))
    comp.elementos.append(("figura", "esquema", num, "esquema"))
    N.imagem(doc, caminho_png)
    N.fonte_elemento(doc, "Fonte: Elaboração própria (2026).")

    N.titulo(doc, "8. Metodologia", 1)
    for i, (tit, bl) in enumerate(mod.METODOLOGIA, 1):
        N.titulo(doc, f"8.{i}. {comp.txt(tit)}", 2)
        blocos(doc, comp, bl, prefixo=f"8.{i}")

    N.titulo(doc, "9. Resultados esperados", 1)
    blocos(doc, comp, mod.RESULTADOS_ESPERADOS)
    N.titulo(doc, "10. Divulgação dos resultados", 1)
    blocos(doc, comp, mod.DIVULGACAO)

    N.titulo(doc, "11. Cronograma de actividades", 1)
    blocos(doc, comp, mod.CRONOGRAMA_TEXTO)
    cronograma(doc, comp)

    N.titulo(doc, "12. Orçamento", 1)
    blocos(doc, comp, mod.ORCAMENTO_TEXTO)
    orcamento(doc, comp)


def cronograma(doc, comp):
    cr = comp.mod.CRONOGRAMA
    ano, mes = cr["inicio"]
    meses = []
    for _ in range(cr["n_meses"]):
        meses.append((ano, MESES[mes - 1]))
        mes += 1
        if mes > 12:
            ano, mes = ano + 1, 1
    num = comp.numeros[("quadro", "cronograma")]
    N.legenda(doc, "Quadro", num, comp.txt(cr.get(
        "titulo", "Cronograma de actividades")))
    comp.elementos.append(("quadro", "cronograma", num, "cronograma"))
    acts = [(comp.txt(t), {i - 1 for i in idx}) for t, idx in cr["actividades"]]
    N.tabela_cronograma(doc, meses, acts)
    N.fonte_elemento(doc, "Fonte: Elaboração própria (2026).")


def mt(valor):
    """1234.5 -> '1.234,50'"""
    s = f"{valor:,.2f}"
    return s.replace(",", "§").replace(".", ",").replace("§", ".")


def orcamento(doc, comp):
    mod = comp.mod
    linhas, total = [], 0.0
    for rub, uni, qtd, cu in mod.ORCAMENTO:
        sub = qtd * cu
        total += sub
        q = mt(qtd).replace(",00", "") if float(qtd).is_integer() else mt(qtd)
        linhas.append([comp.txt(rub), uni, q, mt(cu), mt(sub)])
    imp = g(mod, "ORCAMENTO_IMPREVISTOS", 0.10)
    acento = []
    if imp:
        v = round(total * imp, 2)
        acento.append(len(linhas))
        linhas.append([f"Imprevistos ({int(imp * 100)}% do subtotal)", "", "",
                       "", mt(v)])
        total += v
    linhas.append(["**Total geral**", "", "", "", f"**{mt(total)}**"])
    acento.append(len(linhas) - 1)
    num = comp.numeros[("tabela", "orcamento")]
    N.legenda(doc, "Tabela", num, "Orçamento estimado do estudo, em meticais")
    comp.elementos.append(("tabela", "orcamento", num, "orcamento"))
    N.tabela(doc, ["Rubrica", "Unidade", "Quantidade",
                   "Custo unitário (MT)", "Custo total (MT)"],
             linhas, [5.4, 2.2, 2.4, 3.0, 3.0], linhas_de_acento=acento)
    N.fonte_elemento(doc, "Fonte: Elaboração própria (2026). MT: metical. "
                          "Valores indicativos, a confirmar com fornecedores "
                          "locais à data da execução.")
    comp.total_orcamento = total


def referencias(doc, comp):
    N.titulo(doc, "13. Referências bibliográficas", 1, nova_pagina=True)
    for i, chave in enumerate(comp.bib.ordem, 1):
        N.referencia(doc, i, comp.bib.fontes[chave])


def apendices(doc, comp):
    aps = g(comp.mod, "APENDICES", [])
    N.titulo(doc, "Apêndices", 1, nova_pagina=True)
    for i, (tit, bl) in enumerate(aps):
        letra = "ABCDEFGHIJ"[i]
        N.titulo(doc, f"Apêndice {letra}. {comp.txt(tit)}", 2,
                 nova_pagina=i > 0)
        blocos(doc, comp, bl)


# ==========================================================================
#  principal
# ==========================================================================

def montar(caminho_modulo):
    mod = carregar(caminho_modulo)
    comp = Composicao(mod)
    numerar(comp)
    pasta, saida = pasta_e_ficheiro(mod)
    fig_dir = os.path.join(RAIZ, "_conteudo", "_figuras")
    os.makedirs(fig_dir, exist_ok=True)
    png = os.path.join(fig_dir, f"tema_{mod.NUMERO:02d}_esquema.png")

    doc = N.novo_documento()
    pretextuais(doc, comp)
    seccoes(doc, comp, png)
    n_antes = len(comp.bib.ordem)
    referencias(doc, comp)
    apendices(doc, comp)
    comp.citadas_so_em_apendices = comp.bib.ordem[n_antes:]

    p = doc.core_properties
    p.author = "Estudante de Licenciatura em Farmácia, UniLúrio"
    p.last_modified_by = p.author
    p.title = N.texto_simples(mod.TITULO)
    p.subject = "Protocolo de investigação, Faculdade de Ciências de Saúde"
    p.keywords = "; ".join(mod.PALAVRAS_CHAVE)
    p.comments = ""
    p.category = CATEGORIAS[(mod.NUMERO - 1) // 5 + 1][1]
    doc.save(saida)
    return mod, comp, saida


def relatorio(mod, comp, saida, problemas, avisos, info):
    print("=" * 76)
    print(f"TEMA {mod.NUMERO:02d}: {os.path.relpath(saida, RAIZ)}")
    print("=" * 76)
    for k, v in info.items():
        print(f"  {k:28}: {v}")
    print("-" * 76)
    if problemas:
        print(f"PROBLEMAS ({len(problemas)}):")
        for x in problemas:
            print("  [X]", x)
    else:
        print("PROBLEMAS: nenhum.")
    if avisos:
        print(f"\nAVISOS ({len(avisos)}):")
        for x in avisos:
            print("  [!]", x)
    print("-" * 76)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    caminho = os.path.abspath(sys.argv[1])
    try:
        mod, comp, saida = montar(caminho)
    except (KeyError, ValueError, AttributeError, TypeError) as e:
        print(f"ERRO DE COMPOSICAO: {type(e).__name__}: {e}")
        sys.exit(3)
    problemas, avisos, info = validar(mod, comp, saida)
    relatorio(mod, comp, saida, problemas, avisos, info)
    sys.exit(1 if problemas else 0)
