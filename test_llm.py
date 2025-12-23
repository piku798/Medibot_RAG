from rag.chain import create_rag_chain

rag_chain, retriever = create_rag_chain()

while True:
    query = input("\nAsk medical question (or 'exit'): ")
    if query.lower() == "exit":
        break

    # Run RAG
    answer = rag_chain.invoke(query)

    # Show answer
    print("\n🩺 Answer:\n")
    print(answer)

    # Show sources
    print("\n📚 Sources:")
    docs = retriever.invoke(query)
    for doc in docs:
        print("-", doc.metadata.get("source"))
