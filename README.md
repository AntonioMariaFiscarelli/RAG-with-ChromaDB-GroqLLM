
# 🧠 RAG with ChromaDB + Groq LLM

This project implements a lightweight Retrieval-Augmented Generation (RAG) pipeline using [LangChain](https://www.langchain.com/), [ChromaDB](https://www.trychroma.com/), and [Groq](https://console.groq.com/) LLMs. It enables fast, context-aware question answering over custom document collections using blazing-fast inference from Groq-hosted models.



## 🚀 Features

- 🔍 Document ingestion and embedding with `sentence-transformers`
- 🧠 Vector search using ChromaDB
- 🤖 Response generation via Groq LLMs
- 🧩 Modular LangChain integration
- 📦 Clean Python packaging with `pyproject.toml`



## ⚙️ Setup

### 1. Clone the repo
git clone https://github.com/AntonioMariaFiscarelli/RAG-with-ChromaDB-GroqLLM.git
cd RAG-with-ChromaDB-GroqLLM

### 2.  Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

### 3.  Install dependencies
pip install -e .

### 4. Set your Groq API key
GROQ_API_KEY=your_actual_key_here


🧠 Supported Models
Groq supports the following models:
    llama3-8b-8192
    mixtral-8x7b
    gemma-7b-it

Make sure your API key has access to these models.


📜 License
This project is licensed under the MIT License.

🙋‍♂️ Author
Created by Antonio Fiscarelli

