# -*- coding: utf-8 -*-
"""
Validador de conformidade dos protocolos (norma FCS/UniLurio + padrao de
documentos do utilizador + licoes das auditorias anteriores).

PROBLEMAS bloqueiam a entrega; AVISOS devem ser lidos e resolvidos ou
justificados.
"""
import re
import unicodedata

import docx

import norma as N

SECCOES = [
    "1. INTRODUÇÃO E CONTEXTUALIZAÇÃO",
    "2. IDENTIFICAÇÃO E FORMULAÇÃO DO PROBLEMA E DELIMITAÇÃO",
    "3. OBJECTIVOS", "4. ", "5. JUSTIFICATIVA", "6. REVISÃO DA LITERATURA",
    "7. ESTADO DA ARTE E ESQUEMA CONCEPTUAL", "8. METODOLOGIA",
    "9. RESULTADOS ESPERADOS", "10. DIVULGAÇÃO DOS RESULTADOS",
    "11. CRONOGRAMA DE ACTIVIDADES", "12. ORÇAMENTO",
    "13. REFERÊNCIAS BIBLIOGRÁFICAS", "APÊNDICES",
]

# grafia posterior ao Acordo de 1990 ou brasileira -> forma a usar
GRAFIA = {
    "objetivo": "objectivo", "objetivos": "objectivos", "objetiva": "objectiva",
    "objetivamente": "objectivamente", "atividade": "actividade",
    "atividades": "actividades", "ação": "acção", "ações": "acções",
    "direção": "direcção", "diretor": "director", "diretora": "directora",
    "diretriz": "directriz", "diretrizes": "directrizes", "direto": "directo",
    "direta": "directa", "diretamente": "directamente", "proteção": "protecção",
    "protetor": "protector", "infeção": "infecção", "infeções": "infecções",
    "infecioso": "infeccioso", "infeciosa": "infecciosa",
    "infeciosas": "infecciosas", "infeciosos": "infecciosos",
    "infetado": "infectado", "infetados": "infectados", "fator": "factor",
    "fatores": "factores", "setor": "sector", "setores": "sectores",
    "contato": "contacto", "contatos": "contactos", "correto": "correcto",
    "correta": "correcta", "corretamente": "correctamente",
    "incorreto": "incorrecto", "incorreta": "incorrecta", "efetivo": "efectivo",
    "efetiva": "efectiva", "efetividade": "efectividade", "efetuar": "efectuar",
    "efetuado": "efectuado", "ativo": "activo", "ativa": "activa",
    "ativos": "activos", "ativas": "activas", "inativo": "inactivo",
    "atual": "actual", "atuais": "actuais", "atualmente": "actualmente",
    "atualizado": "actualizado", "atualização": "actualização",
    "projeto": "projecto", "projetos": "projectos", "detetar": "detectar",
    "deteção": "detecção", "detetado": "detectado", "detetados": "detectados",
    "detetada": "detectada", "detetadas": "detectadas", "seleção": "selecção",
    "selecionar": "seleccionar", "selecionado": "seleccionado",
    "selecionados": "seleccionados", "selecionada": "seleccionada",
    "selecionadas": "seleccionadas", "respetivo": "respectivo",
    "respetiva": "respectiva", "respetivos": "respectivos",
    "respetivas": "respectivas", "respetivamente": "respectivamente",
    "perspetiva": "perspectiva", "ótimo": "óptimo", "ótima": "óptima",
    "ótimos": "óptimos", "receção": "recepção", "conceção": "concepção",
    "perceção": "percepção", "espetro": "espectro", "aspeto": "aspecto",
    "aspetos": "aspectos", "exceto": "excepto", "exceção": "excepção",
    "adoção": "adopção", "adotar": "adoptar", "adotado": "adoptado",
    "adotada": "adoptada", "adotados": "adoptados", "reação": "reacção",
    "reações": "reacções", "reativo": "reactivo", "reativos": "reactivos",
    "reagente": "reagente", "exato": "exacto", "exata": "exacta",
    "exatidão": "exactidão", "eletrónico": "electrónico",
    "eletrónica": "electrónica", "eletrónicos": "electrónicos",
    "elétrico": "eléctrico", "elétrica": "eléctrica", "extrato": "extracto",
    "extratos": "extractos", "extração": "extracção", "fração": "fracção",
    "frações": "fracções", "fracionado": "fraccionado", "coletivo": "colectivo",
    "coleta": "recolha", "coletar": "recolher", "ótica": "óptica",
    "ótico": "óptico", "antirretroviral": "anti-retroviral",
    "antirretrovirais": "anti-retrovirais", "antisséptico": "anti-séptico",
    "antissépticos": "anti-sépticos", "antisséptica": "anti-séptica",
    "antissépticas": "anti-sépticas", "autoadministração": "auto-administração",
    "automedicação": "automedicação", "coinfecção": "co-infecção",
    "semiestruturada": "semi-estruturada",
    "semiestruturadas": "semi-estruturadas",
    "semiquantitativa": "semiquantitativa", "equipe": "equipa",
    "equipes": "equipas", "registro": "registo", "registros": "registos",
    "usuário": "utente/utilizador", "usuários": "utentes/utilizadores",
    "treinamento": "formação", "gerenciamento": "gestão",
    "celular": "telemóvel", "geladeira": "frigorífico", "câncer": "cancro",
    "planilha": "folha de cálculo", "banheiro": "casa de banho",
    "de fato": "de facto", "caraterística": "característica",
    "caraterísticas": "características", "caraterizar": "caracterizar",
    "facto": "facto", "espetrofotometria": "espectrofotometria",
    "espetrofotómetro": "espectrofotómetro", "anti-inflamatório":
    "anti-inflamatório", "ótimos": "óptimos", "tato": "tacto",
}

