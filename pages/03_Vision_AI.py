import streamlit as st
import time
import requests
import base64
from PIL import Image, ImageDraw

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
    value="You are a strict HSE safety inspector. Identify any workers in this image who are NOT wearing a safety harness. Explain clearly."
)

selected_model = st.selectbox("2. Select Vision Model:", ["llava", "gpt-4o", "yolov8-custom"])


# ==========================================
# ✅ UPDATED FUNCTION (OLLAMA INTEGRATION)
# ==========================================
def run_vision_analysis(image, prompt, model_name):

    # Instructor mode (keep as is)
    if st.query_params.get("instructor") == "true":
        time.sleep(2)
        return {
            "status": "hazard_detected",
            "human_readable": "I have detected 1 worker climbing the monopole without a secondary safety harness attached.",
            "bounding_box": [120, 45, 300, 250],
            "is_mock": True
        }

    if model_name != "llava":
        return {
            "status": "pending",
            "human_readable": f"Integration for {model_name} is currently a placeholder. Please use 'llava' for local analysis.",
            "bounding_box": [],
            "is_mock": False
        }

    try:
        # Convert image to base64
        image_bytes = image.read()
        image.seek(0)
        base64_image = base64.b64encode(image_bytes).decode("utf-8")

        # Enhanced prompt for JSON response
        json_prompt = f"""{prompt}
        IMPORTANT: Your response MUST be a valid JSON object with the following keys:
        - "status": either "hazard_detected" or "safe"
        - "explanation": a brief explanation of what you see
        - "coordinates": [ymin, xmin, ymax, xmax] if hazard is found, otherwise []
        """

        # Call Ollama local API
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": model_name,
                "prompt": json_prompt,
                "images": [base64_image],
                "stream": False,
                "format": "json"
            },
            timeout=30
        )
        response.raise_for_status()

        data = response.json()
        ai_response_text = data.get("response", "{}")
        
        import json
        try:
            result_data = json.loads(ai_response_text)
            status = result_data.get("status", "safe")
            explanation = result_data.get("explanation", "No explanation provided.")
            bbox = result_data.get("coordinates", [])
            is_mock = False
            
            # Fallback for bbox if LLM didn't provide but detected hazard
            if status == "hazard_detected" and not bbox:
                bbox = [120, 45, 300, 250]
                is_mock = True

            return {
                "status": status,
                "human_readable": explanation,
                "bounding_box": bbox,
                "is_mock": is_mock
            }
        except json.JSONDecodeError:
            return {
                "status": "hazard_detected" if "hazard" in ai_response_text.lower() else "safe",
                "human_readable": ai_response_text,
                "bounding_box": [120, 45, 300, 250],
                "is_mock": True
            }

    except requests.exceptions.ConnectionError:
        return {
            "status": "pending",
            "human_readable": "Could not connect to Ollama. Is 'ollama serve' running on localhost:11434?",
            "bounding_box": [],
            "is_mock": False
        }
    except Exception as e:
        return {
            "status": "pending",
            "human_readable": f"Error: {str(e)}",
            "bounding_box": [],
            "is_mock": False
        }


# ==========================================
# ✅ DRAW BOUNDING BOX FUNCTION
# ==========================================
def draw_box(uploaded_file, bbox):
    image = Image.open(uploaded_file)
    draw = ImageDraw.Draw(image)
    draw.rectangle(bbox, outline="red", width=3)
    return image


# ==========================================
# 🚀 MAIN BUTTON LOGIC
# ==========================================
if st.button("Run Vision AI", type="primary"):
    if uploaded_file is None:
        st.warning("Please upload an image first!")
    else:
        with st.spinner(f"AI ({selected_model}) is analyzing the image..."):
            result = run_vision_analysis(uploaded_file, system_prompt, selected_model)

            st.write("### 🚨 Analysis Results")

            col1, col2 = st.columns(2)

            with col1:
                if result["bounding_box"]:
                    boxed_image = draw_box(uploaded_file, result["bounding_box"])
                    caption = "Detected Hazard (Mock Region)" if result.get("is_mock") else "Detected Hazard"
                    st.image(boxed_image, caption=caption, use_container_width=True)
                else:
                    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

            with col2:
                if result['status'] == "hazard_detected":
                    st.error(f"**Hazard Alert:** {result['human_readable']}")
                    st.json(result)

                elif result['status'] == "pending":
                    st.warning("⚠️ " + result['human_readable'])

                else:
                    st.success("✅ Site appears safe. No compliance violations detected in the image.")