# Transrail AI Workshop: Learning by Doing Participant Guide

Welcome to the **Transrail AI Workshop**. This guide provides a step-by-step approach to building, testing, and understanding practical AI applications tailored to the heavy engineering and infrastructure context. 

For each task, follow the **Learn**, **Do**, **Test**, and **Discover** phases to build your intuition and technical skills.

---

## Phase 1: Foundational AI (Logic & Pattern Recognition)
**Learning Objective:** Understand the core difference between deterministic AI (100% rule-based predictability) and probabilistic AI (predictive machine learning).

### Task 1: Rule-Based AI — "Tower BOQ & Design Compliance Engine"

**The Transrail Context:** Designing high-voltage transmission lattice towers or high-mast lighting poles requires strict adherence to Indian Standards (IS), IEC, or client codes. A single error in the Bill of Quantities (BOQ) can halt manufacturing.

1. **Learn:** Discover that not every problem needs a neural network. For strict engineering safety, rule-based logic is 100% deterministic, auditable, and hallucination-free.
2. **Do:** 
   - Create a dummy `mock_boq.csv` file representing a 400kV transmission tower (columns like `Tower Type`, `Wind Zone`, `Height`, `Steel Grade`, `Flange Thickness`).
   - Write a Python script (`compliance_engine.py`) acting as an "Expert System."
   - Program hard-coded `IF/THEN` business rules. For example: `if wind_zone == 4 and height > 40: if steel_grade != "High-Tensile" or thickness < 25: return "Fail"`
3. **Test:** 
   - Run the script with passing data to verify success.
   - Run the script with failing data. The script **must** output a clear Pass/Fail compliance metric.
4. **Discover (HCI Application):** Ensure your output explicitly lists the *exact* IS/IEC standard violated. This builds immediate trust for a design engineer, rather than an opaque "Computer says no." Deterministic systems are predictable.

### Task 2: AI Visioning & HCI — "The ‘Gloves-On’ Field Co-Pilot"

**The Transrail Context:** Site supervisors log daily progress, ROW delays, and hazards on rugged tablets. They are tired, hands are dirty, and ERP forms are complex.

1. **Learn:** Designing for AI (which makes probabilistic guesses) is fundamentally different from traditional software. You must master Human-in-the-Loop (HITL) and design for trust.
2. **Do (Design Sprint):** Do not write code. Use a rapid prototyping tool (Figma, v0.dev, or Voiceflow).
   - **Context Mapping & Zero-Typing:** Design a "Voice-and-Vision-first" UI. Include one massive button to speak ("Locals stopped work..."), a camera button, and disable the keyboard.
   - **Conversational Repair:** Design a flow for when the AI mishears technical jargon (e.g., misinterpreting "HTLS conductor"). How does the user fix it without typing?
   - **HITL Friction:** Before submitting to Transrail’s SAP/ERP, present an "Explainability Card" showing the AI's translation, alongside a massive "Approve" button.
