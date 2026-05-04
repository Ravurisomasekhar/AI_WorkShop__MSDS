import streamlit as st
import time
from langchain_community.llms import Ollama

st.set_page_config(page_title="Task 4: RAG Tender Interrogator", page_icon="📚")

st.title("📚 Task 4: The 1,000-Page Tender Interrogator")

st.markdown("""
**The Context:** Bidding for PGCIL or international EPC tenders involves digesting hundreds of pages of complex legal and technical constraints.
We will build a Retrieval-Augmented Generation (RAG) pipeline to ground an LLM in a specific document.
""")

st.write("### 🗄️ Vector Database Context")
st.info("For this demo, we are using a sample tender section as our data.")

# ==========================================================
# ✅ LOAD LLM
# ==========================================================

@st.cache_resource
def load_llm():
    return Ollama(model="phi3")

llm = load_llm()

# ==========================================================
# CHAT HISTORY
# ==========================================================

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "I have ingested the tender data. What would you like to know?"}
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ==========================================================
# RAG FUNCTION (MINI VERSION)
# ==========================================================

def run_rag_pipeline(user_query):

    # Demo mode
    if st.query_params.get("instructor") == "true":
        time.sleep(1.5)
        return "Demo answer"

    try:
        # ✅ YOUR TENDER DATA
        context = """
23. Bid Opening 

23.1 The Superintending Engineer GMDA will open all the Bids received (except those received late), 
in the presence of the bidders.

23.3 The Technical Bid shall be opened first.

23.4 Earnest money, forms, and validity shall be announced.

23.5 Technical bids will be evaluated and responsive bidders identified.

23.6 Financial bid opening date and time will be announced.

23.7 Financial bids of only responsive bidders will be opened and prices announced.

23.8 The Superintending Engineer will prepare minutes of the bid opening.
"""

        # ✅ Strong Prompt
        prompt = f"""
You are a tender document assistant.

Rules:
1. Answer ONLY from the context below.
2. Do NOT guess or use outside knowledge.
3. If answer is NOT present, reply EXACTLY:
   "❌ Data not present in document. Cannot answer."

Context:
{context}

Question:
{user_query}

Also include source clause number if possible.
"""

        response = llm.invoke(prompt)
        return response

    except Exception as e:
        return f"❌ Error: {str(e)}"

# ==========================================================
# USER INPUT
# ==========================================================

if prompt := st.chat_input("Ask a question about the tender..."):
    
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        with st.spinner("Analyzing document..."):
            
            response = run_rag_pipeline(prompt)
            st.markdown(response)

            # ✅ HCI clickable example (static)
            st.markdown("[📄 Open Tender PDF (Sample)](PGCIL.pdf#page=1)")

    st.session_state.messages.append({"role": "assistant", "content": response})


    # 