CLICHES_PROBLEMA = [
    "vale ressaltar", "vale a pena ressaltar", "é importante notar",
    "é importante ressaltar", "é importante salientar", "importa salientar",
    "em suma", "mergulhar", "de suma importância", "cabe destacar",
    "no cenário actual", "no cenário atual", "desempenha um papel crucial",
    "papel crucial", "neste contexto dinâmico", "ademais", "outrossim",
]
CLICHES_AVISO = ["robusto", "robusta", "holístic", "sinergia", "alavancar",
                 "potencializar", "crucial", "abrangente", "multifacetad"]

CARACTERES = {"—": "travessão", "–": "traço médio",
              "−": "sinal menos tipográfico", "→": "seta",
              "←": "seta", "⇒": "seta", "≈": "aproximadamente",
              "…": "reticências tipográficas", "•": "marca manual",
              "“": "aspas inglesas", "”": "aspas inglesas",
              "―": "barra horizontal", "‒": "traço numérico"}

GENEROS = ["Staphylococcus", "Escherichia", "Klebsiella", "Pseudomonas",
           "Streptococcus", "Enterococcus", "Enterobacter", "Proteus",
           "Salmonella", "Shigella", "Candida", "Aspergillus", "Plasmodium",
           "Mycobacterium", "Anopheles", "Aedes", "Culex", "Moringa",
           "Chlamydia", "Acinetobacter", "Bacillus", "Vibrio", "Artemisia",
           "Anacardium", "Manihot", "Cocos", "Citrus", "Aloe", "Cassia",
           "Vernonia", "Azadirachta", "Carica", "Psidium", "Burkholderia",
           "Clostridium", "Clostridioides", "Neisseria", "Haemophilus",
           "Treponema", "Trichomonas", "Helicobacter", "Serratia",
           "Citrobacter", "Morganella", "Micrococcus", "Corynebacterium",
           "Lactobacillus", "Penicillium", "Mucor", "Rhizopus", "Zea",
           "Ocimum", "Cymbopogon", "Eucalyptus", "Tamarindus", "Adansonia",
           "Zingiber", "Allium", "Curcuma", "Momordica", "Senna", "Ricinus"]

MESES = ("janeiro|fevereiro|março|abril|maio|junho|julho|agosto|setembro|"
         "outubro|novembro|dezembro")


def _ascii(t):
    return unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode()


def texto_docx(d):
    partes = [p.text for p in d.paragraphs]
    for t in d.tables:
        for linha in t.rows:
            vistas = set()
            for c in linha.cells:
                if id(c._tc) in vistas:
                    continue
                vistas.add(id(c._tc))
                partes.append(c.text)
    return "\n".join(partes)


def strings_do_modulo(mod):
    """Todas as cadeias de texto do modulo (para verificar a marcacao)."""
    fora = {"FONTES", "SEMINAIS"}
    out = []

    def rec(x, onde):
        if isinstance(x, str):
            out.append((onde, x))
        elif isinstance(x, dict):
            for k, v in x.items():
                rec(v, onde)
        elif isinstance(x, (list, tuple)):
            for v in x:
                rec(v, onde)
    for nome in dir(mod):
        if nome.isupper() and nome not in fora:
            rec(getattr(mod, nome), nome)
    return out


def _palavras(t):
    return len(re.findall(r"\b\w[\w\-]*\b", N.texto_simples(t)))


def _ano_ref(ref):
    r = re.sub(r"\[citado[^\]]*\]", "", ref)
    r = re.sub(r"(doi:\S+|https?://\S+|PMID:\s*\d+)", "", r)
    anos = re.findall(r"\b((?:19|20)\d{2})(?=[;.\s\[:,)]|$)", r)
    return int(anos[-1]) if anos else None


# --------------------------------------------------------------------------

