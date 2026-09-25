# -*- coding: utf-8 -*-
"""
Ferramenta de referencias: pesquisa, formatacao Vancouver a partir dos
metadados reais (PubMed / Crossref / doi.org) e verificacao.

Nunca escrever os metadados de um artigo a' mao: gerar sempre com esta
ferramenta e colar a linha devolvida no dicionario FONTES do modulo.

Uso:
  python refs.py buscar "antibiotic prescribing children Africa" [--n 20] [--desde 2016]
  python refs.py doi 10.1186/s12960-023-00812-w [outro_doi ...]
  python refs.py pmid 36912345 [outro_pmid ...]
  python refs.py resumo <PMID ou DOI>          # imprime o abstract (para confirmar dados)
  python refs.py url https://www.who.int/...   # verifica se o endereco responde e mostra o titulo
  python refs.py web --autor "World Health Organization" --titulo "..." \
        --local Geneva --editora "World Health Organization" --ano 2019 --url URL
  python refs.py verificar ../_conteudo/tema_06.py   # confere todas as FONTES
"""
import argparse
import difflib
import hashlib
import html
import importlib.util
import json
import os
import random
import re
import sys
import time
import unicodedata

import requests

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

AQUI = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(AQUI, "_cache")
os.makedirs(CACHE, exist_ok=True)
UA = {"User-Agent": "Mozilla/5.0 (protocolos-tcc-unilurio; referencias)"}
EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
HOJE = "2026 Set 19"
MESES_PT = {"Jan": "Jan", "Feb": "Fev", "Mar": "Mar", "Apr": "Abr",
            "May": "Mai", "Jun": "Jun", "Jul": "Jul", "Aug": "Ago",
            "Sep": "Set", "Oct": "Out", "Nov": "Nov", "Dec": "Dez"}


# --------------------------------------------------------------------------
# rede, com cache e repeticao
# --------------------------------------------------------------------------

def _cache_get(chave):
    f = os.path.join(CACHE, hashlib.sha1(chave.encode()).hexdigest() + ".json")
    if os.path.exists(f):
        try:
            with open(f, encoding="utf-8") as fh:
                return json.load(fh)
        except (OSError, ValueError):
            return None
    return None


def _cache_put(chave, valor):
    f = os.path.join(CACHE, hashlib.sha1(chave.encode()).hexdigest() + ".json")
    tmp = f + f".{os.getpid()}.tmp"
    try:
        with open(tmp, "w", encoding="utf-8") as fh:
            json.dump(valor, fh)
        os.replace(tmp, f)
    except OSError:
        pass


def obter(url, params=None, headers=None, json_resp=True, usar_cache=True,
          tentativas=7):
    chave = url + "?" + json.dumps(params or {}, sort_keys=True) + str(headers)
    if usar_cache:
        c = _cache_get(chave)
        if c is not None:
            return c
    h = dict(UA)
    h.update(headers or {})
    espera = 1.0
    ultimo = None
    for _ in range(tentativas):
        try:
            r = requests.get(url, params=params, headers=h, timeout=40)
            if r.status_code == 429 or r.status_code >= 500:
                ultimo = f"HTTP {r.status_code}"
                time.sleep(espera + random.random())
                espera *= 2
                continue
            if r.status_code == 404:
                return None
            r.raise_for_status()
            valor = r.json() if json_resp else r.text
            if usar_cache:
                _cache_put(chave, valor)
            return valor
        except (requests.RequestException, ValueError) as e:
            ultimo = str(e)[:120]
            time.sleep(espera + random.random())
            espera *= 2
    raise RuntimeError(f"Falha ao obter {url}: {ultimo}")


# --------------------------------------------------------------------------
# PubMed
# --------------------------------------------------------------------------

def pubmed_resumos(pmids):
    pmids = [str(p) for p in pmids]
    if not pmids:
        return {}
    d = obter(EUTILS + "esummary.fcgi",
              {"db": "pubmed", "id": ",".join(pmids), "retmode": "json"})
    res = (d or {}).get("result", {})
    return {p: res[p] for p in pmids if p in res}


def pubmed_procurar(termo, n=20, desde=None):
    params = {"db": "pubmed", "term": termo, "retmode": "json",
              "retmax": n, "sort": "relevance"}
    if desde:
        params.update({"mindate": str(desde), "maxdate": "2026",
                       "datetype": "pdat"})
    d = obter(EUTILS + "esearch.fcgi", params)
    return (d or {}).get("esearchresult", {}).get("idlist", [])


