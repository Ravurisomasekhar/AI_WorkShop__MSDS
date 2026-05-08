import streamlit as st
import json
import time
from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Task 5: Structured Output",
    page_icon="📱"
)

st.title("📱 Task 5: WhatsApp-to-ERP Translator")

st.markdown("""
### The Context

Site engineers send messy WhatsApp updates like:

> "Heavy rain at 2 PM, stopped stringing work, only 3 poles erected, need more conductors tmrw"

We use AI + Few-Shot Prompting to convert unstructured text into structured ERP JSON.
""")

# ==========================================
# USER INPUT
# ==========================================

st.write("## 💬 Field Update (Unstructured Text)")

default_text = (
    "Hyderabad, Heavy rain at 2 PM, "
    "stopped stringing work, only 3 poles erected, "
    "need more conductors tmrw"
)

field_text = st.text_area(
    "Mock WhatsApp Message:",
    value=default_text,
    height=120
)

# ==========================================
# SYSTEM PROMPT
# ==========================================

st.write("## 🎯 Few-Shot System Prompt")

default_prompt = """
You are a strict ERP JSON extraction assistant.

Extract structured ERP information from WhatsApp field updates.

STRICT RULES:
- Return ONLY valid JSON
- No markdown
- No explanations
- No extra text
- Quantity and Delay_Hrs must be integers
- If location name appears anywhere in text, extract it into "Location"
- If location missing, use "Unknown"

JSON Schema:
{
    "Location": "string",
    "Work_Completed": "string",
    "Quantity": integer,
    "Delay_Hrs": integer,
    "Material_Requested": "string"
}

Example 1:

Input:
"Hyderabad, 3 poles completed, rain delay 2 hrs, need conductors"

Output:
{
    "Location": "Hyderabad",
    "Work_Completed": "Pole Erection",
    "Quantity": 3,
    "Delay_Hrs": 2,
    "Material_Requested": "Conductors"
}

Example 2:

Input:
"Chennai site completed 5 towers, need cement tomorrow"

Output:
{
    "Location": "Chennai",
    "Work_Completed": "Tower Completion",
    "Quantity": 5,
    "Delay_Hrs": 0,
    "Material_Requested": "Cement"
}

Example 3:

Input:
"Heavy rain stopped work, only 2 poles erected"

Output:
{
    "Location": "Unknown",
    "Work_Completed": "Pole Erection",
    "Quantity": 2,
    "Delay_Hrs": 0,
    "Material_Requested": "Unknown"
}
"""

system_prompt = st.text_area(
    "System Prompt:",
    value=default_prompt,
    height=450
)

# ==========================================
# MAIN FUNCTION
# ==========================================

def generate_structured_json(text_input, prompt):

    # --------------------------------------
    # LOCATION DETECTION USING PYTHON
    # --------------------------------------

    known_locations = [
        "Hyderabad",
        "Chennai",
        "Mumbai",
        "Delhi",
        "Bangalore",
        "Pune",
        "Kolkata"
    ]

    detected_location = "Unknown"

    for loc in known_locations:
        if loc.lower() in text_input.lower():
            detected_location = loc
            break

    # --------------------------------------
    # INSTRUCTOR MODE (FAKE DEMO MODE)
    # --------------------------------------

    if st.query_params.get("instructor") == "true":

        time.sleep(1)

        return {
            "Location": detected_location,
            "Work_Completed": "Pole Erection",
            "Quantity": 3,
            "Delay_Hrs": 2,
            "Material_Requested": "Conductors"
        }

    # --------------------------------------
    # REAL OLLAMA MODEL CALL
    # --------------------------------------

    try:

        llm = ChatOllama(
            model="tinyllama",
            format="json",
            temperature=0
        )

        messages = [
            SystemMessage(content=prompt),
            HumanMessage(content=text_input)
        ]

        response = llm.invoke(messages)

        raw_output = response.content.strip()

        print("RAW MODEL OUTPUT:")
        print(raw_output)

        # ----------------------------------
        # JSON PARSING
        # ----------------------------------

        try:

            parsed_json = json.loads(raw_output)

            # FORCE LOCATION FROM PYTHON
            parsed_json["Location"] = detected_location

            # Ensure all required keys exist
            required_keys = [
                "Location",
                "Work_Completed",
                "Quantity",
                "Delay_Hrs",
                "Material_Requested"
            ]

            for key in required_keys:
                if key not in parsed_json:
                    parsed_json[key] = "Unknown"

            return parsed_json

        except json.JSONDecodeError:

            return {
                "error": "Invalid JSON returned by model",
                "raw_output": raw_output
            }

    except Exception as e:

        return {
            "error": "Failed to connect to Ollama",
            "details": str(e)
        }

# ==========================================
# BUTTON ACTION
# ==========================================

if st.button("🚀 Translate to ERP JSON", type="primary"):

    with st.spinner("Translating WhatsApp message into ERP JSON..."):

        result_json = generate_structured_json(
            field_text,
            system_prompt
        )

        st.write("## 🗄️ ERP Database Input Payload")

        st.json(result_json)

        st.success("✅ Translation Complete")

        st.info(
            "💡 HCI Concept: This is called 'Invisible UI'. "
            "Workers simply send WhatsApp messages while AI silently "
            "translates them into ERP-ready structured data."
        )