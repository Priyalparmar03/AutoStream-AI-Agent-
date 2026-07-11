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