def pmid_por_doi(doi):
    ids = pubmed_procurar(f"{doi}[doi]", n=2)
    return ids[0] if len(ids) == 1 else None


def _doi_de(s):
    for a in s.get("articleids", []):
        if a.get("idtype") == "doi":
            return a.get("value")
    return None


def _limpar(t):
    t = html.unescape(re.sub(r"<[^>]+>", "", t or "")).strip()
    return re.sub(r"\s+", " ", t)


def _autores_pubmed(s):
    nomes = [a["name"] for a in s.get("authors", [])
             if a.get("authtype", "Author") == "Author" and a.get("name")]
    if not nomes:
        col = s.get("lastauthor") or ""
        return col
    if len(nomes) > 6:
        return ", ".join(nomes[:6]) + ", et al"
    return ", ".join(nomes)


def vancouver_pubmed(s):
    autores = _autores_pubmed(s)
    titulo = _limpar(s.get("title", "")).rstrip(".")
    revista = _limpar(s.get("source", ""))
    ano = (s.get("pubdate") or s.get("epubdate") or "")[:4]
    vol, num, pag = s.get("volume", ""), s.get("issue", ""), s.get("pages", "")
    loc = ano
    if vol:
        loc += f";{vol}"
        if num:
            loc += f"({num})"
    if pag:
        loc += f":{pag}"
    doi = _doi_de(s)
    partes = [f"{autores}." if autores else "", f"{titulo}.", f"{revista}.",
              f"{loc}."]
    ref = " ".join(p for p in partes if p)
    if doi:
        ref += f" doi:{doi}"
    ref += f" PMID: {s.get('uid')}."
    if doi:
        ref = ref.replace(f" doi:{doi} PMID", f" doi:{doi}. PMID")
    return _sem_travessoes(ref)


# --------------------------------------------------------------------------
# Crossref / doi.org
# --------------------------------------------------------------------------

def crossref(doi):
    d = obter(f"https://api.crossref.org/works/{doi}")
    if d and d.get("message"):
        return d["message"]
    try:
        return obter(f"https://doi.org/{doi}",
                     headers={"Accept": "application/vnd.citationstyles.csl+json"})
    except RuntimeError:
        return None


def _iniciais(dado):
    partes = re.split(r"[\s\-\.]+", dado or "")
    return "".join(p[0].upper() for p in partes if p and p[0].isalpha())


def _autores_crossref(m):
    nomes = []
    for a in m.get("author", []) or []:
        if a.get("family"):
            fam = a["family"].strip()
            if fam.isupper():
                fam = fam.title()
            nomes.append(f"{fam} {_iniciais(a.get('given', ''))}".strip())
        elif a.get("name"):
            nomes.append(a["name"].strip())
        elif a.get("literal"):
            nomes.append(a["literal"].strip())
    if len(nomes) > 6:
        return ", ".join(nomes[:6]) + ", et al"
    return ", ".join(nomes)


def _ano_crossref(m):
    for campo in ("published-print", "published-online", "issued", "published",
                  "created"):
        dp = (m.get(campo) or {}).get("date-parts")
        if dp and dp[0] and dp[0][0]:
            return str(dp[0][0])
    return ""


def _primeiro(v):
    if isinstance(v, list):
        return v[0] if v else ""
    return v or ""


def vancouver_crossref(m, doi):
    autores = _autores_crossref(m)
    titulo = _limpar(_primeiro(m.get("title"))).rstrip(".")
    revista = _limpar(_primeiro(m.get("short-container-title"))
                      or _primeiro(m.get("container-title"))
                      or _primeiro(m.get("container-title-short")))
    ano = _ano_crossref(m)
    vol = m.get("volume", "")
    num = m.get("issue", "")
    pag = m.get("page", "") or m.get("article-number", "")
    tipo = m.get("type", "")
    if tipo in ("book", "monograph", "report", "book-chapter") or not revista:
        editora = m.get("publisher", "")
        ref = f"{autores + '. ' if autores else ''}{titulo}. "
        if tipo == "book-chapter" and revista:
            ref += f"In: {revista}. "
        ref += f"{editora}; {ano}. doi:{doi}"
        return _sem_travessoes(ref)
    loc = ano
    if vol:
        loc += f";{vol}"
        if num:
            loc += f"({num})"
    if pag:
        loc += f":{pag}"
    ref = f"{autores + '. ' if autores else ''}{titulo}. {revista}. {loc}. doi:{doi}"
    return _sem_travessoes(ref)


def _sem_travessoes(t):
    return (t.replace("—", ", ").replace("–", "-")
            .replace("−", "-").replace("‐", "-")
            .replace("‑", "-").replace(" ", " "))


