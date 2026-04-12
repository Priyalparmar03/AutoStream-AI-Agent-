# 🤖 AutoStream AI Agent

An AI-powered conversational agent designed to assist creators and businesses with **pricing insights, feature exploration, and lead generation** using a simple RAG-based architecture.

---

## 🚀 Features

* 🧠 Intent Detection (Greeting, Product Query, High Intent)
* 💬 Conversational AI Interface (Streamlit UI)
* 📊 Knowledge-Based Responses (JSON-powered RAG)
* 🎯 Lead Capture System (Name, Email, Platform)
* ⚡ Modular Agent Architecture

---

## 🏗️ Project Architecture

```
User Input → Intent Detection → RAG / Response → Lead Capture → Output
```

---

## 📂 Project Structure

```
AutoStream-AI-Agent/
│
├── agent/
│   ├── intent.py        # Detects user intent
│   ├── rag.py           # Handles knowledge-based responses
│   ├── tools.py         # Lead capture logic
│   ├── state.py         # Manages session state
│
├── data/
│   └── knowledge.json   # Pricing & feature data
│
├── app.py               # Streamlit UI
├── requirements.txt
├── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com//Priyalparmar03/AutoStream-AI-Agent.git
cd AutoStream-AI-Agent
```

---

### 2. Create virtual environment

```bash
conda create -n ai_agent python=3.10 -y
conda activate ai_agent
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run the application

```bash
streamlit run app.py
```

---

## 💡 Example Use Cases

* 💰 Ask about pricing plans
* 🚀 Explore product features
* 🎯 Capture leads for marketing
* 🤖 Simulate AI-powered business assistant

---

## 🧠 Technologies Used

* Python
* Streamlit
* Transformers (Hugging Face)
* Sentence Transformers
* JSON-based RAG

---

## 🔥 Future Improvements

* 🔍 Semantic Search with Embeddings
* 🧠 LLM Integration (OpenAI / Local Models)
* 💾 Conversation Memory
* 🌐 Deployment (Streamlit Cloud / AWS)

---

## 📌 Author

**Priyal Parmar**
parmarpriyal1603@gmail.com
