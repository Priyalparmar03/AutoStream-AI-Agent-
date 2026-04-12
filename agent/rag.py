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
