from pathlib import Path
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


def store_embeddings(
    chunks_dir: str,
    vectordb_dir: str,
    batch_size: int = 500
):
    chunks_dir = Path(chunks_dir)
    vectordb_dir = Path(vectordb_dir)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectordb = Chroma(
        persist_directory=str(vectordb_dir),
        embedding_function=embeddings
    )

    texts = []
    metadatas = []

    for chunk_file in chunks_dir.glob("*.txt"):
        texts.append(chunk_file.read_text(encoding="utf-8"))
        metadatas.append({"source": chunk_file.name})

    total = len(texts)
    print(f"📦 Total chunks: {total}")

    for i in range(0, total, batch_size):
        vectordb.add_texts(
            texts=texts[i:i + batch_size],
            metadatas=metadatas[i:i + batch_size]
        )
        print(f"✅ Stored batch {(i // batch_size) + 1}")

    print("🎉 All embeddings stored successfully!")


if __name__ == "__main__":
    store_embeddings(
        chunks_dir=r"C:\Users\nnaya\MEDIBOT_RAG\data\processed\chunks",
        vectordb_dir=r"C:\Users\nnaya\MEDIBOT_RAG\vectordb\chroma_db"
    )
