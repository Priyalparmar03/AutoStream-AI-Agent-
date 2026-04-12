# from langchain_community.llms import Ollama

# llm = Ollama(model="mistral")

# def detect_intent(user_input):
#     prompt = f"""
# Classify the intent strictly into one:
# - greeting
# - product_query
# - high_intent

# Input: {user_input}

# Return ONLY one word.
# """
#     response = llm.invoke(prompt).strip().lower()
#     return response

from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="mistral")

def detect_intent(user_input):
    prompt = f"""
Classify intent strictly into one:
- greeting
- product_query
- high_intent

Input: {user_input}

Return only one word.
"""
    return llm.invoke(prompt).strip().lower()