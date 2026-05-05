import streamlit as st
import httpx

from langchain_ollama import OllamaLLM
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma

st.set_page_config(page_title="Task 4: RAG Tender Interrogator", page_icon="📚")

st.title("📚 Task 4: The 1,000-Page Tender Interrogator")

st.markdown("""
We are using a real RAG pipeline with ChromaDB + Ollama.
""")

# ==========================================================
# LOAD MODELS + DB
# ==========================================================

@st.cache_resource
def load_models():
    embedding = OllamaEmbeddings(model="nomic-embed-text")

    db = Chroma(
        persist_directory="./chroma_db",
        embedding_function=embedding
    )

    llm = OllamaLLM(model="llama3.2:1b", temperature=0.0)

    return db, llm

db, llm = load_models()

# ==========================================================
# CHAT HISTORY
# ==========================================================

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "I have ingested the tender document. Ask me anything."}
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ==========================================================
# RAG PIPELINE
# ==========================================================

def run_rag_pipeline(user_query):

    try:
        # 🔍 Step 1: Retrieve docs
        docs = db.similarity_search(user_query, k=3)

        # 🧪 DEBUG (VERY IMPORTANT)
        if st.query_params.get("debug") == "true":
            st.write("🔍 Retrieved Documents Count:", len(docs))

        if not docs:
            return "❌ No data retrieved. Check if ChromaDB is loaded correctly.", []

        if st.query_params.get("debug") == "true":
            # Show retrieved chunks (for debugging)
            for i, d in enumerate(docs):
                st.write(f"--- Chunk {i+1} ---")
                st.write(d.page_content[:300])  # preview
                st.write(d.metadata)

        # 📄 Step 2: Build context
        context = "\n\n".join([d.page_content for d in docs])

        # 📌 Step 3: Extract pages
        pages = []
        for d in docs:
            if "page" in d.metadata:
                pages.append(str(d.metadata["page"] + 1))
        
        pages = list(set(pages))
        source_text = ", ".join(pages) if pages else "Unknown"

        # 🤖 Step 4: Prompt
        prompt = f"""You are a helpful assistant analyzing a tender document.
Answer the user's question using ONLY the provided context. 
If the context contains relevant information, summarize it.
If the context does not contain any relevant information, reply EXACTLY with: "❌ Data not present in document. Cannot answer."

Context:
{context}

Question: {user_query}

Important: If you provide an answer, you MUST end your response with:
(Source: page {source_text})
"""

        # 🤖 Step 5: LLM
        response = llm.invoke(prompt)

        return response, pages

    except httpx.ConnectError:
        return "❌ Error: Ollama is not running. Please start Ollama before asking a question.", []
    except Exception as e:
        return f"❌ Error: {str(e)}", []

# ==========================================================
# USER INPUT
# ==========================================================

if prompt := st.chat_input("Ask a question about the tender..."):

    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        with st.spinner("Searching..."):

            response, pages = run_rag_pipeline(prompt)
            st.markdown(response)

            # clickable PDF link
            for p in pages:
                st.markdown(f"[📄 Page {p}](tender.pdf#page={p})")

    st.session_state.messages.append({"role": "assistant", "content": response})