def validar(mod, comp, saida):
    P, A = [], []
    d = docx.Document(saida)
    txt = texto_docx(d)
    baixo = txt.lower()

    # paragrafos (sem titulos) por zona do documento
    zonas = {"pre": [], "corpo": [], "refs": [], "apend": []}
    zona = "pre"
    for p in d.paragraphs:
        est = p.style.name
        if est == "Heading 1":
            t1 = p.text.strip().upper()
            if t1.startswith("1. INTRODU"):
                zona = "corpo"
            elif t1.startswith("13. REFER"):
                zona = "refs"
            elif t1.startswith("APÊNDICES"):
                zona = "apend"
        if est.startswith(("Heading", "TOC")):
            continue
        zonas[zona].append(p.text)
    sem_tit = "\n".join(zonas["corpo"])
    texto_tabelas = "\n".join(texto_docx(d).split("\n")[len(d.paragraphs):])
    # ---------------------------------------------------------- formato --
    s = d.sections[0]
    if (round(s.top_margin.cm, 1), round(s.left_margin.cm, 1)) != (3.0, 2.5):
        P.append("Margens fora da norma (3/3/2,5/2,5 cm).")
    if round(s.page_width.cm, 1) != 21.0:
        P.append("Página diferente de A4.")

    # --------------------------------------------------------- estrutura --
    tit1 = [p.text.strip() for p in d.paragraphs
            if p.style.name == "Heading 1"]
    pos = 0
    for sec in SECCOES:
        achou = False
        for i in range(pos, len(tit1)):
            if tit1[i].upper().startswith(sec):
                pos, achou = i + 1, True
                break
        if not achou:
            P.append(f"Secção obrigatória em falta ou fora de ordem: {sec}")
    vazias = []
    pars = d.paragraphs
    for i, p in enumerate(pars):
        if not p.style.name.startswith("Heading"):
            continue
        seguinte = next((q for q in pars[i + 1:] if q.text.strip() or
                         q._p.xpath(".//w:drawing")), None)
        corpo_tab = p._p.getnext() is not None and \
            p._p.getnext().tag.endswith("tbl")
        if seguinte is None and not corpo_tab:
            vazias.append(p.text[:50])
        elif seguinte is not None and seguinte.style.name.startswith(
                "Heading") and not corpo_tab:
            nv_a = int(re.sub(r"\D", "", p.style.name) or 9)
            nv_b = int(re.sub(r"\D", "", seguinte.style.name) or 9)
            if nv_b <= nv_a:
                vazias.append(p.text[:50])
    if vazias:
        P.append(f"Secções sem conteúdo: {vazias}")

    # ---------------------------------------------------- resumo/abstract --
    for nome, texto, lim in (("Resumo", mod.RESUMO, (250, 300)),
                             ("Abstract", mod.ABSTRACT, (230, 320))):
        n = _palavras(texto)
        if not lim[0] <= n <= lim[1]:
            P.append(f"{nome} com {n} palavras (norma: 250 a 300).")
        if "\n" in texto.strip():
            P.append(f"{nome} deve ser um parágrafo único.")
        if re.search(r"\{[a-z0-9_]+\}|\(\d+(?:[,\-]\d+)*\)", texto):
            P.append(f"{nome} contém citações (a norma proíbe).")
        siglas = sorted(set(re.findall(r"\b[A-Z][A-Z0-9]{1,}[a-z]?\b",
                                       N.texto_simples(texto))))
        if siglas:
            P.append(f"{nome} contém abreviaturas ou siglas {siglas} "
                     f"(a norma proíbe; escrever por extenso).")
    for nome, pal in (("Palavras-chave", mod.PALAVRAS_CHAVE),
                      ("Keywords", mod.KEYWORDS)):
        if not 3 <= len(pal) <= 5:
            P.append(f"{nome}: {len(pal)} termos (norma: 3 a 5).")
        ordenadas = sorted(pal, key=lambda x: _ascii(x).lower())
        if list(pal) != ordenadas:
            P.append(f"{nome} fora da ordem alfabética: {ordenadas}")

    # ------------------------------------------------------- objectivos --
    oe = mod.OBJECTIVOS_ESPECIFICOS
    if not 3 <= len(oe) <= 5:
        P.append(f"{len(oe)} objectivos específicos (norma: 3 a 5).")
    for o in [mod.OBJECTIVO_GERAL] + list(oe):
        v = o.split()[0].lower()
        if not re.search(r"(ar|er|ir|or)$", v):
            P.append(f"Objectivo sem verbo no infinitivo: '{o[:60]}'")
    hip = getattr(mod, "HIPOTESES", [])
    if hip:
        rots = [h[0] for h in hip]
        if not any("H0" in r or "H<sub>0" in r for r in rots):
            P.append("Hipóteses sem hipótese nula (H0).")
    elif not getattr(mod, "QUESTOES", []):
        P.append("Sem hipóteses nem questões de investigação.")

    # quadro de variaveis ligado aos objectivos
    var = [b for b in _todos_blocos(mod)
           if b.get("tipo") == "tabela" and b.get("chave") == "variaveis"]
    if not var:
        P.append("Falta o quadro de variáveis com chave 'variaveis'.")
    else:
        cab = [c.lower() for c in var[0]["cabecalho"]]
        col = next((j for j, c in enumerate(cab) if "objectivo" in c), None)
        if col is None:
            P.append("O quadro 'variaveis' não tem a coluna 'Objectivo'.")
        else:
            usados = set()
            for l in var[0]["linhas"]:
                usados |= {int(x) for x in re.findall(r"\d+", str(l[col]))}
            falta = [i for i in range(1, len(oe) + 1) if i not in usados]
            if falta:
                P.append(f"Objectivos específicos sem variável no quadro "
                         f"'variaveis': {falta}")
    if not any(b.get("tipo") == "tabela" and b.get("chave") == "limitacoes"
               for b in _todos_blocos(mod)):
        P.append("Falta o quadro de limitações e mitigação (chave "
                 "'limitacoes').")

    # metodologia
    tit_met = " | ".join(t for t, _ in mod.METODOLOGIA).lower()
    for rot, padroes in (("tipo/desenho", "tipo|desenho"),
                         ("local e período", "local"),
                         ("população ou material", "popula|material|amostras"),
                         ("amostra e cálculo", "amostra|dimens|tamanho"),
                         ("critérios", "critério"),
                         ("variáveis", "variáve"),
                         ("instrumentos ou métodos", "instrumento|método|ensaio"),
                         ("recolha", "recolha|procedimento"),
                         ("análise", "análise"),
                         ("limitações", "limita"),
                         ("ética", "étic")):
        if not re.search(padroes, tit_met):
            P.append(f"Metodologia sem subsecção de {rot}.")

    # ------------------------------------------------------ caracteres --
    for ch, nome in CARACTERES.items():
        if ch in txt:
            i = txt.index(ch)
            P.append(f"Carácter proibido ({nome}) em: "
                     f"...{txt[max(0, i - 40):i + 20]}...")
    if re.search(r"[\U0001F300-\U0001FAFF☀-➿]", txt):
        P.append("Emojis ou símbolos decorativos no texto.")
    if "**" in txt or re.search(r"\{[a-z0-9_]+\}|\[\[", txt):
        P.append("Marcação por resolver no documento (**, {chave} ou [[ ]]).")

    # ---------------------------------------------------------- grafia --
    corpo = txt.split("13. REFERÊNCIAS BIBLIOGRÁFICAS")[0] + "\n" + \
        (txt.split("APÊNDICES")[-1] if "APÊNDICES" in txt else "")
    cb = corpo.lower()
    for errado, certo in GRAFIA.items():
        if errado == certo:
            continue
        for m in re.finditer(r"(?<![\w-])" + re.escape(errado) + r"(?![\w-])",
                             cb):
            ctx = corpo[max(0, m.start() - 35):m.end() + 25].replace("\n", " ")
            P.append(f"Grafia '{errado}' (usar '{certo}'): ...{ctx}...")
            break
    for m in re.finditer(r"\b\w*ô[mn]\w*\b|\b\w+ê[mn]ic[oa]s?\b", cb):
        if m.group(0) not in ("cônjuge", "cônjuges"):
            P.append(f"Grafia brasileira '{m.group(0)}' (usar acento agudo).")
    for m in re.finditer(r"\b(?:de|em|a|até|desde) (" + MESES + r")\b", corpo):
        P.append(f"Mês em minúscula ('{m.group(0)}'): na grafia anterior ao "
                 f"Acordo os meses escrevem-se com maiúscula.")
        break
    for c in CLICHES_PROBLEMA:
        if c in cb:
            P.append(f"Expressão típica de texto gerado: '{c}'.")
    for c in CLICHES_AVISO:
        n = cb.count(c)
        if n >= 2:
            A.append(f"'{c}' aparece {n} vezes: rever o estilo.")

    # ----------------------------------------------- marcacao no modulo --
    for onde, s_ in strings_do_modulo(mod):
        if onde not in ("APENDICES",) and "**" in s_ and not onde.startswith(
                ("ORCAMENTO",)):
            if not _em_celula(mod, s_):
                P.append(f"Negrito dentro de parágrafo ({onde}): "
                         f"'{s_[:60]}...'")
        for gen in GENEROS:
            for m in re.finditer(r"(?<![\*\w])" + gen + r"\b", s_):
                antes = s_[max(0, m.start() - 1):m.start()]
                if antes != "*":
                    P.append(f"Nome científico sem itálico em {onde}: "
                             f"'{s_[m.start():m.start() + 40]}'")
                    break

    # ---------------------------------------------------- referencias --
    bib = comp.bib
    nao = bib.nao_citadas()
    if nao:
        P.append(f"Referências em FONTES nunca citadas: {nao}")
    if comp.citadas_so_em_apendices:
        P.append(f"Referências citadas pela primeira vez nos apêndices "
                 f"(citar no corpo): {comp.citadas_so_em_apendices}")
    n_ref = len(bib.ordem)
    if n_ref < 30:
        P.append(f"Apenas {n_ref} referências (mínimo 30).")
    antigas, sem_ano, dois, titulos = [], [], {}, {}
    seminais = getattr(mod, "SEMINAIS", {})
    for k in bib.ordem:
        ref = bib.fontes[k]
        if not re.search(r"doi:10\.|PMID:\s*\d|https?://", ref):
            P.append(f"Referência sem DOI, PMID ou URL: {k}")
        for ch in ("—", "–", "−"):
            if ch in ref:
                P.append(f"Referência com travessão: {k}")
        ano = _ano_ref(ref)
        if ano is None:
            sem_ano.append(k)
        elif ano < 2016:
            antigas.append(k)
            if k not in seminais:
                P.append(f"Referência anterior a 2016 sem justificação em "
                         f"SEMINAIS: {k} ({ano})")
        m = re.search(r"doi:\s*(10\.\S+?)(?:\.?\s+PMID|\.?\s*$)", ref)
        if m:
            dd = m.group(1).rstrip(".").lower()
            if dd in dois:
                P.append(f"DOI duplicado: {k} e {dois[dd]}")
            dois[dd] = k
        tt = _ascii(ref.split(". ")[1] if ". " in ref else ref).lower()[:80]
        if tt in titulos and len(tt) > 25:
            P.append(f"Título possivelmente duplicado: {k} e {titulos[tt]}")
        titulos[tt] = k
    if n_ref and len(antigas) / n_ref > 0.2:
        P.append(f"{len(antigas)} de {n_ref} referências anteriores a 2016 "
                 f"(máximo 20%).")
    if sem_ano:
        A.append(f"Referências sem ano identificável: {sem_ano}")
    for k, motivo in seminais.items():
        if k in bib.ordem and not motivo.strip():
            P.append(f"SEMINAIS[{k}] sem motivo.")

    # ordem de citacao no corpo (so paragrafos; por construcao ja' e' certa)
    corpo_ref = sem_tit
    vistos, maximo, saltos = set(), 0, 0
    for m in re.finditer(r"\((\d+(?:[,\-]\d+)*)\)", corpo_ref):
        nums = []
        for parte in m.group(1).split(","):
            a, _, b = parte.partition("-")
            nums += list(range(int(a), int(b or a) + 1))
        if not nums or max(nums) > n_ref:
            continue
        for x in nums:
            if x not in vistos:
                if x != maximo + 1:
                    saltos += 1
                vistos.add(x)
                maximo = max(maximo, x)
    if saltos:
        A.append(f"{saltos} números de citação fora da ordem de primeira "
                 f"aparição (verificar parênteses com números que não sejam "
                 f"citações).")

    # -------------------------------------------- quadros, tabelas, figura --
    for (tipo, chave), numero in comp.numeros.items():
        if (tipo, chave) not in comp.referidos:
            P.append(f"{tipo.capitalize()} {numero} ('{chave}') sem remissão "
                     f"no texto (usar [[{tipo}:{chave}]]).")

    # -------------------------------------------------------- siglas --
    corpo_sig = sem_tit + "\n" + "\n".join(zonas["apend"]) + "\n" + \
        texto_tabelas
    listadas = {s_ for s_, _ in mod.ABREVIATURAS}
    for s_ in listadas:
        padrao = r"(?<![\w-])" + re.escape(s_) + r"(?![\w-])"
        ocorr = list(re.finditer(padrao, corpo_sig))
        if not ocorr:
            P.append(f"Sigla '{s_}' na lista mas não usada no texto.")
            continue
        i = ocorr[0].start()
        janela = corpo_sig[max(0, i - 2):i + len(s_) + 2]
        if "(" not in janela and ")" not in janela:
            A.append(f"Primeira ocorrência de '{s_}' sem a forma extensa "
                     f"seguida da sigla entre parênteses: "
                     f"...{corpo_sig[max(0, i - 60):i + 20]}...")
    candidatas = set(re.findall(r"(?<![\w-])([A-Z][A-Z0-9]{1,7}[a-z]?)"
                                r"(?![\w-])", corpo_sig))
    ignorar = {"II", "III", "IV", "VI", "VII", "VIII", "IX", "XI", "XII",
               "OE", "H0", "H1", "MT", "UV", "CD", "TCC", "N.º"}
    em_falta = sorted(c for c in candidatas - listadas - ignorar
                      if not re.fullmatch(r"[IVX]+|[A-Z]\d", c))
    if em_falta:
        A.append(f"Possíveis siglas usadas mas não listadas: {em_falta[:25]}")

    # ------------------------------------------------------ extensao --
    txt_corpo = txt.split("1. INTRODUÇÃO E CONTEXTUALIZAÇÃO", 1)[-1]
    txt_corpo = txt_corpo.split("13. REFERÊNCIAS BIBLIOGRÁFICAS")[0]
    n_pal = len(re.findall(r"\b\w[\w\-]*\b", txt_corpo))
    if n_pal < 6500:
        P.append(f"Corpo (secções 1 a 12) com {n_pal} palavras: abaixo do "
                 f"mínimo de 6.500 para um protocolo completo.")
    elif n_pal > 12000:
        P.append(f"Corpo (secções 1 a 12) com {n_pal} palavras: acima do "
                 f"máximo de 12.000 (alvo 7.500 a 10.000). Condensar.")
    elif n_pal > 10500:
        A.append(f"Corpo com {n_pal} palavras: acima do alvo de 10.000.")
    aps = getattr(mod, "APENDICES", [])
    if len(aps) < 2:
        P.append("Menos de dois apêndices (instrumento e consentimento ou "
                 "pedido de autorização, no mínimo).")
    tit_aps = " ".join(t.lower() for t, _ in aps)
    if not re.search(r"consentimento|dispensa|autoriza", tit_aps):
        P.append("Nenhum apêndice de consentimento, dispensa ou autorização.")
    for m in re.findall(r"\[(?:preencher|confirmar)[^\]]{0,160}\]", txt, re.I):
        A.append(f"Por preencher/confirmar: {m[:120]}")
    if n_pal and len(re.findall(r"\[(?:preencher|confirmar)", txt, re.I)) > 25:
        A.append("Muitos marcadores [preencher]/[confirmar]: reduzir ao "
                 "indispensável (nomes, contactos, números institucionais).")

    txt_dec = sem_tit.split("13. REFERÊNCIAS BIBLIOGRÁFICAS")[0]
    for m in re.finditer(r"(?<![\d.,])\d{1,3}\.\d{1,2}(?![\d.])", txt_dec):
        ctx = txt_dec[max(0, m.start() - 30):m.start()]
        if re.search(r"(secção|Secção|subsecção|versão|item|pontos?|"
                     r"Apêndice|apêndice|\d\.)\s*$", ctx):
            continue
        A.append(f"Separador decimal suspeito '{m.group(0)}': "
                 f"...{txt_dec[max(0, m.start() - 30):m.end() + 15]}...")
        break

    info = {
        "palavras no corpo (1-12)": n_pal,
        "referencias citadas": n_ref,
        "referencias < 2016": len(antigas),
        "quadros/tabelas/figuras": len(comp.numeros),
        "objectivos especificos": len(oe),
        "apendices": len(aps),
        "orcamento total (MT)": f"{getattr(comp, 'total_orcamento', 0):,.2f}",
        "palavras resumo/abstract": f"{_palavras(mod.RESUMO)} / "
                                    f"{_palavras(mod.ABSTRACT)}",
    }
    return P, A, info


def _todos_blocos(mod):
    import motor
    return [b for b in motor.sequencia_blocos(mod) if isinstance(b, dict)]


def _em_celula(mod, s_):
    for b in _todos_blocos(mod):
        if b.get("tipo") == "tabela":
            for l in b["linhas"]:
                if s_ in [str(c) for c in l]:
                    return True
    return False
