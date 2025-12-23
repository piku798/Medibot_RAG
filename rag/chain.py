from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from rag.prompt import MEDICAL_PROMPT

load_dotenv()
def create_rag_chain():
    # Embeddings + Vector DB
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectordb = Chroma(
        persist_directory=r"C:\Users\nnaya\MEDIBOT_RAG\vectordb\chroma_db",
        embedding_function=embeddings
    )

    retriever = vectordb.as_retriever(search_kwargs={"k": 3})

    # LLM
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0.0
    )

    # Helper to format retrieved docs
    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    # RAG chain (modern, stable)
    rag_chain = (
        {
            "context": retriever | format_docs,
            "question": RunnablePassthrough()
        }
        | MEDICAL_PROMPT
        | llm
        | StrOutputParser()
    )

    return rag_chain, retriever
