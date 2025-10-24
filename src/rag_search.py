import os
from dotenv import load_dotenv
from src.llm import GroqLLM

load_dotenv()

class RAGSearch:
    def __init__(self, retriever, llm,  model_name="llama-3.1-8b-instant", temperature=0.1, max_tokens=1024):
        self.retriever = retriever
        self.llm = llm

    def generate_answer(self, query: str, top_k: int = 3) -> str:
        results = self.retriever.retrieve(query, top_k=top_k)
        context = "\n\n".join([doc['content'] for doc in results]) if results else ""

        if not context:
            return "No relevant context found to answer the question."

        return self.llm.generate_response(query= "What is attention mechanism?", context="") 
