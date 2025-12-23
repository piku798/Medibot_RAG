from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter


def clean_text(text: str) -> str:
    """
    Light cleaning without damaging medical meaning
    """
    lines = text.splitlines()
    cleaned_lines = []

    for line in lines:
        line = line.strip()
        if len(line) < 3:
            continue
        cleaned_lines.append(line)

    return " ".join(cleaned_lines)


def chunk_text(
    input_txt: str,
    output_dir: str,
    chunk_size: int = 500,
    chunk_overlap: int = 100
):
    input_txt = Path(input_txt)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    raw_text = input_txt.read_text(encoding="utf-8")
    cleaned_text = clean_text(raw_text)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ".", " "]
    )

    chunks = splitter.split_text(cleaned_text)

    for idx, chunk in enumerate(chunks):
        chunk_file = output_dir / f"chunk_{idx}.txt"
        chunk_file.write_text(chunk, encoding="utf-8")

    print(f"✅ Created {len(chunks)} medical text chunks")


if __name__ == "__main__":
    chunk_text(
        input_txt=r"C:\Users\nnaya\MEDIBOT_RAG\data\processed\MediBOOk.txt",
        output_dir=r"C:\Users\nnaya\MEDIBOT_RAG\data\processed\chunks",
    )
        