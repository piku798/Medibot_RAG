import fitz  # PyMuPDF
from pathlib import Path


def extract_text_from_pdf(pdf_path: str, output_path: str):
    """
    Extracts text from a PDF file and saves it as a .txt file
    """
    pdf_path = Path(pdf_path)
    output_path = Path(output_path)

    doc = fitz.open(pdf_path)
    all_text = []

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text = page.get_text()
        if text.strip():
            all_text.append(text)

    output_path.write_text("\n".join(all_text), encoding="utf-8")

    print(f"✅ Text extracted successfully: {output_path}")


if __name__ == "__main__":
    extract_text_from_pdf(
        pdf_path=r"C:\Users\nnaya\MEDIBOT_RAG\data\raw\MediBOOk.pdf",
        output_path=r"C:\Users\nnaya\MEDIBOT_RAG\data\processed\MediBOOk.txt",
    )
