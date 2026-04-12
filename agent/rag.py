# import json

# def load_knowledge():
#     with open("data/knowledge.json") as f:
#         return json.load(f)

# def answer_query(query):
#     data = load_knowledge()

#     query = query.lower()

#     if "price" in query or "pricing" in query:
#         return f"""
# Basic Plan: {data['pricing']['basic']['price']}
# Pro Plan: {data['pricing']['pro']['price']}
# """

#     elif "pro" in query:
#         return f"""
# Pro Plan:
# Price: {data['pricing']['pro']['price']}
# Features: {", ".join(data['pricing']['pro']['features'])}
# """

#     elif "basic" in query:
#         return f"""
# Basic Plan:
# Price: {data['pricing']['basic']['price']}
# Features: {", ".join(data['pricing']['basic']['features'])}
# """

#     elif "refund" in query:
#         return data["policies"]["refund"]

#     elif "support" in query:
#         return data["policies"]["support"]

#     return "I can help with pricing, plans, and features!"


# from sentence_transformers import SentenceTransformer
# import faiss
# import json
# import numpy as np

# # Load model
# model = SentenceTransformer('all-MiniLM-L6-v2')

# # Load data
# with open("data/knowledge.json") as f:
#     data = json.load(f)

# # Convert JSON into text chunks
# documents = []

# def flatten_json(data):
#     for key, value in data.items():
#         if isinstance(value, dict):
#             flatten_json(value)
#         elif isinstance(value, list):
#             for item in value:
#                 documents.append(str(item))
#         else:
#             documents.append(str(value))

# flatten_json(data)

# # Create embeddings
# embeddings = model.encode(documents)

# # Store in FAISS
# dimension = embeddings.shape[1]
# index = faiss.IndexFlatL2(dimension)
# index.add(np.array(embeddings))

# def answer_query(query):
#     query_embedding = model.encode([query])
#     D, I = index.search(np.array(query_embedding), k=2)

#     results = [documents[i] for i in I[0]]
#     return " ".join(results)


# import json

# def load_knowledge():
#     with open("data/knowledge.json") as f:
#         return json.load(f)

# def answer_query(query):
#     data = load_knowledge()
#     query = query.lower()

#     if "price" in query or "pricing" in query:
#         return f"Basic: {data['pricing']['basic']['price']}, Pro: {data['pricing']['pro']['price']}"

#     return "I can help with pricing and features!"

import json

def load_knowledge():
    with open("data/knowledge.json") as f:
        return json.load(f)

def answer_query(query):
    data = load_knowledge()
    query = query.lower()

    # Pricing response
    if "price" in query or "pricing" in query:
        basic = data['pricing']['basic']['price']
        pro = data['pricing']['pro']['price']

        return (
            "💰 Here's our pricing breakdown:\n\n"
            f"🔹 Basic Plan: {basic}\n"
            f"🔹 Pro Plan: {pro}\n\n"
            "✨ The Pro plan is best if you want advanced growth and automation features.\n"
            "Would you like help choosing the right plan?"
        )

    # Features response
    elif "feature" in query:
        return (
            "🚀 Our platform helps you grow faster with:\n\n"
            "✔️ AI-powered content strategy\n"
            "✔️ Lead generation tools\n"
            "✔️ Automated engagement\n\n"
            "Let me know if you want details on any specific feature!"
        )

    # Default response
    return (
        "🤖 I can help you with:\n\n"
        "💰 Pricing plans\n"
        "🚀 Features & benefits\n"
        "📈 Growth strategies\n\n"
        "What would you like to explore?"
    )