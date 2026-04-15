import streamlit as st
import time

st.set_page_config(page_title="Task 7: Agent Swarm", page_icon="👥")

st.title("👥 Task 7: The Mock EPC Bid Syndicate")

st.markdown("""
**The Context:** Putting together a winning substation bid requires a syndicate of cross-functional logic.
We will use **CrewAI** to orchestrate specialized AI personas that collaborate and pass data to each other.
""")

st.write("### 📜 Bid Scope of Work (SOW)")
sow_text = st.text_area("Client Requirements:", value="Design and supply a 400kV gas-insulated substation (GIS) extension. Include 2 bays, 300km of HTLS conductor, and all associated civil works. Delivery strictly in 18 months in a high-wind coastal zone.")

st.write("### 🤖 Agent Personas Config")

with st.expander("Define the Technical Lead Agent", expanded=False):
    st.text_area("Role:", "Technical Lead Engineer")
    st.text_area("Goal:", "Extract material quantities and technical risks from the client SOW.")
    st.text_area("Backstory:", "You are a veteran Transrail engineer who spots technical flaws in tenders.")

with st.expander("Define the Procurement Agent", expanded=False):
    st.text_area("Role:", "Global Sourcing Head")
    st.text_area("Goal:", "Price the extracted materials and flag supply chain risks.")
    st.text_area("Backstory:", "You have deep knowledge of global steel prices and shipping logistics.")

with st.expander("Define the Commercial Director", expanded=False):
    st.text_area("Role:", "Commercial Bid Director")
    st.text_area("Goal:", "Take technical & procurement inputs, add 15% margin, and generate final Bid Letter.")
    st.text_area("Backstory:", "You are responsible for ensuring Transrail wins the bid while remaining profitable.")

# ==========================================
# 🛑 PARTICIPANT CODE GOES HERE 🛑
# ==========================================
def run_crew(sow):
    """
    TODO: Build the CrewAI pipeline.
    1. Define the 3 Agents using the config above.
    2. Define 3 Tasks (one assigned to each agent).
    3. Create a Crew (Process=Sequential).
    4. Kickoff the crew!
    """
    # --- INSTRUCTOR MODE FLAG ---
    if st.query_params.get("instructor") == "true":
        steps = [
            {"agent": "🛠️ Technical Lead", "action": "Analyzing SOW. Extracted: 2 GIS Bays, 300km HTLS. Flag: High wind coastal zone requires specialized anti-corrosion coating."},
            {"agent": "🚢 Procurement Head", "action": "Pricing materials. Base GIS: $4M. HTLS: $1.2M. Due to coastal flag, adding $300k for anti-corrosion coating. Total Cost: $5.5M."},
            {"agent": "💼 Commercial Director", "action": "Reviewing $5.5M cost. Adding 15% margin ($825k) and 5% coastal risk buffer ($275k). Final Bid Price: $6.6M. Drafting letter..."}
        ]
        return steps
    # ---------------------------
    
    # --- WRITE YOUR CREWAI LOGIC HERE ---
    # e.g., tech_agent = Agent(role=..., goal=..., backstory=...)
    #       task1 = Task(description=..., agent=tech_agent)
    #       crew = Crew(agents=[...], tasks=[...])
    #       result = crew.kickoff()
    return [{"agent": "🤖 System", "action": "⚠️ CrewAI logic not implemented yet. Please write your code."}]
    # ------------------------------------
# ==========================================

if st.button("Start the Swarm (Kickoff)", type="primary"):
    st.write("### 📡 Swarm Observability Dashboard")
    st.info("Watch the agents talk to each other and pass context sequentially.")
    
    steps = run_crew(sow_text)
    
    for step in steps:
        time.sleep(2) # Fake processing time
        with st.chat_message("ai", avatar=step["agent"][0]):
            st.markdown(f"**{step['agent']}**")
            st.write(step["action"])
    
    time.sleep(1)
    st.success("✅ **Final Commercial Bid Letter Generated ($6.6M)**")
    st.download_button("Download Bid_Letter.md", data="Mock Bid Letter Data", file_name="bid.md")

