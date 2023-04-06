import os
from typing import Optional
from pathlib import Path
from pdfrw import PdfReader, PdfWriter


def update_pdf_author(pdf_path: Path, author: Optional[str]) -> None:
    """Atualiza o metadado Author de todos os arquivos PDF especificado pelo caminho Path."""

    # ler o arquivo PDF usando a biblioteca pdfrw
    pdf = PdfReader(str(pdf_path))

    # atualizar o metadado do autor, se for especificado
    if author:
        pdf.Info.Author = author

    # escrever o arquivo PDF com o novo metadado do autor
    writer = PdfWriter()
    writer.addpages(pdf.pages)
    writer.trailer.Info = pdf.Info
    writer.write(str(pdf_path))


if __name__ == "__main__":
    # solicitar o diretório que contém os arquivos PDF
    pdf_directory = input("Digite o caminho do diretório que contém os arquivos PDF: ")

    # solicitar o novo autor
    new_author = input("Digite o novo autor para os arquivos PDF: ").strip() or None

    # percorrer todos os arquivos no diretório e atualizar o metadado do autor em cada arquivo PDF
    for filename in os.listdir(pdf_directory):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(pdf_directory, filename)
            update_pdf_author(Path(pdf_path), new_author)
