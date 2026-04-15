import streamlit as st
import time

st.set_page_config(page_title="Task 3: Vision AI", page_icon="👁️")

st.title("👁️ Task 3: Drone-Based Safety Spotter")

st.markdown("""
**The Context:** Ensuring workers wear PPE at high altitudes is a constant HSE challenge.
We will use AI vision capabilities to automate hazard detection from drone imagery.
""")

st.write("### 📸 Upload Site Image")
uploaded_file = st.file_uploader("Upload an image of a worker, tower, or site...", type=["jpg", "jpeg", "png"])

st.markdown("### 🧠 AI Call Configuration")
system_prompt = st.text_area(
    "1. Instruct the AI what to look for:", 
    value="You are a strict HSE safety inspector. Identify any workers in this image who are NOT wearing a safety harness. Draw a red bounding box around them."
)

st.selectbox("2. Select Vision Model (Mock):", ["gpt-4o", "claude-3.5-sonnet", "yolov8-custom"])

# ==========================================
# 🛑 PARTICIPANT CODE GOES HERE 🛑
# ==========================================
def run_vision_analysis(image, prompt):
    """
    TODO: Implement the API call to your Vision Model of choice.
    For the workshop, we are returning a mock response. 
    Can you figure out how to parse a real API block?
    """
    
    # --- INSTRUCTOR MODE FLAG ---
    if st.query_params.get("instructor") == "true":
        time.sleep(2)
        mock_response = {
            "status": "hazard_detected",
            "human_readable": "I have detected 1 worker climbing the monopole without a secondary safety harness attached.",
            "bounding_box": [120, 45, 300, 250] # [x_min, y_min, x_max, y_max]
        }
        return mock_response
    # ---------------------------
    
    # --- WRITE YOUR API CALL LOGIC HERE ---
    # e.g., response = openai.chat.completions.create(...)
    return {"status": "pending", "human_readable": "Code not implemented yet.", "bounding_box": []}
    # ------------------------------------------
# ==========================================


if st.button("Run Vision AI", type="primary"):
    if uploaded_file is None:
        st.warning("Please upload an image first!")
    else:
        with st.spinner("AI is analyzing the image..."):
            result = run_vision_analysis(uploaded_file, system_prompt)
            
            st.write("### 🚨 Analysis Results")
            
            col1, col2 = st.columns(2)
            with col1:
                st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
                
            with col2:
                if result['status'] == "hazard_detected":
                    st.error(f"**Hazard Alert:** {result['human_readable']}")
                    
                    st.info("💡 **HCI Challenge:** Instead of showing coordinates, how would you use Python (e.g. OpenCV or Pillow) to actually draw the box `[120, 45, 300, 250]` on the image here?")
                    st.json(result)
                elif result['status'] == "pending":
                    st.warning("⚠️ " + result['human_readable'])
                else:
                    st.success("✅ Site appears safe. No compliance violations detected in the image.")
