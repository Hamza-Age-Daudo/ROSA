"""Actualiza no Microsoft Word os campos do protocolo (indice e numeros de pagina) e
exporta o PDF.

O python-docx escreve o campo do indice mas nao sabe paginar; so o Word calcula em que
pagina cai cada titulo. Este passo abre o documento no Word, sem janela, actualiza todos
os campos, grava e exporta o PDF ao lado.

Uso: python actualizar_word.py [caminho.docx]
"""
import sys
from pathlib import Path

WD_EXPORTAR_PDF = 17


def actualizar_e_exportar(docx, pdf=None):
    """Actualiza indice e campos, grava o .docx e, se pedido, exporta o PDF.

    Devolve True se o Word estava disponivel e o documento foi actualizado.
    """
    aviso = ("abrir o documento no Word e actualizar o indice (Referencias, Actualizar "
             "indice).")
    try:
        import pywintypes
        import win32com.client
    except ImportError:
        print(f"AVISO: pywin32 nao instalado; {aviso}")
        return False

    docx = Path(docx).resolve()
    try:
        word = win32com.client.DispatchEx("Word.Application")
    except pywintypes.com_error as erro:
        print(f"AVISO: o Word nao arrancou ({erro}); {aviso}")
        return False
    word.Visible = False
    word.DisplayAlerts = 0
    # Sem isto o Word deixa um "Backup de ... .wbk" ao lado; a opcao do utilizador e reposta.
    copia_de_seguranca = word.Options.CreateBackup
    word.Options.CreateBackup = False
    try:
        documento = word.Documents.Open(str(docx), False, False, False)
        try:
            documento.Fields.Update()
            for _passagem in range(2):  # a segunda passagem acerta paginas que o indice empurrou
                for indice in documento.TablesOfContents:
                    indice.Update()
            documento.Save()
            if pdf is not None:
                documento.ExportAsFixedFormat(str(Path(pdf).resolve()), WD_EXPORTAR_PDF)
        finally:
            documento.Close(False)
    finally:
        word.Options.CreateBackup = copia_de_seguranca
        word.Quit()
    return True


if __name__ == "__main__":
    alvo = Path(sys.argv[1]) if len(sys.argv) > 1 else (
        Path(__file__).resolve().parent / "03_TCC" / "PROTOCOLO_AGRESSIVIDADE_MUATALA.docx")
    ok = actualizar_e_exportar(alvo, alvo.with_suffix(".pdf"))
    sys.exit(0 if ok else 1)
