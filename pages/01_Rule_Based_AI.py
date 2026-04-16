import streamlit as st
import pandas as pd
import time

st.set_page_config(page_title="Task 1: Rule-Based AI", page_icon="🏗️")

st.title("🏗️ Task 1: Tower Design Compliance Engine")
st.markdown("""
**The Context:** A single error in the Bill of Quantities (BOQ) can halt manufacturing. 
Your goal is to write a deterministic, 100% rule-based engine to validate the BOQ.
""")

# Load Data
try:
    df = pd.read_csv("data/mock_boq.csv")
    st.write("### 📄 Input BOQ Data")
    st.dataframe(df, use_container_width=True)
except FileNotFoundError:
    st.error("mock_boq.csv not found. Please ensure it is in the data/ directory.")
    st.stop()

st.markdown("### 🧪 Engineering Validation logic")

with st.expander("Show Business Rules", expanded=True):
    st.info("""
    **Rules to implement:**
    If `Wind Zone` == 4 and `Height` > 40:
    - `Steel Grade` MUST be "High-Tensile"
    - `Flange Thickness` MUST be >= 25
    """)

# ==========================================
# 🛑 PARTICIPANT CODE GOES HERE 🛑
# ==========================================
def validate_tower(row):
    """
    TODO: Implement the business logic below.
    Return a tuple: (Status, Reason)
    Example: ("Pass", "Compliant") or ("Fail", "Failed IS:802 Flange Thickness Rule")
    """
    wind_zone = row['Wind Zone']
    height = row['Height']
    steel_grade = row['Steel Grade']
    thickness = row['Flange Thickness']
    
    # --- INSTRUCTOR MODE FLAG ---
    # To view the answer, append ?instructor=true to the URL
    if st.query_params.get("instructor") == "true":
        # The Solution
        if wind_zone == 4 and height > 40:
            if steel_grade != "High-Tensile":
                return "Fail", "Steel Grade must be High-Tensile"
            if thickness < 25:
                return "Fail", f"Flange too thin ({thickness}mm). Must be >= 25mm"
                
        return "Pass", "Compliant with IS Standards"
    # ---------------------------
    
    # --- WRITE YOUR IF/THEN STATEMENTS HERE ---
    # status = "Pending"
    # reason = "Code not implemented yet"
    # ------------------------------------------

    # --- WRITE YOUR IF/THEN STATEMENTS HERE ---

    errors = []

    # --- Clean & normalize data ---
    wind_zone = int(wind_zone)
    height = float(height)
    thickness = float(thickness)
    steel_grade = str(steel_grade).strip().lower()

    # --- Rule check ---
    if wind_zone >= 4 and height > 40:
        
        # Rule 1: Steel must be High-Tensile
        if steel_grade != "high-tensile":
            errors.append("Violation of IS 802: Steel Grade must be High-Tensile")
        
        # Rule 2: Thickness must be >= 25mm
        if thickness < 25:
            errors.append(f"Violation of IS 802: Flange Thickness {thickness}mm is less than 25mm")

    # --- Final decision ---
    if len(errors) > 0:
        return "Fail", " | ".join(errors)

    return "Pass", "Compliant with IS 802"

# ==========================================

if st.button("Run Compliance Check", type="primary"):
    with st.spinner("Running deterministic rules..."):
        time.sleep(0.5) # Fake loading for effect
        
        results = []
        for index, row in df.iterrows():
            status, reason = validate_tower(row)
            results.append({"Row": index + 1, "Status": status, "Reason": reason})
        
        results_df = pd.DataFrame(results)
        
        # Display Results with Wow Factor (Colors)
        st.write("### 📊 Compliance Report")
        def color_status(val):
            color = 'green' if val == 'Pass' else 'red'
            return f'color: {color}; font-weight: bold;'
            
        st.dataframe(results_df.style.applymap(color_status, subset=['Status']), use_container_width=True)
        
        if "Fail" in results_df['Status'].values:
            st.error("❌ Warning: Non-compliant materials detected. Halt manufacturing.")
        elif "Pending" in results_df['Status'].values:
            st.warning("⚠️ Logic not fully implemented. Please write your rules above.")
        else:
            st.success("✅ All towers compliant. Ready for manufacturing.")
