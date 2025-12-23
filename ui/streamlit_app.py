import sys
import os

# ✅ Fix Streamlit import path (Windows-safe)
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import streamlit as st
from rag.chain import create_rag_chain

# Page config
st.set_page_config(
    page_title="🩺 MediBot – Medical RAG Assistant",
    page_icon="🩺",
    layout="centered"
)

st.title("🩺 MediBot")
st.caption("Medical Information Assistant (RAG-based)")
st.markdown(
    "**Disclaimer:** This tool provides educational medical information only. "
    "It does NOT provide diagnosis or treatment."
)

# Initialize RAG
@st.cache_resource
def load_rag():
    return create_rag_chain()

rag_chain, retriever = load_rag()

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
user_input = st.chat_input("Ask a medical question (e.g., I have headache)")

if user_input:
    # Show user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate answer
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            answer = rag_chain.invoke(user_input)
            st.markdown(answer)

            # Retrieve sources
            docs = retriever.invoke(user_input)

            with st.expander("📚 Sources"):
                for doc in docs:
                    st.markdown(f"- {doc.metadata.get('source')}")

    # Save assistant response
    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )
