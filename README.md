🩺 MediBot_RAG – Medical AI Assistant using RAG

MediBot_RAG is a production-style Medical Question Answering System built using Retrieval-Augmented Generation (RAG).
It retrieves verified medical knowledge from documents and generates context-grounded, non-hallucinated responses through an LLM, presented via a Streamlit chat interface.

This project demonstrates end-to-end Generative AI system design, covering data ingestion, vector databases, semantic search, LLM orchestration, and UI integration.

🎯 Why This Project Matters (For Recruiters)

✔ Demonstrates real-world RAG pipeline (not a toy chatbot)

✔ Shows LLMOps & GenAI system design skills

✔ Includes retrieval testing before LLM generation (industry best practice)

✔ Medical-safe prompt engineering with disclaimers

✔ Clean modular architecture ready for deployment

🎥 Demo

Streamlit Chat Interface – MediBot in Action

🧠 System Architecture
Medical PDFs
   ↓
Text Extraction (PyMuPDF)
   ↓
Cleaning & Chunking
   ↓
Embeddings (Sentence-Transformers)
   ↓
Vector Database (ChromaDB)
   ↓
Semantic Retriever
   ↓
Medical-Safe Prompt
   ↓
Groq LLM (LLaMA 3.1)
   ↓
Answer + Source Attribution
   ↓
Streamlit Chat UI

🚀 Key Features

📚 Retrieval-Augmented Generation (RAG)

🔎 Semantic Search with Vector Database (ChromaDB)

🧩 Chunking strategy optimized for medical content

🤖 LLM grounding using retrieved context only

🛑 Hallucination prevention & safe refusal logic

💬 Streamlit chat UI with source visibility

🧪 Standalone retriever testing before LLM integration

🔐 Secure API key handling using .env

🛠️ Tech Stack (ATS-Optimized)

Languages & Tools

Python

Git & GitHub

AI / ML / GenAI

Retrieval-Augmented Generation (RAG)

Prompt Engineering

Sentence-Transformers

Large Language Models (LLMs)

Embeddings & Semantic Search

Frameworks & Libraries

LangChain (Core Runnables)

ChromaDB (Vector Database)

Groq API (LLaMA 3.1)

Streamlit (UI)

PyMuPDF (PDF Processing)

python-dotenv

📂 Project Structure
Medibot_RAG/
├── ingestion/
│   ├── loader.py        # PDF → text extraction
│   ├── chunker.py       # Cleaning & chunking
│   └── embed_store.py   # Embeddings → ChromaDB
│
├── rag/
│   ├── prompt.py        # Medical-safe prompt
│   ├── retriever.py     # Vector retriever
│   └── chain.py         # RAG pipeline (modern runnable)
│
├── ui/
│   └── streamlit_app.py # Streamlit chat UI
│
├── output/
│   └── demo_ui.png      # Demo screenshots
│
├── test_retriever.py    # Retriever-only testing
├── test_llm.py          # RAG + LLM testing
├── requirements.txt
├── .gitignore
└── README.md

⚙️ Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/piku798/Medibot_RAG.git
cd Medibot_RAG

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Configure Environment Variables

Create a .env file:

GROQ_API_KEY=your_groq_api_key_here

▶️ How to Run
🔹 Test Retriever (No LLM)
python test_retriever.py

🔹 Test Full RAG + LLM Pipeline
python test_llm.py

🔹 Run Streamlit UI
streamlit run ui/streamlit_app.py

💬 Example Queries

“I have a headache”

“What are common headache treatments?”

“What is Damiana used for medically?”

“Which body systems does Damiana affect?”

🛡️ Medical Safety & Ethics

❌ No diagnosis or prescription

❌ No hallucinated medical facts

✅ Context-only responses

✅ Mandatory medical disclaimer in every answer

Disclaimer:
This application provides educational information only and is not a medical diagnosis. Always consult a licensed medical professional.

📈 What This Project Demonstrates

End-to-end GenAI application development

Vector database design & optimization

LLM grounding and hallucination control

Modular, production-ready Python architecture

UI + backend integration

🔮 Future Enhancements

Emergency symptom detection & alerts

Confidence scoring for answers

Multi-document citation highlighting

FastAPI backend for deployment

Dockerization & cloud deployment

LangGraph-based multi-step reasoning

👤 Author

Neelachala Nayak
AI / ML Engineer | Generative AI Enthusiast

📌 GitHub: https://github.com/piku798