# --------------------------------------------------------------------------
# chaves e formatos
# --------------------------------------------------------------------------

def _ascii(t):
    return unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode()


def chave_sugerida(ref):
    m = re.match(r"\s*([^\s,]+)", ref)
    apelido = _ascii(m.group(1)).lower() if m else "ref"
    apelido = re.sub(r"[^a-z]", "", apelido)[:14] or "ref"
    anos = re.findall(r"\b((?:19|20)\d{2})\b", ref.split("doi:")[0])
    return f"{apelido}{anos[-1] if anos else ''}"


def linha_fontes(ref, chave=None):
    chave = chave or chave_sugerida(ref)
    return f'    "{chave}": "{ref.replace(chr(34), chr(39))}",'


def ref_por_doi(doi):
    doi = doi.strip().replace("https://doi.org/", "").replace("doi:", "")
    pmid = pmid_por_doi(doi)
    if pmid:
        s = pubmed_resumos([pmid]).get(pmid)
        if s and (_doi_de(s) or "").lower() == doi.lower():
            return vancouver_pubmed(s), "PubMed"
    m = crossref(doi)
    if not m:
        return None, "DOI nao encontrado"
    return vancouver_crossref(m, doi), "Crossref"


# --------------------------------------------------------------------------
# comandos
# --------------------------------------------------------------------------

def cmd_buscar(a):
    ids = pubmed_procurar(a.termo, a.n, a.desde)
    if not ids:
        print("Sem resultados.")
        return
    res = pubmed_resumos(ids)
    for p in ids:
        s = res.get(p)
        if not s:
            continue
        ano = (s.get("pubdate") or "")[:4]
        prim = (s.get("authors") or [{}])[0].get("name", "")
        print(f"PMID {p} | {ano} | {prim} | {_limpar(s.get('title'))[:150]} | "
              f"{s.get('source')} | doi:{_doi_de(s) or '-'}")


def cmd_doi(a):
    for doi in a.dois:
        ref, origem = ref_por_doi(doi)
        if not ref:
            print(f"# {doi}: {origem}")
            continue
        print(f"# origem: {origem}")
        print(linha_fontes(ref))


def cmd_pmid(a):
    res = pubmed_resumos(a.pmids)
    for p in a.pmids:
        s = res.get(str(p))
        if not s:
            print(f"# PMID {p}: nao encontrado")
            continue
        print(linha_fontes(vancouver_pubmed(s)))


def cmd_resumo(a):
    ident = a.ident.strip()
    pmid = ident if ident.isdigit() else pmid_por_doi(ident)
    if pmid:
        txt = obter(EUTILS + "efetch.fcgi",
                    {"db": "pubmed", "id": pmid, "rettype": "abstract",
                     "retmode": "text"}, json_resp=False)
        print(txt)
        return
    m = crossref(ident)
    if m and m.get("abstract"):
        print(_limpar(_primeiro(m.get("title"))))
        print(_limpar(m["abstract"]))
    else:
        print("Resumo nao disponivel por API. Ler o texto em "
              f"https://doi.org/{ident} (WebFetch).")


def estado_url(url):
    try:
        r = requests.get(url, headers=UA, timeout=40, allow_redirects=True)
        titulo = ""
        if "html" in r.headers.get("Content-Type", ""):
            m = re.search(r"<title[^>]*>(.*?)</title>", r.text, re.I | re.S)
            titulo = _limpar(m.group(1))[:160] if m else ""
        return r.status_code, titulo, r.url
    except requests.RequestException as e:
        return None, str(e)[:120], url


def cmd_url(a):
    cod, titulo, final = estado_url(a.url)
    print(f"HTTP {cod} | {titulo} | {final}")


def cmd_web(a):
    ref = (f"{a.autor}. {a.titulo} [Internet]. {a.local}: {a.editora}; "
           f"{a.ano} [citado {HOJE}]. Disponível em: {a.url}")
    cod, titulo, _ = estado_url(a.url)
    print(f"# HTTP {cod} | {titulo}")
    print(linha_fontes(_sem_travessoes(ref), a.chave))


# --------------------------------------------------------------------------
# verificacao de um modulo de tema
# --------------------------------------------------------------------------

def _norm(t):
    t = _ascii(_limpar(t)).lower()
    return re.sub(r"[^a-z0-9 ]", " ", t)


def _titulo_confere(titulo_real, ref):
    a, b = _norm(titulo_real).split(), _norm(ref)
    palavras = [w for w in a if len(w) > 3]
    if not palavras:
        return True
    presentes = sum(1 for w in palavras if f" {w} " in f" {b} ")
    return presentes / len(palavras) >= 0.8