3. **Test:** Role-play! Present the prototype to a teammate. Ask them to "log a delay" and correct a jargon mistake without getting frustrated.
4. **Discover:** The vital HCI principles of AI interfaces: **Graceful Degradation** (what happens when AI fails), **Verifiability** (showing the AI's work), and **Agency** (keeping the human in control).

---

## Phase 2: Perceptive & Generative AI (Vision & Unstructured Data)
**Learning Objective:** Master how AI processes messy, unstructured data—like drone images, chaotic field texts, and massive tender PDFs.

### Task 3: Multimodal / Vision AI — "Drone-Based Quality & Safety Spotter"

**The Transrail Context:** Inspecting miles of OHE or transmission lines for defects is slow. Enforcing PPE usage at high altitudes is a constant HSE challenge.

1. **Learn:** Grasp how modern AI "sees" the physical world, bridging the gap between site reality and automated quality assurance.
2. **Do:**
   - Write a Python script (`vision_spotter.py`) using a vision-capable API (like GPT-4o Vision, Claude 3.5 Sonnet) or YOLOv8.
   - Upload images of electrical towers or construction sites.
   - Prompt the AI: *"Identify rusted porcelain insulators"* or *"Draw a bounding box around any worker climbing a monopole without a safety harness."*
3. **Test:** Submit images of safe vs. unsafe conditions. Ensure the AI accurately flags the hazards and ignores compliance.
4. **Discover (HCI Application):** Do not just print text. Prove that returning an image with a visual bounding box drawn directly over the rusted insulator provides an infinitely better user experience than a spreadsheet of coordinates.

### Task 4: Generative AI (RAG) — "The 1,000-Page PGCIL Tender Interrogator"

**The Transrail Context:** Bidding for PGCIL or international EPC tenders requires digesting hundreds of pages of complex legal constraints.

1. **Learn:** Master Retrieval-Augmented Generation (RAG). Learn to strictly "ground" LLMs in proprietary corporate documents, eliminating hallucinations entirely.
2. **Do:**
   - Build a RAG pipeline (`tender_rag.py`) using LangChain, an LLM, and a vector database (e.g., ChromaDB).
   - Chunk and embed a dummy 20-50 page PDF tender document.
   - Create a basic chat interface.
3. **Test:** Ask your script: *"What are the exact Liquidated Damages (LD) clauses for project delays, and what are the payment milestones?"* Read the answer.
4. **Discover (HCI Application):** Force your script to output clickable citation links (e.g., "Source: pg. 42"). A bidding manager cannot legally rely on AI; they *must* be able to click through to the original PDF to verify the answer instantly.

### Task 5: Generative AI (Structuring) — "WhatsApp-to-ERP Daily Progress Translator"

**The Transrail Context:** Remote site operations send fragmented WhatsApp updates like: *"Heavy rain at 2 PM, stopped stringing work, only 3 poles erected, need more conductors tmrw"*.

1. **Learn:** Master "few-shot prompting" to force LLMs to generate highly structured outputs, bridging messy field operations to rigid corporate databases.
2. **Do:**
   - Define a JSON schema matching Transrail's SAP/ERP fields (`Location`, `Work_Completed`, `Quantity`, `Delay_Hrs`, `Material_Requested`).
   - Write a script (`whatsapp_parser.py`) using an LLM API.
   - Use advanced system prompts providing examples (Few-Shot) to instruct the LLM to output *only* syntactically valid JSON based on the text.
3. **Test:** Input chaotic WhatsApp strings and ensure the output is exclusively a perfectly formatted JSON object that a database can ingest directly.
4. **Discover (HCI Application):** Discover the "Invisible UI." The best interface is WhatsApp—because the user already uses it. GenAI acts as a silent backend translator, completely eliminating ERP training friction for field staff.

---

## Phase 3: Agentic AI (Autonomy & Action)
**Learning Objective:** Move from AI that "answers" to AI that "acts" by equipping models with digital tools and decision-making autonomy.

### Task 6: Single-Agent AI (Tool Calling) — "The Autonomous Supply Chain Expeditor"

**The Transrail Context:** If HTLS conductors are delayed, manual expediting is tedious. Agentic AI can execute the follow-up automatically.

1. **Learn:** The "ReAct" (Reason + Act) framework—giving LLMs agency to execute API workflows across external systems.
2. **Do:**
   - Write a Python script (`supply_agent.py`) using LangGraph or the OpenAI Assistants API.
   - Give the AI three dummy "Tools" (Python functions): `query_inventory_db()`, `check_weather_api()`, and `draft_email()`.
   - Prompt the AI: *"Supplier A's steel is delayed. Check inventory. If short, check the weather route and draft a status email to the Project Manager."*
3. **Test:** Run the agent. Watch the logs as it autonomously decides *which* tool to invoke, in what order, based on the results of the previous tool.
4. **Discover (HCI Application):** Supervisory Control. An autonomous agent firing off emails unchecked is dangerous. Design the flow so that the agent pauses and asks for a human manager's manual approval before triggering the `draft_email()` action.

### Task 7: Multi-Agent AI (Swarms) — "The Mock EPC Bid Syndicate"

**The Transrail Context:** A winning substation bid requires a syndicate of cross-functional logic: engineering scope, procurement costs, and commercial risk.

1. **Learn:** The absolute frontier of AI. Orchestrating "swarms" of specialized AI models to collaborate, debate, and solve multi-variable business problems.
2. **Do:**
   - Use a multi-agent framework (CrewAI or MS AutoGen) in a script (`bid_swarm.py`).
   - Spin up three personas:
     - **Agent 1 (Technical Lead):** Extracts material quantities from the SOW.
     - **Agent 2 (Procurement Head):** Prices quantities using a dummy DB and flags supply chain risks.
     - **Agent 3 (Commercial Director):** Takes outputs from A1 and A2, adds a 15% margin, applies risk buffers, and drafts the final bid letter.
3. **Test:** Give Agent 1 a mock Scope of Work. Sit back and watch the swarm converse, hand off tasks, and generate the final holistic document.
4. **Discover (HCI Application):** The Observability Dashboard. How can a human trust three AIs talking to each other? You need an interface that lets humans monitor the real-time conversation and logic of the swarm so they can intercept poor reasoning mid-flight.

---

## Phase 4: The Capstone
**Learning Objective:** Combine Rules, Generative AI, and Autonomous Agents into a single, cohesive, production-grade architecture.

### Task 8: Hybrid AI Architecture — "End-to-End Smart Safety Watchdog"

**The Transrail Context:** Managing safety across dozens of concurrent, high-risk global sites requires a symphony of systems.

1. **Learn:** Real-world enterprise AI is almost never "one model." It is a multi-layered pipeline of sight, logic, language, and action.
2. **Do:** Build a master orchestrator script (`smart_safety.py`):
   - **Vision AI:** Pass an image of a worker without a harness to detect the anomaly.
   - **Rule-Based AI:** Pass the AI's detection to a rigid Python `IF` statement. If `height > 2m`, strictly categorise it as "Level 1 Critical".
   - **Agentic AI:** An agent receives the Critical flag, queries a dummy HR database to find the supervisor's phone number, and acts by calling a Twilio SMS API to fire an alert.
   - **Generative AI:** The agent uses an LLM to dynamically draft a formal "Near-Miss PDF Report" and emails it to the safety committee.
3. **Test:** Feed safe images (nothing happens). Feed an unsafe image and watch the full cascade execute from physical anomaly to corporate email alert.
4. **Discover (HCI Application):** This orchestrator routes the SMS alert directly back to the very tablet UI we designed in **Task 1**. The supervisor—standing on the site—receives the alert dynamically, clicks "Review & Approve," and closes the loop on human accountability. 

*(End of Workshop Guide)*
