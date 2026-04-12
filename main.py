# import sys
# from agent.intent import detect_intent
# from agent.rag import answer_query
# from agent.tools import mock_lead_capture
# from agent.state import AgentState

# print("🚀 AGENT STARTED... (Type 'exit' to stop)\n")

# state = AgentState()

# while True:
#     try:
#         # Force input prompt to show properly
#         print("User: ", end="", flush=True)
#         user_input = sys.stdin.readline().strip()

#         if not user_input:
#             continue

#         if user_input.lower() == "exit":
#             print("Agent: Goodbye! 👋")
#             break

#         # Detect intent
#         intent = detect_intent(user_input)
#         state.intent = intent

#         print(f"(Debug) Detected intent: {intent}")  # Optional debug

#         # Greeting
#         if intent == "greeting":
#             print("Agent: Hello! How can I help you today? 😊")

#         # Product Query → RAG
#         elif intent == "product_query":
#             answer = answer_query(user_input)
#             print("Agent:", answer)

#         # High Intent → Collect details step-by-step
#         elif intent == "high_intent":

#             # Ask Name
#             if not state.name:
#                 print("Agent: Great! Let's get you started 🚀")
#                 print("Agent: What's your name? ", end="", flush=True)
#                 state.name = sys.stdin.readline().strip()
#                 continue

#             # Ask Email
#             if not state.email:
#                 print("Agent: Please enter your email: ", end="", flush=True)
#                 state.email = sys.stdin.readline().strip()
#                 continue

#             # Ask Platform
#             if not state.platform:
#                 print("Agent: Which platform do you create content on? ", end="", flush=True)
#                 state.platform = sys.stdin.readline().strip()
#                 continue

#             # Call tool only after all info collected
#             mock_lead_capture(state.name, state.email, state.platform)
#             print("Agent: ✅ Thanks! Our team will contact you soon.\n")

#             # Reset state for next user (optional but good)
#             state = AgentState()

#         else:
#             print("Agent: 🤔 Can you please clarify your request?")

#     except KeyboardInterrupt:
#         print("\nAgent: Stopped manually.")
#         break

#     except Exception as e:
#         print(f"⚠️ Error: {e}")

import streamlit as st
from agent.intent import detect_intent
from agent.rag import answer_query
from agent.tools import mock_lead_capture
from agent.state import AgentState

# Initialize state
if "state" not in st.session_state:
    st.session_state.state = AgentState()

state = st.session_state.state

st.title("🤖 AutoStream AI Agent")

user_input = st.text_input("Type your message:")

if user_input:

    intent = detect_intent(user_input)
    state.intent = intent

    st.write(f"🧠 Detected Intent: {intent}")

    # Greeting
    if intent == "greeting":
        st.write("👋 Hello! How can I help you today?")

    # Product Query
    elif intent == "product_query":
        answer = answer_query(user_input)
        st.write(answer)

    # High Intent
    elif intent == "high_intent":

        if not state.name:
            state.name = st.text_input("Enter your name:")
        
        elif not state.email:
            state.email = st.text_input("Enter your email:")
        
        elif not state.platform:
            state.platform = st.text_input("Which platform do you use?")
        
        else:
            mock_lead_capture(state.name, state.email, state.platform)
            st.success("🎯 Lead captured successfully!")
            st.session_state.state = AgentState()

    else:
        st.write("🤔 Please clarify your request.")