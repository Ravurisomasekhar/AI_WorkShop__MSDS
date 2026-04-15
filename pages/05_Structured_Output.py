import streamlit as st
import json
import time

st.set_page_config(page_title="Task 5: Structured Output", page_icon="📱")

st.title("📱 Task 5: WhatsApp-to-ERP Translator")

st.markdown("""
**The Context:** Site engineers send messy, fragmented updates via WhatsApp. 
We need to use 'Few-Shot Prompting' to force the LLM to output a strictly formatted JSON object that matches Transrail’s SAP/ERP schema.
""")

st.write("### 💬 Field Update (Unstructured Text)")

default_text = "Heavy rain at 2 PM, stopped stringing work, only 3 poles erected, need more conductors tmrw"
field_text = st.text_area("Mock WhatsApp Message:", value=default_text)

st.write("### 🎯 System Prompt Configuration")
st.markdown("Use this box to write your 'Few-Shot' prompt. Tell the AI exactly what JSON keys you expect.")

system_prompt = st.text_area(
    "System Prompt (Provide Examples Here):",
    height=200,
    value='''You are an ERP data extraction assistant. Extract data from the text and return ONLY valid JSON matching this schema:
{
    "Location": "string (or Unknown)",
    "Work_Completed": "string",
    "Quantity": integer,
    "Delay_Hrs": integer,
    "Material_Requested": "string"
}'''
)

# ==========================================
# 🛑 PARTICIPANT CODE GOES HERE 🛑
# ==========================================
def generate_structured_json(text_input, prompt):
    """
    TODO: Implement the LLM API call with JSON mode enabled.
    """
    
    # --- INSTRUCTOR MODE FLAG ---
    if st.query_params.get("instructor") == "true":
        time.sleep(1)
        mock_json = {
            "Location": "Unknown",
            "Work_Completed": "Pole Erection",
            "Quantity": 3,
            "Delay_Hrs": 2, # Guessed based on 'stopped at 2 PM'
            "Material_Requested": "Conductors"
        }
        return mock_json
    # ---------------------------
    
    # --- WRITE YOUR LLM CALL HERE ---
    # e.g., response = openai.chat.completions.create(
    #           response_format={ "type": "json_object" }
    #       )
    return {"status": "pending", "message": "Code not implemented yet"}
    # --------------------------------

# ==========================================

if st.button("Translate to ERP JSON", type="primary"):
    with st.spinner("Translating unstructured text to JSON..."):
        result_json = generate_structured_json(field_text, system_prompt)
        
        st.write("### 🗄️ ERP Database Input Payload")
        st.json(result_json)
        
        st.info("💡 **HCI Learning:** This is the 'Invisible UI'. The user just sends a WhatsApp message. GenAI handles the translation in the background, eliminating ERP training friction completely.")
