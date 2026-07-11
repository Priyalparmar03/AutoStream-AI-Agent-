from langgraph.graph import StateGraph
from agent.intent import detect_intent
from agent.rag import answer_query
from agent.tools import mock_lead_capture
from agent.state import AgentState

# Nodes
def handle_input(state):
    state.intent = detect_intent(state.user_input)
    return state

def handle_query(state):
    state.response = answer_query(state.user_input)
    return state

def handle_lead(state):
    if not state.name:
        state.response = "What is your name?"
    elif not state.email:
        state.response = "Your email?"
    elif not state.platform:
        state.response = "Which platform?"
    else:
        mock_lead_capture(state.name, state.email, state.platform)
        state.response = "Lead captured successfully!"
    return state


# Graph
builder = StateGraph(AgentState)

builder.add_node("intent", handle_input)
builder.add_node("query", handle_query)
builder.add_node("lead", handle_lead)

# Flow logic
builder.set_entry_point("intent")

builder.add_conditional_edges(
    "intent",
    lambda state: state.intent,
    {
        "greeting": "query",
        "product_query": "query",
        "high_intent": "lead"
    }
)

builder.set_finish_point("query")

graph = builder.compile()
