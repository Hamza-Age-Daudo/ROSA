# -*- coding: utf-8 -*-
"""
Acabamento no Microsoft Word (so' no Windows, com o Word instalado):
actualiza o indice e os campos, conta as paginas e, opcionalmente, exporta
PDF e imagens das paginas para inspeccao visual.

Uso:
  python word.py actualizar ../01_Farmacia_Clinica/PROTOCOLO_T01_X.docx [...]
  python word.py actualizar --todos
  python word.py pdf ../01_Farmacia_Clinica/PROTOCOLO_T01_X.docx [--png 1,2,5-8]

Correr depois da versao final do conteudo: uma nova composicao pelo motor
apaga o indice actualizado.
"""
import glob
import os
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
WD_PDF = 17
WD_PAGINAS = 2


def _word():
    import win32com.client as win32
    w = win32.DispatchEx("Word.Application")
    w.Visible = False
    w.DisplayAlerts = 0
    return w


def actualizar(caminhos, pdf=False):
    w = _word()
    res = {}
    try:
        for c in caminhos:
            c = os.path.abspath(c)
            doc = w.Documents.Open(c, ReadOnly=False, AddToRecentFiles=False)
            try:
                for i in range(1, doc.TablesOfContents.Count + 1):
                    doc.TablesOfContents(i).Update()
                doc.Fields.Update()
                for i in range(1, doc.TablesOfContents.Count + 1):
                    doc.TablesOfContents(i).Update()
                paginas = doc.ComputeStatistics(WD_PAGINAS)
                doc.Save()
                saida_pdf = None
                if pdf:
                    saida_pdf = os.path.splitext(c)[0] + ".pdf"
                    doc.ExportAsFixedFormat(saida_pdf, WD_PDF)
                res[c] = (paginas, saida_pdf)
                print(f"{paginas:3d} páginas | {os.path.relpath(c, RAIZ)}")
            finally:
                doc.Close(False)
    finally:
        w.Quit()
    _gravar_paginas(res)
    return res


def _gravar_paginas(res):
    import json
    f = os.path.join(AQUI, "paginas.json")
    dados = {}
    if os.path.exists(f):
        with open(f, encoding="utf-8") as fh:
            dados = json.load(fh)
    for c, (pag, _) in res.items():
        dados[os.path.basename(c)] = pag
    with open(f, "w", encoding="utf-8") as fh:
        json.dump(dados, fh, ensure_ascii=False, indent=1)


def paginas_png(pdf, paginas, pasta):
    import fitz
    os.makedirs(pasta, exist_ok=True)
    doc = fitz.open(pdf)
    out = []
    for n in paginas:
        if 1 <= n <= doc.page_count:
            pix = doc[n - 1].get_pixmap(dpi=80)
            f = os.path.join(pasta, f"pag_{n:02d}.png")
            pix.save(f)
            out.append(f)
    return out


def _intervalos(txt):
    nums = []
    for parte in txt.split(","):
        a, _, b = parte.partition("-")
        nums += list(range(int(a), int(b or a) + 1))
    return nums


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(2)
    cmd, resto = sys.argv[1], sys.argv[2:]
    if cmd == "actualizar":
        alvos = (sorted(glob.glob(os.path.join(RAIZ, "[0-9][0-9]_*",
                                               "PROTOCOLO_T*.docx")))
                 if resto == ["--todos"] else resto)
        actualizar(alvos)
    elif cmd == "pdf":
        png = None
        if "--png" in resto:
            i = resto.index("--png")
            png = _intervalos(resto[i + 1])
            resto = resto[:i] + resto[i + 2:]
        r = actualizar(resto, pdf=True)
        if png:
            for c, (_, p) in r.items():
                pasta = os.path.join(os.path.dirname(p), "_paginas",
                                     os.path.basename(p)[:-4])
                for f in paginas_png(p, png, pasta):
                    print(f)
