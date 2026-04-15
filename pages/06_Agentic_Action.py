import streamlit as st
import time

st.set_page_config(page_title="Task 6: Autonomous Agent", page_icon="🤖")

st.title("🤖 Task 6: The Autonomous Supply Chain Expeditor")

st.markdown("""
**The Context:** Agentic AI *acts*. If HTLS conductors are delayed, manual expediting is tedious.
We will build a single ReAct (Reason + Act) Agent that can autonomously trigger Python functions (Tools) to solve supply chain delays.
""")

st.write("### 🛠️ Available Tools for the Agent")
st.code("""
@tool
def query_inventory_db(item: str) -> int:
    # Returns buffer inventory count

@tool
def check_weather_api(route: str) -> str:
    # Returns weather forecast

@tool
def draft_email(to: str, subject: str, body: str):
    # Drafts email to Project Manager
""", language="python")

st.write("### 🎯 Trigger the Agent")
trigger_prompt = st.text_area("Agent Objective:", value="Supplier A's steel delivery is delayed by 3 days. Check our database for buffer inventory of 'steel'. If we are short, check the weather on the 'Mumbai-Pune' delivery route and draft a status update email to the Project Manager.")

# ==========================================
# 🛑 PARTICIPANT CODE GOES HERE 🛑
# ==========================================
def build_and_run_agent(objective):
    """
    TODO: Define the Langchain / Anthropic Agent.
    1. Bind the 3 tools to the LLM.
    2. Pass the objective to the agent executor.
    3. Capture its thought pattern.
    """
    
    # --- INSTRUCTOR MODE FLAG ---
    if st.query_params.get("instructor") == "true":
        thoughts = [
            ("Thinking", "I need to check how much steel we have in the buffer DB first."),
            ("Action", "Invoking `query_inventory_db(item='steel')`..."),
            ("Observation", "Returned: 50 tons (Shortfall detected)."),
            ("Thinking", "We are short. I need to check the weather on the delivery route."),
            ("Action", "Invoking `check_weather_api(route='Mumbai-Pune')`..."),
            ("Observation", "Returned: Heavy Monsoons."),
            ("Thinking", "The weather is bad, so the delay is justified. I will draft the email now."),
            ("Action", "Invoking `draft_email(...)`...")
        ]
        return thoughts
    # ---------------------------
    
    # --- WRITE YOUR AGENT LOGIC HERE ---
    # e.g., agent = create_tool_calling_agent(llm, tools, prompt)
    #       executor = AgentExecutor(agent=agent, tools=tools)
    return [("Observation", "⚠️ Agent logic not implemented yet. Please write your code.")]
    # -----------------------------------

# ==========================================

if st.button("Run Autonomous Expeditor", type="primary"):
    with st.status("Agent Executing...", expanded=True) as status:
        
        # Run agent logic
        traces = build_and_run_agent(trigger_prompt)
        
        # Display traces dynamically
        for thought_type, text in traces:
            time.sleep(1) # Fake delay for dramatic effect
            if thought_type == "Thinking":
                st.write(f"🧠 **Thought:** {text}")
            elif thought_type == "Action":
                st.write(f"⚙️ **Tool Call:** `{text}`")
            elif thought_type == "Observation":
                st.write(f"📥 **Observation:** *{text}*")
                st.divider()
                
        status.update(label="Agent Workflow Complete!", state="complete", expanded=True)
        
    st.warning("⚠️ **HCI Pause (Supervisory Control):** The agent drafted the email, but it is waiting for your human approval before hitting send.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.button("Approve & Send Email", type="primary")
    with col2:
        st.button("Reject & Edit")
