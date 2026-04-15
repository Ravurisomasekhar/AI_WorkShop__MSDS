import streamlit as st

st.set_page_config(page_title="Task 2: HCI Design", page_icon="🎨")

st.title("🎨 Task 2: The 'Gloves-On' Field Co-Pilot")

st.markdown("""
**The Context:** Site supervisors log delays and hazards on rugged tablets. They are tired, hands are dirty, and ERP forms are complex.

Unlike traditional software, AI is probabilistic. This means you must design interfaces that handle *uncertainty* gracefully.

### 🎯 Your Mission (Design Sprint)
We are going to write **zero code** for this task. 
Instead, we will use [v0.dev by Vercel](https://v0.dev) to generate a high-fidelity React interface in seconds.

---

### Step 1: Open v0.dev
Navigate to [v0.dev](https://v0.dev) in a new browser tab and create a free account if you haven't already.

### Step 2: The Magic Prompt
Copy the prompt below and paste it into v0.dev. 

> *Feel free to modify this prompt to add your own creative flair!*
""")

prompt = """Create a rugged tablet UI for a high-voltage transmission line construction worker. 
The interface must be 'Voice-and-Vision-first'. 
1. The keyboard should be disabled/hidden. 
2. Show one massive 'Tap to Speak' microphone button in the center (make it highly visible, maybe orange or yellow).
3. Include a large 'Snap Photo' camera button.
4. Show an 'Explainability Card' that displays what the AI transcribed so far (e.g., "AI heard: Locals stopped work at tower 45. Delay: 3 hours.").
5. Include a massive green 'Approve & Sync to ERP' button at the bottom.
6. Make it look modern, dark mode, with a heavy-duty industrial aesthetic suitable for a construction site.
"""

st.code(prompt, language="text")

st.markdown("""
### Step 3: Iterate and Experience
1. Watch v0 generate the UI right before your eyes.
2. What happens if the AI mishears "HTLS conductor" as "Hoteless conductor"? How does the user fix it without a keyboard?
3. **Ask v0 to update the design:** *"Add a quick-select dropdown next to the transcription showing to common Transrail jargon so the user can tap to correct mistakes easily."*

### 🧠 The HCI Learning
By making the "Approve" button massive and showing the AI's transcription *before* saving to the database, you have maintained **Human-in-the-Loop (HITL)** agency and built trust.
""")
