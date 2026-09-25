"""Constroi o protocolo de investigacao sobre factores psicossociais e comportamento
agressivo na Escola Secundaria de Muatala, no estilo da casa UniLurio.

Uso: python construir_protocolo.py [--sem-word]
Saida: 03_TCC/PROTOCOLO_AGRESSIVIDADE_MUATALA.docx e, com o Word disponivel, o PDF ao lado.
"""
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE))

import house_docx as h
from _protocolo_apendices import escrever_apendices
from _protocolo_metodologia import (escrever_cronograma_orcamento, escrever_divulgacao,
                                    escrever_metodologia, escrever_resultados_esperados)
from _protocolo_referencias import Numerador
from _protocolo_revisao import escrever_justificativa, escrever_objectivos, escrever_revisao
from _protocolo_texto import escrever_introducao, escrever_pre_textuais, escrever_problema

DESTINO = BASE / "03_TCC" / "PROTOCOLO_AGRESSIVIDADE_MUATALA.docx"
FIGURA = BASE / "figuras" / "esquema_conceptual.png"


class Escritor:
    """Escreve no documento resolvendo as citacoes Vancouver antes de cada insercao."""

    def __init__(self, doc, numerador):
        self.doc = doc
        self.numerador = numerador

    def resolver(self, texto):
        return self.numerador.resolver(texto)

    def p(self, texto, **opcoes):
        return h.paragrafo(self.doc, self.numerador.resolver(texto), **opcoes)

    def marca(self, texto, **opcoes):
        return h.marca(self.doc, self.numerador.resolver(texto), **opcoes)

    def h1(self, texto):
        return h.titulo(self.doc, texto, 1)

    def h2(self, texto):
        return h.titulo(self.doc, texto, 2)

    def h3(self, texto):
        return h.titulo(self.doc, texto, 3)


def escrever_referencias(doc, numerador):
    """Lista Vancouver pela ordem de citacao, com avanco de 0,75 cm e espaco simples."""
    h.quebra_pagina(doc)
    h.titulo(doc, "REFERÊNCIAS BIBLIOGRÁFICAS", 1)
    for numero, referencia in numerador.lista_final():
        h.referencia(doc, numero, referencia)


def construir(usar_word=True):
    numerador = Numerador()
    doc = h.novo_documento()
    e = Escritor(doc, numerador)

    escrever_pre_textuais(e, h, doc)
    h.numeracao(doc.sections[0], "lowerRoman")
    h.nova_seccao(doc, "decimal", 1)
    escrever_introducao(e)
    escrever_problema(e)
    escrever_objectivos(e)
    escrever_justificativa(e)
    escrever_revisao(e, h, doc, str(FIGURA))
    escrever_metodologia(e, h, doc)
    escrever_resultados_esperados(e)
    escrever_divulgacao(e)
    escrever_cronograma_orcamento(e, h, doc)
    escrever_referencias(doc, numerador)
    escrever_apendices(e, h, doc)

    h.numerar_paginas(doc)
    DESTINO.parent.mkdir(parents=True, exist_ok=True)
    doc.save(DESTINO)

    orfas = numerador.nao_citadas()
    print(f"Documento gravado: {DESTINO}")
    print(f"Referencias citadas: {len(numerador.ordem)}")
    if orfas:
        print(f"AVISO, referencias nao citadas no texto: {', '.join(orfas)}")
    if usar_word:
        from actualizar_word import actualizar_e_exportar
        if actualizar_e_exportar(DESTINO, DESTINO.with_suffix(".pdf")):
            print(f"Indice actualizado no Word e PDF exportado: {DESTINO.with_suffix('.pdf')}")
    return DESTINO


if __name__ == "__main__":
    construir(usar_word="--sem-word" not in sys.argv)
