"""Testes das funcoes do construtor da casa acrescentadas para a versao 2 do protocolo:
formulas com expoentes reais, indice automatico, seccoes com numeracao propria,
referencias com avanco e rodape a 1,5 cm.

Uso: python -m pytest test_house_docx.py -q
"""
import sys
from pathlib import Path

from docx.oxml.ns import qn
from docx.shared import Cm

sys.path.insert(0, str(Path(__file__).resolve().parent))

import house_docx as h


def _formato_numeracao(seccao):
    pg = seccao._sectPr.find(qn("w:pgNumType"))
    if pg is None:
        return None, None
    return pg.get(qn("w:fmt")), pg.get(qn("w:start"))


def test_novo_documento_poe_cabecalho_e_rodape_a_um_centimetro_e_meio():
    doc = h.novo_documento()
    sec = doc.sections[0]
    assert abs(sec.header_distance - Cm(1.5)) < 5000
    assert abs(sec.footer_distance - Cm(1.5)) < 5000


def test_formula_usa_sobrescrito_e_subscrito_reais_do_word():
    doc = h.novo_documento()
    par = h.formula(doc, [("n", None), ("0", "sub"), (" = Z", None), ("2", "sup")])
    runs = par.runs
    assert [r.text for r in runs] == ["n", "0", " = Z", "2"]
    assert runs[1].font.subscript is True
    assert runs[3].font.superscript is True
    assert not runs[0].font.superscript and not runs[0].font.subscript


def test_formula_nao_deixa_caracteres_unicode_de_expoente():
    doc = h.novo_documento()
    par = h.formula(doc, [("d", None), ("2", "sup")])
    assert "²" not in par.text


def test_indice_automatico_insere_campo_toc_com_tres_niveis():
    doc = h.novo_documento()
    h.indice_automatico(doc)
    instrucoes = [n.text for n in doc.element.body.iter(qn("w:instrText"))]
    assert any('TOC \\o "1-3"' in i for i in instrucoes)


def test_nova_seccao_recomeca_a_numeracao_arabe_em_um():
    doc = h.novo_documento()
    h.paragrafo(doc, "Pre-textual")
    h.numeracao(doc.sections[0], "lowerRoman")
    nova = h.nova_seccao(doc, "decimal", 1)
    assert len(doc.sections) == 2
    assert _formato_numeracao(doc.sections[0]) == ("lowerRoman", None)
    assert _formato_numeracao(nova) == ("decimal", "1")


def test_pgnumtype_fica_antes_de_cols_como_exige_o_esquema_ooxml():
    """Regressao: com append, pgNumType ia para o fim de sectPr e o Word pode recusar o
    ficheiro quando nao e ele a grava-lo (construcao com --sem-word)."""
    doc = h.novo_documento()
    h.numeracao(doc.sections[0], "lowerRoman")
    h.nova_seccao(doc, "decimal", 1)
    h.numerar_paginas(doc)
    for sec in doc.sections:
        filhos = [f.tag for f in sec._sectPr]
        assert filhos.index(qn("w:pgNumType")) < filhos.index(qn("w:cols"))


def test_numerar_paginas_so_esconde_o_numero_na_primeira_pagina_da_primeira_seccao():
    doc = h.novo_documento()
    h.paragrafo(doc, "Capa")
    h.nova_seccao(doc, "decimal", 1)
    h.paragrafo(doc, "Introducao")
    h.numerar_paginas(doc)
    assert doc.sections[0].different_first_page_header_footer is True
    assert doc.sections[1].different_first_page_header_footer is False
    for sec in doc.sections:
        assert "PAGE" in sec.footer.paragraphs[0]._element.xml


def test_referencia_tem_primeira_linha_sem_avanco_e_restantes_a_075_cm():
    doc = h.novo_documento()
    par = h.referencia(doc, 1, "Autor A. Titulo. Revista. 2020;1(1):1-9. doi:10.1000/a.")
    pf = par.paragraph_format
    assert par.text.startswith("1. Autor A.")
    assert abs(pf.left_indent - Cm(0.75)) < 5000
    assert abs(pf.first_line_indent + Cm(0.75)) < 5000
    assert pf.line_spacing == 1.0


def test_subtitulo_e_negrito_mas_nao_e_titulo_do_indice():
    doc = h.novo_documento()
    par = h.subtitulo(doc, "Secção I. Dados sociodemográficos")
    assert not par.style.name.startswith("Heading")
    assert all(r.font.bold for r in par.runs)
