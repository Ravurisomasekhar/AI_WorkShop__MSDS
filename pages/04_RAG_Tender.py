import streamlit as st
import time

st.set_page_config(page_title="Task 4: RAG Tender Interrogator", page_icon="📚")

st.title("📚 Task 4: The 1,000-Page Tender Interrogator")

st.markdown("""
**The Context:** Bidding for PGCIL or international EPC tenders involves digesting hundreds of pages of complex legal and technical constraints.
We will build a Retrieval-Augmented Generation (RAG) pipeline to ground an LLM in a specific document.
""")

st.write("### 🗄️ Vector Database Context")
st.info("For this workshop, we assume a dummy 50-page PDF tender document has already been chunked and loaded into ChromaDB.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "I have ingested the 'PGCIL 400kV Substation Tender v2.pdf'. What would you like to know?"}
    ]

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ==========================================
# 🛑 PARTICIPANT CODE GOES HERE 🛑
# ==========================================
def run_rag_pipeline(user_query):
    """
    TODO: Implement the RAG logic.
    1. Embed the user query.
    2. Search the vector database (ChromaDB) for the top 3 similar chunks.
    3. Pass the chunks + query to the LLM to generate an answer.
    4. Ensure it returns a citation!
    """
    # --- INSTRUCTOR MODE FLAG ---
    if st.query_params.get("instructor") == "true":
        time.sleep(1.5)
        return "The exact Liquidated Damages (LD) clause is 0.5% of the contract price per week of delay, up to a maximum of 10%. (Source: *pg. 42, Clause 14.2*)"
    # ---------------------------
    
    # --- WRITE YOUR RAG PIPELINE HERE ---
    # e.g., docs = vector_db.similarity_search(query)
    #       response = llm(prompt=f"Context: {docs} Query: {query}")
    return "⚠️ RAG pipeline code not implemented yet. Please write your code."
    # ------------------------------------

# ==========================================

# React to user input
if prompt := st.chat_input("Ask a question about the tender..."):
    # Display user message
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display assistant response
    with st.chat_message("assistant"):
        with st.spinner("Searching document vectors..."):
            response = run_rag_pipeline(prompt)
            st.markdown(response)
            
            st.success("💡 **HCI Challenge:** Notice the 'Source' citation. Can you make that a clickable link to open the PDF to the exact page?")
            
    st.session_state.messages.append({"role": "assistant", "content": response})
