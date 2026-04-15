import streamlit as st

st.set_page_config(
    page_title="Transrail AI Workshop",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ Transrail AI Workshop: Learning by Doing")

st.markdown("""
Welcome to the interactive sandbox for the **Transrail AI Workshop**.
This application contains 8 hands-on tasks structured as individual pages in the sidebar.

### 🎯 How to use this workspace:
For each task, we have provided the UI scaffolding. Your job is to fill in the **AI Core Logic**.

Look for the `TODO: YOUR CODE HERE` blocks inside the Python files located in the `pages/` directory.

### 🚀 Workshop Phases
1. **Foundational AI**: Rule-Based logic vs Probabilistic AI.
2. **Perceptive & Generative AI**: Working with unstructured text, images, and massive PDFs.
3. **Agentic AI**: Teaching LLMs to use external tools and collaborate.
4. **Capstone**: Stringing them all together into an End-to-End Watchdog limit.

> **Tip:** You can edit the code in real-time. Simply save your `pages/xxx.py` file, and Streamlit will automatically refresh this interface so you can test your logic instantly!

👈 **Select a task from the sidebar to begin.**
""")
