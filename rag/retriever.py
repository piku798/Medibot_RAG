from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


def test_retriever(query: str, k: int = 3):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectordb = Chroma(
        persist_directory=r"C:\Users\nnaya\MEDIBOT_RAG\vectordb\chroma_db",
        embedding_function=embeddings
    )

    results = vectordb.similarity_search(query, k=k)

    print(f"\n🔎 Query: {query}")
    print(f"📄 Retrieved {len(results)} chunks\n")

    for i, doc in enumerate(results, 1):
        print("=" * 80)
        print(f"📌 Chunk {i}")
        print(f"📂 Source: {doc.metadata.get('source')}")
        print("\n📖 Content:\n")
        print(doc.page_content[:1000])  # limit print length
        print("=" * 80)


if __name__ == "__main__":
    while True:
        q = input("\nEnter query (or 'exit'): ")
        if q.lower() == "exit":
            break
        test_retriever(q)
