import streamlit as st
import time

st.set_page_config(page_title="Task 8: Capstone", page_icon="🏆", layout="wide")

st.title("🏆 Capstone: End-to-End Smart Safety Watchdog")

st.markdown("""
**The Context:** Real-world enterprise AI is rarely just one model. It is a symphony of vision, logic rules, text generation, and autonomous action working seamlessly together.
""")

col1, col2 = st.columns([1, 2])

with col1:
    st.write("### 1️⃣ Vision Trigger")
    uploaded = st.file_uploader("Upload Drone Footage", type=["jpg", "png"])
    if uploaded:
        st.image(uploaded, use_column_width=True)

with col2:
    st.write("### ⚙️ The Orchestration Pipeline")
    
    st.info("""
    We are going to chain the modules we built today:
    1. **Task 3:** Vision AI detects lack of harness and estimates height.
    2. **Task 1:** Rule-Based Script categorizes severity (if height > 2m).
    3. **Task 6:** Agent queries DB for Supervisor's phone number.
    4. **Task 5/4:** GenAI drafts the SMS & PDF Report based on the trigger.
    """)

# ==========================================
# 🛑 PARTICIPANT CODE GOES HERE 🛑
# ==========================================
def run_capstone_pipeline():
    """
    TODO: Import your functions from the previous tasks and chain them together!
    
    vision_result = run_vision_analysis(...)
    if vision_result['status'] == 'hazard':
        severity = run_rule_engine(vision_result['height'])
        if severity == 'Critical':
            agent_trigger(vision_result)
    """
    # --- INSTRUCTOR MODE FLAG ---
    if st.query_params.get("instructor") == "true":
        yield "👁️ Vision Model: Detected missing harness at approx 4.5m."
        time.sleep(1)
        yield "⚖️ Rule Engine: Height > 2m detected. Flagging as 'Level 1 CRITICAL'."
        time.sleep(1)
        yield "🤖 Agent: Querying SAP HR for Site Supervisor... Found: +91 98765 43210"
        time.sleep(1)
        yield "📬 Twilio API: Dispatched SMS to Supervisor."
        time.sleep(1)
        yield "📄 GenAI: Drafted HSE Near-Miss Incident Report and emailed Safety Committee."
        return
    # ---------------------------
    
    # --- COMBINE YOUR PIPELINES HERE ---
    yield "⚠️ Capstone logic not implemented yet. Please write your code."
    # -----------------------------------
    
# ==========================================

if st.button("Simulate Pipeline Cascade", type="primary", use_container_width=True):
    if not uploaded:
        st.warning("Upload an image to start the pipeline.")
    else:
        st.write("#### 🚦 Execution Trace Logs")
        container = st.container()
        
        with st.spinner("Pipeline executing..."):
            with container:
                for log_msg in run_capstone_pipeline():
                    st.code(log_msg)
        
        st.success("🎉 **Capstone Complete! Architecture validated.**")
        st.markdown("""
        ### 🔄 Closing the Loop (Task 2 HCI)
        The SMS sent in step 4 links directly back to the **'Voice-and-Vision' UI** you designed in Task 2. 
        The supervisor receives it physically on-site, speaks their explanation, taps approve, and accountability is confirmed.
        
        ### Congratulations on completing the Transrail AI Workshop!
        """)
