# -*- coding: utf-8 -*-
"""
Auditoria global: recompõe e valida todos os módulos _conteudo/tema_NN.py,
verifica as fontes e grava um resumo em _motor/auditoria.json.

Uso:  python auditar_todos.py [--sem-fontes] [NN NN ...]
"""
import glob
import json
import os
import re
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
PY = sys.executable


def correr(args):
    r = subprocess.run([PY] + args, cwd=RAIZ, capture_output=True,
                       text=True, encoding="utf-8", errors="replace")
    return r.returncode, r.stdout + r.stderr


def auditar(caminho, fontes=True):
    nome = os.path.basename(caminho)
    num = int(re.search(r"(\d+)", nome).group(1))
    cod, out = correr([os.path.join("_motor", "motor.py"), caminho])
    info = {"numero": num, "motor_ok": cod == 0}
    for chave, padrao in (("palavras", r"palavras no corpo \(1-12\)\s*:\s*(\d+)"),
                          ("referencias", r"referencias citadas\s*:\s*(\d+)"),
                          ("orcamento", r"orcamento total \(MT\)\s*:\s*([\d,.]+)")):
        m = re.search(padrao, out)
        info[chave] = m.group(1) if m else None
    m = re.search(r"TEMA \d+: (.+\.docx)", out)
    info["docx"] = m.group(1).strip() if m else None
    info["problemas"] = re.findall(r"\[X\] (.+)", out)
    info["avisos"] = len(re.findall(r"\[!\] ", out))
    if fontes:
        cod2, out2 = correr([os.path.join("_motor", "refs.py"), "verificar",
                             caminho])
        m = re.search(r"erros: (\d+) \| avisos: (\d+)", out2)
        info["fontes_erros"] = int(m.group(1)) if m else None
        info["fontes_avisos"] = int(m.group(2)) if m else None
        info["fontes_detalhe"] = [l for l in out2.splitlines()
                                  if l.startswith(("[ERRO", "[AVISO"))]
    return info


if __name__ == "__main__":
    argv = sys.argv[1:]
    fontes = "--sem-fontes" not in argv
    alvos = [a for a in argv if a.isdigit()]
    mods = sorted(glob.glob(os.path.join(RAIZ, "_conteudo", "tema_[0-9][0-9].py")))
    if alvos:
        mods = [m for m in mods
                if re.search(r"tema_(\d+)", m).group(1) in
                {a.zfill(2) for a in alvos}]
    res = []
    for m in mods:
        i = auditar(os.path.relpath(m, RAIZ), fontes)
        res.append(i)
        estado = "OK " if i["motor_ok"] and not i.get("fontes_erros") else "FALHA"
        print(f"[{estado}] T{i['numero']:02d} | palavras {i['palavras']} | "
              f"refs {i['referencias']} | problemas {len(i['problemas'])} | "
              f"fontes erros {i.get('fontes_erros')} avisos "
              f"{i.get('fontes_avisos')}")
    saida = os.path.join(AQUI, "auditoria.json")
    anterior = {}
    if os.path.exists(saida) and alvos:
        with open(saida, encoding="utf-8") as fh:
            anterior = {x["numero"]: x for x in json.load(fh)}
    for i in res:
        anterior[i["numero"]] = i
    with open(saida, "w", encoding="utf-8") as fh:
        json.dump(sorted(anterior.values(), key=lambda x: x["numero"]), fh,
                  ensure_ascii=False, indent=1)
    print(f"\n{len(res)} módulos auditados; resumo em {saida}")