def carregar_fontes(caminho):
    sys.path.insert(0, AQUI)
    spec = importlib.util.spec_from_file_location("tema_verif", caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.FONTES


def verificar_ref(chave, ref):
    """Devolve (estado, mensagem). Estados: OK, AVISO, ERRO."""
    m = re.search(r"doi:\s*(10\.\S+?)(?:\.?\s+PMID|\.?\s*$|\s)", ref + " ")
    pm = re.search(r"PMID:\s*(\d+)", ref)
    if m:
        doi = m.group(1).rstrip(".")
        dados = crossref(doi)
        if not dados:
            return "ERRO", f"DOI nao resolve: {doi}"
        titulo = _primeiro(dados.get("title"))
        if not _titulo_confere(titulo, ref):
            return "ERRO", (f"titulo nao corresponde ao DOI {doi}: "
                            f"real = '{_limpar(titulo)[:110]}'")
        fam = [a.get("family", "") for a in dados.get("author", []) or []]
        if fam and _norm(fam[0]).split() and \
                _norm(fam[0]).split()[0] not in _norm(ref):
            return "AVISO", f"primeiro autor real = {fam[0]}"
        ano = _ano_crossref(dados)
        anos_ref = re.findall(r"\b((?:19|20)\d{2})\b", ref.split("doi:")[0])
        if ano and anos_ref and ano not in anos_ref:
            return "AVISO", f"ano real = {ano} (ref indica {anos_ref})"
        return "OK", f"DOI {doi}"
    if pm:
        s = pubmed_resumos([pm.group(1)]).get(pm.group(1))
        if not s:
            return "ERRO", f"PMID inexistente: {pm.group(1)}"
        if not _titulo_confere(s.get("title", ""), ref):
            return "ERRO", f"titulo nao corresponde ao PMID {pm.group(1)}"
        return "OK", f"PMID {pm.group(1)}"
    u = re.search(r"(https?://\S+)", ref)
    if u:
        url = u.group(1).rstrip(".,;)")
        cod, titulo, _ = estado_url(url)
        if cod is None:
            return "AVISO", f"sem resposta ({titulo}): {url}"
        if cod in (404, 410):
            return "ERRO", f"HTTP {cod}: {url}"
        if cod >= 400:
            return "AVISO", f"HTTP {cod} (bloqueio do sitio?): {url}"
        return "OK", f"URL HTTP {cod} | {titulo[:70]}"
    return "ERRO", "sem DOI, PMID nem URL"


def cmd_verificar(a):
    fontes = carregar_fontes(a.modulo)
    erros = avisos = 0
    vistos = {}
    for chave, ref in fontes.items():
        estado, msg = verificar_ref(chave, ref)
        m = re.search(r"doi:\s*(10\.\S+?)(?:\.?\s+PMID|\.?\s*$|\s)", ref + " ")
        if m:
            d = m.group(1).rstrip(".").lower()
            if d in vistos:
                estado, msg = "ERRO", f"DOI duplicado com {vistos[d]}"
            vistos[d] = chave
        erros += estado == "ERRO"
        avisos += estado == "AVISO"
        print(f"[{estado:5}] {chave}: {msg}")
    print("-" * 70)
    print(f"{len(fontes)} referencias | erros: {erros} | avisos: {avisos}")
    sys.exit(1 if erros else 0)


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("buscar")
    b.add_argument("termo")
    b.add_argument("--n", type=int, default=20)
    b.add_argument("--desde", type=int, default=2016)
    b.set_defaults(f=cmd_buscar)
    d = sub.add_parser("doi")
    d.add_argument("dois", nargs="+")
    d.set_defaults(f=cmd_doi)
    p = sub.add_parser("pmid")
    p.add_argument("pmids", nargs="+")
    p.set_defaults(f=cmd_pmid)
    r = sub.add_parser("resumo")
    r.add_argument("ident")
    r.set_defaults(f=cmd_resumo)
    u = sub.add_parser("url")
    u.add_argument("url")
    u.set_defaults(f=cmd_url)
    w = sub.add_parser("web")
    for arg in ("autor", "titulo", "local", "editora", "ano", "url"):
        w.add_argument(f"--{arg}", required=True)
    w.add_argument("--chave")
    w.set_defaults(f=cmd_web)
    v = sub.add_parser("verificar")
    v.add_argument("modulo")
    v.set_defaults(f=cmd_verificar)
    a = ap.parse_args()
    a.f(a)


if __name__ == "__main__":
    main()
