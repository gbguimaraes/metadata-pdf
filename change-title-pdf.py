from typing import Optional
from pathlib import Path
from pdfrw import PdfReader, PdfWriter


def update_pdf_metadata(pdf_path: Path, title: Optional[str]) -> None:
    """Atualiza o metadado Title de um arquivo PDF especificado pelo caminho Path."""

    # ler o arquivo PDF usando a biblioteca pdfrw
    pdf = PdfReader(str(pdf_path))

    # atualizar os metadados, se for especificado
    if title:
        pdf.Info.Title = title

    # escrever o arquivo PDF com os novos metadados
    writer = PdfWriter()
    writer.addpages(pdf.pages)
    writer.trailer.Info = pdf.Info
    writer.write(str(pdf_path))


if __name__ == "__main__":
    # solicitar o caminho do arquivo PDF
    pdf_path = Path(input("Digite o caminho do arquivo PDF: "))

    # pega automaticamente o nome do arquivo contido no Path e colocar ele como nome do Arquivo
    title = pdf_path.stem

    # solicitar um novo título, se desejado
    # title = input("Digite um novo título (deixe em branco para manter o título atual): ").strip() or None

    # chamar a função update_pdf_metadata com as entradas fornecidas
    update_pdf_metadata(pdf_path, title)
